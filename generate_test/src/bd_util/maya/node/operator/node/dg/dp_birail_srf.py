# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class SweepStyleEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NATURAL = 0
    VIEW = 1


class SweepStyleEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NATURAL = 0
    VIEW = 1

    NAME_MAP = {
        NATURAL: "Natural",
        VIEW: "View",
    }


class SweepStyleEnumField(
    EnumField[SweepStyleEnumAttrOperator, SweepStyleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SweepStyleEnumAttrOperator
    PLUG_CLS = SweepStyleEnumPlugOperator


class TransformModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NON_PROPORTIONAL = 0
    PROPORTIONAL = 1


class TransformModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NON_PROPORTIONAL = 0
    PROPORTIONAL = 1

    NAME_MAP = {
        NON_PROPORTIONAL: "Non proportional",
        PROPORTIONAL: "Proportional",
    }


class TransformModeEnumField(
    EnumField[TransformModeEnumAttrOperator, TransformModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransformModeEnumAttrOperator
    PLUG_CLS = TransformModeEnumPlugOperator


class DpBirailSrf(DG):
    __slots__ = ()

    NODE_TYPE = "dpBirailSrf"

    inputRail1 = DataNurbsCurveField()
    ir1 = inputRail1

    inputRail2 = DataNurbsCurveField()
    ir2 = inputRail2

    sweepStyle = SweepStyleEnumField()
    ss = sweepStyle

    transformMode = TransformModeEnumField()
    tm = transformMode

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface

    surfaceCache = DataNurbsSurfaceField()
    sc = surfaceCache

    inputProfile1 = DataNurbsCurveField()
    ip1 = inputProfile1

    inputProfile2 = DataNurbsCurveField()
    ip2 = inputProfile2

    blendFactor = DoubleField()
    bl = blendFactor

    tangentContinuityProfile1 = BoolField()
    tp1 = tangentContinuityProfile1

    tangentContinuityProfile2 = BoolField()
    tp2 = tangentContinuityProfile2
