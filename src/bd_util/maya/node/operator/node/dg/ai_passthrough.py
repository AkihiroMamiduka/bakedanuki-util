# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_passthrough import (
    Eval10Field,
    Eval11Field,
    Eval12Field,
    Eval13Field,
    Eval14Field,
    Eval15Field,
    Eval16Field,
    Eval17Field,
    Eval18Field,
    Eval19Field,
    Eval1Field,
    Eval20Field,
    Eval2Field,
    Eval3Field,
    Eval4Field,
    Eval5Field,
    Eval6Field,
    Eval7Field,
    Eval8Field,
    Eval9Field,
    HardwareColorField,
    NormalCameraField,
    NormalField,
    OutColorField,
    OutTransparencyField,
    PassthroughField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiPassthrough(DG):
    __slots__ = ()

    NODE_TYPE = "aiPassthrough"

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

    passthroughA = FloatField()
    passthrougha = passthroughA

    passthrough = PassthroughField()
    passthroughR = passthrough.passthroughR
    passthroughr = passthroughR
    passthroughG = passthrough.passthroughG
    passthroughg = passthroughG
    passthroughB = passthrough.passthroughB
    passthroughb = passthroughB

    eval1A = FloatField()
    eval1a = eval1A

    eval1 = Eval1Field()
    eval1R = eval1.eval1R
    eval1r = eval1R
    eval1G = eval1.eval1G
    eval1g = eval1G
    eval1B = eval1.eval1B
    eval1b = eval1B

    eval2A = FloatField()
    eval2a = eval2A

    eval2 = Eval2Field()
    eval2R = eval2.eval2R
    eval2r = eval2R
    eval2G = eval2.eval2G
    eval2g = eval2G
    eval2B = eval2.eval2B
    eval2b = eval2B

    eval3A = FloatField()
    eval3a = eval3A

    eval3 = Eval3Field()
    eval3R = eval3.eval3R
    eval3r = eval3R
    eval3G = eval3.eval3G
    eval3g = eval3G
    eval3B = eval3.eval3B
    eval3b = eval3B

    eval4A = FloatField()
    eval4a = eval4A

    eval4 = Eval4Field()
    eval4R = eval4.eval4R
    eval4r = eval4R
    eval4G = eval4.eval4G
    eval4g = eval4G
    eval4B = eval4.eval4B
    eval4b = eval4B

    eval5A = FloatField()
    eval5a = eval5A

    eval5 = Eval5Field()
    eval5R = eval5.eval5R
    eval5r = eval5R
    eval5G = eval5.eval5G
    eval5g = eval5G
    eval5B = eval5.eval5B
    eval5b = eval5B

    eval6A = FloatField()
    eval6a = eval6A

    eval6 = Eval6Field()
    eval6R = eval6.eval6R
    eval6r = eval6R
    eval6G = eval6.eval6G
    eval6g = eval6G
    eval6B = eval6.eval6B
    eval6b = eval6B

    eval7A = FloatField()
    eval7a = eval7A

    eval7 = Eval7Field()
    eval7R = eval7.eval7R
    eval7r = eval7R
    eval7G = eval7.eval7G
    eval7g = eval7G
    eval7B = eval7.eval7B
    eval7b = eval7B

    eval8A = FloatField()
    eval8a = eval8A

    eval8 = Eval8Field()
    eval8R = eval8.eval8R
    eval8r = eval8R
    eval8G = eval8.eval8G
    eval8g = eval8G
    eval8B = eval8.eval8B
    eval8b = eval8B

    eval9A = FloatField()
    eval9a = eval9A

    eval9 = Eval9Field()
    eval9R = eval9.eval9R
    eval9r = eval9R
    eval9G = eval9.eval9G
    eval9g = eval9G
    eval9B = eval9.eval9B
    eval9b = eval9B

    eval10A = FloatField()
    eval10a = eval10A

    eval10 = Eval10Field()
    eval10R = eval10.eval10R
    eval10r = eval10R
    eval10G = eval10.eval10G
    eval10g = eval10G
    eval10B = eval10.eval10B
    eval10b = eval10B

    eval11A = FloatField()
    eval11a = eval11A

    eval11 = Eval11Field()
    eval11R = eval11.eval11R
    eval11r = eval11R
    eval11G = eval11.eval11G
    eval11g = eval11G
    eval11B = eval11.eval11B
    eval11b = eval11B

    eval12A = FloatField()
    eval12a = eval12A

    eval12 = Eval12Field()
    eval12R = eval12.eval12R
    eval12r = eval12R
    eval12G = eval12.eval12G
    eval12g = eval12G
    eval12B = eval12.eval12B
    eval12b = eval12B

    eval13A = FloatField()
    eval13a = eval13A

    eval13 = Eval13Field()
    eval13R = eval13.eval13R
    eval13r = eval13R
    eval13G = eval13.eval13G
    eval13g = eval13G
    eval13B = eval13.eval13B
    eval13b = eval13B

    eval14A = FloatField()
    eval14a = eval14A

    eval14 = Eval14Field()
    eval14R = eval14.eval14R
    eval14r = eval14R
    eval14G = eval14.eval14G
    eval14g = eval14G
    eval14B = eval14.eval14B
    eval14b = eval14B

    eval15A = FloatField()
    eval15a = eval15A

    eval15 = Eval15Field()
    eval15R = eval15.eval15R
    eval15r = eval15R
    eval15G = eval15.eval15G
    eval15g = eval15G
    eval15B = eval15.eval15B
    eval15b = eval15B

    eval16A = FloatField()
    eval16a = eval16A

    eval16 = Eval16Field()
    eval16R = eval16.eval16R
    eval16r = eval16R
    eval16G = eval16.eval16G
    eval16g = eval16G
    eval16B = eval16.eval16B
    eval16b = eval16B

    eval17A = FloatField()
    eval17a = eval17A

    eval17 = Eval17Field()
    eval17R = eval17.eval17R
    eval17r = eval17R
    eval17G = eval17.eval17G
    eval17g = eval17G
    eval17B = eval17.eval17B
    eval17b = eval17B

    eval18A = FloatField()
    eval18a = eval18A

    eval18 = Eval18Field()
    eval18R = eval18.eval18R
    eval18r = eval18R
    eval18G = eval18.eval18G
    eval18g = eval18G
    eval18B = eval18.eval18B
    eval18b = eval18B

    eval19A = FloatField()
    eval19a = eval19A

    eval19 = Eval19Field()
    eval19R = eval19.eval19R
    eval19r = eval19R
    eval19G = eval19.eval19G
    eval19g = eval19G
    eval19B = eval19.eval19B
    eval19b = eval19B

    eval20A = FloatField()
    eval20a = eval20A

    eval20 = Eval20Field()
    eval20R = eval20.eval20R
    eval20r = eval20R
    eval20G = eval20.eval20G
    eval20g = eval20G
    eval20B = eval20.eval20B
    eval20b = eval20B

    normal = NormalField()
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ
