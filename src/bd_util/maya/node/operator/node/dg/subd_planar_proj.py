# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.subd_planar_proj import (
    ImageCenterField,
    ImageScaleField,
    ProjectionCenterField,
    ProjectionScaleField,
    RotateField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField


class SubdPlanarProj(DG):
    __slots__ = ()

    NODE_TYPE = "subdPlanarProj"

    outSubdiv = TypedField()
    os = outSubdiv

    inSubdiv = TypedField()
    is_ = inSubdiv

    cachedSubdiv = TypedField()
    ic = cachedSubdiv

    inputComponents = TypedField()
    ics = inputComponents

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField()
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    projectionCenter = ProjectionCenterField()
    pc = projectionCenter
    projectionCenterX = projectionCenter.projectionCenterX
    pcx = projectionCenterX
    projectionCenterY = projectionCenter.projectionCenterY
    pcy = projectionCenterY
    projectionCenterZ = projectionCenter.projectionCenterZ
    pcz = projectionCenterZ

    imageCenter = ImageCenterField()
    ic2 = imageCenter
    imageCenterX = imageCenter.imageCenterX
    icx = imageCenterX
    imageCenterY = imageCenter.imageCenterY
    icy = imageCenterY

    rotate = RotateField()
    ro = rotate
    rotateX = rotate.rotateX
    rx = rotateX
    rotateY = rotate.rotateY
    ry = rotateY
    rotateZ = rotate.rotateZ
    rz = rotateZ

    projectionScale = ProjectionScaleField()
    ps = projectionScale
    projectionWidth = projectionScale.projectionWidth
    pw = projectionWidth
    projectionHeight = projectionScale.projectionHeight
    ph = projectionHeight

    imageScale = ImageScaleField()
    is2 = imageScale
    imageScaleU = imageScale.imageScaleU
    isu = imageScaleU
    imageScaleV = imageScale.imageScaleV
    isv = imageScaleV

    rotationAngle = DoubleAngleField()
    ra = rotationAngle

    radius = DoubleLinearField()
    r = radius

    compId = LongField()
    cid = compId
