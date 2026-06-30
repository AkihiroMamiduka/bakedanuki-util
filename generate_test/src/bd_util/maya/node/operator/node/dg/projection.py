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

    pointObj = PointObjField()
    po = pointObj
    pointObjX = pointObj.pointObjX
    pox = pointObjX
    pointObjY = pointObj.pointObjY
    poy = pointObjY
    pointObjZ = pointObj.pointObjZ
    poz = pointObjZ

    pointCamera = PointCameraField()
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    filterSize = FilterSizeField()
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

    filter = FloatField()
    f = filter

    filterOffset = FloatField()
    fo = filterOffset

    blend = FloatField()
    b = blend

    local = BoolField()
    lo = local

    wrap = BoolField()
    w = wrap

    invert = BoolField()
    i = invert

    alphaIsLuminance = BoolField()
    ail = alphaIsLuminance

    colorGain = ColorGainField()
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField()
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField()
    ag = alphaGain

    alphaOffset = FloatField()
    ao = alphaOffset

    defaultColor = DefaultColorField()
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField()
    oa = outAlpha

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    srfNormal = SrfNormalField()
    srn = srfNormal
    srfNormalX = srfNormal.srfNormalX
    snx = srfNormalX
    srfNormalY = srfNormal.srfNormalY
    sny = srfNormalY
    srfNormalZ = srfNormal.srfNormalZ
    snz = srfNormalZ

    refPointObj = RefPointObjField()
    rpo = refPointObj
    refPointObjX = refPointObj.refPointObjX
    rox = refPointObjX
    refPointObjY = refPointObj.refPointObjY
    roy = refPointObjY
    refPointObjZ = refPointObj.refPointObjZ
    roz = refPointObjZ

    refPointCamera = RefPointCameraField()
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ

    xPixelAngle = FloatField()
    xpa = xPixelAngle

    image = ImageField()
    im = image
    imageR = image.imageR
    imr = imageR
    imageG = image.imageG
    img = imageG
    imageB = image.imageB
    imb = imageB

    transparency = TransparencyField()
    it = transparency
    transparencyR = transparency.transparencyR
    itr = transparencyR
    transparencyG = transparency.transparencyG
    itg = transparencyG
    transparencyB = transparency.transparencyB
    itb = transparencyB

    uAngle = DoubleAngleField()
    ua = uAngle

    vAngle = DoubleAngleField()
    va = vAngle

    projType = ProjTypeEnumField()
    t = projType

    linkedCamera = MessageField()
    lc = linkedCamera

    fitType = FitTypeEnumField()
    ft = fitType

    fitFill = FitFillEnumField()
    ff = fitFill

    ripples = RipplesField()
    r = ripples
    ripplesX = ripples.ripplesX
    rx = ripplesX
    ripplesY = ripples.ripplesY
    ry = ripplesY
    ripplesZ = ripples.ripplesZ
    rz = ripplesZ

    depth = DepthField()
    d = depth
    depthMin = depth.depthMin
    dmn = depthMin
    depthMax = depth.depthMax
    dmx = depthMax

    amplitudeX = FloatField()
    ax = amplitudeX

    amplitudeY = FloatField()
    ay = amplitudeY

    ratio = FloatField()
    ra = ratio

    infoBits = LongField()
    ib = infoBits

    depWts = FloatField()
    dwt = depWts

    angWts = FloatField()
    awt = angWts

    camPos = CamPosField()
    cpo = camPos
    camPsX = camPos.camPsX
    cpx = camPsX
    camPsY = camPos.camPsY
    cpy = camPsY
    camPsZ = camPos.camPsZ
    cpz = camPsZ

    camAg = CamAgField()
    cag = camAg
    camAngX = camAg.camAngX
    cax = camAngX
    camAngY = camAg.camAngY
    cay = camAngY
    camAngZ = camAg.camAngZ
    caz = camAngZ

    passTr = BoolField()
    pst = passTr

    transparencyGain = TransparencyGainField()
    tg = transparencyGain
    transparencyGainR = transparencyGain.transparencyGainR
    tgr = transparencyGainR
    transparencyGainG = transparencyGain.transparencyGainG
    tgg = transparencyGainG
    transparencyGainB = transparencyGain.transparencyGainB
    tgb = transparencyGainB

    transparencyOffset = TransparencyOffsetField()
    to = transparencyOffset
    transparencyOffsetR = transparencyOffset.transparencyOffsetR
    tor = transparencyOffsetR
    transparencyOffsetG = transparencyOffset.transparencyOffsetG
    tog = transparencyOffsetG
    transparencyOffsetB = transparencyOffset.transparencyOffsetB
    tob = transparencyOffsetB

    defaultTransparency = DefaultTransparencyField()
    dt = defaultTransparency
    defaultTransparencyR = defaultTransparency.defaultTransparencyR
    dtr = defaultTransparencyR
    defaultTransparencyG = defaultTransparency.defaultTransparencyG
    dtg = defaultTransparencyG
    defaultTransparencyB = defaultTransparency.defaultTransparencyB
    dtb = defaultTransparencyB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    vertexCameraOne = VertexCameraOneField()
    vc1 = vertexCameraOne
    vertexCameraOneX = vertexCameraOne.vertexCameraOneX
    c1x = vertexCameraOneX
    vertexCameraOneY = vertexCameraOne.vertexCameraOneY
    c1y = vertexCameraOneY
    vertexCameraOneZ = vertexCameraOne.vertexCameraOneZ
    c1z = vertexCameraOneZ

    vertexCameraTwo = VertexCameraTwoField()
    vc2 = vertexCameraTwo
    vertexCameraTwoX = vertexCameraTwo.vertexCameraTwoX
    c2x = vertexCameraTwoX
    vertexCameraTwoY = vertexCameraTwo.vertexCameraTwoY
    c2y = vertexCameraTwoY
    vertexCameraTwoZ = vertexCameraTwo.vertexCameraTwoZ
    c2z = vertexCameraTwoZ

    vertexCameraThree = VertexCameraThreeField()
    vc3 = vertexCameraThree
    vertexCameraThreeX = vertexCameraThree.vertexCameraThreeX
    c3x = vertexCameraThreeX
    vertexCameraThreeY = vertexCameraThree.vertexCameraThreeY
    c3y = vertexCameraThreeY
    vertexCameraThreeZ = vertexCameraThree.vertexCameraThreeZ
    c3z = vertexCameraThreeZ

    vertexUvOne = VertexUvOneField()
    vt1 = vertexUvOne
    vertexUvOneU = vertexUvOne.vertexUvOneU
    t1u = vertexUvOneU
    vertexUvOneV = vertexUvOne.vertexUvOneV
    t1v = vertexUvOneV

    vertexUvTwo = VertexUvTwoField()
    vt2 = vertexUvTwo
    vertexUvTwoU = vertexUvTwo.vertexUvTwoU
    t2u = vertexUvTwoU
    vertexUvTwoV = vertexUvTwo.vertexUvTwoV
    t2v = vertexUvTwoV

    vertexUvThree = VertexUvThreeField()
    vt3 = vertexUvThree
    vertexUvThreeU = vertexUvThree.vertexUvThreeU
    t3u = vertexUvThreeU
    vertexUvThreeV = vertexUvThree.vertexUvThreeV
    t3v = vertexUvThreeV

    uvFilterSize = UvFilterSizeField()
    uf = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    ufx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    ufy = uvFilterSizeY

    tangentUCamera = TangentUCameraField()
    tu = tangentUCamera
    tangentUx = tangentUCamera.tangentUx
    tux = tangentUx
    tangentUy = tangentUCamera.tangentUy
    tuy = tangentUy
    tangentUz = tangentUCamera.tangentUz
    tuz = tangentUz

    tangentVCamera = TangentVCameraField()
    tv = tangentVCamera
    tangentVx = tangentVCamera.tangentVx
    tvx = tangentVx
    tangentVy = tangentVCamera.tangentVy
    tvy = tangentVy
    tangentVz = tangentVCamera.tangentVz
    tvz = tangentVz

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    aiUseReferenceObject = BoolField()
    ai_use_reference_object = aiUseReferenceObject
