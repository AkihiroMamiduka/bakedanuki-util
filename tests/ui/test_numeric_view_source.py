# coding: utf-8
"""数値Viewを再利用するときの旧通知・下書き・連続編集の境界を検証する。"""

import gc
from weakref import ref

import pytest

from bd_util.ui import (
    BoolViewModel,
    FloatBinding,
    FloatPresentation,
    FloatRangeSliderSpinBox,
    FloatSlider,
    FloatSliderSpinBox,
    FloatSpinBox,
    FloatValueStepSpinBox,
    FloatViewModel,
    IntBinding,
    IntPresentation,
    IntRangeSliderSpinBox,
    IntSlider,
    IntSliderSpinBox,
    IntSpinBox,
    IntValueStepSpinBox,
    IntViewModel,
    qt,
)
from bd_util.ui.binding._view_source import ViewSourceConnections


class Data:
    """再接続前後の正本と実際の書込みを記録する。"""

    def __init__(self, value):
        """初期値を無書込みで保持する。"""
        self._value = value
        self.writes = []

    @property
    def value(self):
        """現在の正本を返す。"""
        return self._value

    @value.setter
    def value(self, value):
        """実変更要求を記録して正本を更新する。"""
        self.writes.append(value)
        self._value = value


def flush():
    """破棄予約と旧世代のqueued通知を処理する。"""
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    qt.QApplication.processEvents()
    qt.QApplication.processEvents()


@pytest.fixture
def owner(qt_application):
    """数値Viewと正本をtest終了時にまとめて破棄する。"""
    widget = qt.QWidget()
    yield widget
    widget.deleteLater()
    flush()


def bind(kind, value, owner):
    """同じ入力範囲で型別の書込み記録付きBindingを作る。"""
    data = Data(float(value) if kind == "float" else int(value))
    factory, presentation = (
        (FloatBinding, FloatPresentation(minimum=0, maximum=100))
        if kind == "float"
        else (IntBinding, IntPresentation(minimum=0, maximum=100))
    )
    binding = factory.from_attribute(
        data, "value", presentation=presentation, parent=owner
    )
    return data, binding


def make_editor(kind, shape, source, owner):
    """同じテストを単体Viewと複合Viewの両方へ適用する。"""
    factories = (
        {
            "spin": FloatSpinBox,
            "slider": FloatSlider,
            "step": FloatValueStepSpinBox,
            "combo": FloatSliderSpinBox,
            "range": FloatRangeSliderSpinBox,
        }
        if kind == "float"
        else {
            "spin": IntSpinBox,
            "slider": IntSlider,
            "step": IntValueStepSpinBox,
            "combo": IntSliderSpinBox,
            "range": IntRangeSliderSpinBox,
        }
    )
    options = (
        {"minimum": 0, "maximum": 100}
        if shape in ("slider", "combo", "range")
        else {}
    )
    return factories[shape](source, owner, **options)


def spin(editor):
    """値の下書きを持つ入力欄を取得する。"""
    return getattr(editor, "spin_box", editor)


def slider(editor):
    """連続編集を持つ単体または複合のSliderを取得する。"""
    return getattr(editor, "slider", editor)


@pytest.mark.parametrize("kind", ["float", "int"])
@pytest.mark.parametrize("shape", ["spin", "slider", "step", "combo", "range"])
def test_replacement_ignores_old_disposal_and_queued_destruction(
    owner, kind, shape
):
    """旧Binding破棄のqueued通知が、新しい入力元を無効にしない。"""
    old_data, old = bind(kind, 12, owner)
    new_data, new = bind(kind, 34, owner)
    editor = make_editor(kind, shape, old, owner)
    old.dispose()
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    editor.set_source(new)
    flush()
    assert editor.view_model is new.view_model
    assert editor.isEnabled()
    if shape != "slider":
        assert spin(editor).value() == 34
        assert spin(editor).isEnabled()
    if shape in ("step", "range"):
        assert editor.step_spin_box.isEnabled()
    assert not old_data.writes
    assert not new_data.writes


@pytest.mark.parametrize("kind", ["float", "int"])
@pytest.mark.parametrize("shape", ["spin", "step", "combo", "range"])
def test_drafts_are_cancelled_and_old_changes_do_not_repaint(
    owner, kind, shape
):
    """値とStepの旧下書きを捨て、旧正本の後続変更を新表示へ反映しない。"""
    old_data, old = bind(kind, 12, owner)
    new_data, new = bind(kind, 34, owner)
    editor = make_editor(kind, shape, old, owner)
    field = spin(editor)
    field.lineEdit().setText("99")
    field.lineEdit().setModified(True)
    if shape in ("step", "range"):
        editor.step_spin_box.lineEdit().setText("77")
        editor.step_spin_box.lineEdit().setModified(True)
    editor.set_source(new.view_model)
    old.set_value(56)
    old.dispose()
    flush()
    field.interpretText()
    assert field.value() == 34
    if shape in ("step", "range"):
        editor.step_spin_box.interpretText()
        assert editor.step_spin_box.value() != 77
    assert old_data.writes == [56]
    assert not new_data.writes


@pytest.mark.parametrize("kind", ["float", "int"])
@pytest.mark.parametrize("shape", ["slider", "combo", "range"])
def test_replacement_finishes_drag_and_ignores_old_mouse_movement(
    owner, kind, shape
):
    """付け替えで旧編集を終了し、押下中に残った移動は新正本へ渡さない。"""
    old_data, old = bind(kind, 12, owner)
    new_data, new = bind(kind, 34, owner)
    editor = make_editor(kind, shape, old, owner)
    control = slider(editor)
    control.sliderPressed.emit()
    assert old.view_model.is_editing
    editor.set_source(new)
    assert not old.view_model.is_editing
    assert not new.view_model.is_editing
    qt.QApplication.sendEvent(
        control,
        qt.QtGui.QMouseEvent(
            qt.QEvent.Type.MouseMove,
            qt.QPointF(80, 5),
            qt.QPointF(80, 5),
            qt.Qt.MouseButton.NoButton,
            qt.Qt.MouseButton.LeftButton,
            qt.Qt.KeyboardModifier.NoModifier,
        ),
    )
    assert not old_data.writes
    assert not new_data.writes


@pytest.mark.parametrize("kind", ["float", "int"])
@pytest.mark.parametrize("shape", ["spin", "slider", "step", "combo", "range"])
def test_invalid_source_keeps_previous_source(owner, kind, shape):
    """終了済み入力元は切替前に拒否し、元の表示と入力先を維持する。"""
    old_data, old = bind(kind, 12, owner)
    _, new = bind(kind, 34, owner)
    editor = make_editor(kind, shape, old, owner)
    invalid = new.view_model
    invalid.dispose()
    with pytest.raises(RuntimeError):
        editor.set_source(invalid)
    assert editor.view_model is old.view_model
    assert not old_data.writes


@pytest.mark.parametrize("kind", ["float", "int"])
@pytest.mark.parametrize("shape", ["spin", "slider", "step", "combo"])
def test_source_change_inside_handler_does_not_write_either_source(
    owner, kind, shape
):
    """handlerが未処理を返しても、再入で付け替えた後は旧入力を適用しない。"""
    old_data, old = bind(kind, 12, owner)
    new_data, new = bind(kind, 34, owner)
    editor = make_editor(kind, shape, old, owner)
    field = slider(editor) if shape == "slider" else spin(editor)

    def change_source(_value):
        """入力処理の途中で、同じViewを別の正本へ付け替える。"""
        editor.set_source(new)
        return False

    field.setValueRequestHandler(change_source)
    field.setValue(80)
    assert editor.view_model is new.view_model
    assert not old_data.writes
    assert not new_data.writes


@pytest.mark.parametrize("kind", ["float", "int"])
@pytest.mark.parametrize("shape", ["slider", "combo", "range"])
def test_nested_replacement_during_edit_finished_keeps_latest_source(
    owner, kind, shape
):
    """旧操作の終了通知から再接続された場合は、最後の入力元を優先する。"""
    old_data, old = bind(kind, 12, owner)
    new_data, new = bind(kind, 34, owner)
    latest_data, latest = bind(kind, 56, owner)
    editor = make_editor(kind, shape, old, owner)
    control = slider(editor)
    control.sliderPressed.emit()

    def choose_latest():
        """終了通知から別の入力元を選び直す。"""
        editor.set_source(latest)

    control.editFinished.connect(choose_latest)
    editor.set_source(new)
    assert editor.view_model is latest.view_model
    assert control.view_model is latest.view_model
    if shape != "slider":
        assert spin(editor).view_model is latest.view_model
    assert not old_data.writes
    assert not new_data.writes
    assert not latest_data.writes


@pytest.mark.parametrize("kind", ["float", "int"])
def test_source_change_inside_step_handler_does_not_apply_fallback(
    owner, kind
):
    """Step handlerからの再接続後はQt既定の増減を新正本へ適用しない。"""
    old_data, old = bind(kind, 12, owner)
    new_data, new = bind(kind, 34, owner)
    editor = make_editor(kind, "step", old, owner)

    def change_source(_steps):
        """増減処理中に接続先を変更し、既定処理を要求する。"""
        editor.set_source(new)
        return False

    editor.spin_box.setStepRequestHandler(change_source)
    editor.spin_box.stepBy(1)
    assert editor.spin_box.value() == 34
    assert not old_data.writes
    assert not new_data.writes


@pytest.mark.parametrize("builtin", [False, True])
def test_source_connection_does_not_retain_destroyed_view(
    qt_application, builtin
):
    """接続済みのPython・Qt組込メソッドが破棄済みViewを保持しない。"""

    class Receiver(qt.QWidget):
        """Pythonのbound methodでも同じ寿命の契約を確認する。"""

        def receive(self, enabled):
            """sourceから入力可否を受け取る。"""
            self.setEnabled(enabled)

    source = BoolViewModel()
    widget = Receiver()
    weak_widget = ref(widget)
    connections = ViewSourceConnections(widget)
    connections.connect(
        source.value.changed, widget.setEnabled if builtin else widget.receive
    )
    widget.deleteLater()
    flush()
    del widget
    gc.collect()
    assert weak_widget() is None
    source.set_value_command.execute(True)
    source.deleteLater()
    flush()


@pytest.mark.parametrize("kind", ["float", "int"])
@pytest.mark.parametrize("shape", ["slider", "combo", "range"])
def test_disposed_destination_during_edit_finish_keeps_old_source(
    owner, kind, shape
):
    """終了通知で新入力元が失効した場合は、旧接続と複合Viewの整合を保つ。"""
    old_data, old = bind(kind, 12, owner)
    new_data, new = bind(kind, 34, owner)
    destination = new.view_model
    editor = make_editor(kind, shape, old, owner)
    control = slider(editor)
    control.sliderPressed.emit()

    def invalidate_destination():
        """切替の途中で接続候補を明示終了、またはQtから破棄する。"""
        if shape == "slider":
            destination.dispose()
        else:
            destination.deleteLater()
            qt.QApplication.sendPostedEvents(
                None, qt.QEvent.Type.DeferredDelete
            )

    control.editFinished.connect(invalidate_destination)
    with pytest.raises(RuntimeError):
        editor.set_source(new)
    assert editor.view_model is old.view_model
    assert control.view_model is old.view_model
    assert not old.view_model.is_editing
    if shape != "slider":
        assert spin(editor).view_model is old.view_model
    assert not old_data.writes
    assert not new_data.writes

    # 新入力元の失効後も、保持した旧入力元の表示通知は生きている
    old.set_value(56)
    if shape != "slider":
        assert spin(editor).value() == 56
    if shape == "range":
        assert editor.minimum_spin_box.isEnabled()
        assert editor.maximum_spin_box.isEnabled()
    flush()


@pytest.mark.parametrize("cancel", [False, True])
def test_source_destruction_is_deferred_and_respects_cleared_generation(
    qt_application, cancel
):
    """実Qt削除の通知を次のイベントへ渡し、その前の接続取消も尊重する。"""
    owner = qt.QWidget()
    source = qt.QObject()
    connections = ViewSourceConnections(owner)
    notifications = []

    def on_destroyed():
        """破棄後も有効な接続世代だけが通知を受け取ったことを記録する。"""
        notifications.append(True)

    connections.connect(
        source.destroyed, on_destroyed, queued=True, discard_args=True
    )
    source.deleteLater()
    qt.QApplication.sendPostedEvents(source, qt.QEvent.Type.DeferredDelete)
    assert not qt.isValid(source)
    assert not notifications
    if cancel:
        connections.clear()
    qt_application.processEvents()
    assert notifications == ([] if cancel else [True])
    owner.deleteLater()
    flush()
