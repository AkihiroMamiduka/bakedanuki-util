"""パス解決とExplorer操作APIの引数・戻り値型を固定する。"""

from pathlib import Path
from typing import assert_type

from bd_util.py.path import open_path_in_explorer, resolve_relative_path

assert_type(resolve_relative_path(__file__, "menu.png"), Path)
assert_type(open_path_in_explorer(Path(__file__)), None)
assert_type(
    resolve_relative_path(
        base_file=Path(__file__), relative_path="sub/data.json"
    ),
    Path,
)
