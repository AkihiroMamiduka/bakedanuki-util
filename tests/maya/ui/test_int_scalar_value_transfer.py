# coding: utf-8
"""整数scalarの検出、Copy／Paste、範囲と旧schemaの互換性を確認する。"""

import pytest
from maya import cmds

from bd_util.maya.node.inspection import inspect_scalar_attributes
from bd_util.maya.ui import (
    MayaNodeValueSnapshot,
    MayaScalarValueSnapshot,
    MayaScalarValueTransfer,
    apply_scalar_value_transfer,
    capture_scalar_node_values,
    decode_scalar_value_transfer,
    encode_scalar_value_transfer,
)


def test_integer_capture_paste_and_undo(new_scene):
    """三つの整数型とcompound子を精度を失わず一括転送する。"""
    source = cmds.createNode("transform")
    target = cmds.createNode("transform")
    for node in (source, target):
        for kind in ("byte", "short", "long"):
            cmds.addAttr(node, longName=kind + "Value", attributeType=kind)
        cmds.addAttr(
            node,
            longName="group",
            attributeType="compound",
            numberOfChildren=1,
        )
        cmds.addAttr(
            node, longName="childValue", attributeType="long", parent="group"
        )
    values = (
        ("byteValue", 255),
        ("shortValue", -32768),
        ("longValue", 2147483647),
        ("group.childValue", -2147483648),
    )
    for path, value in values:
        cmds.setAttr(source + "." + path, value)
    attributes = {
        item.path: item for item in inspect_scalar_attributes(source)
    }
    assert [attributes[path].kind for path, _value in values] == [
        "byte",
        "short",
        "long",
        "long",
    ]
    snapshot = capture_scalar_node_values(
        source, tuple(attributes[path] for path, _value in values)
    )
    transfer = MayaScalarValueTransfer((snapshot,))
    document = encode_scalar_value_transfer(transfer)
    assert document["version"] == 3
    assert decode_scalar_value_transfer(document) == transfer
    assert [item.value for item in snapshot.values] == [
        value for _path, value in values
    ]

    cmds.undoInfo(state=True)
    cmds.flushUndo()
    result = apply_scalar_value_transfer((target,), transfer)
    assert result.changed and result.eligible_count == len(values)
    assert result.excluded == ()
    assert [cmds.getAttr(target + "." + path) for path, _value in values] == [
        value for _path, value in values
    ]
    cmds.undo()
    assert all(
        cmds.getAttr(target + "." + path) == 0 for path, _value in values
    )
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_integer_schema_range_and_legacy_version(new_scene):
    """整数型の不正値を拒否し、従来のversion 2値は読める。"""
    del new_scene
    for kind, invalid in (
        ("byte", -1),
        ("short", 32768),
        ("long", 2147483648),
    ):
        with pytest.raises(ValueError):
            MayaScalarValueSnapshot("count", kind, invalid)
    for invalid in (True, 1.5, "1"):
        with pytest.raises(TypeError):
            MayaScalarValueSnapshot("count", "long", invalid)
    document = encode_scalar_value_transfer(
        MayaScalarValueTransfer(
            (
                MayaNodeValueSnapshot(
                    (MayaScalarValueSnapshot("count", "long", 1),)
                ),
            )
        )
    )
    document["version"] = 2
    with pytest.raises(ValueError, match="version 1・2"):
        decode_scalar_value_transfer(document)
    document["nodes"] = [
        {"values": [{"path": "enabled", "kind": "bool", "value": True}]}
    ]
    assert (
        decode_scalar_value_transfer(document).nodes[0].values[0].value is True
    )
