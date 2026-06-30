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

    # TODO: lightDataArray.lightDirectionX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightDirectionY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightDirectionZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    outValue = FloatField()
    o = outValue
