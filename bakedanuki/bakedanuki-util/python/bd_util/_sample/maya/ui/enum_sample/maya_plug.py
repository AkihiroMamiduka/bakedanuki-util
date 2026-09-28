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
    """既存の Maya enum 属性を正本として表示する。

    新しい Window を開く前に、表示中の Window を破棄する。ノードは作成しない。

    Args:
        node_name: 対象ノード名。
        attribute_name: 対象の enum 属性名。

    Returns:
        対象属性を編集する Window。
    """
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
    """表示中の Window と Maya enum binding を破棄する。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
