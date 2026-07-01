# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class SolidTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NOTHING = 0
    TRANSFORM = 1
    OFFSET = 2


class SolidTypeEnumAttrOperator(EnumAttrOperator):
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


class CapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CAP = 0
    STITCH = 1


class CapTypeEnumAttrOperator(EnumAttrOperator):
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


class BridgeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    INU = 1
    INV = 2
    BOTH = 3


class BridgeEnumAttrOperator(EnumAttrOperator):
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


class NurbsToSubdivProc(DG):
    __slots__ = ()

    NODE_TYPE = "nurbsToSubdivProc"

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    outputSubd = TypedField()
    os = outputSubd

    maxPolyCount = LongField()
    mpc = maxPolyCount

    reverseNormal = BoolField()
    rn = reverseNormal

    matchPeriodic = BoolField()
    mp = matchPeriodic

    collapsePoles = BoolField()
    cp = collapsePoles

    solidType = SolidTypeEnumField()
    st = solidType

    capType = CapTypeEnumField()
    ct = capType

    transform = DataMatrixField()
    t = transform

    offset = DoubleLinearField()
    o = offset

    bridge = BridgeEnumField()
    br = bridge

    bridgeInU = DataNurbsCurveField()
    biu = bridgeInU

    bridgeInV = DataNurbsCurveField()
    biv = bridgeInV
