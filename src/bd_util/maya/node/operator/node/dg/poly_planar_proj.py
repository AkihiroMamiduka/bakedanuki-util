# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_planar_proj import (
    ImageCenterField,
    ImageScaleField,
    ProjectionCenterField,
    ProjectionScaleField,
    RotateField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class PolyPlanarProj(DG):
    __slots__ = ()

    NODE_TYPE = "polyPlanarProj"

    output = DataMeshField()
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField()
    cin = cacheInput

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField()
    vmap = vertexIdMap

    edgeIdMap = BoolField()
    emap = edgeIdMap

    faceIdMap = BoolField()
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField()
    uic = useInputComp

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
    ic = imageCenter
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

    uvSetName = DataStringField()
    uvs = uvSetName

    imageScale = ImageScaleField()
    is_ = imageScale
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

    isPerspective = BoolField()
    per = isPerspective

    cameraMatrix = DataMatrixField()
    cam = cameraMatrix

    portLeft = ShortField()
    plft = portLeft

    portBottom = ShortField()
    pbot = portBottom

    portRight = ShortField()
    prgt = portRight

    portTop = ShortField()
    ptop = portTop
