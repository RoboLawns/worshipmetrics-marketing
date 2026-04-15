#!/usr/bin/env python3
"""
Update all 35 troubleshooting MDX files with:
1. coverImage frontmatter
2. Hero <figure> after opening paragraph (before <ProductCTA>)
3. Diagram <figure> after <ProductCTA> (before first ## heading)
"""
import os
import re
import json

WORKTREE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(WORKTREE, "src", "content", "troubleshooting")
RESULTS_JSON = os.path.join(WORKTREE, "scripts", "image_results.json")

with open(RESULTS_JSON) as f:
    IMAGE_DATA = json.load(f)


def filename_to_alt(filename):
    """Convert image filename to SEO alt text."""
    name = os.path.splitext(filename)[0]
    # Remove trailing -church, -troubleshooting, -diagram patterns for cleaner alt
    parts = name.replace('-', ' ').strip()
    return parts.title()


def make_alt(filename, context_hint):
    """Generate descriptive alt text from filename + context."""
    name = os.path.splitext(filename)[0]
    words = name.split('-')
    # Build natural alt text
    return ' '.join(words).title()


def make_figure(img_path, width, height, alt, title, caption, is_hero=True):
    """Generate a <figure> element with full SEO attributes."""
    loading = "" if is_hero else '\n    loading="lazy"'
    return f'''<figure>
  <img
    src="{img_path}"
    alt="{alt}"
    title="{title}"
    width="{width}"
    height="{height}"{loading}
  />
  <figcaption>{caption}</figcaption>
</figure>'''


# Per-article image metadata for alt text and captions
ARTICLE_META = {
    "atem-mini-not-detected-computer": {
        "hero_alt": "Blackmagic ATEM Mini Pro video switcher for church production",
        "hero_title": "Blackmagic ATEM Mini Pro — compact live production switcher used in church AV setups",
        "hero_caption": "The Blackmagic ATEM Mini Pro is widely used in church livestreaming setups as a USB webcam and multi-camera switcher.",
        "diag_alt": "Blackmagic ATEM Mini rear panel showing HDMI inputs and USB output",
        "diag_title": "ATEM Mini rear panel — HDMI inputs 1–4, USB webcam output, and Ethernet port",
        "diag_caption": "The ATEM Mini rear panel: verify your computer is connected to the USB port (not HDMI), and that the device shows as a webcam in your OS.",
    },
    "atem-mini-usb-webcam-not-recognized": {
        "hero_alt": "Blackmagic ATEM Mini connected via USB as a webcam for church streaming",
        "hero_title": "Blackmagic ATEM Mini — USB webcam output for OBS and video conferencing",
        "hero_caption": "The ATEM Mini outputs as a USB webcam, allowing OBS, Zoom, and streaming software to use it as a capture device.",
        "diag_alt": "Blackmagic ATEM Mini USB webcam connection diagram showing cable routing",
        "diag_title": "ATEM Mini USB connection — correct cable from USB-C port to computer",
        "diag_caption": "Connect the ATEM Mini's USB-C port to your computer. The device should appear as 'Blackmagic Design' in your USB devices list.",
    },
    "audio-delay-video-stream-fix": {
        "hero_alt": "OBS Studio audio mixer showing sync offset controls",
        "hero_title": "OBS Studio audio mixer — use Advanced Audio Properties to set sync offset",
        "hero_caption": "OBS Studio's audio mixer lets you apply sync offset per source to compensate for audio/video delay in your church stream.",
        "diag_alt": "OBS Studio sources panel showing audio and video source layout",
        "diag_title": "OBS Studio source layout — audio and video sources with individual delay controls",
        "diag_caption": "In OBS, right-click any audio source and select 'Advanced Audio Properties' to set a sync offset in milliseconds.",
    },
    "avkans-camera-web-ui-not-loading": {
        "hero_alt": "AVKANS PTZ camera for church live streaming with network connectivity",
        "hero_title": "AVKANS PTZ Camera — PoE-powered IP camera with web UI management",
        "hero_caption": "The AVKANS PTZ camera is managed via a web browser interface. If the web UI won't load, the issue is typically a network or IP address conflict.",
        "diag_alt": "AVKANS PTZ camera network connection setup for web UI access",
        "diag_title": "AVKANS PTZ camera network configuration — same subnet required for web UI access",
        "diag_caption": "Your computer and the AVKANS camera must be on the same subnet (e.g., both 192.168.1.x) for the web UI to load. Check that no firewall is blocking port 80.",
    },
    "behringer-x32-usb-audio-not-working": {
        "hero_alt": "Behringer X32 digital mixing console for church audio",
        "hero_title": "Behringer X32 — 40-channel digital mixer used in church productions",
        "hero_caption": "The Behringer X32 is a popular digital mixer in church AV setups. USB audio requires correct routing configuration in the X32's setup menus.",
        "diag_alt": "Behringer X32 digital mixer showing USB routing and channel configuration",
        "diag_title": "Behringer X32 USB routing — configure USB return channels for computer audio",
        "diag_caption": "On the X32, go to Setup > USB/Card to verify USB audio routing. Assign the correct USB return channels to your mix bus for streaming.",
    },
    "camera-image-flickering-church": {
        "hero_alt": "AVKANS PTZ camera mounted in church for livestreaming",
        "hero_title": "AVKANS PTZ Camera — adjustable power frequency setting to eliminate flicker",
        "hero_caption": "Camera flicker is almost always caused by a mismatch between the camera's power frequency setting and your local power grid (50Hz vs 60Hz).",
        "diag_alt": "AVKANS PTZ camera settings panel showing power frequency configuration",
        "diag_title": "PTZ camera frequency setting — match to local power grid to eliminate flicker",
        "diag_caption": "In the AVKANS web UI, navigate to Image Settings and change the power frequency to match your region: 60Hz (Americas) or 50Hz (Europe/UK/Australia).",
    },
    "camera-lagging-behind-audio-stream": {
        "hero_alt": "Blackmagic ATEM Mini Pro live streaming switcher for church",
        "hero_title": "Blackmagic ATEM Mini Pro — live streaming with audio sync control",
        "hero_caption": "Camera lag behind audio is typically caused by encoding delay. The ATEM Mini and OBS both offer sync offset controls to compensate.",
        "diag_alt": "OBS Studio audio mixer with sync offset settings for camera lag compensation",
        "diag_title": "OBS Studio sync offset — correct camera lag by adding delay to audio sources",
        "diag_caption": "In OBS, right-click an audio source and go to Advanced Audio Properties. Increase the Sync Offset to delay audio until it matches your video.",
    },
    "church-network-bandwidth-streaming": {
        "hero_alt": "OBS Studio streaming interface for church network bandwidth management",
        "hero_title": "OBS Studio — configure bitrate and encoder settings for church network bandwidth",
        "hero_caption": "OBS Studio is the most common streaming software in church setups. Properly configuring the output bitrate is key to stable streaming on limited bandwidth.",
        "diag_alt": "OBS Studio output settings panel showing bitrate and encoder configuration",
        "diag_title": "OBS Studio output settings — bitrate and encoder settings for church network optimization",
        "diag_caption": "In OBS Settings > Output, lower your bitrate to 2500–3500 kbps if your church network is congested. This prevents dropped frames and stream disconnects.",
    },
    "crackle-popping-audio-church-stream": {
        "hero_alt": "Behringer X32 digital mixer for church audio with streaming mix",
        "hero_title": "Behringer X32 — digital audio mixer used for church livestream audio",
        "hero_caption": "Audio crackle and popping on the Behringer X32 is usually caused by buffer size mismatches, USB driver issues, or sample rate conflicts.",
        "diag_alt": "OBS Studio audio mixer showing bitrate and audio monitoring settings",
        "diag_title": "OBS Studio audio settings — correct bitrate and monitoring mode to eliminate crackling",
        "diag_caption": "In OBS Settings > Audio, make sure your sample rate (44.1kHz or 48kHz) matches the X32's sample rate. Mismatches cause persistent crackle and distortion.",
    },
    "echo-feedback-church-live-stream": {
        "hero_alt": "Behringer X32 digital mixer for church live stream feedback elimination",
        "hero_title": "Behringer X32 — use aux send routing to create a separate streaming mix without feedback",
        "hero_caption": "Echo and feedback in your livestream usually means your monitoring output is feeding back into your stream mix. The X32's bus routing can isolate these.",
        "diag_alt": "OBS Studio audio monitoring settings showing monitoring mode configuration",
        "diag_title": "OBS Studio audio monitoring — turn off Monitor and Output to prevent echo",
        "diag_caption": "In OBS Advanced Audio Properties, set each source's monitoring mode to 'Monitor Off' to prevent the stream output from feeding back through your speakers.",
    },
    "facebook-live-connection-failed-church": {
        "hero_alt": "OBS Studio interface for Facebook Live streaming from church",
        "hero_title": "OBS Studio — configure Facebook Live RTMP settings for church streaming",
        "hero_caption": "OBS Studio connects to Facebook Live via RTMP. Connection failures are usually caused by incorrect stream key or network issues.",
        "diag_alt": "OBS Studio stream settings panel showing Facebook Live RTMP configuration",
        "diag_title": "OBS Studio stream settings — Facebook Live server and stream key configuration",
        "diag_caption": "In OBS Settings > Stream, select 'Facebook Live' as the service. Always generate a fresh stream key from Facebook's Live Producer dashboard before each service.",
    },
    "hdmi-signal-dropping-church-setup": {
        "hero_alt": "Blackmagic ATEM Mini Pro HDMI video switcher for church production",
        "hero_title": "Blackmagic ATEM Mini — 4-input HDMI switcher used in church video production",
        "hero_caption": "HDMI signal drops on the ATEM Mini are commonly caused by cable quality, length, or incompatible resolutions between the camera and switcher.",
        "diag_alt": "Blackmagic ATEM Mini HDMI connection diagram showing camera-to-switcher cabling",
        "diag_title": "ATEM Mini HDMI connections — correct camera-to-switcher cable routing",
        "diag_caption": "Each HDMI input on the ATEM Mini requires a quality cable under 5 metres. Verify both the camera and switcher are set to the same resolution (e.g., 1080p 30fps).",
    },
    "high-latency-stream-viewers-church": {
        "hero_alt": "OBS Studio streaming interface showing latency and buffer settings",
        "hero_title": "OBS Studio — configure low-latency streaming settings for church broadcasts",
        "hero_caption": "High viewer latency (30+ seconds) is typically caused by YouTube's default DVR buffer. Switching to 'Ultra-low latency' mode reduces this significantly.",
        "diag_alt": "OBS Studio output settings showing keyframe interval configuration for low latency",
        "diag_title": "OBS Studio output settings — set keyframe interval to 2 seconds for low-latency streaming",
        "diag_caption": "In OBS Settings > Output, set the Keyframe Interval to 2 seconds. This is required for YouTube's low-latency mode to work correctly.",
    },
    "kiloview-encoder-web-ui-password": {
        "hero_alt": "Kiloview N2 portable wireless NDI encoder for church streaming",
        "hero_title": "Kiloview N2 — wireless HDMI to NDI encoder with web-based management interface",
        "hero_caption": "The Kiloview N2 is managed via a web browser interface. The default login credentials and IP reset procedure are covered in this guide.",
        "diag_alt": "Kiloview N2 NDI encoder network connection and IP configuration diagram",
        "diag_title": "Kiloview N2 network setup — find the encoder's IP to access the web UI",
        "diag_caption": "Connect the Kiloview N2 to your network via Ethernet or Wi-Fi. Use your router's DHCP client list to find its assigned IP address, then open it in a browser.",
    },
    "magewell-encoder-not-streaming": {
        "hero_alt": "Magewell Ultra Encode HDMI hardware encoder for church streaming",
        "hero_title": "Magewell Ultra Encode HDMI — standalone hardware encoder for church livestreaming",
        "hero_caption": "The Magewell Ultra Encode HDMI is a standalone hardware encoder that requires correct RTMP/SRT configuration and a stable network connection to stream.",
        "diag_alt": "Magewell Ultra Encode HDMI web interface showing streaming configuration panel",
        "diag_title": "Magewell Ultra Encode web UI — configure RTMP server URL and stream key here",
        "diag_caption": "Access the Magewell web interface by navigating to its IP address. Under 'Publish Streams', verify the RTMP URL format and stream key match your platform's settings.",
    },
    "mixer-usb-not-recognized-computer": {
        "hero_alt": "Behringer X32 digital mixer USB audio interface for computer recording",
        "hero_title": "Behringer X32 — USB audio interface mode for direct computer recording and streaming",
        "hero_caption": "The Behringer X32 doubles as a USB audio interface, but requires the correct USB routing configuration and driver installation on Windows.",
        "diag_alt": "Behringer X32 USB audio connection diagram showing routing to computer",
        "diag_title": "Behringer X32 USB routing — configure card outputs for computer audio interface use",
        "diag_caption": "On the X32, navigate to Setup > Card and verify that USB is selected as the card type. Your computer should then recognise the X32 as an audio interface.",
    },
    "multistream-one-platform-failing": {
        "hero_alt": "OBS Studio multistream setup for simultaneous YouTube and Facebook streaming",
        "hero_title": "OBS Studio — configure multiple RTMP outputs for simultaneous platform streaming",
        "hero_caption": "OBS Studio 30+ supports native multistream to send your church service to YouTube, Facebook, and other platforms simultaneously.",
        "diag_alt": "OBS Studio stream settings showing RTMP server configuration for multistream",
        "diag_title": "OBS Studio multistream RTMP settings — configure each platform with correct server and key",
        "diag_caption": "In OBS Settings > Stream, enable 'Multiple RTMP Outputs'. Add each platform's RTMP server URL and stream key separately to stream to all platforms at once.",
    },
    "ndi-camera-not-showing-obs-vmix": {
        "hero_alt": "AVKANS PTZ NDI camera for church live streaming with OBS or vMix",
        "hero_title": "AVKANS PTZ NDI Camera — configure NDI output for OBS and vMix discovery",
        "hero_caption": "NDI cameras must be on the same network subnet as OBS or vMix for automatic discovery to work. Firewall settings are a common cause of missing NDI sources.",
        "diag_alt": "OBS Studio NDI source selection showing camera discovery configuration",
        "diag_title": "OBS Studio NDI source — NDI camera must appear in Source Properties to be used",
        "diag_caption": "In OBS, add a new source and select 'NDI Source'. If your AVKANS camera doesn't appear in the dropdown, verify both devices are on the same network subnet.",
    },
    "ndi-not-working-church-network": {
        "hero_alt": "AVKANS PTZ camera NDI network configuration for church AV setup",
        "hero_title": "AVKANS PTZ Camera — NDI requires all devices on the same network subnet",
        "hero_caption": "NDI uses multicast discovery which only works within a single network subnet. VLANs and subnet boundaries will block NDI discovery.",
        "diag_alt": "Kiloview N2 NDI encoder network topology diagram showing device connectivity",
        "diag_title": "NDI network topology — all NDI devices must be on the same VLAN and subnet",
        "diag_caption": "For reliable NDI, put all cameras, encoders, and production computers on the same wired Ethernet switch with no VLAN separation between them.",
    },
    "no-audio-youtube-facebook-stream": {
        "hero_alt": "OBS Studio audio mixer showing no audio output configuration",
        "hero_title": "OBS Studio audio mixer — troubleshoot missing audio on YouTube and Facebook streams",
        "hero_caption": "No audio on your stream is usually caused by OBS capturing the wrong audio device or the audio track not being enabled for the stream output.",
        "diag_alt": "OBS Studio audio sources panel showing track selection and monitoring mode",
        "diag_title": "OBS Studio audio track selection — verify audio tracks are enabled for stream output",
        "diag_caption": "In OBS Settings > Output > Recording, verify that audio Track 1 is checked. Then in the mixer, confirm your audio sources are not muted and showing signal.",
    },
    "obs-black-screen-church-stream": {
        "hero_alt": "OBS Studio interface showing black screen display capture configuration",
        "hero_title": "OBS Studio — fix black screen by changing capture mode from Display to Window Capture",
        "hero_caption": "OBS black screen on Display Capture is extremely common and is usually fixed by switching to Window Capture or changing the graphics adapter setting.",
        "diag_alt": "OBS Studio sources panel showing capture mode options for black screen fix",
        "diag_title": "OBS Studio sources — switch from Display Capture to Window Capture to fix black screen",
        "diag_caption": "Right-click the black Display Capture source, select Properties, and try selecting a different display. Or delete it and add a Window Capture source instead.",
    },
    "obs-not-connecting-twitch-youtube": {
        "hero_alt": "OBS Studio stream connection settings for YouTube and Twitch",
        "hero_title": "OBS Studio — troubleshoot RTMP connection failures to YouTube and Twitch",
        "hero_caption": "Connection failures in OBS are typically caused by an expired stream key, network firewall blocking RTMP port 1935, or an incorrect server URL.",
        "diag_alt": "OBS Studio stream service settings panel showing server and stream key fields",
        "diag_title": "OBS Studio stream settings — correct service, server, and stream key configuration",
        "diag_caption": "In OBS Settings > Stream, select your platform from the Service dropdown. Always use 'Get Stream Key' to generate a fresh key rather than reusing an old one.",
    },
    "propresenter-ndi-output-not-visible": {
        "hero_alt": "ProPresenter 7 worship presentation software interface",
        "hero_title": "ProPresenter 7 — industry-leading worship presentation software with NDI output support",
        "hero_caption": "ProPresenter 7 can send its output as an NDI source, allowing OBS, vMix, and other software to receive the presentation over the network.",
        "diag_alt": "ProPresenter 7 live production workflow in a church environment",
        "diag_title": "ProPresenter in live church production — configure NDI output settings correctly",
        "diag_caption": "Enable NDI output in ProPresenter under Preferences > Network. After enabling, restart ProPresenter and look for it as 'ProPresenter' in your NDI source list.",
    },
    "ptz-camera-losing-ip-address": {
        "hero_alt": "AVKANS PTZ camera with static IP configuration for church network",
        "hero_title": "AVKANS PTZ Camera — assign a static IP to prevent address changes after reboot",
        "hero_caption": "PTZ cameras that lose their IP address on reboot are using DHCP. Assigning a static IP ensures the camera is always reachable at the same address.",
        "diag_alt": "PTZ camera static IP network settings diagram showing configuration fields",
        "diag_title": "PTZ camera static IP setup — configure IP, subnet mask, and gateway in web UI",
        "diag_caption": "In the PTZ camera's web UI, go to Network Settings and switch from DHCP to Static. Assign an IP outside your router's DHCP range (e.g., 192.168.1.200) to avoid conflicts.",
    },
    "ptz-camera-not-connecting-network": {
        "hero_alt": "AVKANS PTZ camera network connection troubleshooting for church setup",
        "hero_title": "AVKANS PTZ Camera — diagnose and fix network connection failures",
        "hero_caption": "PTZ cameras that won't connect to the network are usually on the wrong subnet, have a static IP conflict, or are connected to an unmanaged switch without PoE.",
        "diag_alt": "PTZ camera network connection diagram showing switch and computer connectivity",
        "diag_title": "PTZ camera network setup — camera and computer must be on the same subnet",
        "diag_caption": "Connect the PTZ camera to the same network switch as your production computer. Both must be on the same subnet (e.g., 192.168.1.x) to communicate.",
    },
    "ptz-preset-not-recalling-correctly": {
        "hero_alt": "AVKANS PTZ camera preset recall and position control for church production",
        "hero_title": "AVKANS PTZ Camera — configure preset speed and position for accurate recall",
        "hero_caption": "PTZ presets that overshoot or stop in the wrong position are usually caused by incorrect preset speed settings or mechanical calibration issues.",
        "diag_alt": "PTZ camera preset configuration panel showing speed and position settings",
        "diag_title": "PTZ preset speed settings — lower preset speed for more accurate position recall",
        "diag_caption": "In the PTZ camera's web UI, reduce the preset movement speed to 50% or lower. Slower movement gives the camera time to decelerate and stop precisely at the saved position.",
    },
    "roland-v1hd-no-video-output": {
        "hero_alt": "Roland V-1HD video switcher for church live production",
        "hero_title": "Roland V-1HD — 4-input HD video switcher with HDMI outputs for church production",
        "hero_caption": "The Roland V-1HD is a compact 4-input video switcher. No video output is typically caused by an incorrect output format, wrong output mode, or HDMI handshake failure.",
        "diag_alt": "Roland V-1HD rear panel diagram showing HDMI inputs and output connections",
        "diag_title": "Roland V-1HD rear panel — verify HDMI cables are in inputs 1–4 and program output is correct",
        "diag_caption": "Check the V-1HD rear panel: the PROGRAM OUT HDMI should connect to your display or capture card. Verify the output resolution matches what your display supports (1080p 60fps).",
    },
    "stream-dropping-frames-church": {
        "hero_alt": "OBS Studio showing dropped frames warning in status bar",
        "hero_title": "OBS Studio — diagnose and fix dropped frames during church livestreaming",
        "hero_caption": "Dropped frames in OBS indicate your PC or network can't keep up with the encoder. The status bar shows the percentage of dropped frames in real time.",
        "diag_alt": "OBS Studio encoder performance settings showing CPU usage and bitrate configuration",
        "diag_title": "OBS Studio encoder settings — switch to hardware encoding to reduce dropped frames",
        "diag_caption": "In OBS Settings > Output, change the encoder from x264 (CPU) to NVENC or AMF (GPU hardware encoding) to drastically reduce CPU load and dropped frames.",
    },
    "stream-key-invalid-church-fix": {
        "hero_alt": "OBS Studio stream key invalid error and connection settings",
        "hero_title": "OBS Studio — fix invalid stream key errors for YouTube and other platforms",
        "hero_caption": "An invalid stream key error means OBS connected to the platform's server but was rejected. The key is expired, incorrect, or copied with extra spaces.",
        "diag_alt": "OBS Studio stream settings panel showing stream key field and service configuration",
        "diag_title": "OBS Studio stream key — paste key from YouTube Studio and verify no extra spaces",
        "diag_caption": "In OBS Settings > Stream, click 'Get Stream Key' to open your platform's dashboard. Copy the key, paste into Notepad first to remove hidden characters, then paste into OBS.",
    },
    "streaming-mix-too-loud-quiet": {
        "hero_alt": "Behringer X32 digital mixer streaming audio mix level configuration",
        "hero_title": "Behringer X32 — configure a separate streaming mix at the correct level",
        "hero_caption": "Your streaming mix should be independent of your house mix. The X32's matrix or auxilary outputs let you control stream levels without affecting the room sound.",
        "diag_alt": "OBS Studio audio mixer showing volume levels and streaming output configuration",
        "diag_title": "OBS Studio audio levels — target -14 LUFS for streaming, monitor with VU meters",
        "diag_caption": "In OBS, aim for audio peaks around -12 to -6 dB on the mixer. The streaming platform (YouTube, Facebook) will apply its own normalization, so avoid clipping.",
    },
    "streaming-pc-dropping-connection": {
        "hero_alt": "OBS Studio streaming PC network connection settings and auto-reconnect",
        "hero_title": "OBS Studio — enable auto-reconnect to recover from network drops automatically",
        "hero_caption": "A streaming PC that keeps disconnecting usually has a network issue, overloaded CPU, or insufficient upload bandwidth. OBS auto-reconnect can recover brief outages.",
        "diag_alt": "OBS Studio auto-reconnect and network settings configuration panel",
        "diag_title": "OBS Studio auto-reconnect settings — enable with 10 second timeout and 20 retries",
        "diag_caption": "In OBS Settings > Output > Streaming, enable Auto-Reconnect with a 10-second timeout and at least 10 retry attempts to automatically recover from brief network drops.",
    },
    "teradek-vidiu-x-stream-failing": {
        "hero_alt": "Teradek VidiU X hardware encoder for church live streaming",
        "hero_title": "Teradek VidiU X — standalone hardware encoder for YouTube and RTMP streaming",
        "hero_caption": "The Teradek VidiU X is a hardware encoder that streams directly without a PC. Connection failures are usually RTMP configuration or network issues.",
        "diag_alt": "Teradek VidiU X rear panel showing HDMI input and Ethernet connection",
        "diag_title": "Teradek VidiU X connections — HDMI input from camera, Ethernet for reliable streaming",
        "diag_caption": "Always connect the Teradek VidiU X via Ethernet rather than Wi-Fi for reliable streaming. Access the web UI at its IP address to verify RTMP server URL and stream key.",
    },
    "vlan-setup-av-streaming-church": {
        "hero_alt": "AVKANS PTZ camera in church VLAN network architecture for AV streaming",
        "hero_title": "Church AV VLAN setup — isolate PTZ cameras and streaming PC on a dedicated network segment",
        "hero_caption": "A dedicated VLAN for church AV equipment prevents congregation Wi-Fi from competing with your streaming bandwidth and NDI traffic.",
        "diag_alt": "Church AV VLAN network architecture diagram showing switch configuration",
        "diag_title": "Church AV VLAN topology — separate AV equipment from general congregation network",
        "diag_caption": "A basic AV VLAN puts your PTZ cameras, streaming PC, and NDI encoders on ports 1–4 of a managed switch, while congregation Wi-Fi and staff computers use ports 5+.",
    },
    "vmix-inputs-not-displaying": {
        "hero_alt": "vMix software interface showing live inputs and production layout",
        "hero_title": "vMix — professional live production software with multi-input support",
        "hero_caption": "vMix inputs showing black screens are usually caused by HDMI resolution mismatches, wrong input device selection, or HDCP copy protection on the source.",
        "diag_alt": "vMix software input configuration panel showing device and resolution settings",
        "diag_title": "vMix input properties — match resolution and device to fix black screen inputs",
        "diag_caption": "Double-click any black input in vMix to open its properties. Verify the correct HDMI port is selected and that the resolution matches your source device's output format.",
    },
    "youtube-stream-offline-mid-service": {
        "hero_alt": "OBS Studio YouTube stream recovery and auto-reconnect configuration",
        "hero_title": "OBS Studio — recover from mid-service YouTube stream outages in under 30 seconds",
        "hero_caption": "When YouTube shows 'Stream Offline' mid-service, OBS auto-reconnect can recover automatically. Manual restart takes 10–15 seconds if auto-reconnect isn't enabled.",
        "diag_alt": "OBS Studio auto-reconnect and YouTube stream settings configuration",
        "diag_title": "OBS Studio auto-reconnect settings — configure for YouTube stream recovery",
        "diag_caption": "Enable OBS auto-reconnect in Settings > Output > Streaming. Set timeout to 10s, delay to 2s, and max attempts to 20 so OBS recovers from YouTube outages without intervention.",
    },
}


def update_mdx(slug, hero_data, diag_data):
    """Update a single MDX file with cover image and figure elements."""
    mdx_path = os.path.join(CONTENT_DIR, f"{slug}.mdx")
    if not os.path.exists(mdx_path):
        print(f"  SKIP (not found): {mdx_path}")
        return False

    with open(mdx_path, 'r', encoding='utf-8') as f:
        content = f.read()

    meta = ARTICLE_META.get(slug, {})
    if not meta:
        print(f"  WARN: No metadata for {slug}, skipping")
        return False

    hero_path = hero_data["path"]
    hero_w, hero_h = hero_data["size"]
    diag_path = diag_data["path"]
    diag_w, diag_h = diag_data["size"]

    # ── 1. Add coverImage to frontmatter ─────────────────────────────────
    # Find the second --- (end of frontmatter)
    fm_end = content.find('\n---', 4)  # skip first ---
    if fm_end == -1:
        print(f"  FAIL: Could not find frontmatter end in {slug}")
        return False

    # Check if coverImage already exists
    if 'coverImage:' in content[:fm_end]:
        print(f"  INFO: coverImage already exists in {slug}, updating")
        content = re.sub(r'coverImage:.*', f'coverImage: "{hero_path}"', content)
    else:
        # Insert before closing ---
        insert_pos = fm_end
        content = content[:insert_pos] + f'\ncoverImage: "{hero_path}"' + content[insert_pos:]
        # Update fm_end position
        fm_end = content.find('\n---', 4)

    # ── 2. Build figure elements ──────────────────────────────────────────
    hero_figure = make_figure(
        hero_path, hero_w, hero_h,
        meta["hero_alt"], meta["hero_title"], meta["hero_caption"],
        is_hero=True
    )
    diag_figure = make_figure(
        diag_path, diag_w, diag_h,
        meta["diag_alt"], meta["diag_title"], meta["diag_caption"],
        is_hero=False
    )

    # ── 3. Find insertion points ──────────────────────────────────────────
    # Find <ProductCTA line
    product_cta_match = re.search(r'<ProductCTA[^/]*/>', content)
    if not product_cta_match:
        print(f"  FAIL: Could not find <ProductCTA/> in {slug}")
        return False

    cta_start = product_cta_match.start()
    cta_end = product_cta_match.end()

    # Find the first ## heading after the ProductCTA
    first_heading_match = re.search(r'\n## ', content[cta_end:])
    if not first_heading_match:
        print(f"  FAIL: Could not find first ## heading after ProductCTA in {slug}")
        return False

    first_heading_pos = cta_end + first_heading_match.start()

    # ── 4. Skip if already enriched ──────────────────────────────────────
    if '<figure>' in content:
        print(f"  INFO: Already has <figure> in {slug}, skipping body insertion")
        # Still update coverImage (already done above), write the file
        with open(mdx_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        return True

    # ── 5. Insert diagram figure before first ## heading ─────────────────
    # Insert diagram between ProductCTA and first heading
    before_heading = content[:first_heading_pos]
    after_heading = content[first_heading_pos:]
    content = before_heading + '\n\n' + diag_figure + '\n' + after_heading

    # Recalculate CTA position after insertion
    product_cta_match = re.search(r'<ProductCTA[^/]*/>', content)
    cta_start = product_cta_match.start()

    # ── 6. Insert hero figure before ProductCTA ───────────────────────────
    # Find text immediately before the ProductCTA (end of opening paragraph)
    before_cta = content[:cta_start]
    after_cta = content[cta_start:]

    # Ensure proper spacing
    content = before_cta.rstrip() + '\n\n' + hero_figure + '\n\n' + after_cta

    # Write updated file
    with open(mdx_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

    print(f"  OK: {slug}")
    return True


def main():
    print(f"\n=== Updating MDX files ===\n")
    success = 0
    failed = 0
    for slug, data in IMAGE_DATA.items():
        hero = data.get("hero")
        diagram = data.get("diagram")
        if not hero or not diagram:
            print(f"[{slug}] SKIP: missing hero or diagram data")
            failed += 1
            continue
        print(f"[{slug}]")
        ok = update_mdx(slug, hero, diagram)
        if ok:
            success += 1
        else:
            failed += 1

    print(f"\n=== SUMMARY ===")
    print(f"Updated: {success}")
    print(f"Failed/Skipped: {failed}")


if __name__ == "__main__":
    main()
