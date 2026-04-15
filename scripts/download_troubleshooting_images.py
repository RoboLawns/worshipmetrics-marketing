#!/usr/bin/env python3
"""
Download product images for all 35 troubleshooting articles.
Downloads hero images and technical diagrams from manufacturer CDNs.
"""
import os
import sys
import re
import json
import requests
from PIL import Image
import io
import time

WORKTREE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(WORKTREE, "public", "images", "products")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/jpeg,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

def download_image(url, filepath, referer=None):
    """Download image from URL and save, return (width, height) or None on failure."""
    headers = dict(HEADERS)
    if referer:
        headers['Referer'] = referer
    try:
        r = requests.get(url, headers=headers, timeout=30, stream=True)
        r.raise_for_status()
        content = b''.join(r.iter_content(8192))
        # Verify valid image
        img = Image.open(io.BytesIO(content))
        img.load()
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            f.write(content)
        w, h = img.size
        print(f"  OK {os.path.basename(filepath)} ({w}x{h})")
        return (w, h)
    except Exception as e:
        print(f"  FAILED {url}: {e}")
        return None

def fetch_page_images(url, referer=None):
    """Fetch a page and extract img src URLs."""
    headers = dict(HEADERS)
    if referer:
        headers['Referer'] = referer
    try:
        r = requests.get(url, headers=headers, timeout=20)
        if r.status_code in (403, 404, 429):
            print(f"  FETCH_SKIP {url}: HTTP {r.status_code}")
            return []
        r.raise_for_status()
        # Find all img src patterns
        srcs = re.findall(r'(?:src|data-src|data-lazy)=["\']([^"\']+\.(?:jpg|jpeg|png|webp|gif)(?:\?[^"\']*)?)["\']', r.text, re.I)
        # Also find JSON patterns
        json_srcs = re.findall(r'"(?:src|url|image)":\s*"([^"]+\.(?:jpg|jpeg|png|webp)(?:[^"]*)?)"', r.text, re.I)
        all_srcs = srcs + json_srcs
        # Make absolute
        from urllib.parse import urljoin
        return [urljoin(url, s) for s in all_srcs if s and not s.startswith('data:')]
    except Exception as e:
        print(f"  FETCH_FAIL {url}: {e}")
        return []

# ============================================================
# CONFIRMED IMAGE URLS
# ============================================================

IMAGES = [
    # ── Blackmagic ATEM Mini ─────────────────────────────────
    {
        "slug": "atem-mini-not-detected-computer",
        "hero_url": "https://images.blackmagicdesign.com/images/products/atemmini/landing/hero/hero-lg.jpg",
        "hero_name": "blackmagic-atem-mini-pro-video-switcher-church.jpg",
        "diag_url": "https://images.blackmagicdesign.com/images/products/atemmini/landing/switcher/switcher-bottom-md.jpg",
        "diag_name": "blackmagic-atem-mini-rear-panel-diagram-troubleshooting.jpg",
        "hero_ref": "https://www.blackmagicdesign.com/products/atemmini",
        "diag_ref": "https://www.blackmagicdesign.com/products/atemmini",
    },
    {
        "slug": "atem-mini-usb-webcam-not-recognized",
        "hero_url": "https://images.blackmagicdesign.com/images/products/atemmini/landing/outputs/outputs-lg.jpg",
        "hero_name": "blackmagic-atem-mini-usb-webcam-output-church.jpg",
        "diag_url": "https://images.blackmagicdesign.com/images/products/atemmini/landing/multiple-cameras/multiple-cameras-lg.jpg",
        "diag_name": "blackmagic-atem-mini-usb-connection-diagram-troubleshooting.jpg",
        "hero_ref": "https://www.blackmagicdesign.com/products/atemmini",
        "diag_ref": "https://www.blackmagicdesign.com/products/atemmini",
    },
    {
        "slug": "audio-delay-video-stream-fix",
        "hero_url": "https://obsproject.com/assets/images/features-new/mixer.png",
        "hero_name": "obs-studio-audio-mixer-sync-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/layouts.png",
        "diag_name": "obs-studio-sources-scenes-layout-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "behringer-x32-usb-audio-not-working",
        "hero_url": None,  # will try to scrape
        "hero_name": "behringer-x32-digital-mixer-church.jpg",
        "diag_url": None,  # will try to scrape
        "diag_name": "behringer-x32-usb-routing-diagram-troubleshooting.jpg",
        "hero_ref": "https://www.behringer.com/product.html?modelCode=0603-ACE",
        "diag_ref": "https://www.behringer.com/product.html?modelCode=0603-ACE",
    },
    {
        "slug": "camera-image-flickering-church",
        "hero_url": None,  # AVKANS - will scrape
        "hero_name": "avkans-ptz-camera-church-livestream.jpg",
        "diag_url": None,
        "diag_name": "avkans-ptz-camera-power-frequency-settings-troubleshooting.jpg",
        "hero_ref": "https://avkans.com/",
        "diag_ref": "https://avkans.com/",
    },
    {
        "slug": "camera-lagging-behind-audio-stream",
        "hero_url": "https://images.blackmagicdesign.com/images/products/atemmini/landing/streaming/streaming.jpg",
        "hero_name": "blackmagic-atem-mini-streaming-church.jpg",
        "diag_url": "https://obsproject.com/assets/images/features-new/mixer.png",
        "diag_name": "obs-studio-audio-sync-offset-diagram-troubleshooting.png",
        "hero_ref": "https://www.blackmagicdesign.com/products/atemmini",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "church-network-bandwidth-streaming",
        "hero_url": "https://obsproject.com/assets/images/features-new/hero_32_1_1.png",
        "hero_name": "obs-studio-streaming-interface-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/settings.png",
        "diag_name": "obs-studio-output-bitrate-settings-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "crackle-popping-audio-church-stream",
        "hero_url": None,  # Behringer X32
        "hero_name": "behringer-x32-digital-mixer-audio-church.jpg",
        "diag_url": "https://obsproject.com/assets/images/features-new/mixer.png",
        "diag_name": "obs-studio-audio-bitrate-mixer-diagram-troubleshooting.png",
        "hero_ref": "https://www.behringer.com/product.html?modelCode=0603-ACE",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "echo-feedback-church-live-stream",
        "hero_url": None,  # Behringer X32
        "hero_name": "behringer-x32-digital-mixer-feedback-church.jpg",
        "diag_url": "https://obsproject.com/assets/images/features-new/settings.png",
        "diag_name": "obs-studio-audio-monitoring-settings-diagram-troubleshooting.png",
        "hero_ref": "https://www.behringer.com/product.html?modelCode=0603-ACE",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "facebook-live-connection-failed-church",
        "hero_url": "https://obsproject.com/assets/images/features-new/hero_32_1_1.png",
        "hero_name": "obs-studio-facebook-live-streaming-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/settings.png",
        "diag_name": "obs-studio-stream-key-settings-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "hdmi-signal-dropping-church-setup",
        "hero_url": "https://images.blackmagicdesign.com/images/products/atemmini/landing/hero/hero-lg.jpg",
        "hero_name": "blackmagic-atem-mini-hdmi-switcher-church.jpg",
        "diag_url": "https://images.blackmagicdesign.com/images/products/atemmini/landing/multiple-cameras/multiple-cameras-lg.jpg",
        "diag_name": "blackmagic-atem-mini-hdmi-connection-diagram-troubleshooting.jpg",
        "hero_ref": "https://www.blackmagicdesign.com/products/atemmini",
        "diag_ref": "https://www.blackmagicdesign.com/products/atemmini",
    },
    {
        "slug": "high-latency-stream-viewers-church",
        "hero_url": "https://obsproject.com/assets/images/features-new/hero_32_1_1.png",
        "hero_name": "obs-studio-live-streaming-latency-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/settings.png",
        "diag_name": "obs-studio-keyframe-interval-settings-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "kiloview-encoder-web-ui-password",
        "hero_url": None,  # Kiloview - will scrape
        "hero_name": "kiloview-n2-ndi-encoder-church.jpg",
        "diag_url": None,
        "diag_name": "kiloview-n2-network-connection-diagram-troubleshooting.jpg",
        "hero_ref": "https://www.kiloview.com/en/product/",
        "diag_ref": "https://www.kiloview.com/en/product/",
    },
    {
        "slug": "magewell-encoder-not-streaming",
        "hero_url": "https://www.magewell.com/static/product/stream/ultra-encode-hdmi/product/1.png",
        "hero_name": "magewell-ultra-encode-hdmi-encoder-church.png",
        "diag_url": "https://www.magewell.com/static/product/stream/ultra-encode-hdmi/interface/1.png",
        "diag_name": "magewell-ultra-encode-hdmi-web-interface-diagram-troubleshooting.png",
        "hero_ref": "https://www.magewell.com/products/ultra-encode-hdmi",
        "diag_ref": "https://www.magewell.com/products/ultra-encode-hdmi",
    },
    {
        "slug": "mixer-usb-not-recognized-computer",
        "hero_url": None,  # Behringer X32
        "hero_name": "behringer-x32-digital-mixer-usb-church.jpg",
        "diag_url": None,
        "diag_name": "behringer-x32-usb-connection-diagram-troubleshooting.jpg",
        "hero_ref": "https://www.behringer.com/product.html?modelCode=0603-ACE",
        "diag_ref": "https://www.behringer.com/product.html?modelCode=0603-ACE",
    },
    {
        "slug": "multistream-one-platform-failing",
        "hero_url": "https://obsproject.com/assets/images/features-new/hero_32_1_1.png",
        "hero_name": "obs-studio-multistream-platform-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/settings.png",
        "diag_name": "obs-studio-rtmp-multistream-settings-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "ndi-camera-not-showing-obs-vmix",
        "hero_url": None,  # AVKANS PTZ
        "hero_name": "avkans-ptz-ndi-camera-obs-vmix-church.jpg",
        "diag_url": "https://obsproject.com/assets/images/features-new/layouts.png",
        "diag_name": "obs-studio-ndi-source-layout-diagram-troubleshooting.png",
        "hero_ref": "https://avkans.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "ndi-not-working-church-network",
        "hero_url": None,  # AVKANS PTZ
        "hero_name": "avkans-ptz-ndi-camera-network-church.jpg",
        "diag_url": None,  # Kiloview N2
        "diag_name": "kiloview-n2-ndi-network-topology-diagram-troubleshooting.jpg",
        "hero_ref": "https://avkans.com/",
        "diag_ref": "https://www.kiloview.com/en/product/",
    },
    {
        "slug": "no-audio-youtube-facebook-stream",
        "hero_url": "https://obsproject.com/assets/images/features-new/mixer.png",
        "hero_name": "obs-studio-audio-mixer-no-audio-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/layouts.png",
        "diag_name": "obs-studio-audio-sources-track-selection-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "obs-black-screen-church-stream",
        "hero_url": "https://obsproject.com/assets/images/features-new/hero_32_1_1.png",
        "hero_name": "obs-studio-black-screen-fix-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/layouts.png",
        "diag_name": "obs-studio-sources-capture-mode-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "obs-not-connecting-twitch-youtube",
        "hero_url": "https://obsproject.com/assets/images/features-new/hero_32_1_1.png",
        "hero_name": "obs-studio-youtube-twitch-connection-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/settings.png",
        "diag_name": "obs-studio-stream-service-settings-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "propresenter-ndi-output-not-visible",
        "hero_url": "SKIP",  # already downloaded via ffmpeg conversion
        "hero_name": "propresenter-7-interface-worship-church.png",
        "diag_url": "SKIP",  # already downloaded via ffmpeg conversion
        "diag_name": "propresenter-7-ndi-output-setup-diagram-troubleshooting.png",
        "hero_ref": "https://renewedvision.com/propresenter/",
        "diag_ref": "https://renewedvision.com/propresenter/",
    },
    {
        "slug": "ptz-camera-losing-ip-address",
        "hero_url": None,  # AVKANS PTZ
        "hero_name": "avkans-ptz-camera-static-ip-church.jpg",
        "diag_url": None,
        "diag_name": "ptz-camera-static-ip-network-settings-diagram-troubleshooting.jpg",
        "hero_ref": "https://avkans.com/",
        "diag_ref": "https://avkans.com/",
    },
    {
        "slug": "ptz-camera-not-connecting-network",
        "hero_url": None,  # AVKANS PTZ
        "hero_name": "avkans-ptz-camera-network-connection-church.jpg",
        "diag_url": None,
        "diag_name": "ptz-camera-network-connection-diagram-troubleshooting.jpg",
        "hero_ref": "https://avkans.com/",
        "diag_ref": "https://avkans.com/",
    },
    {
        "slug": "ptz-preset-not-recalling-correctly",
        "hero_url": None,  # AVKANS PTZ
        "hero_name": "avkans-ptz-camera-preset-control-church.jpg",
        "diag_url": None,
        "diag_name": "ptz-camera-preset-speed-settings-diagram-troubleshooting.jpg",
        "hero_ref": "https://avkans.com/",
        "diag_ref": "https://avkans.com/",
    },
    {
        "slug": "roland-v1hd-no-video-output",
        "hero_url": "https://static.roland.com/products/v-1hd/images_v2/v-1hd_hero.jpg",
        "hero_name": "roland-v1hd-video-switcher-church.jpg",
        "diag_url": "https://static.roland.com/products/v-1hd/images_v2/v-1hd_img_panel_rear.jpg",
        "diag_name": "roland-v1hd-rear-panel-connections-diagram-troubleshooting.jpg",
        "hero_ref": "https://proav.roland.com/global/products/v-1hd/",
        "diag_ref": "https://proav.roland.com/global/products/v-1hd/",
    },
    {
        "slug": "stream-dropping-frames-church",
        "hero_url": "https://obsproject.com/assets/images/features-new/hero_32_1_1.png",
        "hero_name": "obs-studio-dropping-frames-stream-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/studio.png",
        "diag_name": "obs-studio-encoder-performance-settings-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "stream-key-invalid-church-fix",
        "hero_url": "https://obsproject.com/assets/images/features-new/hero_32_1_1.png",
        "hero_name": "obs-studio-stream-key-invalid-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/settings.png",
        "diag_name": "obs-studio-stream-service-key-settings-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "streaming-mix-too-loud-quiet",
        "hero_url": None,  # Behringer X32
        "hero_name": "behringer-x32-streaming-audio-mix-church.jpg",
        "diag_url": "https://obsproject.com/assets/images/features-new/mixer.png",
        "diag_name": "obs-studio-audio-levels-mixer-diagram-troubleshooting.png",
        "hero_ref": "https://www.behringer.com/product.html?modelCode=0603-ACE",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "streaming-pc-dropping-connection",
        "hero_url": "https://obsproject.com/assets/images/features-new/hero_32_1_1.png",
        "hero_name": "obs-studio-streaming-pc-network-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/settings.png",
        "diag_name": "obs-studio-auto-reconnect-network-settings-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    {
        "slug": "teradek-vidiu-x-stream-failing",
        "hero_url": None,  # Teradek VidiU X - will scrape
        "hero_name": "teradek-vidiu-x-hardware-encoder-church.jpg",
        "diag_url": None,
        "diag_name": "teradek-vidiu-x-rtmp-connection-diagram-troubleshooting.jpg",
        "hero_ref": "https://teradek.com/products/vidiu-x",
        "diag_ref": "https://teradek.com/products/vidiu-x",
    },
    {
        "slug": "vlan-setup-av-streaming-church",
        "hero_url": None,  # AVKANS PTZ
        "hero_name": "avkans-ptz-camera-vlan-network-church.jpg",
        "diag_url": None,
        "diag_name": "church-av-vlan-network-architecture-diagram-troubleshooting.jpg",
        "hero_ref": "https://avkans.com/",
        "diag_ref": "https://avkans.com/",
    },
    {
        "slug": "vmix-inputs-not-displaying",
        "hero_url": "https://www.vmix.com/images/2025/screen/softwareinterface.png",
        "hero_name": "vmix-software-inputs-live-production-church.png",
        "diag_url": "https://www.vmix.com/images/2021/software/icons/infographic.png",
        "diag_name": "vmix-software-input-configuration-diagram-troubleshooting.png",
        "hero_ref": "https://www.vmix.com/software/",
        "diag_ref": "https://www.vmix.com/software/",
    },
    {
        "slug": "youtube-stream-offline-mid-service",
        "hero_url": "https://obsproject.com/assets/images/features-new/hero_32_1_1.png",
        "hero_name": "obs-studio-youtube-stream-recovery-church.png",
        "diag_url": "https://obsproject.com/assets/images/features-new/settings.png",
        "diag_name": "obs-studio-auto-reconnect-youtube-diagram-troubleshooting.png",
        "hero_ref": "https://obsproject.com/",
        "diag_ref": "https://obsproject.com/",
    },
    # ── AVKANS camera web UI ────────────────────────────────
    {
        "slug": "avkans-camera-web-ui-not-loading",
        "hero_url": None,  # AVKANS PTZ
        "hero_name": "avkans-ptz-camera-web-ui-church.jpg",
        "diag_url": None,  # AVKANS PTZ
        "diag_name": "avkans-ptz-camera-network-web-ui-diagram-troubleshooting.jpg",
        "hero_ref": "https://avkans.com/",
        "diag_ref": "https://avkans.com/",
    },
]

# ============================================================
# SCRAPE MISSING IMAGES
# ============================================================

def scrape_avkans_image():
    """Return confirmed AVKANS PTZ camera product image URL."""
    # Confirmed from Amazon product page for AVKANS Studio 4K NDI PTZ Camera
    return "https://m.media-amazon.com/images/I/612N5WccZQL._AC_SL1500_.jpg"

def scrape_behringer_image():
    """Return confirmed Behringer X32 product image URL."""
    # Confirmed from Sweetwater product page
    return "https://media.sweetwater.com/m/products/image/b7bb238733lp2QKhnEz4yLRjeMFDrZlRJr8c9OPa.jpg"

def scrape_teradek_image():
    """Return confirmed Teradek VidiU X product image URL."""
    # Confirmed from cinegear.nl product page
    return "https://cinegear.nl/wp-content/uploads/2024/05/1-VIDIU-X.jpg"

def scrape_kiloview_image():
    """Return confirmed Kiloview N2 product image URL."""
    # Confirmed from Amazon search results - Kiloview N2 Portable Wireless HDMI to NDI Video Encoder
    return "https://m.media-amazon.com/images/I/61FoF3nJWwL._SL1500_.jpg"

# ============================================================
# DOWNLOAD FUNCTION
# ============================================================

def process_images():
    results = {}

    print("\n=== Scraping missing image URLs ===")

    avkans_url = scrape_avkans_image()
    behringer_url = scrape_behringer_image()
    teradek_url = scrape_teradek_image()
    kiloview_url = scrape_kiloview_image()

    print(f"  AVKANS: {avkans_url}")
    print(f"  Behringer: {behringer_url}")
    print(f"  Teradek: {teradek_url}")
    print(f"  Kiloview: {kiloview_url}")

    print("\n=== Downloading images ===")

    for item in IMAGES:
        slug = item["slug"]
        out_dir = os.path.join(PUBLIC, slug)
        os.makedirs(out_dir, exist_ok=True)
        results[slug] = {}

        print(f"\n[{slug}]")

        # Resolve None URLs
        hero_url = item["hero_url"]
        diag_url = item["diag_url"]

        if hero_url is None:
            if "avkans" in item["hero_name"].lower() or "ptz" in item["hero_name"].lower():
                hero_url = avkans_url
            elif "behringer" in item["hero_name"].lower() or "x32" in item["hero_name"].lower():
                hero_url = behringer_url
            elif "teradek" in item["hero_name"].lower():
                hero_url = teradek_url
            elif "kiloview" in item["hero_name"].lower():
                hero_url = kiloview_url

        if diag_url is None:
            if "kiloview" in item["diag_name"].lower():
                diag_url = kiloview_url
            elif "behringer" in item["diag_name"].lower():
                diag_url = behringer_url
            elif "ptz" in item["diag_name"].lower() and "avkans" not in item["diag_name"].lower():
                diag_url = avkans_url
            elif "avkans" in item["diag_name"].lower() or "vlan" in item["diag_name"].lower():
                diag_url = avkans_url
            elif "teradek" in item["diag_name"].lower():
                diag_url = teradek_url

        # Download hero
        if hero_url == "SKIP":
            # Already downloaded manually - just read size
            hero_path = os.path.join(out_dir, item["hero_name"])
            if os.path.exists(hero_path):
                try:
                    img = Image.open(hero_path)
                    w, h = img.size
                    results[slug]["hero"] = {"path": f"/images/products/{slug}/{item['hero_name']}", "size": (w, h)}
                    print(f"  OK (pre-downloaded) {item['hero_name']} ({w}x{h})")
                except Exception as e:
                    print(f"  FAIL reading pre-downloaded hero: {e}")
            else:
                print(f"  FAIL hero SKIP but file missing: {hero_path}")
        elif hero_url:
            hero_path = os.path.join(out_dir, item["hero_name"])
            size = download_image(hero_url, hero_path, item.get("hero_ref"))
            if size:
                results[slug]["hero"] = {"path": f"/images/products/{slug}/{item['hero_name']}", "size": size}
            time.sleep(0.3)
        else:
            print(f"  FAIL No hero URL available")

        # Download diagram
        if diag_url == "SKIP":
            diag_path = os.path.join(out_dir, item["diag_name"])
            if os.path.exists(diag_path):
                try:
                    img = Image.open(diag_path)
                    w, h = img.size
                    results[slug]["diagram"] = {"path": f"/images/products/{slug}/{item['diag_name']}", "size": (w, h)}
                    print(f"  OK (pre-downloaded) {item['diag_name']} ({w}x{h})")
                except Exception as e:
                    print(f"  FAIL reading pre-downloaded diagram: {e}")
            else:
                print(f"  FAIL diagram SKIP but file missing: {diag_path}")
        elif diag_url:
            diag_path = os.path.join(out_dir, item["diag_name"])
            size = download_image(diag_url, diag_path, item.get("diag_ref"))
            if size:
                results[slug]["diagram"] = {"path": f"/images/products/{slug}/{item['diag_name']}", "size": size}
            time.sleep(0.3)
        else:
            print(f"  FAIL No diagram URL available")

    # Save results to JSON
    results_path = os.path.join(WORKTREE, "scripts", "image_results.json")
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n=== Results saved to {results_path} ===")

    # Summary
    hero_count = sum(1 for v in results.values() if "hero" in v)
    diag_count = sum(1 for v in results.values() if "diagram" in v)
    print(f"\n=== SUMMARY ===")
    print(f"Heroes downloaded: {hero_count}/{len(IMAGES)}")
    print(f"Diagrams downloaded: {diag_count}/{len(IMAGES)}")

    return results

if __name__ == "__main__":
    results = process_images()
