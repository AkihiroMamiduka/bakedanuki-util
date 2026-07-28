# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.long_compound.long2_compound._base import (
    Long2CompoundBaseAttrOperator,
    Long2CompoundBasePlugOperator,
    Long2CompoundBaseField,
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


class PositionAdjustPlugOperator(
    Double3CompoundBasePlugOperator["PositionAdjustAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionAdjust0", "positionAdjust0"),
        ("positionAdjust1", "positionAdjust1"),
        ("positionAdjust2", "positionAdjust2"),
    )

    positionAdjust0 = DoubleField(default_value=0.0)

    positionAdjust1 = DoubleField(default_value=0.0)

    positionAdjust2 = DoubleField(default_value=0.0)


class PositionAdjustAttrOperator(
    Double3CompoundBaseAttrOperator[PositionAdjustPlugOperator]
):
    __slots__ = ()

    positionAdjust0 = DoubleField(default_value=0.0)

    positionAdjust1 = DoubleField(default_value=0.0)

    positionAdjust2 = DoubleField(default_value=0.0)


class PositionAdjustField(
    Double3CompoundBaseField[
        PositionAdjustAttrOperator, PositionAdjustPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PositionAdjustAttrOperator
    PLUG_CLS = PositionAdjustPlugOperator

    positionAdjust0 = DoubleField(default_value=0.0)

    positionAdjust1 = DoubleField(default_value=0.0)

    positionAdjust2 = DoubleField(default_value=0.0)


class RotationAdjustPlugOperator(
    Double3CompoundBasePlugOperator["RotationAdjustAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationAdjust0", "rotationAdjust0"),
        ("rotationAdjust1", "rotationAdjust1"),
        ("rotationAdjust2", "rotationAdjust2"),
    )

    rotationAdjust0 = DoubleField(default_value=0.0)

    rotationAdjust1 = DoubleField(default_value=0.0)

    rotationAdjust2 = DoubleField(default_value=0.0)


class RotationAdjustAttrOperator(
    Double3CompoundBaseAttrOperator[RotationAdjustPlugOperator]
):
    __slots__ = ()

    rotationAdjust0 = DoubleField(default_value=0.0)

    rotationAdjust1 = DoubleField(default_value=0.0)

    rotationAdjust2 = DoubleField(default_value=0.0)


class RotationAdjustField(
    Double3CompoundBaseField[
        RotationAdjustAttrOperator, RotationAdjustPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RotationAdjustAttrOperator
    PLUG_CLS = RotationAdjustPlugOperator

    rotationAdjust0 = DoubleField(default_value=0.0)

    rotationAdjust1 = DoubleField(default_value=0.0)

    rotationAdjust2 = DoubleField(default_value=0.0)


class ScaleAdjustPlugOperator(
    Double3CompoundBasePlugOperator["ScaleAdjustAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleAdjust0", "scaleAdjust0"),
        ("scaleAdjust1", "scaleAdjust1"),
        ("scaleAdjust2", "scaleAdjust2"),
    )

    scaleAdjust0 = DoubleField(default_value=0.0)

    scaleAdjust1 = DoubleField(default_value=0.0)

    scaleAdjust2 = DoubleField(default_value=0.0)


class ScaleAdjustAttrOperator(
    Double3CompoundBaseAttrOperator[ScaleAdjustPlugOperator]
):
    __slots__ = ()

    scaleAdjust0 = DoubleField(default_value=0.0)

    scaleAdjust1 = DoubleField(default_value=0.0)

    scaleAdjust2 = DoubleField(default_value=0.0)


class ScaleAdjustField(
    Double3CompoundBaseField[ScaleAdjustAttrOperator, ScaleAdjustPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAdjustAttrOperator
    PLUG_CLS = ScaleAdjustPlugOperator

    scaleAdjust0 = DoubleField(default_value=0.0)

    scaleAdjust1 = DoubleField(default_value=0.0)

    scaleAdjust2 = DoubleField(default_value=0.0)


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


class VectorMessagesPlugOperator(
    CompoundPlugOperator["VectorMessagesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("animationMessage", "animationMessage"),
        ("extrudeMessage", "extrudeMessage"),
        ("transformMessage", "transformMessage"),
        ("remeshMessage", "remeshMessage"),
    )

    animationMessage = MessageField()

    extrudeMessage = MessageField()

    transformMessage = MessageField()

    remeshMessage = MessageField()


class VectorMessagesAttrOperator(
    CompoundAttrOperator[VectorMessagesPlugOperator]
):
    __slots__ = ()

    animationMessage = MessageField()

    extrudeMessage = MessageField()

    transformMessage = MessageField()

    remeshMessage = MessageField()


class VectorMessagesField(
    CompoundField[VectorMessagesAttrOperator, VectorMessagesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VectorMessagesAttrOperator
    PLUG_CLS = VectorMessagesPlugOperator

    animationMessage = MessageField()

    extrudeMessage = MessageField()

    transformMessage = MessageField()

    remeshMessage = MessageField()


class RandomRangePlugOperator(
    Long2CompoundBasePlugOperator["RandomRangeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("randomRange0", "randomRange0"),
        ("randomRange1", "randomRange1"),
    )

    randomRange0 = LongField(default_value=0)

    randomRange1 = LongField(default_value=10)


class RandomRangeAttrOperator(
    Long2CompoundBaseAttrOperator[RandomRangePlugOperator]
):
    __slots__ = ()

    randomRange0 = LongField(default_value=0)

    randomRange1 = LongField(default_value=10)


class RandomRangeField(
    Long2CompoundBaseField[RandomRangeAttrOperator, RandomRangePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RandomRangeAttrOperator
    PLUG_CLS = RandomRangePlugOperator

    randomRange0 = LongField(default_value=0)

    randomRange1 = LongField(default_value=10)
