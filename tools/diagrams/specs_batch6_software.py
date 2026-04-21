"""Batch 6 — software articles (28)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from _batch_helper import run  # noqa: E402


def flow(title, subtitle, nodes, edges, footer=''):
    return {
        'type': 'signal_flow',
        'title': title, 'subtitle': subtitle,
        'nodes': [{'label': n[0], 'sub': n[1]} for n in nodes],
        'edges': [{'type': t} for t in edges],
        **({'footer': footer} if footer else {}),
    }


def steps(title, subtitle, steps_list, footer=''):
    return {
        'type': 'preset_workflow',
        'title': title, 'subtitle': subtitle,
        'steps': [{'label': s[0], 'sub': s[1]} for s in steps_list],
        **({'footer': footer} if footer else {}),
    }


def stack(title, subtitle, layers, footer=''):
    return {
        'type': 'stack',
        'title': title, 'subtitle': subtitle,
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


SUB = 'software'

ENTRIES = {
    'castr-vs-restream-church': {'subdir': SUB, 'spec': cmp2(
        'Castr vs Restream', 'Church multistreaming platforms',
        'Castr', 'Restream',
        [('Destinations','20+',True,'30+',True),('Record','Cloud',True,'Cloud',True),
         ('Price','From $13',True,'From $19',None),('Schedule','Yes',True,'Yes',True),
         ('Support','Good',True,'Good',True),('Best For','Budget',True,'Feature set',True)],
    )},
    'easyworship-7-church-setup': {'subdir': SUB, 'spec': steps(
        'EasyWorship 7 Setup', 'From install to first service',
        [('Install','Windows only'),('Import','songs + media'),
         ('Outputs','FOH + stream'),('Rehearse','dry run')],
    )},
    'easyworship-ndi-streaming': {'subdir': SUB, 'spec': flow(
        'EasyWorship NDI Output', 'Send graphics to your stream',
        [('EasyWorship','lyrics + media'),('NDI Out','alpha keyed'),
         ('OBS / vMix','source'),('Stream','composite out')],
        ['NDI','NDI','RTMP'],
    )},
    'easyworship-vs-propresenter': {'subdir': SUB, 'spec': cmp2(
        'EasyWorship vs ProPresenter', 'Worship media software',
        'EasyWorship', 'ProPresenter',
        [('Platform','Windows',False,'Mac + Win',True),
         ('Price','$699 once',True,'$399/yr',False),
         ('Library','Good',None,'Huge',True),
         ('NDI',' Yes',True,'Yes',True),
         ('Learning','Easier',True,'Steeper',None),
         ('Community','Growing',None,'Large',True)],
    )},
    'obs-audio-routing-church-mixer': {'subdir': SUB, 'spec': flow(
        'OBS Audio from Church Mixer', 'USB and aux routing for streaming',
        [('Mixer','FOH + bcast bus'),('USB','multitrack'),
         ('PC','audio interface'),('OBS','stream audio')],
        ['Audio','USB','USB'],
    )},
    'obs-bitrate-settings-church': {'subdir': SUB, 'spec': stack(
        'OBS Bitrate Settings', 'Recommended settings by resolution',
        [('4K','20-40 Mbps'),('1080p60','9 Mbps'),
         ('1080p30','6 Mbps'),('720p30','3-4 Mbps'),('Audio','160-320 kbps')],
    )},
    'obs-church-complete-setup': {'subdir': SUB, 'spec': steps(
        'OBS Complete Church Setup', 'First-time OBS config for worship',
        [('Install','latest build'),('Scenes','5-6 templates'),
         ('Audio','mixer routing'),('Stream','CDN + test')],
    )},
    'obs-dropping-frames-fix': {'subdir': SUB, 'spec': steps(
        'OBS Dropped Frames Fix', 'Diagnose and fix frame drops',
        [('Network','wired + test'),('Bitrate','reduce kbps'),
         ('Encoder','NVENC preset'),('Scenes','simplify sources')],
    )},
    'obs-multistream-restream': {'subdir': SUB, 'spec': flow(
        'OBS Multistream Flow', 'One source, many destinations',
        [('OBS','single output'),('Restream.io','fan-out'),
         ('YouTube','ingest'),('Facebook','ingest')],
        ['RTMP','RTMP','RTMP'],
    )},
    'obs-ndi-church-cameras': {'subdir': SUB, 'spec': flow(
        'OBS NDI Camera Inputs', 'Cameras appear as native sources',
        [('NDI Cam','source'),('Switch','gigabit'),
         ('OBS PC','NDI plugin'),('Stream','RTMP out')],
        ['NDI','NDI','RTMP'],
    )},
    'obs-propresenter-ndi-together': {'subdir': SUB, 'spec': flow(
        'OBS + ProPresenter via NDI', 'Graphics overlay workflow',
        [('ProPresenter','NDI out'),('OBS','NDI source'),
         ('Compose','scene + alpha'),('Stream','RTMP out')],
        ['NDI','NDI','RTMP'],
    )},
    'obs-scenes-church-service': {'subdir': SUB, 'spec': steps(
        'OBS Scenes for Worship', 'Scene templates by service phase',
        [('Pre-service','splash + music'),('Worship','wide cam'),
         ('Sermon','pastor tight'),('Closing','outro + CTA')],
    )},
    'obs-transitions-stingers-church': {'subdir': SUB, 'spec': steps(
        'OBS Transitions & Stingers', 'Branded transitions for worship',
        [('Design','branded MP4'),('Import','stinger source'),
         ('Map','hotkey trigger'),('Test','live preview')],
    )},
    'obs-vmix-when-to-upgrade': {'subdir': SUB, 'spec': cmp2(
        'When to Upgrade OBS→vMix', 'Feature thresholds for the switch',
        'OBS', 'vMix',
        [('Cost','Free',True,'$60-$1200',False),
         ('NDI','Plugin',None,'Native',True),
         ('ISO Rec','Plugin',None,'Native',True),
         ('Replay','No',False,'Yes',True),
         ('Stability','Good',True,'Very high',True),
         ('Support','Forum',None,'Paid',True)],
    )},
    'propresenter-7-church-setup': {'subdir': SUB, 'spec': steps(
        'ProPresenter 7 Setup', 'From install to first Sunday',
        [('Install','Mac or Win'),('Library','songs + bible'),
         ('Outputs','FOH + NDI'),('Rehearse','stage display')],
    )},
    'propresenter-alpha-keyer-atem': {'subdir': SUB, 'spec': flow(
        'ProPresenter + ATEM Alpha', 'Clean keyed lyrics over video',
        [('ProPresenter','fill + key'),('ATEM Mini','upstream key'),
         ('Cam + Lyrics','composite'),('Stream','RTMP out')],
        ['HDMI','SDI','RTMP'],
    )},
    'propresenter-ndi-output-obs-vmix': {'subdir': SUB, 'spec': flow(
        'ProPresenter NDI to OBS/vMix', 'Send lyrics over the network',
        [('ProPresenter','NDI out'),('Network','same subnet'),
         ('OBS/vMix','NDI source'),('Stream','composite')],
        ['NDI','NDI','RTMP'],
    )},
    'propresenter-planning-center-integration': {'subdir': SUB, 'spec': flow(
        'ProPresenter + PCO Integration', 'Service import and sync',
        [('Planning Center','service plan'),('PCO API','sync'),
         ('ProPresenter','auto-populate'),('Sunday','ready')],
        ['Ethernet','Ethernet','Ethernet'],
    )},
    'propresenter-stage-display-setup': {'subdir': SUB, 'spec': stack(
        'ProPresenter Stage Display', 'What worship leaders see',
        [('Current Slide','lyrics now'),('Next Slide','up next'),
         ('Clock','service time'),('Notes','director cue'),('Chord','chart layer')],
    )},
    'propresenter-troubleshooting-performance': {'subdir': SUB, 'spec': steps(
        'ProPresenter Performance Fix', 'Crashing, lag, and slow playback',
        [('Library','clean unused'),('Media','transcode H.264'),
         ('GPU','update driver'),('Cache','rebuild')],
    )},
    'restream-church-multiplatform-setup': {'subdir': SUB, 'spec': steps(
        'Restream Multistream Setup', 'YouTube + Facebook + more',
        [('Sign up','Restream.io'),('Destinations','add CDNs'),
         ('Ingest','stream key'),('Go Live','monitor all')],
    )},
    'restream-obs-integration': {'subdir': SUB, 'spec': flow(
        'OBS + Restream Integration', 'Fan-out from a single OBS output',
        [('OBS','encode once'),('Restream','cloud relay'),
         ('YouTube','ingest'),('Facebook','ingest')],
        ['RTMP','RTMP','RTMP'],
    )},
    'vmix-4k-church-streaming': {'subdir': SUB, 'spec': steps(
        'vMix 4K Church Streaming', 'UHD production in four steps',
        [('Hardware','GPU + CPU'),('Inputs','4K NDI / SDI'),
         ('Encode','HEVC preset'),('Stream','4K RTMP')],
    )},
    'vmix-church-setup-guide': {'subdir': SUB, 'spec': steps(
        'vMix Setup Guide', 'First-time vMix config for worship',
        [('Install','Windows PC'),('Inputs','cams + audio'),
         ('Scenes','build presets'),('Stream','go live')],
    )},
    'vmix-instant-replay-church': {'subdir': SUB, 'spec': stack(
        'vMix Instant Replay', 'Replay workflow layers',
        [('Input','live cam feed'),('Record','continuous buffer'),
         ('Mark','in / out points'),('Playback','slo-mo out'),('Stream','to PGM')],
    )},
    'vmix-ndi-camera-inputs': {'subdir': SUB, 'spec': flow(
        'vMix NDI Camera Inputs', 'Adding network cameras to vMix',
        [('NDI Cam','source'),('Gigabit Switch','same subnet'),
         ('vMix','NDI input'),('Program','stream out')],
        ['NDI','NDI','RTMP'],
    )},
    'vmix-title-overlays-lower-thirds': {'subdir': SUB, 'spec': steps(
        'vMix Titles & Lower Thirds', 'Branded graphics for worship',
        [('Template','GT Title'),('Fields','text + image'),
         ('Trigger','hotkey / macro'),('Cue','as overlay')],
    )},
    'vmix-vs-obs-church': {'subdir': SUB, 'spec': cmp2(
        'vMix vs OBS', 'Software switcher comparison',
        'vMix', 'OBS Studio',
        [('Cost','$60-$1200',False,'Free',True),
         ('NDI','Native',True,'Plugin',None),
         ('ISO Record','Native',True,'Plugin',None),
         ('Replay','Yes',True,'No',False),
         ('Titles','GT pro',True,'Text src',None),
         ('Stability','Very high',True,'High',True)],
    )},
}


if __name__ == '__main__':
    run(ENTRIES)
