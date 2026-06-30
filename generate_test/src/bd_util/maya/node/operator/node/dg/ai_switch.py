# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_switch import (
    HardwareColorField,
    Input0Field,
    Input10Field,
    Input11Field,
    Input12Field,
    Input13Field,
    Input14Field,
    Input15Field,
    Input16Field,
    Input17Field,
    Input18Field,
    Input19Field,
    Input1Field,
    Input2Field,
    Input3Field,
    Input4Field,
    Input5Field,
    Input6Field,
    Input7Field,
    Input8Field,
    Input9Field,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class AiSwitch(DG):
    __slots__ = ()

    NODE_TYPE = "aiSwitch"

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

    index = LongField()

    input0A = FloatField()
    input0a = input0A

    input0 = Input0Field()
    input0R = input0.input0R
    input0r = input0R
    input0G = input0.input0G
    input0g = input0G
    input0B = input0.input0B
    input0b = input0B

    input1A = FloatField()
    input1a = input1A

    input1 = Input1Field()
    input1R = input1.input1R
    input1r = input1R
    input1G = input1.input1G
    input1g = input1G
    input1B = input1.input1B
    input1b = input1B

    input2A = FloatField()
    input2a = input2A

    input2 = Input2Field()
    input2R = input2.input2R
    input2r = input2R
    input2G = input2.input2G
    input2g = input2G
    input2B = input2.input2B
    input2b = input2B

    input3A = FloatField()
    input3a = input3A

    input3 = Input3Field()
    input3R = input3.input3R
    input3r = input3R
    input3G = input3.input3G
    input3g = input3G
    input3B = input3.input3B
    input3b = input3B

    input4A = FloatField()
    input4a = input4A

    input4 = Input4Field()
    input4R = input4.input4R
    input4r = input4R
    input4G = input4.input4G
    input4g = input4G
    input4B = input4.input4B
    input4b = input4B

    input5A = FloatField()
    input5a = input5A

    input5 = Input5Field()
    input5R = input5.input5R
    input5r = input5R
    input5G = input5.input5G
    input5g = input5G
    input5B = input5.input5B
    input5b = input5B

    input6A = FloatField()
    input6a = input6A

    input6 = Input6Field()
    input6R = input6.input6R
    input6r = input6R
    input6G = input6.input6G
    input6g = input6G
    input6B = input6.input6B
    input6b = input6B

    input7A = FloatField()
    input7a = input7A

    input7 = Input7Field()
    input7R = input7.input7R
    input7r = input7R
    input7G = input7.input7G
    input7g = input7G
    input7B = input7.input7B
    input7b = input7B

    input8A = FloatField()
    input8a = input8A

    input8 = Input8Field()
    input8R = input8.input8R
    input8r = input8R
    input8G = input8.input8G
    input8g = input8G
    input8B = input8.input8B
    input8b = input8B

    input9A = FloatField()
    input9a = input9A

    input9 = Input9Field()
    input9R = input9.input9R
    input9r = input9R
    input9G = input9.input9G
    input9g = input9G
    input9B = input9.input9B
    input9b = input9B

    input10A = FloatField()
    input10a = input10A

    input10 = Input10Field()
    input10R = input10.input10R
    input10r = input10R
    input10G = input10.input10G
    input10g = input10G
    input10B = input10.input10B
    input10b = input10B

    input11A = FloatField()
    input11a = input11A

    input11 = Input11Field()
    input11R = input11.input11R
    input11r = input11R
    input11G = input11.input11G
    input11g = input11G
    input11B = input11.input11B
    input11b = input11B

    input12A = FloatField()
    input12a = input12A

    input12 = Input12Field()
    input12R = input12.input12R
    input12r = input12R
    input12G = input12.input12G
    input12g = input12G
    input12B = input12.input12B
    input12b = input12B

    input13A = FloatField()
    input13a = input13A

    input13 = Input13Field()
    input13R = input13.input13R
    input13r = input13R
    input13G = input13.input13G
    input13g = input13G
    input13B = input13.input13B
    input13b = input13B

    input14A = FloatField()
    input14a = input14A

    input14 = Input14Field()
    input14R = input14.input14R
    input14r = input14R
    input14G = input14.input14G
    input14g = input14G
    input14B = input14.input14B
    input14b = input14B

    input15A = FloatField()
    input15a = input15A

    input15 = Input15Field()
    input15R = input15.input15R
    input15r = input15R
    input15G = input15.input15G
    input15g = input15G
    input15B = input15.input15B
    input15b = input15B

    input16A = FloatField()
    input16a = input16A

    input16 = Input16Field()
    input16R = input16.input16R
    input16r = input16R
    input16G = input16.input16G
    input16g = input16G
    input16B = input16.input16B
    input16b = input16B

    input17A = FloatField()
    input17a = input17A

    input17 = Input17Field()
    input17R = input17.input17R
    input17r = input17R
    input17G = input17.input17G
    input17g = input17G
    input17B = input17.input17B
    input17b = input17B

    input18A = FloatField()
    input18a = input18A

    input18 = Input18Field()
    input18R = input18.input18R
    input18r = input18R
    input18G = input18.input18G
    input18g = input18G
    input18B = input18.input18B
    input18b = input18B

    input19A = FloatField()
    input19a = input19A

    input19 = Input19Field()
    input19R = input19.input19R
    input19r = input19R
    input19G = input19.input19G
    input19g = input19G
    input19B = input19.input19B
    input19b = input19B
