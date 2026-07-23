# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.optical_fx import (
    FlareColorField,
    FogColorField,
    GlowColorField,
    HaloColorField,
    LightColorField,
    VisibilityField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.dt.matrix import DataMatrixField


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


class _GeneratedOpticalFX(DG):
    __slots__ = ()

    NODE_TYPE = "opticalFX"

    active = BoolField(default_value=True)
    act = active

    glowType = GlowTypeEnumField(default_value=1)
    gt = glowType

    haloType = HaloTypeEnumField(default_value=0)
    ht = haloType

    fogType = ShortField(default_value=0, min_value=0, max_value=5)
    ft = fogType

    lensFlare = BoolField(default_value=False)
    lf = lensFlare

    glowColor = GlowColorField(default_value=(1.0, 1.0, 1.0))
    gc = glowColor
    glowColorR = glowColor.glowColorR
    gr = glowColorR
    glowColorG = glowColor.glowColorG
    gg = glowColorG
    glowColorB = glowColor.glowColorB
    gb = glowColorB

    haloColor = HaloColorField(default_value=(1.0, 1.0, 1.0))
    hc = haloColor
    haloColorR = haloColor.haloColorR
    hr = haloColorR
    haloColorG = haloColor.haloColorG
    hg = haloColorG
    haloColorB = haloColor.haloColorB
    hb = haloColorB

    fogColor = FogColorField(default_value=(1.0, 1.0, 1.0))
    fc = fogColor
    fogColorR = fogColor.fogColorR
    fr = fogColorR
    fogColorG = fogColor.fogColorG
    fg = fogColorG
    fogColorB = fogColor.fogColorB
    fb = fogColorB

    flareColor = FlareColorField(default_value=(1.0, 1.0, 1.0))
    rc = flareColor
    flareColorR = flareColor.flareColorR
    rr = flareColorR
    flareColorG = flareColor.flareColorG
    rg = flareColorG
    flareColorB = flareColor.flareColorB
    rb = flareColorB

    flareIntensity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    fi = flareIntensity

    flareNumCircles = FloatField(default_value=20.0, min_value=0.0, soft_max_value=30.0)
    fn = flareNumCircles

    flareMinSize = FloatField(default_value=0.10000000149011612, soft_min_value=0.001, soft_max_value=5.0)
    fm = flareMinSize

    flareMaxSize = FloatField(default_value=1.0, soft_min_value=0.001, soft_max_value=5.0)
    fa = flareMaxSize

    flareColSpread = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    lc = flareColSpread

    flareFocus = FloatField(default_value=0.6000000238418579, soft_min_value=0.0, soft_max_value=1.0)
    ff = flareFocus

    flareVertical = FloatField(default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0)
    fv = flareVertical

    flareHorizontal = FloatField(default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0)
    fh = flareHorizontal

    flareLength = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    fl = flareLength

    hexagonFlare = BoolField(default_value=False)
    hf = hexagonFlare

    glowIntensity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    gi = glowIntensity

    haloIntensity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    hi = haloIntensity

    fogIntensity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    oi = fogIntensity

    glowSpread = FloatField(default_value=1.0, soft_min_value=0.001, soft_max_value=5.0)
    gs = glowSpread

    haloSpread = FloatField(default_value=1.0, soft_min_value=0.001, soft_max_value=5.0)
    hs = haloSpread

    fogSpread = FloatField(default_value=1.0, soft_min_value=0.001, soft_max_value=5.0)
    fs = fogSpread

    glowNoise = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gd = glowNoise

    fogNoise = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fd = fogNoise

    glowRadialNoise = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gn = glowRadialNoise

    fogRadialNoise = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fz = fogRadialNoise

    glowStarLevel = FloatField(default_value=3.0, soft_min_value=0.0, soft_max_value=10.0)
    gv = glowStarLevel

    fogStarlevel = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    fe = fogStarlevel

    glowOpacity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=0.5)
    go = glowOpacity

    fogOpacity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=0.5)
    fo = fogOpacity

    radialFrequency = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=5.0)
    rf = radialFrequency

    starPoints = FloatField(default_value=4.0, soft_min_value=0.0, soft_max_value=10.0)
    sp = starPoints

    rotation = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)
    ra = rotation

    noiseUscale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    nu = noiseUscale

    noiseVscale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    nv = noiseVscale

    noiseUoffset = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    ni = noiseUoffset

    noiseVoffset = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=10.0)
    nf = noiseVoffset

    noiseThreshold = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    nt = noiseThreshold

    ignoreLight = BoolField(default_value=False)
    il = ignoreLight

    lightWorldMat = DataMatrixField(readable=False)
    lw = lightWorldMat

    lightConnection = MessageField(writable=False)
    ln = lightConnection

    glowVisibility = FloatField(default_value=1.0, readable=False)
    gvb = glowVisibility

    lightColor = LightColorField(default_value=(1.0, 1.0, 1.0), readable=False)
    lr = lightColor
    lightColorR = lightColor.lightColorR
    lcr = lightColorR
    lightColorG = lightColor.lightColorG
    lcg = lightColorG
    lightColorB = lightColor.lightColorB
    lgb = lightColorB

    visibility = VisibilityField(default_value=(1.0, 1.0, 1.0), readable=False)
    vb = visibility
    visibilityR = visibility.visibilityR
    vbr = visibilityR
    visibilityG = visibility.visibilityG
    vbg = visibilityG
    visibilityB = visibility.visibilityB
    vbb = visibilityB
