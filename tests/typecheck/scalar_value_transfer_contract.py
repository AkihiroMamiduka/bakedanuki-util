# coding: utf-8
"""Maya scalar値transferの公開型をIDE利用時と同じ入口で固定する。"""

from typing import assert_type

from bd_util.maya.node.inspection import ScalarAttributeInfo
from bd_util.maya.ui import (
    MayaNodeValueSnapshot,
    MayaScalarPasteResult,
    MayaScalarValue,
    MayaScalarValueClipboard,
    MayaScalarValueSnapshot,
    MayaScalarValueTransfer,
    apply_scalar_value_transfer,
    capture_scalar_node_values,
    decode_scalar_value_transfer,
    encode_scalar_value_transfer,
)
from bd_util.ui import EnumDefinition, JsonClipboard


def contract(
    node_name: str,
    target_names: tuple[str, ...],
    attributes: tuple[ScalarAttributeInfo, ...],
    value: MayaScalarValue,
) -> None:
    """公開facadeから具体型と戻り値を辿れることを確認する。"""
    definition = EnumDefinition.from_mapping({0: "Off", 5: "On"})
    snapshot = MayaScalarValueSnapshot("mode", "enum", 5, definition)
    node = MayaNodeValueSnapshot((snapshot,))
    transfer = MayaScalarValueTransfer((node,))
    assert_type(value, bool | float | int)
    assert_type(
        capture_scalar_node_values(node_name, attributes),
        MayaNodeValueSnapshot,
    )
    assert_type(encode_scalar_value_transfer(transfer), dict[str, object])
    assert_type(decode_scalar_value_transfer({}), MayaScalarValueTransfer)
    assert_type(
        apply_scalar_value_transfer(target_names, transfer),
        MayaScalarPasteResult,
    )
    clipboard = MayaScalarValueClipboard()
    assert_type(clipboard.contains(), bool)
    assert_type(clipboard.read(), MayaScalarValueTransfer)
    generic = JsonClipboard("application/x-contract+json", "CONTRACT/1\n")
    assert_type(generic.read(), object)
