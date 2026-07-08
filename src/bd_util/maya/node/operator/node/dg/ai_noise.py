# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_noise import (
    Color1Field,
    Color2Field,
    OffsetField,
    OutColorField,
    OutTransparencyField,
    PField,
    ScaleField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
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
        UV: "uv",
    }


class CoordSpaceEnumField(
    EnumField[CoordSpaceEnumAttrOperator, CoordSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordSpaceEnumAttrOperator
    PLUG_CLS = CoordSpaceEnumPlugOperator


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SCALAR = 0
    VECTOR = 1


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SCALAR = 0
    VECTOR = 1

    NAME_MAP = {
        SCALAR: "scalar",
        VECTOR: "vector",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class AiNoise(DG):
    __slots__ = ()

    NODE_TYPE = "aiNoise"

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

    octaves = LongField(default_value=1, soft_min_value=1, soft_max_value=8)

    distortion = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    lacunarity = FloatField(default_value=1.9199999570846558, min_value=9.999999747378752e-05, soft_min_value=1.0, soft_max_value=5.0)

    amplitude = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

    scale = ScaleField(default_value=(1.0, 1.0, 1.0))
    scaleX = scale.scaleX
    scalex = scaleX
    scaleY = scale.scaleY
    scaley = scaleY
    scaleZ = scale.scaleZ
    scalez = scaleZ

    offset = OffsetField(default_value=(0.0, 0.0, 0.0))
    offsetX = offset.offsetX
    offsetx = offsetX
    offsetY = offset.offsetY
    offsety = offsetY
    offsetZ = offset.offsetZ
    offsetz = offsetZ

    coordSpace = CoordSpaceEnumField(default_value=1)
    coord_space = coordSpace

    prefName = DataStringField()
    pref_name = prefName

    P = PField(default_value=(0.0, 0.0, 0.0))
    PX = P.PX
    Px = PX
    PY = P.PY
    Py = PY
    PZ = P.PZ
    Pz = PZ

    time = FloatField(default_value=0.0)

    color1 = Color1Field(default_value=(0.0, 0.0, 0.0))
    color1R = color1.color1R
    color1r = color1R
    color1G = color1.color1G
    color1g = color1G
    color1B = color1.color1B
    color1b = color1B

    color2 = Color2Field(default_value=(1.0, 1.0, 1.0))
    color2R = color2.color2R
    color2r = color2R
    color2G = color2.color2G
    color2g = color2G
    color2B = color2.color2B
    color2b = color2B

    mode = ModeEnumField(default_value=0)
