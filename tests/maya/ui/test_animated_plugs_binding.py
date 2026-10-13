# coding: utf-8
"""既存アニメーションへの明示値入力と複数属性のUndoを検証する。"""

import pytest
from maya import cmds

from bd_util.maya.ui import (
    MayaBoolPlugsBinding,
    MayaEditSession,
    MayaEnumPlugsBinding,
    MayaFloatOffsetEdit,
    MayaFloatPlugsBinding,
    MayaFloatValueEdit,
    apply_plugs_values,
    resolve_bool_plug,
    resolve_enum_plug,
    resolve_float_plug,
)
from bd_util.ui import qt


def flush():
    """Maya通知後の値同期と所有者の破棄を処理する。"""
    for _ in range(3):
        qt.QtCore.QCoreApplication.processEvents()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            None, qt.QEvent.Type.DeferredDelete
        )


@pytest.fixture
def scene(new_scene):
    """通常属性とアニメーション属性を比較できる環境を作る。"""
    owner = qt.QObject()
    nodes = [cmds.createNode("transform") for _ in range(3)]
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    yield nodes, owner
    owner.deleteLater()
    flush()
    cmds.currentUnit(linear=units[0], angle=units[1])


def animate(plug, first=2, last=8):
    """二つの時刻へキーを作り、その間の現在時刻を評価する。"""
    cmds.setKeyframe(plug, time=1, value=first)
    cmds.setKeyframe(plug, time=10, value=last)
    cmds.currentTime(5)
    return cmds.listConnections(plug, source=True, destination=False)[0]


def bind(nodes, owner, attribute="tx", *, key_animated=True):
    """指定順の数値属性へアニメーション編集方針を渡す。"""
    return MayaFloatPlugsBinding(
        [resolve_float_plug(node, attribute) for node in nodes],
        key_animated=key_animated,
        parent=owner,
    )


def test_animation_edit_is_opt_in_and_same_value_does_not_insert(scene):
    """既定の読み取り専用と、同値入力でキーを作らない契約を維持する。"""
    nodes, owner = scene
    curve = animate(nodes[0] + ".tx")
    disabled = MayaFloatPlugsBinding(
        [resolve_float_plug(nodes[0], "tx")], parent=owner
    )
    binding = bind(nodes[:1], owner)
    cmds.flushUndo()
    assert not disabled.view_model.set_value_command.can_execute
    assert not disabled.set_value(12)
    assert binding.view_model.set_value_command.can_execute
    assert not binding.set_value(binding.value)
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 2
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_mixed_static_animated_and_locked_targets_share_one_undo(scene):
    """混在入力を即座に実値へ同期し、追加キーと通常値を一回でUndoする。"""
    nodes, owner = scene
    curve = animate(nodes[0] + ".tx")
    initial = cmds.getAttr(nodes[0] + ".tx")
    cmds.setAttr(nodes[2] + ".tx", lock=True)
    binding = bind(nodes, owner)
    cmds.flushUndo()
    assert binding.writable_count == 2
    assert binding.set_value(12)
    assert binding.value == 12
    assert [cmds.getAttr(node + ".tx") for node in nodes] == [12, 12, 0]
    assert cmds.keyframe(curve, query=True, time=(5, 5), valueChange=True) == [
        12
    ]
    cmds.undo()
    flush()
    assert binding.value == pytest.approx(initial)
    assert cmds.getAttr(nodes[1] + ".tx") == 0
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 2
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    assert binding.value == 12
    assert cmds.getAttr(nodes[1] + ".tx") == 12


@pytest.mark.parametrize("kind", ["bool", "enum"])
def test_discrete_values_write_existing_animation(scene, kind):
    """boolとenumも現在時刻のキー経由で値を確定する。"""
    nodes, owner = scene
    if kind == "bool":
        path, before, after = "visibility", True, False
        factory, resolver = MayaBoolPlugsBinding, resolve_bool_plug
    else:
        path, before, after = "mode", 0, 2
        factory, resolver = MayaEnumPlugsBinding, resolve_enum_plug
        cmds.addAttr(
            nodes[0], longName=path, attributeType="enum", enumName="A:B:C"
        )
    curve = animate(nodes[0] + "." + path, before, before)
    binding = factory(
        [resolver(nodes[0], path)], key_animated=True, parent=owner
    )
    cmds.flushUndo()
    assert binding.set_value(after)
    assert binding.value == after
    assert cmds.getAttr(nodes[0] + "." + path) == after
    cmds.undo()
    flush()
    assert binding.value == before
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 2


@pytest.mark.parametrize(
    "attribute,unit_options,value,expected",
    [
        ("tx", {"linear": "m"}, 125.0, 1.25),
        ("rx", {"angle": "rad"}, 90.0, 1.5707963267948966),
    ],
)
def test_public_units_are_preserved_for_animated_values(
    scene, attribute, unit_options, value, expected
):
    """cmとdegreeの公開入力をMayaの現在表示単位へ正しく反映する。"""
    nodes, owner = scene
    animate(nodes[0] + "." + attribute)
    cmds.currentUnit(**unit_options)
    binding = bind(nodes[:1], owner, attribute)
    assert binding.set_value(value)
    assert binding.value == pytest.approx(value)
    assert cmds.getAttr(nodes[0] + "." + attribute) == pytest.approx(expected)


def test_notifications_and_time_changes_never_create_keys(scene):
    """時刻移動と外部キー更新の再読取りは他属性へ書き戻さない。"""
    nodes, owner = scene
    curve = animate(nodes[0] + ".tx")
    binding = bind(nodes[:2], owner)
    for time, expected in [(1, 2), (10, 8), (1, 2)]:
        cmds.currentTime(time)
        flush()
        assert binding.value == expected
    cmds.keyframe(curve, edit=True, time=(1, 1), valueChange=6)
    flush()
    assert binding.value == 6
    assert cmds.getAttr(nodes[1] + ".tx") == 0
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 2


def test_multirow_offsets_and_continuous_edits_share_animation_backend(scene):
    """複数行と相対入力を同じbackendへ渡し、連続変更を一回でUndoする。"""
    nodes, owner = scene
    curve = animate(nodes[0] + ".tx")
    initial = cmds.getAttr(nodes[0] + ".tx")
    animated = bind(nodes[:1], owner)
    static = bind(nodes[1:2], owner)
    session = MayaEditSession(owner)
    cmds.flushUndo()
    session.begin()
    assert apply_plugs_values(
        [MayaFloatValueEdit(animated, 12), MayaFloatOffsetEdit(static, 3)],
        edit_session=session,
    )
    assert apply_plugs_values(
        [MayaFloatOffsetEdit(animated, 2), MayaFloatValueEdit(static, 9)],
        edit_session=session,
    )
    session.finish()
    assert animated.value == 14
    assert static.value == 9
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 3
    cmds.undo()
    flush()
    assert animated.value == pytest.approx(initial)
    assert static.value == 0
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 2
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_later_static_failure_removes_previously_inserted_key(
    scene, monkeypatch
):
    """後続の通常値書込み失敗時に、追加したキーを値だけ残さず復旧する。"""
    nodes, owner = scene
    curve = animate(nodes[0] + ".tx")
    initial = cmds.getAttr(nodes[0] + ".tx")
    binding = bind(nodes[:2], owner)
    original = cmds.setAttr

    def fail_later(name, value, **kwargs):
        """後続対象の新規入力だけを失敗させる。"""
        if (
            name.split(".", 1)[0].rsplit("|", 1)[-1] == nodes[1]
            and value == 12
        ):
            raise RuntimeError("later write failed")
        return original(name, value, **kwargs)

    monkeypatch.setattr(cmds, "setAttr", fail_later)
    with pytest.raises(RuntimeError, match="later write failed"):
        binding.set_value(12)
    assert binding.value == pytest.approx(initial)
    assert cmds.getAttr(nodes[1] + ".tx") == 0
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 2


def test_parent_lock_and_general_input_remain_read_only(scene):
    """アニメーション対応を有効にしても親lockと一般接続を解放しない。"""
    nodes, owner = scene
    animate(nodes[0] + ".tx")
    cmds.setAttr(nodes[0] + ".translate", lock=True)
    locked = bind(nodes[:1], owner)
    assert not locked.view_model.set_value_command.can_execute
    assert locked.target_states[0].reason == "ロックされています"
    cmds.connectAttr(nodes[1] + ".tx", nodes[2] + ".tx")
    connected = bind(nodes[2:], owner)
    assert not connected.view_model.set_value_command.can_execute
    assert not connected.set_value(12)
    assert cmds.isConnected(nodes[1] + ".tx", nodes[2] + ".tx")
