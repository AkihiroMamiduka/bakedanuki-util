# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.texture_to_geom import OutColorDataField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.byte import ByteField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedTextureToGeom(DG):
    __slots__ = ()

    NODE_TYPE = "textureToGeom"

    segmentCount = LongField(default_value=0, writable=False)
    sc = segmentCount

    output = DataMeshField(writable=False)
    out = output

    outColorData = OutColorDataField(multi=True, writable=False)
    ocd = outColorData

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB

    outSegFace = TypedField(multi=True, writable=False)
    ofm = outSegFace

    segGroupIds = LongField(multi=True, default_value=-1)
    sgi = segGroupIds

    inputMesh = DataMeshField()
    im = inputMesh

    inputMeshUVSet = DataStringField()
    iuv = inputMeshUVSet

    quantize = BoolField(default_value=False)
    qut = quantize

    quantizeLevels = ByteField(default_value=10, min_value=1, max_value=64)
    qutl = quantizeLevels

    maxColorDiff = FloatField(default_value=0.125, min_value=9.999999747378752e-06, max_value=0.5)
    mcd = maxColorDiff

    minSegmentSize = FloatField(default_value=0.004999999888241291, min_value=0.0, max_value=1.0)
    msz = minSegmentSize

    spatialRadius = LongField(default_value=7, min_value=3, max_value=10)
    spr = spatialRadius

    colorRange = FloatField(default_value=4.5, min_value=1.0, max_value=10.0)
    crng = colorRange

    imageFile = DataStringField()
    if_ = imageFile

    meshQuality = DoubleField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0)
    mq = meshQuality

    surfaceOffset = FloatField(default_value=0.009999999776482582, soft_min_value=0.0, soft_max_value=1.0)
    so = surfaceOffset

    smoothBoundary = BoolField(default_value=True)
    smbd = smoothBoundary

    smoothFactor = FloatField(default_value=0.5, min_value=9.999999747378752e-06, max_value=0.9999900000002526)
    smf = smoothFactor

    fitTolerance = FloatField(default_value=0.007000000216066837, min_value=0.0, max_value=4.0)
    ft = fitTolerance

    hardCornerDetect = BoolField(default_value=True)
    hcd = hardCornerDetect

    hardCornerMaxLength = FloatField(default_value=10.0, min_value=10.0, max_value=100.0)
    hcml = hardCornerMaxLength

    simplifyBoundary = BoolField(default_value=True)
    smpl = simplifyBoundary

    simplifyThreshold = DoubleField(default_value=1e-10, min_value=1e-10, max_value=1.0)
    smpt = simplifyThreshold

    pointsOnBoundary = BoolField(default_value=True)
    pob = pointsOnBoundary

    maxPointsAdded = LongField(default_value=0, min_value=0, soft_max_value=100000)
    mpa = maxPointsAdded

    shaderScript = DataStringField()
    shs = shaderScript
