# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.lod_thresholds import (
    CameraField,
    InBoxMaxField,
    InBoxMinField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class LodThresholds(DG):
    __slots__ = ()

    NODE_TYPE = "lodThresholds"

    inBoxMin = InBoxMinField()
    bmn = inBoxMin
    inBoxMinX = inBoxMin.inBoxMinX
    bmix = inBoxMinX
    inBoxMinY = inBoxMin.inBoxMinY
    bmiy = inBoxMinY
    inBoxMinZ = inBoxMin.inBoxMinZ
    bmiz = inBoxMinZ

    inBoxMax = InBoxMaxField()
    bmx = inBoxMax
    inBoxMaxX = inBoxMax.inBoxMaxX
    bmax = inBoxMaxX
    inBoxMaxY = inBoxMax.inBoxMaxY
    bmay = inBoxMaxY
    inBoxMaxZ = inBoxMax.inBoxMaxZ
    bmaz = inBoxMaxZ

    camera = CameraField()
    cam = camera
    cameraX = camera.cameraX
    cax = cameraX
    cameraY = camera.cameraY
    cay = cameraY
    cameraZ = camera.cameraZ
    caz = cameraZ

    threshold = DoubleLinearField(multi=True)
    th = threshold

    distance = DoubleLinearField()
    d = distance

    activeLevel = LongField()
    al = activeLevel

    outLevel = BoolField(multi=True)
    ol = outLevel
