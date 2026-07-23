# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.uv_chooser import (
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
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedUvChooser(DG):
    __slots__ = ()

    NODE_TYPE = "uvChooser"

    stCoord = StCoordField(default_value=(0.0, 0.0))
    st = stCoord
    sCoord = stCoord.sCoord
    s = sCoord
    tCoord = stCoord.tCoord
    t = tCoord

    vertexStOne = VertexStOneField(default_value=(0.0, 0.0))
    vs1 = vertexStOne
    vertexStOneS = vertexStOne.vertexStOneS
    s1s = vertexStOneS
    vertexStOneT = vertexStOne.vertexStOneT
    s1t = vertexStOneT

    vertexStTwo = VertexStTwoField(default_value=(0.0, 0.0))
    vs2 = vertexStTwo
    vertexStTwoS = vertexStTwo.vertexStTwoS
    s2s = vertexStTwoS
    vertexStTwoT = vertexStTwo.vertexStTwoT
    s2t = vertexStTwoT

    vertexStThree = VertexStThreeField(default_value=(0.0, 0.0))
    vs3 = vertexStThree
    vertexStThreeS = vertexStThree.vertexStThreeS
    s3s = vertexStThreeS
    vertexStThreeT = vertexStThree.vertexStThreeT
    s3t = vertexStThreeT

    uvSets = DataStringField(multi=True)
    uvs = uvSets

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

    infoBits = LongField(default_value=0)
    ib = infoBits

    outUv = OutUvField(default_value=(0.0, 0.0), writable=False)
    ouv = outUv
    outU = outUv.outU
    ou = outU
    outV = outUv.outV
    ov = outV

    outVertexUvOne = OutVertexUvOneField(default_value=(0.0, 0.0))
    ov1 = outVertexUvOne
    outVertexUvOneU = outVertexUvOne.outVertexUvOneU
    o1u = outVertexUvOneU
    outVertexUvOneV = outVertexUvOne.outVertexUvOneV
    o1v = outVertexUvOneV

    outVertexUvTwo = OutVertexUvTwoField(default_value=(0.0, 0.0))
    ov2 = outVertexUvTwo
    outVertexUvTwoU = outVertexUvTwo.outVertexUvTwoU
    o2u = outVertexUvTwoU
    outVertexUvTwoV = outVertexUvTwo.outVertexUvTwoV
    o2v = outVertexUvTwoV

    outVertexUvThree = OutVertexUvThreeField(default_value=(0.0, 0.0))
    ov3 = outVertexUvThree
    outVertexUvThreeU = outVertexUvThree.outVertexUvThreeU
    o3u = outVertexUvThreeU
    outVertexUvThreeV = outVertexUvThree.outVertexUvThreeV
    o3v = outVertexUvThreeV

    outVertexCameraOne = OutVertexCameraOneField(default_value=(0.0, 0.0, 0.0))
    oc1 = outVertexCameraOne
    outVertexCameraOneX = outVertexCameraOne.outVertexCameraOneX
    o1x = outVertexCameraOneX
    outVertexCameraOneY = outVertexCameraOne.outVertexCameraOneY
    o1y = outVertexCameraOneY
    outVertexCameraOneZ = outVertexCameraOne.outVertexCameraOneZ
    o1z = outVertexCameraOneZ
