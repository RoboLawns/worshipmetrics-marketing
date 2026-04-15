#!/usr/bin/env python3
"""
WorshipMetrics Diagram Generator
Generates branded SVG diagrams for church AV knowledge base articles.
"""

import sys
import argparse
import math

BG_COLOR       = "#f0f4f8"
DEVICE_FILL    = "#0d1f2d"
DEVICE_STROKE  = "#c9a84c"
DEVICE_TEXT    = "#ffffff"
ARROW_COLOR    = "#2563eb"
LABEL_COLOR    = "#4b5563"
GRID_COLOR     = "#dde3ea"

CAT_COLORS = {
    "router":   "#1a3a5c",
    "switch":   "#1a3a5c",
    "camera":   "#1a4a2e",
    "encoder":  "#3a1a4a",
    "server":   "#2a2a1a",
    "laptop":   "#3a2a1a",
    "computer": "#3a2a1a",
    "default":  "#0d1f2d",
}

W, H = 1200, 630

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

def wrap_text(text, max_chars=14):
    words = text.split()
    lines, line = [], ""
    for w in words:
        if len(line) + len(w) + 1 <= max_chars:
            line = (line + " " + w).strip()
        else:
            if line: lines.append(line)
            line = w
    if line: lines.append(line)
    return lines

def device_color(name):
    low = name.lower()
    for k, v in CAT_COLORS.items():
        if k in low: return v
    return CAT_COLORS["default"]

def arrow_marker():
    return f"""
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="{ARROW_COLOR}" />
    </marker>
    <filter id="dropshadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#00000033"/>
    </filter>
  </defs>"""

def box(x, y, w, h, label, fill=None, stroke=None, text_color=None, font_size=13):
    fill = fill or DEVICE_FILL
    stroke = stroke or DEVICE_STROKE
    text_color = text_color or DEVICE_TEXT
    lines = wrap_text(label, max_chars=max(10, w // 9))
    line_h = font_size + 4
    total_text_h = len(lines) * line_h
    text_y_start = y + h / 2 - total_text_h / 2 + font_size
    text_els = ""
    for i, ln in enumerate(lines):
        ty = text_y_start + i * line_h
        text_els += f'\n    <text x="{x+w/2:.1f}" y="{ty:.1f}" text-anchor="middle" font-size="{font_size}" fill="{text_color}" font-weight="600" font-family="Inter,Helvetica,Arial,sans-serif">{esc(ln)}</text>'
    return f"""
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" ry="8" fill="{fill}" stroke="{stroke}" stroke-width="2" filter="url(#dropshadow)" />
  {text_els}"""

def line_with_label(x1, y1, x2, y2, label="", dashed=False, color=None):
    color = color or ARROW_COLOR
    dash = 'stroke-dasharray="6,4"' if dashed else ""
    lx = (x1 + x2) / 2
    ly = (y1 + y2) / 2 - 8
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    if abs(angle) > 90: angle += 180
    label_el = ""
    if label:
        label_el = f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" font-size="11" fill="{LABEL_COLOR}" font-family="Inter,Helvetica,Arial,sans-serif" transform="rotate({angle:.1f},{lx:.1f},{ly:.1f})">{esc(label)}</text>'
    return f"""
  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="2" {dash} marker-end="url(#arrowhead)" />
  {label_el}"""

def title_bar(title):
    return f"""
  <rect x="0" y="0" width="{W}" height="52" fill="{DEVICE_FILL}" />
  <text x="24" y="34" font-size="20" font-weight="700" fill="{DEVICE_STROKE}" font-family="Inter,Helvetica,Arial,sans-serif">{esc(title)}</text>
  <text x="{W-24}" y="34" font-size="13" fill="#8899aa" text-anchor="end" font-family="Inter,Helvetica,Arial,sans-serif">WorshipMetrics.io</text>"""

def footer():
    return f"""
  <rect x="0" y="{H-28}" width="{W}" height="28" fill="{DEVICE_FILL}" opacity="0.6"/>
  <text x="{W//2}" y="{H-10}" text-anchor="middle" font-size="11" fill="#8899aa" font-family="Inter,Helvetica,Arial,sans-serif">© WorshipMetrics.io — Church AV Knowledge Base</text>"""

def signal_flow(title, devices, connections):
    n = len(devices)
    BOX_W = min(160, max(110, (W - 120) // n - 30))
    BOX_H = 72
    MARGIN_SIDE = 60
    spacing = (W - MARGIN_SIDE * 2 - BOX_W * n) / max(n - 1, 1)
    cy = H // 2 + 10
    conn_map = {}
    for c in connections:
        parts = c.split(":")
        label = parts[1].strip() if len(parts) > 1 else ""
        ends = parts[0].split("->")
        if len(ends) == 2: conn_map[(ends[0].strip(), ends[1].strip())] = label
    svg_parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
                 arrow_marker(),
                 f'<rect width="{W}" height="{H}" fill="{BG_COLOR}"/>']
    for gx in range(0, W, 60):
        svg_parts.append(f'<line x1="{gx}" y1="52" x2="{gx}" y2="{H-28}" stroke="{GRID_COLOR}" stroke-width="1"/>')
    svg_parts.append(title_bar(title))
    for i, dev in enumerate(devices):
        x = MARGIN_SIDE + i * (BOX_W + spacing)
        svg_parts.append(box(x, cy - BOX_H/2, BOX_W, BOX_H, dev))
    drawn = set()
    for (src, dst), lbl in conn_map.items():
        si = next((i for i,d in enumerate(devices) if d==src), None)
        di = next((i for i,d in enumerate(devices) if d==dst), None)
        if si is not None and di is not None:
            sx = MARGIN_SIDE + si*(BOX_W+spacing) + BOX_W
            dx = MARGIN_SIDE + di*(BOX_W+spacing)
            svg_parts.append(line_with_label(sx, cy, dx, cy, lbl))
            drawn.add((si,di))
    for i in range(n-1):
        if (i,i+1) not in drawn:
            sx = MARGIN_SIDE + i*(BOX_W+spacing) + BOX_W
            dx = MARGIN_SIDE + (i+1)*(BOX_W+spacing)
            svg_parts.append(line_with_label(sx, cy, dx, cy))
    svg_parts.extend([footer(), '</svg>'])
    return "\n".join(svg_parts)

def network_topology(title, devices, connections):
    BOX_W, BOX_H = 130, 60
    cx, cy = W//2, H//2+10
    hub = devices[0]
    spokes = devices[1:]
    ns = len(spokes)
    radius = min(220, max(160, ns*40))
    angle_step = 360 / max(ns, 1)
    positions = {hub: (cx, cy)}
    for i, dev in enumerate(spokes):
        angle = math.radians(angle_step*i - 90)
        positions[dev] = (cx + radius*math.cos(angle), cy + radius*math.sin(angle))
    conn_map = {}
    for c in connections:
        parts = c.split(":")
        label = parts[1].strip() if len(parts) > 1 else ""
        ends = parts[0].split("->")
        if len(ends) == 2: conn_map[(ends[0].strip(), ends[1].strip())] = label
    svg_parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
                 arrow_marker(),
                 f'<rect width="{W}" height="{H}" fill="{BG_COLOR}"/>',
                 title_bar(title)]
    for (src, dst), lbl in conn_map.items():
        if src in positions and dst in positions:
            sx, sy = positions[src]
            dx, dy = positions[dst]
            angle = math.atan2(dy-sy, dx-sx)
            svg_parts.append(line_with_label(sx+(BOX_W/2+4)*math.cos(angle), sy+(BOX_H/2+4)*math.sin(angle),
                                              dx-(BOX_W/2+4)*math.cos(angle), dy-(BOX_H/2+4)*math.sin(angle), lbl))
    for dev, (px, py) in positions.items():
        fill = device_color(dev)
        stroke = DEVICE_STROKE if dev==hub else "#4a7fa5"
        svg_parts.append(box(px-BOX_W/2, py-BOX_H/2, BOX_W, BOX_H, dev, fill=fill, stroke=stroke))
    svg_parts.extend([footer(), '</svg>'])
    return "\n".join(svg_parts)

def audio_routing(title, devices, connections):
    conn_map = {}
    for c in connections:
        parts = c.split(":")
        label = parts[1].strip() if len(parts) > 1 else ""
        ends = parts[0].split("->")
        if len(ends) == 2: conn_map[(ends[0].strip(), ends[1].strip())] = label
    scores = {d: 0 for d in devices}
    for (src, dst) in conn_map:
        if src in scores: scores[src] += 1
        if dst in scores: scores[dst] += 1
    mixer = max(scores, key=lambda d: (("mix" in d.lower() or "console" in d.lower())*100 + scores[d]))
    inputs  = [d for d in devices if d != mixer and any(k[0]==d for k in conn_map)]
    outputs = [d for d in devices if d != mixer and d not in inputs]
    if not outputs:
        half = len(devices)//2
        inputs  = [d for d in devices if d!=mixer][:half]
        outputs = [d for d in devices if d!=mixer][half:]
    BOX_W, BOX_H = 140, 56
    MIX_W = 160
    MIX_H = max(100, len(inputs)*70)
    TOP_PAD = 80
    col_l_x = 60
    col_r_x = W - 60 - BOX_W
    mix_x = (W - MIX_W)//2
    mix_y = (H - MIX_H)//2 + 10
    def col_y(idx, total, bh, total_h=H-TOP_PAD-60):
        sp = total_h / max(total, 1)
        return TOP_PAD + sp*idx + sp/2 - bh/2
    positions = {mixer: (mix_x+MIX_W/2, mix_y+MIX_H/2)}
    for i, dev in enumerate(inputs):
        y = col_y(i, len(inputs), BOX_H)
        positions[dev] = (col_l_x+BOX_W/2, y+BOX_H/2)
    for i, dev in enumerate(outputs):
        y = col_y(i, len(outputs), BOX_H)
        positions[dev] = (col_r_x+BOX_W/2, y+BOX_H/2)
    svg_parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
                 arrow_marker(),
                 f'<rect width="{W}" height="{H}" fill="{BG_COLOR}"/>',
                 title_bar(title)]
    for (src, dst), lbl in conn_map.items():
        if src in positions and dst in positions:
            sx, sy = positions[src]
            dx, dy = positions[dst]
            angle = math.atan2(dy-sy, dx-sx)
            hw = MIX_W/2 if src==mixer or dst==mixer else BOX_W/2
            hh = MIX_H/2 if src==mixer or dst==mixer else BOX_H/2
            sx2 = sx + (hw if src==mixer else BOX_W/2)*math.cos(angle)
            sy2 = sy + (hh if src==mixer else BOX_H/2)*math.sin(angle)
            dx2 = dx - (hw if dst==mixer else BOX_W/2)*math.cos(angle)
            dy2 = dy - (hh if dst==mixer else BOX_H/2)*math.sin(angle)
            dashed = any(t in lbl.lower() for t in ["ts","rca","aux","stereo","unbalanced"])
            svg_parts.append(line_with_label(sx2, sy2, dx2, dy2, lbl, dashed=dashed))
    svg_parts.append(box(mix_x, mix_y, MIX_W, MIX_H, mixer, fill="#1a2e42", stroke=DEVICE_STROKE))
    for dev in inputs:
        px, py = positions[dev]
        svg_parts.append(box(px-BOX_W/2, py-BOX_H/2, BOX_W, BOX_H, dev, fill="#1a3a2a", stroke="#4caf79"))
    for dev in outputs:
        px, py = positions[dev]
        svg_parts.append(box(px-BOX_W/2, py-BOX_H/2, BOX_W, BOX_H, dev, fill="#2a1a3a", stroke="#9c6aba"))
    legend_y = H - 50
    svg_parts.append(f'<rect x="40" y="{legend_y}" width="14" height="3" fill="{ARROW_COLOR}"/>')
    svg_parts.append(f'<text x="60" y="{legend_y+4}" font-size="11" fill="{LABEL_COLOR}" font-family="Inter,Helvetica,Arial,sans-serif">Balanced (XLR / TRS)</text>')
    svg_parts.append(f'<line x1="220" y1="{legend_y+1}" x2="234" y2="{legend_y+1}" stroke="{ARROW_COLOR}" stroke-width="2" stroke-dasharray="4,3"/>')
    svg_parts.append(f'<text x="240" y="{legend_y+4}" font-size="11" fill="{LABEL_COLOR}" font-family="Inter,Helvetica,Arial,sans-serif">Unbalanced / Line</text>')
    svg_parts.extend([footer(), '</svg>'])
    return "\n".join(svg_parts)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", required=True, choices=["signal_flow","network_topology","audio_routing"])
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--devices", required=True)
    parser.add_argument("--connections", default="")
    args = parser.parse_args()
    devices = [d.strip() for d in args.devices.split(",") if d.strip()]
    connections = [c.strip() for c in args.connections.split(",") if c.strip()]
    if args.type == "signal_flow":        svg = signal_flow(args.title, devices, connections)
    elif args.type == "network_topology": svg = network_topology(args.title, devices, connections)
    elif args.type == "audio_routing":    svg = audio_routing(args.title, devices, connections)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"OK Saved {args.output}")

if __name__ == "__main__":
    main()
