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
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.string import DataStringField
from ..std.dt.vector_array import DataVectorArrayField
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
    wl.w = weights


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField()
    wl.w = weights


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class ManipulatorTransformsPlugOperator(
    CompoundPlugOperator["ManipulatorTransformsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("manipulatorPositionsPP", "manipulatorPositionsPP"),
        ("manipulatorWordPositionsPP", "manipulatorWordPositionsPP"),
        ("manipulatorLinePositionsPP", "manipulatorLinePositionsPP"),
        ("manipulatorRotationsPP", "manipulatorRotationsPP"),
        ("manipulatorWordRotationsPP", "manipulatorWordRotationsPP"),
        ("manipulatorLineRotationsPP", "manipulatorLineRotationsPP"),
        ("manipulatorScalesPP", "manipulatorScalesPP"),
        ("manipulatorWordScalesPP", "manipulatorWordScalesPP"),
        ("manipulatorLineScalesPP", "manipulatorLineScalesPP"),
        ("manipulateId", "manipulateId"),
        ("manipulatePolygon", "manipulatePolygon"),
        ("manipulateWord", "manipulateWord"),
        ("manipulateLine", "manipulateLine"),
        ("alignmentAdjustments", "alignmentAdjustments"),
        ("manipulatorMode", "manipulatorMode"),
    )

    manipulatorPositionsPP = DataVectorArrayField()

    manipulatorWordPositionsPP = DataVectorArrayField()

    manipulatorLinePositionsPP = DataVectorArrayField()

    manipulatorRotationsPP = DataVectorArrayField()

    manipulatorWordRotationsPP = DataVectorArrayField()

    manipulatorLineRotationsPP = DataVectorArrayField()

    manipulatorScalesPP = DataVectorArrayField()

    manipulatorWordScalesPP = DataVectorArrayField()

    manipulatorLineScalesPP = DataVectorArrayField()

    manipulateId = LongField()

    manipulatePolygon = LongField()

    manipulateWord = LongField()

    manipulateLine = LongField()

    alignmentAdjustments = DataDoubleArrayField()

    manipulatorMode = EnumField()


class ManipulatorTransformsAttrOperator(
    CompoundAttrOperator[ManipulatorTransformsPlugOperator]
):
    __slots__ = ()

    manipulatorPositionsPP = DataVectorArrayField()

    manipulatorWordPositionsPP = DataVectorArrayField()

    manipulatorLinePositionsPP = DataVectorArrayField()

    manipulatorRotationsPP = DataVectorArrayField()

    manipulatorWordRotationsPP = DataVectorArrayField()

    manipulatorLineRotationsPP = DataVectorArrayField()

    manipulatorScalesPP = DataVectorArrayField()

    manipulatorWordScalesPP = DataVectorArrayField()

    manipulatorLineScalesPP = DataVectorArrayField()

    manipulateId = LongField()

    manipulatePolygon = LongField()

    manipulateWord = LongField()

    manipulateLine = LongField()

    alignmentAdjustments = DataDoubleArrayField()

    manipulatorMode = EnumField()


class ManipulatorTransformsField(
    CompoundField[ManipulatorTransformsAttrOperator, ManipulatorTransformsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ManipulatorTransformsAttrOperator
    PLUG_CLS = ManipulatorTransformsPlugOperator

    manipulatorPositionsPP = DataVectorArrayField()

    manipulatorWordPositionsPP = DataVectorArrayField()

    manipulatorLinePositionsPP = DataVectorArrayField()

    manipulatorRotationsPP = DataVectorArrayField()

    manipulatorWordRotationsPP = DataVectorArrayField()

    manipulatorLineRotationsPP = DataVectorArrayField()

    manipulatorScalesPP = DataVectorArrayField()

    manipulatorWordScalesPP = DataVectorArrayField()

    manipulatorLineScalesPP = DataVectorArrayField()

    manipulateId = LongField()

    manipulatePolygon = LongField()

    manipulateWord = LongField()

    manipulateLine = LongField()

    alignmentAdjustments = DataDoubleArrayField()

    manipulatorMode = EnumField()


class GroupingPlugOperator(
    CompoundPlugOperator["GroupingAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("solidsPerCharacter", "solidsPerCharacter"),
        ("solidsPerWord", "solidsPerWord"),
        ("solidsPerLine", "solidsPerLine"),
    )

    solidsPerCharacter = DataDoubleArrayField()

    solidsPerWord = DataDoubleArrayField()

    solidsPerLine = DataDoubleArrayField()


class GroupingAttrOperator(
    CompoundAttrOperator[GroupingPlugOperator]
):
    __slots__ = ()

    solidsPerCharacter = DataDoubleArrayField()

    solidsPerWord = DataDoubleArrayField()

    solidsPerLine = DataDoubleArrayField()


class GroupingField(
    CompoundField[GroupingAttrOperator, GroupingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GroupingAttrOperator
    PLUG_CLS = GroupingPlugOperator

    solidsPerCharacter = DataDoubleArrayField()

    solidsPerWord = DataDoubleArrayField()

    solidsPerLine = DataDoubleArrayField()
