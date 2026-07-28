# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.string import DataStringField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


class ManipulatorModeEnumPlugOperator(
    EnumPlugOperator["ManipulatorModeEnumAttrOperator"]
):
    __slots__ = ()

    CHARACTER = 0
    WORD = 1
    LINE = 2


class ManipulatorModeEnumAttrOperator(
    EnumAttrOperator[ManipulatorModeEnumPlugOperator]
):
    __slots__ = ()

    CHARACTER = 0
    WORD = 1
    LINE = 2

    NAME_MAP = {
        CHARACTER: "Character",
        WORD: "Word",
        LINE: "Line",
    }


class ManipulatorModeEnumField(
    EnumField[ManipulatorModeEnumAttrOperator, ManipulatorModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ManipulatorModeEnumAttrOperator
    PLUG_CLS = ManipulatorModeEnumPlugOperator


class InputPlugOperator(CompoundPlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputGeometry", "ig"),
        ("groupId", "gi"),
        ("componentTagExpression", "gtg"),
    )

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(CompoundAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputField(CompoundField[InputAttrOperator, InputPlugOperator]):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class EnvelopeWeightsListPlugOperator(
    CompoundPlugOperator["EnvelopeWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("envelopeWeights", "owt"),)

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListField(
    CompoundField[
        EnvelopeWeightsListAttrOperator, EnvelopeWeightsListPlugOperator
    ]
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

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class FunctionAttrOperator(
    Long3CompoundBaseAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class FunctionField(
    Long3CompoundBaseField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class WeightListPlugOperator(CompoundPlugOperator["WeightListAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weights", "wl.w"),)

    weights = FloatField(multi=True, default_value=1.0)


class WeightListAttrOperator(CompoundAttrOperator[WeightListPlugOperator]):
    __slots__ = ()

    weights = FloatField(multi=True, default_value=1.0)


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

    manipulateId = LongField(default_value=0)

    manipulatePolygon = LongField(default_value=0)

    manipulateWord = LongField(default_value=0)

    manipulateLine = LongField(default_value=0)

    alignmentAdjustments = DataDoubleArrayField()

    manipulatorMode = ManipulatorModeEnumField(default_value=1)


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

    manipulateId = LongField(default_value=0)

    manipulatePolygon = LongField(default_value=0)

    manipulateWord = LongField(default_value=0)

    manipulateLine = LongField(default_value=0)

    alignmentAdjustments = DataDoubleArrayField()

    manipulatorMode = ManipulatorModeEnumField(default_value=1)


class ManipulatorTransformsField(
    CompoundField[
        ManipulatorTransformsAttrOperator, ManipulatorTransformsPlugOperator
    ]
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

    manipulateId = LongField(default_value=0)

    manipulatePolygon = LongField(default_value=0)

    manipulateWord = LongField(default_value=0)

    manipulateLine = LongField(default_value=0)

    alignmentAdjustments = DataDoubleArrayField()

    manipulatorMode = ManipulatorModeEnumField(default_value=1)


class GroupingPlugOperator(CompoundPlugOperator["GroupingAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("solidsPerCharacter", "solidsPerCharacter"),
        ("solidsPerWord", "solidsPerWord"),
        ("solidsPerLine", "solidsPerLine"),
    )

    solidsPerCharacter = DataDoubleArrayField()

    solidsPerWord = DataDoubleArrayField()

    solidsPerLine = DataDoubleArrayField()


class GroupingAttrOperator(CompoundAttrOperator[GroupingPlugOperator]):
    __slots__ = ()

    solidsPerCharacter = DataDoubleArrayField()

    solidsPerWord = DataDoubleArrayField()

    solidsPerLine = DataDoubleArrayField()


class GroupingField(CompoundField[GroupingAttrOperator, GroupingPlugOperator]):
    __slots__ = ()

    ATTR_CLS = GroupingAttrOperator
    PLUG_CLS = GroupingPlugOperator

    solidsPerCharacter = DataDoubleArrayField()

    solidsPerWord = DataDoubleArrayField()

    solidsPerLine = DataDoubleArrayField()
