# coding: utf-8
from maya import cmds

from bd_util._sample.maya.ui.int_sample import minimal
from bd_util._sample.maya.ui.int_sample.data import IntSampleData
from bd_util.ui import qt


def flush():
    """Qtの遅延破棄を処理する。"""
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def test_minimal_sample_edits_refreshes_and_reopens_without_scene_changes(
    qt_application, maya_standalone
):
    """複数View、入力制限、外部変更、再表示とシーン非変更を確認する。"""
    nodes_before = cmds.ls(long=True)
    minimal.dispose()
    window = minimal.show()
    widget = window.widget
    try:
        assert minimal.show() is window
        assert widget.signed_binding.store.instance == IntSampleData()
        assert widget.spin_box.value() == widget.linked_spin_box.value() == 42
        assert widget.value_label.text() == "42"
        assert widget.limited_spin_box.value() == 128
        assert (
            widget.limited_spin_box.minimum(),
            widget.limited_spin_box.maximum(),
        ) == (
            0,
            255,
        )

        widget.spin_box.setValue(17)
        assert widget.signed_binding.value == 17
        assert widget.linked_spin_box.value() == 17
        assert widget.value_label.text() == "17"
        widget.linked_spin_box.stepBy(1)
        assert widget.signed_binding.value == 27
        widget.input_check_box.click()
        assert not widget.spin_box.isEnabled()
        widget.spin_box.setValue(99)
        assert widget.spin_box.value() == widget.linked_spin_box.value() == 27

        widget.minimum_button.click()
        assert widget.signed_binding.value == -(2**31)
        assert widget.value_label.text() == str(-(2**31))
        widget.maximum_button.click()
        assert widget.signed_binding.value == 2**31 - 1
        assert widget.value_label.text() == str(2**31 - 1)
        widget.limited_spin_box.setValue(255)
        assert widget.limited_binding.value == 255
        assert widget.limited_label.text() == "255"

        widget.set_data_button.click()
        data = widget.signed_binding.store.instance
        assert data.signed_value == -123456789
        assert data.limited_value == 200
        assert widget.signed_binding.value == 2**31 - 1
        assert widget.limited_binding.value == 255
        widget.refresh_button.click()
        assert widget.signed_binding.value == -123456789
        assert widget.linked_spin_box.value() == -123456789
        assert widget.limited_spin_box.value() == 200
        assert widget.limited_label.text() == "200"
        assert cmds.ls(long=True) == nodes_before

        window.close()
        flush()
        assert not qt.isValid(window)
        reopened = minimal.show()
        assert reopened is not window
        assert reopened.widget.signed_binding.value == 42
        assert reopened.widget.limited_binding.value == 128
    finally:
        minimal.dispose()
        flush()
