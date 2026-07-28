# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class SweepStyleEnumPlugOperator(EnumPlugOperator["SweepStyleEnumAttrOperator"]):
    __slots__ = ()

    NATURAL = 0
    VIEW = 1


class SweepStyleEnumAttrOperator(EnumAttrOperator[SweepStyleEnumPlugOperator]):
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


class TransformModeEnumPlugOperator(EnumPlugOperator["TransformModeEnumAttrOperator"]):
    __slots__ = ()

    NON_PROPORTIONAL = 0
    PROPORTIONAL = 1


class TransformModeEnumAttrOperator(EnumAttrOperator[TransformModeEnumPlugOperator]):
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


class GeneratedDpBirailSrf(DG):
    __slots__ = ()

    NODE_TYPE = "dpBirailSrf"

    inputRail1 = DataNurbsCurveField()
    ir1 = inputRail1

    inputRail2 = DataNurbsCurveField()
    ir2 = inputRail2

    sweepStyle = SweepStyleEnumField(default_value=0, writable=False)
    ss = sweepStyle

    transformMode = TransformModeEnumField(default_value=0)
    tm = transformMode

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface

    surfaceCache = DataNurbsSurfaceField()
    sc = surfaceCache

    inputProfile1 = DataNurbsCurveField()
    ip1 = inputProfile1

    inputProfile2 = DataNurbsCurveField()
    ip2 = inputProfile2

    blendFactor = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    bl = blendFactor

    tangentContinuityProfile1 = BoolField(default_value=False)
    tp1 = tangentContinuityProfile1

    tangentContinuityProfile2 = BoolField(default_value=False)
    tp2 = tangentContinuityProfile2
