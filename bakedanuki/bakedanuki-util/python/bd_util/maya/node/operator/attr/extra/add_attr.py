# coding:utf-8
from __future__ import annotations

from typing import ClassVar

# self
#   difine
#       at
#           std
from ..define.std.at.scalar.enum import EnumPlugOperator
from ..define.std.at.compound import CompoundPlugOperator

#   extra
#      at
#           std
from .std.at.bool import ExtraBoolField
from .std.at.byte import ExtraByteField
from .std.at.char import ExtraCharField
from .std.at.compound import ExtraCompoundField
from .std.at.double_angle import ExtraDoubleAngleField
from .std.at.double_linear import ExtraDoubleLinearField
from .std.at.double import ExtraDoubleField
from .std.at.enum import ExtraEnumField
from .std.at.float_angle import ExtraFloatAngleField
from .std.at.float_linear import ExtraFloatLinearField
from .std.at.float import ExtraFloatField
from .std.at.flt_matrix import ExtraFltMatrixField
from .std.at.generic import ExtraGenericField
from .std.at.long_long_int import ExtraLongLongIntField
from .std.at.long import ExtraLongField
from .std.at.matrix import ExtraMatrixField
from .std.at.message import ExtraMessageField
from .std.at.short import ExtraShortField
from .std.at.time import ExtraTimeField

#          custom
from .custom.double2 import ExtraDouble2Field
from .custom.double3 import ExtraDouble3Field
from .custom.double4 import ExtraDouble4Field
from .custom.quat import ExtraQuat4Field
from .custom.double_linear2 import ExtraDoubleLinear2Field
from .custom.double_linear3 import ExtraDoubleLinear3Field
from .custom.double_angle2 import ExtraDoubleAngle2Field
from .custom.double_angle3 import ExtraDoubleAngle3Field
from .custom.float2 import ExtraFloat2Field
from .custom.float3 import ExtraFloat3Field
from .custom.float_linear2 import ExtraFloatLinear2Field
from .custom.float_linear3 import ExtraFloatLinear3Field
from .custom.float_angle2 import ExtraFloatAngle2Field
from .custom.float_angle3 import ExtraFloatAngle3Field
from .custom.long2 import ExtraLong2Field
from .custom.long3 import ExtraLong3Field
from .custom.short2 import ExtraShort2Field
from .custom.short3 import ExtraShort3Field

#       dt
from .std.dt.double_array import ExtraDataDoubleArrayField
from .std.dt.float_array import ExtraDataFloatArrayField
from .std.dt.int32_array import ExtraDataInt32ArrayField
from .std.dt.lattice import ExtraDataLatticeField
from .std.dt.matrix import ExtraDataMatrixField
from .std.dt.mesh import ExtraDataMeshField
from .std.dt.nurbs_curve import ExtraDataNurbsCurveField
from .std.dt.nurbs_surface import ExtraDataNurbsSurfaceField
from .std.dt.point_array import ExtraDataPointArrayField
from .std.dt.string_array import ExtraDataStringArrayField
from .std.dt.string import ExtraDataStringField
from .std.dt.vector_array import ExtraDataVectorArrayField

_UNSET = object()


def _field_kwargs(
    *,
    long_name: str | None = None,
    short_name: str | None = None,
    default_value=_UNSET,
    min_value=_UNSET,
    max_value=_UNSET,
    soft_min_value=_UNSET,
    soft_max_value=_UNSET,
    multi: bool = False,
    readable: bool | None = None,
    writable: bool | None = None,
    category: str | None = None,
):
    kwargs = {
        "long_name": long_name,
        "short_name": short_name,
        "multi": multi,
        "readable": readable,
        "writable": writable,
        "category": category,
    }
    if default_value is not _UNSET:
        kwargs["default_value"] = default_value
    if min_value is not _UNSET:
        kwargs["min_value"] = min_value
    if max_value is not _UNSET:
        kwargs["max_value"] = max_value
    if soft_min_value is not _UNSET:
        kwargs["soft_min_value"] = soft_min_value
    if soft_max_value is not _UNSET:
        kwargs["soft_max_value"] = soft_max_value
    return kwargs


# simple
class AddAttrAt:
    """addAttr(attributeType=...) 用フィールド群。"""

    @classmethod
    def bool(
        cls,
        default_value: bool = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraBoolField:
        return ExtraBoolField(
            **_field_kwargs(
                default_value=default_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
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
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraByteField:
        return ExtraByteField(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
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
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraCharField:
        return ExtraCharField(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
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
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleAngleField:
        return ExtraDoubleAngleField(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
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
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleLinearField:
        return ExtraDoubleLinearField(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
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
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleField:
        return ExtraDoubleField(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def double2(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDouble2Field:
        return ExtraDouble2Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
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
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDouble3Field:
        return ExtraDouble3Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def double4(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDouble4Field:
        return ExtraDouble4Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def quat(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraQuat4Field:
        return ExtraQuat4Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def double_linear2(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleLinear2Field:
        return ExtraDoubleLinear2Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def double_linear3(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleLinear3Field:
        return ExtraDoubleLinear3Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def double_angle2(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleAngle2Field:
        return ExtraDoubleAngle2Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def double_angle3(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleAngle3Field:
        return ExtraDoubleAngle3Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def float_angle(
        cls,
        default_value: float = None,
        min_value: float = None,
        max_value: float = None,
        soft_min_value: float = None,
        soft_max_value: float = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatAngleField:
        return ExtraFloatAngleField(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def float_linear(
        cls,
        default_value: float = None,
        min_value: float = None,
        max_value: float = None,
        soft_min_value: float = None,
        soft_max_value: float = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatLinearField:
        return ExtraFloatLinearField(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
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
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatField:
        return ExtraFloatField(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def float2(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloat2Field:
        return ExtraFloat2Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def float3(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloat3Field:
        return ExtraFloat3Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def float_linear2(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatLinear2Field:
        return ExtraFloatLinear2Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def float_linear3(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatLinear3Field:
        return ExtraFloatLinear3Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def float_angle2(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatAngle2Field:
        return ExtraFloatAngle2Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def float_angle3(
        cls,
        default_value: list[float] = None,
        min_value: float | list[float] = None,
        max_value: float | list[float] = None,
        soft_min_value: float | list[float] = None,
        soft_max_value: float | list[float] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatAngle3Field:
        return ExtraFloatAngle3Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def flt_matrix(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFltMatrixField:
        return ExtraFltMatrixField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def generic(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraGenericField:
        return ExtraGenericField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def long_long_int(
        cls,
        default_value: int = None,
        soft_min_value: int = None,
        soft_max_value: int = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraLongLongIntField:
        return ExtraLongLongIntField(
            **_field_kwargs(
                default_value=default_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
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
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraLongField:
        return ExtraLongField(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def long2(
        cls,
        default_value: list[int] = None,
        min_value: int | list[int] = None,
        max_value: int | list[int] = None,
        soft_min_value: int | list[int] = None,
        soft_max_value: int | list[int] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraLong2Field:
        return ExtraLong2Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def long3(
        cls,
        default_value: list[int] = None,
        min_value: int | list[int] = None,
        max_value: int | list[int] = None,
        soft_min_value: int | list[int] = None,
        soft_max_value: int | list[int] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraLong3Field:
        return ExtraLong3Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def matrix(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraMatrixField:
        return ExtraMatrixField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def message(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraMessageField:
        return ExtraMessageField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
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
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraShortField:
        return ExtraShortField(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def short2(
        cls,
        default_value: list[int] = None,
        min_value: int | list[int] = None,
        max_value: int | list[int] = None,
        soft_min_value: int | list[int] = None,
        soft_max_value: int | list[int] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraShort2Field:
        return ExtraShort2Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def short3(
        cls,
        default_value: list[int] = None,
        min_value: int | list[int] = None,
        max_value: int | list[int] = None,
        soft_min_value: int | list[int] = None,
        soft_max_value: int | list[int] = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraShort3Field:
        return ExtraShort3Field(
            **_field_kwargs(
                default_value=default_value,
                min_value=min_value,
                max_value=max_value,
                soft_min_value=soft_min_value,
                soft_max_value=soft_max_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def time(
        cls,
        default_value: float = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraTimeField:
        return ExtraTimeField(
            **_field_kwargs(
                default_value=default_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )


class AddAttrDt:
    """addAttr(dataType=...) 用フィールド群。"""

    @classmethod
    def double_array(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataDoubleArrayField:
        return ExtraDataDoubleArrayField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def float_array(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataFloatArrayField:
        return ExtraDataFloatArrayField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def int32_array(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataInt32ArrayField:
        return ExtraDataInt32ArrayField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def lattice(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataLatticeField:
        return ExtraDataLatticeField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def matrix(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataMatrixField:
        return ExtraDataMatrixField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def mesh(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataMeshField:
        return ExtraDataMeshField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def nurbs_curve(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataNurbsCurveField:
        return ExtraDataNurbsCurveField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def nurbs_surface(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataNurbsSurfaceField:
        return ExtraDataNurbsSurfaceField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def point_array(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataPointArrayField:
        return ExtraDataPointArrayField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def string_array(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataStringArrayField:
        return ExtraDataStringArrayField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def string(
        cls,
        default_value: str = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataStringField:
        return ExtraDataStringField(
            **_field_kwargs(
                default_value=default_value,
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )

    @classmethod
    def vector_array(
        cls,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataVectorArrayField:
        return ExtraDataVectorArrayField(
            **_field_kwargs(
                multi=multi,
                long_name=long_name,
                short_name=short_name,
                readable=readable,
                writable=writable,
                category=category,
            )
        )


# define
class DefineEnum:
    field = ExtraEnumField
    plug_operator = EnumPlugOperator


class DefineCompound:
    field = ExtraCompoundField
    plug_operator = CompoundPlugOperator


class DefineAddAttrAt:
    enum = DefineEnum
    compound = DefineCompound


class DefineAddAttr:
    at = DefineAddAttrAt


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

    define = DefineAddAttr
