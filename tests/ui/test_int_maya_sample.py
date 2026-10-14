# coding: utf-8
from maya import cmds

from bd_util._sample.maya.ui.int_sample import maya_plug
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import qt


def flush():
    """Maya callbackとQtの遅延破棄を処理する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


def test_maya_int_sample_edits_and_disposes_callbacks(
    qt_application, maya_standalone
):
    """デモノードで各型の編集、混在解除とcallback解放を確認する。"""
    maya_plug.dispose()
    window = maya_plug.show_demo()
    first, second = window.node_names
    widget = window.widget
    registries = window.findChildren(MayaCallbackRegistry)
    try:
        assert len(registries) == 3
        assert widget.byte_spin_box.value() == 128
        assert (
            widget.byte_spin_box.minimum(),
            widget.byte_spin_box.maximum(),
        ) == (
            0,
            255,
        )
        assert widget.short_spin_box.value() == 5
        assert (
            widget.short_spin_box.minimum(),
            widget.short_spin_box.maximum(),
        ) == (
            -20,
            20,
        )
        assert widget.long_spin_box.value() == 3
        assert widget.long_binding.is_mixed
        widget.align_button.click()
        assert cmds.getAttr(second + ".longValue") == 3
        assert not widget.long_binding.is_mixed
        widget.byte_spin_box.setValue(255)
        assert cmds.getAttr(first + ".byteValue") == 255
        assert widget.byte_label.text() == "255"
        widget.short_spin_box.setValue(-20)
        assert cmds.getAttr(first + ".shortValue") == -20
        widget.long_spin_box.setValue(2147483647)
        assert cmds.getAttr(first + ".longValue") == 2147483647
        assert cmds.getAttr(second + ".longValue") == 2147483647

        cmds.setAttr(first + ".byteValue", 200)
        flush()
        widget.refresh_button.click()
        assert widget.byte_spin_box.value() == 200
        window.close()
        flush()
        assert all(registry.callback_ids == () for registry in registries)
        assert not qt.isValid(window)
        assert cmds.objExists(first) and cmds.objExists(second)
    finally:
        maya_plug.dispose()
        cmds.delete(first, second)
        flush()
