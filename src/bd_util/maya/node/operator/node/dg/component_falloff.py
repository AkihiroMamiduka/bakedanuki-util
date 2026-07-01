# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.component_falloff import (
    WeightInfoLayersField,
    WeightLayersField,
)
from ...attr.define.std.at.typed import TypedField


class ComponentFalloff(DG):
    __slots__ = ()

    NODE_TYPE = "componentFalloff"

    weightedGeometry = TypedField()
    wgm = weightedGeometry

    weightInfoLayers = WeightInfoLayersField(multi=True)
    wil = weightInfoLayers

    weightLayers = WeightLayersField(multi=True)
    whl = weightLayers

    outputWeightFunction = TypedField(multi=True)
    wft = outputWeightFunction
