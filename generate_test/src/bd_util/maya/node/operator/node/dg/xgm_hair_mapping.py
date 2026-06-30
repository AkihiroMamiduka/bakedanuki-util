# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_hair_mapping import (
    CoverageField,
    OffsetField,
    OutUVField,
    OutUvFilterSizeField,
    RepeatUVField,
    TranslateFrameField,
    UvCoordField,
    UvFilterSizeField,
)


class XgmHairMapping(DG):
    __slots__ = ()

    NODE_TYPE = "xgmHairMapping"

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

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
