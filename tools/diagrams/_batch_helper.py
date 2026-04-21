"""Shared helpers for batch spec files.

Each batch file maps: slug -> (content_subdir, spec). We render every spec
into public/images/products/<slug>/cover.svg and inject the coverImage
frontmatter into the matching mdx file if missing.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from render_diagram import render  # noqa: E402

REPO = Path('/sessions/jolly-bold-darwin/mnt/worshipmetrics-marketing')
IMG_ROOT = REPO / 'public' / 'images' / 'products'
CONTENT_ROOT = REPO / 'src' / 'content'


def run(entries):
    """entries: dict of slug -> {'subdir': <content-subfolder>, 'spec': <spec>}"""
    for slug, info in entries.items():
        spec = info['spec']
        subdir = info['subdir']
        out = IMG_ROOT / slug / 'cover.svg'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(spec))

        mdx = CONTENT_ROOT / subdir / f'{slug}.mdx'
        if not mdx.exists():
            print(f'!! missing mdx: {mdx}')
            continue
        src = mdx.read_text()
        parts = src.split('---', 2)
        if len(parts) < 3:
            print(f'!! bad frontmatter: {mdx}')
            continue
        if 'coverImage:' in parts[1]:
            print(f'ok  (had cover)  {slug}')
            continue
        new = re.sub(
            r'(description: .*\n)',
            lambda m: m.group(1) + f'coverImage: "/images/products/{slug}/cover.svg"\n',
            src, count=1,
        )
        mdx.write_text(new)
        print(f'ok  {slug}')
