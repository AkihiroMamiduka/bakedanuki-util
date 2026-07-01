# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField


class HipsEffectorPivotPlugOperator(
    CompoundPlugOperator["HipsEffectorPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HipsEffectorPivotX", "HipsEffectorPivotX"),
        ("HipsEffectorPivotY", "HipsEffectorPivotY"),
        ("HipsEffectorPivotZ", "HipsEffectorPivotZ"),
    )

    HipsEffectorPivotX = DoubleLinearField()

    HipsEffectorPivotY = DoubleLinearField()

    HipsEffectorPivotZ = DoubleLinearField()


class HipsEffectorPivotAttrOperator(
    CompoundAttrOperator[HipsEffectorPivotPlugOperator]
):
    __slots__ = ()

    HipsEffectorPivotX = DoubleLinearField()

    HipsEffectorPivotY = DoubleLinearField()

    HipsEffectorPivotZ = DoubleLinearField()


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

    LeftAnkleEffectorPivotX = DoubleLinearField()

    LeftAnkleEffectorPivotY = DoubleLinearField()

    LeftAnkleEffectorPivotZ = DoubleLinearField()


class LeftAnkleEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftAnkleEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftAnkleEffectorPivotX = DoubleLinearField()

    LeftAnkleEffectorPivotY = DoubleLinearField()

    LeftAnkleEffectorPivotZ = DoubleLinearField()


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

    RightAnkleEffectorPivotX = DoubleLinearField()

    RightAnkleEffectorPivotY = DoubleLinearField()

    RightAnkleEffectorPivotZ = DoubleLinearField()


class RightAnkleEffectorPivotAttrOperator(
    CompoundAttrOperator[RightAnkleEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightAnkleEffectorPivotX = DoubleLinearField()

    RightAnkleEffectorPivotY = DoubleLinearField()

    RightAnkleEffectorPivotZ = DoubleLinearField()


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

    LeftWristEffectorPivotX = DoubleLinearField()

    LeftWristEffectorPivotY = DoubleLinearField()

    LeftWristEffectorPivotZ = DoubleLinearField()


class LeftWristEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftWristEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftWristEffectorPivotX = DoubleLinearField()

    LeftWristEffectorPivotY = DoubleLinearField()

    LeftWristEffectorPivotZ = DoubleLinearField()


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

    RightWristEffectorPivotX = DoubleLinearField()

    RightWristEffectorPivotY = DoubleLinearField()

    RightWristEffectorPivotZ = DoubleLinearField()


class RightWristEffectorPivotAttrOperator(
    CompoundAttrOperator[RightWristEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightWristEffectorPivotX = DoubleLinearField()

    RightWristEffectorPivotY = DoubleLinearField()

    RightWristEffectorPivotZ = DoubleLinearField()


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

    LeftKneeEffectorPivotX = DoubleLinearField()

    LeftKneeEffectorPivotY = DoubleLinearField()

    LeftKneeEffectorPivotZ = DoubleLinearField()


class LeftKneeEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftKneeEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftKneeEffectorPivotX = DoubleLinearField()

    LeftKneeEffectorPivotY = DoubleLinearField()

    LeftKneeEffectorPivotZ = DoubleLinearField()


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

    RightKneeEffectorPivotX = DoubleLinearField()

    RightKneeEffectorPivotY = DoubleLinearField()

    RightKneeEffectorPivotZ = DoubleLinearField()


class RightKneeEffectorPivotAttrOperator(
    CompoundAttrOperator[RightKneeEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightKneeEffectorPivotX = DoubleLinearField()

    RightKneeEffectorPivotY = DoubleLinearField()

    RightKneeEffectorPivotZ = DoubleLinearField()


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

    LeftElbowEffectorPivotX = DoubleLinearField()

    LeftElbowEffectorPivotY = DoubleLinearField()

    LeftElbowEffectorPivotZ = DoubleLinearField()


class LeftElbowEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftElbowEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftElbowEffectorPivotX = DoubleLinearField()

    LeftElbowEffectorPivotY = DoubleLinearField()

    LeftElbowEffectorPivotZ = DoubleLinearField()


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

    RightElbowEffectorPivotX = DoubleLinearField()

    RightElbowEffectorPivotY = DoubleLinearField()

    RightElbowEffectorPivotZ = DoubleLinearField()


class RightElbowEffectorPivotAttrOperator(
    CompoundAttrOperator[RightElbowEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightElbowEffectorPivotX = DoubleLinearField()

    RightElbowEffectorPivotY = DoubleLinearField()

    RightElbowEffectorPivotZ = DoubleLinearField()


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

    ChestOriginEffectorPivotX = DoubleLinearField()

    ChestOriginEffectorPivotY = DoubleLinearField()

    ChestOriginEffectorPivotZ = DoubleLinearField()


class ChestOriginEffectorPivotAttrOperator(
    CompoundAttrOperator[ChestOriginEffectorPivotPlugOperator]
):
    __slots__ = ()

    ChestOriginEffectorPivotX = DoubleLinearField()

    ChestOriginEffectorPivotY = DoubleLinearField()

    ChestOriginEffectorPivotZ = DoubleLinearField()


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

    ChestEndEffectorPivotX = DoubleLinearField()

    ChestEndEffectorPivotY = DoubleLinearField()

    ChestEndEffectorPivotZ = DoubleLinearField()


class ChestEndEffectorPivotAttrOperator(
    CompoundAttrOperator[ChestEndEffectorPivotPlugOperator]
):
    __slots__ = ()

    ChestEndEffectorPivotX = DoubleLinearField()

    ChestEndEffectorPivotY = DoubleLinearField()

    ChestEndEffectorPivotZ = DoubleLinearField()


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

    LeftFootEffectorPivotX = DoubleLinearField()

    LeftFootEffectorPivotY = DoubleLinearField()

    LeftFootEffectorPivotZ = DoubleLinearField()


class LeftFootEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootEffectorPivotX = DoubleLinearField()

    LeftFootEffectorPivotY = DoubleLinearField()

    LeftFootEffectorPivotZ = DoubleLinearField()


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

    RightFootEffectorPivotX = DoubleLinearField()

    RightFootEffectorPivotY = DoubleLinearField()

    RightFootEffectorPivotZ = DoubleLinearField()


class RightFootEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootEffectorPivotX = DoubleLinearField()

    RightFootEffectorPivotY = DoubleLinearField()

    RightFootEffectorPivotZ = DoubleLinearField()


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

    LeftShoulderEffectorPivotX = DoubleLinearField()

    LeftShoulderEffectorPivotY = DoubleLinearField()

    LeftShoulderEffectorPivotZ = DoubleLinearField()


class LeftShoulderEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftShoulderEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftShoulderEffectorPivotX = DoubleLinearField()

    LeftShoulderEffectorPivotY = DoubleLinearField()

    LeftShoulderEffectorPivotZ = DoubleLinearField()


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

    RightShoulderEffectorPivotX = DoubleLinearField()

    RightShoulderEffectorPivotY = DoubleLinearField()

    RightShoulderEffectorPivotZ = DoubleLinearField()


class RightShoulderEffectorPivotAttrOperator(
    CompoundAttrOperator[RightShoulderEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightShoulderEffectorPivotX = DoubleLinearField()

    RightShoulderEffectorPivotY = DoubleLinearField()

    RightShoulderEffectorPivotZ = DoubleLinearField()


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

    HeadEffectorPivotX = DoubleLinearField()

    HeadEffectorPivotY = DoubleLinearField()

    HeadEffectorPivotZ = DoubleLinearField()


class HeadEffectorPivotAttrOperator(
    CompoundAttrOperator[HeadEffectorPivotPlugOperator]
):
    __slots__ = ()

    HeadEffectorPivotX = DoubleLinearField()

    HeadEffectorPivotY = DoubleLinearField()

    HeadEffectorPivotZ = DoubleLinearField()


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

    LeftHipEffectorPivotX = DoubleLinearField()

    LeftHipEffectorPivotY = DoubleLinearField()

    LeftHipEffectorPivotZ = DoubleLinearField()


class LeftHipEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHipEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHipEffectorPivotX = DoubleLinearField()

    LeftHipEffectorPivotY = DoubleLinearField()

    LeftHipEffectorPivotZ = DoubleLinearField()


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

    RightHipEffectorPivotX = DoubleLinearField()

    RightHipEffectorPivotY = DoubleLinearField()

    RightHipEffectorPivotZ = DoubleLinearField()


class RightHipEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHipEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHipEffectorPivotX = DoubleLinearField()

    RightHipEffectorPivotY = DoubleLinearField()

    RightHipEffectorPivotZ = DoubleLinearField()


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

    LeftHandEffectorPivotX = DoubleLinearField()

    LeftHandEffectorPivotY = DoubleLinearField()

    LeftHandEffectorPivotZ = DoubleLinearField()


class LeftHandEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandEffectorPivotX = DoubleLinearField()

    LeftHandEffectorPivotY = DoubleLinearField()

    LeftHandEffectorPivotZ = DoubleLinearField()


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

    RightHandEffectorPivotX = DoubleLinearField()

    RightHandEffectorPivotY = DoubleLinearField()

    RightHandEffectorPivotZ = DoubleLinearField()


class RightHandEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandEffectorPivotX = DoubleLinearField()

    RightHandEffectorPivotY = DoubleLinearField()

    RightHandEffectorPivotZ = DoubleLinearField()


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

    LeftHandThumbEffectorPivotX = DoubleLinearField()

    LeftHandThumbEffectorPivotY = DoubleLinearField()

    LeftHandThumbEffectorPivotZ = DoubleLinearField()


class LeftHandThumbEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandThumbEffectorPivotX = DoubleLinearField()

    LeftHandThumbEffectorPivotY = DoubleLinearField()

    LeftHandThumbEffectorPivotZ = DoubleLinearField()


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

    LeftHandIndexEffectorPivotX = DoubleLinearField()

    LeftHandIndexEffectorPivotY = DoubleLinearField()

    LeftHandIndexEffectorPivotZ = DoubleLinearField()


class LeftHandIndexEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandIndexEffectorPivotX = DoubleLinearField()

    LeftHandIndexEffectorPivotY = DoubleLinearField()

    LeftHandIndexEffectorPivotZ = DoubleLinearField()


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

    LeftHandMiddleEffectorPivotX = DoubleLinearField()

    LeftHandMiddleEffectorPivotY = DoubleLinearField()

    LeftHandMiddleEffectorPivotZ = DoubleLinearField()


class LeftHandMiddleEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandMiddleEffectorPivotX = DoubleLinearField()

    LeftHandMiddleEffectorPivotY = DoubleLinearField()

    LeftHandMiddleEffectorPivotZ = DoubleLinearField()


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

    LeftHandRingEffectorPivotX = DoubleLinearField()

    LeftHandRingEffectorPivotY = DoubleLinearField()

    LeftHandRingEffectorPivotZ = DoubleLinearField()


class LeftHandRingEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandRingEffectorPivotX = DoubleLinearField()

    LeftHandRingEffectorPivotY = DoubleLinearField()

    LeftHandRingEffectorPivotZ = DoubleLinearField()


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

    LeftHandPinkyEffectorPivotX = DoubleLinearField()

    LeftHandPinkyEffectorPivotY = DoubleLinearField()

    LeftHandPinkyEffectorPivotZ = DoubleLinearField()


class LeftHandPinkyEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandPinkyEffectorPivotX = DoubleLinearField()

    LeftHandPinkyEffectorPivotY = DoubleLinearField()

    LeftHandPinkyEffectorPivotZ = DoubleLinearField()


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

    LeftHandExtraFingerEffectorPivotX = DoubleLinearField()

    LeftHandExtraFingerEffectorPivotY = DoubleLinearField()

    LeftHandExtraFingerEffectorPivotZ = DoubleLinearField()


class LeftHandExtraFingerEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftHandExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFingerEffectorPivotX = DoubleLinearField()

    LeftHandExtraFingerEffectorPivotY = DoubleLinearField()

    LeftHandExtraFingerEffectorPivotZ = DoubleLinearField()


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

    RightHandThumbEffectorPivotX = DoubleLinearField()

    RightHandThumbEffectorPivotY = DoubleLinearField()

    RightHandThumbEffectorPivotZ = DoubleLinearField()


class RightHandThumbEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandThumbEffectorPivotX = DoubleLinearField()

    RightHandThumbEffectorPivotY = DoubleLinearField()

    RightHandThumbEffectorPivotZ = DoubleLinearField()


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

    RightHandIndexEffectorPivotX = DoubleLinearField()

    RightHandIndexEffectorPivotY = DoubleLinearField()

    RightHandIndexEffectorPivotZ = DoubleLinearField()


class RightHandIndexEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandIndexEffectorPivotX = DoubleLinearField()

    RightHandIndexEffectorPivotY = DoubleLinearField()

    RightHandIndexEffectorPivotZ = DoubleLinearField()


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

    RightHandMiddleEffectorPivotX = DoubleLinearField()

    RightHandMiddleEffectorPivotY = DoubleLinearField()

    RightHandMiddleEffectorPivotZ = DoubleLinearField()


class RightHandMiddleEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandMiddleEffectorPivotX = DoubleLinearField()

    RightHandMiddleEffectorPivotY = DoubleLinearField()

    RightHandMiddleEffectorPivotZ = DoubleLinearField()


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

    RightHandRingEffectorPivotX = DoubleLinearField()

    RightHandRingEffectorPivotY = DoubleLinearField()

    RightHandRingEffectorPivotZ = DoubleLinearField()


class RightHandRingEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandRingEffectorPivotX = DoubleLinearField()

    RightHandRingEffectorPivotY = DoubleLinearField()

    RightHandRingEffectorPivotZ = DoubleLinearField()


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

    RightHandPinkyEffectorPivotX = DoubleLinearField()

    RightHandPinkyEffectorPivotY = DoubleLinearField()

    RightHandPinkyEffectorPivotZ = DoubleLinearField()


class RightHandPinkyEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandPinkyEffectorPivotX = DoubleLinearField()

    RightHandPinkyEffectorPivotY = DoubleLinearField()

    RightHandPinkyEffectorPivotZ = DoubleLinearField()


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

    RightHandExtraFingerEffectorPivotX = DoubleLinearField()

    RightHandExtraFingerEffectorPivotY = DoubleLinearField()

    RightHandExtraFingerEffectorPivotZ = DoubleLinearField()


class RightHandExtraFingerEffectorPivotAttrOperator(
    CompoundAttrOperator[RightHandExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightHandExtraFingerEffectorPivotX = DoubleLinearField()

    RightHandExtraFingerEffectorPivotY = DoubleLinearField()

    RightHandExtraFingerEffectorPivotZ = DoubleLinearField()


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

    LeftFootThumbEffectorPivotX = DoubleLinearField()

    LeftFootThumbEffectorPivotY = DoubleLinearField()

    LeftFootThumbEffectorPivotZ = DoubleLinearField()


class LeftFootThumbEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootThumbEffectorPivotX = DoubleLinearField()

    LeftFootThumbEffectorPivotY = DoubleLinearField()

    LeftFootThumbEffectorPivotZ = DoubleLinearField()


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

    LeftFootIndexEffectorPivotX = DoubleLinearField()

    LeftFootIndexEffectorPivotY = DoubleLinearField()

    LeftFootIndexEffectorPivotZ = DoubleLinearField()


class LeftFootIndexEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootIndexEffectorPivotX = DoubleLinearField()

    LeftFootIndexEffectorPivotY = DoubleLinearField()

    LeftFootIndexEffectorPivotZ = DoubleLinearField()


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

    LeftFootMiddleEffectorPivotX = DoubleLinearField()

    LeftFootMiddleEffectorPivotY = DoubleLinearField()

    LeftFootMiddleEffectorPivotZ = DoubleLinearField()


class LeftFootMiddleEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootMiddleEffectorPivotX = DoubleLinearField()

    LeftFootMiddleEffectorPivotY = DoubleLinearField()

    LeftFootMiddleEffectorPivotZ = DoubleLinearField()


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

    LeftFootRingEffectorPivotX = DoubleLinearField()

    LeftFootRingEffectorPivotY = DoubleLinearField()

    LeftFootRingEffectorPivotZ = DoubleLinearField()


class LeftFootRingEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootRingEffectorPivotX = DoubleLinearField()

    LeftFootRingEffectorPivotY = DoubleLinearField()

    LeftFootRingEffectorPivotZ = DoubleLinearField()


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

    LeftFootPinkyEffectorPivotX = DoubleLinearField()

    LeftFootPinkyEffectorPivotY = DoubleLinearField()

    LeftFootPinkyEffectorPivotZ = DoubleLinearField()


class LeftFootPinkyEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootPinkyEffectorPivotX = DoubleLinearField()

    LeftFootPinkyEffectorPivotY = DoubleLinearField()

    LeftFootPinkyEffectorPivotZ = DoubleLinearField()


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

    LeftFootExtraFingerEffectorPivotX = DoubleLinearField()

    LeftFootExtraFingerEffectorPivotY = DoubleLinearField()

    LeftFootExtraFingerEffectorPivotZ = DoubleLinearField()


class LeftFootExtraFingerEffectorPivotAttrOperator(
    CompoundAttrOperator[LeftFootExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFingerEffectorPivotX = DoubleLinearField()

    LeftFootExtraFingerEffectorPivotY = DoubleLinearField()

    LeftFootExtraFingerEffectorPivotZ = DoubleLinearField()


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

    RightFootThumbEffectorPivotX = DoubleLinearField()

    RightFootThumbEffectorPivotY = DoubleLinearField()

    RightFootThumbEffectorPivotZ = DoubleLinearField()


class RightFootThumbEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootThumbEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootThumbEffectorPivotX = DoubleLinearField()

    RightFootThumbEffectorPivotY = DoubleLinearField()

    RightFootThumbEffectorPivotZ = DoubleLinearField()


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

    RightFootIndexEffectorPivotX = DoubleLinearField()

    RightFootIndexEffectorPivotY = DoubleLinearField()

    RightFootIndexEffectorPivotZ = DoubleLinearField()


class RightFootIndexEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootIndexEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootIndexEffectorPivotX = DoubleLinearField()

    RightFootIndexEffectorPivotY = DoubleLinearField()

    RightFootIndexEffectorPivotZ = DoubleLinearField()


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

    RightFootMiddleEffectorPivotX = DoubleLinearField()

    RightFootMiddleEffectorPivotY = DoubleLinearField()

    RightFootMiddleEffectorPivotZ = DoubleLinearField()


class RightFootMiddleEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootMiddleEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootMiddleEffectorPivotX = DoubleLinearField()

    RightFootMiddleEffectorPivotY = DoubleLinearField()

    RightFootMiddleEffectorPivotZ = DoubleLinearField()


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

    RightFootRingEffectorPivotX = DoubleLinearField()

    RightFootRingEffectorPivotY = DoubleLinearField()

    RightFootRingEffectorPivotZ = DoubleLinearField()


class RightFootRingEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootRingEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootRingEffectorPivotX = DoubleLinearField()

    RightFootRingEffectorPivotY = DoubleLinearField()

    RightFootRingEffectorPivotZ = DoubleLinearField()


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

    RightFootPinkyEffectorPivotX = DoubleLinearField()

    RightFootPinkyEffectorPivotY = DoubleLinearField()

    RightFootPinkyEffectorPivotZ = DoubleLinearField()


class RightFootPinkyEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootPinkyEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootPinkyEffectorPivotX = DoubleLinearField()

    RightFootPinkyEffectorPivotY = DoubleLinearField()

    RightFootPinkyEffectorPivotZ = DoubleLinearField()


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

    RightFootExtraFingerEffectorPivotX = DoubleLinearField()

    RightFootExtraFingerEffectorPivotY = DoubleLinearField()

    RightFootExtraFingerEffectorPivotZ = DoubleLinearField()


class RightFootExtraFingerEffectorPivotAttrOperator(
    CompoundAttrOperator[RightFootExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    RightFootExtraFingerEffectorPivotX = DoubleLinearField()

    RightFootExtraFingerEffectorPivotY = DoubleLinearField()

    RightFootExtraFingerEffectorPivotZ = DoubleLinearField()


class RightFootExtraFingerEffectorPivotField(
    CompoundField[RightFootExtraFingerEffectorPivotAttrOperator, RightFootExtraFingerEffectorPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFingerEffectorPivotAttrOperator
    PLUG_CLS = RightFootExtraFingerEffectorPivotPlugOperator
