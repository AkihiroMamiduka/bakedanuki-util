# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.lod_thresholds import (
    CameraField,
    InBoxMaxField,
    InBoxMinField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField


class _GeneratedLodThresholds(DG):
    __slots__ = ()

    NODE_TYPE = "lodThresholds"

    inBoxMin = InBoxMinField(default_value=(0.0, 0.0, 0.0))
    bmn = inBoxMin
    inBoxMinX = inBoxMin.inBoxMinX
    bmix = inBoxMinX
    inBoxMinY = inBoxMin.inBoxMinY
    bmiy = inBoxMinY
    inBoxMinZ = inBoxMin.inBoxMinZ
    bmiz = inBoxMinZ

    inBoxMax = InBoxMaxField(default_value=(0.0, 0.0, 0.0))
    bmx = inBoxMax
    inBoxMaxX = inBoxMax.inBoxMaxX
    bmax = inBoxMaxX
    inBoxMaxY = inBoxMax.inBoxMaxY
    bmay = inBoxMaxY
    inBoxMaxZ = inBoxMax.inBoxMaxZ
    bmaz = inBoxMaxZ

    camera = CameraField(default_value=(0.0, 0.0, 0.0))
    cam = camera
    cameraX = camera.cameraX
    cax = cameraX
    cameraY = camera.cameraY
    cay = cameraY
    cameraZ = camera.cameraZ
    caz = cameraZ

    threshold = DoubleLinearField(multi=True, default_value=0.0)
    th = threshold

    distance = DoubleLinearField(default_value=0.0)
    d = distance

    activeLevel = LongField(default_value=0)
    al = activeLevel

    outLevel = BoolField(multi=True, default_value=False, writable=False)
    ol = outLevel
