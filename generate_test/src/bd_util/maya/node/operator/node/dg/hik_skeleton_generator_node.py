# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hik_skeleton_generator_node import (
    HeadRField,
    HeadSField,
    HeadTField,
    HipsRField,
    HipsSField,
    HipsTField,
    HipsTranslationRField,
    HipsTranslationSField,
    HipsTranslationTField,
    LeafLeftArmRoll1RField,
    LeafLeftArmRoll1SField,
    LeafLeftArmRoll1TField,
    LeafLeftArmRoll2RField,
    LeafLeftArmRoll2SField,
    LeafLeftArmRoll2TField,
    LeafLeftArmRoll3RField,
    LeafLeftArmRoll3SField,
    LeafLeftArmRoll3TField,
    LeafLeftArmRoll4RField,
    LeafLeftArmRoll4SField,
    LeafLeftArmRoll4TField,
    LeafLeftArmRoll5RField,
    LeafLeftArmRoll5SField,
    LeafLeftArmRoll5TField,
    LeafLeftForeArmRoll1RField,
    LeafLeftForeArmRoll1SField,
    LeafLeftForeArmRoll1TField,
    LeafLeftForeArmRoll2RField,
    LeafLeftForeArmRoll2SField,
    LeafLeftForeArmRoll2TField,
    LeafLeftForeArmRoll3RField,
    LeafLeftForeArmRoll3SField,
    LeafLeftForeArmRoll3TField,
    LeafLeftForeArmRoll4RField,
    LeafLeftForeArmRoll4SField,
    LeafLeftForeArmRoll4TField,
    LeafLeftForeArmRoll5RField,
    LeafLeftForeArmRoll5SField,
    LeafLeftForeArmRoll5TField,
    LeafLeftLegRoll1RField,
    LeafLeftLegRoll1SField,
    LeafLeftLegRoll1TField,
    LeafLeftLegRoll2RField,
    LeafLeftLegRoll2SField,
    LeafLeftLegRoll2TField,
    LeafLeftLegRoll3RField,
    LeafLeftLegRoll3SField,
    LeafLeftLegRoll3TField,
    LeafLeftLegRoll4RField,
    LeafLeftLegRoll4SField,
    LeafLeftLegRoll4TField,
    LeafLeftLegRoll5RField,
    LeafLeftLegRoll5SField,
    LeafLeftLegRoll5TField,
    LeafLeftUpLegRoll1RField,
    LeafLeftUpLegRoll1SField,
    LeafLeftUpLegRoll1TField,
    LeafLeftUpLegRoll2RField,
    LeafLeftUpLegRoll2SField,
    LeafLeftUpLegRoll2TField,
    LeafLeftUpLegRoll3RField,
    LeafLeftUpLegRoll3SField,
    LeafLeftUpLegRoll3TField,
    LeafLeftUpLegRoll4RField,
    LeafLeftUpLegRoll4SField,
    LeafLeftUpLegRoll4TField,
    LeafLeftUpLegRoll5RField,
    LeafLeftUpLegRoll5SField,
    LeafLeftUpLegRoll5TField,
    LeafRightArmRoll1RField,
    LeafRightArmRoll1SField,
    LeafRightArmRoll1TField,
    LeafRightArmRoll2RField,
    LeafRightArmRoll2SField,
    LeafRightArmRoll2TField,
    LeafRightArmRoll3RField,
    LeafRightArmRoll3SField,
    LeafRightArmRoll3TField,
    LeafRightArmRoll4RField,
    LeafRightArmRoll4SField,
    LeafRightArmRoll4TField,
    LeafRightArmRoll5RField,
    LeafRightArmRoll5SField,
    LeafRightArmRoll5TField,
    LeafRightForeArmRoll1RField,
    LeafRightForeArmRoll1SField,
    LeafRightForeArmRoll1TField,
    LeafRightForeArmRoll2RField,
    LeafRightForeArmRoll2SField,
    LeafRightForeArmRoll2TField,
    LeafRightForeArmRoll3RField,
    LeafRightForeArmRoll3SField,
    LeafRightForeArmRoll3TField,
    LeafRightForeArmRoll4RField,
    LeafRightForeArmRoll4SField,
    LeafRightForeArmRoll4TField,
    LeafRightForeArmRoll5RField,
    LeafRightForeArmRoll5SField,
    LeafRightForeArmRoll5TField,
    LeafRightLegRoll1RField,
    LeafRightLegRoll1SField,
    LeafRightLegRoll1TField,
    LeafRightLegRoll2RField,
    LeafRightLegRoll2SField,
    LeafRightLegRoll2TField,
    LeafRightLegRoll3RField,
    LeafRightLegRoll3SField,
    LeafRightLegRoll3TField,
    LeafRightLegRoll4RField,
    LeafRightLegRoll4SField,
    LeafRightLegRoll4TField,
    LeafRightLegRoll5RField,
    LeafRightLegRoll5SField,
    LeafRightLegRoll5TField,
    LeafRightUpLegRoll1RField,
    LeafRightUpLegRoll1SField,
    LeafRightUpLegRoll1TField,
    LeafRightUpLegRoll2RField,
    LeafRightUpLegRoll2SField,
    LeafRightUpLegRoll2TField,
    LeafRightUpLegRoll3RField,
    LeafRightUpLegRoll3SField,
    LeafRightUpLegRoll3TField,
    LeafRightUpLegRoll4RField,
    LeafRightUpLegRoll4SField,
    LeafRightUpLegRoll4TField,
    LeafRightUpLegRoll5RField,
    LeafRightUpLegRoll5SField,
    LeafRightUpLegRoll5TField,
    LeftArmRField,
    LeftArmRollRField,
    LeftArmRollSField,
    LeftArmRollTField,
    LeftArmSField,
    LeftArmTField,
    LeftFingerBaseRField,
    LeftFingerBaseSField,
    LeftFingerBaseTField,
    LeftFootExtraFinger1RField,
    LeftFootExtraFinger1SField,
    LeftFootExtraFinger1TField,
    LeftFootExtraFinger2RField,
    LeftFootExtraFinger2SField,
    LeftFootExtraFinger2TField,
    LeftFootExtraFinger3RField,
    LeftFootExtraFinger3SField,
    LeftFootExtraFinger3TField,
    LeftFootExtraFinger4RField,
    LeftFootExtraFinger4SField,
    LeftFootExtraFinger4TField,
    LeftFootIndex1RField,
    LeftFootIndex1SField,
    LeftFootIndex1TField,
    LeftFootIndex2RField,
    LeftFootIndex2SField,
    LeftFootIndex2TField,
    LeftFootIndex3RField,
    LeftFootIndex3SField,
    LeftFootIndex3TField,
    LeftFootIndex4RField,
    LeftFootIndex4SField,
    LeftFootIndex4TField,
    LeftFootMiddle1RField,
    LeftFootMiddle1SField,
    LeftFootMiddle1TField,
    LeftFootMiddle2RField,
    LeftFootMiddle2SField,
    LeftFootMiddle2TField,
    LeftFootMiddle3RField,
    LeftFootMiddle3SField,
    LeftFootMiddle3TField,
    LeftFootMiddle4RField,
    LeftFootMiddle4SField,
    LeftFootMiddle4TField,
    LeftFootPinky1RField,
    LeftFootPinky1SField,
    LeftFootPinky1TField,
    LeftFootPinky2RField,
    LeftFootPinky2SField,
    LeftFootPinky2TField,
    LeftFootPinky3RField,
    LeftFootPinky3SField,
    LeftFootPinky3TField,
    LeftFootPinky4RField,
    LeftFootPinky4SField,
    LeftFootPinky4TField,
    LeftFootRField,
    LeftFootRing1RField,
    LeftFootRing1SField,
    LeftFootRing1TField,
    LeftFootRing2RField,
    LeftFootRing2SField,
    LeftFootRing2TField,
    LeftFootRing3RField,
    LeftFootRing3SField,
    LeftFootRing3TField,
    LeftFootRing4RField,
    LeftFootRing4SField,
    LeftFootRing4TField,
    LeftFootSField,
    LeftFootTField,
    LeftFootThumb1RField,
    LeftFootThumb1SField,
    LeftFootThumb1TField,
    LeftFootThumb2RField,
    LeftFootThumb2SField,
    LeftFootThumb2TField,
    LeftFootThumb3RField,
    LeftFootThumb3SField,
    LeftFootThumb3TField,
    LeftFootThumb4RField,
    LeftFootThumb4SField,
    LeftFootThumb4TField,
    LeftForeArmRField,
    LeftForeArmRollRField,
    LeftForeArmRollSField,
    LeftForeArmRollTField,
    LeftForeArmSField,
    LeftForeArmTField,
    LeftHandExtraFinger1RField,
    LeftHandExtraFinger1SField,
    LeftHandExtraFinger1TField,
    LeftHandExtraFinger2RField,
    LeftHandExtraFinger2SField,
    LeftHandExtraFinger2TField,
    LeftHandExtraFinger3RField,
    LeftHandExtraFinger3SField,
    LeftHandExtraFinger3TField,
    LeftHandExtraFinger4RField,
    LeftHandExtraFinger4SField,
    LeftHandExtraFinger4TField,
    LeftHandIndex1RField,
    LeftHandIndex1SField,
    LeftHandIndex1TField,
    LeftHandIndex2RField,
    LeftHandIndex2SField,
    LeftHandIndex2TField,
    LeftHandIndex3RField,
    LeftHandIndex3SField,
    LeftHandIndex3TField,
    LeftHandIndex4RField,
    LeftHandIndex4SField,
    LeftHandIndex4TField,
    LeftHandMiddle1RField,
    LeftHandMiddle1SField,
    LeftHandMiddle1TField,
    LeftHandMiddle2RField,
    LeftHandMiddle2SField,
    LeftHandMiddle2TField,
    LeftHandMiddle3RField,
    LeftHandMiddle3SField,
    LeftHandMiddle3TField,
    LeftHandMiddle4RField,
    LeftHandMiddle4SField,
    LeftHandMiddle4TField,
    LeftHandPinky1RField,
    LeftHandPinky1SField,
    LeftHandPinky1TField,
    LeftHandPinky2RField,
    LeftHandPinky2SField,
    LeftHandPinky2TField,
    LeftHandPinky3RField,
    LeftHandPinky3SField,
    LeftHandPinky3TField,
    LeftHandPinky4RField,
    LeftHandPinky4SField,
    LeftHandPinky4TField,
    LeftHandRField,
    LeftHandRing1RField,
    LeftHandRing1SField,
    LeftHandRing1TField,
    LeftHandRing2RField,
    LeftHandRing2SField,
    LeftHandRing2TField,
    LeftHandRing3RField,
    LeftHandRing3SField,
    LeftHandRing3TField,
    LeftHandRing4RField,
    LeftHandRing4SField,
    LeftHandRing4TField,
    LeftHandSField,
    LeftHandTField,
    LeftHandThumb1RField,
    LeftHandThumb1SField,
    LeftHandThumb1TField,
    LeftHandThumb2RField,
    LeftHandThumb2SField,
    LeftHandThumb2TField,
    LeftHandThumb3RField,
    LeftHandThumb3SField,
    LeftHandThumb3TField,
    LeftHandThumb4RField,
    LeftHandThumb4SField,
    LeftHandThumb4TField,
    LeftInFootExtraFingerRField,
    LeftInFootExtraFingerSField,
    LeftInFootExtraFingerTField,
    LeftInFootIndexRField,
    LeftInFootIndexSField,
    LeftInFootIndexTField,
    LeftInFootMiddleRField,
    LeftInFootMiddleSField,
    LeftInFootMiddleTField,
    LeftInFootPinkyRField,
    LeftInFootPinkySField,
    LeftInFootPinkyTField,
    LeftInFootRingRField,
    LeftInFootRingSField,
    LeftInFootRingTField,
    LeftInFootThumbRField,
    LeftInFootThumbSField,
    LeftInFootThumbTField,
    LeftInHandExtraFingerRField,
    LeftInHandExtraFingerSField,
    LeftInHandExtraFingerTField,
    LeftInHandIndexRField,
    LeftInHandIndexSField,
    LeftInHandIndexTField,
    LeftInHandMiddleRField,
    LeftInHandMiddleSField,
    LeftInHandMiddleTField,
    LeftInHandPinkyRField,
    LeftInHandPinkySField,
    LeftInHandPinkyTField,
    LeftInHandRingRField,
    LeftInHandRingSField,
    LeftInHandRingTField,
    LeftInHandThumbRField,
    LeftInHandThumbSField,
    LeftInHandThumbTField,
    LeftLegRField,
    LeftLegRollRField,
    LeftLegRollSField,
    LeftLegRollTField,
    LeftLegSField,
    LeftLegTField,
    LeftShoulderExtraRField,
    LeftShoulderExtraSField,
    LeftShoulderExtraTField,
    LeftShoulderRField,
    LeftShoulderSField,
    LeftShoulderTField,
    LeftToeBaseRField,
    LeftToeBaseSField,
    LeftToeBaseTField,
    LeftUpLegRField,
    LeftUpLegRollRField,
    LeftUpLegRollSField,
    LeftUpLegRollTField,
    LeftUpLegSField,
    LeftUpLegTField,
    Neck1RField,
    Neck1SField,
    Neck1TField,
    Neck2RField,
    Neck2SField,
    Neck2TField,
    Neck3RField,
    Neck3SField,
    Neck3TField,
    Neck4RField,
    Neck4SField,
    Neck4TField,
    Neck5RField,
    Neck5SField,
    Neck5TField,
    Neck6RField,
    Neck6SField,
    Neck6TField,
    Neck7RField,
    Neck7SField,
    Neck7TField,
    Neck8RField,
    Neck8SField,
    Neck8TField,
    Neck9RField,
    Neck9SField,
    Neck9TField,
    NeckRField,
    NeckSField,
    NeckTField,
    ReferenceRField,
    ReferenceSField,
    ReferenceTField,
    RightArmRField,
    RightArmRollRField,
    RightArmRollSField,
    RightArmRollTField,
    RightArmSField,
    RightArmTField,
    RightFingerBaseRField,
    RightFingerBaseSField,
    RightFingerBaseTField,
    RightFootExtraFinger1RField,
    RightFootExtraFinger1SField,
    RightFootExtraFinger1TField,
    RightFootExtraFinger2RField,
    RightFootExtraFinger2SField,
    RightFootExtraFinger2TField,
    RightFootExtraFinger3RField,
    RightFootExtraFinger3SField,
    RightFootExtraFinger3TField,
    RightFootExtraFinger4RField,
    RightFootExtraFinger4SField,
    RightFootExtraFinger4TField,
    RightFootIndex1RField,
    RightFootIndex1SField,
    RightFootIndex1TField,
    RightFootIndex2RField,
    RightFootIndex2SField,
    RightFootIndex2TField,
    RightFootIndex3RField,
    RightFootIndex3SField,
    RightFootIndex3TField,
    RightFootIndex4RField,
    RightFootIndex4SField,
    RightFootIndex4TField,
    RightFootMiddle1RField,
    RightFootMiddle1SField,
    RightFootMiddle1TField,
    RightFootMiddle2RField,
    RightFootMiddle2SField,
    RightFootMiddle2TField,
    RightFootMiddle3RField,
    RightFootMiddle3SField,
    RightFootMiddle3TField,
    RightFootMiddle4RField,
    RightFootMiddle4SField,
    RightFootMiddle4TField,
    RightFootPinky1RField,
    RightFootPinky1SField,
    RightFootPinky1TField,
    RightFootPinky2RField,
    RightFootPinky2SField,
    RightFootPinky2TField,
    RightFootPinky3RField,
    RightFootPinky3SField,
    RightFootPinky3TField,
    RightFootPinky4RField,
    RightFootPinky4SField,
    RightFootPinky4TField,
    RightFootRField,
    RightFootRing1RField,
    RightFootRing1SField,
    RightFootRing1TField,
    RightFootRing2RField,
    RightFootRing2SField,
    RightFootRing2TField,
    RightFootRing3RField,
    RightFootRing3SField,
    RightFootRing3TField,
    RightFootRing4RField,
    RightFootRing4SField,
    RightFootRing4TField,
    RightFootSField,
    RightFootTField,
    RightFootThumb1RField,
    RightFootThumb1SField,
    RightFootThumb1TField,
    RightFootThumb2RField,
    RightFootThumb2SField,
    RightFootThumb2TField,
    RightFootThumb3RField,
    RightFootThumb3SField,
    RightFootThumb3TField,
    RightFootThumb4RField,
    RightFootThumb4SField,
    RightFootThumb4TField,
    RightForeArmRField,
    RightForeArmRollRField,
    RightForeArmRollSField,
    RightForeArmRollTField,
    RightForeArmSField,
    RightForeArmTField,
    RightHandExtraFinger1RField,
    RightHandExtraFinger1SField,
    RightHandExtraFinger1TField,
    RightHandExtraFinger2RField,
    RightHandExtraFinger2SField,
    RightHandExtraFinger2TField,
    RightHandExtraFinger3RField,
    RightHandExtraFinger3SField,
    RightHandExtraFinger3TField,
    RightHandExtraFinger4RField,
    RightHandExtraFinger4SField,
    RightHandExtraFinger4TField,
    RightHandIndex1RField,
    RightHandIndex1SField,
    RightHandIndex1TField,
    RightHandIndex2RField,
    RightHandIndex2SField,
    RightHandIndex2TField,
    RightHandIndex3RField,
    RightHandIndex3SField,
    RightHandIndex3TField,
    RightHandIndex4RField,
    RightHandIndex4SField,
    RightHandIndex4TField,
    RightHandMiddle1RField,
    RightHandMiddle1SField,
    RightHandMiddle1TField,
    RightHandMiddle2RField,
    RightHandMiddle2SField,
    RightHandMiddle2TField,
    RightHandMiddle3RField,
    RightHandMiddle3SField,
    RightHandMiddle3TField,
    RightHandMiddle4RField,
    RightHandMiddle4SField,
    RightHandMiddle4TField,
    RightHandPinky1RField,
    RightHandPinky1SField,
    RightHandPinky1TField,
    RightHandPinky2RField,
    RightHandPinky2SField,
    RightHandPinky2TField,
    RightHandPinky3RField,
    RightHandPinky3SField,
    RightHandPinky3TField,
    RightHandPinky4RField,
    RightHandPinky4SField,
    RightHandPinky4TField,
    RightHandRField,
    RightHandRing1RField,
    RightHandRing1SField,
    RightHandRing1TField,
    RightHandRing2RField,
    RightHandRing2SField,
    RightHandRing2TField,
    RightHandRing3RField,
    RightHandRing3SField,
    RightHandRing3TField,
    RightHandRing4RField,
    RightHandRing4SField,
    RightHandRing4TField,
    RightHandSField,
    RightHandTField,
    RightHandThumb1RField,
    RightHandThumb1SField,
    RightHandThumb1TField,
    RightHandThumb2RField,
    RightHandThumb2SField,
    RightHandThumb2TField,
    RightHandThumb3RField,
    RightHandThumb3SField,
    RightHandThumb3TField,
    RightHandThumb4RField,
    RightHandThumb4SField,
    RightHandThumb4TField,
    RightInFootExtraFingerRField,
    RightInFootExtraFingerSField,
    RightInFootExtraFingerTField,
    RightInFootIndexRField,
    RightInFootIndexSField,
    RightInFootIndexTField,
    RightInFootMiddleRField,
    RightInFootMiddleSField,
    RightInFootMiddleTField,
    RightInFootPinkyRField,
    RightInFootPinkySField,
    RightInFootPinkyTField,
    RightInFootRingRField,
    RightInFootRingSField,
    RightInFootRingTField,
    RightInFootThumbRField,
    RightInFootThumbSField,
    RightInFootThumbTField,
    RightInHandExtraFingerRField,
    RightInHandExtraFingerSField,
    RightInHandExtraFingerTField,
    RightInHandIndexRField,
    RightInHandIndexSField,
    RightInHandIndexTField,
    RightInHandMiddleRField,
    RightInHandMiddleSField,
    RightInHandMiddleTField,
    RightInHandPinkyRField,
    RightInHandPinkySField,
    RightInHandPinkyTField,
    RightInHandRingRField,
    RightInHandRingSField,
    RightInHandRingTField,
    RightInHandThumbRField,
    RightInHandThumbSField,
    RightInHandThumbTField,
    RightLegRField,
    RightLegRollRField,
    RightLegRollSField,
    RightLegRollTField,
    RightLegSField,
    RightLegTField,
    RightShoulderExtraRField,
    RightShoulderExtraSField,
    RightShoulderExtraTField,
    RightShoulderRField,
    RightShoulderSField,
    RightShoulderTField,
    RightToeBaseRField,
    RightToeBaseSField,
    RightToeBaseTField,
    RightUpLegRField,
    RightUpLegRollRField,
    RightUpLegRollSField,
    RightUpLegRollTField,
    RightUpLegSField,
    RightUpLegTField,
    Spine1RField,
    Spine1SField,
    Spine1TField,
    Spine2RField,
    Spine2SField,
    Spine2TField,
    Spine3RField,
    Spine3SField,
    Spine3TField,
    Spine4RField,
    Spine4SField,
    Spine4TField,
    Spine5RField,
    Spine5SField,
    Spine5TField,
    Spine6RField,
    Spine6SField,
    Spine6TField,
    Spine7RField,
    Spine7SField,
    Spine7TField,
    Spine8RField,
    Spine8SField,
    Spine8TField,
    Spine9RField,
    Spine9SField,
    Spine9TField,
    SpineRField,
    SpineSField,
    SpineTField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class HIKSkeletonGeneratorNode(DG):
    __slots__ = ()

    NODE_TYPE = "HIKSkeletonGeneratorNode"

    SpineCount = LongField()

    NeckCount = LongField()

    ShoulderCount = LongField()

    WantUpperArmRollBone = BoolField()

    WantLowerArmRollBone = BoolField()

    WantUpperLegRollBone = BoolField()

    WantLowerLegRollBone = BoolField()

    NbUpperArmRollBones = LongField()

    NbLowerArmRollBones = LongField()

    NbUpperLegRollBones = LongField()

    NbLowerLegRollBones = LongField()

    WantIndexFinger = BoolField()

    WantMiddleFinger = BoolField()

    WantRingFinger = BoolField()

    WantPinkyFinger = BoolField()

    WantThumb = BoolField()

    WantExtraFinger = BoolField()

    WantFingerBase = BoolField()

    WantInHandJoint = BoolField()

    FingerJointCount = LongField()

    WantIndexToe = BoolField()

    WantMiddleToe = BoolField()

    WantRingToe = BoolField()

    WantPinkyToe = BoolField()

    WantBigToe = BoolField()

    WantFootThumb = BoolField()

    WantToeBase = BoolField()

    WantInFootJoint = BoolField()

    ToeJointCount = LongField()

    WantHipsTranslation = BoolField()

    CharacterNode = MessageField()

    ReferenceT = ReferenceTField()
    ReferenceTx = ReferenceT.ReferenceTx
    ReferenceTy = ReferenceT.ReferenceTy
    ReferenceTz = ReferenceT.ReferenceTz

    ReferenceR = ReferenceRField()
    ReferenceRx = ReferenceR.ReferenceRx
    ReferenceRy = ReferenceR.ReferenceRy
    ReferenceRz = ReferenceR.ReferenceRz

    ReferenceS = ReferenceSField()
    ReferenceSx = ReferenceS.ReferenceSx
    ReferenceSy = ReferenceS.ReferenceSy
    ReferenceSz = ReferenceS.ReferenceSz

    HipsT = HipsTField()
    HipsTx = HipsT.HipsTx
    HipsTy = HipsT.HipsTy
    HipsTz = HipsT.HipsTz

    HipsR = HipsRField()
    HipsRx = HipsR.HipsRx
    HipsRy = HipsR.HipsRy
    HipsRz = HipsR.HipsRz

    HipsS = HipsSField()
    HipsSx = HipsS.HipsSx
    HipsSy = HipsS.HipsSy
    HipsSz = HipsS.HipsSz

    LeftUpLegT = LeftUpLegTField()
    LeftUpLegTx = LeftUpLegT.LeftUpLegTx
    LeftUpLegTy = LeftUpLegT.LeftUpLegTy
    LeftUpLegTz = LeftUpLegT.LeftUpLegTz

    LeftUpLegR = LeftUpLegRField()
    LeftUpLegRx = LeftUpLegR.LeftUpLegRx
    LeftUpLegRy = LeftUpLegR.LeftUpLegRy
    LeftUpLegRz = LeftUpLegR.LeftUpLegRz

    LeftUpLegS = LeftUpLegSField()
    LeftUpLegSx = LeftUpLegS.LeftUpLegSx
    LeftUpLegSy = LeftUpLegS.LeftUpLegSy
    LeftUpLegSz = LeftUpLegS.LeftUpLegSz

    LeftLegT = LeftLegTField()
    LeftLegTx = LeftLegT.LeftLegTx
    LeftLegTy = LeftLegT.LeftLegTy
    LeftLegTz = LeftLegT.LeftLegTz

    LeftLegR = LeftLegRField()
    LeftLegRx = LeftLegR.LeftLegRx
    LeftLegRy = LeftLegR.LeftLegRy
    LeftLegRz = LeftLegR.LeftLegRz

    LeftLegS = LeftLegSField()
    LeftLegSx = LeftLegS.LeftLegSx
    LeftLegSy = LeftLegS.LeftLegSy
    LeftLegSz = LeftLegS.LeftLegSz

    LeftFootT = LeftFootTField()
    LeftFootTx = LeftFootT.LeftFootTx
    LeftFootTy = LeftFootT.LeftFootTy
    LeftFootTz = LeftFootT.LeftFootTz

    LeftFootR = LeftFootRField()
    LeftFootRx = LeftFootR.LeftFootRx
    LeftFootRy = LeftFootR.LeftFootRy
    LeftFootRz = LeftFootR.LeftFootRz

    LeftFootS = LeftFootSField()
    LeftFootSx = LeftFootS.LeftFootSx
    LeftFootSy = LeftFootS.LeftFootSy
    LeftFootSz = LeftFootS.LeftFootSz

    RightUpLegT = RightUpLegTField()
    RightUpLegTx = RightUpLegT.RightUpLegTx
    RightUpLegTy = RightUpLegT.RightUpLegTy
    RightUpLegTz = RightUpLegT.RightUpLegTz

    RightUpLegR = RightUpLegRField()
    RightUpLegRx = RightUpLegR.RightUpLegRx
    RightUpLegRy = RightUpLegR.RightUpLegRy
    RightUpLegRz = RightUpLegR.RightUpLegRz

    RightUpLegS = RightUpLegSField()
    RightUpLegSx = RightUpLegS.RightUpLegSx
    RightUpLegSy = RightUpLegS.RightUpLegSy
    RightUpLegSz = RightUpLegS.RightUpLegSz

    RightLegT = RightLegTField()
    RightLegTx = RightLegT.RightLegTx
    RightLegTy = RightLegT.RightLegTy
    RightLegTz = RightLegT.RightLegTz

    RightLegR = RightLegRField()
    RightLegRx = RightLegR.RightLegRx
    RightLegRy = RightLegR.RightLegRy
    RightLegRz = RightLegR.RightLegRz

    RightLegS = RightLegSField()
    RightLegSx = RightLegS.RightLegSx
    RightLegSy = RightLegS.RightLegSy
    RightLegSz = RightLegS.RightLegSz

    RightFootT = RightFootTField()
    RightFootTx = RightFootT.RightFootTx
    RightFootTy = RightFootT.RightFootTy
    RightFootTz = RightFootT.RightFootTz

    RightFootR = RightFootRField()
    RightFootRx = RightFootR.RightFootRx
    RightFootRy = RightFootR.RightFootRy
    RightFootRz = RightFootR.RightFootRz

    RightFootS = RightFootSField()
    RightFootSx = RightFootS.RightFootSx
    RightFootSy = RightFootS.RightFootSy
    RightFootSz = RightFootS.RightFootSz

    SpineT = SpineTField()
    SpineTx = SpineT.SpineTx
    SpineTy = SpineT.SpineTy
    SpineTz = SpineT.SpineTz

    SpineR = SpineRField()
    SpineRx = SpineR.SpineRx
    SpineRy = SpineR.SpineRy
    SpineRz = SpineR.SpineRz

    SpineS = SpineSField()
    SpineSx = SpineS.SpineSx
    SpineSy = SpineS.SpineSy
    SpineSz = SpineS.SpineSz

    LeftArmT = LeftArmTField()
    LeftArmTx = LeftArmT.LeftArmTx
    LeftArmTy = LeftArmT.LeftArmTy
    LeftArmTz = LeftArmT.LeftArmTz

    LeftArmR = LeftArmRField()
    LeftArmRx = LeftArmR.LeftArmRx
    LeftArmRy = LeftArmR.LeftArmRy
    LeftArmRz = LeftArmR.LeftArmRz

    LeftArmS = LeftArmSField()
    LeftArmSx = LeftArmS.LeftArmSx
    LeftArmSy = LeftArmS.LeftArmSy
    LeftArmSz = LeftArmS.LeftArmSz

    LeftForeArmT = LeftForeArmTField()
    LeftForeArmTx = LeftForeArmT.LeftForeArmTx
    LeftForeArmTy = LeftForeArmT.LeftForeArmTy
    LeftForeArmTz = LeftForeArmT.LeftForeArmTz

    LeftForeArmR = LeftForeArmRField()
    LeftForeArmRx = LeftForeArmR.LeftForeArmRx
    LeftForeArmRy = LeftForeArmR.LeftForeArmRy
    LeftForeArmRz = LeftForeArmR.LeftForeArmRz

    LeftForeArmS = LeftForeArmSField()
    LeftForeArmSx = LeftForeArmS.LeftForeArmSx
    LeftForeArmSy = LeftForeArmS.LeftForeArmSy
    LeftForeArmSz = LeftForeArmS.LeftForeArmSz

    LeftHandT = LeftHandTField()
    LeftHandTx = LeftHandT.LeftHandTx
    LeftHandTy = LeftHandT.LeftHandTy
    LeftHandTz = LeftHandT.LeftHandTz

    LeftHandR = LeftHandRField()
    LeftHandRx = LeftHandR.LeftHandRx
    LeftHandRy = LeftHandR.LeftHandRy
    LeftHandRz = LeftHandR.LeftHandRz

    LeftHandS = LeftHandSField()
    LeftHandSx = LeftHandS.LeftHandSx
    LeftHandSy = LeftHandS.LeftHandSy
    LeftHandSz = LeftHandS.LeftHandSz

    RightArmT = RightArmTField()
    RightArmTx = RightArmT.RightArmTx
    RightArmTy = RightArmT.RightArmTy
    RightArmTz = RightArmT.RightArmTz

    RightArmR = RightArmRField()
    RightArmRx = RightArmR.RightArmRx
    RightArmRy = RightArmR.RightArmRy
    RightArmRz = RightArmR.RightArmRz

    RightArmS = RightArmSField()
    RightArmSx = RightArmS.RightArmSx
    RightArmSy = RightArmS.RightArmSy
    RightArmSz = RightArmS.RightArmSz

    RightForeArmT = RightForeArmTField()
    RightForeArmTx = RightForeArmT.RightForeArmTx
    RightForeArmTy = RightForeArmT.RightForeArmTy
    RightForeArmTz = RightForeArmT.RightForeArmTz

    RightForeArmR = RightForeArmRField()
    RightForeArmRx = RightForeArmR.RightForeArmRx
    RightForeArmRy = RightForeArmR.RightForeArmRy
    RightForeArmRz = RightForeArmR.RightForeArmRz

    RightForeArmS = RightForeArmSField()
    RightForeArmSx = RightForeArmS.RightForeArmSx
    RightForeArmSy = RightForeArmS.RightForeArmSy
    RightForeArmSz = RightForeArmS.RightForeArmSz

    RightHandT = RightHandTField()
    RightHandTx = RightHandT.RightHandTx
    RightHandTy = RightHandT.RightHandTy
    RightHandTz = RightHandT.RightHandTz

    RightHandR = RightHandRField()
    RightHandRx = RightHandR.RightHandRx
    RightHandRy = RightHandR.RightHandRy
    RightHandRz = RightHandR.RightHandRz

    RightHandS = RightHandSField()
    RightHandSx = RightHandS.RightHandSx
    RightHandSy = RightHandS.RightHandSy
    RightHandSz = RightHandS.RightHandSz

    HeadT = HeadTField()
    HeadTx = HeadT.HeadTx
    HeadTy = HeadT.HeadTy
    HeadTz = HeadT.HeadTz

    HeadR = HeadRField()
    HeadRx = HeadR.HeadRx
    HeadRy = HeadR.HeadRy
    HeadRz = HeadR.HeadRz

    HeadS = HeadSField()
    HeadSx = HeadS.HeadSx
    HeadSy = HeadS.HeadSy
    HeadSz = HeadS.HeadSz

    LeftToeBaseT = LeftToeBaseTField()
    LeftToeBaseTx = LeftToeBaseT.LeftToeBaseTx
    LeftToeBaseTy = LeftToeBaseT.LeftToeBaseTy
    LeftToeBaseTz = LeftToeBaseT.LeftToeBaseTz

    LeftToeBaseR = LeftToeBaseRField()
    LeftToeBaseRx = LeftToeBaseR.LeftToeBaseRx
    LeftToeBaseRy = LeftToeBaseR.LeftToeBaseRy
    LeftToeBaseRz = LeftToeBaseR.LeftToeBaseRz

    LeftToeBaseS = LeftToeBaseSField()
    LeftToeBaseSx = LeftToeBaseS.LeftToeBaseSx
    LeftToeBaseSy = LeftToeBaseS.LeftToeBaseSy
    LeftToeBaseSz = LeftToeBaseS.LeftToeBaseSz

    RightToeBaseT = RightToeBaseTField()
    RightToeBaseTx = RightToeBaseT.RightToeBaseTx
    RightToeBaseTy = RightToeBaseT.RightToeBaseTy
    RightToeBaseTz = RightToeBaseT.RightToeBaseTz

    RightToeBaseR = RightToeBaseRField()
    RightToeBaseRx = RightToeBaseR.RightToeBaseRx
    RightToeBaseRy = RightToeBaseR.RightToeBaseRy
    RightToeBaseRz = RightToeBaseR.RightToeBaseRz

    RightToeBaseS = RightToeBaseSField()
    RightToeBaseSx = RightToeBaseS.RightToeBaseSx
    RightToeBaseSy = RightToeBaseS.RightToeBaseSy
    RightToeBaseSz = RightToeBaseS.RightToeBaseSz

    LeftShoulderT = LeftShoulderTField()
    LeftShoulderTx = LeftShoulderT.LeftShoulderTx
    LeftShoulderTy = LeftShoulderT.LeftShoulderTy
    LeftShoulderTz = LeftShoulderT.LeftShoulderTz

    LeftShoulderR = LeftShoulderRField()
    LeftShoulderRx = LeftShoulderR.LeftShoulderRx
    LeftShoulderRy = LeftShoulderR.LeftShoulderRy
    LeftShoulderRz = LeftShoulderR.LeftShoulderRz

    LeftShoulderS = LeftShoulderSField()
    LeftShoulderSx = LeftShoulderS.LeftShoulderSx
    LeftShoulderSy = LeftShoulderS.LeftShoulderSy
    LeftShoulderSz = LeftShoulderS.LeftShoulderSz

    RightShoulderT = RightShoulderTField()
    RightShoulderTx = RightShoulderT.RightShoulderTx
    RightShoulderTy = RightShoulderT.RightShoulderTy
    RightShoulderTz = RightShoulderT.RightShoulderTz

    RightShoulderR = RightShoulderRField()
    RightShoulderRx = RightShoulderR.RightShoulderRx
    RightShoulderRy = RightShoulderR.RightShoulderRy
    RightShoulderRz = RightShoulderR.RightShoulderRz

    RightShoulderS = RightShoulderSField()
    RightShoulderSx = RightShoulderS.RightShoulderSx
    RightShoulderSy = RightShoulderS.RightShoulderSy
    RightShoulderSz = RightShoulderS.RightShoulderSz

    NeckT = NeckTField()
    NeckTx = NeckT.NeckTx
    NeckTy = NeckT.NeckTy
    NeckTz = NeckT.NeckTz

    NeckR = NeckRField()
    NeckRx = NeckR.NeckRx
    NeckRy = NeckR.NeckRy
    NeckRz = NeckR.NeckRz

    NeckS = NeckSField()
    NeckSx = NeckS.NeckSx
    NeckSy = NeckS.NeckSy
    NeckSz = NeckS.NeckSz

    LeftFingerBaseT = LeftFingerBaseTField()
    LeftFingerBaseTx = LeftFingerBaseT.LeftFingerBaseTx
    LeftFingerBaseTy = LeftFingerBaseT.LeftFingerBaseTy
    LeftFingerBaseTz = LeftFingerBaseT.LeftFingerBaseTz

    LeftFingerBaseR = LeftFingerBaseRField()
    LeftFingerBaseRx = LeftFingerBaseR.LeftFingerBaseRx
    LeftFingerBaseRy = LeftFingerBaseR.LeftFingerBaseRy
    LeftFingerBaseRz = LeftFingerBaseR.LeftFingerBaseRz

    LeftFingerBaseS = LeftFingerBaseSField()
    LeftFingerBaseSx = LeftFingerBaseS.LeftFingerBaseSx
    LeftFingerBaseSy = LeftFingerBaseS.LeftFingerBaseSy
    LeftFingerBaseSz = LeftFingerBaseS.LeftFingerBaseSz

    RightFingerBaseT = RightFingerBaseTField()
    RightFingerBaseTx = RightFingerBaseT.RightFingerBaseTx
    RightFingerBaseTy = RightFingerBaseT.RightFingerBaseTy
    RightFingerBaseTz = RightFingerBaseT.RightFingerBaseTz

    RightFingerBaseR = RightFingerBaseRField()
    RightFingerBaseRx = RightFingerBaseR.RightFingerBaseRx
    RightFingerBaseRy = RightFingerBaseR.RightFingerBaseRy
    RightFingerBaseRz = RightFingerBaseR.RightFingerBaseRz

    RightFingerBaseS = RightFingerBaseSField()
    RightFingerBaseSx = RightFingerBaseS.RightFingerBaseSx
    RightFingerBaseSy = RightFingerBaseS.RightFingerBaseSy
    RightFingerBaseSz = RightFingerBaseS.RightFingerBaseSz

    Spine1T = Spine1TField()
    Spine1Tx = Spine1T.Spine1Tx
    Spine1Ty = Spine1T.Spine1Ty
    Spine1Tz = Spine1T.Spine1Tz

    Spine1R = Spine1RField()
    Spine1Rx = Spine1R.Spine1Rx
    Spine1Ry = Spine1R.Spine1Ry
    Spine1Rz = Spine1R.Spine1Rz

    Spine1S = Spine1SField()
    Spine1Sx = Spine1S.Spine1Sx
    Spine1Sy = Spine1S.Spine1Sy
    Spine1Sz = Spine1S.Spine1Sz

    Spine2T = Spine2TField()
    Spine2Tx = Spine2T.Spine2Tx
    Spine2Ty = Spine2T.Spine2Ty
    Spine2Tz = Spine2T.Spine2Tz

    Spine2R = Spine2RField()
    Spine2Rx = Spine2R.Spine2Rx
    Spine2Ry = Spine2R.Spine2Ry
    Spine2Rz = Spine2R.Spine2Rz

    Spine2S = Spine2SField()
    Spine2Sx = Spine2S.Spine2Sx
    Spine2Sy = Spine2S.Spine2Sy
    Spine2Sz = Spine2S.Spine2Sz

    Spine3T = Spine3TField()
    Spine3Tx = Spine3T.Spine3Tx
    Spine3Ty = Spine3T.Spine3Ty
    Spine3Tz = Spine3T.Spine3Tz

    Spine3R = Spine3RField()
    Spine3Rx = Spine3R.Spine3Rx
    Spine3Ry = Spine3R.Spine3Ry
    Spine3Rz = Spine3R.Spine3Rz

    Spine3S = Spine3SField()
    Spine3Sx = Spine3S.Spine3Sx
    Spine3Sy = Spine3S.Spine3Sy
    Spine3Sz = Spine3S.Spine3Sz

    Spine4T = Spine4TField()
    Spine4Tx = Spine4T.Spine4Tx
    Spine4Ty = Spine4T.Spine4Ty
    Spine4Tz = Spine4T.Spine4Tz

    Spine4R = Spine4RField()
    Spine4Rx = Spine4R.Spine4Rx
    Spine4Ry = Spine4R.Spine4Ry
    Spine4Rz = Spine4R.Spine4Rz

    Spine4S = Spine4SField()
    Spine4Sx = Spine4S.Spine4Sx
    Spine4Sy = Spine4S.Spine4Sy
    Spine4Sz = Spine4S.Spine4Sz

    Spine5T = Spine5TField()
    Spine5Tx = Spine5T.Spine5Tx
    Spine5Ty = Spine5T.Spine5Ty
    Spine5Tz = Spine5T.Spine5Tz

    Spine5R = Spine5RField()
    Spine5Rx = Spine5R.Spine5Rx
    Spine5Ry = Spine5R.Spine5Ry
    Spine5Rz = Spine5R.Spine5Rz

    Spine5S = Spine5SField()
    Spine5Sx = Spine5S.Spine5Sx
    Spine5Sy = Spine5S.Spine5Sy
    Spine5Sz = Spine5S.Spine5Sz

    Spine6T = Spine6TField()
    Spine6Tx = Spine6T.Spine6Tx
    Spine6Ty = Spine6T.Spine6Ty
    Spine6Tz = Spine6T.Spine6Tz

    Spine6R = Spine6RField()
    Spine6Rx = Spine6R.Spine6Rx
    Spine6Ry = Spine6R.Spine6Ry
    Spine6Rz = Spine6R.Spine6Rz

    Spine6S = Spine6SField()
    Spine6Sx = Spine6S.Spine6Sx
    Spine6Sy = Spine6S.Spine6Sy
    Spine6Sz = Spine6S.Spine6Sz

    Spine7T = Spine7TField()
    Spine7Tx = Spine7T.Spine7Tx
    Spine7Ty = Spine7T.Spine7Ty
    Spine7Tz = Spine7T.Spine7Tz

    Spine7R = Spine7RField()
    Spine7Rx = Spine7R.Spine7Rx
    Spine7Ry = Spine7R.Spine7Ry
    Spine7Rz = Spine7R.Spine7Rz

    Spine7S = Spine7SField()
    Spine7Sx = Spine7S.Spine7Sx
    Spine7Sy = Spine7S.Spine7Sy
    Spine7Sz = Spine7S.Spine7Sz

    Spine8T = Spine8TField()
    Spine8Tx = Spine8T.Spine8Tx
    Spine8Ty = Spine8T.Spine8Ty
    Spine8Tz = Spine8T.Spine8Tz

    Spine8R = Spine8RField()
    Spine8Rx = Spine8R.Spine8Rx
    Spine8Ry = Spine8R.Spine8Ry
    Spine8Rz = Spine8R.Spine8Rz

    Spine8S = Spine8SField()
    Spine8Sx = Spine8S.Spine8Sx
    Spine8Sy = Spine8S.Spine8Sy
    Spine8Sz = Spine8S.Spine8Sz

    Spine9T = Spine9TField()
    Spine9Tx = Spine9T.Spine9Tx
    Spine9Ty = Spine9T.Spine9Ty
    Spine9Tz = Spine9T.Spine9Tz

    Spine9R = Spine9RField()
    Spine9Rx = Spine9R.Spine9Rx
    Spine9Ry = Spine9R.Spine9Ry
    Spine9Rz = Spine9R.Spine9Rz

    Spine9S = Spine9SField()
    Spine9Sx = Spine9S.Spine9Sx
    Spine9Sy = Spine9S.Spine9Sy
    Spine9Sz = Spine9S.Spine9Sz

    Neck1T = Neck1TField()
    Neck1Tx = Neck1T.Neck1Tx
    Neck1Ty = Neck1T.Neck1Ty
    Neck1Tz = Neck1T.Neck1Tz

    Neck1R = Neck1RField()
    Neck1Rx = Neck1R.Neck1Rx
    Neck1Ry = Neck1R.Neck1Ry
    Neck1Rz = Neck1R.Neck1Rz

    Neck1S = Neck1SField()
    Neck1Sx = Neck1S.Neck1Sx
    Neck1Sy = Neck1S.Neck1Sy
    Neck1Sz = Neck1S.Neck1Sz

    Neck2T = Neck2TField()
    Neck2Tx = Neck2T.Neck2Tx
    Neck2Ty = Neck2T.Neck2Ty
    Neck2Tz = Neck2T.Neck2Tz

    Neck2R = Neck2RField()
    Neck2Rx = Neck2R.Neck2Rx
    Neck2Ry = Neck2R.Neck2Ry
    Neck2Rz = Neck2R.Neck2Rz

    Neck2S = Neck2SField()
    Neck2Sx = Neck2S.Neck2Sx
    Neck2Sy = Neck2S.Neck2Sy
    Neck2Sz = Neck2S.Neck2Sz

    Neck3T = Neck3TField()
    Neck3Tx = Neck3T.Neck3Tx
    Neck3Ty = Neck3T.Neck3Ty
    Neck3Tz = Neck3T.Neck3Tz

    Neck3R = Neck3RField()
    Neck3Rx = Neck3R.Neck3Rx
    Neck3Ry = Neck3R.Neck3Ry
    Neck3Rz = Neck3R.Neck3Rz

    Neck3S = Neck3SField()
    Neck3Sx = Neck3S.Neck3Sx
    Neck3Sy = Neck3S.Neck3Sy
    Neck3Sz = Neck3S.Neck3Sz

    Neck4T = Neck4TField()
    Neck4Tx = Neck4T.Neck4Tx
    Neck4Ty = Neck4T.Neck4Ty
    Neck4Tz = Neck4T.Neck4Tz

    Neck4R = Neck4RField()
    Neck4Rx = Neck4R.Neck4Rx
    Neck4Ry = Neck4R.Neck4Ry
    Neck4Rz = Neck4R.Neck4Rz

    Neck4S = Neck4SField()
    Neck4Sx = Neck4S.Neck4Sx
    Neck4Sy = Neck4S.Neck4Sy
    Neck4Sz = Neck4S.Neck4Sz

    Neck5T = Neck5TField()
    Neck5Tx = Neck5T.Neck5Tx
    Neck5Ty = Neck5T.Neck5Ty
    Neck5Tz = Neck5T.Neck5Tz

    Neck5R = Neck5RField()
    Neck5Rx = Neck5R.Neck5Rx
    Neck5Ry = Neck5R.Neck5Ry
    Neck5Rz = Neck5R.Neck5Rz

    Neck5S = Neck5SField()
    Neck5Sx = Neck5S.Neck5Sx
    Neck5Sy = Neck5S.Neck5Sy
    Neck5Sz = Neck5S.Neck5Sz

    Neck6T = Neck6TField()
    Neck6Tx = Neck6T.Neck6Tx
    Neck6Ty = Neck6T.Neck6Ty
    Neck6Tz = Neck6T.Neck6Tz

    Neck6R = Neck6RField()
    Neck6Rx = Neck6R.Neck6Rx
    Neck6Ry = Neck6R.Neck6Ry
    Neck6Rz = Neck6R.Neck6Rz

    Neck6S = Neck6SField()
    Neck6Sx = Neck6S.Neck6Sx
    Neck6Sy = Neck6S.Neck6Sy
    Neck6Sz = Neck6S.Neck6Sz

    Neck7T = Neck7TField()
    Neck7Tx = Neck7T.Neck7Tx
    Neck7Ty = Neck7T.Neck7Ty
    Neck7Tz = Neck7T.Neck7Tz

    Neck7R = Neck7RField()
    Neck7Rx = Neck7R.Neck7Rx
    Neck7Ry = Neck7R.Neck7Ry
    Neck7Rz = Neck7R.Neck7Rz

    Neck7S = Neck7SField()
    Neck7Sx = Neck7S.Neck7Sx
    Neck7Sy = Neck7S.Neck7Sy
    Neck7Sz = Neck7S.Neck7Sz

    Neck8T = Neck8TField()
    Neck8Tx = Neck8T.Neck8Tx
    Neck8Ty = Neck8T.Neck8Ty
    Neck8Tz = Neck8T.Neck8Tz

    Neck8R = Neck8RField()
    Neck8Rx = Neck8R.Neck8Rx
    Neck8Ry = Neck8R.Neck8Ry
    Neck8Rz = Neck8R.Neck8Rz

    Neck8S = Neck8SField()
    Neck8Sx = Neck8S.Neck8Sx
    Neck8Sy = Neck8S.Neck8Sy
    Neck8Sz = Neck8S.Neck8Sz

    Neck9T = Neck9TField()
    Neck9Tx = Neck9T.Neck9Tx
    Neck9Ty = Neck9T.Neck9Ty
    Neck9Tz = Neck9T.Neck9Tz

    Neck9R = Neck9RField()
    Neck9Rx = Neck9R.Neck9Rx
    Neck9Ry = Neck9R.Neck9Ry
    Neck9Rz = Neck9R.Neck9Rz

    Neck9S = Neck9SField()
    Neck9Sx = Neck9S.Neck9Sx
    Neck9Sy = Neck9S.Neck9Sy
    Neck9Sz = Neck9S.Neck9Sz

    LeftUpLegRollT = LeftUpLegRollTField()
    LeftUpLegRollTx = LeftUpLegRollT.LeftUpLegRollTx
    LeftUpLegRollTy = LeftUpLegRollT.LeftUpLegRollTy
    LeftUpLegRollTz = LeftUpLegRollT.LeftUpLegRollTz

    LeftUpLegRollR = LeftUpLegRollRField()
    LeftUpLegRollRx = LeftUpLegRollR.LeftUpLegRollRx
    LeftUpLegRollRy = LeftUpLegRollR.LeftUpLegRollRy
    LeftUpLegRollRz = LeftUpLegRollR.LeftUpLegRollRz

    LeftUpLegRollS = LeftUpLegRollSField()
    LeftUpLegRollSx = LeftUpLegRollS.LeftUpLegRollSx
    LeftUpLegRollSy = LeftUpLegRollS.LeftUpLegRollSy
    LeftUpLegRollSz = LeftUpLegRollS.LeftUpLegRollSz

    LeftLegRollT = LeftLegRollTField()
    LeftLegRollTx = LeftLegRollT.LeftLegRollTx
    LeftLegRollTy = LeftLegRollT.LeftLegRollTy
    LeftLegRollTz = LeftLegRollT.LeftLegRollTz

    LeftLegRollR = LeftLegRollRField()
    LeftLegRollRx = LeftLegRollR.LeftLegRollRx
    LeftLegRollRy = LeftLegRollR.LeftLegRollRy
    LeftLegRollRz = LeftLegRollR.LeftLegRollRz

    LeftLegRollS = LeftLegRollSField()
    LeftLegRollSx = LeftLegRollS.LeftLegRollSx
    LeftLegRollSy = LeftLegRollS.LeftLegRollSy
    LeftLegRollSz = LeftLegRollS.LeftLegRollSz

    RightUpLegRollT = RightUpLegRollTField()
    RightUpLegRollTx = RightUpLegRollT.RightUpLegRollTx
    RightUpLegRollTy = RightUpLegRollT.RightUpLegRollTy
    RightUpLegRollTz = RightUpLegRollT.RightUpLegRollTz

    RightUpLegRollR = RightUpLegRollRField()
    RightUpLegRollRx = RightUpLegRollR.RightUpLegRollRx
    RightUpLegRollRy = RightUpLegRollR.RightUpLegRollRy
    RightUpLegRollRz = RightUpLegRollR.RightUpLegRollRz

    RightUpLegRollS = RightUpLegRollSField()
    RightUpLegRollSx = RightUpLegRollS.RightUpLegRollSx
    RightUpLegRollSy = RightUpLegRollS.RightUpLegRollSy
    RightUpLegRollSz = RightUpLegRollS.RightUpLegRollSz

    RightLegRollT = RightLegRollTField()
    RightLegRollTx = RightLegRollT.RightLegRollTx
    RightLegRollTy = RightLegRollT.RightLegRollTy
    RightLegRollTz = RightLegRollT.RightLegRollTz

    RightLegRollR = RightLegRollRField()
    RightLegRollRx = RightLegRollR.RightLegRollRx
    RightLegRollRy = RightLegRollR.RightLegRollRy
    RightLegRollRz = RightLegRollR.RightLegRollRz

    RightLegRollS = RightLegRollSField()
    RightLegRollSx = RightLegRollS.RightLegRollSx
    RightLegRollSy = RightLegRollS.RightLegRollSy
    RightLegRollSz = RightLegRollS.RightLegRollSz

    LeftArmRollT = LeftArmRollTField()
    LeftArmRollTx = LeftArmRollT.LeftArmRollTx
    LeftArmRollTy = LeftArmRollT.LeftArmRollTy
    LeftArmRollTz = LeftArmRollT.LeftArmRollTz

    LeftArmRollR = LeftArmRollRField()
    LeftArmRollRx = LeftArmRollR.LeftArmRollRx
    LeftArmRollRy = LeftArmRollR.LeftArmRollRy
    LeftArmRollRz = LeftArmRollR.LeftArmRollRz

    LeftArmRollS = LeftArmRollSField()
    LeftArmRollSx = LeftArmRollS.LeftArmRollSx
    LeftArmRollSy = LeftArmRollS.LeftArmRollSy
    LeftArmRollSz = LeftArmRollS.LeftArmRollSz

    LeftForeArmRollT = LeftForeArmRollTField()
    LeftForeArmRollTx = LeftForeArmRollT.LeftForeArmRollTx
    LeftForeArmRollTy = LeftForeArmRollT.LeftForeArmRollTy
    LeftForeArmRollTz = LeftForeArmRollT.LeftForeArmRollTz

    LeftForeArmRollR = LeftForeArmRollRField()
    LeftForeArmRollRx = LeftForeArmRollR.LeftForeArmRollRx
    LeftForeArmRollRy = LeftForeArmRollR.LeftForeArmRollRy
    LeftForeArmRollRz = LeftForeArmRollR.LeftForeArmRollRz

    LeftForeArmRollS = LeftForeArmRollSField()
    LeftForeArmRollSx = LeftForeArmRollS.LeftForeArmRollSx
    LeftForeArmRollSy = LeftForeArmRollS.LeftForeArmRollSy
    LeftForeArmRollSz = LeftForeArmRollS.LeftForeArmRollSz

    RightArmRollT = RightArmRollTField()
    RightArmRollTx = RightArmRollT.RightArmRollTx
    RightArmRollTy = RightArmRollT.RightArmRollTy
    RightArmRollTz = RightArmRollT.RightArmRollTz

    RightArmRollR = RightArmRollRField()
    RightArmRollRx = RightArmRollR.RightArmRollRx
    RightArmRollRy = RightArmRollR.RightArmRollRy
    RightArmRollRz = RightArmRollR.RightArmRollRz

    RightArmRollS = RightArmRollSField()
    RightArmRollSx = RightArmRollS.RightArmRollSx
    RightArmRollSy = RightArmRollS.RightArmRollSy
    RightArmRollSz = RightArmRollS.RightArmRollSz

    RightForeArmRollT = RightForeArmRollTField()
    RightForeArmRollTx = RightForeArmRollT.RightForeArmRollTx
    RightForeArmRollTy = RightForeArmRollT.RightForeArmRollTy
    RightForeArmRollTz = RightForeArmRollT.RightForeArmRollTz

    RightForeArmRollR = RightForeArmRollRField()
    RightForeArmRollRx = RightForeArmRollR.RightForeArmRollRx
    RightForeArmRollRy = RightForeArmRollR.RightForeArmRollRy
    RightForeArmRollRz = RightForeArmRollR.RightForeArmRollRz

    RightForeArmRollS = RightForeArmRollSField()
    RightForeArmRollSx = RightForeArmRollS.RightForeArmRollSx
    RightForeArmRollSy = RightForeArmRollS.RightForeArmRollSy
    RightForeArmRollSz = RightForeArmRollS.RightForeArmRollSz

    HipsTranslationT = HipsTranslationTField()
    HipsTranslationTx = HipsTranslationT.HipsTranslationTx
    HipsTranslationTy = HipsTranslationT.HipsTranslationTy
    HipsTranslationTz = HipsTranslationT.HipsTranslationTz

    HipsTranslationR = HipsTranslationRField()
    HipsTranslationRx = HipsTranslationR.HipsTranslationRx
    HipsTranslationRy = HipsTranslationR.HipsTranslationRy
    HipsTranslationRz = HipsTranslationR.HipsTranslationRz

    HipsTranslationS = HipsTranslationSField()
    HipsTranslationSx = HipsTranslationS.HipsTranslationSx
    HipsTranslationSy = HipsTranslationS.HipsTranslationSy
    HipsTranslationSz = HipsTranslationS.HipsTranslationSz

    LeftHandThumb1T = LeftHandThumb1TField()
    LeftHandThumb1Tx = LeftHandThumb1T.LeftHandThumb1Tx
    LeftHandThumb1Ty = LeftHandThumb1T.LeftHandThumb1Ty
    LeftHandThumb1Tz = LeftHandThumb1T.LeftHandThumb1Tz

    LeftHandThumb1R = LeftHandThumb1RField()
    LeftHandThumb1Rx = LeftHandThumb1R.LeftHandThumb1Rx
    LeftHandThumb1Ry = LeftHandThumb1R.LeftHandThumb1Ry
    LeftHandThumb1Rz = LeftHandThumb1R.LeftHandThumb1Rz

    LeftHandThumb1S = LeftHandThumb1SField()
    LeftHandThumb1Sx = LeftHandThumb1S.LeftHandThumb1Sx
    LeftHandThumb1Sy = LeftHandThumb1S.LeftHandThumb1Sy
    LeftHandThumb1Sz = LeftHandThumb1S.LeftHandThumb1Sz

    LeftHandThumb2T = LeftHandThumb2TField()
    LeftHandThumb2Tx = LeftHandThumb2T.LeftHandThumb2Tx
    LeftHandThumb2Ty = LeftHandThumb2T.LeftHandThumb2Ty
    LeftHandThumb2Tz = LeftHandThumb2T.LeftHandThumb2Tz

    LeftHandThumb2R = LeftHandThumb2RField()
    LeftHandThumb2Rx = LeftHandThumb2R.LeftHandThumb2Rx
    LeftHandThumb2Ry = LeftHandThumb2R.LeftHandThumb2Ry
    LeftHandThumb2Rz = LeftHandThumb2R.LeftHandThumb2Rz

    LeftHandThumb2S = LeftHandThumb2SField()
    LeftHandThumb2Sx = LeftHandThumb2S.LeftHandThumb2Sx
    LeftHandThumb2Sy = LeftHandThumb2S.LeftHandThumb2Sy
    LeftHandThumb2Sz = LeftHandThumb2S.LeftHandThumb2Sz

    LeftHandThumb3T = LeftHandThumb3TField()
    LeftHandThumb3Tx = LeftHandThumb3T.LeftHandThumb3Tx
    LeftHandThumb3Ty = LeftHandThumb3T.LeftHandThumb3Ty
    LeftHandThumb3Tz = LeftHandThumb3T.LeftHandThumb3Tz

    LeftHandThumb3R = LeftHandThumb3RField()
    LeftHandThumb3Rx = LeftHandThumb3R.LeftHandThumb3Rx
    LeftHandThumb3Ry = LeftHandThumb3R.LeftHandThumb3Ry
    LeftHandThumb3Rz = LeftHandThumb3R.LeftHandThumb3Rz

    LeftHandThumb3S = LeftHandThumb3SField()
    LeftHandThumb3Sx = LeftHandThumb3S.LeftHandThumb3Sx
    LeftHandThumb3Sy = LeftHandThumb3S.LeftHandThumb3Sy
    LeftHandThumb3Sz = LeftHandThumb3S.LeftHandThumb3Sz

    LeftHandThumb4T = LeftHandThumb4TField()
    LeftHandThumb4Tx = LeftHandThumb4T.LeftHandThumb4Tx
    LeftHandThumb4Ty = LeftHandThumb4T.LeftHandThumb4Ty
    LeftHandThumb4Tz = LeftHandThumb4T.LeftHandThumb4Tz

    LeftHandThumb4R = LeftHandThumb4RField()
    LeftHandThumb4Rx = LeftHandThumb4R.LeftHandThumb4Rx
    LeftHandThumb4Ry = LeftHandThumb4R.LeftHandThumb4Ry
    LeftHandThumb4Rz = LeftHandThumb4R.LeftHandThumb4Rz

    LeftHandThumb4S = LeftHandThumb4SField()
    LeftHandThumb4Sx = LeftHandThumb4S.LeftHandThumb4Sx
    LeftHandThumb4Sy = LeftHandThumb4S.LeftHandThumb4Sy
    LeftHandThumb4Sz = LeftHandThumb4S.LeftHandThumb4Sz

    LeftHandIndex1T = LeftHandIndex1TField()
    LeftHandIndex1Tx = LeftHandIndex1T.LeftHandIndex1Tx
    LeftHandIndex1Ty = LeftHandIndex1T.LeftHandIndex1Ty
    LeftHandIndex1Tz = LeftHandIndex1T.LeftHandIndex1Tz

    LeftHandIndex1R = LeftHandIndex1RField()
    LeftHandIndex1Rx = LeftHandIndex1R.LeftHandIndex1Rx
    LeftHandIndex1Ry = LeftHandIndex1R.LeftHandIndex1Ry
    LeftHandIndex1Rz = LeftHandIndex1R.LeftHandIndex1Rz

    LeftHandIndex1S = LeftHandIndex1SField()
    LeftHandIndex1Sx = LeftHandIndex1S.LeftHandIndex1Sx
    LeftHandIndex1Sy = LeftHandIndex1S.LeftHandIndex1Sy
    LeftHandIndex1Sz = LeftHandIndex1S.LeftHandIndex1Sz

    LeftHandIndex2T = LeftHandIndex2TField()
    LeftHandIndex2Tx = LeftHandIndex2T.LeftHandIndex2Tx
    LeftHandIndex2Ty = LeftHandIndex2T.LeftHandIndex2Ty
    LeftHandIndex2Tz = LeftHandIndex2T.LeftHandIndex2Tz

    LeftHandIndex2R = LeftHandIndex2RField()
    LeftHandIndex2Rx = LeftHandIndex2R.LeftHandIndex2Rx
    LeftHandIndex2Ry = LeftHandIndex2R.LeftHandIndex2Ry
    LeftHandIndex2Rz = LeftHandIndex2R.LeftHandIndex2Rz

    LeftHandIndex2S = LeftHandIndex2SField()
    LeftHandIndex2Sx = LeftHandIndex2S.LeftHandIndex2Sx
    LeftHandIndex2Sy = LeftHandIndex2S.LeftHandIndex2Sy
    LeftHandIndex2Sz = LeftHandIndex2S.LeftHandIndex2Sz

    LeftHandIndex3T = LeftHandIndex3TField()
    LeftHandIndex3Tx = LeftHandIndex3T.LeftHandIndex3Tx
    LeftHandIndex3Ty = LeftHandIndex3T.LeftHandIndex3Ty
    LeftHandIndex3Tz = LeftHandIndex3T.LeftHandIndex3Tz

    LeftHandIndex3R = LeftHandIndex3RField()
    LeftHandIndex3Rx = LeftHandIndex3R.LeftHandIndex3Rx
    LeftHandIndex3Ry = LeftHandIndex3R.LeftHandIndex3Ry
    LeftHandIndex3Rz = LeftHandIndex3R.LeftHandIndex3Rz

    LeftHandIndex3S = LeftHandIndex3SField()
    LeftHandIndex3Sx = LeftHandIndex3S.LeftHandIndex3Sx
    LeftHandIndex3Sy = LeftHandIndex3S.LeftHandIndex3Sy
    LeftHandIndex3Sz = LeftHandIndex3S.LeftHandIndex3Sz

    LeftHandIndex4T = LeftHandIndex4TField()
    LeftHandIndex4Tx = LeftHandIndex4T.LeftHandIndex4Tx
    LeftHandIndex4Ty = LeftHandIndex4T.LeftHandIndex4Ty
    LeftHandIndex4Tz = LeftHandIndex4T.LeftHandIndex4Tz

    LeftHandIndex4R = LeftHandIndex4RField()
    LeftHandIndex4Rx = LeftHandIndex4R.LeftHandIndex4Rx
    LeftHandIndex4Ry = LeftHandIndex4R.LeftHandIndex4Ry
    LeftHandIndex4Rz = LeftHandIndex4R.LeftHandIndex4Rz

    LeftHandIndex4S = LeftHandIndex4SField()
    LeftHandIndex4Sx = LeftHandIndex4S.LeftHandIndex4Sx
    LeftHandIndex4Sy = LeftHandIndex4S.LeftHandIndex4Sy
    LeftHandIndex4Sz = LeftHandIndex4S.LeftHandIndex4Sz

    LeftHandMiddle1T = LeftHandMiddle1TField()
    LeftHandMiddle1Tx = LeftHandMiddle1T.LeftHandMiddle1Tx
    LeftHandMiddle1Ty = LeftHandMiddle1T.LeftHandMiddle1Ty
    LeftHandMiddle1Tz = LeftHandMiddle1T.LeftHandMiddle1Tz

    LeftHandMiddle1R = LeftHandMiddle1RField()
    LeftHandMiddle1Rx = LeftHandMiddle1R.LeftHandMiddle1Rx
    LeftHandMiddle1Ry = LeftHandMiddle1R.LeftHandMiddle1Ry
    LeftHandMiddle1Rz = LeftHandMiddle1R.LeftHandMiddle1Rz

    LeftHandMiddle1S = LeftHandMiddle1SField()
    LeftHandMiddle1Sx = LeftHandMiddle1S.LeftHandMiddle1Sx
    LeftHandMiddle1Sy = LeftHandMiddle1S.LeftHandMiddle1Sy
    LeftHandMiddle1Sz = LeftHandMiddle1S.LeftHandMiddle1Sz

    LeftHandMiddle2T = LeftHandMiddle2TField()
    LeftHandMiddle2Tx = LeftHandMiddle2T.LeftHandMiddle2Tx
    LeftHandMiddle2Ty = LeftHandMiddle2T.LeftHandMiddle2Ty
    LeftHandMiddle2Tz = LeftHandMiddle2T.LeftHandMiddle2Tz

    LeftHandMiddle2R = LeftHandMiddle2RField()
    LeftHandMiddle2Rx = LeftHandMiddle2R.LeftHandMiddle2Rx
    LeftHandMiddle2Ry = LeftHandMiddle2R.LeftHandMiddle2Ry
    LeftHandMiddle2Rz = LeftHandMiddle2R.LeftHandMiddle2Rz

    LeftHandMiddle2S = LeftHandMiddle2SField()
    LeftHandMiddle2Sx = LeftHandMiddle2S.LeftHandMiddle2Sx
    LeftHandMiddle2Sy = LeftHandMiddle2S.LeftHandMiddle2Sy
    LeftHandMiddle2Sz = LeftHandMiddle2S.LeftHandMiddle2Sz

    LeftHandMiddle3T = LeftHandMiddle3TField()
    LeftHandMiddle3Tx = LeftHandMiddle3T.LeftHandMiddle3Tx
    LeftHandMiddle3Ty = LeftHandMiddle3T.LeftHandMiddle3Ty
    LeftHandMiddle3Tz = LeftHandMiddle3T.LeftHandMiddle3Tz

    LeftHandMiddle3R = LeftHandMiddle3RField()
    LeftHandMiddle3Rx = LeftHandMiddle3R.LeftHandMiddle3Rx
    LeftHandMiddle3Ry = LeftHandMiddle3R.LeftHandMiddle3Ry
    LeftHandMiddle3Rz = LeftHandMiddle3R.LeftHandMiddle3Rz

    LeftHandMiddle3S = LeftHandMiddle3SField()
    LeftHandMiddle3Sx = LeftHandMiddle3S.LeftHandMiddle3Sx
    LeftHandMiddle3Sy = LeftHandMiddle3S.LeftHandMiddle3Sy
    LeftHandMiddle3Sz = LeftHandMiddle3S.LeftHandMiddle3Sz

    LeftHandMiddle4T = LeftHandMiddle4TField()
    LeftHandMiddle4Tx = LeftHandMiddle4T.LeftHandMiddle4Tx
    LeftHandMiddle4Ty = LeftHandMiddle4T.LeftHandMiddle4Ty
    LeftHandMiddle4Tz = LeftHandMiddle4T.LeftHandMiddle4Tz

    LeftHandMiddle4R = LeftHandMiddle4RField()
    LeftHandMiddle4Rx = LeftHandMiddle4R.LeftHandMiddle4Rx
    LeftHandMiddle4Ry = LeftHandMiddle4R.LeftHandMiddle4Ry
    LeftHandMiddle4Rz = LeftHandMiddle4R.LeftHandMiddle4Rz

    LeftHandMiddle4S = LeftHandMiddle4SField()
    LeftHandMiddle4Sx = LeftHandMiddle4S.LeftHandMiddle4Sx
    LeftHandMiddle4Sy = LeftHandMiddle4S.LeftHandMiddle4Sy
    LeftHandMiddle4Sz = LeftHandMiddle4S.LeftHandMiddle4Sz

    LeftHandRing1T = LeftHandRing1TField()
    LeftHandRing1Tx = LeftHandRing1T.LeftHandRing1Tx
    LeftHandRing1Ty = LeftHandRing1T.LeftHandRing1Ty
    LeftHandRing1Tz = LeftHandRing1T.LeftHandRing1Tz

    LeftHandRing1R = LeftHandRing1RField()
    LeftHandRing1Rx = LeftHandRing1R.LeftHandRing1Rx
    LeftHandRing1Ry = LeftHandRing1R.LeftHandRing1Ry
    LeftHandRing1Rz = LeftHandRing1R.LeftHandRing1Rz

    LeftHandRing1S = LeftHandRing1SField()
    LeftHandRing1Sx = LeftHandRing1S.LeftHandRing1Sx
    LeftHandRing1Sy = LeftHandRing1S.LeftHandRing1Sy
    LeftHandRing1Sz = LeftHandRing1S.LeftHandRing1Sz

    LeftHandRing2T = LeftHandRing2TField()
    LeftHandRing2Tx = LeftHandRing2T.LeftHandRing2Tx
    LeftHandRing2Ty = LeftHandRing2T.LeftHandRing2Ty
    LeftHandRing2Tz = LeftHandRing2T.LeftHandRing2Tz

    LeftHandRing2R = LeftHandRing2RField()
    LeftHandRing2Rx = LeftHandRing2R.LeftHandRing2Rx
    LeftHandRing2Ry = LeftHandRing2R.LeftHandRing2Ry
    LeftHandRing2Rz = LeftHandRing2R.LeftHandRing2Rz

    LeftHandRing2S = LeftHandRing2SField()
    LeftHandRing2Sx = LeftHandRing2S.LeftHandRing2Sx
    LeftHandRing2Sy = LeftHandRing2S.LeftHandRing2Sy
    LeftHandRing2Sz = LeftHandRing2S.LeftHandRing2Sz

    LeftHandRing3T = LeftHandRing3TField()
    LeftHandRing3Tx = LeftHandRing3T.LeftHandRing3Tx
    LeftHandRing3Ty = LeftHandRing3T.LeftHandRing3Ty
    LeftHandRing3Tz = LeftHandRing3T.LeftHandRing3Tz

    LeftHandRing3R = LeftHandRing3RField()
    LeftHandRing3Rx = LeftHandRing3R.LeftHandRing3Rx
    LeftHandRing3Ry = LeftHandRing3R.LeftHandRing3Ry
    LeftHandRing3Rz = LeftHandRing3R.LeftHandRing3Rz

    LeftHandRing3S = LeftHandRing3SField()
    LeftHandRing3Sx = LeftHandRing3S.LeftHandRing3Sx
    LeftHandRing3Sy = LeftHandRing3S.LeftHandRing3Sy
    LeftHandRing3Sz = LeftHandRing3S.LeftHandRing3Sz

    LeftHandRing4T = LeftHandRing4TField()
    LeftHandRing4Tx = LeftHandRing4T.LeftHandRing4Tx
    LeftHandRing4Ty = LeftHandRing4T.LeftHandRing4Ty
    LeftHandRing4Tz = LeftHandRing4T.LeftHandRing4Tz

    LeftHandRing4R = LeftHandRing4RField()
    LeftHandRing4Rx = LeftHandRing4R.LeftHandRing4Rx
    LeftHandRing4Ry = LeftHandRing4R.LeftHandRing4Ry
    LeftHandRing4Rz = LeftHandRing4R.LeftHandRing4Rz

    LeftHandRing4S = LeftHandRing4SField()
    LeftHandRing4Sx = LeftHandRing4S.LeftHandRing4Sx
    LeftHandRing4Sy = LeftHandRing4S.LeftHandRing4Sy
    LeftHandRing4Sz = LeftHandRing4S.LeftHandRing4Sz

    LeftHandPinky1T = LeftHandPinky1TField()
    LeftHandPinky1Tx = LeftHandPinky1T.LeftHandPinky1Tx
    LeftHandPinky1Ty = LeftHandPinky1T.LeftHandPinky1Ty
    LeftHandPinky1Tz = LeftHandPinky1T.LeftHandPinky1Tz

    LeftHandPinky1R = LeftHandPinky1RField()
    LeftHandPinky1Rx = LeftHandPinky1R.LeftHandPinky1Rx
    LeftHandPinky1Ry = LeftHandPinky1R.LeftHandPinky1Ry
    LeftHandPinky1Rz = LeftHandPinky1R.LeftHandPinky1Rz

    LeftHandPinky1S = LeftHandPinky1SField()
    LeftHandPinky1Sx = LeftHandPinky1S.LeftHandPinky1Sx
    LeftHandPinky1Sy = LeftHandPinky1S.LeftHandPinky1Sy
    LeftHandPinky1Sz = LeftHandPinky1S.LeftHandPinky1Sz

    LeftHandPinky2T = LeftHandPinky2TField()
    LeftHandPinky2Tx = LeftHandPinky2T.LeftHandPinky2Tx
    LeftHandPinky2Ty = LeftHandPinky2T.LeftHandPinky2Ty
    LeftHandPinky2Tz = LeftHandPinky2T.LeftHandPinky2Tz

    LeftHandPinky2R = LeftHandPinky2RField()
    LeftHandPinky2Rx = LeftHandPinky2R.LeftHandPinky2Rx
    LeftHandPinky2Ry = LeftHandPinky2R.LeftHandPinky2Ry
    LeftHandPinky2Rz = LeftHandPinky2R.LeftHandPinky2Rz

    LeftHandPinky2S = LeftHandPinky2SField()
    LeftHandPinky2Sx = LeftHandPinky2S.LeftHandPinky2Sx
    LeftHandPinky2Sy = LeftHandPinky2S.LeftHandPinky2Sy
    LeftHandPinky2Sz = LeftHandPinky2S.LeftHandPinky2Sz

    LeftHandPinky3T = LeftHandPinky3TField()
    LeftHandPinky3Tx = LeftHandPinky3T.LeftHandPinky3Tx
    LeftHandPinky3Ty = LeftHandPinky3T.LeftHandPinky3Ty
    LeftHandPinky3Tz = LeftHandPinky3T.LeftHandPinky3Tz

    LeftHandPinky3R = LeftHandPinky3RField()
    LeftHandPinky3Rx = LeftHandPinky3R.LeftHandPinky3Rx
    LeftHandPinky3Ry = LeftHandPinky3R.LeftHandPinky3Ry
    LeftHandPinky3Rz = LeftHandPinky3R.LeftHandPinky3Rz

    LeftHandPinky3S = LeftHandPinky3SField()
    LeftHandPinky3Sx = LeftHandPinky3S.LeftHandPinky3Sx
    LeftHandPinky3Sy = LeftHandPinky3S.LeftHandPinky3Sy
    LeftHandPinky3Sz = LeftHandPinky3S.LeftHandPinky3Sz

    LeftHandPinky4T = LeftHandPinky4TField()
    LeftHandPinky4Tx = LeftHandPinky4T.LeftHandPinky4Tx
    LeftHandPinky4Ty = LeftHandPinky4T.LeftHandPinky4Ty
    LeftHandPinky4Tz = LeftHandPinky4T.LeftHandPinky4Tz

    LeftHandPinky4R = LeftHandPinky4RField()
    LeftHandPinky4Rx = LeftHandPinky4R.LeftHandPinky4Rx
    LeftHandPinky4Ry = LeftHandPinky4R.LeftHandPinky4Ry
    LeftHandPinky4Rz = LeftHandPinky4R.LeftHandPinky4Rz

    LeftHandPinky4S = LeftHandPinky4SField()
    LeftHandPinky4Sx = LeftHandPinky4S.LeftHandPinky4Sx
    LeftHandPinky4Sy = LeftHandPinky4S.LeftHandPinky4Sy
    LeftHandPinky4Sz = LeftHandPinky4S.LeftHandPinky4Sz

    LeftHandExtraFinger1T = LeftHandExtraFinger1TField()
    LeftHandExtraFinger1Tx = LeftHandExtraFinger1T.LeftHandExtraFinger1Tx
    LeftHandExtraFinger1Ty = LeftHandExtraFinger1T.LeftHandExtraFinger1Ty
    LeftHandExtraFinger1Tz = LeftHandExtraFinger1T.LeftHandExtraFinger1Tz

    LeftHandExtraFinger1R = LeftHandExtraFinger1RField()
    LeftHandExtraFinger1Rx = LeftHandExtraFinger1R.LeftHandExtraFinger1Rx
    LeftHandExtraFinger1Ry = LeftHandExtraFinger1R.LeftHandExtraFinger1Ry
    LeftHandExtraFinger1Rz = LeftHandExtraFinger1R.LeftHandExtraFinger1Rz

    LeftHandExtraFinger1S = LeftHandExtraFinger1SField()
    LeftHandExtraFinger1Sx = LeftHandExtraFinger1S.LeftHandExtraFinger1Sx
    LeftHandExtraFinger1Sy = LeftHandExtraFinger1S.LeftHandExtraFinger1Sy
    LeftHandExtraFinger1Sz = LeftHandExtraFinger1S.LeftHandExtraFinger1Sz

    LeftHandExtraFinger2T = LeftHandExtraFinger2TField()
    LeftHandExtraFinger2Tx = LeftHandExtraFinger2T.LeftHandExtraFinger2Tx
    LeftHandExtraFinger2Ty = LeftHandExtraFinger2T.LeftHandExtraFinger2Ty
    LeftHandExtraFinger2Tz = LeftHandExtraFinger2T.LeftHandExtraFinger2Tz

    LeftHandExtraFinger2R = LeftHandExtraFinger2RField()
    LeftHandExtraFinger2Rx = LeftHandExtraFinger2R.LeftHandExtraFinger2Rx
    LeftHandExtraFinger2Ry = LeftHandExtraFinger2R.LeftHandExtraFinger2Ry
    LeftHandExtraFinger2Rz = LeftHandExtraFinger2R.LeftHandExtraFinger2Rz

    LeftHandExtraFinger2S = LeftHandExtraFinger2SField()
    LeftHandExtraFinger2Sx = LeftHandExtraFinger2S.LeftHandExtraFinger2Sx
    LeftHandExtraFinger2Sy = LeftHandExtraFinger2S.LeftHandExtraFinger2Sy
    LeftHandExtraFinger2Sz = LeftHandExtraFinger2S.LeftHandExtraFinger2Sz

    LeftHandExtraFinger3T = LeftHandExtraFinger3TField()
    LeftHandExtraFinger3Tx = LeftHandExtraFinger3T.LeftHandExtraFinger3Tx
    LeftHandExtraFinger3Ty = LeftHandExtraFinger3T.LeftHandExtraFinger3Ty
    LeftHandExtraFinger3Tz = LeftHandExtraFinger3T.LeftHandExtraFinger3Tz

    LeftHandExtraFinger3R = LeftHandExtraFinger3RField()
    LeftHandExtraFinger3Rx = LeftHandExtraFinger3R.LeftHandExtraFinger3Rx
    LeftHandExtraFinger3Ry = LeftHandExtraFinger3R.LeftHandExtraFinger3Ry
    LeftHandExtraFinger3Rz = LeftHandExtraFinger3R.LeftHandExtraFinger3Rz

    LeftHandExtraFinger3S = LeftHandExtraFinger3SField()
    LeftHandExtraFinger3Sx = LeftHandExtraFinger3S.LeftHandExtraFinger3Sx
    LeftHandExtraFinger3Sy = LeftHandExtraFinger3S.LeftHandExtraFinger3Sy
    LeftHandExtraFinger3Sz = LeftHandExtraFinger3S.LeftHandExtraFinger3Sz

    LeftHandExtraFinger4T = LeftHandExtraFinger4TField()
    LeftHandExtraFinger4Tx = LeftHandExtraFinger4T.LeftHandExtraFinger4Tx
    LeftHandExtraFinger4Ty = LeftHandExtraFinger4T.LeftHandExtraFinger4Ty
    LeftHandExtraFinger4Tz = LeftHandExtraFinger4T.LeftHandExtraFinger4Tz

    LeftHandExtraFinger4R = LeftHandExtraFinger4RField()
    LeftHandExtraFinger4Rx = LeftHandExtraFinger4R.LeftHandExtraFinger4Rx
    LeftHandExtraFinger4Ry = LeftHandExtraFinger4R.LeftHandExtraFinger4Ry
    LeftHandExtraFinger4Rz = LeftHandExtraFinger4R.LeftHandExtraFinger4Rz

    LeftHandExtraFinger4S = LeftHandExtraFinger4SField()
    LeftHandExtraFinger4Sx = LeftHandExtraFinger4S.LeftHandExtraFinger4Sx
    LeftHandExtraFinger4Sy = LeftHandExtraFinger4S.LeftHandExtraFinger4Sy
    LeftHandExtraFinger4Sz = LeftHandExtraFinger4S.LeftHandExtraFinger4Sz

    RightHandThumb1T = RightHandThumb1TField()
    RightHandThumb1Tx = RightHandThumb1T.RightHandThumb1Tx
    RightHandThumb1Ty = RightHandThumb1T.RightHandThumb1Ty
    RightHandThumb1Tz = RightHandThumb1T.RightHandThumb1Tz

    RightHandThumb1R = RightHandThumb1RField()
    RightHandThumb1Rx = RightHandThumb1R.RightHandThumb1Rx
    RightHandThumb1Ry = RightHandThumb1R.RightHandThumb1Ry
    RightHandThumb1Rz = RightHandThumb1R.RightHandThumb1Rz

    RightHandThumb1S = RightHandThumb1SField()
    RightHandThumb1Sx = RightHandThumb1S.RightHandThumb1Sx
    RightHandThumb1Sy = RightHandThumb1S.RightHandThumb1Sy
    RightHandThumb1Sz = RightHandThumb1S.RightHandThumb1Sz

    RightHandThumb2T = RightHandThumb2TField()
    RightHandThumb2Tx = RightHandThumb2T.RightHandThumb2Tx
    RightHandThumb2Ty = RightHandThumb2T.RightHandThumb2Ty
    RightHandThumb2Tz = RightHandThumb2T.RightHandThumb2Tz

    RightHandThumb2R = RightHandThumb2RField()
    RightHandThumb2Rx = RightHandThumb2R.RightHandThumb2Rx
    RightHandThumb2Ry = RightHandThumb2R.RightHandThumb2Ry
    RightHandThumb2Rz = RightHandThumb2R.RightHandThumb2Rz

    RightHandThumb2S = RightHandThumb2SField()
    RightHandThumb2Sx = RightHandThumb2S.RightHandThumb2Sx
    RightHandThumb2Sy = RightHandThumb2S.RightHandThumb2Sy
    RightHandThumb2Sz = RightHandThumb2S.RightHandThumb2Sz

    RightHandThumb3T = RightHandThumb3TField()
    RightHandThumb3Tx = RightHandThumb3T.RightHandThumb3Tx
    RightHandThumb3Ty = RightHandThumb3T.RightHandThumb3Ty
    RightHandThumb3Tz = RightHandThumb3T.RightHandThumb3Tz

    RightHandThumb3R = RightHandThumb3RField()
    RightHandThumb3Rx = RightHandThumb3R.RightHandThumb3Rx
    RightHandThumb3Ry = RightHandThumb3R.RightHandThumb3Ry
    RightHandThumb3Rz = RightHandThumb3R.RightHandThumb3Rz

    RightHandThumb3S = RightHandThumb3SField()
    RightHandThumb3Sx = RightHandThumb3S.RightHandThumb3Sx
    RightHandThumb3Sy = RightHandThumb3S.RightHandThumb3Sy
    RightHandThumb3Sz = RightHandThumb3S.RightHandThumb3Sz

    RightHandThumb4T = RightHandThumb4TField()
    RightHandThumb4Tx = RightHandThumb4T.RightHandThumb4Tx
    RightHandThumb4Ty = RightHandThumb4T.RightHandThumb4Ty
    RightHandThumb4Tz = RightHandThumb4T.RightHandThumb4Tz

    RightHandThumb4R = RightHandThumb4RField()
    RightHandThumb4Rx = RightHandThumb4R.RightHandThumb4Rx
    RightHandThumb4Ry = RightHandThumb4R.RightHandThumb4Ry
    RightHandThumb4Rz = RightHandThumb4R.RightHandThumb4Rz

    RightHandThumb4S = RightHandThumb4SField()
    RightHandThumb4Sx = RightHandThumb4S.RightHandThumb4Sx
    RightHandThumb4Sy = RightHandThumb4S.RightHandThumb4Sy
    RightHandThumb4Sz = RightHandThumb4S.RightHandThumb4Sz

    RightHandIndex1T = RightHandIndex1TField()
    RightHandIndex1Tx = RightHandIndex1T.RightHandIndex1Tx
    RightHandIndex1Ty = RightHandIndex1T.RightHandIndex1Ty
    RightHandIndex1Tz = RightHandIndex1T.RightHandIndex1Tz

    RightHandIndex1R = RightHandIndex1RField()
    RightHandIndex1Rx = RightHandIndex1R.RightHandIndex1Rx
    RightHandIndex1Ry = RightHandIndex1R.RightHandIndex1Ry
    RightHandIndex1Rz = RightHandIndex1R.RightHandIndex1Rz

    RightHandIndex1S = RightHandIndex1SField()
    RightHandIndex1Sx = RightHandIndex1S.RightHandIndex1Sx
    RightHandIndex1Sy = RightHandIndex1S.RightHandIndex1Sy
    RightHandIndex1Sz = RightHandIndex1S.RightHandIndex1Sz

    RightHandIndex2T = RightHandIndex2TField()
    RightHandIndex2Tx = RightHandIndex2T.RightHandIndex2Tx
    RightHandIndex2Ty = RightHandIndex2T.RightHandIndex2Ty
    RightHandIndex2Tz = RightHandIndex2T.RightHandIndex2Tz

    RightHandIndex2R = RightHandIndex2RField()
    RightHandIndex2Rx = RightHandIndex2R.RightHandIndex2Rx
    RightHandIndex2Ry = RightHandIndex2R.RightHandIndex2Ry
    RightHandIndex2Rz = RightHandIndex2R.RightHandIndex2Rz

    RightHandIndex2S = RightHandIndex2SField()
    RightHandIndex2Sx = RightHandIndex2S.RightHandIndex2Sx
    RightHandIndex2Sy = RightHandIndex2S.RightHandIndex2Sy
    RightHandIndex2Sz = RightHandIndex2S.RightHandIndex2Sz

    RightHandIndex3T = RightHandIndex3TField()
    RightHandIndex3Tx = RightHandIndex3T.RightHandIndex3Tx
    RightHandIndex3Ty = RightHandIndex3T.RightHandIndex3Ty
    RightHandIndex3Tz = RightHandIndex3T.RightHandIndex3Tz

    RightHandIndex3R = RightHandIndex3RField()
    RightHandIndex3Rx = RightHandIndex3R.RightHandIndex3Rx
    RightHandIndex3Ry = RightHandIndex3R.RightHandIndex3Ry
    RightHandIndex3Rz = RightHandIndex3R.RightHandIndex3Rz

    RightHandIndex3S = RightHandIndex3SField()
    RightHandIndex3Sx = RightHandIndex3S.RightHandIndex3Sx
    RightHandIndex3Sy = RightHandIndex3S.RightHandIndex3Sy
    RightHandIndex3Sz = RightHandIndex3S.RightHandIndex3Sz

    RightHandIndex4T = RightHandIndex4TField()
    RightHandIndex4Tx = RightHandIndex4T.RightHandIndex4Tx
    RightHandIndex4Ty = RightHandIndex4T.RightHandIndex4Ty
    RightHandIndex4Tz = RightHandIndex4T.RightHandIndex4Tz

    RightHandIndex4R = RightHandIndex4RField()
    RightHandIndex4Rx = RightHandIndex4R.RightHandIndex4Rx
    RightHandIndex4Ry = RightHandIndex4R.RightHandIndex4Ry
    RightHandIndex4Rz = RightHandIndex4R.RightHandIndex4Rz

    RightHandIndex4S = RightHandIndex4SField()
    RightHandIndex4Sx = RightHandIndex4S.RightHandIndex4Sx
    RightHandIndex4Sy = RightHandIndex4S.RightHandIndex4Sy
    RightHandIndex4Sz = RightHandIndex4S.RightHandIndex4Sz

    RightHandMiddle1T = RightHandMiddle1TField()
    RightHandMiddle1Tx = RightHandMiddle1T.RightHandMiddle1Tx
    RightHandMiddle1Ty = RightHandMiddle1T.RightHandMiddle1Ty
    RightHandMiddle1Tz = RightHandMiddle1T.RightHandMiddle1Tz

    RightHandMiddle1R = RightHandMiddle1RField()
    RightHandMiddle1Rx = RightHandMiddle1R.RightHandMiddle1Rx
    RightHandMiddle1Ry = RightHandMiddle1R.RightHandMiddle1Ry
    RightHandMiddle1Rz = RightHandMiddle1R.RightHandMiddle1Rz

    RightHandMiddle1S = RightHandMiddle1SField()
    RightHandMiddle1Sx = RightHandMiddle1S.RightHandMiddle1Sx
    RightHandMiddle1Sy = RightHandMiddle1S.RightHandMiddle1Sy
    RightHandMiddle1Sz = RightHandMiddle1S.RightHandMiddle1Sz

    RightHandMiddle2T = RightHandMiddle2TField()
    RightHandMiddle2Tx = RightHandMiddle2T.RightHandMiddle2Tx
    RightHandMiddle2Ty = RightHandMiddle2T.RightHandMiddle2Ty
    RightHandMiddle2Tz = RightHandMiddle2T.RightHandMiddle2Tz

    RightHandMiddle2R = RightHandMiddle2RField()
    RightHandMiddle2Rx = RightHandMiddle2R.RightHandMiddle2Rx
    RightHandMiddle2Ry = RightHandMiddle2R.RightHandMiddle2Ry
    RightHandMiddle2Rz = RightHandMiddle2R.RightHandMiddle2Rz

    RightHandMiddle2S = RightHandMiddle2SField()
    RightHandMiddle2Sx = RightHandMiddle2S.RightHandMiddle2Sx
    RightHandMiddle2Sy = RightHandMiddle2S.RightHandMiddle2Sy
    RightHandMiddle2Sz = RightHandMiddle2S.RightHandMiddle2Sz

    RightHandMiddle3T = RightHandMiddle3TField()
    RightHandMiddle3Tx = RightHandMiddle3T.RightHandMiddle3Tx
    RightHandMiddle3Ty = RightHandMiddle3T.RightHandMiddle3Ty
    RightHandMiddle3Tz = RightHandMiddle3T.RightHandMiddle3Tz

    RightHandMiddle3R = RightHandMiddle3RField()
    RightHandMiddle3Rx = RightHandMiddle3R.RightHandMiddle3Rx
    RightHandMiddle3Ry = RightHandMiddle3R.RightHandMiddle3Ry
    RightHandMiddle3Rz = RightHandMiddle3R.RightHandMiddle3Rz

    RightHandMiddle3S = RightHandMiddle3SField()
    RightHandMiddle3Sx = RightHandMiddle3S.RightHandMiddle3Sx
    RightHandMiddle3Sy = RightHandMiddle3S.RightHandMiddle3Sy
    RightHandMiddle3Sz = RightHandMiddle3S.RightHandMiddle3Sz

    RightHandMiddle4T = RightHandMiddle4TField()
    RightHandMiddle4Tx = RightHandMiddle4T.RightHandMiddle4Tx
    RightHandMiddle4Ty = RightHandMiddle4T.RightHandMiddle4Ty
    RightHandMiddle4Tz = RightHandMiddle4T.RightHandMiddle4Tz

    RightHandMiddle4R = RightHandMiddle4RField()
    RightHandMiddle4Rx = RightHandMiddle4R.RightHandMiddle4Rx
    RightHandMiddle4Ry = RightHandMiddle4R.RightHandMiddle4Ry
    RightHandMiddle4Rz = RightHandMiddle4R.RightHandMiddle4Rz

    RightHandMiddle4S = RightHandMiddle4SField()
    RightHandMiddle4Sx = RightHandMiddle4S.RightHandMiddle4Sx
    RightHandMiddle4Sy = RightHandMiddle4S.RightHandMiddle4Sy
    RightHandMiddle4Sz = RightHandMiddle4S.RightHandMiddle4Sz

    RightHandRing1T = RightHandRing1TField()
    RightHandRing1Tx = RightHandRing1T.RightHandRing1Tx
    RightHandRing1Ty = RightHandRing1T.RightHandRing1Ty
    RightHandRing1Tz = RightHandRing1T.RightHandRing1Tz

    RightHandRing1R = RightHandRing1RField()
    RightHandRing1Rx = RightHandRing1R.RightHandRing1Rx
    RightHandRing1Ry = RightHandRing1R.RightHandRing1Ry
    RightHandRing1Rz = RightHandRing1R.RightHandRing1Rz

    RightHandRing1S = RightHandRing1SField()
    RightHandRing1Sx = RightHandRing1S.RightHandRing1Sx
    RightHandRing1Sy = RightHandRing1S.RightHandRing1Sy
    RightHandRing1Sz = RightHandRing1S.RightHandRing1Sz

    RightHandRing2T = RightHandRing2TField()
    RightHandRing2Tx = RightHandRing2T.RightHandRing2Tx
    RightHandRing2Ty = RightHandRing2T.RightHandRing2Ty
    RightHandRing2Tz = RightHandRing2T.RightHandRing2Tz

    RightHandRing2R = RightHandRing2RField()
    RightHandRing2Rx = RightHandRing2R.RightHandRing2Rx
    RightHandRing2Ry = RightHandRing2R.RightHandRing2Ry
    RightHandRing2Rz = RightHandRing2R.RightHandRing2Rz

    RightHandRing2S = RightHandRing2SField()
    RightHandRing2Sx = RightHandRing2S.RightHandRing2Sx
    RightHandRing2Sy = RightHandRing2S.RightHandRing2Sy
    RightHandRing2Sz = RightHandRing2S.RightHandRing2Sz

    RightHandRing3T = RightHandRing3TField()
    RightHandRing3Tx = RightHandRing3T.RightHandRing3Tx
    RightHandRing3Ty = RightHandRing3T.RightHandRing3Ty
    RightHandRing3Tz = RightHandRing3T.RightHandRing3Tz

    RightHandRing3R = RightHandRing3RField()
    RightHandRing3Rx = RightHandRing3R.RightHandRing3Rx
    RightHandRing3Ry = RightHandRing3R.RightHandRing3Ry
    RightHandRing3Rz = RightHandRing3R.RightHandRing3Rz

    RightHandRing3S = RightHandRing3SField()
    RightHandRing3Sx = RightHandRing3S.RightHandRing3Sx
    RightHandRing3Sy = RightHandRing3S.RightHandRing3Sy
    RightHandRing3Sz = RightHandRing3S.RightHandRing3Sz

    RightHandRing4T = RightHandRing4TField()
    RightHandRing4Tx = RightHandRing4T.RightHandRing4Tx
    RightHandRing4Ty = RightHandRing4T.RightHandRing4Ty
    RightHandRing4Tz = RightHandRing4T.RightHandRing4Tz

    RightHandRing4R = RightHandRing4RField()
    RightHandRing4Rx = RightHandRing4R.RightHandRing4Rx
    RightHandRing4Ry = RightHandRing4R.RightHandRing4Ry
    RightHandRing4Rz = RightHandRing4R.RightHandRing4Rz

    RightHandRing4S = RightHandRing4SField()
    RightHandRing4Sx = RightHandRing4S.RightHandRing4Sx
    RightHandRing4Sy = RightHandRing4S.RightHandRing4Sy
    RightHandRing4Sz = RightHandRing4S.RightHandRing4Sz

    RightHandPinky1T = RightHandPinky1TField()
    RightHandPinky1Tx = RightHandPinky1T.RightHandPinky1Tx
    RightHandPinky1Ty = RightHandPinky1T.RightHandPinky1Ty
    RightHandPinky1Tz = RightHandPinky1T.RightHandPinky1Tz

    RightHandPinky1R = RightHandPinky1RField()
    RightHandPinky1Rx = RightHandPinky1R.RightHandPinky1Rx
    RightHandPinky1Ry = RightHandPinky1R.RightHandPinky1Ry
    RightHandPinky1Rz = RightHandPinky1R.RightHandPinky1Rz

    RightHandPinky1S = RightHandPinky1SField()
    RightHandPinky1Sx = RightHandPinky1S.RightHandPinky1Sx
    RightHandPinky1Sy = RightHandPinky1S.RightHandPinky1Sy
    RightHandPinky1Sz = RightHandPinky1S.RightHandPinky1Sz

    RightHandPinky2T = RightHandPinky2TField()
    RightHandPinky2Tx = RightHandPinky2T.RightHandPinky2Tx
    RightHandPinky2Ty = RightHandPinky2T.RightHandPinky2Ty
    RightHandPinky2Tz = RightHandPinky2T.RightHandPinky2Tz

    RightHandPinky2R = RightHandPinky2RField()
    RightHandPinky2Rx = RightHandPinky2R.RightHandPinky2Rx
    RightHandPinky2Ry = RightHandPinky2R.RightHandPinky2Ry
    RightHandPinky2Rz = RightHandPinky2R.RightHandPinky2Rz

    RightHandPinky2S = RightHandPinky2SField()
    RightHandPinky2Sx = RightHandPinky2S.RightHandPinky2Sx
    RightHandPinky2Sy = RightHandPinky2S.RightHandPinky2Sy
    RightHandPinky2Sz = RightHandPinky2S.RightHandPinky2Sz

    RightHandPinky3T = RightHandPinky3TField()
    RightHandPinky3Tx = RightHandPinky3T.RightHandPinky3Tx
    RightHandPinky3Ty = RightHandPinky3T.RightHandPinky3Ty
    RightHandPinky3Tz = RightHandPinky3T.RightHandPinky3Tz

    RightHandPinky3R = RightHandPinky3RField()
    RightHandPinky3Rx = RightHandPinky3R.RightHandPinky3Rx
    RightHandPinky3Ry = RightHandPinky3R.RightHandPinky3Ry
    RightHandPinky3Rz = RightHandPinky3R.RightHandPinky3Rz

    RightHandPinky3S = RightHandPinky3SField()
    RightHandPinky3Sx = RightHandPinky3S.RightHandPinky3Sx
    RightHandPinky3Sy = RightHandPinky3S.RightHandPinky3Sy
    RightHandPinky3Sz = RightHandPinky3S.RightHandPinky3Sz

    RightHandPinky4T = RightHandPinky4TField()
    RightHandPinky4Tx = RightHandPinky4T.RightHandPinky4Tx
    RightHandPinky4Ty = RightHandPinky4T.RightHandPinky4Ty
    RightHandPinky4Tz = RightHandPinky4T.RightHandPinky4Tz

    RightHandPinky4R = RightHandPinky4RField()
    RightHandPinky4Rx = RightHandPinky4R.RightHandPinky4Rx
    RightHandPinky4Ry = RightHandPinky4R.RightHandPinky4Ry
    RightHandPinky4Rz = RightHandPinky4R.RightHandPinky4Rz

    RightHandPinky4S = RightHandPinky4SField()
    RightHandPinky4Sx = RightHandPinky4S.RightHandPinky4Sx
    RightHandPinky4Sy = RightHandPinky4S.RightHandPinky4Sy
    RightHandPinky4Sz = RightHandPinky4S.RightHandPinky4Sz

    RightHandExtraFinger1T = RightHandExtraFinger1TField()
    RightHandExtraFinger1Tx = RightHandExtraFinger1T.RightHandExtraFinger1Tx
    RightHandExtraFinger1Ty = RightHandExtraFinger1T.RightHandExtraFinger1Ty
    RightHandExtraFinger1Tz = RightHandExtraFinger1T.RightHandExtraFinger1Tz

    RightHandExtraFinger1R = RightHandExtraFinger1RField()
    RightHandExtraFinger1Rx = RightHandExtraFinger1R.RightHandExtraFinger1Rx
    RightHandExtraFinger1Ry = RightHandExtraFinger1R.RightHandExtraFinger1Ry
    RightHandExtraFinger1Rz = RightHandExtraFinger1R.RightHandExtraFinger1Rz

    RightHandExtraFinger1S = RightHandExtraFinger1SField()
    RightHandExtraFinger1Sx = RightHandExtraFinger1S.RightHandExtraFinger1Sx
    RightHandExtraFinger1Sy = RightHandExtraFinger1S.RightHandExtraFinger1Sy
    RightHandExtraFinger1Sz = RightHandExtraFinger1S.RightHandExtraFinger1Sz

    RightHandExtraFinger2T = RightHandExtraFinger2TField()
    RightHandExtraFinger2Tx = RightHandExtraFinger2T.RightHandExtraFinger2Tx
    RightHandExtraFinger2Ty = RightHandExtraFinger2T.RightHandExtraFinger2Ty
    RightHandExtraFinger2Tz = RightHandExtraFinger2T.RightHandExtraFinger2Tz

    RightHandExtraFinger2R = RightHandExtraFinger2RField()
    RightHandExtraFinger2Rx = RightHandExtraFinger2R.RightHandExtraFinger2Rx
    RightHandExtraFinger2Ry = RightHandExtraFinger2R.RightHandExtraFinger2Ry
    RightHandExtraFinger2Rz = RightHandExtraFinger2R.RightHandExtraFinger2Rz

    RightHandExtraFinger2S = RightHandExtraFinger2SField()
    RightHandExtraFinger2Sx = RightHandExtraFinger2S.RightHandExtraFinger2Sx
    RightHandExtraFinger2Sy = RightHandExtraFinger2S.RightHandExtraFinger2Sy
    RightHandExtraFinger2Sz = RightHandExtraFinger2S.RightHandExtraFinger2Sz

    RightHandExtraFinger3T = RightHandExtraFinger3TField()
    RightHandExtraFinger3Tx = RightHandExtraFinger3T.RightHandExtraFinger3Tx
    RightHandExtraFinger3Ty = RightHandExtraFinger3T.RightHandExtraFinger3Ty
    RightHandExtraFinger3Tz = RightHandExtraFinger3T.RightHandExtraFinger3Tz

    RightHandExtraFinger3R = RightHandExtraFinger3RField()
    RightHandExtraFinger3Rx = RightHandExtraFinger3R.RightHandExtraFinger3Rx
    RightHandExtraFinger3Ry = RightHandExtraFinger3R.RightHandExtraFinger3Ry
    RightHandExtraFinger3Rz = RightHandExtraFinger3R.RightHandExtraFinger3Rz

    RightHandExtraFinger3S = RightHandExtraFinger3SField()
    RightHandExtraFinger3Sx = RightHandExtraFinger3S.RightHandExtraFinger3Sx
    RightHandExtraFinger3Sy = RightHandExtraFinger3S.RightHandExtraFinger3Sy
    RightHandExtraFinger3Sz = RightHandExtraFinger3S.RightHandExtraFinger3Sz

    RightHandExtraFinger4T = RightHandExtraFinger4TField()
    RightHandExtraFinger4Tx = RightHandExtraFinger4T.RightHandExtraFinger4Tx
    RightHandExtraFinger4Ty = RightHandExtraFinger4T.RightHandExtraFinger4Ty
    RightHandExtraFinger4Tz = RightHandExtraFinger4T.RightHandExtraFinger4Tz

    RightHandExtraFinger4R = RightHandExtraFinger4RField()
    RightHandExtraFinger4Rx = RightHandExtraFinger4R.RightHandExtraFinger4Rx
    RightHandExtraFinger4Ry = RightHandExtraFinger4R.RightHandExtraFinger4Ry
    RightHandExtraFinger4Rz = RightHandExtraFinger4R.RightHandExtraFinger4Rz

    RightHandExtraFinger4S = RightHandExtraFinger4SField()
    RightHandExtraFinger4Sx = RightHandExtraFinger4S.RightHandExtraFinger4Sx
    RightHandExtraFinger4Sy = RightHandExtraFinger4S.RightHandExtraFinger4Sy
    RightHandExtraFinger4Sz = RightHandExtraFinger4S.RightHandExtraFinger4Sz

    LeftFootThumb1T = LeftFootThumb1TField()
    LeftFootThumb1Tx = LeftFootThumb1T.LeftFootThumb1Tx
    LeftFootThumb1Ty = LeftFootThumb1T.LeftFootThumb1Ty
    LeftFootThumb1Tz = LeftFootThumb1T.LeftFootThumb1Tz

    LeftFootThumb1R = LeftFootThumb1RField()
    LeftFootThumb1Rx = LeftFootThumb1R.LeftFootThumb1Rx
    LeftFootThumb1Ry = LeftFootThumb1R.LeftFootThumb1Ry
    LeftFootThumb1Rz = LeftFootThumb1R.LeftFootThumb1Rz

    LeftFootThumb1S = LeftFootThumb1SField()
    LeftFootThumb1Sx = LeftFootThumb1S.LeftFootThumb1Sx
    LeftFootThumb1Sy = LeftFootThumb1S.LeftFootThumb1Sy
    LeftFootThumb1Sz = LeftFootThumb1S.LeftFootThumb1Sz

    LeftFootThumb2T = LeftFootThumb2TField()
    LeftFootThumb2Tx = LeftFootThumb2T.LeftFootThumb2Tx
    LeftFootThumb2Ty = LeftFootThumb2T.LeftFootThumb2Ty
    LeftFootThumb2Tz = LeftFootThumb2T.LeftFootThumb2Tz

    LeftFootThumb2R = LeftFootThumb2RField()
    LeftFootThumb2Rx = LeftFootThumb2R.LeftFootThumb2Rx
    LeftFootThumb2Ry = LeftFootThumb2R.LeftFootThumb2Ry
    LeftFootThumb2Rz = LeftFootThumb2R.LeftFootThumb2Rz

    LeftFootThumb2S = LeftFootThumb2SField()
    LeftFootThumb2Sx = LeftFootThumb2S.LeftFootThumb2Sx
    LeftFootThumb2Sy = LeftFootThumb2S.LeftFootThumb2Sy
    LeftFootThumb2Sz = LeftFootThumb2S.LeftFootThumb2Sz

    LeftFootThumb3T = LeftFootThumb3TField()
    LeftFootThumb3Tx = LeftFootThumb3T.LeftFootThumb3Tx
    LeftFootThumb3Ty = LeftFootThumb3T.LeftFootThumb3Ty
    LeftFootThumb3Tz = LeftFootThumb3T.LeftFootThumb3Tz

    LeftFootThumb3R = LeftFootThumb3RField()
    LeftFootThumb3Rx = LeftFootThumb3R.LeftFootThumb3Rx
    LeftFootThumb3Ry = LeftFootThumb3R.LeftFootThumb3Ry
    LeftFootThumb3Rz = LeftFootThumb3R.LeftFootThumb3Rz

    LeftFootThumb3S = LeftFootThumb3SField()
    LeftFootThumb3Sx = LeftFootThumb3S.LeftFootThumb3Sx
    LeftFootThumb3Sy = LeftFootThumb3S.LeftFootThumb3Sy
    LeftFootThumb3Sz = LeftFootThumb3S.LeftFootThumb3Sz

    LeftFootThumb4T = LeftFootThumb4TField()
    LeftFootThumb4Tx = LeftFootThumb4T.LeftFootThumb4Tx
    LeftFootThumb4Ty = LeftFootThumb4T.LeftFootThumb4Ty
    LeftFootThumb4Tz = LeftFootThumb4T.LeftFootThumb4Tz

    LeftFootThumb4R = LeftFootThumb4RField()
    LeftFootThumb4Rx = LeftFootThumb4R.LeftFootThumb4Rx
    LeftFootThumb4Ry = LeftFootThumb4R.LeftFootThumb4Ry
    LeftFootThumb4Rz = LeftFootThumb4R.LeftFootThumb4Rz

    LeftFootThumb4S = LeftFootThumb4SField()
    LeftFootThumb4Sx = LeftFootThumb4S.LeftFootThumb4Sx
    LeftFootThumb4Sy = LeftFootThumb4S.LeftFootThumb4Sy
    LeftFootThumb4Sz = LeftFootThumb4S.LeftFootThumb4Sz

    LeftFootIndex1T = LeftFootIndex1TField()
    LeftFootIndex1Tx = LeftFootIndex1T.LeftFootIndex1Tx
    LeftFootIndex1Ty = LeftFootIndex1T.LeftFootIndex1Ty
    LeftFootIndex1Tz = LeftFootIndex1T.LeftFootIndex1Tz

    LeftFootIndex1R = LeftFootIndex1RField()
    LeftFootIndex1Rx = LeftFootIndex1R.LeftFootIndex1Rx
    LeftFootIndex1Ry = LeftFootIndex1R.LeftFootIndex1Ry
    LeftFootIndex1Rz = LeftFootIndex1R.LeftFootIndex1Rz

    LeftFootIndex1S = LeftFootIndex1SField()
    LeftFootIndex1Sx = LeftFootIndex1S.LeftFootIndex1Sx
    LeftFootIndex1Sy = LeftFootIndex1S.LeftFootIndex1Sy
    LeftFootIndex1Sz = LeftFootIndex1S.LeftFootIndex1Sz

    LeftFootIndex2T = LeftFootIndex2TField()
    LeftFootIndex2Tx = LeftFootIndex2T.LeftFootIndex2Tx
    LeftFootIndex2Ty = LeftFootIndex2T.LeftFootIndex2Ty
    LeftFootIndex2Tz = LeftFootIndex2T.LeftFootIndex2Tz

    LeftFootIndex2R = LeftFootIndex2RField()
    LeftFootIndex2Rx = LeftFootIndex2R.LeftFootIndex2Rx
    LeftFootIndex2Ry = LeftFootIndex2R.LeftFootIndex2Ry
    LeftFootIndex2Rz = LeftFootIndex2R.LeftFootIndex2Rz

    LeftFootIndex2S = LeftFootIndex2SField()
    LeftFootIndex2Sx = LeftFootIndex2S.LeftFootIndex2Sx
    LeftFootIndex2Sy = LeftFootIndex2S.LeftFootIndex2Sy
    LeftFootIndex2Sz = LeftFootIndex2S.LeftFootIndex2Sz

    LeftFootIndex3T = LeftFootIndex3TField()
    LeftFootIndex3Tx = LeftFootIndex3T.LeftFootIndex3Tx
    LeftFootIndex3Ty = LeftFootIndex3T.LeftFootIndex3Ty
    LeftFootIndex3Tz = LeftFootIndex3T.LeftFootIndex3Tz

    LeftFootIndex3R = LeftFootIndex3RField()
    LeftFootIndex3Rx = LeftFootIndex3R.LeftFootIndex3Rx
    LeftFootIndex3Ry = LeftFootIndex3R.LeftFootIndex3Ry
    LeftFootIndex3Rz = LeftFootIndex3R.LeftFootIndex3Rz

    LeftFootIndex3S = LeftFootIndex3SField()
    LeftFootIndex3Sx = LeftFootIndex3S.LeftFootIndex3Sx
    LeftFootIndex3Sy = LeftFootIndex3S.LeftFootIndex3Sy
    LeftFootIndex3Sz = LeftFootIndex3S.LeftFootIndex3Sz

    LeftFootIndex4T = LeftFootIndex4TField()
    LeftFootIndex4Tx = LeftFootIndex4T.LeftFootIndex4Tx
    LeftFootIndex4Ty = LeftFootIndex4T.LeftFootIndex4Ty
    LeftFootIndex4Tz = LeftFootIndex4T.LeftFootIndex4Tz

    LeftFootIndex4R = LeftFootIndex4RField()
    LeftFootIndex4Rx = LeftFootIndex4R.LeftFootIndex4Rx
    LeftFootIndex4Ry = LeftFootIndex4R.LeftFootIndex4Ry
    LeftFootIndex4Rz = LeftFootIndex4R.LeftFootIndex4Rz

    LeftFootIndex4S = LeftFootIndex4SField()
    LeftFootIndex4Sx = LeftFootIndex4S.LeftFootIndex4Sx
    LeftFootIndex4Sy = LeftFootIndex4S.LeftFootIndex4Sy
    LeftFootIndex4Sz = LeftFootIndex4S.LeftFootIndex4Sz

    LeftFootMiddle1T = LeftFootMiddle1TField()
    LeftFootMiddle1Tx = LeftFootMiddle1T.LeftFootMiddle1Tx
    LeftFootMiddle1Ty = LeftFootMiddle1T.LeftFootMiddle1Ty
    LeftFootMiddle1Tz = LeftFootMiddle1T.LeftFootMiddle1Tz

    LeftFootMiddle1R = LeftFootMiddle1RField()
    LeftFootMiddle1Rx = LeftFootMiddle1R.LeftFootMiddle1Rx
    LeftFootMiddle1Ry = LeftFootMiddle1R.LeftFootMiddle1Ry
    LeftFootMiddle1Rz = LeftFootMiddle1R.LeftFootMiddle1Rz

    LeftFootMiddle1S = LeftFootMiddle1SField()
    LeftFootMiddle1Sx = LeftFootMiddle1S.LeftFootMiddle1Sx
    LeftFootMiddle1Sy = LeftFootMiddle1S.LeftFootMiddle1Sy
    LeftFootMiddle1Sz = LeftFootMiddle1S.LeftFootMiddle1Sz

    LeftFootMiddle2T = LeftFootMiddle2TField()
    LeftFootMiddle2Tx = LeftFootMiddle2T.LeftFootMiddle2Tx
    LeftFootMiddle2Ty = LeftFootMiddle2T.LeftFootMiddle2Ty
    LeftFootMiddle2Tz = LeftFootMiddle2T.LeftFootMiddle2Tz

    LeftFootMiddle2R = LeftFootMiddle2RField()
    LeftFootMiddle2Rx = LeftFootMiddle2R.LeftFootMiddle2Rx
    LeftFootMiddle2Ry = LeftFootMiddle2R.LeftFootMiddle2Ry
    LeftFootMiddle2Rz = LeftFootMiddle2R.LeftFootMiddle2Rz

    LeftFootMiddle2S = LeftFootMiddle2SField()
    LeftFootMiddle2Sx = LeftFootMiddle2S.LeftFootMiddle2Sx
    LeftFootMiddle2Sy = LeftFootMiddle2S.LeftFootMiddle2Sy
    LeftFootMiddle2Sz = LeftFootMiddle2S.LeftFootMiddle2Sz

    LeftFootMiddle3T = LeftFootMiddle3TField()
    LeftFootMiddle3Tx = LeftFootMiddle3T.LeftFootMiddle3Tx
    LeftFootMiddle3Ty = LeftFootMiddle3T.LeftFootMiddle3Ty
    LeftFootMiddle3Tz = LeftFootMiddle3T.LeftFootMiddle3Tz

    LeftFootMiddle3R = LeftFootMiddle3RField()
    LeftFootMiddle3Rx = LeftFootMiddle3R.LeftFootMiddle3Rx
    LeftFootMiddle3Ry = LeftFootMiddle3R.LeftFootMiddle3Ry
    LeftFootMiddle3Rz = LeftFootMiddle3R.LeftFootMiddle3Rz

    LeftFootMiddle3S = LeftFootMiddle3SField()
    LeftFootMiddle3Sx = LeftFootMiddle3S.LeftFootMiddle3Sx
    LeftFootMiddle3Sy = LeftFootMiddle3S.LeftFootMiddle3Sy
    LeftFootMiddle3Sz = LeftFootMiddle3S.LeftFootMiddle3Sz

    LeftFootMiddle4T = LeftFootMiddle4TField()
    LeftFootMiddle4Tx = LeftFootMiddle4T.LeftFootMiddle4Tx
    LeftFootMiddle4Ty = LeftFootMiddle4T.LeftFootMiddle4Ty
    LeftFootMiddle4Tz = LeftFootMiddle4T.LeftFootMiddle4Tz

    LeftFootMiddle4R = LeftFootMiddle4RField()
    LeftFootMiddle4Rx = LeftFootMiddle4R.LeftFootMiddle4Rx
    LeftFootMiddle4Ry = LeftFootMiddle4R.LeftFootMiddle4Ry
    LeftFootMiddle4Rz = LeftFootMiddle4R.LeftFootMiddle4Rz

    LeftFootMiddle4S = LeftFootMiddle4SField()
    LeftFootMiddle4Sx = LeftFootMiddle4S.LeftFootMiddle4Sx
    LeftFootMiddle4Sy = LeftFootMiddle4S.LeftFootMiddle4Sy
    LeftFootMiddle4Sz = LeftFootMiddle4S.LeftFootMiddle4Sz

    LeftFootRing1T = LeftFootRing1TField()
    LeftFootRing1Tx = LeftFootRing1T.LeftFootRing1Tx
    LeftFootRing1Ty = LeftFootRing1T.LeftFootRing1Ty
    LeftFootRing1Tz = LeftFootRing1T.LeftFootRing1Tz

    LeftFootRing1R = LeftFootRing1RField()
    LeftFootRing1Rx = LeftFootRing1R.LeftFootRing1Rx
    LeftFootRing1Ry = LeftFootRing1R.LeftFootRing1Ry
    LeftFootRing1Rz = LeftFootRing1R.LeftFootRing1Rz

    LeftFootRing1S = LeftFootRing1SField()
    LeftFootRing1Sx = LeftFootRing1S.LeftFootRing1Sx
    LeftFootRing1Sy = LeftFootRing1S.LeftFootRing1Sy
    LeftFootRing1Sz = LeftFootRing1S.LeftFootRing1Sz

    LeftFootRing2T = LeftFootRing2TField()
    LeftFootRing2Tx = LeftFootRing2T.LeftFootRing2Tx
    LeftFootRing2Ty = LeftFootRing2T.LeftFootRing2Ty
    LeftFootRing2Tz = LeftFootRing2T.LeftFootRing2Tz

    LeftFootRing2R = LeftFootRing2RField()
    LeftFootRing2Rx = LeftFootRing2R.LeftFootRing2Rx
    LeftFootRing2Ry = LeftFootRing2R.LeftFootRing2Ry
    LeftFootRing2Rz = LeftFootRing2R.LeftFootRing2Rz

    LeftFootRing2S = LeftFootRing2SField()
    LeftFootRing2Sx = LeftFootRing2S.LeftFootRing2Sx
    LeftFootRing2Sy = LeftFootRing2S.LeftFootRing2Sy
    LeftFootRing2Sz = LeftFootRing2S.LeftFootRing2Sz

    LeftFootRing3T = LeftFootRing3TField()
    LeftFootRing3Tx = LeftFootRing3T.LeftFootRing3Tx
    LeftFootRing3Ty = LeftFootRing3T.LeftFootRing3Ty
    LeftFootRing3Tz = LeftFootRing3T.LeftFootRing3Tz

    LeftFootRing3R = LeftFootRing3RField()
    LeftFootRing3Rx = LeftFootRing3R.LeftFootRing3Rx
    LeftFootRing3Ry = LeftFootRing3R.LeftFootRing3Ry
    LeftFootRing3Rz = LeftFootRing3R.LeftFootRing3Rz

    LeftFootRing3S = LeftFootRing3SField()
    LeftFootRing3Sx = LeftFootRing3S.LeftFootRing3Sx
    LeftFootRing3Sy = LeftFootRing3S.LeftFootRing3Sy
    LeftFootRing3Sz = LeftFootRing3S.LeftFootRing3Sz

    LeftFootRing4T = LeftFootRing4TField()
    LeftFootRing4Tx = LeftFootRing4T.LeftFootRing4Tx
    LeftFootRing4Ty = LeftFootRing4T.LeftFootRing4Ty
    LeftFootRing4Tz = LeftFootRing4T.LeftFootRing4Tz

    LeftFootRing4R = LeftFootRing4RField()
    LeftFootRing4Rx = LeftFootRing4R.LeftFootRing4Rx
    LeftFootRing4Ry = LeftFootRing4R.LeftFootRing4Ry
    LeftFootRing4Rz = LeftFootRing4R.LeftFootRing4Rz

    LeftFootRing4S = LeftFootRing4SField()
    LeftFootRing4Sx = LeftFootRing4S.LeftFootRing4Sx
    LeftFootRing4Sy = LeftFootRing4S.LeftFootRing4Sy
    LeftFootRing4Sz = LeftFootRing4S.LeftFootRing4Sz

    LeftFootPinky1T = LeftFootPinky1TField()
    LeftFootPinky1Tx = LeftFootPinky1T.LeftFootPinky1Tx
    LeftFootPinky1Ty = LeftFootPinky1T.LeftFootPinky1Ty
    LeftFootPinky1Tz = LeftFootPinky1T.LeftFootPinky1Tz

    LeftFootPinky1R = LeftFootPinky1RField()
    LeftFootPinky1Rx = LeftFootPinky1R.LeftFootPinky1Rx
    LeftFootPinky1Ry = LeftFootPinky1R.LeftFootPinky1Ry
    LeftFootPinky1Rz = LeftFootPinky1R.LeftFootPinky1Rz

    LeftFootPinky1S = LeftFootPinky1SField()
    LeftFootPinky1Sx = LeftFootPinky1S.LeftFootPinky1Sx
    LeftFootPinky1Sy = LeftFootPinky1S.LeftFootPinky1Sy
    LeftFootPinky1Sz = LeftFootPinky1S.LeftFootPinky1Sz

    LeftFootPinky2T = LeftFootPinky2TField()
    LeftFootPinky2Tx = LeftFootPinky2T.LeftFootPinky2Tx
    LeftFootPinky2Ty = LeftFootPinky2T.LeftFootPinky2Ty
    LeftFootPinky2Tz = LeftFootPinky2T.LeftFootPinky2Tz

    LeftFootPinky2R = LeftFootPinky2RField()
    LeftFootPinky2Rx = LeftFootPinky2R.LeftFootPinky2Rx
    LeftFootPinky2Ry = LeftFootPinky2R.LeftFootPinky2Ry
    LeftFootPinky2Rz = LeftFootPinky2R.LeftFootPinky2Rz

    LeftFootPinky2S = LeftFootPinky2SField()
    LeftFootPinky2Sx = LeftFootPinky2S.LeftFootPinky2Sx
    LeftFootPinky2Sy = LeftFootPinky2S.LeftFootPinky2Sy
    LeftFootPinky2Sz = LeftFootPinky2S.LeftFootPinky2Sz

    LeftFootPinky3T = LeftFootPinky3TField()
    LeftFootPinky3Tx = LeftFootPinky3T.LeftFootPinky3Tx
    LeftFootPinky3Ty = LeftFootPinky3T.LeftFootPinky3Ty
    LeftFootPinky3Tz = LeftFootPinky3T.LeftFootPinky3Tz

    LeftFootPinky3R = LeftFootPinky3RField()
    LeftFootPinky3Rx = LeftFootPinky3R.LeftFootPinky3Rx
    LeftFootPinky3Ry = LeftFootPinky3R.LeftFootPinky3Ry
    LeftFootPinky3Rz = LeftFootPinky3R.LeftFootPinky3Rz

    LeftFootPinky3S = LeftFootPinky3SField()
    LeftFootPinky3Sx = LeftFootPinky3S.LeftFootPinky3Sx
    LeftFootPinky3Sy = LeftFootPinky3S.LeftFootPinky3Sy
    LeftFootPinky3Sz = LeftFootPinky3S.LeftFootPinky3Sz

    LeftFootPinky4T = LeftFootPinky4TField()
    LeftFootPinky4Tx = LeftFootPinky4T.LeftFootPinky4Tx
    LeftFootPinky4Ty = LeftFootPinky4T.LeftFootPinky4Ty
    LeftFootPinky4Tz = LeftFootPinky4T.LeftFootPinky4Tz

    LeftFootPinky4R = LeftFootPinky4RField()
    LeftFootPinky4Rx = LeftFootPinky4R.LeftFootPinky4Rx
    LeftFootPinky4Ry = LeftFootPinky4R.LeftFootPinky4Ry
    LeftFootPinky4Rz = LeftFootPinky4R.LeftFootPinky4Rz

    LeftFootPinky4S = LeftFootPinky4SField()
    LeftFootPinky4Sx = LeftFootPinky4S.LeftFootPinky4Sx
    LeftFootPinky4Sy = LeftFootPinky4S.LeftFootPinky4Sy
    LeftFootPinky4Sz = LeftFootPinky4S.LeftFootPinky4Sz

    LeftFootExtraFinger1T = LeftFootExtraFinger1TField()
    LeftFootExtraFinger1Tx = LeftFootExtraFinger1T.LeftFootExtraFinger1Tx
    LeftFootExtraFinger1Ty = LeftFootExtraFinger1T.LeftFootExtraFinger1Ty
    LeftFootExtraFinger1Tz = LeftFootExtraFinger1T.LeftFootExtraFinger1Tz

    LeftFootExtraFinger1R = LeftFootExtraFinger1RField()
    LeftFootExtraFinger1Rx = LeftFootExtraFinger1R.LeftFootExtraFinger1Rx
    LeftFootExtraFinger1Ry = LeftFootExtraFinger1R.LeftFootExtraFinger1Ry
    LeftFootExtraFinger1Rz = LeftFootExtraFinger1R.LeftFootExtraFinger1Rz

    LeftFootExtraFinger1S = LeftFootExtraFinger1SField()
    LeftFootExtraFinger1Sx = LeftFootExtraFinger1S.LeftFootExtraFinger1Sx
    LeftFootExtraFinger1Sy = LeftFootExtraFinger1S.LeftFootExtraFinger1Sy
    LeftFootExtraFinger1Sz = LeftFootExtraFinger1S.LeftFootExtraFinger1Sz

    LeftFootExtraFinger2T = LeftFootExtraFinger2TField()
    LeftFootExtraFinger2Tx = LeftFootExtraFinger2T.LeftFootExtraFinger2Tx
    LeftFootExtraFinger2Ty = LeftFootExtraFinger2T.LeftFootExtraFinger2Ty
    LeftFootExtraFinger2Tz = LeftFootExtraFinger2T.LeftFootExtraFinger2Tz

    LeftFootExtraFinger2R = LeftFootExtraFinger2RField()
    LeftFootExtraFinger2Rx = LeftFootExtraFinger2R.LeftFootExtraFinger2Rx
    LeftFootExtraFinger2Ry = LeftFootExtraFinger2R.LeftFootExtraFinger2Ry
    LeftFootExtraFinger2Rz = LeftFootExtraFinger2R.LeftFootExtraFinger2Rz

    LeftFootExtraFinger2S = LeftFootExtraFinger2SField()
    LeftFootExtraFinger2Sx = LeftFootExtraFinger2S.LeftFootExtraFinger2Sx
    LeftFootExtraFinger2Sy = LeftFootExtraFinger2S.LeftFootExtraFinger2Sy
    LeftFootExtraFinger2Sz = LeftFootExtraFinger2S.LeftFootExtraFinger2Sz

    LeftFootExtraFinger3T = LeftFootExtraFinger3TField()
    LeftFootExtraFinger3Tx = LeftFootExtraFinger3T.LeftFootExtraFinger3Tx
    LeftFootExtraFinger3Ty = LeftFootExtraFinger3T.LeftFootExtraFinger3Ty
    LeftFootExtraFinger3Tz = LeftFootExtraFinger3T.LeftFootExtraFinger3Tz

    LeftFootExtraFinger3R = LeftFootExtraFinger3RField()
    LeftFootExtraFinger3Rx = LeftFootExtraFinger3R.LeftFootExtraFinger3Rx
    LeftFootExtraFinger3Ry = LeftFootExtraFinger3R.LeftFootExtraFinger3Ry
    LeftFootExtraFinger3Rz = LeftFootExtraFinger3R.LeftFootExtraFinger3Rz

    LeftFootExtraFinger3S = LeftFootExtraFinger3SField()
    LeftFootExtraFinger3Sx = LeftFootExtraFinger3S.LeftFootExtraFinger3Sx
    LeftFootExtraFinger3Sy = LeftFootExtraFinger3S.LeftFootExtraFinger3Sy
    LeftFootExtraFinger3Sz = LeftFootExtraFinger3S.LeftFootExtraFinger3Sz

    LeftFootExtraFinger4T = LeftFootExtraFinger4TField()
    LeftFootExtraFinger4Tx = LeftFootExtraFinger4T.LeftFootExtraFinger4Tx
    LeftFootExtraFinger4Ty = LeftFootExtraFinger4T.LeftFootExtraFinger4Ty
    LeftFootExtraFinger4Tz = LeftFootExtraFinger4T.LeftFootExtraFinger4Tz

    LeftFootExtraFinger4R = LeftFootExtraFinger4RField()
    LeftFootExtraFinger4Rx = LeftFootExtraFinger4R.LeftFootExtraFinger4Rx
    LeftFootExtraFinger4Ry = LeftFootExtraFinger4R.LeftFootExtraFinger4Ry
    LeftFootExtraFinger4Rz = LeftFootExtraFinger4R.LeftFootExtraFinger4Rz

    LeftFootExtraFinger4S = LeftFootExtraFinger4SField()
    LeftFootExtraFinger4Sx = LeftFootExtraFinger4S.LeftFootExtraFinger4Sx
    LeftFootExtraFinger4Sy = LeftFootExtraFinger4S.LeftFootExtraFinger4Sy
    LeftFootExtraFinger4Sz = LeftFootExtraFinger4S.LeftFootExtraFinger4Sz

    RightFootThumb1T = RightFootThumb1TField()
    RightFootThumb1Tx = RightFootThumb1T.RightFootThumb1Tx
    RightFootThumb1Ty = RightFootThumb1T.RightFootThumb1Ty
    RightFootThumb1Tz = RightFootThumb1T.RightFootThumb1Tz

    RightFootThumb1R = RightFootThumb1RField()
    RightFootThumb1Rx = RightFootThumb1R.RightFootThumb1Rx
    RightFootThumb1Ry = RightFootThumb1R.RightFootThumb1Ry
    RightFootThumb1Rz = RightFootThumb1R.RightFootThumb1Rz

    RightFootThumb1S = RightFootThumb1SField()
    RightFootThumb1Sx = RightFootThumb1S.RightFootThumb1Sx
    RightFootThumb1Sy = RightFootThumb1S.RightFootThumb1Sy
    RightFootThumb1Sz = RightFootThumb1S.RightFootThumb1Sz

    RightFootThumb2T = RightFootThumb2TField()
    RightFootThumb2Tx = RightFootThumb2T.RightFootThumb2Tx
    RightFootThumb2Ty = RightFootThumb2T.RightFootThumb2Ty
    RightFootThumb2Tz = RightFootThumb2T.RightFootThumb2Tz

    RightFootThumb2R = RightFootThumb2RField()
    RightFootThumb2Rx = RightFootThumb2R.RightFootThumb2Rx
    RightFootThumb2Ry = RightFootThumb2R.RightFootThumb2Ry
    RightFootThumb2Rz = RightFootThumb2R.RightFootThumb2Rz

    RightFootThumb2S = RightFootThumb2SField()
    RightFootThumb2Sx = RightFootThumb2S.RightFootThumb2Sx
    RightFootThumb2Sy = RightFootThumb2S.RightFootThumb2Sy
    RightFootThumb2Sz = RightFootThumb2S.RightFootThumb2Sz

    RightFootThumb3T = RightFootThumb3TField()
    RightFootThumb3Tx = RightFootThumb3T.RightFootThumb3Tx
    RightFootThumb3Ty = RightFootThumb3T.RightFootThumb3Ty
    RightFootThumb3Tz = RightFootThumb3T.RightFootThumb3Tz

    RightFootThumb3R = RightFootThumb3RField()
    RightFootThumb3Rx = RightFootThumb3R.RightFootThumb3Rx
    RightFootThumb3Ry = RightFootThumb3R.RightFootThumb3Ry
    RightFootThumb3Rz = RightFootThumb3R.RightFootThumb3Rz

    RightFootThumb3S = RightFootThumb3SField()
    RightFootThumb3Sx = RightFootThumb3S.RightFootThumb3Sx
    RightFootThumb3Sy = RightFootThumb3S.RightFootThumb3Sy
    RightFootThumb3Sz = RightFootThumb3S.RightFootThumb3Sz

    RightFootThumb4T = RightFootThumb4TField()
    RightFootThumb4Tx = RightFootThumb4T.RightFootThumb4Tx
    RightFootThumb4Ty = RightFootThumb4T.RightFootThumb4Ty
    RightFootThumb4Tz = RightFootThumb4T.RightFootThumb4Tz

    RightFootThumb4R = RightFootThumb4RField()
    RightFootThumb4Rx = RightFootThumb4R.RightFootThumb4Rx
    RightFootThumb4Ry = RightFootThumb4R.RightFootThumb4Ry
    RightFootThumb4Rz = RightFootThumb4R.RightFootThumb4Rz

    RightFootThumb4S = RightFootThumb4SField()
    RightFootThumb4Sx = RightFootThumb4S.RightFootThumb4Sx
    RightFootThumb4Sy = RightFootThumb4S.RightFootThumb4Sy
    RightFootThumb4Sz = RightFootThumb4S.RightFootThumb4Sz

    RightFootIndex1T = RightFootIndex1TField()
    RightFootIndex1Tx = RightFootIndex1T.RightFootIndex1Tx
    RightFootIndex1Ty = RightFootIndex1T.RightFootIndex1Ty
    RightFootIndex1Tz = RightFootIndex1T.RightFootIndex1Tz

    RightFootIndex1R = RightFootIndex1RField()
    RightFootIndex1Rx = RightFootIndex1R.RightFootIndex1Rx
    RightFootIndex1Ry = RightFootIndex1R.RightFootIndex1Ry
    RightFootIndex1Rz = RightFootIndex1R.RightFootIndex1Rz

    RightFootIndex1S = RightFootIndex1SField()
    RightFootIndex1Sx = RightFootIndex1S.RightFootIndex1Sx
    RightFootIndex1Sy = RightFootIndex1S.RightFootIndex1Sy
    RightFootIndex1Sz = RightFootIndex1S.RightFootIndex1Sz

    RightFootIndex2T = RightFootIndex2TField()
    RightFootIndex2Tx = RightFootIndex2T.RightFootIndex2Tx
    RightFootIndex2Ty = RightFootIndex2T.RightFootIndex2Ty
    RightFootIndex2Tz = RightFootIndex2T.RightFootIndex2Tz

    RightFootIndex2R = RightFootIndex2RField()
    RightFootIndex2Rx = RightFootIndex2R.RightFootIndex2Rx
    RightFootIndex2Ry = RightFootIndex2R.RightFootIndex2Ry
    RightFootIndex2Rz = RightFootIndex2R.RightFootIndex2Rz

    RightFootIndex2S = RightFootIndex2SField()
    RightFootIndex2Sx = RightFootIndex2S.RightFootIndex2Sx
    RightFootIndex2Sy = RightFootIndex2S.RightFootIndex2Sy
    RightFootIndex2Sz = RightFootIndex2S.RightFootIndex2Sz

    RightFootIndex3T = RightFootIndex3TField()
    RightFootIndex3Tx = RightFootIndex3T.RightFootIndex3Tx
    RightFootIndex3Ty = RightFootIndex3T.RightFootIndex3Ty
    RightFootIndex3Tz = RightFootIndex3T.RightFootIndex3Tz

    RightFootIndex3R = RightFootIndex3RField()
    RightFootIndex3Rx = RightFootIndex3R.RightFootIndex3Rx
    RightFootIndex3Ry = RightFootIndex3R.RightFootIndex3Ry
    RightFootIndex3Rz = RightFootIndex3R.RightFootIndex3Rz

    RightFootIndex3S = RightFootIndex3SField()
    RightFootIndex3Sx = RightFootIndex3S.RightFootIndex3Sx
    RightFootIndex3Sy = RightFootIndex3S.RightFootIndex3Sy
    RightFootIndex3Sz = RightFootIndex3S.RightFootIndex3Sz

    RightFootIndex4T = RightFootIndex4TField()
    RightFootIndex4Tx = RightFootIndex4T.RightFootIndex4Tx
    RightFootIndex4Ty = RightFootIndex4T.RightFootIndex4Ty
    RightFootIndex4Tz = RightFootIndex4T.RightFootIndex4Tz

    RightFootIndex4R = RightFootIndex4RField()
    RightFootIndex4Rx = RightFootIndex4R.RightFootIndex4Rx
    RightFootIndex4Ry = RightFootIndex4R.RightFootIndex4Ry
    RightFootIndex4Rz = RightFootIndex4R.RightFootIndex4Rz

    RightFootIndex4S = RightFootIndex4SField()
    RightFootIndex4Sx = RightFootIndex4S.RightFootIndex4Sx
    RightFootIndex4Sy = RightFootIndex4S.RightFootIndex4Sy
    RightFootIndex4Sz = RightFootIndex4S.RightFootIndex4Sz

    RightFootMiddle1T = RightFootMiddle1TField()
    RightFootMiddle1Tx = RightFootMiddle1T.RightFootMiddle1Tx
    RightFootMiddle1Ty = RightFootMiddle1T.RightFootMiddle1Ty
    RightFootMiddle1Tz = RightFootMiddle1T.RightFootMiddle1Tz

    RightFootMiddle1R = RightFootMiddle1RField()
    RightFootMiddle1Rx = RightFootMiddle1R.RightFootMiddle1Rx
    RightFootMiddle1Ry = RightFootMiddle1R.RightFootMiddle1Ry
    RightFootMiddle1Rz = RightFootMiddle1R.RightFootMiddle1Rz

    RightFootMiddle1S = RightFootMiddle1SField()
    RightFootMiddle1Sx = RightFootMiddle1S.RightFootMiddle1Sx
    RightFootMiddle1Sy = RightFootMiddle1S.RightFootMiddle1Sy
    RightFootMiddle1Sz = RightFootMiddle1S.RightFootMiddle1Sz

    RightFootMiddle2T = RightFootMiddle2TField()
    RightFootMiddle2Tx = RightFootMiddle2T.RightFootMiddle2Tx
    RightFootMiddle2Ty = RightFootMiddle2T.RightFootMiddle2Ty
    RightFootMiddle2Tz = RightFootMiddle2T.RightFootMiddle2Tz

    RightFootMiddle2R = RightFootMiddle2RField()
    RightFootMiddle2Rx = RightFootMiddle2R.RightFootMiddle2Rx
    RightFootMiddle2Ry = RightFootMiddle2R.RightFootMiddle2Ry
    RightFootMiddle2Rz = RightFootMiddle2R.RightFootMiddle2Rz

    RightFootMiddle2S = RightFootMiddle2SField()
    RightFootMiddle2Sx = RightFootMiddle2S.RightFootMiddle2Sx
    RightFootMiddle2Sy = RightFootMiddle2S.RightFootMiddle2Sy
    RightFootMiddle2Sz = RightFootMiddle2S.RightFootMiddle2Sz

    RightFootMiddle3T = RightFootMiddle3TField()
    RightFootMiddle3Tx = RightFootMiddle3T.RightFootMiddle3Tx
    RightFootMiddle3Ty = RightFootMiddle3T.RightFootMiddle3Ty
    RightFootMiddle3Tz = RightFootMiddle3T.RightFootMiddle3Tz

    RightFootMiddle3R = RightFootMiddle3RField()
    RightFootMiddle3Rx = RightFootMiddle3R.RightFootMiddle3Rx
    RightFootMiddle3Ry = RightFootMiddle3R.RightFootMiddle3Ry
    RightFootMiddle3Rz = RightFootMiddle3R.RightFootMiddle3Rz

    RightFootMiddle3S = RightFootMiddle3SField()
    RightFootMiddle3Sx = RightFootMiddle3S.RightFootMiddle3Sx
    RightFootMiddle3Sy = RightFootMiddle3S.RightFootMiddle3Sy
    RightFootMiddle3Sz = RightFootMiddle3S.RightFootMiddle3Sz

    RightFootMiddle4T = RightFootMiddle4TField()
    RightFootMiddle4Tx = RightFootMiddle4T.RightFootMiddle4Tx
    RightFootMiddle4Ty = RightFootMiddle4T.RightFootMiddle4Ty
    RightFootMiddle4Tz = RightFootMiddle4T.RightFootMiddle4Tz

    RightFootMiddle4R = RightFootMiddle4RField()
    RightFootMiddle4Rx = RightFootMiddle4R.RightFootMiddle4Rx
    RightFootMiddle4Ry = RightFootMiddle4R.RightFootMiddle4Ry
    RightFootMiddle4Rz = RightFootMiddle4R.RightFootMiddle4Rz

    RightFootMiddle4S = RightFootMiddle4SField()
    RightFootMiddle4Sx = RightFootMiddle4S.RightFootMiddle4Sx
    RightFootMiddle4Sy = RightFootMiddle4S.RightFootMiddle4Sy
    RightFootMiddle4Sz = RightFootMiddle4S.RightFootMiddle4Sz

    RightFootRing1T = RightFootRing1TField()
    RightFootRing1Tx = RightFootRing1T.RightFootRing1Tx
    RightFootRing1Ty = RightFootRing1T.RightFootRing1Ty
    RightFootRing1Tz = RightFootRing1T.RightFootRing1Tz

    RightFootRing1R = RightFootRing1RField()
    RightFootRing1Rx = RightFootRing1R.RightFootRing1Rx
    RightFootRing1Ry = RightFootRing1R.RightFootRing1Ry
    RightFootRing1Rz = RightFootRing1R.RightFootRing1Rz

    RightFootRing1S = RightFootRing1SField()
    RightFootRing1Sx = RightFootRing1S.RightFootRing1Sx
    RightFootRing1Sy = RightFootRing1S.RightFootRing1Sy
    RightFootRing1Sz = RightFootRing1S.RightFootRing1Sz

    RightFootRing2T = RightFootRing2TField()
    RightFootRing2Tx = RightFootRing2T.RightFootRing2Tx
    RightFootRing2Ty = RightFootRing2T.RightFootRing2Ty
    RightFootRing2Tz = RightFootRing2T.RightFootRing2Tz

    RightFootRing2R = RightFootRing2RField()
    RightFootRing2Rx = RightFootRing2R.RightFootRing2Rx
    RightFootRing2Ry = RightFootRing2R.RightFootRing2Ry
    RightFootRing2Rz = RightFootRing2R.RightFootRing2Rz

    RightFootRing2S = RightFootRing2SField()
    RightFootRing2Sx = RightFootRing2S.RightFootRing2Sx
    RightFootRing2Sy = RightFootRing2S.RightFootRing2Sy
    RightFootRing2Sz = RightFootRing2S.RightFootRing2Sz

    RightFootRing3T = RightFootRing3TField()
    RightFootRing3Tx = RightFootRing3T.RightFootRing3Tx
    RightFootRing3Ty = RightFootRing3T.RightFootRing3Ty
    RightFootRing3Tz = RightFootRing3T.RightFootRing3Tz

    RightFootRing3R = RightFootRing3RField()
    RightFootRing3Rx = RightFootRing3R.RightFootRing3Rx
    RightFootRing3Ry = RightFootRing3R.RightFootRing3Ry
    RightFootRing3Rz = RightFootRing3R.RightFootRing3Rz

    RightFootRing3S = RightFootRing3SField()
    RightFootRing3Sx = RightFootRing3S.RightFootRing3Sx
    RightFootRing3Sy = RightFootRing3S.RightFootRing3Sy
    RightFootRing3Sz = RightFootRing3S.RightFootRing3Sz

    RightFootRing4T = RightFootRing4TField()
    RightFootRing4Tx = RightFootRing4T.RightFootRing4Tx
    RightFootRing4Ty = RightFootRing4T.RightFootRing4Ty
    RightFootRing4Tz = RightFootRing4T.RightFootRing4Tz

    RightFootRing4R = RightFootRing4RField()
    RightFootRing4Rx = RightFootRing4R.RightFootRing4Rx
    RightFootRing4Ry = RightFootRing4R.RightFootRing4Ry
    RightFootRing4Rz = RightFootRing4R.RightFootRing4Rz

    RightFootRing4S = RightFootRing4SField()
    RightFootRing4Sx = RightFootRing4S.RightFootRing4Sx
    RightFootRing4Sy = RightFootRing4S.RightFootRing4Sy
    RightFootRing4Sz = RightFootRing4S.RightFootRing4Sz

    RightFootPinky1T = RightFootPinky1TField()
    RightFootPinky1Tx = RightFootPinky1T.RightFootPinky1Tx
    RightFootPinky1Ty = RightFootPinky1T.RightFootPinky1Ty
    RightFootPinky1Tz = RightFootPinky1T.RightFootPinky1Tz

    RightFootPinky1R = RightFootPinky1RField()
    RightFootPinky1Rx = RightFootPinky1R.RightFootPinky1Rx
    RightFootPinky1Ry = RightFootPinky1R.RightFootPinky1Ry
    RightFootPinky1Rz = RightFootPinky1R.RightFootPinky1Rz

    RightFootPinky1S = RightFootPinky1SField()
    RightFootPinky1Sx = RightFootPinky1S.RightFootPinky1Sx
    RightFootPinky1Sy = RightFootPinky1S.RightFootPinky1Sy
    RightFootPinky1Sz = RightFootPinky1S.RightFootPinky1Sz

    RightFootPinky2T = RightFootPinky2TField()
    RightFootPinky2Tx = RightFootPinky2T.RightFootPinky2Tx
    RightFootPinky2Ty = RightFootPinky2T.RightFootPinky2Ty
    RightFootPinky2Tz = RightFootPinky2T.RightFootPinky2Tz

    RightFootPinky2R = RightFootPinky2RField()
    RightFootPinky2Rx = RightFootPinky2R.RightFootPinky2Rx
    RightFootPinky2Ry = RightFootPinky2R.RightFootPinky2Ry
    RightFootPinky2Rz = RightFootPinky2R.RightFootPinky2Rz

    RightFootPinky2S = RightFootPinky2SField()
    RightFootPinky2Sx = RightFootPinky2S.RightFootPinky2Sx
    RightFootPinky2Sy = RightFootPinky2S.RightFootPinky2Sy
    RightFootPinky2Sz = RightFootPinky2S.RightFootPinky2Sz

    RightFootPinky3T = RightFootPinky3TField()
    RightFootPinky3Tx = RightFootPinky3T.RightFootPinky3Tx
    RightFootPinky3Ty = RightFootPinky3T.RightFootPinky3Ty
    RightFootPinky3Tz = RightFootPinky3T.RightFootPinky3Tz

    RightFootPinky3R = RightFootPinky3RField()
    RightFootPinky3Rx = RightFootPinky3R.RightFootPinky3Rx
    RightFootPinky3Ry = RightFootPinky3R.RightFootPinky3Ry
    RightFootPinky3Rz = RightFootPinky3R.RightFootPinky3Rz

    RightFootPinky3S = RightFootPinky3SField()
    RightFootPinky3Sx = RightFootPinky3S.RightFootPinky3Sx
    RightFootPinky3Sy = RightFootPinky3S.RightFootPinky3Sy
    RightFootPinky3Sz = RightFootPinky3S.RightFootPinky3Sz

    RightFootPinky4T = RightFootPinky4TField()
    RightFootPinky4Tx = RightFootPinky4T.RightFootPinky4Tx
    RightFootPinky4Ty = RightFootPinky4T.RightFootPinky4Ty
    RightFootPinky4Tz = RightFootPinky4T.RightFootPinky4Tz

    RightFootPinky4R = RightFootPinky4RField()
    RightFootPinky4Rx = RightFootPinky4R.RightFootPinky4Rx
    RightFootPinky4Ry = RightFootPinky4R.RightFootPinky4Ry
    RightFootPinky4Rz = RightFootPinky4R.RightFootPinky4Rz

    RightFootPinky4S = RightFootPinky4SField()
    RightFootPinky4Sx = RightFootPinky4S.RightFootPinky4Sx
    RightFootPinky4Sy = RightFootPinky4S.RightFootPinky4Sy
    RightFootPinky4Sz = RightFootPinky4S.RightFootPinky4Sz

    RightFootExtraFinger1T = RightFootExtraFinger1TField()
    RightFootExtraFinger1Tx = RightFootExtraFinger1T.RightFootExtraFinger1Tx
    RightFootExtraFinger1Ty = RightFootExtraFinger1T.RightFootExtraFinger1Ty
    RightFootExtraFinger1Tz = RightFootExtraFinger1T.RightFootExtraFinger1Tz

    RightFootExtraFinger1R = RightFootExtraFinger1RField()
    RightFootExtraFinger1Rx = RightFootExtraFinger1R.RightFootExtraFinger1Rx
    RightFootExtraFinger1Ry = RightFootExtraFinger1R.RightFootExtraFinger1Ry
    RightFootExtraFinger1Rz = RightFootExtraFinger1R.RightFootExtraFinger1Rz

    RightFootExtraFinger1S = RightFootExtraFinger1SField()
    RightFootExtraFinger1Sx = RightFootExtraFinger1S.RightFootExtraFinger1Sx
    RightFootExtraFinger1Sy = RightFootExtraFinger1S.RightFootExtraFinger1Sy
    RightFootExtraFinger1Sz = RightFootExtraFinger1S.RightFootExtraFinger1Sz

    RightFootExtraFinger2T = RightFootExtraFinger2TField()
    RightFootExtraFinger2Tx = RightFootExtraFinger2T.RightFootExtraFinger2Tx
    RightFootExtraFinger2Ty = RightFootExtraFinger2T.RightFootExtraFinger2Ty
    RightFootExtraFinger2Tz = RightFootExtraFinger2T.RightFootExtraFinger2Tz

    RightFootExtraFinger2R = RightFootExtraFinger2RField()
    RightFootExtraFinger2Rx = RightFootExtraFinger2R.RightFootExtraFinger2Rx
    RightFootExtraFinger2Ry = RightFootExtraFinger2R.RightFootExtraFinger2Ry
    RightFootExtraFinger2Rz = RightFootExtraFinger2R.RightFootExtraFinger2Rz

    RightFootExtraFinger2S = RightFootExtraFinger2SField()
    RightFootExtraFinger2Sx = RightFootExtraFinger2S.RightFootExtraFinger2Sx
    RightFootExtraFinger2Sy = RightFootExtraFinger2S.RightFootExtraFinger2Sy
    RightFootExtraFinger2Sz = RightFootExtraFinger2S.RightFootExtraFinger2Sz

    RightFootExtraFinger3T = RightFootExtraFinger3TField()
    RightFootExtraFinger3Tx = RightFootExtraFinger3T.RightFootExtraFinger3Tx
    RightFootExtraFinger3Ty = RightFootExtraFinger3T.RightFootExtraFinger3Ty
    RightFootExtraFinger3Tz = RightFootExtraFinger3T.RightFootExtraFinger3Tz

    RightFootExtraFinger3R = RightFootExtraFinger3RField()
    RightFootExtraFinger3Rx = RightFootExtraFinger3R.RightFootExtraFinger3Rx
    RightFootExtraFinger3Ry = RightFootExtraFinger3R.RightFootExtraFinger3Ry
    RightFootExtraFinger3Rz = RightFootExtraFinger3R.RightFootExtraFinger3Rz

    RightFootExtraFinger3S = RightFootExtraFinger3SField()
    RightFootExtraFinger3Sx = RightFootExtraFinger3S.RightFootExtraFinger3Sx
    RightFootExtraFinger3Sy = RightFootExtraFinger3S.RightFootExtraFinger3Sy
    RightFootExtraFinger3Sz = RightFootExtraFinger3S.RightFootExtraFinger3Sz

    RightFootExtraFinger4T = RightFootExtraFinger4TField()
    RightFootExtraFinger4Tx = RightFootExtraFinger4T.RightFootExtraFinger4Tx
    RightFootExtraFinger4Ty = RightFootExtraFinger4T.RightFootExtraFinger4Ty
    RightFootExtraFinger4Tz = RightFootExtraFinger4T.RightFootExtraFinger4Tz

    RightFootExtraFinger4R = RightFootExtraFinger4RField()
    RightFootExtraFinger4Rx = RightFootExtraFinger4R.RightFootExtraFinger4Rx
    RightFootExtraFinger4Ry = RightFootExtraFinger4R.RightFootExtraFinger4Ry
    RightFootExtraFinger4Rz = RightFootExtraFinger4R.RightFootExtraFinger4Rz

    RightFootExtraFinger4S = RightFootExtraFinger4SField()
    RightFootExtraFinger4Sx = RightFootExtraFinger4S.RightFootExtraFinger4Sx
    RightFootExtraFinger4Sy = RightFootExtraFinger4S.RightFootExtraFinger4Sy
    RightFootExtraFinger4Sz = RightFootExtraFinger4S.RightFootExtraFinger4Sz

    LeftInHandThumbT = LeftInHandThumbTField()
    LeftInHandThumbTx = LeftInHandThumbT.LeftInHandThumbTx
    LeftInHandThumbTy = LeftInHandThumbT.LeftInHandThumbTy
    LeftInHandThumbTz = LeftInHandThumbT.LeftInHandThumbTz

    LeftInHandThumbR = LeftInHandThumbRField()
    LeftInHandThumbRx = LeftInHandThumbR.LeftInHandThumbRx
    LeftInHandThumbRy = LeftInHandThumbR.LeftInHandThumbRy
    LeftInHandThumbRz = LeftInHandThumbR.LeftInHandThumbRz

    LeftInHandThumbS = LeftInHandThumbSField()
    LeftInHandThumbSx = LeftInHandThumbS.LeftInHandThumbSx
    LeftInHandThumbSy = LeftInHandThumbS.LeftInHandThumbSy
    LeftInHandThumbSz = LeftInHandThumbS.LeftInHandThumbSz

    LeftInHandIndexT = LeftInHandIndexTField()
    LeftInHandIndexTx = LeftInHandIndexT.LeftInHandIndexTx
    LeftInHandIndexTy = LeftInHandIndexT.LeftInHandIndexTy
    LeftInHandIndexTz = LeftInHandIndexT.LeftInHandIndexTz

    LeftInHandIndexR = LeftInHandIndexRField()
    LeftInHandIndexRx = LeftInHandIndexR.LeftInHandIndexRx
    LeftInHandIndexRy = LeftInHandIndexR.LeftInHandIndexRy
    LeftInHandIndexRz = LeftInHandIndexR.LeftInHandIndexRz

    LeftInHandIndexS = LeftInHandIndexSField()
    LeftInHandIndexSx = LeftInHandIndexS.LeftInHandIndexSx
    LeftInHandIndexSy = LeftInHandIndexS.LeftInHandIndexSy
    LeftInHandIndexSz = LeftInHandIndexS.LeftInHandIndexSz

    LeftInHandMiddleT = LeftInHandMiddleTField()
    LeftInHandMiddleTx = LeftInHandMiddleT.LeftInHandMiddleTx
    LeftInHandMiddleTy = LeftInHandMiddleT.LeftInHandMiddleTy
    LeftInHandMiddleTz = LeftInHandMiddleT.LeftInHandMiddleTz

    LeftInHandMiddleR = LeftInHandMiddleRField()
    LeftInHandMiddleRx = LeftInHandMiddleR.LeftInHandMiddleRx
    LeftInHandMiddleRy = LeftInHandMiddleR.LeftInHandMiddleRy
    LeftInHandMiddleRz = LeftInHandMiddleR.LeftInHandMiddleRz

    LeftInHandMiddleS = LeftInHandMiddleSField()
    LeftInHandMiddleSx = LeftInHandMiddleS.LeftInHandMiddleSx
    LeftInHandMiddleSy = LeftInHandMiddleS.LeftInHandMiddleSy
    LeftInHandMiddleSz = LeftInHandMiddleS.LeftInHandMiddleSz

    LeftInHandRingT = LeftInHandRingTField()
    LeftInHandRingTx = LeftInHandRingT.LeftInHandRingTx
    LeftInHandRingTy = LeftInHandRingT.LeftInHandRingTy
    LeftInHandRingTz = LeftInHandRingT.LeftInHandRingTz

    LeftInHandRingR = LeftInHandRingRField()
    LeftInHandRingRx = LeftInHandRingR.LeftInHandRingRx
    LeftInHandRingRy = LeftInHandRingR.LeftInHandRingRy
    LeftInHandRingRz = LeftInHandRingR.LeftInHandRingRz

    LeftInHandRingS = LeftInHandRingSField()
    LeftInHandRingSx = LeftInHandRingS.LeftInHandRingSx
    LeftInHandRingSy = LeftInHandRingS.LeftInHandRingSy
    LeftInHandRingSz = LeftInHandRingS.LeftInHandRingSz

    LeftInHandPinkyT = LeftInHandPinkyTField()
    LeftInHandPinkyTx = LeftInHandPinkyT.LeftInHandPinkyTx
    LeftInHandPinkyTy = LeftInHandPinkyT.LeftInHandPinkyTy
    LeftInHandPinkyTz = LeftInHandPinkyT.LeftInHandPinkyTz

    LeftInHandPinkyR = LeftInHandPinkyRField()
    LeftInHandPinkyRx = LeftInHandPinkyR.LeftInHandPinkyRx
    LeftInHandPinkyRy = LeftInHandPinkyR.LeftInHandPinkyRy
    LeftInHandPinkyRz = LeftInHandPinkyR.LeftInHandPinkyRz

    LeftInHandPinkyS = LeftInHandPinkySField()
    LeftInHandPinkySx = LeftInHandPinkyS.LeftInHandPinkySx
    LeftInHandPinkySy = LeftInHandPinkyS.LeftInHandPinkySy
    LeftInHandPinkySz = LeftInHandPinkyS.LeftInHandPinkySz

    LeftInHandExtraFingerT = LeftInHandExtraFingerTField()
    LeftInHandExtraFingerTx = LeftInHandExtraFingerT.LeftInHandExtraFingerTx
    LeftInHandExtraFingerTy = LeftInHandExtraFingerT.LeftInHandExtraFingerTy
    LeftInHandExtraFingerTz = LeftInHandExtraFingerT.LeftInHandExtraFingerTz

    LeftInHandExtraFingerR = LeftInHandExtraFingerRField()
    LeftInHandExtraFingerRx = LeftInHandExtraFingerR.LeftInHandExtraFingerRx
    LeftInHandExtraFingerRy = LeftInHandExtraFingerR.LeftInHandExtraFingerRy
    LeftInHandExtraFingerRz = LeftInHandExtraFingerR.LeftInHandExtraFingerRz

    LeftInHandExtraFingerS = LeftInHandExtraFingerSField()
    LeftInHandExtraFingerSx = LeftInHandExtraFingerS.LeftInHandExtraFingerSx
    LeftInHandExtraFingerSy = LeftInHandExtraFingerS.LeftInHandExtraFingerSy
    LeftInHandExtraFingerSz = LeftInHandExtraFingerS.LeftInHandExtraFingerSz

    RightInHandThumbT = RightInHandThumbTField()
    RightInHandThumbTx = RightInHandThumbT.RightInHandThumbTx
    RightInHandThumbTy = RightInHandThumbT.RightInHandThumbTy
    RightInHandThumbTz = RightInHandThumbT.RightInHandThumbTz

    RightInHandThumbR = RightInHandThumbRField()
    RightInHandThumbRx = RightInHandThumbR.RightInHandThumbRx
    RightInHandThumbRy = RightInHandThumbR.RightInHandThumbRy
    RightInHandThumbRz = RightInHandThumbR.RightInHandThumbRz

    RightInHandThumbS = RightInHandThumbSField()
    RightInHandThumbSx = RightInHandThumbS.RightInHandThumbSx
    RightInHandThumbSy = RightInHandThumbS.RightInHandThumbSy
    RightInHandThumbSz = RightInHandThumbS.RightInHandThumbSz

    RightInHandIndexT = RightInHandIndexTField()
    RightInHandIndexTx = RightInHandIndexT.RightInHandIndexTx
    RightInHandIndexTy = RightInHandIndexT.RightInHandIndexTy
    RightInHandIndexTz = RightInHandIndexT.RightInHandIndexTz

    RightInHandIndexR = RightInHandIndexRField()
    RightInHandIndexRx = RightInHandIndexR.RightInHandIndexRx
    RightInHandIndexRy = RightInHandIndexR.RightInHandIndexRy
    RightInHandIndexRz = RightInHandIndexR.RightInHandIndexRz

    RightInHandIndexS = RightInHandIndexSField()
    RightInHandIndexSx = RightInHandIndexS.RightInHandIndexSx
    RightInHandIndexSy = RightInHandIndexS.RightInHandIndexSy
    RightInHandIndexSz = RightInHandIndexS.RightInHandIndexSz

    RightInHandMiddleT = RightInHandMiddleTField()
    RightInHandMiddleTx = RightInHandMiddleT.RightInHandMiddleTx
    RightInHandMiddleTy = RightInHandMiddleT.RightInHandMiddleTy
    RightInHandMiddleTz = RightInHandMiddleT.RightInHandMiddleTz

    RightInHandMiddleR = RightInHandMiddleRField()
    RightInHandMiddleRx = RightInHandMiddleR.RightInHandMiddleRx
    RightInHandMiddleRy = RightInHandMiddleR.RightInHandMiddleRy
    RightInHandMiddleRz = RightInHandMiddleR.RightInHandMiddleRz

    RightInHandMiddleS = RightInHandMiddleSField()
    RightInHandMiddleSx = RightInHandMiddleS.RightInHandMiddleSx
    RightInHandMiddleSy = RightInHandMiddleS.RightInHandMiddleSy
    RightInHandMiddleSz = RightInHandMiddleS.RightInHandMiddleSz

    RightInHandRingT = RightInHandRingTField()
    RightInHandRingTx = RightInHandRingT.RightInHandRingTx
    RightInHandRingTy = RightInHandRingT.RightInHandRingTy
    RightInHandRingTz = RightInHandRingT.RightInHandRingTz

    RightInHandRingR = RightInHandRingRField()
    RightInHandRingRx = RightInHandRingR.RightInHandRingRx
    RightInHandRingRy = RightInHandRingR.RightInHandRingRy
    RightInHandRingRz = RightInHandRingR.RightInHandRingRz

    RightInHandRingS = RightInHandRingSField()
    RightInHandRingSx = RightInHandRingS.RightInHandRingSx
    RightInHandRingSy = RightInHandRingS.RightInHandRingSy
    RightInHandRingSz = RightInHandRingS.RightInHandRingSz

    RightInHandPinkyT = RightInHandPinkyTField()
    RightInHandPinkyTx = RightInHandPinkyT.RightInHandPinkyTx
    RightInHandPinkyTy = RightInHandPinkyT.RightInHandPinkyTy
    RightInHandPinkyTz = RightInHandPinkyT.RightInHandPinkyTz

    RightInHandPinkyR = RightInHandPinkyRField()
    RightInHandPinkyRx = RightInHandPinkyR.RightInHandPinkyRx
    RightInHandPinkyRy = RightInHandPinkyR.RightInHandPinkyRy
    RightInHandPinkyRz = RightInHandPinkyR.RightInHandPinkyRz

    RightInHandPinkyS = RightInHandPinkySField()
    RightInHandPinkySx = RightInHandPinkyS.RightInHandPinkySx
    RightInHandPinkySy = RightInHandPinkyS.RightInHandPinkySy
    RightInHandPinkySz = RightInHandPinkyS.RightInHandPinkySz

    RightInHandExtraFingerT = RightInHandExtraFingerTField()
    RightInHandExtraFingerTx = RightInHandExtraFingerT.RightInHandExtraFingerTx
    RightInHandExtraFingerTy = RightInHandExtraFingerT.RightInHandExtraFingerTy
    RightInHandExtraFingerTz = RightInHandExtraFingerT.RightInHandExtraFingerTz

    RightInHandExtraFingerR = RightInHandExtraFingerRField()
    RightInHandExtraFingerRx = RightInHandExtraFingerR.RightInHandExtraFingerRx
    RightInHandExtraFingerRy = RightInHandExtraFingerR.RightInHandExtraFingerRy
    RightInHandExtraFingerRz = RightInHandExtraFingerR.RightInHandExtraFingerRz

    RightInHandExtraFingerS = RightInHandExtraFingerSField()
    RightInHandExtraFingerSx = RightInHandExtraFingerS.RightInHandExtraFingerSx
    RightInHandExtraFingerSy = RightInHandExtraFingerS.RightInHandExtraFingerSy
    RightInHandExtraFingerSz = RightInHandExtraFingerS.RightInHandExtraFingerSz

    LeftInFootThumbT = LeftInFootThumbTField()
    LeftInFootThumbTx = LeftInFootThumbT.LeftInFootThumbTx
    LeftInFootThumbTy = LeftInFootThumbT.LeftInFootThumbTy
    LeftInFootThumbTz = LeftInFootThumbT.LeftInFootThumbTz

    LeftInFootThumbR = LeftInFootThumbRField()
    LeftInFootThumbRx = LeftInFootThumbR.LeftInFootThumbRx
    LeftInFootThumbRy = LeftInFootThumbR.LeftInFootThumbRy
    LeftInFootThumbRz = LeftInFootThumbR.LeftInFootThumbRz

    LeftInFootThumbS = LeftInFootThumbSField()
    LeftInFootThumbSx = LeftInFootThumbS.LeftInFootThumbSx
    LeftInFootThumbSy = LeftInFootThumbS.LeftInFootThumbSy
    LeftInFootThumbSz = LeftInFootThumbS.LeftInFootThumbSz

    LeftInFootIndexT = LeftInFootIndexTField()
    LeftInFootIndexTx = LeftInFootIndexT.LeftInFootIndexTx
    LeftInFootIndexTy = LeftInFootIndexT.LeftInFootIndexTy
    LeftInFootIndexTz = LeftInFootIndexT.LeftInFootIndexTz

    LeftInFootIndexR = LeftInFootIndexRField()
    LeftInFootIndexRx = LeftInFootIndexR.LeftInFootIndexRx
    LeftInFootIndexRy = LeftInFootIndexR.LeftInFootIndexRy
    LeftInFootIndexRz = LeftInFootIndexR.LeftInFootIndexRz

    LeftInFootIndexS = LeftInFootIndexSField()
    LeftInFootIndexSx = LeftInFootIndexS.LeftInFootIndexSx
    LeftInFootIndexSy = LeftInFootIndexS.LeftInFootIndexSy
    LeftInFootIndexSz = LeftInFootIndexS.LeftInFootIndexSz

    LeftInFootMiddleT = LeftInFootMiddleTField()
    LeftInFootMiddleTx = LeftInFootMiddleT.LeftInFootMiddleTx
    LeftInFootMiddleTy = LeftInFootMiddleT.LeftInFootMiddleTy
    LeftInFootMiddleTz = LeftInFootMiddleT.LeftInFootMiddleTz

    LeftInFootMiddleR = LeftInFootMiddleRField()
    LeftInFootMiddleRx = LeftInFootMiddleR.LeftInFootMiddleRx
    LeftInFootMiddleRy = LeftInFootMiddleR.LeftInFootMiddleRy
    LeftInFootMiddleRz = LeftInFootMiddleR.LeftInFootMiddleRz

    LeftInFootMiddleS = LeftInFootMiddleSField()
    LeftInFootMiddleSx = LeftInFootMiddleS.LeftInFootMiddleSx
    LeftInFootMiddleSy = LeftInFootMiddleS.LeftInFootMiddleSy
    LeftInFootMiddleSz = LeftInFootMiddleS.LeftInFootMiddleSz

    LeftInFootRingT = LeftInFootRingTField()
    LeftInFootRingTx = LeftInFootRingT.LeftInFootRingTx
    LeftInFootRingTy = LeftInFootRingT.LeftInFootRingTy
    LeftInFootRingTz = LeftInFootRingT.LeftInFootRingTz

    LeftInFootRingR = LeftInFootRingRField()
    LeftInFootRingRx = LeftInFootRingR.LeftInFootRingRx
    LeftInFootRingRy = LeftInFootRingR.LeftInFootRingRy
    LeftInFootRingRz = LeftInFootRingR.LeftInFootRingRz

    LeftInFootRingS = LeftInFootRingSField()
    LeftInFootRingSx = LeftInFootRingS.LeftInFootRingSx
    LeftInFootRingSy = LeftInFootRingS.LeftInFootRingSy
    LeftInFootRingSz = LeftInFootRingS.LeftInFootRingSz

    LeftInFootPinkyT = LeftInFootPinkyTField()
    LeftInFootPinkyTx = LeftInFootPinkyT.LeftInFootPinkyTx
    LeftInFootPinkyTy = LeftInFootPinkyT.LeftInFootPinkyTy
    LeftInFootPinkyTz = LeftInFootPinkyT.LeftInFootPinkyTz

    LeftInFootPinkyR = LeftInFootPinkyRField()
    LeftInFootPinkyRx = LeftInFootPinkyR.LeftInFootPinkyRx
    LeftInFootPinkyRy = LeftInFootPinkyR.LeftInFootPinkyRy
    LeftInFootPinkyRz = LeftInFootPinkyR.LeftInFootPinkyRz

    LeftInFootPinkyS = LeftInFootPinkySField()
    LeftInFootPinkySx = LeftInFootPinkyS.LeftInFootPinkySx
    LeftInFootPinkySy = LeftInFootPinkyS.LeftInFootPinkySy
    LeftInFootPinkySz = LeftInFootPinkyS.LeftInFootPinkySz

    LeftInFootExtraFingerT = LeftInFootExtraFingerTField()
    LeftInFootExtraFingerTx = LeftInFootExtraFingerT.LeftInFootExtraFingerTx
    LeftInFootExtraFingerTy = LeftInFootExtraFingerT.LeftInFootExtraFingerTy
    LeftInFootExtraFingerTz = LeftInFootExtraFingerT.LeftInFootExtraFingerTz

    LeftInFootExtraFingerR = LeftInFootExtraFingerRField()
    LeftInFootExtraFingerRx = LeftInFootExtraFingerR.LeftInFootExtraFingerRx
    LeftInFootExtraFingerRy = LeftInFootExtraFingerR.LeftInFootExtraFingerRy
    LeftInFootExtraFingerRz = LeftInFootExtraFingerR.LeftInFootExtraFingerRz

    LeftInFootExtraFingerS = LeftInFootExtraFingerSField()
    LeftInFootExtraFingerSx = LeftInFootExtraFingerS.LeftInFootExtraFingerSx
    LeftInFootExtraFingerSy = LeftInFootExtraFingerS.LeftInFootExtraFingerSy
    LeftInFootExtraFingerSz = LeftInFootExtraFingerS.LeftInFootExtraFingerSz

    RightInFootThumbT = RightInFootThumbTField()
    RightInFootThumbTx = RightInFootThumbT.RightInFootThumbTx
    RightInFootThumbTy = RightInFootThumbT.RightInFootThumbTy
    RightInFootThumbTz = RightInFootThumbT.RightInFootThumbTz

    RightInFootThumbR = RightInFootThumbRField()
    RightInFootThumbRx = RightInFootThumbR.RightInFootThumbRx
    RightInFootThumbRy = RightInFootThumbR.RightInFootThumbRy
    RightInFootThumbRz = RightInFootThumbR.RightInFootThumbRz

    RightInFootThumbS = RightInFootThumbSField()
    RightInFootThumbSx = RightInFootThumbS.RightInFootThumbSx
    RightInFootThumbSy = RightInFootThumbS.RightInFootThumbSy
    RightInFootThumbSz = RightInFootThumbS.RightInFootThumbSz

    RightInFootIndexT = RightInFootIndexTField()
    RightInFootIndexTx = RightInFootIndexT.RightInFootIndexTx
    RightInFootIndexTy = RightInFootIndexT.RightInFootIndexTy
    RightInFootIndexTz = RightInFootIndexT.RightInFootIndexTz

    RightInFootIndexR = RightInFootIndexRField()
    RightInFootIndexRx = RightInFootIndexR.RightInFootIndexRx
    RightInFootIndexRy = RightInFootIndexR.RightInFootIndexRy
    RightInFootIndexRz = RightInFootIndexR.RightInFootIndexRz

    RightInFootIndexS = RightInFootIndexSField()
    RightInFootIndexSx = RightInFootIndexS.RightInFootIndexSx
    RightInFootIndexSy = RightInFootIndexS.RightInFootIndexSy
    RightInFootIndexSz = RightInFootIndexS.RightInFootIndexSz

    RightInFootMiddleT = RightInFootMiddleTField()
    RightInFootMiddleTx = RightInFootMiddleT.RightInFootMiddleTx
    RightInFootMiddleTy = RightInFootMiddleT.RightInFootMiddleTy
    RightInFootMiddleTz = RightInFootMiddleT.RightInFootMiddleTz

    RightInFootMiddleR = RightInFootMiddleRField()
    RightInFootMiddleRx = RightInFootMiddleR.RightInFootMiddleRx
    RightInFootMiddleRy = RightInFootMiddleR.RightInFootMiddleRy
    RightInFootMiddleRz = RightInFootMiddleR.RightInFootMiddleRz

    RightInFootMiddleS = RightInFootMiddleSField()
    RightInFootMiddleSx = RightInFootMiddleS.RightInFootMiddleSx
    RightInFootMiddleSy = RightInFootMiddleS.RightInFootMiddleSy
    RightInFootMiddleSz = RightInFootMiddleS.RightInFootMiddleSz

    RightInFootRingT = RightInFootRingTField()
    RightInFootRingTx = RightInFootRingT.RightInFootRingTx
    RightInFootRingTy = RightInFootRingT.RightInFootRingTy
    RightInFootRingTz = RightInFootRingT.RightInFootRingTz

    RightInFootRingR = RightInFootRingRField()
    RightInFootRingRx = RightInFootRingR.RightInFootRingRx
    RightInFootRingRy = RightInFootRingR.RightInFootRingRy
    RightInFootRingRz = RightInFootRingR.RightInFootRingRz

    RightInFootRingS = RightInFootRingSField()
    RightInFootRingSx = RightInFootRingS.RightInFootRingSx
    RightInFootRingSy = RightInFootRingS.RightInFootRingSy
    RightInFootRingSz = RightInFootRingS.RightInFootRingSz

    RightInFootPinkyT = RightInFootPinkyTField()
    RightInFootPinkyTx = RightInFootPinkyT.RightInFootPinkyTx
    RightInFootPinkyTy = RightInFootPinkyT.RightInFootPinkyTy
    RightInFootPinkyTz = RightInFootPinkyT.RightInFootPinkyTz

    RightInFootPinkyR = RightInFootPinkyRField()
    RightInFootPinkyRx = RightInFootPinkyR.RightInFootPinkyRx
    RightInFootPinkyRy = RightInFootPinkyR.RightInFootPinkyRy
    RightInFootPinkyRz = RightInFootPinkyR.RightInFootPinkyRz

    RightInFootPinkyS = RightInFootPinkySField()
    RightInFootPinkySx = RightInFootPinkyS.RightInFootPinkySx
    RightInFootPinkySy = RightInFootPinkyS.RightInFootPinkySy
    RightInFootPinkySz = RightInFootPinkyS.RightInFootPinkySz

    RightInFootExtraFingerT = RightInFootExtraFingerTField()
    RightInFootExtraFingerTx = RightInFootExtraFingerT.RightInFootExtraFingerTx
    RightInFootExtraFingerTy = RightInFootExtraFingerT.RightInFootExtraFingerTy
    RightInFootExtraFingerTz = RightInFootExtraFingerT.RightInFootExtraFingerTz

    RightInFootExtraFingerR = RightInFootExtraFingerRField()
    RightInFootExtraFingerRx = RightInFootExtraFingerR.RightInFootExtraFingerRx
    RightInFootExtraFingerRy = RightInFootExtraFingerR.RightInFootExtraFingerRy
    RightInFootExtraFingerRz = RightInFootExtraFingerR.RightInFootExtraFingerRz

    RightInFootExtraFingerS = RightInFootExtraFingerSField()
    RightInFootExtraFingerSx = RightInFootExtraFingerS.RightInFootExtraFingerSx
    RightInFootExtraFingerSy = RightInFootExtraFingerS.RightInFootExtraFingerSy
    RightInFootExtraFingerSz = RightInFootExtraFingerS.RightInFootExtraFingerSz

    LeftShoulderExtraT = LeftShoulderExtraTField()
    LeftShoulderExtraTx = LeftShoulderExtraT.LeftShoulderExtraTx
    LeftShoulderExtraTy = LeftShoulderExtraT.LeftShoulderExtraTy
    LeftShoulderExtraTz = LeftShoulderExtraT.LeftShoulderExtraTz

    LeftShoulderExtraR = LeftShoulderExtraRField()
    LeftShoulderExtraRx = LeftShoulderExtraR.LeftShoulderExtraRx
    LeftShoulderExtraRy = LeftShoulderExtraR.LeftShoulderExtraRy
    LeftShoulderExtraRz = LeftShoulderExtraR.LeftShoulderExtraRz

    LeftShoulderExtraS = LeftShoulderExtraSField()
    LeftShoulderExtraSx = LeftShoulderExtraS.LeftShoulderExtraSx
    LeftShoulderExtraSy = LeftShoulderExtraS.LeftShoulderExtraSy
    LeftShoulderExtraSz = LeftShoulderExtraS.LeftShoulderExtraSz

    RightShoulderExtraT = RightShoulderExtraTField()
    RightShoulderExtraTx = RightShoulderExtraT.RightShoulderExtraTx
    RightShoulderExtraTy = RightShoulderExtraT.RightShoulderExtraTy
    RightShoulderExtraTz = RightShoulderExtraT.RightShoulderExtraTz

    RightShoulderExtraR = RightShoulderExtraRField()
    RightShoulderExtraRx = RightShoulderExtraR.RightShoulderExtraRx
    RightShoulderExtraRy = RightShoulderExtraR.RightShoulderExtraRy
    RightShoulderExtraRz = RightShoulderExtraR.RightShoulderExtraRz

    RightShoulderExtraS = RightShoulderExtraSField()
    RightShoulderExtraSx = RightShoulderExtraS.RightShoulderExtraSx
    RightShoulderExtraSy = RightShoulderExtraS.RightShoulderExtraSy
    RightShoulderExtraSz = RightShoulderExtraS.RightShoulderExtraSz

    LeafLeftUpLegRoll1T = LeafLeftUpLegRoll1TField()
    LeafLeftUpLegRoll1Tx = LeafLeftUpLegRoll1T.LeafLeftUpLegRoll1Tx
    LeafLeftUpLegRoll1Ty = LeafLeftUpLegRoll1T.LeafLeftUpLegRoll1Ty
    LeafLeftUpLegRoll1Tz = LeafLeftUpLegRoll1T.LeafLeftUpLegRoll1Tz

    LeafLeftUpLegRoll1R = LeafLeftUpLegRoll1RField()
    LeafLeftUpLegRoll1Rx = LeafLeftUpLegRoll1R.LeafLeftUpLegRoll1Rx
    LeafLeftUpLegRoll1Ry = LeafLeftUpLegRoll1R.LeafLeftUpLegRoll1Ry
    LeafLeftUpLegRoll1Rz = LeafLeftUpLegRoll1R.LeafLeftUpLegRoll1Rz

    LeafLeftUpLegRoll1S = LeafLeftUpLegRoll1SField()
    LeafLeftUpLegRoll1Sx = LeafLeftUpLegRoll1S.LeafLeftUpLegRoll1Sx
    LeafLeftUpLegRoll1Sy = LeafLeftUpLegRoll1S.LeafLeftUpLegRoll1Sy
    LeafLeftUpLegRoll1Sz = LeafLeftUpLegRoll1S.LeafLeftUpLegRoll1Sz

    LeafLeftLegRoll1T = LeafLeftLegRoll1TField()
    LeafLeftLegRoll1Tx = LeafLeftLegRoll1T.LeafLeftLegRoll1Tx
    LeafLeftLegRoll1Ty = LeafLeftLegRoll1T.LeafLeftLegRoll1Ty
    LeafLeftLegRoll1Tz = LeafLeftLegRoll1T.LeafLeftLegRoll1Tz

    LeafLeftLegRoll1R = LeafLeftLegRoll1RField()
    LeafLeftLegRoll1Rx = LeafLeftLegRoll1R.LeafLeftLegRoll1Rx
    LeafLeftLegRoll1Ry = LeafLeftLegRoll1R.LeafLeftLegRoll1Ry
    LeafLeftLegRoll1Rz = LeafLeftLegRoll1R.LeafLeftLegRoll1Rz

    LeafLeftLegRoll1S = LeafLeftLegRoll1SField()
    LeafLeftLegRoll1Sx = LeafLeftLegRoll1S.LeafLeftLegRoll1Sx
    LeafLeftLegRoll1Sy = LeafLeftLegRoll1S.LeafLeftLegRoll1Sy
    LeafLeftLegRoll1Sz = LeafLeftLegRoll1S.LeafLeftLegRoll1Sz

    LeafRightUpLegRoll1T = LeafRightUpLegRoll1TField()
    LeafRightUpLegRoll1Tx = LeafRightUpLegRoll1T.LeafRightUpLegRoll1Tx
    LeafRightUpLegRoll1Ty = LeafRightUpLegRoll1T.LeafRightUpLegRoll1Ty
    LeafRightUpLegRoll1Tz = LeafRightUpLegRoll1T.LeafRightUpLegRoll1Tz

    LeafRightUpLegRoll1R = LeafRightUpLegRoll1RField()
    LeafRightUpLegRoll1Rx = LeafRightUpLegRoll1R.LeafRightUpLegRoll1Rx
    LeafRightUpLegRoll1Ry = LeafRightUpLegRoll1R.LeafRightUpLegRoll1Ry
    LeafRightUpLegRoll1Rz = LeafRightUpLegRoll1R.LeafRightUpLegRoll1Rz

    LeafRightUpLegRoll1S = LeafRightUpLegRoll1SField()
    LeafRightUpLegRoll1Sx = LeafRightUpLegRoll1S.LeafRightUpLegRoll1Sx
    LeafRightUpLegRoll1Sy = LeafRightUpLegRoll1S.LeafRightUpLegRoll1Sy
    LeafRightUpLegRoll1Sz = LeafRightUpLegRoll1S.LeafRightUpLegRoll1Sz

    LeafRightLegRoll1T = LeafRightLegRoll1TField()
    LeafRightLegRoll1Tx = LeafRightLegRoll1T.LeafRightLegRoll1Tx
    LeafRightLegRoll1Ty = LeafRightLegRoll1T.LeafRightLegRoll1Ty
    LeafRightLegRoll1Tz = LeafRightLegRoll1T.LeafRightLegRoll1Tz

    LeafRightLegRoll1R = LeafRightLegRoll1RField()
    LeafRightLegRoll1Rx = LeafRightLegRoll1R.LeafRightLegRoll1Rx
    LeafRightLegRoll1Ry = LeafRightLegRoll1R.LeafRightLegRoll1Ry
    LeafRightLegRoll1Rz = LeafRightLegRoll1R.LeafRightLegRoll1Rz

    LeafRightLegRoll1S = LeafRightLegRoll1SField()
    LeafRightLegRoll1Sx = LeafRightLegRoll1S.LeafRightLegRoll1Sx
    LeafRightLegRoll1Sy = LeafRightLegRoll1S.LeafRightLegRoll1Sy
    LeafRightLegRoll1Sz = LeafRightLegRoll1S.LeafRightLegRoll1Sz

    LeafLeftArmRoll1T = LeafLeftArmRoll1TField()
    LeafLeftArmRoll1Tx = LeafLeftArmRoll1T.LeafLeftArmRoll1Tx
    LeafLeftArmRoll1Ty = LeafLeftArmRoll1T.LeafLeftArmRoll1Ty
    LeafLeftArmRoll1Tz = LeafLeftArmRoll1T.LeafLeftArmRoll1Tz

    LeafLeftArmRoll1R = LeafLeftArmRoll1RField()
    LeafLeftArmRoll1Rx = LeafLeftArmRoll1R.LeafLeftArmRoll1Rx
    LeafLeftArmRoll1Ry = LeafLeftArmRoll1R.LeafLeftArmRoll1Ry
    LeafLeftArmRoll1Rz = LeafLeftArmRoll1R.LeafLeftArmRoll1Rz

    LeafLeftArmRoll1S = LeafLeftArmRoll1SField()
    LeafLeftArmRoll1Sx = LeafLeftArmRoll1S.LeafLeftArmRoll1Sx
    LeafLeftArmRoll1Sy = LeafLeftArmRoll1S.LeafLeftArmRoll1Sy
    LeafLeftArmRoll1Sz = LeafLeftArmRoll1S.LeafLeftArmRoll1Sz

    LeafLeftForeArmRoll1T = LeafLeftForeArmRoll1TField()
    LeafLeftForeArmRoll1Tx = LeafLeftForeArmRoll1T.LeafLeftForeArmRoll1Tx
    LeafLeftForeArmRoll1Ty = LeafLeftForeArmRoll1T.LeafLeftForeArmRoll1Ty
    LeafLeftForeArmRoll1Tz = LeafLeftForeArmRoll1T.LeafLeftForeArmRoll1Tz

    LeafLeftForeArmRoll1R = LeafLeftForeArmRoll1RField()
    LeafLeftForeArmRoll1Rx = LeafLeftForeArmRoll1R.LeafLeftForeArmRoll1Rx
    LeafLeftForeArmRoll1Ry = LeafLeftForeArmRoll1R.LeafLeftForeArmRoll1Ry
    LeafLeftForeArmRoll1Rz = LeafLeftForeArmRoll1R.LeafLeftForeArmRoll1Rz

    LeafLeftForeArmRoll1S = LeafLeftForeArmRoll1SField()
    LeafLeftForeArmRoll1Sx = LeafLeftForeArmRoll1S.LeafLeftForeArmRoll1Sx
    LeafLeftForeArmRoll1Sy = LeafLeftForeArmRoll1S.LeafLeftForeArmRoll1Sy
    LeafLeftForeArmRoll1Sz = LeafLeftForeArmRoll1S.LeafLeftForeArmRoll1Sz

    LeafRightArmRoll1T = LeafRightArmRoll1TField()
    LeafRightArmRoll1Tx = LeafRightArmRoll1T.LeafRightArmRoll1Tx
    LeafRightArmRoll1Ty = LeafRightArmRoll1T.LeafRightArmRoll1Ty
    LeafRightArmRoll1Tz = LeafRightArmRoll1T.LeafRightArmRoll1Tz

    LeafRightArmRoll1R = LeafRightArmRoll1RField()
    LeafRightArmRoll1Rx = LeafRightArmRoll1R.LeafRightArmRoll1Rx
    LeafRightArmRoll1Ry = LeafRightArmRoll1R.LeafRightArmRoll1Ry
    LeafRightArmRoll1Rz = LeafRightArmRoll1R.LeafRightArmRoll1Rz

    LeafRightArmRoll1S = LeafRightArmRoll1SField()
    LeafRightArmRoll1Sx = LeafRightArmRoll1S.LeafRightArmRoll1Sx
    LeafRightArmRoll1Sy = LeafRightArmRoll1S.LeafRightArmRoll1Sy
    LeafRightArmRoll1Sz = LeafRightArmRoll1S.LeafRightArmRoll1Sz

    LeafRightForeArmRoll1T = LeafRightForeArmRoll1TField()
    LeafRightForeArmRoll1Tx = LeafRightForeArmRoll1T.LeafRightForeArmRoll1Tx
    LeafRightForeArmRoll1Ty = LeafRightForeArmRoll1T.LeafRightForeArmRoll1Ty
    LeafRightForeArmRoll1Tz = LeafRightForeArmRoll1T.LeafRightForeArmRoll1Tz

    LeafRightForeArmRoll1R = LeafRightForeArmRoll1RField()
    LeafRightForeArmRoll1Rx = LeafRightForeArmRoll1R.LeafRightForeArmRoll1Rx
    LeafRightForeArmRoll1Ry = LeafRightForeArmRoll1R.LeafRightForeArmRoll1Ry
    LeafRightForeArmRoll1Rz = LeafRightForeArmRoll1R.LeafRightForeArmRoll1Rz

    LeafRightForeArmRoll1S = LeafRightForeArmRoll1SField()
    LeafRightForeArmRoll1Sx = LeafRightForeArmRoll1S.LeafRightForeArmRoll1Sx
    LeafRightForeArmRoll1Sy = LeafRightForeArmRoll1S.LeafRightForeArmRoll1Sy
    LeafRightForeArmRoll1Sz = LeafRightForeArmRoll1S.LeafRightForeArmRoll1Sz

    LeafLeftUpLegRoll2T = LeafLeftUpLegRoll2TField()
    LeafLeftUpLegRoll2Tx = LeafLeftUpLegRoll2T.LeafLeftUpLegRoll2Tx
    LeafLeftUpLegRoll2Ty = LeafLeftUpLegRoll2T.LeafLeftUpLegRoll2Ty
    LeafLeftUpLegRoll2Tz = LeafLeftUpLegRoll2T.LeafLeftUpLegRoll2Tz

    LeafLeftUpLegRoll2R = LeafLeftUpLegRoll2RField()
    LeafLeftUpLegRoll2Rx = LeafLeftUpLegRoll2R.LeafLeftUpLegRoll2Rx
    LeafLeftUpLegRoll2Ry = LeafLeftUpLegRoll2R.LeafLeftUpLegRoll2Ry
    LeafLeftUpLegRoll2Rz = LeafLeftUpLegRoll2R.LeafLeftUpLegRoll2Rz

    LeafLeftUpLegRoll2S = LeafLeftUpLegRoll2SField()
    LeafLeftUpLegRoll2Sx = LeafLeftUpLegRoll2S.LeafLeftUpLegRoll2Sx
    LeafLeftUpLegRoll2Sy = LeafLeftUpLegRoll2S.LeafLeftUpLegRoll2Sy
    LeafLeftUpLegRoll2Sz = LeafLeftUpLegRoll2S.LeafLeftUpLegRoll2Sz

    LeafLeftLegRoll2T = LeafLeftLegRoll2TField()
    LeafLeftLegRoll2Tx = LeafLeftLegRoll2T.LeafLeftLegRoll2Tx
    LeafLeftLegRoll2Ty = LeafLeftLegRoll2T.LeafLeftLegRoll2Ty
    LeafLeftLegRoll2Tz = LeafLeftLegRoll2T.LeafLeftLegRoll2Tz

    LeafLeftLegRoll2R = LeafLeftLegRoll2RField()
    LeafLeftLegRoll2Rx = LeafLeftLegRoll2R.LeafLeftLegRoll2Rx
    LeafLeftLegRoll2Ry = LeafLeftLegRoll2R.LeafLeftLegRoll2Ry
    LeafLeftLegRoll2Rz = LeafLeftLegRoll2R.LeafLeftLegRoll2Rz

    LeafLeftLegRoll2S = LeafLeftLegRoll2SField()
    LeafLeftLegRoll2Sx = LeafLeftLegRoll2S.LeafLeftLegRoll2Sx
    LeafLeftLegRoll2Sy = LeafLeftLegRoll2S.LeafLeftLegRoll2Sy
    LeafLeftLegRoll2Sz = LeafLeftLegRoll2S.LeafLeftLegRoll2Sz

    LeafRightUpLegRoll2T = LeafRightUpLegRoll2TField()
    LeafRightUpLegRoll2Tx = LeafRightUpLegRoll2T.LeafRightUpLegRoll2Tx
    LeafRightUpLegRoll2Ty = LeafRightUpLegRoll2T.LeafRightUpLegRoll2Ty
    LeafRightUpLegRoll2Tz = LeafRightUpLegRoll2T.LeafRightUpLegRoll2Tz

    LeafRightUpLegRoll2R = LeafRightUpLegRoll2RField()
    LeafRightUpLegRoll2Rx = LeafRightUpLegRoll2R.LeafRightUpLegRoll2Rx
    LeafRightUpLegRoll2Ry = LeafRightUpLegRoll2R.LeafRightUpLegRoll2Ry
    LeafRightUpLegRoll2Rz = LeafRightUpLegRoll2R.LeafRightUpLegRoll2Rz

    LeafRightUpLegRoll2S = LeafRightUpLegRoll2SField()
    LeafRightUpLegRoll2Sx = LeafRightUpLegRoll2S.LeafRightUpLegRoll2Sx
    LeafRightUpLegRoll2Sy = LeafRightUpLegRoll2S.LeafRightUpLegRoll2Sy
    LeafRightUpLegRoll2Sz = LeafRightUpLegRoll2S.LeafRightUpLegRoll2Sz

    LeafRightLegRoll2T = LeafRightLegRoll2TField()
    LeafRightLegRoll2Tx = LeafRightLegRoll2T.LeafRightLegRoll2Tx
    LeafRightLegRoll2Ty = LeafRightLegRoll2T.LeafRightLegRoll2Ty
    LeafRightLegRoll2Tz = LeafRightLegRoll2T.LeafRightLegRoll2Tz

    LeafRightLegRoll2R = LeafRightLegRoll2RField()
    LeafRightLegRoll2Rx = LeafRightLegRoll2R.LeafRightLegRoll2Rx
    LeafRightLegRoll2Ry = LeafRightLegRoll2R.LeafRightLegRoll2Ry
    LeafRightLegRoll2Rz = LeafRightLegRoll2R.LeafRightLegRoll2Rz

    LeafRightLegRoll2S = LeafRightLegRoll2SField()
    LeafRightLegRoll2Sx = LeafRightLegRoll2S.LeafRightLegRoll2Sx
    LeafRightLegRoll2Sy = LeafRightLegRoll2S.LeafRightLegRoll2Sy
    LeafRightLegRoll2Sz = LeafRightLegRoll2S.LeafRightLegRoll2Sz

    LeafLeftArmRoll2T = LeafLeftArmRoll2TField()
    LeafLeftArmRoll2Tx = LeafLeftArmRoll2T.LeafLeftArmRoll2Tx
    LeafLeftArmRoll2Ty = LeafLeftArmRoll2T.LeafLeftArmRoll2Ty
    LeafLeftArmRoll2Tz = LeafLeftArmRoll2T.LeafLeftArmRoll2Tz

    LeafLeftArmRoll2R = LeafLeftArmRoll2RField()
    LeafLeftArmRoll2Rx = LeafLeftArmRoll2R.LeafLeftArmRoll2Rx
    LeafLeftArmRoll2Ry = LeafLeftArmRoll2R.LeafLeftArmRoll2Ry
    LeafLeftArmRoll2Rz = LeafLeftArmRoll2R.LeafLeftArmRoll2Rz

    LeafLeftArmRoll2S = LeafLeftArmRoll2SField()
    LeafLeftArmRoll2Sx = LeafLeftArmRoll2S.LeafLeftArmRoll2Sx
    LeafLeftArmRoll2Sy = LeafLeftArmRoll2S.LeafLeftArmRoll2Sy
    LeafLeftArmRoll2Sz = LeafLeftArmRoll2S.LeafLeftArmRoll2Sz

    LeafLeftForeArmRoll2T = LeafLeftForeArmRoll2TField()
    LeafLeftForeArmRoll2Tx = LeafLeftForeArmRoll2T.LeafLeftForeArmRoll2Tx
    LeafLeftForeArmRoll2Ty = LeafLeftForeArmRoll2T.LeafLeftForeArmRoll2Ty
    LeafLeftForeArmRoll2Tz = LeafLeftForeArmRoll2T.LeafLeftForeArmRoll2Tz

    LeafLeftForeArmRoll2R = LeafLeftForeArmRoll2RField()
    LeafLeftForeArmRoll2Rx = LeafLeftForeArmRoll2R.LeafLeftForeArmRoll2Rx
    LeafLeftForeArmRoll2Ry = LeafLeftForeArmRoll2R.LeafLeftForeArmRoll2Ry
    LeafLeftForeArmRoll2Rz = LeafLeftForeArmRoll2R.LeafLeftForeArmRoll2Rz

    LeafLeftForeArmRoll2S = LeafLeftForeArmRoll2SField()
    LeafLeftForeArmRoll2Sx = LeafLeftForeArmRoll2S.LeafLeftForeArmRoll2Sx
    LeafLeftForeArmRoll2Sy = LeafLeftForeArmRoll2S.LeafLeftForeArmRoll2Sy
    LeafLeftForeArmRoll2Sz = LeafLeftForeArmRoll2S.LeafLeftForeArmRoll2Sz

    LeafRightArmRoll2T = LeafRightArmRoll2TField()
    LeafRightArmRoll2Tx = LeafRightArmRoll2T.LeafRightArmRoll2Tx
    LeafRightArmRoll2Ty = LeafRightArmRoll2T.LeafRightArmRoll2Ty
    LeafRightArmRoll2Tz = LeafRightArmRoll2T.LeafRightArmRoll2Tz

    LeafRightArmRoll2R = LeafRightArmRoll2RField()
    LeafRightArmRoll2Rx = LeafRightArmRoll2R.LeafRightArmRoll2Rx
    LeafRightArmRoll2Ry = LeafRightArmRoll2R.LeafRightArmRoll2Ry
    LeafRightArmRoll2Rz = LeafRightArmRoll2R.LeafRightArmRoll2Rz

    LeafRightArmRoll2S = LeafRightArmRoll2SField()
    LeafRightArmRoll2Sx = LeafRightArmRoll2S.LeafRightArmRoll2Sx
    LeafRightArmRoll2Sy = LeafRightArmRoll2S.LeafRightArmRoll2Sy
    LeafRightArmRoll2Sz = LeafRightArmRoll2S.LeafRightArmRoll2Sz

    LeafRightForeArmRoll2T = LeafRightForeArmRoll2TField()
    LeafRightForeArmRoll2Tx = LeafRightForeArmRoll2T.LeafRightForeArmRoll2Tx
    LeafRightForeArmRoll2Ty = LeafRightForeArmRoll2T.LeafRightForeArmRoll2Ty
    LeafRightForeArmRoll2Tz = LeafRightForeArmRoll2T.LeafRightForeArmRoll2Tz

    LeafRightForeArmRoll2R = LeafRightForeArmRoll2RField()
    LeafRightForeArmRoll2Rx = LeafRightForeArmRoll2R.LeafRightForeArmRoll2Rx
    LeafRightForeArmRoll2Ry = LeafRightForeArmRoll2R.LeafRightForeArmRoll2Ry
    LeafRightForeArmRoll2Rz = LeafRightForeArmRoll2R.LeafRightForeArmRoll2Rz

    LeafRightForeArmRoll2S = LeafRightForeArmRoll2SField()
    LeafRightForeArmRoll2Sx = LeafRightForeArmRoll2S.LeafRightForeArmRoll2Sx
    LeafRightForeArmRoll2Sy = LeafRightForeArmRoll2S.LeafRightForeArmRoll2Sy
    LeafRightForeArmRoll2Sz = LeafRightForeArmRoll2S.LeafRightForeArmRoll2Sz

    LeafLeftUpLegRoll3T = LeafLeftUpLegRoll3TField()
    LeafLeftUpLegRoll3Tx = LeafLeftUpLegRoll3T.LeafLeftUpLegRoll3Tx
    LeafLeftUpLegRoll3Ty = LeafLeftUpLegRoll3T.LeafLeftUpLegRoll3Ty
    LeafLeftUpLegRoll3Tz = LeafLeftUpLegRoll3T.LeafLeftUpLegRoll3Tz

    LeafLeftUpLegRoll3R = LeafLeftUpLegRoll3RField()
    LeafLeftUpLegRoll3Rx = LeafLeftUpLegRoll3R.LeafLeftUpLegRoll3Rx
    LeafLeftUpLegRoll3Ry = LeafLeftUpLegRoll3R.LeafLeftUpLegRoll3Ry
    LeafLeftUpLegRoll3Rz = LeafLeftUpLegRoll3R.LeafLeftUpLegRoll3Rz

    LeafLeftUpLegRoll3S = LeafLeftUpLegRoll3SField()
    LeafLeftUpLegRoll3Sx = LeafLeftUpLegRoll3S.LeafLeftUpLegRoll3Sx
    LeafLeftUpLegRoll3Sy = LeafLeftUpLegRoll3S.LeafLeftUpLegRoll3Sy
    LeafLeftUpLegRoll3Sz = LeafLeftUpLegRoll3S.LeafLeftUpLegRoll3Sz

    LeafLeftLegRoll3T = LeafLeftLegRoll3TField()
    LeafLeftLegRoll3Tx = LeafLeftLegRoll3T.LeafLeftLegRoll3Tx
    LeafLeftLegRoll3Ty = LeafLeftLegRoll3T.LeafLeftLegRoll3Ty
    LeafLeftLegRoll3Tz = LeafLeftLegRoll3T.LeafLeftLegRoll3Tz

    LeafLeftLegRoll3R = LeafLeftLegRoll3RField()
    LeafLeftLegRoll3Rx = LeafLeftLegRoll3R.LeafLeftLegRoll3Rx
    LeafLeftLegRoll3Ry = LeafLeftLegRoll3R.LeafLeftLegRoll3Ry
    LeafLeftLegRoll3Rz = LeafLeftLegRoll3R.LeafLeftLegRoll3Rz

    LeafLeftLegRoll3S = LeafLeftLegRoll3SField()
    LeafLeftLegRoll3Sx = LeafLeftLegRoll3S.LeafLeftLegRoll3Sx
    LeafLeftLegRoll3Sy = LeafLeftLegRoll3S.LeafLeftLegRoll3Sy
    LeafLeftLegRoll3Sz = LeafLeftLegRoll3S.LeafLeftLegRoll3Sz

    LeafRightUpLegRoll3T = LeafRightUpLegRoll3TField()
    LeafRightUpLegRoll3Tx = LeafRightUpLegRoll3T.LeafRightUpLegRoll3Tx
    LeafRightUpLegRoll3Ty = LeafRightUpLegRoll3T.LeafRightUpLegRoll3Ty
    LeafRightUpLegRoll3Tz = LeafRightUpLegRoll3T.LeafRightUpLegRoll3Tz

    LeafRightUpLegRoll3R = LeafRightUpLegRoll3RField()
    LeafRightUpLegRoll3Rx = LeafRightUpLegRoll3R.LeafRightUpLegRoll3Rx
    LeafRightUpLegRoll3Ry = LeafRightUpLegRoll3R.LeafRightUpLegRoll3Ry
    LeafRightUpLegRoll3Rz = LeafRightUpLegRoll3R.LeafRightUpLegRoll3Rz

    LeafRightUpLegRoll3S = LeafRightUpLegRoll3SField()
    LeafRightUpLegRoll3Sx = LeafRightUpLegRoll3S.LeafRightUpLegRoll3Sx
    LeafRightUpLegRoll3Sy = LeafRightUpLegRoll3S.LeafRightUpLegRoll3Sy
    LeafRightUpLegRoll3Sz = LeafRightUpLegRoll3S.LeafRightUpLegRoll3Sz

    LeafRightLegRoll3T = LeafRightLegRoll3TField()
    LeafRightLegRoll3Tx = LeafRightLegRoll3T.LeafRightLegRoll3Tx
    LeafRightLegRoll3Ty = LeafRightLegRoll3T.LeafRightLegRoll3Ty
    LeafRightLegRoll3Tz = LeafRightLegRoll3T.LeafRightLegRoll3Tz

    LeafRightLegRoll3R = LeafRightLegRoll3RField()
    LeafRightLegRoll3Rx = LeafRightLegRoll3R.LeafRightLegRoll3Rx
    LeafRightLegRoll3Ry = LeafRightLegRoll3R.LeafRightLegRoll3Ry
    LeafRightLegRoll3Rz = LeafRightLegRoll3R.LeafRightLegRoll3Rz

    LeafRightLegRoll3S = LeafRightLegRoll3SField()
    LeafRightLegRoll3Sx = LeafRightLegRoll3S.LeafRightLegRoll3Sx
    LeafRightLegRoll3Sy = LeafRightLegRoll3S.LeafRightLegRoll3Sy
    LeafRightLegRoll3Sz = LeafRightLegRoll3S.LeafRightLegRoll3Sz

    LeafLeftArmRoll3T = LeafLeftArmRoll3TField()
    LeafLeftArmRoll3Tx = LeafLeftArmRoll3T.LeafLeftArmRoll3Tx
    LeafLeftArmRoll3Ty = LeafLeftArmRoll3T.LeafLeftArmRoll3Ty
    LeafLeftArmRoll3Tz = LeafLeftArmRoll3T.LeafLeftArmRoll3Tz

    LeafLeftArmRoll3R = LeafLeftArmRoll3RField()
    LeafLeftArmRoll3Rx = LeafLeftArmRoll3R.LeafLeftArmRoll3Rx
    LeafLeftArmRoll3Ry = LeafLeftArmRoll3R.LeafLeftArmRoll3Ry
    LeafLeftArmRoll3Rz = LeafLeftArmRoll3R.LeafLeftArmRoll3Rz

    LeafLeftArmRoll3S = LeafLeftArmRoll3SField()
    LeafLeftArmRoll3Sx = LeafLeftArmRoll3S.LeafLeftArmRoll3Sx
    LeafLeftArmRoll3Sy = LeafLeftArmRoll3S.LeafLeftArmRoll3Sy
    LeafLeftArmRoll3Sz = LeafLeftArmRoll3S.LeafLeftArmRoll3Sz

    LeafLeftForeArmRoll3T = LeafLeftForeArmRoll3TField()
    LeafLeftForeArmRoll3Tx = LeafLeftForeArmRoll3T.LeafLeftForeArmRoll3Tx
    LeafLeftForeArmRoll3Ty = LeafLeftForeArmRoll3T.LeafLeftForeArmRoll3Ty
    LeafLeftForeArmRoll3Tz = LeafLeftForeArmRoll3T.LeafLeftForeArmRoll3Tz

    LeafLeftForeArmRoll3R = LeafLeftForeArmRoll3RField()
    LeafLeftForeArmRoll3Rx = LeafLeftForeArmRoll3R.LeafLeftForeArmRoll3Rx
    LeafLeftForeArmRoll3Ry = LeafLeftForeArmRoll3R.LeafLeftForeArmRoll3Ry
    LeafLeftForeArmRoll3Rz = LeafLeftForeArmRoll3R.LeafLeftForeArmRoll3Rz

    LeafLeftForeArmRoll3S = LeafLeftForeArmRoll3SField()
    LeafLeftForeArmRoll3Sx = LeafLeftForeArmRoll3S.LeafLeftForeArmRoll3Sx
    LeafLeftForeArmRoll3Sy = LeafLeftForeArmRoll3S.LeafLeftForeArmRoll3Sy
    LeafLeftForeArmRoll3Sz = LeafLeftForeArmRoll3S.LeafLeftForeArmRoll3Sz

    LeafRightArmRoll3T = LeafRightArmRoll3TField()
    LeafRightArmRoll3Tx = LeafRightArmRoll3T.LeafRightArmRoll3Tx
    LeafRightArmRoll3Ty = LeafRightArmRoll3T.LeafRightArmRoll3Ty
    LeafRightArmRoll3Tz = LeafRightArmRoll3T.LeafRightArmRoll3Tz

    LeafRightArmRoll3R = LeafRightArmRoll3RField()
    LeafRightArmRoll3Rx = LeafRightArmRoll3R.LeafRightArmRoll3Rx
    LeafRightArmRoll3Ry = LeafRightArmRoll3R.LeafRightArmRoll3Ry
    LeafRightArmRoll3Rz = LeafRightArmRoll3R.LeafRightArmRoll3Rz

    LeafRightArmRoll3S = LeafRightArmRoll3SField()
    LeafRightArmRoll3Sx = LeafRightArmRoll3S.LeafRightArmRoll3Sx
    LeafRightArmRoll3Sy = LeafRightArmRoll3S.LeafRightArmRoll3Sy
    LeafRightArmRoll3Sz = LeafRightArmRoll3S.LeafRightArmRoll3Sz

    LeafRightForeArmRoll3T = LeafRightForeArmRoll3TField()
    LeafRightForeArmRoll3Tx = LeafRightForeArmRoll3T.LeafRightForeArmRoll3Tx
    LeafRightForeArmRoll3Ty = LeafRightForeArmRoll3T.LeafRightForeArmRoll3Ty
    LeafRightForeArmRoll3Tz = LeafRightForeArmRoll3T.LeafRightForeArmRoll3Tz

    LeafRightForeArmRoll3R = LeafRightForeArmRoll3RField()
    LeafRightForeArmRoll3Rx = LeafRightForeArmRoll3R.LeafRightForeArmRoll3Rx
    LeafRightForeArmRoll3Ry = LeafRightForeArmRoll3R.LeafRightForeArmRoll3Ry
    LeafRightForeArmRoll3Rz = LeafRightForeArmRoll3R.LeafRightForeArmRoll3Rz

    LeafRightForeArmRoll3S = LeafRightForeArmRoll3SField()
    LeafRightForeArmRoll3Sx = LeafRightForeArmRoll3S.LeafRightForeArmRoll3Sx
    LeafRightForeArmRoll3Sy = LeafRightForeArmRoll3S.LeafRightForeArmRoll3Sy
    LeafRightForeArmRoll3Sz = LeafRightForeArmRoll3S.LeafRightForeArmRoll3Sz

    LeafLeftUpLegRoll4T = LeafLeftUpLegRoll4TField()
    LeafLeftUpLegRoll4Tx = LeafLeftUpLegRoll4T.LeafLeftUpLegRoll4Tx
    LeafLeftUpLegRoll4Ty = LeafLeftUpLegRoll4T.LeafLeftUpLegRoll4Ty
    LeafLeftUpLegRoll4Tz = LeafLeftUpLegRoll4T.LeafLeftUpLegRoll4Tz

    LeafLeftUpLegRoll4R = LeafLeftUpLegRoll4RField()
    LeafLeftUpLegRoll4Rx = LeafLeftUpLegRoll4R.LeafLeftUpLegRoll4Rx
    LeafLeftUpLegRoll4Ry = LeafLeftUpLegRoll4R.LeafLeftUpLegRoll4Ry
    LeafLeftUpLegRoll4Rz = LeafLeftUpLegRoll4R.LeafLeftUpLegRoll4Rz

    LeafLeftUpLegRoll4S = LeafLeftUpLegRoll4SField()
    LeafLeftUpLegRoll4Sx = LeafLeftUpLegRoll4S.LeafLeftUpLegRoll4Sx
    LeafLeftUpLegRoll4Sy = LeafLeftUpLegRoll4S.LeafLeftUpLegRoll4Sy
    LeafLeftUpLegRoll4Sz = LeafLeftUpLegRoll4S.LeafLeftUpLegRoll4Sz

    LeafLeftLegRoll4T = LeafLeftLegRoll4TField()
    LeafLeftLegRoll4Tx = LeafLeftLegRoll4T.LeafLeftLegRoll4Tx
    LeafLeftLegRoll4Ty = LeafLeftLegRoll4T.LeafLeftLegRoll4Ty
    LeafLeftLegRoll4Tz = LeafLeftLegRoll4T.LeafLeftLegRoll4Tz

    LeafLeftLegRoll4R = LeafLeftLegRoll4RField()
    LeafLeftLegRoll4Rx = LeafLeftLegRoll4R.LeafLeftLegRoll4Rx
    LeafLeftLegRoll4Ry = LeafLeftLegRoll4R.LeafLeftLegRoll4Ry
    LeafLeftLegRoll4Rz = LeafLeftLegRoll4R.LeafLeftLegRoll4Rz

    LeafLeftLegRoll4S = LeafLeftLegRoll4SField()
    LeafLeftLegRoll4Sx = LeafLeftLegRoll4S.LeafLeftLegRoll4Sx
    LeafLeftLegRoll4Sy = LeafLeftLegRoll4S.LeafLeftLegRoll4Sy
    LeafLeftLegRoll4Sz = LeafLeftLegRoll4S.LeafLeftLegRoll4Sz

    LeafRightUpLegRoll4T = LeafRightUpLegRoll4TField()
    LeafRightUpLegRoll4Tx = LeafRightUpLegRoll4T.LeafRightUpLegRoll4Tx
    LeafRightUpLegRoll4Ty = LeafRightUpLegRoll4T.LeafRightUpLegRoll4Ty
    LeafRightUpLegRoll4Tz = LeafRightUpLegRoll4T.LeafRightUpLegRoll4Tz

    LeafRightUpLegRoll4R = LeafRightUpLegRoll4RField()
    LeafRightUpLegRoll4Rx = LeafRightUpLegRoll4R.LeafRightUpLegRoll4Rx
    LeafRightUpLegRoll4Ry = LeafRightUpLegRoll4R.LeafRightUpLegRoll4Ry
    LeafRightUpLegRoll4Rz = LeafRightUpLegRoll4R.LeafRightUpLegRoll4Rz

    LeafRightUpLegRoll4S = LeafRightUpLegRoll4SField()
    LeafRightUpLegRoll4Sx = LeafRightUpLegRoll4S.LeafRightUpLegRoll4Sx
    LeafRightUpLegRoll4Sy = LeafRightUpLegRoll4S.LeafRightUpLegRoll4Sy
    LeafRightUpLegRoll4Sz = LeafRightUpLegRoll4S.LeafRightUpLegRoll4Sz

    LeafRightLegRoll4T = LeafRightLegRoll4TField()
    LeafRightLegRoll4Tx = LeafRightLegRoll4T.LeafRightLegRoll4Tx
    LeafRightLegRoll4Ty = LeafRightLegRoll4T.LeafRightLegRoll4Ty
    LeafRightLegRoll4Tz = LeafRightLegRoll4T.LeafRightLegRoll4Tz

    LeafRightLegRoll4R = LeafRightLegRoll4RField()
    LeafRightLegRoll4Rx = LeafRightLegRoll4R.LeafRightLegRoll4Rx
    LeafRightLegRoll4Ry = LeafRightLegRoll4R.LeafRightLegRoll4Ry
    LeafRightLegRoll4Rz = LeafRightLegRoll4R.LeafRightLegRoll4Rz

    LeafRightLegRoll4S = LeafRightLegRoll4SField()
    LeafRightLegRoll4Sx = LeafRightLegRoll4S.LeafRightLegRoll4Sx
    LeafRightLegRoll4Sy = LeafRightLegRoll4S.LeafRightLegRoll4Sy
    LeafRightLegRoll4Sz = LeafRightLegRoll4S.LeafRightLegRoll4Sz

    LeafLeftArmRoll4T = LeafLeftArmRoll4TField()
    LeafLeftArmRoll4Tx = LeafLeftArmRoll4T.LeafLeftArmRoll4Tx
    LeafLeftArmRoll4Ty = LeafLeftArmRoll4T.LeafLeftArmRoll4Ty
    LeafLeftArmRoll4Tz = LeafLeftArmRoll4T.LeafLeftArmRoll4Tz

    LeafLeftArmRoll4R = LeafLeftArmRoll4RField()
    LeafLeftArmRoll4Rx = LeafLeftArmRoll4R.LeafLeftArmRoll4Rx
    LeafLeftArmRoll4Ry = LeafLeftArmRoll4R.LeafLeftArmRoll4Ry
    LeafLeftArmRoll4Rz = LeafLeftArmRoll4R.LeafLeftArmRoll4Rz

    LeafLeftArmRoll4S = LeafLeftArmRoll4SField()
    LeafLeftArmRoll4Sx = LeafLeftArmRoll4S.LeafLeftArmRoll4Sx
    LeafLeftArmRoll4Sy = LeafLeftArmRoll4S.LeafLeftArmRoll4Sy
    LeafLeftArmRoll4Sz = LeafLeftArmRoll4S.LeafLeftArmRoll4Sz

    LeafLeftForeArmRoll4T = LeafLeftForeArmRoll4TField()
    LeafLeftForeArmRoll4Tx = LeafLeftForeArmRoll4T.LeafLeftForeArmRoll4Tx
    LeafLeftForeArmRoll4Ty = LeafLeftForeArmRoll4T.LeafLeftForeArmRoll4Ty
    LeafLeftForeArmRoll4Tz = LeafLeftForeArmRoll4T.LeafLeftForeArmRoll4Tz

    LeafLeftForeArmRoll4R = LeafLeftForeArmRoll4RField()
    LeafLeftForeArmRoll4Rx = LeafLeftForeArmRoll4R.LeafLeftForeArmRoll4Rx
    LeafLeftForeArmRoll4Ry = LeafLeftForeArmRoll4R.LeafLeftForeArmRoll4Ry
    LeafLeftForeArmRoll4Rz = LeafLeftForeArmRoll4R.LeafLeftForeArmRoll4Rz

    LeafLeftForeArmRoll4S = LeafLeftForeArmRoll4SField()
    LeafLeftForeArmRoll4Sx = LeafLeftForeArmRoll4S.LeafLeftForeArmRoll4Sx
    LeafLeftForeArmRoll4Sy = LeafLeftForeArmRoll4S.LeafLeftForeArmRoll4Sy
    LeafLeftForeArmRoll4Sz = LeafLeftForeArmRoll4S.LeafLeftForeArmRoll4Sz

    LeafRightArmRoll4T = LeafRightArmRoll4TField()
    LeafRightArmRoll4Tx = LeafRightArmRoll4T.LeafRightArmRoll4Tx
    LeafRightArmRoll4Ty = LeafRightArmRoll4T.LeafRightArmRoll4Ty
    LeafRightArmRoll4Tz = LeafRightArmRoll4T.LeafRightArmRoll4Tz

    LeafRightArmRoll4R = LeafRightArmRoll4RField()
    LeafRightArmRoll4Rx = LeafRightArmRoll4R.LeafRightArmRoll4Rx
    LeafRightArmRoll4Ry = LeafRightArmRoll4R.LeafRightArmRoll4Ry
    LeafRightArmRoll4Rz = LeafRightArmRoll4R.LeafRightArmRoll4Rz

    LeafRightArmRoll4S = LeafRightArmRoll4SField()
    LeafRightArmRoll4Sx = LeafRightArmRoll4S.LeafRightArmRoll4Sx
    LeafRightArmRoll4Sy = LeafRightArmRoll4S.LeafRightArmRoll4Sy
    LeafRightArmRoll4Sz = LeafRightArmRoll4S.LeafRightArmRoll4Sz

    LeafRightForeArmRoll4T = LeafRightForeArmRoll4TField()
    LeafRightForeArmRoll4Tx = LeafRightForeArmRoll4T.LeafRightForeArmRoll4Tx
    LeafRightForeArmRoll4Ty = LeafRightForeArmRoll4T.LeafRightForeArmRoll4Ty
    LeafRightForeArmRoll4Tz = LeafRightForeArmRoll4T.LeafRightForeArmRoll4Tz

    LeafRightForeArmRoll4R = LeafRightForeArmRoll4RField()
    LeafRightForeArmRoll4Rx = LeafRightForeArmRoll4R.LeafRightForeArmRoll4Rx
    LeafRightForeArmRoll4Ry = LeafRightForeArmRoll4R.LeafRightForeArmRoll4Ry
    LeafRightForeArmRoll4Rz = LeafRightForeArmRoll4R.LeafRightForeArmRoll4Rz

    LeafRightForeArmRoll4S = LeafRightForeArmRoll4SField()
    LeafRightForeArmRoll4Sx = LeafRightForeArmRoll4S.LeafRightForeArmRoll4Sx
    LeafRightForeArmRoll4Sy = LeafRightForeArmRoll4S.LeafRightForeArmRoll4Sy
    LeafRightForeArmRoll4Sz = LeafRightForeArmRoll4S.LeafRightForeArmRoll4Sz

    LeafLeftUpLegRoll5T = LeafLeftUpLegRoll5TField()
    LeafLeftUpLegRoll5Tx = LeafLeftUpLegRoll5T.LeafLeftUpLegRoll5Tx
    LeafLeftUpLegRoll5Ty = LeafLeftUpLegRoll5T.LeafLeftUpLegRoll5Ty
    LeafLeftUpLegRoll5Tz = LeafLeftUpLegRoll5T.LeafLeftUpLegRoll5Tz

    LeafLeftUpLegRoll5R = LeafLeftUpLegRoll5RField()
    LeafLeftUpLegRoll5Rx = LeafLeftUpLegRoll5R.LeafLeftUpLegRoll5Rx
    LeafLeftUpLegRoll5Ry = LeafLeftUpLegRoll5R.LeafLeftUpLegRoll5Ry
    LeafLeftUpLegRoll5Rz = LeafLeftUpLegRoll5R.LeafLeftUpLegRoll5Rz

    LeafLeftUpLegRoll5S = LeafLeftUpLegRoll5SField()
    LeafLeftUpLegRoll5Sx = LeafLeftUpLegRoll5S.LeafLeftUpLegRoll5Sx
    LeafLeftUpLegRoll5Sy = LeafLeftUpLegRoll5S.LeafLeftUpLegRoll5Sy
    LeafLeftUpLegRoll5Sz = LeafLeftUpLegRoll5S.LeafLeftUpLegRoll5Sz

    LeafLeftLegRoll5T = LeafLeftLegRoll5TField()
    LeafLeftLegRoll5Tx = LeafLeftLegRoll5T.LeafLeftLegRoll5Tx
    LeafLeftLegRoll5Ty = LeafLeftLegRoll5T.LeafLeftLegRoll5Ty
    LeafLeftLegRoll5Tz = LeafLeftLegRoll5T.LeafLeftLegRoll5Tz

    LeafLeftLegRoll5R = LeafLeftLegRoll5RField()
    LeafLeftLegRoll5Rx = LeafLeftLegRoll5R.LeafLeftLegRoll5Rx
    LeafLeftLegRoll5Ry = LeafLeftLegRoll5R.LeafLeftLegRoll5Ry
    LeafLeftLegRoll5Rz = LeafLeftLegRoll5R.LeafLeftLegRoll5Rz

    LeafLeftLegRoll5S = LeafLeftLegRoll5SField()
    LeafLeftLegRoll5Sx = LeafLeftLegRoll5S.LeafLeftLegRoll5Sx
    LeafLeftLegRoll5Sy = LeafLeftLegRoll5S.LeafLeftLegRoll5Sy
    LeafLeftLegRoll5Sz = LeafLeftLegRoll5S.LeafLeftLegRoll5Sz

    LeafRightUpLegRoll5T = LeafRightUpLegRoll5TField()
    LeafRightUpLegRoll5Tx = LeafRightUpLegRoll5T.LeafRightUpLegRoll5Tx
    LeafRightUpLegRoll5Ty = LeafRightUpLegRoll5T.LeafRightUpLegRoll5Ty
    LeafRightUpLegRoll5Tz = LeafRightUpLegRoll5T.LeafRightUpLegRoll5Tz

    LeafRightUpLegRoll5R = LeafRightUpLegRoll5RField()
    LeafRightUpLegRoll5Rx = LeafRightUpLegRoll5R.LeafRightUpLegRoll5Rx
    LeafRightUpLegRoll5Ry = LeafRightUpLegRoll5R.LeafRightUpLegRoll5Ry
    LeafRightUpLegRoll5Rz = LeafRightUpLegRoll5R.LeafRightUpLegRoll5Rz

    LeafRightUpLegRoll5S = LeafRightUpLegRoll5SField()
    LeafRightUpLegRoll5Sx = LeafRightUpLegRoll5S.LeafRightUpLegRoll5Sx
    LeafRightUpLegRoll5Sy = LeafRightUpLegRoll5S.LeafRightUpLegRoll5Sy
    LeafRightUpLegRoll5Sz = LeafRightUpLegRoll5S.LeafRightUpLegRoll5Sz

    LeafRightLegRoll5T = LeafRightLegRoll5TField()
    LeafRightLegRoll5Tx = LeafRightLegRoll5T.LeafRightLegRoll5Tx
    LeafRightLegRoll5Ty = LeafRightLegRoll5T.LeafRightLegRoll5Ty
    LeafRightLegRoll5Tz = LeafRightLegRoll5T.LeafRightLegRoll5Tz

    LeafRightLegRoll5R = LeafRightLegRoll5RField()
    LeafRightLegRoll5Rx = LeafRightLegRoll5R.LeafRightLegRoll5Rx
    LeafRightLegRoll5Ry = LeafRightLegRoll5R.LeafRightLegRoll5Ry
    LeafRightLegRoll5Rz = LeafRightLegRoll5R.LeafRightLegRoll5Rz

    LeafRightLegRoll5S = LeafRightLegRoll5SField()
    LeafRightLegRoll5Sx = LeafRightLegRoll5S.LeafRightLegRoll5Sx
    LeafRightLegRoll5Sy = LeafRightLegRoll5S.LeafRightLegRoll5Sy
    LeafRightLegRoll5Sz = LeafRightLegRoll5S.LeafRightLegRoll5Sz

    LeafLeftArmRoll5T = LeafLeftArmRoll5TField()
    LeafLeftArmRoll5Tx = LeafLeftArmRoll5T.LeafLeftArmRoll5Tx
    LeafLeftArmRoll5Ty = LeafLeftArmRoll5T.LeafLeftArmRoll5Ty
    LeafLeftArmRoll5Tz = LeafLeftArmRoll5T.LeafLeftArmRoll5Tz

    LeafLeftArmRoll5R = LeafLeftArmRoll5RField()
    LeafLeftArmRoll5Rx = LeafLeftArmRoll5R.LeafLeftArmRoll5Rx
    LeafLeftArmRoll5Ry = LeafLeftArmRoll5R.LeafLeftArmRoll5Ry
    LeafLeftArmRoll5Rz = LeafLeftArmRoll5R.LeafLeftArmRoll5Rz

    LeafLeftArmRoll5S = LeafLeftArmRoll5SField()
    LeafLeftArmRoll5Sx = LeafLeftArmRoll5S.LeafLeftArmRoll5Sx
    LeafLeftArmRoll5Sy = LeafLeftArmRoll5S.LeafLeftArmRoll5Sy
    LeafLeftArmRoll5Sz = LeafLeftArmRoll5S.LeafLeftArmRoll5Sz

    LeafLeftForeArmRoll5T = LeafLeftForeArmRoll5TField()
    LeafLeftForeArmRoll5Tx = LeafLeftForeArmRoll5T.LeafLeftForeArmRoll5Tx
    LeafLeftForeArmRoll5Ty = LeafLeftForeArmRoll5T.LeafLeftForeArmRoll5Ty
    LeafLeftForeArmRoll5Tz = LeafLeftForeArmRoll5T.LeafLeftForeArmRoll5Tz

    LeafLeftForeArmRoll5R = LeafLeftForeArmRoll5RField()
    LeafLeftForeArmRoll5Rx = LeafLeftForeArmRoll5R.LeafLeftForeArmRoll5Rx
    LeafLeftForeArmRoll5Ry = LeafLeftForeArmRoll5R.LeafLeftForeArmRoll5Ry
    LeafLeftForeArmRoll5Rz = LeafLeftForeArmRoll5R.LeafLeftForeArmRoll5Rz

    LeafLeftForeArmRoll5S = LeafLeftForeArmRoll5SField()
    LeafLeftForeArmRoll5Sx = LeafLeftForeArmRoll5S.LeafLeftForeArmRoll5Sx
    LeafLeftForeArmRoll5Sy = LeafLeftForeArmRoll5S.LeafLeftForeArmRoll5Sy
    LeafLeftForeArmRoll5Sz = LeafLeftForeArmRoll5S.LeafLeftForeArmRoll5Sz

    LeafRightArmRoll5T = LeafRightArmRoll5TField()
    LeafRightArmRoll5Tx = LeafRightArmRoll5T.LeafRightArmRoll5Tx
    LeafRightArmRoll5Ty = LeafRightArmRoll5T.LeafRightArmRoll5Ty
    LeafRightArmRoll5Tz = LeafRightArmRoll5T.LeafRightArmRoll5Tz

    LeafRightArmRoll5R = LeafRightArmRoll5RField()
    LeafRightArmRoll5Rx = LeafRightArmRoll5R.LeafRightArmRoll5Rx
    LeafRightArmRoll5Ry = LeafRightArmRoll5R.LeafRightArmRoll5Ry
    LeafRightArmRoll5Rz = LeafRightArmRoll5R.LeafRightArmRoll5Rz

    LeafRightArmRoll5S = LeafRightArmRoll5SField()
    LeafRightArmRoll5Sx = LeafRightArmRoll5S.LeafRightArmRoll5Sx
    LeafRightArmRoll5Sy = LeafRightArmRoll5S.LeafRightArmRoll5Sy
    LeafRightArmRoll5Sz = LeafRightArmRoll5S.LeafRightArmRoll5Sz

    LeafRightForeArmRoll5T = LeafRightForeArmRoll5TField()
    LeafRightForeArmRoll5Tx = LeafRightForeArmRoll5T.LeafRightForeArmRoll5Tx
    LeafRightForeArmRoll5Ty = LeafRightForeArmRoll5T.LeafRightForeArmRoll5Ty
    LeafRightForeArmRoll5Tz = LeafRightForeArmRoll5T.LeafRightForeArmRoll5Tz

    LeafRightForeArmRoll5R = LeafRightForeArmRoll5RField()
    LeafRightForeArmRoll5Rx = LeafRightForeArmRoll5R.LeafRightForeArmRoll5Rx
    LeafRightForeArmRoll5Ry = LeafRightForeArmRoll5R.LeafRightForeArmRoll5Ry
    LeafRightForeArmRoll5Rz = LeafRightForeArmRoll5R.LeafRightForeArmRoll5Rz

    LeafRightForeArmRoll5S = LeafRightForeArmRoll5SField()
    LeafRightForeArmRoll5Sx = LeafRightForeArmRoll5S.LeafRightForeArmRoll5Sx
    LeafRightForeArmRoll5Sy = LeafRightForeArmRoll5S.LeafRightForeArmRoll5Sy
    LeafRightForeArmRoll5Sz = LeafRightForeArmRoll5S.LeafRightForeArmRoll5Sz
