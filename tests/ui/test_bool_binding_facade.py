# coding: utf-8
from dataclasses import dataclass

import pytest

from bd_util._sample.maya.ui.bool_sample import minimal
from bd_util.ui import BoolBinding, BoolCheckBox, qt


@dataclass
class _Data:
    enabled: bool = True


def _flush(application: qt.QApplication) -> None:
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QtCore.QEvent.Type.DeferredDelete
    )
    application.processEvents()


def test_attribute_binding_shares_views_and_refreshes_data(qt_application):
    data = _Data()
    binding = BoolBinding.from_attribute(data, "enabled")
    first = BoolCheckBox(binding.view_model)
    second = BoolCheckBox(binding.view_model)
    try:
        assert binding.store.instance is data
        assert binding.view_model.store is binding.store
        first.click()
        assert data.enabled is False
        assert second.isChecked() is False
        first.deleteLater()
        _flush(qt_application)
        assert not binding.is_disposed
        assert binding.set_value(True)
        assert second.isChecked() is True
        assert not binding.set_value(True)
        data.enabled = False
        assert binding.value is True
        assert binding.refresh()
        assert not second.isChecked()
    finally:
        binding.dispose()
        if qt.isValid(first):
            first.deleteLater()
        second.deleteLater()
        _flush(qt_application)


@pytest.mark.parametrize("during_change", [False, True])
def test_dispose_stops_retained_view_model_before_deferred_delete(
    qt_application, during_change
):
    data = _Data()
    binding = BoolBinding.from_attribute(data, "enabled")
    view_model = binding.view_model
    view = BoolCheckBox(view_model)
    if during_change:
        view_model.value.changed.connect(binding.dispose)
        binding.set_value(False)
    else:
        binding.dispose()
    stopped_value = data.enabled
    assert binding.is_disposed
    assert view_model.is_disposed
    assert not view_model.set_value_command.can_execute
    assert not view_model.set_value_command.execute(not stopped_value)
    assert not view_model.refresh_from_store(binding.store)
    assert not view.isEnabled()
    assert data.enabled is stopped_value
    with pytest.raises(RuntimeError, match="終了しています"):
        binding.set_value(True)
    with pytest.raises(RuntimeError, match="終了しています"):
        binding.refresh()
    binding.dispose()
    _flush(qt_application)
    assert not qt.isValid(view_model)
    view.deleteLater()
    _flush(qt_application)


def test_parent_destruction_ends_binding_and_disables_surviving_view(
    qt_application,
):
    owner = qt.QObject()
    binding = BoolBinding.from_attribute(_Data(), "enabled", parent=owner)
    view = BoolCheckBox(binding.view_model)
    owner.deleteLater()
    _flush(qt_application)
    assert binding.is_disposed
    assert not view.isEnabled()
    binding.dispose()
    view.deleteLater()
    _flush(qt_application)


def test_constructor_failure_releases_owned_qobjects(qt_application):
    class UnreadableStore:
        is_available = True
        is_writable = True

        def read(self) -> bool:
            raise ValueError("cannot read")

        def write(self, value: bool) -> bool:
            raise AssertionError("must not write")

    owner = qt.QObject()
    with pytest.raises(ValueError, match="cannot read"):
        BoolBinding(UnreadableStore(), parent=owner)
    _flush(qt_application)
    assert not owner.children()
    owner.deleteLater()
    _flush(qt_application)


def test_binding_preserves_store_normalization_and_read_only_state(
    qt_application,
):
    class NormalizingData:
        @property
        def enabled(self) -> bool:
            return True

        @enabled.setter
        def enabled(self, value: bool) -> None:
            return

    @dataclass(frozen=True)
    class ReadOnlyData:
        enabled: bool = True

    for data in (NormalizingData(), ReadOnlyData()):
        binding = BoolBinding.from_attribute(data, "enabled")
        assert not binding.set_value(False)
        assert binding.value is True
        binding.dispose()
    _flush(qt_application)


def test_minimal_sample_uses_public_binding_and_reopens(
    qt_application, maya_standalone
):
    try:
        first = minimal.show()
        assert minimal.show() is first
        binding = first.widget.binding
        first.widget.check_box.click()
        assert not binding.store.instance.visible_by_default
        assert first.close()
        _flush(qt_application)
        assert binding.is_disposed
        second = minimal.show()
        assert second is not first
        assert second.widget.binding.value
    finally:
        minimal.dispose()
        _flush(qt_application)
