# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)


class Pose_poseQuatPlugOperator(
    QuatCompoundBasePlugOperator["Pose_poseQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("poseQuatX", "pqx"),
        ("poseQuatY", "pqy"),
        ("poseQuatZ", "pqz"),
        ("poseQuatW", "pqw"),
    )

    poseQuatX = DoubleField()
    pqx = poseQuatX

    poseQuatY = DoubleField()
    pqy = poseQuatY

    poseQuatZ = DoubleField()
    pqz = poseQuatZ

    poseQuatW = DoubleField()
    pqw = poseQuatW


class Pose_poseQuatAttrOperator(
    QuatCompoundBaseAttrOperator[Pose_poseQuatPlugOperator]
):
    __slots__ = ()

    poseQuatX = DoubleField()
    pqx = poseQuatX

    poseQuatY = DoubleField()
    pqy = poseQuatY

    poseQuatZ = DoubleField()
    pqz = poseQuatZ

    poseQuatW = DoubleField()
    pqw = poseQuatW


class Pose_poseQuatField(
    QuatCompoundBaseField[Pose_poseQuatAttrOperator, Pose_poseQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Pose_poseQuatAttrOperator
    PLUG_CLS = Pose_poseQuatPlugOperator

    poseQuatX = DoubleField()
    pqx = poseQuatX

    poseQuatY = DoubleField()
    pqy = poseQuatY

    poseQuatZ = DoubleField()
    pqz = poseQuatZ

    poseQuatW = DoubleField()
    pqw = poseQuatW


class InputQuatPlugOperator(
    QuatCompoundBasePlugOperator["InputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputQuatX", "iqx"),
        ("inputQuatY", "iqy"),
        ("inputQuatZ", "iqz"),
        ("inputQuatW", "iqw"),
    )

    inputQuatX = DoubleField(default_value=0.0)
    iqx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
    iqw = inputQuatW


class InputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[InputQuatPlugOperator]
):
    __slots__ = ()

    inputQuatX = DoubleField(default_value=0.0)
    iqx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
    iqw = inputQuatW


class InputQuatField(
    QuatCompoundBaseField[InputQuatAttrOperator, InputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputQuatAttrOperator
    PLUG_CLS = InputQuatPlugOperator

    inputQuatX = DoubleField(default_value=0.0)
    iqx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
    iqw = inputQuatW


class PosePlugOperator(CompoundPlugOperator["PoseAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("poseQuat", "pq"),
        ("enabled", "en"),
    )

    poseQuat = Pose_poseQuatField(default_value=(0.0, 0.0, 0.0, 0.0))
    pq = poseQuat

    enabled = BoolField(default_value=True)
    en = enabled


class PoseAttrOperator(CompoundAttrOperator[PosePlugOperator]):
    __slots__ = ()

    poseQuat = Pose_poseQuatField(default_value=(0.0, 0.0, 0.0, 0.0))
    pq = poseQuat

    enabled = BoolField(default_value=True)
    en = enabled


class PoseField(CompoundField[PoseAttrOperator, PosePlugOperator]):
    __slots__ = ()

    ATTR_CLS = PoseAttrOperator
    PLUG_CLS = PosePlugOperator
