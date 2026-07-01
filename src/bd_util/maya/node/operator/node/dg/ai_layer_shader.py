# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_layer_shader import (
    HardwareColorField,
    Input1Field,
    Input2Field,
    Input3Field,
    Input4Field,
    Input5Field,
    Input6Field,
    Input7Field,
    Input8Field,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiLayerShader(DG):
    __slots__ = ()

    NODE_TYPE = "aiLayerShader"

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

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    hardwareColor = HardwareColorField()
    hwc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hwcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hwcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hwcb = hardwareColorB

    enable1 = BoolField()

    name1 = DataStringField()

    input1A = FloatField()
    input1a = input1A

    input1 = Input1Field()
    input1R = input1.input1R
    input1r = input1R
    input1G = input1.input1G
    input1g = input1G
    input1B = input1.input1B
    input1b = input1B

    mix1 = FloatField()

    enable2 = BoolField()

    name2 = DataStringField()

    input2A = FloatField()
    input2a = input2A

    input2 = Input2Field()
    input2R = input2.input2R
    input2r = input2R
    input2G = input2.input2G
    input2g = input2G
    input2B = input2.input2B
    input2b = input2B

    mix2 = FloatField()

    enable3 = BoolField()

    name3 = DataStringField()

    input3A = FloatField()
    input3a = input3A

    input3 = Input3Field()
    input3R = input3.input3R
    input3r = input3R
    input3G = input3.input3G
    input3g = input3G
    input3B = input3.input3B
    input3b = input3B

    mix3 = FloatField()

    enable4 = BoolField()

    name4 = DataStringField()

    input4A = FloatField()
    input4a = input4A

    input4 = Input4Field()
    input4R = input4.input4R
    input4r = input4R
    input4G = input4.input4G
    input4g = input4G
    input4B = input4.input4B
    input4b = input4B

    mix4 = FloatField()

    enable5 = BoolField()

    name5 = DataStringField()

    input5A = FloatField()
    input5a = input5A

    input5 = Input5Field()
    input5R = input5.input5R
    input5r = input5R
    input5G = input5.input5G
    input5g = input5G
    input5B = input5.input5B
    input5b = input5B

    mix5 = FloatField()

    enable6 = BoolField()

    name6 = DataStringField()

    input6A = FloatField()
    input6a = input6A

    input6 = Input6Field()
    input6R = input6.input6R
    input6r = input6R
    input6G = input6.input6G
    input6g = input6G
    input6B = input6.input6B
    input6b = input6B

    mix6 = FloatField()

    enable7 = BoolField()

    name7 = DataStringField()

    input7A = FloatField()
    input7a = input7A

    input7 = Input7Field()
    input7R = input7.input7R
    input7r = input7R
    input7G = input7.input7G
    input7g = input7G
    input7B = input7.input7B
    input7b = input7B

    mix7 = FloatField()

    enable8 = BoolField()

    name8 = DataStringField()

    input8A = FloatField()
    input8a = input8A

    input8 = Input8Field()
    input8R = input8.input8R
    input8r = input8R
    input8G = input8.input8G
    input8g = input8G
    input8B = input8.input8B
    input8b = input8B

    mix8 = FloatField()
