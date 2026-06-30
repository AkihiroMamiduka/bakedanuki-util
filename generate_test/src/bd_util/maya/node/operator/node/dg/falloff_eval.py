# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.falloff_eval import (
    PerFunctionWeightsField,
    PerVertexWeightsField,
)
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class FalloffEval(DG):
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

    perFunctionWeights = PerFunctionWeightsField(multi=True)
    pfw = perFunctionWeights

    perVertexWeights = PerVertexWeightsField(multi=True)
    pvw = perVertexWeights
