"""Generate one inline diagram per conceptual/how-to article and embed it
after the first H2 in each .mdx body.

Scope: the 152 articles covered by batches 2-7.
Output: public/images/products/<slug>/inline.svg
Inject: ![<title>](/images/products/<slug>/inline.svg) after first H2.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from render_diagram import render  # noqa: E402

REPO = Path('/sessions/jolly-bold-darwin/mnt/worshipmetrics-marketing')
IMG_ROOT = REPO / 'public' / 'images' / 'products'
CONTENT_ROOT = REPO / 'src' / 'content'


# ---------------------------------------------------------------------------
# Slug -> subdir discovery
# ---------------------------------------------------------------------------

BUDGET_SLUGS = [
    'church-av-setup-under-500',
    'church-av-setup-under-1000',
    'church-av-setup-under-2500',
    'church-av-setup-under-5000',
    'church-av-setup-under-10000',
    'church-av-upgrade-roadmap',
]

WORKFLOW_SLUGS = [
    'budget-ptz-complete-system',
    'church-av-disaster-recovery',
    'church-plant-streaming-guide',
    'hybrid-church-in-person-online',
    'large-church-production-guide',
    'medium-church-av-setup-guide',
    'multi-campus-av-distribution',
    'ndi-first-church-production',
    'small-church-streaming-setup-guide',
    'sunday-morning-checklist',
    'upgrading-church-av-step-by-step',
    'volunteer-proof-av-setup',
]


def load_batch_entries():
    import importlib
    all_entries = {}
    for batch in [
        'specs_batch4_comparisons',
        'specs_batch5_troubleshooting',
        'specs_batch6_software',
        'specs_batch7_devices',
    ]:
        m = importlib.import_module(batch)
        for name, val in vars(m).items():
            if (
                isinstance(val, dict)
                and val
                and all(isinstance(v, dict) and 'spec' in v for v in val.values())
            ):
                all_entries.update(val)
                break
    return all_entries


# ---------------------------------------------------------------------------
# Inline spec builders -- one per category, complementing the cover
# ---------------------------------------------------------------------------


def budget_inline(slug: str) -> dict:
    """Budget articles get a signal_flow showing the typical streaming chain
    for that tier. Cover is hero_concept, inline is signal_flow -- different view.
    """
    tiers = {
        'church-av-setup-under-500': (
            'Under-$500 Streaming Chain',
            'Phone camera to the congregation',
            [
                {'label': 'Phone / USB cam', 'sub': '720p source'},
                {'label': 'Laptop',          'sub': 'OBS Studio'},
                {'label': 'YouTube Live',    'sub': 'free CDN'},
            ],
            [{'type': 'USB'}, {'type': 'RTMP'}],
        ),
        'church-av-setup-under-1000': (
            'Under-$1K Streaming Chain',
            'Single PTZ to live audience',
            [
                {'label': 'Tenveo VHD30U', 'sub': 'HDMI PTZ'},
                {'label': 'Capture card',  'sub': 'USB 3.0'},
                {'label': 'Laptop + OBS',  'sub': '1080p encode'},
                {'label': 'Streaming CDN', 'sub': 'YouTube / FB'},
            ],
            [{'type': 'HDMI'}, {'type': 'USB'}, {'type': 'RTMP'}],
        ),
        'church-av-setup-under-2500': (
            'Under-$2.5K Production Chain',
            'Two cameras through ATEM Mini',
            [
                {'label': 'Camera 1',     'sub': 'PTZ HDMI'},
                {'label': 'Camera 2',     'sub': 'PTZ HDMI'},
                {'label': 'ATEM Mini',    'sub': 'switcher'},
                {'label': 'OBS / YouTube','sub': 'encode + stream'},
            ],
            [{'type': 'HDMI'}, {'type': 'HDMI'}, {'type': 'USB'}],
        ),
        'church-av-setup-under-5000': (
            'Under-$5K Production Chain',
            'Three cameras + digital mixer to stream',
            [
                {'label': '3x PTZ',        'sub': 'HDMI'},
                {'label': 'ATEM Mini Pro', 'sub': 'ISO switcher'},
                {'label': 'XR18 Mixer',    'sub': 'audio embed'},
                {'label': 'Streaming PC',  'sub': 'OBS + record'},
                {'label': 'CDN',           'sub': 'RTMP'},
            ],
            [{'type': 'HDMI'}, {'type': 'Audio'}, {'type': 'USB'}, {'type': 'RTMP'}],
        ),
        'church-av-setup-under-10000': (
            'Under-$10K Production Chain',
            'NDI camera network with dedicated production PC',
            [
                {'label': '4x NDI PTZ',  'sub': 'gigabit'},
                {'label': 'PoE Switch',  'sub': 'VLAN'},
                {'label': 'vMix PC',     'sub': 'NDI inputs'},
                {'label': 'Recorder',    'sub': 'ISO + PGM'},
                {'label': 'CDN',         'sub': 'multi-bitrate'},
            ],
            [{'type': 'NDI'}, {'type': 'NDI'}, {'type': 'NDI'}, {'type': 'RTMP'}],
        ),
        'church-av-upgrade-roadmap': (
            'Typical Upgrade Path',
            'From phone camera to NDI production over 3 phases',
            [
                {'label': 'Phone + OBS',   'sub': 'phase 1'},
                {'label': '+ PTZ',         'sub': 'phase 2'},
                {'label': '+ Switcher',    'sub': 'phase 3'},
                {'label': 'NDI network',   'sub': 'phase 4'},
            ],
            [{'type': 'HDMI'}, {'type': 'HDMI'}, {'type': 'NDI'}],
        ),
    }
    title, subtitle, nodes, edges = tiers[slug]
    return {
        'type': 'signal_flow',
        'title': title,
        'subtitle': subtitle,
        'nodes': nodes,
        'edges': edges,
        'footer': 'Typical signal chain at this budget tier',
    }


def workflow_inline(slug: str) -> dict:
    """Workflow articles get a preset_workflow with 4 steps."""
    flows = {
        'budget-ptz-complete-system': ('Budget PTZ Build', 'Four steps from cart to streaming', [
            ('Pick PTZs', '2-3 HDMI cams'),
            ('Wire HDMI', 'to switcher'),
            ('Switcher',  'ATEM / OBS'),
            ('Go Live',   'RTMP out'),
        ]),
        'church-av-disaster-recovery': ('Recovery Plan', 'Four steps when the stream goes down', [
            ('Detect',   'monitor drops'),
            ('Failover', 'backup encoder'),
            ('Notify',   'team + viewers'),
            ('Restore',  'primary path'),
        ]),
        'church-plant-streaming-guide': ('Church Plant Streaming', 'From zero to first Sunday stream', [
            ('Plan',    'needs + budget'),
            ('Gear',    'phone / PTZ'),
            ('Rehearse','dry run'),
            ('Go Live', 'Sunday AM'),
        ]),
        'hybrid-church-in-person-online': ('Hybrid Service Flow', 'One production serving two audiences', [
            ('Capture',  'cams + audio'),
            ('Mix',      'IMAG + stream'),
            ('Distribute','FOH + CDN'),
            ('Engage',   'chat host'),
        ]),
        'large-church-production-guide': ('Large Church Workflow', 'Multi-camera production pipeline', [
            ('Ingest',  '4-6 NDI cams'),
            ('Switch',  'vMix / TriCaster'),
            ('Mix',     'audio desk'),
            ('Stream',  'multi-CDN'),
        ]),
        'medium-church-av-setup-guide': ('Medium Church Build', 'Four phases to a reliable production', [
            ('Cameras', '2-3 PTZ'),
            ('Switcher','ATEM / vMix'),
            ('Audio',   'digital mixer'),
            ('Stream',  'RTMP out'),
        ]),
        'multi-campus-av-distribution': ('Multi-Campus Distribution', 'One feed to many venues', [
            ('Main Campus','program'),
            ('Encode',     'SRT / NDI'),
            ('Distribute', 'WAN / CDN'),
            ('Play Out',   'each venue'),
        ]),
        'ndi-first-church-production': ('NDI-First Production', 'All IP, one network', [
            ('NDI Cams',  'gigabit'),
            ('Switch',    'PoE + VLAN'),
            ('vMix PC',   'NDI in/out'),
            ('Stream',    'NDI to RTMP'),
        ]),
        'small-church-streaming-setup-guide': ('Small Church Streaming', 'Four-step Sunday setup', [
            ('Camera',  'single PTZ'),
            ('Audio',   'mixer tap'),
            ('Encoder', 'OBS / ATEM'),
            ('Live',    'YouTube'),
        ]),
        'sunday-morning-checklist': ('Sunday Morning Runbook', 'Four phases before the count-in', [
            ('Power On', 'all gear'),
            ('Test AV',  'levels + focus'),
            ('Rehearse', 'countdown'),
            ('Go Live',  'stream start'),
        ]),
        'upgrading-church-av-step-by-step': ('Upgrade Sequence', 'Four-step incremental upgrade', [
            ('Audit',   'current gear'),
            ('Priority','biggest win'),
            ('Install', 'replace + test'),
            ('Train',   'volunteers'),
        ]),
        'volunteer-proof-av-setup': ('Volunteer-Proof Workflow', 'Setup built for non-technical teams', [
            ('Label',    'every cable'),
            ('Presets',  'one-button'),
            ('Checklist','printed'),
            ('Escalate', 'support path'),
        ]),
    }
    title, subtitle, steps = flows[slug]
    return {
        'type': 'preset_workflow',
        'title': title,
        'subtitle': subtitle,
        'steps': [{'label': lbl, 'sub': sub} for lbl, sub in steps],
        'footer': 'Core workflow for this article',
    }


def comparison_inline(slug: str, spec: dict) -> dict:
    """For comparison articles, the cover is already a comparison table.
    Inline gets a signal_flow showing the typical shared production chain
    so both options slot into the same context.
    """
    return {
        'type': 'signal_flow',
        'title': 'Where These Options Fit',
        'subtitle': 'Typical production chain both options plug into',
        'nodes': [
            {'label': 'Camera',    'sub': 'PTZ / DSLR'},
            {'label': 'Switcher',  'sub': 'compared'},
            {'label': 'Encoder',   'sub': 'OBS / vMix'},
            {'label': 'Stream',    'sub': 'CDN out'},
        ],
        'edges': [{'type': 'HDMI'}, {'type': 'USB'}, {'type': 'RTMP'}],
        'footer': 'Shared signal chain context',
    }


def troubleshoot_inline(slug: str, spec: dict) -> dict:
    """Troubleshoot articles: cover is preset_workflow (diag steps).
    Inline is a signal_flow showing where the fault usually happens.
    """
    return {
        'type': 'signal_flow',
        'title': 'Where to Look First',
        'subtitle': 'The link in the chain where this fault usually sits',
        'nodes': [
            {'label': 'Source',    'sub': 'camera / mic'},
            {'label': 'Transport', 'sub': 'cable / network'},
            {'label': 'Processor', 'sub': 'switcher / mixer'},
            {'label': 'Output',    'sub': 'screen / stream'},
        ],
        'edges': [{'type': 'HDMI'}, {'type': 'NDI'}, {'type': 'RTMP'}],
        'footer': 'Diagnostic signal chain',
    }


def software_inline(slug: str, spec: dict) -> dict:
    """Software articles: cover is often a stack. Inline is a signal_flow
    showing the app in a live production."""
    return {
        'type': 'signal_flow',
        'title': 'In a Live Production',
        'subtitle': 'How the app sits in the Sunday-morning signal chain',
        'nodes': [
            {'label': 'Cameras',  'sub': 'HDMI / NDI'},
            {'label': 'This App', 'sub': 'switch / mix'},
            {'label': 'Encoder',  'sub': 'RTMP / SRT'},
            {'label': 'Audience', 'sub': 'in-room + online'},
        ],
        'edges': [{'type': 'HDMI'}, {'type': 'USB'}, {'type': 'RTMP'}],
        'footer': 'Production pipeline placement',
    }


def device_inline(slug: str, spec: dict) -> dict:
    """Device articles: cover is often signal_flow or preset_workflow.
    Inline is a small network_topology showing the device in a church zone.
    """
    return {
        'type': 'network_topology',
        'title': 'Typical Church Deployment',
        'subtitle': 'Where this device sits in a production environment',
        'zones': [
            {'x': 80,  'y': 260, 'w': 620, 'h': 560, 'label': 'Sanctuary'},
            {'x': 880, 'y': 260, 'w': 640, 'h': 560, 'label': 'Production Booth'},
        ],
        'devices': [
            {'id': 'src1', 'x': 180, 'y': 400, 'label': 'Source 1', 'sub': 'camera / mic'},
            {'id': 'src2', 'x': 180, 'y': 600, 'label': 'Source 2', 'sub': 'camera / mic'},
            {'id': 'dev',  'x': 460, 'y': 500, 'label': 'This Device', 'sub': 'under review'},
            {'id': 'pc',   'x': 980, 'y': 400, 'label': 'Stream PC', 'sub': 'OBS / vMix'},
            {'id': 'cdn',  'x': 980, 'y': 600, 'label': 'CDN',       'sub': 'RTMP out'},
        ],
        'edges': [
            {'from': 'src1', 'to': 'dev', 'type': 'HDMI'},
            {'from': 'src2', 'to': 'dev', 'type': 'HDMI'},
            {'from': 'dev',  'to': 'pc',  'type': 'NDI'},
            {'from': 'pc',   'to': 'cdn', 'type': 'RTMP'},
        ],
        'footer': 'Device in a typical church topology',
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

INLINE_MARK = '<!-- inline-diagram -->'


def inject_after_first_h2(src: str, slug: str, alt: str) -> str:
    if INLINE_MARK in src:
        return src  # already injected

    # Split off frontmatter so we search only the body
    parts = src.split('---', 2)
    if len(parts) < 3:
        return src
    head = '---' + parts[1] + '---'
    body = parts[2]

    img_md = (
        f'\n{INLINE_MARK}\n'
        f'<figure class="kb-figure">\n'
        f'  <img src="/images/products/{slug}/inline.svg" alt="{alt}" '
        f'loading="lazy" class="kb-inline-diagram" />\n'
        f'</figure>\n'
    )

    # Find first H2 and the next H2 (or end of body)
    h2_pattern = re.compile(r'^## .+$', re.MULTILINE)
    matches = list(h2_pattern.finditer(body))
    if not matches:
        return src

    first = matches[0]
    # Insert after the first paragraph following the first H2
    # Find the next H2 (or end)
    next_start = matches[1].start() if len(matches) > 1 else len(body)

    # Insert right before next_start (end of first section)
    new_body = body[:next_start] + img_md + '\n' + body[next_start:]
    return head + new_body


def run():
    entries: dict[str, dict] = {}

    # Budget
    for slug in BUDGET_SLUGS:
        entries[slug] = {'subdir': 'budget', 'spec': budget_inline(slug)}

    # Workflows
    for slug in WORKFLOW_SLUGS:
        entries[slug] = {'subdir': 'workflows', 'spec': workflow_inline(slug)}

    # Batches 4-7
    batch_data = load_batch_entries()
    import importlib

    def subdir_for(slug: str, cover_spec_type: str) -> str:
        # Walk src/content to find which subdir contains this slug
        for p in CONTENT_ROOT.rglob(f'{slug}.mdx'):
            rel = p.relative_to(CONTENT_ROOT)
            return str(rel.parent)
        return ''

    # Figure out which batch each slug came from so we pick the right builder
    modmap = {}
    for batch in [
        'specs_batch4_comparisons',
        'specs_batch5_troubleshooting',
        'specs_batch6_software',
        'specs_batch7_devices',
    ]:
        m = importlib.import_module(batch)
        for name, val in vars(m).items():
            if (
                isinstance(val, dict) and val
                and all(isinstance(v, dict) and 'spec' in v for v in val.values())
            ):
                for slug in val:
                    modmap[slug] = batch
                break

    builder_for_batch = {
        'specs_batch4_comparisons': comparison_inline,
        'specs_batch5_troubleshooting': troubleshoot_inline,
        'specs_batch6_software': software_inline,
        'specs_batch7_devices': device_inline,
    }

    for slug, info in batch_data.items():
        batch = modmap[slug]
        builder = builder_for_batch[batch]
        entries[slug] = {
            'subdir': subdir_for(slug, info['spec'].get('type', '')),
            'spec': builder(slug, info['spec']),
        }

    # Render + inject
    ok = 0
    missing = 0
    already = 0
    bad = 0
    for slug, info in entries.items():
        spec = info['spec']
        subdir = info['subdir']
        out = IMG_ROOT / slug / 'inline.svg'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(spec))

        mdx_path = CONTENT_ROOT / subdir / f'{slug}.mdx'
        if not mdx_path.exists():
            # fallback search
            hits = list(CONTENT_ROOT.rglob(f'{slug}.mdx'))
            if not hits:
                print(f'!! missing mdx: {slug}')
                missing += 1
                continue
            mdx_path = hits[0]

        src = mdx_path.read_text()
        if INLINE_MARK in src:
            already += 1
            continue

        title_m = re.search(r'^title:\s*"?([^"\n]+)"?', src, re.MULTILINE)
        alt = (title_m.group(1).strip() if title_m else slug).replace('"', '')
        new_src = inject_after_first_h2(src, slug, f'{alt} — inline diagram')
        if new_src == src:
            print(f'?? no h2 found: {slug}')
            bad += 1
            continue
        mdx_path.write_text(new_src)
        ok += 1

    print(f'done: ok={ok} already={already} missing={missing} no_h2={bad} total={len(entries)}')


if __name__ == '__main__':
    run()
