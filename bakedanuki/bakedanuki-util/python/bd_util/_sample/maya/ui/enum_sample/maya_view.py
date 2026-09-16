# coding: utf-8
from .....maya.ui import (
    MayaEnumBinding,
    MayaWindowController,
    resolve_enum_plug,
)
from .....ui import EnumDefinition
from ._window import EnumSampleWindow
from .data import EnumData, ROTATE_ORDER_DEFINITION

_controller: MayaWindowController[EnumSampleWindow] | None = None


def show(
    node_name: str,
    attribute_name: str = "rotateOrder",
    data: EnumData | None = None,
    *,
    definition: EnumDefinition = ROTATE_ORDER_DEFINITION,
) -> EnumSampleWindow:
    """Python初期値を既存Maya enumへ反映し、双方の入力を確認する。"""
    global _controller
    plug = resolve_enum_plug(node_name, attribute_name)
    data = data if data is not None else EnumData()
    dispose()
    _controller = MayaWindowController(
        lambda parent: EnumSampleWindow(
            lambda owner: MayaEnumBinding.from_attribute(
                data,
                "mode",
                definition=definition,
                maya_plug=plug,
                parent=owner,
            ),
            "bakedanuki-util enum / Python + Maya",
            parent,
        )
    )
    return _controller.show()


def dispose() -> None:
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
