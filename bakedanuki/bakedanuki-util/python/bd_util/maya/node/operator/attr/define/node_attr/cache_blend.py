# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.time import TimeField
from ..std.dt.double_array import DataDoubleArrayField


class InCachePlugOperator(
    CompoundPlugOperator["InCacheAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vectorArray", "va"),
        ("perPtWeights", "ppw"),
    )

    vectorArray = GenericField(multi=True)
    va = vectorArray

    perPtWeights = DataDoubleArrayField(multi=True)
    ppw = perPtWeights


class InCacheAttrOperator(
    CompoundAttrOperator[InCachePlugOperator]
):
    __slots__ = ()

    vectorArray = GenericField(multi=True)
    va = vectorArray

    perPtWeights = DataDoubleArrayField(multi=True)
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

    start = TimeField(default_value=0.0)
    st = start

    end = TimeField(default_value=0.0)
    e = end

    range = BoolField(default_value=False)
    ra = range

    weight = DoubleField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    w = weight


class CacheDataAttrOperator(
    CompoundAttrOperator[CacheDataPlugOperator]
):
    __slots__ = ()

    start = TimeField(default_value=0.0)
    st = start

    end = TimeField(default_value=0.0)
    e = end

    range = BoolField(default_value=False)
    ra = range

    weight = DoubleField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    w = weight


class CacheDataField(
    CompoundField[CacheDataAttrOperator, CacheDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CacheDataAttrOperator
    PLUG_CLS = CacheDataPlugOperator
