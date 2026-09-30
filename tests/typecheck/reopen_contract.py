# coding: utf-8
"""開いているtoolの再表示APIの公開型を確認する。"""

from typing import assert_type

from bd_util.maya.ui import OpenTool, snapshot_open_tools

assert_type(snapshot_open_tools("bd_tools"), tuple[OpenTool, ...])
assert_type(
    snapshot_open_tools(
        "bd_tools",
        dock_tools=((("bd_tools", "sample", "sample.ui", "show"), "control"),),
    ),
    tuple[OpenTool, ...],
)
