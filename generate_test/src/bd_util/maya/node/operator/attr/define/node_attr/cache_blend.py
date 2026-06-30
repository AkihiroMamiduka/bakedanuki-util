# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar.time import TimeField
from ..std.dt.double_array import DataDoubleArrayField


class InCachePlugOperator(
    CompoundPlugOperator["InCacheAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vectorArray", "va"),
        ("perPtWeights", "ppw"),
    )

    vectorArray = GenericField()
    va = vectorArray

    perPtWeights = DataDoubleArrayField()
    ppw = perPtWeights


class InCacheAttrOperator(
    CompoundAttrOperator[InCachePlugOperator]
):
    __slots__ = ()

    vectorArray = GenericField()
    va = vectorArray

    perPtWeights = DataDoubleArrayField()
    ppw = perPtWeights


class InCacheField(
    CompoundField[InCacheAttrOperator, InCachePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InCacheAttrOperator
    PLUG_CLS = InCachePlugOperator


class CacheDataPlugOperator(
    CompoundPlugOperator["CacheDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("start", "st"),
        ("end", "e"),
        ("range", "ra"),
        ("weight", "w"),
    )

    start = TimeField()
    st = start

    end = TimeField()
    e = end

    range = BoolField()
    ra = range

    weight = DoubleField()
    w = weight


class CacheDataAttrOperator(
    CompoundAttrOperator[CacheDataPlugOperator]
):
    __slots__ = ()

    start = TimeField()
    st = start

    end = TimeField()
    e = end

    range = BoolField()
    ra = range

    weight = DoubleField()
    w = weight


class CacheDataField(
    CompoundField[CacheDataAttrOperator, CacheDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CacheDataAttrOperator
    PLUG_CLS = CacheDataPlugOperator
