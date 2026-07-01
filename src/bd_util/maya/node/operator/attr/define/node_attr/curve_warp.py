# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


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


class ScaleCurvePlugOperator(
    CompoundPlugOperator["ScaleCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleCurve_Position", "scaleCurvep"),
        ("scaleCurve_Value", "scaleCurvev"),
    )

    scaleCurve_Position = FloatField()
    scaleCurvep = scaleCurve_Position

    scaleCurve_Value = FloatField()
    scaleCurvev = scaleCurve_Value


class ScaleCurveAttrOperator(
    CompoundAttrOperator[ScaleCurvePlugOperator]
):
    __slots__ = ()

    scaleCurve_Position = FloatField()
    scaleCurvep = scaleCurve_Position

    scaleCurve_Value = FloatField()
    scaleCurvev = scaleCurve_Value


class ScaleCurveField(
    CompoundField[ScaleCurveAttrOperator, ScaleCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleCurveAttrOperator
    PLUG_CLS = ScaleCurvePlugOperator


class TwistCurvePlugOperator(
    CompoundPlugOperator["TwistCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("twistCurve_Position", "twistCurvep"),
        ("twistCurve_Value", "twistCurvev"),
    )

    twistCurve_Position = FloatField()
    twistCurvep = twistCurve_Position

    twistCurve_Value = FloatField()
    twistCurvev = twistCurve_Value


class TwistCurveAttrOperator(
    CompoundAttrOperator[TwistCurvePlugOperator]
):
    __slots__ = ()

    twistCurve_Position = FloatField()
    twistCurvep = twistCurve_Position

    twistCurve_Value = FloatField()
    twistCurvev = twistCurve_Value


class TwistCurveField(
    CompoundField[TwistCurveAttrOperator, TwistCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TwistCurveAttrOperator
    PLUG_CLS = TwistCurvePlugOperator
