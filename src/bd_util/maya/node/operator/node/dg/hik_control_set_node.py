# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField


class HIKControlSetNode(DG):
    __slots__ = ()

    NODE_TYPE = "HIKControlSetNode"

    InputCharacterDefinition = TypedField()
    HIC = InputCharacterDefinition

    Reference = MessageField()

    Hips = MessageField()

    LeftUpLeg = MessageField()

    LeftLeg = MessageField()

    LeftFoot = MessageField()

    RightUpLeg = MessageField()

    RightLeg = MessageField()

    RightFoot = MessageField()

    Spine = MessageField()

    LeftArm = MessageField()

    LeftForeArm = MessageField()

    LeftHand = MessageField()

    RightArm = MessageField()

    RightForeArm = MessageField()

    RightHand = MessageField()

    Head = MessageField()

    LeftToeBase = MessageField()

    RightToeBase = MessageField()

    LeftShoulder = MessageField()

    RightShoulder = MessageField()

    Neck = MessageField()

    LeftFingerBase = MessageField()

    RightFingerBase = MessageField()

    Spine1 = MessageField()

    Spine2 = MessageField()

    Spine3 = MessageField()

    Spine4 = MessageField()

    Spine5 = MessageField()

    Spine6 = MessageField()

    Spine7 = MessageField()

    Spine8 = MessageField()

    Spine9 = MessageField()

    Neck1 = MessageField()

    Neck2 = MessageField()

    Neck3 = MessageField()

    Neck4 = MessageField()

    Neck5 = MessageField()

    Neck6 = MessageField()

    Neck7 = MessageField()

    Neck8 = MessageField()

    Neck9 = MessageField()

    LeftUpLegRoll = MessageField()

    LeftLegRoll = MessageField()

    RightUpLegRoll = MessageField()

    RightLegRoll = MessageField()

    LeftArmRoll = MessageField()

    LeftForeArmRoll = MessageField()

    RightArmRoll = MessageField()

    RightForeArmRoll = MessageField()

    HipsTranslation = MessageField()

    LeftHandThumb1 = MessageField()

    LeftHandThumb2 = MessageField()

    LeftHandThumb3 = MessageField()

    LeftHandThumb4 = MessageField()

    LeftHandIndex1 = MessageField()

    LeftHandIndex2 = MessageField()

    LeftHandIndex3 = MessageField()

    LeftHandIndex4 = MessageField()

    LeftHandMiddle1 = MessageField()

    LeftHandMiddle2 = MessageField()

    LeftHandMiddle3 = MessageField()

    LeftHandMiddle4 = MessageField()

    LeftHandRing1 = MessageField()

    LeftHandRing2 = MessageField()

    LeftHandRing3 = MessageField()

    LeftHandRing4 = MessageField()

    LeftHandPinky1 = MessageField()

    LeftHandPinky2 = MessageField()

    LeftHandPinky3 = MessageField()

    LeftHandPinky4 = MessageField()

    LeftHandExtraFinger1 = MessageField()

    LeftHandExtraFinger2 = MessageField()

    LeftHandExtraFinger3 = MessageField()

    LeftHandExtraFinger4 = MessageField()

    RightHandThumb1 = MessageField()

    RightHandThumb2 = MessageField()

    RightHandThumb3 = MessageField()

    RightHandThumb4 = MessageField()

    RightHandIndex1 = MessageField()

    RightHandIndex2 = MessageField()

    RightHandIndex3 = MessageField()

    RightHandIndex4 = MessageField()

    RightHandMiddle1 = MessageField()

    RightHandMiddle2 = MessageField()

    RightHandMiddle3 = MessageField()

    RightHandMiddle4 = MessageField()

    RightHandRing1 = MessageField()

    RightHandRing2 = MessageField()

    RightHandRing3 = MessageField()

    RightHandRing4 = MessageField()

    RightHandPinky1 = MessageField()

    RightHandPinky2 = MessageField()

    RightHandPinky3 = MessageField()

    RightHandPinky4 = MessageField()

    RightHandExtraFinger1 = MessageField()

    RightHandExtraFinger2 = MessageField()

    RightHandExtraFinger3 = MessageField()

    RightHandExtraFinger4 = MessageField()

    LeftFootThumb1 = MessageField()

    LeftFootThumb2 = MessageField()

    LeftFootThumb3 = MessageField()

    LeftFootThumb4 = MessageField()

    LeftFootIndex1 = MessageField()

    LeftFootIndex2 = MessageField()

    LeftFootIndex3 = MessageField()

    LeftFootIndex4 = MessageField()

    LeftFootMiddle1 = MessageField()

    LeftFootMiddle2 = MessageField()

    LeftFootMiddle3 = MessageField()

    LeftFootMiddle4 = MessageField()

    LeftFootRing1 = MessageField()

    LeftFootRing2 = MessageField()

    LeftFootRing3 = MessageField()

    LeftFootRing4 = MessageField()

    LeftFootPinky1 = MessageField()

    LeftFootPinky2 = MessageField()

    LeftFootPinky3 = MessageField()

    LeftFootPinky4 = MessageField()

    LeftFootExtraFinger1 = MessageField()

    LeftFootExtraFinger2 = MessageField()

    LeftFootExtraFinger3 = MessageField()

    LeftFootExtraFinger4 = MessageField()

    RightFootThumb1 = MessageField()

    RightFootThumb2 = MessageField()

    RightFootThumb3 = MessageField()

    RightFootThumb4 = MessageField()

    RightFootIndex1 = MessageField()

    RightFootIndex2 = MessageField()

    RightFootIndex3 = MessageField()

    RightFootIndex4 = MessageField()

    RightFootMiddle1 = MessageField()

    RightFootMiddle2 = MessageField()

    RightFootMiddle3 = MessageField()

    RightFootMiddle4 = MessageField()

    RightFootRing1 = MessageField()

    RightFootRing2 = MessageField()

    RightFootRing3 = MessageField()

    RightFootRing4 = MessageField()

    RightFootPinky1 = MessageField()

    RightFootPinky2 = MessageField()

    RightFootPinky3 = MessageField()

    RightFootPinky4 = MessageField()

    RightFootExtraFinger1 = MessageField()

    RightFootExtraFinger2 = MessageField()

    RightFootExtraFinger3 = MessageField()

    RightFootExtraFinger4 = MessageField()

    LeftInHandThumb = MessageField()

    LeftInHandIndex = MessageField()

    LeftInHandMiddle = MessageField()

    LeftInHandRing = MessageField()

    LeftInHandPinky = MessageField()

    LeftInHandExtraFinger = MessageField()

    RightInHandThumb = MessageField()

    RightInHandIndex = MessageField()

    RightInHandMiddle = MessageField()

    RightInHandRing = MessageField()

    RightInHandPinky = MessageField()

    RightInHandExtraFinger = MessageField()

    LeftInFootThumb = MessageField()

    LeftInFootIndex = MessageField()

    LeftInFootMiddle = MessageField()

    LeftInFootRing = MessageField()

    LeftInFootPinky = MessageField()

    LeftInFootExtraFinger = MessageField()

    RightInFootThumb = MessageField()

    RightInFootIndex = MessageField()

    RightInFootMiddle = MessageField()

    RightInFootRing = MessageField()

    RightInFootPinky = MessageField()

    RightInFootExtraFinger = MessageField()

    LeftShoulderExtra = MessageField()

    RightShoulderExtra = MessageField()

    LeafLeftUpLegRoll1 = MessageField()

    LeafLeftLegRoll1 = MessageField()

    LeafRightUpLegRoll1 = MessageField()

    LeafRightLegRoll1 = MessageField()

    LeafLeftArmRoll1 = MessageField()

    LeafLeftForeArmRoll1 = MessageField()

    LeafRightArmRoll1 = MessageField()

    LeafRightForeArmRoll1 = MessageField()

    LeafLeftUpLegRoll2 = MessageField()

    LeafLeftLegRoll2 = MessageField()

    LeafRightUpLegRoll2 = MessageField()

    LeafRightLegRoll2 = MessageField()

    LeafLeftArmRoll2 = MessageField()

    LeafLeftForeArmRoll2 = MessageField()

    LeafRightArmRoll2 = MessageField()

    LeafRightForeArmRoll2 = MessageField()

    LeafLeftUpLegRoll3 = MessageField()

    LeafLeftLegRoll3 = MessageField()

    LeafRightUpLegRoll3 = MessageField()

    LeafRightLegRoll3 = MessageField()

    LeafLeftArmRoll3 = MessageField()

    LeafLeftForeArmRoll3 = MessageField()

    LeafRightArmRoll3 = MessageField()

    LeafRightForeArmRoll3 = MessageField()

    LeafLeftUpLegRoll4 = MessageField()

    LeafLeftLegRoll4 = MessageField()

    LeafRightUpLegRoll4 = MessageField()

    LeafRightLegRoll4 = MessageField()

    LeafLeftArmRoll4 = MessageField()

    LeafLeftForeArmRoll4 = MessageField()

    LeafRightArmRoll4 = MessageField()

    LeafRightForeArmRoll4 = MessageField()

    LeafLeftUpLegRoll5 = MessageField()

    LeafLeftLegRoll5 = MessageField()

    LeafRightUpLegRoll5 = MessageField()

    LeafRightLegRoll5 = MessageField()

    LeafLeftArmRoll5 = MessageField()

    LeafLeftForeArmRoll5 = MessageField()

    LeafRightArmRoll5 = MessageField()

    LeafRightForeArmRoll5 = MessageField()

    HipsEffector = MessageField(multi=True)

    IKNodeCurrIdx0 = LongField()

    LeftAnkleEffector = MessageField(multi=True)

    IKNodeCurrIdx1 = LongField()

    RightAnkleEffector = MessageField(multi=True)

    IKNodeCurrIdx2 = LongField()

    LeftWristEffector = MessageField(multi=True)

    IKNodeCurrIdx3 = LongField()

    RightWristEffector = MessageField(multi=True)

    IKNodeCurrIdx4 = LongField()

    LeftKneeEffector = MessageField(multi=True)

    IKNodeCurrIdx5 = LongField()

    RightKneeEffector = MessageField(multi=True)

    IKNodeCurrIdx6 = LongField()

    LeftElbowEffector = MessageField(multi=True)

    IKNodeCurrIdx7 = LongField()

    RightElbowEffector = MessageField(multi=True)

    IKNodeCurrIdx8 = LongField()

    ChestOriginEffector = MessageField(multi=True)

    IKNodeCurrIdx9 = LongField()

    ChestEndEffector = MessageField(multi=True)

    IKNodeCurrIdx10 = LongField()

    LeftFootEffector = MessageField(multi=True)

    IKNodeCurrIdx11 = LongField()

    RightFootEffector = MessageField(multi=True)

    IKNodeCurrIdx12 = LongField()

    LeftShoulderEffector = MessageField(multi=True)

    IKNodeCurrIdx13 = LongField()

    RightShoulderEffector = MessageField(multi=True)

    IKNodeCurrIdx14 = LongField()

    HeadEffector = MessageField(multi=True)

    IKNodeCurrIdx15 = LongField()

    LeftHipEffector = MessageField(multi=True)

    IKNodeCurrIdx16 = LongField()

    RightHipEffector = MessageField(multi=True)

    IKNodeCurrIdx17 = LongField()

    LeftHandEffector = MessageField(multi=True)

    IKNodeCurrIdx18 = LongField()

    RightHandEffector = MessageField(multi=True)

    IKNodeCurrIdx19 = LongField()

    LeftHandThumbEffector = MessageField(multi=True)

    IKNodeCurrIdx20 = LongField()

    LeftHandIndexEffector = MessageField(multi=True)

    IKNodeCurrIdx21 = LongField()

    LeftHandMiddleEffector = MessageField(multi=True)

    IKNodeCurrIdx22 = LongField()

    LeftHandRingEffector = MessageField(multi=True)

    IKNodeCurrIdx23 = LongField()

    LeftHandPinkyEffector = MessageField(multi=True)

    IKNodeCurrIdx24 = LongField()

    LeftHandExtraFingerEffector = MessageField(multi=True)

    IKNodeCurrIdx25 = LongField()

    RightHandThumbEffector = MessageField(multi=True)

    IKNodeCurrIdx26 = LongField()

    RightHandIndexEffector = MessageField(multi=True)

    IKNodeCurrIdx27 = LongField()

    RightHandMiddleEffector = MessageField(multi=True)

    IKNodeCurrIdx28 = LongField()

    RightHandRingEffector = MessageField(multi=True)

    IKNodeCurrIdx29 = LongField()

    RightHandPinkyEffector = MessageField(multi=True)

    IKNodeCurrIdx30 = LongField()

    RightHandExtraFingerEffector = MessageField(multi=True)

    IKNodeCurrIdx31 = LongField()

    LeftFootThumbEffector = MessageField(multi=True)

    IKNodeCurrIdx32 = LongField()

    LeftFootIndexEffector = MessageField(multi=True)

    IKNodeCurrIdx33 = LongField()

    LeftFootMiddleEffector = MessageField(multi=True)

    IKNodeCurrIdx34 = LongField()

    LeftFootRingEffector = MessageField(multi=True)

    IKNodeCurrIdx35 = LongField()

    LeftFootPinkyEffector = MessageField(multi=True)

    IKNodeCurrIdx36 = LongField()

    LeftFootExtraFingerEffector = MessageField(multi=True)

    IKNodeCurrIdx37 = LongField()

    RightFootThumbEffector = MessageField(multi=True)

    IKNodeCurrIdx38 = LongField()

    RightFootIndexEffector = MessageField(multi=True)

    IKNodeCurrIdx39 = LongField()

    RightFootMiddleEffector = MessageField(multi=True)

    IKNodeCurrIdx40 = LongField()

    RightFootRingEffector = MessageField(multi=True)

    IKNodeCurrIdx41 = LongField()

    RightFootPinkyEffector = MessageField(multi=True)

    IKNodeCurrIdx42 = LongField()

    RightFootExtraFingerEffector = MessageField(multi=True)

    IKNodeCurrIdx43 = LongField()

    rigAlign = BoolField()
    ra = rigAlign

    rigAlignOut = BoolField()
    rao = rigAlignOut
