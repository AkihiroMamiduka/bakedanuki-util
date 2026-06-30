# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ffd import (
    BaseLatticeField,
    DeformedLatticeField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    StuCacheListField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField


class UsePartialResolutionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FULL = 0
    PARTIAL = 1


class UsePartialResolutionEnumAttrOperator(EnumAttrOperator):
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


class OutsideLatticeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    INSIDE = 0
    ALL = 1
    FALLOFF = 2


class OutsideLatticeEnumAttrOperator(EnumAttrOperator):
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


class Ffd(DG):
    __slots__ = ()

    NODE_TYPE = "ffd"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True)
    ocw = envelopeWeightsList

    blockGPU = BoolField()
    bgp = blockGPU

    envelope = FloatField()
    en = envelope

    function = FunctionField()
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True)
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

    stuCacheList = StuCacheListField(multi=True)
    scl = stuCacheList

    partialResolution = DoubleField()
    ptr = partialResolution

    localInfluenceS = ShortField()
    lis = localInfluenceS

    localInfluenceT = ShortField()
    lit = localInfluenceT

    localInfluenceU = ShortField()
    liu = localInfluenceU

    freezeGeometry = BoolField()
    fg = freezeGeometry

    bindToOriginalGeometry = BoolField()
    bog = bindToOriginalGeometry

    local = BoolField()
    lo = local

    usePartialResolution = UsePartialResolutionEnumField()
    upr = usePartialResolution

    outsideLattice = OutsideLatticeEnumField()
    ot = outsideLattice

    outsideFalloffDist = DoubleField()
    ofd = outsideFalloffDist
