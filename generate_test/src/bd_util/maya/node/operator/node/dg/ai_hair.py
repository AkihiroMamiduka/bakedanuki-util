# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_hair import (
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
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiHair(DG):
    __slots__ = ()

    NODE_TYPE = "aiHair"

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

    rootcolor = RootcolorField()
    rootcolorR = rootcolor.rootcolorR
    rootcolorr = rootcolorR
    rootcolorG = rootcolor.rootcolorG
    rootcolorg = rootcolorG
    rootcolorB = rootcolor.rootcolorB
    rootcolorb = rootcolorB

    tipcolor = TipcolorField()
    tipcolorR = tipcolor.tipcolorR
    tipcolorr = tipcolorR
    tipcolorG = tipcolor.tipcolorG
    tipcolorg = tipcolorG
    tipcolorB = tipcolor.tipcolorB
    tipcolorb = tipcolorB

    opacity = OpacityField()
    opacityR = opacity.opacityR
    opacityr = opacityR
    opacityG = opacity.opacityG
    opacityg = opacityG
    opacityB = opacity.opacityB
    opacityb = opacityB

    ambdiff = FloatField()

    spec = FloatField()

    specColor = SpecColorField()
    spec_color = specColor
    specColorR = specColor.specColorR
    spec_colorr = specColorR
    specColorG = specColor.specColorG
    spec_colorg = specColorG
    specColorB = specColor.specColorB
    spec_colorb = specColorB

    specShift = FloatField()
    spec_shift = specShift

    specGloss = FloatField()
    spec_gloss = specGloss

    spec2 = FloatField()

    spec2Color = Spec2ColorField()
    spec2_color = spec2Color
    spec2ColorR = spec2Color.spec2ColorR
    spec2_colorr = spec2ColorR
    spec2ColorG = spec2Color.spec2ColorG
    spec2_colorg = spec2ColorG
    spec2ColorB = spec2Color.spec2ColorB
    spec2_colorb = spec2ColorB

    spec2Shift = FloatField()
    spec2_shift = spec2Shift

    spec2Gloss = FloatField()
    spec2_gloss = spec2Gloss

    transmission = FloatField()

    transmissionColor = TransmissionColorField()
    transmission_color = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    transmission_colorr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    transmission_colorg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    transmission_colorb = transmissionColorB

    transmissionSpread = FloatField()
    transmission_spread = transmissionSpread

    kdInd = FloatField()
    kd_ind = kdInd

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    aiEnableMatte = BoolField()
    ai_enable_matte = aiEnableMatte

    aiMatteColor = AiMatteColorField()
    ai_matte_color = aiMatteColor
    aiMatteColorR = aiMatteColor.aiMatteColorR
    ai_matte_colorr = aiMatteColorR
    aiMatteColorG = aiMatteColor.aiMatteColorG
    ai_matte_colorg = aiMatteColorG
    aiMatteColorB = aiMatteColor.aiMatteColorB
    ai_matte_colorb = aiMatteColorB

    aiMatteColorA = FloatField()
    ai_matte_color_a = aiMatteColorA
