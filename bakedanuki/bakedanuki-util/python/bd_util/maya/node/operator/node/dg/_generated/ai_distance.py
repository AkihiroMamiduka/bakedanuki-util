# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_distance import (
    FarColorField,
    NearColorField,
    OutColorField,
    Out_directionField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiDistance(DG):
    __slots__ = ()

    NODE_TYPE = "aiDistance"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    out_distance = FloatField(default_value=0.0, writable=False)

    out_direction = Out_directionField(default_value=(0.0, 0.0, 0.0), writable=False)
    out_directionX = out_direction.out_directionX
    out_directionx = out_directionX
    out_directionY = out_direction.out_directionY
    out_directiony = out_directionY
    out_directionZ = out_direction.out_directionZ
    out_directionz = out_directionZ

    samples = LongField(default_value=16, min_value=1)

    distance = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    nearColor = NearColorField(default_value=(0.0, 0.0, 0.0))
    near_color = nearColor
    nearColorR = nearColor.nearColorR
    near_colorr = nearColorR
    nearColorG = nearColor.nearColorG
    near_colorg = nearColorG
    nearColorB = nearColor.nearColorB
    near_colorb = nearColorB

    farColor = FarColorField(default_value=(1.0, 1.0, 1.0))
    far_color = farColor
    farColorR = farColor.farColorR
    far_colorr = farColorR
    farColorG = farColor.farColorG
    far_colorg = farColorG
    farColorB = farColor.farColorB
    far_colorb = farColorB

    traceSet = DataStringField()
    trace_set = traceSet

    inclusive = BoolField(default_value=True)
