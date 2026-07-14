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

    HipsEffectorPivot = HipsEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    HipsEffectorReachT = DoubleField(multi=True, default_value=0.0)

    HipsEffectorReachR = DoubleField(multi=True, default_value=0.0)

    HipsEffectorPull = DoubleField(default_value=0.0)

    HipsEffectorStiffness = DoubleField(default_value=0.0)

    LeftAnkleEffectorGX = MatrixField(multi=True)

    LeftAnkleEffectorPivot = LeftAnkleEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftAnkleEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftAnkleEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftAnkleEffectorPull = DoubleField(default_value=0.0)

    LeftAnkleEffectorStiffness = DoubleField(default_value=0.0)

    RightAnkleEffectorGX = MatrixField(multi=True)

    RightAnkleEffectorPivot = RightAnkleEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightAnkleEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightAnkleEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightAnkleEffectorPull = DoubleField(default_value=0.0)

    RightAnkleEffectorStiffness = DoubleField(default_value=0.0)

    LeftWristEffectorGX = MatrixField(multi=True)

    LeftWristEffectorPivot = LeftWristEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftWristEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftWristEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftWristEffectorPull = DoubleField(default_value=0.0)

    LeftWristEffectorStiffness = DoubleField(default_value=0.0)

    RightWristEffectorGX = MatrixField(multi=True)

    RightWristEffectorPivot = RightWristEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightWristEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightWristEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightWristEffectorPull = DoubleField(default_value=0.0)

    RightWristEffectorStiffness = DoubleField(default_value=0.0)

    LeftKneeEffectorGX = MatrixField(multi=True)

    LeftKneeEffectorPivot = LeftKneeEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftKneeEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftKneeEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftKneeEffectorPull = DoubleField(default_value=0.0)

    LeftKneeEffectorStiffness = DoubleField(default_value=0.0)

    RightKneeEffectorGX = MatrixField(multi=True)

    RightKneeEffectorPivot = RightKneeEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightKneeEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightKneeEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightKneeEffectorPull = DoubleField(default_value=0.0)

    RightKneeEffectorStiffness = DoubleField(default_value=0.0)

    LeftElbowEffectorGX = MatrixField(multi=True)

    LeftElbowEffectorPivot = LeftElbowEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftElbowEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftElbowEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftElbowEffectorPull = DoubleField(default_value=0.0)

    LeftElbowEffectorStiffness = DoubleField(default_value=0.0)

    RightElbowEffectorGX = MatrixField(multi=True)

    RightElbowEffectorPivot = RightElbowEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightElbowEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightElbowEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightElbowEffectorPull = DoubleField(default_value=0.0)

    RightElbowEffectorStiffness = DoubleField(default_value=0.0)

    ChestOriginEffectorGX = MatrixField(multi=True)

    ChestOriginEffectorPivot = ChestOriginEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    ChestOriginEffectorReachT = DoubleField(multi=True, default_value=0.0)

    ChestOriginEffectorReachR = DoubleField(multi=True, default_value=0.0)

    ChestOriginEffectorPull = DoubleField(default_value=0.0)

    ChestOriginEffectorStiffness = DoubleField(default_value=0.0)

    ChestEndEffectorGX = MatrixField(multi=True)

    ChestEndEffectorPivot = ChestEndEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    ChestEndEffectorReachT = DoubleField(multi=True, default_value=0.0)

    ChestEndEffectorReachR = DoubleField(multi=True, default_value=0.0)

    ChestEndEffectorPull = DoubleField(default_value=0.0)

    ChestEndEffectorStiffness = DoubleField(default_value=0.0)

    LeftFootEffectorGX = MatrixField(multi=True)

    LeftFootEffectorPivot = LeftFootEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftFootEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftFootEffectorPull = DoubleField(default_value=0.0)

    LeftFootEffectorStiffness = DoubleField(default_value=0.0)

    RightFootEffectorGX = MatrixField(multi=True)

    RightFootEffectorPivot = RightFootEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightFootEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightFootEffectorPull = DoubleField(default_value=0.0)

    RightFootEffectorStiffness = DoubleField(default_value=0.0)

    LeftShoulderEffectorGX = MatrixField(multi=True)

    LeftShoulderEffectorPivot = LeftShoulderEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftShoulderEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftShoulderEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftShoulderEffectorPull = DoubleField(default_value=0.0)

    LeftShoulderEffectorStiffness = DoubleField(default_value=0.0)

    RightShoulderEffectorGX = MatrixField(multi=True)

    RightShoulderEffectorPivot = RightShoulderEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightShoulderEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightShoulderEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightShoulderEffectorPull = DoubleField(default_value=0.0)

    RightShoulderEffectorStiffness = DoubleField(default_value=0.0)

    HeadEffectorGX = MatrixField(multi=True)

    HeadEffectorPivot = HeadEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    HeadEffectorReachT = DoubleField(multi=True, default_value=0.0)

    HeadEffectorReachR = DoubleField(multi=True, default_value=0.0)

    HeadEffectorPull = DoubleField(default_value=0.0)

    HeadEffectorStiffness = DoubleField(default_value=0.0)

    LeftHipEffectorGX = MatrixField(multi=True)

    LeftHipEffectorPivot = LeftHipEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHipEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftHipEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftHipEffectorPull = DoubleField(default_value=0.0)

    LeftHipEffectorStiffness = DoubleField(default_value=0.0)

    RightHipEffectorGX = MatrixField(multi=True)

    RightHipEffectorPivot = RightHipEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHipEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightHipEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightHipEffectorPull = DoubleField(default_value=0.0)

    RightHipEffectorStiffness = DoubleField(default_value=0.0)

    LeftHandEffectorGX = MatrixField(multi=True)

    LeftHandEffectorPivot = LeftHandEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftHandEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftHandEffectorPull = DoubleField(default_value=0.0)

    LeftHandEffectorStiffness = DoubleField(default_value=0.0)

    RightHandEffectorGX = MatrixField(multi=True)

    RightHandEffectorPivot = RightHandEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightHandEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightHandEffectorPull = DoubleField(default_value=0.0)

    RightHandEffectorStiffness = DoubleField(default_value=0.0)

    LeftHandThumbEffectorGX = MatrixField(multi=True)

    LeftHandThumbEffectorPivot = LeftHandThumbEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandThumbEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftHandThumbEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftHandThumbEffectorPull = DoubleField(default_value=0.0)

    LeftHandThumbEffectorStiffness = DoubleField(default_value=0.0)

    LeftHandIndexEffectorGX = MatrixField(multi=True)

    LeftHandIndexEffectorPivot = LeftHandIndexEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandIndexEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftHandIndexEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftHandIndexEffectorPull = DoubleField(default_value=0.0)

    LeftHandIndexEffectorStiffness = DoubleField(default_value=0.0)

    LeftHandMiddleEffectorGX = MatrixField(multi=True)

    LeftHandMiddleEffectorPivot = LeftHandMiddleEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandMiddleEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftHandMiddleEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftHandMiddleEffectorPull = DoubleField(default_value=0.0)

    LeftHandMiddleEffectorStiffness = DoubleField(default_value=0.0)

    LeftHandRingEffectorGX = MatrixField(multi=True)

    LeftHandRingEffectorPivot = LeftHandRingEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandRingEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftHandRingEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftHandRingEffectorPull = DoubleField(default_value=0.0)

    LeftHandRingEffectorStiffness = DoubleField(default_value=0.0)

    LeftHandPinkyEffectorGX = MatrixField(multi=True)

    LeftHandPinkyEffectorPivot = LeftHandPinkyEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandPinkyEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftHandPinkyEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftHandPinkyEffectorPull = DoubleField(default_value=0.0)

    LeftHandPinkyEffectorStiffness = DoubleField(default_value=0.0)

    LeftHandExtraFingerEffectorGX = MatrixField(multi=True)

    LeftHandExtraFingerEffectorPivot = LeftHandExtraFingerEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftHandExtraFingerEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftHandExtraFingerEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftHandExtraFingerEffectorPull = DoubleField(default_value=0.0)

    LeftHandExtraFingerEffectorStiffness = DoubleField(default_value=0.0)

    RightHandThumbEffectorGX = MatrixField(multi=True)

    RightHandThumbEffectorPivot = RightHandThumbEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandThumbEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightHandThumbEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightHandThumbEffectorPull = DoubleField(default_value=0.0)

    RightHandThumbEffectorStiffness = DoubleField(default_value=0.0)

    RightHandIndexEffectorGX = MatrixField(multi=True)

    RightHandIndexEffectorPivot = RightHandIndexEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandIndexEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightHandIndexEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightHandIndexEffectorPull = DoubleField(default_value=0.0)

    RightHandIndexEffectorStiffness = DoubleField(default_value=0.0)

    RightHandMiddleEffectorGX = MatrixField(multi=True)

    RightHandMiddleEffectorPivot = RightHandMiddleEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandMiddleEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightHandMiddleEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightHandMiddleEffectorPull = DoubleField(default_value=0.0)

    RightHandMiddleEffectorStiffness = DoubleField(default_value=0.0)

    RightHandRingEffectorGX = MatrixField(multi=True)

    RightHandRingEffectorPivot = RightHandRingEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandRingEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightHandRingEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightHandRingEffectorPull = DoubleField(default_value=0.0)

    RightHandRingEffectorStiffness = DoubleField(default_value=0.0)

    RightHandPinkyEffectorGX = MatrixField(multi=True)

    RightHandPinkyEffectorPivot = RightHandPinkyEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandPinkyEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightHandPinkyEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightHandPinkyEffectorPull = DoubleField(default_value=0.0)

    RightHandPinkyEffectorStiffness = DoubleField(default_value=0.0)

    RightHandExtraFingerEffectorGX = MatrixField(multi=True)

    RightHandExtraFingerEffectorPivot = RightHandExtraFingerEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightHandExtraFingerEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightHandExtraFingerEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightHandExtraFingerEffectorPull = DoubleField(default_value=0.0)

    RightHandExtraFingerEffectorStiffness = DoubleField(default_value=0.0)

    LeftFootThumbEffectorGX = MatrixField(multi=True)

    LeftFootThumbEffectorPivot = LeftFootThumbEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootThumbEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftFootThumbEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftFootThumbEffectorPull = DoubleField(default_value=0.0)

    LeftFootThumbEffectorStiffness = DoubleField(default_value=0.0)

    LeftFootIndexEffectorGX = MatrixField(multi=True)

    LeftFootIndexEffectorPivot = LeftFootIndexEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootIndexEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftFootIndexEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftFootIndexEffectorPull = DoubleField(default_value=0.0)

    LeftFootIndexEffectorStiffness = DoubleField(default_value=0.0)

    LeftFootMiddleEffectorGX = MatrixField(multi=True)

    LeftFootMiddleEffectorPivot = LeftFootMiddleEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootMiddleEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftFootMiddleEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftFootMiddleEffectorPull = DoubleField(default_value=0.0)

    LeftFootMiddleEffectorStiffness = DoubleField(default_value=0.0)

    LeftFootRingEffectorGX = MatrixField(multi=True)

    LeftFootRingEffectorPivot = LeftFootRingEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootRingEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftFootRingEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftFootRingEffectorPull = DoubleField(default_value=0.0)

    LeftFootRingEffectorStiffness = DoubleField(default_value=0.0)

    LeftFootPinkyEffectorGX = MatrixField(multi=True)

    LeftFootPinkyEffectorPivot = LeftFootPinkyEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootPinkyEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftFootPinkyEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftFootPinkyEffectorPull = DoubleField(default_value=0.0)

    LeftFootPinkyEffectorStiffness = DoubleField(default_value=0.0)

    LeftFootExtraFingerEffectorGX = MatrixField(multi=True)

    LeftFootExtraFingerEffectorPivot = LeftFootExtraFingerEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    LeftFootExtraFingerEffectorReachT = DoubleField(multi=True, default_value=0.0)

    LeftFootExtraFingerEffectorReachR = DoubleField(multi=True, default_value=0.0)

    LeftFootExtraFingerEffectorPull = DoubleField(default_value=0.0)

    LeftFootExtraFingerEffectorStiffness = DoubleField(default_value=0.0)

    RightFootThumbEffectorGX = MatrixField(multi=True)

    RightFootThumbEffectorPivot = RightFootThumbEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootThumbEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightFootThumbEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightFootThumbEffectorPull = DoubleField(default_value=0.0)

    RightFootThumbEffectorStiffness = DoubleField(default_value=0.0)

    RightFootIndexEffectorGX = MatrixField(multi=True)

    RightFootIndexEffectorPivot = RightFootIndexEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootIndexEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightFootIndexEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightFootIndexEffectorPull = DoubleField(default_value=0.0)

    RightFootIndexEffectorStiffness = DoubleField(default_value=0.0)

    RightFootMiddleEffectorGX = MatrixField(multi=True)

    RightFootMiddleEffectorPivot = RightFootMiddleEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootMiddleEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightFootMiddleEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightFootMiddleEffectorPull = DoubleField(default_value=0.0)

    RightFootMiddleEffectorStiffness = DoubleField(default_value=0.0)

    RightFootRingEffectorGX = MatrixField(multi=True)

    RightFootRingEffectorPivot = RightFootRingEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootRingEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightFootRingEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightFootRingEffectorPull = DoubleField(default_value=0.0)

    RightFootRingEffectorStiffness = DoubleField(default_value=0.0)

    RightFootPinkyEffectorGX = MatrixField(multi=True)

    RightFootPinkyEffectorPivot = RightFootPinkyEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootPinkyEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightFootPinkyEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightFootPinkyEffectorPull = DoubleField(default_value=0.0)

    RightFootPinkyEffectorStiffness = DoubleField(default_value=0.0)

    RightFootExtraFingerEffectorGX = MatrixField(multi=True)

    RightFootExtraFingerEffectorPivot = RightFootExtraFingerEffectorPivotField(multi=True, default_value=(0.0, 0.0, 0.0))

    RightFootExtraFingerEffectorReachT = DoubleField(multi=True, default_value=0.0)

    RightFootExtraFingerEffectorReachR = DoubleField(multi=True, default_value=0.0)

    RightFootExtraFingerEffectorPull = DoubleField(default_value=0.0)

    RightFootExtraFingerEffectorStiffness = DoubleField(default_value=0.0)

    leftHandFloorGX = MatrixField()

    rightHandFloorGX = MatrixField()

    leftFootFloorGX = MatrixField()

    rightFootFloorGX = MatrixField()
