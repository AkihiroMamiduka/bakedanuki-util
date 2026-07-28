# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.dt.string import DataStringField


class WeightInfoLayersPlugOperator(
    CompoundPlugOperator["WeightInfoLayersAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("layerName", "lnm"),
        ("defaultWeight", "dwt"),
    )

    layerName = DataStringField()
    lnm = layerName

    defaultWeight = FloatField(default_value=1.0)
    dwt = defaultWeight


class WeightInfoLayersAttrOperator(
    CompoundAttrOperator[WeightInfoLayersPlugOperator]
):
    __slots__ = ()

    layerName = DataStringField()
    lnm = layerName

    defaultWeight = FloatField(default_value=1.0)
    dwt = defaultWeight


class WeightInfoLayersField(
    CompoundField[WeightInfoLayersAttrOperator, WeightInfoLayersPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightInfoLayersAttrOperator
    PLUG_CLS = WeightInfoLayersPlugOperator


class WeightLayersPlugOperator(
    CompoundPlugOperator["WeightLayersAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weights", "wht"),)

    weights = DoubleField(multi=True, default_value=1.0)
    wht = weights


class WeightLayersAttrOperator(CompoundAttrOperator[WeightLayersPlugOperator]):
    __slots__ = ()

    weights = DoubleField(multi=True, default_value=1.0)
    wht = weights


class WeightLayersField(
    CompoundField[WeightLayersAttrOperator, WeightLayersPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightLayersAttrOperator
    PLUG_CLS = WeightLayersPlugOperator
