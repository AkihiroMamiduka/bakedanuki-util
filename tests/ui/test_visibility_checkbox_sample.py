# coding: utf-8
from __future__ import annotations

from maya import cmds, standalone

from bd_util._sample.maya.ui.visibility_checkbox import (
    VisibilityCheckBoxWindow,
)
from bd_util.ui import qt


def test_visibility_checkbox_sample_uses_dataclass_store(
    qt_application: qt.QApplication,
    capsys,
) -> None:
    # QApplicationを先に生成してからMaya standaloneを初期化する。
    initialized_here = False
    try:
        standalone.initialize(name="python")
        initialized_here = True
    except RuntimeError:
        pass
    cmds.file(new=True, force=True)

    # 配布sampleの実行経路でもUI、dataclass、Maya plugを同期する。
    node_name = cmds.createNode("transform", name="sampleViewTest")
    window = VisibilityCheckBoxWindow(node_name)
    try:
        assert window.data.visible_by_default is True
        assert window.visibility_checkbox.isChecked()

        window.visibility_checkbox.click()
        assert window.data.visible_by_default is False
        assert not cmds.getAttr(f"{node_name}.visibility")

        assert window.set_visibility(True)
        assert window.data.visible_by_default is True
        assert cmds.getAttr(f"{node_name}.visibility")

        window.print_value_button.click()
        assert (
            "VisibilityData.visible_by_default = True"
            in capsys.readouterr().out
        )
    finally:
        window.deleteLater()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            window,
            qt.QtCore.QEvent.Type.DeferredDelete,
        )
        qt_application.processEvents()
        cmds.file(new=True, force=True)
        if initialized_here:
            standalone.uninitialize()
