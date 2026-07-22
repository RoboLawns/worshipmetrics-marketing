# WorshipMetrics Launch Messaging Plan

_Drafted 2026-07-22 · pairs with the Homestretch scoreboard (57% built, 42/321 shipped)_

---

## 1. The positioning shift

**From:** "The support team for your church's AV." (support-first — we help you run *your* stream)
**To:** "We handle your live stream — and everything around it." (destination-first — the stream runs *through us*)

With Livestream 2.0 (Cloudflare ingest + fan-out re-streaming + recordings + live clips), WorshipMetrics stops being a layer *next to* the stream and becomes the place the stream *lives*. That collapses the pitch from ten features into one sentence:

> **Send us one feed. We put it everywhere, record it, clip it, watch it live, and answer the phone seven days a week.**

Everything else the app does — planning, volunteers, presentation, switcher control, device maps, monitoring — is no longer a feature list. It's the answer to "what does 'everything around it' mean?"

**Category we claim:** the church live streaming platform (not "streaming tool," not "church management software").
**One-line differentiator vs. every competitor:** they give you software; we take responsibility for Sunday. Human support, seven days a week, from people who run church production.

**Who we're talking to:**
1. **The volunteer tech director** (primary) — wants Sunday to stop being scary. Message: "handled."
2. **The pastor / exec pastor** (buyer) — wants reach, reliability, one bill. Message: "one platform, one number to call."

---

## 2. Tagline

**Recommended:**

> ### Your live stream, handled.

Why: it's the user promise in three words, it's ownable (nobody in the category says "handled"), and it implies the support story without needing a second clause. Works standalone under the lockup, on merch, in ads.

**Runners-up (keep for section headers / campaigns):**
- "We handle the stream. And everything around it." — the long-form version; great homepage sub or About opener.
- "One feed in. Every Sunday out." — the re-streaming pitch; use on the streaming feature page.
- "Sunday has a pulse. We watch it." — brand-flavored (beat icon tie-in); use for monitoring/support sections, not the master tagline.
- "Plan it. Present it. Stream it. Handled." — sequence-flavored; good for video scripts.

**Retire:** "Know first. Fix faster." (current hero) and "Catch problems first. Document your system. Get real help." (footer tag). Both are support-era; fold their spirit into the support pillar section instead.

---

## 3. Message architecture — the order matters

Lead with the destination, prove it with support, then widen to the platform. Never open with the feature grid.

**Tier 1 — the promise (hero):** We handle your live stream.
**Tier 2 — the proof (why believe it):**
1. One feed in, everywhere out — Cloudflare fan-out to YouTube, Facebook, your website, anywhere (`WM-296`)
2. Every service recorded, trimmed, and clipped — even live during the service (`WM-315` `WM-297` `WM-298`)
3. Watched live, with alerts when anything drops (`WM-087` ✅ shipped)
4. **Real humans, 7 days a week** — support staffed by people who run church production, plus Luminos AI
**Tier 3 — the platform (everything around it),** in service-lifecycle order:

| Order | Pillar (internal) | Marketing name | The one-liner |
|---|---|---|---|
| 1 | Plan | **Plan the service** | Order of service, songs, keys, chord charts, run it live with timers |
| 2 | People | **Schedule the team** | Volunteers, positions, invites, team chat |
| 3 | Present | **Put it on screen** | Slides, lyrics, stage display |
| 4 | Produce | **Run the booth** | Switcher control, PTZ cameras, audio meters, booth health |
| 5 | Publish | **Stream it everywhere** | The Tier-2 story — this pillar is the hero |
| 6 | Pulse | **Watch everything** | Fleet monitoring, stream health, alerts, attendance |
| 7 | Patch | **Know your gear** | Device inventory, signal map, patch sheets |

The "7 P's" naming is a gift — keep it as the platform motif ("Seven jobs. One platform.") but always translate each P into a verb phrase for outsiders.

**The consolidation argument (pricing page + comparison pages):** WorshipMetrics replaces the stack — a streaming provider (BoxCast/Resi/Restream), planning software (Planning Center), presentation software (ProPresenter), team chat (Slack), monitoring (nothing — churches don't have it), and the support contract nobody offers. One subscription, one login, one phone number: 910-WORSHIP.

---

## 4. Homepage — sequential presentation

1. **Hero.** Eyebrow: `LIVE STREAMING · PRODUCTION · 7-DAY SUPPORT`. H1: **"Your live stream, handled."** Sub: "Send WorshipMetrics one feed. We stream it to every destination, record and clip it, watch it live, and answer the phone seven days a week — with every tool your team needs around it." CTA: Get started free / Talk to a person.
2. **How it works, in one line.** Three steps with the beat icon as the connector: *One feed in → everywhere out → clips by Monday.*
3. **Re-streaming.** "One feed in. Every Sunday out." Destinations grid (YouTube, Facebook, website embed, custom RTMP).
4. **Recordings & clips.** "Sunday doesn't end at noon." Auto-recorded services, trim and hand off to clips, chop clips live during service.
5. **The support wall.** "Seven days a week, a human who runs church production." 910-WORSHIP, tickets, chat, Luminos AI with your actual system context. This section carries the old "Know first. Fix faster." energy — monitoring + stream-drop alerts + proactive help.
6. **The platform band.** "Everything around the stream." Seven cards in lifecycle order (table above), each linking to its page.
7. **Replace-your-stack comparison.** Table: what you're paying for today vs. one WorshipMetrics subscription.
8. **Social proof / pilot program** and closing CTA.

**Headline bank for feature pages:**
- /live-streaming (new page): "One feed in. Every Sunday out."
- /solutions/worship-clips: "The sermon, clipped before Monday."
- /services (Plan): "Sunday is planned by Wednesday."
- /volunteers (People): "The team schedules itself."
- /present (new): "Lyrics up. Stage covered."
- /tech-manager / booth (Produce): "The booth, in one window."
- /av-monitoring (Pulse): "We're watching, so you can worship."
- /system-documentation (Patch): "Every cable, mapped."
- /pricing support section: "910-WORSHIP. Seven days a week. A person answers."

---

## 5. Honesty guardrails — what messaging must wait for

The streaming-destination claim is only true when the Livestream 2.0 items ship. Gate public copy on these:

| Claim | Requires | Homestretch status |
|---|---|---|
| "We stream to every destination" | `WM-296` Cloudflare fan-out | **Not started** |
| "Every service recorded + trimmed" | `WM-315` recordings library | **Not started** |
| "Clip live during the service" | `WM-297` | **Not started** |
| "Clip from the recording after" | `WM-298` | **Not started** |
| "We alert you the moment the stream drops" | `WM-087` | ✅ Shipped |
| "Alerts on your phone" | `WM-319` mobile push | Not started (say "email + in-app" until then) |
| "Works on your phone" (volunteers) | Responsive shell (15%) | Don't claim yet |
| "7-day support" | Operational commitment, not code | Confirm staffing before it goes on the homepage |

Until `WM-296`–`WM-298` ship, marketing can say "coming at launch" on a waitlist/announcement page but the homepage hero must not promise it. **Sequencing: ship Publish pillar → flip the homepage.** Present (37%) and show control (not started) stay out of headline copy entirely at launch; they're roadmap.

---

## 6. Rollout plan

**Phase 1 — now (pre-launch, current site):**
- Update footer tagline + why-us page to the new frame ("and everything around it") without claiming fan-out yet.
- Build /live-streaming as an announcement page ("Livestream 2.0 is coming — one feed in, every Sunday out") with waitlist CTA; start SEO aging ("church live streaming platform", "boxcast alternative", "restream for churches", "church streaming service with support").
- Add the 7-day support promise to nav topbar, pricing, and contact — once staffing is confirmed.

**Phase 2 — launch (Livestream 2.0 ships):**
- Flip homepage to the Section-4 sequence; retire "Know first. Fix faster."
- Nav reorder: **Streaming** first (new), then Plan, People, Present, Produce, Pulse, System, Support.
- Publish comparison pages (vs BoxCast, vs Resi, vs Restream, vs "the stack").
- Update OG images, Google Ads copy, and structured data descriptions to the new tagline.

**Phase 3 — post-launch:**
- Case study from a pilot church: "one feed in" story with numbers.
- Present/show-control messaging only when those pillars pass ~70%.

---

## 7. Voice notes (per brand kit)

Archivo 800 headlines: short, declarative, period at the end. "Your live stream, handled." not "The all-in-one solution for church streaming!" Mono eyebrows carry the technical/measured voice (`ONE FEED IN · EVERY SUNDAY OUT`). Plain-spoken body copy — we talk like the person who answers 910-WORSHIP, because that's the product.
