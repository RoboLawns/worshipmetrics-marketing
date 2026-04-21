"""Batch 7 — devices (42 articles)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from _batch_helper import run  # noqa: E402


def flow(title, subtitle, nodes, edges, footer=''):
    return {
        'type': 'signal_flow', 'title': title, 'subtitle': subtitle,
        'nodes': [{'label': n[0], 'sub': n[1]} for n in nodes],
        'edges': [{'type': t} for t in edges],
        **({'footer': footer} if footer else {}),
    }


def steps(title, subtitle, steps_list, footer=''):
    return {
        'type': 'preset_workflow', 'title': title, 'subtitle': subtitle,
        'steps': [{'label': s[0], 'sub': s[1]} for s in steps_list],
        **({'footer': footer} if footer else {}),
    }


def stack(title, subtitle, layers, footer=''):
    return {
        'type': 'stack', 'title': title, 'subtitle': subtitle,
        'layers': [{'label': l[0], 'sub': l[1]} for l in layers],
        **({'footer': footer} if footer else {}),
    }


def cmp2(title, subtitle, a, b, rows):
    return {
        'type': 'comparison', 'title': title, 'subtitle': subtitle,
        'rows': [r[0] for r in rows],
        'columns': [
            {'label': a, 'values': [{'text': r[1], **({'good': r[2]} if r[2] is not None else {})} for r in rows]},
            {'label': b, 'values': [{'text': r[3], **({'good': r[4]} if r[4] is not None else {})} for r in rows]},
        ],
    }


SUB = 'devices'

ENTRIES = {
    # --- Behringer WING ---
    'behringer-wing-dante-aes50': {'subdir': SUB, 'spec': flow(
        'WING Dante & AES50 Setup', 'Digital snake over Cat5e',
        [('WING Console','AES50 A/B'),('Stagebox','S32 / SD16'),
         ('Dante Card','WING-LIVE'),('Recorder','multitrack')],
        ['Ethernet','Ethernet','USB'],
    )},
    'behringer-wing-scene-workflow': {'subdir': SUB, 'spec': steps(
        'WING Scene Workflow', 'Show management for complex services',
        [('Build','snapshot library'),('Group','by service type'),
         ('Cue','scoped recall'),('Rehearse','volunteer test')],
    )},
    'behringer-wing-setup-guide': {'subdir': SUB, 'spec': steps(
        'Behringer WING Setup', 'First-time WING configuration',
        [('Power + boot','firmware check'),('Patch','inputs + buses'),
         ('Routing','FOH + bcast'),('Save','snapshot show')],
    )},
    'behringer-wing-streaming-integration': {'subdir': SUB, 'spec': flow(
        'WING Streaming Audio', 'USB and AES67 to the stream',
        [('WING','48-ch USB'),('PC','streaming rig'),
         ('OBS / vMix','audio source'),('Stream','bcast bus')],
        ['USB','USB','RTMP'],
    )},

    # --- X32 Compact ---
    'behringer-x32-compact-scene-management': {'subdir': SUB, 'spec': steps(
        'X32 Compact Scenes', 'Show management for churches',
        [('Design','service template'),('Save','scene library'),
         ('Scope','safe critical ch'),('Recall','one-button')],
    )},
    'behringer-x32-compact-setup-guide': {'subdir': SUB, 'spec': steps(
        'X32 Compact Setup', 'Getting your X32 Compact ready for Sunday',
        [('Power','boot + update'),('Patch','stage inputs'),
         ('Routing','mains + mons'),('Scene','save as default')],
    )},
    'behringer-x32-compact-streaming-setup': {'subdir': SUB, 'spec': flow(
        'X32 Compact Streaming Audio', 'USB + aux bus routing',
        [('X32 Compact','32-ch USB'),('PC','streaming rig'),
         ('OBS','audio input'),('Stream','broadcast bus')],
        ['USB','USB','RTMP'],
    )},
    'behringer-x32-compact-vs-full-x32': {'subdir': SUB, 'spec': cmp2(
        'X32 Compact vs Full X32', 'Which console for your church',
        'X32 Compact', 'Full X32',
        [('Faders','16 + 1',None,'25 + 1',True),
         ('Channels','32 mic',True,'32 mic',True),
         ('Screen','7"',True,'7"',True),
         ('Stagebox','S16/SD16',True,'S16/SD16',True),
         ('Footprint','smaller',True,'full',None),
         ('Price','~$2,000',True,'~$2,300',None)],
    )},
    'behringer-x32-compact-x32-edit': {'subdir': SUB, 'spec': flow(
        'X32 Compact + X32-Edit', 'Remote control over the network',
        [('X32 Compact','Ethernet port'),('Switch','LAN'),
         ('PC','X32-Edit'),('Control','full mirror')],
        ['Ethernet','Ethernet','Ethernet'],
    )},
    'behringer-x32-edit-remote-control': {'subdir': SUB, 'spec': steps(
        'X32-Edit Remote Setup', 'Mirror the console from a laptop',
        [('Install','X32-Edit app'),('Network','same subnet'),
         ('Connect','set IP match'),('Sync','mirror console')],
    )},
    'behringer-x32-gain-staging-worship': {'subdir': SUB, 'spec': steps(
        'X32 Gain Staging', 'Clean gain structure for worship',
        [('Preamp','peak -18 dBFS'),('Channel','headroom'),
         ('Bus','bcast separate'),('Master','-3 dBFS cap')],
    )},
    'behringer-x32-multitrack-recording': {'subdir': SUB, 'spec': flow(
        'X32 Multi-Track Recording', '32-channel multitrack to DAW',
        [('X32','32-ch preamps'),('USB','multitrack out'),
         ('DAW','Reaper / Logic'),('Mix','post-service')],
        ['Audio','USB','USB'],
    )},
    'behringer-x32-scene-recall-volunteers': {'subdir': SUB, 'spec': steps(
        'X32 Volunteer Scenes', 'One-button recall for volunteers',
        [('Design','4-6 named scenes'),('Safe','critical params'),
         ('Hotkey','user buttons'),('Label','clear text')],
    )},
    'behringer-x32-setup-guide-church': {'subdir': SUB, 'spec': steps(
        'X32 Church Setup', 'First-time X32 configuration',
        [('Power','firmware current'),('Patch','inputs + outs'),
         ('Routing','FOH + bcast'),('Snapshot','save default')],
    )},
    'behringer-x32-streaming-audio-obs-vmix': {'subdir': SUB, 'spec': flow(
        'X32 Streaming Audio', 'Route to OBS and vMix',
        [('X32','bcast mix bus'),('USB 32-ch','to PC'),
         ('OBS / vMix','select input'),('Stream','bcast out')],
        ['USB','USB','RTMP'],
    )},
    'behringer-x32-troubleshooting-audio': {'subdir': SUB, 'spec': steps(
        'X32 Audio Troubleshoot', 'No audio, feedback, common fixes',
        [('Check signal','meters + solo'),('Gain','preamp level'),
         ('Routing','verify sends'),('Feedback','EQ notch')],
    )},

    # --- XR12 / XR18 ---
    'behringer-xr12-app-streaming-setup': {'subdir': SUB, 'spec': flow(
        'XR12 App + Streaming', 'Tablet control and USB to PC',
        [('XR12','rack mixer'),('WiFi','same SSID'),
         ('X-Air app','iPad control'),('USB','to OBS PC')],
        ['Wireless','Wireless','USB'],
    )},
    'behringer-xr12-setup-guide': {'subdir': SUB, 'spec': steps(
        'XR12 Small-Church Setup', 'First-time XR12 configuration',
        [('Rack','mount + power'),('Network','wifi AP mode'),
         ('App','pair iPad'),('Test','input levels')],
    )},
    'behringer-xr12-vs-xr18': {'subdir': SUB, 'spec': cmp2(
        'XR12 vs XR18', 'Which Behringer X-Air',
        'XR12', 'XR18',
        [('Mic Inputs','4 + 4',None,'16',True),
         ('Size','1U',True,'1U',True),
         ('USB Rec','stereo',False,'18-ch',True),
         ('Effects','4 FX',True,'4 FX',True),
         ('Price','~$450',True,'~$700',None),
         ('Best For','tiny church',True,'small church',True)],
    )},
    'behringer-xr18-network-setup': {'subdir': SUB, 'spec': {
        'type': 'network_topology',
        'title': 'XR18 Network Setup',
        'subtitle': 'Router vs direct Ethernet for church WiFi',
        'zones': [
            {'x': 80,  'y': 260, 'w': 620, 'h': 560, 'label': 'Option A — Router'},
            {'x': 880, 'y': 260, 'w': 640, 'h': 560, 'label': 'Option B — Direct'},
        ],
        'devices': [
            {'id': 'mx1','x': 150,'y': 440,'label': 'XR18','sub': 'mixer'},
            {'id': 'rt', 'x': 430,'y': 440,'label': 'Router','sub': 'AP + DHCP'},
            {'id': 'ip1','x': 150,'y': 620,'label': 'iPad','sub': 'X-Air app'},
            {'id': 'mx2','x': 960,'y': 440,'label': 'XR18','sub': 'AP mode'},
            {'id': 'ip2','x': 960,'y': 620,'label': 'iPad','sub': 'direct join'},
        ],
        'edges': [
            {'from': 'mx1','to': 'rt', 'type': 'Ethernet'},
            {'from': 'rt', 'to': 'ip1','type': 'Wireless'},
            {'from': 'mx2','to': 'ip2','type': 'Wireless'},
        ],
    }},
    'behringer-xr18-setup-guide-church': {'subdir': SUB, 'spec': steps(
        'XR18 Church Setup', 'Full config for small church',
        [('Rack','install + power'),('Network','router or AP'),
         ('App','X-Air pair'),('Scene','save default')],
    )},
    'behringer-xr18-streaming-aux-usb': {'subdir': SUB, 'spec': flow(
        'XR18 Streaming Mix', 'Create a separate stream bus',
        [('XR18','inputs'),('Aux Bus','bcast mix'),
         ('USB','to PC'),('OBS','stream audio')],
        ['Audio','USB','RTMP'],
    )},
    'behringer-xr18-troubleshooting': {'subdir': SUB, 'spec': steps(
        'XR18 Connection Fix', 'App and network troubleshooting',
        [('WiFi','same SSID'),('IP','subnet match'),
         ('Firewall','disable on PC'),('Reset','hold setup')],
    )},
    'behringer-xr18-x-air-app-setup': {'subdir': SUB, 'spec': steps(
        'X-Air App Setup', 'iPad / Android control',
        [('Install','X-Air app'),('Connect','same WiFi'),
         ('Select','XR18 from list'),('Adjust','faders + FX')],
    )},

    # --- Epiphan ---
    'epiphan-pearl-mini-multi-input': {'subdir': SUB, 'spec': flow(
        'Pearl Mini Multi-Input', 'Record multiple sources at once',
        [('HDMI 1','cam'),('HDMI 2','slides'),
         ('Pearl Mini','layouts'),('Record','ISO + PGM')],
        ['HDMI','HDMI','Ethernet'],
    )},
    'epiphan-pearl-mini-setup-guide': {'subdir': SUB, 'spec': steps(
        'Pearl Mini Setup', 'Standalone record + stream',
        [('Connect','HDMI inputs'),('Layout','PGM + ISO'),
         ('Stream','RTMP / SRT'),('Record','USB / SD')],
    )},
    'epiphan-webcaster-x2-setup-guide': {'subdir': SUB, 'spec': steps(
        'Webcaster X2 Setup', 'Plug-and-stream appliance setup',
        [('Connect','HDMI + LAN'),('Platform','YouTube / FB'),
         ('Authorize','device pair'),('Go live','hit button')],
    )},
    'epiphan-webcaster-x2-troubleshooting': {'subdir': SUB, 'spec': steps(
        'Webcaster X2 Fix', 'Connection issues resolved',
        [('HDMI','source lock'),('Network','wired gbE'),
         ('CDN','reauth account'),('Firmware','update')],
    )},
    'epiphan-webcaster-x2-youtube-facebook': {'subdir': SUB, 'spec': flow(
        'Webcaster X2 to CDN', 'Live stream to YouTube + Facebook',
        [('Camera','HDMI out'),('Webcaster X2','encoder'),
         ('Internet','RTMP out'),('YT + FB','ingest')],
        ['HDMI','Ethernet','RTMP'],
    )},

    # --- Kiloview ---
    'kiloview-dc230-multi-campus-decoder': {'subdir': SUB, 'spec': flow(
        'Kiloview DC230 Decoder', 'Receive stream at satellite campus',
        [('Main Campus','SRT / RTMP'),('Internet','WAN'),
         ('DC230','decoder'),('Satellite PA','HDMI out')],
        ['RTMP','Ethernet','HDMI'],
    )},
    'kiloview-e1-hdmi-setup-guide': {'subdir': SUB, 'spec': steps(
        'Kiloview E1 Setup', 'HDMI encoder first-time config',
        [('Power','PoE or DC'),('Web UI','find IP'),
         ('Source','HDMI input'),('Stream','SRT / RTMP')],
    )},
    'kiloview-e1-srt-caller-listener': {'subdir': SUB, 'spec': cmp2(
        'SRT Caller vs Listener', 'Kiloview E1 SRT mode explainer',
        'Caller Mode', 'Listener Mode',
        [('Role','initiates',None,'waits for',None),
         ('Firewall','easy outbound',True,'needs port open',False),
         ('Use Case','to remote',True,'receive at campus',True),
         ('NAT','works through',True,'needs public IP',False),
         ('Setup','simpler',True,'more config',None),
         ('Best For','streaming out',True,'campus receive',True)],
    )},
    'kiloview-e1-srt-rtmp-streaming': {'subdir': SUB, 'spec': flow(
        'Kiloview E1 SRT + RTMP', 'Low-latency and CDN streaming',
        [('Camera','HDMI out'),('Kiloview E1','encoder'),
         ('SRT','contribution'),('RTMP','public CDN')],
        ['HDMI','Ethernet','RTMP'],
    )},
    'kiloview-e1-vs-magewell': {'subdir': SUB, 'spec': cmp2(
        'Kiloview E1 vs Magewell Ultra', 'Budget vs pro encoder',
        'Kiloview E1', 'Magewell Ultra',
        [('Inputs','HDMI',None,'HDMI + SDI',True),
         ('SRT','Yes',True,'Yes',True),
         ('Build','plastic',None,'metal',True),
         ('PoE','Yes',True,'Yes',True),
         ('Price','~$400',True,'~$800',False),
         ('Support','good',None,'US pro',True)],
    )},
    'kiloview-e2-sdi-multi-campus': {'subdir': SUB, 'spec': flow(
        'Kiloview E2 Multi-Campus', 'SDI distribution to satellites',
        [('Main PGM','SDI out'),('Kiloview E2','encoder'),
         ('Internet','WAN'),('Campuses','decode + PA')],
        ['SDI','Ethernet','RTMP'],
    )},
    'kiloview-e2-sdi-setup-guide': {'subdir': SUB, 'spec': steps(
        'Kiloview E2 SDI Setup', 'SDI encoder first-time config',
        [('Power','PoE or DC'),('SDI In','camera / switcher'),
         ('Web UI','IP access'),('Stream','SRT / RTMP')],
    )},
    'kiloview-n2-multi-campus-setup': {'subdir': SUB, 'spec': flow(
        'Kiloview N2 NDI Distribution', 'Cross-room NDI delivery',
        [('Main Room','HDMI PGM'),('Kiloview N2','HDMI→NDI'),
         ('Network','gigabit LAN'),('Overflow Room','NDI decoder')],
        ['HDMI','NDI','NDI'],
    )},
    'kiloview-n2-ndi-network-discovery': {'subdir': SUB, 'spec': steps(
        'Kiloview N2 NDI Discovery', 'Make sure OBS sees the source',
        [('Subnet','same VLAN'),('mDNS','allow multicast'),
         ('Access Manager','add manually'),('Firewall','NDI ports')],
    )},
    'kiloview-n2-obs-vmix-ndi-source': {'subdir': SUB, 'spec': flow(
        'Kiloview N2 to OBS/vMix', 'Network video into your switcher',
        [('HDMI Source','cam / switcher'),('Kiloview N2','HDMI→NDI'),
         ('OBS / vMix','NDI input'),('Stream','composite out')],
        ['HDMI','NDI','RTMP'],
    )},
    'kiloview-n2-setup-guide': {'subdir': SUB, 'spec': steps(
        'Kiloview N2 Setup', 'HDMI-to-NDI encoder setup',
        [('Power','PoE+'),('Connect','HDMI in'),
         ('Web UI','find IP'),('Verify','NDI in OBS')],
    )},
    'kiloview-web-ui-configuration-guide': {'subdir': SUB, 'spec': stack(
        'Kiloview Web UI Overview', 'Five configuration sections',
        [('System','firmware + reboot'),('Network','DHCP / static'),
         ('Video','source + output'),('Stream','RTMP / SRT / NDI'),
         ('Security','password + lock')],
    )},

    # --- Yamaha ---
    'yamaha-tf5-vs-behringer-x32': {'subdir': SUB, 'spec': cmp2(
        'Yamaha TF5 vs Behringer X32', 'Mid-tier digital console comparison',
        'Yamaha TF5', 'Behringer X32',
        [('Channels','48',True,'32',None),
         ('Preamps','D-PRE',True,'Midas',True),
         ('Stagebox','Tio1608-D',True,'S16',True),
         ('Touchscreen','12"',True,'7"',None),
         ('Price','~$5,000',False,'~$2,300',True),
         ('Community','large',True,'huge',True)],
    )},
}


if __name__ == '__main__':
    run(ENTRIES)
