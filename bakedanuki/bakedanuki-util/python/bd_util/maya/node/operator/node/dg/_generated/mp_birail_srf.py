# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class GeneratedMpBirailSrf(DG):
    __slots__ = ()

    NODE_TYPE = "mpBirailSrf"

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

    inputProfile = DataNurbsCurveField(multi=True)
    ip = inputProfile

    tangentContinuityProfile1 = BoolField(default_value=False)
    tp1 = tangentContinuityProfile1

    tangentContinuityProfile2 = BoolField(default_value=False)
    tp2 = tangentContinuityProfile2
