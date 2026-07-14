# coding: utf-8
from __future__ import annotations

from typing import Type

import maya.cmds as cmds

from ....attr.query import get_attribute_info
from ._core import AttrOperator
from .define.std.at.numeric_scalar.bool import BoolAttrOperator
from .define.std.at.numeric_scalar_range.byte import ByteAttrOperator
from .define.std.at.numeric_scalar_range.char import CharAttrOperator
from .define.std.at.compound import CompoundAttrOperator
from .define.std.at.numeric_scalar_range.double import DoubleAttrOperator
from .define.std.at.unit_scalar_range.double_angle import (
    DoubleAngleAttrOperator,
)
from .define.std.at.unit_scalar_range.double_linear import (
    DoubleLinearAttrOperator,
)
from .define.std.at.enum import EnumAttrOperator
from .define.std.at.numeric_scalar_range.float import FloatAttrOperator
from .define.std.at.flt_matrix import FltMatrixAttrOperator
from .define.std.at.numeric_scalar_range.long import LongAttrOperator
from .define.custom.at.scalar_compound.numeric_compound.double_compound.double2_compound.double2 import (
    Double2AttrOperator as NumericDouble2AttrOperator,
)
from .define.custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import (
    Double3AttrOperator as NumericDouble3AttrOperator,
)
from .define.custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.double4 import (
    Double4AttrOperator as NumericDouble4AttrOperator,
)
from .define.custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.quat_compound.quat import (
    Quat4AttrOperator,
)
from .define.custom.at.scalar_compound.numeric_compound.float_compound.float2_compound.float2 import (
    Float2AttrOperator as NumericFloat2AttrOperator,
)
from .define.custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import (
    Float3AttrOperator as NumericFloat3AttrOperator,
)
from .define.custom.at.scalar_compound.numeric_compound.long_compound.long2_compound.long2 import (
    Long2AttrOperator,
)
from .define.custom.at.scalar_compound.numeric_compound.long_compound.long3_compound.long3 import (
    Long3AttrOperator,
)
from .define.custom.at.scalar_compound.unit_compound.angle_compound.double2.double_angle2 import (
    DoubleAngle2AttrOperator,
)
from .define.custom.at.scalar_compound.unit_compound.angle_compound.double3.double_angle3 import (
    DoubleAngle3AttrOperator,
)
from .define.custom.at.scalar_compound.unit_compound.angle_compound.float2.float_angle2 import (
    FloatAngle2AttrOperator,
)
from .define.custom.at.scalar_compound.unit_compound.angle_compound.float3.float_angle3 import (
    FloatAngle3AttrOperator,
)
from .define.custom.at.scalar_compound.unit_compound.linear_compound.double2.double_linear2 import (
    DoubleLinear2AttrOperator,
)
from .define.custom.at.scalar_compound.unit_compound.linear_compound.double3.double_linear3 import (
    DoubleLinear3AttrOperator,
)
from .define.custom.at.scalar_compound.unit_compound.linear_compound.float2.float_linear2 import (
    FloatLinear2AttrOperator,
)
from .define.custom.at.scalar_compound.unit_compound.linear_compound.float3.float_linear3 import (
    FloatLinear3AttrOperator,
)
from .define.std.at.matrix import MatrixAttrOperator
from .define.std.at.message import MessageAttrOperator
from .define.std.at.reflectance import ReflectanceAttrOperator
from .define.std.at.numeric_scalar_range.short import ShortAttrOperator
from .define.custom.at.scalar_compound.numeric_compound.short_compound.short2_compound.short2 import (
    Short2AttrOperator,
)
from .define.custom.at.scalar_compound.numeric_compound.short_compound.short3_compound.short3 import (
    Short3AttrOperator,
)
from .define.std.at.spectrum import SpectrumAttrOperator
from .define.std.at.unit_scalar.time import TimeAttrOperator
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

_AT_CLASS_MAP: dict[str, Type[AttrOperator]] = {
    cls.ATTR_TYPE: cls
    for cls in [
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
    ]
}

_FLOATING_POINT_COMPOUND_ATTR_TYPES = frozenset(
    ["double2", "double3", "double4", "float2", "float3"]
)

_FLOATING_POINT_COMPOUND_CLASS_MAP: dict[
    tuple[str, str, int], Type[AttrOperator]
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
        return cmds.attributeQuery(attr, node=node, longName=True)
    except Exception:
        return attr


def _lookup_floating_point_compound_attr_cls(
    node: str, attr: str, attribute_type: str
) -> Type[AttrOperator]:
    child_attrs = cmds.attributeQuery(attr, node=node, listChildren=True) or []
    if not child_attrs:
        raise TypeError(
            "Unsupported floating point compound attribute: "
            f"{node}.{attr} ({attribute_type}) has no child attributes."
        )

    child_types = []
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


_DT_CLASS_MAP: dict[str, Type[AttrOperator]] = {
    cls.DATA_TYPE: cls
    for cls in [
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
    ]
}


def lookup_attr_cls(node: str, attr: str) -> Type[AttrOperator] | None:
    """
    ノード名とアトリビュート名から、対応する Attr クラスを返す。

    アトリビュートが データ型（typed attribute）の場合は dt 階層の Attr クラスを、
    アトリビュート型の場合は at 階層の Attr クラスを返す。
    対応するクラスが見つからない場合は None を返す。

    Args:
        node (str): ノード名
        attr (str): アトリビュート名

    Returns:
        Type[Attr] | None: 対応する Attr クラス。見つからない場合は None。
    """
    attr_info = get_attribute_info(node, attr)

    if attr_info.data_type is not None:
        return _DT_CLASS_MAP.get(attr_info.data_type)

    if attr_info.attribute_type in _FLOATING_POINT_COMPOUND_ATTR_TYPES:
        return _lookup_floating_point_compound_attr_cls(
            node, attr, attr_info.attribute_type
        )

    return _AT_CLASS_MAP.get(attr_info.attribute_type)
