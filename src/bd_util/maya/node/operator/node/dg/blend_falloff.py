# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.blend_falloff import TargetField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField


class BlendFalloff(DG):
    __slots__ = ()

    NODE_TYPE = "blendFalloff"

    baseWeight = FloatField()
    env = baseWeight

    target = TargetField(multi=True)
    tgt = target

    outputWeightFunction = TypedField()
    wft = outputWeightFunction
