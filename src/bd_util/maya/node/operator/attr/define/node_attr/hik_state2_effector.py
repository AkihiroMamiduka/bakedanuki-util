# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField


class HipsEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["HipsEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HipsEffectorpivotOffsetX", "HipsEffectorpivotOffsetX"),
        ("HipsEffectorpivotOffsetY", "HipsEffectorpivotOffsetY"),
        ("HipsEffectorpivotOffsetZ", "HipsEffectorpivotOffsetZ"),
    )

    HipsEffectorpivotOffsetX = DoubleLinearField()

    HipsEffectorpivotOffsetY = DoubleLinearField()

    HipsEffectorpivotOffsetZ = DoubleLinearField()


class HipsEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[HipsEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    HipsEffectorpivotOffsetX = DoubleLinearField()

    HipsEffectorpivotOffsetY = DoubleLinearField()

    HipsEffectorpivotOffsetZ = DoubleLinearField()


class HipsEffectorpivotOffsetField(
    CompoundField[HipsEffectorpivotOffsetAttrOperator, HipsEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsEffectorpivotOffsetAttrOperator
    PLUG_CLS = HipsEffectorpivotOffsetPlugOperator


class LeftAnkleEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftAnkleEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftAnkleEffectorpivotOffsetX", "LeftAnkleEffectorpivotOffsetX"),
        ("LeftAnkleEffectorpivotOffsetY", "LeftAnkleEffectorpivotOffsetY"),
        ("LeftAnkleEffectorpivotOffsetZ", "LeftAnkleEffectorpivotOffsetZ"),
    )

    LeftAnkleEffectorpivotOffsetX = DoubleLinearField()

    LeftAnkleEffectorpivotOffsetY = DoubleLinearField()

    LeftAnkleEffectorpivotOffsetZ = DoubleLinearField()


class LeftAnkleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftAnkleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftAnkleEffectorpivotOffsetX = DoubleLinearField()

    LeftAnkleEffectorpivotOffsetY = DoubleLinearField()

    LeftAnkleEffectorpivotOffsetZ = DoubleLinearField()


class LeftAnkleEffectorpivotOffsetField(
    CompoundField[LeftAnkleEffectorpivotOffsetAttrOperator, LeftAnkleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftAnkleEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftAnkleEffectorpivotOffsetPlugOperator


class RightAnkleEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightAnkleEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightAnkleEffectorpivotOffsetX", "RightAnkleEffectorpivotOffsetX"),
        ("RightAnkleEffectorpivotOffsetY", "RightAnkleEffectorpivotOffsetY"),
        ("RightAnkleEffectorpivotOffsetZ", "RightAnkleEffectorpivotOffsetZ"),
    )

    RightAnkleEffectorpivotOffsetX = DoubleLinearField()

    RightAnkleEffectorpivotOffsetY = DoubleLinearField()

    RightAnkleEffectorpivotOffsetZ = DoubleLinearField()


class RightAnkleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightAnkleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightAnkleEffectorpivotOffsetX = DoubleLinearField()

    RightAnkleEffectorpivotOffsetY = DoubleLinearField()

    RightAnkleEffectorpivotOffsetZ = DoubleLinearField()


class RightAnkleEffectorpivotOffsetField(
    CompoundField[RightAnkleEffectorpivotOffsetAttrOperator, RightAnkleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightAnkleEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightAnkleEffectorpivotOffsetPlugOperator


class LeftWristEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftWristEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftWristEffectorpivotOffsetX", "LeftWristEffectorpivotOffsetX"),
        ("LeftWristEffectorpivotOffsetY", "LeftWristEffectorpivotOffsetY"),
        ("LeftWristEffectorpivotOffsetZ", "LeftWristEffectorpivotOffsetZ"),
    )

    LeftWristEffectorpivotOffsetX = DoubleLinearField()

    LeftWristEffectorpivotOffsetY = DoubleLinearField()

    LeftWristEffectorpivotOffsetZ = DoubleLinearField()


class LeftWristEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftWristEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftWristEffectorpivotOffsetX = DoubleLinearField()

    LeftWristEffectorpivotOffsetY = DoubleLinearField()

    LeftWristEffectorpivotOffsetZ = DoubleLinearField()


class LeftWristEffectorpivotOffsetField(
    CompoundField[LeftWristEffectorpivotOffsetAttrOperator, LeftWristEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftWristEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftWristEffectorpivotOffsetPlugOperator


class RightWristEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightWristEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightWristEffectorpivotOffsetX", "RightWristEffectorpivotOffsetX"),
        ("RightWristEffectorpivotOffsetY", "RightWristEffectorpivotOffsetY"),
        ("RightWristEffectorpivotOffsetZ", "RightWristEffectorpivotOffsetZ"),
    )

    RightWristEffectorpivotOffsetX = DoubleLinearField()

    RightWristEffectorpivotOffsetY = DoubleLinearField()

    RightWristEffectorpivotOffsetZ = DoubleLinearField()


class RightWristEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightWristEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightWristEffectorpivotOffsetX = DoubleLinearField()

    RightWristEffectorpivotOffsetY = DoubleLinearField()

    RightWristEffectorpivotOffsetZ = DoubleLinearField()


class RightWristEffectorpivotOffsetField(
    CompoundField[RightWristEffectorpivotOffsetAttrOperator, RightWristEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightWristEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightWristEffectorpivotOffsetPlugOperator


class LeftKneeEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftKneeEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftKneeEffectorpivotOffsetX", "LeftKneeEffectorpivotOffsetX"),
        ("LeftKneeEffectorpivotOffsetY", "LeftKneeEffectorpivotOffsetY"),
        ("LeftKneeEffectorpivotOffsetZ", "LeftKneeEffectorpivotOffsetZ"),
    )

    LeftKneeEffectorpivotOffsetX = DoubleLinearField()

    LeftKneeEffectorpivotOffsetY = DoubleLinearField()

    LeftKneeEffectorpivotOffsetZ = DoubleLinearField()


class LeftKneeEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftKneeEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftKneeEffectorpivotOffsetX = DoubleLinearField()

    LeftKneeEffectorpivotOffsetY = DoubleLinearField()

    LeftKneeEffectorpivotOffsetZ = DoubleLinearField()


class LeftKneeEffectorpivotOffsetField(
    CompoundField[LeftKneeEffectorpivotOffsetAttrOperator, LeftKneeEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftKneeEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftKneeEffectorpivotOffsetPlugOperator


class RightKneeEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightKneeEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightKneeEffectorpivotOffsetX", "RightKneeEffectorpivotOffsetX"),
        ("RightKneeEffectorpivotOffsetY", "RightKneeEffectorpivotOffsetY"),
        ("RightKneeEffectorpivotOffsetZ", "RightKneeEffectorpivotOffsetZ"),
    )

    RightKneeEffectorpivotOffsetX = DoubleLinearField()

    RightKneeEffectorpivotOffsetY = DoubleLinearField()

    RightKneeEffectorpivotOffsetZ = DoubleLinearField()


class RightKneeEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightKneeEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightKneeEffectorpivotOffsetX = DoubleLinearField()

    RightKneeEffectorpivotOffsetY = DoubleLinearField()

    RightKneeEffectorpivotOffsetZ = DoubleLinearField()


class RightKneeEffectorpivotOffsetField(
    CompoundField[RightKneeEffectorpivotOffsetAttrOperator, RightKneeEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightKneeEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightKneeEffectorpivotOffsetPlugOperator


class LeftElbowEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftElbowEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftElbowEffectorpivotOffsetX", "LeftElbowEffectorpivotOffsetX"),
        ("LeftElbowEffectorpivotOffsetY", "LeftElbowEffectorpivotOffsetY"),
        ("LeftElbowEffectorpivotOffsetZ", "LeftElbowEffectorpivotOffsetZ"),
    )

    LeftElbowEffectorpivotOffsetX = DoubleLinearField()

    LeftElbowEffectorpivotOffsetY = DoubleLinearField()

    LeftElbowEffectorpivotOffsetZ = DoubleLinearField()


class LeftElbowEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftElbowEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftElbowEffectorpivotOffsetX = DoubleLinearField()

    LeftElbowEffectorpivotOffsetY = DoubleLinearField()

    LeftElbowEffectorpivotOffsetZ = DoubleLinearField()


class LeftElbowEffectorpivotOffsetField(
    CompoundField[LeftElbowEffectorpivotOffsetAttrOperator, LeftElbowEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftElbowEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftElbowEffectorpivotOffsetPlugOperator


class RightElbowEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightElbowEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightElbowEffectorpivotOffsetX", "RightElbowEffectorpivotOffsetX"),
        ("RightElbowEffectorpivotOffsetY", "RightElbowEffectorpivotOffsetY"),
        ("RightElbowEffectorpivotOffsetZ", "RightElbowEffectorpivotOffsetZ"),
    )

    RightElbowEffectorpivotOffsetX = DoubleLinearField()

    RightElbowEffectorpivotOffsetY = DoubleLinearField()

    RightElbowEffectorpivotOffsetZ = DoubleLinearField()


class RightElbowEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightElbowEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightElbowEffectorpivotOffsetX = DoubleLinearField()

    RightElbowEffectorpivotOffsetY = DoubleLinearField()

    RightElbowEffectorpivotOffsetZ = DoubleLinearField()


class RightElbowEffectorpivotOffsetField(
    CompoundField[RightElbowEffectorpivotOffsetAttrOperator, RightElbowEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightElbowEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightElbowEffectorpivotOffsetPlugOperator


class ChestOriginEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["ChestOriginEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ChestOriginEffectorpivotOffsetX", "ChestOriginEffectorpivotOffsetX"),
        ("ChestOriginEffectorpivotOffsetY", "ChestOriginEffectorpivotOffsetY"),
        ("ChestOriginEffectorpivotOffsetZ", "ChestOriginEffectorpivotOffsetZ"),
    )

    ChestOriginEffectorpivotOffsetX = DoubleLinearField()

    ChestOriginEffectorpivotOffsetY = DoubleLinearField()

    ChestOriginEffectorpivotOffsetZ = DoubleLinearField()


class ChestOriginEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[ChestOriginEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ChestOriginEffectorpivotOffsetX = DoubleLinearField()

    ChestOriginEffectorpivotOffsetY = DoubleLinearField()

    ChestOriginEffectorpivotOffsetZ = DoubleLinearField()


class ChestOriginEffectorpivotOffsetField(
    CompoundField[ChestOriginEffectorpivotOffsetAttrOperator, ChestOriginEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ChestOriginEffectorpivotOffsetAttrOperator
    PLUG_CLS = ChestOriginEffectorpivotOffsetPlugOperator


class ChestEndEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["ChestEndEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ChestEndEffectorpivotOffsetX", "ChestEndEffectorpivotOffsetX"),
        ("ChestEndEffectorpivotOffsetY", "ChestEndEffectorpivotOffsetY"),
        ("ChestEndEffectorpivotOffsetZ", "ChestEndEffectorpivotOffsetZ"),
    )

    ChestEndEffectorpivotOffsetX = DoubleLinearField()

    ChestEndEffectorpivotOffsetY = DoubleLinearField()

    ChestEndEffectorpivotOffsetZ = DoubleLinearField()


class ChestEndEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[ChestEndEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ChestEndEffectorpivotOffsetX = DoubleLinearField()

    ChestEndEffectorpivotOffsetY = DoubleLinearField()

    ChestEndEffectorpivotOffsetZ = DoubleLinearField()


class ChestEndEffectorpivotOffsetField(
    CompoundField[ChestEndEffectorpivotOffsetAttrOperator, ChestEndEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ChestEndEffectorpivotOffsetAttrOperator
    PLUG_CLS = ChestEndEffectorpivotOffsetPlugOperator


class LeftFootEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftFootEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootEffectorpivotOffsetX", "LeftFootEffectorpivotOffsetX"),
        ("LeftFootEffectorpivotOffsetY", "LeftFootEffectorpivotOffsetY"),
        ("LeftFootEffectorpivotOffsetZ", "LeftFootEffectorpivotOffsetZ"),
    )

    LeftFootEffectorpivotOffsetX = DoubleLinearField()

    LeftFootEffectorpivotOffsetY = DoubleLinearField()

    LeftFootEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootEffectorpivotOffsetX = DoubleLinearField()

    LeftFootEffectorpivotOffsetY = DoubleLinearField()

    LeftFootEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootEffectorpivotOffsetField(
    CompoundField[LeftFootEffectorpivotOffsetAttrOperator, LeftFootEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftFootEffectorpivotOffsetPlugOperator


class RightFootEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightFootEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootEffectorpivotOffsetX", "RightFootEffectorpivotOffsetX"),
        ("RightFootEffectorpivotOffsetY", "RightFootEffectorpivotOffsetY"),
        ("RightFootEffectorpivotOffsetZ", "RightFootEffectorpivotOffsetZ"),
    )

    RightFootEffectorpivotOffsetX = DoubleLinearField()

    RightFootEffectorpivotOffsetY = DoubleLinearField()

    RightFootEffectorpivotOffsetZ = DoubleLinearField()


class RightFootEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootEffectorpivotOffsetX = DoubleLinearField()

    RightFootEffectorpivotOffsetY = DoubleLinearField()

    RightFootEffectorpivotOffsetZ = DoubleLinearField()


class RightFootEffectorpivotOffsetField(
    CompoundField[RightFootEffectorpivotOffsetAttrOperator, RightFootEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightFootEffectorpivotOffsetPlugOperator


class LeftShoulderEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftShoulderEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftShoulderEffectorpivotOffsetX", "LeftShoulderEffectorpivotOffsetX"),
        ("LeftShoulderEffectorpivotOffsetY", "LeftShoulderEffectorpivotOffsetY"),
        ("LeftShoulderEffectorpivotOffsetZ", "LeftShoulderEffectorpivotOffsetZ"),
    )

    LeftShoulderEffectorpivotOffsetX = DoubleLinearField()

    LeftShoulderEffectorpivotOffsetY = DoubleLinearField()

    LeftShoulderEffectorpivotOffsetZ = DoubleLinearField()


class LeftShoulderEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftShoulderEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftShoulderEffectorpivotOffsetX = DoubleLinearField()

    LeftShoulderEffectorpivotOffsetY = DoubleLinearField()

    LeftShoulderEffectorpivotOffsetZ = DoubleLinearField()


class LeftShoulderEffectorpivotOffsetField(
    CompoundField[LeftShoulderEffectorpivotOffsetAttrOperator, LeftShoulderEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftShoulderEffectorpivotOffsetPlugOperator


class RightShoulderEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightShoulderEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightShoulderEffectorpivotOffsetX", "RightShoulderEffectorpivotOffsetX"),
        ("RightShoulderEffectorpivotOffsetY", "RightShoulderEffectorpivotOffsetY"),
        ("RightShoulderEffectorpivotOffsetZ", "RightShoulderEffectorpivotOffsetZ"),
    )

    RightShoulderEffectorpivotOffsetX = DoubleLinearField()

    RightShoulderEffectorpivotOffsetY = DoubleLinearField()

    RightShoulderEffectorpivotOffsetZ = DoubleLinearField()


class RightShoulderEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightShoulderEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightShoulderEffectorpivotOffsetX = DoubleLinearField()

    RightShoulderEffectorpivotOffsetY = DoubleLinearField()

    RightShoulderEffectorpivotOffsetZ = DoubleLinearField()


class RightShoulderEffectorpivotOffsetField(
    CompoundField[RightShoulderEffectorpivotOffsetAttrOperator, RightShoulderEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightShoulderEffectorpivotOffsetPlugOperator


class HeadEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["HeadEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HeadEffectorpivotOffsetX", "HeadEffectorpivotOffsetX"),
        ("HeadEffectorpivotOffsetY", "HeadEffectorpivotOffsetY"),
        ("HeadEffectorpivotOffsetZ", "HeadEffectorpivotOffsetZ"),
    )

    HeadEffectorpivotOffsetX = DoubleLinearField()

    HeadEffectorpivotOffsetY = DoubleLinearField()

    HeadEffectorpivotOffsetZ = DoubleLinearField()


class HeadEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[HeadEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    HeadEffectorpivotOffsetX = DoubleLinearField()

    HeadEffectorpivotOffsetY = DoubleLinearField()

    HeadEffectorpivotOffsetZ = DoubleLinearField()


class HeadEffectorpivotOffsetField(
    CompoundField[HeadEffectorpivotOffsetAttrOperator, HeadEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HeadEffectorpivotOffsetAttrOperator
    PLUG_CLS = HeadEffectorpivotOffsetPlugOperator


class LeftHipEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftHipEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHipEffectorpivotOffsetX", "LeftHipEffectorpivotOffsetX"),
        ("LeftHipEffectorpivotOffsetY", "LeftHipEffectorpivotOffsetY"),
        ("LeftHipEffectorpivotOffsetZ", "LeftHipEffectorpivotOffsetZ"),
    )

    LeftHipEffectorpivotOffsetX = DoubleLinearField()

    LeftHipEffectorpivotOffsetY = DoubleLinearField()

    LeftHipEffectorpivotOffsetZ = DoubleLinearField()


class LeftHipEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHipEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHipEffectorpivotOffsetX = DoubleLinearField()

    LeftHipEffectorpivotOffsetY = DoubleLinearField()

    LeftHipEffectorpivotOffsetZ = DoubleLinearField()


class LeftHipEffectorpivotOffsetField(
    CompoundField[LeftHipEffectorpivotOffsetAttrOperator, LeftHipEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHipEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftHipEffectorpivotOffsetPlugOperator


class RightHipEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightHipEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHipEffectorpivotOffsetX", "RightHipEffectorpivotOffsetX"),
        ("RightHipEffectorpivotOffsetY", "RightHipEffectorpivotOffsetY"),
        ("RightHipEffectorpivotOffsetZ", "RightHipEffectorpivotOffsetZ"),
    )

    RightHipEffectorpivotOffsetX = DoubleLinearField()

    RightHipEffectorpivotOffsetY = DoubleLinearField()

    RightHipEffectorpivotOffsetZ = DoubleLinearField()


class RightHipEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHipEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHipEffectorpivotOffsetX = DoubleLinearField()

    RightHipEffectorpivotOffsetY = DoubleLinearField()

    RightHipEffectorpivotOffsetZ = DoubleLinearField()


class RightHipEffectorpivotOffsetField(
    CompoundField[RightHipEffectorpivotOffsetAttrOperator, RightHipEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHipEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightHipEffectorpivotOffsetPlugOperator


class LeftHandEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftHandEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandEffectorpivotOffsetX", "LeftHandEffectorpivotOffsetX"),
        ("LeftHandEffectorpivotOffsetY", "LeftHandEffectorpivotOffsetY"),
        ("LeftHandEffectorpivotOffsetZ", "LeftHandEffectorpivotOffsetZ"),
    )

    LeftHandEffectorpivotOffsetX = DoubleLinearField()

    LeftHandEffectorpivotOffsetY = DoubleLinearField()

    LeftHandEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandEffectorpivotOffsetX = DoubleLinearField()

    LeftHandEffectorpivotOffsetY = DoubleLinearField()

    LeftHandEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandEffectorpivotOffsetField(
    CompoundField[LeftHandEffectorpivotOffsetAttrOperator, LeftHandEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftHandEffectorpivotOffsetPlugOperator


class RightHandEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightHandEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandEffectorpivotOffsetX", "RightHandEffectorpivotOffsetX"),
        ("RightHandEffectorpivotOffsetY", "RightHandEffectorpivotOffsetY"),
        ("RightHandEffectorpivotOffsetZ", "RightHandEffectorpivotOffsetZ"),
    )

    RightHandEffectorpivotOffsetX = DoubleLinearField()

    RightHandEffectorpivotOffsetY = DoubleLinearField()

    RightHandEffectorpivotOffsetZ = DoubleLinearField()


class RightHandEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandEffectorpivotOffsetX = DoubleLinearField()

    RightHandEffectorpivotOffsetY = DoubleLinearField()

    RightHandEffectorpivotOffsetZ = DoubleLinearField()


class RightHandEffectorpivotOffsetField(
    CompoundField[RightHandEffectorpivotOffsetAttrOperator, RightHandEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightHandEffectorpivotOffsetPlugOperator


class LeftHandThumbEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftHandThumbEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumbEffectorpivotOffsetX", "LeftHandThumbEffectorpivotOffsetX"),
        ("LeftHandThumbEffectorpivotOffsetY", "LeftHandThumbEffectorpivotOffsetY"),
        ("LeftHandThumbEffectorpivotOffsetZ", "LeftHandThumbEffectorpivotOffsetZ"),
    )

    LeftHandThumbEffectorpivotOffsetX = DoubleLinearField()

    LeftHandThumbEffectorpivotOffsetY = DoubleLinearField()

    LeftHandThumbEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandThumbEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandThumbEffectorpivotOffsetX = DoubleLinearField()

    LeftHandThumbEffectorpivotOffsetY = DoubleLinearField()

    LeftHandThumbEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandThumbEffectorpivotOffsetField(
    CompoundField[LeftHandThumbEffectorpivotOffsetAttrOperator, LeftHandThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumbEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftHandThumbEffectorpivotOffsetPlugOperator


class LeftHandIndexEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftHandIndexEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndexEffectorpivotOffsetX", "LeftHandIndexEffectorpivotOffsetX"),
        ("LeftHandIndexEffectorpivotOffsetY", "LeftHandIndexEffectorpivotOffsetY"),
        ("LeftHandIndexEffectorpivotOffsetZ", "LeftHandIndexEffectorpivotOffsetZ"),
    )

    LeftHandIndexEffectorpivotOffsetX = DoubleLinearField()

    LeftHandIndexEffectorpivotOffsetY = DoubleLinearField()

    LeftHandIndexEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandIndexEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandIndexEffectorpivotOffsetX = DoubleLinearField()

    LeftHandIndexEffectorpivotOffsetY = DoubleLinearField()

    LeftHandIndexEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandIndexEffectorpivotOffsetField(
    CompoundField[LeftHandIndexEffectorpivotOffsetAttrOperator, LeftHandIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndexEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftHandIndexEffectorpivotOffsetPlugOperator


class LeftHandMiddleEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftHandMiddleEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddleEffectorpivotOffsetX", "LeftHandMiddleEffectorpivotOffsetX"),
        ("LeftHandMiddleEffectorpivotOffsetY", "LeftHandMiddleEffectorpivotOffsetY"),
        ("LeftHandMiddleEffectorpivotOffsetZ", "LeftHandMiddleEffectorpivotOffsetZ"),
    )

    LeftHandMiddleEffectorpivotOffsetX = DoubleLinearField()

    LeftHandMiddleEffectorpivotOffsetY = DoubleLinearField()

    LeftHandMiddleEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandMiddleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandMiddleEffectorpivotOffsetX = DoubleLinearField()

    LeftHandMiddleEffectorpivotOffsetY = DoubleLinearField()

    LeftHandMiddleEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandMiddleEffectorpivotOffsetField(
    CompoundField[LeftHandMiddleEffectorpivotOffsetAttrOperator, LeftHandMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddleEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftHandMiddleEffectorpivotOffsetPlugOperator


class LeftHandRingEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftHandRingEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRingEffectorpivotOffsetX", "LeftHandRingEffectorpivotOffsetX"),
        ("LeftHandRingEffectorpivotOffsetY", "LeftHandRingEffectorpivotOffsetY"),
        ("LeftHandRingEffectorpivotOffsetZ", "LeftHandRingEffectorpivotOffsetZ"),
    )

    LeftHandRingEffectorpivotOffsetX = DoubleLinearField()

    LeftHandRingEffectorpivotOffsetY = DoubleLinearField()

    LeftHandRingEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandRingEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandRingEffectorpivotOffsetX = DoubleLinearField()

    LeftHandRingEffectorpivotOffsetY = DoubleLinearField()

    LeftHandRingEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandRingEffectorpivotOffsetField(
    CompoundField[LeftHandRingEffectorpivotOffsetAttrOperator, LeftHandRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRingEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftHandRingEffectorpivotOffsetPlugOperator


class LeftHandPinkyEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftHandPinkyEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinkyEffectorpivotOffsetX", "LeftHandPinkyEffectorpivotOffsetX"),
        ("LeftHandPinkyEffectorpivotOffsetY", "LeftHandPinkyEffectorpivotOffsetY"),
        ("LeftHandPinkyEffectorpivotOffsetZ", "LeftHandPinkyEffectorpivotOffsetZ"),
    )

    LeftHandPinkyEffectorpivotOffsetX = DoubleLinearField()

    LeftHandPinkyEffectorpivotOffsetY = DoubleLinearField()

    LeftHandPinkyEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandPinkyEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandPinkyEffectorpivotOffsetX = DoubleLinearField()

    LeftHandPinkyEffectorpivotOffsetY = DoubleLinearField()

    LeftHandPinkyEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandPinkyEffectorpivotOffsetField(
    CompoundField[LeftHandPinkyEffectorpivotOffsetAttrOperator, LeftHandPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinkyEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftHandPinkyEffectorpivotOffsetPlugOperator


class LeftHandExtraFingerEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftHandExtraFingerEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFingerEffectorpivotOffsetX", "LeftHandExtraFingerEffectorpivotOffsetX"),
        ("LeftHandExtraFingerEffectorpivotOffsetY", "LeftHandExtraFingerEffectorpivotOffsetY"),
        ("LeftHandExtraFingerEffectorpivotOffsetZ", "LeftHandExtraFingerEffectorpivotOffsetZ"),
    )

    LeftHandExtraFingerEffectorpivotOffsetX = DoubleLinearField()

    LeftHandExtraFingerEffectorpivotOffsetY = DoubleLinearField()

    LeftHandExtraFingerEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandExtraFingerEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFingerEffectorpivotOffsetX = DoubleLinearField()

    LeftHandExtraFingerEffectorpivotOffsetY = DoubleLinearField()

    LeftHandExtraFingerEffectorpivotOffsetZ = DoubleLinearField()


class LeftHandExtraFingerEffectorpivotOffsetField(
    CompoundField[LeftHandExtraFingerEffectorpivotOffsetAttrOperator, LeftHandExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFingerEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftHandExtraFingerEffectorpivotOffsetPlugOperator


class RightHandThumbEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightHandThumbEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumbEffectorpivotOffsetX", "RightHandThumbEffectorpivotOffsetX"),
        ("RightHandThumbEffectorpivotOffsetY", "RightHandThumbEffectorpivotOffsetY"),
        ("RightHandThumbEffectorpivotOffsetZ", "RightHandThumbEffectorpivotOffsetZ"),
    )

    RightHandThumbEffectorpivotOffsetX = DoubleLinearField()

    RightHandThumbEffectorpivotOffsetY = DoubleLinearField()

    RightHandThumbEffectorpivotOffsetZ = DoubleLinearField()


class RightHandThumbEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandThumbEffectorpivotOffsetX = DoubleLinearField()

    RightHandThumbEffectorpivotOffsetY = DoubleLinearField()

    RightHandThumbEffectorpivotOffsetZ = DoubleLinearField()


class RightHandThumbEffectorpivotOffsetField(
    CompoundField[RightHandThumbEffectorpivotOffsetAttrOperator, RightHandThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumbEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightHandThumbEffectorpivotOffsetPlugOperator


class RightHandIndexEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightHandIndexEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndexEffectorpivotOffsetX", "RightHandIndexEffectorpivotOffsetX"),
        ("RightHandIndexEffectorpivotOffsetY", "RightHandIndexEffectorpivotOffsetY"),
        ("RightHandIndexEffectorpivotOffsetZ", "RightHandIndexEffectorpivotOffsetZ"),
    )

    RightHandIndexEffectorpivotOffsetX = DoubleLinearField()

    RightHandIndexEffectorpivotOffsetY = DoubleLinearField()

    RightHandIndexEffectorpivotOffsetZ = DoubleLinearField()


class RightHandIndexEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandIndexEffectorpivotOffsetX = DoubleLinearField()

    RightHandIndexEffectorpivotOffsetY = DoubleLinearField()

    RightHandIndexEffectorpivotOffsetZ = DoubleLinearField()


class RightHandIndexEffectorpivotOffsetField(
    CompoundField[RightHandIndexEffectorpivotOffsetAttrOperator, RightHandIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndexEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightHandIndexEffectorpivotOffsetPlugOperator


class RightHandMiddleEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightHandMiddleEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddleEffectorpivotOffsetX", "RightHandMiddleEffectorpivotOffsetX"),
        ("RightHandMiddleEffectorpivotOffsetY", "RightHandMiddleEffectorpivotOffsetY"),
        ("RightHandMiddleEffectorpivotOffsetZ", "RightHandMiddleEffectorpivotOffsetZ"),
    )

    RightHandMiddleEffectorpivotOffsetX = DoubleLinearField()

    RightHandMiddleEffectorpivotOffsetY = DoubleLinearField()

    RightHandMiddleEffectorpivotOffsetZ = DoubleLinearField()


class RightHandMiddleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandMiddleEffectorpivotOffsetX = DoubleLinearField()

    RightHandMiddleEffectorpivotOffsetY = DoubleLinearField()

    RightHandMiddleEffectorpivotOffsetZ = DoubleLinearField()


class RightHandMiddleEffectorpivotOffsetField(
    CompoundField[RightHandMiddleEffectorpivotOffsetAttrOperator, RightHandMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddleEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightHandMiddleEffectorpivotOffsetPlugOperator


class RightHandRingEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightHandRingEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRingEffectorpivotOffsetX", "RightHandRingEffectorpivotOffsetX"),
        ("RightHandRingEffectorpivotOffsetY", "RightHandRingEffectorpivotOffsetY"),
        ("RightHandRingEffectorpivotOffsetZ", "RightHandRingEffectorpivotOffsetZ"),
    )

    RightHandRingEffectorpivotOffsetX = DoubleLinearField()

    RightHandRingEffectorpivotOffsetY = DoubleLinearField()

    RightHandRingEffectorpivotOffsetZ = DoubleLinearField()


class RightHandRingEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandRingEffectorpivotOffsetX = DoubleLinearField()

    RightHandRingEffectorpivotOffsetY = DoubleLinearField()

    RightHandRingEffectorpivotOffsetZ = DoubleLinearField()


class RightHandRingEffectorpivotOffsetField(
    CompoundField[RightHandRingEffectorpivotOffsetAttrOperator, RightHandRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRingEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightHandRingEffectorpivotOffsetPlugOperator


class RightHandPinkyEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightHandPinkyEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinkyEffectorpivotOffsetX", "RightHandPinkyEffectorpivotOffsetX"),
        ("RightHandPinkyEffectorpivotOffsetY", "RightHandPinkyEffectorpivotOffsetY"),
        ("RightHandPinkyEffectorpivotOffsetZ", "RightHandPinkyEffectorpivotOffsetZ"),
    )

    RightHandPinkyEffectorpivotOffsetX = DoubleLinearField()

    RightHandPinkyEffectorpivotOffsetY = DoubleLinearField()

    RightHandPinkyEffectorpivotOffsetZ = DoubleLinearField()


class RightHandPinkyEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandPinkyEffectorpivotOffsetX = DoubleLinearField()

    RightHandPinkyEffectorpivotOffsetY = DoubleLinearField()

    RightHandPinkyEffectorpivotOffsetZ = DoubleLinearField()


class RightHandPinkyEffectorpivotOffsetField(
    CompoundField[RightHandPinkyEffectorpivotOffsetAttrOperator, RightHandPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinkyEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightHandPinkyEffectorpivotOffsetPlugOperator


class RightHandExtraFingerEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightHandExtraFingerEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFingerEffectorpivotOffsetX", "RightHandExtraFingerEffectorpivotOffsetX"),
        ("RightHandExtraFingerEffectorpivotOffsetY", "RightHandExtraFingerEffectorpivotOffsetY"),
        ("RightHandExtraFingerEffectorpivotOffsetZ", "RightHandExtraFingerEffectorpivotOffsetZ"),
    )

    RightHandExtraFingerEffectorpivotOffsetX = DoubleLinearField()

    RightHandExtraFingerEffectorpivotOffsetY = DoubleLinearField()

    RightHandExtraFingerEffectorpivotOffsetZ = DoubleLinearField()


class RightHandExtraFingerEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandExtraFingerEffectorpivotOffsetX = DoubleLinearField()

    RightHandExtraFingerEffectorpivotOffsetY = DoubleLinearField()

    RightHandExtraFingerEffectorpivotOffsetZ = DoubleLinearField()


class RightHandExtraFingerEffectorpivotOffsetField(
    CompoundField[RightHandExtraFingerEffectorpivotOffsetAttrOperator, RightHandExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFingerEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightHandExtraFingerEffectorpivotOffsetPlugOperator


class LeftFootThumbEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftFootThumbEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumbEffectorpivotOffsetX", "LeftFootThumbEffectorpivotOffsetX"),
        ("LeftFootThumbEffectorpivotOffsetY", "LeftFootThumbEffectorpivotOffsetY"),
        ("LeftFootThumbEffectorpivotOffsetZ", "LeftFootThumbEffectorpivotOffsetZ"),
    )

    LeftFootThumbEffectorpivotOffsetX = DoubleLinearField()

    LeftFootThumbEffectorpivotOffsetY = DoubleLinearField()

    LeftFootThumbEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootThumbEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootThumbEffectorpivotOffsetX = DoubleLinearField()

    LeftFootThumbEffectorpivotOffsetY = DoubleLinearField()

    LeftFootThumbEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootThumbEffectorpivotOffsetField(
    CompoundField[LeftFootThumbEffectorpivotOffsetAttrOperator, LeftFootThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumbEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftFootThumbEffectorpivotOffsetPlugOperator


class LeftFootIndexEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftFootIndexEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndexEffectorpivotOffsetX", "LeftFootIndexEffectorpivotOffsetX"),
        ("LeftFootIndexEffectorpivotOffsetY", "LeftFootIndexEffectorpivotOffsetY"),
        ("LeftFootIndexEffectorpivotOffsetZ", "LeftFootIndexEffectorpivotOffsetZ"),
    )

    LeftFootIndexEffectorpivotOffsetX = DoubleLinearField()

    LeftFootIndexEffectorpivotOffsetY = DoubleLinearField()

    LeftFootIndexEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootIndexEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootIndexEffectorpivotOffsetX = DoubleLinearField()

    LeftFootIndexEffectorpivotOffsetY = DoubleLinearField()

    LeftFootIndexEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootIndexEffectorpivotOffsetField(
    CompoundField[LeftFootIndexEffectorpivotOffsetAttrOperator, LeftFootIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndexEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftFootIndexEffectorpivotOffsetPlugOperator


class LeftFootMiddleEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftFootMiddleEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddleEffectorpivotOffsetX", "LeftFootMiddleEffectorpivotOffsetX"),
        ("LeftFootMiddleEffectorpivotOffsetY", "LeftFootMiddleEffectorpivotOffsetY"),
        ("LeftFootMiddleEffectorpivotOffsetZ", "LeftFootMiddleEffectorpivotOffsetZ"),
    )

    LeftFootMiddleEffectorpivotOffsetX = DoubleLinearField()

    LeftFootMiddleEffectorpivotOffsetY = DoubleLinearField()

    LeftFootMiddleEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootMiddleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootMiddleEffectorpivotOffsetX = DoubleLinearField()

    LeftFootMiddleEffectorpivotOffsetY = DoubleLinearField()

    LeftFootMiddleEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootMiddleEffectorpivotOffsetField(
    CompoundField[LeftFootMiddleEffectorpivotOffsetAttrOperator, LeftFootMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddleEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftFootMiddleEffectorpivotOffsetPlugOperator


class LeftFootRingEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftFootRingEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRingEffectorpivotOffsetX", "LeftFootRingEffectorpivotOffsetX"),
        ("LeftFootRingEffectorpivotOffsetY", "LeftFootRingEffectorpivotOffsetY"),
        ("LeftFootRingEffectorpivotOffsetZ", "LeftFootRingEffectorpivotOffsetZ"),
    )

    LeftFootRingEffectorpivotOffsetX = DoubleLinearField()

    LeftFootRingEffectorpivotOffsetY = DoubleLinearField()

    LeftFootRingEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootRingEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootRingEffectorpivotOffsetX = DoubleLinearField()

    LeftFootRingEffectorpivotOffsetY = DoubleLinearField()

    LeftFootRingEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootRingEffectorpivotOffsetField(
    CompoundField[LeftFootRingEffectorpivotOffsetAttrOperator, LeftFootRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRingEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftFootRingEffectorpivotOffsetPlugOperator


class LeftFootPinkyEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftFootPinkyEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinkyEffectorpivotOffsetX", "LeftFootPinkyEffectorpivotOffsetX"),
        ("LeftFootPinkyEffectorpivotOffsetY", "LeftFootPinkyEffectorpivotOffsetY"),
        ("LeftFootPinkyEffectorpivotOffsetZ", "LeftFootPinkyEffectorpivotOffsetZ"),
    )

    LeftFootPinkyEffectorpivotOffsetX = DoubleLinearField()

    LeftFootPinkyEffectorpivotOffsetY = DoubleLinearField()

    LeftFootPinkyEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootPinkyEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootPinkyEffectorpivotOffsetX = DoubleLinearField()

    LeftFootPinkyEffectorpivotOffsetY = DoubleLinearField()

    LeftFootPinkyEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootPinkyEffectorpivotOffsetField(
    CompoundField[LeftFootPinkyEffectorpivotOffsetAttrOperator, LeftFootPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinkyEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftFootPinkyEffectorpivotOffsetPlugOperator


class LeftFootExtraFingerEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["LeftFootExtraFingerEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFingerEffectorpivotOffsetX", "LeftFootExtraFingerEffectorpivotOffsetX"),
        ("LeftFootExtraFingerEffectorpivotOffsetY", "LeftFootExtraFingerEffectorpivotOffsetY"),
        ("LeftFootExtraFingerEffectorpivotOffsetZ", "LeftFootExtraFingerEffectorpivotOffsetZ"),
    )

    LeftFootExtraFingerEffectorpivotOffsetX = DoubleLinearField()

    LeftFootExtraFingerEffectorpivotOffsetY = DoubleLinearField()

    LeftFootExtraFingerEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootExtraFingerEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFingerEffectorpivotOffsetX = DoubleLinearField()

    LeftFootExtraFingerEffectorpivotOffsetY = DoubleLinearField()

    LeftFootExtraFingerEffectorpivotOffsetZ = DoubleLinearField()


class LeftFootExtraFingerEffectorpivotOffsetField(
    CompoundField[LeftFootExtraFingerEffectorpivotOffsetAttrOperator, LeftFootExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFingerEffectorpivotOffsetAttrOperator
    PLUG_CLS = LeftFootExtraFingerEffectorpivotOffsetPlugOperator


class RightFootThumbEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightFootThumbEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumbEffectorpivotOffsetX", "RightFootThumbEffectorpivotOffsetX"),
        ("RightFootThumbEffectorpivotOffsetY", "RightFootThumbEffectorpivotOffsetY"),
        ("RightFootThumbEffectorpivotOffsetZ", "RightFootThumbEffectorpivotOffsetZ"),
    )

    RightFootThumbEffectorpivotOffsetX = DoubleLinearField()

    RightFootThumbEffectorpivotOffsetY = DoubleLinearField()

    RightFootThumbEffectorpivotOffsetZ = DoubleLinearField()


class RightFootThumbEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootThumbEffectorpivotOffsetX = DoubleLinearField()

    RightFootThumbEffectorpivotOffsetY = DoubleLinearField()

    RightFootThumbEffectorpivotOffsetZ = DoubleLinearField()


class RightFootThumbEffectorpivotOffsetField(
    CompoundField[RightFootThumbEffectorpivotOffsetAttrOperator, RightFootThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumbEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightFootThumbEffectorpivotOffsetPlugOperator


class RightFootIndexEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightFootIndexEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndexEffectorpivotOffsetX", "RightFootIndexEffectorpivotOffsetX"),
        ("RightFootIndexEffectorpivotOffsetY", "RightFootIndexEffectorpivotOffsetY"),
        ("RightFootIndexEffectorpivotOffsetZ", "RightFootIndexEffectorpivotOffsetZ"),
    )

    RightFootIndexEffectorpivotOffsetX = DoubleLinearField()

    RightFootIndexEffectorpivotOffsetY = DoubleLinearField()

    RightFootIndexEffectorpivotOffsetZ = DoubleLinearField()


class RightFootIndexEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootIndexEffectorpivotOffsetX = DoubleLinearField()

    RightFootIndexEffectorpivotOffsetY = DoubleLinearField()

    RightFootIndexEffectorpivotOffsetZ = DoubleLinearField()


class RightFootIndexEffectorpivotOffsetField(
    CompoundField[RightFootIndexEffectorpivotOffsetAttrOperator, RightFootIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndexEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightFootIndexEffectorpivotOffsetPlugOperator


class RightFootMiddleEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightFootMiddleEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddleEffectorpivotOffsetX", "RightFootMiddleEffectorpivotOffsetX"),
        ("RightFootMiddleEffectorpivotOffsetY", "RightFootMiddleEffectorpivotOffsetY"),
        ("RightFootMiddleEffectorpivotOffsetZ", "RightFootMiddleEffectorpivotOffsetZ"),
    )

    RightFootMiddleEffectorpivotOffsetX = DoubleLinearField()

    RightFootMiddleEffectorpivotOffsetY = DoubleLinearField()

    RightFootMiddleEffectorpivotOffsetZ = DoubleLinearField()


class RightFootMiddleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootMiddleEffectorpivotOffsetX = DoubleLinearField()

    RightFootMiddleEffectorpivotOffsetY = DoubleLinearField()

    RightFootMiddleEffectorpivotOffsetZ = DoubleLinearField()


class RightFootMiddleEffectorpivotOffsetField(
    CompoundField[RightFootMiddleEffectorpivotOffsetAttrOperator, RightFootMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddleEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightFootMiddleEffectorpivotOffsetPlugOperator


class RightFootRingEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightFootRingEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRingEffectorpivotOffsetX", "RightFootRingEffectorpivotOffsetX"),
        ("RightFootRingEffectorpivotOffsetY", "RightFootRingEffectorpivotOffsetY"),
        ("RightFootRingEffectorpivotOffsetZ", "RightFootRingEffectorpivotOffsetZ"),
    )

    RightFootRingEffectorpivotOffsetX = DoubleLinearField()

    RightFootRingEffectorpivotOffsetY = DoubleLinearField()

    RightFootRingEffectorpivotOffsetZ = DoubleLinearField()


class RightFootRingEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootRingEffectorpivotOffsetX = DoubleLinearField()

    RightFootRingEffectorpivotOffsetY = DoubleLinearField()

    RightFootRingEffectorpivotOffsetZ = DoubleLinearField()


class RightFootRingEffectorpivotOffsetField(
    CompoundField[RightFootRingEffectorpivotOffsetAttrOperator, RightFootRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRingEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightFootRingEffectorpivotOffsetPlugOperator


class RightFootPinkyEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightFootPinkyEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinkyEffectorpivotOffsetX", "RightFootPinkyEffectorpivotOffsetX"),
        ("RightFootPinkyEffectorpivotOffsetY", "RightFootPinkyEffectorpivotOffsetY"),
        ("RightFootPinkyEffectorpivotOffsetZ", "RightFootPinkyEffectorpivotOffsetZ"),
    )

    RightFootPinkyEffectorpivotOffsetX = DoubleLinearField()

    RightFootPinkyEffectorpivotOffsetY = DoubleLinearField()

    RightFootPinkyEffectorpivotOffsetZ = DoubleLinearField()


class RightFootPinkyEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootPinkyEffectorpivotOffsetX = DoubleLinearField()

    RightFootPinkyEffectorpivotOffsetY = DoubleLinearField()

    RightFootPinkyEffectorpivotOffsetZ = DoubleLinearField()


class RightFootPinkyEffectorpivotOffsetField(
    CompoundField[RightFootPinkyEffectorpivotOffsetAttrOperator, RightFootPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinkyEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightFootPinkyEffectorpivotOffsetPlugOperator


class RightFootExtraFingerEffectorpivotOffsetPlugOperator(
    CompoundPlugOperator["RightFootExtraFingerEffectorpivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFingerEffectorpivotOffsetX", "RightFootExtraFingerEffectorpivotOffsetX"),
        ("RightFootExtraFingerEffectorpivotOffsetY", "RightFootExtraFingerEffectorpivotOffsetY"),
        ("RightFootExtraFingerEffectorpivotOffsetZ", "RightFootExtraFingerEffectorpivotOffsetZ"),
    )

    RightFootExtraFingerEffectorpivotOffsetX = DoubleLinearField()

    RightFootExtraFingerEffectorpivotOffsetY = DoubleLinearField()

    RightFootExtraFingerEffectorpivotOffsetZ = DoubleLinearField()


class RightFootExtraFingerEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootExtraFingerEffectorpivotOffsetX = DoubleLinearField()

    RightFootExtraFingerEffectorpivotOffsetY = DoubleLinearField()

    RightFootExtraFingerEffectorpivotOffsetZ = DoubleLinearField()


class RightFootExtraFingerEffectorpivotOffsetField(
    CompoundField[RightFootExtraFingerEffectorpivotOffsetAttrOperator, RightFootExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFingerEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightFootExtraFingerEffectorpivotOffsetPlugOperator
