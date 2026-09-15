# coding: utf-8
"""複数属性Bindingが既存の入力Viewから使用できることを検証する。"""

import pytest
from maya import cmds

from bd_util.maya.ui import (
    MayaBoolPlugsBinding,
    MayaFloatPlugsBinding,
    resolve_bool_plug,
    resolve_float_plug,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import BoolComboBox, FloatSliderSpinBox, qt


def flush():
    """Qtイベントと削除予約を処理する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


@pytest.fixture
def scene(qt_application, maya_standalone):
    """実Viewの親と二つのtransformを用意する。"""
    cmds.file(new=True, force=True)
    owner = qt.QWidget()
    nodes = [cmds.createNode("transform") for _ in range(2)]
    yield nodes, owner
    if qt.isValid(owner):
        owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None


def test_bool_existing_combo_uses_group_command(scene):
    """既存のoff/on入力を一回のUndoで全対象へ適用する。"""
    nodes, owner = scene
    cmds.setAttr(f"{nodes[1]}.visibility", False)
    cmds.flushUndo()
    binding = MayaBoolPlugsBinding(
        [resolve_bool_plug(node, "visibility") for node in nodes], parent=owner
    )
    editor = BoolComboBox(
        binding, false_text="off", true_text="on", parent=owner
    )
    assert binding.is_mixed
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    editor.setCurrentIndex(0)
    assert [cmds.getAttr(f"{node}.visibility") for node in nodes] == [
        False,
        False,
    ]
    cmds.undo()
    flush()
    assert binding.is_mixed
    assert binding.value is True
    binding.dispose()


def test_float_existing_slider_shares_drag_and_owner_releases_callbacks(scene):
    """既存の複合Viewで一括ドラッグし、親破棄だけでも監視を解放する。"""
    nodes, owner = scene
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(node, "scaleX") for node in nodes], parent=owner
    )
    editor = FloatSliderSpinBox(binding, owner, minimum=0, maximum=10)
    registries = binding.findChildren(MayaCallbackRegistry)
    cmds.flushUndo()
    editor.slider.setSliderDown(True)
    editor.slider.setValue(200)
    editor.slider.setValue(400)
    assert [cmds.getAttr(f"{node}.scaleX") for node in nodes] == [4, 4]
    editor.slider.setSliderDown(False)
    cmds.undo()
    flush()
    assert [cmds.getAttr(f"{node}.scaleX") for node in nodes] == [1, 1]
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    editor.slider.setSliderDown(True)
    editor.slider.setValue(500)
    owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None
    assert all(registry.is_disposed for registry in registries)
