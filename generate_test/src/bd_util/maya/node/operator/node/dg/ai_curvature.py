# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_curvature import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


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


class AiCurvature(DG):
    __slots__ = ()

    NODE_TYPE = "aiCurvature"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    output = OutputEnumField()

    samples = LongField()

    radius = FloatField()

    spread = FloatField()

    threshold = FloatField()

    bias = FloatField()

    multiply = FloatField()

    traceSet = DataStringField()
    trace_set = traceSet

    inclusive = BoolField()

    selfOnly = BoolField()
    self_only = selfOnly
