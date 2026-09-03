# coding: utf-8
from __future__ import annotations

from maya import cmds, standalone

from bd_util._sample.maya.ui.bool_views import BoolViewsWindow
from bd_util.ui import qt


def _assert_value(
    window: BoolViewsWindow,
    node_name: str,
    value: bool,
) -> None:
    """sample内の正本、全View、Maya plugが同じ値か確認する。"""
    assert window.data.visible_by_default is value
    assert window.check_box.isChecked() is value
    assert window.combo_box.currentData() is value
    assert window.push_button.isChecked() is value
    assert window.push_button.text() == ("On" if value else "Off")
    assert window.radio_button_group.false_button.isChecked() is not value
    assert window.radio_button_group.true_button.isChecked() is value
    assert window.status_label.text() == (
        "Status: On" if value else "Status: Off"
    )
    assert bool(cmds.getAttr(f"{node_name}.visibility")) is value


def test_bool_views_sample_uses_dataclass_store(
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

    # 配布sampleの全View、dataclass、Maya plugを同期する。
    node_name = cmds.createNode("transform", name="sampleViewTest")
    window = BoolViewsWindow(node_name)
    try:
        _assert_value(window, node_name, True)

        window.check_box.click()
        _assert_value(window, node_name, False)

        window.combo_box.setCurrentIndex(window.combo_box.findData(True))
        _assert_value(window, node_name, True)

        window.push_button.click()
        _assert_value(window, node_name, False)

        window.radio_button_group.true_button.click()
        _assert_value(window, node_name, True)

        assert window.set_value(False)
        _assert_value(window, node_name, False)

        # Mayaからの外部入力も遅延callback後に全Viewと正本へ反映する。
        cmds.setAttr(f"{node_name}.visibility", True)
        qt_application.processEvents()
        qt_application.processEvents()
        _assert_value(window, node_name, True)

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
