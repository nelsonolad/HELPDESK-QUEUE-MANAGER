# Integration & API Troubleshooting

**Category:** Technical  
**Last Updated:** 2024-01-10  
**Helpful:** 88% (based on 96 ratings)

---

## My integration stopped working

Start with these checks before contacting support:

**Check 1 — Is the integration still connected?**
Go to **Settings → Integrations** and check the status indicator next to your integration. If it shows a red or yellow indicator, the connection has been broken and needs to be reconnected.

**Fix:** Click **Reconnect** → re-authenticate with your third-party credentials.

**Check 2 — Has your API key or credentials changed?**
If you recently changed your password or rotated API keys in the connected service (Zapier, Slack, Salesforce, etc.), the integration will stop working until you update the credentials here.

**Fix:** Settings → Integrations → select the integration → Update Credentials.

**Check 3 — Did the third-party service have an outage?**
Check the status page for the connected service (e.g., [status.zapier.com](https://status.zapier.com), [status.slack.com](https://status.slack.com)) to confirm it was not their issue.

---

## Webhook not triggering

1. Confirm the webhook URL is correct and reachable from the internet
2. Check that the event type matches what you've subscribed to
3. Test the webhook using the **Send Test** button in Settings → Webhooks
4. Check your server logs for the incoming request — if the request is arriving but failing, the issue is on your server side

**Webhook delivery log:** Settings → Webhooks → select your webhook → View Delivery Log. This shows every attempt and its response code.

Common response codes:
- `200` — successful
- `401` — authentication error (check your secret/token)
- `404` — URL not found (check your endpoint path)
- `500` — error on your server side

---

## API rate limits

The API allows **1,000 requests per hour** per API key. If you exceed this:
- Requests return a `429 Too Many Requests` response
- Limits reset at the top of each hour
- The response includes a `Retry-After` header indicating when to retry

**To avoid rate limit issues:**
- Implement exponential backoff in your API client
- Cache responses where possible instead of polling repeatedly
- Use webhooks instead of polling for real-time updates

---

## Getting your API key

Go to **Settings → API → Generate API Key**. Keep it secure — treat it like a password.

If your API key has been exposed, revoke it immediately from the same page and generate a new one.

---

## Contact Support

For integration issues not resolved by the above, contact support with:
- The integration name
- Error message or response code
- A screenshot of the integration status page
- Approximate time the issue started

Email: support@{{company_domain}}  
Subject: `Integration Issue — [Integration Name]`
