# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_clip_geo import (
    HardwareColorField,
    IntersectionField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiClipGeo(DG):
    __slots__ = ()

    NODE_TYPE = "aiClipGeo"

    outColor = OutColorField(default_value=(0.5, 0.5, 0.5), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(
        default_value=(0.5, 0.5, 0.5), writable=False
    )
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

    intersectionA = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    intersectiona = intersectionA

    intersection = IntersectionField(default_value=(0.0, 0.0, 0.0))
    intersectionR = intersection.intersectionR
    intersectionr = intersectionR
    intersectionG = intersection.intersectionG
    intersectiong = intersectionG
    intersectionB = intersection.intersectionB
    intersectionb = intersectionB

    traceSet = DataStringField()
    trace_set = traceSet

    inclusive = BoolField(default_value=True)
