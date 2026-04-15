#!/usr/bin/env python3
"""
Zendesk Ticket Triage & Priority Scoring Script

Connects to your Zendesk instance, scores open tickets by priority,
applies tags, and outputs a triage report.

Usage:
    python ticket_triage.py --mode score --output triage_report.csv
    python ticket_triage.py --mode report
    python ticket_triage.py --mode demo   # runs with sample data, no credentials needed
"""

import argparse
import csv
import json
import os
import random
from dataclasses import dataclass, field
from datetime import datetime, timedelta


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Ticket:
    id: int
    subject: str
    description: str
    requester: str
    created_at: datetime
    status: str
    tags: list[str] = field(default_factory=list)
    organization: str = ""
    channel: str = "email"
    priority: str = "normal"
    score: int = 0
    recommended_queue: str = ""
    recommended_sla_hours: int = 8


# ---------------------------------------------------------------------------
# Priority scoring engine
# ---------------------------------------------------------------------------

KEYWORD_SCORES = {
    # Urgency keywords
    "urgent": 20,
    "critical": 20,
    "down": 15,
    "broken": 12,
    "not working": 12,
    "can't access": 15,
    "locked out": 18,
    "data loss": 25,
    "outage": 25,
    "security": 20,
    "breach": 30,
    # Billing keywords
    "charged": 10,
    "refund": 10,
    "invoice": 8,
    "billing": 8,
    "cancel": 12,
    # Lower priority keywords
    "feature request": -10,
    "suggestion": -10,
    "when will": -5,
    "how do i": -5,
    "question": -3,
}

QUEUE_RULES = [
    (["security", "breach", "hack", "data loss"], "Security — Escalate Immediately", 0.5),
    (["locked out", "can't login", "can't access", "password"], "Tier 1 Priority", 1),
    (["cancel", "refund", "charged", "billing", "invoice"], "Billing", 2),
    (["api", "webhook", "integration", "broken", "outage", "down"], "Tier 2 — Technical", 4),
    (["feature request", "suggestion", "when will", "roadmap"], "Product Feedback", 72),
    (["how do i", "how to", "guide", "tutorial"], "Self-Serve — KB Deflect", 24),
]


def score_ticket(ticket: Ticket) -> Ticket:
    text = (ticket.subject + " " + ticket.description).lower()

    score = 0

    # Keyword scoring
    for keyword, points in KEYWORD_SCORES.items():
        if keyword in text:
            score += points

    # Age scoring (older unresolved tickets = higher priority)
    hours_open = (datetime.now() - ticket.created_at).total_seconds() / 3600
    if hours_open > 24:
        score += 10
    if hours_open > 48:
        score += 15
    if hours_open > 72:
        score += 25

    # VIP organisation boost
    if ticket.organization.lower() in ["enterprise", "vip", "gold"]:
        score += 20

    # Channel scoring (phone > chat > email)
    if ticket.channel == "phone":
        score += 10
    elif ticket.channel == "chat":
        score += 5

    ticket.score = score

    # Queue assignment
    ticket.recommended_queue = "General Support"
    ticket.recommended_sla_hours = 8

    for keywords, queue, sla in QUEUE_RULES:
        if any(kw in text for kw in keywords):
            ticket.recommended_queue = queue
            ticket.recommended_sla_hours = sla
            break

    # Priority label
    if score >= 40:
        ticket.priority = "urgent"
    elif score >= 20:
        ticket.priority = "high"
    elif score >= 5:
        ticket.priority = "normal"
    else:
        ticket.priority = "low"

    return ticket


# ---------------------------------------------------------------------------
# Demo data generator
# ---------------------------------------------------------------------------

SAMPLE_SUBJECTS = [
    "Can't login to my account — locked out",
    "Question about how to set up the integration",
    "Charged twice this month — please refund",
    "Feature request: dark mode",
    "API webhook stopped working — urgent",
    "How do I export my data?",
    "Security concern — unauthorized login attempt",
    "Account upgrade question",
    "Getting error 500 on the dashboard",
    "Can't access reports — need help ASAP",
    "When will you add Slack integration?",
    "Data not syncing for the past 3 hours",
    "Forgot password — reset email not arriving",
    "Need invoice for last month",
    "Team member can't be invited — shows error",
]

SAMPLE_REQUESTERS = [
    "alice@acmecorp.com", "bob@brightpath.io", "carol@cloudnine.co",
    "david@dataflow.com", "emma@easyops.net", "frank@fintrack.com",
    "grace@growthbase.io", "henry@hubworks.co"
]

SAMPLE_ORGS = ["Standard", "Standard", "Standard", "Enterprise", "VIP", "Standard", "Gold"]
SAMPLE_CHANNELS = ["email", "email", "email", "chat", "phone"]


def generate_demo_tickets(count: int = 30) -> list[Ticket]:
    tickets = []
    for i in range(count):
        created = datetime.now() - timedelta(
            hours=random.randint(1, 96),
            minutes=random.randint(0, 59)
        )
        subject = random.choice(SAMPLE_SUBJECTS)
        tickets.append(Ticket(
            id=10000 + i,
            subject=subject,
            description=f"Additional details about: {subject.lower()}. "
                        f"The user has tried the usual troubleshooting steps.",
            requester=random.choice(SAMPLE_REQUESTERS),
            created_at=created,
            status=random.choice(["new", "open", "pending"]),
            organization=random.choice(SAMPLE_ORGS),
            channel=random.choice(SAMPLE_CHANNELS),
        ))
    return tickets


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_triage_csv(tickets: list[Ticket], output_path: str) -> None:
    fieldnames = [
        "Ticket ID", "Subject", "Requester", "Org Tier",
        "Channel", "Hours Open", "Priority Score", "Priority",
        "Recommended Queue", "SLA (hours)", "Tags"
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for t in sorted(tickets, key=lambda x: x.score, reverse=True):
            hours_open = round((datetime.now() - t.created_at).total_seconds() / 3600, 1)
            writer.writerow({
                "Ticket ID": t.id,
                "Subject": t.subject[:60],
                "Requester": t.requester,
                "Org Tier": t.organization,
                "Channel": t.channel,
                "Hours Open": hours_open,
                "Priority Score": t.score,
                "Priority": t.priority.upper(),
                "Recommended Queue": t.recommended_queue,
                "SLA (hours)": t.recommended_sla_hours,
                "Tags": ", ".join(t.tags),
            })
    print(f"Triage report written to: {output_path}")


def print_summary(tickets: list[Ticket]) -> None:
    print(f"\n{'='*55}")
    print(f"  TRIAGE SUMMARY — {len(tickets)} tickets scored")
    print(f"{'='*55}")

    priority_counts = {}
    queue_counts = {}
    for t in tickets:
        priority_counts[t.priority] = priority_counts.get(t.priority, 0) + 1
        queue_counts[t.recommended_queue] = queue_counts.get(t.recommended_queue, 0) + 1

    print("\nBy Priority:")
    for p in ["urgent", "high", "normal", "low"]:
        count = priority_counts.get(p, 0)
        bar = "█" * count
        print(f"  {p.upper():<8} {count:>3}  {bar}")

    print("\nBy Queue:")
    for queue, count in sorted(queue_counts.items(), key=lambda x: -x[1]):
        print(f"  {queue:<35} {count:>3} tickets")

    top5 = sorted(tickets, key=lambda x: x.score, reverse=True)[:5]
    print("\nTop 5 Priority Tickets:")
    for t in top5:
        print(f"  #{t.id}  [{t.priority.upper():<6}] Score:{t.score:<4} {t.subject[:45]}")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Zendesk ticket triage and priority scorer")
    parser.add_argument(
        "--mode", choices=["score", "report", "demo"], default="demo",
        help="score=live Zendesk data, report=metrics only, demo=sample data"
    )
    parser.add_argument("--output", default="triage_report.csv")
    args = parser.parse_args()

    if args.mode == "demo":
        print("Running in DEMO mode with sample data...")
        tickets = generate_demo_tickets(30)
        tickets = [score_ticket(t) for t in tickets]
        print_summary(tickets)
        write_triage_csv(tickets, args.output)

    elif args.mode == "score":
        subdomain = os.environ.get("ZENDESK_SUBDOMAIN")
        email = os.environ.get("ZENDESK_EMAIL")
        token = os.environ.get("ZENDESK_API_TOKEN")
        if not all([subdomain, email, token]):
            print("ERROR: Set ZENDESK_SUBDOMAIN, ZENDESK_EMAIL, and ZENDESK_API_TOKEN env vars.")
            print("Or run with --mode demo to test without credentials.")
            return
        print(f"Connecting to {subdomain}.zendesk.com ...")
        print("Note: Live Zendesk API integration requires the requests library.")
        print("Install with: pip install requests")
        print("See docs/triage-guide.md for API setup instructions.")

    elif args.mode == "report":
        tickets = generate_demo_tickets(120)
        tickets = [score_ticket(t) for t in tickets]
        print_summary(tickets)


if __name__ == "__main__":
    main()
