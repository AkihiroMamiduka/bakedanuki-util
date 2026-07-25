# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField


class HipsEffectorPivotPlugOperator(
    CompoundPlugOperator["HipsEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HipsEffectorPivotX", "HipsEffectorPivotX"),
        ("HipsEffectorPivotY", "HipsEffectorPivotY"),
        ("HipsEffectorPivotZ", "HipsEffectorPivotZ"),
    )

    HipsEffectorPivotX = DoubleLinearField(default_value=0.0)

    HipsEffectorPivotY = DoubleLinearField(default_value=0.0)

    HipsEffectorPivotZ = DoubleLinearField(default_value=0.0)


class HipsEffectorPivotAttrOperator(
    CompoundAttrOperator[HipsEffectorPivotPlugOperator]
):
    __slots__ = ()

    HipsEffectorPivotX = DoubleLinearField(default_value=0.0)

    HipsEffectorPivotY = DoubleLinearField(default_value=0.0)

    HipsEffectorPivotZ = DoubleLinearField(default_value=0.0)


class HipsEffectorPivotField(
    CompoundField[HipsEffectorPivotAttrOperator, HipsEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsEffectorPivotAttrOperator
    PLUG_CLS = HipsEffectorPivotPlugOperator


class LeftAnkleEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftAnkleEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftAnkleEffectorPivotX", "LeftAnkleEffectorPivotX"),
        ("LeftAnkleEffectorPivotY", "LeftAnkleEffectorPivotY"),
        ("LeftAnkleEffectorPivotZ", "LeftAnkleEffectorPivotZ"),
    )

    LeftAnkleEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftAnkleEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftAnkleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftAnkleEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftAnkleEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftAnkleEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftAnkleEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftAnkleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftAnkleEffectorPivotField(
    CompoundField[LeftAnkleEffectorPivotAttrOperator, LeftAnkleEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftAnkleEffectorPivotAttrOperator
    PLUG_CLS = LeftAnkleEffectorPivotPlugOperator


class RightAnkleEffectorPivotPlugOperator(
    CompoundPlugOperator["RightAnkleEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightAnkleEffectorPivotX", "RightAnkleEffectorPivotX"),
        ("RightAnkleEffectorPivotY", "RightAnkleEffectorPivotY"),
        ("RightAnkleEffectorPivotZ", "RightAnkleEffectorPivotZ"),
    )

    RightAnkleEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightAnkleEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightAnkleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightAnkleEffectorPivotAttrOperator(
    CompoundAttrOperator[RightAnkleEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightAnkleEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightAnkleEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightAnkleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightAnkleEffectorPivotField(
    CompoundField[RightAnkleEffectorPivotAttrOperator, RightAnkleEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightAnkleEffectorPivotAttrOperator
    PLUG_CLS = RightAnkleEffectorPivotPlugOperator


class LeftWristEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftWristEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftWristEffectorPivotX", "LeftWristEffectorPivotX"),
        ("LeftWristEffectorPivotY", "LeftWristEffectorPivotY"),
        ("LeftWristEffectorPivotZ", "LeftWristEffectorPivotZ"),
    )

    LeftWristEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftWristEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftWristEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftWristEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftWristEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftWristEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftWristEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftWristEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftWristEffectorPivotField(
    CompoundField[LeftWristEffectorPivotAttrOperator, LeftWristEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftWristEffectorPivotAttrOperator
    PLUG_CLS = LeftWristEffectorPivotPlugOperator


class RightWristEffectorPivotPlugOperator(
    CompoundPlugOperator["RightWristEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightWristEffectorPivotX", "RightWristEffectorPivotX"),
        ("RightWristEffectorPivotY", "RightWristEffectorPivotY"),
        ("RightWristEffectorPivotZ", "RightWristEffectorPivotZ"),
    )

    RightWristEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightWristEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightWristEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightWristEffectorPivotAttrOperator(
    CompoundAttrOperator[RightWristEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightWristEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightWristEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightWristEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightWristEffectorPivotField(
    CompoundField[RightWristEffectorPivotAttrOperator, RightWristEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightWristEffectorPivotAttrOperator
    PLUG_CLS = RightWristEffectorPivotPlugOperator


class LeftKneeEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftKneeEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftKneeEffectorPivotX", "LeftKneeEffectorPivotX"),
        ("LeftKneeEffectorPivotY", "LeftKneeEffectorPivotY"),
        ("LeftKneeEffectorPivotZ", "LeftKneeEffectorPivotZ"),
    )

    LeftKneeEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftKneeEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftKneeEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftKneeEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftKneeEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftKneeEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftKneeEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftKneeEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftKneeEffectorPivotField(
    CompoundField[LeftKneeEffectorPivotAttrOperator, LeftKneeEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftKneeEffectorPivotAttrOperator
    PLUG_CLS = LeftKneeEffectorPivotPlugOperator


class RightKneeEffectorPivotPlugOperator(
    CompoundPlugOperator["RightKneeEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightKneeEffectorPivotX", "RightKneeEffectorPivotX"),
        ("RightKneeEffectorPivotY", "RightKneeEffectorPivotY"),
        ("RightKneeEffectorPivotZ", "RightKneeEffectorPivotZ"),
    )

    RightKneeEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightKneeEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightKneeEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightKneeEffectorPivotAttrOperator(
    CompoundAttrOperator[RightKneeEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightKneeEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightKneeEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightKneeEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightKneeEffectorPivotField(
    CompoundField[RightKneeEffectorPivotAttrOperator, RightKneeEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightKneeEffectorPivotAttrOperator
    PLUG_CLS = RightKneeEffectorPivotPlugOperator


class LeftElbowEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftElbowEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftElbowEffectorPivotX", "LeftElbowEffectorPivotX"),
        ("LeftElbowEffectorPivotY", "LeftElbowEffectorPivotY"),
        ("LeftElbowEffectorPivotZ", "LeftElbowEffectorPivotZ"),
    )

    LeftElbowEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftElbowEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftElbowEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftElbowEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftElbowEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftElbowEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftElbowEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftElbowEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftElbowEffectorPivotField(
    CompoundField[LeftElbowEffectorPivotAttrOperator, LeftElbowEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftElbowEffectorPivotAttrOperator
    PLUG_CLS = LeftElbowEffectorPivotPlugOperator


class RightElbowEffectorPivotPlugOperator(
    CompoundPlugOperator["RightElbowEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightElbowEffectorPivotX", "RightElbowEffectorPivotX"),
        ("RightElbowEffectorPivotY", "RightElbowEffectorPivotY"),
        ("RightElbowEffectorPivotZ", "RightElbowEffectorPivotZ"),
    )

    RightElbowEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightElbowEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightElbowEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightElbowEffectorPivotAttrOperator(
    CompoundAttrOperator[RightElbowEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightElbowEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightElbowEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightElbowEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightElbowEffectorPivotField(
    CompoundField[RightElbowEffectorPivotAttrOperator, RightElbowEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightElbowEffectorPivotAttrOperator
    PLUG_CLS = RightElbowEffectorPivotPlugOperator


class ChestOriginEffectorPivotPlugOperator(
    CompoundPlugOperator["ChestOriginEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ChestOriginEffectorPivotX", "ChestOriginEffectorPivotX"),
        ("ChestOriginEffectorPivotY", "ChestOriginEffectorPivotY"),
        ("ChestOriginEffectorPivotZ", "ChestOriginEffectorPivotZ"),
    )

    ChestOriginEffectorPivotX = DoubleLinearField(default_value=0.0)

    ChestOriginEffectorPivotY = DoubleLinearField(default_value=0.0)

    ChestOriginEffectorPivotZ = DoubleLinearField(default_value=0.0)


class ChestOriginEffectorPivotAttrOperator(
    CompoundAttrOperator[ChestOriginEffectorPivotPlugOperator]
):
    __slots__ = ()

    ChestOriginEffectorPivotX = DoubleLinearField(default_value=0.0)

    ChestOriginEffectorPivotY = DoubleLinearField(default_value=0.0)

    ChestOriginEffectorPivotZ = DoubleLinearField(default_value=0.0)


class ChestOriginEffectorPivotField(
    CompoundField[ChestOriginEffectorPivotAttrOperator, ChestOriginEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ChestOriginEffectorPivotAttrOperator
    PLUG_CLS = ChestOriginEffectorPivotPlugOperator


class ChestEndEffectorPivotPlugOperator(
    CompoundPlugOperator["ChestEndEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ChestEndEffectorPivotX", "ChestEndEffectorPivotX"),
        ("ChestEndEffectorPivotY", "ChestEndEffectorPivotY"),
        ("ChestEndEffectorPivotZ", "ChestEndEffectorPivotZ"),
    )

    ChestEndEffectorPivotX = DoubleLinearField(default_value=0.0)

    ChestEndEffectorPivotY = DoubleLinearField(default_value=0.0)

    ChestEndEffectorPivotZ = DoubleLinearField(default_value=0.0)


class ChestEndEffectorPivotAttrOperator(
    CompoundAttrOperator[ChestEndEffectorPivotPlugOperator]
):
    __slots__ = ()

    ChestEndEffectorPivotX = DoubleLinearField(default_value=0.0)

    ChestEndEffectorPivotY = DoubleLinearField(default_value=0.0)

    ChestEndEffectorPivotZ = DoubleLinearField(default_value=0.0)


class ChestEndEffectorPivotField(
    CompoundField[ChestEndEffectorPivotAttrOperator, ChestEndEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ChestEndEffectorPivotAttrOperator
    PLUG_CLS = ChestEndEffectorPivotPlugOperator


class LeftFootEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftFootEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootEffectorPivotX", "LeftFootEffectorPivotX"),
        ("LeftFootEffectorPivotY", "LeftFootEffectorPivotY"),
        ("LeftFootEffectorPivotZ", "LeftFootEffectorPivotZ"),
    )

    LeftFootEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootEffectorPivotField(
    CompoundField[LeftFootEffectorPivotAttrOperator, LeftFootEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootEffectorPivotAttrOperator
    PLUG_CLS = LeftFootEffectorPivotPlugOperator


class RightFootEffectorPivotPlugOperator(
    CompoundPlugOperator["RightFootEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootEffectorPivotX", "RightFootEffectorPivotX"),
        ("RightFootEffectorPivotY", "RightFootEffectorPivotY"),
        ("RightFootEffectorPivotZ", "RightFootEffectorPivotZ"),
    )

    RightFootEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootEffectorPivotField(
    CompoundField[RightFootEffectorPivotAttrOperator, RightFootEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootEffectorPivotAttrOperator
    PLUG_CLS = RightFootEffectorPivotPlugOperator


class LeftShoulderEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftShoulderEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftShoulderEffectorPivotX", "LeftShoulderEffectorPivotX"),
        ("LeftShoulderEffectorPivotY", "LeftShoulderEffectorPivotY"),
        ("LeftShoulderEffectorPivotZ", "LeftShoulderEffectorPivotZ"),
    )

    LeftShoulderEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftShoulderEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftShoulderEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftShoulderEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftShoulderEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftShoulderEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftShoulderEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftShoulderEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftShoulderEffectorPivotField(
    CompoundField[LeftShoulderEffectorPivotAttrOperator, LeftShoulderEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderEffectorPivotAttrOperator
    PLUG_CLS = LeftShoulderEffectorPivotPlugOperator


class RightShoulderEffectorPivotPlugOperator(
    CompoundPlugOperator["RightShoulderEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightShoulderEffectorPivotX", "RightShoulderEffectorPivotX"),
        ("RightShoulderEffectorPivotY", "RightShoulderEffectorPivotY"),
        ("RightShoulderEffectorPivotZ", "RightShoulderEffectorPivotZ"),
    )

    RightShoulderEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightShoulderEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightShoulderEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightShoulderEffectorPivotAttrOperator(
    CompoundAttrOperator[RightShoulderEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightShoulderEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightShoulderEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightShoulderEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightShoulderEffectorPivotField(
    CompoundField[RightShoulderEffectorPivotAttrOperator, RightShoulderEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderEffectorPivotAttrOperator
    PLUG_CLS = RightShoulderEffectorPivotPlugOperator


class HeadEffectorPivotPlugOperator(
    CompoundPlugOperator["HeadEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HeadEffectorPivotX", "HeadEffectorPivotX"),
        ("HeadEffectorPivotY", "HeadEffectorPivotY"),
        ("HeadEffectorPivotZ", "HeadEffectorPivotZ"),
    )

    HeadEffectorPivotX = DoubleLinearField(default_value=0.0)

    HeadEffectorPivotY = DoubleLinearField(default_value=0.0)

    HeadEffectorPivotZ = DoubleLinearField(default_value=0.0)


class HeadEffectorPivotAttrOperator(
    CompoundAttrOperator[HeadEffectorPivotPlugOperator]
):
    __slots__ = ()

    HeadEffectorPivotX = DoubleLinearField(default_value=0.0)

    HeadEffectorPivotY = DoubleLinearField(default_value=0.0)

    HeadEffectorPivotZ = DoubleLinearField(default_value=0.0)


class HeadEffectorPivotField(
    CompoundField[HeadEffectorPivotAttrOperator, HeadEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HeadEffectorPivotAttrOperator
    PLUG_CLS = HeadEffectorPivotPlugOperator


class LeftHipEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftHipEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHipEffectorPivotX", "LeftHipEffectorPivotX"),
        ("LeftHipEffectorPivotY", "LeftHipEffectorPivotY"),
        ("LeftHipEffectorPivotZ", "LeftHipEffectorPivotZ"),
    )

    LeftHipEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHipEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHipEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHipEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHipEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHipEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHipEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHipEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHipEffectorPivotField(
    CompoundField[LeftHipEffectorPivotAttrOperator, LeftHipEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHipEffectorPivotAttrOperator
    PLUG_CLS = LeftHipEffectorPivotPlugOperator


class RightHipEffectorPivotPlugOperator(
    CompoundPlugOperator["RightHipEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHipEffectorPivotX", "RightHipEffectorPivotX"),
        ("RightHipEffectorPivotY", "RightHipEffectorPivotY"),
        ("RightHipEffectorPivotZ", "RightHipEffectorPivotZ"),
    )

    RightHipEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHipEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHipEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHipEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHipEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHipEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHipEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHipEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHipEffectorPivotField(
    CompoundField[RightHipEffectorPivotAttrOperator, RightHipEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHipEffectorPivotAttrOperator
    PLUG_CLS = RightHipEffectorPivotPlugOperator


class LeftHandEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftHandEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandEffectorPivotX", "LeftHandEffectorPivotX"),
        ("LeftHandEffectorPivotY", "LeftHandEffectorPivotY"),
        ("LeftHandEffectorPivotZ", "LeftHandEffectorPivotZ"),
    )

    LeftHandEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandEffectorPivotField(
    CompoundField[LeftHandEffectorPivotAttrOperator, LeftHandEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandEffectorPivotAttrOperator
    PLUG_CLS = LeftHandEffectorPivotPlugOperator


class RightHandEffectorPivotPlugOperator(
    CompoundPlugOperator["RightHandEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandEffectorPivotX", "RightHandEffectorPivotX"),
        ("RightHandEffectorPivotY", "RightHandEffectorPivotY"),
        ("RightHandEffectorPivotZ", "RightHandEffectorPivotZ"),
    )

    RightHandEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandEffectorPivotField(
    CompoundField[RightHandEffectorPivotAttrOperator, RightHandEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandEffectorPivotAttrOperator
    PLUG_CLS = RightHandEffectorPivotPlugOperator


class LeftHandThumbEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftHandThumbEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumbEffectorPivotX", "LeftHandThumbEffectorPivotX"),
        ("LeftHandThumbEffectorPivotY", "LeftHandThumbEffectorPivotY"),
        ("LeftHandThumbEffectorPivotZ", "LeftHandThumbEffectorPivotZ"),
    )

    LeftHandThumbEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandThumbEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandThumbEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandThumbEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandThumbEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandThumbEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandThumbEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandThumbEffectorPivotField(
    CompoundField[LeftHandThumbEffectorPivotAttrOperator, LeftHandThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumbEffectorPivotAttrOperator
    PLUG_CLS = LeftHandThumbEffectorPivotPlugOperator


class LeftHandIndexEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftHandIndexEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndexEffectorPivotX", "LeftHandIndexEffectorPivotX"),
        ("LeftHandIndexEffectorPivotY", "LeftHandIndexEffectorPivotY"),
        ("LeftHandIndexEffectorPivotZ", "LeftHandIndexEffectorPivotZ"),
    )

    LeftHandIndexEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandIndexEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandIndexEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandIndexEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandIndexEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandIndexEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandIndexEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandIndexEffectorPivotField(
    CompoundField[LeftHandIndexEffectorPivotAttrOperator, LeftHandIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndexEffectorPivotAttrOperator
    PLUG_CLS = LeftHandIndexEffectorPivotPlugOperator


class LeftHandMiddleEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftHandMiddleEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddleEffectorPivotX", "LeftHandMiddleEffectorPivotX"),
        ("LeftHandMiddleEffectorPivotY", "LeftHandMiddleEffectorPivotY"),
        ("LeftHandMiddleEffectorPivotZ", "LeftHandMiddleEffectorPivotZ"),
    )

    LeftHandMiddleEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandMiddleEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandMiddleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandMiddleEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandMiddleEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandMiddleEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandMiddleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandMiddleEffectorPivotField(
    CompoundField[LeftHandMiddleEffectorPivotAttrOperator, LeftHandMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddleEffectorPivotAttrOperator
    PLUG_CLS = LeftHandMiddleEffectorPivotPlugOperator


class LeftHandRingEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftHandRingEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRingEffectorPivotX", "LeftHandRingEffectorPivotX"),
        ("LeftHandRingEffectorPivotY", "LeftHandRingEffectorPivotY"),
        ("LeftHandRingEffectorPivotZ", "LeftHandRingEffectorPivotZ"),
    )

    LeftHandRingEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandRingEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandRingEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandRingEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandRingEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandRingEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandRingEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandRingEffectorPivotField(
    CompoundField[LeftHandRingEffectorPivotAttrOperator, LeftHandRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRingEffectorPivotAttrOperator
    PLUG_CLS = LeftHandRingEffectorPivotPlugOperator


class LeftHandPinkyEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftHandPinkyEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinkyEffectorPivotX", "LeftHandPinkyEffectorPivotX"),
        ("LeftHandPinkyEffectorPivotY", "LeftHandPinkyEffectorPivotY"),
        ("LeftHandPinkyEffectorPivotZ", "LeftHandPinkyEffectorPivotZ"),
    )

    LeftHandPinkyEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandPinkyEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandPinkyEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandPinkyEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandPinkyEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandPinkyEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandPinkyEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandPinkyEffectorPivotField(
    CompoundField[LeftHandPinkyEffectorPivotAttrOperator, LeftHandPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinkyEffectorPivotAttrOperator
    PLUG_CLS = LeftHandPinkyEffectorPivotPlugOperator


class LeftHandExtraFingerEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftHandExtraFingerEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFingerEffectorPivotX", "LeftHandExtraFingerEffectorPivotX"),
        ("LeftHandExtraFingerEffectorPivotY", "LeftHandExtraFingerEffectorPivotY"),
        ("LeftHandExtraFingerEffectorPivotZ", "LeftHandExtraFingerEffectorPivotZ"),
    )

    LeftHandExtraFingerEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandExtraFingerEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandExtraFingerEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandExtraFingerEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFingerEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftHandExtraFingerEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftHandExtraFingerEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftHandExtraFingerEffectorPivotField(
    CompoundField[LeftHandExtraFingerEffectorPivotAttrOperator, LeftHandExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFingerEffectorPivotAttrOperator
    PLUG_CLS = LeftHandExtraFingerEffectorPivotPlugOperator


class RightHandThumbEffectorPivotPlugOperator(
    CompoundPlugOperator["RightHandThumbEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumbEffectorPivotX", "RightHandThumbEffectorPivotX"),
        ("RightHandThumbEffectorPivotY", "RightHandThumbEffectorPivotY"),
        ("RightHandThumbEffectorPivotZ", "RightHandThumbEffectorPivotZ"),
    )

    RightHandThumbEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandThumbEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandThumbEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandThumbEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandThumbEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandThumbEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandThumbEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandThumbEffectorPivotField(
    CompoundField[RightHandThumbEffectorPivotAttrOperator, RightHandThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumbEffectorPivotAttrOperator
    PLUG_CLS = RightHandThumbEffectorPivotPlugOperator


class RightHandIndexEffectorPivotPlugOperator(
    CompoundPlugOperator["RightHandIndexEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndexEffectorPivotX", "RightHandIndexEffectorPivotX"),
        ("RightHandIndexEffectorPivotY", "RightHandIndexEffectorPivotY"),
        ("RightHandIndexEffectorPivotZ", "RightHandIndexEffectorPivotZ"),
    )

    RightHandIndexEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandIndexEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandIndexEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandIndexEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandIndexEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandIndexEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandIndexEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandIndexEffectorPivotField(
    CompoundField[RightHandIndexEffectorPivotAttrOperator, RightHandIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndexEffectorPivotAttrOperator
    PLUG_CLS = RightHandIndexEffectorPivotPlugOperator


class RightHandMiddleEffectorPivotPlugOperator(
    CompoundPlugOperator["RightHandMiddleEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddleEffectorPivotX", "RightHandMiddleEffectorPivotX"),
        ("RightHandMiddleEffectorPivotY", "RightHandMiddleEffectorPivotY"),
        ("RightHandMiddleEffectorPivotZ", "RightHandMiddleEffectorPivotZ"),
    )

    RightHandMiddleEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandMiddleEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandMiddleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandMiddleEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandMiddleEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandMiddleEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandMiddleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandMiddleEffectorPivotField(
    CompoundField[RightHandMiddleEffectorPivotAttrOperator, RightHandMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddleEffectorPivotAttrOperator
    PLUG_CLS = RightHandMiddleEffectorPivotPlugOperator


class RightHandRingEffectorPivotPlugOperator(
    CompoundPlugOperator["RightHandRingEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRingEffectorPivotX", "RightHandRingEffectorPivotX"),
        ("RightHandRingEffectorPivotY", "RightHandRingEffectorPivotY"),
        ("RightHandRingEffectorPivotZ", "RightHandRingEffectorPivotZ"),
    )

    RightHandRingEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandRingEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandRingEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandRingEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandRingEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandRingEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandRingEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandRingEffectorPivotField(
    CompoundField[RightHandRingEffectorPivotAttrOperator, RightHandRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRingEffectorPivotAttrOperator
    PLUG_CLS = RightHandRingEffectorPivotPlugOperator


class RightHandPinkyEffectorPivotPlugOperator(
    CompoundPlugOperator["RightHandPinkyEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinkyEffectorPivotX", "RightHandPinkyEffectorPivotX"),
        ("RightHandPinkyEffectorPivotY", "RightHandPinkyEffectorPivotY"),
        ("RightHandPinkyEffectorPivotZ", "RightHandPinkyEffectorPivotZ"),
    )

    RightHandPinkyEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandPinkyEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandPinkyEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandPinkyEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandPinkyEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandPinkyEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandPinkyEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandPinkyEffectorPivotField(
    CompoundField[RightHandPinkyEffectorPivotAttrOperator, RightHandPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinkyEffectorPivotAttrOperator
    PLUG_CLS = RightHandPinkyEffectorPivotPlugOperator


class RightHandExtraFingerEffectorPivotPlugOperator(
    CompoundPlugOperator["RightHandExtraFingerEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFingerEffectorPivotX", "RightHandExtraFingerEffectorPivotX"),
        ("RightHandExtraFingerEffectorPivotY", "RightHandExtraFingerEffectorPivotY"),
        ("RightHandExtraFingerEffectorPivotZ", "RightHandExtraFingerEffectorPivotZ"),
    )

    RightHandExtraFingerEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandExtraFingerEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandExtraFingerEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandExtraFingerEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandExtraFingerEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightHandExtraFingerEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightHandExtraFingerEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightHandExtraFingerEffectorPivotField(
    CompoundField[RightHandExtraFingerEffectorPivotAttrOperator, RightHandExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFingerEffectorPivotAttrOperator
    PLUG_CLS = RightHandExtraFingerEffectorPivotPlugOperator


class LeftFootThumbEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftFootThumbEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumbEffectorPivotX", "LeftFootThumbEffectorPivotX"),
        ("LeftFootThumbEffectorPivotY", "LeftFootThumbEffectorPivotY"),
        ("LeftFootThumbEffectorPivotZ", "LeftFootThumbEffectorPivotZ"),
    )

    LeftFootThumbEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootThumbEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootThumbEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootThumbEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootThumbEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootThumbEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootThumbEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootThumbEffectorPivotField(
    CompoundField[LeftFootThumbEffectorPivotAttrOperator, LeftFootThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumbEffectorPivotAttrOperator
    PLUG_CLS = LeftFootThumbEffectorPivotPlugOperator


class LeftFootIndexEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftFootIndexEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndexEffectorPivotX", "LeftFootIndexEffectorPivotX"),
        ("LeftFootIndexEffectorPivotY", "LeftFootIndexEffectorPivotY"),
        ("LeftFootIndexEffectorPivotZ", "LeftFootIndexEffectorPivotZ"),
    )

    LeftFootIndexEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootIndexEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootIndexEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootIndexEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootIndexEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootIndexEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootIndexEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootIndexEffectorPivotField(
    CompoundField[LeftFootIndexEffectorPivotAttrOperator, LeftFootIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndexEffectorPivotAttrOperator
    PLUG_CLS = LeftFootIndexEffectorPivotPlugOperator


class LeftFootMiddleEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftFootMiddleEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddleEffectorPivotX", "LeftFootMiddleEffectorPivotX"),
        ("LeftFootMiddleEffectorPivotY", "LeftFootMiddleEffectorPivotY"),
        ("LeftFootMiddleEffectorPivotZ", "LeftFootMiddleEffectorPivotZ"),
    )

    LeftFootMiddleEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootMiddleEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootMiddleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootMiddleEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootMiddleEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootMiddleEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootMiddleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootMiddleEffectorPivotField(
    CompoundField[LeftFootMiddleEffectorPivotAttrOperator, LeftFootMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddleEffectorPivotAttrOperator
    PLUG_CLS = LeftFootMiddleEffectorPivotPlugOperator


class LeftFootRingEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftFootRingEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRingEffectorPivotX", "LeftFootRingEffectorPivotX"),
        ("LeftFootRingEffectorPivotY", "LeftFootRingEffectorPivotY"),
        ("LeftFootRingEffectorPivotZ", "LeftFootRingEffectorPivotZ"),
    )

    LeftFootRingEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootRingEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootRingEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootRingEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootRingEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootRingEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootRingEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootRingEffectorPivotField(
    CompoundField[LeftFootRingEffectorPivotAttrOperator, LeftFootRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRingEffectorPivotAttrOperator
    PLUG_CLS = LeftFootRingEffectorPivotPlugOperator


class LeftFootPinkyEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftFootPinkyEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinkyEffectorPivotX", "LeftFootPinkyEffectorPivotX"),
        ("LeftFootPinkyEffectorPivotY", "LeftFootPinkyEffectorPivotY"),
        ("LeftFootPinkyEffectorPivotZ", "LeftFootPinkyEffectorPivotZ"),
    )

    LeftFootPinkyEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootPinkyEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootPinkyEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootPinkyEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootPinkyEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootPinkyEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootPinkyEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootPinkyEffectorPivotField(
    CompoundField[LeftFootPinkyEffectorPivotAttrOperator, LeftFootPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinkyEffectorPivotAttrOperator
    PLUG_CLS = LeftFootPinkyEffectorPivotPlugOperator


class LeftFootExtraFingerEffectorPivotPlugOperator(
    CompoundPlugOperator["LeftFootExtraFingerEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFingerEffectorPivotX", "LeftFootExtraFingerEffectorPivotX"),
        ("LeftFootExtraFingerEffectorPivotY", "LeftFootExtraFingerEffectorPivotY"),
        ("LeftFootExtraFingerEffectorPivotZ", "LeftFootExtraFingerEffectorPivotZ"),
    )

    LeftFootExtraFingerEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootExtraFingerEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootExtraFingerEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootExtraFingerEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFingerEffectorPivotX = DoubleLinearField(default_value=0.0)

    LeftFootExtraFingerEffectorPivotY = DoubleLinearField(default_value=0.0)

    LeftFootExtraFingerEffectorPivotZ = DoubleLinearField(default_value=0.0)


class LeftFootExtraFingerEffectorPivotField(
    CompoundField[LeftFootExtraFingerEffectorPivotAttrOperator, LeftFootExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFingerEffectorPivotAttrOperator
    PLUG_CLS = LeftFootExtraFingerEffectorPivotPlugOperator


class RightFootThumbEffectorPivotPlugOperator(
    CompoundPlugOperator["RightFootThumbEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumbEffectorPivotX", "RightFootThumbEffectorPivotX"),
        ("RightFootThumbEffectorPivotY", "RightFootThumbEffectorPivotY"),
        ("RightFootThumbEffectorPivotZ", "RightFootThumbEffectorPivotZ"),
    )

    RightFootThumbEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootThumbEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootThumbEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootThumbEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootThumbEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootThumbEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootThumbEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootThumbEffectorPivotField(
    CompoundField[RightFootThumbEffectorPivotAttrOperator, RightFootThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumbEffectorPivotAttrOperator
    PLUG_CLS = RightFootThumbEffectorPivotPlugOperator


class RightFootIndexEffectorPivotPlugOperator(
    CompoundPlugOperator["RightFootIndexEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndexEffectorPivotX", "RightFootIndexEffectorPivotX"),
        ("RightFootIndexEffectorPivotY", "RightFootIndexEffectorPivotY"),
        ("RightFootIndexEffectorPivotZ", "RightFootIndexEffectorPivotZ"),
    )

    RightFootIndexEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootIndexEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootIndexEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootIndexEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootIndexEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootIndexEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootIndexEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootIndexEffectorPivotField(
    CompoundField[RightFootIndexEffectorPivotAttrOperator, RightFootIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndexEffectorPivotAttrOperator
    PLUG_CLS = RightFootIndexEffectorPivotPlugOperator


class RightFootMiddleEffectorPivotPlugOperator(
    CompoundPlugOperator["RightFootMiddleEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddleEffectorPivotX", "RightFootMiddleEffectorPivotX"),
        ("RightFootMiddleEffectorPivotY", "RightFootMiddleEffectorPivotY"),
        ("RightFootMiddleEffectorPivotZ", "RightFootMiddleEffectorPivotZ"),
    )

    RightFootMiddleEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootMiddleEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootMiddleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootMiddleEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootMiddleEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootMiddleEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootMiddleEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootMiddleEffectorPivotField(
    CompoundField[RightFootMiddleEffectorPivotAttrOperator, RightFootMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddleEffectorPivotAttrOperator
    PLUG_CLS = RightFootMiddleEffectorPivotPlugOperator


class RightFootRingEffectorPivotPlugOperator(
    CompoundPlugOperator["RightFootRingEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRingEffectorPivotX", "RightFootRingEffectorPivotX"),
        ("RightFootRingEffectorPivotY", "RightFootRingEffectorPivotY"),
        ("RightFootRingEffectorPivotZ", "RightFootRingEffectorPivotZ"),
    )

    RightFootRingEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootRingEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootRingEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootRingEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootRingEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootRingEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootRingEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootRingEffectorPivotField(
    CompoundField[RightFootRingEffectorPivotAttrOperator, RightFootRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRingEffectorPivotAttrOperator
    PLUG_CLS = RightFootRingEffectorPivotPlugOperator


class RightFootPinkyEffectorPivotPlugOperator(
    CompoundPlugOperator["RightFootPinkyEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinkyEffectorPivotX", "RightFootPinkyEffectorPivotX"),
        ("RightFootPinkyEffectorPivotY", "RightFootPinkyEffectorPivotY"),
        ("RightFootPinkyEffectorPivotZ", "RightFootPinkyEffectorPivotZ"),
    )

    RightFootPinkyEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootPinkyEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootPinkyEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootPinkyEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootPinkyEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootPinkyEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootPinkyEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootPinkyEffectorPivotField(
    CompoundField[RightFootPinkyEffectorPivotAttrOperator, RightFootPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinkyEffectorPivotAttrOperator
    PLUG_CLS = RightFootPinkyEffectorPivotPlugOperator


class RightFootExtraFingerEffectorPivotPlugOperator(
    CompoundPlugOperator["RightFootExtraFingerEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFingerEffectorPivotX", "RightFootExtraFingerEffectorPivotX"),
        ("RightFootExtraFingerEffectorPivotY", "RightFootExtraFingerEffectorPivotY"),
        ("RightFootExtraFingerEffectorPivotZ", "RightFootExtraFingerEffectorPivotZ"),
    )

    RightFootExtraFingerEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootExtraFingerEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootExtraFingerEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootExtraFingerEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootExtraFingerEffectorPivotX = DoubleLinearField(default_value=0.0)

    RightFootExtraFingerEffectorPivotY = DoubleLinearField(default_value=0.0)

    RightFootExtraFingerEffectorPivotZ = DoubleLinearField(default_value=0.0)


class RightFootExtraFingerEffectorPivotField(
    CompoundField[RightFootExtraFingerEffectorPivotAttrOperator, RightFootExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFingerEffectorPivotAttrOperator
    PLUG_CLS = RightFootExtraFingerEffectorPivotPlugOperator
