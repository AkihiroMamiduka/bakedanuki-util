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
    """Python 側の値を既存 Maya enum 属性と同期する Window を表示する。

    Args:
        node_name: 対象ノード名。
        attribute_name: 対象の enum 属性名。
        data: Python 側の `mode` を保持するオブジェクト。`None` なら新規作成。
        definition: enum の整数値と表示名の対応。

    Returns:
        Python と Maya の値を編集する Window。
    """
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
    """表示中の Window と Python・Maya 間の binding を破棄する。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
