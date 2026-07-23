# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_curvature import (
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class OutputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONVEX = 0
    CONCAVE = 1
    BOTH = 2


class OutputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONVEX = 0
    CONCAVE = 1
    BOTH = 2

    NAME_MAP = {
        CONVEX: "convex",
        CONCAVE: "concave",
        BOTH: "both",
    }


class OutputEnumField(
    EnumField[OutputEnumAttrOperator, OutputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputEnumAttrOperator
    PLUG_CLS = OutputEnumPlugOperator


class _GeneratedAiCurvature(DG):
    __slots__ = ()

    NODE_TYPE = "aiCurvature"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    output = OutputEnumField(default_value=0)

    samples = LongField(default_value=3, min_value=0, soft_min_value=1, soft_max_value=10)

    radius = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=5.0)

    spread = FloatField(default_value=1.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

    threshold = FloatField(default_value=0.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

    bias = FloatField(default_value=0.5, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

    multiply = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)

    traceSet = DataStringField()
    trace_set = traceSet

    inclusive = BoolField(default_value=True)

    selfOnly = BoolField(default_value=False)
    self_only = selfOnly
