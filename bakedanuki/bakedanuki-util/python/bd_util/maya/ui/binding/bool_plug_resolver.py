# coding: utf-8
"""既存Maya nodeの単一bool attributeを型付きPlugへ解決する。"""

from __future__ import annotations

from typing import cast

from maya.api import OpenMaya as om

from ...node import Nodes
from ...node._attribute_lookup import attribute_path, find_attribute_plug
from ...node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolAttrOperator,
    BoolPlugOperator,
)
from ...node.operator.node._core import NodeOperator


def _require_name(value: object, argument_name: str) -> str:
    """空でない名前を検証する。"""
    if not isinstance(value, str):
        raise TypeError(
            f"{argument_name}にはstrを指定してください: "
            f"{type(value).__name__}"
        )
    if not value:
        raise ValueError(f"{argument_name}には空でないstrを指定してください")
    return value


def _dynamic_bool_plug(
    node: NodeOperator,
    attribute_name: str,
) -> BoolPlugOperator:
    """既存bool属性を親pathを維持した型付きPlugへ変換する。"""
    # 名前が重複するcompound子は完全なpathでのみ解決する
    try:
        m_plug = find_attribute_plug(node.fn_node, attribute_name)
    except AttributeError as e:
        raise AttributeError(
            f"Maya node '{node.cmd_access_name}'にattribute "
            f"'{attribute_name}'は存在しません"
        ) from e

    # 配列に属さないscalarならcompoundの子も受け入れる
    if m_plug.isCompound:
        raise TypeError(
            f"Maya attribute '{node.cmd_access_name}.{attribute_name}'には"
            "scalar boolを指定してください"
        )
    ancestor = m_plug
    while True:
        if ancestor.isArray or ancestor.isElement:
            raise TypeError("配列配下のplugには対応していません")
        if not ancestor.isChild:
            break
        ancestor = ancestor.parent()

    # numeric attributeの中でもboolean型だけを同期対象として受け入れる。
    attribute = m_plug.attribute()
    if not attribute.hasFn(om.MFn.kNumericAttribute):
        raise TypeError(
            f"Maya attribute '{node.cmd_access_name}.{attribute_name}'には"
            "boolを指定してください"
        )
    numeric_attribute = om.MFnNumericAttribute(attribute)
    if numeric_attribute.numericType() != om.MFnNumericData.kBoolean:
        raise TypeError(
            f"Maya attribute '{node.cmd_access_name}.{attribute_name}'には"
            "boolを指定してください"
        )

    # 動的attributeの正式名から型付きBoolPlugOperatorを組み立てる。
    attribute_fn = om.MFnAttribute(attribute)
    path = attribute_path(m_plug)
    long_name = (
        cast(str, attribute_fn.name)
        if attribute_fn.enforcingUniqueName
        else path
    )
    short_name = cast(str, attribute_fn.shortName)
    attribute_operator = BoolAttrOperator(
        node_cls=type(node),
        name=long_name,
        long_name=long_name,
        short_name=short_name,
        attr_path=path,
    )
    return BoolPlugOperator(
        node=node,
        oprt_attr=attribute_operator,
        parent_attr_path="",
    )


def resolve_bool_plug(
    node_name: str,
    attribute_name: str,
) -> BoolPlugOperator:
    """既存scalar boolを長名・短名・compoundの相対pathで取得する。"""
    node_name = _require_name(node_name, "node_name")
    attribute_name = _require_name(attribute_name, "attribute_name")
    if any(character in attribute_name for character in "[]"):
        raise ValueError(
            "attribute_nameには単一の属性名か相対pathを指定してください"
        )
    # scene上の既存nodeを汎用NodeOperatorとして取得する。
    node = Nodes().existing(node_name)

    return _dynamic_bool_plug(node, attribute_name)
