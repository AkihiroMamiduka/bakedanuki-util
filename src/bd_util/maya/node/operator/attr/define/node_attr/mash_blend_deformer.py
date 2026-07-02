# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


class CurveRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CurveRamp_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class CurveRamp_InterpEnumField(
    EnumField[CurveRamp_InterpEnumAttrOperator, CurveRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurveRamp_InterpEnumAttrOperator
    PLUG_CLS = CurveRamp_InterpEnumPlugOperator


class InflationRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class InflationRamp_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class InflationRamp_InterpEnumField(
    EnumField[InflationRamp_InterpEnumAttrOperator, InflationRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InflationRamp_InterpEnumAttrOperator
    PLUG_CLS = InflationRamp_InterpEnumPlugOperator


class BlendRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class BlendRamp_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class BlendRamp_InterpEnumField(
    EnumField[BlendRamp_InterpEnumAttrOperator, BlendRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendRamp_InterpEnumAttrOperator
    PLUG_CLS = BlendRamp_InterpEnumPlugOperator


class SmoothingRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class SmoothingRamp_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class SmoothingRamp_InterpEnumField(
    EnumField[SmoothingRamp_InterpEnumAttrOperator, SmoothingRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmoothingRamp_InterpEnumAttrOperator
    PLUG_CLS = SmoothingRamp_InterpEnumPlugOperator


class InputPlugOperator(
    CompoundPlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputGeometry", "ig"),
        ("groupId", "gi"),
        ("componentTagExpression", "gtg"),
    )

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField()
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField()
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputField(
    CompoundField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class EnvelopeWeightsListPlugOperator(
    CompoundPlugOperator["EnvelopeWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("envelopeWeights", "owt"),
    )

    envelopeWeights = FloatField()
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField()
    owt = envelopeWeights


class EnvelopeWeightsListField(
    CompoundField[EnvelopeWeightsListAttrOperator, EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnvelopeWeightsListAttrOperator
    PLUG_CLS = EnvelopeWeightsListPlugOperator


class FunctionPlugOperator(
    Long3CompoundBasePlugOperator["FunctionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fchild1", "f1"),
        ("fchild2", "f2"),
        ("fchild3", "f3"),
    )

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class FunctionAttrOperator(
    Long3CompoundBaseAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class FunctionField(
    Long3CompoundBaseField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class WeightListPlugOperator(
    CompoundPlugOperator["WeightListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weights", "wl.w"),
    )

    weights = FloatField()


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField()


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class CurveRampPlugOperator(
    CompoundPlugOperator["CurveRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("curveRamp_Position", "curveRampp"),
        ("curveRamp_FloatValue", "curveRampfv"),
        ("curveRamp_Interp", "curveRampi"),
    )

    curveRamp_Position = FloatField()
    curveRampp = curveRamp_Position

    curveRamp_FloatValue = FloatField()
    curveRampfv = curveRamp_FloatValue

    curveRamp_Interp = CurveRamp_InterpEnumField()
    curveRampi = curveRamp_Interp


class CurveRampAttrOperator(
    CompoundAttrOperator[CurveRampPlugOperator]
):
    __slots__ = ()

    curveRamp_Position = FloatField()
    curveRampp = curveRamp_Position

    curveRamp_FloatValue = FloatField()
    curveRampfv = curveRamp_FloatValue

    curveRamp_Interp = CurveRamp_InterpEnumField()
    curveRampi = curveRamp_Interp


class CurveRampField(
    CompoundField[CurveRampAttrOperator, CurveRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurveRampAttrOperator
    PLUG_CLS = CurveRampPlugOperator


class InflationRampPlugOperator(
    CompoundPlugOperator["InflationRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inflationRamp_Position", "inflationRampp"),
        ("inflationRamp_FloatValue", "inflationRampfv"),
        ("inflationRamp_Interp", "inflationRampi"),
    )

    inflationRamp_Position = FloatField()
    inflationRampp = inflationRamp_Position

    inflationRamp_FloatValue = FloatField()
    inflationRampfv = inflationRamp_FloatValue

    inflationRamp_Interp = InflationRamp_InterpEnumField()
    inflationRampi = inflationRamp_Interp


class InflationRampAttrOperator(
    CompoundAttrOperator[InflationRampPlugOperator]
):
    __slots__ = ()

    inflationRamp_Position = FloatField()
    inflationRampp = inflationRamp_Position

    inflationRamp_FloatValue = FloatField()
    inflationRampfv = inflationRamp_FloatValue

    inflationRamp_Interp = InflationRamp_InterpEnumField()
    inflationRampi = inflationRamp_Interp


class InflationRampField(
    CompoundField[InflationRampAttrOperator, InflationRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InflationRampAttrOperator
    PLUG_CLS = InflationRampPlugOperator


class BlendRampPlugOperator(
    CompoundPlugOperator["BlendRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("blendRamp_Position", "blendRampp"),
        ("blendRamp_FloatValue", "blendRampfv"),
        ("blendRamp_Interp", "blendRampi"),
    )

    blendRamp_Position = FloatField()
    blendRampp = blendRamp_Position

    blendRamp_FloatValue = FloatField()
    blendRampfv = blendRamp_FloatValue

    blendRamp_Interp = BlendRamp_InterpEnumField()
    blendRampi = blendRamp_Interp


class BlendRampAttrOperator(
    CompoundAttrOperator[BlendRampPlugOperator]
):
    __slots__ = ()

    blendRamp_Position = FloatField()
    blendRampp = blendRamp_Position

    blendRamp_FloatValue = FloatField()
    blendRampfv = blendRamp_FloatValue

    blendRamp_Interp = BlendRamp_InterpEnumField()
    blendRampi = blendRamp_Interp


class BlendRampField(
    CompoundField[BlendRampAttrOperator, BlendRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendRampAttrOperator
    PLUG_CLS = BlendRampPlugOperator


class SmoothingRampPlugOperator(
    CompoundPlugOperator["SmoothingRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("smoothingRamp_Position", "smoothingRampp"),
        ("smoothingRamp_FloatValue", "smoothingRampfv"),
        ("smoothingRamp_Interp", "smoothingRampi"),
    )

    smoothingRamp_Position = FloatField()
    smoothingRampp = smoothingRamp_Position

    smoothingRamp_FloatValue = FloatField()
    smoothingRampfv = smoothingRamp_FloatValue

    smoothingRamp_Interp = SmoothingRamp_InterpEnumField()
    smoothingRampi = smoothingRamp_Interp


class SmoothingRampAttrOperator(
    CompoundAttrOperator[SmoothingRampPlugOperator]
):
    __slots__ = ()

    smoothingRamp_Position = FloatField()
    smoothingRampp = smoothingRamp_Position

    smoothingRamp_FloatValue = FloatField()
    smoothingRampfv = smoothingRamp_FloatValue

    smoothingRamp_Interp = SmoothingRamp_InterpEnumField()
    smoothingRampi = smoothingRamp_Interp


class SmoothingRampField(
    CompoundField[SmoothingRampAttrOperator, SmoothingRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmoothingRampAttrOperator
    PLUG_CLS = SmoothingRampPlugOperator


class MColourPlugOperator(
    Float3CompoundBasePlugOperator["MColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mColourR", "mcr"),
        ("mColourG", "mcg"),
        ("mColourB", "mcb"),
    )

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourAttrOperator(
    Float3CompoundBaseAttrOperator[MColourPlugOperator]
):
    __slots__ = ()

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB
