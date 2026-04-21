"""Batch 4 — comparisons (31 articles). All comparison layout."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from _batch_helper import run  # noqa: E402


def cmp_spec(title, subtitle, a_label, b_label, rows):
    """rows: list of (label, a_text, a_good_or_none, b_text, b_good_or_none)"""
    cols = [
        {'label': a_label, 'values': []},
        {'label': b_label, 'values': []},
    ]
    row_labels = []
    for r in rows:
        row_labels.append(r[0])
        cols[0]['values'].append({'text': r[1], **({'good': r[2]} if r[2] is not None else {})})
        cols[1]['values'].append({'text': r[3], **({'good': r[4]} if r[4] is not None else {})})
    return {
        'type': 'comparison',
        'title': title,
        'subtitle': subtitle,
        'rows': row_labels,
        'columns': cols,
    }


SUB = 'comparisons'

ENTRIES = {
    'allen-heath-cq18t-vs-behringer-xr18': {'subdir': SUB, 'spec': cmp_spec(
        'CQ-18T vs Behringer XR18', 'Small-church digital mixer comparison',
        'A&H CQ-18T', 'Behringer XR18',
        [
            ('Channels',    '16 mic in', True,  '16 mic in', True),
            ('Touchscreen', 'Built-in 7"', True, 'Tablet only', False),
            ('Price',       '~$1,200', None,   '~$700', True),
            ('Scenes',      'Yes', True,        'Yes', True),
            ('Recording',   'USB 18-ch', True, 'USB 18-ch', True),
            ('Build',       'Pro-grade', True, 'Budget', None),
        ],
    )},
    'analog-vs-digital-mixer-small-church': {'subdir': SUB, 'spec': cmp_spec(
        'Analog vs Digital Mixer', 'Upgrade calculus for small churches',
        'Analog Mixer', 'Digital Mixer',
        [
            ('Scenes',       'No', False,      'Yes', True),
            ('Effects',      'External', False,'Built-in', True),
            ('Remote',       'None', False,    'App/iPad', True),
            ('Recording',    'Tape/aux', False,'USB multitrack', True),
            ('Price',        '$300+', None,    '$700+', None),
            ('Learning',     'Fast', True,     'Steeper', None),
        ],
    )},
    'atem-mini-extreme-vs-atem-television-studio': {'subdir': SUB, 'spec': cmp_spec(
        'ATEM Mini Extreme vs TV Studio HD', 'Compact vs rack-mount for churches',
        'Mini Extreme', 'TV Studio HD',
        [
            ('Inputs',       '8 HDMI', True,  '4 SDI + 4 HDMI', True),
            ('Form Factor',  'Compact desk', True,'1RU rack', None),
            ('ISO Record',   'Yes', True,     'No', False),
            ('Macros',       'Yes', True,     'Yes', True),
            ('Price',        '~$1,000', True, '~$3,000', False),
            ('Best For',     'Streaming', None,'Broadcast', None),
        ],
    )},
    'atem-mini-pro-vs-roland-v1hd': {'subdir': SUB, 'spec': cmp_spec(
        'ATEM Mini Pro vs Roland V-1HD', 'Compact HDMI switchers for worship',
        'ATEM Mini Pro', 'Roland V-1HD',
        [
            ('Inputs',       '4 HDMI', True,  '4 HDMI', True),
            ('Built-in Stream','Yes', True,  'No', False),
            ('USB Webcam',   'Yes', True,    'No', False),
            ('T-Bar',        'No', False,    'Yes', True),
            ('Price',        '~$500', True,  '~$700', None),
            ('Software',     'ATEM SW', True,'Roland', None),
        ],
    )},
    'atem-mini-vs-atem-mini-pro-church': {'subdir': SUB, 'spec': cmp_spec(
        'ATEM Mini vs Mini Pro', 'Which ATEM for your church',
        'ATEM Mini', 'ATEM Mini Pro',
        [
            ('Inputs',       '4 HDMI', True, '4 HDMI', True),
            ('Direct Stream','No', False,    'Yes', True),
            ('Recording',    'No', False,    'USB disk', True),
            ('Multiview',    'No', False,    'Yes', True),
            ('Price',        '~$300', True,  '~$500', None),
            ('Best For',     'Prod switch', None,'Streaming', True),
        ],
    )},
    'atem-mini-vs-vmix-software-switcher': {'subdir': SUB, 'spec': cmp_spec(
        'ATEM Mini vs vMix', 'Hardware vs software switching',
        'ATEM Mini', 'vMix',
        [
            ('Form',         'Hardware', None,'Software', None),
            ('Inputs',       '4 HDMI', None, 'Unlimited NDI', True),
            ('ISO Record',   'No', False,    'Yes', True),
            ('Graphics',     'Basic', None,  'Full', True),
            ('PC Needed',    'No', True,     'Yes', False),
            ('Price',        '~$300', True,  '$60-$1200', None),
        ],
    )},
    'avkans-vs-tenveo-church-ptz': {'subdir': SUB, 'spec': cmp_spec(
        'AVKANS vs Tenveo PTZ', 'Which to buy for church production',
        'AVKANS U100', 'Tenveo VHD20U',
        [
            ('Output',       'NDI + HDMI', True,'HDMI + USB', True),
            ('Native NDI',   'Yes', True,    'No', False),
            ('PoE',          'U200 only', None,'No', False),
            ('Zoom',         '20x', True,    '20x', True),
            ('Price',        '~$400', True,  '~$300', True),
            ('Best For',     'OBS / vMix', None,'ATEM / Roland', None),
        ],
    )},
    'avkans-vs-tongveo-ndi-camera': {'subdir': SUB, 'spec': cmp_spec(
        'AVKANS vs TONGVEO NDI', 'Budget NDI PTZ showdown',
        'AVKANS U200', 'TONGVEO NDI',
        [
            ('Native NDI',   'Yes', True,    'Yes', True),
            ('PoE',          'Yes', True,    'Yes', True),
            ('Zoom',         '20x', True,    '20x', True),
            ('Warranty',     '2 year', True, '1 year', False),
            ('Price',        '~$500', None,  '~$450', True),
            ('Support',      'US-based', True,'China', False),
        ],
    )},
    'behringer-x32-vs-allen-heath-sq5': {'subdir': SUB, 'spec': cmp_spec(
        'X32 vs Allen & Heath SQ-5', 'Flagship digital mixers for churches',
        'Behringer X32', 'A&H SQ-5',
        [
            ('Channels',     '32 mic', True, '48 mic', True),
            ('Preamps',      'Midas', True,  '96kHz', True),
            ('Touchscreen',  '7"', True,     '7"', True),
            ('Price',        '~$2,300', True,'~$3,800', False),
            ('Sound',        'Clean', True,  'Premium', True),
            ('Expansion',    'S16 stagebox', True,'DX168', True),
        ],
    )},
    'behringer-xr18-vs-mackie-dl32r': {'subdir': SUB, 'spec': cmp_spec(
        'XR18 vs Mackie DL32R', 'Rack mixers for mid-size churches',
        'Behringer XR18', 'Mackie DL32R',
        [
            ('Channels',     '16 mic', None, '32 mic', True),
            ('Form',         'Half rack', None,'Full rack', None),
            ('Tablet UI',    'X-Air Edit', True,'Master Fader', True),
            ('Price',        '~$700', True, '~$2,000', False),
            ('Recording',    '18-ch USB', True,'32-ch USB', True),
            ('Best For',     'Small church', None,'Medium', None),
        ],
    )},
    'best-church-streaming-setup-budget': {'subdir': SUB, 'spec': cmp_spec(
        '$1K vs $5K Streaming', 'What an extra $4K actually buys you',
        'Under $1,000', 'Under $5,000',
        [
            ('Cameras',      '1 USB PTZ', None,'3 NDI PTZ', True),
            ('Switcher',     'OBS only', None,'ATEM Extreme', True),
            ('Audio',        'XR12', None,   'X32 Compact', True),
            ('Encoder',      'OBS PC', None, 'Dedicated rig', True),
            ('Resolution',   '1080p30', None,'1080p60', True),
            ('ISO Record',   'No', False,    'Yes', True),
        ],
    )},
    'best-digital-mixer-church-under-1000': {'subdir': SUB, 'spec': {
        'type': 'hero_concept',
        'title': 'Best Digital Mixers Under $1K',
        'subtitle': 'Three church-ready picks for 2024',
        'tag': 'Buyer Guide',
        'stat': '3', 'stat_label': 'top picks',
        'bullets': [
            'Behringer XR18 — tablet workflow, ~$700',
            'Allen & Heath CQ-18T — touchscreen, ~$1,000',
            'Behringer X32 Rack — rack-mount power, ~$1,900',
            'All with multitrack USB recording',
        ],
        'footer': 'Digital mixer buyer guide',
    }},
    'best-encoder-church-streaming': {'subdir': SUB, 'spec': cmp_spec(
        'Magewell vs Teradek vs Kiloview', 'Hardware encoder face-off',
        'Magewell Ultra', 'Teradek VidiU',
        [
            ('Inputs',       'HDMI + SDI', True,'HDMI only', None),
            ('SRT',          'Yes', True,    'Yes', True),
            ('Dashboard',    'Web UI', True, 'Core cloud', True),
            ('Reliability',  'Pro-grade', True,'Pro-grade', True),
            ('Price',        '~$800', None,  '~$1,000', None),
            ('Best For',     'Budget pros', None,'Field kits', None),
        ],
    )},
    'best-hardware-encoder-church-streaming': {'subdir': SUB, 'spec': {
        'type': 'hero_concept',
        'title': 'Best Hardware Encoders 2024',
        'subtitle': 'Pro streaming reliability without a PC',
        'tag': 'Buyer Guide',
        'stat': '5', 'stat_label': 'encoders reviewed',
        'bullets': [
            'Magewell Ultra Encode — HDMI + SRT, ~$800',
            'Teradek VidiU Go — field-ready, ~$1,000',
            'Kiloview E2 — budget NDI in, ~$500',
            'Epiphan Pearl Mini — multi-source pro, ~$2,500',
        ],
        'footer': 'Hardware encoder buyer guide',
    }},
    'best-ptz-camera-church-under-1000': {'subdir': SUB, 'spec': {
        'type': 'hero_concept',
        'title': 'Best PTZ Under $1,000',
        'subtitle': 'Mid-tier church cameras for 2024',
        'tag': 'Buyer Guide',
        'stat': '4', 'stat_label': 'models reviewed',
        'bullets': [
            'AVKANS PTZ-U30 — 30x NDI, ~$600',
            'OBSBOT Tail Air — AI tracking, ~$499',
            'Tenveo VHD30U — 30x USB + HDMI, ~$350',
            'FoMaKo FMK-20X — NDI + PoE, ~$900',
        ],
        'footer': 'PTZ camera picks in the $500-$1000 tier',
    }},
    'best-ptz-camera-church-under-500': {'subdir': SUB, 'spec': {
        'type': 'hero_concept',
        'title': 'Best PTZ Under $500',
        'subtitle': 'Budget PTZ cameras for worship',
        'tag': 'Buyer Guide',
        'stat': '4', 'stat_label': 'models reviewed',
        'bullets': [
            'AVKANS PTZ-U100 — NDI, 20x, ~$400',
            'Tenveo VHD30U — USB + HDMI, 30x, ~$350',
            'Tenveo VHD20U — HDMI, 20x, ~$300',
            'AVKANS PTZ-U200 — NDI + PoE, ~$500',
        ],
        'footer': 'Budget PTZ camera buyer guide',
    }},
    'best-video-switcher-church-under-500': {'subdir': SUB, 'spec': {
        'type': 'hero_concept',
        'title': 'Best Switchers Under $500',
        'subtitle': 'Compact switchers that work for worship',
        'tag': 'Buyer Guide',
        'stat': '4', 'stat_label': 'switchers reviewed',
        'bullets': [
            'ATEM Mini — 4 HDMI, ~$300',
            'ATEM Mini Pro — direct stream, ~$495',
            'Roland V-02HD — HDMI scaler, ~$450',
            'vMix Basic HD — software, ~$60',
        ],
        'footer': 'Sub-$500 video switcher picks',
    }},
    'budget-ptz-vs-ptzoptics-church': {'subdir': SUB, 'spec': cmp_spec(
        'Budget PTZ vs PTZOptics', 'Is the price premium worth it?',
        'Budget PTZ', 'PTZOptics',
        [
            ('Sensor',       'Sony CMOS', None,'Sony Exmor', True),
            ('NDI',          'Depends', None, 'Yes (HX)', True),
            ('Warranty',     '1 year', False,'3 year', True),
            ('Support',      'Limited', False,'US-based', True),
            ('Price',        '~$400', True,  '~$2,500', False),
            ('Longevity',    '2-3 yr', None, '5+ yr', True),
        ],
    )},
    'fomako-vs-avkans-ptz-church': {'subdir': SUB, 'spec': cmp_spec(
        'FoMaKo vs AVKANS PTZ', 'Two budget NDI camera brands',
        'FoMaKo FMK-20X', 'AVKANS U200',
        [
            ('NDI',          'Native', True, 'Native', True),
            ('Zoom',         '20x', True,    '20x', True),
            ('PoE',          'Yes', True,    'Yes', True),
            ('Presets',      '255', True,    '255', True),
            ('Price',        '~$900', None,  '~$500', True),
            ('Support',      'China', None,  'US warehouse', True),
        ],
    )},
    'hardware-encoder-vs-obs-church': {'subdir': SUB, 'spec': cmp_spec(
        'Hardware Encoder vs OBS PC', 'Which is more reliable on Sunday?',
        'Hardware Encoder', 'OBS on PC',
        [
            ('Boot Time',    '<30s', True,   '2-5 min', False),
            ('Crash Risk',   'Near zero', True,'Windows updates', False),
            ('Scenes',       'Limited', False,'Unlimited', True),
            ('Graphics',     'Basic', False, 'Full', True),
            ('Cost',         '$800+', False, '$0 software', True),
            ('Uptime',       'Very high', True,'Depends', None),
        ],
    )},
    'hardware-vs-software-switcher-church': {'subdir': SUB, 'spec': cmp_spec(
        'Hardware vs Software Switcher', 'Real tradeoffs for church production',
        'Hardware (ATEM)', 'Software (vMix)',
        [
            ('Reliability',  'Very high', True,'PC dependent', None),
            ('Inputs',       'Fixed', False, 'Flexible', True),
            ('Graphics',     'Limited', False,'Full', True),
            ('ISO Rec',      'Some', None,   'Yes', True),
            ('Price',        '$300-$3K', None,'$60-$1200', None),
            ('Learning',     'Tactile', True,'Software', None),
        ],
    )},
    'kiloview-vs-magewell-church': {'subdir': SUB, 'spec': cmp_spec(
        'Kiloview vs Magewell', 'Budget vs pro church encoding',
        'Kiloview E2', 'Magewell Ultra',
        [
            ('Inputs',       'HDMI', None,   'HDMI + SDI', True),
            ('NDI In',       'Yes', True,    'Yes', True),
            ('SRT',          'Yes', True,    'Yes', True),
            ('Build',        'Plastic', None,'Metal', True),
            ('Price',        '~$500', True,  '~$800', False),
            ('Best For',     'Budget rigs', None,'Pro deploys', True),
        ],
    )},
    'magewell-vs-teradek-church-streaming': {'subdir': SUB, 'spec': cmp_spec(
        'Magewell vs Teradek', 'Pro streaming encoder comparison',
        'Magewell Ultra', 'Teradek VidiU Go',
        [
            ('Inputs',       'HDMI + SDI', True,'HDMI only', None),
            ('Bonding',      'No', False,    'Core cloud', True),
            ('Battery',      'No', False,    'Yes', True),
            ('SRT',          'Yes', True,    'Yes', True),
            ('Price',        '~$800', True,  '~$1,000', None),
            ('Best For',     'Fixed install', None,'Field / mobile', True),
        ],
    )},
    'obs-vs-streamlabs-church': {'subdir': SUB, 'spec': cmp_spec(
        'OBS vs Streamlabs', 'Free church streaming software',
        'OBS Studio', 'Streamlabs',
        [
            ('Cost',         'Free', True,   'Free + Pro', None),
            ('Performance',  'Lightest', True,'Heavier', False),
            ('Plugins',      'Massive', True,'Built-in', None),
            ('NDI',          'Plugin', True, 'Plugin', True),
            ('Setup',        'Manual', None, 'Wizards', True),
            ('Best For',     'Any church', True,'Beginners', None),
        ],
    )},
    'obs-vs-vmix-church-streaming': {'subdir': SUB, 'spec': cmp_spec(
        'OBS vs vMix', 'Software switcher showdown',
        'OBS Studio', 'vMix',
        [
            ('Cost',         'Free', True,   '$60-$1200', False),
            ('NDI',          'Plugin', True, 'Native', True),
            ('ISO Record',   'Plugin', None, 'Native', True),
            ('Instant Replay','No', False,   'Yes', True),
            ('Graphics',     'Basic', None,  'Pro CG', True),
            ('Learning',     'Gentle', True, 'Steeper', None),
        ],
    )},
    'obsbot-tail-air-vs-avkans-ptz': {'subdir': SUB, 'spec': cmp_spec(
        'OBSBOT Tail Air vs AVKANS', 'AI camera vs traditional PTZ',
        'OBSBOT Tail Air', 'AVKANS U100',
        [
            ('AI Tracking',  'Yes', True,    'No', False),
            ('Zoom',         '4x optical', False,'20x', True),
            ('NDI HX',       'Yes', True,    'Full NDI', True),
            ('Form',         'Compact', True,'Full PTZ', None),
            ('Price',        '~$499', None,  '~$400', True),
            ('Best For',     'Small sanct', True,'Multi-cam', None),
        ],
    )},
    'propresenter-vs-easyworship-church': {'subdir': SUB, 'spec': cmp_spec(
        'ProPresenter vs EasyWorship', 'Worship media software',
        'ProPresenter', 'EasyWorship',
        [
            ('Platform',     'Mac + Win', True,'Windows', False),
            ('Price',        '$399/yr', False,'$699 one-time', True),
            ('Library',      'Huge', True,   'Solid', None),
            ('NDI Out',      'Yes', True,    'Yes', True),
            ('Learning',     'Steeper', None,'Easier', True),
            ('Best For',     'Complex', True,'Simple', True),
        ],
    )},
    'restream-vs-castr-church': {'subdir': SUB, 'spec': cmp_spec(
        'Restream vs Castr', 'Church multistreaming platforms',
        'Restream', 'Castr',
        [
            ('Destinations', '30+', True,    '20+', True),
            ('Recording',    'Cloud', True,  'Cloud', True),
            ('Analytics',    'Yes', True,    'Yes', True),
            ('Price',        'From $19', None,'From $13', True),
            ('Reliability',  'High', True,   'High', True),
            ('Best For',     'Multi-platform', True,'Budget', True),
        ],
    )},
    'roland-v1hd-vs-kiloview-switcher': {'subdir': SUB, 'spec': cmp_spec(
        'Roland V-1HD vs Kiloview', 'HDMI switcher vs NDI converter',
        'Roland V-1HD', 'Kiloview NDI',
        [
            ('Form',         'Hardware', True,'NDI box', None),
            ('Inputs',       '4 HDMI', True, '1 HDMI in', False),
            ('T-Bar',        'Yes', True,    'No', False),
            ('NDI',          'No', False,    'Yes', True),
            ('Price',        '~$700', None,  '~$500', True),
            ('Best For',     'Hardware sw', None,'NDI workflows', True),
        ],
    )},
    'wirecast-vs-vmix-church': {'subdir': SUB, 'spec': cmp_spec(
        'Wirecast vs vMix', 'Pro software switching compared',
        'Wirecast', 'vMix',
        [
            ('Platform',     'Mac + Win', True,'Win only', False),
            ('NDI',          'Yes', True,    'Yes', True),
            ('ISO Record',   'Pro', True,    'Yes', True),
            ('Replay',       'Limited', None,'Full', True),
            ('Price',        '$695+', False, '$60-$1200', True),
            ('Stability',    'High', True,   'Very high', True),
        ],
    )},
    'yamaha-tf5-vs-behringer-x32-compact': {'subdir': SUB, 'spec': cmp_spec(
        'Yamaha TF5 vs X32 Compact', 'Mid-tier digital mixers for churches',
        'Yamaha TF5', 'X32 Compact',
        [
            ('Channels',     '48', True,     '40', True),
            ('Preamps',      'Yamaha D-PRE', True,'Midas', True),
            ('Touchscreen',  '7"', True,     '7"', True),
            ('Price',        '~$3,500', False,'~$2,000', True),
            ('Sound',        'Pristine', True,'Clean', True),
            ('Support',      'Yamaha', True, 'Behringer', None),
        ],
    )},
}


if __name__ == '__main__':
    run(ENTRIES)
