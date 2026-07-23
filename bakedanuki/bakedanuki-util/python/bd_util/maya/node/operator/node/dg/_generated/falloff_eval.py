# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.falloff_eval import (
    PerFunctionWeightsField,
    PerVertexWeightsField,
)
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedFalloffEval(DG):
    __slots__ = ()

    NODE_TYPE = "falloffEval"

    currentGeometry = TypedField()
    cgm = currentGeometry

    originalGeometry = TypedField()
    ogm = originalGeometry

    componentTagExpression = DataStringField()
    gtg = componentTagExpression

    weightFunction = TypedField(multi=True)
    whf = weightFunction

    perFunctionWeights = PerFunctionWeightsField(multi=True, default_value=0.0, writable=False)
    pfw = perFunctionWeights

    perVertexWeights = PerVertexWeightsField(multi=True, default_value=0.0, writable=False)
    pvw = perVertexWeights
