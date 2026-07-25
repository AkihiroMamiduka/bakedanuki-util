# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.subd_planar_proj import (
    ImageCenterField,
    ImageScaleField,
    ProjectionCenterField,
    ProjectionScaleField,
    RotateField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.matrix import DataMatrixField


class _GeneratedSubdPlanarProj(DG):
    __slots__ = ()

    NODE_TYPE = "subdPlanarProj"

    outSubdiv = TypedField(writable=False)
    os = outSubdiv

    inSubdiv = TypedField()
    is_ = inSubdiv

    cachedSubdiv = TypedField()
    ic = cachedSubdiv

    inputComponents = TypedField()
    ics = inputComponents

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField(default_value=False)
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    projectionCenter = ProjectionCenterField(default_value=(0.0, 0.0, 0.0))
    pc = projectionCenter
    projectionCenterX = projectionCenter.projectionCenterX
    pcx = projectionCenterX
    projectionCenterY = projectionCenter.projectionCenterY
    pcy = projectionCenterY
    projectionCenterZ = projectionCenter.projectionCenterZ
    pcz = projectionCenterZ

    imageCenter = ImageCenterField(default_value=(0.5, 0.5))
    ic2 = imageCenter
    imageCenterX = imageCenter.imageCenterX
    icx = imageCenterX
    imageCenterY = imageCenter.imageCenterY
    icy = imageCenterY

    rotate = RotateField(default_value=(0.0, 0.0, 0.0))
    ro = rotate
    rotateX = rotate.rotateX
    rx = rotateX
    rotateY = rotate.rotateY
    ry = rotateY
    rotateZ = rotate.rotateZ
    rz = rotateZ

    projectionScale = ProjectionScaleField(default_value=(1.0, 1.0), min_value=(0.0, 0.0), soft_max_value=(2.0, 2.0))
    ps = projectionScale
    projectionWidth = projectionScale.projectionWidth
    pw = projectionWidth
    projectionHeight = projectionScale.projectionHeight
    ph = projectionHeight

    imageScale = ImageScaleField(default_value=(1.0, 1.0))
    is2 = imageScale
    imageScaleU = imageScale.imageScaleU
    isu = imageScaleU
    imageScaleV = imageScale.imageScaleV
    isv = imageScaleV

    rotationAngle = DoubleAngleField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)
    ra = rotationAngle

    radius = DoubleLinearField(default_value=10.0)
    r = radius

    compId = LongField(default_value=0, writable=False)
    cid = compId
