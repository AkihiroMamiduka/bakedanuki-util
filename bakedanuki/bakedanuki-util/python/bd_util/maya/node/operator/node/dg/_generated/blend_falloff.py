# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.blend_falloff import TargetField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField


class GeneratedBlendFalloff(DG):
    __slots__ = ()

    NODE_TYPE = "blendFalloff"

    baseWeight = FloatField(default_value=1.0)
    env = baseWeight

    target = TargetField(multi=True)
    tgt = target

    outputWeightFunction = TypedField(writable=False)
    wft = outputWeightFunction
