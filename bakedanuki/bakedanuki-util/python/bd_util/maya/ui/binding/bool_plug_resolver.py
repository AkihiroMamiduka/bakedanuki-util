# coding: utf-8
"""既存Maya nodeの単一bool attributeを型付きPlugへ解決する。"""

from __future__ import annotations

from typing import cast

from maya.api import OpenMaya as om

from ...node import Nodes
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
    """NodeOperatorに未定義のdynamic bool attributeを型付きPlugへ変換する。"""
    # Maya nodeから指定名のMPlugを直接検索する。
    try:
        m_plug = node.fn_node.findPlug(attribute_name, False)
    except RuntimeError as e:
        raise AttributeError(
            f"Maya node '{node.cmd_access_name}'にattribute "
            f"'{attribute_name}'は存在しません"
        ) from e

    # この入口では最上位の単一attributeだけを扱う。
    if m_plug.isArray or m_plug.isCompound or m_plug.isChild:
        raise TypeError(
            f"Maya attribute '{node.cmd_access_name}.{attribute_name}'には"
            "最上位のscalar boolを指定してください"
        )

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
    long_name = cast(str, attribute_fn.name)
    short_name = cast(str, attribute_fn.shortName)
    attribute_operator = BoolAttrOperator(
        node_cls=type(node),
        name=long_name,
        long_name=long_name,
        short_name=short_name,
        attr_path=long_name,
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
    """既存nodeの最上位scalar boolを長い名前または短い名前で取得する。"""
    node_name = _require_name(node_name, "node_name")
    attribute_name = _require_name(attribute_name, "attribute_name")
    if any(character in attribute_name for character in ".[]"):
        raise ValueError(
            "attribute_nameには最上位の単一attribute名を指定してください"
        )
    # scene上の既存nodeを汎用NodeOperatorとして取得する。
    node = Nodes().existing(node_name)

    # 定義済みattributeはNodeOperatorの型付きアクセスを優先する。
    try:
        plug = node[attribute_name]
    except AttributeError:
        # 追加attributeはMaya APIから型を確認して動的に解決する。
        return _dynamic_bool_plug(node, attribute_name)

    # 定義済みattributeもbool型でなければ同期対象から除外する。
    if not isinstance(plug, BoolPlugOperator):
        return _dynamic_bool_plug(node, attribute_name)
    m_plug = plug.plug
    if m_plug.isArray or m_plug.isCompound or m_plug.isChild:
        raise TypeError("最上位のscalar boolを指定してください")
    return plug
