#!/usr/bin/env python3
"""Run from any checkout without installing dependencies."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cropmodels.cli import main

raise SystemExit(main())
