# Knowledge Base Style Guide

Follow these standards when writing or reviewing KB articles to ensure consistency, clarity, and high deflection rates.

---

## The goal of every KB article

A good KB article does **one thing**: helps the reader solve their problem without contacting support.

If they still need to contact support after reading it, the article failed.

---

## Article structure

Every article must have:

1. **Title** — a question or task statement (see below)
2. **Category label and last-updated date** at the top
3. **Answer first** — lead with the solution, not context
4. **Steps** for procedural content (numbered, action-first)
5. **Troubleshooting section** for common failure modes
6. **Contact support section** at the bottom — always include

Optional:
- Note or warning callouts for important caveats
- Screenshots or GIFs for complex UI flows

---

## Title rules

Titles should match how users search — usually a question or task:

| Good | Avoid |
|------|-------|
| How do I reset my password? | Password reset |
| Why am I being charged twice? | Billing issues |
| How to invite team members | Team member management |
| I can't log in — what do I do? | Login troubleshooting |

Use the user's language, not product jargon.

---

## Writing style

**Be direct.** Users are frustrated. Don't make them read three paragraphs before getting to the answer.

**Write in second person.** "You can find your invoices in Settings" not "Invoices can be found in Settings."

**Use active voice.** "Click Save" not "The Save button should be clicked."

**Keep sentences short.** If a sentence has more than 20 words, break it up.

**Avoid jargon.** "Two-step verification" not "Multi-factor authentication" (unless you explain the term first).

---

## Formatting rules

- Use **numbered lists** for sequential steps
- Use **bullet points** for non-sequential lists of 3+ items
- Use **bold** for UI element names: "Click **Settings** → **Billing**"
- Use `code formatting` for exact text the user types or sees (URLs, error codes)
- Use tables for comparisons and quick-reference content
- Add a horizontal rule (`---`) between major sections

---

## Screenshots

Include a screenshot when:
- The UI location is hard to describe in words
- The step involves a non-obvious UI element
- Users commonly get confused at this point

Screenshot rules:
- Annotate with red rectangles/arrows pointing to the relevant element
- Crop to show only the relevant part of the screen
- Alt text: describe what the image shows ("Settings page with Billing tab highlighted")
- Keep file size under 200KB

---

## Tone

Empathetic but efficient. Acknowledge frustration briefly, then move to the solution.

| Tone to use | Tone to avoid |
|-------------|--------------|
| "Here's how to fix that quickly." | "We're so sorry you're experiencing this issue!" |
| "This usually happens when..." | "Unfortunately this is a known limitation..." |
| "Contact support if this doesn't work." | "Please don't hesitate to reach out to our team!" |

---

## Measuring article quality

Track monthly:
- **Helpfulness rating** — target ≥ 85% "Yes, this helped"
- **Time on page** — under 2 minutes = article is clear; over 5 minutes = likely confusing
- **Ticket deflection** — did ticket volume for this topic drop after article was published?
- **Search terms** — are users finding this article? Are the title/tags right?

If an article's helpfulness drops below 70%, flag it for a rewrite.

---

## Review cadence

- New articles: reviewed by one peer before publishing
- Existing articles: audited every 90 days or after any product update that affects the topic
- Articles referencing deprecated features: archived or updated within 2 weeks of feature removal
