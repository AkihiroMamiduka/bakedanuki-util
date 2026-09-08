# coding: utf-8
from __future__ import annotations

from ......ui import BoolBinding, BoolCheckBox, qt
from .data import DisplayOptionsData


class DisplayOptionsWidget(qt.QWidget):
    """3つのbool属性を編集し、変更通知で表示と編集可否を更新する。"""

    def __init__(
        self,
        data: DisplayOptionsData,
        parent: qt.QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.data = data
        self.visible_binding = BoolBinding.from_attribute(
            data, "visible", parent=self
        )
        self.labels_binding = BoolBinding.from_attribute(
            data, "show_labels", parent=self
        )
        self.editing_binding = BoolBinding.from_attribute(
            data, "allow_editing", parent=self
        )

        self.editing_check_box = BoolCheckBox(
            self.editing_binding, "Allow editing", self
        )
        self.options_group = qt.QGroupBox("Display options", self)
        self.visible_check_box = BoolCheckBox(
            self.visible_binding, "Visible", self.options_group
        )
        self.labels_check_box = BoolCheckBox(
            self.labels_binding, "Show labels", self.options_group
        )
        options_layout = qt.QVBoxLayout(self.options_group)
        options_layout.addWidget(self.visible_check_box)
        options_layout.addWidget(self.labels_check_box)

        preview_group = qt.QGroupBox("Preview", self)
        preview_group.setMinimumHeight(110)
        self.preview_content = qt.QWidget(preview_group)
        marker = qt.QFrame(self.preview_content)
        marker.setFrameShape(qt.QFrame.Shape.Box)
        marker.setLineWidth(2)
        marker.setFixedSize(48, 32)
        self.preview_label = qt.QLabel("Sample object", self.preview_content)
        self.preview_label.setAlignment(qt.Qt.AlignmentFlag.AlignCenter)
        content_layout = qt.QVBoxLayout(self.preview_content)
        content_layout.addWidget(marker, 0, qt.Qt.AlignmentFlag.AlignHCenter)
        content_layout.addWidget(self.preview_label)
        preview_layout = qt.QVBoxLayout(preview_group)
        preview_layout.addWidget(self.preview_content)

        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.editing_check_box)
        layout.addWidget(self.options_group)
        layout.addWidget(preview_group)

        self.visible_binding.changed.connect(self.preview_content.setVisible)
        self.labels_binding.changed.connect(self.preview_label.setVisible)
        # 親の操作可否で制御し、各Bool View自身のCommand実行可否と両立する。
        self.editing_binding.changed.connect(self.options_group.setEnabled)

        # changedは初期値を再通知しないため、初期表示を明示的に適用する。
        self.preview_content.setVisible(self.visible_binding.value)
        self.preview_label.setVisible(self.labels_binding.value)
        self.options_group.setEnabled(self.editing_binding.value)

    def refresh_from_data(self) -> None:
        """Pythonデータへ直接代入した値を、各Bindingへ読み直す。"""
        self.visible_binding.refresh()
        self.labels_binding.refresh()
        self.editing_binding.refresh()
