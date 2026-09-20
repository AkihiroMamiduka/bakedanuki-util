# coding: utf-8
from dataclasses import dataclass

import pytest

from bd_util.ui import (
    EnumBinding,
    EnumComboBox,
    EnumDefinition,
    EnumItem,
    EnumLabel,
    EnumViewModel,
    PythonEnumAttributeStore,
    qt,
)

DEFINITION = EnumDefinition.from_mapping(
    {-2: "Negative", 0: "Off", 5: "Preview", 10: "Final"}
)


@dataclass
class Data:
    mode: int = 0


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def wheel(widget, delta=120):
    """フォーカスを移さず、指定量のホイールイベントを送る。"""
    event = qt.QtGui.QWheelEvent(
        qt.QPointF(5, 5),
        qt.QPointF(5, 5),
        qt.QPoint(),
        qt.QPoint(0, delta),
        qt.Qt.MouseButton.NoButton,
        qt.Qt.KeyboardModifier.NoModifier,
        qt.Qt.ScrollPhase.NoScrollPhase,
        False,
    )
    qt.QApplication.sendEvent(widget, event)


@pytest.mark.parametrize("value", [True, False, 1.0, "5", None])
def test_invalid_values_never_write_python(value):
    data = Data()
    store = PythonEnumAttributeStore(data, "mode", definition=DEFINITION)
    with pytest.raises(TypeError):
        store.write(value)
    assert data.mode == 0
    data.mode = value
    with pytest.raises(TypeError):
        store.read()


def test_definition_is_immutable_and_validates_keys_and_names():
    mapping = {5: "Preview", -2: "Negative"}
    definition = EnumDefinition.from_mapping(mapping)
    mapping[5] = "Modified"
    assert definition.items == (
        EnumItem(5, "Preview"),
        EnumItem(-2, "Negative"),
    )
    assert definition.matches(
        EnumDefinition.from_mapping({-2: "Negative", 5: "Preview"})
    )
    for items in (
        (EnumItem(0, "A"), EnumItem(0, "B")),
        (EnumItem(0, "A"), EnumItem(1, "A")),
    ):
        with pytest.raises(ValueError):
            EnumDefinition(items)
    with pytest.raises(TypeError):
        EnumDefinition([EnumItem(0, "A")])
    with pytest.raises(ValueError):
        EnumItem(0, "")


def test_shared_views_use_values_not_positions_and_preserve_unknown(
    qt_application,
):
    data = Data(5)
    binding = EnumBinding.from_attribute(data, "mode", definition=DEFINITION)
    first = EnumComboBox(binding)
    second = EnumComboBox(binding.view_model)
    label = EnumLabel(binding)
    events = []
    binding.changed.connect(events.append)
    try:
        assert first.currentIndex() == 2
        assert label.text() == "Preview"
        first.setCurrentIndex(3)
        assert binding.value == data.mode == 10
        assert second.currentIndex() == 3
        assert label.text() == "Final"
        assert events == [10]
        data.mode = 1
        assert binding.value == 10
        binding.refresh()
        assert binding.value == 1
        assert not binding.is_value_defined
        assert first.currentIndex() == -1
        assert first.placeholderText() == "未定義 (1)"
        assert label.text() == "未定義 (1)"
        assert first.isEnabled()
        with pytest.raises(ValueError):
            binding.set_value(1)
        assert data.mode == 1
        first.setCurrentIndex(0)
        assert data.mode == binding.value == -2
        first.setInputEnabled(False)
        first.setCurrentIndex(1)
        assert data.mode == -2
        second.setCurrentIndex(1)
        assert data.mode == 0
        assert not first.isEnabled()
        assert label.text() == "Off"
    finally:
        for view in (first, second, label):
            view.deleteLater()
        binding.dispose()
        flush()


def test_combo_wheel_focus_option_preserves_default_and_allows_override(
    qt_application,
):
    """enum欄で非フォーカス時のホイール受付を切り替える。"""
    data = Data(5)
    binding = EnumBinding.from_attribute(data, "mode", definition=DEFINITION)
    owner = qt.QWidget()
    default = EnumComboBox(binding, owner)
    custom = EnumComboBox(binding, owner, wheel_requires_focus=True)
    other = qt.QLineEdit(owner)
    layout = qt.QVBoxLayout(owner)
    layout.addWidget(default)
    layout.addWidget(custom)
    layout.addWidget(other)
    owner.show()
    owner.activateWindow()
    other.setFocus()
    flush()
    try:
        assert not default.wheel_requires_focus()
        assert custom.wheel_requires_focus()
        assert default.focusPolicy() == qt.Qt.FocusPolicy.WheelFocus
        assert custom.focusPolicy() == qt.Qt.FocusPolicy.StrongFocus

        wheel(default)
        assert data.mode == 0
        other.setFocus()
        flush()
        wheel(custom)
        assert data.mode == 0

        custom.set_wheel_requires_focus(False)
        assert not custom.wheel_requires_focus()
        assert custom.focusPolicy() == qt.Qt.FocusPolicy.WheelFocus
        wheel(custom)
        assert data.mode == -2

        custom.set_wheel_requires_focus(True)
        other.setFocus()
        flush()
        wheel(custom, -120)
        assert data.mode == -2
        custom.setFocus()
        flush()
        wheel(custom, -120)
        assert data.mode == 0
    finally:
        owner.deleteLater()
        binding.dispose()
        flush()


def test_combo_wheel_focus_option_rejects_non_bool(qt_application):
    """enum欄のホイール設定へbool以外を受け付けない。"""
    binding = EnumBinding.from_attribute(Data(), "mode", definition=DEFINITION)
    with pytest.raises(TypeError):
        EnumComboBox(binding, wheel_requires_focus=1)
    combo = EnumComboBox(binding)
    try:
        with pytest.raises(TypeError):
            combo.set_wheel_requires_focus(1)
    finally:
        combo.deleteLater()
        binding.dispose()
        flush()


def test_large_python_integers_are_not_narrowed_by_qt(qt_application):
    value = 2**80
    definition = EnumDefinition.from_mapping({0: "Off", value: "Large"})
    data = Data()
    binding = EnumBinding.from_attribute(data, "mode", definition=definition)
    view = EnumComboBox(binding)
    events = []
    binding.changed.connect(events.append)
    try:
        view.setCurrentIndex(1)
        assert data.mode == binding.value == value
        assert events == [value]
        assert view.currentData().value == value
    finally:
        view.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize(
    "mode", ["normalize", "reject", "raise_after", "invalid"]
)
def test_setter_actuals_and_failure_recovery(qt_application, mode):
    class Model:
        _mode = 0

        @property
        def mode(self):
            return self._mode

        @mode.setter
        def mode(self, value):
            if mode == "normalize":
                self._mode = 1  # setterが返した未定義値も実値として保持する。
            elif mode == "raise_after":
                self._mode = 10
                raise ValueError("setter failed")
            elif mode == "invalid":
                self._mode = "invalid"

    data = Model()
    binding = EnumBinding.from_attribute(data, "mode", definition=DEFINITION)
    try:
        if mode in ("raise_after", "invalid"):
            with pytest.raises((ValueError, TypeError)):
                binding.set_value(5)
        else:
            binding.set_value(5)
        if mode == "invalid":
            assert not binding.view_model.set_value_command.can_execute
            data._mode = 5
            binding.refresh()
            assert binding.value == 5
            assert binding.view_model.set_value_command.can_execute
        else:
            assert binding.value == data.mode
    finally:
        binding.dispose()
        flush()


def test_readonly_and_deleted_attributes(qt_application):
    @dataclass(frozen=True, slots=True)
    class Frozen:
        mode: int = 5

    binding = EnumBinding.from_attribute(
        Frozen(), "mode", definition=DEFINITION
    )
    combo = EnumComboBox(binding)
    label = EnumLabel(binding)
    try:
        assert not combo.isEnabled()
        assert label.isEnabled()
        assert label.text() == "Preview"
        assert not binding.set_value(10)
    finally:
        combo.deleteLater()
        label.deleteLater()
        binding.dispose()
        flush()

    class Plain:
        def __init__(self):
            self.mode = 5

    data = Plain()
    binding = EnumBinding.from_attribute(data, "mode", definition=DEFINITION)
    try:
        del data.mode
        binding.refresh()
        assert not binding.view_model.set_value_command.can_execute
        data.mode = 10
        binding.refresh()
        assert binding.value == 10
        assert binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()
        flush()


def test_definition_notifications_publish_consistent_state_and_allow_reentry(
    qt_application,
):
    class Store:
        definition = DEFINITION
        is_available = True
        is_writable = True
        value = 5

        def read(self):
            return self.value

        def write(self, value):
            self.value = value
            return value

    store = Store()
    binding = EnumBinding(store)
    label = EnumLabel(binding)
    values = []
    definitions = []
    binding.changed.connect(values.append)
    binding.definition_changed.connect(
        lambda definition: definitions.append((definition, binding.value))
    )
    try:
        store.definition = EnumDefinition.from_mapping(
            {0: "Off", 5: "Renamed"}
        )
        assert not binding.refresh()
        assert label.text() == "Renamed"
        assert values == []
        assert definitions == [(store.definition, 5)]
        store.definition = EnumDefinition.from_mapping({0: "Off", 10: "Final"})
        store.value = 10
        binding.definition_changed.connect(
            lambda _definition: binding.set_value(0)
        )
        binding.refresh()
        assert binding.value == store.value == 0
        assert values == [0]
        assert label.text() == "Off"
        store.definition = EnumDefinition()
        binding.refresh()
        assert not binding.view_model.set_value_command.can_execute
        assert label.text() == "未定義 (0)"
    finally:
        label.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("dispose_from_signal", [False, True])
def test_shared_owner_and_dispose_during_notification(
    qt_application, dispose_from_signal
):
    owner = qt.QObject()
    binding = EnumBinding.from_attribute(
        Data(), "mode", definition=DEFINITION, parent=owner
    )
    combo = EnumComboBox(binding)
    label = EnumLabel(binding)
    if dispose_from_signal:
        binding.changed.connect(lambda _value: binding.dispose())
        binding.set_value(5)
    else:
        owner.deleteLater()
    flush()
    assert not combo.isEnabled()
    assert not label.isEnabled()
    combo.setCurrentIndex(2)
    combo.deleteLater()
    label.deleteLater()
    if qt.isValid(owner):
        owner.deleteLater()
    flush()


def test_memory_only_view_model_and_same_value_confirmations(qt_application):
    vm = EnumViewModel(5, definition=DEFINITION)
    changed = []
    executed = []
    vm.value.changed.connect(changed.append)
    vm.set_value_command.executed.connect(executed.append)
    assert not vm.set_value_command.execute(5)
    assert vm.set_value_command.execute(-2)
    assert changed == [-2]
    assert executed == [5, -2]
    vm.dispose()
    assert not vm.set_value_command.execute(10)
    vm.deleteLater()
    flush()


def test_reentrant_noop_refresh_does_not_hide_a_value_change(qt_application):
    class Store:
        definition = DEFINITION
        is_available = True
        is_writable = False
        value = 0

        def read(self):
            return self.value

        def write(self, value):
            self.value = value
            return value

    store = Store()
    binding = EnumBinding(store)
    values = []
    binding.changed.connect(values.append)
    binding.view_model.set_value_command.can_execute_changed.connect(
        lambda _enabled: binding.refresh()
    )
    try:
        store.is_writable = True
        store.value = 5
        binding.refresh()
        assert binding.value == 5
        assert values == [5]
    finally:
        binding.dispose()
        flush()


def test_reentrant_definition_only_refresh_keeps_value_notification(
    qt_application,
):
    class Store:
        definition = DEFINITION
        is_available = True
        is_writable = True
        value = 0

        def read(self):
            return self.value

        def write(self, value):
            self.value = value
            return value

    store = Store()
    binding = EnumBinding(store)
    values = []
    binding.changed.connect(values.append)

    def replace_definition(definition):
        if definition.item_for_value(5).name == "First":
            store.definition = EnumDefinition.from_mapping(
                {0: "Off", 5: "Second"}
            )
            binding.refresh()

    binding.definition_changed.connect(replace_definition)
    try:
        store.value = 5
        store.definition = EnumDefinition.from_mapping({0: "Off", 5: "First"})
        binding.refresh()
        assert binding.value == 5
        assert binding.definition.item_for_value(5).name == "Second"
        assert values == [5]
    finally:
        binding.dispose()
        flush()
