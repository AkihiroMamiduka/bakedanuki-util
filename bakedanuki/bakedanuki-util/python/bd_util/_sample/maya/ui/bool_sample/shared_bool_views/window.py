# coding: utf-8
from __future__ import annotations

from ......ui import BoolViewModel, qt
from .widget import SharedBoolViewsWidget


class SharedBoolViewsWindow(qt.QDialog):
    """共有ViewModelに接続したWidgetを配置するsample Window。"""

    def __init__(
        self,
        view_model: BoolViewModel,
        window_name: str,
        *,
        data_description: str = "Shared Data Store",
        maya_description: str = "None",
        parent: qt.QWidget | None = None,
    ) -> None:
        """共通のViewModelとWindow識別名を受け取って表示を構成する。"""
        # A / BをタイトルとobjectNameで区別する。
        super().__init__(parent)
        self.setObjectName(f"bdUtilSharedBoolViewsWindow{window_name}")
        self.setWindowTitle(
            f"bakedanuki-util shared bool views - Window {window_name}"
        )
        self.resize(480, 360)

        # WindowはWidgetを配置し、共有bindingの所有はManagerへ任せる。
        self.bool_views_widget = SharedBoolViewsWidget(
            view_model,
            data_description=data_description,
            maya_description=maya_description,
            parent=self,
        )

        # このWindowだけを閉じる操作を用意する。
        close_button = qt.QPushButton(f"Close Window {window_name}", self)
        close_button.clicked.connect(self.close)

        # Feature WidgetとWindow操作を縦に並べる。
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.bool_views_widget)
        layout.addWidget(close_button)
