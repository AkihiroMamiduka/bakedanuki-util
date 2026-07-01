# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_color_jitter import (
    InputField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class FaceModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FACE_ID = 0
    UNIFORM_ID = 1


class FaceModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FACE_ID = 0
    UNIFORM_ID = 1

    NAME_MAP = {
        FACE_ID: "face id",
        UNIFORM_ID: "uniform id",
    }


class FaceModeEnumField(
    EnumField[FaceModeEnumAttrOperator, FaceModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FaceModeEnumAttrOperator
    PLUG_CLS = FaceModeEnumPlugOperator


class AiColorJitter(DG):
    __slots__ = ()

    NODE_TYPE = "aiColorJitter"

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

    input = InputField()
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    dataInput = LongField()
    data_input = dataInput

    dataGainMin = FloatField()
    data_gain_min = dataGainMin

    dataGainMax = FloatField()
    data_gain_max = dataGainMax

    dataHueMin = FloatField()
    data_hue_min = dataHueMin

    dataHueMax = FloatField()
    data_hue_max = dataHueMax

    dataSaturationMin = FloatField()
    data_saturation_min = dataSaturationMin

    dataSaturationMax = FloatField()
    data_saturation_max = dataSaturationMax

    dataSeed = LongField()
    data_seed = dataSeed

    procGainMin = FloatField()
    proc_gain_min = procGainMin

    procGainMax = FloatField()
    proc_gain_max = procGainMax

    procHueMin = FloatField()
    proc_hue_min = procHueMin

    procHueMax = FloatField()
    proc_hue_max = procHueMax

    procSaturationMin = FloatField()
    proc_saturation_min = procSaturationMin

    procSaturationMax = FloatField()
    proc_saturation_max = procSaturationMax

    procSeed = LongField()
    proc_seed = procSeed

    objGainMin = FloatField()
    obj_gain_min = objGainMin

    objGainMax = FloatField()
    obj_gain_max = objGainMax

    objHueMin = FloatField()
    obj_hue_min = objHueMin

    objHueMax = FloatField()
    obj_hue_max = objHueMax

    objSaturationMin = FloatField()
    obj_saturation_min = objSaturationMin

    objSaturationMax = FloatField()
    obj_saturation_max = objSaturationMax

    objSeed = LongField()
    obj_seed = objSeed

    faceGainMin = FloatField()
    face_gain_min = faceGainMin

    faceGainMax = FloatField()
    face_gain_max = faceGainMax

    faceHueMin = FloatField()
    face_hue_min = faceHueMin

    faceHueMax = FloatField()
    face_hue_max = faceHueMax

    faceSaturationMin = FloatField()
    face_saturation_min = faceSaturationMin

    faceSaturationMax = FloatField()
    face_saturation_max = faceSaturationMax

    faceSeed = LongField()
    face_seed = faceSeed

    faceMode = FaceModeEnumField()
    face_mode = faceMode
