# Church AV Knowledge Base — Full Expanded Site Scope
**For: Coding & Content Generation Agents**
**Version:** 2.0 — Ambitious Full Build
**Builds on:** `church-av-kb-agent-scope.md` + `church-ptz-kb-expansion-scope.md`

---

## Vision

Build the most comprehensive, device-specific church AV knowledge base on the internet. Every page targets a real search query from a real church AV volunteer or tech director who just bought gear, can't get it working, and has nobody to call. We answer every question better than the manufacturer does. Every article ends with a natural path to Tech Manager.

**Target page count at full build:** 300–400 indexed pages
**Content model:** Device Category → Brand → Model → Article Type
**Conversion goal:** Tech Manager downloads, sign-ups, discovery calls

---

## Site Architecture — Full Route Map

```
/                                   Home
/articles/[slug]                    General AV knowledge base (existing 20)
/category/[category]                Category index pages
/cameras/                           PTZ camera hub (from scope v1)
/cameras/[brand]/[slug]             Camera brand + model docs
/switchers/                         Video switcher hub  ← NEW
/switchers/[brand]/[slug]           Switcher docs
/encoders/                          Hardware encoder hub  ← NEW
/encoders/[brand]/[slug]            Encoder docs
/mixers/                            Audio mixer hub  ← NEW
/mixers/[brand]/[slug]              Mixer docs
/software/                          Streaming software hub  ← NEW
/software/[app]/[slug]              Software docs
/workflows/                         End-to-end production workflows  ← NEW
/workflows/[slug]                   Complete church streaming workflow guides
/compare/[slug]                     Head-to-head comparison pages  ← NEW
/budget/[size]                      Budget-tier solution guides  ← NEW
/troubleshooting/                   Master troubleshooting index  ← NEW
/troubleshooting/[slug]             Problem-first articles
/search                             Pagefind search
/about                              About page
```

Each hub page (`/cameras`, `/switchers`, etc.) is a high-value SEO landing page in its own right — brand index, article count, category description, internal linking.

---

## Content Collections — Full Schema

### Existing: `src/content/articles/` — General KB (20 articles, keep as-is)

### Existing: `src/content/cameras/` — PTZ Camera Docs (from scope v1)

### New: `src/content/devices/`
Shared schema for switchers, encoders, mixers. Keeps the data model consistent across all hardware categories.

```ts
const devices = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    deviceCategory: z.enum(['switcher', 'encoder', 'mixer', 'capture-card', 'converter']),
    brand: z.string(),               // "Blackmagic", "Roland", "Behringer", etc.
    modelId: z.string(),             // slug-safe model identifier
    modelFullName: z.string(),       // display name
    articleType: z.enum([
      'setup-guide',
      'troubleshooting',
      'integration',
      'firmware-update',
      'multi-unit',
      'software-control',
      'comparison',
      'overview',
      'workflow',
    ]),
    category: z.enum([
      'device-setup',
      'troubleshooting',
      'how-to',
      'streaming',
      'audio',
      'comparison',
    ]),
    tags: z.array(z.string()),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']),
    priceRange: z.enum(['under-500', '500-1500', '1500-plus']).optional(),
    publishedAt: z.date(),
    updatedAt: z.date().optional(),
    relatedModels: z.array(z.string()).optional(),
    productCTA: z.boolean().default(true),
  }),
});
```

### New: `src/content/software/`
```ts
const software = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    app: z.enum(['obs', 'vmix', 'propresenter', 'easyworship', 'restream', 'castr', 'streamlabs', 'wirecast', 'atem-software']),
    articleType: z.enum(['setup-guide', 'feature-guide', 'integration', 'troubleshooting', 'comparison']),
    tags: z.array(z.string()),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']),
    publishedAt: z.date(),
    updatedAt: z.date().optional(),
    productCTA: z.boolean().default(true),
  }),
});
```

### New: `src/content/workflows/`
```ts
const workflows = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    churchSize: z.enum(['small', 'medium', 'large', 'multi-campus']),
    budget: z.enum(['under-1k', '1k-5k', '5k-plus']),
    gearList: z.array(z.string()),   // model IDs referenced
    tags: z.array(z.string()),
    publishedAt: z.date(),
    updatedAt: z.date().optional(),
    productCTA: z.boolean().default(true),
  }),
});
```

### New: `src/content/comparisons/`
```ts
const comparisons = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    competitorA: z.string(),
    competitorB: z.string(),
    competitorC: z.string().optional(),
    verdict: z.string(),             // one sentence recommendation
    tags: z.array(z.string()),
    publishedAt: z.date(),
    productCTA: z.boolean().default(true),
  }),
});
```

---

## SECTION 1: PTZ Cameras (from scope v1 — execute first)

*Refer to `church-ptz-kb-expansion-scope.md` for full detail.*

**Brands:** AVKANS, Tenveo, TONGVEO, FoMaKo, SMTAV, OBSBOT, Minrray
**Route:** `/cameras/[brand]/[slug]`
**Target articles:** ~48 model-specific + 6 cross-brand
**Status:** Fully specced in previous scope doc

---

## SECTION 2: Video Switchers

**Route:** `/switchers/[brand]/[slug]`
**Why this matters:** The ATEM Mini is in tens of thousands of churches. Kiloview and Roland are growing fast. Every church with 2+ cameras has a switcher and most have config problems they can't solve.

### Brands & Models

#### Blackmagic Design — Priority: 🔥 Highest
Most popular switcher brand in churches by far.

| Model ID | Full Name | Price Tier | Church Penetration |
|---|---|---|---|
| `atem-mini` | ATEM Mini | Under $300 | Massive — entry level |
| `atem-mini-pro` | ATEM Mini Pro | ~$500 | Very high |
| `atem-mini-pro-iso` | ATEM Mini Pro ISO | ~$800 | High |
| `atem-mini-extreme` | ATEM Mini Extreme | ~$1,200 | Medium |
| `atem-television-studio-hd` | ATEM Television Studio HD | ~$1,000 | Medium |
| `atem-television-studio-4k` | ATEM Television Studio 4K | ~$3,000 | Growing |
| `web-presenter-hd` | Blackmagic Web Presenter HD | ~$500 | High |

**Known pain points:**
- ATEM software control install and network discovery
- NDI sources not appearing in ATEM setup
- Audio routing from Behringer X32/X-Air to ATEM
- Upstream/downstream keyer setup with ProPresenter
- USB webcam output mode for Zoom/Teams
- Multi-cam preset recall via ATEM Macro
- Color correction per-input setup
- HDMI vs SDI signal path confusion

#### Roland — Priority: High

| Model ID | Full Name | Price Tier |
|---|---|---|
| `roland-v-1hd` | Roland V-1HD 4-Channel HD Video Mixer | ~$700 |
| `roland-v-02hd` | Roland V-02HD Streaming Video Mixer | ~$400 |
| `roland-v-160hd` | Roland V-160HD 16-Channel | ~$3,500 |

**Known pain points:**
- V-1HD transition effects and T-bar calibration
- Audio follow (AFV) setup
- NDI input configuration
- Connecting Roland to OBS as video source

#### Kiloview — Priority: Rising (budget-conscious, fast-growing)

| Model ID | Full Name | Notes |
|---|---|---|
| `kiloview-n2` | Kiloview N2 HDMI-NDI Encoder | HDMI to NDI conversion |
| `kiloview-e1` | Kiloview E1 HDMI Encoder | SRT/RTMP streaming |
| `kiloview-dc230` | Kiloview DC230 IP Video Decoder | Multi-site playback |

**Known pain points:**
- Web UI first-time configuration
- SRT caller vs listener mode confusion
- NDI discovery on church networks
- Multi-campus SRT distribution setup

#### Article Types Per Switcher Model (generate all 6 for ATEM Mini/Pro, top 4 for others)

| # | Article Type | Example Slug |
|---|---|---|
| 1 | Initial setup guide | `setup-guide-atem-mini-pro` |
| 2 | Audio routing guide | `audio-routing-atem-mini-behringer-x32` |
| 3 | NDI / software integration | `ndi-integration-atem-mini-obs` |
| 4 | ProPresenter keyer setup | `propresenter-keyer-atem-mini` |
| 5 | Troubleshooting dropped stream | `atem-mini-stream-dropping-fix` |
| 6 | Macro automation guide | `atem-mini-macros-church-automation` |

#### Cross-Switcher Comparison Articles

- `atem-mini-pro-vs-roland-v1hd-church`
- `atem-mini-vs-vmix-software-church`
- `best-video-switcher-church-under-500`
- `best-video-switcher-church-under-1000`
- `hardware-vs-software-switcher-church`

---

## SECTION 3: Hardware Encoders

**Route:** `/encoders/[brand]/[slug]`
**Why this matters:** Churches streaming to multiple platforms simultaneously need a reliable encoder. Magewell, Kiloview, and Teradek are the main players. Tons of first-time setup confusion.

### Brands & Models

#### Magewell — Priority: 🔥 High

| Model ID | Full Name | Notes |
|---|---|---|
| `magewell-ultra-encode-hdmi` | Magewell Ultra Encode HDMI | Most popular church encoder |
| `magewell-ultra-encode-sdi` | Magewell Ultra Encode SDI | SDI signal chain churches |
| `magewell-ultra-stream` | Magewell Ultra Stream HDMI | Standalone streaming |
| `magewell-usb-capture-hdmi` | Magewell USB Capture HDMI | Capture card for OBS |

**Pain points:**
- RTMP stream key configuration per platform
- SRT output setup for multi-campus distribution
- Bitrate and resolution settings for church environments
- Web UI first-time configuration

#### Teradek — Priority: Medium-High (aspirational purchase, many churches)

| Model ID | Full Name | Notes |
|---|---|---|
| `teradek-vidiu-x` | Teradek VidiU X | Popular church streamer |
| `teradek-vidiu-go` | Teradek VidiU Go | Bonded cellular streaming |
| `teradek-bolt-6` | Teradek Bolt 6 XT | Wireless video transmission |

#### Kiloview Encoders (overlaps with switcher section — cross-link)

| Model ID | Full Name |
|---|---|
| `kiloview-e1-hdmi` | Kiloview E1 HDMI Encoder |
| `kiloview-e2-sdi` | Kiloview E2 SDI Encoder |

#### Epiphan — Priority: Established install base

| Model ID | Full Name |
|---|---|
| `epiphan-webcaster-x2` | Epiphan Webcaster X2 |
| `epiphan-pearl-mini` | Epiphan Pearl Mini |

#### Article Types Per Encoder Model (generate top 5 for Magewell/Teradek, top 3 for others)

| # | Article Type | Example Slug |
|---|---|---|
| 1 | Initial setup + stream key config | `setup-guide-magewell-ultra-encode-hdmi` |
| 2 | Multi-platform streaming setup | `magewell-multistream-youtube-facebook` |
| 3 | SRT for multi-campus | `magewell-srt-multi-campus-church` |
| 4 | Bitrate optimization | `encoder-bitrate-settings-church-streaming` |
| 5 | Troubleshooting stream drops | `magewell-stream-dropping-fix` |

#### Cross-Encoder Comparison Articles

- `magewell-vs-teradek-church-streaming`
- `hardware-encoder-vs-obs-church`
- `best-encoder-church-streaming-under-500`
- `kiloview-vs-magewell-church`

---

## SECTION 4: Audio Mixers

**Route:** `/mixers/[brand]/[slug]`
**Why this matters:** Behringer X32 alone is installed in hundreds of thousands of churches globally. Configuration for streaming is constantly searched, poorly documented by manufacturers.

### Brands & Models

#### Behringer — Priority: 🔥 Highest volume by install base

| Model ID | Full Name | Notes |
|---|---|---|
| `behringer-x32` | Behringer X32 Digital Mixer | Most common church mixer globally |
| `behringer-x32-compact` | Behringer X32 Compact | Mid-size churches |
| `behringer-x-air-xr18` | Behringer X-Air XR18 | Small churches, tablet-controlled |
| `behringer-x-air-xr12` | Behringer X-Air XR12 | Entry-level X-Air |
| `behringer-wing` | Behringer WING | Growing in larger churches |

**Pain points:**
- USB audio routing to streaming PC for OBS/vMix
- Aux bus setup for streaming mix vs front-of-house mix
- X32-Edit remote control software setup
- Dante/AES50 digital snake setup
- Scene saving and recall for Sunday services
- X-Air app connectivity and control
- Feedback suppression and EQ for streaming audio

#### Allen & Heath — Priority: High (growing church install base)

| Model ID | Full Name | Notes |
|---|---|---|
| `allen-heath-sq5` | Allen & Heath SQ-5 | 48-channel, popular upgrade |
| `allen-heath-sq6` | Allen & Heath SQ-6 | Larger churches |
| `allen-heath-cq18t` | Allen & Heath CQ-18T | Budget digital, touch screen |
| `allen-heath-avantis` | Allen & Heath Avantis | Large churches |

**Pain points:**
- dSNAKE / GigACE digital snake setup
- Scene/Show file management for volunteers
- USB streaming output configuration
- Surface/tablet remote control setup

#### Yamaha — Priority: High (legacy install base + new TF series)

| Model ID | Full Name | Notes |
|---|---|---|
| `yamaha-tf1` | Yamaha TF1 | 16-channel, small-medium churches |
| `yamaha-tf3` | Yamaha TF3 | 24-channel |
| `yamaha-tf5` | Yamaha TF5 | 32-channel, popular mid-size |
| `yamaha-mg16xu` | Yamaha MG16XU | Budget analog, USB recording |

**Pain points:**
- TF StageMix iPad app setup
- USB audio interface for streaming
- Scene memory and snapshot management
- Dante card installation (NY64-D)

#### Mackie — Priority: Medium (budget market)

| Model ID | Full Name | Notes |
|---|---|---|
| `mackie-dl32r` | Mackie DL32R | Rack-mount, tablet-controlled |
| `mackie-profx16v3` | Mackie ProFX16v3 | Budget analog with USB |

#### PreSonus — Priority: Medium

| Model ID | Full Name | Notes |
|---|---|---|
| `presonus-studiolive-32s` | PreSonus StudioLive 32S | Serious church setups |
| `presonus-studiolive-16r` | PreSonus StudioLive 16R | Rack-mount, stage box |

#### Article Types Per Mixer Model (generate all 7 for Behringer X32, top 5 for others)

| # | Article Type | Example Slug |
|---|---|---|
| 1 | Initial setup guide | `setup-guide-behringer-x32-church` |
| 2 | Streaming audio setup (aux/USB) | `behringer-x32-streaming-audio-obs-vmix` |
| 3 | Volunteer-friendly scene setup | `behringer-x32-scene-recall-volunteers` |
| 4 | Remote control setup | `behringer-x32-edit-remote-control` |
| 5 | Gain staging for worship | `behringer-x32-gain-staging-church` |
| 6 | Multi-track recording | `behringer-x32-multitrack-recording` |
| 7 | Troubleshooting no sound / feedback | `behringer-x32-troubleshooting-no-audio` |

#### Cross-Mixer Comparison Articles

- `behringer-x32-vs-allen-heath-sq5-church`
- `behringer-x-air-xr18-vs-mackie-dl32r`
- `best-digital-mixer-church-under-1000`
- `best-digital-mixer-church-under-3000`
- `analog-vs-digital-mixer-small-church`
- `yamaha-tf-series-vs-behringer-x32`

---

## SECTION 5: Streaming Software

**Route:** `/software/[app]/[slug]`
**Why this matters:** OBS alone drives enormous search volume. Church-specific guides for streaming software are very thin. These rank fast and convert well.

### Apps to Cover

#### OBS Studio — Priority: 🔥 Highest

| Article Slug | Topic |
|---|---|
| `obs-church-complete-setup` | Full church streaming setup guide |
| `obs-scenes-church-service` | Scene setup for typical service flow |
| `obs-ndi-church-cameras` | NDI camera sources in OBS |
| `obs-audio-routing-church-mixer` | USB/aux audio from mixer to OBS |
| `obs-multistream-restream` | Streaming to YouTube + Facebook simultaneously |
| `obs-bitrate-settings-church` | Resolution and bitrate optimization |
| `obs-dropping-frames-fix` | Dropped frames troubleshooting |
| `obs-transitions-stingers-church` | Custom transitions for professional look |
| `obs-propresenter-ndi-together` | OBS + ProPresenter NDI integration |
| `obs-vmix-when-to-upgrade` | When OBS isn't enough, upgrade to vMix |

#### vMix — Priority: High

| Article Slug | Topic |
|---|---|
| `vmix-church-setup-guide` | Complete vMix church streaming guide |
| `vmix-ndi-camera-inputs` | NDI cameras in vMix |
| `vmix-instant-replay-church` | Replay system for worship |
| `vmix-4k-church-streaming` | 4K production in vMix |
| `vmix-vs-obs-church` | Which is right for your church? |
| `vmix-title-overlays-lower-thirds` | Graphics and lower thirds |

#### ProPresenter — Priority: High

| Article Slug | Topic |
|---|---|
| `propresenter-7-church-setup` | Complete ProPresenter 7 setup guide |
| `propresenter-ndi-output-obs-vmix` | NDI output into streaming software |
| `propresenter-stage-display-setup` | Stage display for worship leaders |
| `propresenter-alpha-keyer-atem` | Alpha keyer with ATEM Mini |
| `propresenter-scripture-planning-center` | PCO + ProPresenter integration |
| `propresenter-troubleshooting-crash` | Crash and performance troubleshooting |

#### Restream / Castr — Priority: Medium

| Article Slug | Topic |
|---|---|
| `restream-church-multiplatform-setup` | Setup guide for church multistreaming |
| `castr-vs-restream-church` | Which multistream service for churches? |
| `restream-obs-integration` | OBS + Restream together |

#### EasyWorship — Priority: Medium (niche but loyal install base)

| Article Slug | Topic |
|---|---|
| `easyworship-7-church-setup` | Complete setup guide |
| `easyworship-vs-propresenter` | Comparison for church media teams |
| `easyworship-ndi-streaming` | NDI output configuration |

---

## SECTION 6: End-to-End Workflow Guides

**Route:** `/workflows/[slug]`
**Why this matters:** These are pillar pages. High word count, high authority, massive internal linking surface. Every gear page links TO a workflow. Every workflow links to all gear pages. These also make the best AdWords landing pages — someone searching "church live streaming setup guide" hits a workflow page that links to every product your platform manages.

### Workflow Articles to Generate

| Slug | Title | Church Size | Budget |
|---|---|---|---|
| `small-church-streaming-setup-guide` | Complete Streaming Setup for Small Churches (Under 200 Seats) | Small | Under $1k |
| `medium-church-av-setup-guide` | Multi-Camera AV Setup for Medium Churches (200–500 Seats) | Medium | $1k–$5k |
| `large-church-production-guide` | Professional Live Production for Large Churches (500+ Seats) | Large | $5k+ |
| `multi-campus-av-distribution` | AV Distribution Across Multiple Church Campuses | Multi-campus | $5k+ |
| `church-plant-streaming-guide` | Live Streaming on a Shoestring: The Church Plant Setup | Small | Under $500 |
| `budget-ptz-complete-system` | Building a Complete PTZ Camera System on a Budget | Any | Under $2k |
| `ndi-first-church-production` | Going NDI-First: Full IP Video Production for Churches | Medium-Large | $2k–$8k |
| `volunteer-proof-av-setup` | Building a Volunteer-Proof AV System for Your Church | Any | Any |
| `hybrid-church-in-person-online` | Hybrid Church Setup: Serving In-Person and Online Simultaneously | Medium | $2k–$5k |
| `sunday-morning-checklist` | The Complete Sunday Morning AV Checklist (Printable) | Any | Any |
| `church-av-disaster-recovery` | When It All Goes Wrong: AV Failure Recovery on Sunday Morning | Any | Any |
| `upgrading-church-av-step-by-step` | Upgrading Your Church AV System Step by Step Without Disruption | Any | Any |

---

## SECTION 7: Comparison Pages

**Route:** `/compare/[slug]`
**Why this matters:** "X vs Y church" queries are pure purchase-intent traffic. One of the highest-converting content types in any technical niche. These pages also rank fast because the keywords are specific.

### Comparisons to Generate

#### Camera Comparisons
- `avkans-vs-tenveo-church-ptz`
- `avkans-vs-tongveo-ndi-camera`
- `fomako-vs-avkans-ptz-church`
- `ptzoptics-vs-avkans-budget-church`
- `budget-ptz-vs-ptzoptics-value`

#### Switcher Comparisons
- `atem-mini-vs-atem-mini-pro-church`
- `atem-mini-pro-vs-roland-v1hd`
- `atem-mini-extreme-vs-atem-television-studio`
- `atem-mini-vs-vmix-software-switcher`
- `roland-v1hd-vs-kiloview-switcher`

#### Mixer Comparisons
- `behringer-x32-vs-allen-heath-sq5`
- `behringer-x-air-xr18-vs-mackie-dl32r`
- `yamaha-tf5-vs-behringer-x32-compact`
- `allen-heath-cq18t-vs-behringer-xr18`
- `analog-vs-digital-mixer-church`

#### Software Comparisons
- `obs-vs-vmix-church-streaming`
- `propresenter-vs-easyworship-church`
- `obs-vs-streamlabs-church`
- `restream-vs-castr-church`
- `wirecast-vs-vmix-church`

#### Encoder Comparisons
- `magewell-vs-teradek-vidiu-church`
- `hardware-encoder-vs-obs-pc-church`
- `kiloview-e1-vs-magewell-ultra-stream`
- `boxcaster-vs-magewell-church`

#### Cross-Category ("Best for" Comparisons)
- `best-ptz-camera-church-under-500`
- `best-ptz-camera-church-under-1000`
- `best-video-switcher-church-under-500`
- `best-digital-mixer-church-under-1000`
- `best-hardware-encoder-church-streaming`
- `best-church-streaming-setup-budget`

---

## SECTION 8: Budget Tier Guides

**Route:** `/budget/[tier]`
**Why this matters:** "church streaming setup $X budget" is a massive top-of-funnel query. These pages aggregate gear recommendations, link to every relevant product page, and are natural AdWords landing pages.

### Budget Pages to Generate

| Slug | Title | Target Query |
|---|---|---|
| `church-av-setup-under-500` | Church AV Setup Guide: Under $500 | "church live streaming setup cheap" |
| `church-av-setup-under-1000` | Church AV Setup Guide: Under $1,000 | "church streaming setup $1000" |
| `church-av-setup-under-2500` | Church AV Setup Guide: Under $2,500 | "small church av setup budget" |
| `church-av-setup-under-5000` | Church AV Setup Guide: Under $5,000 | "medium church av equipment list" |
| `church-av-setup-under-10000` | Church AV Setup Guide: Under $10,000 | "church production system $10k" |
| `church-av-upgrade-roadmap` | Church AV Upgrade Roadmap: What to Buy First | "how to upgrade church av system" |

---

## SECTION 9: Troubleshooting Hub

**Route:** `/troubleshooting/[slug]`
**Why this matters:** Problem-first queries ("why is my X doing Y") are the highest-intent searches on the entire site. These people are mid-crisis. Fastest to convert to Tech Manager because they've just experienced the exact pain point your product solves.

### Troubleshooting Articles to Generate

#### Video/Camera Issues
- `ptz-camera-not-connecting-network`
- `ndi-camera-not-showing-obs-vmix`
- `camera-image-flickering-church`
- `ptz-preset-not-recalling-correctly`
- `hdmi-signal-dropping-church-setup`
- `camera-lagging-behind-audio-stream`

#### Audio Issues
- `echo-feedback-church-live-stream`
- `audio-delay-video-stream-fix`
- `no-audio-on-youtube-facebook-stream`
- `mixer-usb-not-recognized-computer`
- `crackle-popping-audio-church-stream`
- `streaming-mix-too-loud-quiet`

#### Streaming Issues
- `stream-dropping-frames-church`
- `youtube-stream-offline-mid-service`
- `facebook-live-connection-failed-church`
- `stream-key-invalid-church-fix`
- `obs-black-screen-church-stream`
- `high-latency-stream-viewers-church`
- `multistream-one-platform-failing`

#### Network Issues
- `ndi-not-working-church-network`
- `ptz-camera-losing-ip-address`
- `streaming-pc-dropping-connection`
- `church-network-bandwidth-streaming`
- `vlan-setup-av-streaming-church`

#### Equipment-Specific Quick Fixes
- `atem-mini-not-detected-computer`
- `behringer-x32-usb-audio-not-working`
- `propresenter-ndi-output-not-visible`
- `avkans-camera-web-ui-not-loading`
- `magewell-encoder-not-streaming`

---

## Data Files to Create

### `src/data/brands.ts`
Brand metadata for all hardware categories: cameras, switchers, encoders, mixers.

```ts
export type BrandCategory = 'camera' | 'switcher' | 'encoder' | 'mixer' | 'software';

export interface Brand {
  slug: string;
  name: string;
  category: BrandCategory[];
  origin: 'chinese-budget' | 'western-pro' | 'western-budget';
  pricePosition: 'budget' | 'mid' | 'pro';
  churchMarketShare: 'dominant' | 'high' | 'medium' | 'niche';
  description: string;
  amazonSearchUrl?: string;
}
```

Populate for all brands across all sections above.

### `src/data/models.ts`
All device models with specs, price tier, and article cross-references. Used to generate related-model links automatically.

### `src/data/troubleshooting.ts`
Symptom-to-article mapping. Powers a "Describe your problem" search widget on `/troubleshooting`.

---

## New UI Components Required

| Component | Description |
|---|---|
| `DeviceCard.astro` | Like ArticleCard but for hardware — shows brand, model name, price tier badge, article count |
| `BrandHubPage.astro` | Template for `/cameras/avkans`, `/switchers/blackmagic`, etc. — brand header + article grid |
| `CategoryHubPage.astro` | Template for `/cameras`, `/switchers`, `/mixers` etc. — brand cards + featured articles |
| `WorkflowCard.astro` | Card for workflow guides — shows church size tag, budget tier, gear count |
| `ComparisonTable.astro` | Side-by-side spec table component — used in comparison articles |
| `TroubleshootingCard.astro` | Problem-first card — shows symptom as headline, urgency badge |
| `GearList.astro` | Inline gear list component — shows equipment used in a workflow with links to docs |
| `BudgetTierBadge.astro` | Visual badge: Under $500 / $500–$2.5k / $2.5k+ |
| `TroubleshootingWidget.astro` | Interactive "describe your problem" quick-search on the troubleshooting hub page |

---

## Internal Linking Strategy

This is critical for SEO. Every article must link to at least 3 other pages using these rules:

- **Device articles** → link to the hub page, 2 related models, 1 relevant workflow
- **Workflow articles** → link to every device mentioned (gear list component)
- **Comparison articles** → link to dedicated article pages for each product compared
- **Troubleshooting articles** → link to the relevant device setup guide + workflow
- **Budget guides** → link to every device recommended within that budget tier
- **Hub pages** → link to all brand pages under them

Build an `src/utils/relatedContent.ts` utility that accepts a collection entry and returns related articles using shared tags and modelId references.

---

## Product CTA Strategy by Page Type

| Page Type | CTA Message | CTA Placement |
|---|---|---|
| Camera setup guides | "Manage your [Brand] cameras remotely with Tech Manager" | 60% through article |
| Switcher docs | "Monitor your ATEM and cameras from one dashboard" | 60% through article |
| Mixer docs | "Track your entire AV stack — mixers, cameras, encoders — in Tech Manager" | 60% through article |
| Troubleshooting pages | "Stop troubleshooting blind — Tech Manager alerts you before Sunday" | TOP of article (high urgency) |
| Workflow guides | "Tech Manager is the layer that connects all of this gear" | Mid-article + bottom |
| Comparison pages | "Whichever you choose, Tech Manager manages both" | After verdict section |
| Budget guides | "Whatever your budget, Tech Manager grows with your setup" | Bottom of article |

**Troubleshooting pages get the CTA at the TOP** — these visitors are in crisis mode and that's exactly the emotional state where Tech Manager converts best.

---

## SEO Page Title Formulas

Follow these templates for `<title>` tags — they've been researched for click-through rates:

- Setup guides: `[Model Name] Setup Guide for Churches — [Year] | [Site Name]`
- Troubleshooting: `[Problem]: [Model] Fix for Churches | [Site Name]`
- Comparisons: `[Product A] vs [Product B] for Church [Category] ([Year]) | [Site Name]`
- Budget guides: `Best Church AV Setup Under $[X]: Complete [Year] Guide | [Site Name]`
- Workflows: `[Church Size] Church [Topic] Guide: Step-by-Step [Year] | [Site Name]`

---

## Astro Route Files Required

Beyond the existing routes from scope v1, add:

```
src/pages/
├── switchers/
│   ├── index.astro           (switcher hub)
│   └── [brand]/
│       └── [slug].astro
├── encoders/
│   ├── index.astro
│   └── [brand]/
│       └── [slug].astro
├── mixers/
│   ├── index.astro
│   └── [brand]/
│       └── [slug].astro
├── software/
│   ├── index.astro
│   └── [app]/
│       └── [slug].astro
├── workflows/
│   ├── index.astro
│   └── [slug].astro
├── compare/
│   ├── index.astro
│   └── [slug].astro
├── budget/
│   ├── index.astro
│   └── [size].astro
└── troubleshooting/
    ├── index.astro
    └── [slug].astro
```

---

## Estimated Page Count at Full Build

| Section | Articles | Hub/Index Pages | Total |
|---|---|---|---|
| General AV KB | 20 | 6 category pages | 26 |
| PTZ Cameras | 54 | 7 brand pages + 1 hub | 62 |
| Video Switchers | 40 | 4 brand pages + 1 hub | 45 |
| Hardware Encoders | 25 | 4 brand pages + 1 hub | 30 |
| Audio Mixers | 50 | 5 brand pages + 1 hub | 56 |
| Streaming Software | 30 | 5 app pages + 1 hub | 36 |
| Workflow Guides | 12 | 1 hub | 13 |
| Comparison Pages | 35 | 1 hub | 36 |
| Budget Tier Guides | 6 | 1 hub | 7 |
| Troubleshooting | 35 | 1 hub | 36 |
| **TOTAL** | **307** | **~40** | **~350** |

---

## Generation Priority Order

**Phase 1 — Highest traffic, fastest to rank (build first):**
1. All PTZ camera articles (AVKANS + Tenveo first)
2. ATEM Mini + ATEM Mini Pro full article set
3. Behringer X32 full article set
4. OBS Studio all 10 articles
5. Top 5 troubleshooting articles

**Phase 2 — Expand coverage:**
6. Roland V-1HD + remaining ATEM models
7. Allen & Heath SQ5 + Yamaha TF series
8. vMix + ProPresenter article sets
9. Magewell encoder articles
10. All comparison pages

**Phase 3 — Pillar pages + long tail:**
11. All 12 workflow guides
12. All 6 budget tier guides
13. Remaining camera brands (FoMaKo, SMTAV, OBSBOT)
14. Remaining troubleshooting articles
15. Remaining encoder and mixer brands

---

## Definition of Done — Full Build

- [ ] All 8 Astro content collections defined in `config.ts`
- [ ] All ~40 route files created and rendering
- [ ] All hub/index pages show correct article counts
- [ ] All brand pages list correct models and article sets
- [ ] All workflow guides reference correct gear with working internal links
- [ ] All comparison pages render spec tables with ComparisonTable component
- [ ] All troubleshooting pages show CTA at TOP of article
- [ ] Budget tier pages link to all recommended device pages
- [ ] Pagefind indexes all collections and returns results
- [ ] Sitemap includes all ~350 pages
- [ ] No broken internal links across any content type
- [ ] Product CTA copy is brand/model-specific (not generic placeholders) on device pages
- [ ] Lighthouse mobile ≥ 95 on home page
- [ ] `relatedContent.ts` utility wiring all collections together

---

*Scope version 2.0 — static build, no backend. ~350 total pages at full build.*
