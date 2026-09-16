# coding: utf-8
from maya import cmds

from bd_util._sample.maya.ui.enum_sample import minimal, maya_plug, maya_view
from bd_util._sample.maya.ui.enum_sample.data import EnumData
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import qt


def flush():
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


def test_minimal_sample_shares_views_and_reopens(
    qt_application, maya_standalone
):
    minimal.dispose()
    window = minimal.show()
    try:
        assert minimal.show() is window
        window.combo_box.setCurrentIndex(3)
        assert window.data.mode == 10
        assert window.linked_combo_box.currentIndex() == 3
        assert window.label.text() == "Final"
        window.data.mode = 1
        window.refresh_button.click()
        assert window.label.text() == "未定義 (1)"
        assert window.value_label.text() == "1"
        window.close()
        flush()
        assert not qt.isValid(window)
        reopened = minimal.show()
        assert reopened.data.mode == 5
    finally:
        minimal.dispose()
        flush()


def test_maya_samples_share_views_and_release_callbacks(
    qt_application, maya_standalone
):
    node = cmds.createNode("transform")
    data = EnumData(5)
    try:
        cmds.setAttr(node + ".rotateOrder", 2)
        window = maya_plug.show(node)
        assert window.binding.value == 2
        window.combo_box.setCurrentIndex(3)
        assert cmds.getAttr(node + ".rotateOrder") == 3
        assert window.label.text() == "xzy"
        maya_plug.dispose()
        flush()
        window = maya_view.show(node, data=data)
        assert cmds.getAttr(node + ".rotateOrder") == 5
        registries = window.findChildren(MayaCallbackRegistry)
        assert len(registries) == 1
        cmds.setAttr(node + ".rotateOrder", 1)
        flush()
        assert data.mode == window.binding.value == 1
        assert (
            window.combo_box.currentIndex()
            == window.linked_combo_box.currentIndex()
            == 1
        )
        assert window.label.text() == "yzx"
        window.close()
        flush()
        assert all(registry.callback_ids == () for registry in registries)
        cmds.setAttr(node + ".rotateOrder", 0)
        flush()
        assert data.mode == 1
    finally:
        maya_plug.dispose()
        maya_view.dispose()
        cmds.delete(node)
        flush()
