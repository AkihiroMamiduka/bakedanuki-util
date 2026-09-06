# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util._sample.maya.ui.bool_sample.shared_bool_views import (
    SharedBoolViewsManager,
    SharedBoolViewsWindow,
)
from bd_util.maya.ui import MayaCallbackRegistry
from bd_util.ui import qt


@dataclass
class SampleSharedData:
    """既定名以外のPython bool attributeを共有するtest用data。"""

    enabled: bool = True


def _process_events(application: qt.QApplication) -> None:
    """Windowの遅延破棄と、Maya callback後の遅延同期を処理する。"""
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None,
        qt.QtCore.QEvent.Type.DeferredDelete,
    )
    application.processEvents()
    application.processEvents()


def _assert_views(window: SharedBoolViewsWindow, value: bool) -> None:
    """1つのWindow内の全5種類のViewが同じ値を表示することを確認する。"""
    widget = window.bool_views_widget
    assert widget.view_model.value.value is value
    assert widget.check_box.isChecked() is value
    assert widget.combo_box.currentData() is value
    assert widget.push_button.isChecked() is value
    assert widget.push_button.text() == ("On" if value else "Off")
    assert widget.radio_button_group.false_button.isChecked() is not value
    assert widget.radio_button_group.true_button.isChecked() is value
    assert widget.status_label.text() == (
        "Status: On" if value else "Status: Off"
    )


def test_shared_sample_syncs_all_views_and_arbitrary_python_data(
    qt_application: qt.QApplication,
    maya_standalone: None,
    capsys: pytest.CaptureFixture[str],
) -> None:
    # 任意のPython objectを正本にして、同じViewModelを2つのWindowへ渡す。
    data = SampleSharedData()
    manager = SharedBoolViewsManager(data, "enabled")
    try:
        window_a, window_b = manager.show()
        widget_a = window_a.bool_views_widget
        widget_b = window_b.bool_views_widget
        assert widget_a.view_model is manager.view_model
        assert widget_b.view_model is manager.view_model
        assert manager.view_model.parent() is not widget_a
        assert manager.view_model.parent() is not widget_b
        assert manager.maya_view is None
        assert manager.show() == (window_a, window_b)

        # 両Windowの各入力Viewから値を変更し、正本と相手Windowへ反映する。
        widget_a.check_box.click()
        assert data.enabled is False
        _assert_views(window_a, False)
        _assert_views(window_b, False)

        widget_b.combo_box.setCurrentIndex(widget_b.combo_box.findData(True))
        assert data.enabled is True
        _assert_views(window_a, True)
        _assert_views(window_b, True)

        widget_a.push_button.click()
        assert data.enabled is False
        _assert_views(window_a, False)
        _assert_views(window_b, False)

        widget_b.radio_button_group.true_button.click()
        assert data.enabled is True
        _assert_views(window_a, True)
        _assert_views(window_b, True)

        # Python Commandからの入力も両Windowへ反映する。
        assert manager.set_value(False)
        _assert_views(window_a, False)
        _assert_views(window_b, False)

        # 出力ボタンは未refreshの正本を読み、表示値との違いも確認できる。
        data.enabled = True
        widget_a.print_value_button.click()
        widget_b.print_value_button.click()
        assert (
            capsys.readouterr().out.count("SampleSharedData.enabled = True")
            == 2
        )
        assert manager.value is False
        assert manager.refresh_from_data()
        _assert_views(window_a, True)
        _assert_views(window_b, True)
    finally:
        manager.dispose()
        _process_events(qt_application)


@pytest.mark.parametrize("closed_name", ["A", "B"])
def test_shared_sample_reopens_windows_with_the_same_view_model(
    qt_application: qt.QApplication,
    maya_standalone: None,
    closed_name: Literal["A", "B"],
) -> None:
    data = SampleSharedData()
    manager = SharedBoolViewsManager(data, "enabled")
    view_model = manager.view_model
    owner = view_model.parent()
    assert owner is not None
    try:
        window_a, window_b = manager.show()
        closed = window_a if closed_name == "A" else window_b
        survivor = window_b if closed_name == "A" else window_a

        # ×ボタンと同じclose経路で片方を破棄しても、他方は操作を続けられる。
        assert closed.close()
        _process_events(qt_application)
        assert not qt.isValid(closed)
        assert qt.isValid(view_model)
        assert qt.isValid(owner)
        survivor.bool_views_widget.check_box.click()
        assert data.enabled is False
        _assert_views(survivor, False)

        # 閉じたWindowだけを新しく生成し、同じViewModelの現在値を表示する。
        reopened = manager.show_a() if closed_name == "A" else manager.show_b()
        assert reopened is not closed
        assert reopened.bool_views_widget.view_model is view_model
        _assert_views(reopened, False)
        reopened.bool_views_widget.push_button.click()
        _assert_views(survivor, True)

        # 全Windowを閉じた後もPython操作でき、再表示で現在値へ接続し直す。
        survivor.close()
        reopened.close()
        _process_events(qt_application)
        assert manager.window_a is None
        assert manager.window_b is None
        assert not manager.is_disposed
        assert manager.set_value(False)
        window_a, window_b = manager.show()
        assert window_a.bool_views_widget.view_model is view_model
        assert window_b.bool_views_widget.view_model is view_model
        _assert_views(window_a, False)
        _assert_views(window_b, False)
    finally:
        manager.dispose()
        _process_events(qt_application)

    # 明示終了は共有QObjectも破棄し、終了後の操作を明確に拒否する。
    assert manager.is_disposed
    assert not qt.isValid(view_model)
    assert not qt.isValid(owner)
    assert not qt.isValid(window_a)
    assert not qt.isValid(window_b)
    manager.dispose()
    with pytest.raises(RuntimeError, match="終了しています"):
        manager.show()
    with pytest.raises(RuntimeError, match="終了しています"):
        manager.set_value(True)


@pytest.mark.parametrize("attribute_name", ["visibility", "customVisibility"])
def test_shared_sample_keeps_one_maya_binding_until_dispose(
    qt_application: qt.QApplication,
    maya_standalone: None,
    attribute_name: str,
) -> None:
    # 標準attributeと追加bool attributeの両方で同じ共有構成を確認する。
    cmds.file(new=True, force=True)
    node_name = cmds.createNode("transform", name="sharedBoolSampleTest")
    if attribute_name != "visibility":
        cmds.addAttr(node_name, longName=attribute_name, attributeType="bool")
    plug_name = f"{node_name}.{attribute_name}"
    data = SampleSharedData(False)
    manager = SharedBoolViewsManager(
        data,
        "enabled",
        maya_node_name=node_name,
        maya_attribute_name=attribute_name,
    )
    try:
        view_model = manager.view_model
        maya_view = manager.maya_view
        assert maya_view is not None
        owner = view_model.parent()
        assert owner is not None
        assert maya_view.parent() is owner
        registries = [
            child
            for child in owner.children()
            if isinstance(child, MayaCallbackRegistry)
        ]
        assert len(registries) == 1
        registry = registries[0]
        callback_ids = registry.callback_ids
        assert callback_ids
        assert bool(cmds.getAttr(plug_name)) is False

        # Qt入力からMayaへ、Maya外部変更から両Windowへ同期する。
        window_a, window_b = manager.show()
        window_a.bool_views_widget.check_box.click()
        assert bool(cmds.getAttr(plug_name)) is True
        _assert_views(window_b, True)
        cmds.setAttr(plug_name, False)
        _process_events(qt_application)
        assert data.enabled is False
        _assert_views(window_a, False)
        _assert_views(window_b, False)

        # 片方を閉じても、残ったWindowとMayaの双方向同期を続ける。
        window_a.close()
        _process_events(qt_application)
        assert manager.window_a is None
        assert registry.callback_ids == callback_ids
        window_b.bool_views_widget.push_button.click()
        assert data.enabled is True
        assert bool(cmds.getAttr(plug_name)) is True
        cmds.setAttr(plug_name, False)
        _process_events(qt_application)
        assert data.enabled is False
        _assert_views(window_b, False)

        # Windowが1つもなくてもMaya入力を正本へ取り込む。
        window_b.close()
        _process_events(qt_application)
        assert manager.window_a is None
        assert manager.window_b is None
        assert registry.callback_ids == callback_ids
        cmds.setAttr(plug_name, True)
        _process_events(qt_application)
        assert data.enabled is True
        assert manager.value is True

        # 再表示ではViewModelもMaya callbackも追加生成しない。
        window_a, window_b = manager.show()
        assert manager.view_model is view_model
        assert manager.maya_view is maya_view
        assert registry.callback_ids == callback_ids
        _assert_views(window_a, True)
        _assert_views(window_b, True)

        # 遅延同期が保留中でも、disposeはMaya callbackを即座に解除する。
        cmds.setAttr(plug_name, False)
        manager.dispose()
        assert registry.callback_ids == ()
        assert maya_view.is_disposed
        assert manager.window_a is None
        assert manager.window_b is None
        _process_events(qt_application)
        assert data.enabled is True
        assert not qt.isValid(view_model)
        assert not qt.isValid(maya_view)
        assert not qt.isValid(window_a)
        assert not qt.isValid(window_b)

        # 終了後の外部変更は同期せず、指定node自体は削除しない。
        data.enabled = False
        cmds.setAttr(plug_name, True)
        _process_events(qt_application)
        assert data.enabled is False
        assert cmds.objExists(node_name)
    finally:
        manager.dispose()
        _process_events(qt_application)
        cmds.file(new=True, force=True)


def test_shared_sample_releases_callbacks_after_failed_initial_sync(
    qt_application: qt.QApplication,
    maya_standalone: None,
) -> None:
    # 初期値を反映できないlocked plugで、生成失敗時のcallback解除を確認する。
    cmds.file(new=True, force=True)
    node_name = cmds.createNode("transform", name="lockedSharedBoolSampleTest")
    cmds.setAttr(f"{node_name}.visibility", lock=True)
    selection = om.MSelectionList()
    selection.add(node_name)
    node = selection.getDependNode(0)
    callback_ids = tuple(om.MMessage.nodeCallbacks(node))
    try:
        with pytest.raises(RuntimeError, match="書き込めません"):
            SharedBoolViewsManager(
                SampleSharedData(False),
                "enabled",
                maya_node_name=node_name,
                maya_attribute_name="visibility",
            )
        assert tuple(om.MMessage.nodeCallbacks(node)) == callback_ids
        _process_events(qt_application)
        assert tuple(om.MMessage.nodeCallbacks(node)) == callback_ids
    finally:
        cmds.file(new=True, force=True)


def test_shared_sample_requires_maya_names_as_pair(
    qt_application: qt.QApplication,
) -> None:
    # 任意のMaya同期先はnode名とattribute名を組で受け付ける。
    with pytest.raises(ValueError, match="両方指定"):
        SharedBoolViewsManager(
            SampleSharedData(), "enabled", maya_node_name="node"
        )
    with pytest.raises(ValueError, match="両方指定"):
        SharedBoolViewsManager(
            SampleSharedData(), "enabled", maya_attribute_name="visibility"
        )
