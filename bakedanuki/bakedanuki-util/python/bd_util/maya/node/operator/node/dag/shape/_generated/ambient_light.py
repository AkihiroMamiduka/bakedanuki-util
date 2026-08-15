# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.ambient_light import (
    ColorField,
    LightDataValueField,
    NormalCameraField,
    OpticalFXvisibilityField,
    PointCameraField,
    ShadowColorField,
    UvCoordField,
    UvFilterSizeField,
)
from .....attr.define.std.at.addr import AddrField
from .....attr.define.std.at.flt_matrix import FltMatrixField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.char import CharField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField


class GeneratedAmbientLight(Shape):
    __slots__ = ()

    NODE_TYPE = "ambientLight"

    color = ColorField(default_value=(1.0, 1.0, 1.0))
    cl = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    intensity = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    in_ = intensity

    useRayTraceShadows = BoolField(default_value=True)
    urs = useRayTraceShadows

    shadowColor = ShadowColorField(default_value=(0.0, 0.0, 0.0))
    sc = shadowColor
    shadColorR = shadowColor.shadColorR
    scr = shadColorR
    shadColorG = shadowColor.shadColorG
    scg = shadColorG
    shadColorB = shadowColor.shadColorB
    scb = shadColorB

    shadowRays = ShortField(default_value=1, min_value=1, soft_max_value=40)
    shr = shadowRays

    rayDepthLimit = ShortField(default_value=3, min_value=0, soft_max_value=10)
    rdl = rayDepthLimit

    centerOfIllumination = DoubleField(default_value=5.0, min_value=1e-10)
    col = centerOfIllumination

    pointCamera = PointCameraField(
        default_value=(1.0, 1.0, 1.0), readable=False
    )
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    matrixWorldToEye = FltMatrixField(readable=False)
    wte = matrixWorldToEye

    matrixEyeToWorld = FltMatrixField(readable=False)
    etw = matrixEyeToWorld

    objectId = AddrField(default_value=0.0, readable=False)
    oi = objectId

    primitiveId = LongField(default_value=0, readable=False)
    pi = primitiveId

    raySampler = AddrField(default_value=0.0, readable=False)
    rts = raySampler

    rayDepth = ShortField(default_value=0, readable=False)
    rd = rayDepth

    renderState = LongField(default_value=0, readable=False)
    rdst = renderState

    locatorScale = DoubleField(default_value=1.0, min_value=1e-10)
    lls = locatorScale

    uvCoord = UvCoordField(default_value=(0.0, 0.0), writable=False)
    uv = uvCoord
    uCoord = uvCoord.uCoord
    uu = uCoord
    vCoord = uvCoord.vCoord
    vv = vCoord

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0), writable=False)
    fq = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    infoBits = LongField(default_value=0)
    ib = infoBits

    lightData = LightDataValueField(writable=False)
    ltd = lightData
    lightDirection = lightData.lightDirection
    ld = lightDirection
    lightIntensity = lightData.lightIntensity
    li = lightIntensity
    lightAmbient = lightData.lightAmbient
    la = lightAmbient
    lightDiffuse = lightData.lightDiffuse
    ldf = lightDiffuse
    lightSpecular = lightData.lightSpecular
    ls = lightSpecular
    lightShadowFraction = lightData.lightShadowFraction
    lsf = lightShadowFraction
    preShadowIntensity = lightData.preShadowIntensity
    psi = preShadowIntensity
    lightBlindData = lightData.lightBlindData
    lbl = lightBlindData

    opticalFXvisibility = OpticalFXvisibilityField(
        default_value=(1.0, 1.0, 1.0), writable=False
    )
    ov = opticalFXvisibility
    opticalFXvisibilityR = opticalFXvisibility.opticalFXvisibilityR
    ovr = opticalFXvisibilityR
    opticalFXvisibilityG = opticalFXvisibility.opticalFXvisibilityG
    ovg = opticalFXvisibilityG
    opticalFXvisibilityB = opticalFXvisibility.opticalFXvisibilityB
    ovb = opticalFXvisibilityB

    rayInstance = LongField(default_value=0, readable=False)
    ryi = rayInstance

    ambientShade = FloatField(
        default_value=0.44999998807907104, min_value=0.0, max_value=1.0
    )
    as_ = ambientShade

    objectType = CharField(
        default_value=1, min_value=0, max_value=255, readable=False
    )
    ot = objectType

    shadowRadius = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    sr = shadowRadius

    castSoftShadows = BoolField(default_value=False)
    cw = castSoftShadows

    normalCamera = NormalCameraField(
        default_value=(1.0, 1.0, 1.0), readable=False
    )
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    receiveShadows = BoolField(default_value=True)
    gs = receiveShadows
