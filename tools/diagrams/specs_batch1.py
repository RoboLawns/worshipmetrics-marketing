"""
Batch 1 diagram specs (articles 1-10).

Using the typed-connection color system introduced after the first pass:
  - Each edge declares `type: 'NDI' | 'HDMI' | 'USB' | 'RTSP' | 'RTMP' | ...`
  - The renderer colors the arrow accordingly and auto-adds a legend.
  - No inline edge labels — they overlap node labels.

Run: python3 specs_batch1.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from render_diagram import render  # noqa: E402

ROOT = Path('/sessions/jolly-bold-darwin/mnt/worshipmetrics-marketing/public/images/products')

SPECS = {
    # 1. AVKANS vs Tenveo comparison — comparison type, no edges so no legend
    'avkans-vs-tenveo-church-ptz-comparison': {
        'type': 'comparison',
        'title': 'AVKANS vs Tenveo PTZ Cameras',
        'subtitle': 'Church production comparison — network-first vs plug-and-play',
        'rows': ['Primary Output', 'Zoom', 'Native NDI', 'PoE Option', 'Best Switcher', 'Starting Price'],
        'columns': [
            {
                'label': 'AVKANS PTZ-U100',
                'values': [
                    {'text': 'NDI + HDMI'},
                    {'text': '20x optical'},
                    {'text': 'Yes', 'good': True},
                    {'text': 'U200 only', 'good': False},
                    {'text': 'OBS / vMix'},
                    {'text': '~$400'},
                ],
            },
            {
                'label': 'Tenveo VHD20U',
                'values': [
                    {'text': 'HDMI + USB'},
                    {'text': '20x optical'},
                    {'text': 'No (TEVO-NDI only)', 'good': False},
                    {'text': 'No', 'good': False},
                    {'text': 'ATEM / Roland'},
                    {'text': '~$300'},
                ],
            },
        ],
        'footer': 'AVKANS vs Tenveo — pick by switcher, not by spec sheet',
    },

    # 2. Budget PTZ cameras buyer guide — hero concept, no edges
    'budget-ptz-cameras-church-under-500': {
        'type': 'hero_concept',
        'title': 'Best Budget PTZ Cameras Under $500',
        'subtitle': 'Four cameras that cover every church workflow',
        'tag': 'Buyer Guide',
        'stat': '4',
        'stat_label': 'cameras reviewed',
        'bullets': [
            'AVKANS U100 — NDI, 20x, ~$400',
            'Tenveo VHD30U — USB+HDMI, 30x, ~$350',
            'Tenveo VHD20U — HDMI, 20x, ~$300',
            'AVKANS U200 — NDI + PoE, 20x, ~$500',
        ],
        'footer': 'Budget PTZ picks for church streaming',
    },

    # 3. UV510A HDMI connection — HDMI signal chain
    'minrray-uv510a-hdmi-connection': {
        'type': 'signal_flow',
        'title': 'Minrray UV510A HDMI to Switcher',
        'subtitle': '1080p59.94 straight to ATEM or capture card',
        'nodes': [
            {'label': 'UV510A',       'sub': '1080p59.94'},
            {'label': 'HDMI cable',   'sub': 'high-speed'},
            {'label': 'ATEM / vMix',  'sub': 'HDMI in'},
            {'label': 'Program out',  'sub': 'stream / record'},
        ],
        'edges': [
            {'type': 'HDMI'},
            {'type': 'HDMI'},
            {'type': 'RTMP'},
        ],
        'footer': 'Minrray UV510A HDMI signal chain',
    },

    # 4. UV510A IP streaming — RTSP over LAN, then RTMP out
    'minrray-uv510a-ip-streaming': {
        'type': 'signal_flow',
        'title': 'Minrray UV510A RTSP Over IP',
        'subtitle': 'Network video to OBS or vMix over CAT6',
        'nodes': [
            {'label': 'UV510A',        'sub': '192.168.1.100'},
            {'label': 'Gigabit Switch','sub': 'same subnet'},
            {'label': 'OBS / vMix PC', 'sub': 'RTSP source'},
            {'label': 'CDN',           'sub': 'live stream'},
        ],
        'edges': [
            {'type': 'RTSP'},
            {'type': 'Ethernet'},
            {'type': 'RTMP'},
        ],
        'footer': 'RTSP streaming over LAN — no HDMI run needed',
    },

    # 5. UV510A setup — preset workflow, no edges
    'minrray-uv510a-setup-guide': {
        'type': 'preset_workflow',
        'title': 'Minrray UV510A First-Time Setup',
        'subtitle': 'From unboxing to first live shot in four steps',
        'steps': [
            {'label': 'Power Up',   'sub': '15-20s boot'},
            {'label': 'Network',    'sub': 'CAT6 + DHCP'},
            {'label': 'Web Login',  'sub': 'admin / admin'},
            {'label': 'Test Shot',  'sub': 'HDMI or RTSP'},
        ],
        'footer': 'UV510A initial configuration workflow',
    },

    # 6. UV510A web management — stack, no edges
    'minrray-uv510a-web-management': {
        'type': 'stack',
        'title': 'Minrray UV510A Web Interface',
        'subtitle': 'Five configuration sections inside the browser UI',
        'layers': [
            {'label': 'System',       'sub': 'firmware, time, reboot'},
            {'label': 'Network',      'sub': 'DHCP / static IP / DNS'},
            {'label': 'Video Output', 'sub': '1080p59.94, HDMI / RTSP'},
            {'label': 'PTZ Control',  'sub': 'pan, tilt, zoom, speed'},
            {'label': 'Presets',      'sub': 'save / recall up to 255'},
        ],
        'footer': 'UV510A browser management layout',
    },

    # 7. UV570A church production — multi-cam NDI topology
    'minrray-uv570a-church-production': {
        'type': 'network_topology',
        'title': 'UV570A in a Full Church Production',
        'subtitle': 'Three-camera NDI workflow with switcher and stream out',
        'zones': [
            {'x': 80,  'y': 260, 'w': 620, 'h': 560, 'label': 'Sanctuary'},
            {'x': 880, 'y': 260, 'w': 640, 'h': 560, 'label': 'Production Booth'},
        ],
        'devices': [
            {'id': 'c1', 'x': 130, 'y': 340, 'label': 'UV570A 1', 'sub': 'FOH wide'},
            {'id': 'c2', 'x': 130, 'y': 470, 'label': 'UV570A 2', 'sub': 'Pulpit tight'},
            {'id': 'c3', 'x': 130, 'y': 600, 'label': 'UV570A 3', 'sub': 'Worship wide'},
            {'id': 'sw', 'x': 430, 'y': 470, 'label': 'PoE Switch', 'sub': 'gigabit'},
            {'id': 'pc', 'x': 940, 'y': 340, 'label': 'vMix PC', 'sub': 'NDI sources'},
            {'id': 'rec','x': 940, 'y': 470, 'label': 'Recorder', 'sub': 'ISO + PGM'},
            {'id': 'cdn','x': 940, 'y': 600, 'label': 'CDN', 'sub': 'RTMP out'},
        ],
        'edges': [
            {'from': 'c1', 'to': 'sw', 'type': 'PoE'},
            {'from': 'c2', 'to': 'sw', 'type': 'PoE'},
            {'from': 'c3', 'to': 'sw', 'type': 'PoE'},
            {'from': 'sw', 'to': 'pc', 'type': 'NDI'},
            {'from': 'pc', 'to': 'rec','type': 'NDI'},
            {'from': 'pc', 'to': 'cdn','type': 'RTMP'},
        ],
    },

    # 8. UV570A controller setup — VISCA control path
    'minrray-uv570a-controller-setup': {
        'type': 'signal_flow',
        'title': 'UV570A Controller & Joystick Setup',
        'subtitle': 'VISCA control from a hardware joystick to the camera',
        'nodes': [
            {'label': 'PTZ Joystick',   'sub': 'hardware'},
            {'label': 'Controller Box', 'sub': 'RS-422 / IP'},
            {'label': 'Network / Serial','sub': 'VISCA over IP'},
            {'label': 'UV570A',         'sub': 'pan / tilt / zoom'},
        ],
        'edges': [
            {'type': 'USB'},
            {'type': 'VISCA'},
            {'type': 'VISCA'},
        ],
        'footer': 'Professional PTZ control over VISCA',
    },

    # 9. UV570A NDI configuration — pure NDI chain
    'minrray-uv570a-ndi-configuration': {
        'type': 'signal_flow',
        'title': 'UV570A NDI Configuration',
        'subtitle': 'Cable-free video over the church network',
        'nodes': [
            {'label': 'UV570A',        'sub': 'NDI source'},
            {'label': 'Gigabit Switch','sub': 'same subnet'},
            {'label': 'OBS / vMix',    'sub': 'NDI input'},
            {'label': 'Program out',   'sub': 'stream'},
        ],
        'edges': [
            {'type': 'NDI'},
            {'type': 'NDI'},
            {'type': 'RTMP'},
        ],
    },

    # 10. UV570A setup — preset workflow
    'minrray-uv570a-setup-guide': {
        'type': 'preset_workflow',
        'title': 'UV570A First-Time Setup',
        'subtitle': '30x NDI camera ready in four steps',
        'steps': [
            {'label': 'Unbox + Mount',   'sub': 'ceiling / wall'},
            {'label': 'Power & Network', 'sub': 'PoE+ or DC'},
            {'label': 'Web UI Login',    'sub': 'change default pwd'},
            {'label': 'NDI Verify',      'sub': 'discover in OBS'},
        ],
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
