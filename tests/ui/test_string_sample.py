# coding: utf-8
from maya import cmds

from bd_util._sample.maya.ui.string_sample import maya_plug
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import StringLineEdit, qt


def flush() -> None:
    """Windowとcallbackの遅延終了を処理する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


def test_joint_sample_shares_line_edits_and_releases_callbacks(
    qt_application, maya_standalone
):
    """既存jointのotherTypeを共有Viewで編集して終了できる。"""
    joint = cmds.createNode("joint")
    cmds.setAttr(joint + ".otherType", "elbow", type="string")
    window = maya_plug.show(joint)
    try:
        assert isinstance(window.line_edit, StringLineEdit)
        assert window.line_edit.text() == "elbow"
        assert window.linked_line_edit.text() == "elbow"
        window.binding.set_value("wrist")
        assert window.label.text() == "wrist"
        assert window.linked_line_edit.text() == "wrist"
        assert cmds.getAttr(joint + ".otherType") == "wrist"
        registries = window.findChildren(MayaCallbackRegistry)
        assert len(registries) == 1
        window.close()
        flush()
        assert all(registry.callback_ids == () for registry in registries)
    finally:
        maya_plug.dispose()
        cmds.delete(joint)
        flush()
