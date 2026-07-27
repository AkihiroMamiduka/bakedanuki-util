# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_hair import (
    AiMatteColorField,
    OpacityField,
    OutColorField,
    OutTransparencyField,
    RootcolorField,
    Spec2ColorField,
    SpecColorField,
    TipcolorField,
    TransmissionColorField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiHair(DG):
    __slots__ = ()

    NODE_TYPE = "aiHair"

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

    rootcolor = RootcolorField(default_value=(0.10000000149011612, 0.10000000149011612, 0.10000000149011612))
    rootcolorR = rootcolor.rootcolorR
    rootcolorr = rootcolorR
    rootcolorG = rootcolor.rootcolorG
    rootcolorg = rootcolorG
    rootcolorB = rootcolor.rootcolorB
    rootcolorb = rootcolorB

    tipcolor = TipcolorField(default_value=(0.5, 0.5, 0.5))
    tipcolorR = tipcolor.tipcolorR
    tipcolorr = tipcolorR
    tipcolorG = tipcolor.tipcolorG
    tipcolorg = tipcolorG
    tipcolorB = tipcolor.tipcolorB
    tipcolorb = tipcolorB

    opacity = OpacityField(default_value=(1.0, 1.0, 1.0))
    opacityR = opacity.opacityR
    opacityr = opacityR
    opacityG = opacity.opacityG
    opacityg = opacityG
    opacityB = opacity.opacityB
    opacityb = opacityB

    ambdiff = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)

    spec = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    specColor = SpecColorField(default_value=(1.0, 1.0, 1.0))
    spec_color = specColor
    specColorR = specColor.specColorR
    spec_colorr = specColorR
    specColorG = specColor.specColorG
    spec_colorg = specColorG
    specColorB = specColor.specColorB
    spec_colorb = specColorB

    specShift = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=0.0)
    spec_shift = specShift

    specGloss = FloatField(default_value=10.0)
    spec_gloss = specGloss

    spec2 = FloatField(default_value=0.0, min_value=0.0, max_value=1.0, soft_max_value=1.0)

    spec2Color = Spec2ColorField(default_value=(1.0, 0.4000000059604645, 0.10000000149011612))
    spec2_color = spec2Color
    spec2ColorR = spec2Color.spec2ColorR
    spec2_colorr = spec2ColorR
    spec2ColorG = spec2Color.spec2ColorG
    spec2_colorg = spec2ColorG
    spec2ColorB = spec2Color.spec2ColorB
    spec2_colorb = spec2ColorB

    spec2Shift = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=15.0)
    spec2_shift = spec2Shift

    spec2Gloss = FloatField(default_value=7.0)
    spec2_gloss = spec2Gloss

    transmission = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)

    transmissionColor = TransmissionColorField(default_value=(1.0, 0.4000000059604645, 0.10000000149011612))
    transmission_color = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    transmission_colorr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    transmission_colorg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    transmission_colorb = transmissionColorB

    transmissionSpread = FloatField(default_value=1.0, soft_min_value=0.5, soft_max_value=5.0)
    transmission_spread = transmissionSpread

    kdInd = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)
    kd_ind = kdInd

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiEnableMatte = BoolField(default_value=False, category="arnold")
    ai_enable_matte = aiEnableMatte

    aiMatteColor = AiMatteColorField(default_value=(0.0, 0.0, 0.0), category="arnold")
    ai_matte_color = aiMatteColor
    aiMatteColorR = aiMatteColor.aiMatteColorR
    ai_matte_colorr = aiMatteColorR
    aiMatteColorG = aiMatteColor.aiMatteColorG
    ai_matte_colorg = aiMatteColorG
    aiMatteColorB = aiMatteColor.aiMatteColorB
    ai_matte_colorb = aiMatteColorB

    aiMatteColorA = FloatField(default_value=0.0, min_value=0.0, max_value=1.0, category="arnold")
    ai_matte_color_a = aiMatteColorA
