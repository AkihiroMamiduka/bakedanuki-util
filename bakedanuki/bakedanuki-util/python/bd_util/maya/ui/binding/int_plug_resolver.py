# coding: utf-8
"""既存Maya nodeのbyte・short・long属性を型付きPlugへ解決する。"""

from __future__ import annotations

from typing import Literal, TypeAlias, cast

from maya.api import OpenMaya as om

from ...node import Nodes
from ...node._attribute_lookup import attribute_path, find_attribute_plug
from ...node.operator.attr.define.std.at.scalar.numeric.range.byte import (
    ByteAttrOperator,
    BytePlugOperator,
)
from ...node.operator.attr.define.std.at.scalar.numeric.range.short import (
    ShortAttrOperator,
    ShortPlugOperator,
)
from ...node.operator.attr.define.std.at.scalar.numeric.range.long import (
    LongAttrOperator,
    LongPlugOperator,
)

MayaIntPlug: TypeAlias = (
    BytePlugOperator | ShortPlugOperator | LongPlugOperator
)
IntPlugKind: TypeAlias = Literal["byte", "short", "long"]


def int_plug_kind(plug: om.MPlug) -> IntPlugKind:
    """配列配下以外の単一byte・short・long属性だけを受け付ける。"""
    if plug.isCompound:
        raise TypeError("plugには単一の整数属性を指定してください")
    ancestor = plug
    while True:
        if ancestor.isArray or ancestor.isElement:
            raise TypeError("配列配下のplugには対応していません")
        if not ancestor.isChild:
            break
        ancestor = ancestor.parent()
    attribute = plug.attribute()
    if not attribute.hasFn(om.MFn.kNumericAttribute):
        raise TypeError("plugにはbyte・short・long属性を指定してください")
    numeric_type = om.MFnNumericAttribute(attribute).numericType()
    if numeric_type == om.MFnNumericData.kByte:
        return "byte"
    if numeric_type == om.MFnNumericData.kShort:
        return "short"
    if numeric_type == om.MFnNumericData.kLong:
        return "long"
    raise TypeError("plugにはbyte・short・long属性を指定してください")


def require_int_plug(value: object) -> MayaIntPlug:
    """型付きPlugとMaya属性の整数型が一致することを検証する。"""
    expected: IntPlugKind
    if isinstance(value, BytePlugOperator):
        expected = "byte"
    elif isinstance(value, ShortPlugOperator):
        expected = "short"
    elif isinstance(value, LongPlugOperator):
        expected = "long"
    else:
        raise TypeError("plugには整数用PlugOperatorを指定してください")
    result = value
    if int_plug_kind(result.plug) != expected:
        raise TypeError("PlugOperatorとMaya属性の整数型が一致しません")
    return result


def _require_name(value: object, argument_name: str) -> str:
    """空でないnode名または属性名を検証する。"""
    if not isinstance(value, str):
        raise TypeError(f"{argument_name}にはstrを指定してください")
    if not value:
        raise ValueError(f"{argument_name}には空でないstrを指定してください")
    return value


def resolve_int_plug(node_name: str, attribute_name: str) -> MayaIntPlug:
    """既存の単一整数属性を長名・短名・compound子pathで解決する。"""
    node_name = _require_name(node_name, "node_name")
    attribute_name = _require_name(attribute_name, "attribute_name")
    if any(character in attribute_name for character in "[]"):
        raise ValueError(
            "attribute_nameには単一の属性名か相対pathを指定してください"
        )
    node = Nodes().existing(node_name)
    try:
        plug = find_attribute_plug(node.fn_node, attribute_name)
    except AttributeError as error:
        raise AttributeError(
            f"属性が見つかりません: {node_name}.{attribute_name}"
        ) from error
    kind = int_plug_kind(plug)
    attribute = om.MFnAttribute(plug.attribute())
    path = attribute_path(plug)
    long_name = (
        cast(str, attribute.name) if attribute.enforcingUniqueName else path
    )
    short_name = cast(str, attribute.shortName)
    if kind == "byte":
        return BytePlugOperator(
            node=node,
            parent_attr_path="",
            oprt_attr=ByteAttrOperator(
                node_cls=type(node),
                name=long_name,
                long_name=long_name,
                short_name=short_name,
                attr_path=path,
            ),
        )
    if kind == "short":
        return ShortPlugOperator(
            node=node,
            parent_attr_path="",
            oprt_attr=ShortAttrOperator(
                node_cls=type(node),
                name=long_name,
                long_name=long_name,
                short_name=short_name,
                attr_path=path,
            ),
        )
    return LongPlugOperator(
        node=node,
        parent_attr_path="",
        oprt_attr=LongAttrOperator(
            node_cls=type(node),
            name=long_name,
            long_name=long_name,
            short_name=short_name,
            attr_path=path,
        ),
    )
