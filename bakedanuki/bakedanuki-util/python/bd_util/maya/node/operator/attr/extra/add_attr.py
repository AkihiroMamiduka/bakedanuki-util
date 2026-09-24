# coding:utf-8
from __future__ import annotations

from typing import Any, ClassVar

# 属性定義と追加属性のフィールドをまとめて公開する。
from ..define.std.at.scalar.enum import EnumPlugOperator
from ..define.std.at.compound import CompoundPlugOperator

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
    default_value: Any = _UNSET,
    min_value: Any = _UNSET,
    max_value: Any = _UNSET,
    soft_min_value: Any = _UNSET,
    soft_max_value: Any = _UNSET,
    multi: bool = False,
    readable: bool | None = None,
    writable: bool | None = None,
    category: str | None = None,
) -> dict[str, Any]:
    kwargs: dict[str, Any] = {
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


class AddAttrAt:
    """Maya の ``attributeType`` に対応する追加属性を定義する。

    各メソッドは NodeOperator のクラス属性に置く AttributeField を返す。

    共通の ``multi`` は配列属性、``long_name`` / ``short_name`` は
    Maya 側の属性名を指定する。``readable`` / ``writable`` と
    ``category`` は Maya 属性のフラグ・カテゴリに渡す。
    数値型で使う ``min_value`` / ``max_value`` は許容範囲、
    ``soft_min_value`` / ``soft_max_value`` は UI 上の推奨範囲。
    """

    @classmethod
    def bool(
        cls,
        default_value: bool | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraBoolField:
        """真偽値の追加属性を定義する。"""
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
        default_value: int | None = None,
        min_value: int | None = None,
        max_value: int | None = None,
        soft_min_value: int | None = None,
        soft_max_value: int | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraByteField:
        """byte 型の追加属性を定義する。"""
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
        default_value: int | None = None,
        min_value: int | None = None,
        max_value: int | None = None,
        soft_min_value: int | None = None,
        soft_max_value: int | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraCharField:
        """char 型の追加属性を定義する。"""
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
        default_value: float | None = None,
        min_value: float | None = None,
        max_value: float | None = None,
        soft_min_value: float | None = None,
        soft_max_value: float | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleAngleField:
        """double 精度の角度属性を定義する。"""
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
        default_value: float | None = None,
        min_value: float | None = None,
        max_value: float | None = None,
        soft_min_value: float | None = None,
        soft_max_value: float | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleLinearField:
        """double 精度の距離属性を定義する。値の単位は cm。"""
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
        default_value: float | None = None,
        min_value: float | None = None,
        max_value: float | None = None,
        soft_min_value: float | None = None,
        soft_max_value: float | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleField:
        """double 型の追加属性を定義する。"""
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
        default_value: tuple[float, float] | None = None,
        min_value: float | tuple[float, float] | None = None,
        max_value: float | tuple[float, float] | None = None,
        soft_min_value: float | tuple[float, float] | None = None,
        soft_max_value: float | tuple[float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDouble2Field:
        """2 成分の double 属性を定義する。"""
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
        default_value: tuple[float, float, float] | None = None,
        min_value: float | tuple[float, float, float] | None = None,
        max_value: float | tuple[float, float, float] | None = None,
        soft_min_value: float | tuple[float, float, float] | None = None,
        soft_max_value: float | tuple[float, float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDouble3Field:
        """3 成分の double 属性を定義する。"""
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
        default_value: tuple[float, float, float, float] | None = None,
        min_value: float | tuple[float, float, float, float] | None = None,
        max_value: float | tuple[float, float, float, float] | None = None,
        soft_min_value: (
            float | tuple[float, float, float, float] | None
        ) = None,
        soft_max_value: (
            float | tuple[float, float, float, float] | None
        ) = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDouble4Field:
        """4 成分の double 属性を定義する。"""
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
        default_value: tuple[float, float, float, float] | None = None,
        min_value: float | tuple[float, float, float, float] | None = None,
        max_value: float | tuple[float, float, float, float] | None = None,
        soft_min_value: (
            float | tuple[float, float, float, float] | None
        ) = None,
        soft_max_value: (
            float | tuple[float, float, float, float] | None
        ) = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraQuat4Field:
        """4 成分の Quaternion 属性を定義する。"""
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
        default_value: tuple[float, float] | None = None,
        min_value: float | tuple[float, float] | None = None,
        max_value: float | tuple[float, float] | None = None,
        soft_min_value: float | tuple[float, float] | None = None,
        soft_max_value: float | tuple[float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleLinear2Field:
        """2 成分の距離属性を定義する。値の単位は cm。"""
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
        default_value: tuple[float, float, float] | None = None,
        min_value: float | tuple[float, float, float] | None = None,
        max_value: float | tuple[float, float, float] | None = None,
        soft_min_value: float | tuple[float, float, float] | None = None,
        soft_max_value: float | tuple[float, float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleLinear3Field:
        """3 成分の距離属性を定義する。値の単位は cm。"""
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
        default_value: tuple[float, float] | None = None,
        min_value: float | tuple[float, float] | None = None,
        max_value: float | tuple[float, float] | None = None,
        soft_min_value: float | tuple[float, float] | None = None,
        soft_max_value: float | tuple[float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleAngle2Field:
        """2 成分の角度属性を定義する。"""
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
        default_value: tuple[float, float, float] | None = None,
        min_value: float | tuple[float, float, float] | None = None,
        max_value: float | tuple[float, float, float] | None = None,
        soft_min_value: float | tuple[float, float, float] | None = None,
        soft_max_value: float | tuple[float, float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDoubleAngle3Field:
        """3 成分の角度属性を定義する。"""
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
        default_value: float | None = None,
        min_value: float | None = None,
        max_value: float | None = None,
        soft_min_value: float | None = None,
        soft_max_value: float | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatAngleField:
        """float 精度の角度属性を定義する。"""
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
        default_value: float | None = None,
        min_value: float | None = None,
        max_value: float | None = None,
        soft_min_value: float | None = None,
        soft_max_value: float | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatLinearField:
        """float 精度の距離属性を定義する。値の単位は cm。"""
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
        default_value: float | None = None,
        min_value: float | None = None,
        max_value: float | None = None,
        soft_min_value: float | None = None,
        soft_max_value: float | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatField:
        """float 型の追加属性を定義する。"""
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
        default_value: tuple[float, float] | None = None,
        min_value: float | tuple[float, float] | None = None,
        max_value: float | tuple[float, float] | None = None,
        soft_min_value: float | tuple[float, float] | None = None,
        soft_max_value: float | tuple[float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloat2Field:
        """2 成分の float 属性を定義する。"""
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
        default_value: tuple[float, float, float] | None = None,
        min_value: float | tuple[float, float, float] | None = None,
        max_value: float | tuple[float, float, float] | None = None,
        soft_min_value: float | tuple[float, float, float] | None = None,
        soft_max_value: float | tuple[float, float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloat3Field:
        """3 成分の float 属性を定義する。"""
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
        default_value: tuple[float, float] | None = None,
        min_value: float | tuple[float, float] | None = None,
        max_value: float | tuple[float, float] | None = None,
        soft_min_value: float | tuple[float, float] | None = None,
        soft_max_value: float | tuple[float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatLinear2Field:
        """2 成分の距離属性を定義する。値の単位は cm。"""
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
        default_value: tuple[float, float, float] | None = None,
        min_value: float | tuple[float, float, float] | None = None,
        max_value: float | tuple[float, float, float] | None = None,
        soft_min_value: float | tuple[float, float, float] | None = None,
        soft_max_value: float | tuple[float, float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatLinear3Field:
        """3 成分の距離属性を定義する。値の単位は cm。"""
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
        default_value: tuple[float, float] | None = None,
        min_value: float | tuple[float, float] | None = None,
        max_value: float | tuple[float, float] | None = None,
        soft_min_value: float | tuple[float, float] | None = None,
        soft_max_value: float | tuple[float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatAngle2Field:
        """2 成分の角度属性を定義する。"""
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
        default_value: tuple[float, float, float] | None = None,
        min_value: float | tuple[float, float, float] | None = None,
        max_value: float | tuple[float, float, float] | None = None,
        soft_min_value: float | tuple[float, float, float] | None = None,
        soft_max_value: float | tuple[float, float, float] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraFloatAngle3Field:
        """3 成分の角度属性を定義する。"""
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
        """float 精度の行列属性を定義する。"""
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
        """generic 型の追加属性を定義する。"""
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
        default_value: int | None = None,
        soft_min_value: int | None = None,
        soft_max_value: int | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraLongLongIntField:
        """64 bit 整数の追加属性を定義する。"""
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
        default_value: int | None = None,
        min_value: int | None = None,
        max_value: int | None = None,
        soft_min_value: int | None = None,
        soft_max_value: int | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraLongField:
        """long 整数の追加属性を定義する。"""
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
        default_value: tuple[int, int] | None = None,
        min_value: int | tuple[int, int] | None = None,
        max_value: int | tuple[int, int] | None = None,
        soft_min_value: int | tuple[int, int] | None = None,
        soft_max_value: int | tuple[int, int] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraLong2Field:
        """2 成分の long 整数属性を定義する。"""
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
        default_value: tuple[int, int, int] | None = None,
        min_value: int | tuple[int, int, int] | None = None,
        max_value: int | tuple[int, int, int] | None = None,
        soft_min_value: int | tuple[int, int, int] | None = None,
        soft_max_value: int | tuple[int, int, int] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraLong3Field:
        """3 成分の long 整数属性を定義する。"""
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
        """attributeType の行列属性を定義する。"""
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
        """message 型の追加属性を定義する。"""
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
        default_value: int | None = None,
        min_value: int | None = None,
        max_value: int | None = None,
        soft_min_value: int | None = None,
        soft_max_value: int | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraShortField:
        """short 整数の追加属性を定義する。"""
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
        default_value: tuple[int, int] | None = None,
        min_value: int | tuple[int, int] | None = None,
        max_value: int | tuple[int, int] | None = None,
        soft_min_value: int | tuple[int, int] | None = None,
        soft_max_value: int | tuple[int, int] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraShort2Field:
        """2 成分の short 整数属性を定義する。"""
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
        default_value: tuple[int, int, int] | None = None,
        min_value: int | tuple[int, int, int] | None = None,
        max_value: int | tuple[int, int, int] | None = None,
        soft_min_value: int | tuple[int, int, int] | None = None,
        soft_max_value: int | tuple[int, int, int] | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraShort3Field:
        """3 成分の short 整数属性を定義する。"""
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
        default_value: float | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraTimeField:
        """時間属性を定義する。値は Maya の UI 時間単位。"""
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
    """Maya の ``dataType`` に対応する追加属性を定義する。

    各メソッドは ``multi``、属性名、readable / writable、category を
    ``AddAttrAt`` と同じ意味で受け取る。
    """

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
        """double 配列の dataType 属性を定義する。"""
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
        """float 配列の dataType 属性を定義する。"""
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
        """32 bit 整数配列の dataType 属性を定義する。"""
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
        """lattice データの属性を定義する。"""
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
        """dataType の行列属性を定義する。"""
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
        """mesh データの属性を定義する。"""
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
        """NURBS curve データの属性を定義する。"""
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
        """NURBS surface データの属性を定義する。"""
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
        """point 配列の dataType 属性を定義する。"""
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
        """文字列配列の dataType 属性を定義する。"""
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
        default_value: str | None = None,
        multi: bool = False,
        long_name: str | None = None,
        short_name: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ) -> ExtraDataStringField:
        """文字列の dataType 属性を定義する。"""
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
        """vector 配列の dataType 属性を定義する。"""
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


class DefineEnum:
    """enum 用の Field と PlugOperator 型をまとめる。"""

    field = ExtraEnumField
    plug_operator = EnumPlugOperator


class DefineCompound:
    """compound 用の Field と PlugOperator 型をまとめる。"""

    field = ExtraCompoundField
    plug_operator = CompoundPlugOperator


class DefineAddAttrAt:
    """enum / compound の型定義への入口。"""

    enum = DefineEnum
    compound = DefineCompound


class DefineAddAttr:
    """追加属性の型定義への入口。"""

    at = DefineAddAttrAt


class AddAttr:
    """NodeOperator に追加する AttributeField の入口。

    Examples:
        >>> class NewNode(NodeOperator):
        ...     weight = AddAttr.at.double(default_value=1.0)
        ...     matrix = AddAttr.at.matrix()
        ...     data_matrix = AddAttr.dt.matrix()
    """

    at: ClassVar[AddAttrAt] = AddAttrAt()
    dt: ClassVar[AddAttrDt] = AddAttrDt()

    define = DefineAddAttr
