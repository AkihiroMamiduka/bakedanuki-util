# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_smart_extrude import (
    CompBoundingBoxMaxField,
    CompBoundingBoxMinField,
    CompPivotOrientationField,
    PivotField,
    PivotOrientationField,
    TranslateField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class _GeneratedPolySmartExtrude(DG):
    __slots__ = ()

    NODE_TYPE = "polySmartExtrude"

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

    compBoundingBoxMin = CompBoundingBoxMinField(default_value=(0.0, 0.0, 0.0))
    cbn = compBoundingBoxMin
    compBoundingBoxMinX = compBoundingBoxMin.compBoundingBoxMinX
    cnx = compBoundingBoxMinX
    compBoundingBoxMinY = compBoundingBoxMin.compBoundingBoxMinY
    cny = compBoundingBoxMinY
    compBoundingBoxMinZ = compBoundingBoxMin.compBoundingBoxMinZ
    cnz = compBoundingBoxMinZ

    compBoundingBoxMax = CompBoundingBoxMaxField(default_value=(1.0, 1.0, 1.0))
    cbx = compBoundingBoxMax
    compBoundingBoxMaxX = compBoundingBoxMax.compBoundingBoxMaxX
    cxx = compBoundingBoxMaxX
    compBoundingBoxMaxY = compBoundingBoxMax.compBoundingBoxMaxY
    cxy = compBoundingBoxMaxY
    compBoundingBoxMaxZ = compBoundingBoxMax.compBoundingBoxMaxZ
    cxz = compBoundingBoxMaxZ

    translate = TranslateField(default_value=(0.0, 0.0, 0.0))
    t = translate
    translateX = translate.translateX
    tx = translateX
    translateY = translate.translateY
    ty = translateY
    translateZ = translate.translateZ
    tz = translateZ

    pivot = PivotField(default_value=(0.0, 0.0, 0.0))
    pvt = pivot
    pivotX = pivot.pivotX
    pvx = pivotX
    pivotY = pivot.pivotY
    pvy = pivotY
    pivotZ = pivot.pivotZ
    pvz = pivotZ

    interactiveUpdate = BoolField(default_value=True)
    iu = interactiveUpdate

    pivotOrientation = PivotOrientationField(default_value=(0.0, 0.0, 0.0))
    por = pivotOrientation
    pivotOrientationX = pivotOrientation.pivotOrientationX
    pox = pivotOrientationX
    pivotOrientationY = pivotOrientation.pivotOrientationY
    poy = pivotOrientationY
    pivotOrientationZ = pivotOrientation.pivotOrientationZ
    poz = pivotOrientationZ

    compPivotOrientation = CompPivotOrientationField(default_value=(0.0, 0.0, 0.0))
    cpr = compPivotOrientation
    compPivotOrientationX = compPivotOrientation.compPivotOrientationX
    cpx = compPivotOrientationX
    compPivotOrientationY = compPivotOrientation.compPivotOrientationY
    cpy = compPivotOrientationY
    compPivotOrientationZ = compPivotOrientation.compPivotOrientationZ
    cpz = compPivotOrientationZ
