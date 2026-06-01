# coding: utf-8
from __future__ import annotations

from typing import Type

from .....maya.attr.query import get_attribute_info
from ._core import AttrOperator
from .at.bool import BoolAttr
from .at.byte import ByteAttr
from .at.char import CharAttr
from .at.compound import CompoundAttr
from .at.double import DoubleAttr
from .at.double2 import Double2Attr
from .at.double3 import Double3Attr
from .at.double_angle import DoubleAngleAttr
from .at.double_linear import DoubleLinearAttr
from .at.enum import EnumAttr
from .at.float import FloatAttr
from .at.float2 import Float2Attr
from .at.float3 import Float3Attr
from .at.flt_matrix import FltMatrixAttr
from .at.long import LongAttr
from .at.long2 import Long2Attr
from .at.long3 import Long3Attr
from .at.matrix import MatrixAttr
from .at.message import MessageAttr
from .at.reflectance import ReflectanceAttr
from .at.short import ShortAttr
from .at.short2 import Short2Attr
from .at.short3 import Short3Attr
from .at.spectrum import SpectrumAttr
from .at.time import TimeAttr
from .at.typed import TypedAttr
from .dt.double2 import DataDouble2Attr
from .dt.double3 import DataDouble3Attr
from .dt.double_array import DataDoubleArrayAttr
from .dt.float2 import DataFloat2Attr
from .dt.float3 import DataFloat3Attr
from .dt.float_array import DataFloatArrayAttr
from .dt.int32_array import DataInt32ArrayAttr
from .dt.lattice import DataLatticeAttr
from .dt.long2 import DataLong2Attr
from .dt.long3 import DataLong3Attr
from .dt.matrix import DataMatrixAttr
from .dt.mesh import DataMeshAttr
from .dt.nurbs_curve import DataNurbsCurveAttr
from .dt.nurbs_surface import DataNurbsSurfaceAttr
from .dt.point_array import DataPointArrayAttr
from .dt.reflectance_rgb import DataReflectanceRGBAttr
from .dt.short2 import DataShort2Attr
from .dt.short3 import DataShort3Attr
from .dt.specrtrum_rgb import DataSpectrumRGBAttr
from .dt.string import DataStringAttr
from .dt.string_array import DataStringArrayAttr
from .dt.vector_array import DataVectorArrayAttr

_AT_CLASS_MAP: dict[str, Type[AttrOperator]] = {
    cls.ATTR_TYPE: cls
    for cls in [
        BoolAttr,
        ByteAttr,
        CharAttr,
        CompoundAttr,
        DoubleAttr,
        Double2Attr,
        Double3Attr,
        DoubleAngleAttr,
        DoubleLinearAttr,
        EnumAttr,
        FloatAttr,
        Float2Attr,
        Float3Attr,
        FltMatrixAttr,
        LongAttr,
        Long2Attr,
        Long3Attr,
        MatrixAttr,
        MessageAttr,
        ReflectanceAttr,
        ShortAttr,
        Short2Attr,
        Short3Attr,
        SpectrumAttr,
        TimeAttr,
        TypedAttr,
    ]
}

_DT_CLASS_MAP: dict[str, Type[AttrOperator]] = {
    cls.DATA_TYPE: cls
    for cls in [
        DataDouble2Attr,
        DataDouble3Attr,
        DataDoubleArrayAttr,
        DataFloat2Attr,
        DataFloat3Attr,
        DataFloatArrayAttr,
        DataInt32ArrayAttr,
        DataLatticeAttr,
        DataLong2Attr,
        DataLong3Attr,
        DataMatrixAttr,
        DataMeshAttr,
        DataNurbsCurveAttr,
        DataNurbsSurfaceAttr,
        DataPointArrayAttr,
        DataReflectanceRGBAttr,
        DataShort2Attr,
        DataShort3Attr,
        DataSpectrumRGBAttr,
        DataStringAttr,
        DataStringArrayAttr,
        DataVectorArrayAttr,
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
