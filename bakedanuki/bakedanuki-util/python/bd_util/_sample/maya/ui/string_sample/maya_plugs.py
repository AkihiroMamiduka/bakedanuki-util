# coding: utf-8
from collections.abc import Sequence
from maya import cmds

from .....maya.ui import (
    MayaStringPlugsBinding,
    MayaWindowController,
    resolve_string_plug,
)
from ._plugs_window import StringPlugsSampleWindow

_controller: MayaWindowController[StringPlugsSampleWindow] | None = None


def show(node_names: Sequence[str]) -> StringPlugsSampleWindow:
    """指定順の既存jointを正本とする一括編集Windowを開く。"""
    global _controller
    if isinstance(node_names, str) or not node_names:
        raise ValueError("node_namesには一つ以上のjoint名を指定してください")
    names = tuple(node_names)
    for name in names:
        if cmds.nodeType(name) != "joint":
            raise TypeError(f"jointではありません: {name}")
    plugs = tuple(resolve_string_plug(name, "otherType") for name in names)
    dispose()
    _controller = MayaWindowController(
        lambda parent: StringPlugsSampleWindow(
            lambda owner: MayaStringPlugsBinding(plugs, parent=owner), parent
        )
    )
    return _controller.show()


def show_selected() -> StringPlugsSampleWindow:
    """現在選択しているjointを指定順で一度だけ取得して表示する。"""
    names = cmds.ls(selection=True, long=True, type="joint") or []
    return show(names)


def dispose() -> None:
    """表示中のWindowと全Maya callbackを破棄する。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
