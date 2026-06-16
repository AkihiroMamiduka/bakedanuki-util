# coding:utf-8
from __future__ import annotations

from typing import ClassVar

from bd_util.maya.node.operator.attr.extra.std.dt.string_array import (
    ExtraDataStringArrayField,
)

# self
#   at
#       std
from .std.at.bool import ExtraBoolField
from .std.at.byte import ExtraByteField
from .std.at.char import ExtraCharField
from .std.at.compound import ExtraCompoundField
from .std.at.double_angle import ExtraDoubleAngleField
from .std.at.double_linear import ExtraDoubleLinearField
from .std.at.double import ExtraDoubleField
from .std.at.double2 import ExtraDouble2Field

# from .std.at.double3 import ExtraDouble3Field
from .std.at.double4 import ExtraDouble4Field
from .std.at.enum import ExtraEnumField
from ..define.std.at.enum import EnumAttrOperator, EnumPlugOperator
from .std.at.float import ExtraFloatField
from .std.at.float2 import ExtraFloat2Field
from .std.at.float3 import ExtraFloat3Field
from .std.at.flt_matrix import ExtraFltMatrixField
from .std.at.generic import ExtraGenericField
from .std.at.light_data import ExtraLightDataField
from .std.at.long_long_int import ExtraLongLongIntField
from .std.at.long import ExtraLongField
from .std.at.long2 import ExtraLong2Field
from .std.at.long3 import ExtraLong3Field
from .std.at.matrix import ExtraMatrixField
from .std.at.message import ExtraMessageField
from .std.at.reflectance import ExtraReflectanceField
from .std.at.short import ExtraShortField
from .std.at.short2 import ExtraShort2Field
from .std.at.short3 import ExtraShort3Field
from .std.at.spectrum import ExtraSpectrumField
from .std.at.time import ExtraTimeField

#       custom
from .custom.double3 import ExtraDouble3Field

#   dt
from .std.dt.double_array import ExtraDataDoubleArrayField
from .std.dt.float_array import ExtraDataFloatArrayField
from .std.dt.int32_array import ExtraDataInt32ArrayField
from .std.dt.lattice import ExtraDataLatticeField
from .std.dt.matrix import ExtraDataMatrixField
from .std.dt.mesh import ExtraDataMeshField
from .std.dt.nurbs_curve import ExtraDataNurbsCurveField
from .std.dt.nurbs_surface import ExtraDataNurbsSurfaceField
from .std.dt.point_array import ExtraDataPointArrayField
from .std.dt.string import ExtraDataStringField
from .std.dt.vector_array import ExtraDataVectorArrayField


# simple
class AddAttrAt:
    """addAttr(attributeType=...) 用フィールド群。"""

    # byte: ClassVar[type[ExtraByteField]] = ExtraByteField
    # char: ClassVar[type[ExtraCharField]] = ExtraCharField
    compound: ClassVar[type[ExtraCompoundField]] = ExtraCompoundField
    # double_angle: ClassVar[type[ExtraDoubleAngleField]] = ExtraDoubleAngleField
    # double_linear: ClassVar[type[ExtraDoubleLinearField]] = (
    #     ExtraDoubleLinearField
    # )
    # double: ClassVar[type[ExtraDoubleField]] = ExtraDoubleField
    double2: ClassVar[type[ExtraDouble2Field]] = ExtraDouble2Field
    # double3: ClassVar[type[ExtraDouble3Field]] = ExtraDouble3Field
    double4: ClassVar[type[ExtraDouble4Field]] = ExtraDouble4Field

    enum: ClassVar[type[ExtraEnumField]] = ExtraEnumField

    # float: ClassVar[type[ExtraFloatField]] = ExtraFloatField
    float2: ClassVar[type[ExtraFloat2Field]] = ExtraFloat2Field
    float3: ClassVar[type[ExtraFloat3Field]] = ExtraFloat3Field
    # flt_matrix: ClassVar[type[ExtraFltMatrixField]] = ExtraFltMatrixField
    # generic: ClassVar[type[ExtraGenericField]] = ExtraGenericField
    light_data: ClassVar[type[ExtraLightDataField]] = ExtraLightDataField
    # long_long_int: ClassVar[type[ExtraLongLongIntField]] = (
    #     ExtraLongLongIntField
    # )
    # long: ClassVar[type[ExtraLongField]] = ExtraLongField
    long2: ClassVar[type[ExtraLong2Field]] = ExtraLong2Field
    long3: ClassVar[type[ExtraLong3Field]] = ExtraLong3Field
    # matrix: ClassVar[type[ExtraMatrixField]] = ExtraMatrixField
    # message: ClassVar[type[ExtraMessageField]] = ExtraMessageField
    reflectance: ClassVar[type[ExtraReflectanceField]] = ExtraReflectanceField
    # short: ClassVar[type[ExtraShortField]] = ExtraShortField
    short2: ClassVar[type[ExtraShort2Field]] = ExtraShort2Field
    short3: ClassVar[type[ExtraShort3Field]] = ExtraShort3Field
    spectrum: ClassVar[type[ExtraSpectrumField]] = ExtraSpectrumField
    # time: ClassVar[type[ExtraTimeField]] = ExtraTimeField

    @classmethod
    def bool(
        cls,
        default_value: bool = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraBoolField:
        return ExtraBoolField(
            default_value=default_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def byte(
        cls,
        default_value: int = None,
        min_value: int = None,
        max_value: int = None,
        soft_min_value: int = None,
        soft_max_value: int = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraByteField:
        return ExtraByteField(
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def char(
        cls,
        default_value: int = None,
        min_value: int = None,
        max_value: int = None,
        soft_min_value: int = None,
        soft_max_value: int = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraCharField:
        return ExtraCharField(
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def double_angle(
        cls,
        default_value: float = None,
        min_value: float = None,
        max_value: float = None,
        soft_min_value: float = None,
        soft_max_value: float = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleAngleField:
        return ExtraDoubleAngleField(
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def double_linear(
        cls,
        default_value: float = None,
        min_value: float = None,
        max_value: float = None,
        soft_min_value: float = None,
        soft_max_value: float = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleLinearField:
        return ExtraDoubleLinearField(
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def double(
        cls,
        default_value: float = None,
        min_value: float = None,
        max_value: float = None,
        soft_min_value: float = None,
        soft_max_value: float = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleField:
        return ExtraDoubleField(
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def double3(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDouble3Field:
        return ExtraDouble3Field(
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def float(
        cls,
        default_value: float = None,
        min_value: float = None,
        max_value: float = None,
        soft_min_value: float = None,
        soft_max_value: float = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatField:
        return ExtraFloatField(
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def flt_matrix(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFltMatrixField:
        return ExtraFltMatrixField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def generic(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraGenericField:
        return ExtraGenericField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def long_long_int(
        cls,
        default_value: int = None,
        soft_min_value: int = None,
        soft_max_value: int = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraLongLongIntField:
        return ExtraLongLongIntField(
            default_value=default_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def long(
        cls,
        default_value: int = None,
        min_value: int = None,
        max_value: int = None,
        soft_min_value: int = None,
        soft_max_value: int = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraLongField:
        return ExtraLongField(
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def matrix(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraMatrixField:
        return ExtraMatrixField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def message(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraMessageField:
        return ExtraMessageField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def short(
        cls,
        default_value: int = None,
        min_value: int = None,
        max_value: int = None,
        soft_min_value: int = None,
        soft_max_value: int = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraShortField:
        return ExtraShortField(
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def time(
        cls,
        default_value: float = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraTimeField:
        return ExtraTimeField(
            default_value=default_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )


class AddAttrDt:
    """addAttr(dataType=...) 用フィールド群。"""

    @classmethod
    def double_array(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataDoubleArrayField:
        return ExtraDataDoubleArrayField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def float_array(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataFloatArrayField:
        return ExtraDataFloatArrayField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def int32_array(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataInt32ArrayField:
        return ExtraDataInt32ArrayField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def lattice(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataLatticeField:
        return ExtraDataLatticeField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def matrix(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataMatrixField:
        return ExtraDataMatrixField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def mesh(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataMeshField:
        return ExtraDataMeshField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def nurbs_curve(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataNurbsCurveField:
        return ExtraDataNurbsCurveField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def nurbs_surface(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataNurbsSurfaceField:
        return ExtraDataNurbsSurfaceField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def point_array(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataPointArrayField:
        return ExtraDataPointArrayField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def string_array(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataStringArrayField:
        return ExtraDataStringArrayField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def string(
        cls,
        default_value: str = None,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataStringField:
        return ExtraDataStringField(
            default_value=default_value,
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )

    @classmethod
    def vector_array(
        cls,
        multi: bool = False,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataVectorArrayField:
        return ExtraDataVectorArrayField(
            multi=multi,
            readable=readable,
            writable=writable,
            category=category,
        )


# define
class DefineEnum:
    field: ClassVar[type[ExtraEnumField]] = ExtraEnumField
    attr_operator: ClassVar[type[EnumAttrOperator]] = EnumAttrOperator
    plug_operator: ClassVar[type[EnumPlugOperator]] = EnumPlugOperator


class DefineAddAttrAt:
    enum: ClassVar[type[DefineEnum]] = DefineEnum


class DefineAddAttr:
    at: ClassVar[DefineAddAttrAt] = DefineAddAttrAt()


# add_attr
class AddAttr:
    """
    Extra Attribute Field の呼び出しハブ。

    使用例:
        class NewNode(NodeOperator):
            testDouble = AddAttr.double(default_value=1.0)
            testMatrix = AddAttr.at.matrix()
            testDataMatrix = AddAttr.dt.matrix()
    """

    at: ClassVar[AddAttrAt] = AddAttrAt()
    dt: ClassVar[AddAttrDt] = AddAttrDt()

    define: ClassVar[DefineAddAttr] = DefineAddAttr()
