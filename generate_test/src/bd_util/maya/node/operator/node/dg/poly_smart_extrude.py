# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_smart_extrude import (
    CompBoundingBoxMaxField,
    CompBoundingBoxMinField,
    CompPivotOrientationField,
    PivotField,
    PivotOrientationField,
    TranslateField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class PolySmartExtrude(DG):
    __slots__ = ()

    NODE_TYPE = "polySmartExtrude"

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

    compBoundingBoxMin = CompBoundingBoxMinField()
    cbn = compBoundingBoxMin
    compBoundingBoxMinX = compBoundingBoxMin.compBoundingBoxMinX
    cnx = compBoundingBoxMinX
    compBoundingBoxMinY = compBoundingBoxMin.compBoundingBoxMinY
    cny = compBoundingBoxMinY
    compBoundingBoxMinZ = compBoundingBoxMin.compBoundingBoxMinZ
    cnz = compBoundingBoxMinZ

    compBoundingBoxMax = CompBoundingBoxMaxField()
    cbx = compBoundingBoxMax
    compBoundingBoxMaxX = compBoundingBoxMax.compBoundingBoxMaxX
    cxx = compBoundingBoxMaxX
    compBoundingBoxMaxY = compBoundingBoxMax.compBoundingBoxMaxY
    cxy = compBoundingBoxMaxY
    compBoundingBoxMaxZ = compBoundingBoxMax.compBoundingBoxMaxZ
    cxz = compBoundingBoxMaxZ

    translate = TranslateField()
    t = translate
    translateX = translate.translateX
    tx = translateX
    translateY = translate.translateY
    ty = translateY
    translateZ = translate.translateZ
    tz = translateZ

    pivot = PivotField()
    pvt = pivot
    pivotX = pivot.pivotX
    pvx = pivotX
    pivotY = pivot.pivotY
    pvy = pivotY
    pivotZ = pivot.pivotZ
    pvz = pivotZ

    interactiveUpdate = BoolField()
    iu = interactiveUpdate

    pivotOrientation = PivotOrientationField()
    por = pivotOrientation
    pivotOrientationX = pivotOrientation.pivotOrientationX
    pox = pivotOrientationX
    pivotOrientationY = pivotOrientation.pivotOrientationY
    poy = pivotOrientationY
    pivotOrientationZ = pivotOrientation.pivotOrientationZ
    poz = pivotOrientationZ

    compPivotOrientation = CompPivotOrientationField()
    cpr = compPivotOrientation
    compPivotOrientationX = compPivotOrientation.compPivotOrientationX
    cpx = compPivotOrientationX
    compPivotOrientationY = compPivotOrientation.compPivotOrientationY
    cpy = compPivotOrientationY
    compPivotOrientationZ = compPivotOrientation.compPivotOrientationZ
    cpz = compPivotOrientationZ
