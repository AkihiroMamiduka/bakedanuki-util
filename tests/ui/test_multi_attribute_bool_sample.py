# coding: utf-8
import pytest

from bd_util._sample.maya.ui.bool_sample import multi_attribute
from bd_util.ui import qt


def _flush(application):
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QtCore.QEvent.Type.DeferredDelete
    )
    application.processEvents()


@pytest.mark.parametrize(
    "visible, show_labels, allow_editing",
    [
        (True, True, True),
        (False, True, False),
        (True, False, True),
        (False, False, False),
    ],
)
def test_initial_data_controls_preview_and_editing(
    qt_application, visible, show_labels, allow_editing
):
    data = multi_attribute.DisplayOptionsData(
        visible, show_labels, allow_editing
    )
    widget = multi_attribute.DisplayOptionsWidget(data)
    try:
        assert widget.data is data
        assert widget.visible_check_box.isChecked() is visible
        assert widget.labels_check_box.isChecked() is show_labels
        assert widget.editing_check_box.isChecked() is allow_editing
        assert widget.preview_content.isHidden() is not visible
        assert widget.preview_label.isHidden() is not show_labels
        assert widget.options_group.isEnabled() is allow_editing
        assert widget.visible_check_box.isEnabled() is allow_editing
        assert widget.labels_check_box.isEnabled() is allow_editing
        assert widget.editing_check_box.isEnabled()
    finally:
        widget.deleteLater()
        _flush(qt_application)


def test_ui_edits_are_independent_and_disabled_options_preserve_data(
    qt_application,
):
    data = multi_attribute.DisplayOptionsData()
    widget = multi_attribute.DisplayOptionsWidget(data)
    try:
        widget.labels_check_box.click()
        assert data == multi_attribute.DisplayOptionsData(True, False, True)
        assert widget.preview_label.isHidden()
        assert not widget.preview_content.isHidden()
        widget.visible_check_box.click()
        assert data == multi_attribute.DisplayOptionsData(False, False, True)
        assert widget.preview_content.isHidden()

        widget.editing_check_box.click()
        assert data == multi_attribute.DisplayOptionsData(False, False, False)
        widget.visible_check_box.click()
        widget.labels_check_box.click()
        assert data == multi_attribute.DisplayOptionsData(False, False, False)

        # UIの編集禁止中も、Pythonからの変更は表示へ反映する。
        widget.visible_binding.set_value(True)
        widget.labels_binding.set_value(True)
        assert data == multi_attribute.DisplayOptionsData(True, True, False)
        assert not widget.preview_content.isHidden()
        assert not widget.preview_label.isHidden()
        assert not widget.visible_check_box.isEnabled()
        assert not widget.labels_check_box.isEnabled()
        widget.editing_check_box.click()
        assert data == multi_attribute.DisplayOptionsData()
        assert widget.visible_check_box.isEnabled()
        assert widget.labels_check_box.isEnabled()
    finally:
        widget.deleteLater()
        _flush(qt_application)


def test_direct_data_edits_require_refresh_for_all_three_bindings(
    qt_application,
):
    data = multi_attribute.DisplayOptionsData()
    widget = multi_attribute.DisplayOptionsWidget(data)
    try:
        data.visible = False
        data.show_labels = False
        data.allow_editing = False
        assert not widget.preview_content.isHidden()
        assert not widget.preview_label.isHidden()
        assert widget.options_group.isEnabled()
        widget.refresh_from_data()
        assert widget.preview_content.isHidden()
        assert widget.preview_label.isHidden()
        assert not widget.options_group.isEnabled()
        assert not widget.visible_check_box.isChecked()
        assert not widget.labels_check_box.isChecked()
        assert not widget.editing_check_box.isChecked()

        data.visible = True
        data.show_labels = True
        data.allow_editing = True
        widget.refresh_from_data()
        assert not widget.preview_content.isHidden()
        assert not widget.preview_label.isHidden()
        assert widget.options_group.isEnabled()
    finally:
        widget.deleteLater()
        _flush(qt_application)


def test_allow_editing_does_not_override_a_views_command_availability(
    qt_application,
):
    widget = multi_attribute.DisplayOptionsWidget(
        multi_attribute.DisplayOptionsData(allow_editing=False)
    )
    try:
        widget.labels_binding.dispose()
        _flush(qt_application)
        widget.editing_binding.set_value(True)
        assert widget.options_group.isEnabled()
        assert widget.visible_check_box.isEnabled()
        assert not widget.labels_check_box.isEnabled()
    finally:
        widget.deleteLater()
        _flush(qt_application)


def test_window_close_disposes_all_bindings_and_reopens_with_new_data(
    qt_application, maya_standalone
):
    try:
        first = multi_attribute.show()
        assert multi_attribute.show() is first
        widget = first.widget
        data = widget.data
        bindings = (
            widget.visible_binding,
            widget.labels_binding,
            widget.editing_binding,
        )
        assert all(binding.parent() is widget for binding in bindings)
        widget.labels_check_box.click()
        assert not data.show_labels
        assert first.close()
        _flush(qt_application)
        assert all(binding.is_disposed for binding in bindings)
        assert not qt.isValid(widget)
        assert not data.show_labels
        second = multi_attribute.show()
        assert second is not first
        assert second.widget.data is not data
        assert second.widget.data == multi_attribute.DisplayOptionsData()
        assert not second.widget.preview_label.isHidden()
    finally:
        multi_attribute.dispose()
        _flush(qt_application)
