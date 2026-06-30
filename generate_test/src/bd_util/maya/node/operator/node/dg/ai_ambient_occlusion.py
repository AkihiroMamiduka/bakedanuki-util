# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_ambient_occlusion import (
    BlackField,
    HardwareColorField,
    NormalCameraField,
    NormalField,
    OutColorField,
    OutTransparencyField,
    WhiteField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class AiAmbientOcclusion(DG):
    __slots__ = ()

    NODE_TYPE = "aiAmbientOcclusion"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

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

    samples = LongField()

    spread = FloatField()

    nearClip = FloatField()
    near_clip = nearClip

    farClip = FloatField()
    far_clip = farClip

    falloff = FloatField()

    black = BlackField()
    blackR = black.blackR
    blackr = blackR
    blackG = black.blackG
    blackg = blackG
    blackB = black.blackB
    blackb = blackB

    white = WhiteField()
    whiteR = white.whiteR
    whiter = whiteR
    whiteG = white.whiteG
    whiteg = whiteG
    whiteB = white.whiteB
    whiteb = whiteB

    normal = NormalField()
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ

    invertNormals = BoolField()
    invert_normals = invertNormals

    traceSet = DataStringField()
    trace_set = traceSet

    inclusive = BoolField()

    selfOnly = BoolField()
    self_only = selfOnly
