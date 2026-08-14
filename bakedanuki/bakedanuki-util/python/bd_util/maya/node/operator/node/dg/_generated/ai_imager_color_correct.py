# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_imager_color_correct import (
    HighlightsGainField,
    HighlightsOffsetField,
    MainGainField,
    MainOffsetField,
    MidtonesGainField,
    MidtonesOffsetField,
    ShadowsGainField,
    ShadowsOffsetField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiImagerColorCorrect(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerColorCorrect"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    mainSaturation = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    main_saturation = mainSaturation

    mainContrast = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    main_contrast = mainContrast

    mainGamma = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=5.0
    )
    main_gamma = mainGamma

    mainGain = MainGainField(default_value=(1.0, 1.0, 1.0))
    main_gain = mainGain
    mainGainR = mainGain.mainGainR
    main_gainr = mainGainR
    mainGainG = mainGain.mainGainG
    main_gaing = mainGainG
    mainGainB = mainGain.mainGainB
    main_gainb = mainGainB

    mainOffset = MainOffsetField(default_value=(0.0, 0.0, 0.0))
    main_offset = mainOffset
    mainOffsetR = mainOffset.mainOffsetR
    main_offsetr = mainOffsetR
    mainOffsetG = mainOffset.mainOffsetG
    main_offsetg = mainOffsetG
    mainOffsetB = mainOffset.mainOffsetB
    main_offsetb = mainOffsetB

    shadowsSaturation = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    shadows_saturation = shadowsSaturation

    shadowsContrast = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    shadows_contrast = shadowsContrast

    shadowsGamma = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=5.0
    )
    shadows_gamma = shadowsGamma

    shadowsGain = ShadowsGainField(default_value=(1.0, 1.0, 1.0))
    shadows_gain = shadowsGain
    shadowsGainR = shadowsGain.shadowsGainR
    shadows_gainr = shadowsGainR
    shadowsGainG = shadowsGain.shadowsGainG
    shadows_gaing = shadowsGainG
    shadowsGainB = shadowsGain.shadowsGainB
    shadows_gainb = shadowsGainB

    shadowsOffset = ShadowsOffsetField(default_value=(0.0, 0.0, 0.0))
    shadows_offset = shadowsOffset
    shadowsOffsetR = shadowsOffset.shadowsOffsetR
    shadows_offsetr = shadowsOffsetR
    shadowsOffsetG = shadowsOffset.shadowsOffsetG
    shadows_offsetg = shadowsOffsetG
    shadowsOffsetB = shadowsOffset.shadowsOffsetB
    shadows_offsetb = shadowsOffsetB

    midtonesSaturation = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    midtones_saturation = midtonesSaturation

    midtonesContrast = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    midtones_contrast = midtonesContrast

    midtonesGamma = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=5.0
    )
    midtones_gamma = midtonesGamma

    midtonesGain = MidtonesGainField(default_value=(1.0, 1.0, 1.0))
    midtones_gain = midtonesGain
    midtonesGainR = midtonesGain.midtonesGainR
    midtones_gainr = midtonesGainR
    midtonesGainG = midtonesGain.midtonesGainG
    midtones_gaing = midtonesGainG
    midtonesGainB = midtonesGain.midtonesGainB
    midtones_gainb = midtonesGainB

    midtonesOffset = MidtonesOffsetField(default_value=(0.0, 0.0, 0.0))
    midtones_offset = midtonesOffset
    midtonesOffsetR = midtonesOffset.midtonesOffsetR
    midtones_offsetr = midtonesOffsetR
    midtonesOffsetG = midtonesOffset.midtonesOffsetG
    midtones_offsetg = midtonesOffsetG
    midtonesOffsetB = midtonesOffset.midtonesOffsetB
    midtones_offsetb = midtonesOffsetB

    highlightsSaturation = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    highlights_saturation = highlightsSaturation

    highlightsContrast = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    highlights_contrast = highlightsContrast

    highlightsGamma = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=5.0
    )
    highlights_gamma = highlightsGamma

    highlightsGain = HighlightsGainField(default_value=(1.0, 1.0, 1.0))
    highlights_gain = highlightsGain
    highlightsGainR = highlightsGain.highlightsGainR
    highlights_gainr = highlightsGainR
    highlightsGainG = highlightsGain.highlightsGainG
    highlights_gaing = highlightsGainG
    highlightsGainB = highlightsGain.highlightsGainB
    highlights_gainb = highlightsGainB

    highlightsOffset = HighlightsOffsetField(default_value=(0.0, 0.0, 0.0))
    highlights_offset = highlightsOffset
    highlightsOffsetR = highlightsOffset.highlightsOffsetR
    highlights_offsetr = highlightsOffsetR
    highlightsOffsetG = highlightsOffset.highlightsOffsetG
    highlights_offsetg = highlightsOffsetG
    highlightsOffsetB = highlightsOffset.highlightsOffsetB
    highlights_offsetb = highlightsOffsetB
