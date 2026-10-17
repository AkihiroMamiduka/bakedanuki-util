"""相対パス解決APIの引数と戻り値型を固定する。"""

from pathlib import Path
from typing import assert_type

from bd_util.py.path import resolve_relative_path

assert_type(resolve_relative_path(__file__, "menu.png"), Path)
assert_type(
    resolve_relative_path(
        base_file=Path(__file__), relative_path="sub/data.json"
    ),
    Path,
)
