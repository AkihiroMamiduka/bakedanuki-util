# coding: utf-8
"""整数複合ViewのMaya Undo、設定復元とサンプルの終了を検証する。"""

from dataclasses import dataclass

import pytest
from maya import cmds

from bd_util.maya.ui import (
    MayaIntBinding,
    MayaIntPlugBinding,
    resolve_int_plug,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util.ui import IntRangeSliderSpinBox, SettingsPath, UiStateManager, qt
from bd_util._sample.maya.ui.int_sample import range_slider as sample


@dataclass
class Data:
    """Mayaと同期するPython整数正本。"""

    value: int = 10


def flush():
    """callbackと遅延破棄を完了する。"""
    for _ in range(3):
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        qt.QApplication.processEvents()


@pytest.fixture
def scene(qt_application, maya_standalone):
    """独立したscene・Window所有者を作る。"""
    cmds.file(new=True, force=True)
    undo = cmds.undoInfo(query=True, state=True)
    auto = cmds.autoKeyframe(query=True, state=True)
    cmds.undoInfo(state=True)
    cmds.autoKeyframe(state=False)
    owner = qt.QWidget()
    node = cmds.createNode("transform")
    for attribute in ("byte", "short", "long"):
        cmds.addAttr(
            node, longName=attribute + "Value", attributeType=attribute
        )
        cmds.setAttr(node + "." + attribute + "Value", 10)
    yield owner, node
    sample.dispose()
    owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None
    cmds.autoKeyframe(state=auto)
    cmds.undoInfo(state=undo)


@pytest.mark.parametrize("source", ["maya", "python"])
@pytest.mark.parametrize("attribute", ["byteValue", "shortValue", "longValue"])
def test_settings_do_not_write_maya_and_drag_or_value_has_separate_undo(
    scene, tmp_path, source, attribute
):
    """設定編集・保存・復元は履歴を増やさず、範囲変更は操作を確定終了する。"""
    owner, node = scene
    path = node + "." + attribute
    plug = resolve_int_plug(node, attribute)
    binding = (
        MayaIntPlugBinding(plug, parent=owner)
        if source == "maya"
        else MayaIntBinding.from_attribute(
            Data(), "value", maya_plug=plug, parent=owner
        )
    )
    editor = IntRangeSliderSpinBox(
        binding,
        owner,
        minimum=0,
        maximum=100,
        step_mode="multiplicative",
    )
    settings = qt.QtCore.QSettings(
        str(tmp_path / "view.ini"), qt.QtCore.QSettings.Format.IniFormat
    )
    manager = UiStateManager(settings, SettingsPath("sample/editor/main"))
    manager.register_int_range_slider_spin_box("value", editor)
    cmds.flushUndo()
    editor.setIntRange(-20, 100)
    editor.step_spin_box.stepUp()
    assert editor.singleStep() == 10
    assert manager.save()
    editor.setIntRange(0, 10)
    editor.setSingleStep(1)
    assert manager.restore() == frozenset({"value"})
    assert editor.intRange() == (-20, 100)
    assert editor.singleStep() == 10
    assert binding.value == cmds.getAttr(path) == 10
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    editor.slider.setSliderDown(True)
    editor.slider.setValue(editor.slider.maximum())
    assert binding.value == cmds.getAttr(path) == 100
    editor.setIntRange(0, 50)
    assert not binding.view_model.is_editing
    assert FloatEditUndo._active is None
    assert editor.spin_box.value() == 100
    assert editor.slider.value() == editor.slider.maximum()
    cmds.undo()
    flush()
    assert binding.value == cmds.getAttr(path) == 10
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert editor.intRange() == (0, 50)
    assert editor.singleStep() == 10
    editor.spin_box.stepUp()
    assert binding.value == cmds.getAttr(path) == 20
    cmds.undo()
    flush()
    assert binding.value == 10


@pytest.mark.parametrize("source", ["maya", "python"])
def test_restore_ends_gesture_without_value_write_and_survives_readonly(
    scene, tmp_path, source
):
    """操作中の設定復元でUndoを閉じ、ロック中もView設定だけは編集できる。"""
    owner, node = scene
    path = node + ".longValue"
    plug = resolve_int_plug(node, "longValue")
    binding = (
        MayaIntPlugBinding(plug, parent=owner)
        if source == "maya"
        else MayaIntBinding.from_attribute(
            Data(), "value", maya_plug=plug, parent=owner
        )
    )
    editor = IntRangeSliderSpinBox(binding, owner, minimum=0, maximum=100)
    settings = qt.QtCore.QSettings(
        str(tmp_path / "view.ini"), qt.QtCore.QSettings.Format.IniFormat
    )
    manager = UiStateManager(settings, SettingsPath("sample/editor/main"))
    manager.register_int_range_slider_spin_box("value", editor)
    assert manager.save()
    editor.setIntRange(0, 200)
    cmds.flushUndo()
    editor.slider.setSliderDown(True)
    editor.slider.setValue(80)
    assert binding.value == 80
    assert manager.restore() == frozenset({"value"})
    assert not binding.view_model.is_editing
    assert binding.value == 80
    cmds.undo()
    flush()
    assert binding.value == 10
    cmds.setAttr(path, lock=True)
    flush()
    editor.setIntRange(-100, 100)
    editor.step_spin_box.setValue(15)
    assert editor.singleStep() == 15
    assert editor.minimum_spin_box.isEnabled()
    assert editor.step_spin_box.isEnabled()
    assert binding.value == cmds.getAttr(path) == 10


def test_sample_reopen_preserves_each_view_setting_and_releases_callbacks(
    scene, tmp_path, monkeypatch
):
    """サンプルの再表示で操作設定だけを復元し、再生成した正本は初期値を保つ。"""
    settings = qt.QtCore.QSettings(
        str(tmp_path / "sample.ini"), qt.QtCore.QSettings.Format.IniFormat
    )

    def create_manager(path):
        """利用者の設定へ書き込まず、テスト専用設定を渡す。"""
        return UiStateManager(settings, SettingsPath(path))

    monkeypatch.setattr(sample, "create_ui_state_manager", create_manager)
    window = sample.show_demo()
    flush()
    nodes = window.node_names
    assert nodes is not None
    window.python_editor.setIntRange(-(2**31), 2**31 - 1)
    window.python_editor.setSingleStep(15)
    window.linked_editor.setIntRange(-5, 5)
    window.linked_editor.setSingleStep(100)
    window.editors["maya"].slider.setSliderDown(True)
    window.editors["maya"].slider.setValue(80)
    sample.dispose()
    flush()
    assert FloatEditUndo._active is None
    reopened = sample.show_maya(*nodes)
    flush()
    assert reopened.python_editor.intRange() == (-(2**31), 2**31 - 1)
    assert reopened.python_editor.singleStep() == 15
    assert reopened.linked_editor.intRange() == (-5, 5)
    assert reopened.linked_editor.singleStep() == 100
    assert reopened.python_binding.value == 42
    assert reopened.simple_editor.spin_box.value() == 42
    assert reopened.sync_binding.value == 42
    reopened.reset_settings()
    assert reopened.python_editor.intRange() == (0, 100)
    assert reopened.linked_editor.intRange() == (-10, 10)
    assert reopened.python_editor.singleStep() == 1
    assert reopened.python_binding.value == 42
    sample.dispose()
    flush()


def test_sample_python_only_does_not_create_nodes(
    scene, tmp_path, monkeypatch
):
    """Python版はsceneへノードを追加せず表示する。"""
    settings = qt.QtCore.QSettings(
        str(tmp_path / "sample.ini"), qt.QtCore.QSettings.Format.IniFormat
    )

    def create_manager(path):
        """サンプルの保存先を一時ファイルへ差し替える。"""
        return UiStateManager(settings, SettingsPath(path))

    monkeypatch.setattr(sample, "create_ui_state_manager", create_manager)
    before = tuple(cmds.ls())
    window = sample.show()
    flush()
    assert tuple(cmds.ls()) == before
    assert window.maya_binding is None
    assert window.sync_binding is None
    assert window.editor_settings.registered_keys == ("python", "linked")
