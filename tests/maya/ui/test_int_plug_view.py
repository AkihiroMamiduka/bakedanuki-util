# coding: utf-8
"""Python正本とMaya整数Viewの同期、失敗復旧と履歴を検証する。"""

from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import (
    MayaCallbackRegistry,
    MayaIntBinding,
    MayaIntPlugBinding,
    MayaIntPlugView,
    MayaIntPlugsBinding,
    resolve_int_plug,
)
from bd_util.maya.ui.callback import dispose_owned_callbacks
from bd_util.ui import IntBinding, IntPresentation, IntViewModel, qt


@dataclass
class Data:
    """正本として使う符号付き32-bit整数属性。"""

    value: int = 1


def flush():
    """Maya通知後の遅延同期とQt破棄を実行する。"""
    for _ in range(3):
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        qt.QApplication.processEvents()


@pytest.fixture(params=["byte", "short", "long"])
def scene(new_scene, request):
    """三種類の整数属性とcallback所有者を作る。"""
    cmds.undoInfo(state=True)
    node = cmds.createNode("transform")
    cmds.addAttr(
        node, longName="count", attributeType=request.param, keyable=True
    )
    owner = qt.QObject()
    yield node, resolve_int_plug(node, "count"), owner, request.param
    owner.deleteLater()
    flush()


def test_python_initial_command_direct_assignment_and_maya_input(scene):
    """Python初期値、Command、明示refresh、Maya外部入力を同期する。"""
    node, plug, owner, _ = scene
    cmds.setAttr(node + ".count", 10)
    data = Data(128)
    binding = MayaIntBinding.from_attribute(
        data, "value", maya_plug=plug, parent=owner
    )
    assert binding.value == data.value == cmds.getAttr(node + ".count") == 128
    assert binding.maya_view.plug_operator is plug
    assert binding.set_value(200)
    data.value = 15
    assert binding.value == cmds.getAttr(node + ".count") == 200
    binding.refresh()
    assert cmds.getAttr(node + ".count") == 15
    cmds.setAttr(node + ".count", 25)
    assert data.value == 15
    assert not binding.maya_view.is_synchronized
    flush()
    assert binding.value == data.value == 25
    assert type(binding.value) is int
    assert binding.maya_view.is_synchronized


@pytest.mark.parametrize("confirmation", ["command", "refresh"])
def test_later_same_python_confirmation_wins_pending_maya_input(
    scene, confirmation
):
    """同値のPython確定通知も先行する未処理Maya入力より優先する。"""
    node, plug, owner, _ = scene
    binding = MayaIntBinding.from_attribute(
        Data(), "value", maya_plug=plug, parent=owner
    )
    cmds.setAttr(node + ".count", 20)
    assert not (
        binding.set_value(1)
        if confirmation == "command"
        else binding.refresh()
    )
    flush()
    assert binding.value == cmds.getAttr(node + ".count") == 1
    assert binding.maya_view.is_synchronized


def test_exact_type_limits_no_clamp_and_recovery(scene):
    """型範囲超過でPython値を切り詰めず、正常値への復帰と端点を確認する。"""
    node, plug, owner, kind = scene
    limits = {
        "byte": (0, 255),
        "short": (-(2**15), 2**15 - 1),
        "long": (-(2**31), 2**31 - 1),
    }
    lower, upper = limits[kind]
    data = Data()
    binding = MayaIntBinding.from_attribute(
        data, "value", maya_plug=plug, parent=owner
    )
    errors = []
    binding.maya_view.sync_failed.connect(errors.append)
    for value in (lower, upper):
        binding.set_value(value)
        assert binding.value == cmds.getAttr(node + ".count") == value
        assert binding.maya_view.is_synchronized
    if kind != "long":
        binding.set_value(upper + 1)
        assert data.value == upper + 1
        assert cmds.getAttr(node + ".count") == upper
        assert not binding.maya_view.is_synchronized
        assert isinstance(errors[-1], ValueError)
        assert binding.view_model.set_value_command.can_execute
        with pytest.raises(ValueError):
            binding.maya_view.sync_from_view_model()
    binding.set_value(2)
    assert binding.maya_view.is_synchronized
    assert binding.maya_view.last_sync_error is None
    for invalid in (True, 2.0, 2**31, -(2**31) - 1):
        with pytest.raises((TypeError, ValueError)):
            binding.set_value(invalid)
        assert data.value == 2


def test_hard_limit_is_sync_constraint_and_python_presentation_is_preserved(
    scene,
):
    """Mayaのhard limitをPython側の入力範囲へ混入させない。"""
    node, plug, owner, _ = scene
    cmds.addAttr(node + ".count", edit=True, minValue=0, maxValue=10)
    presentation = IntPresentation(minimum=-100, maximum=100)
    data = Data()
    binding = MayaIntBinding.from_attribute(
        data, "value", maya_plug=plug, presentation=presentation, parent=owner
    )
    assert binding.view_model.presentation == presentation
    assert binding.set_value(20)
    assert data.value == 20
    assert cmds.getAttr(node + ".count") == 1
    assert not binding.maya_view.is_synchronized
    assert binding.set_value(5)
    assert binding.maya_view.is_synchronized


@pytest.mark.parametrize(
    "mode", ["correct", "reject", "before", "after", "invalid"]
)
def test_maya_input_uses_setter_confirmed_value_and_original_exception(
    scene, mode
):
    """setterの補正・拒否・部分更新・不正値を正本の確定結果として扱う。"""
    node, plug, owner, _ = scene

    class Model:
        """setterで入力結果を制御するPython正本。"""

        _value = 1
        error = RuntimeError("setter failed")

        @property
        def value(self):
            """現在の正本値を返す。"""
            return self._value

        @value.setter
        def value(self, value):
            """補正・拒否・例外を切り替える。"""
            if mode == "before":
                raise self.error
            if mode == "reject":
                return
            self._value = value // 10 * 10
            if mode == "invalid":
                self._value = True
            if mode == "after":
                raise self.error

    data = Model()
    binding = MayaIntBinding.from_attribute(
        data, "value", maya_plug=plug, parent=owner
    )
    cmds.setAttr(node + ".count", 37)
    flush()
    expected = 30 if mode in ("correct", "after") else 1
    assert binding.value == expected
    if mode != "invalid":
        assert cmds.getAttr(node + ".count") == expected
    if mode in ("before", "after"):
        assert binding.maya_view.last_sync_error is data.error
    elif mode == "invalid":
        assert not binding.view_model.set_value_command.can_execute
        data._value = 8
        binding.refresh()
        assert binding.maya_view.is_synchronized
    else:
        assert binding.maya_view.is_synchronized


def test_lock_connection_pending_sync_and_newer_maya_input(scene):
    """lock・接続中のPython編集を保持し、解除後に再同期する。"""
    node, plug, owner, kind = scene
    data = Data()
    binding = MayaIntBinding.from_attribute(
        data, "value", maya_plug=plug, parent=owner
    )
    path = node + ".count"
    cmds.setAttr(path, lock=True)
    flush()
    binding.set_value(5)
    assert data.value == 5
    assert binding.view_model.set_value_command.can_execute
    assert not binding.maya_view.is_synchronized
    cmds.setAttr(path, lock=False)
    flush()
    assert cmds.getAttr(path) == 5
    source = cmds.createNode("transform")
    cmds.addAttr(source, longName="count", attributeType=kind)
    cmds.setAttr(source + ".count", 20)
    cmds.connectAttr(source + ".count", path)
    flush()
    assert data.value == 5
    binding.set_value(7)
    assert cmds.getAttr(path) == 20
    cmds.disconnectAttr(source + ".count", path)
    flush()
    assert data.value == cmds.getAttr(path) == 7
    cmds.connectAttr(source + ".count", path)
    cmds.disconnectAttr(source + ".count", path)
    flush()
    assert data.value == 7
    cmds.setAttr(path, lock=True)
    binding.set_value(8)
    cmds.setAttr(path, lock=False)
    cmds.setAttr(path, 9)
    flush()
    assert data.value == cmds.getAttr(path) == 9


def test_maya_undo_redo_noop_and_setter_correction_preserve_history(scene):
    """追加echo書込みを避け、setter補正のUndoでもRedo履歴を保持する。"""
    node, plug, owner, _ = scene

    class Model:
        """奇数入力を一つ下の偶数へ補正する正本。"""

        _value = 2

        @property
        def value(self):
            """補正済みの整数を返す。"""
            return self._value

        @value.setter
        def value(self, value):
            """偶数の整数を確定する。"""
            self._value = value // 2 * 2

    data = Model()
    binding = MayaIntBinding.from_attribute(
        data, "value", maya_plug=plug, parent=owner
    )
    cmds.flushUndo()
    binding.refresh()
    binding.set_value(2)
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    binding.set_value(8)
    cmds.undo()
    flush()
    assert data.value == cmds.getAttr(node + ".count") == 2
    cmds.redo()
    flush()
    assert data.value == 8
    cmds.flushUndo()
    cmds.setAttr(node + ".count", 37)
    flush()
    assert data.value == cmds.getAttr(node + ".count") == 36
    cmds.undo()
    flush()
    assert data.value == 36
    assert cmds.getAttr(node + ".count") == 37
    assert not binding.maya_view.is_synchronized
    assert not cmds.undoInfo(q=True, redoQueueEmpty=True)
    cmds.undo()
    flush()
    assert data.value == cmds.getAttr(node + ".count") == 8
    cmds.redo()
    flush()
    assert cmds.getAttr(node + ".count") == 37
    assert not cmds.undoInfo(q=True, redoQueueEmpty=True)
    cmds.redo()
    flush()
    assert binding.maya_view.is_synchronized
    assert data.value == cmds.getAttr(node + ".count") == 36


def test_initial_failure_single_view_cleanup_and_node_deletion(scene):
    """初期同期失敗・重複拒否・予約取消し・削除時の独立性を検証する。"""
    node, plug, owner, _ = scene
    binding = IntBinding.from_attribute(Data(2), "value", parent=owner)
    before = tuple(om.MMessage.nodeCallbacks(plug.plug.node()))
    cmds.setAttr(node + ".count", lock=True)
    with pytest.raises(RuntimeError, match="書き込めません"):
        MayaIntPlugView(binding.view_model, plug, owner)
    assert tuple(om.MMessage.nodeCallbacks(plug.plug.node())) == before
    flush()
    assert all(
        registry.is_disposed
        for registry in owner.findChildren(MayaCallbackRegistry)
    )
    cmds.setAttr(node + ".count", lock=False)
    view = MayaIntPlugView(binding.view_model, plug, owner)
    with pytest.raises(RuntimeError, match="複数"):
        MayaIntPlugView(binding.view_model, plug, owner)
    cmds.setAttr(node + ".count", 3)
    view.dispose()
    flush()
    assert binding.value == 2
    binding.set_value(4)
    assert cmds.getAttr(node + ".count") == 3
    replacement = MayaIntPlugView(binding.view_model, plug, owner)
    cmds.delete(node)
    assert replacement.is_disposed
    binding.set_value(5)
    assert binding.value == 5


def test_view_requires_python_store_optional_target_and_external_registry_disposal(
    scene,
):
    """未接続・Maya正本を拒否し、同期先省略と外部解除を扱う。"""
    _, plug, owner, _ = scene
    vm = IntViewModel(parent=owner)
    with pytest.raises(RuntimeError, match="Storeを接続"):
        MayaIntPlugView(vm, plug, owner)
    for maya_binding in (
        MayaIntPlugBinding(plug, parent=owner),
        MayaIntPlugsBinding((plug,), parent=owner),
    ):
        with pytest.raises(RuntimeError, match="Python側を正本"):
            MayaIntPlugView(maya_binding.view_model, plug, owner)
        maya_binding.dispose()
    binding = MayaIntBinding.from_attribute(Data(2), "value", parent=owner)
    assert binding.maya_view is None
    assert binding.set_value(3)
    view = MayaIntPlugView(binding.view_model, plug, owner)
    dispose_owned_callbacks(owner)
    assert view.is_disposed
    assert binding.set_value(4)
    assert view.last_sync_error is None


def test_readonly_python_rejects_maya_input_and_explicit_retry_restores_value(
    scene,
):
    """Pythonのreadonly属性ではMaya入力を採用せず、明示再同期で戻す。"""
    node, plug, owner, _ = scene

    class ReadOnly:
        """setterのない整数正本。"""

        @property
        def value(self):
            """固定された整数を返す。"""
            return 2

    binding = MayaIntBinding.from_attribute(
        ReadOnly(), "value", maya_plug=plug, parent=owner
    )
    cmds.setAttr(node + ".count", 5)
    flush()
    assert binding.value == 2
    assert not binding.maya_view.is_synchronized
    assert binding.maya_view.sync_from_view_model()
    assert cmds.getAttr(node + ".count") == 2


def test_compound_parent_lock_connection_rename_and_attribute_removal(
    new_scene,
):
    """compound祖先の制約とリネーム、属性削除後の独立性を確認する。"""
    owner = qt.QObject()
    nodes = [cmds.createNode("transform") for _ in range(2)]
    for node in nodes:
        cmds.addAttr(node, longName="counts", attributeType="long2")
        cmds.addAttr(
            node, longName="first", attributeType="long", parent="counts"
        )
        cmds.addAttr(
            node, longName="second", attributeType="long", parent="counts"
        )
    plug = resolve_int_plug(nodes[0], "counts.first")
    binding = MayaIntBinding.from_attribute(
        Data(), "value", maya_plug=plug, parent=owner
    )
    try:
        cmds.setAttr(nodes[0] + ".counts", lock=True)
        binding.set_value(7)
        assert not binding.maya_view.is_synchronized
        cmds.setAttr(nodes[0] + ".counts", lock=False)
        flush()
        assert cmds.getAttr(nodes[0] + ".first") == 7
        cmds.connectAttr(nodes[1] + ".counts", nodes[0] + ".counts")
        binding.set_value(8)
        flush()
        assert binding.value == 8
        cmds.disconnectAttr(nodes[1] + ".counts", nodes[0] + ".counts")
        flush()
        renamed = cmds.rename(nodes[0], "renamedIntSource")
        binding.set_value(9)
        assert cmds.getAttr(renamed + ".first") == 9
        cmds.deleteAttr(renamed + ".counts")
        flush()
        assert binding.maya_view.is_disposed
        assert binding.set_value(10)
    finally:
        owner.deleteLater()
        flush()


def test_initial_range_failure_leaves_no_callbacks_or_changed_maya_value(
    scene,
):
    """初期値がhard limitを超える場合はMaya値を変更せず構築を中断する。"""
    node, plug, owner, _ = scene
    cmds.addAttr(node + ".count", edit=True, minValue=0, maxValue=10)
    before = tuple(om.MMessage.nodeCallbacks(plug.plug.node()))
    data = Data(20)
    with pytest.raises(ValueError):
        MayaIntBinding.from_attribute(
            data, "value", maya_plug=plug, parent=owner
        )
    assert data.value == 20
    assert cmds.getAttr(node + ".count") == 0
    assert tuple(om.MMessage.nodeCallbacks(plug.plug.node())) == before


def test_animated_destination_evaluation_is_not_python_input(scene):
    """時間カーブの評価値を正本へ流し込まず、切断後にPython値を適用する。"""
    node, plug, owner, _ = scene
    data = Data(2)
    binding = MayaIntBinding.from_attribute(
        data, "value", maya_plug=plug, parent=owner
    )
    path = node + ".count"
    cmds.setKeyframe(path, time=1, value=2.25)
    cmds.setKeyframe(path, time=10, value=8.75)
    curve = cmds.listConnections(path, source=True, destination=False)[0]
    before = cmds.keyframe(curve, query=True, valueChange=True)
    cmds.currentTime(5)
    flush()
    binding.set_value(25)
    assert data.value == 25
    assert not binding.maya_view.is_writable
    assert not binding.maya_view.is_synchronized
    assert cmds.keyframe(curve, query=True, valueChange=True) == before
    cmds.disconnectAttr(curve + ".output", path)
    flush()
    assert binding.value == cmds.getAttr(path) == 25
    assert binding.maya_view.is_synchronized


def test_invalid_view_model_owner_and_plug_are_rejected(scene):
    """動的呼出しでも不正なViewModel・所有者・属性を構築前に拒否する。"""
    _, plug, owner, _ = scene
    binding = IntBinding.from_attribute(Data(), "value", parent=owner)
    with pytest.raises(TypeError, match="IntViewModel"):
        MayaIntPlugView(object(), plug, owner)
    with pytest.raises(TypeError, match="QObject"):
        MayaIntPlugView(binding.view_model, plug, object())
    with pytest.raises(TypeError, match="PlugOperator"):
        MayaIntPlugView(binding.view_model, object(), owner)
