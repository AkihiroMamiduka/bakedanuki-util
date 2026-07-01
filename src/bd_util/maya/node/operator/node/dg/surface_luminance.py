# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.surface_luminance import (
    LightDataArrayField,
    NormalCameraField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class SurfaceLuminance(DG):
    __slots__ = ()

    NODE_TYPE = "surfaceLuminance"

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    lightDataArray = LightDataArrayField(multi=True)
    ltd = lightDataArray

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ

    lightIntensityR = FloatField()
    lir = lightIntensityR

    lightIntensityG = FloatField()
    lig = lightIntensityG

    lightIntensityB = FloatField()
    lib = lightIntensityB

    outValue = FloatField()
    o = outValue
