# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..custom import Float2Field


class CachedUVsPlugOperator(CompoundPlugOperator["CachedUVsAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("uvPoints", "uvp"),)

    uvPoints = Float2Field(multi=True, default_value=(0.0, 0.0))
    uvp = uvPoints


class CachedUVsAttrOperator(CompoundAttrOperator[CachedUVsPlugOperator]):
    __slots__ = ()

    uvPoints = Float2Field(multi=True, default_value=(0.0, 0.0))
    uvp = uvPoints


class CachedUVsField(
    CompoundField[CachedUVsAttrOperator, CachedUVsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CachedUVsAttrOperator
    PLUG_CLS = CachedUVsPlugOperator
