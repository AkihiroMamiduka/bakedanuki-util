# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.optical_fx import (
    FlareColorField,
    FogColorField,
    GlowColorField,
    HaloColorField,
    LightColorField,
    VisibilityField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.dt.matrix import DataMatrixField


class GlowTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    EXPONENTIAL = 2
    BALL = 3
    LENS_FLARE = 4
    RIM_HALO = 5


class GlowTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    EXPONENTIAL = 2
    BALL = 3
    LENS_FLARE = 4
    RIM_HALO = 5

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        EXPONENTIAL: "Exponential",
        BALL: "Ball",
        LENS_FLARE: "Lens Flare",
        RIM_HALO: "Rim Halo",
    }


class GlowTypeEnumField(
    EnumField[GlowTypeEnumAttrOperator, GlowTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GlowTypeEnumAttrOperator
    PLUG_CLS = GlowTypeEnumPlugOperator


class HaloTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    EXPONENTIAL = 2
    BALL = 3
    LENS_FLARE = 4
    RIM_HALO = 5


class HaloTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    EXPONENTIAL = 2
    BALL = 3
    LENS_FLARE = 4
    RIM_HALO = 5

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        EXPONENTIAL: "Exponential",
        BALL: "Ball",
        LENS_FLARE: "Lens Flare",
        RIM_HALO: "Rim Halo",
    }


class HaloTypeEnumField(
    EnumField[HaloTypeEnumAttrOperator, HaloTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HaloTypeEnumAttrOperator
    PLUG_CLS = HaloTypeEnumPlugOperator


class OpticalFX(DG):
    __slots__ = ()

    NODE_TYPE = "opticalFX"

    active = BoolField()
    act = active

    glowType = GlowTypeEnumField()
    gt = glowType

    haloType = HaloTypeEnumField()
    ht = haloType

    fogType = ShortField()
    ft = fogType

    lensFlare = BoolField()
    lf = lensFlare

    glowColor = GlowColorField()
    gc = glowColor
    glowColorR = glowColor.glowColorR
    gr = glowColorR
    glowColorG = glowColor.glowColorG
    gg = glowColorG
    glowColorB = glowColor.glowColorB
    gb = glowColorB

    haloColor = HaloColorField()
    hc = haloColor
    haloColorR = haloColor.haloColorR
    hr = haloColorR
    haloColorG = haloColor.haloColorG
    hg = haloColorG
    haloColorB = haloColor.haloColorB
    hb = haloColorB

    fogColor = FogColorField()
    fc = fogColor
    fogColorR = fogColor.fogColorR
    fr = fogColorR
    fogColorG = fogColor.fogColorG
    fg = fogColorG
    fogColorB = fogColor.fogColorB
    fb = fogColorB

    flareColor = FlareColorField()
    rc = flareColor
    flareColorR = flareColor.flareColorR
    rr = flareColorR
    flareColorG = flareColor.flareColorG
    rg = flareColorG
    flareColorB = flareColor.flareColorB
    rb = flareColorB

    flareIntensity = FloatField()
    fi = flareIntensity

    flareNumCircles = FloatField()
    fn = flareNumCircles

    flareMinSize = FloatField()
    fm = flareMinSize

    flareMaxSize = FloatField()
    fa = flareMaxSize

    flareColSpread = FloatField()
    lc = flareColSpread

    flareFocus = FloatField()
    ff = flareFocus

    flareVertical = FloatField()
    fv = flareVertical

    flareHorizontal = FloatField()
    fh = flareHorizontal

    flareLength = FloatField()
    fl = flareLength

    hexagonFlare = BoolField()
    hf = hexagonFlare

    glowIntensity = FloatField()
    gi = glowIntensity

    haloIntensity = FloatField()
    hi = haloIntensity

    fogIntensity = FloatField()
    oi = fogIntensity

    glowSpread = FloatField()
    gs = glowSpread

    haloSpread = FloatField()
    hs = haloSpread

    fogSpread = FloatField()
    fs = fogSpread

    glowNoise = FloatField()
    gd = glowNoise

    fogNoise = FloatField()
    fd = fogNoise

    glowRadialNoise = FloatField()
    gn = glowRadialNoise

    fogRadialNoise = FloatField()
    fz = fogRadialNoise

    glowStarLevel = FloatField()
    gv = glowStarLevel

    fogStarlevel = FloatField()
    fe = fogStarlevel

    glowOpacity = FloatField()
    go = glowOpacity

    fogOpacity = FloatField()
    fo = fogOpacity

    radialFrequency = FloatField()
    rf = radialFrequency

    starPoints = FloatField()
    sp = starPoints

    rotation = FloatField()
    ra = rotation

    noiseUscale = FloatField()
    nu = noiseUscale

    noiseVscale = FloatField()
    nv = noiseVscale

    noiseUoffset = FloatField()
    ni = noiseUoffset

    noiseVoffset = FloatField()
    nf = noiseVoffset

    noiseThreshold = FloatField()
    nt = noiseThreshold

    ignoreLight = BoolField()
    il = ignoreLight

    lightWorldMat = DataMatrixField()
    lw = lightWorldMat

    lightConnection = MessageField()
    ln = lightConnection

    glowVisibility = FloatField()
    gvb = glowVisibility

    lightColor = LightColorField()
    lr = lightColor
    lightColorR = lightColor.lightColorR
    lcr = lightColorR
    lightColorG = lightColor.lightColorG
    lcg = lightColorG
    lightColorB = lightColor.lightColorB
    lgb = lightColorB

    visibility = VisibilityField()
    vb = visibility
    visibilityR = visibility.visibilityR
    vbr = visibilityR
    visibilityG = visibility.visibilityG
    vbg = visibilityG
    visibilityB = visibility.visibilityB
    vbb = visibilityB
