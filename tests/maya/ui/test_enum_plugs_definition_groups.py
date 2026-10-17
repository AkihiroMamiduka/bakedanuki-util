# coding: utf-8
"""enum定義の実体共有による高速化と、共有しない対象の安全性を検証する。"""

import pytest
from maya import cmds

from bd_util.maya import _identity
from bd_util.maya.ui import (
    MayaEnumPlugsBinding,
    MayaEnumValueEdit,
    apply_plugs_values,
    resolve_enum_plug,
)
from bd_util.maya.ui.binding._enum_plug_value import EnumPlugValue


def test_thousand_joint_enum_edit_bounds_definition_reads(
    new_scene, monkeypatch
):
    """千jointの共有enumを線形回数で検証し、一操作のUndoとRedoを保つ。"""
    count = 1000
    nodes = [cmds.createNode("joint") for _ in range(count)]
    plugs = [resolve_enum_plug(node, "drawStyle") for node in nodes]
    attribute = plugs[0].plug.attribute()
    assert all(plug.plug.attribute() == attribute for plug in plugs)
    binding = MayaEnumPlugsBinding(plugs, monitor=False)
    definition_property = EnumPlugValue.definition
    reads = 0

    def count_definition(value):
        """旧実装の二乗取得は早期に止め、定義の実読取り回数を数える。"""
        nonlocal reads
        reads += 1
        if reads > 20 * count:
            pytest.fail("共有enumの定義取得が対象数に対して多すぎます")
        return definition_property.__get__(value, EnumPlugValue)

    try:
        cmds.flushUndo()
        with monkeypatch.context() as counting:
            counting.setattr(
                EnumPlugValue, "definition", property(count_definition)
            )
            assert apply_plugs_values((MayaEnumValueEdit(binding, 2),))
        assert 0 < reads <= 20 * count
        assert all(cmds.getAttr(node + ".drawStyle") == 2 for node in nodes)
        cmds.undo()
        assert all(cmds.getAttr(node + ".drawStyle") == 0 for node in nodes)
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        cmds.redo()
        assert all(cmds.getAttr(node + ".drawStyle") == 2 for node in nodes)
    finally:
        binding.dispose()
        binding.deleteLater()


@pytest.mark.parametrize("collide", [False, True])
def test_independent_enum_definitions_remain_live_when_locked(
    new_scene, monkeypatch, collide
):
    """同名同内容でも別実体を分離し、衝突とlockがあっても最新定義を照合する。"""
    nodes = [cmds.createNode("network") for _ in range(3)]
    for node in nodes:
        cmds.addAttr(
            node, longName="mode", attributeType="enum", enumName="A:B"
        )

    def same_hash(node):
        """異なるnodeと属性が同じhashを持つ条件を作る。"""
        return 1

    if collide:
        monkeypatch.setattr(_identity, "_object_hash", same_hash)
    binding = MayaEnumPlugsBinding(
        [resolve_enum_plug(node, "mode") for node in nodes], monitor=False
    )
    try:
        assert binding.set_value(1)
        cmds.addAttr(nodes[-1] + ".mode", edit=True, enumName="A:Changed")
        cmds.setAttr(nodes[-1] + ".mode", lock=True)
        cmds.flushUndo()

        # 書込み対象外の後続も定義の一致条件から外さない
        assert not binding.set_value(0)
        assert [cmds.getAttr(node + ".mode") for node in nodes] == [1, 1, 1]
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        assert "enum定義" in binding.target_states[-1].reason

        # 不一致を恒久cacheせず、定義が戻れば利用可能な対象への入力を再開する
        cmds.setAttr(nodes[-1] + ".mode", lock=False)
        cmds.addAttr(nodes[-1] + ".mode", edit=True, enumName="A:B")
        cmds.setAttr(nodes[-1] + ".mode", lock=True)
        binding.refresh()
        assert binding.set_value(0)
        assert [cmds.getAttr(node + ".mode") for node in nodes] == [0, 0, 1]
    finally:
        binding.dispose()
        binding.deleteLater()


@pytest.mark.parametrize("monitor", [False, True])
def test_shared_group_survives_member_deletion_without_retargeting(
    new_scene, monitor
):
    """後続groupの削除memberを飛ばし、基準削除と同名再作成では編集を止める。"""
    first = cmds.createNode("network", name="enumGroupRepresentative")
    joints = [cmds.createNode("joint") for _ in range(2)]
    definition = cmds.attributeQuery(
        "drawStyle", node=joints[0], listEnum=True
    )[0]
    cmds.addAttr(
        first, longName="mode", attributeType="enum", enumName=definition
    )
    binding = MayaEnumPlugsBinding(
        [resolve_enum_plug(first, "mode")]
        + [resolve_enum_plug(node, "drawStyle") for node in joints],
        monitor=monitor,
    )
    try:
        # 全体基準とは別の共有groupで、先頭memberだけを削除する
        cmds.delete(joints[0])
        assert binding.set_value(2)
        assert cmds.getAttr(first + ".mode") == 2
        assert cmds.getAttr(joints[1] + ".drawStyle") == 2
        assert not binding.target_states[1].is_available

        cmds.delete(first)
        replacement = cmds.createNode("network", name=first)
        cmds.addAttr(
            replacement,
            longName="mode",
            attributeType="enum",
            enumName=definition,
        )
        assert replacement == first
        cmds.flushUndo()
        assert not binding.set_value(1)
        assert cmds.getAttr(replacement + ".mode") == 0
        assert cmds.getAttr(joints[1] + ".drawStyle") == 2
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    finally:
        binding.dispose()
        binding.deleteLater()
