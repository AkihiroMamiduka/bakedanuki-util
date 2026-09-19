# coding: utf-8
"""既存の値Viewが外側の一括入力へ操作を委譲できることを検証する。"""

from bd_util.ui import (
    BoolCheckBox,
    BoolViewModel,
    EnumComboBox,
    EnumDefinition,
    EnumViewModel,
    FloatSlider,
    FloatSpinBox,
    FloatViewModel,
    qt,
)


def test_float_spin_box_delegates_value_and_step(
    qt_application: qt.QApplication,
) -> None:
    """値入力と上下操作を処理済みにすると、元の正本へ重ねて入力しない。"""
    owner = qt.QWidget()
    view_model = FloatViewModel(2.0, owner)
    spin_box = FloatSpinBox(view_model, owner, single_step=0.5)
    values: list[float] = []
    steps: list[int] = []
    spin_box.setValueRequestHandler(lambda value: values.append(value) is None)
    spin_box.setStepRequestHandler(lambda step: steps.append(step) is None)

    spin_box.setValue(4.0)
    spin_box.stepBy(2)

    assert values == [4.0]
    assert steps == [2]
    assert view_model.value.value == 2.0
    assert spin_box.value() == 2.0


def test_float_slider_delegates_continuous_edit(
    qt_application: qt.QApplication,
) -> None:
    """Sliderの連続入力を外側へ渡し、開始と終了も一度ずつ通知する。"""
    owner = qt.QWidget()
    view_model = FloatViewModel(2.0, owner)
    slider = FloatSlider(view_model, owner, minimum=0.0, maximum=10.0)
    values: list[float] = []
    events: list[str] = []
    slider.setValueRequestHandler(lambda value: values.append(value) is None)
    slider.editStarted.connect(lambda: events.append("start"))
    slider.editFinished.connect(lambda: events.append("finish"))

    slider.setSliderDown(True)
    slider.setValue(500)
    slider.setValue(700)
    slider.setSliderDown(False)

    assert values == [5.0, 7.0]
    assert events == ["start", "finish"]
    assert view_model.value.value == 2.0
    assert slider.value() == 200


def test_bool_check_box_delegates_value(
    qt_application: qt.QApplication,
) -> None:
    """CheckBox入力を処理済みにすると、元のbool正本を変更しない。"""
    owner = qt.QWidget()
    view_model = BoolViewModel(True, owner)
    check_box = BoolCheckBox(view_model, parent=owner)
    values: list[bool] = []
    check_box.setValueRequestHandler(
        lambda value: values.append(value) is None
    )

    check_box.click()

    assert values == [False]
    assert view_model.value.value is True
    assert check_box.isChecked()


def test_enum_combo_box_delegates_value(
    qt_application: qt.QApplication,
) -> None:
    """ComboBox入力を処理済みにすると、元のenum正本を変更しない。"""
    owner = qt.QWidget()
    definition = EnumDefinition.from_mapping({0: "Off", 5: "On"})
    view_model = EnumViewModel(0, owner, definition=definition)
    combo_box = EnumComboBox(view_model, owner)
    values: list[int] = []
    combo_box.setValueRequestHandler(
        lambda value: values.append(value) is None
    )

    combo_box.setCurrentIndex(1)

    assert values == [5]
    assert view_model.value.value == 0
    assert combo_box.currentIndex() == 0
