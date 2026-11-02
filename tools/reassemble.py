"""Reassemble chunked tool sources before CI build."""

from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "chunks" / "manifest.json"


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for name, spec in data.items():
        blob = "".join((ROOT / part).read_text(encoding="ascii") for part in spec["parts"])
        raw = base64.b64decode(blob)
        digest = hashlib.sha256(raw).hexdigest()
        if digest != spec["sha256"]:
            raise SystemExit(f"{name} sha256 mismatch: got {digest}, want {spec['sha256']}")
        target = ROOT / name
        target.write_bytes(raw)
        print(f"Wrote {target} ({len(raw)} bytes)")


if __name__ == "__main__":
    main()
