# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hik_effector2_state import (
    ChestEndEffectorPivotField,
    ChestOriginEffectorPivotField,
    HeadEffectorPivotField,
    HipsEffectorPivotField,
    LeftAnkleEffectorPivotField,
    LeftElbowEffectorPivotField,
    LeftFootEffectorPivotField,
    LeftFootExtraFingerEffectorPivotField,
    LeftFootIndexEffectorPivotField,
    LeftFootMiddleEffectorPivotField,
    LeftFootPinkyEffectorPivotField,
    LeftFootRingEffectorPivotField,
    LeftFootThumbEffectorPivotField,
    LeftHandEffectorPivotField,
    LeftHandExtraFingerEffectorPivotField,
    LeftHandIndexEffectorPivotField,
    LeftHandMiddleEffectorPivotField,
    LeftHandPinkyEffectorPivotField,
    LeftHandRingEffectorPivotField,
    LeftHandThumbEffectorPivotField,
    LeftHipEffectorPivotField,
    LeftKneeEffectorPivotField,
    LeftShoulderEffectorPivotField,
    LeftWristEffectorPivotField,
    RightAnkleEffectorPivotField,
    RightElbowEffectorPivotField,
    RightFootEffectorPivotField,
    RightFootExtraFingerEffectorPivotField,
    RightFootIndexEffectorPivotField,
    RightFootMiddleEffectorPivotField,
    RightFootPinkyEffectorPivotField,
    RightFootRingEffectorPivotField,
    RightFootThumbEffectorPivotField,
    RightHandEffectorPivotField,
    RightHandExtraFingerEffectorPivotField,
    RightHandIndexEffectorPivotField,
    RightHandMiddleEffectorPivotField,
    RightHandPinkyEffectorPivotField,
    RightHandRingEffectorPivotField,
    RightHandThumbEffectorPivotField,
    RightHipEffectorPivotField,
    RightKneeEffectorPivotField,
    RightShoulderEffectorPivotField,
    RightWristEffectorPivotField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField


class HIKEffector2State(DG):
    __slots__ = ()

    NODE_TYPE = "HIKEffector2State"

    OutputEffectorState = TypedField()
    EFF = OutputEffectorState

    OutputEffectorStateNoAux = TypedField()
    EFFNA = OutputEffectorStateNoAux

    HipsEffectorGX = MatrixField(multi=True)

    HipsEffectorPivot = HipsEffectorPivotField(multi=True)

    HipsEffectorReachT = DoubleField(multi=True)

    HipsEffectorReachR = DoubleField(multi=True)

    HipsEffectorPull = DoubleField()

    HipsEffectorStiffness = DoubleField()

    LeftAnkleEffectorGX = MatrixField(multi=True)

    LeftAnkleEffectorPivot = LeftAnkleEffectorPivotField(multi=True)

    LeftAnkleEffectorReachT = DoubleField(multi=True)

    LeftAnkleEffectorReachR = DoubleField(multi=True)

    LeftAnkleEffectorPull = DoubleField()

    LeftAnkleEffectorStiffness = DoubleField()

    RightAnkleEffectorGX = MatrixField(multi=True)

    RightAnkleEffectorPivot = RightAnkleEffectorPivotField(multi=True)

    RightAnkleEffectorReachT = DoubleField(multi=True)

    RightAnkleEffectorReachR = DoubleField(multi=True)

    RightAnkleEffectorPull = DoubleField()

    RightAnkleEffectorStiffness = DoubleField()

    LeftWristEffectorGX = MatrixField(multi=True)

    LeftWristEffectorPivot = LeftWristEffectorPivotField(multi=True)

    LeftWristEffectorReachT = DoubleField(multi=True)

    LeftWristEffectorReachR = DoubleField(multi=True)

    LeftWristEffectorPull = DoubleField()

    LeftWristEffectorStiffness = DoubleField()

    RightWristEffectorGX = MatrixField(multi=True)

    RightWristEffectorPivot = RightWristEffectorPivotField(multi=True)

    RightWristEffectorReachT = DoubleField(multi=True)

    RightWristEffectorReachR = DoubleField(multi=True)

    RightWristEffectorPull = DoubleField()

    RightWristEffectorStiffness = DoubleField()

    LeftKneeEffectorGX = MatrixField(multi=True)

    LeftKneeEffectorPivot = LeftKneeEffectorPivotField(multi=True)

    LeftKneeEffectorReachT = DoubleField(multi=True)

    LeftKneeEffectorReachR = DoubleField(multi=True)

    LeftKneeEffectorPull = DoubleField()

    LeftKneeEffectorStiffness = DoubleField()

    RightKneeEffectorGX = MatrixField(multi=True)

    RightKneeEffectorPivot = RightKneeEffectorPivotField(multi=True)

    RightKneeEffectorReachT = DoubleField(multi=True)

    RightKneeEffectorReachR = DoubleField(multi=True)

    RightKneeEffectorPull = DoubleField()

    RightKneeEffectorStiffness = DoubleField()

    LeftElbowEffectorGX = MatrixField(multi=True)

    LeftElbowEffectorPivot = LeftElbowEffectorPivotField(multi=True)

    LeftElbowEffectorReachT = DoubleField(multi=True)

    LeftElbowEffectorReachR = DoubleField(multi=True)

    LeftElbowEffectorPull = DoubleField()

    LeftElbowEffectorStiffness = DoubleField()

    RightElbowEffectorGX = MatrixField(multi=True)

    RightElbowEffectorPivot = RightElbowEffectorPivotField(multi=True)

    RightElbowEffectorReachT = DoubleField(multi=True)

    RightElbowEffectorReachR = DoubleField(multi=True)

    RightElbowEffectorPull = DoubleField()

    RightElbowEffectorStiffness = DoubleField()

    ChestOriginEffectorGX = MatrixField(multi=True)

    ChestOriginEffectorPivot = ChestOriginEffectorPivotField(multi=True)

    ChestOriginEffectorReachT = DoubleField(multi=True)

    ChestOriginEffectorReachR = DoubleField(multi=True)

    ChestOriginEffectorPull = DoubleField()

    ChestOriginEffectorStiffness = DoubleField()

    ChestEndEffectorGX = MatrixField(multi=True)

    ChestEndEffectorPivot = ChestEndEffectorPivotField(multi=True)

    ChestEndEffectorReachT = DoubleField(multi=True)

    ChestEndEffectorReachR = DoubleField(multi=True)

    ChestEndEffectorPull = DoubleField()

    ChestEndEffectorStiffness = DoubleField()

    LeftFootEffectorGX = MatrixField(multi=True)

    LeftFootEffectorPivot = LeftFootEffectorPivotField(multi=True)

    LeftFootEffectorReachT = DoubleField(multi=True)

    LeftFootEffectorReachR = DoubleField(multi=True)

    LeftFootEffectorPull = DoubleField()

    LeftFootEffectorStiffness = DoubleField()

    RightFootEffectorGX = MatrixField(multi=True)

    RightFootEffectorPivot = RightFootEffectorPivotField(multi=True)

    RightFootEffectorReachT = DoubleField(multi=True)

    RightFootEffectorReachR = DoubleField(multi=True)

    RightFootEffectorPull = DoubleField()

    RightFootEffectorStiffness = DoubleField()

    LeftShoulderEffectorGX = MatrixField(multi=True)

    LeftShoulderEffectorPivot = LeftShoulderEffectorPivotField(multi=True)

    LeftShoulderEffectorReachT = DoubleField(multi=True)

    LeftShoulderEffectorReachR = DoubleField(multi=True)

    LeftShoulderEffectorPull = DoubleField()

    LeftShoulderEffectorStiffness = DoubleField()

    RightShoulderEffectorGX = MatrixField(multi=True)

    RightShoulderEffectorPivot = RightShoulderEffectorPivotField(multi=True)

    RightShoulderEffectorReachT = DoubleField(multi=True)

    RightShoulderEffectorReachR = DoubleField(multi=True)

    RightShoulderEffectorPull = DoubleField()

    RightShoulderEffectorStiffness = DoubleField()

    HeadEffectorGX = MatrixField(multi=True)

    HeadEffectorPivot = HeadEffectorPivotField(multi=True)

    HeadEffectorReachT = DoubleField(multi=True)

    HeadEffectorReachR = DoubleField(multi=True)

    HeadEffectorPull = DoubleField()

    HeadEffectorStiffness = DoubleField()

    LeftHipEffectorGX = MatrixField(multi=True)

    LeftHipEffectorPivot = LeftHipEffectorPivotField(multi=True)

    LeftHipEffectorReachT = DoubleField(multi=True)

    LeftHipEffectorReachR = DoubleField(multi=True)

    LeftHipEffectorPull = DoubleField()

    LeftHipEffectorStiffness = DoubleField()

    RightHipEffectorGX = MatrixField(multi=True)

    RightHipEffectorPivot = RightHipEffectorPivotField(multi=True)

    RightHipEffectorReachT = DoubleField(multi=True)

    RightHipEffectorReachR = DoubleField(multi=True)

    RightHipEffectorPull = DoubleField()

    RightHipEffectorStiffness = DoubleField()

    LeftHandEffectorGX = MatrixField(multi=True)

    LeftHandEffectorPivot = LeftHandEffectorPivotField(multi=True)

    LeftHandEffectorReachT = DoubleField(multi=True)

    LeftHandEffectorReachR = DoubleField(multi=True)

    LeftHandEffectorPull = DoubleField()

    LeftHandEffectorStiffness = DoubleField()

    RightHandEffectorGX = MatrixField(multi=True)

    RightHandEffectorPivot = RightHandEffectorPivotField(multi=True)

    RightHandEffectorReachT = DoubleField(multi=True)

    RightHandEffectorReachR = DoubleField(multi=True)

    RightHandEffectorPull = DoubleField()

    RightHandEffectorStiffness = DoubleField()

    LeftHandThumbEffectorGX = MatrixField(multi=True)

    LeftHandThumbEffectorPivot = LeftHandThumbEffectorPivotField(multi=True)

    LeftHandThumbEffectorReachT = DoubleField(multi=True)

    LeftHandThumbEffectorReachR = DoubleField(multi=True)

    LeftHandThumbEffectorPull = DoubleField()

    LeftHandThumbEffectorStiffness = DoubleField()

    LeftHandIndexEffectorGX = MatrixField(multi=True)

    LeftHandIndexEffectorPivot = LeftHandIndexEffectorPivotField(multi=True)

    LeftHandIndexEffectorReachT = DoubleField(multi=True)

    LeftHandIndexEffectorReachR = DoubleField(multi=True)

    LeftHandIndexEffectorPull = DoubleField()

    LeftHandIndexEffectorStiffness = DoubleField()

    LeftHandMiddleEffectorGX = MatrixField(multi=True)

    LeftHandMiddleEffectorPivot = LeftHandMiddleEffectorPivotField(multi=True)

    LeftHandMiddleEffectorReachT = DoubleField(multi=True)

    LeftHandMiddleEffectorReachR = DoubleField(multi=True)

    LeftHandMiddleEffectorPull = DoubleField()

    LeftHandMiddleEffectorStiffness = DoubleField()

    LeftHandRingEffectorGX = MatrixField(multi=True)

    LeftHandRingEffectorPivot = LeftHandRingEffectorPivotField(multi=True)

    LeftHandRingEffectorReachT = DoubleField(multi=True)

    LeftHandRingEffectorReachR = DoubleField(multi=True)

    LeftHandRingEffectorPull = DoubleField()

    LeftHandRingEffectorStiffness = DoubleField()

    LeftHandPinkyEffectorGX = MatrixField(multi=True)

    LeftHandPinkyEffectorPivot = LeftHandPinkyEffectorPivotField(multi=True)

    LeftHandPinkyEffectorReachT = DoubleField(multi=True)

    LeftHandPinkyEffectorReachR = DoubleField(multi=True)

    LeftHandPinkyEffectorPull = DoubleField()

    LeftHandPinkyEffectorStiffness = DoubleField()

    LeftHandExtraFingerEffectorGX = MatrixField(multi=True)

    LeftHandExtraFingerEffectorPivot = LeftHandExtraFingerEffectorPivotField(multi=True)

    LeftHandExtraFingerEffectorReachT = DoubleField(multi=True)

    LeftHandExtraFingerEffectorReachR = DoubleField(multi=True)

    LeftHandExtraFingerEffectorPull = DoubleField()

    LeftHandExtraFingerEffectorStiffness = DoubleField()

    RightHandThumbEffectorGX = MatrixField(multi=True)

    RightHandThumbEffectorPivot = RightHandThumbEffectorPivotField(multi=True)

    RightHandThumbEffectorReachT = DoubleField(multi=True)

    RightHandThumbEffectorReachR = DoubleField(multi=True)

    RightHandThumbEffectorPull = DoubleField()

    RightHandThumbEffectorStiffness = DoubleField()

    RightHandIndexEffectorGX = MatrixField(multi=True)

    RightHandIndexEffectorPivot = RightHandIndexEffectorPivotField(multi=True)

    RightHandIndexEffectorReachT = DoubleField(multi=True)

    RightHandIndexEffectorReachR = DoubleField(multi=True)

    RightHandIndexEffectorPull = DoubleField()

    RightHandIndexEffectorStiffness = DoubleField()

    RightHandMiddleEffectorGX = MatrixField(multi=True)

    RightHandMiddleEffectorPivot = RightHandMiddleEffectorPivotField(multi=True)

    RightHandMiddleEffectorReachT = DoubleField(multi=True)

    RightHandMiddleEffectorReachR = DoubleField(multi=True)

    RightHandMiddleEffectorPull = DoubleField()

    RightHandMiddleEffectorStiffness = DoubleField()

    RightHandRingEffectorGX = MatrixField(multi=True)

    RightHandRingEffectorPivot = RightHandRingEffectorPivotField(multi=True)

    RightHandRingEffectorReachT = DoubleField(multi=True)

    RightHandRingEffectorReachR = DoubleField(multi=True)

    RightHandRingEffectorPull = DoubleField()

    RightHandRingEffectorStiffness = DoubleField()

    RightHandPinkyEffectorGX = MatrixField(multi=True)

    RightHandPinkyEffectorPivot = RightHandPinkyEffectorPivotField(multi=True)

    RightHandPinkyEffectorReachT = DoubleField(multi=True)

    RightHandPinkyEffectorReachR = DoubleField(multi=True)

    RightHandPinkyEffectorPull = DoubleField()

    RightHandPinkyEffectorStiffness = DoubleField()

    RightHandExtraFingerEffectorGX = MatrixField(multi=True)

    RightHandExtraFingerEffectorPivot = RightHandExtraFingerEffectorPivotField(multi=True)

    RightHandExtraFingerEffectorReachT = DoubleField(multi=True)

    RightHandExtraFingerEffectorReachR = DoubleField(multi=True)

    RightHandExtraFingerEffectorPull = DoubleField()

    RightHandExtraFingerEffectorStiffness = DoubleField()

    LeftFootThumbEffectorGX = MatrixField(multi=True)

    LeftFootThumbEffectorPivot = LeftFootThumbEffectorPivotField(multi=True)

    LeftFootThumbEffectorReachT = DoubleField(multi=True)

    LeftFootThumbEffectorReachR = DoubleField(multi=True)

    LeftFootThumbEffectorPull = DoubleField()

    LeftFootThumbEffectorStiffness = DoubleField()

    LeftFootIndexEffectorGX = MatrixField(multi=True)

    LeftFootIndexEffectorPivot = LeftFootIndexEffectorPivotField(multi=True)

    LeftFootIndexEffectorReachT = DoubleField(multi=True)

    LeftFootIndexEffectorReachR = DoubleField(multi=True)

    LeftFootIndexEffectorPull = DoubleField()

    LeftFootIndexEffectorStiffness = DoubleField()

    LeftFootMiddleEffectorGX = MatrixField(multi=True)

    LeftFootMiddleEffectorPivot = LeftFootMiddleEffectorPivotField(multi=True)

    LeftFootMiddleEffectorReachT = DoubleField(multi=True)

    LeftFootMiddleEffectorReachR = DoubleField(multi=True)

    LeftFootMiddleEffectorPull = DoubleField()

    LeftFootMiddleEffectorStiffness = DoubleField()

    LeftFootRingEffectorGX = MatrixField(multi=True)

    LeftFootRingEffectorPivot = LeftFootRingEffectorPivotField(multi=True)

    LeftFootRingEffectorReachT = DoubleField(multi=True)

    LeftFootRingEffectorReachR = DoubleField(multi=True)

    LeftFootRingEffectorPull = DoubleField()

    LeftFootRingEffectorStiffness = DoubleField()

    LeftFootPinkyEffectorGX = MatrixField(multi=True)

    LeftFootPinkyEffectorPivot = LeftFootPinkyEffectorPivotField(multi=True)

    LeftFootPinkyEffectorReachT = DoubleField(multi=True)

    LeftFootPinkyEffectorReachR = DoubleField(multi=True)

    LeftFootPinkyEffectorPull = DoubleField()

    LeftFootPinkyEffectorStiffness = DoubleField()

    LeftFootExtraFingerEffectorGX = MatrixField(multi=True)

    LeftFootExtraFingerEffectorPivot = LeftFootExtraFingerEffectorPivotField(multi=True)

    LeftFootExtraFingerEffectorReachT = DoubleField(multi=True)

    LeftFootExtraFingerEffectorReachR = DoubleField(multi=True)

    LeftFootExtraFingerEffectorPull = DoubleField()

    LeftFootExtraFingerEffectorStiffness = DoubleField()

    RightFootThumbEffectorGX = MatrixField(multi=True)

    RightFootThumbEffectorPivot = RightFootThumbEffectorPivotField(multi=True)

    RightFootThumbEffectorReachT = DoubleField(multi=True)

    RightFootThumbEffectorReachR = DoubleField(multi=True)

    RightFootThumbEffectorPull = DoubleField()

    RightFootThumbEffectorStiffness = DoubleField()

    RightFootIndexEffectorGX = MatrixField(multi=True)

    RightFootIndexEffectorPivot = RightFootIndexEffectorPivotField(multi=True)

    RightFootIndexEffectorReachT = DoubleField(multi=True)

    RightFootIndexEffectorReachR = DoubleField(multi=True)

    RightFootIndexEffectorPull = DoubleField()

    RightFootIndexEffectorStiffness = DoubleField()

    RightFootMiddleEffectorGX = MatrixField(multi=True)

    RightFootMiddleEffectorPivot = RightFootMiddleEffectorPivotField(multi=True)

    RightFootMiddleEffectorReachT = DoubleField(multi=True)

    RightFootMiddleEffectorReachR = DoubleField(multi=True)

    RightFootMiddleEffectorPull = DoubleField()

    RightFootMiddleEffectorStiffness = DoubleField()

    RightFootRingEffectorGX = MatrixField(multi=True)

    RightFootRingEffectorPivot = RightFootRingEffectorPivotField(multi=True)

    RightFootRingEffectorReachT = DoubleField(multi=True)

    RightFootRingEffectorReachR = DoubleField(multi=True)

    RightFootRingEffectorPull = DoubleField()

    RightFootRingEffectorStiffness = DoubleField()

    RightFootPinkyEffectorGX = MatrixField(multi=True)

    RightFootPinkyEffectorPivot = RightFootPinkyEffectorPivotField(multi=True)

    RightFootPinkyEffectorReachT = DoubleField(multi=True)

    RightFootPinkyEffectorReachR = DoubleField(multi=True)

    RightFootPinkyEffectorPull = DoubleField()

    RightFootPinkyEffectorStiffness = DoubleField()

    RightFootExtraFingerEffectorGX = MatrixField(multi=True)

    RightFootExtraFingerEffectorPivot = RightFootExtraFingerEffectorPivotField(multi=True)

    RightFootExtraFingerEffectorReachT = DoubleField(multi=True)

    RightFootExtraFingerEffectorReachR = DoubleField(multi=True)

    RightFootExtraFingerEffectorPull = DoubleField()

    RightFootExtraFingerEffectorStiffness = DoubleField()

    leftHandFloorGX = MatrixField()

    rightHandFloorGX = MatrixField()

    leftFootFloorGX = MatrixField()

    rightFootFloorGX = MatrixField()
