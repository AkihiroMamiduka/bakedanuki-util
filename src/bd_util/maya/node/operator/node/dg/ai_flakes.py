# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_flakes import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class CoordSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    PREF = 2
    UV = 3


class CoordSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    PREF = 2
    UV = 3

    NAME_MAP = {
        WORLD: "world",
        OBJECT: "object",
        PREF: "Pref",
        UV: "UV",
    }


class CoordSpaceEnumField(
    EnumField[CoordSpaceEnumAttrOperator, CoordSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordSpaceEnumAttrOperator
    PLUG_CLS = CoordSpaceEnumPlugOperator


class OutputSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    TANGENT = 1


class OutputSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    TANGENT = 1

    NAME_MAP = {
        WORLD: "world",
        TANGENT: "tangent",
    }


class OutputSpaceEnumField(
    EnumField[OutputSpaceEnumAttrOperator, OutputSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputSpaceEnumAttrOperator
    PLUG_CLS = OutputSpaceEnumPlugOperator


class AiFlakes(DG):
    __slots__ = ()

    NODE_TYPE = "aiFlakes"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    scale = FloatField()

    density = FloatField()

    step = FloatField()

    depth = FloatField()

    IOR = FloatField()

    normalRandomize = FloatField()
    normal_randomize = normalRandomize

    coordSpace = CoordSpaceEnumField()
    coord_space = coordSpace

    prefName = DataStringField()
    pref_name = prefName

    outputSpace = OutputSpaceEnumField()
    output_space = outputSpace
