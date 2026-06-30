# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.shader_glow import (
    GlowColorField,
    HaloColorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


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


class ShaderGlow(DG):
    __slots__ = ()

    NODE_TYPE = "shaderGlow"

    glowType = GlowTypeEnumField()
    gt = glowType

    haloType = HaloTypeEnumField()
    ht = haloType

    glowIntensity = FloatField()
    gi = glowIntensity

    glowColor = GlowColorField()
    gc = glowColor
    glowColorR = glowColor.glowColorR
    gr = glowColorR
    glowColorG = glowColor.glowColorG
    gg = glowColorG
    glowColorB = glowColor.glowColorB
    gb = glowColorB

    glowSpread = FloatField()
    gs = glowSpread

    glowEccentricity = FloatField()
    gecc = glowEccentricity

    glowRadialNoise = FloatField()
    gn = glowRadialNoise

    glowStarLevel = FloatField()
    gv = glowStarLevel

    glowOpacity = FloatField()
    go = glowOpacity

    glowRingIntensity = FloatField()
    gri = glowRingIntensity

    glowRingFrequency = FloatField()
    grf = glowRingFrequency

    glowFilterWidth = LongField()
    gfw = glowFilterWidth

    haloIntensity = FloatField()
    hi = haloIntensity

    haloColor = HaloColorField()
    hc = haloColor
    haloColorR = haloColor.haloColorR
    hr = haloColorR
    haloColorG = haloColor.haloColorG
    hg = haloColorG
    haloColorB = haloColor.haloColorB
    hb = haloColorB

    haloSpread = FloatField()
    hs = haloSpread

    haloEccentricity = FloatField()
    hecc = haloEccentricity

    haloRadialNoise = FloatField()
    hn = haloRadialNoise

    haloStarLevel = FloatField()
    hv = haloStarLevel

    haloOpacity = FloatField()
    ho = haloOpacity

    haloRingIntensity = FloatField()
    hri = haloRingIntensity

    haloRingFrequency = FloatField()
    hrf = haloRingFrequency

    haloFilterWidth = LongField()
    hfw = haloFilterWidth

    quality = FloatField()
    qual = quality

    threshold = FloatField()
    th = threshold

    radialFrequency = FloatField()
    rf = radialFrequency

    starPoints = FloatField()
    sp = starPoints

    rotation = FloatField()
    ra = rotation

    autoExposure = BoolField()
    ae = autoExposure
