# coding: utf-8
"""値とstepの複合Viewで正本・表示設定・寿命の境界を検証する。"""

import gc
from weakref import ref

import pytest

from bd_util.ui import (
    FloatBinding,
    FloatPresentation,
    FloatSpinBox,
    FloatStepSpinBox,
    FloatValueStepSpinBox,
    qt,
)


class Data:
    """書込み回数と未丸めの正本を記録する。"""

    def __init__(self):
        """表示精度より細かい初期値を用意する。"""
        self._value = 0.123456789
        self.writes = []

    @property
    def value(self):
        """値を取得する。"""
        return self._value

    @value.setter
    def value(self, value):
        """実際の書込みだけを記録する。"""
        self.writes.append(value)
        self._value = value


def flush():
    """破棄予約とqueued signalを処理する。"""
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    qt.QApplication.processEvents()


def enter(widget, text):
    """step入力欄の文字をEnterで確定する。"""
    widget.lineEdit().setText(text)
    for kind in (qt.QEvent.Type.KeyPress, qt.QEvent.Type.KeyRelease):
        qt.QApplication.sendEvent(
            widget,
            qt.QtGui.QKeyEvent(
                kind,
                qt.Qt.Key.Key_Return,
                qt.Qt.KeyboardModifier.NoModifier,
            ),
        )


@pytest.fixture
def owner(qt_application):
    """各testに独立したWidgetの親を用意する。"""
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    flush()


@pytest.mark.parametrize("use_binding", [True, False])
def test_step_changes_only_view_and_value_input_writes_once(
    owner, use_binding
):
    """stepの入力は正本を維持し、値入力だけが一度書き込む。"""
    data = Data()
    binding = FloatBinding.from_attribute(data, "value", parent=owner)
    editor = FloatValueStepSpinBox(
        binding if use_binding else binding.view_model,
        owner,
        decimals=3,
        single_step=1,
        step_mode="multiplicative",
    )
    other = FloatValueStepSpinBox(binding, owner, single_step=15)
    changes = []
    editor.settingsChanged.connect(lambda: changes.append(editor.singleStep()))
    assert isinstance(editor.spin_box, FloatSpinBox)
    assert isinstance(editor.step_spin_box, FloatStepSpinBox)
    assert (
        editor.view_model is editor.spin_box.view_model is binding.view_model
    )
    editor.step_spin_box.stepDown()
    enter(editor.step_spin_box, "0.001")
    editor.setSingleStep(0.001)
    assert changes == [0.1, 0.001]
    assert other.singleStep() == 15
    assert data.writes == []
    assert data.value == 0.123456789
    editor.spin_box.setValue(0.5)
    editor.spin_box.stepUp()
    assert data.writes == [0.5, 0.501]
    assert other.spin_box.value() == 0.501


@pytest.mark.parametrize("show_unit", [False, True])
def test_additive_step_and_unit_changes_preserve_numeric_step(
    owner, show_unit
):
    """加算stepと単位変更を値編集から分離し、古い単位の保留入力を捨てる。"""
    data = Data()
    binding = FloatBinding.from_attribute(data, "value", parent=owner)
    unit_options = {"step_show_unit": True} if show_unit else {}
    editor = FloatValueStepSpinBox(
        binding,
        owner,
        single_step=15,
        step_mode="additive",
        step_increment=15,
        **unit_options,
    )
    assert not editor.spin_box.isUnitVisible()
    if show_unit:
        editor.spin_box.setUnitVisible(True)
    editor.step_spin_box.stepUp()
    assert editor.singleStep() == 30
    enter(editor.step_spin_box, "7.5")
    editor.step_spin_box.lineEdit().setText("999")
    binding.view_model.set_presentation_adapter(
        lambda p: FloatPresentation(scale=0.01, suffix=" m")
    )
    assert editor.singleStep() == editor.step_spin_box.value() == 7.5
    assert (
        editor.step_spin_box.suffix()
        == editor.spin_box.suffix()
        == (" m" if show_unit else "")
    )
    assert "999" not in editor.step_spin_box.text()
    assert data.writes == []


def test_disposal_stops_both_fields_and_pending_step(owner):
    """終了通知後は値とstepを停止し、保留入力の確定通知も発生させない。"""
    binding = FloatBinding.from_attribute(Data(), "value", parent=owner)
    editor = FloatValueStepSpinBox(binding, owner, single_step=1)
    changes = []
    editor.settingsChanged.connect(lambda: changes.append(editor.singleStep()))
    editor.step_spin_box.lineEdit().setText("999")
    binding.view_model.dispose()
    assert not editor.spin_box.isEnabled()
    assert not editor.step_spin_box.isEnabled()
    assert editor.step_spin_box.value() == 1
    editor.step_spin_box.setValue(2)
    assert editor.singleStep() == editor.step_spin_box.value() == 1
    assert changes == []
    with pytest.raises(RuntimeError):
        editor.setSingleStep(3)
    with pytest.raises(RuntimeError):
        _ = editor.view_model


def test_qt_deletion_of_source_stops_step_and_view_keeps_binding_alive(owner):
    """ViewだけでもBindingを保持し、QObject破棄後にはstepを停止する。"""
    binding = FloatBinding.from_attribute(Data(), "value")
    binding_ref = ref(binding)
    editor = FloatValueStepSpinBox(binding, owner)
    del binding
    gc.collect()
    assert binding_ref() is not None
    editor.view_model.deleteLater()
    flush()
    assert not editor.step_spin_box.isEnabled()
    assert not editor.spin_box.isEnabled()


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"single_step": 0}, ValueError),
        ({"single_step": float("inf")}, ValueError),
        ({"single_step": True}, TypeError),
        ({"step_mode": "unknown"}, ValueError),
        ({"step_increment": -1}, ValueError),
        ({"decimals": -1}, ValueError),
        ({"step_show_unit": 1}, TypeError),
    ],
)
def test_invalid_constructor_leaves_no_partial_view(owner, settings, error):
    """不正設定は子生成前に拒否し、共有Bindingへ影響させない。"""
    binding = FloatBinding.from_attribute(Data(), "value", parent=owner)
    before = owner.children()
    with pytest.raises(error):
        FloatValueStepSpinBox(binding, owner, **settings)
    assert owner.children() == before
    assert not binding.is_disposed


def test_readonly_value_still_allows_local_step_settings(owner):
    """正本が読取り専用でも、View自身のstep設定は変更できる。"""

    class Readonly:
        """setterのない値を持つ正本。"""

        @property
        def value(self):
            """固定の値を返す。"""
            return 1.0

    binding = FloatBinding.from_attribute(Readonly(), "value", parent=owner)
    editor = FloatValueStepSpinBox(binding, owner, step_show_unit=False)
    assert not editor.spin_box.isEnabled()
    assert editor.step_spin_box.isEnabled()
    editor.setSingleStep(2)
    assert binding.value == 1
    assert editor.singleStep() == 2
