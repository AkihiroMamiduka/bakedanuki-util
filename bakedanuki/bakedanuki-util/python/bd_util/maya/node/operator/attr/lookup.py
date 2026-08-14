# coding: utf-8
from __future__ import annotations

from typing import Any, Literal, cast

import maya.cmds as cmds

from ....attr.query import get_attribute_info
from ._core import AttrOperator
from .define.custom import (
    Double2AttrOperator as NumericDouble2AttrOperator,
    Double3AttrOperator as NumericDouble3AttrOperator,
    Double4AttrOperator as NumericDouble4AttrOperator,
    DoubleAngle2AttrOperator,
    DoubleAngle3AttrOperator,
    DoubleLinear2AttrOperator,
    DoubleLinear3AttrOperator,
    Float2AttrOperator as NumericFloat2AttrOperator,
    Float3AttrOperator as NumericFloat3AttrOperator,
    FloatAngle2AttrOperator,
    FloatAngle3AttrOperator,
    FloatLinear2AttrOperator,
    FloatLinear3AttrOperator,
    Long2AttrOperator,
    Long3AttrOperator,
    Quat4AttrOperator,
    Short2AttrOperator,
    Short3AttrOperator,
)
from .define.std.at.scalar.numeric.bool import BoolAttrOperator
from .define.std.at.scalar.numeric.range.byte import ByteAttrOperator
from .define.std.at.scalar.numeric.range.char import CharAttrOperator
from .define.std.at.compound import CompoundAttrOperator
from .define.std.at.scalar.numeric.range.double import DoubleAttrOperator
from .define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleAttrOperator,
)
from .define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearAttrOperator,
)
from .define.std.at.scalar.enum import EnumAttrOperator
from .define.std.at.scalar.numeric.range.float import FloatAttrOperator
from .define.std.at.flt_matrix import FltMatrixAttrOperator
from .define.std.at.scalar.numeric.range.long import LongAttrOperator
from .define.std.at.matrix import MatrixAttrOperator
from .define.std.at.message import MessageAttrOperator
from .define.std.at.reflectance import ReflectanceAttrOperator
from .define.std.at.scalar.numeric.range.short import ShortAttrOperator
from .define.std.at.spectrum import SpectrumAttrOperator
from .define.std.at.scalar.unit.time import TimeAttrOperator
from .define.std.at.typed import TypedAttrOperator
from .define.std.dt.double2 import DataDouble2AttrOperator
from .define.std.dt.double3 import DataDouble3AttrOperator
from .define.std.dt.double_array import DataDoubleArrayAttrOperator
from .define.std.dt.float2 import DataFloat2AttrOperator
from .define.std.dt.float3 import DataFloat3AttrOperator
from .define.std.dt.float_array import DataFloatArrayAttrOperator
from .define.std.dt.int32_array import DataInt32ArrayAttrOperator
from .define.std.dt.lattice import DataLatticeAttrOperator
from .define.std.dt.long2 import DataLong2AttrOperator
from .define.std.dt.long3 import DataLong3AttrOperator
from .define.std.dt.matrix import DataMatrixAttrOperator
from .define.std.dt.mesh import DataMeshAttrOperator
from .define.std.dt.nurbs_curve import DataNurbsCurveAttrOperator
from .define.std.dt.nurbs_surface import DataNurbsSurfaceAttrOperator
from .define.std.dt.point_array import DataPointArrayAttrOperator
from .define.std.dt.reflectance_rgb import DataReflectanceRGBAttrOperator
from .define.std.dt.short2 import DataShort2AttrOperator
from .define.std.dt.short3 import DataShort3AttrOperator
from .define.std.dt.specrtrum_rgb import DataSpectrumRGBAttrOperator
from .define.std.dt.string import DataStringAttrOperator
from .define.std.dt.string_array import DataStringArrayAttrOperator
from .define.std.dt.vector_array import DataVectorArrayAttrOperator

_AttrOperatorClass = type[AttrOperator[Any]]


def _build_class_map(
    classes: tuple[_AttrOperatorClass, ...],
    type_attribute: Literal["ATTR_TYPE", "DATA_TYPE"],
) -> dict[str, _AttrOperatorClass]:
    class_map: dict[str, _AttrOperatorClass] = {}
    for attr_cls in classes:
        type_name = (
            attr_cls.ATTR_TYPE
            if type_attribute == "ATTR_TYPE"
            else attr_cls.DATA_TYPE
        )
        if type_name is None:
            raise TypeError(
                f"{attr_cls.__name__}.{type_attribute} must be defined."
            )
        class_map[type_name] = attr_cls
    return class_map


_AT_CLASS_MAP = _build_class_map(
    (
        BoolAttrOperator,
        ByteAttrOperator,
        CharAttrOperator,
        CompoundAttrOperator,
        DoubleAttrOperator,
        DoubleAngleAttrOperator,
        DoubleLinearAttrOperator,
        EnumAttrOperator,
        FloatAttrOperator,
        FltMatrixAttrOperator,
        LongAttrOperator,
        Long2AttrOperator,
        Long3AttrOperator,
        MatrixAttrOperator,
        MessageAttrOperator,
        ReflectanceAttrOperator,
        ShortAttrOperator,
        Short2AttrOperator,
        Short3AttrOperator,
        SpectrumAttrOperator,
        TimeAttrOperator,
        TypedAttrOperator,
    ),
    "ATTR_TYPE",
)

_FLOATING_POINT_COMPOUND_ATTR_TYPES = frozenset(
    ["double2", "double3", "double4", "float2", "float3"]
)

_FLOATING_POINT_COMPOUND_CLASS_MAP: dict[
    tuple[str, str, int], _AttrOperatorClass
] = {
    ("double2", "double", 2): NumericDouble2AttrOperator,
    ("double2", "doubleLinear", 2): DoubleLinear2AttrOperator,
    ("double2", "doubleAngle", 2): DoubleAngle2AttrOperator,
    ("double3", "double", 3): NumericDouble3AttrOperator,
    ("double3", "doubleLinear", 3): DoubleLinear3AttrOperator,
    ("double3", "doubleAngle", 3): DoubleAngle3AttrOperator,
    ("double4", "double", 4): NumericDouble4AttrOperator,
    ("float2", "float", 2): NumericFloat2AttrOperator,
    ("float2", "doubleLinear", 2): FloatLinear2AttrOperator,
    ("float2", "floatLinear", 2): FloatLinear2AttrOperator,
    ("float2", "doubleAngle", 2): FloatAngle2AttrOperator,
    ("float2", "floatAngle", 2): FloatAngle2AttrOperator,
    ("float3", "float", 3): NumericFloat3AttrOperator,
    ("float3", "doubleLinear", 3): FloatLinear3AttrOperator,
    ("float3", "floatLinear", 3): FloatLinear3AttrOperator,
    ("float3", "doubleAngle", 3): FloatAngle3AttrOperator,
    ("float3", "floatAngle", 3): FloatAngle3AttrOperator,
}


def _get_attr_long_name(node: str, attr: str) -> str:
    try:
        return cast(str, cmds.attributeQuery(attr, node=node, longName=True))
    except Exception:
        return attr


def _lookup_floating_point_compound_attr_cls(
    node: str, attr: str, attribute_type: str
) -> _AttrOperatorClass:
    child_attrs = (
        cast(
            list[str] | None,
            cmds.attributeQuery(attr, node=node, listChildren=True),
        )
        or []
    )
    if not child_attrs:
        raise TypeError(
            "Unsupported floating point compound attribute: "
            f"{node}.{attr} ({attribute_type}) has no child attributes."
        )

    child_types: list[str] = []
    for child_attr in child_attrs:
        child_info = get_attribute_info(node, child_attr)
        if child_info.attribute_type is None:
            raise TypeError(
                "Unsupported floating point compound child attribute: "
                f"{node}.{child_attr} has no attribute type."
            )
        child_types.append(child_info.attribute_type)

    first_child_type = child_types[0]
    if any(child_type != first_child_type for child_type in child_types):
        raise TypeError(
            "Unsupported mixed floating point compound child types: "
            f"{node}.{attr} ({attribute_type}) -> {child_types}"
        )

    key = (attribute_type, first_child_type, len(child_types))
    attr_cls = _FLOATING_POINT_COMPOUND_CLASS_MAP.get(key)
    if attr_cls is None:
        raise TypeError(
            "Unsupported floating point compound attribute: "
            f"{node}.{attr} -> {key}"
        )

    attr_long_name = _get_attr_long_name(node, attr)
    if key == ("double4", "double", 4) and "quat" in attr_long_name.lower():
        return Quat4AttrOperator

    return attr_cls


_DT_CLASS_MAP = _build_class_map(
    (
        DataDouble2AttrOperator,
        DataDouble3AttrOperator,
        DataDoubleArrayAttrOperator,
        DataFloat2AttrOperator,
        DataFloat3AttrOperator,
        DataFloatArrayAttrOperator,
        DataInt32ArrayAttrOperator,
        DataLatticeAttrOperator,
        DataLong2AttrOperator,
        DataLong3AttrOperator,
        DataMatrixAttrOperator,
        DataMeshAttrOperator,
        DataNurbsCurveAttrOperator,
        DataNurbsSurfaceAttrOperator,
        DataPointArrayAttrOperator,
        DataReflectanceRGBAttrOperator,
        DataShort2AttrOperator,
        DataShort3AttrOperator,
        DataSpectrumRGBAttrOperator,
        DataStringAttrOperator,
        DataStringArrayAttrOperator,
        DataVectorArrayAttrOperator,
    ),
    "DATA_TYPE",
)


def lookup_attr_cls(node: str, attr: str) -> _AttrOperatorClass | None:
    """
    ノード名とアトリビュート名から、対応する Attr クラスを返す。

    アトリビュートが データ型（typed attribute）の場合は dt 階層の Attr クラスを、
    アトリビュート型の場合は at 階層の Attr クラスを返す。
    対応するクラスが見つからない場合は None を返す。

    Args:
        node (str): ノード名
        attr (str): アトリビュート名

    Returns:
        type[AttrOperator[Any]] | None: 対応する Attr クラス。
            見つからない場合は None。
    """
    attr_info = get_attribute_info(node, attr)

    if attr_info.data_type is not None:
        return _DT_CLASS_MAP.get(attr_info.data_type)

    if attr_info.attribute_type in _FLOATING_POINT_COMPOUND_ATTR_TYPES:
        return _lookup_floating_point_compound_attr_cls(
            node, attr, attr_info.attribute_type
        )

    if attr_info.attribute_type is None:
        return None
    return _AT_CLASS_MAP.get(attr_info.attribute_type)
