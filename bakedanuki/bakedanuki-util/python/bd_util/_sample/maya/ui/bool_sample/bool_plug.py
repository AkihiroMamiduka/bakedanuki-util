# coding: utf-8
"""bool UI sampleで共用する、任意Maya bool plugの指定と解決。"""

from __future__ import annotations

from typing import cast

from maya.api import OpenMaya as om

from ..... import Nodes
from .....maya.node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolAttrOperator,
    BoolPlugOperator,
)
from .....maya.node.operator.node._core import NodeOperator


def _require_optional_name(
    value: object | None, argument_name: str
) -> str | None:
    """任意指定の名前を空でないstrとして検証する。"""
    # 任意引数のNoneは未指定としてそのまま受け入れる。
    if value is None:
        return None

    # 名前が指定された場合は空でないstrだけを受け入れる。
    if not isinstance(value, str):
        raise TypeError(
            f"{argument_name}にはstrまたはNoneを指定してください: "
            f"{type(value).__name__}"
        )
    if not value:
        raise ValueError(f"{argument_name}には空でないstrを指定してください")
    return value


def validate_maya_view_names(
    node_name: object | None,
    attribute_name: object | None,
) -> tuple[str, str] | None:
    """Maya Viewのnode名とattribute名を組として検証する。"""
    # node名とattribute名をそれぞれ任意の名前として検証する。
    node_name = _require_optional_name(node_name, "maya_node_name")
    attribute_name = _require_optional_name(
        attribute_name,
        "maya_attribute_name",
    )

    # Maya Viewはnode名とattribute名の両方が揃った場合だけ有効にする。
    if (node_name is None) != (attribute_name is None):
        raise ValueError(
            "maya_node_nameとmaya_attribute_nameは両方指定してください"
        )
    if node_name is None or attribute_name is None:
        return None
    return node_name, attribute_name


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

    # このsampleが扱う単一bool以外の配列・compoundは拒否する。
    if m_plug.isArray or m_plug.isCompound:
        raise TypeError(
            f"Maya attribute '{node.cmd_access_name}.{attribute_name}'には"
            "scalar boolを指定してください"
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
) -> tuple[NodeOperator, BoolPlugOperator]:
    """任意nodeのscalar bool attributeを型付きPlugとして返す。"""
    # scene上の既存nodeを汎用NodeOperatorとして取得する。
    node = Nodes().existing(node_name)

    # 定義済みattributeはNodeOperatorの型付きアクセスを優先する。
    try:
        plug = node[attribute_name]
    except AttributeError:
        # 追加attributeはMaya APIから型を確認して動的に解決する。
        return node, _dynamic_bool_plug(node, attribute_name)

    # 定義済みattributeもbool型でなければ同期対象から除外する。
    if not isinstance(plug, BoolPlugOperator):
        raise TypeError(
            f"Maya attribute '{node.cmd_access_name}.{attribute_name}'には"
            "boolを指定してください"
        )
    return node, plug
