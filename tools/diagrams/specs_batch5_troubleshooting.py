"""Batch 5 — troubleshooting (33 articles). All preset_workflow diagnostics."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from _batch_helper import run  # noqa: E402


def diag(title, subtitle, steps, footer=''):
    return {
        'type': 'preset_workflow',
        'title': title,
        'subtitle': subtitle,
        'steps': [{'label': s[0], 'sub': s[1]} for s in steps],
        **({'footer': footer} if footer else {}),
    }


SUB = 'troubleshooting'


ENTRIES = {
    'atem-mini-not-detected-computer': {'subdir': SUB, 'spec': diag(
        'ATEM Mini Not Detected', 'Computer can\'t find the switcher',
        [('USB cable', 'swap + data-rate'), ('Drivers', 'ATEM SW install'),
         ('Firmware', 'update via USB'), ('Port', 'try another USB')],
    )},
    'atem-mini-usb-webcam-not-recognized': {'subdir': SUB, 'spec': diag(
        'ATEM Mini USB Webcam Fix', 'Windows/Mac won\'t see ATEM as camera',
        [('Mode', 'set to webcam out'), ('Drivers', 'update ATEM SW'),
         ('Port', 'avoid hubs'), ('App', 'restart OBS / Zoom')],
    )},
    'audio-delay-video-stream-fix': {'subdir': SUB, 'spec': diag(
        'A/V Sync Fix', 'Realign lip-sync on the live stream',
        [('Measure', 'clap test'), ('Adjust', 'OBS offset ms'),
         ('Mixer', 'delay on ch'), ('Verify', 'preview + record')],
    )},
    'avkans-camera-web-ui-not-loading': {'subdir': SUB, 'spec': diag(
        'AVKANS Web UI Fix', 'Browser can\'t reach the camera',
        [('IP check', 'ping camera'), ('Subnet', 'match PC'),
         ('Browser', 'try Chrome/Edge'), ('Reset', 'factory if needed')],
    )},
    'behringer-x32-usb-audio-not-working': {'subdir': SUB, 'spec': diag(
        'X32 USB Audio Fix', 'OBS / DAW not seeing X32 channels',
        [('Driver', 'X32 USB install'), ('Routing', 'setup USB out'),
         ('App audio', 'select X32'), ('Sample rate', '48kHz match')],
    )},
    'camera-image-flickering-church': {'subdir': SUB, 'spec': diag(
        'Camera Flicker Fix', 'Stuttering or strobing image',
        [('Shutter', 'match AC hz'), ('Frame rate', '30 or 60'),
         ('Lights', 'LED compat'), ('Bandwidth', 'network test')],
    )},
    'camera-lagging-behind-audio-stream': {'subdir': SUB, 'spec': diag(
        'Video Lag Fix', 'Video arrives late vs audio',
        [('Encoder', 'reduce buffer'), ('CPU', 'check load'),
         ('Network', 'upload test'), ('Preset', 'lower output')],
    )},
    'church-network-bandwidth-streaming': {'subdir': SUB, 'spec': diag(
        'Church Streaming Bandwidth', 'How much upload you actually need',
        [('1080p30', '6 Mbps up'), ('1080p60', '9 Mbps up'),
         ('+ backup', '2x headroom'), ('Test', 'speedtest + monitor')],
    )},
    'crackle-popping-audio-church-stream': {'subdir': SUB, 'spec': diag(
        'Crackling Audio Fix', 'Pops and clicks on stream',
        [('Cables', 'inspect XLR / TRS'), ('Gain', 'reduce preamp'),
         ('Buffer', 'raise ASIO ms'), ('Ground', 'check loops')],
    )},
    'echo-feedback-church-live-stream': {'subdir': SUB, 'spec': diag(
        'Echo & Feedback Fix', 'Clean up the online mix',
        [('Mic bleed', 'mute open chans'), ('Monitor', 'kill open returns'),
         ('EQ', 'notch feedback freq'), ('Route', 'separate bcast bus')],
    )},
    'facebook-live-connection-failed-church': {'subdir': SUB, 'spec': diag(
        'Facebook Live Fix', 'Connection failed mid-stream',
        [('Stream key', 'regenerate'), ('Bitrate', 'lower to 4000'),
         ('DNS', 'flush + retry'), ('Restream', 'fallback platform')],
    )},
    'hdmi-signal-dropping-church-setup': {'subdir': SUB, 'spec': diag(
        'HDMI Drop Fix', 'Black flashes and lost sync',
        [('Cable', 'certified high-speed'), ('HDCP', 'disable source'),
         ('Scaler', 'insert Roland'), ('Run length', 'fiber / amp')],
    )},
    'high-latency-stream-viewers-church': {'subdir': SUB, 'spec': diag(
        'High Latency Fix', 'Viewers are 30+ seconds behind',
        [('CDN', 'low-latency mode'), ('Player', 'LL-HLS / DASH'),
         ('Encoder', 'keyframe 2s'), ('ISP', 'upload stability')],
    )},
    'kiloview-encoder-web-ui-password': {'subdir': SUB, 'spec': diag(
        'Kiloview Web UI Fix', 'Password reset and UI access',
        [('IP scan', 'find device'), ('Hold reset', '10s button'),
         ('Login', 'admin / admin'), ('Update', 'firmware patch')],
    )},
    'mixer-usb-not-recognized-computer': {'subdir': SUB, 'spec': diag(
        'Mixer USB Audio Fix', 'PC doesn\'t see the mixer',
        [('Driver', 'vendor install'), ('Port', 'USB 2 / 3 swap'),
         ('Sample rate', '48kHz match'), ('App', 'select device')],
    )},
    'multistream-one-platform-failing': {'subdir': SUB, 'spec': diag(
        'Multistream Platform Fix', 'One destination keeps dropping',
        [('Bitrate', 'respect cap'), ('Key', 'regenerate'),
         ('Firewall', 'port 1935 / 443'), ('Restream', 'retry logic')],
    )},
    'ndi-camera-not-showing-obs-vmix': {'subdir': SUB, 'spec': diag(
        'NDI Camera Discovery Fix', 'Camera missing from source list',
        [('Subnet', 'same VLAN'), ('mDNS', 'allow multicast'),
         ('NDI Tools', 'Access Manager'), ('Firewall', 'NDI ports')],
    )},
    'ndi-not-working-church-network': {'subdir': SUB, 'spec': diag(
        'NDI Network Fix', 'End-to-end NDI troubleshooting',
        [('Unicast', 'force mode'), ('Switch', 'IGMP snooping'),
         ('MTU', 'jumbo frames'), ('Discovery', 'manual add')],
    )},
    'no-audio-youtube-facebook-stream': {'subdir': SUB, 'spec': diag(
        'No Stream Audio Fix', 'Stream has video but no sound',
        [('OBS', 'audio device set'), ('Mixer', 'USB out routed'),
         ('Levels', 'not muted'), ('CDN', 'upload verify')],
    )},
    'obs-black-screen-church-stream': {'subdir': SUB, 'spec': diag(
        'OBS Black Screen Fix', 'Preview is all black',
        [('GPU', 'compat render'), ('Capture', 'game / display'),
         ('Driver', 'update NVIDIA'), ('Source', 'add fresh')],
    )},
    'obs-not-connecting-twitch-youtube': {'subdir': SUB, 'spec': diag(
        'OBS Connection Fix', 'Won\'t connect to CDN',
        [('Key', 'refresh stream key'), ('Region', 'closest server'),
         ('DNS', 'flush + 8.8.8.8'), ('Firewall', 'allow OBS')],
    )},
    'propresenter-ndi-output-not-visible': {'subdir': SUB, 'spec': diag(
        'ProPresenter NDI Fix', 'OBS / vMix can\'t see PP source',
        [('Enable', 'output via NDI'), ('Version', 'PP7 + plugin'),
         ('Network', 'same subnet'), ('Discovery', 'Access Manager')],
    )},
    'ptz-camera-losing-ip-address': {'subdir': SUB, 'spec': diag(
        'PTZ IP Drop Fix', 'Camera keeps getting new IPs',
        [('DHCP', 'reserve MAC'), ('Static', 'set in camera UI'),
         ('Lease', 'long lease time'), ('Switch', 'check PoE reboot')],
    )},
    'ptz-camera-not-connecting-network': {'subdir': SUB, 'spec': diag(
        'PTZ Network Fix', 'Camera won\'t join LAN',
        [('Cable', 'link lights'), ('IP', 'subnet match'),
         ('PoE', 'switch budget'), ('Factory', 'reset + rediscover')],
    )},
    'ptz-preset-not-recalling-correctly': {'subdir': SUB, 'spec': diag(
        'PTZ Preset Drift Fix', 'Presets snap to wrong position',
        [('Re-set', 'overwrite preset'), ('Speed', 'slow recall'),
         ('Encoder', 'check position'), ('Firmware', 'update')],
    )},
    'roland-v1hd-no-video-output': {'subdir': SUB, 'spec': diag(
        'Roland V-1HD Output Fix', 'Program out shows black',
        [('Input', 'active source'), ('Output', 'format scaling'),
         ('HDCP', 'disable source'), ('Factory', 'reset if needed')],
    )},
    'stream-dropping-frames-church': {'subdir': SUB, 'spec': diag(
        'OBS Dropped Frames Fix', 'Stream is dropping encoder frames',
        [('Bitrate', 'reduce kbps'), ('Encoder', 'NVENC / QSV'),
         ('Network', 'wired + test'), ('Scenes', 'simplify')],
    )},
    'stream-key-invalid-church-fix': {'subdir': SUB, 'spec': diag(
        'Stream Key Invalid Fix', 'CDN rejects the key',
        [('Regenerate', 'new key'), ('Region', 'correct ingest'),
         ('Copy', 'no spaces'), ('Account', 'live enabled')],
    )},
    'streaming-mix-too-loud-quiet': {'subdir': SUB, 'spec': diag(
        'Online Mix Level Fix', 'Broadcast feed is too loud / quiet',
        [('Target', '-16 LUFS'), ('Compress', 'bus limiter'),
         ('Separate', 'bcast bus'), ('Monitor', 'VU meter')],
    )},
    'streaming-pc-dropping-connection': {'subdir': SUB, 'spec': diag(
        'Streaming PC Net Fix', 'PC keeps dropping off the network',
        [('Wired', 'kill wifi'), ('Driver', 'update NIC'),
         ('Power', 'disable USB sleep'), ('Switch', 'port swap')],
    )},
    'vlan-setup-av-streaming-church': {'subdir': SUB, 'spec': {
        'type': 'network_topology',
        'title': 'Church AV VLAN Setup',
        'subtitle': 'Isolate streaming and camera traffic',
        'zones': [
            {'x': 80,  'y': 260, 'w': 620, 'h': 560, 'label': 'Camera VLAN 10'},
            {'x': 880, 'y': 260, 'w': 640, 'h': 560, 'label': 'Production VLAN 20'},
        ],
        'devices': [
            {'id': 'c1', 'x': 150, 'y': 380, 'label': 'PTZ 1', 'sub': '10.0.10.11'},
            {'id': 'c2', 'x': 150, 'y': 510, 'label': 'PTZ 2', 'sub': '10.0.10.12'},
            {'id': 'c3', 'x': 150, 'y': 640, 'label': 'PTZ 3', 'sub': '10.0.10.13'},
            {'id': 'sw', 'x': 430, 'y': 510, 'label': 'L3 Switch', 'sub': 'tag VLANs'},
            {'id': 'pc', 'x': 940, 'y': 410, 'label': 'vMix PC', 'sub': '10.0.20.5'},
            {'id': 'en', 'x': 940, 'y': 540, 'label': 'Encoder', 'sub': '10.0.20.6'},
            {'id': 'rt', 'x': 940, 'y': 670, 'label': 'Router',  'sub': 'internet'},
        ],
        'edges': [
            {'from': 'c1', 'to': 'sw', 'type': 'PoE'},
            {'from': 'c2', 'to': 'sw', 'type': 'PoE'},
            {'from': 'c3', 'to': 'sw', 'type': 'PoE'},
            {'from': 'sw', 'to': 'pc', 'type': 'NDI'},
            {'from': 'sw', 'to': 'en', 'type': 'NDI'},
            {'from': 'en', 'to': 'rt', 'type': 'RTMP'},
        ],
    }},
    'vmix-inputs-not-displaying': {'subdir': SUB, 'spec': diag(
        'vMix Input Fix', 'Inputs show blank or missing',
        [('Source', 'verify path'), ('Format', 'codec compat'),
         ('GPU', 'render update'), ('Refresh', 'reload input')],
    )},
    'youtube-stream-offline-mid-service': {'subdir': SUB, 'spec': diag(
        'YouTube Stream Recovery', 'Stream goes offline during service',
        [('Detect', 'watch monitor'), ('Restart', 'new stream'),
         ('Key', 'use backup key'), ('Notify', 'social fallback')],
    )},
}


if __name__ == '__main__':
    run(ENTRIES)
