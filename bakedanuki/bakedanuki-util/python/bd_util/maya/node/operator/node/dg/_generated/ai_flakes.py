# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_flakes import (
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedAiFlakes(DG):
    __slots__ = ()

    NODE_TYPE = "aiFlakes"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    scale = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=100.0)

    density = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)

    step = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    depth = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    IOR = FloatField(default_value=1.5199999809265137, min_value=0.0, soft_max_value=10.0)

    normalRandomize = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    normal_randomize = normalRandomize

    coordSpace = CoordSpaceEnumField(default_value=2)
    coord_space = coordSpace

    prefName = DataStringField()
    pref_name = prefName

    outputSpace = OutputSpaceEnumField(default_value=0)
    output_space = outputSpace
