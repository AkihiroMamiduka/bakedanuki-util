# coding: utf-8
from .....maya.ui import (
    MayaEnumPlugBinding,
    MayaWindowController,
    resolve_enum_plug,
)
from ._window import EnumSampleWindow

_controller: MayaWindowController[EnumSampleWindow] | None = None


def show(
    node_name: str, attribute_name: str = "rotateOrder"
) -> EnumSampleWindow:
    """既存enum属性を正本にする。nodeを作成・初期化しない。"""
    global _controller
    plug = resolve_enum_plug(node_name, attribute_name)
    dispose()
    _controller = MayaWindowController(
        lambda parent: EnumSampleWindow(
            lambda owner: MayaEnumPlugBinding(plug, parent=owner),
            "bakedanuki-util enum / Maya plug",
            parent,
        )
    )
    return _controller.show()


def dispose() -> None:
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
