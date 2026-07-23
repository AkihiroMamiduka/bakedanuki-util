# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.shader_glow import (
    GlowColorField,
    HaloColorField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField


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


class _GeneratedShaderGlow(DG):
    __slots__ = ()

    NODE_TYPE = "shaderGlow"

    glowType = GlowTypeEnumField(default_value=1)
    gt = glowType

    haloType = HaloTypeEnumField(default_value=1)
    ht = haloType

    glowIntensity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    gi = glowIntensity

    glowColor = GlowColorField(default_value=(1.0, 1.0, 1.0))
    gc = glowColor
    glowColorR = glowColor.glowColorR
    gr = glowColorR
    glowColorG = glowColor.glowColorG
    gg = glowColorG
    glowColorB = glowColor.glowColorB
    gb = glowColorB

    glowSpread = FloatField(default_value=0.05000000074505806, soft_min_value=0.001, soft_max_value=1.0)
    gs = glowSpread

    glowEccentricity = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=1.0)
    gecc = glowEccentricity

    glowRadialNoise = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=4.0)
    gn = glowRadialNoise

    glowStarLevel = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=4.0)
    gv = glowStarLevel

    glowOpacity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    go = glowOpacity

    glowRingIntensity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gri = glowRingIntensity

    glowRingFrequency = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    grf = glowRingFrequency

    glowFilterWidth = LongField(default_value=1)
    gfw = glowFilterWidth

    haloIntensity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    hi = haloIntensity

    haloColor = HaloColorField(default_value=(1.0, 1.0, 1.0))
    hc = haloColor
    haloColorR = haloColor.haloColorR
    hr = haloColorR
    haloColorG = haloColor.haloColorG
    hg = haloColorG
    haloColorB = haloColor.haloColorB
    hb = haloColorB

    haloSpread = FloatField(default_value=0.30000001192092896, soft_min_value=0.0, soft_max_value=1.0)
    hs = haloSpread

    haloEccentricity = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=1.0)
    hecc = haloEccentricity

    haloRadialNoise = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=4.0)
    hn = haloRadialNoise

    haloStarLevel = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=4.0)
    hv = haloStarLevel

    haloOpacity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ho = haloOpacity

    haloRingIntensity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    hri = haloRingIntensity

    haloRingFrequency = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    hrf = haloRingFrequency

    haloFilterWidth = LongField(default_value=1)
    hfw = haloFilterWidth

    quality = FloatField(default_value=0.5, min_value=0.0, soft_max_value=5.0)
    qual = quality

    threshold = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    th = threshold

    radialFrequency = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    rf = radialFrequency

    starPoints = FloatField(default_value=4.0, soft_min_value=0.0, soft_max_value=10.0)
    sp = starPoints

    rotation = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)
    ra = rotation

    autoExposure = BoolField(default_value=True)
    ae = autoExposure
