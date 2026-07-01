# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
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


class TranslateInPPPlugOperator(
    CompoundPlugOperator["TranslateInPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionInPP", "positionInPP"),
        ("scaleInPP", "scaleInPP"),
        ("rotationInPP", "rotationInPP"),
    )

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()


class TranslateInPPAttrOperator(
    CompoundAttrOperator[TranslateInPPPlugOperator]
):
    __slots__ = ()

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()


class TranslateInPPField(
    CompoundField[TranslateInPPAttrOperator, TranslateInPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateInPPAttrOperator
    PLUG_CLS = TranslateInPPPlugOperator

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()


class AnimationPositionPlugOperator(
    CompoundPlugOperator["AnimationPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("animationPositionX", "animationPositionX"),
        ("animationPositionY", "animationPositionY"),
        ("animationPositionZ", "animationPositionZ"),
    )

    animationPositionX = DoubleLinearField()

    animationPositionY = DoubleLinearField()

    animationPositionZ = DoubleLinearField()


class AnimationPositionAttrOperator(
    CompoundAttrOperator[AnimationPositionPlugOperator]
):
    __slots__ = ()

    animationPositionX = DoubleLinearField()

    animationPositionY = DoubleLinearField()

    animationPositionZ = DoubleLinearField()


class AnimationPositionField(
    CompoundField[AnimationPositionAttrOperator, AnimationPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimationPositionAttrOperator
    PLUG_CLS = AnimationPositionPlugOperator

    animationPositionX = DoubleLinearField()

    animationPositionY = DoubleLinearField()

    animationPositionZ = DoubleLinearField()


class AnimationRotationPlugOperator(
    CompoundPlugOperator["AnimationRotationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("animationRotationX", "animationRotationX"),
        ("animationRotationY", "animationRotationY"),
        ("animationRotationZ", "animationRotationZ"),
    )

    animationRotationX = DoubleAngleField()

    animationRotationY = DoubleAngleField()

    animationRotationZ = DoubleAngleField()


class AnimationRotationAttrOperator(
    CompoundAttrOperator[AnimationRotationPlugOperator]
):
    __slots__ = ()

    animationRotationX = DoubleAngleField()

    animationRotationY = DoubleAngleField()

    animationRotationZ = DoubleAngleField()


class AnimationRotationField(
    CompoundField[AnimationRotationAttrOperator, AnimationRotationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimationRotationAttrOperator
    PLUG_CLS = AnimationRotationPlugOperator

    animationRotationX = DoubleAngleField()

    animationRotationY = DoubleAngleField()

    animationRotationZ = DoubleAngleField()


class AnimationScalePlugOperator(
    CompoundPlugOperator["AnimationScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("animationScaleX", "animationScaleX"),
        ("animationScaleY", "animationScaleY"),
        ("animationScaleZ", "animationScaleZ"),
    )

    animationScaleX = DoubleField()

    animationScaleY = DoubleField()

    animationScaleZ = DoubleField()


class AnimationScaleAttrOperator(
    CompoundAttrOperator[AnimationScalePlugOperator]
):
    __slots__ = ()

    animationScaleX = DoubleField()

    animationScaleY = DoubleField()

    animationScaleZ = DoubleField()


class AnimationScaleField(
    CompoundField[AnimationScaleAttrOperator, AnimationScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimationScaleAttrOperator
    PLUG_CLS = AnimationScalePlugOperator

    animationScaleX = DoubleField()

    animationScaleY = DoubleField()

    animationScaleZ = DoubleField()
