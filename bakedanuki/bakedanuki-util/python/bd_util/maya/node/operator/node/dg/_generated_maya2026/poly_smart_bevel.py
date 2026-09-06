# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from ....attr.define.std.at.scalar.unit.range.float_linear import (
    FloatLinearField,
)
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class FilterFromSmoothingEnumPlugOperator(
    EnumPlugOperator["FilterFromSmoothingEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 1
    SMOOTH = 2
    HARD = 3


class FilterFromSmoothingEnumAttrOperator(
    EnumAttrOperator[FilterFromSmoothingEnumPlugOperator]
):
    __slots__ = ()

    OFF = 1
    SMOOTH = 2
    HARD = 3

    NAME_MAP = {
        OFF: "Off",
        SMOOTH: "Smooth",
        HARD: "Hard",
    }


class FilterFromSmoothingEnumField(
    EnumField[
        FilterFromSmoothingEnumAttrOperator,
        FilterFromSmoothingEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FilterFromSmoothingEnumAttrOperator
    PLUG_CLS = FilterFromSmoothingEnumPlugOperator


class GeneratedPolySmartBevel(DG):
    __slots__ = ()

    NODE_TYPE = "polySmartBevel"

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

    defaultGroupId = LongField(default_value=0)
    dg = defaultGroupId

    gwABIVersion = LongField(default_value=-1)
    gav = gwABIVersion

    width = FloatLinearField(
        default_value=float("nan"), min_value=0.0, soft_max_value=5.0
    )
    w = width

    segments = LongField(default_value=1, min_value=1, soft_max_value=12)
    sg = segments

    depth = FloatLinearField(default_value=0.5, min_value=-0.5, max_value=1.0)
    dep = depth

    filterFromSmoothing = FilterFromSmoothingEnumField(default_value=1)
    ffs = filterFromSmoothing

    filterEdgesBySelection = BoolField(default_value=True)
    fes = filterEdgesBySelection

    filterHardEdges = BoolField(default_value=False)
    fhe = filterHardEdges

    filterEdgesByAngle = BoolField(default_value=False)
    fea = filterEdgesByAngle

    filterAngle = DoubleAngleField(
        default_value=29.999999999999996, min_value=0.0, max_value=180.0
    )
    fa = filterAngle

    filterEdgesByMaxAngle = BoolField(default_value=False)
    fmx = filterEdgesByMaxAngle

    filterMaxAngle = DoubleAngleField(
        default_value=0.0, min_value=0.0, max_value=180.0
    )
    mxa = filterMaxAngle

    selectedEdgeGroup = TypedField(writable=False)
    seg = selectedEdgeGroup

    selectedFaceGroup = TypedField(writable=False)
    sfg = selectedFaceGroup

    setPerimeterHard = BoolField(default_value=False)
    sph = setPerimeterHard

    smoothingThreshold = DoubleAngleField(
        default_value=29.999999999999996, min_value=0.0, max_value=180.0
    )
    sth = smoothingThreshold

    limitWidth = BoolField(default_value=True)
    kw = limitWidth

    maxSafeWidth = FloatLinearField(default_value=float("nan"), min_value=0.0)
    msw = maxSafeWidth

    sequenceSmoothingIterationLimit = LongField(
        default_value=100, min_value=0, max_value=10000
    )
    ssl = sequenceSmoothingIterationLimit

    normalSmoothingIterationLimit = LongField(
        default_value=100, min_value=0, max_value=10000
    )
    nsl = normalSmoothingIterationLimit

    safeWidthLimitBoundingBox = BoolField(default_value=True)
    sbb = safeWidthLimitBoundingBox

    safeWidthLimitMeshBoundary = BoolField(default_value=True)
    smb = safeWidthLimitMeshBoundary

    safeWidthLimitConvex = BoolField(default_value=True)
    slc = safeWidthLimitConvex

    safeWidthLimitHardIslands = BoolField(default_value=False)
    shi = safeWidthLimitHardIslands

    safeWidthLimitBinarySearch = BoolField(default_value=True)
    sbs = safeWidthLimitBinarySearch

    alongEdgeSequenceSmoothing = BoolField(default_value=True)
    aes = alongEdgeSequenceSmoothing

    vertexWeldCleanup = BoolField(default_value=True)
    vwc = vertexWeldCleanup

    vertexWeldCleanupThreshold = FloatLinearField(
        default_value=0.25, min_value=0.0, max_value=1.0
    )
    vwt = vertexWeldCleanupThreshold
