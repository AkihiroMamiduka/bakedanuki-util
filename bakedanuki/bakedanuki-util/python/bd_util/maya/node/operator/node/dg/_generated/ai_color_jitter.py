# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_color_jitter import (
    InputField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class FaceModeEnumPlugOperator(EnumPlugOperator["FaceModeEnumAttrOperator"]):
    __slots__ = ()

    FACE_ID = 0
    UNIFORM_ID = 1


class FaceModeEnumAttrOperator(EnumAttrOperator[FaceModeEnumPlugOperator]):
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


class GeneratedAiColorJitter(DG):
    __slots__ = ()

    NODE_TYPE = "aiColorJitter"

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

    input = InputField(default_value=(1.0, 1.0, 1.0))
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    dataInput = LongField(default_value=0)
    data_input = dataInput

    dataGainMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    data_gain_min = dataGainMin

    dataGainMax = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    data_gain_max = dataGainMax

    dataHueMin = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    data_hue_min = dataHueMin

    dataHueMax = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    data_hue_max = dataHueMax

    dataSaturationMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    data_saturation_min = dataSaturationMin

    dataSaturationMax = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    data_saturation_max = dataSaturationMax

    dataSeed = LongField(default_value=0)
    data_seed = dataSeed

    procGainMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    proc_gain_min = procGainMin

    procGainMax = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    proc_gain_max = procGainMax

    procHueMin = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    proc_hue_min = procHueMin

    procHueMax = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    proc_hue_max = procHueMax

    procSaturationMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    proc_saturation_min = procSaturationMin

    procSaturationMax = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    proc_saturation_max = procSaturationMax

    procSeed = LongField(default_value=0)
    proc_seed = procSeed

    objGainMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    obj_gain_min = objGainMin

    objGainMax = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    obj_gain_max = objGainMax

    objHueMin = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    obj_hue_min = objHueMin

    objHueMax = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    obj_hue_max = objHueMax

    objSaturationMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    obj_saturation_min = objSaturationMin

    objSaturationMax = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    obj_saturation_max = objSaturationMax

    objSeed = LongField(default_value=0)
    obj_seed = objSeed

    faceGainMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    face_gain_min = faceGainMin

    faceGainMax = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    face_gain_max = faceGainMax

    faceHueMin = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    face_hue_min = faceHueMin

    faceHueMax = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    face_hue_max = faceHueMax

    faceSaturationMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    face_saturation_min = faceSaturationMin

    faceSaturationMax = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    face_saturation_max = faceSaturationMax

    faceSeed = LongField(default_value=0)
    face_seed = faceSeed

    faceMode = FaceModeEnumField(default_value=0)
    face_mode = faceMode
