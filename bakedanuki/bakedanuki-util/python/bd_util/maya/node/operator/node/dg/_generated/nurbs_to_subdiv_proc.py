# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class SolidTypeEnumPlugOperator(EnumPlugOperator["SolidTypeEnumAttrOperator"]):
    __slots__ = ()

    NOTHING = 0
    TRANSFORM = 1
    OFFSET = 2


class SolidTypeEnumAttrOperator(EnumAttrOperator[SolidTypeEnumPlugOperator]):
    __slots__ = ()

    NOTHING = 0
    TRANSFORM = 1
    OFFSET = 2

    NAME_MAP = {
        NOTHING: "Nothing",
        TRANSFORM: "Transform",
        OFFSET: "Offset",
    }


class SolidTypeEnumField(
    EnumField[SolidTypeEnumAttrOperator, SolidTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolidTypeEnumAttrOperator
    PLUG_CLS = SolidTypeEnumPlugOperator


class CapTypeEnumPlugOperator(EnumPlugOperator["CapTypeEnumAttrOperator"]):
    __slots__ = ()

    CAP = 0
    STITCH = 1


class CapTypeEnumAttrOperator(EnumAttrOperator[CapTypeEnumPlugOperator]):
    __slots__ = ()

    CAP = 0
    STITCH = 1

    NAME_MAP = {
        CAP: "Cap",
        STITCH: "Stitch",
    }


class CapTypeEnumField(
    EnumField[CapTypeEnumAttrOperator, CapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CapTypeEnumAttrOperator
    PLUG_CLS = CapTypeEnumPlugOperator


class BridgeEnumPlugOperator(EnumPlugOperator["BridgeEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    INU = 1
    INV = 2
    BOTH = 3


class BridgeEnumAttrOperator(EnumAttrOperator[BridgeEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    INU = 1
    INV = 2
    BOTH = 3

    NAME_MAP = {
        NONE: "None",
        INU: "InU",
        INV: "InV",
        BOTH: "Both",
    }


class BridgeEnumField(
    EnumField[BridgeEnumAttrOperator, BridgeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BridgeEnumAttrOperator
    PLUG_CLS = BridgeEnumPlugOperator


class GeneratedNurbsToSubdivProc(DG):
    __slots__ = ()

    NODE_TYPE = "nurbsToSubdivProc"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    outputSubd = TypedField(writable=False)
    os = outputSubd

    maxPolyCount = LongField(default_value=1000, min_value=1, max_value=100000)
    mpc = maxPolyCount

    reverseNormal = BoolField(default_value=True)
    rn = reverseNormal

    matchPeriodic = BoolField(default_value=False)
    mp = matchPeriodic

    collapsePoles = BoolField(default_value=False)
    cp = collapsePoles

    solidType = SolidTypeEnumField(default_value=2)
    st = solidType

    capType = CapTypeEnumField(default_value=0)
    ct = capType

    transform = DataMatrixField()
    t = transform

    offset = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    o = offset

    bridge = BridgeEnumField(default_value=0)
    br = bridge

    bridgeInU = DataNurbsCurveField()
    biu = bridgeInU

    bridgeInV = DataNurbsCurveField()
    biv = bridgeInV
