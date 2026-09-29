# coding: utf-8
from .....maya.ui import (
    MayaStringPlugBinding,
    MayaWindowController,
    resolve_string_plug,
)
from ._window import StringSampleWindow

_controller: MayaWindowController[StringSampleWindow] | None = None


def show(node_name: str) -> StringSampleWindow:
    """既存jointのotherTypeを正本とする一行編集Windowを開く。"""
    global _controller
    plug = resolve_string_plug(node_name, "otherType")
    dispose()
    _controller = MayaWindowController(
        lambda parent: StringSampleWindow(
            lambda owner: MayaStringPlugBinding(plug, parent=owner),
            "bakedanuki-util string / joint.otherType",
            parent,
        )
    )
    return _controller.show()


def dispose() -> None:
    """表示中のWindowとMaya callbackを破棄する。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
