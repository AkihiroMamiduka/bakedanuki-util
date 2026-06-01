# coding: utf-8
from __future__ import annotations

from typing import Type

from .....maya.attr.query import get_attribute_info
from ._core import AttrOperator
from .at.bool import BoolAttrOperator
from .at.byte import ByteAttrOperator
from .at.char import CharAttrOperator
from .at.compound import CompoundAttrOperator
from .at.double import DoubleAttrOperator
from .at.double2 import Double2AttrOperator
from .at.double3 import Double3AttrOperator
from .at.double_angle import DoubleAngleAttrOperator
from .at.double_linear import DoubleLinearAttrOperator
from .at.enum import EnumAttrOperator
from .at.float import FloatAttrOperator
from .at.float2 import Float2AttrOperator
from .at.float3 import Float3AttrOperator
from .at.flt_matrix import FltMatrixAttrOperator
from .at.long import LongAttrOperator
from .at.long2 import Long2AttrOperator
from .at.long3 import Long3AttrOperator
from .at.matrix import MatrixAttrOperator
from .at.message import MessageAttrOperator
from .at.reflectance import ReflectanceAttr
from .at.short import ShortAttrOperator
from .at.short2 import Short2AttrOperator
from .at.short3 import Short3AttrOperator
from .at.spectrum import SpectrumAttrOperator
from .at.time import TimeAttrOperator
from .at.typed import TypedAttrOperator
from .dt.double2 import DataDouble2AttrOperator
from .dt.double3 import DataDouble3AttrOperator
from .dt.double_array import DataDoubleArrayAttrOperator
from .dt.float2 import DataFloat2AttrOperator
from .dt.float3 import DataFloat3AttrOperator
from .dt.float_array import DataFloatArrayAttrOperator
from .dt.int32_array import DataInt32ArrayAttrOperator
from .dt.lattice import DataLatticeAttrOperator
from .dt.long2 import DataLong2AttrOperator
from .dt.long3 import DataLong3AttrOperator
from .dt.matrix import DataMatrixAttrOperator
from .dt.mesh import DataMeshAttrOperator
from .dt.nurbs_curve import DataNurbsCurveAttrOperator
from .dt.nurbs_surface import DataNurbsSurfaceAttrOperator
from .dt.point_array import DataPointArrayAttrOperator
from .dt.reflectance_rgb import DataReflectanceRGBAttrOperator
from .dt.short2 import DataShort2AttrOperator
from .dt.short3 import DataShort3AttrOperator
from .dt.specrtrum_rgb import DataSpectrumRGBAttrOperator
from .dt.string import DataStringAttrOperator
from .dt.string_array import DataStringArrayAttrOperator
from .dt.vector_array import DataVectorArrayAttrOperator

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
