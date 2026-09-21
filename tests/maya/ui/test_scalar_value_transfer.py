# coding: utf-8
"""Maya scalar値の型付きcopyと同path pasteを検証する。"""

import math

import pytest
from maya import cmds

from bd_util.maya.node.inspection import inspect_scalar_attributes
from bd_util.maya.ui import (
    MayaNodeValueSnapshot,
    MayaScalarValueSnapshot,
    MayaScalarValueTransfer,
    apply_scalar_value_transfer,
    apply_scalar_value_transfer_to_paths,
    apply_scalar_value_to_paths,
    capture_all_scalar_node_values,
    capture_scalar_node_values,
    decode_scalar_value_transfer,
    encode_scalar_value_transfer,
)
from bd_util.ui import EnumDefinition


def _attributes(node_name, *paths):
    """指定pathの属性情報を引数順に返す。"""
    lookup = {
        attribute.path: attribute
        for attribute in inspect_scalar_attributes(node_name)
    }
    return tuple(lookup[path] for path in paths)


@pytest.fixture
def scene(new_scene):
    """三つのtransformと単位・Undo設定を用意して元へ戻す。"""
    nodes = [cmds.createNode("transform") for _ in range(3)]
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    undo_enabled = cmds.undoInfo(q=True, state=True)
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    yield nodes
    cmds.currentUnit(linear=units[0], angle=units[1])
    cmds.undoInfo(state=undo_enabled)


def test_capture_round_trip_and_multi_target_paste_share_one_undo(scene):
    """全scalar型を公開単位で保持し、複数nodeへ一回で貼ってUndoする。"""
    source, first, second = scene
    cmds.setAttr(source + ".tx", 12.5)
    cmds.setAttr(source + ".rx", 30.0)
    cmds.setAttr(source + ".sx", 2.25)
    cmds.setAttr(source + ".visibility", False)
    cmds.setAttr(source + ".rotateOrder", 5)
    attributes = _attributes(
        source,
        "translate.translateX",
        "rotate.rotateX",
        "scale.scaleX",
        "visibility",
        "rotateOrder",
    )
    cmds.currentUnit(linear="m", angle="rad")

    snapshot = capture_scalar_node_values(source, attributes)
    transfer = MayaScalarValueTransfer((snapshot,))
    restored = decode_scalar_value_transfer(
        encode_scalar_value_transfer(transfer)
    )
    assert restored == transfer
    assert [item.value for item in snapshot.values[:3]] == pytest.approx(
        [12.5, 30.0, 2.25]
    )
    cmds.flushUndo()

    result = apply_scalar_value_transfer((first, second), restored)
    assert result.changed
    assert result.eligible_count == 10
    assert result.excluded == ()
    assert [cmds.getAttr(node + ".tx") for node in (first, second)] == [
        0.125,
        0.125,
    ]
    assert [cmds.getAttr(node + ".rx") for node in (first, second)] == (
        pytest.approx([math.pi / 6] * 2)
    )
    assert [cmds.getAttr(node + ".sx") for node in (first, second)] == [
        2.25,
        2.25,
    ]
    assert [
        cmds.getAttr(node + ".visibility") for node in (first, second)
    ] == [False, False]
    assert [
        cmds.getAttr(node + ".rotateOrder") for node in (first, second)
    ] == [5, 5]

    cmds.undo()
    assert [cmds.getAttr(node + ".tx") for node in (first, second)] == [0, 0]
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_capture_all_includes_hidden_supported_scalar_attributes(scene):
    """表示状態と行選択に依存せず、対応する非表示属性もすべて取得する。"""
    source, _first, _second = scene
    cmds.addAttr(source, ln="hiddenValue", at="double", keyable=False)
    cmds.setAttr(source + ".hiddenValue", 4.25)

    snapshot = capture_all_scalar_node_values(source)
    values = {item.path: item.value for item in snapshot.values}

    assert values["hiddenValue"] == 4.25
    assert values["translate.translateX"] == 0.0
    assert values["visibility"] is True


def test_same_path_kind_enum_and_writability_select_targets(scene):
    """欠落・型違い・enum定義違い・lockだけを対象外として報告する。"""
    source, first, second = scene
    for node in (source, first, second):
        cmds.addAttr(node, ln="weight", at="double", keyable=True)
        cmds.addAttr(
            node,
            ln="mode",
            at="enum",
            enumName="Off=0:On=5",
            keyable=True,
        )
    cmds.addAttr(source, ln="onlySource", at="double", keyable=True)
    cmds.addAttr(source, ln="differentKind", at="double", keyable=True)
    for node in (first, second):
        cmds.addAttr(node, ln="differentKind", at="bool", keyable=True)
    cmds.setAttr(source + ".weight", 3.5)
    cmds.setAttr(source + ".mode", 5)
    cmds.setAttr(source + ".onlySource", 7.0)
    cmds.setAttr(second + ".weight", lock=True)
    cmds.addAttr(second + ".mode", edit=True, enumName="Off=0:Other=5")
    transfer = MayaScalarValueTransfer(
        (
            capture_scalar_node_values(
                source,
                _attributes(
                    source,
                    "weight",
                    "mode",
                    "onlySource",
                    "differentKind",
                ),
            ),
        )
    )
    cmds.flushUndo()

    result = apply_scalar_value_transfer((first, second), transfer)
    assert result.changed
    assert result.eligible_count == 2
    assert cmds.getAttr(first + ".weight") == 3.5
    assert cmds.getAttr(first + ".mode") == 5
    assert cmds.getAttr(second + ".weight") == 0
    assert cmds.getAttr(second + ".mode") == 0
    assert len(result.excluded) == 6
    assert any("ロック" in reason for reason in result.excluded)
    assert any("enum定義" in reason for reason in result.excluded)
    assert sum("対応する属性なし" in reason for reason in result.excluded) == 2
    assert sum("型・単位が異なる" in reason for reason in result.excluded) == 2

    cmds.undo()
    assert cmds.getAttr(first + ".weight") == 0
    assert cmds.getAttr(first + ".mode") == 0
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_later_range_error_rejects_all_eligible_targets(scene):
    """一つの範囲違反があれば他targetも書き込まずUndoを残さない。"""
    source, first, second = scene
    for node in (source, first, second):
        options = {"maxValue": 5.0} if node == second else {}
        cmds.addAttr(node, ln="limited", at="double", **options)
    cmds.setAttr(source + ".limited", 9.0)
    transfer = MayaScalarValueTransfer(
        (capture_scalar_node_values(source, _attributes(source, "limited")),)
    )
    cmds.flushUndo()

    with pytest.raises(ValueError, match="上限"):
        apply_scalar_value_transfer((first, second), transfer)
    assert cmds.getAttr(first + ".limited") == 0
    assert cmds.getAttr(second + ".limited") == 0
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_noop_and_only_excluded_targets_leave_undo_empty(scene):
    """同値または全対象外の貼り付けでは変更とUndo項目を作らない。"""
    source, first, second = scene
    cmds.setAttr(source + ".sx", 1.0)
    transfer = MayaScalarValueTransfer(
        (
            capture_scalar_node_values(
                source, _attributes(source, "scale.scaleX")
            ),
        )
    )
    cmds.setAttr(second + ".sx", lock=True)
    cmds.flushUndo()

    result = apply_scalar_value_transfer((first, second), transfer)
    assert not result.changed
    assert result.eligible_count == 1
    assert len(result.excluded) == 1
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_schema_rejects_unknown_or_ambiguous_external_data():
    """version、未知key、重複path、型の曖昧さを復元前に拒否する。"""
    definition = EnumDefinition.from_mapping({0: "Off", 5: "On"})
    valid = MayaScalarValueTransfer(
        (
            MayaNodeValueSnapshot(
                (MayaScalarValueSnapshot("mode", "enum", 5, definition),)
            ),
        )
    )
    document = encode_scalar_value_transfer(valid)
    document["version"] = True
    with pytest.raises(TypeError):
        decode_scalar_value_transfer(document)

    unknown = encode_scalar_value_transfer(valid)
    unknown["extra"] = 1
    with pytest.raises(ValueError, match="未対応のkey"):
        decode_scalar_value_transfer(unknown)

    duplicate = encode_scalar_value_transfer(valid)
    nodes = duplicate["nodes"]
    assert isinstance(nodes, list)
    node = nodes[0]
    assert isinstance(node, dict)
    values = node["values"]
    assert isinstance(values, list)
    values.append(dict(values[0]))
    with pytest.raises(ValueError, match="複数回"):
        decode_scalar_value_transfer(duplicate)


def test_multiple_sources_are_reserved_but_not_silently_applied(scene):
    """schemaで保持できる複数sourceを現段階の貼り付けで拒否する。"""
    source, first, _second = scene
    snapshot = capture_scalar_node_values(
        source, _attributes(source, "translate.translateX")
    )
    transfer = MayaScalarValueTransfer((snapshot, snapshot))
    with pytest.raises(ValueError, match="一つのコピー元"):
        apply_scalar_value_transfer((first,), transfer)


def test_single_value_pastes_to_multiple_paths_and_nodes_with_one_undo(scene):
    """一つの値を同じ型の複数pathと複数nodeへ展開してUndoする。"""
    source, first, second = scene
    cmds.setAttr(source + ".tx", 7.5)
    transfer = MayaScalarValueTransfer(
        (
            capture_scalar_node_values(
                source, _attributes(source, "translate.translateX")
            ),
        )
    )
    cmds.setAttr(second + ".tz", lock=True)
    cmds.flushUndo()

    result = apply_scalar_value_to_paths(
        (first, second),
        ("translate.translateY", "translate.translateZ"),
        transfer,
    )
    assert result.changed
    assert result.eligible_count == 3
    assert len(result.excluded) == 1
    assert "ロック" in result.excluded[0]
    assert [cmds.getAttr(node + ".ty") for node in (first, second)] == [
        7.5,
        7.5,
    ]
    assert cmds.getAttr(first + ".tz") == 7.5
    assert cmds.getAttr(second + ".tz") == 0

    cmds.undo()
    assert [cmds.getAttr(node + ".ty") for node in (first, second)] == [0, 0]
    assert cmds.getAttr(first + ".tz") == 0
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_multiple_values_paste_only_to_selected_same_paths(scene):
    """複数搬送値から指定pathだけを選び、ないコピー値は対象外として報告する。"""
    source, first, second = scene
    cmds.setAttr(source + ".tx", 7.5)
    cmds.setAttr(source + ".ty", 8.5)
    for node in (first, second):
        cmds.addAttr(node, ln="targetOnly", at="double", keyable=True)
    transfer = MayaScalarValueTransfer(
        (
            capture_scalar_node_values(
                source,
                _attributes(
                    source,
                    "translate.translateX",
                    "translate.translateY",
                ),
            ),
        )
    )
    cmds.flushUndo()

    result = apply_scalar_value_transfer_to_paths(
        (first, second),
        ("translate.translateX", "targetOnly"),
        transfer,
    )

    assert result.changed
    assert result.eligible_count == 2
    assert len(result.excluded) == 2
    assert all("コピーされた値なし" in item for item in result.excluded)
    assert [cmds.getAttr(node + ".tx") for node in (first, second)] == [
        7.5,
        7.5,
    ]
    assert [cmds.getAttr(node + ".ty") for node in (first, second)] == [0, 0]

    cmds.undo()
    assert [cmds.getAttr(node + ".tx") for node in (first, second)] == [0, 0]
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_single_enum_value_requires_matching_definition_at_each_path(scene):
    """enum値の複数path展開でも整数値と項目名の定義を照合する。"""
    source, first, second = scene
    for node in (source, first, second):
        cmds.addAttr(
            node,
            ln="mode",
            at="enum",
            enumName="Off=0:On=5",
            keyable=True,
        )
        cmds.addAttr(
            node,
            ln="quality",
            at="enum",
            enumName="Off=0:On=5",
            keyable=True,
        )
    cmds.addAttr(second, ln="variant", at="enum", enumName="Off=0:Other=5")
    cmds.addAttr(first, ln="variant", at="enum", enumName="Off=0:On=5")
    cmds.setAttr(source + ".mode", 5)
    transfer = MayaScalarValueTransfer(
        (capture_scalar_node_values(source, _attributes(source, "mode")),)
    )
    cmds.flushUndo()

    result = apply_scalar_value_to_paths(
        (first, second), ("quality", "variant"), transfer
    )
    assert result.changed
    assert result.eligible_count == 3
    assert len(result.excluded) == 1
    assert "enum定義" in result.excluded[0]
    assert [cmds.getAttr(node + ".quality") for node in (first, second)] == [
        5,
        5,
    ]
    assert cmds.getAttr(first + ".variant") == 5
    assert cmds.getAttr(second + ".variant") == 0


def test_single_value_path_paste_rejects_ambiguous_inputs(scene):
    """複数搬送値、空path集合、重複pathをscene変更前に拒否する。"""
    source, first, _second = scene
    one_value = MayaScalarValueTransfer(
        (
            capture_scalar_node_values(
                source, _attributes(source, "translate.translateX")
            ),
        )
    )
    multiple_values = MayaScalarValueTransfer(
        (
            capture_scalar_node_values(
                source,
                _attributes(
                    source,
                    "translate.translateX",
                    "translate.translateY",
                ),
            ),
        )
    )
    with pytest.raises(ValueError, match="一つの属性値"):
        apply_scalar_value_to_paths(
            (first,), ("translate.translateY",), multiple_values
        )
    with pytest.raises(ValueError, match="一つ以上"):
        apply_scalar_value_to_paths((first,), (), one_value)
    with pytest.raises(ValueError, match="複数回"):
        apply_scalar_value_to_paths(
            (first,),
            ("translate.translateY", "translate.translateY"),
            one_value,
        )
