# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_imager_color_correct import (
    HighlightsGainField,
    HighlightsOffsetField,
    MainGainField,
    MainOffsetField,
    MidtonesGainField,
    MidtonesOffsetField,
    ShadowsGainField,
    ShadowsOffsetField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiImagerColorCorrect(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerColorCorrect"

    out = MessageField()

    enable = BoolField()

    layerSelection = DataStringField()
    layer_selection = layerSelection

    mainSaturation = FloatField()
    main_saturation = mainSaturation

    mainContrast = FloatField()
    main_contrast = mainContrast

    mainGamma = FloatField()
    main_gamma = mainGamma

    mainGain = MainGainField()
    main_gain = mainGain
    mainGainR = mainGain.mainGainR
    main_gainr = mainGainR
    mainGainG = mainGain.mainGainG
    main_gaing = mainGainG
    mainGainB = mainGain.mainGainB
    main_gainb = mainGainB

    mainOffset = MainOffsetField()
    main_offset = mainOffset
    mainOffsetR = mainOffset.mainOffsetR
    main_offsetr = mainOffsetR
    mainOffsetG = mainOffset.mainOffsetG
    main_offsetg = mainOffsetG
    mainOffsetB = mainOffset.mainOffsetB
    main_offsetb = mainOffsetB

    shadowsSaturation = FloatField()
    shadows_saturation = shadowsSaturation

    shadowsContrast = FloatField()
    shadows_contrast = shadowsContrast

    shadowsGamma = FloatField()
    shadows_gamma = shadowsGamma

    shadowsGain = ShadowsGainField()
    shadows_gain = shadowsGain
    shadowsGainR = shadowsGain.shadowsGainR
    shadows_gainr = shadowsGainR
    shadowsGainG = shadowsGain.shadowsGainG
    shadows_gaing = shadowsGainG
    shadowsGainB = shadowsGain.shadowsGainB
    shadows_gainb = shadowsGainB

    shadowsOffset = ShadowsOffsetField()
    shadows_offset = shadowsOffset
    shadowsOffsetR = shadowsOffset.shadowsOffsetR
    shadows_offsetr = shadowsOffsetR
    shadowsOffsetG = shadowsOffset.shadowsOffsetG
    shadows_offsetg = shadowsOffsetG
    shadowsOffsetB = shadowsOffset.shadowsOffsetB
    shadows_offsetb = shadowsOffsetB

    midtonesSaturation = FloatField()
    midtones_saturation = midtonesSaturation

    midtonesContrast = FloatField()
    midtones_contrast = midtonesContrast

    midtonesGamma = FloatField()
    midtones_gamma = midtonesGamma

    midtonesGain = MidtonesGainField()
    midtones_gain = midtonesGain
    midtonesGainR = midtonesGain.midtonesGainR
    midtones_gainr = midtonesGainR
    midtonesGainG = midtonesGain.midtonesGainG
    midtones_gaing = midtonesGainG
    midtonesGainB = midtonesGain.midtonesGainB
    midtones_gainb = midtonesGainB

    midtonesOffset = MidtonesOffsetField()
    midtones_offset = midtonesOffset
    midtonesOffsetR = midtonesOffset.midtonesOffsetR
    midtones_offsetr = midtonesOffsetR
    midtonesOffsetG = midtonesOffset.midtonesOffsetG
    midtones_offsetg = midtonesOffsetG
    midtonesOffsetB = midtonesOffset.midtonesOffsetB
    midtones_offsetb = midtonesOffsetB

    highlightsSaturation = FloatField()
    highlights_saturation = highlightsSaturation

    highlightsContrast = FloatField()
    highlights_contrast = highlightsContrast

    highlightsGamma = FloatField()
    highlights_gamma = highlightsGamma

    highlightsGain = HighlightsGainField()
    highlights_gain = highlightsGain
    highlightsGainR = highlightsGain.highlightsGainR
    highlights_gainr = highlightsGainR
    highlightsGainG = highlightsGain.highlightsGainG
    highlights_gaing = highlightsGainG
    highlightsGainB = highlightsGain.highlightsGainB
    highlights_gainb = highlightsGainB

    highlightsOffset = HighlightsOffsetField()
    highlights_offset = highlightsOffset
    highlightsOffsetR = highlightsOffset.highlightsOffsetR
    highlights_offsetr = highlightsOffsetR
    highlightsOffsetG = highlightsOffset.highlightsOffsetG
    highlights_offsetg = highlightsOffsetG
    highlightsOffsetB = highlightsOffset.highlightsOffsetB
    highlights_offsetb = highlightsOffsetB
