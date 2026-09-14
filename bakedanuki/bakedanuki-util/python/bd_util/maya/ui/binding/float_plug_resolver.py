# coding: utf-8
from __future__ import annotations

from typing import Literal, TypeAlias, cast

from maya.api import OpenMaya as om

from ...node import Nodes
from ...node.operator.attr.define.std.at.scalar.numeric.range.double import (
    DoubleAttrOperator,
    DoublePlugOperator,
)
from ...node.operator.attr.define.std.at.scalar.numeric.range.float import (
    FloatAttrOperator,
    FloatPlugOperator,
)
from ...node.operator.attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleAttrOperator,
    DoubleAnglePlugOperator,
)
from ...node.operator.attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearAttrOperator,
    DoubleLinearPlugOperator,
)
from ...node.operator.attr.define.std.at.scalar.unit.range.float_angle import (
    FloatAnglePlugOperator,
)
from ...node.operator.attr.define.std.at.scalar.unit.range.float_linear import (
    FloatLinearPlugOperator,
)

MayaFloatPlug: TypeAlias = (
    DoublePlugOperator
    | FloatPlugOperator
    | DoubleLinearPlugOperator
    | DoubleAnglePlugOperator
    | FloatLinearPlugOperator
    | FloatAnglePlugOperator
)
FloatPlugKind: TypeAlias = Literal["number", "distance", "angle"]


def float_plug_kind(plug: om.MPlug) -> FloatPlugKind:
    """配列配下を除くscalar float/double・距離・角度だけを受け付ける。"""
    if plug.isCompound:
        raise TypeError("plugには単一の浮動小数点属性を指定してください")
    ancestor = plug
    while True:
        if ancestor.isArray or ancestor.isElement:
            raise TypeError("配列配下のplugには対応していません")
        if not ancestor.isChild:
            break
        ancestor = ancestor.parent()
    attribute = plug.attribute()
    if attribute.hasFn(om.MFn.kUnitAttribute):
        unit_type = om.MFnUnitAttribute(attribute).unitType()
        if unit_type == om.MFnUnitAttribute.kDistance:
            return "distance"
        if unit_type == om.MFnUnitAttribute.kAngle:
            return "angle"
    elif attribute.hasFn(om.MFn.kNumericAttribute):
        if om.MFnNumericAttribute(attribute).numericType() in (
            om.MFnNumericData.kFloat,
            om.MFnNumericData.kDouble,
        ):
            return "number"
    raise TypeError("plugにはfloat/double・距離・角度属性を指定してください")


def require_float_plug(value: object) -> MayaFloatPlug:
    if not isinstance(
        value,
        (
            DoublePlugOperator,
            FloatPlugOperator,
            DoubleLinearPlugOperator,
            DoubleAnglePlugOperator,
            FloatLinearPlugOperator,
            FloatAnglePlugOperator,
        ),
    ):
        raise TypeError("plugには浮動小数点用PlugOperatorを指定してください")
    float_plug_kind(value.plug)
    return value


def resolve_float_plug(node_name: str, attribute_name: str) -> MayaFloatPlug:
    """既存scalar属性を長名・短名・compoundの子の名前から解決する。"""
    node_name = _require_name(node_name, "node_name")
    attribute_name = _require_name(attribute_name, "attribute_name")
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
    kind = float_plug_kind(plug)
    attribute = om.MFnAttribute(plug.attribute())
    long_name = cast(str, attribute.name)
    short_name = cast(str, attribute.shortName)
    path = cast(
        str,
        plug.partialName(
            includeNodeName=False,
            useFullAttributePath=True,
            useLongNames=True,
        ),
    )
    if kind == "distance":
        return DoubleLinearPlugOperator(
            node=node,
            parent_attr_path="",
            oprt_attr=DoubleLinearAttrOperator(
                node_cls=type(node),
                name=long_name,
                long_name=long_name,
                short_name=short_name,
                attr_path=path,
            ),
        )
    if kind == "angle":
        return DoubleAnglePlugOperator(
            node=node,
            parent_attr_path="",
            oprt_attr=DoubleAngleAttrOperator(
                node_cls=type(node),
                name=long_name,
                long_name=long_name,
                short_name=short_name,
                attr_path=path,
            ),
        )
    if (
        om.MFnNumericAttribute(plug.attribute()).numericType()
        == om.MFnNumericData.kFloat
    ):
        return FloatPlugOperator(
            node=node,
            parent_attr_path="",
            oprt_attr=FloatAttrOperator(
                node_cls=type(node),
                name=long_name,
                long_name=long_name,
                short_name=short_name,
                attr_path=path,
            ),
        )
    return DoublePlugOperator(
        node=node,
        parent_attr_path="",
        oprt_attr=DoubleAttrOperator(
            node_cls=type(node),
            name=long_name,
            long_name=long_name,
            short_name=short_name,
            attr_path=path,
        ),
    )


def _require_name(value: object, argument_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{argument_name}にはstrを指定してください")
    if not value:
        raise ValueError(f"{argument_name}には空でない名前を指定してください")
    return value
