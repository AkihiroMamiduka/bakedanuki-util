# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.place2d_texture import (
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
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedPlace2dTexture(DG):
    __slots__ = ()

    NODE_TYPE = "place2dTexture"

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

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

    vertexCameraOne = VertexCameraOneField(default_value=(0.0, 0.0, 0.0))
    vc1 = vertexCameraOne
    vertexCameraOneX = vertexCameraOne.vertexCameraOneX
    c1x = vertexCameraOneX
    vertexCameraOneY = vertexCameraOne.vertexCameraOneY
    c1y = vertexCameraOneY
    vertexCameraOneZ = vertexCameraOne.vertexCameraOneZ
    c1z = vertexCameraOneZ

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0))
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    coverage = CoverageField(
        default_value=(1.0, 1.0),
        min_value=(0.0, 0.0),
        soft_max_value=(1.0, 1.0),
    )
    c = coverage
    coverageU = coverage.coverageU
    cu = coverageU
    coverageV = coverage.coverageV
    cv = coverageV

    translateFrame = TranslateFrameField(default_value=(0.0, 0.0))
    tf = translateFrame
    translateFrameU = translateFrame.translateFrameU
    tfu = translateFrameU
    translateFrameV = translateFrame.translateFrameV
    tfv = translateFrameV

    rotateFrame = DoubleAngleField(
        default_value=0.0,
        soft_min_value=0.0,
        soft_max_value=359.99999958864004,
    )
    rf = rotateFrame

    mirrorU = BoolField(default_value=False)
    mu = mirrorU

    mirrorV = BoolField(default_value=False)
    mv = mirrorV

    stagger = BoolField(default_value=False)
    s = stagger

    wrapU = BoolField(default_value=True)
    wu = wrapU

    wrapV = BoolField(default_value=True)
    wv = wrapV

    repeatUV = RepeatUVField(default_value=(1.0, 1.0))
    re = repeatUV
    repeatU = repeatUV.repeatU
    reu = repeatU
    repeatV = repeatUV.repeatV
    rev = repeatV

    offset = OffsetField(default_value=(0.0, 0.0))
    of = offset
    offsetU = offset.offsetU
    ofu = offsetU
    offsetV = offset.offsetV
    ofv = offsetV

    rotateUV = DoubleAngleField(
        default_value=0.0,
        soft_min_value=0.0,
        soft_max_value=359.99999958864004,
    )
    r = rotateUV

    noiseUV = NoiseUVField(default_value=(0.0, 0.0), min_value=(0.0, 0.0))
    n = noiseUV
    noiseU = noiseUV.noiseU
    nu = noiseU
    noiseV = noiseUV.noiseV
    nv = noiseV

    fast = BoolField(default_value=False)
    fa = fast

    outUV = OutUVField(default_value=(0.0, 0.0), writable=False)
    o = outUV
    outU = outUV.outU
    ou = outU
    outV = outUV.outV
    ov = outV

    outUvFilterSize = OutUvFilterSizeField(
        default_value=(0.0, 0.0), writable=False
    )
    ofs = outUvFilterSize
    outUvFilterSizeX = outUvFilterSize.outUvFilterSizeX
    ofsx = outUvFilterSizeX
    outUvFilterSizeY = outUvFilterSize.outUvFilterSizeY
    ofsy = outUvFilterSizeY

    doTransform = BoolField(default_value=True, writable=False)
    do = doTransform
