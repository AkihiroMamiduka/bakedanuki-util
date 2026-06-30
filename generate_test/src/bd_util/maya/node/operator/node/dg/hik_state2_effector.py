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

    HipsEffectorpivotOffset = HipsEffectorpivotOffsetField(multi=True)

    LeftAnkleEffectorGX = MatrixField()

    LeftAnkleEffectorGXM = MatrixField(multi=True)

    LeftAnkleEffectorpivotOffset = LeftAnkleEffectorpivotOffsetField(multi=True)

    RightAnkleEffectorGX = MatrixField()

    RightAnkleEffectorGXM = MatrixField(multi=True)

    RightAnkleEffectorpivotOffset = RightAnkleEffectorpivotOffsetField(multi=True)

    LeftWristEffectorGX = MatrixField()

    LeftWristEffectorGXM = MatrixField(multi=True)

    LeftWristEffectorpivotOffset = LeftWristEffectorpivotOffsetField(multi=True)

    RightWristEffectorGX = MatrixField()

    RightWristEffectorGXM = MatrixField(multi=True)

    RightWristEffectorpivotOffset = RightWristEffectorpivotOffsetField(multi=True)

    LeftKneeEffectorGX = MatrixField()

    LeftKneeEffectorGXM = MatrixField(multi=True)

    LeftKneeEffectorpivotOffset = LeftKneeEffectorpivotOffsetField(multi=True)

    RightKneeEffectorGX = MatrixField()

    RightKneeEffectorGXM = MatrixField(multi=True)

    RightKneeEffectorpivotOffset = RightKneeEffectorpivotOffsetField(multi=True)

    LeftElbowEffectorGX = MatrixField()

    LeftElbowEffectorGXM = MatrixField(multi=True)

    LeftElbowEffectorpivotOffset = LeftElbowEffectorpivotOffsetField(multi=True)

    RightElbowEffectorGX = MatrixField()

    RightElbowEffectorGXM = MatrixField(multi=True)

    RightElbowEffectorpivotOffset = RightElbowEffectorpivotOffsetField(multi=True)

    ChestOriginEffectorGX = MatrixField()

    ChestOriginEffectorGXM = MatrixField(multi=True)

    ChestOriginEffectorpivotOffset = ChestOriginEffectorpivotOffsetField(multi=True)

    ChestEndEffectorGX = MatrixField()

    ChestEndEffectorGXM = MatrixField(multi=True)

    ChestEndEffectorpivotOffset = ChestEndEffectorpivotOffsetField(multi=True)

    LeftFootEffectorGX = MatrixField()

    LeftFootEffectorGXM = MatrixField(multi=True)

    LeftFootEffectorpivotOffset = LeftFootEffectorpivotOffsetField(multi=True)

    RightFootEffectorGX = MatrixField()

    RightFootEffectorGXM = MatrixField(multi=True)

    RightFootEffectorpivotOffset = RightFootEffectorpivotOffsetField(multi=True)

    LeftShoulderEffectorGX = MatrixField()

    LeftShoulderEffectorGXM = MatrixField(multi=True)

    LeftShoulderEffectorpivotOffset = LeftShoulderEffectorpivotOffsetField(multi=True)

    RightShoulderEffectorGX = MatrixField()

    RightShoulderEffectorGXM = MatrixField(multi=True)

    RightShoulderEffectorpivotOffset = RightShoulderEffectorpivotOffsetField(multi=True)

    HeadEffectorGX = MatrixField()

    HeadEffectorGXM = MatrixField(multi=True)

    HeadEffectorpivotOffset = HeadEffectorpivotOffsetField(multi=True)

    LeftHipEffectorGX = MatrixField()

    LeftHipEffectorGXM = MatrixField(multi=True)

    LeftHipEffectorpivotOffset = LeftHipEffectorpivotOffsetField(multi=True)

    RightHipEffectorGX = MatrixField()

    RightHipEffectorGXM = MatrixField(multi=True)

    RightHipEffectorpivotOffset = RightHipEffectorpivotOffsetField(multi=True)

    LeftHandEffectorGX = MatrixField()

    LeftHandEffectorGXM = MatrixField(multi=True)

    LeftHandEffectorpivotOffset = LeftHandEffectorpivotOffsetField(multi=True)

    RightHandEffectorGX = MatrixField()

    RightHandEffectorGXM = MatrixField(multi=True)

    RightHandEffectorpivotOffset = RightHandEffectorpivotOffsetField(multi=True)

    LeftHandThumbEffectorGX = MatrixField()

    LeftHandThumbEffectorGXM = MatrixField(multi=True)

    LeftHandThumbEffectorpivotOffset = LeftHandThumbEffectorpivotOffsetField(multi=True)

    LeftHandIndexEffectorGX = MatrixField()

    LeftHandIndexEffectorGXM = MatrixField(multi=True)

    LeftHandIndexEffectorpivotOffset = LeftHandIndexEffectorpivotOffsetField(multi=True)

    LeftHandMiddleEffectorGX = MatrixField()

    LeftHandMiddleEffectorGXM = MatrixField(multi=True)

    LeftHandMiddleEffectorpivotOffset = LeftHandMiddleEffectorpivotOffsetField(multi=True)

    LeftHandRingEffectorGX = MatrixField()

    LeftHandRingEffectorGXM = MatrixField(multi=True)

    LeftHandRingEffectorpivotOffset = LeftHandRingEffectorpivotOffsetField(multi=True)

    LeftHandPinkyEffectorGX = MatrixField()

    LeftHandPinkyEffectorGXM = MatrixField(multi=True)

    LeftHandPinkyEffectorpivotOffset = LeftHandPinkyEffectorpivotOffsetField(multi=True)

    LeftHandExtraFingerEffectorGX = MatrixField()

    LeftHandExtraFingerEffectorGXM = MatrixField(multi=True)

    LeftHandExtraFingerEffectorpivotOffset = LeftHandExtraFingerEffectorpivotOffsetField(multi=True)

    RightHandThumbEffectorGX = MatrixField()

    RightHandThumbEffectorGXM = MatrixField(multi=True)

    RightHandThumbEffectorpivotOffset = RightHandThumbEffectorpivotOffsetField(multi=True)

    RightHandIndexEffectorGX = MatrixField()

    RightHandIndexEffectorGXM = MatrixField(multi=True)

    RightHandIndexEffectorpivotOffset = RightHandIndexEffectorpivotOffsetField(multi=True)

    RightHandMiddleEffectorGX = MatrixField()

    RightHandMiddleEffectorGXM = MatrixField(multi=True)

    RightHandMiddleEffectorpivotOffset = RightHandMiddleEffectorpivotOffsetField(multi=True)

    RightHandRingEffectorGX = MatrixField()

    RightHandRingEffectorGXM = MatrixField(multi=True)

    RightHandRingEffectorpivotOffset = RightHandRingEffectorpivotOffsetField(multi=True)

    RightHandPinkyEffectorGX = MatrixField()

    RightHandPinkyEffectorGXM = MatrixField(multi=True)

    RightHandPinkyEffectorpivotOffset = RightHandPinkyEffectorpivotOffsetField(multi=True)

    RightHandExtraFingerEffectorGX = MatrixField()

    RightHandExtraFingerEffectorGXM = MatrixField(multi=True)

    RightHandExtraFingerEffectorpivotOffset = RightHandExtraFingerEffectorpivotOffsetField(multi=True)

    LeftFootThumbEffectorGX = MatrixField()

    LeftFootThumbEffectorGXM = MatrixField(multi=True)

    LeftFootThumbEffectorpivotOffset = LeftFootThumbEffectorpivotOffsetField(multi=True)

    LeftFootIndexEffectorGX = MatrixField()

    LeftFootIndexEffectorGXM = MatrixField(multi=True)

    LeftFootIndexEffectorpivotOffset = LeftFootIndexEffectorpivotOffsetField(multi=True)

    LeftFootMiddleEffectorGX = MatrixField()

    LeftFootMiddleEffectorGXM = MatrixField(multi=True)

    LeftFootMiddleEffectorpivotOffset = LeftFootMiddleEffectorpivotOffsetField(multi=True)

    LeftFootRingEffectorGX = MatrixField()

    LeftFootRingEffectorGXM = MatrixField(multi=True)

    LeftFootRingEffectorpivotOffset = LeftFootRingEffectorpivotOffsetField(multi=True)

    LeftFootPinkyEffectorGX = MatrixField()

    LeftFootPinkyEffectorGXM = MatrixField(multi=True)

    LeftFootPinkyEffectorpivotOffset = LeftFootPinkyEffectorpivotOffsetField(multi=True)

    LeftFootExtraFingerEffectorGX = MatrixField()

    LeftFootExtraFingerEffectorGXM = MatrixField(multi=True)

    LeftFootExtraFingerEffectorpivotOffset = LeftFootExtraFingerEffectorpivotOffsetField(multi=True)

    RightFootThumbEffectorGX = MatrixField()

    RightFootThumbEffectorGXM = MatrixField(multi=True)

    RightFootThumbEffectorpivotOffset = RightFootThumbEffectorpivotOffsetField(multi=True)

    RightFootIndexEffectorGX = MatrixField()

    RightFootIndexEffectorGXM = MatrixField(multi=True)

    RightFootIndexEffectorpivotOffset = RightFootIndexEffectorpivotOffsetField(multi=True)

    RightFootMiddleEffectorGX = MatrixField()

    RightFootMiddleEffectorGXM = MatrixField(multi=True)

    RightFootMiddleEffectorpivotOffset = RightFootMiddleEffectorpivotOffsetField(multi=True)

    RightFootRingEffectorGX = MatrixField()

    RightFootRingEffectorGXM = MatrixField(multi=True)

    RightFootRingEffectorpivotOffset = RightFootRingEffectorpivotOffsetField(multi=True)

    RightFootPinkyEffectorGX = MatrixField()

    RightFootPinkyEffectorGXM = MatrixField(multi=True)

    RightFootPinkyEffectorpivotOffset = RightFootPinkyEffectorpivotOffsetField(multi=True)

    RightFootExtraFingerEffectorGX = MatrixField()

    RightFootExtraFingerEffectorGXM = MatrixField(multi=True)

    RightFootExtraFingerEffectorpivotOffset = RightFootExtraFingerEffectorpivotOffsetField(multi=True)
