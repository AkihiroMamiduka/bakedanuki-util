# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mountain import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    OutColorField,
    RockColorField,
    SnowColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedMountain(DG):
    __slots__ = ()

    NODE_TYPE = "mountain"

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0))
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    filter = FloatField(
        default_value=1.0,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    f = filter

    filterOffset = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    fo = filterOffset

    invert = BoolField(default_value=False)
    i = invert

    alphaIsLuminance = BoolField(default_value=False)
    ail = alphaIsLuminance

    colorGain = ColorGainField(
        default_value=(1.0, 1.0, 1.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(2.0, 2.0, 2.0),
    )
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(2.0, 2.0, 2.0),
    )
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=2.0
    )
    ag = alphaGain

    alphaOffset = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=2.0
    )
    ao = alphaOffset

    defaultColor = DefaultColorField(
        default_value=(0.5, 0.5, 0.5),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    oa = outAlpha

    snowColor = SnowColorField(
        default_value=(1.0, 1.0, 1.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    sc = snowColor
    snowColorR = snowColor.snowColorR
    scr = snowColorR
    snowColorG = snowColor.snowColorG
    scg = snowColorG
    snowColorB = snowColor.snowColorB
    scb = snowColorB

    rockColor = RockColorField(
        default_value=(0.2619999945163727, 0.10199999809265137, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    rc = rockColor
    rockColorR = rockColor.rockColorR
    rcr = rockColorR
    rockColorG = rockColor.rockColorG
    rcg = rockColorG
    rockColorB = rockColor.rockColorB
    rcb = rockColorB

    amplitude = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    a = amplitude

    snowRoughness = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
    sr = snowRoughness

    rockRoughness = FloatField(
        default_value=0.7070000171661377, min_value=0.0, max_value=1.0
    )
    rr = rockRoughness

    boundary = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    bo = boundary

    snowAltitude = FloatField(
        default_value=0.5, min_value=0.0, soft_max_value=1.0
    )
    sa = snowAltitude

    snowDropoff = FloatField(
        default_value=2.0, min_value=0.0, soft_max_value=2.0
    )
    sd = snowDropoff

    snowSlope = FloatField(
        default_value=0.800000011920929, min_value=0.0, soft_max_value=3.0
    )
    ss = snowSlope

    depthMax = FloatField(default_value=20.0, min_value=0.0, max_value=40.0)
    dmx = depthMax
