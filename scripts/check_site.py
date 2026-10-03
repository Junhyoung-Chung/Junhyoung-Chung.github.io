#!/usr/bin/env python3
"""Verify generated pages, links, lazy PDF loading, and build-environment boundaries."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.refs, self.ids, self.iframes, self.h1 = [], [], [], 0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'iframe':
            self.iframes.append(a)
        for key in ('href', 'src'):
            if key in a and a[key]:
                self.refs.append((tag, a[key]))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('site', type=Path)
    parser.add_argument('--production', action='store_true')
    parser.add_argument('--baseurl', default='')
    args = parser.parse_args()
    root = args.site.resolve()
    pages = {p: Page(p.read_text()) for p in root.rglob('*.html')}
    assert pages, 'No generated pages'
    for path, page in pages.items():
        text = path.read_text()
        assert len(page.ids) == len(set(page.ids)), f'Duplicate ID: {path}'
        assert not page.iframes, f'PDF embedded before selection: {path}'
        assert 'clientSecret' not in text and 'gitalk' not in text, f'Legacy comments leaked: {path}'
        assert 'Writing archive' not in text and 'MathJax' not in text, f'Removed writing UI leaked: {path}'
        if not args.production:
            assert 'googletagmanager.com' not in text and 'G-CH97FJJG6N' not in text, f'Analytics in preview: {path}'
        elif path.name != 'index.html' or path.parent.name != 'home':
            if not path.name.startswith('google'):
                assert text.count("var measurementId = \"G-CH97FJJG6N\"") == 1, f'Missing/duplicate Analytics: {path}'
                assert 'window.location.hostname !== "junhyoung-chung.github.io"' in text, f'Missing Analytics host gate: {path}'
        for tag, ref in page.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                continue
            raw_path = unquote(url.path)
            if not raw_path:
                target = path
            elif raw_path.startswith('/'):
                if args.baseurl:
                    assert raw_path == args.baseurl or raw_path.startswith(args.baseurl + '/'), f'Missing baseurl: {path}: {ref}'
                    raw_path = raw_path[len(args.baseurl):]
                target = root / raw_path.lstrip('/')
            else:
                target = path.parent / raw_path
            if target.is_dir():
                target = target / 'index.html'
            target = target.resolve()
            assert target.is_relative_to(root) and target.is_file(), f'Broken local link: {path.relative_to(root)} -> {ref}'
            if url.fragment and tag == 'a' and target in pages:
                assert unquote(url.fragment) in pages[target].ids, f'Broken fragment: {path.relative_to(root)} -> {ref}'
    for name in ['DESIGN.md', 'MIGRATION.md', 'README.md', 'scripts', 'tests', 'review', 'vendor', '_drafts', '_posts', 'archive', '.git']:
        assert not (root / name).exists(), f'Internal file published: {name}'
    assert not list(root.glob('[0-9][0-9][0-9][0-9]/*/*/*.html')), 'Removed dated article route still published'
    total = sum(p.stat().st_size for p in root.rglob('*') if p.is_file())
    assert total < 200 * 1024 * 1024, f'Site exceeds the 200 MiB review budget: {total}'
    print(f'PASS: {len(pages)} HTML pages, local links/anchors, no eager PDFs, Analytics gates; site {total / 2**20:.2f} MiB')

if __name__ == '__main__':
    main()
