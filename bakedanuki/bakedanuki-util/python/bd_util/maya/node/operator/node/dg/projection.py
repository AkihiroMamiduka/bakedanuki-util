# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.projection import (
    CamAgField,
    CamPosField,
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    DefaultTransparencyField,
    DepthField,
    FilterSizeField,
    ImageField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
    PointCameraField,
    PointObjField,
    RefPointCameraField,
    RefPointObjField,
    RipplesField,
    SrfNormalField,
    TangentUCameraField,
    TangentVCameraField,
    TransparencyField,
    TransparencyGainField,
    TransparencyOffsetField,
    UvCoordField,
    UvFilterSizeField,
    VertexCameraOneField,
    VertexCameraThreeField,
    VertexCameraTwoField,
    VertexUvOneField,
    VertexUvThreeField,
    VertexUvTwoField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.dt.string import DataStringField


class ProjTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    PLANAR = 1
    SPHERICAL = 2
    CYLINDRICAL = 3
    BALL = 4
    CUBIC = 5
    TRIPLANAR = 6
    CONCENTRIC = 7
    PERSPECTIVE = 8


class ProjTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    PLANAR = 1
    SPHERICAL = 2
    CYLINDRICAL = 3
    BALL = 4
    CUBIC = 5
    TRIPLANAR = 6
    CONCENTRIC = 7
    PERSPECTIVE = 8

    NAME_MAP = {
        OFF: "Off",
        PLANAR: "Planar",
        SPHERICAL: "Spherical",
        CYLINDRICAL: "Cylindrical",
        BALL: "Ball",
        CUBIC: "Cubic",
        TRIPLANAR: "TriPlanar",
        CONCENTRIC: "Concentric",
        PERSPECTIVE: "Perspective",
    }


class ProjTypeEnumField(
    EnumField[ProjTypeEnumAttrOperator, ProjTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProjTypeEnumAttrOperator
    PLUG_CLS = ProjTypeEnumPlugOperator


class FitTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    MATCH_CAMERA_FILM_GATE = 1
    MATCH_CAMERA_RESOLUTION = 2


class FitTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    MATCH_CAMERA_FILM_GATE = 1
    MATCH_CAMERA_RESOLUTION = 2

    NAME_MAP = {
        NONE: "None",
        MATCH_CAMERA_FILM_GATE: "Match Camera Film Gate",
        MATCH_CAMERA_RESOLUTION: "Match Camera Resolution",
    }


class FitTypeEnumField(
    EnumField[FitTypeEnumAttrOperator, FitTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FitTypeEnumAttrOperator
    PLUG_CLS = FitTypeEnumPlugOperator


class FitFillEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FILL = 0
    HORIZONTAL = 1
    VERTICAL = 2


class FitFillEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FILL = 0
    HORIZONTAL = 1
    VERTICAL = 2

    NAME_MAP = {
        FILL: "Fill",
        HORIZONTAL: "Horizontal",
        VERTICAL: "Vertical",
    }


class FitFillEnumField(
    EnumField[FitFillEnumAttrOperator, FitFillEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FitFillEnumAttrOperator
    PLUG_CLS = FitFillEnumPlugOperator


class Projection(DG):
    __slots__ = ()

    NODE_TYPE = "projection"

    pointObj = PointObjField(default_value=(0.0, 0.0, 0.0))
    po = pointObj
    pointObjX = pointObj.pointObjX
    pox = pointObjX
    pointObjY = pointObj.pointObjY
    poy = pointObjY
    pointObjZ = pointObj.pointObjZ
    poz = pointObjZ

    pointCamera = PointCameraField(default_value=(0.0, 0.0, 0.0))
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    filterSize = FilterSizeField(default_value=(0.0, 0.0, 0.0))
    fs = filterSize
    filterSizeX = filterSize.filterSizeX
    fsx = filterSizeX
    filterSizeY = filterSize.filterSizeY
    fsy = filterSizeY
    filterSizeZ = filterSize.filterSizeZ
    fsz = filterSizeZ

    placementMatrix = FltMatrixField()
    pm = placementMatrix

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    filter = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    f = filter

    filterOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fo = filterOffset

    blend = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    b = blend

    local = BoolField(default_value=False)
    lo = local

    wrap = BoolField(default_value=True)
    w = wrap

    invert = BoolField(default_value=False)
    i = invert

    alphaIsLuminance = BoolField(default_value=False)
    ail = alphaIsLuminance

    colorGain = ColorGainField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    ag = alphaGain

    alphaOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    ao = alphaOffset

    defaultColor = DefaultColorField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    oa = outAlpha

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    srfNormal = SrfNormalField(default_value=(0.0, 0.0, 1.0))
    srn = srfNormal
    srfNormalX = srfNormal.srfNormalX
    snx = srfNormalX
    srfNormalY = srfNormal.srfNormalY
    sny = srfNormalY
    srfNormalZ = srfNormal.srfNormalZ
    snz = srfNormalZ

    refPointObj = RefPointObjField(default_value=(0.0, 0.0, 0.0))
    rpo = refPointObj
    refPointObjX = refPointObj.refPointObjX
    rox = refPointObjX
    refPointObjY = refPointObj.refPointObjY
    roy = refPointObjY
    refPointObjZ = refPointObj.refPointObjZ
    roz = refPointObjZ

    refPointCamera = RefPointCameraField(default_value=(0.0, 0.0, 0.0))
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ

    xPixelAngle = FloatField(default_value=0.002053000032901764, readable=False)
    xpa = xPixelAngle

    image = ImageField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    im = image
    imageR = image.imageR
    imr = imageR
    imageG = image.imageG
    img = imageG
    imageB = image.imageB
    imb = imageB

    transparency = TransparencyField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    it = transparency
    transparencyR = transparency.transparencyR
    itr = transparencyR
    transparencyG = transparency.transparencyG
    itg = transparencyG
    transparencyB = transparency.transparencyB
    itb = transparencyB

    uAngle = DoubleAngleField(default_value=180.0, min_value=0.0, max_value=360.0)
    ua = uAngle

    vAngle = DoubleAngleField(default_value=90.0, min_value=0.0, max_value=180.0)
    va = vAngle

    projType = ProjTypeEnumField(default_value=1)
    t = projType

    linkedCamera = MessageField()
    lc = linkedCamera

    fitType = FitTypeEnumField(default_value=1)
    ft = fitType

    fitFill = FitFillEnumField(default_value=0)
    ff = fitFill

    ripples = RipplesField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(20.0, 20.0, 20.0))
    r = ripples
    ripplesX = ripples.ripplesX
    rx = ripplesX
    ripplesY = ripples.ripplesY
    ry = ripplesY
    ripplesZ = ripples.ripplesZ
    rz = ripplesZ

    depth = DepthField(default_value=(0.0, 10.0), min_value=(0.0, 0.0), max_value=(25.0, 25.0))
    d = depth
    depthMin = depth.depthMin
    dmn = depthMin
    depthMax = depth.depthMax
    dmx = depthMax

    amplitudeX = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ax = amplitudeX

    amplitudeY = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ay = amplitudeY

    ratio = FloatField(default_value=0.30000001192092896, min_value=0.0, max_value=1.0)
    ra = ratio

    infoBits = LongField(default_value=0)
    ib = infoBits

    depWts = FloatField(default_value=0.0, writable=False)
    dwt = depWts

    angWts = FloatField(default_value=0.0, writable=False)
    awt = angWts

    camPos = CamPosField(default_value=(0.0, 0.0, 0.0))
    cpo = camPos
    camPsX = camPos.camPsX
    cpx = camPsX
    camPsY = camPos.camPsY
    cpy = camPsY
    camPsZ = camPos.camPsZ
    cpz = camPsZ

    camAg = CamAgField(default_value=(0.0, 0.0, 0.0))
    cag = camAg
    camAngX = camAg.camAngX
    cax = camAngX
    camAngY = camAg.camAngY
    cay = camAngY
    camAngZ = camAg.camAngZ
    caz = camAngZ

    passTr = BoolField(default_value=False)
    pst = passTr

    transparencyGain = TransparencyGainField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    tg = transparencyGain
    transparencyGainR = transparencyGain.transparencyGainR
    tgr = transparencyGainR
    transparencyGainG = transparencyGain.transparencyGainG
    tgg = transparencyGainG
    transparencyGainB = transparencyGain.transparencyGainB
    tgb = transparencyGainB

    transparencyOffset = TransparencyOffsetField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    to = transparencyOffset
    transparencyOffsetR = transparencyOffset.transparencyOffsetR
    tor = transparencyOffsetR
    transparencyOffsetG = transparencyOffset.transparencyOffsetG
    tog = transparencyOffsetG
    transparencyOffsetB = transparencyOffset.transparencyOffsetB
    tob = transparencyOffsetB

    defaultTransparency = DefaultTransparencyField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    dt = defaultTransparency
    defaultTransparencyR = defaultTransparency.defaultTransparencyR
    dtr = defaultTransparencyR
    defaultTransparencyG = defaultTransparency.defaultTransparencyG
    dtg = defaultTransparencyG
    defaultTransparencyB = defaultTransparency.defaultTransparencyB
    dtb = defaultTransparencyB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    vertexCameraOne = VertexCameraOneField(default_value=(0.0, 0.0, 0.0))
    vc1 = vertexCameraOne
    vertexCameraOneX = vertexCameraOne.vertexCameraOneX
    c1x = vertexCameraOneX
    vertexCameraOneY = vertexCameraOne.vertexCameraOneY
    c1y = vertexCameraOneY
    vertexCameraOneZ = vertexCameraOne.vertexCameraOneZ
    c1z = vertexCameraOneZ

    vertexCameraTwo = VertexCameraTwoField(default_value=(0.0, 0.0, 0.0))
    vc2 = vertexCameraTwo
    vertexCameraTwoX = vertexCameraTwo.vertexCameraTwoX
    c2x = vertexCameraTwoX
    vertexCameraTwoY = vertexCameraTwo.vertexCameraTwoY
    c2y = vertexCameraTwoY
    vertexCameraTwoZ = vertexCameraTwo.vertexCameraTwoZ
    c2z = vertexCameraTwoZ

    vertexCameraThree = VertexCameraThreeField(default_value=(0.0, 0.0, 0.0))
    vc3 = vertexCameraThree
    vertexCameraThreeX = vertexCameraThree.vertexCameraThreeX
    c3x = vertexCameraThreeX
    vertexCameraThreeY = vertexCameraThree.vertexCameraThreeY
    c3y = vertexCameraThreeY
    vertexCameraThreeZ = vertexCameraThree.vertexCameraThreeZ
    c3z = vertexCameraThreeZ

    vertexUvOne = VertexUvOneField(default_value=(0.0, 0.0))
    vt1 = vertexUvOne
    vertexUvOneU = vertexUvOne.vertexUvOneU
    t1u = vertexUvOneU
    vertexUvOneV = vertexUvOne.vertexUvOneV
    t1v = vertexUvOneV

    vertexUvTwo = VertexUvTwoField(default_value=(0.0, 0.0))
    vt2 = vertexUvTwo
    vertexUvTwoU = vertexUvTwo.vertexUvTwoU
    t2u = vertexUvTwoU
    vertexUvTwoV = vertexUvTwo.vertexUvTwoV
    t2v = vertexUvTwoV

    vertexUvThree = VertexUvThreeField(default_value=(0.0, 0.0))
    vt3 = vertexUvThree
    vertexUvThreeU = vertexUvThree.vertexUvThreeU
    t3u = vertexUvThreeU
    vertexUvThreeV = vertexUvThree.vertexUvThreeV
    t3v = vertexUvThreeV

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0))
    uf = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    ufx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    ufy = uvFilterSizeY

    tangentUCamera = TangentUCameraField(default_value=(1.0, 0.0, 0.0))
    tu = tangentUCamera
    tangentUx = tangentUCamera.tangentUx
    tux = tangentUx
    tangentUy = tangentUCamera.tangentUy
    tuy = tangentUy
    tangentUz = tangentUCamera.tangentUz
    tuz = tangentUz

    tangentVCamera = TangentVCameraField(default_value=(0.0, 1.0, 0.0))
    tv = tangentVCamera
    tangentVx = tangentVCamera.tangentVx
    tvx = tangentVx
    tangentVy = tangentVCamera.tangentVy
    tvy = tangentVy
    tangentVz = tangentVCamera.tangentVz
    tvz = tangentVz

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiUseReferenceObject = BoolField(default_value=True, category="arnold")
    ai_use_reference_object = aiUseReferenceObject
