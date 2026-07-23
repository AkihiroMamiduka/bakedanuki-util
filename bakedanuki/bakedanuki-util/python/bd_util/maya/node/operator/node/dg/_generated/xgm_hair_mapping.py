# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.xgm_hair_mapping import (
    CoverageField,
    OffsetField,
    OutUVField,
    OutUvFilterSizeField,
    RepeatUVField,
    TranslateFrameField,
    UvCoordField,
    UvFilterSizeField,
)


class _GeneratedXgmHairMapping(DG):
    __slots__ = ()

    NODE_TYPE = "xgmHairMapping"

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0))
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    coverage = CoverageField(default_value=(1.0, 1.0), min_value=(0.0, 0.0))
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

    outUV = OutUVField(default_value=(0.0, 0.0), writable=False)
    o = outUV
    outU = outUV.outU
    ou = outU
    outV = outUV.outV
    ov = outV

    outUvFilterSize = OutUvFilterSizeField(default_value=(0.0, 0.0), writable=False)
    ofs = outUvFilterSize
    outUvFilterSizeX = outUvFilterSize.outUvFilterSizeX
    ofsx = outUvFilterSizeX
    outUvFilterSizeY = outUvFilterSize.outUvFilterSizeY
    ofsy = outUvFilterSizeY
