"""Batch 3 — workflow guides (12 articles)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from render_diagram import render  # noqa: E402

ROOT = Path('/sessions/jolly-bold-darwin/mnt/worshipmetrics-marketing/public/images/products')

SPECS = {
    'budget-ptz-complete-system': {
        'type': 'signal_flow',
        'title': 'Budget PTZ System End-to-End',
        'subtitle': 'Camera to stream on a $1,500 budget',
        'nodes': [
            {'label': 'PTZ Camera', 'sub': 'Tenveo / AVKANS'},
            {'label': 'Capture',    'sub': 'USB or HDMI'},
            {'label': 'OBS PC',     'sub': 'scenes + audio'},
            {'label': 'CDN',        'sub': 'RTMP out'},
        ],
        'edges': [
            {'type': 'USB'},
            {'type': 'HDMI'},
            {'type': 'RTMP'},
        ],
        'footer': 'Complete budget PTZ production chain',
    },
    'church-av-disaster-recovery': {
        'type': 'preset_workflow',
        'title': 'Sunday AV Failure Recovery',
        'subtitle': 'What to do when it all goes wrong mid-service',
        'steps': [
            {'label': 'Identify',  'sub': 'audio / video / stream'},
            {'label': 'Isolate',   'sub': 'failing component'},
            {'label': 'Fallback',  'sub': 'backup path'},
            {'label': 'Recover',   'sub': 'restore primary'},
        ],
        'footer': 'Four-step failure recovery workflow',
    },
    'church-plant-streaming-guide': {
        'type': 'hero_concept',
        'title': 'Church Plant Streaming',
        'subtitle': 'The shoestring setup that actually works',
        'tag': 'Plant Guide',
        'stat': '4',
        'stat_label': 'core pieces',
        'bullets': [
            'Phone or Tenveo USB camera',
            'Small USB mixer + dynamic mic',
            'OBS on a laptop',
            'Wired 10 Mbps upload',
        ],
        'footer': 'Minimum viable streaming for new church plants',
    },
    'hybrid-church-in-person-online': {
        'type': 'signal_flow',
        'title': 'Hybrid Church Signal Flow',
        'subtitle': 'Serve the room and the stream simultaneously',
        'nodes': [
            {'label': 'Sources',    'sub': 'cams + mics'},
            {'label': 'Mixer',      'sub': 'split FOH / bcast'},
            {'label': 'Switcher',   'sub': 'ATEM / vMix'},
            {'label': 'In-Room',    'sub': 'screens + PA'},
            {'label': 'Online',     'sub': 'stream out'},
        ],
        'edges': [
            {'type': 'Audio'},
            {'type': 'SDI'},
            {'type': 'HDMI'},
            {'type': 'RTMP'},
        ],
        'footer': 'Simultaneous in-person and online production',
    },
    'large-church-production-guide': {
        'type': 'network_topology',
        'title': 'Large Church Production Topology',
        'subtitle': '500+ seats with multi-cam NDI and redundancy',
        'zones': [
            {'x': 80,  'y': 260, 'w': 620, 'h': 560, 'label': 'Sanctuary'},
            {'x': 880, 'y': 260, 'w': 640, 'h': 560, 'label': 'Control Room'},
        ],
        'devices': [
            {'id': 'c1', 'x': 130, 'y': 330, 'label': 'Cam 1', 'sub': 'FOH wide'},
            {'id': 'c2', 'x': 130, 'y': 440, 'label': 'Cam 2', 'sub': 'Pastor'},
            {'id': 'c3', 'x': 130, 'y': 550, 'label': 'Cam 3', 'sub': 'Worship'},
            {'id': 'c4', 'x': 130, 'y': 660, 'label': 'Cam 4', 'sub': 'Audience'},
            {'id': 'sw', 'x': 430, 'y': 490, 'label': 'Core Switch', 'sub': '10G + PoE'},
            {'id': 'vm', 'x': 940, 'y': 340, 'label': 'vMix Pro',  'sub': 'ISO record'},
            {'id': 'au', 'x': 940, 'y': 470, 'label': 'SQ-6',      'sub': 'bcast mix'},
            {'id': 'en', 'x': 940, 'y': 600, 'label': 'Encoder',   'sub': 'dual CDN'},
        ],
        'edges': [
            {'from': 'c1', 'to': 'sw', 'type': 'NDI'},
            {'from': 'c2', 'to': 'sw', 'type': 'NDI'},
            {'from': 'c3', 'to': 'sw', 'type': 'NDI'},
            {'from': 'c4', 'to': 'sw', 'type': 'NDI'},
            {'from': 'sw', 'to': 'vm', 'type': 'NDI'},
            {'from': 'sw', 'to': 'au', 'type': 'Audio'},
            {'from': 'vm', 'to': 'en', 'type': 'RTMP'},
        ],
    },
    'medium-church-av-setup-guide': {
        'type': 'signal_flow',
        'title': 'Medium Church AV Chain',
        'subtitle': '200-500 seats with multi-cam production',
        'nodes': [
            {'label': '3 PTZs',    'sub': 'NDI or HDMI'},
            {'label': 'Switcher',  'sub': 'ATEM Extreme'},
            {'label': 'Encoder',   'sub': 'vMix / Pearl'},
            {'label': 'Stream',    'sub': 'YouTube + FB'},
        ],
        'edges': [
            {'type': 'NDI'},
            {'type': 'HDMI'},
            {'type': 'RTMP'},
        ],
        'footer': 'Production chain for medium sanctuaries',
    },
    'multi-campus-av-distribution': {
        'type': 'network_topology',
        'title': 'Multi-Campus AV Distribution',
        'subtitle': 'One service, multiple sanctuaries',
        'zones': [
            {'x': 80,  'y': 260, 'w': 620, 'h': 560, 'label': 'Main Campus'},
            {'x': 880, 'y': 260, 'w': 640, 'h': 560, 'label': 'Satellite Campuses'},
        ],
        'devices': [
            {'id': 'src', 'x': 150, 'y': 420, 'label': 'Source Feed', 'sub': 'PGM + audio'},
            {'id': 'enc', 'x': 430, 'y': 420, 'label': 'Encoder',     'sub': 'SRT out'},
            {'id': 'cdn', 'x': 940, 'y': 330, 'label': 'Internet',    'sub': 'SRT / RTMP'},
            {'id': 'b',   'x': 940, 'y': 460, 'label': 'Campus B',    'sub': 'decoder + PA'},
            {'id': 'c',   'x': 940, 'y': 590, 'label': 'Campus C',    'sub': 'decoder + PA'},
        ],
        'edges': [
            {'from': 'src', 'to': 'enc', 'type': 'SDI'},
            {'from': 'enc', 'to': 'cdn', 'type': 'Ethernet'},
            {'from': 'cdn', 'to': 'b',   'type': 'RTMP'},
            {'from': 'cdn', 'to': 'c',   'type': 'RTMP'},
        ],
    },
    'ndi-first-church-production': {
        'type': 'network_topology',
        'title': 'NDI-First Church Production',
        'subtitle': 'Full IP video — no SDI, no HDMI runs',
        'zones': [
            {'x': 80,  'y': 260, 'w': 620, 'h': 560, 'label': 'Sanctuary'},
            {'x': 880, 'y': 260, 'w': 640, 'h': 560, 'label': 'Production'},
        ],
        'devices': [
            {'id': 'c1', 'x': 130, 'y': 360, 'label': 'NDI Cam 1', 'sub': 'wide'},
            {'id': 'c2', 'x': 130, 'y': 490, 'label': 'NDI Cam 2', 'sub': 'tight'},
            {'id': 'c3', 'x': 130, 'y': 620, 'label': 'NDI Cam 3', 'sub': 'worship'},
            {'id': 'sw', 'x': 430, 'y': 490, 'label': 'PoE Switch', 'sub': '10G uplink'},
            {'id': 'vm', 'x': 940, 'y': 360, 'label': 'vMix',      'sub': 'NDI inputs'},
            {'id': 'mx', 'x': 940, 'y': 490, 'label': 'NDI Matrix','sub': 'routing'},
            {'id': 'cd', 'x': 940, 'y': 620, 'label': 'CDN',       'sub': 'RTMP out'},
        ],
        'edges': [
            {'from': 'c1', 'to': 'sw', 'type': 'PoE'},
            {'from': 'c2', 'to': 'sw', 'type': 'PoE'},
            {'from': 'c3', 'to': 'sw', 'type': 'PoE'},
            {'from': 'sw', 'to': 'vm', 'type': 'NDI'},
            {'from': 'sw', 'to': 'mx', 'type': 'NDI'},
            {'from': 'vm', 'to': 'cd', 'type': 'RTMP'},
        ],
    },
    'small-church-streaming-setup-guide': {
        'type': 'signal_flow',
        'title': 'Small Church Streaming Setup',
        'subtitle': 'Under 200 seats — single-camera production',
        'nodes': [
            {'label': 'PTZ Cam',   'sub': 'Tenveo'},
            {'label': 'Mixer',     'sub': 'USB audio'},
            {'label': 'OBS PC',    'sub': 'scene + audio'},
            {'label': 'YouTube',   'sub': 'RTMP ingest'},
        ],
        'edges': [
            {'type': 'USB'},
            {'type': 'USB'},
            {'type': 'RTMP'},
        ],
        'footer': 'Single-cam setup for small sanctuaries',
    },
    'sunday-morning-checklist': {
        'type': 'preset_workflow',
        'title': 'Sunday Morning AV Checklist',
        'subtitle': 'Four-stage pre-service sequence',
        'steps': [
            {'label': '60 min',  'sub': 'power + boot'},
            {'label': '30 min',  'sub': 'levels + presets'},
            {'label': '15 min',  'sub': 'stream test'},
            {'label': 'Go',      'sub': 'start record'},
        ],
        'footer': 'Pre-service checklist for worship AV',
    },
    'upgrading-church-av-step-by-step': {
        'type': 'preset_workflow',
        'title': 'AV Upgrade Without Disruption',
        'subtitle': 'Swap gear without taking Sunday down',
        'steps': [
            {'label': 'Audit',     'sub': 'document current'},
            {'label': 'Parallel',  'sub': 'install new alongside'},
            {'label': 'Cutover',   'sub': 'weeknight swap'},
            {'label': 'Verify',    'sub': 'test + keep spare'},
        ],
        'footer': 'Zero-downtime AV upgrade workflow',
    },
    'volunteer-proof-av-setup': {
        'type': 'preset_workflow',
        'title': 'Volunteer-Proof AV Setup',
        'subtitle': 'Design so anyone can run Sunday service',
        'steps': [
            {'label': 'Label',     'sub': 'every cable + port'},
            {'label': 'Preset',    'sub': 'scenes + scenes'},
            {'label': 'Document',  'sub': 'one-page runbook'},
            {'label': 'Train',     'sub': 'shadow + solo'},
        ],
        'footer': 'Four principles for volunteer-resilient AV',
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
