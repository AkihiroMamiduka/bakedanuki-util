"""アイコンパス解決APIの戻り値型を固定する。"""

from pathlib import Path
from typing import assert_type

from bd_util.py.path import icon_path

assert_type(icon_path(__file__, "menu.png"), Path)
assert_type(icon_path(Path(__file__), "menu.png"), Path)
