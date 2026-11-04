#!/usr/bin/env python3
"""Regroupe le repo.json de chaque plugin listé dans plugins.txt en un seul repo.json.

Si un dépôt est illisible ou invalide, le script s'arrête sans rien écrire :
le repo.json déjà publié reste en place plutôt que de perdre un plugin.
"""
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW_URL = "https://raw.githubusercontent.com/{repo}/main/repo.json"
REQUIRED_KEYS = ("InternalName", "Name", "AssemblyVersion", "DownloadLinkInstall")


def read_repos():
    lines = (ROOT / "plugins.txt").read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


def fetch_manifests(repo):
    with urllib.request.urlopen(RAW_URL.format(repo=repo), timeout=30) as response:
        # utf-8-sig : accepte un repo.json écrit avec un BOM par PowerShell.
        manifests = json.loads(response.read().decode("utf-8-sig"))

    if not isinstance(manifests, list) or not manifests:
        raise ValueError("repo.json doit être une liste non vide")
    for manifest in manifests:
        missing = [key for key in REQUIRED_KEYS if not manifest.get(key)]
        if missing:
            raise ValueError(f"champs manquants : {', '.join(missing)}")
    return manifests


def main():
    merged = []
    seen = set()
    for repo in read_repos():
        try:
            manifests = fetch_manifests(repo)
        except Exception as error:
            sys.exit(f"{repo} : {error}")

        for manifest in manifests:
            name = manifest["InternalName"].lower()
            if name in seen:
                sys.exit(f"{repo} : {manifest['InternalName']} est déjà présent")
            seen.add(name)
            merged.append(manifest)
            print(f"{manifest['InternalName']} {manifest['AssemblyVersion']}")

    text = json.dumps(merged, ensure_ascii=False, indent=2) + "\n"
    (ROOT / "repo.json").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
