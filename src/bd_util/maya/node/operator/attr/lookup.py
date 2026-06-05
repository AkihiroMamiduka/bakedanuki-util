# coding: utf-8
from __future__ import annotations

from typing import Type

from .....maya.attr.query import get_attribute_info
from ._core import AttrOperator
from .std.at.bool import BoolAttrOperator
from .std.at.byte import ByteAttrOperator
from .std.at.char import CharAttrOperator
from .std.at.compound import CompoundAttrOperator
from .std.at.double import DoubleAttrOperator
from .std.at.double2 import Double2AttrOperator
from .std.at.double3 import Double3AttrOperator
from .std.at.double_angle import DoubleAngleAttrOperator
from .std.at.double_linear import DoubleLinearAttrOperator
from .std.at.enum import EnumAttrOperator
from .std.at.float import FloatAttrOperator
from .std.at.float2 import Float2AttrOperator
from .std.at.float3 import Float3AttrOperator
from .std.at.flt_matrix import FltMatrixAttrOperator
from .std.at.long import LongAttrOperator
from .std.at.long2 import Long2AttrOperator
from .std.at.long3 import Long3AttrOperator
from .std.at.matrix import MatrixAttrOperator
from .std.at.message import MessageAttrOperator
from .std.at.reflectance import ReflectanceAttr
from .std.at.short import ShortAttrOperator
from .std.at.short2 import Short2AttrOperator
from .std.at.short3 import Short3AttrOperator
from .std.at.spectrum import SpectrumAttrOperator
from .std.at.time import TimeAttrOperator
from .std.at.typed import TypedAttrOperator
from .std.dt.double2 import DataDouble2AttrOperator
from .std.dt.double3 import DataDouble3AttrOperator
from .std.dt.double_array import DataDoubleArrayAttrOperator
from .std.dt.float2 import DataFloat2AttrOperator
from .std.dt.float3 import DataFloat3AttrOperator
from .std.dt.float_array import DataFloatArrayAttrOperator
from .std.dt.int32_array import DataInt32ArrayAttrOperator
from .std.dt.lattice import DataLatticeAttrOperator
from .std.dt.long2 import DataLong2AttrOperator
from .std.dt.long3 import DataLong3AttrOperator
from .std.dt.matrix import DataMatrixAttrOperator
from .std.dt.mesh import DataMeshAttrOperator
from .std.dt.nurbs_curve import DataNurbsCurveAttrOperator
from .std.dt.nurbs_surface import DataNurbsSurfaceAttrOperator
from .std.dt.point_array import DataPointArrayAttrOperator
from .std.dt.reflectance_rgb import DataReflectanceRGBAttrOperator
from .std.dt.short2 import DataShort2AttrOperator
from .std.dt.short3 import DataShort3AttrOperator
from .std.dt.specrtrum_rgb import DataSpectrumRGBAttrOperator
from .std.dt.string import DataStringAttrOperator
from .std.dt.string_array import DataStringArrayAttrOperator
from .std.dt.vector_array import DataVectorArrayAttrOperator

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
        ReflectanceAttr,
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
