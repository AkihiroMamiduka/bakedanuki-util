# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_ambient_occlusion import (
    BlackField,
    HardwareColorField,
    NormalCameraField,
    NormalField,
    OutColorField,
    OutTransparencyField,
    WhiteField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiAmbientOcclusion(DG):
    __slots__ = ()

    NODE_TYPE = "aiAmbientOcclusion"

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

    samples = LongField(default_value=3, min_value=0, soft_max_value=10)

    spread = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    nearClip = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)
    near_clip = nearClip

    farClip = FloatField(default_value=100.0, min_value=0.0, soft_max_value=2000.0)
    far_clip = farClip

    falloff = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    black = BlackField(default_value=(0.0, 0.0, 0.0))
    blackR = black.blackR
    blackr = blackR
    blackG = black.blackG
    blackg = blackG
    blackB = black.blackB
    blackb = blackB

    white = WhiteField(default_value=(1.0, 1.0, 1.0))
    whiteR = white.whiteR
    whiter = whiteR
    whiteG = white.whiteG
    whiteg = whiteG
    whiteB = white.whiteB
    whiteb = whiteB

    normal = NormalField(default_value=(0.0, 0.0, 0.0))
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ

    invertNormals = BoolField(default_value=False)
    invert_normals = invertNormals

    traceSet = DataStringField()
    trace_set = traceSet

    inclusive = BoolField(default_value=True)

    selfOnly = BoolField(default_value=False)
    self_only = selfOnly
