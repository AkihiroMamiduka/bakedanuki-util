# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_utility import (
    ColorField,
    HardwareColorField,
    NormalCameraField,
    NormalField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class ColorModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    COLOR = 0
    NG = 1
    NS = 2
    N = 3
    BARY = 4
    UV = 5
    U = 6
    V = 7
    DPDU = 8
    DPDV = 9
    P = 10
    PRIMS = 11
    UNIFORMID = 12
    WIRE = 13
    POLYWIRE = 14
    OBJ = 15
    EDGELENGTH = 16
    FLOATGRID = 17
    REFLECTLINE = 18
    BAD_UVS = 19
    NLIGHTS = 20
    ID = 21
    BUMPDIFF = 22
    PIXELERROR = 23


class ColorModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    COLOR = 0
    NG = 1
    NS = 2
    N = 3
    BARY = 4
    UV = 5
    U = 6
    V = 7
    DPDU = 8
    DPDV = 9
    P = 10
    PRIMS = 11
    UNIFORMID = 12
    WIRE = 13
    POLYWIRE = 14
    OBJ = 15
    EDGELENGTH = 16
    FLOATGRID = 17
    REFLECTLINE = 18
    BAD_UVS = 19
    NLIGHTS = 20
    ID = 21
    BUMPDIFF = 22
    PIXELERROR = 23

    NAME_MAP = {
        COLOR: "color",
        NG: "ng",
        NS: "ns",
        N: "n",
        BARY: "bary",
        UV: "uv",
        U: "u",
        V: "v",
        DPDU: "dpdu",
        DPDV: "dpdv",
        P: "p",
        PRIMS: "prims",
        UNIFORMID: "uniformid",
        WIRE: "wire",
        POLYWIRE: "polywire",
        OBJ: "obj",
        EDGELENGTH: "edgelength",
        FLOATGRID: "floatgrid",
        REFLECTLINE: "reflectline",
        BAD_UVS: "bad_uvs",
        NLIGHTS: "nlights",
        ID: "id",
        BUMPDIFF: "bumpdiff",
        PIXELERROR: "pixelerror",
    }


class ColorModeEnumField(
    EnumField[ColorModeEnumAttrOperator, ColorModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorModeEnumAttrOperator
    PLUG_CLS = ColorModeEnumPlugOperator


class ShadeModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NDOTEYE = 0
    LAMBERT = 1
    FLAT = 2
    AMBOCC = 3
    PLASTIC = 4
    METAL = 5


class ShadeModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NDOTEYE = 0
    LAMBERT = 1
    FLAT = 2
    AMBOCC = 3
    PLASTIC = 4
    METAL = 5

    NAME_MAP = {
        NDOTEYE: "ndoteye",
        LAMBERT: "lambert",
        FLAT: "flat",
        AMBOCC: "ambocc",
        PLASTIC: "plastic",
        METAL: "metal",
    }


class ShadeModeEnumField(
    EnumField[ShadeModeEnumAttrOperator, ShadeModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadeModeEnumAttrOperator
    PLUG_CLS = ShadeModeEnumPlugOperator


class OverlayModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    WIRE = 1
    POLYWIRE = 2


class OverlayModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    WIRE = 1
    POLYWIRE = 2

    NAME_MAP = {
        NONE: "none",
        WIRE: "wire",
        POLYWIRE: "polywire",
    }


class OverlayModeEnumField(
    EnumField[OverlayModeEnumAttrOperator, OverlayModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OverlayModeEnumAttrOperator
    PLUG_CLS = OverlayModeEnumPlugOperator


class _GeneratedAiUtility(DG):
    __slots__ = ()

    NODE_TYPE = "aiUtility"

    outColor = OutColorField(default_value=(0.5, 0.5, 0.5), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.5, 0.5, 0.5), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 0.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    hardwareColor = HardwareColorField(default_value=(0.5, 0.5, 0.5))
    hwc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hwcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hwcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hwcb = hardwareColorB

    colorMode = ColorModeEnumField(default_value=0)
    color_mode = colorMode

    shadeMode = ShadeModeEnumField(default_value=0)
    shade_mode = shadeMode

    overlayMode = OverlayModeEnumField(default_value=0)
    overlay_mode = overlayMode

    color = ColorField(default_value=(1.0, 1.0, 1.0))
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    aoDistance = FloatField(default_value=100.0, min_value=0.0, soft_max_value=200.0)
    ao_distance = aoDistance

    roughness = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=1.0)

    normal = NormalField(default_value=(0.0, 0.0, 0.0))
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ
