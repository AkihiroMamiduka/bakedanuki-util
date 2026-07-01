# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.matrix import DataMatrixField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
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


class SoftModXformsPlugOperator(
    CompoundPlugOperator["SoftModXformsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("preMatrix", "pre"),
        ("weightedMatrix", "wt"),
        ("postMatrix", "post"),
    )

    preMatrix = DataMatrixField()
    pre = preMatrix

    weightedMatrix = DataMatrixField()
    wt = weightedMatrix

    postMatrix = DataMatrixField()
    post = postMatrix


class SoftModXformsAttrOperator(
    CompoundAttrOperator[SoftModXformsPlugOperator]
):
    __slots__ = ()

    preMatrix = DataMatrixField()
    pre = preMatrix

    weightedMatrix = DataMatrixField()
    wt = weightedMatrix

    postMatrix = DataMatrixField()
    post = postMatrix


class SoftModXformsField(
    CompoundField[SoftModXformsAttrOperator, SoftModXformsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SoftModXformsAttrOperator
    PLUG_CLS = SoftModXformsPlugOperator

    preMatrix = DataMatrixField()
    pre = preMatrix

    weightedMatrix = DataMatrixField()
    wt = weightedMatrix

    postMatrix = DataMatrixField()
    post = postMatrix


class FalloffCurvePlugOperator(
    CompoundPlugOperator["FalloffCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffCurve_Position", "fcp"),
        ("falloffCurve_FloatValue", "fcfv"),
        ("falloffCurve_Interp", "fci"),
    )

    falloffCurve_Position = FloatField()
    fcp = falloffCurve_Position

    falloffCurve_FloatValue = FloatField()
    fcfv = falloffCurve_FloatValue

    falloffCurve_Interp = EnumField()
    fci = falloffCurve_Interp


class FalloffCurveAttrOperator(
    CompoundAttrOperator[FalloffCurvePlugOperator]
):
    __slots__ = ()

    falloffCurve_Position = FloatField()
    fcp = falloffCurve_Position

    falloffCurve_FloatValue = FloatField()
    fcfv = falloffCurve_FloatValue

    falloffCurve_Interp = EnumField()
    fci = falloffCurve_Interp


class FalloffCurveField(
    CompoundField[FalloffCurveAttrOperator, FalloffCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffCurveAttrOperator
    PLUG_CLS = FalloffCurvePlugOperator


class FalloffCenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["FalloffCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffCenterX", "fcx"),
        ("falloffCenterY", "fcy"),
        ("falloffCenterZ", "fcz"),
    )

    falloffCenterX = DoubleLinearField()
    fcx = falloffCenterX

    falloffCenterY = DoubleLinearField()
    fcy = falloffCenterY

    falloffCenterZ = DoubleLinearField()
    fcz = falloffCenterZ


class FalloffCenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[FalloffCenterPlugOperator]
):
    __slots__ = ()

    falloffCenterX = DoubleLinearField()
    fcx = falloffCenterX

    falloffCenterY = DoubleLinearField()
    fcy = falloffCenterY

    falloffCenterZ = DoubleLinearField()
    fcz = falloffCenterZ


class FalloffCenterField(
    DoubleLinear3CompoundBaseField[FalloffCenterAttrOperator, FalloffCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffCenterAttrOperator
    PLUG_CLS = FalloffCenterPlugOperator

    falloffCenterX = DoubleLinearField()
    fcx = falloffCenterX

    falloffCenterY = DoubleLinearField()
    fcy = falloffCenterY

    falloffCenterZ = DoubleLinearField()
    fcz = falloffCenterZ
