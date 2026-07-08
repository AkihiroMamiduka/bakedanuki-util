# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hik_state2_effector import (
    ChestEndEffectorpivotOffsetField,
    ChestOriginEffectorpivotOffsetField,
    HeadEffectorpivotOffsetField,
    HipsEffectorpivotOffsetField,
    LeftAnkleEffectorpivotOffsetField,
    LeftElbowEffectorpivotOffsetField,
    LeftFootEffectorpivotOffsetField,
    LeftFootExtraFingerEffectorpivotOffsetField,
    LeftFootIndexEffectorpivotOffsetField,
    LeftFootMiddleEffectorpivotOffsetField,
    LeftFootPinkyEffectorpivotOffsetField,
    LeftFootRingEffectorpivotOffsetField,
    LeftFootThumbEffectorpivotOffsetField,
    LeftHandEffectorpivotOffsetField,
    LeftHandExtraFingerEffectorpivotOffsetField,
    LeftHandIndexEffectorpivotOffsetField,
    LeftHandMiddleEffectorpivotOffsetField,
    LeftHandPinkyEffectorpivotOffsetField,
    LeftHandRingEffectorpivotOffsetField,
    LeftHandThumbEffectorpivotOffsetField,
    LeftHipEffectorpivotOffsetField,
    LeftKneeEffectorpivotOffsetField,
    LeftShoulderEffectorpivotOffsetField,
    LeftWristEffectorpivotOffsetField,
    RightAnkleEffectorpivotOffsetField,
    RightElbowEffectorpivotOffsetField,
    RightFootEffectorpivotOffsetField,
    RightFootExtraFingerEffectorpivotOffsetField,
    RightFootIndexEffectorpivotOffsetField,
    RightFootMiddleEffectorpivotOffsetField,
    RightFootPinkyEffectorpivotOffsetField,
    RightFootRingEffectorpivotOffsetField,
    RightFootThumbEffectorpivotOffsetField,
    RightHandEffectorpivotOffsetField,
    RightHandExtraFingerEffectorpivotOffsetField,
    RightHandIndexEffectorpivotOffsetField,
    RightHandMiddleEffectorpivotOffsetField,
    RightHandPinkyEffectorpivotOffsetField,
    RightHandRingEffectorpivotOffsetField,
    RightHandThumbEffectorpivotOffsetField,
    RightHipEffectorpivotOffsetField,
    RightKneeEffectorpivotOffsetField,
    RightShoulderEffectorpivotOffsetField,
    RightWristEffectorpivotOffsetField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.typed import TypedField


class HIKState2Effector(DG):
    __slots__ = ()

    NODE_TYPE = "HIKState2Effector"

    InputEffectorState = TypedField()

    HipsEffectorGX = MatrixField()

    HipsEffectorGXM = MatrixField(multi=True)

    HipsEffectorpivotOffset = HipsEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftAnkleEffectorGX = MatrixField()

    LeftAnkleEffectorGXM = MatrixField(multi=True)

    LeftAnkleEffectorpivotOffset = LeftAnkleEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightAnkleEffectorGX = MatrixField()

    RightAnkleEffectorGXM = MatrixField(multi=True)

    RightAnkleEffectorpivotOffset = RightAnkleEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftWristEffectorGX = MatrixField()

    LeftWristEffectorGXM = MatrixField(multi=True)

    LeftWristEffectorpivotOffset = LeftWristEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightWristEffectorGX = MatrixField()

    RightWristEffectorGXM = MatrixField(multi=True)

    RightWristEffectorpivotOffset = RightWristEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftKneeEffectorGX = MatrixField()

    LeftKneeEffectorGXM = MatrixField(multi=True)

    LeftKneeEffectorpivotOffset = LeftKneeEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightKneeEffectorGX = MatrixField()

    RightKneeEffectorGXM = MatrixField(multi=True)

    RightKneeEffectorpivotOffset = RightKneeEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftElbowEffectorGX = MatrixField()

    LeftElbowEffectorGXM = MatrixField(multi=True)

    LeftElbowEffectorpivotOffset = LeftElbowEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightElbowEffectorGX = MatrixField()

    RightElbowEffectorGXM = MatrixField(multi=True)

    RightElbowEffectorpivotOffset = RightElbowEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    ChestOriginEffectorGX = MatrixField()

    ChestOriginEffectorGXM = MatrixField(multi=True)

    ChestOriginEffectorpivotOffset = ChestOriginEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    ChestEndEffectorGX = MatrixField()

    ChestEndEffectorGXM = MatrixField(multi=True)

    ChestEndEffectorpivotOffset = ChestEndEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootEffectorGX = MatrixField()

    LeftFootEffectorGXM = MatrixField(multi=True)

    LeftFootEffectorpivotOffset = LeftFootEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootEffectorGX = MatrixField()

    RightFootEffectorGXM = MatrixField(multi=True)

    RightFootEffectorpivotOffset = RightFootEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftShoulderEffectorGX = MatrixField()

    LeftShoulderEffectorGXM = MatrixField(multi=True)

    LeftShoulderEffectorpivotOffset = LeftShoulderEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightShoulderEffectorGX = MatrixField()

    RightShoulderEffectorGXM = MatrixField(multi=True)

    RightShoulderEffectorpivotOffset = RightShoulderEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    HeadEffectorGX = MatrixField()

    HeadEffectorGXM = MatrixField(multi=True)

    HeadEffectorpivotOffset = HeadEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHipEffectorGX = MatrixField()

    LeftHipEffectorGXM = MatrixField(multi=True)

    LeftHipEffectorpivotOffset = LeftHipEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHipEffectorGX = MatrixField()

    RightHipEffectorGXM = MatrixField(multi=True)

    RightHipEffectorpivotOffset = RightHipEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandEffectorGX = MatrixField()

    LeftHandEffectorGXM = MatrixField(multi=True)

    LeftHandEffectorpivotOffset = LeftHandEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandEffectorGX = MatrixField()

    RightHandEffectorGXM = MatrixField(multi=True)

    RightHandEffectorpivotOffset = RightHandEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandThumbEffectorGX = MatrixField()

    LeftHandThumbEffectorGXM = MatrixField(multi=True)

    LeftHandThumbEffectorpivotOffset = LeftHandThumbEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandIndexEffectorGX = MatrixField()

    LeftHandIndexEffectorGXM = MatrixField(multi=True)

    LeftHandIndexEffectorpivotOffset = LeftHandIndexEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandMiddleEffectorGX = MatrixField()

    LeftHandMiddleEffectorGXM = MatrixField(multi=True)

    LeftHandMiddleEffectorpivotOffset = LeftHandMiddleEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandRingEffectorGX = MatrixField()

    LeftHandRingEffectorGXM = MatrixField(multi=True)

    LeftHandRingEffectorpivotOffset = LeftHandRingEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandPinkyEffectorGX = MatrixField()

    LeftHandPinkyEffectorGXM = MatrixField(multi=True)

    LeftHandPinkyEffectorpivotOffset = LeftHandPinkyEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandExtraFingerEffectorGX = MatrixField()

    LeftHandExtraFingerEffectorGXM = MatrixField(multi=True)

    LeftHandExtraFingerEffectorpivotOffset = LeftHandExtraFingerEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandThumbEffectorGX = MatrixField()

    RightHandThumbEffectorGXM = MatrixField(multi=True)

    RightHandThumbEffectorpivotOffset = RightHandThumbEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandIndexEffectorGX = MatrixField()

    RightHandIndexEffectorGXM = MatrixField(multi=True)

    RightHandIndexEffectorpivotOffset = RightHandIndexEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandMiddleEffectorGX = MatrixField()

    RightHandMiddleEffectorGXM = MatrixField(multi=True)

    RightHandMiddleEffectorpivotOffset = RightHandMiddleEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandRingEffectorGX = MatrixField()

    RightHandRingEffectorGXM = MatrixField(multi=True)

    RightHandRingEffectorpivotOffset = RightHandRingEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandPinkyEffectorGX = MatrixField()

    RightHandPinkyEffectorGXM = MatrixField(multi=True)

    RightHandPinkyEffectorpivotOffset = RightHandPinkyEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandExtraFingerEffectorGX = MatrixField()

    RightHandExtraFingerEffectorGXM = MatrixField(multi=True)

    RightHandExtraFingerEffectorpivotOffset = RightHandExtraFingerEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootThumbEffectorGX = MatrixField()

    LeftFootThumbEffectorGXM = MatrixField(multi=True)

    LeftFootThumbEffectorpivotOffset = LeftFootThumbEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootIndexEffectorGX = MatrixField()

    LeftFootIndexEffectorGXM = MatrixField(multi=True)

    LeftFootIndexEffectorpivotOffset = LeftFootIndexEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootMiddleEffectorGX = MatrixField()

    LeftFootMiddleEffectorGXM = MatrixField(multi=True)

    LeftFootMiddleEffectorpivotOffset = LeftFootMiddleEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootRingEffectorGX = MatrixField()

    LeftFootRingEffectorGXM = MatrixField(multi=True)

    LeftFootRingEffectorpivotOffset = LeftFootRingEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootPinkyEffectorGX = MatrixField()

    LeftFootPinkyEffectorGXM = MatrixField(multi=True)

    LeftFootPinkyEffectorpivotOffset = LeftFootPinkyEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootExtraFingerEffectorGX = MatrixField()

    LeftFootExtraFingerEffectorGXM = MatrixField(multi=True)

    LeftFootExtraFingerEffectorpivotOffset = LeftFootExtraFingerEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootThumbEffectorGX = MatrixField()

    RightFootThumbEffectorGXM = MatrixField(multi=True)

    RightFootThumbEffectorpivotOffset = RightFootThumbEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootIndexEffectorGX = MatrixField()

    RightFootIndexEffectorGXM = MatrixField(multi=True)

    RightFootIndexEffectorpivotOffset = RightFootIndexEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootMiddleEffectorGX = MatrixField()

    RightFootMiddleEffectorGXM = MatrixField(multi=True)

    RightFootMiddleEffectorpivotOffset = RightFootMiddleEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootRingEffectorGX = MatrixField()

    RightFootRingEffectorGXM = MatrixField(multi=True)

    RightFootRingEffectorpivotOffset = RightFootRingEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootPinkyEffectorGX = MatrixField()

    RightFootPinkyEffectorGXM = MatrixField(multi=True)

    RightFootPinkyEffectorpivotOffset = RightFootPinkyEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootExtraFingerEffectorGX = MatrixField()

    RightFootExtraFingerEffectorGXM = MatrixField(multi=True)

    RightFootExtraFingerEffectorpivotOffset = RightFootExtraFingerEffectorpivotOffsetField(multi=True, default_value=(0.0, 0.0, 0.0))
