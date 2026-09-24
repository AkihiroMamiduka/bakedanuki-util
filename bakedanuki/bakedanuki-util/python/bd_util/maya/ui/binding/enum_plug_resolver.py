# coding: utf-8
from __future__ import annotations

from typing import Any, TypeAlias, cast

from maya.api import OpenMaya as om

from ...node import Nodes
from ...node._attribute_lookup import attribute_path, find_attribute_plug
from ...node.operator.attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
)

# 具象enumごとのAttrOperator型引数は、このadapter境界でのみ消去する。
MayaEnumPlug: TypeAlias = EnumPlugOperator[Any]


def _require_scalar_enum(plug: om.MPlug) -> None:
    if plug.isCompound or not plug.attribute().hasFn(om.MFn.kEnumAttribute):
        raise TypeError("plugにはscalar enumを指定してください")
    ancestor = plug
    while True:
        if ancestor.isArray or ancestor.isElement:
            raise TypeError("配列配下のplugには対応していません")
        if not ancestor.isChild:
            break
        ancestor = ancestor.parent()


def require_enum_plug(value: object) -> MayaEnumPlug:
    """配列配下ではない単一enum属性のPlugOperatorを検証する。

    Args:
        value: 検証するPlugOperator。

    Returns:
        検証済みのenum PlugOperator。

    Raises:
        TypeError: enum以外、compound、または配列配下のplugの場合。
    """
    if not isinstance(value, EnumPlugOperator):
        raise TypeError("plugにはEnumPlugOperatorを指定してください")
    result = cast(MayaEnumPlug, value)
    _require_scalar_enum(result.plug)
    return result


def _require_name(value: object) -> str:
    if not isinstance(value, str):
        raise TypeError("node_nameとattribute_nameにはstrを指定してください")
    if not value:
        raise ValueError("node_nameとattribute_nameには空でないstrが必要です")
    return value


def resolve_enum_plug(node_name: str, attribute_name: str) -> MayaEnumPlug:
    """既存のenum属性を長名・短名・compoundの相対pathから解決する。"""
    node_name = _require_name(node_name)
    attribute_name = _require_name(attribute_name)
    if any(character in attribute_name for character in "[]"):
        raise ValueError("配列要素のpathには対応していません")
    node = Nodes().existing(node_name)
    plug = find_attribute_plug(node.fn_node, attribute_name)
    _require_scalar_enum(plug)
    attribute = om.MFnAttribute(plug.attribute())
    path = attribute_path(plug)
    name = cast(str, attribute.name) if attribute.enforcingUniqueName else path
    operator: EnumAttrOperator[MayaEnumPlug] = EnumAttrOperator(
        node_cls=type(node),
        name=name,
        long_name=name,
        short_name=cast(str, attribute.shortName),
        attr_path=path,
    )
    return EnumPlugOperator(node=node, oprt_attr=operator, parent_attr_path="")
