# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.texture_to_geom import OutColorDataField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.byte import ByteField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class TextureToGeom(DG):
    __slots__ = ()

    NODE_TYPE = "textureToGeom"

    segmentCount = LongField()
    sc = segmentCount

    output = DataMeshField()
    out = output

    outColorData = OutColorDataField(multi=True)
    ocd = outColorData

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB

    outSegFace = TypedField(multi=True)
    ofm = outSegFace

    segGroupIds = LongField(multi=True)
    sgi = segGroupIds

    inputMesh = DataMeshField()
    im = inputMesh

    inputMeshUVSet = DataStringField()
    iuv = inputMeshUVSet

    quantize = BoolField()
    qut = quantize

    quantizeLevels = ByteField()
    qutl = quantizeLevels

    maxColorDiff = FloatField()
    mcd = maxColorDiff

    minSegmentSize = FloatField()
    msz = minSegmentSize

    spatialRadius = LongField()
    spr = spatialRadius

    colorRange = FloatField()
    crng = colorRange

    imageFile = DataStringField()
    if_ = imageFile

    meshQuality = DoubleField()
    mq = meshQuality

    surfaceOffset = FloatField()
    so = surfaceOffset

    smoothBoundary = BoolField()
    smbd = smoothBoundary

    smoothFactor = FloatField()
    smf = smoothFactor

    fitTolerance = FloatField()
    ft = fitTolerance

    hardCornerDetect = BoolField()
    hcd = hardCornerDetect

    hardCornerMaxLength = FloatField()
    hcml = hardCornerMaxLength

    simplifyBoundary = BoolField()
    smpl = simplifyBoundary

    simplifyThreshold = DoubleField()
    smpt = simplifyThreshold

    pointsOnBoundary = BoolField()
    pob = pointsOnBoundary

    maxPointsAdded = LongField()
    mpa = maxPointsAdded

    shaderScript = DataStringField()
    shs = shaderScript
