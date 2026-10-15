# coding: utf-8
"""値とStepの複合Viewが両欄を表示領域に収めることを検証する。"""

from dataclasses import dataclass

import pytest

from bd_util.ui import (
    FloatBinding,
    FloatValueStepSpinBox,
    IntBinding,
    IntValueStepSpinBox,
    qt,
)


@dataclass
class Values:
    """整数と浮動小数点の入力元。"""

    integer: int = 42
    floating: float = 42.0


@pytest.mark.parametrize("integer", [True, False])
@pytest.mark.parametrize("value_width", [None, 156])
def test_step_stays_visible_when_value_width_changes(
    qt_application, integer, value_width
):
    """自動幅と固定幅の値欄でStepが隠れず、拡大後も幅を保つ。"""
    owner = qt.QWidget()
    values = Values()
    if integer:
        binding = IntBinding.from_attribute(values, "integer", parent=owner)
        editor = IntValueStepSpinBox(
            binding, owner, value_width=value_width, step_width=68
        )
    else:
        binding = FloatBinding.from_attribute(values, "floating", parent=owner)
        editor = FloatValueStepSpinBox(
            binding, owner, value_width=value_width, step_width=68
        )
    layout = qt.QVBoxLayout(owner)
    layout.addWidget(editor)
    try:
        owner.show()
        for width in (500, 800, 500):
            owner.resize(width, owner.sizeHint().height())
            qt.QApplication.processEvents()
            value_rect = editor.spin_box.geometry()
            step_rect = editor.step_spin_box.geometry()
            assert editor.rect().contains(value_rect)
            assert editor.rect().contains(step_rect)
            assert value_rect.right() < step_rect.left()
            assert step_rect.width() == 68
            assert editor.step_spin_box.visibleRegion().boundingRect() == (
                editor.step_spin_box.rect()
            )
            if value_width is not None:
                assert value_rect.width() == value_width
    finally:
        binding.dispose()
        owner.close()
        owner.deleteLater()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
