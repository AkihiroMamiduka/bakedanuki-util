# coding: utf-8
from __future__ import annotations

import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
PACKAGE_PYTHON_DIR = ROOT_DIR / "bakedanuki" / "bakedanuki-util" / "python"

if str(PACKAGE_PYTHON_DIR) not in sys.path:
    sys.path.insert(0, str(PACKAGE_PYTHON_DIR))
