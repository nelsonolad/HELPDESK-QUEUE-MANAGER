# Ticket Triage Guide — Agent SOP

This guide explains how to triage incoming tickets correctly and consistently. Following it keeps first-contact resolution high and SLAs green.

---

## The 3-step triage process

Every new ticket gets three things within the first 2 minutes of touching it:

1. **Categorise** — what type of issue is this?
2. **Prioritise** — how urgent is it?
3. **Route** — does it stay with you or get escalated?

---

## Step 1: Categorise

Read the subject line and first two sentences of the description. Assign one tag:

| Category | Signs | Tag |
|----------|-------|-----|
| Login / Access | "can't login", "locked out", "password", "access denied" | `login_issue` |
| Billing | "charged", "invoice", "refund", "cancel", "subscription" | `billing` |
| Technical / Bug | "not working", "error", "broken", "won't load", "500" | `technical` |
| Integration | "API", "webhook", "Zapier", "sync", "integration" | `integration` |
| How-To | "how do I", "how to", "guide", "where is" | `how_to` |
| Feature Request | "it would be great if", "can you add", "feature request" | `feature_request` |
| Security | "hack", "breach", "unauthorized", "someone accessed" | `security` |

If it spans two categories, pick the most urgent one.

---

## Step 2: Prioritise

Use this matrix — find the row that best matches the ticket:

| Situation | Priority | SLA |
|-----------|----------|-----|
| Customer can't use the product at all | Urgent | 1 hour |
| Security concern or suspected breach | Urgent | 30 min |
| Enterprise/VIP customer, any issue | Urgent | 30 min |
| Billing dispute or accidental charge | High | 2 hours |
| Technical bug affecting core workflow | High | 4 hours |
| Login issue (not Enterprise) | High | 2 hours |
| General how-to question | Normal | 8 hours |
| Feature request | Low | 72 hours |

**When in doubt, go one level higher on priority.** It's better to over-prioritise than miss an SLA.

---

## Step 3: Route

| Category | Who handles it |
|----------|----------------|
| Login / Access (Tier 1) | You — resolve directly |
| How-To | You — check KB first; link article or answer directly |
| Billing | Assign to Billing queue |
| Technical / Bug (can't reproduce) | You — escalate to Tier 2 if 2 attempts fail |
| Integration / API | Escalate to Tier 2 immediately |
| Security | Escalate to Senior Engineer immediately — do NOT attempt to resolve yourself |
| Feature Request | Assign to Product Feedback queue; send acknowledgement macro |

---

## First response standards

**Within SLA window:**
- Acknowledge every ticket immediately with an automated response (trigger handles this)
- Personalise your first real response — use the customer's name, reference their specific issue

**What a good first response includes:**
1. Acknowledgement of the issue in your own words ("It sounds like...")
2. What you're doing about it right now
3. Expected next update time
4. Direct question if you need more info — one question only

**What to avoid:**
- Generic openers: "Thank you for contacting support..."
- Multiple questions in one reply
- Asking for info that was already in the ticket
- Promising a fix time you can't keep

---

## Escalation rules

Escalate to Tier 2 when:
- You've attempted two different solutions and the issue persists
- The issue requires backend database access or code changes
- The issue involves an API, webhook, or third-party integration
- The customer has been waiting > 4 hours with no resolution

When escalating:
1. Add an internal note summarising: issue, what you've already tried, customer tone
2. Change assignee to Tier 2 group
3. Send a brief update to the customer: "I've looped in a technical specialist who can dig deeper — you'll hear from them within [X] hours."
4. Do not mark as Pending unless waiting on customer input

---

## Common resolutions (no escalation needed)

**Password reset:**
Admin Centre → Users → select user → Reset password. Takes 2 minutes.

**Account unlock:**
Admin Centre → Users → select user → Unlock. If persistent, check for failed login spike.

**Wrong plan / billing confusion:**
Check their subscription in Billing → Subscriptions. Screenshot and explain clearly. Refunds require Billing team involvement.

**Feature doesn't work as expected:**
Check if the feature is on their plan tier. Many "bugs" are feature-gated.

**Email not receiving:**
Check spam filters first. Then check MX records and email logs in admin.

---

## Closing a ticket

Only close (Solved) when:
- The issue is confirmed resolved by you or the customer
- 24 hours have passed since your last message with no reply (pending → solved)

Always add a resolution note before closing:
> "Resolved by [action taken]. Root cause: [what caused it]."

This feeds into weekly reporting and KB improvements.
