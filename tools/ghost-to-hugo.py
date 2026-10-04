#!/usr/bin/env python3
"""One-off conversion of the old Ghost blog's posts to Hugo page bundles.

Usage: ghost-to-hugo.py POSTS.json OUT_DIR

POSTS.json is {"posts": [...]} with Ghost's post fields and tags as
[{"name", "slug"}]: either a Content API export, or the published posts taken
from the 2026-05-01 database export, which predates the attacker's edits and
is the source used for the blog.

Writes OUT_DIR/content/posts/<slug>/index.md and OUT_DIR/conversion-report.md.
Uses only each post's `html` and metadata; the codeinjection fields are never
read, because the old blog was compromised (they hold the attacker's script).
Also removes the attacker's spam paragraphs, script tags and iframes from
unknown hosts, and fails if anything suspicious survives.

Needs: pandoc (pypandoc), beautifulsoup4, lxml.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import pypandoc
from bs4 import BeautifulSoup, Comment

SITE_HOSTS = {"davidplanella.org", "www.davidplanella.org", "blog.davidplanella.org"}
SPAM_HOSTS = {"www.camisetatienda.com", "camisetatienda.com"}
IFRAME_HOSTS = {"www.youtube.com", "www.youtube-nocookie.com", "www.mixcloud.com",
                "docs.google.com", "web.archive.org", "player.vimeo.com"}
# Anything matching this in the output stops the conversion.
FORBIDDEN = re.compile(r"<script|javascript:|\son\w+\s*=|camisetatienda|clo4shara", re.I)


def clean_url(url):
    """Drop Ghost's ?ref= tracking and make links to the blog itself root-relative."""
    # Ghost's database stores links to the blog itself as __GHOST_URL__/path.
    url = url.replace("__GHOST_URL__", "")
    parts = urlsplit(url)
    query = urlencode([(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
                       if not (k == "ref" and v in SITE_HOSTS)])
    if parts.netloc in SITE_HOSTS:
        return urlunsplit(("", "", parts.path or "/", query, parts.fragment))
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, parts.fragment))


def clean_html(post, report):
    soup = BeautifulSoup(post["html"] or "", "lxml")
    body = soup.body or soup
    slug = post["slug"]

    for el in list(body.find_all(recursive=False)):
        if el.find("a", href=lambda h: h and urlsplit(h).netloc in SPAM_HOSTS):
            report["spam"].append((slug, el.get_text(" ", strip=True)))
            el.decompose()
    for c in body.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    for s in body.find_all("script"):
        report["scripts"].append((slug, s.get("src") or s.get_text()[:80]))
        s.decompose()
    for f in body.find_all("iframe"):
        host = urlsplit(f.get("src", "")).netloc
        if host in IFRAME_HOSTS:
            report["iframes"][host] += 1
        else:
            report["iframes_removed"].append((slug, f.get("src", "")))
            f.decompose()
    for tag in body.find_all(True):
        for attr in [a for a in tag.attrs if a.lower().startswith("on")]:
            del tag[attr]
        for attr in ("srcset", "sizes", "loading"):
            tag.attrs.pop(attr, None)
        if tag.get("href"):
            tag["href"] = clean_url(tag["href"])
        if tag.get("src"):
            tag["src"] = clean_url(tag["src"])
            if tag.name == "img":
                src = tag["src"]
                (report["images_local"] if src.startswith("/") else report["images_remote"])[src] += 1
    return "".join(str(c) for c in body.contents)


def yaml_str(value):
    return json.dumps(value, ensure_ascii=False)


def front_matter(post):
    lines = ["---",
             f"title: {yaml_str(post['title'])}",
             f"slug: {yaml_str(post['slug'])}",
             # published_at only: updated_at was overwritten by the attacker's edits.
             f"date: {post['published_at']}"]
    description = post.get("custom_excerpt") or post.get("meta_description")
    if description:
        lines.append(f"description: {yaml_str(description)}")
    # Tag slugs, not names, so Hugo's /tag/<slug>/ URLs match Ghost's exactly.
    # Ghost internal tags (names starting with #) are not shown publicly.
    tags = [t["slug"] for t in post.get("tags") or [] if not t["name"].startswith("#")]
    if tags:
        lines.append("tags: [" + ", ".join(yaml_str(t) for t in tags) + "]")
    if post.get("feature_image"):
        # Hugo's standard key for a page's images (first = feature image).
        lines.append(f"images: [{yaml_str(clean_url(post['feature_image']))}]")
    if post.get("featured"):
        lines.append("featured: true")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def hugo_urlize(name):
    """Approximation of Hugo's urlize for tag names, to spot URL changes."""
    return re.sub(r"[^\w\-]+", "", re.sub(r"\s+", "-", name.strip().lower()))


def main(src, out):
    posts = [p for p in json.load(open(src))["posts"] if p.get("type", "post") == "post"]
    out = Path(out)
    report = {"spam": [], "scripts": [], "iframes": Counter(), "iframes_removed": [],
              "images_local": Counter(), "images_remote": Counter()}
    tag_urls = {}
    bad = []
    for post in posts:
        html = clean_html(post, report)
        md = pypandoc.convert_text(html, "gfm", format="html", extra_args=["--wrap=none", "--sandbox"])
        text = front_matter(post) + md
        if FORBIDDEN.search(text):
            bad.append((post["slug"], FORBIDDEN.search(text).group(0)))
        path = out / "content" / "posts" / post["slug"] / "index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        for t in post.get("tags") or []:
            if not t["name"].startswith("#"):
                tag_urls[t["slug"]] = t["name"]

    # One _index.md per tag gives each tag page its display name.
    for slug, name in tag_urls.items():
        path = out / "content" / "tags" / slug / "_index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"---\ntitle: {yaml_str(name)}\nslug: {yaml_str(slug)}\n---\n")

    tag_changes = sorted((n, s, hugo_urlize(n)) for s, n in tag_urls.items() if hugo_urlize(n) != s)
    r = [f"# Ghost to Hugo conversion report\n\nPosts converted: {len(posts)}\n",
         f"## Spam paragraphs removed ({len(report['spam'])})\n"]
    r += [f"- `{s}`: {t[:160]}" for s, t in report["spam"]]
    r += [f"\n## Script tags removed ({len(report['scripts'])})\n"]
    r += [f"- `{s}`: {t}" for s, t in report["scripts"]]
    r += ["\n## Embeds kept\n"] + [f"- {h}: {n}" for h, n in report["iframes"].most_common()]
    r += [f"\n## Embeds removed ({len(report['iframes_removed'])})\n"]
    r += [f"- `{s}`: {u}" for s, u in report["iframes_removed"]]
    r += [f"\n## Local images referenced ({len(report['images_local'])} files)\n",
          "These must be copied from the Step 0 archive into `static/` at the same path.\n"]
    prefixes = Counter("/".join(p.split("/")[:2]) for p in report["images_local"])
    r += [f"- `{p}/...`: {n}" for p, n in prefixes.most_common()]
    r += [f"\n## Remote images ({len(report['images_remote'])})\n"]
    r += [f"- {u}" for u in sorted(report["images_remote"])]
    r += [f"\n## Tags whose URL would change ({len(tag_changes)})\n",
          "Ghost slug vs Hugo's default from the name. Handled: posts use the Ghost slugs as tag values, and content/tags/<slug>/_index.md sets the display name.\n"]
    r += [f"- {n}: `/tag/{s}/` vs `/tag/{h}/`" for n, s, h in tag_changes]
    r += [f"\n## Suspicious content left ({len(bad)})\n"] + [f"- `{s}`: {m}" for s, m in bad]
    (out / "conversion-report.md").write_text("\n".join(r) + "\n")
    (out / "images-needed.txt").write_text("\n".join(sorted(report["images_local"])) + "\n")
    print(f"{len(posts)} posts, {len(report['spam'])} spam paragraphs removed, "
          f"{len(report['scripts'])} scripts removed, {len(bad)} suspicious left")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
