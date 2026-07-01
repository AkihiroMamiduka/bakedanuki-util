# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField


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
