# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField


class VectorMessagesPlugOperator(
    CompoundPlugOperator["VectorMessagesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("animationMessage", "animationMessage"),
        ("extrudeMessage", "extrudeMessage"),
        ("transformMessage", "transformMessage"),
        ("remeshMessage", "remeshMessage"),
        ("adjustMessage", "adjustMessage"),
    )

    animationMessage = MessageField()

    extrudeMessage = MessageField()

    transformMessage = MessageField()

    remeshMessage = MessageField()

    adjustMessage = MessageField()


class VectorMessagesAttrOperator(
    CompoundAttrOperator[VectorMessagesPlugOperator]
):
    __slots__ = ()

    animationMessage = MessageField()

    extrudeMessage = MessageField()

    transformMessage = MessageField()

    remeshMessage = MessageField()

    adjustMessage = MessageField()


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

    adjustMessage = MessageField()


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
