# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.c_muscle_shader import (
    DispDataField,
    ImageField,
    PointWorldField,
    UvCoordField,
    VertexUvOneField,
    VertexUvThreeField,
    VertexUvTwoField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class CMuscleShader(DG):
    __slots__ = ()

    NODE_TYPE = "cMuscleShader"

    pointWorld = PointWorldField()
    pw = pointWorld
    pointWorldX = pointWorld.pointWorldX
    pwx = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    pwy = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    pwz = pointWorldZ

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

    image = ImageField()
    i = image
    imageR = image.imageR
    ir = imageR
    imageG = image.imageG
    ig = imageG
    imageB = image.imageB
    ib = imageB

    inDisplacement = FloatField()
    id = inDisplacement

    dispData = DispDataField()
    ddata = dispData
    muscleMatrix = dispData.muscleMatrix
    mm = muscleMatrix
    curves = dispData.curves
    crv = curves
    mode = dispData.mode
    md = mode
    length = dispData.length
    len = length
    sizeRadius = dispData.sizeRadius
    siz = sizeRadius
    amplitude = dispData.amplitude
    amp = amplitude
    falloff = dispData.falloff
    fal = falloff
    pushMode = dispData.pushMode
    pmd = pushMode
    combineMode = dispData.combineMode
    cmd = combineMode
    shader = dispData.shader
    sha = shader

    displacement = FloatField()
    d = displacement

    displacementLocal = FloatField()
    dl = displacementLocal

    displacementLocalNormalized = FloatField()
    dln = displacementLocalNormalized
