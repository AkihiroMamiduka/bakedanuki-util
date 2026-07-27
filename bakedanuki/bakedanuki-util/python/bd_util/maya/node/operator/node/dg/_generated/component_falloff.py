# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.component_falloff import (
    WeightInfoLayersField,
    WeightLayersField,
)
from ....attr.define.std.at.typed import TypedField


class GeneratedComponentFalloff(DG):
    __slots__ = ()

    NODE_TYPE = "componentFalloff"

    weightedGeometry = TypedField()
    wgm = weightedGeometry

    weightInfoLayers = WeightInfoLayersField(multi=True)
    wil = weightInfoLayers

    weightLayers = WeightLayersField(multi=True, default_value=1.0)
    whl = weightLayers

    outputWeightFunction = TypedField(multi=True, writable=False)
    wft = outputWeightFunction
