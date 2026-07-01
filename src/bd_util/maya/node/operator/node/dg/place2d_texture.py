# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.place2d_texture import (
    CoverageField,
    NoiseUVField,
    OffsetField,
    OutUVField,
    OutUvFilterSizeField,
    RepeatUVField,
    TranslateFrameField,
    UvCoordField,
    UvFilterSizeField,
    VertexCameraOneField,
    VertexUvOneField,
    VertexUvThreeField,
    VertexUvTwoField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField


class Place2dTexture(DG):
    __slots__ = ()

    NODE_TYPE = "place2dTexture"

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

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

    vertexCameraOne = VertexCameraOneField()
    vc1 = vertexCameraOne
    vertexCameraOneX = vertexCameraOne.vertexCameraOneX
    c1x = vertexCameraOneX
    vertexCameraOneY = vertexCameraOne.vertexCameraOneY
    c1y = vertexCameraOneY
    vertexCameraOneZ = vertexCameraOne.vertexCameraOneZ
    c1z = vertexCameraOneZ

    uvFilterSize = UvFilterSizeField()
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    coverage = CoverageField()
    c = coverage
    coverageU = coverage.coverageU
    cu = coverageU
    coverageV = coverage.coverageV
    cv = coverageV

    translateFrame = TranslateFrameField()
    tf = translateFrame
    translateFrameU = translateFrame.translateFrameU
    tfu = translateFrameU
    translateFrameV = translateFrame.translateFrameV
    tfv = translateFrameV

    rotateFrame = DoubleAngleField()
    rf = rotateFrame

    mirrorU = BoolField()
    mu = mirrorU

    mirrorV = BoolField()
    mv = mirrorV

    stagger = BoolField()
    s = stagger

    wrapU = BoolField()
    wu = wrapU

    wrapV = BoolField()
    wv = wrapV

    repeatUV = RepeatUVField()
    re = repeatUV
    repeatU = repeatUV.repeatU
    reu = repeatU
    repeatV = repeatUV.repeatV
    rev = repeatV

    offset = OffsetField()
    of = offset
    offsetU = offset.offsetU
    ofu = offsetU
    offsetV = offset.offsetV
    ofv = offsetV

    rotateUV = DoubleAngleField()
    r = rotateUV

    noiseUV = NoiseUVField()
    n = noiseUV
    noiseU = noiseUV.noiseU
    nu = noiseU
    noiseV = noiseUV.noiseV
    nv = noiseV

    fast = BoolField()
    fa = fast

    outUV = OutUVField()
    o = outUV
    outU = outUV.outU
    ou = outU
    outV = outUV.outV
    ov = outV

    outUvFilterSize = OutUvFilterSizeField()
    ofs = outUvFilterSize
    outUvFilterSizeX = outUvFilterSize.outUvFilterSizeX
    ofsx = outUvFilterSizeX
    outUvFilterSizeY = outUvFilterSize.outUvFilterSizeY
    ofsy = outUvFilterSizeY

    doTransform = BoolField()
    do = doTransform
