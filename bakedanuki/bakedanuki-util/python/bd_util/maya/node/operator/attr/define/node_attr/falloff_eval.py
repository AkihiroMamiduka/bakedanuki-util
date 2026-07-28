# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField


class PerFunctionWeightsPlugOperator(
    CompoundPlugOperator["PerFunctionWeightsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("perFunctionVertexWeights", "pfvw"),)

    perFunctionVertexWeights = FloatField(
        multi=True, default_value=0.0, writable=False
    )
    pfvw = perFunctionVertexWeights


class PerFunctionWeightsAttrOperator(
    CompoundAttrOperator[PerFunctionWeightsPlugOperator]
):
    __slots__ = ()

    perFunctionVertexWeights = FloatField(
        multi=True, default_value=0.0, writable=False
    )
    pfvw = perFunctionVertexWeights


class PerFunctionWeightsField(
    CompoundField[
        PerFunctionWeightsAttrOperator, PerFunctionWeightsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PerFunctionWeightsAttrOperator
    PLUG_CLS = PerFunctionWeightsPlugOperator


class PerVertexWeightsPlugOperator(
    CompoundPlugOperator["PerVertexWeightsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("perVertexFalloffWeights", "pvfw"),)

    perVertexFalloffWeights = DoubleField(
        multi=True, default_value=0.0, writable=False
    )
    pvfw = perVertexFalloffWeights


class PerVertexWeightsAttrOperator(
    CompoundAttrOperator[PerVertexWeightsPlugOperator]
):
    __slots__ = ()

    perVertexFalloffWeights = DoubleField(
        multi=True, default_value=0.0, writable=False
    )
    pvfw = perVertexFalloffWeights


class PerVertexWeightsField(
    CompoundField[PerVertexWeightsAttrOperator, PerVertexWeightsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PerVertexWeightsAttrOperator
    PLUG_CLS = PerVertexWeightsPlugOperator
