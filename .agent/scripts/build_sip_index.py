#!/usr/bin/env python3
"""
build_sip_index.py - Regenerates the skills, agents and workflows tables of the sip-marketing resolver.

Thin wrapper around the kit's generic generator (inbox SIP-020 of 0 Padrões): one generator for every
SIP hub, so the tables follow the same format everywhere.

Usage (from the hub root):
    python3 .agent/scripts/build_sip_index.py          # rewrite the tables
    python3 .agent/scripts/build_sip_index.py --check  # exit 1 if a table is stale
"""

import os
import subprocess
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parent.parent.parent
# Kit location: env SUPER_IA_PROJECTS_PATH, else the "0 Padrões" folder next to this hub.
KIT_DIR = Path(os.environ.get("SUPER_IA_PROJECTS_PATH", str(HUB.parent / "0 Padrões")))
KIT_GENERATOR = KIT_DIR / ".agent" / "scripts" / "build_sip_index.py"


def main() -> int:
    if not KIT_GENERATOR.is_file():
        print(f"Kit generator not found at {KIT_GENERATOR}; install the 0 Padrões kit on this machine.", file=sys.stderr)
        return 2
    cmd = [sys.executable, str(KIT_GENERATOR), "--hub", str(HUB), "--resolver", "sip-marketing", *sys.argv[1:]]
    return subprocess.run(cmd).returncode


if __name__ == "__main__":
    sys.exit(main())
