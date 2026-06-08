# coding: utf-8
from __future__ import annotations

from typing import Type

from .....maya.attr.query import get_attribute_info
from ._core import AttrOperator
from .define.std.at.bool import BoolAttrOperator
from .define.std.at.byte import ByteAttrOperator
from .define.std.at.char import CharAttrOperator
from .define.std.at.compound import CompoundAttrOperator
from .define.std.at.double import DoubleAttrOperator
from .define.std.at.double2 import Double2AttrOperator
from .define.std.at.double3 import Double3AttrOperator
from .define.std.at.double_angle import DoubleAngleAttrOperator
from .define.std.at.double_linear import DoubleLinearAttrOperator
from .define.std.at.enum import EnumAttrOperator
from .define.std.at.float import FloatAttrOperator
from .define.std.at.float2 import Float2AttrOperator
from .define.std.at.float3 import Float3AttrOperator
from .define.std.at.flt_matrix import FltMatrixAttrOperator
from .define.std.at.long import LongAttrOperator
from .define.std.at.long2 import Long2AttrOperator
from .define.std.at.long3 import Long3AttrOperator
from .define.std.at.matrix import MatrixAttrOperator
from .define.std.at.message import MessageAttrOperator
from .define.std.at.reflectance import ReflectanceAttrOperator
from .define.std.at.short import ShortAttrOperator
from .define.std.at.short2 import Short2AttrOperator
from .define.std.at.short3 import Short3AttrOperator
from .define.std.at.spectrum import SpectrumAttrOperator
from .define.std.at.time import TimeAttrOperator
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
        Double2AttrOperator,
        Double3AttrOperator,
        DoubleAngleAttrOperator,
        DoubleLinearAttrOperator,
        EnumAttrOperator,
        FloatAttrOperator,
        Float2AttrOperator,
        Float3AttrOperator,
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
    else:
        return _AT_CLASS_MAP.get(attr_info.attribute_type)
