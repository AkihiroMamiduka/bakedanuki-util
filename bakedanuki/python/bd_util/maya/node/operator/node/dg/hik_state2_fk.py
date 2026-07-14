# coding: utf-8
from ._core import DG
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.typed import TypedField


class HIKState2FK(DG):
    __slots__ = ()

    NODE_TYPE = "HIKState2FK"

    InputCharacterState = TypedField()

    InputCharacterDefinition = TypedField()

    ReferenceGX = MatrixField()

    HipsGX = MatrixField()

    LeftUpLegGX = MatrixField()

    LeftLegGX = MatrixField()

    LeftFootGX = MatrixField()

    RightUpLegGX = MatrixField()

    RightLegGX = MatrixField()

    RightFootGX = MatrixField()

    SpineGX = MatrixField()

    LeftArmGX = MatrixField()

    LeftForeArmGX = MatrixField()

    LeftHandGX = MatrixField()

    RightArmGX = MatrixField()

    RightForeArmGX = MatrixField()

    RightHandGX = MatrixField()

    HeadGX = MatrixField()

    LeftToeBaseGX = MatrixField()

    RightToeBaseGX = MatrixField()

    LeftShoulderGX = MatrixField()

    RightShoulderGX = MatrixField()

    NeckGX = MatrixField()

    LeftFingerBaseGX = MatrixField()

    RightFingerBaseGX = MatrixField()

    Spine1GX = MatrixField()

    Spine2GX = MatrixField()

    Spine3GX = MatrixField()

    Spine4GX = MatrixField()

    Spine5GX = MatrixField()

    Spine6GX = MatrixField()

    Spine7GX = MatrixField()

    Spine8GX = MatrixField()

    Spine9GX = MatrixField()

    Neck1GX = MatrixField()

    Neck2GX = MatrixField()

    Neck3GX = MatrixField()

    Neck4GX = MatrixField()

    Neck5GX = MatrixField()

    Neck6GX = MatrixField()

    Neck7GX = MatrixField()

    Neck8GX = MatrixField()

    Neck9GX = MatrixField()

    LeftUpLegRollGX = MatrixField()

    LeftLegRollGX = MatrixField()

    RightUpLegRollGX = MatrixField()

    RightLegRollGX = MatrixField()

    LeftArmRollGX = MatrixField()

    LeftForeArmRollGX = MatrixField()

    RightArmRollGX = MatrixField()

    RightForeArmRollGX = MatrixField()

    HipsTranslationGX = MatrixField()

    LeftHandThumb1GX = MatrixField()

    LeftHandThumb2GX = MatrixField()

    LeftHandThumb3GX = MatrixField()

    LeftHandThumb4GX = MatrixField()

    LeftHandIndex1GX = MatrixField()

    LeftHandIndex2GX = MatrixField()

    LeftHandIndex3GX = MatrixField()

    LeftHandIndex4GX = MatrixField()

    LeftHandMiddle1GX = MatrixField()

    LeftHandMiddle2GX = MatrixField()

    LeftHandMiddle3GX = MatrixField()

    LeftHandMiddle4GX = MatrixField()

    LeftHandRing1GX = MatrixField()

    LeftHandRing2GX = MatrixField()

    LeftHandRing3GX = MatrixField()

    LeftHandRing4GX = MatrixField()

    LeftHandPinky1GX = MatrixField()

    LeftHandPinky2GX = MatrixField()

    LeftHandPinky3GX = MatrixField()

    LeftHandPinky4GX = MatrixField()

    LeftHandExtraFinger1GX = MatrixField()

    LeftHandExtraFinger2GX = MatrixField()

    LeftHandExtraFinger3GX = MatrixField()

    LeftHandExtraFinger4GX = MatrixField()

    RightHandThumb1GX = MatrixField()

    RightHandThumb2GX = MatrixField()

    RightHandThumb3GX = MatrixField()

    RightHandThumb4GX = MatrixField()

    RightHandIndex1GX = MatrixField()

    RightHandIndex2GX = MatrixField()

    RightHandIndex3GX = MatrixField()

    RightHandIndex4GX = MatrixField()

    RightHandMiddle1GX = MatrixField()

    RightHandMiddle2GX = MatrixField()

    RightHandMiddle3GX = MatrixField()

    RightHandMiddle4GX = MatrixField()

    RightHandRing1GX = MatrixField()

    RightHandRing2GX = MatrixField()

    RightHandRing3GX = MatrixField()

    RightHandRing4GX = MatrixField()

    RightHandPinky1GX = MatrixField()

    RightHandPinky2GX = MatrixField()

    RightHandPinky3GX = MatrixField()

    RightHandPinky4GX = MatrixField()

    RightHandExtraFinger1GX = MatrixField()

    RightHandExtraFinger2GX = MatrixField()

    RightHandExtraFinger3GX = MatrixField()

    RightHandExtraFinger4GX = MatrixField()

    LeftFootThumb1GX = MatrixField()

    LeftFootThumb2GX = MatrixField()

    LeftFootThumb3GX = MatrixField()

    LeftFootThumb4GX = MatrixField()

    LeftFootIndex1GX = MatrixField()

    LeftFootIndex2GX = MatrixField()

    LeftFootIndex3GX = MatrixField()

    LeftFootIndex4GX = MatrixField()

    LeftFootMiddle1GX = MatrixField()

    LeftFootMiddle2GX = MatrixField()

    LeftFootMiddle3GX = MatrixField()

    LeftFootMiddle4GX = MatrixField()

    LeftFootRing1GX = MatrixField()

    LeftFootRing2GX = MatrixField()

    LeftFootRing3GX = MatrixField()

    LeftFootRing4GX = MatrixField()

    LeftFootPinky1GX = MatrixField()

    LeftFootPinky2GX = MatrixField()

    LeftFootPinky3GX = MatrixField()

    LeftFootPinky4GX = MatrixField()

    LeftFootExtraFinger1GX = MatrixField()

    LeftFootExtraFinger2GX = MatrixField()

    LeftFootExtraFinger3GX = MatrixField()

    LeftFootExtraFinger4GX = MatrixField()

    RightFootThumb1GX = MatrixField()

    RightFootThumb2GX = MatrixField()

    RightFootThumb3GX = MatrixField()

    RightFootThumb4GX = MatrixField()

    RightFootIndex1GX = MatrixField()

    RightFootIndex2GX = MatrixField()

    RightFootIndex3GX = MatrixField()

    RightFootIndex4GX = MatrixField()

    RightFootMiddle1GX = MatrixField()

    RightFootMiddle2GX = MatrixField()

    RightFootMiddle3GX = MatrixField()

    RightFootMiddle4GX = MatrixField()

    RightFootRing1GX = MatrixField()

    RightFootRing2GX = MatrixField()

    RightFootRing3GX = MatrixField()

    RightFootRing4GX = MatrixField()

    RightFootPinky1GX = MatrixField()

    RightFootPinky2GX = MatrixField()

    RightFootPinky3GX = MatrixField()

    RightFootPinky4GX = MatrixField()

    RightFootExtraFinger1GX = MatrixField()

    RightFootExtraFinger2GX = MatrixField()

    RightFootExtraFinger3GX = MatrixField()

    RightFootExtraFinger4GX = MatrixField()

    LeftInHandThumbGX = MatrixField()

    LeftInHandIndexGX = MatrixField()

    LeftInHandMiddleGX = MatrixField()

    LeftInHandRingGX = MatrixField()

    LeftInHandPinkyGX = MatrixField()

    LeftInHandExtraFingerGX = MatrixField()

    RightInHandThumbGX = MatrixField()

    RightInHandIndexGX = MatrixField()

    RightInHandMiddleGX = MatrixField()

    RightInHandRingGX = MatrixField()

    RightInHandPinkyGX = MatrixField()

    RightInHandExtraFingerGX = MatrixField()

    LeftInFootThumbGX = MatrixField()

    LeftInFootIndexGX = MatrixField()

    LeftInFootMiddleGX = MatrixField()

    LeftInFootRingGX = MatrixField()

    LeftInFootPinkyGX = MatrixField()

    LeftInFootExtraFingerGX = MatrixField()

    RightInFootThumbGX = MatrixField()

    RightInFootIndexGX = MatrixField()

    RightInFootMiddleGX = MatrixField()

    RightInFootRingGX = MatrixField()

    RightInFootPinkyGX = MatrixField()

    RightInFootExtraFingerGX = MatrixField()

    LeftShoulderExtraGX = MatrixField()

    RightShoulderExtraGX = MatrixField()

    LeafLeftUpLegRoll1GX = MatrixField()

    LeafLeftLegRoll1GX = MatrixField()

    LeafRightUpLegRoll1GX = MatrixField()

    LeafRightLegRoll1GX = MatrixField()

    LeafLeftArmRoll1GX = MatrixField()

    LeafLeftForeArmRoll1GX = MatrixField()

    LeafRightArmRoll1GX = MatrixField()

    LeafRightForeArmRoll1GX = MatrixField()

    LeafLeftUpLegRoll2GX = MatrixField()

    LeafLeftLegRoll2GX = MatrixField()

    LeafRightUpLegRoll2GX = MatrixField()

    LeafRightLegRoll2GX = MatrixField()

    LeafLeftArmRoll2GX = MatrixField()

    LeafLeftForeArmRoll2GX = MatrixField()

    LeafRightArmRoll2GX = MatrixField()

    LeafRightForeArmRoll2GX = MatrixField()

    LeafLeftUpLegRoll3GX = MatrixField()

    LeafLeftLegRoll3GX = MatrixField()

    LeafRightUpLegRoll3GX = MatrixField()

    LeafRightLegRoll3GX = MatrixField()

    LeafLeftArmRoll3GX = MatrixField()

    LeafLeftForeArmRoll3GX = MatrixField()

    LeafRightArmRoll3GX = MatrixField()

    LeafRightForeArmRoll3GX = MatrixField()

    LeafLeftUpLegRoll4GX = MatrixField()

    LeafLeftLegRoll4GX = MatrixField()

    LeafRightUpLegRoll4GX = MatrixField()

    LeafRightLegRoll4GX = MatrixField()

    LeafLeftArmRoll4GX = MatrixField()

    LeafLeftForeArmRoll4GX = MatrixField()

    LeafRightArmRoll4GX = MatrixField()

    LeafRightForeArmRoll4GX = MatrixField()

    LeafLeftUpLegRoll5GX = MatrixField()

    LeafLeftLegRoll5GX = MatrixField()

    LeafRightUpLegRoll5GX = MatrixField()

    LeafRightLegRoll5GX = MatrixField()

    LeafLeftArmRoll5GX = MatrixField()

    LeafLeftForeArmRoll5GX = MatrixField()

    LeafRightArmRoll5GX = MatrixField()

    LeafRightForeArmRoll5GX = MatrixField()
