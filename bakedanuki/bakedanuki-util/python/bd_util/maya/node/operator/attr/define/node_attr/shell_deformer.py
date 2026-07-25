# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.typed import TypedField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
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

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
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

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
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


class WeightListPlugOperator(
    CompoundPlugOperator["WeightListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weights", "wl.w"),
    )

    weights = FloatField(multi=True, default_value=1.0)


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField(multi=True, default_value=1.0)


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

    animationPositionX = DoubleLinearField(default_value=0.0)

    animationPositionY = DoubleLinearField(default_value=0.0)

    animationPositionZ = DoubleLinearField(default_value=0.0)


class AnimationPositionAttrOperator(
    CompoundAttrOperator[AnimationPositionPlugOperator]
):
    __slots__ = ()

    animationPositionX = DoubleLinearField(default_value=0.0)

    animationPositionY = DoubleLinearField(default_value=0.0)

    animationPositionZ = DoubleLinearField(default_value=0.0)


class AnimationPositionField(
    CompoundField[AnimationPositionAttrOperator, AnimationPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimationPositionAttrOperator
    PLUG_CLS = AnimationPositionPlugOperator

    animationPositionX = DoubleLinearField(default_value=0.0)

    animationPositionY = DoubleLinearField(default_value=0.0)

    animationPositionZ = DoubleLinearField(default_value=0.0)


class AnimationRotationPlugOperator(
    CompoundPlugOperator["AnimationRotationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("animationRotationX", "animationRotationX"),
        ("animationRotationY", "animationRotationY"),
        ("animationRotationZ", "animationRotationZ"),
    )

    animationRotationX = DoubleAngleField(default_value=0.0)

    animationRotationY = DoubleAngleField(default_value=0.0)

    animationRotationZ = DoubleAngleField(default_value=0.0)


class AnimationRotationAttrOperator(
    CompoundAttrOperator[AnimationRotationPlugOperator]
):
    __slots__ = ()

    animationRotationX = DoubleAngleField(default_value=0.0)

    animationRotationY = DoubleAngleField(default_value=0.0)

    animationRotationZ = DoubleAngleField(default_value=0.0)


class AnimationRotationField(
    CompoundField[AnimationRotationAttrOperator, AnimationRotationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimationRotationAttrOperator
    PLUG_CLS = AnimationRotationPlugOperator

    animationRotationX = DoubleAngleField(default_value=0.0)

    animationRotationY = DoubleAngleField(default_value=0.0)

    animationRotationZ = DoubleAngleField(default_value=0.0)


class AnimationScalePlugOperator(
    CompoundPlugOperator["AnimationScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("animationScaleX", "animationScaleX"),
        ("animationScaleY", "animationScaleY"),
        ("animationScaleZ", "animationScaleZ"),
    )

    animationScaleX = DoubleField(default_value=1.0)

    animationScaleY = DoubleField(default_value=1.0)

    animationScaleZ = DoubleField(default_value=1.0)


class AnimationScaleAttrOperator(
    CompoundAttrOperator[AnimationScalePlugOperator]
):
    __slots__ = ()

    animationScaleX = DoubleField(default_value=1.0)

    animationScaleY = DoubleField(default_value=1.0)

    animationScaleZ = DoubleField(default_value=1.0)


class AnimationScaleField(
    CompoundField[AnimationScaleAttrOperator, AnimationScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimationScaleAttrOperator
    PLUG_CLS = AnimationScalePlugOperator

    animationScaleX = DoubleField(default_value=1.0)

    animationScaleY = DoubleField(default_value=1.0)

    animationScaleZ = DoubleField(default_value=1.0)
