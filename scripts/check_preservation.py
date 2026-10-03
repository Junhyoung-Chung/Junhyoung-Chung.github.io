#!/usr/bin/env python3
"""Check the migration's public content contract, before and after replacing the theme."""
from pathlib import Path
import argparse
import hashlib
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "f69ddd4b2d636ef892f324acacc82d282bda643f"
PRESERVED = ["assets/CV.pdf", "google5272b05d391d3ed0.html", "googlee35a5a5e4a9bd991.html"]
TITLES = [
    "Prediction of high-risk mountain accident areas using a Hurdle model",
    "Discovering causal structures in corrupted data: Frugality in anchored Gaussian DAG models",
    "Learning distribution-free anchored linear structural equation models in the presence of measurement error",
    "Horse race rank prediction using learning-to-rank approaches",
    "Convex distance operator transport: A convex and geometry-preserving formulation",
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path)
    parser.add_argument("--compare-base", action="store_true", help="Migration-only check: require the CV to match the original revision byte for byte")
    args = parser.parse_args()
    target = args.site.resolve() if args.site else ROOT
    for name in PRESERVED:
        if name == "assets/CV.pdf" and not args.compare_base:
            assert (target / name).read_bytes().startswith(b"%PDF-"), "CV must remain a PDF"
            continue
        previous = subprocess.check_output(["git", "show", f"{BASE}:{name}"], cwd=ROOT)
        assert hashlib.sha256((target / name).read_bytes()).digest() == hashlib.sha256(previous).digest(), name
    publications = (target / "publications/index.html").read_text()
    for title in TITLES:
        assert title in publications, f"Missing publication: {title}"
    assert publications.index("Journal Papers") < publications.index("Conference Paper")
    if args.site:
        routes = ["index.html", "home/index.html", "publications/index.html", "research/index.html", "archive/index.html", "404.html"]
        for post in (ROOT / "_posts").glob("*.md"):
            year, month, day, slug = post.stem.split("-", 3)
            routes.append(f"{year}/{month}/{day}/{slug}.html")
        for route in routes:
            assert (target / route).is_file(), f"Missing route: {route}"
    else:
        assert "G-CH97FJJG6N" in (ROOT / "_config.yml").read_text()
    print("PASS: CV" + (" bytes" if args.compare_base else " PDF") + ", verification bytes, publication titles/order" + (", legacy routes" if args.site else ", GA4 ID"))

if __name__ == "__main__":
    main()
