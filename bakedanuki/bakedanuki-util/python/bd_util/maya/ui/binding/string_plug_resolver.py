# coding: utf-8
from __future__ import annotations

from typing import cast

from maya.api import OpenMaya as om

from ...node import Nodes
from ...node._attribute_lookup import attribute_path, find_attribute_plug
from ...node.operator.attr.define.std.dt.string import (
    DataStringAttrOperator,
    DataStringPlugOperator,
)

MayaStringPlug = DataStringPlugOperator


def _require_scalar_string(plug: om.MPlug) -> None:
    """配列配下ではない単一のtyped string属性を検証する。"""
    attribute = plug.attribute()
    if (
        plug.isCompound
        or not attribute.hasFn(om.MFn.kTypedAttribute)
        or om.MFnTypedAttribute(attribute).attrType() != om.MFnData.kString
    ):
        raise TypeError("plugには単一のstring属性を指定してください")
    ancestor = plug
    while True:
        if ancestor.isArray or ancestor.isElement:
            raise TypeError("配列配下のplugには対応していません")
        if not ancestor.isChild:
            break
        ancestor = ancestor.parent()


def require_string_plug(value: object) -> MayaStringPlug:
    """型付きの単一string PlugOperatorを検証する。"""
    if not isinstance(value, DataStringPlugOperator):
        raise TypeError("plugにはDataStringPlugOperatorを指定してください")
    _require_scalar_string(value.plug)
    return value


def _require_name(value: object, argument_name: str) -> str:
    """既存nodeと属性の検索に使う非空名を検証する。"""
    if not isinstance(value, str):
        raise TypeError(f"{argument_name}にはstrを指定してください")
    if not value:
        raise ValueError(f"{argument_name}には空でない名前を指定してください")
    return value


def resolve_string_plug(node_name: str, attribute_name: str) -> MayaStringPlug:
    """既存の単一string属性を長名・短名・相対pathから解決する。"""
    node_name = _require_name(node_name, "node_name")
    attribute_name = _require_name(attribute_name, "attribute_name")
    if any(character in attribute_name for character in "[]"):
        raise ValueError("配列要素のpathには対応していません")
    node = Nodes().existing(node_name)
    try:
        plug = find_attribute_plug(node.fn_node, attribute_name)
    except AttributeError as error:
        raise AttributeError(
            f"属性が見つかりません: {node_name}.{attribute_name}"
        ) from error
    _require_scalar_string(plug)
    attribute = om.MFnAttribute(plug.attribute())
    path = attribute_path(plug)
    name = cast(str, attribute.name) if attribute.enforcingUniqueName else path
    operator = DataStringAttrOperator(
        node_cls=type(node),
        name=name,
        long_name=name,
        short_name=cast(str, attribute.shortName),
        attr_path=path,
    )
    return DataStringPlugOperator(
        node=node, oprt_attr=operator, parent_attr_path=""
    )
