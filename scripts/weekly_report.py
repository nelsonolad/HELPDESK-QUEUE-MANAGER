#!/usr/bin/env python3
"""
Weekly Helpdesk Metrics Report Generator

Generates an HTML dashboard from ticket data.

Usage:
    python weekly_report.py --week 2024-W03 --output report.html
    python weekly_report.py --demo
"""

import argparse
import random
from datetime import datetime, timedelta


def generate_demo_metrics():
    return {
        "week": "2024-W03",
        "total_tickets": 78,
        "resolved": 71,
        "open": 7,
        "fcr_rate": 82,
        "avg_resolution_hours": 6.5,
        "csat": 4.6,
        "deflected_by_kb": 27,
        "by_priority": {"urgent": 4, "high": 12, "normal": 45, "low": 17},
        "by_queue": {
            "Tier 1 Priority": 18,
            "Billing": 11,
            "Tier 2 — Technical": 14,
            "General Support": 24,
            "Product Feedback": 11,
        },
        "daily_volume": {
            "Mon": 19, "Tue": 16, "Wed": 14,
            "Thu": 15, "Fri": 14
        },
        "top_kb_articles": [
            ("Password Reset Guide", 42),
            ("How to Invite Team Members", 38),
            ("Billing & Invoice FAQ", 31),
            ("API Integration Troubleshooting", 28),
            ("Account Access Issues", 24),
        ]
    }


def render_html(m: dict) -> str:
    max_daily = max(m["daily_volume"].values())
    bar_rows = ""
    for day, vol in m["daily_volume"].items():
        pct = round((vol / max_daily) * 100)
        bar_rows += f"""
        <tr>
          <td style="padding:4px 10px 4px 0;font-size:13px;color:#555;width:36px">{day}</td>
          <td style="padding:4px 0;">
            <div style="background:#185FA5;height:18px;width:{pct}%;border-radius:3px;min-width:4px;"></div>
          </td>
          <td style="padding:4px 0 4px 8px;font-size:13px;color:#333;width:30px">{vol}</td>
        </tr>"""

    queue_rows = ""
    total_q = sum(m["by_queue"].values())
    for queue, count in sorted(m["by_queue"].items(), key=lambda x: -x[1]):
        pct = round((count / total_q) * 100)
        queue_rows += f"""
        <tr style="border-bottom:0.5px solid #eee;">
          <td style="padding:8px 12px 8px 0;font-size:13px;">{queue}</td>
          <td style="padding:8px 0;font-size:13px;font-weight:500;">{count}</td>
          <td style="padding:8px 0 8px 12px;font-size:13px;color:#888;">{pct}%</td>
        </tr>"""

    kb_rows = ""
    for title, views in m["top_kb_articles"]:
        kb_rows += f"""
        <tr style="border-bottom:0.5px solid #eee;">
          <td style="padding:7px 12px 7px 0;font-size:13px;">{title}</td>
          <td style="padding:7px 0;font-size:13px;font-weight:500;color:#0C447C;">{views}</td>
        </tr>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Helpdesk Weekly Report — {m['week']}</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
         color: #1a1a1a; background: #f8f8f6; margin: 0; padding: 2rem; }}
  h1 {{ font-size: 22px; font-weight: 600; margin: 0 0 4px; }}
  .sub {{ font-size: 14px; color: #666; margin: 0 0 2rem; }}
  .grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 2rem; }}
  .card {{ background: #fff; border: 0.5px solid #e0e0dc; border-radius: 10px; padding: 16px 20px; }}
  .card .num {{ font-size: 28px; font-weight: 600; }}
  .card .lbl {{ font-size: 12px; color: #888; margin-top: 2px; }}
  .card .num.green {{ color: #0F6E56; }}
  .card .num.blue {{ color: #185FA5; }}
  .row2 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }}
  .panel {{ background: #fff; border: 0.5px solid #e0e0dc; border-radius: 10px; padding: 1.25rem; }}
  .panel h2 {{ font-size: 13px; font-weight: 500; text-transform: uppercase;
               letter-spacing: 0.06em; color: #888; margin: 0 0 1rem; }}
  table {{ width: 100%; border-collapse: collapse; }}
</style>
</head>
<body>

<h1>Helpdesk Weekly Report</h1>
<p class="sub">Week {m['week']} &nbsp;·&nbsp; Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>

<div class="grid">
  <div class="card">
    <div class="num">{m['total_tickets']}</div>
    <div class="lbl">Total tickets</div>
  </div>
  <div class="card">
    <div class="num green">{m['fcr_rate']}%</div>
    <div class="lbl">First-contact resolution</div>
  </div>
  <div class="card">
    <div class="num blue">{m['avg_resolution_hours']}h</div>
    <div class="lbl">Avg. resolution time</div>
  </div>
  <div class="card">
    <div class="num">{m['csat']}/5</div>
    <div class="lbl">CSAT score</div>
  </div>
</div>

<div class="row2">
  <div class="panel">
    <h2>Daily volume</h2>
    <table>{bar_rows}</table>
  </div>
  <div class="panel">
    <h2>By queue</h2>
    <table>{queue_rows}</table>
  </div>
  <div class="panel">
    <h2>Top KB articles</h2>
    <table>{kb_rows}</table>
    <p style="font-size:12px;color:#888;margin-top:12px;">
      {m['deflected_by_kb']} tickets deflected via self-serve this week
    </p>
  </div>
</div>

</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Generate weekly helpdesk report")
    parser.add_argument("--week", default="2024-W03")
    parser.add_argument("--output", default="weekly_report.html")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    metrics = generate_demo_metrics()
    metrics["week"] = args.week

    html = render_html(metrics)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Report written to: {args.output}")
    print(f"Open in browser: open {args.output}")


if __name__ == "__main__":
    main()
