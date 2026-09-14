# coding: utf-8
from dataclasses import dataclass
from typing import Protocol, cast

from maya.api import OpenMaya as om

from ...node import Nodes
from ...node.operator.node._core import NodeOperator
from .float_plug_resolver import float_plug_kind


class MayaFloat3Plug(Protocol):
    """既存PlugOperatorと名前解決結果に共通する3成分plugの境界。"""

    @property
    def node(self) -> NodeOperator:
        """対象nodeのOperatorを返す。"""
        raise NotImplementedError

    @property
    def plug(self) -> om.MPlug:
        """3成分の親MPlugを返す。"""
        raise NotImplementedError


@dataclass(frozen=True)
class _ResolvedFloat3Plug:
    """既存nodeと解決済み親plugを保持する読み取り専用の参照。"""

    node: NodeOperator
    plug: om.MPlug


def require_float3_plug(value: object) -> MayaFloat3Plug:
    """配列配下を除く、同種の数値3成分を持つ親plugだけを受け付ける。"""
    plug: object = getattr(value, "plug", None)
    node: object = getattr(value, "node", None)
    if not isinstance(plug, om.MPlug) or not isinstance(node, NodeOperator):
        raise TypeError(
            "plugには3成分のPlugOperatorまたは名前解決結果を指定してください"
        )
    # 配列本体へchild()を呼ばず、親を含めて配列配下を先に除外する。
    ancestor = plug
    while True:
        if ancestor.isArray or ancestor.isElement:
            raise TypeError("配列配下のplugには対応していません")
        if not ancestor.isChild:
            break
        ancestor = ancestor.parent()
    if not plug.isCompound or plug.numChildren() != 3:
        raise TypeError("plugには3成分のnumeric compoundを指定してください")
    attribute = plug.attribute()
    if not attribute.hasFn(om.MFn.kNumericAttribute):
        raise TypeError("汎用compoundやtyped dataには対応していません")
    numeric_type = om.MFnNumericAttribute(attribute).numericType()
    if numeric_type not in (
        om.MFnNumericData.k3Double,
        om.MFnNumericData.k3Float,
    ):
        raise TypeError("plugにはdouble3またはfloat3を指定してください")

    # 各子の実型と祖先の配列構造をscalar側と同じ境界で検証する。
    kinds = tuple(float_plug_kind(plug.child(index)) for index in range(3))
    if len(set(kinds)) != 1:
        raise TypeError("3成分の単位種別は一致している必要があります")
    return cast(MayaFloat3Plug, value)


def resolve_float3_plug(node_name: str, attribute_name: str) -> MayaFloat3Plug:
    """既存3成分属性を長名・短名から解決し、構成を検証する。"""
    node_name = _require_name(node_name)
    attribute_name = _require_name(attribute_name)
    if any(character in attribute_name for character in ".[]"):
        raise ValueError(
            "attribute_nameには属性パスではなく単一の属性名を指定してください"
        )
    node = Nodes().existing(node_name)
    try:
        plug = node.fn_node.findPlug(attribute_name, False)
    except RuntimeError as error:
        raise AttributeError(
            f"属性が見つかりません: {node_name}.{attribute_name}"
        ) from error
    return require_float3_plug(_ResolvedFloat3Plug(node, plug))


def _require_name(value: object) -> str:
    """node名・属性名として空でない文字列を検証する。"""
    if not isinstance(value, str):
        raise TypeError("node名と属性名にはstrを指定してください")
    if not value:
        raise ValueError("node名と属性名には空でない名前を指定してください")
    return value
