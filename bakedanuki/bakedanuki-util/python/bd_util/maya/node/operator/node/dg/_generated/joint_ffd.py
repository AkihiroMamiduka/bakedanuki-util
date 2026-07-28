# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.joint_ffd import (
    BaseLatticeField,
    DeformedLatticeField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    StuCacheListField,
    WeightListField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.typed import TypedField


class UsePartialResolutionEnumPlugOperator(EnumPlugOperator["UsePartialResolutionEnumAttrOperator"]):
    __slots__ = ()

    FULL = 0
    PARTIAL = 1


class UsePartialResolutionEnumAttrOperator(EnumAttrOperator[UsePartialResolutionEnumPlugOperator]):
    __slots__ = ()

    FULL = 0
    PARTIAL = 1

    NAME_MAP = {
        FULL: "Full",
        PARTIAL: "Partial",
    }


class UsePartialResolutionEnumField(
    EnumField[UsePartialResolutionEnumAttrOperator, UsePartialResolutionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UsePartialResolutionEnumAttrOperator
    PLUG_CLS = UsePartialResolutionEnumPlugOperator


class OutsideLatticeEnumPlugOperator(EnumPlugOperator["OutsideLatticeEnumAttrOperator"]):
    __slots__ = ()

    INSIDE = 0
    ALL = 1
    FALLOFF = 2


class OutsideLatticeEnumAttrOperator(EnumAttrOperator[OutsideLatticeEnumPlugOperator]):
    __slots__ = ()

    INSIDE = 0
    ALL = 1
    FALLOFF = 2

    NAME_MAP = {
        INSIDE: "Inside",
        ALL: "All",
        FALLOFF: "Falloff",
    }


class OutsideLatticeEnumField(
    EnumField[OutsideLatticeEnumAttrOperator, OutsideLatticeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutsideLatticeEnumAttrOperator
    PLUG_CLS = OutsideLatticeEnumPlugOperator


class GeneratedJointFfd(DG):
    __slots__ = ()

    NODE_TYPE = "jointFfd"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True, default_value=1.0, writable=False)
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(default_value=1.0, min_value=-2.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
    en = envelope

    function = FunctionField(default_value=(0, 0, 0), readable=False)
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True, default_value=1.0)
    wl = weightList

    deformedLattice = DeformedLatticeField()
    dl = deformedLattice
    deformedLatticePoints = deformedLattice.deformedLatticePoints
    dlp = deformedLatticePoints
    deformedLatticeMatrix = deformedLattice.deformedLatticeMatrix
    dlm = deformedLatticeMatrix

    baseLattice = BaseLatticeField()
    bl = baseLattice
    baseLatticePoints = baseLattice.baseLatticePoints
    blp = baseLatticePoints
    baseLatticeMatrix = baseLattice.baseLatticeMatrix
    blm = baseLatticeMatrix

    stuCacheList = StuCacheListField(multi=True, default_value=0.0)
    scl = stuCacheList

    partialResolution = DoubleField(default_value=0.01, min_value=0.0, max_value=0.1)
    ptr = partialResolution

    localInfluenceS = ShortField(default_value=2, min_value=2, max_value=30)
    lis = localInfluenceS

    localInfluenceT = ShortField(default_value=2, min_value=2, max_value=30)
    lit = localInfluenceT

    localInfluenceU = ShortField(default_value=2, min_value=2, max_value=30)
    liu = localInfluenceU

    freezeGeometry = BoolField(default_value=False)
    fg = freezeGeometry

    bindToOriginalGeometry = BoolField(default_value=False)
    bog = bindToOriginalGeometry

    local = BoolField(default_value=False)
    lo = local

    usePartialResolution = UsePartialResolutionEnumField(default_value=0)
    upr = usePartialResolution

    outsideLattice = OutsideLatticeEnumField(default_value=0)
    ot = outsideLattice

    outsideFalloffDist = DoubleField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    ofd = outsideFalloffDist

    baseLattice2Matrix = MatrixField()
    b2 = baseLattice2Matrix

    groupIdUpperBindSkin = LongField(multi=True, default_value=-1)
    gu = groupIdUpperBindSkin

    groupIdLowerBindSkin = LongField(multi=True, default_value=-1)
    gl = groupIdLowerBindSkin

    upperBindSkinNode = MessageField()
    ub = upperBindSkinNode

    lowerBindSkinNode = MessageField()
    lb = lowerBindSkinNode

    useComponentCache = BoolField(default_value=True)
    uc = useComponentCache

    upperComponentCache = TypedField(multi=True, writable=False)
    cu = upperComponentCache

    lowerComponentCache = TypedField(multi=True, writable=False)
    cl = lowerComponentCache
