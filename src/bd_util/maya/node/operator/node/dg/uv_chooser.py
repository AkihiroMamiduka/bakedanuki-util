# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.uv_chooser import (
    OutUvField,
    OutVertexCameraOneField,
    OutVertexUvOneField,
    OutVertexUvThreeField,
    OutVertexUvTwoField,
    StCoordField,
    UvCoordField,
    VertexCameraOneField,
    VertexStOneField,
    VertexStThreeField,
    VertexStTwoField,
    VertexUvOneField,
    VertexUvThreeField,
    VertexUvTwoField,
)
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class UvChooser(DG):
    __slots__ = ()

    NODE_TYPE = "uvChooser"

    stCoord = StCoordField()
    st = stCoord
    sCoord = stCoord.sCoord
    s = sCoord
    tCoord = stCoord.tCoord
    t = tCoord

    vertexStOne = VertexStOneField()
    vs1 = vertexStOne
    vertexStOneS = vertexStOne.vertexStOneS
    s1s = vertexStOneS
    vertexStOneT = vertexStOne.vertexStOneT
    s1t = vertexStOneT

    vertexStTwo = VertexStTwoField()
    vs2 = vertexStTwo
    vertexStTwoS = vertexStTwo.vertexStTwoS
    s2s = vertexStTwoS
    vertexStTwoT = vertexStTwo.vertexStTwoT
    s2t = vertexStTwoT

    vertexStThree = VertexStThreeField()
    vs3 = vertexStThree
    vertexStThreeS = vertexStThree.vertexStThreeS
    s3s = vertexStThreeS
    vertexStThreeT = vertexStThree.vertexStThreeT
    s3t = vertexStThreeT

    uvSets = DataStringField(multi=True)
    uvs = uvSets

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

    infoBits = LongField()
    ib = infoBits

    outUv = OutUvField()
    ouv = outUv
    outU = outUv.outU
    ou = outU
    outV = outUv.outV
    ov = outV

    outVertexUvOne = OutVertexUvOneField()
    ov1 = outVertexUvOne
    outVertexUvOneU = outVertexUvOne.outVertexUvOneU
    o1u = outVertexUvOneU
    outVertexUvOneV = outVertexUvOne.outVertexUvOneV
    o1v = outVertexUvOneV

    outVertexUvTwo = OutVertexUvTwoField()
    ov2 = outVertexUvTwo
    outVertexUvTwoU = outVertexUvTwo.outVertexUvTwoU
    o2u = outVertexUvTwoU
    outVertexUvTwoV = outVertexUvTwo.outVertexUvTwoV
    o2v = outVertexUvTwoV

    outVertexUvThree = OutVertexUvThreeField()
    ov3 = outVertexUvThree
    outVertexUvThreeU = outVertexUvThree.outVertexUvThreeU
    o3u = outVertexUvThreeU
    outVertexUvThreeV = outVertexUvThree.outVertexUvThreeV
    o3v = outVertexUvThreeV

    outVertexCameraOne = OutVertexCameraOneField()
    oc1 = outVertexCameraOne
    outVertexCameraOneX = outVertexCameraOne.outVertexCameraOneX
    o1x = outVertexCameraOneX
    outVertexCameraOneY = outVertexCameraOne.outVertexCameraOneY
    o1y = outVertexCameraOneY
    outVertexCameraOneZ = outVertexCameraOne.outVertexCameraOneZ
    o1z = outVertexCameraOneZ
