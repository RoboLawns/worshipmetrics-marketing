#!/usr/bin/env python3
"""
WorshipMetrics Diagram Renderer
================================
Produces branded 1600x900 SVG diagrams from a structured JSON/Python spec.

Diagram types (see references/layouts.md for layout details):
  - network_topology: boxes connected by wires, optional zones/rooms
  - signal_flow:      left-to-right chain of nodes with labeled arrows
  - camera_placement: top-down sanctuary with camera positions + coverage arcs
  - preset_workflow:  numbered circular/linear steps with labels
  - comparison:       side-by-side columns with checkmark/x rows
  - stack:            generic labeled stack (cards over cards) for concept art
  - hero_concept:     big headline over a muted product silhouette + accent bar

All diagrams share the same palette, fonts, grid, header bar, and footer
branding so the site feels cohesive.

Usage (as a script):
    python render_diagram.py spec.json out.svg

Usage (as a library):
    from render_diagram import render
    svg = render(spec_dict)
    Path("out.svg").write_text(svg)

A spec is a dict like:
    {
      "type": "signal_flow",
      "title": "Camera to Encoder to CDN",
      "subtitle": "Signal flow for PTZ streaming",
      "nodes": [
        {"label": "PTZ Camera", "sub": "NDI out"},
        {"label": "Encoder",    "sub": "H.264"},
        {"label": "CDN",        "sub": "RTMP"}
      ],
      "edges": [
        {"label": "NDI"},
        {"label": "RTMP"}
      ]
    }

See the `EXAMPLES` block at the bottom of this file for one example of each type.
"""

from __future__ import annotations
import json
import html
import math
import sys
from pathlib import Path
from typing import Any

# ── Brand palette ─────────────────────────────────────────
# Matches the dark treatment used on existing cover SVGs:
# bg gradient 0B0E14 -> 13181F with a blue wash, accent #3B82F6,
# grid #1E2733. We also use the lighter brand indigo #4361ee for
# node fills so diagrams pop against the dark background.
BG_TOP       = "#0B0E14"
BG_MID       = "#13181F"
BG_ACCENT    = "#3B82F6"
GRID         = "#1E2733"
NODE_FILL    = "#1a2233"
NODE_STROKE  = "#4361ee"
NODE_HI      = "#5b7cff"
ARROW        = "#7aa0ff"
ARROW_LABEL  = "#c9d4ee"
TEXT_PRIMARY = "#f5f7fb"
TEXT_MUTED   = "#94a3c4"
WARM         = "#f59e0b"
OK           = "#34d399"
BAD          = "#f87171"

# ── Connection-type color system ─────────────────────────
# Rather than labeling every arrow in the diagram body (which collides with
# node labels and clutters the composition), each connection type is drawn in
# its own color and the diagram shows a small legend near the bottom. Only
# the types actually used in a given diagram appear in the legend.
CONNECTION_COLORS = {
    "NDI":      "#5b7cff",  # primary brand blue
    "HDMI":     "#34d399",  # green
    "SDI":      "#a78bfa",  # purple
    "USB":      "#f59e0b",  # amber
    "RTSP":     "#22d3ee",  # cyan
    "RTMP":     "#f472b6",  # pink
    "Ethernet": "#7aa0ff",  # soft blue (generic wired)
    "PoE":      "#93c5fd",  # pale blue
    "VISCA":    "#facc15",  # yellow
    "Power":    "#f87171",  # red
    "Audio":    "#fb923c",  # orange
    "Wireless": "#c4b5fd",  # lavender
}


def _conn_color(edge: dict) -> str:
    """Resolve an edge's display color.

    Precedence: explicit `color` > `type` lookup > default arrow color.
    Unknown types fall back to the default so nothing breaks.
    """
    if edge.get("color"):
        return edge["color"]
    t = edge.get("type")
    if t and t in CONNECTION_COLORS:
        return CONNECTION_COLORS[t]
    return ARROW


def _marker_id(color: str) -> str:
    """Deterministic marker id for a given arrow color."""
    return "arrow_" + color.lstrip("#")

W, H = 1600, 900
FONT = "'IBM Plex Sans', 'Outfit', system-ui, sans-serif"
MONO = "'IBM Plex Mono', ui-monospace, monospace"


def _esc(s: str) -> str:
    return html.escape(str(s), quote=False)


def _base_defs(arrow_colors: set[str] | None = None) -> str:
    """Emit gradients + one arrow marker for each arrow color in use.

    The default arrow color is always included so diagrams that don't use
    typed connections still have a working marker.
    """
    colors = set(arrow_colors or set())
    colors.add(ARROW)
    markers = []
    for c in sorted(colors):
        markers.append(
            f'<marker id="{_marker_id(c)}" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
        )
    return f"""
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG_TOP}"/>
      <stop offset="70%" stop-color="{BG_MID}"/>
      <stop offset="100%" stop-color="{BG_ACCENT}" stop-opacity="0.35"/>
    </linearGradient>
    <linearGradient id="accentBar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{BG_ACCENT}"/>
      <stop offset="100%" stop-color="{BG_ACCENT}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="nodeGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#202a3d"/>
      <stop offset="100%" stop-color="#141a27"/>
    </linearGradient>
    {"".join(markers)}
  </defs>"""


def _legend(types: list[str], y: float = H - 95) -> str:
    """Render a horizontal legend row of color swatches + type labels.

    `types` is an ordered list of connection types (keys in CONNECTION_COLORS,
    or "CUSTOM" entries represented as (label, color) tuples). Unknown types
    are silently dropped so callers don't have to pre-validate.
    """
    entries: list[tuple[str, str]] = []
    for t in types:
        if isinstance(t, tuple):
            label, color = t
            entries.append((label, color))
        elif t in CONNECTION_COLORS:
            entries.append((t, CONNECTION_COLORS[t]))
    if not entries:
        return ""
    parts = [f'<g>']
    x = 60
    for label, color in entries:
        parts.append(
            f'<line x1="{x}" y1="{y}" x2="{x + 44}" y2="{y}" stroke="{color}" '
            f'stroke-width="4" stroke-linecap="round"/>'
        )
        parts.append(
            f'<text x="{x + 54}" y="{y + 6}" fill="{TEXT_MUTED}" '
            f'font-family="{MONO}" font-size="17" font-weight="600">'
            f'{_esc(label)}</text>'
        )
        # Width = 44 (line) + 10 (gap) + approx label width + 28 (spacer)
        x += 44 + 10 + len(label) * 11 + 32
    parts.append("</g>")
    return "\n".join(parts)


def _background(title_for_a11y: str, desc_for_a11y: str) -> str:
    return f"""  <title id="t">{_esc(title_for_a11y)}</title>
  <desc id="d">{_esc(desc_for_a11y)}</desc>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <g stroke="{GRID}" stroke-width="1" opacity="0.55">
    <line x1="0" y1="225" x2="{W}" y2="225"/>
    <line x1="0" y1="450" x2="{W}" y2="450"/>
    <line x1="0" y1="675" x2="{W}" y2="675"/>
    <line x1="400" y1="0" x2="400" y2="{H}"/>
    <line x1="800" y1="0" x2="800" y2="{H}"/>
    <line x1="1200" y1="0" x2="1200" y2="{H}"/>
  </g>
  <rect x="0" y="0" width="{W}" height="8" fill="url(#accentBar)"/>"""


def _header(title: str, subtitle: str, eyebrow: str = "WORSHIPMETRICS") -> str:
    return f"""
  <text x="60" y="70" fill="{BG_ACCENT}" font-family="{FONT}" font-size="20"
        font-weight="700" letter-spacing="4">{_esc(eyebrow)}</text>
  <text x="60" y="135" fill="{TEXT_PRIMARY}" font-family="{FONT}" font-size="52"
        font-weight="700">{_esc(title)}</text>
  <text x="60" y="175" fill="{TEXT_MUTED}" font-family="{FONT}" font-size="22"
        font-weight="400">{_esc(subtitle)}</text>"""


def _footer(footer: str) -> str:
    if not footer:
        return ""
    return f"""
  <text x="60" y="{H - 40}" fill="{TEXT_MUTED}" font-family="{FONT}"
        font-size="18">{_esc(footer)}</text>
  <text x="{W - 60}" y="{H - 40}" fill="{TEXT_MUTED}" font-family="{FONT}"
        font-size="18" text-anchor="end">worshipmetrics.com</text>"""


# ── Primitive: a rounded "chip" node with label + optional sub-label ──
def _chip(x: float, y: float, w: float, h: float, label: str,
          sub: str = "", accent: str = NODE_STROKE,
          fill: str = "url(#nodeGrad)") -> str:
    label_y = y + h / 2 + (4 if sub else 10)
    sub_svg = ""
    if sub:
        sub_svg = (
            f'<text x="{x + w/2}" y="{y + h/2 + 32}" fill="{TEXT_MUTED}" '
            f'font-family="{MONO}" font-size="18" text-anchor="middle">'
            f"{_esc(sub)}</text>"
        )
    return f"""
  <g>
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" ry="14"
          fill="{fill}" stroke="{accent}" stroke-width="2.5"/>
    <text x="{x + w/2}" y="{label_y}" fill="{TEXT_PRIMARY}"
          font-family="{FONT}" font-size="26" font-weight="600"
          text-anchor="middle">{_esc(label)}</text>
    {sub_svg}
  </g>"""


# ── Layouts ──────────────────────────────────────────────

def _signal_flow(spec: dict) -> str:
    """Left-to-right chain. Connection types are shown by color + legend, not by
    inline text labels (which collide with node labels). Pass `type` on each
    edge to color-code it."""
    nodes = spec["nodes"]
    edges = spec.get("edges", [{}] * (len(nodes) - 1))
    top = 440
    node_h = 140
    gutter = 60
    usable = W - gutter * 2
    node_w = min(260, (usable - 90 * (len(nodes) - 1)) / len(nodes))
    gap = (usable - node_w * len(nodes)) / max(1, len(nodes) - 1)
    node_parts: list[str] = []
    edge_parts: list[str] = []
    xs = []
    for i, n in enumerate(nodes):
        x = gutter + i * (node_w + gap)
        xs.append(x)
        node_parts.append(_chip(x, top, node_w, node_h, n["label"], n.get("sub", "")))
    # Arrows (drawn first so chips paint over any residual tip)
    for i, e in enumerate(edges[: len(nodes) - 1]):
        x1 = xs[i] + node_w + 8
        x2 = xs[i + 1] - 8
        y = top + node_h / 2
        color = _conn_color(e)
        edge_parts.append(
            f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" '
            f'stroke="{color}" stroke-width="4" marker-end="url(#{_marker_id(color)})"/>'
        )
    return "\n".join(edge_parts + node_parts)


def _rect_edge_point(cx: float, cy: float, hw: float, hh: float,
                     tx: float, ty: float) -> tuple[float, float]:
    """Where a ray from (cx,cy) toward (tx,ty) exits a rect of half-size (hw,hh)."""
    dx = tx - cx
    dy = ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    # Scale factor to hit each axis bound
    sx = hw / abs(dx) if dx else float("inf")
    sy = hh / abs(dy) if dy else float("inf")
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s


def _network_topology(spec: dict) -> str:
    """Zones render as soft cards; devices sit inside zones; edges connect devices by id.

    Render order is deliberate: zones -> edges -> nodes -> edge labels. That way
    connector lines stop at the chip edges (not the centers) AND the chips paint
    over any residual line, so nothing pokes through a device rectangle.
    """
    zones = spec.get("zones", [])
    devices = spec.get("devices", [])
    edges = spec.get("edges", [])
    zone_parts: list[str] = []
    edge_parts: list[str] = []
    node_parts: list[str] = []
    label_parts: list[str] = []

    # Zones (drawn first, under everything)
    for z in zones:
        x, y, w, h = z["x"], z["y"], z["w"], z["h"]
        zone_parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" ry="18" '
            f'fill="#141a27" fill-opacity="0.65" stroke="{GRID}" stroke-width="1.5" '
            f'stroke-dasharray="6 6"/>'
        )
        zone_parts.append(
            f'<text x="{x + 18}" y="{y + 30}" fill="{TEXT_MUTED}" '
            f'font-family="{MONO}" font-size="16" font-weight="700" '
            f'letter-spacing="2">{_esc(z["label"].upper())}</text>'
        )

    # Collect device geometry (without emitting yet so we can draw edges first)
    by_id: dict[str, tuple[float, float, float, float, float, float]] = {}
    for d in devices:
        dx, dy = d["x"], d["y"]
        dw = d.get("w", 200)
        dh = d.get("h", 90)
        by_id[d["id"]] = (dx + dw / 2, dy + dh / 2, dx, dy, dw, dh)
        node_parts.append(
            _chip(dx, dy, dw, dh, d["label"], d.get("sub", ""),
                  accent=d.get("accent", NODE_STROKE))
        )

    # Edges — terminate at rectangle edges, colored by connection type
    for e in edges:
        ax, ay, _, _, aw, ah = by_id[e["from"]]
        bx, by, _, _, bw, bh = by_id[e["to"]]
        x1, y1 = _rect_edge_point(ax, ay, aw / 2, ah / 2, bx, by)
        x2, y2 = _rect_edge_point(bx, by, bw / 2, bh / 2, ax, ay)
        color = _conn_color(e)
        edge_parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="4" '
            f'marker-end="url(#{_marker_id(color)})" opacity="0.95"/>'
        )

    # Order matters: zones -> edges -> nodes. No inline edge labels — use legend.
    return "\n".join(zone_parts + edge_parts + node_parts)


def _camera_placement(spec: dict) -> str:
    """Top-down sanctuary: stage + pews + camera chips with coverage arcs."""
    parts = []
    # Sanctuary shell
    parts.append(
        f'<rect x="220" y="280" width="1160" height="520" rx="28" ry="28" '
        f'fill="#141a27" stroke="{GRID}" stroke-width="2"/>'
    )
    # Stage
    parts.append(
        f'<rect x="260" y="320" width="1080" height="120" rx="12" ry="12" '
        f'fill="#1a2540" stroke="{NODE_STROKE}" stroke-width="1.5"/>'
    )
    parts.append(
        f'<text x="800" y="395" fill="{TEXT_MUTED}" font-family="{MONO}" '
        f'font-size="22" text-anchor="middle" font-weight="700" '
        f'letter-spacing="3">STAGE</text>'
    )
    # Pew rows
    for i, y in enumerate([500, 560, 620, 680, 740]):
        parts.append(
            f'<rect x="300" y="{y}" width="1000" height="28" rx="6" ry="6" '
            f'fill="#1e2733" opacity="{0.9 - i * 0.12}"/>'
        )
    # Cameras
    for cam in spec.get("cameras", []):
        cx, cy = cam["x"], cam["y"]
        parts.append(
            f'<circle cx="{cx}" cy="{cy}" r="22" fill="{NODE_HI}" '
            f'stroke="#fff" stroke-width="2"/>'
        )
        parts.append(
            f'<text x="{cx}" y="{cy + 7}" fill="#0B0E14" font-family="{FONT}" '
            f'font-size="20" font-weight="800" text-anchor="middle">'
            f'{_esc(cam.get("id", ""))}</text>'
        )
        # Coverage arc
        ang = cam.get("angle", 60)
        facing = cam.get("facing", 0)  # degrees, 0 = pointing right
        r = cam.get("reach", 280)
        a1 = math.radians(facing - ang / 2)
        a2 = math.radians(facing + ang / 2)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        large = 1 if ang > 180 else 0
        parts.append(
            f'<path d="M {cx} {cy} L {x1:.1f} {y1:.1f} A {r} {r} 0 {large} 1 '
            f'{x2:.1f} {y2:.1f} Z" fill="{BG_ACCENT}" fill-opacity="0.18" '
            f'stroke="{BG_ACCENT}" stroke-width="1.5" stroke-opacity="0.6"/>'
        )
        if cam.get("label"):
            parts.append(
                f'<text x="{cx}" y="{cy - 34}" fill="{TEXT_PRIMARY}" '
                f'font-family="{FONT}" font-size="17" text-anchor="middle" '
                f'font-weight="600">{_esc(cam["label"])}</text>'
            )
    return "\n".join(parts)


def _preset_workflow(spec: dict) -> str:
    steps = spec["steps"]
    top = 460
    node_w, node_h = 240, 150
    gutter = 60
    count = len(steps)
    gap = (W - gutter * 2 - node_w * count) / max(1, count - 1)
    parts = []
    for i, s in enumerate(steps):
        x = gutter + i * (node_w + gap)
        y = top
        parts.append(
            f'<rect x="{x}" y="{y}" width="{node_w}" height="{node_h}" rx="18" ry="18" '
            f'fill="url(#nodeGrad)" stroke="{NODE_STROKE}" stroke-width="2.5"/>'
        )
        parts.append(
            f'<circle cx="{x + 38}" cy="{y + 38}" r="26" fill="{BG_ACCENT}"/>'
            f'<text x="{x + 38}" y="{y + 46}" fill="#0B0E14" font-family="{FONT}" '
            f'font-size="26" font-weight="800" text-anchor="middle">{i + 1}</text>'
        )
        parts.append(
            f'<text x="{x + 20}" y="{y + 95}" fill="{TEXT_PRIMARY}" '
            f'font-family="{FONT}" font-size="22" font-weight="600">'
            f'{_esc(s["label"])}</text>'
        )
        if s.get("sub"):
            parts.append(
                f'<text x="{x + 20}" y="{y + 125}" fill="{TEXT_MUTED}" '
                f'font-family="{MONO}" font-size="16">{_esc(s["sub"])}</text>'
            )
        if i < count - 1:
            ax1 = x + node_w + 6
            ax2 = x + node_w + gap - 6
            ay = y + node_h / 2
            parts.append(
                f'<line x1="{ax1}" y1="{ay}" x2="{ax2}" y2="{ay}" '
                f'stroke="{ARROW}" stroke-width="3" marker-end="url(#arrow)"/>'
            )
    return "\n".join(parts)


def _comparison(spec: dict) -> str:
    cols = spec["columns"]  # list of {label, rows: [{feature, value, good}]}
    rows_meta = spec.get("rows", [])  # list of feature labels, in order
    parts = []
    col_count = len(cols)
    gutter = 80
    label_w = 340
    col_w = (W - gutter * 2 - label_w) / col_count
    top = 300
    row_h = 62

    # Row labels
    for i, rname in enumerate(rows_meta):
        y = top + (i + 1) * row_h
        parts.append(
            f'<text x="{gutter + label_w - 24}" y="{y}" fill="{TEXT_MUTED}" '
            f'font-family="{FONT}" font-size="20" font-weight="600" '
            f'text-anchor="end">{_esc(rname)}</text>'
        )
        parts.append(
            f'<line x1="{gutter + label_w}" y1="{y + 10}" x2="{W - gutter}" '
            f'y2="{y + 10}" stroke="{GRID}" stroke-width="1"/>'
        )

    # Columns
    for ci, col in enumerate(cols):
        cx = gutter + label_w + ci * col_w
        parts.append(
            f'<rect x="{cx + 12}" y="{top - 10}" width="{col_w - 24}" '
            f'height="{(len(rows_meta) + 1) * row_h + 16}" rx="16" ry="16" '
            f'fill="#141a27" stroke="{NODE_STROKE}" stroke-width="2"/>'
        )
        parts.append(
            f'<text x="{cx + col_w / 2}" y="{top + 30}" fill="{TEXT_PRIMARY}" '
            f'font-family="{FONT}" font-size="26" font-weight="700" '
            f'text-anchor="middle">{_esc(col["label"])}</text>'
        )
        for i, r in enumerate(col.get("values", [])):
            y = top + (i + 1) * row_h
            good = r.get("good")
            txt = r.get("text", "")
            color = OK if good is True else BAD if good is False else TEXT_PRIMARY
            parts.append(
                f'<text x="{cx + col_w / 2}" y="{y}" fill="{color}" '
                f'font-family="{FONT}" font-size="19" font-weight="600" '
                f'text-anchor="middle">{_esc(txt)}</text>'
            )
    return "\n".join(parts)


def _stack(spec: dict) -> str:
    layers = spec["layers"]  # top-to-bottom
    top = 280
    layer_h = 80
    gap = 14
    gutter = 260
    parts = []
    for i, layer in enumerate(layers):
        y = top + i * (layer_h + gap)
        parts.append(
            f'<rect x="{gutter}" y="{y}" width="{W - gutter * 2}" height="{layer_h}" '
            f'rx="14" ry="14" fill="url(#nodeGrad)" stroke="{NODE_STROKE}" '
            f'stroke-width="2"/>'
        )
        parts.append(
            f'<text x="{gutter + 30}" y="{y + layer_h / 2 + 10}" fill="{TEXT_PRIMARY}" '
            f'font-family="{FONT}" font-size="26" font-weight="600">'
            f'{_esc(layer["label"])}</text>'
        )
        if layer.get("sub"):
            parts.append(
                f'<text x="{W - gutter - 30}" y="{y + layer_h / 2 + 10}" '
                f'fill="{TEXT_MUTED}" font-family="{MONO}" font-size="19" '
                f'text-anchor="end">{_esc(layer["sub"])}</text>'
            )
    return "\n".join(parts)


def _hero_concept(spec: dict) -> str:
    """Big headline concept art for category/overview articles."""
    parts = []
    tag = spec.get("tag", "GUIDE")
    stat = spec.get("stat", "")
    stat_label = spec.get("stat_label", "")
    parts.append(
        f'<rect x="60" y="300" width="280" height="46" rx="23" ry="23" '
        f'fill="{BG_ACCENT}" fill-opacity="0.2" stroke="{BG_ACCENT}" '
        f'stroke-width="1.5"/>'
        f'<text x="200" y="331" fill="{BG_ACCENT}" font-family="{MONO}" '
        f'font-size="18" font-weight="700" text-anchor="middle" '
        f'letter-spacing="2">{_esc(tag.upper())}</text>'
    )
    if stat:
        parts.append(
            f'<text x="{W - 100}" y="560" fill="{BG_ACCENT}" font-family="{FONT}" '
            f'font-size="200" font-weight="800" text-anchor="end" '
            f'opacity="0.92">{_esc(stat)}</text>'
        )
    if stat_label:
        parts.append(
            f'<text x="{W - 100}" y="600" fill="{TEXT_MUTED}" font-family="{MONO}" '
            f'font-size="22" text-anchor="end">{_esc(stat_label)}</text>'
        )
    for i, bullet in enumerate(spec.get("bullets", [])[:4]):
        parts.append(
            f'<circle cx="88" cy="{420 + i * 60}" r="6" fill="{BG_ACCENT}"/>'
            f'<text x="112" y="{428 + i * 60}" fill="{TEXT_PRIMARY}" '
            f'font-family="{FONT}" font-size="26">{_esc(bullet)}</text>'
        )
    return "\n".join(parts)


RENDERERS = {
    "signal_flow": _signal_flow,
    "network_topology": _network_topology,
    "camera_placement": _camera_placement,
    "preset_workflow": _preset_workflow,
    "comparison": _comparison,
    "stack": _stack,
    "hero_concept": _hero_concept,
}


def _collect_connection_types(spec: dict) -> list[str]:
    """Return the ordered, de-duplicated list of connection types used by the
    spec's edges. Honors edges' `type` field; explicit `color` without `type`
    is ignored here (the caller can pass an explicit legend).
    """
    seen: list[str] = []
    for e in spec.get("edges", []) or []:
        t = e.get("type")
        if t and t not in seen:
            seen.append(t)
    return seen


def _collect_arrow_colors(spec: dict) -> set[str]:
    """Every color that appears on an edge, so _base_defs can emit matching
    arrowhead markers. Always includes the default arrow color."""
    colors = {ARROW}
    for e in spec.get("edges", []) or []:
        colors.add(_conn_color(e))
    return colors


def render(spec: dict[str, Any]) -> str:
    t = spec["type"]
    if t not in RENDERERS:
        raise ValueError(f"Unknown diagram type: {t}. "
                         f"Valid: {sorted(RENDERERS)}")
    title = spec.get("title", "")
    subtitle = spec.get("subtitle", "")
    eyebrow = spec.get("eyebrow", "WORSHIPMETRICS")
    footer = spec.get("footer", spec.get("a11y_desc", ""))
    body = RENDERERS[t](spec)

    # Legend: auto-derived from edge types, or explicit `legend` override.
    # `legend` can be either a list of type names or a list of (label, color).
    legend_items = spec.get("legend")
    if legend_items is None:
        legend_items = _collect_connection_types(spec)
    legend_svg = _legend(legend_items) if legend_items else ""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
     role="img" aria-labelledby="t d">
{_base_defs(_collect_arrow_colors(spec))}
{_background(title, subtitle)}
{_header(title, subtitle, eyebrow)}
{body}
{legend_svg}
{_footer(footer)}
</svg>
"""


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: render_diagram.py spec.json out.svg", file=sys.stderr)
        return 2
    spec = json.loads(Path(argv[1]).read_text())
    svg = render(spec)
    Path(argv[2]).write_text(svg)
    print(f"Wrote {argv[2]} ({len(svg)} bytes, type={spec['type']})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
