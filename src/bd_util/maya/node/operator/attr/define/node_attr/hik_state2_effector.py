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

    HipsEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    HipsEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    HipsEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class HipsEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[HipsEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    HipsEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    HipsEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    HipsEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftAnkleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftAnkleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftAnkleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftAnkleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftAnkleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftAnkleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftAnkleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftAnkleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightAnkleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightAnkleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightAnkleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightAnkleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightAnkleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightAnkleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightAnkleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightAnkleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftWristEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftWristEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftWristEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftWristEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftWristEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftWristEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftWristEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftWristEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightWristEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightWristEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightWristEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightWristEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightWristEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightWristEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightWristEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightWristEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftKneeEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftKneeEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftKneeEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftKneeEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftKneeEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftKneeEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftKneeEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftKneeEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightKneeEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightKneeEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightKneeEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightKneeEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightKneeEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightKneeEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightKneeEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightKneeEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftElbowEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftElbowEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftElbowEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftElbowEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftElbowEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftElbowEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftElbowEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftElbowEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightElbowEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightElbowEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightElbowEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightElbowEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightElbowEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightElbowEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightElbowEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightElbowEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    ChestOriginEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    ChestOriginEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    ChestOriginEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class ChestOriginEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[ChestOriginEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ChestOriginEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    ChestOriginEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    ChestOriginEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    ChestEndEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    ChestEndEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    ChestEndEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class ChestEndEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[ChestEndEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ChestEndEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    ChestEndEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    ChestEndEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftFootEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftFootEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightFootEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightFootEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftShoulderEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftShoulderEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftShoulderEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftShoulderEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftShoulderEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftShoulderEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftShoulderEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftShoulderEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightShoulderEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightShoulderEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightShoulderEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightShoulderEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightShoulderEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightShoulderEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightShoulderEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightShoulderEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    HeadEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    HeadEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    HeadEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class HeadEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[HeadEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    HeadEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    HeadEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    HeadEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftHipEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHipEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHipEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftHipEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHipEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHipEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHipEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHipEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightHipEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHipEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHipEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightHipEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHipEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHipEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHipEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHipEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftHandEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftHandEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightHandEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightHandEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftHandThumbEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandThumbEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandThumbEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftHandThumbEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandThumbEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandThumbEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandThumbEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftHandIndexEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandIndexEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandIndexEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftHandIndexEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandIndexEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandIndexEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandIndexEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftHandMiddleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandMiddleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandMiddleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftHandMiddleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandMiddleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandMiddleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandMiddleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftHandRingEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandRingEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandRingEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftHandRingEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandRingEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandRingEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandRingEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftHandPinkyEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandPinkyEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandPinkyEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftHandPinkyEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandPinkyEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandPinkyEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandPinkyEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftHandExtraFingerEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandExtraFingerEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandExtraFingerEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftHandExtraFingerEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftHandExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFingerEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftHandExtraFingerEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftHandExtraFingerEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightHandThumbEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandThumbEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandThumbEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightHandThumbEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandThumbEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandThumbEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandThumbEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightHandIndexEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandIndexEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandIndexEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightHandIndexEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandIndexEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandIndexEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandIndexEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightHandMiddleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandMiddleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandMiddleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightHandMiddleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandMiddleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandMiddleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandMiddleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightHandRingEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandRingEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandRingEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightHandRingEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandRingEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandRingEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandRingEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightHandPinkyEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandPinkyEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandPinkyEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightHandPinkyEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandPinkyEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandPinkyEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandPinkyEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightHandExtraFingerEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandExtraFingerEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandExtraFingerEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightHandExtraFingerEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightHandExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightHandExtraFingerEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightHandExtraFingerEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightHandExtraFingerEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftFootThumbEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootThumbEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootThumbEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftFootThumbEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootThumbEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootThumbEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootThumbEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftFootIndexEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootIndexEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootIndexEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftFootIndexEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootIndexEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootIndexEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootIndexEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftFootMiddleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootMiddleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootMiddleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftFootMiddleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootMiddleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootMiddleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootMiddleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftFootRingEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootRingEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootRingEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftFootRingEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootRingEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootRingEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootRingEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftFootPinkyEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootPinkyEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootPinkyEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftFootPinkyEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootPinkyEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootPinkyEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootPinkyEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    LeftFootExtraFingerEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootExtraFingerEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootExtraFingerEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class LeftFootExtraFingerEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[LeftFootExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFingerEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    LeftFootExtraFingerEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    LeftFootExtraFingerEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightFootThumbEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootThumbEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootThumbEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightFootThumbEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootThumbEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootThumbEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootThumbEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootThumbEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightFootIndexEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootIndexEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootIndexEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightFootIndexEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootIndexEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootIndexEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootIndexEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootIndexEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightFootMiddleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootMiddleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootMiddleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightFootMiddleEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootMiddleEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootMiddleEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootMiddleEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootMiddleEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightFootRingEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootRingEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootRingEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightFootRingEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootRingEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootRingEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootRingEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootRingEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightFootPinkyEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootPinkyEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootPinkyEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightFootPinkyEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootPinkyEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootPinkyEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootPinkyEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootPinkyEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


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

    RightFootExtraFingerEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootExtraFingerEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootExtraFingerEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightFootExtraFingerEffectorpivotOffsetAttrOperator(
    CompoundAttrOperator[RightFootExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    RightFootExtraFingerEffectorpivotOffsetX = DoubleLinearField(default_value=0.0)

    RightFootExtraFingerEffectorpivotOffsetY = DoubleLinearField(default_value=0.0)

    RightFootExtraFingerEffectorpivotOffsetZ = DoubleLinearField(default_value=0.0)


class RightFootExtraFingerEffectorpivotOffsetField(
    CompoundField[RightFootExtraFingerEffectorpivotOffsetAttrOperator, RightFootExtraFingerEffectorpivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFingerEffectorpivotOffsetAttrOperator
    PLUG_CLS = RightFootExtraFingerEffectorpivotOffsetPlugOperator
