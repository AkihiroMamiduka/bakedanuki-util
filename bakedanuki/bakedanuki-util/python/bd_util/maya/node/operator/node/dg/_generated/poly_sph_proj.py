# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_sph_proj import (
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
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedPolySphProj(DG):
    __slots__ = ()

    NODE_TYPE = "polySphProj"

    output = DataMeshField(writable=False)
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField(default_value=0)
    cin = cacheInput

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField(default_value=False)
    vmap = vertexIdMap

    edgeIdMap = BoolField(default_value=False)
    emap = edgeIdMap

    faceIdMap = BoolField(default_value=False)
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField(default_value=True)
    uic = useInputComp

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
    ic = imageCenter
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

    projectionScale = ProjectionScaleField(default_value=(180.0, 90.0), min_value=(0.0, 0.0), max_value=(360.0, 180.0))
    ps = projectionScale
    projectionHorizontalSweep = projectionScale.projectionHorizontalSweep
    phs = projectionHorizontalSweep
    projectionVerticalSweep = projectionScale.projectionVerticalSweep
    pvs = projectionVerticalSweep

    uvSetName = DataStringField()
    uvs = uvSetName

    imageScale = ImageScaleField(default_value=(1.0, 1.0))
    is_ = imageScale
    imageScaleU = imageScale.imageScaleU
    isu = imageScaleU
    imageScaleV = imageScale.imageScaleV
    isv = imageScaleV

    radius = DoubleLinearField(default_value=10.0)
    r = radius

    rotationAngle = DoubleAngleField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)
    ra = rotationAngle

    seamCorrect = BoolField(default_value=False)
    sc = seamCorrect

    compId = LongField(default_value=0, writable=False)
    cid = compId

    useOldPolyProjection = BoolField(default_value=False)
    uopp = useOldPolyProjection
