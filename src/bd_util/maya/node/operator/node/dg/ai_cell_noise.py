# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_cell_noise import (
    ColorField,
    OffsetField,
    OutColorField,
    OutTransparencyField,
    PField,
    PaletteField,
    ScaleField,
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


class PatternEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NOISE1 = 0
    NOISE2 = 1
    CELL1 = 2
    CELL2 = 3
    WORLEY1 = 4
    WORLEY2 = 5
    ALLIGATOR = 6


class PatternEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NOISE1 = 0
    NOISE2 = 1
    CELL1 = 2
    CELL2 = 3
    WORLEY1 = 4
    WORLEY2 = 5
    ALLIGATOR = 6

    NAME_MAP = {
        NOISE1: "noise1",
        NOISE2: "noise2",
        CELL1: "cell1",
        CELL2: "cell2",
        WORLEY1: "worley1",
        WORLEY2: "worley2",
        ALLIGATOR: "alligator",
    }


class PatternEnumField(
    EnumField[PatternEnumAttrOperator, PatternEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PatternEnumAttrOperator
    PLUG_CLS = PatternEnumPlugOperator


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
        UV: "uv",
    }


class CoordSpaceEnumField(
    EnumField[CoordSpaceEnumAttrOperator, CoordSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordSpaceEnumAttrOperator
    PLUG_CLS = CoordSpaceEnumPlugOperator


class AiCellNoise(DG):
    __slots__ = ()

    NODE_TYPE = "aiCellNoise"

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

    pattern = PatternEnumField()

    additive = BoolField()

    octaves = LongField()

    randomness = FloatField()

    lacunarity = FloatField()

    amplitude = FloatField()

    scale = ScaleField()
    scaleX = scale.scaleX
    scalex = scaleX
    scaleY = scale.scaleY
    scaley = scaleY
    scaleZ = scale.scaleZ
    scalez = scaleZ

    offset = OffsetField()
    offsetX = offset.offsetX
    offsetx = offsetX
    offsetY = offset.offsetY
    offsety = offsetY
    offsetZ = offset.offsetZ
    offsetz = offsetZ

    coordSpace = CoordSpaceEnumField()
    coord_space = coordSpace

    prefName = DataStringField()
    pref_name = prefName

    P = PField()
    PX = P.PX
    Px = PX
    PY = P.PY
    Py = PY
    PZ = P.PZ
    Pz = PZ

    time = FloatField()

    color = ColorField()
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    palette = PaletteField()
    paletteR = palette.paletteR
    paletter = paletteR
    paletteG = palette.paletteG
    paletteg = paletteG
    paletteB = palette.paletteB
    paletteb = paletteB

    density = FloatField()
