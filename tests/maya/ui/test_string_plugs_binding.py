# coding: utf-8
import pytest
from maya import cmds

from bd_util.maya.ui import MayaStringPlugsBinding, resolve_string_plug
from bd_util.maya.ui.binding import plugs_binding
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import qt


def flush() -> None:
    """Maya callbackとQtの遅延処理を終える。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


def create_joints(*values: str) -> tuple[str, ...]:
    """異なるotherTypeを持つ既存joint相当の対象を作る。"""
    result = []
    for value in values:
        joint = cmds.createNode("joint")
        cmds.setAttr(joint + ".otherType", value, type="string")
        result.append(joint)
    return tuple(result)


def bind_joints(joints: tuple[str, ...]) -> MayaStringPlugsBinding:
    """指定順のotherTypeを一つのBindingへ接続する。"""
    return MayaStringPlugsBinding(
        [resolve_string_plug(joint, "otherType") for joint in joints]
    )


def test_mixed_representative_input_empty_undo_and_redo(new_scene):
    """混在を読取り専用で検出し、同値要求も一回Undoで揃える。"""
    joints = create_joints("arm", "leg", "")
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    binding = bind_joints(joints)
    values = []
    states = []
    binding.changed.connect(values.append)
    binding.state_changed.connect(lambda: states.append(binding.is_mixed))
    try:
        assert binding.value == "arm"
        assert binding.is_mixed
        assert binding.target_count == binding.writable_count == 3
        assert [cmds.getAttr(joint + ".otherType") for joint in joints] == [
            "arm",
            "leg",
            "",
        ]
        assert binding.apply_representative_value()
        assert not binding.is_mixed
        assert values == []
        assert [cmds.getAttr(joint + ".otherType") for joint in joints] == [
            "arm",
            "arm",
            "arm",
        ]
        cmds.undo()
        flush()
        assert binding.is_mixed
        assert [cmds.getAttr(joint + ".otherType") for joint in joints] == [
            "arm",
            "leg",
            "",
        ]
        assert not cmds.undoInfo(query=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert not binding.is_mixed
        assert binding.set_value("")
        assert binding.value == ""
        assert [cmds.getAttr(joint + ".otherType") for joint in joints] == [
            "",
            "",
            "",
        ]
        assert not binding.set_value("")
        assert values == [""]
        assert states[0] is False
        assert True in states
        assert states[-1] is False
    finally:
        binding.dispose()
        flush()


def test_nonrepresentative_external_change_and_readonly_targets(new_scene):
    """後続だけの外部変更と編集不可対象を個別に扱う。"""
    joints = create_joints("a", "a", "a")
    binding = bind_joints(joints)
    states = []
    binding.state_changed.connect(lambda: states.append(binding.is_mixed))
    try:
        cmds.setAttr(joints[1] + ".otherType", "outside", type="string")
        flush()
        assert binding.value == "a"
        assert binding.is_mixed
        assert states[-1]
        cmds.setAttr(joints[2] + ".otherType", lock=True)
        flush()
        assert binding.writable_count == 2
        assert binding.target_states[2].reason == "ロックされています"
        assert binding.set_value("new")
        assert cmds.getAttr(joints[0] + ".otherType") == "new"
        assert cmds.getAttr(joints[1] + ".otherType") == "new"
        assert cmds.getAttr(joints[2] + ".otherType") == "a"
        assert binding.is_mixed
        cmds.setAttr(joints[0] + ".otherType", lock=True)
        flush()
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value("ignored")
        assert cmds.getAttr(joints[1] + ".otherType") == "new"
    finally:
        binding.dispose()
        flush()


def test_invalid_input_duplicate_and_deleted_target(new_scene):
    """型と重複を拒否し、削除した対象へUndoで再接続しない。"""
    joints = create_joints("a", "b")
    plug = resolve_string_plug(joints[0], "otherType")
    with pytest.raises(ValueError):
        MayaStringPlugsBinding([plug, plug])
    with pytest.raises(ValueError):
        MayaStringPlugsBinding([])
    binding = bind_joints(joints)
    try:
        with pytest.raises(TypeError):
            binding.set_value(2)
        with pytest.raises(ValueError):
            binding.set_value("bad\x00value")
        assert cmds.getAttr(joints[0] + ".otherType") == "a"
        assert cmds.getAttr(joints[1] + ".otherType") == "b"
        cmds.delete(joints[1])
        flush()
        assert not binding.target_states[1].is_available
        assert binding.writable_count == 1
        assert binding.set_value("surviving")
        cmds.undo()
        flush()
        cmds.undo()
        flush()
        assert not binding.target_states[1].is_available
    finally:
        binding.dispose()
        flush()


def test_mid_write_failure_restores_prior_values(new_scene, monkeypatch):
    """後続書込み失敗時は先行対象を元の値へ戻す。"""
    joints = create_joints("first", "second")
    binding = bind_joints(joints)
    original_apply = plugs_binding._PreparedStringWrite.apply
    apply_calls = 0
    failures = []
    binding.edit_failed.connect(failures.append)

    def fail_second(write: plugs_binding._PreparedStringWrite) -> None:
        """二件目の書込みだけ失敗させる。"""
        nonlocal apply_calls
        apply_calls += 1
        if apply_calls == 2:
            raise RuntimeError("二件目を拒否")
        original_apply(write)

    monkeypatch.setattr(
        plugs_binding._PreparedStringWrite, "apply", fail_second
    )
    try:
        with pytest.raises(RuntimeError, match="二件目を拒否"):
            binding.set_value("new")
        assert cmds.getAttr(joints[0] + ".otherType") == "first"
        assert cmds.getAttr(joints[1] + ".otherType") == "second"
        assert binding.value == "first"
        assert failures and "二件目を拒否" in failures[-1]
    finally:
        binding.dispose()
        flush()


def test_callbacks_released_on_dispose(new_scene):
    """Binding終了時に全nodeのMaya callbackを解除する。"""
    joints = create_joints("a", "b")
    binding = bind_joints(joints)
    registry = binding.findChildren(MayaCallbackRegistry)[0]
    assert registry.callback_ids
    binding.dispose()
    flush()
    assert registry.callback_ids == ()


def test_connection_and_duplicate_dag_names_follow_real_targets(new_scene):
    """同名jointの完全pathを使い、入力接続だけを除外する。"""
    parents = [cmds.createNode("transform") for _ in range(2)]
    joints = [
        cmds.createNode("joint", name="same", parent=parent)
        for parent in parents
    ]
    paths = [
        cmds.listRelatives(parent, children=True, fullPath=True)[0]
        for parent in parents
    ]
    binding = bind_joints(tuple(paths))
    try:
        source = cmds.createNode("network")
        cmds.addAttr(source, longName="text", dataType="string")
        cmds.setAttr(source + ".text", "driven", type="string")
        cmds.connectAttr(source + ".text", paths[1] + ".otherType")
        flush()
        assert binding.writable_count == 1
        assert "入力接続" in (binding.target_states[1].reason or "")
        assert binding.set_value("first only")
        assert cmds.getAttr(paths[0] + ".otherType") == "first only"
        assert cmds.getAttr(paths[1] + ".otherType") == "driven"
        cmds.disconnectAttr(source + ".text", paths[1] + ".otherType")
        renamed = cmds.rename(paths[1], "renamedStringJoint")
        flush()
        assert binding.set_value("both")
        assert cmds.getAttr(paths[0] + ".otherType") == "both"
        assert cmds.getAttr(renamed + ".otherType") == "both"
    finally:
        binding.dispose()
        flush()
