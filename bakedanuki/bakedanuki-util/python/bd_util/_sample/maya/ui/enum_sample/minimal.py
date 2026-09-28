# coding: utf-8
from .....maya.ui import MayaWindowController
from .....ui import EnumBinding, qt
from ._window import EnumSampleWindow
from .data import EnumData, MODE_DEFINITION


class MinimalEnumWindow(EnumSampleWindow):
    """Python オブジェクトの `mode` を編集する最小 enum サンプル。"""

    def __init__(self, parent: qt.QWidget | None = None) -> None:
        self.data = EnumData()
        super().__init__(
            lambda owner: EnumBinding.from_attribute(
                self.data, "mode", definition=MODE_DEFINITION, parent=owner
            ),
            "bakedanuki-util enum / Python",
            parent,
        )


_controller = MayaWindowController(MinimalEnumWindow)


def show() -> MinimalEnumWindow:
    """サンプル Window を表示し、表示中なら同じインスタンスを返す。"""
    return _controller.show()


def dispose() -> None:
    """サンプル Window とその binding を破棄する。"""
    _controller.dispose()
