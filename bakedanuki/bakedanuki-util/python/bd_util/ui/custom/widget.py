from typing import Any, Literal


from .. import qt

LayoutType = Literal["v_box", "h_box"]


class CustomWidget(qt.QWidget):
    def __init__(
        self,
        *args: Any,
        layout_type: LayoutType = "v_box",
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)

        # layout
        if layout_type == "v_box":
            self.setLayout(qt.QVBoxLayout())
        elif layout_type == "h_box":
            self.setLayout(qt.QHBoxLayout())


wid = CustomWidget(layout_type="v_box")
