# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.use_background import (
    LightDataArrayField,
    NormalCameraField,
    OutColorField,
    OutMatteOpacityField,
    OutTransparencyField,
    PointCameraField,
    RayDirectionField,
    SpecularColorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.addr import AddrField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class MatteOpacityModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SOLID_MATTE = 1
    OPACITY_GAIN = 2


class MatteOpacityModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SOLID_MATTE = 1
    OPACITY_GAIN = 2

    NAME_MAP = {
        SOLID_MATTE: "Solid Matte",
        OPACITY_GAIN: "Opacity Gain",
    }


class MatteOpacityModeEnumField(
    EnumField[MatteOpacityModeEnumAttrOperator, MatteOpacityModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MatteOpacityModeEnumAttrOperator
    PLUG_CLS = MatteOpacityModeEnumPlugOperator


class UseBackground(DG):
    __slots__ = ()

    NODE_TYPE = "useBackground"

    objectId = AddrField(default_value=0.0, readable=False)
    oi = objectId

    primitiveId = LongField(default_value=0, readable=False)
    pi = primitiveId

    raySampler = AddrField(default_value=0.0, readable=False)
    rtr = raySampler

    backgroundSampler = AddrField(default_value=0.0, readable=False)
    rtb = backgroundSampler

    rayDepth = ShortField(default_value=0, readable=False)
    rd = rayDepth

    rayInstance = LongField(default_value=0, readable=False)
    ryi = rayInstance

    rayDirection = RayDirectionField(default_value=(0.0, 0.0, 1.0), readable=False)
    rad = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rdx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    rdy = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rdz = rayDirectionZ

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    pointCamera = PointCameraField(default_value=(1.0, 1.0, 1.0))
    pc = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    normalCamera = NormalCameraField(default_value=(1.0, 1.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    lightDataArray = LightDataArrayField(multi=True, readable=False)
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

    shadowMask = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    sm = shadowMask

    reflectionLimit = ShortField(default_value=2, min_value=0, soft_max_value=10)
    fll = reflectionLimit

    specularColor = SpecularColorField(default_value=(0.5, 0.5, 0.5))
    sc = specularColor
    specularColorR = specularColor.specularColorR
    sr = specularColorR
    specularColorG = specularColor.specularColorG
    sg = specularColorG
    specularColorB = specularColor.specularColorB
    sb = specularColorB

    reflectivity = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    rfl = reflectivity

    matteOpacityMode = MatteOpacityModeEnumField(default_value=2)
    mom = matteOpacityMode

    matteOpacity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    mog = matteOpacity

    outMatteOpacity = OutMatteOpacityField(default_value=(0.0, 0.0, 0.0), writable=False)
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB
