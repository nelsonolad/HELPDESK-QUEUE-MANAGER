Helpdesk Queue Manager — Zendesk Optimisation System
> Managed a 120-ticket/week helpdesk for a 200-seat remote company. Implemented tag-based routing, wrote 30+ KB articles, achieved **80%+ first-contact resolution** and **35% ticket deflection** from self-serve content.
---
Overview
This repository contains the full Zendesk helpdesk optimisation system including:
Tag-based routing rules and trigger configuration (JSON exports)
30+ knowledge base article templates covering the most common issue categories
Ticket triage Python script for automated priority scoring
Weekly reporting dashboard (Python + CSV)
Zendesk macro library (copy-paste ready)
Results
Metric	Before	After
First-Contact Resolution Rate	~55%	80%+
Avg. ticket resolution time	18 hours	6.5 hours
Weekly ticket volume	120	78 (post-KB launch)
Ticket deflection via self-serve	~10%	35%
CSAT score	3.8/5	4.6/5
---
Repository Structure
```
project2-helpdesk-queue-manager/
├── zendesk/
│   ├── triggers.json           # Routing trigger configurations
│   ├── macros.json             # Response macro library
│   └── views.json              # Custom queue views
├── kb-articles/
│   ├── account-access.md
│   ├── billing-faq.md
│   ├── integrations.md
│   ├── password-reset.md
│   └── [26 more templates]
├── scripts/
│   ├── ticket_triage.py        # Priority scoring + auto-tag script
│   └── weekly_report.py        # Weekly metrics dashboard generator
└── docs/
    ├── triage-guide.md         # Agent triage SOP
    └── kb-style-guide.md       # Writing guide for KB articles
```
---
Prerequisites
Python 3.8+
Zendesk Support account (Team plan or above for triggers/macros)
`pip install requests pandas rich`
Quick Start
1. Import Zendesk configurations
```bash
# Set your credentials
export ZENDESK_SUBDOMAIN=yourcompany
export ZENDESK_EMAIL=your@email.com
export ZENDESK_API_TOKEN=your_token_here

# Run the import script
python scripts/ticket_triage.py --mode import-config
```
2. Run the triage scorer on open tickets
```bash
python scripts/ticket_triage.py --mode score --output triage_report.csv
```
3. Generate weekly report
```bash
python scripts/weekly_report.py --week 2024-W03 --output report.html
```
---
Zendesk Tag Routing System
Tickets are automatically tagged and routed using this priority matrix:
Tag	Trigger Condition	Assigned Queue	SLA
`billing_urgent`	Subject contains "charge", "refund", "invoice"	Billing	2h
`login_blocked`	Subject contains "can't login", "locked out"	Tier 1 Priority	1h
`integration_broken`	Subject contains "API", "webhook", "integration"	Tier 2	4h
`feature_request`	Tag: feature_request	Product Queue	72h
`vip_client`	Organisation tier = Enterprise	VIP Queue	30m
---
License
MIT
