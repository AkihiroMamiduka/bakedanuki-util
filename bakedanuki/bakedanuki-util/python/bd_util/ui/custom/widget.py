from typing import Any, Literal


from .. import qt

LayoutType = Literal["v_box", "h_box"]


class CustomWidget(qt.QWidget):
    """縦または横のBoxLayoutを初期配置したWidget。"""

    def __init__(
        self,
        *args: Any,
        layout_type: LayoutType = "v_box",
        **kwargs: Any,
    ):
        """指定したLayoutを持つWidgetを作る。

        Args:
            *args: ``QWidget`` へ渡す位置引数。
            layout_type: ``v_box`` は縦、``h_box`` は横に配置する。
            **kwargs: ``QWidget`` へ渡すキーワード引数。
        """
        super().__init__(*args, **kwargs)

        # 指定した方向のBoxLayoutを、このWidgetの初期Layoutとして設定する。
        if layout_type == "v_box":
            self.setLayout(qt.QVBoxLayout())
        elif layout_type == "h_box":
            self.setLayout(qt.QHBoxLayout())


wid = CustomWidget(layout_type="v_box")
