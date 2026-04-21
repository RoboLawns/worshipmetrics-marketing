"""Batch 2 — budget tier guides (6 articles)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from render_diagram import render  # noqa: E402

ROOT = Path('/sessions/jolly-bold-darwin/mnt/worshipmetrics-marketing/public/images/products')

SPECS = {
    'church-av-setup-under-500': {
        'type': 'hero_concept',
        'title': 'Church AV Under $500',
        'subtitle': 'One camera, one mic, one stream — it works',
        'tag': 'Budget Tier',
        'stat': '$500',
        'stat_label': 'total budget',
        'bullets': [
            'Smartphone or Tenveo VHD30U camera',
            '4-channel USB mixer + dynamic mic',
            'OBS on existing PC',
            'Wired internet (5 Mbps up minimum)',
        ],
        'footer': 'Starter streaming build for small churches',
    },
    'church-av-setup-under-1000': {
        'type': 'hero_concept',
        'title': 'Church AV Under $1,000',
        'subtitle': '1080p streaming with real production audio',
        'tag': 'Budget Tier',
        'stat': '$1K',
        'stat_label': 'total budget',
        'bullets': [
            'Tenveo VHD20U or VHD30U PTZ',
            'Behringer XR12 digital mixer',
            'Magewell USB Capture + streaming PC',
            'Two wireless or wired mics',
        ],
        'footer': 'Single-camera 1080p production',
    },
    'church-av-setup-under-2500': {
        'type': 'hero_concept',
        'title': 'Church AV Under $2,500',
        'subtitle': 'Two cameras, real switcher, clean audio',
        'tag': 'Budget Tier',
        'stat': '$2.5K',
        'stat_label': 'total budget',
        'bullets': [
            'Two AVKANS or Tenveo PTZ cameras',
            'ATEM Mini Pro switcher',
            'Behringer XR18 or X32 Rack',
            'Dedicated streaming PC + wireless mics',
        ],
        'footer': 'Multi-cam production for growing churches',
    },
    'church-av-setup-under-5000': {
        'type': 'hero_concept',
        'title': 'Church AV Under $5,000',
        'subtitle': 'Three cameras, NDI workflow, broadcast-ready',
        'tag': 'Budget Tier',
        'stat': '$5K',
        'stat_label': 'total budget',
        'bullets': [
            'Three NDI PTZ cameras + PoE switch',
            'vMix or ATEM Mini Extreme ISO',
            'Allen & Heath SQ-5 or X32 Compact',
            'Dedicated encoder + streaming rig',
        ],
        'footer': 'Full multi-cam NDI production',
    },
    'church-av-setup-under-10000': {
        'type': 'hero_concept',
        'title': 'Church AV Under $10,000',
        'subtitle': 'Broadcast-grade multi-cam with redundancy',
        'tag': 'Budget Tier',
        'stat': '$10K',
        'stat_label': 'total budget',
        'bullets': [
            'Four 30x NDI cameras + redundant PoE',
            'vMix Pro or ATEM TV Studio HD',
            'Allen & Heath SQ-6 or X32 full',
            'Dual encoders + backup streaming path',
        ],
        'footer': 'Premium church production build',
    },
    'church-av-upgrade-roadmap': {
        'type': 'preset_workflow',
        'title': 'Church AV Upgrade Roadmap',
        'subtitle': 'What to buy first, second, and third',
        'steps': [
            {'label': 'Year 1', 'sub': 'Audio + internet'},
            {'label': 'Year 2', 'sub': 'PTZ + switcher'},
            {'label': 'Year 3', 'sub': 'Third camera'},
            {'label': 'Year 4', 'sub': 'Graphics + ISO'},
        ],
        'footer': 'Phased upgrade priorities for church AV',
    },
}


def main() -> None:
    for slug, spec in SPECS.items():
        out = ROOT / slug / 'cover.svg'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(spec))
        print(f'wrote {slug}')


if __name__ == '__main__':
    main()
