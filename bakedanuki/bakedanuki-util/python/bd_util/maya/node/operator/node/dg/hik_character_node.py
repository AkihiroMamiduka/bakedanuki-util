# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hik_character_node import (
    HeadJointOrientField,
    HeadMaxRLimitField,
    HeadMinRLimitField,
    HeadRField,
    HeadRotateAxisField,
    HeadSField,
    HeadTField,
    HipsJointOrientField,
    HipsMaxRLimitField,
    HipsMinRLimitField,
    HipsRField,
    HipsRotateAxisField,
    HipsSField,
    HipsTField,
    HipsTranslationJointOrientField,
    HipsTranslationMaxRLimitField,
    HipsTranslationMinRLimitField,
    HipsTranslationRField,
    HipsTranslationRotateAxisField,
    HipsTranslationSField,
    HipsTranslationTField,
    LeafLeftArmRoll1JointOrientField,
    LeafLeftArmRoll1MaxRLimitField,
    LeafLeftArmRoll1MinRLimitField,
    LeafLeftArmRoll1RField,
    LeafLeftArmRoll1RotateAxisField,
    LeafLeftArmRoll1SField,
    LeafLeftArmRoll1TField,
    LeafLeftArmRoll2JointOrientField,
    LeafLeftArmRoll2MaxRLimitField,
    LeafLeftArmRoll2MinRLimitField,
    LeafLeftArmRoll2RField,
    LeafLeftArmRoll2RotateAxisField,
    LeafLeftArmRoll2SField,
    LeafLeftArmRoll2TField,
    LeafLeftArmRoll3JointOrientField,
    LeafLeftArmRoll3MaxRLimitField,
    LeafLeftArmRoll3MinRLimitField,
    LeafLeftArmRoll3RField,
    LeafLeftArmRoll3RotateAxisField,
    LeafLeftArmRoll3SField,
    LeafLeftArmRoll3TField,
    LeafLeftArmRoll4JointOrientField,
    LeafLeftArmRoll4MaxRLimitField,
    LeafLeftArmRoll4MinRLimitField,
    LeafLeftArmRoll4RField,
    LeafLeftArmRoll4RotateAxisField,
    LeafLeftArmRoll4SField,
    LeafLeftArmRoll4TField,
    LeafLeftArmRoll5JointOrientField,
    LeafLeftArmRoll5MaxRLimitField,
    LeafLeftArmRoll5MinRLimitField,
    LeafLeftArmRoll5RField,
    LeafLeftArmRoll5RotateAxisField,
    LeafLeftArmRoll5SField,
    LeafLeftArmRoll5TField,
    LeafLeftForeArmRoll1JointOrientField,
    LeafLeftForeArmRoll1MaxRLimitField,
    LeafLeftForeArmRoll1MinRLimitField,
    LeafLeftForeArmRoll1RField,
    LeafLeftForeArmRoll1RotateAxisField,
    LeafLeftForeArmRoll1SField,
    LeafLeftForeArmRoll1TField,
    LeafLeftForeArmRoll2JointOrientField,
    LeafLeftForeArmRoll2MaxRLimitField,
    LeafLeftForeArmRoll2MinRLimitField,
    LeafLeftForeArmRoll2RField,
    LeafLeftForeArmRoll2RotateAxisField,
    LeafLeftForeArmRoll2SField,
    LeafLeftForeArmRoll2TField,
    LeafLeftForeArmRoll3JointOrientField,
    LeafLeftForeArmRoll3MaxRLimitField,
    LeafLeftForeArmRoll3MinRLimitField,
    LeafLeftForeArmRoll3RField,
    LeafLeftForeArmRoll3RotateAxisField,
    LeafLeftForeArmRoll3SField,
    LeafLeftForeArmRoll3TField,
    LeafLeftForeArmRoll4JointOrientField,
    LeafLeftForeArmRoll4MaxRLimitField,
    LeafLeftForeArmRoll4MinRLimitField,
    LeafLeftForeArmRoll4RField,
    LeafLeftForeArmRoll4RotateAxisField,
    LeafLeftForeArmRoll4SField,
    LeafLeftForeArmRoll4TField,
    LeafLeftForeArmRoll5JointOrientField,
    LeafLeftForeArmRoll5MaxRLimitField,
    LeafLeftForeArmRoll5MinRLimitField,
    LeafLeftForeArmRoll5RField,
    LeafLeftForeArmRoll5RotateAxisField,
    LeafLeftForeArmRoll5SField,
    LeafLeftForeArmRoll5TField,
    LeafLeftLegRoll1JointOrientField,
    LeafLeftLegRoll1MaxRLimitField,
    LeafLeftLegRoll1MinRLimitField,
    LeafLeftLegRoll1RField,
    LeafLeftLegRoll1RotateAxisField,
    LeafLeftLegRoll1SField,
    LeafLeftLegRoll1TField,
    LeafLeftLegRoll2JointOrientField,
    LeafLeftLegRoll2MaxRLimitField,
    LeafLeftLegRoll2MinRLimitField,
    LeafLeftLegRoll2RField,
    LeafLeftLegRoll2RotateAxisField,
    LeafLeftLegRoll2SField,
    LeafLeftLegRoll2TField,
    LeafLeftLegRoll3JointOrientField,
    LeafLeftLegRoll3MaxRLimitField,
    LeafLeftLegRoll3MinRLimitField,
    LeafLeftLegRoll3RField,
    LeafLeftLegRoll3RotateAxisField,
    LeafLeftLegRoll3SField,
    LeafLeftLegRoll3TField,
    LeafLeftLegRoll4JointOrientField,
    LeafLeftLegRoll4MaxRLimitField,
    LeafLeftLegRoll4MinRLimitField,
    LeafLeftLegRoll4RField,
    LeafLeftLegRoll4RotateAxisField,
    LeafLeftLegRoll4SField,
    LeafLeftLegRoll4TField,
    LeafLeftLegRoll5JointOrientField,
    LeafLeftLegRoll5MaxRLimitField,
    LeafLeftLegRoll5MinRLimitField,
    LeafLeftLegRoll5RField,
    LeafLeftLegRoll5RotateAxisField,
    LeafLeftLegRoll5SField,
    LeafLeftLegRoll5TField,
    LeafLeftUpLegRoll1JointOrientField,
    LeafLeftUpLegRoll1MaxRLimitField,
    LeafLeftUpLegRoll1MinRLimitField,
    LeafLeftUpLegRoll1RField,
    LeafLeftUpLegRoll1RotateAxisField,
    LeafLeftUpLegRoll1SField,
    LeafLeftUpLegRoll1TField,
    LeafLeftUpLegRoll2JointOrientField,
    LeafLeftUpLegRoll2MaxRLimitField,
    LeafLeftUpLegRoll2MinRLimitField,
    LeafLeftUpLegRoll2RField,
    LeafLeftUpLegRoll2RotateAxisField,
    LeafLeftUpLegRoll2SField,
    LeafLeftUpLegRoll2TField,
    LeafLeftUpLegRoll3JointOrientField,
    LeafLeftUpLegRoll3MaxRLimitField,
    LeafLeftUpLegRoll3MinRLimitField,
    LeafLeftUpLegRoll3RField,
    LeafLeftUpLegRoll3RotateAxisField,
    LeafLeftUpLegRoll3SField,
    LeafLeftUpLegRoll3TField,
    LeafLeftUpLegRoll4JointOrientField,
    LeafLeftUpLegRoll4MaxRLimitField,
    LeafLeftUpLegRoll4MinRLimitField,
    LeafLeftUpLegRoll4RField,
    LeafLeftUpLegRoll4RotateAxisField,
    LeafLeftUpLegRoll4SField,
    LeafLeftUpLegRoll4TField,
    LeafLeftUpLegRoll5JointOrientField,
    LeafLeftUpLegRoll5MaxRLimitField,
    LeafLeftUpLegRoll5MinRLimitField,
    LeafLeftUpLegRoll5RField,
    LeafLeftUpLegRoll5RotateAxisField,
    LeafLeftUpLegRoll5SField,
    LeafLeftUpLegRoll5TField,
    LeafRightArmRoll1JointOrientField,
    LeafRightArmRoll1MaxRLimitField,
    LeafRightArmRoll1MinRLimitField,
    LeafRightArmRoll1RField,
    LeafRightArmRoll1RotateAxisField,
    LeafRightArmRoll1SField,
    LeafRightArmRoll1TField,
    LeafRightArmRoll2JointOrientField,
    LeafRightArmRoll2MaxRLimitField,
    LeafRightArmRoll2MinRLimitField,
    LeafRightArmRoll2RField,
    LeafRightArmRoll2RotateAxisField,
    LeafRightArmRoll2SField,
    LeafRightArmRoll2TField,
    LeafRightArmRoll3JointOrientField,
    LeafRightArmRoll3MaxRLimitField,
    LeafRightArmRoll3MinRLimitField,
    LeafRightArmRoll3RField,
    LeafRightArmRoll3RotateAxisField,
    LeafRightArmRoll3SField,
    LeafRightArmRoll3TField,
    LeafRightArmRoll4JointOrientField,
    LeafRightArmRoll4MaxRLimitField,
    LeafRightArmRoll4MinRLimitField,
    LeafRightArmRoll4RField,
    LeafRightArmRoll4RotateAxisField,
    LeafRightArmRoll4SField,
    LeafRightArmRoll4TField,
    LeafRightArmRoll5JointOrientField,
    LeafRightArmRoll5MaxRLimitField,
    LeafRightArmRoll5MinRLimitField,
    LeafRightArmRoll5RField,
    LeafRightArmRoll5RotateAxisField,
    LeafRightArmRoll5SField,
    LeafRightArmRoll5TField,
    LeafRightForeArmRoll1JointOrientField,
    LeafRightForeArmRoll1MaxRLimitField,
    LeafRightForeArmRoll1MinRLimitField,
    LeafRightForeArmRoll1RField,
    LeafRightForeArmRoll1RotateAxisField,
    LeafRightForeArmRoll1SField,
    LeafRightForeArmRoll1TField,
    LeafRightForeArmRoll2JointOrientField,
    LeafRightForeArmRoll2MaxRLimitField,
    LeafRightForeArmRoll2MinRLimitField,
    LeafRightForeArmRoll2RField,
    LeafRightForeArmRoll2RotateAxisField,
    LeafRightForeArmRoll2SField,
    LeafRightForeArmRoll2TField,
    LeafRightForeArmRoll3JointOrientField,
    LeafRightForeArmRoll3MaxRLimitField,
    LeafRightForeArmRoll3MinRLimitField,
    LeafRightForeArmRoll3RField,
    LeafRightForeArmRoll3RotateAxisField,
    LeafRightForeArmRoll3SField,
    LeafRightForeArmRoll3TField,
    LeafRightForeArmRoll4JointOrientField,
    LeafRightForeArmRoll4MaxRLimitField,
    LeafRightForeArmRoll4MinRLimitField,
    LeafRightForeArmRoll4RField,
    LeafRightForeArmRoll4RotateAxisField,
    LeafRightForeArmRoll4SField,
    LeafRightForeArmRoll4TField,
    LeafRightForeArmRoll5JointOrientField,
    LeafRightForeArmRoll5MaxRLimitField,
    LeafRightForeArmRoll5MinRLimitField,
    LeafRightForeArmRoll5RField,
    LeafRightForeArmRoll5RotateAxisField,
    LeafRightForeArmRoll5SField,
    LeafRightForeArmRoll5TField,
    LeafRightLegRoll1JointOrientField,
    LeafRightLegRoll1MaxRLimitField,
    LeafRightLegRoll1MinRLimitField,
    LeafRightLegRoll1RField,
    LeafRightLegRoll1RotateAxisField,
    LeafRightLegRoll1SField,
    LeafRightLegRoll1TField,
    LeafRightLegRoll2JointOrientField,
    LeafRightLegRoll2MaxRLimitField,
    LeafRightLegRoll2MinRLimitField,
    LeafRightLegRoll2RField,
    LeafRightLegRoll2RotateAxisField,
    LeafRightLegRoll2SField,
    LeafRightLegRoll2TField,
    LeafRightLegRoll3JointOrientField,
    LeafRightLegRoll3MaxRLimitField,
    LeafRightLegRoll3MinRLimitField,
    LeafRightLegRoll3RField,
    LeafRightLegRoll3RotateAxisField,
    LeafRightLegRoll3SField,
    LeafRightLegRoll3TField,
    LeafRightLegRoll4JointOrientField,
    LeafRightLegRoll4MaxRLimitField,
    LeafRightLegRoll4MinRLimitField,
    LeafRightLegRoll4RField,
    LeafRightLegRoll4RotateAxisField,
    LeafRightLegRoll4SField,
    LeafRightLegRoll4TField,
    LeafRightLegRoll5JointOrientField,
    LeafRightLegRoll5MaxRLimitField,
    LeafRightLegRoll5MinRLimitField,
    LeafRightLegRoll5RField,
    LeafRightLegRoll5RotateAxisField,
    LeafRightLegRoll5SField,
    LeafRightLegRoll5TField,
    LeafRightUpLegRoll1JointOrientField,
    LeafRightUpLegRoll1MaxRLimitField,
    LeafRightUpLegRoll1MinRLimitField,
    LeafRightUpLegRoll1RField,
    LeafRightUpLegRoll1RotateAxisField,
    LeafRightUpLegRoll1SField,
    LeafRightUpLegRoll1TField,
    LeafRightUpLegRoll2JointOrientField,
    LeafRightUpLegRoll2MaxRLimitField,
    LeafRightUpLegRoll2MinRLimitField,
    LeafRightUpLegRoll2RField,
    LeafRightUpLegRoll2RotateAxisField,
    LeafRightUpLegRoll2SField,
    LeafRightUpLegRoll2TField,
    LeafRightUpLegRoll3JointOrientField,
    LeafRightUpLegRoll3MaxRLimitField,
    LeafRightUpLegRoll3MinRLimitField,
    LeafRightUpLegRoll3RField,
    LeafRightUpLegRoll3RotateAxisField,
    LeafRightUpLegRoll3SField,
    LeafRightUpLegRoll3TField,
    LeafRightUpLegRoll4JointOrientField,
    LeafRightUpLegRoll4MaxRLimitField,
    LeafRightUpLegRoll4MinRLimitField,
    LeafRightUpLegRoll4RField,
    LeafRightUpLegRoll4RotateAxisField,
    LeafRightUpLegRoll4SField,
    LeafRightUpLegRoll4TField,
    LeafRightUpLegRoll5JointOrientField,
    LeafRightUpLegRoll5MaxRLimitField,
    LeafRightUpLegRoll5MinRLimitField,
    LeafRightUpLegRoll5RField,
    LeafRightUpLegRoll5RotateAxisField,
    LeafRightUpLegRoll5SField,
    LeafRightUpLegRoll5TField,
    LeftArmJointOrientField,
    LeftArmMaxRLimitField,
    LeftArmMinRLimitField,
    LeftArmRField,
    LeftArmRollJointOrientField,
    LeftArmRollMaxRLimitField,
    LeftArmRollMinRLimitField,
    LeftArmRollRField,
    LeftArmRollRotateAxisField,
    LeftArmRollSField,
    LeftArmRollTField,
    LeftArmRotateAxisField,
    LeftArmSField,
    LeftArmTField,
    LeftFingerBaseJointOrientField,
    LeftFingerBaseMaxRLimitField,
    LeftFingerBaseMinRLimitField,
    LeftFingerBaseRField,
    LeftFingerBaseRotateAxisField,
    LeftFingerBaseSField,
    LeftFingerBaseTField,
    LeftFootExtraFinger1JointOrientField,
    LeftFootExtraFinger1MaxRLimitField,
    LeftFootExtraFinger1MinRLimitField,
    LeftFootExtraFinger1RField,
    LeftFootExtraFinger1RotateAxisField,
    LeftFootExtraFinger1SField,
    LeftFootExtraFinger1TField,
    LeftFootExtraFinger2JointOrientField,
    LeftFootExtraFinger2MaxRLimitField,
    LeftFootExtraFinger2MinRLimitField,
    LeftFootExtraFinger2RField,
    LeftFootExtraFinger2RotateAxisField,
    LeftFootExtraFinger2SField,
    LeftFootExtraFinger2TField,
    LeftFootExtraFinger3JointOrientField,
    LeftFootExtraFinger3MaxRLimitField,
    LeftFootExtraFinger3MinRLimitField,
    LeftFootExtraFinger3RField,
    LeftFootExtraFinger3RotateAxisField,
    LeftFootExtraFinger3SField,
    LeftFootExtraFinger3TField,
    LeftFootExtraFinger4JointOrientField,
    LeftFootExtraFinger4MaxRLimitField,
    LeftFootExtraFinger4MinRLimitField,
    LeftFootExtraFinger4RField,
    LeftFootExtraFinger4RotateAxisField,
    LeftFootExtraFinger4SField,
    LeftFootExtraFinger4TField,
    LeftFootIndex1JointOrientField,
    LeftFootIndex1MaxRLimitField,
    LeftFootIndex1MinRLimitField,
    LeftFootIndex1RField,
    LeftFootIndex1RotateAxisField,
    LeftFootIndex1SField,
    LeftFootIndex1TField,
    LeftFootIndex2JointOrientField,
    LeftFootIndex2MaxRLimitField,
    LeftFootIndex2MinRLimitField,
    LeftFootIndex2RField,
    LeftFootIndex2RotateAxisField,
    LeftFootIndex2SField,
    LeftFootIndex2TField,
    LeftFootIndex3JointOrientField,
    LeftFootIndex3MaxRLimitField,
    LeftFootIndex3MinRLimitField,
    LeftFootIndex3RField,
    LeftFootIndex3RotateAxisField,
    LeftFootIndex3SField,
    LeftFootIndex3TField,
    LeftFootIndex4JointOrientField,
    LeftFootIndex4MaxRLimitField,
    LeftFootIndex4MinRLimitField,
    LeftFootIndex4RField,
    LeftFootIndex4RotateAxisField,
    LeftFootIndex4SField,
    LeftFootIndex4TField,
    LeftFootJointOrientField,
    LeftFootMaxRLimitField,
    LeftFootMiddle1JointOrientField,
    LeftFootMiddle1MaxRLimitField,
    LeftFootMiddle1MinRLimitField,
    LeftFootMiddle1RField,
    LeftFootMiddle1RotateAxisField,
    LeftFootMiddle1SField,
    LeftFootMiddle1TField,
    LeftFootMiddle2JointOrientField,
    LeftFootMiddle2MaxRLimitField,
    LeftFootMiddle2MinRLimitField,
    LeftFootMiddle2RField,
    LeftFootMiddle2RotateAxisField,
    LeftFootMiddle2SField,
    LeftFootMiddle2TField,
    LeftFootMiddle3JointOrientField,
    LeftFootMiddle3MaxRLimitField,
    LeftFootMiddle3MinRLimitField,
    LeftFootMiddle3RField,
    LeftFootMiddle3RotateAxisField,
    LeftFootMiddle3SField,
    LeftFootMiddle3TField,
    LeftFootMiddle4JointOrientField,
    LeftFootMiddle4MaxRLimitField,
    LeftFootMiddle4MinRLimitField,
    LeftFootMiddle4RField,
    LeftFootMiddle4RotateAxisField,
    LeftFootMiddle4SField,
    LeftFootMiddle4TField,
    LeftFootMinRLimitField,
    LeftFootPinky1JointOrientField,
    LeftFootPinky1MaxRLimitField,
    LeftFootPinky1MinRLimitField,
    LeftFootPinky1RField,
    LeftFootPinky1RotateAxisField,
    LeftFootPinky1SField,
    LeftFootPinky1TField,
    LeftFootPinky2JointOrientField,
    LeftFootPinky2MaxRLimitField,
    LeftFootPinky2MinRLimitField,
    LeftFootPinky2RField,
    LeftFootPinky2RotateAxisField,
    LeftFootPinky2SField,
    LeftFootPinky2TField,
    LeftFootPinky3JointOrientField,
    LeftFootPinky3MaxRLimitField,
    LeftFootPinky3MinRLimitField,
    LeftFootPinky3RField,
    LeftFootPinky3RotateAxisField,
    LeftFootPinky3SField,
    LeftFootPinky3TField,
    LeftFootPinky4JointOrientField,
    LeftFootPinky4MaxRLimitField,
    LeftFootPinky4MinRLimitField,
    LeftFootPinky4RField,
    LeftFootPinky4RotateAxisField,
    LeftFootPinky4SField,
    LeftFootPinky4TField,
    LeftFootRField,
    LeftFootRing1JointOrientField,
    LeftFootRing1MaxRLimitField,
    LeftFootRing1MinRLimitField,
    LeftFootRing1RField,
    LeftFootRing1RotateAxisField,
    LeftFootRing1SField,
    LeftFootRing1TField,
    LeftFootRing2JointOrientField,
    LeftFootRing2MaxRLimitField,
    LeftFootRing2MinRLimitField,
    LeftFootRing2RField,
    LeftFootRing2RotateAxisField,
    LeftFootRing2SField,
    LeftFootRing2TField,
    LeftFootRing3JointOrientField,
    LeftFootRing3MaxRLimitField,
    LeftFootRing3MinRLimitField,
    LeftFootRing3RField,
    LeftFootRing3RotateAxisField,
    LeftFootRing3SField,
    LeftFootRing3TField,
    LeftFootRing4JointOrientField,
    LeftFootRing4MaxRLimitField,
    LeftFootRing4MinRLimitField,
    LeftFootRing4RField,
    LeftFootRing4RotateAxisField,
    LeftFootRing4SField,
    LeftFootRing4TField,
    LeftFootRotateAxisField,
    LeftFootSField,
    LeftFootTField,
    LeftFootThumb1JointOrientField,
    LeftFootThumb1MaxRLimitField,
    LeftFootThumb1MinRLimitField,
    LeftFootThumb1RField,
    LeftFootThumb1RotateAxisField,
    LeftFootThumb1SField,
    LeftFootThumb1TField,
    LeftFootThumb2JointOrientField,
    LeftFootThumb2MaxRLimitField,
    LeftFootThumb2MinRLimitField,
    LeftFootThumb2RField,
    LeftFootThumb2RotateAxisField,
    LeftFootThumb2SField,
    LeftFootThumb2TField,
    LeftFootThumb3JointOrientField,
    LeftFootThumb3MaxRLimitField,
    LeftFootThumb3MinRLimitField,
    LeftFootThumb3RField,
    LeftFootThumb3RotateAxisField,
    LeftFootThumb3SField,
    LeftFootThumb3TField,
    LeftFootThumb4JointOrientField,
    LeftFootThumb4MaxRLimitField,
    LeftFootThumb4MinRLimitField,
    LeftFootThumb4RField,
    LeftFootThumb4RotateAxisField,
    LeftFootThumb4SField,
    LeftFootThumb4TField,
    LeftForeArmJointOrientField,
    LeftForeArmMaxRLimitField,
    LeftForeArmMinRLimitField,
    LeftForeArmRField,
    LeftForeArmRollJointOrientField,
    LeftForeArmRollMaxRLimitField,
    LeftForeArmRollMinRLimitField,
    LeftForeArmRollRField,
    LeftForeArmRollRotateAxisField,
    LeftForeArmRollSField,
    LeftForeArmRollTField,
    LeftForeArmRotateAxisField,
    LeftForeArmSField,
    LeftForeArmTField,
    LeftHandExtraFinger1JointOrientField,
    LeftHandExtraFinger1MaxRLimitField,
    LeftHandExtraFinger1MinRLimitField,
    LeftHandExtraFinger1RField,
    LeftHandExtraFinger1RotateAxisField,
    LeftHandExtraFinger1SField,
    LeftHandExtraFinger1TField,
    LeftHandExtraFinger2JointOrientField,
    LeftHandExtraFinger2MaxRLimitField,
    LeftHandExtraFinger2MinRLimitField,
    LeftHandExtraFinger2RField,
    LeftHandExtraFinger2RotateAxisField,
    LeftHandExtraFinger2SField,
    LeftHandExtraFinger2TField,
    LeftHandExtraFinger3JointOrientField,
    LeftHandExtraFinger3MaxRLimitField,
    LeftHandExtraFinger3MinRLimitField,
    LeftHandExtraFinger3RField,
    LeftHandExtraFinger3RotateAxisField,
    LeftHandExtraFinger3SField,
    LeftHandExtraFinger3TField,
    LeftHandExtraFinger4JointOrientField,
    LeftHandExtraFinger4MaxRLimitField,
    LeftHandExtraFinger4MinRLimitField,
    LeftHandExtraFinger4RField,
    LeftHandExtraFinger4RotateAxisField,
    LeftHandExtraFinger4SField,
    LeftHandExtraFinger4TField,
    LeftHandIndex1JointOrientField,
    LeftHandIndex1MaxRLimitField,
    LeftHandIndex1MinRLimitField,
    LeftHandIndex1RField,
    LeftHandIndex1RotateAxisField,
    LeftHandIndex1SField,
    LeftHandIndex1TField,
    LeftHandIndex2JointOrientField,
    LeftHandIndex2MaxRLimitField,
    LeftHandIndex2MinRLimitField,
    LeftHandIndex2RField,
    LeftHandIndex2RotateAxisField,
    LeftHandIndex2SField,
    LeftHandIndex2TField,
    LeftHandIndex3JointOrientField,
    LeftHandIndex3MaxRLimitField,
    LeftHandIndex3MinRLimitField,
    LeftHandIndex3RField,
    LeftHandIndex3RotateAxisField,
    LeftHandIndex3SField,
    LeftHandIndex3TField,
    LeftHandIndex4JointOrientField,
    LeftHandIndex4MaxRLimitField,
    LeftHandIndex4MinRLimitField,
    LeftHandIndex4RField,
    LeftHandIndex4RotateAxisField,
    LeftHandIndex4SField,
    LeftHandIndex4TField,
    LeftHandJointOrientField,
    LeftHandMaxRLimitField,
    LeftHandMiddle1JointOrientField,
    LeftHandMiddle1MaxRLimitField,
    LeftHandMiddle1MinRLimitField,
    LeftHandMiddle1RField,
    LeftHandMiddle1RotateAxisField,
    LeftHandMiddle1SField,
    LeftHandMiddle1TField,
    LeftHandMiddle2JointOrientField,
    LeftHandMiddle2MaxRLimitField,
    LeftHandMiddle2MinRLimitField,
    LeftHandMiddle2RField,
    LeftHandMiddle2RotateAxisField,
    LeftHandMiddle2SField,
    LeftHandMiddle2TField,
    LeftHandMiddle3JointOrientField,
    LeftHandMiddle3MaxRLimitField,
    LeftHandMiddle3MinRLimitField,
    LeftHandMiddle3RField,
    LeftHandMiddle3RotateAxisField,
    LeftHandMiddle3SField,
    LeftHandMiddle3TField,
    LeftHandMiddle4JointOrientField,
    LeftHandMiddle4MaxRLimitField,
    LeftHandMiddle4MinRLimitField,
    LeftHandMiddle4RField,
    LeftHandMiddle4RotateAxisField,
    LeftHandMiddle4SField,
    LeftHandMiddle4TField,
    LeftHandMinRLimitField,
    LeftHandPinky1JointOrientField,
    LeftHandPinky1MaxRLimitField,
    LeftHandPinky1MinRLimitField,
    LeftHandPinky1RField,
    LeftHandPinky1RotateAxisField,
    LeftHandPinky1SField,
    LeftHandPinky1TField,
    LeftHandPinky2JointOrientField,
    LeftHandPinky2MaxRLimitField,
    LeftHandPinky2MinRLimitField,
    LeftHandPinky2RField,
    LeftHandPinky2RotateAxisField,
    LeftHandPinky2SField,
    LeftHandPinky2TField,
    LeftHandPinky3JointOrientField,
    LeftHandPinky3MaxRLimitField,
    LeftHandPinky3MinRLimitField,
    LeftHandPinky3RField,
    LeftHandPinky3RotateAxisField,
    LeftHandPinky3SField,
    LeftHandPinky3TField,
    LeftHandPinky4JointOrientField,
    LeftHandPinky4MaxRLimitField,
    LeftHandPinky4MinRLimitField,
    LeftHandPinky4RField,
    LeftHandPinky4RotateAxisField,
    LeftHandPinky4SField,
    LeftHandPinky4TField,
    LeftHandRField,
    LeftHandRing1JointOrientField,
    LeftHandRing1MaxRLimitField,
    LeftHandRing1MinRLimitField,
    LeftHandRing1RField,
    LeftHandRing1RotateAxisField,
    LeftHandRing1SField,
    LeftHandRing1TField,
    LeftHandRing2JointOrientField,
    LeftHandRing2MaxRLimitField,
    LeftHandRing2MinRLimitField,
    LeftHandRing2RField,
    LeftHandRing2RotateAxisField,
    LeftHandRing2SField,
    LeftHandRing2TField,
    LeftHandRing3JointOrientField,
    LeftHandRing3MaxRLimitField,
    LeftHandRing3MinRLimitField,
    LeftHandRing3RField,
    LeftHandRing3RotateAxisField,
    LeftHandRing3SField,
    LeftHandRing3TField,
    LeftHandRing4JointOrientField,
    LeftHandRing4MaxRLimitField,
    LeftHandRing4MinRLimitField,
    LeftHandRing4RField,
    LeftHandRing4RotateAxisField,
    LeftHandRing4SField,
    LeftHandRing4TField,
    LeftHandRotateAxisField,
    LeftHandSField,
    LeftHandTField,
    LeftHandThumb1JointOrientField,
    LeftHandThumb1MaxRLimitField,
    LeftHandThumb1MinRLimitField,
    LeftHandThumb1RField,
    LeftHandThumb1RotateAxisField,
    LeftHandThumb1SField,
    LeftHandThumb1TField,
    LeftHandThumb2JointOrientField,
    LeftHandThumb2MaxRLimitField,
    LeftHandThumb2MinRLimitField,
    LeftHandThumb2RField,
    LeftHandThumb2RotateAxisField,
    LeftHandThumb2SField,
    LeftHandThumb2TField,
    LeftHandThumb3JointOrientField,
    LeftHandThumb3MaxRLimitField,
    LeftHandThumb3MinRLimitField,
    LeftHandThumb3RField,
    LeftHandThumb3RotateAxisField,
    LeftHandThumb3SField,
    LeftHandThumb3TField,
    LeftHandThumb4JointOrientField,
    LeftHandThumb4MaxRLimitField,
    LeftHandThumb4MinRLimitField,
    LeftHandThumb4RField,
    LeftHandThumb4RotateAxisField,
    LeftHandThumb4SField,
    LeftHandThumb4TField,
    LeftInFootExtraFingerJointOrientField,
    LeftInFootExtraFingerMaxRLimitField,
    LeftInFootExtraFingerMinRLimitField,
    LeftInFootExtraFingerRField,
    LeftInFootExtraFingerRotateAxisField,
    LeftInFootExtraFingerSField,
    LeftInFootExtraFingerTField,
    LeftInFootIndexJointOrientField,
    LeftInFootIndexMaxRLimitField,
    LeftInFootIndexMinRLimitField,
    LeftInFootIndexRField,
    LeftInFootIndexRotateAxisField,
    LeftInFootIndexSField,
    LeftInFootIndexTField,
    LeftInFootMiddleJointOrientField,
    LeftInFootMiddleMaxRLimitField,
    LeftInFootMiddleMinRLimitField,
    LeftInFootMiddleRField,
    LeftInFootMiddleRotateAxisField,
    LeftInFootMiddleSField,
    LeftInFootMiddleTField,
    LeftInFootPinkyJointOrientField,
    LeftInFootPinkyMaxRLimitField,
    LeftInFootPinkyMinRLimitField,
    LeftInFootPinkyRField,
    LeftInFootPinkyRotateAxisField,
    LeftInFootPinkySField,
    LeftInFootPinkyTField,
    LeftInFootRingJointOrientField,
    LeftInFootRingMaxRLimitField,
    LeftInFootRingMinRLimitField,
    LeftInFootRingRField,
    LeftInFootRingRotateAxisField,
    LeftInFootRingSField,
    LeftInFootRingTField,
    LeftInFootThumbJointOrientField,
    LeftInFootThumbMaxRLimitField,
    LeftInFootThumbMinRLimitField,
    LeftInFootThumbRField,
    LeftInFootThumbRotateAxisField,
    LeftInFootThumbSField,
    LeftInFootThumbTField,
    LeftInHandExtraFingerJointOrientField,
    LeftInHandExtraFingerMaxRLimitField,
    LeftInHandExtraFingerMinRLimitField,
    LeftInHandExtraFingerRField,
    LeftInHandExtraFingerRotateAxisField,
    LeftInHandExtraFingerSField,
    LeftInHandExtraFingerTField,
    LeftInHandIndexJointOrientField,
    LeftInHandIndexMaxRLimitField,
    LeftInHandIndexMinRLimitField,
    LeftInHandIndexRField,
    LeftInHandIndexRotateAxisField,
    LeftInHandIndexSField,
    LeftInHandIndexTField,
    LeftInHandMiddleJointOrientField,
    LeftInHandMiddleMaxRLimitField,
    LeftInHandMiddleMinRLimitField,
    LeftInHandMiddleRField,
    LeftInHandMiddleRotateAxisField,
    LeftInHandMiddleSField,
    LeftInHandMiddleTField,
    LeftInHandPinkyJointOrientField,
    LeftInHandPinkyMaxRLimitField,
    LeftInHandPinkyMinRLimitField,
    LeftInHandPinkyRField,
    LeftInHandPinkyRotateAxisField,
    LeftInHandPinkySField,
    LeftInHandPinkyTField,
    LeftInHandRingJointOrientField,
    LeftInHandRingMaxRLimitField,
    LeftInHandRingMinRLimitField,
    LeftInHandRingRField,
    LeftInHandRingRotateAxisField,
    LeftInHandRingSField,
    LeftInHandRingTField,
    LeftInHandThumbJointOrientField,
    LeftInHandThumbMaxRLimitField,
    LeftInHandThumbMinRLimitField,
    LeftInHandThumbRField,
    LeftInHandThumbRotateAxisField,
    LeftInHandThumbSField,
    LeftInHandThumbTField,
    LeftLegJointOrientField,
    LeftLegMaxRLimitField,
    LeftLegMinRLimitField,
    LeftLegRField,
    LeftLegRollJointOrientField,
    LeftLegRollMaxRLimitField,
    LeftLegRollMinRLimitField,
    LeftLegRollRField,
    LeftLegRollRotateAxisField,
    LeftLegRollSField,
    LeftLegRollTField,
    LeftLegRotateAxisField,
    LeftLegSField,
    LeftLegTField,
    LeftShoulderExtraJointOrientField,
    LeftShoulderExtraMaxRLimitField,
    LeftShoulderExtraMinRLimitField,
    LeftShoulderExtraRField,
    LeftShoulderExtraRotateAxisField,
    LeftShoulderExtraSField,
    LeftShoulderExtraTField,
    LeftShoulderJointOrientField,
    LeftShoulderMaxRLimitField,
    LeftShoulderMinRLimitField,
    LeftShoulderRField,
    LeftShoulderRotateAxisField,
    LeftShoulderSField,
    LeftShoulderTField,
    LeftToeBaseJointOrientField,
    LeftToeBaseMaxRLimitField,
    LeftToeBaseMinRLimitField,
    LeftToeBaseRField,
    LeftToeBaseRotateAxisField,
    LeftToeBaseSField,
    LeftToeBaseTField,
    LeftUpLegJointOrientField,
    LeftUpLegMaxRLimitField,
    LeftUpLegMinRLimitField,
    LeftUpLegRField,
    LeftUpLegRollJointOrientField,
    LeftUpLegRollMaxRLimitField,
    LeftUpLegRollMinRLimitField,
    LeftUpLegRollRField,
    LeftUpLegRollRotateAxisField,
    LeftUpLegRollSField,
    LeftUpLegRollTField,
    LeftUpLegRotateAxisField,
    LeftUpLegSField,
    LeftUpLegTField,
    Neck1JointOrientField,
    Neck1MaxRLimitField,
    Neck1MinRLimitField,
    Neck1RField,
    Neck1RotateAxisField,
    Neck1SField,
    Neck1TField,
    Neck2JointOrientField,
    Neck2MaxRLimitField,
    Neck2MinRLimitField,
    Neck2RField,
    Neck2RotateAxisField,
    Neck2SField,
    Neck2TField,
    Neck3JointOrientField,
    Neck3MaxRLimitField,
    Neck3MinRLimitField,
    Neck3RField,
    Neck3RotateAxisField,
    Neck3SField,
    Neck3TField,
    Neck4JointOrientField,
    Neck4MaxRLimitField,
    Neck4MinRLimitField,
    Neck4RField,
    Neck4RotateAxisField,
    Neck4SField,
    Neck4TField,
    Neck5JointOrientField,
    Neck5MaxRLimitField,
    Neck5MinRLimitField,
    Neck5RField,
    Neck5RotateAxisField,
    Neck5SField,
    Neck5TField,
    Neck6JointOrientField,
    Neck6MaxRLimitField,
    Neck6MinRLimitField,
    Neck6RField,
    Neck6RotateAxisField,
    Neck6SField,
    Neck6TField,
    Neck7JointOrientField,
    Neck7MaxRLimitField,
    Neck7MinRLimitField,
    Neck7RField,
    Neck7RotateAxisField,
    Neck7SField,
    Neck7TField,
    Neck8JointOrientField,
    Neck8MaxRLimitField,
    Neck8MinRLimitField,
    Neck8RField,
    Neck8RotateAxisField,
    Neck8SField,
    Neck8TField,
    Neck9JointOrientField,
    Neck9MaxRLimitField,
    Neck9MinRLimitField,
    Neck9RField,
    Neck9RotateAxisField,
    Neck9SField,
    Neck9TField,
    NeckJointOrientField,
    NeckMaxRLimitField,
    NeckMinRLimitField,
    NeckRField,
    NeckRotateAxisField,
    NeckSField,
    NeckTField,
    ReferenceJointOrientField,
    ReferenceMaxRLimitField,
    ReferenceMinRLimitField,
    ReferenceRField,
    ReferenceRotateAxisField,
    ReferenceSField,
    ReferenceTField,
    RightArmJointOrientField,
    RightArmMaxRLimitField,
    RightArmMinRLimitField,
    RightArmRField,
    RightArmRollJointOrientField,
    RightArmRollMaxRLimitField,
    RightArmRollMinRLimitField,
    RightArmRollRField,
    RightArmRollRotateAxisField,
    RightArmRollSField,
    RightArmRollTField,
    RightArmRotateAxisField,
    RightArmSField,
    RightArmTField,
    RightFingerBaseJointOrientField,
    RightFingerBaseMaxRLimitField,
    RightFingerBaseMinRLimitField,
    RightFingerBaseRField,
    RightFingerBaseRotateAxisField,
    RightFingerBaseSField,
    RightFingerBaseTField,
    RightFootExtraFinger1JointOrientField,
    RightFootExtraFinger1MaxRLimitField,
    RightFootExtraFinger1MinRLimitField,
    RightFootExtraFinger1RField,
    RightFootExtraFinger1RotateAxisField,
    RightFootExtraFinger1SField,
    RightFootExtraFinger1TField,
    RightFootExtraFinger2JointOrientField,
    RightFootExtraFinger2MaxRLimitField,
    RightFootExtraFinger2MinRLimitField,
    RightFootExtraFinger2RField,
    RightFootExtraFinger2RotateAxisField,
    RightFootExtraFinger2SField,
    RightFootExtraFinger2TField,
    RightFootExtraFinger3JointOrientField,
    RightFootExtraFinger3MaxRLimitField,
    RightFootExtraFinger3MinRLimitField,
    RightFootExtraFinger3RField,
    RightFootExtraFinger3RotateAxisField,
    RightFootExtraFinger3SField,
    RightFootExtraFinger3TField,
    RightFootExtraFinger4JointOrientField,
    RightFootExtraFinger4MaxRLimitField,
    RightFootExtraFinger4MinRLimitField,
    RightFootExtraFinger4RField,
    RightFootExtraFinger4RotateAxisField,
    RightFootExtraFinger4SField,
    RightFootExtraFinger4TField,
    RightFootIndex1JointOrientField,
    RightFootIndex1MaxRLimitField,
    RightFootIndex1MinRLimitField,
    RightFootIndex1RField,
    RightFootIndex1RotateAxisField,
    RightFootIndex1SField,
    RightFootIndex1TField,
    RightFootIndex2JointOrientField,
    RightFootIndex2MaxRLimitField,
    RightFootIndex2MinRLimitField,
    RightFootIndex2RField,
    RightFootIndex2RotateAxisField,
    RightFootIndex2SField,
    RightFootIndex2TField,
    RightFootIndex3JointOrientField,
    RightFootIndex3MaxRLimitField,
    RightFootIndex3MinRLimitField,
    RightFootIndex3RField,
    RightFootIndex3RotateAxisField,
    RightFootIndex3SField,
    RightFootIndex3TField,
    RightFootIndex4JointOrientField,
    RightFootIndex4MaxRLimitField,
    RightFootIndex4MinRLimitField,
    RightFootIndex4RField,
    RightFootIndex4RotateAxisField,
    RightFootIndex4SField,
    RightFootIndex4TField,
    RightFootJointOrientField,
    RightFootMaxRLimitField,
    RightFootMiddle1JointOrientField,
    RightFootMiddle1MaxRLimitField,
    RightFootMiddle1MinRLimitField,
    RightFootMiddle1RField,
    RightFootMiddle1RotateAxisField,
    RightFootMiddle1SField,
    RightFootMiddle1TField,
    RightFootMiddle2JointOrientField,
    RightFootMiddle2MaxRLimitField,
    RightFootMiddle2MinRLimitField,
    RightFootMiddle2RField,
    RightFootMiddle2RotateAxisField,
    RightFootMiddle2SField,
    RightFootMiddle2TField,
    RightFootMiddle3JointOrientField,
    RightFootMiddle3MaxRLimitField,
    RightFootMiddle3MinRLimitField,
    RightFootMiddle3RField,
    RightFootMiddle3RotateAxisField,
    RightFootMiddle3SField,
    RightFootMiddle3TField,
    RightFootMiddle4JointOrientField,
    RightFootMiddle4MaxRLimitField,
    RightFootMiddle4MinRLimitField,
    RightFootMiddle4RField,
    RightFootMiddle4RotateAxisField,
    RightFootMiddle4SField,
    RightFootMiddle4TField,
    RightFootMinRLimitField,
    RightFootPinky1JointOrientField,
    RightFootPinky1MaxRLimitField,
    RightFootPinky1MinRLimitField,
    RightFootPinky1RField,
    RightFootPinky1RotateAxisField,
    RightFootPinky1SField,
    RightFootPinky1TField,
    RightFootPinky2JointOrientField,
    RightFootPinky2MaxRLimitField,
    RightFootPinky2MinRLimitField,
    RightFootPinky2RField,
    RightFootPinky2RotateAxisField,
    RightFootPinky2SField,
    RightFootPinky2TField,
    RightFootPinky3JointOrientField,
    RightFootPinky3MaxRLimitField,
    RightFootPinky3MinRLimitField,
    RightFootPinky3RField,
    RightFootPinky3RotateAxisField,
    RightFootPinky3SField,
    RightFootPinky3TField,
    RightFootPinky4JointOrientField,
    RightFootPinky4MaxRLimitField,
    RightFootPinky4MinRLimitField,
    RightFootPinky4RField,
    RightFootPinky4RotateAxisField,
    RightFootPinky4SField,
    RightFootPinky4TField,
    RightFootRField,
    RightFootRing1JointOrientField,
    RightFootRing1MaxRLimitField,
    RightFootRing1MinRLimitField,
    RightFootRing1RField,
    RightFootRing1RotateAxisField,
    RightFootRing1SField,
    RightFootRing1TField,
    RightFootRing2JointOrientField,
    RightFootRing2MaxRLimitField,
    RightFootRing2MinRLimitField,
    RightFootRing2RField,
    RightFootRing2RotateAxisField,
    RightFootRing2SField,
    RightFootRing2TField,
    RightFootRing3JointOrientField,
    RightFootRing3MaxRLimitField,
    RightFootRing3MinRLimitField,
    RightFootRing3RField,
    RightFootRing3RotateAxisField,
    RightFootRing3SField,
    RightFootRing3TField,
    RightFootRing4JointOrientField,
    RightFootRing4MaxRLimitField,
    RightFootRing4MinRLimitField,
    RightFootRing4RField,
    RightFootRing4RotateAxisField,
    RightFootRing4SField,
    RightFootRing4TField,
    RightFootRotateAxisField,
    RightFootSField,
    RightFootTField,
    RightFootThumb1JointOrientField,
    RightFootThumb1MaxRLimitField,
    RightFootThumb1MinRLimitField,
    RightFootThumb1RField,
    RightFootThumb1RotateAxisField,
    RightFootThumb1SField,
    RightFootThumb1TField,
    RightFootThumb2JointOrientField,
    RightFootThumb2MaxRLimitField,
    RightFootThumb2MinRLimitField,
    RightFootThumb2RField,
    RightFootThumb2RotateAxisField,
    RightFootThumb2SField,
    RightFootThumb2TField,
    RightFootThumb3JointOrientField,
    RightFootThumb3MaxRLimitField,
    RightFootThumb3MinRLimitField,
    RightFootThumb3RField,
    RightFootThumb3RotateAxisField,
    RightFootThumb3SField,
    RightFootThumb3TField,
    RightFootThumb4JointOrientField,
    RightFootThumb4MaxRLimitField,
    RightFootThumb4MinRLimitField,
    RightFootThumb4RField,
    RightFootThumb4RotateAxisField,
    RightFootThumb4SField,
    RightFootThumb4TField,
    RightForeArmJointOrientField,
    RightForeArmMaxRLimitField,
    RightForeArmMinRLimitField,
    RightForeArmRField,
    RightForeArmRollJointOrientField,
    RightForeArmRollMaxRLimitField,
    RightForeArmRollMinRLimitField,
    RightForeArmRollRField,
    RightForeArmRollRotateAxisField,
    RightForeArmRollSField,
    RightForeArmRollTField,
    RightForeArmRotateAxisField,
    RightForeArmSField,
    RightForeArmTField,
    RightHandExtraFinger1JointOrientField,
    RightHandExtraFinger1MaxRLimitField,
    RightHandExtraFinger1MinRLimitField,
    RightHandExtraFinger1RField,
    RightHandExtraFinger1RotateAxisField,
    RightHandExtraFinger1SField,
    RightHandExtraFinger1TField,
    RightHandExtraFinger2JointOrientField,
    RightHandExtraFinger2MaxRLimitField,
    RightHandExtraFinger2MinRLimitField,
    RightHandExtraFinger2RField,
    RightHandExtraFinger2RotateAxisField,
    RightHandExtraFinger2SField,
    RightHandExtraFinger2TField,
    RightHandExtraFinger3JointOrientField,
    RightHandExtraFinger3MaxRLimitField,
    RightHandExtraFinger3MinRLimitField,
    RightHandExtraFinger3RField,
    RightHandExtraFinger3RotateAxisField,
    RightHandExtraFinger3SField,
    RightHandExtraFinger3TField,
    RightHandExtraFinger4JointOrientField,
    RightHandExtraFinger4MaxRLimitField,
    RightHandExtraFinger4MinRLimitField,
    RightHandExtraFinger4RField,
    RightHandExtraFinger4RotateAxisField,
    RightHandExtraFinger4SField,
    RightHandExtraFinger4TField,
    RightHandIndex1JointOrientField,
    RightHandIndex1MaxRLimitField,
    RightHandIndex1MinRLimitField,
    RightHandIndex1RField,
    RightHandIndex1RotateAxisField,
    RightHandIndex1SField,
    RightHandIndex1TField,
    RightHandIndex2JointOrientField,
    RightHandIndex2MaxRLimitField,
    RightHandIndex2MinRLimitField,
    RightHandIndex2RField,
    RightHandIndex2RotateAxisField,
    RightHandIndex2SField,
    RightHandIndex2TField,
    RightHandIndex3JointOrientField,
    RightHandIndex3MaxRLimitField,
    RightHandIndex3MinRLimitField,
    RightHandIndex3RField,
    RightHandIndex3RotateAxisField,
    RightHandIndex3SField,
    RightHandIndex3TField,
    RightHandIndex4JointOrientField,
    RightHandIndex4MaxRLimitField,
    RightHandIndex4MinRLimitField,
    RightHandIndex4RField,
    RightHandIndex4RotateAxisField,
    RightHandIndex4SField,
    RightHandIndex4TField,
    RightHandJointOrientField,
    RightHandMaxRLimitField,
    RightHandMiddle1JointOrientField,
    RightHandMiddle1MaxRLimitField,
    RightHandMiddle1MinRLimitField,
    RightHandMiddle1RField,
    RightHandMiddle1RotateAxisField,
    RightHandMiddle1SField,
    RightHandMiddle1TField,
    RightHandMiddle2JointOrientField,
    RightHandMiddle2MaxRLimitField,
    RightHandMiddle2MinRLimitField,
    RightHandMiddle2RField,
    RightHandMiddle2RotateAxisField,
    RightHandMiddle2SField,
    RightHandMiddle2TField,
    RightHandMiddle3JointOrientField,
    RightHandMiddle3MaxRLimitField,
    RightHandMiddle3MinRLimitField,
    RightHandMiddle3RField,
    RightHandMiddle3RotateAxisField,
    RightHandMiddle3SField,
    RightHandMiddle3TField,
    RightHandMiddle4JointOrientField,
    RightHandMiddle4MaxRLimitField,
    RightHandMiddle4MinRLimitField,
    RightHandMiddle4RField,
    RightHandMiddle4RotateAxisField,
    RightHandMiddle4SField,
    RightHandMiddle4TField,
    RightHandMinRLimitField,
    RightHandPinky1JointOrientField,
    RightHandPinky1MaxRLimitField,
    RightHandPinky1MinRLimitField,
    RightHandPinky1RField,
    RightHandPinky1RotateAxisField,
    RightHandPinky1SField,
    RightHandPinky1TField,
    RightHandPinky2JointOrientField,
    RightHandPinky2MaxRLimitField,
    RightHandPinky2MinRLimitField,
    RightHandPinky2RField,
    RightHandPinky2RotateAxisField,
    RightHandPinky2SField,
    RightHandPinky2TField,
    RightHandPinky3JointOrientField,
    RightHandPinky3MaxRLimitField,
    RightHandPinky3MinRLimitField,
    RightHandPinky3RField,
    RightHandPinky3RotateAxisField,
    RightHandPinky3SField,
    RightHandPinky3TField,
    RightHandPinky4JointOrientField,
    RightHandPinky4MaxRLimitField,
    RightHandPinky4MinRLimitField,
    RightHandPinky4RField,
    RightHandPinky4RotateAxisField,
    RightHandPinky4SField,
    RightHandPinky4TField,
    RightHandRField,
    RightHandRing1JointOrientField,
    RightHandRing1MaxRLimitField,
    RightHandRing1MinRLimitField,
    RightHandRing1RField,
    RightHandRing1RotateAxisField,
    RightHandRing1SField,
    RightHandRing1TField,
    RightHandRing2JointOrientField,
    RightHandRing2MaxRLimitField,
    RightHandRing2MinRLimitField,
    RightHandRing2RField,
    RightHandRing2RotateAxisField,
    RightHandRing2SField,
    RightHandRing2TField,
    RightHandRing3JointOrientField,
    RightHandRing3MaxRLimitField,
    RightHandRing3MinRLimitField,
    RightHandRing3RField,
    RightHandRing3RotateAxisField,
    RightHandRing3SField,
    RightHandRing3TField,
    RightHandRing4JointOrientField,
    RightHandRing4MaxRLimitField,
    RightHandRing4MinRLimitField,
    RightHandRing4RField,
    RightHandRing4RotateAxisField,
    RightHandRing4SField,
    RightHandRing4TField,
    RightHandRotateAxisField,
    RightHandSField,
    RightHandTField,
    RightHandThumb1JointOrientField,
    RightHandThumb1MaxRLimitField,
    RightHandThumb1MinRLimitField,
    RightHandThumb1RField,
    RightHandThumb1RotateAxisField,
    RightHandThumb1SField,
    RightHandThumb1TField,
    RightHandThumb2JointOrientField,
    RightHandThumb2MaxRLimitField,
    RightHandThumb2MinRLimitField,
    RightHandThumb2RField,
    RightHandThumb2RotateAxisField,
    RightHandThumb2SField,
    RightHandThumb2TField,
    RightHandThumb3JointOrientField,
    RightHandThumb3MaxRLimitField,
    RightHandThumb3MinRLimitField,
    RightHandThumb3RField,
    RightHandThumb3RotateAxisField,
    RightHandThumb3SField,
    RightHandThumb3TField,
    RightHandThumb4JointOrientField,
    RightHandThumb4MaxRLimitField,
    RightHandThumb4MinRLimitField,
    RightHandThumb4RField,
    RightHandThumb4RotateAxisField,
    RightHandThumb4SField,
    RightHandThumb4TField,
    RightInFootExtraFingerJointOrientField,
    RightInFootExtraFingerMaxRLimitField,
    RightInFootExtraFingerMinRLimitField,
    RightInFootExtraFingerRField,
    RightInFootExtraFingerRotateAxisField,
    RightInFootExtraFingerSField,
    RightInFootExtraFingerTField,
    RightInFootIndexJointOrientField,
    RightInFootIndexMaxRLimitField,
    RightInFootIndexMinRLimitField,
    RightInFootIndexRField,
    RightInFootIndexRotateAxisField,
    RightInFootIndexSField,
    RightInFootIndexTField,
    RightInFootMiddleJointOrientField,
    RightInFootMiddleMaxRLimitField,
    RightInFootMiddleMinRLimitField,
    RightInFootMiddleRField,
    RightInFootMiddleRotateAxisField,
    RightInFootMiddleSField,
    RightInFootMiddleTField,
    RightInFootPinkyJointOrientField,
    RightInFootPinkyMaxRLimitField,
    RightInFootPinkyMinRLimitField,
    RightInFootPinkyRField,
    RightInFootPinkyRotateAxisField,
    RightInFootPinkySField,
    RightInFootPinkyTField,
    RightInFootRingJointOrientField,
    RightInFootRingMaxRLimitField,
    RightInFootRingMinRLimitField,
    RightInFootRingRField,
    RightInFootRingRotateAxisField,
    RightInFootRingSField,
    RightInFootRingTField,
    RightInFootThumbJointOrientField,
    RightInFootThumbMaxRLimitField,
    RightInFootThumbMinRLimitField,
    RightInFootThumbRField,
    RightInFootThumbRotateAxisField,
    RightInFootThumbSField,
    RightInFootThumbTField,
    RightInHandExtraFingerJointOrientField,
    RightInHandExtraFingerMaxRLimitField,
    RightInHandExtraFingerMinRLimitField,
    RightInHandExtraFingerRField,
    RightInHandExtraFingerRotateAxisField,
    RightInHandExtraFingerSField,
    RightInHandExtraFingerTField,
    RightInHandIndexJointOrientField,
    RightInHandIndexMaxRLimitField,
    RightInHandIndexMinRLimitField,
    RightInHandIndexRField,
    RightInHandIndexRotateAxisField,
    RightInHandIndexSField,
    RightInHandIndexTField,
    RightInHandMiddleJointOrientField,
    RightInHandMiddleMaxRLimitField,
    RightInHandMiddleMinRLimitField,
    RightInHandMiddleRField,
    RightInHandMiddleRotateAxisField,
    RightInHandMiddleSField,
    RightInHandMiddleTField,
    RightInHandPinkyJointOrientField,
    RightInHandPinkyMaxRLimitField,
    RightInHandPinkyMinRLimitField,
    RightInHandPinkyRField,
    RightInHandPinkyRotateAxisField,
    RightInHandPinkySField,
    RightInHandPinkyTField,
    RightInHandRingJointOrientField,
    RightInHandRingMaxRLimitField,
    RightInHandRingMinRLimitField,
    RightInHandRingRField,
    RightInHandRingRotateAxisField,
    RightInHandRingSField,
    RightInHandRingTField,
    RightInHandThumbJointOrientField,
    RightInHandThumbMaxRLimitField,
    RightInHandThumbMinRLimitField,
    RightInHandThumbRField,
    RightInHandThumbRotateAxisField,
    RightInHandThumbSField,
    RightInHandThumbTField,
    RightLegJointOrientField,
    RightLegMaxRLimitField,
    RightLegMinRLimitField,
    RightLegRField,
    RightLegRollJointOrientField,
    RightLegRollMaxRLimitField,
    RightLegRollMinRLimitField,
    RightLegRollRField,
    RightLegRollRotateAxisField,
    RightLegRollSField,
    RightLegRollTField,
    RightLegRotateAxisField,
    RightLegSField,
    RightLegTField,
    RightShoulderExtraJointOrientField,
    RightShoulderExtraMaxRLimitField,
    RightShoulderExtraMinRLimitField,
    RightShoulderExtraRField,
    RightShoulderExtraRotateAxisField,
    RightShoulderExtraSField,
    RightShoulderExtraTField,
    RightShoulderJointOrientField,
    RightShoulderMaxRLimitField,
    RightShoulderMinRLimitField,
    RightShoulderRField,
    RightShoulderRotateAxisField,
    RightShoulderSField,
    RightShoulderTField,
    RightToeBaseJointOrientField,
    RightToeBaseMaxRLimitField,
    RightToeBaseMinRLimitField,
    RightToeBaseRField,
    RightToeBaseRotateAxisField,
    RightToeBaseSField,
    RightToeBaseTField,
    RightUpLegJointOrientField,
    RightUpLegMaxRLimitField,
    RightUpLegMinRLimitField,
    RightUpLegRField,
    RightUpLegRollJointOrientField,
    RightUpLegRollMaxRLimitField,
    RightUpLegRollMinRLimitField,
    RightUpLegRollRField,
    RightUpLegRollRotateAxisField,
    RightUpLegRollSField,
    RightUpLegRollTField,
    RightUpLegRotateAxisField,
    RightUpLegSField,
    RightUpLegTField,
    Spine1JointOrientField,
    Spine1MaxRLimitField,
    Spine1MinRLimitField,
    Spine1RField,
    Spine1RotateAxisField,
    Spine1SField,
    Spine1TField,
    Spine2JointOrientField,
    Spine2MaxRLimitField,
    Spine2MinRLimitField,
    Spine2RField,
    Spine2RotateAxisField,
    Spine2SField,
    Spine2TField,
    Spine3JointOrientField,
    Spine3MaxRLimitField,
    Spine3MinRLimitField,
    Spine3RField,
    Spine3RotateAxisField,
    Spine3SField,
    Spine3TField,
    Spine4JointOrientField,
    Spine4MaxRLimitField,
    Spine4MinRLimitField,
    Spine4RField,
    Spine4RotateAxisField,
    Spine4SField,
    Spine4TField,
    Spine5JointOrientField,
    Spine5MaxRLimitField,
    Spine5MinRLimitField,
    Spine5RField,
    Spine5RotateAxisField,
    Spine5SField,
    Spine5TField,
    Spine6JointOrientField,
    Spine6MaxRLimitField,
    Spine6MinRLimitField,
    Spine6RField,
    Spine6RotateAxisField,
    Spine6SField,
    Spine6TField,
    Spine7JointOrientField,
    Spine7MaxRLimitField,
    Spine7MinRLimitField,
    Spine7RField,
    Spine7RotateAxisField,
    Spine7SField,
    Spine7TField,
    Spine8JointOrientField,
    Spine8MaxRLimitField,
    Spine8MinRLimitField,
    Spine8RField,
    Spine8RotateAxisField,
    Spine8SField,
    Spine8TField,
    Spine9JointOrientField,
    Spine9MaxRLimitField,
    Spine9MinRLimitField,
    Spine9RField,
    Spine9RotateAxisField,
    Spine9SField,
    Spine9TField,
    SpineJointOrientField,
    SpineMaxRLimitField,
    SpineMinRLimitField,
    SpineRField,
    SpineRotateAxisField,
    SpineSField,
    SpineTField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField


class ReferenceRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class ReferenceRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class ReferenceRotateOrderEnumField(
    EnumField[ReferenceRotateOrderEnumAttrOperator, ReferenceRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReferenceRotateOrderEnumAttrOperator
    PLUG_CLS = ReferenceRotateOrderEnumPlugOperator


class HipsRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class HipsRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class HipsRotateOrderEnumField(
    EnumField[HipsRotateOrderEnumAttrOperator, HipsRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsRotateOrderEnumAttrOperator
    PLUG_CLS = HipsRotateOrderEnumPlugOperator


class LeftUpLegRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftUpLegRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftUpLegRotateOrderEnumField(
    EnumField[LeftUpLegRotateOrderEnumAttrOperator, LeftUpLegRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegRotateOrderEnumAttrOperator
    PLUG_CLS = LeftUpLegRotateOrderEnumPlugOperator


class LeftLegRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftLegRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftLegRotateOrderEnumField(
    EnumField[LeftLegRotateOrderEnumAttrOperator, LeftLegRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegRotateOrderEnumAttrOperator
    PLUG_CLS = LeftLegRotateOrderEnumPlugOperator


class LeftFootRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootRotateOrderEnumField(
    EnumField[LeftFootRotateOrderEnumAttrOperator, LeftFootRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootRotateOrderEnumPlugOperator


class RightUpLegRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightUpLegRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightUpLegRotateOrderEnumField(
    EnumField[RightUpLegRotateOrderEnumAttrOperator, RightUpLegRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegRotateOrderEnumAttrOperator
    PLUG_CLS = RightUpLegRotateOrderEnumPlugOperator


class RightLegRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightLegRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightLegRotateOrderEnumField(
    EnumField[RightLegRotateOrderEnumAttrOperator, RightLegRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegRotateOrderEnumAttrOperator
    PLUG_CLS = RightLegRotateOrderEnumPlugOperator


class RightFootRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootRotateOrderEnumField(
    EnumField[RightFootRotateOrderEnumAttrOperator, RightFootRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRotateOrderEnumAttrOperator
    PLUG_CLS = RightFootRotateOrderEnumPlugOperator


class SpineRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class SpineRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class SpineRotateOrderEnumField(
    EnumField[SpineRotateOrderEnumAttrOperator, SpineRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpineRotateOrderEnumAttrOperator
    PLUG_CLS = SpineRotateOrderEnumPlugOperator


class LeftArmRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftArmRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftArmRotateOrderEnumField(
    EnumField[LeftArmRotateOrderEnumAttrOperator, LeftArmRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmRotateOrderEnumAttrOperator
    PLUG_CLS = LeftArmRotateOrderEnumPlugOperator


class LeftForeArmRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftForeArmRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftForeArmRotateOrderEnumField(
    EnumField[LeftForeArmRotateOrderEnumAttrOperator, LeftForeArmRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmRotateOrderEnumAttrOperator
    PLUG_CLS = LeftForeArmRotateOrderEnumPlugOperator


class LeftHandRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandRotateOrderEnumField(
    EnumField[LeftHandRotateOrderEnumAttrOperator, LeftHandRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandRotateOrderEnumPlugOperator


class RightArmRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightArmRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightArmRotateOrderEnumField(
    EnumField[RightArmRotateOrderEnumAttrOperator, RightArmRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmRotateOrderEnumAttrOperator
    PLUG_CLS = RightArmRotateOrderEnumPlugOperator


class RightForeArmRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightForeArmRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightForeArmRotateOrderEnumField(
    EnumField[RightForeArmRotateOrderEnumAttrOperator, RightForeArmRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmRotateOrderEnumAttrOperator
    PLUG_CLS = RightForeArmRotateOrderEnumPlugOperator


class RightHandRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandRotateOrderEnumField(
    EnumField[RightHandRotateOrderEnumAttrOperator, RightHandRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRotateOrderEnumAttrOperator
    PLUG_CLS = RightHandRotateOrderEnumPlugOperator


class HeadRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class HeadRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class HeadRotateOrderEnumField(
    EnumField[HeadRotateOrderEnumAttrOperator, HeadRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HeadRotateOrderEnumAttrOperator
    PLUG_CLS = HeadRotateOrderEnumPlugOperator


class LeftToeBaseRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftToeBaseRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftToeBaseRotateOrderEnumField(
    EnumField[LeftToeBaseRotateOrderEnumAttrOperator, LeftToeBaseRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftToeBaseRotateOrderEnumAttrOperator
    PLUG_CLS = LeftToeBaseRotateOrderEnumPlugOperator


class RightToeBaseRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightToeBaseRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightToeBaseRotateOrderEnumField(
    EnumField[RightToeBaseRotateOrderEnumAttrOperator, RightToeBaseRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightToeBaseRotateOrderEnumAttrOperator
    PLUG_CLS = RightToeBaseRotateOrderEnumPlugOperator


class LeftShoulderRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftShoulderRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftShoulderRotateOrderEnumField(
    EnumField[LeftShoulderRotateOrderEnumAttrOperator, LeftShoulderRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderRotateOrderEnumAttrOperator
    PLUG_CLS = LeftShoulderRotateOrderEnumPlugOperator


class RightShoulderRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightShoulderRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightShoulderRotateOrderEnumField(
    EnumField[RightShoulderRotateOrderEnumAttrOperator, RightShoulderRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderRotateOrderEnumAttrOperator
    PLUG_CLS = RightShoulderRotateOrderEnumPlugOperator


class NeckRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class NeckRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class NeckRotateOrderEnumField(
    EnumField[NeckRotateOrderEnumAttrOperator, NeckRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NeckRotateOrderEnumAttrOperator
    PLUG_CLS = NeckRotateOrderEnumPlugOperator


class LeftFingerBaseRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFingerBaseRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFingerBaseRotateOrderEnumField(
    EnumField[LeftFingerBaseRotateOrderEnumAttrOperator, LeftFingerBaseRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFingerBaseRotateOrderEnumAttrOperator
    PLUG_CLS = LeftFingerBaseRotateOrderEnumPlugOperator


class RightFingerBaseRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFingerBaseRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFingerBaseRotateOrderEnumField(
    EnumField[RightFingerBaseRotateOrderEnumAttrOperator, RightFingerBaseRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFingerBaseRotateOrderEnumAttrOperator
    PLUG_CLS = RightFingerBaseRotateOrderEnumPlugOperator


class Spine1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Spine1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Spine1RotateOrderEnumField(
    EnumField[Spine1RotateOrderEnumAttrOperator, Spine1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine1RotateOrderEnumAttrOperator
    PLUG_CLS = Spine1RotateOrderEnumPlugOperator


class Spine2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Spine2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Spine2RotateOrderEnumField(
    EnumField[Spine2RotateOrderEnumAttrOperator, Spine2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine2RotateOrderEnumAttrOperator
    PLUG_CLS = Spine2RotateOrderEnumPlugOperator


class Spine3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Spine3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Spine3RotateOrderEnumField(
    EnumField[Spine3RotateOrderEnumAttrOperator, Spine3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine3RotateOrderEnumAttrOperator
    PLUG_CLS = Spine3RotateOrderEnumPlugOperator


class Spine4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Spine4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Spine4RotateOrderEnumField(
    EnumField[Spine4RotateOrderEnumAttrOperator, Spine4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine4RotateOrderEnumAttrOperator
    PLUG_CLS = Spine4RotateOrderEnumPlugOperator


class Spine5RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Spine5RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Spine5RotateOrderEnumField(
    EnumField[Spine5RotateOrderEnumAttrOperator, Spine5RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine5RotateOrderEnumAttrOperator
    PLUG_CLS = Spine5RotateOrderEnumPlugOperator


class Spine6RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Spine6RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Spine6RotateOrderEnumField(
    EnumField[Spine6RotateOrderEnumAttrOperator, Spine6RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine6RotateOrderEnumAttrOperator
    PLUG_CLS = Spine6RotateOrderEnumPlugOperator


class Spine7RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Spine7RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Spine7RotateOrderEnumField(
    EnumField[Spine7RotateOrderEnumAttrOperator, Spine7RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine7RotateOrderEnumAttrOperator
    PLUG_CLS = Spine7RotateOrderEnumPlugOperator


class Spine8RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Spine8RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Spine8RotateOrderEnumField(
    EnumField[Spine8RotateOrderEnumAttrOperator, Spine8RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine8RotateOrderEnumAttrOperator
    PLUG_CLS = Spine8RotateOrderEnumPlugOperator


class Spine9RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Spine9RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Spine9RotateOrderEnumField(
    EnumField[Spine9RotateOrderEnumAttrOperator, Spine9RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine9RotateOrderEnumAttrOperator
    PLUG_CLS = Spine9RotateOrderEnumPlugOperator


class Neck1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Neck1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Neck1RotateOrderEnumField(
    EnumField[Neck1RotateOrderEnumAttrOperator, Neck1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck1RotateOrderEnumAttrOperator
    PLUG_CLS = Neck1RotateOrderEnumPlugOperator


class Neck2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Neck2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Neck2RotateOrderEnumField(
    EnumField[Neck2RotateOrderEnumAttrOperator, Neck2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck2RotateOrderEnumAttrOperator
    PLUG_CLS = Neck2RotateOrderEnumPlugOperator


class Neck3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Neck3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Neck3RotateOrderEnumField(
    EnumField[Neck3RotateOrderEnumAttrOperator, Neck3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck3RotateOrderEnumAttrOperator
    PLUG_CLS = Neck3RotateOrderEnumPlugOperator


class Neck4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Neck4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Neck4RotateOrderEnumField(
    EnumField[Neck4RotateOrderEnumAttrOperator, Neck4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck4RotateOrderEnumAttrOperator
    PLUG_CLS = Neck4RotateOrderEnumPlugOperator


class Neck5RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Neck5RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Neck5RotateOrderEnumField(
    EnumField[Neck5RotateOrderEnumAttrOperator, Neck5RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck5RotateOrderEnumAttrOperator
    PLUG_CLS = Neck5RotateOrderEnumPlugOperator


class Neck6RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Neck6RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Neck6RotateOrderEnumField(
    EnumField[Neck6RotateOrderEnumAttrOperator, Neck6RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck6RotateOrderEnumAttrOperator
    PLUG_CLS = Neck6RotateOrderEnumPlugOperator


class Neck7RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Neck7RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Neck7RotateOrderEnumField(
    EnumField[Neck7RotateOrderEnumAttrOperator, Neck7RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck7RotateOrderEnumAttrOperator
    PLUG_CLS = Neck7RotateOrderEnumPlugOperator


class Neck8RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Neck8RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Neck8RotateOrderEnumField(
    EnumField[Neck8RotateOrderEnumAttrOperator, Neck8RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck8RotateOrderEnumAttrOperator
    PLUG_CLS = Neck8RotateOrderEnumPlugOperator


class Neck9RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class Neck9RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class Neck9RotateOrderEnumField(
    EnumField[Neck9RotateOrderEnumAttrOperator, Neck9RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck9RotateOrderEnumAttrOperator
    PLUG_CLS = Neck9RotateOrderEnumPlugOperator


class LeftUpLegRollRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftUpLegRollRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftUpLegRollRotateOrderEnumField(
    EnumField[LeftUpLegRollRotateOrderEnumAttrOperator, LeftUpLegRollRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegRollRotateOrderEnumAttrOperator
    PLUG_CLS = LeftUpLegRollRotateOrderEnumPlugOperator


class LeftLegRollRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftLegRollRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftLegRollRotateOrderEnumField(
    EnumField[LeftLegRollRotateOrderEnumAttrOperator, LeftLegRollRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegRollRotateOrderEnumAttrOperator
    PLUG_CLS = LeftLegRollRotateOrderEnumPlugOperator


class RightUpLegRollRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightUpLegRollRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightUpLegRollRotateOrderEnumField(
    EnumField[RightUpLegRollRotateOrderEnumAttrOperator, RightUpLegRollRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegRollRotateOrderEnumAttrOperator
    PLUG_CLS = RightUpLegRollRotateOrderEnumPlugOperator


class RightLegRollRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightLegRollRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightLegRollRotateOrderEnumField(
    EnumField[RightLegRollRotateOrderEnumAttrOperator, RightLegRollRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegRollRotateOrderEnumAttrOperator
    PLUG_CLS = RightLegRollRotateOrderEnumPlugOperator


class LeftArmRollRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftArmRollRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftArmRollRotateOrderEnumField(
    EnumField[LeftArmRollRotateOrderEnumAttrOperator, LeftArmRollRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmRollRotateOrderEnumAttrOperator
    PLUG_CLS = LeftArmRollRotateOrderEnumPlugOperator


class LeftForeArmRollRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftForeArmRollRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftForeArmRollRotateOrderEnumField(
    EnumField[LeftForeArmRollRotateOrderEnumAttrOperator, LeftForeArmRollRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmRollRotateOrderEnumAttrOperator
    PLUG_CLS = LeftForeArmRollRotateOrderEnumPlugOperator


class RightArmRollRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightArmRollRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightArmRollRotateOrderEnumField(
    EnumField[RightArmRollRotateOrderEnumAttrOperator, RightArmRollRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmRollRotateOrderEnumAttrOperator
    PLUG_CLS = RightArmRollRotateOrderEnumPlugOperator


class RightForeArmRollRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightForeArmRollRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightForeArmRollRotateOrderEnumField(
    EnumField[RightForeArmRollRotateOrderEnumAttrOperator, RightForeArmRollRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmRollRotateOrderEnumAttrOperator
    PLUG_CLS = RightForeArmRollRotateOrderEnumPlugOperator


class HipsTranslationRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class HipsTranslationRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class HipsTranslationRotateOrderEnumField(
    EnumField[HipsTranslationRotateOrderEnumAttrOperator, HipsTranslationRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsTranslationRotateOrderEnumAttrOperator
    PLUG_CLS = HipsTranslationRotateOrderEnumPlugOperator


class LeftHandThumb1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandThumb1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandThumb1RotateOrderEnumField(
    EnumField[LeftHandThumb1RotateOrderEnumAttrOperator, LeftHandThumb1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandThumb1RotateOrderEnumPlugOperator


class LeftHandThumb2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandThumb2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandThumb2RotateOrderEnumField(
    EnumField[LeftHandThumb2RotateOrderEnumAttrOperator, LeftHandThumb2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandThumb2RotateOrderEnumPlugOperator


class LeftHandThumb3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandThumb3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandThumb3RotateOrderEnumField(
    EnumField[LeftHandThumb3RotateOrderEnumAttrOperator, LeftHandThumb3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandThumb3RotateOrderEnumPlugOperator


class LeftHandThumb4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandThumb4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandThumb4RotateOrderEnumField(
    EnumField[LeftHandThumb4RotateOrderEnumAttrOperator, LeftHandThumb4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandThumb4RotateOrderEnumPlugOperator


class LeftHandIndex1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandIndex1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandIndex1RotateOrderEnumField(
    EnumField[LeftHandIndex1RotateOrderEnumAttrOperator, LeftHandIndex1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandIndex1RotateOrderEnumPlugOperator


class LeftHandIndex2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandIndex2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandIndex2RotateOrderEnumField(
    EnumField[LeftHandIndex2RotateOrderEnumAttrOperator, LeftHandIndex2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandIndex2RotateOrderEnumPlugOperator


class LeftHandIndex3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandIndex3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandIndex3RotateOrderEnumField(
    EnumField[LeftHandIndex3RotateOrderEnumAttrOperator, LeftHandIndex3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandIndex3RotateOrderEnumPlugOperator


class LeftHandIndex4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandIndex4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandIndex4RotateOrderEnumField(
    EnumField[LeftHandIndex4RotateOrderEnumAttrOperator, LeftHandIndex4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandIndex4RotateOrderEnumPlugOperator


class LeftHandMiddle1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandMiddle1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandMiddle1RotateOrderEnumField(
    EnumField[LeftHandMiddle1RotateOrderEnumAttrOperator, LeftHandMiddle1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandMiddle1RotateOrderEnumPlugOperator


class LeftHandMiddle2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandMiddle2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandMiddle2RotateOrderEnumField(
    EnumField[LeftHandMiddle2RotateOrderEnumAttrOperator, LeftHandMiddle2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandMiddle2RotateOrderEnumPlugOperator


class LeftHandMiddle3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandMiddle3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandMiddle3RotateOrderEnumField(
    EnumField[LeftHandMiddle3RotateOrderEnumAttrOperator, LeftHandMiddle3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandMiddle3RotateOrderEnumPlugOperator


class LeftHandMiddle4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandMiddle4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandMiddle4RotateOrderEnumField(
    EnumField[LeftHandMiddle4RotateOrderEnumAttrOperator, LeftHandMiddle4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandMiddle4RotateOrderEnumPlugOperator


class LeftHandRing1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandRing1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandRing1RotateOrderEnumField(
    EnumField[LeftHandRing1RotateOrderEnumAttrOperator, LeftHandRing1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandRing1RotateOrderEnumPlugOperator


class LeftHandRing2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandRing2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandRing2RotateOrderEnumField(
    EnumField[LeftHandRing2RotateOrderEnumAttrOperator, LeftHandRing2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandRing2RotateOrderEnumPlugOperator


class LeftHandRing3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandRing3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandRing3RotateOrderEnumField(
    EnumField[LeftHandRing3RotateOrderEnumAttrOperator, LeftHandRing3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandRing3RotateOrderEnumPlugOperator


class LeftHandRing4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandRing4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandRing4RotateOrderEnumField(
    EnumField[LeftHandRing4RotateOrderEnumAttrOperator, LeftHandRing4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandRing4RotateOrderEnumPlugOperator


class LeftHandPinky1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandPinky1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandPinky1RotateOrderEnumField(
    EnumField[LeftHandPinky1RotateOrderEnumAttrOperator, LeftHandPinky1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandPinky1RotateOrderEnumPlugOperator


class LeftHandPinky2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandPinky2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandPinky2RotateOrderEnumField(
    EnumField[LeftHandPinky2RotateOrderEnumAttrOperator, LeftHandPinky2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandPinky2RotateOrderEnumPlugOperator


class LeftHandPinky3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandPinky3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandPinky3RotateOrderEnumField(
    EnumField[LeftHandPinky3RotateOrderEnumAttrOperator, LeftHandPinky3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandPinky3RotateOrderEnumPlugOperator


class LeftHandPinky4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandPinky4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandPinky4RotateOrderEnumField(
    EnumField[LeftHandPinky4RotateOrderEnumAttrOperator, LeftHandPinky4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandPinky4RotateOrderEnumPlugOperator


class LeftHandExtraFinger1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandExtraFinger1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandExtraFinger1RotateOrderEnumField(
    EnumField[LeftHandExtraFinger1RotateOrderEnumAttrOperator, LeftHandExtraFinger1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandExtraFinger1RotateOrderEnumPlugOperator


class LeftHandExtraFinger2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandExtraFinger2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandExtraFinger2RotateOrderEnumField(
    EnumField[LeftHandExtraFinger2RotateOrderEnumAttrOperator, LeftHandExtraFinger2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandExtraFinger2RotateOrderEnumPlugOperator


class LeftHandExtraFinger3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandExtraFinger3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandExtraFinger3RotateOrderEnumField(
    EnumField[LeftHandExtraFinger3RotateOrderEnumAttrOperator, LeftHandExtraFinger3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandExtraFinger3RotateOrderEnumPlugOperator


class LeftHandExtraFinger4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftHandExtraFinger4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftHandExtraFinger4RotateOrderEnumField(
    EnumField[LeftHandExtraFinger4RotateOrderEnumAttrOperator, LeftHandExtraFinger4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftHandExtraFinger4RotateOrderEnumPlugOperator


class RightHandThumb1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandThumb1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandThumb1RotateOrderEnumField(
    EnumField[RightHandThumb1RotateOrderEnumAttrOperator, RightHandThumb1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb1RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandThumb1RotateOrderEnumPlugOperator


class RightHandThumb2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandThumb2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandThumb2RotateOrderEnumField(
    EnumField[RightHandThumb2RotateOrderEnumAttrOperator, RightHandThumb2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb2RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandThumb2RotateOrderEnumPlugOperator


class RightHandThumb3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandThumb3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandThumb3RotateOrderEnumField(
    EnumField[RightHandThumb3RotateOrderEnumAttrOperator, RightHandThumb3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb3RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandThumb3RotateOrderEnumPlugOperator


class RightHandThumb4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandThumb4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandThumb4RotateOrderEnumField(
    EnumField[RightHandThumb4RotateOrderEnumAttrOperator, RightHandThumb4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb4RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandThumb4RotateOrderEnumPlugOperator


class RightHandIndex1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandIndex1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandIndex1RotateOrderEnumField(
    EnumField[RightHandIndex1RotateOrderEnumAttrOperator, RightHandIndex1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex1RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandIndex1RotateOrderEnumPlugOperator


class RightHandIndex2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandIndex2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandIndex2RotateOrderEnumField(
    EnumField[RightHandIndex2RotateOrderEnumAttrOperator, RightHandIndex2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex2RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandIndex2RotateOrderEnumPlugOperator


class RightHandIndex3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandIndex3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandIndex3RotateOrderEnumField(
    EnumField[RightHandIndex3RotateOrderEnumAttrOperator, RightHandIndex3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex3RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandIndex3RotateOrderEnumPlugOperator


class RightHandIndex4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandIndex4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandIndex4RotateOrderEnumField(
    EnumField[RightHandIndex4RotateOrderEnumAttrOperator, RightHandIndex4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex4RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandIndex4RotateOrderEnumPlugOperator


class RightHandMiddle1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandMiddle1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandMiddle1RotateOrderEnumField(
    EnumField[RightHandMiddle1RotateOrderEnumAttrOperator, RightHandMiddle1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle1RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandMiddle1RotateOrderEnumPlugOperator


class RightHandMiddle2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandMiddle2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandMiddle2RotateOrderEnumField(
    EnumField[RightHandMiddle2RotateOrderEnumAttrOperator, RightHandMiddle2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle2RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandMiddle2RotateOrderEnumPlugOperator


class RightHandMiddle3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandMiddle3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandMiddle3RotateOrderEnumField(
    EnumField[RightHandMiddle3RotateOrderEnumAttrOperator, RightHandMiddle3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle3RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandMiddle3RotateOrderEnumPlugOperator


class RightHandMiddle4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandMiddle4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandMiddle4RotateOrderEnumField(
    EnumField[RightHandMiddle4RotateOrderEnumAttrOperator, RightHandMiddle4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle4RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandMiddle4RotateOrderEnumPlugOperator


class RightHandRing1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandRing1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandRing1RotateOrderEnumField(
    EnumField[RightHandRing1RotateOrderEnumAttrOperator, RightHandRing1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing1RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandRing1RotateOrderEnumPlugOperator


class RightHandRing2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandRing2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandRing2RotateOrderEnumField(
    EnumField[RightHandRing2RotateOrderEnumAttrOperator, RightHandRing2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing2RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandRing2RotateOrderEnumPlugOperator


class RightHandRing3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandRing3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandRing3RotateOrderEnumField(
    EnumField[RightHandRing3RotateOrderEnumAttrOperator, RightHandRing3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing3RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandRing3RotateOrderEnumPlugOperator


class RightHandRing4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandRing4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandRing4RotateOrderEnumField(
    EnumField[RightHandRing4RotateOrderEnumAttrOperator, RightHandRing4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing4RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandRing4RotateOrderEnumPlugOperator


class RightHandPinky1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandPinky1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandPinky1RotateOrderEnumField(
    EnumField[RightHandPinky1RotateOrderEnumAttrOperator, RightHandPinky1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky1RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandPinky1RotateOrderEnumPlugOperator


class RightHandPinky2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandPinky2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandPinky2RotateOrderEnumField(
    EnumField[RightHandPinky2RotateOrderEnumAttrOperator, RightHandPinky2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky2RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandPinky2RotateOrderEnumPlugOperator


class RightHandPinky3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandPinky3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandPinky3RotateOrderEnumField(
    EnumField[RightHandPinky3RotateOrderEnumAttrOperator, RightHandPinky3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky3RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandPinky3RotateOrderEnumPlugOperator


class RightHandPinky4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandPinky4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandPinky4RotateOrderEnumField(
    EnumField[RightHandPinky4RotateOrderEnumAttrOperator, RightHandPinky4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky4RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandPinky4RotateOrderEnumPlugOperator


class RightHandExtraFinger1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandExtraFinger1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandExtraFinger1RotateOrderEnumField(
    EnumField[RightHandExtraFinger1RotateOrderEnumAttrOperator, RightHandExtraFinger1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger1RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandExtraFinger1RotateOrderEnumPlugOperator


class RightHandExtraFinger2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandExtraFinger2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandExtraFinger2RotateOrderEnumField(
    EnumField[RightHandExtraFinger2RotateOrderEnumAttrOperator, RightHandExtraFinger2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger2RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandExtraFinger2RotateOrderEnumPlugOperator


class RightHandExtraFinger3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandExtraFinger3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandExtraFinger3RotateOrderEnumField(
    EnumField[RightHandExtraFinger3RotateOrderEnumAttrOperator, RightHandExtraFinger3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger3RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandExtraFinger3RotateOrderEnumPlugOperator


class RightHandExtraFinger4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightHandExtraFinger4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightHandExtraFinger4RotateOrderEnumField(
    EnumField[RightHandExtraFinger4RotateOrderEnumAttrOperator, RightHandExtraFinger4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger4RotateOrderEnumAttrOperator
    PLUG_CLS = RightHandExtraFinger4RotateOrderEnumPlugOperator


class LeftFootThumb1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootThumb1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootThumb1RotateOrderEnumField(
    EnumField[LeftFootThumb1RotateOrderEnumAttrOperator, LeftFootThumb1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootThumb1RotateOrderEnumPlugOperator


class LeftFootThumb2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootThumb2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootThumb2RotateOrderEnumField(
    EnumField[LeftFootThumb2RotateOrderEnumAttrOperator, LeftFootThumb2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootThumb2RotateOrderEnumPlugOperator


class LeftFootThumb3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootThumb3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootThumb3RotateOrderEnumField(
    EnumField[LeftFootThumb3RotateOrderEnumAttrOperator, LeftFootThumb3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootThumb3RotateOrderEnumPlugOperator


class LeftFootThumb4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootThumb4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootThumb4RotateOrderEnumField(
    EnumField[LeftFootThumb4RotateOrderEnumAttrOperator, LeftFootThumb4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootThumb4RotateOrderEnumPlugOperator


class LeftFootIndex1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootIndex1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootIndex1RotateOrderEnumField(
    EnumField[LeftFootIndex1RotateOrderEnumAttrOperator, LeftFootIndex1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootIndex1RotateOrderEnumPlugOperator


class LeftFootIndex2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootIndex2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootIndex2RotateOrderEnumField(
    EnumField[LeftFootIndex2RotateOrderEnumAttrOperator, LeftFootIndex2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootIndex2RotateOrderEnumPlugOperator


class LeftFootIndex3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootIndex3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootIndex3RotateOrderEnumField(
    EnumField[LeftFootIndex3RotateOrderEnumAttrOperator, LeftFootIndex3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootIndex3RotateOrderEnumPlugOperator


class LeftFootIndex4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootIndex4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootIndex4RotateOrderEnumField(
    EnumField[LeftFootIndex4RotateOrderEnumAttrOperator, LeftFootIndex4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootIndex4RotateOrderEnumPlugOperator


class LeftFootMiddle1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootMiddle1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootMiddle1RotateOrderEnumField(
    EnumField[LeftFootMiddle1RotateOrderEnumAttrOperator, LeftFootMiddle1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootMiddle1RotateOrderEnumPlugOperator


class LeftFootMiddle2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootMiddle2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootMiddle2RotateOrderEnumField(
    EnumField[LeftFootMiddle2RotateOrderEnumAttrOperator, LeftFootMiddle2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootMiddle2RotateOrderEnumPlugOperator


class LeftFootMiddle3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootMiddle3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootMiddle3RotateOrderEnumField(
    EnumField[LeftFootMiddle3RotateOrderEnumAttrOperator, LeftFootMiddle3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootMiddle3RotateOrderEnumPlugOperator


class LeftFootMiddle4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootMiddle4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootMiddle4RotateOrderEnumField(
    EnumField[LeftFootMiddle4RotateOrderEnumAttrOperator, LeftFootMiddle4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootMiddle4RotateOrderEnumPlugOperator


class LeftFootRing1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootRing1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootRing1RotateOrderEnumField(
    EnumField[LeftFootRing1RotateOrderEnumAttrOperator, LeftFootRing1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootRing1RotateOrderEnumPlugOperator


class LeftFootRing2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootRing2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootRing2RotateOrderEnumField(
    EnumField[LeftFootRing2RotateOrderEnumAttrOperator, LeftFootRing2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootRing2RotateOrderEnumPlugOperator


class LeftFootRing3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootRing3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootRing3RotateOrderEnumField(
    EnumField[LeftFootRing3RotateOrderEnumAttrOperator, LeftFootRing3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootRing3RotateOrderEnumPlugOperator


class LeftFootRing4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootRing4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootRing4RotateOrderEnumField(
    EnumField[LeftFootRing4RotateOrderEnumAttrOperator, LeftFootRing4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootRing4RotateOrderEnumPlugOperator


class LeftFootPinky1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootPinky1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootPinky1RotateOrderEnumField(
    EnumField[LeftFootPinky1RotateOrderEnumAttrOperator, LeftFootPinky1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootPinky1RotateOrderEnumPlugOperator


class LeftFootPinky2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootPinky2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootPinky2RotateOrderEnumField(
    EnumField[LeftFootPinky2RotateOrderEnumAttrOperator, LeftFootPinky2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootPinky2RotateOrderEnumPlugOperator


class LeftFootPinky3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootPinky3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootPinky3RotateOrderEnumField(
    EnumField[LeftFootPinky3RotateOrderEnumAttrOperator, LeftFootPinky3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootPinky3RotateOrderEnumPlugOperator


class LeftFootPinky4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootPinky4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootPinky4RotateOrderEnumField(
    EnumField[LeftFootPinky4RotateOrderEnumAttrOperator, LeftFootPinky4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootPinky4RotateOrderEnumPlugOperator


class LeftFootExtraFinger1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootExtraFinger1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootExtraFinger1RotateOrderEnumField(
    EnumField[LeftFootExtraFinger1RotateOrderEnumAttrOperator, LeftFootExtraFinger1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger1RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootExtraFinger1RotateOrderEnumPlugOperator


class LeftFootExtraFinger2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootExtraFinger2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootExtraFinger2RotateOrderEnumField(
    EnumField[LeftFootExtraFinger2RotateOrderEnumAttrOperator, LeftFootExtraFinger2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger2RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootExtraFinger2RotateOrderEnumPlugOperator


class LeftFootExtraFinger3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootExtraFinger3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootExtraFinger3RotateOrderEnumField(
    EnumField[LeftFootExtraFinger3RotateOrderEnumAttrOperator, LeftFootExtraFinger3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger3RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootExtraFinger3RotateOrderEnumPlugOperator


class LeftFootExtraFinger4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftFootExtraFinger4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftFootExtraFinger4RotateOrderEnumField(
    EnumField[LeftFootExtraFinger4RotateOrderEnumAttrOperator, LeftFootExtraFinger4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger4RotateOrderEnumAttrOperator
    PLUG_CLS = LeftFootExtraFinger4RotateOrderEnumPlugOperator


class RightFootThumb1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootThumb1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootThumb1RotateOrderEnumField(
    EnumField[RightFootThumb1RotateOrderEnumAttrOperator, RightFootThumb1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb1RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootThumb1RotateOrderEnumPlugOperator


class RightFootThumb2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootThumb2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootThumb2RotateOrderEnumField(
    EnumField[RightFootThumb2RotateOrderEnumAttrOperator, RightFootThumb2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb2RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootThumb2RotateOrderEnumPlugOperator


class RightFootThumb3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootThumb3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootThumb3RotateOrderEnumField(
    EnumField[RightFootThumb3RotateOrderEnumAttrOperator, RightFootThumb3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb3RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootThumb3RotateOrderEnumPlugOperator


class RightFootThumb4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootThumb4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootThumb4RotateOrderEnumField(
    EnumField[RightFootThumb4RotateOrderEnumAttrOperator, RightFootThumb4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb4RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootThumb4RotateOrderEnumPlugOperator


class RightFootIndex1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootIndex1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootIndex1RotateOrderEnumField(
    EnumField[RightFootIndex1RotateOrderEnumAttrOperator, RightFootIndex1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex1RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootIndex1RotateOrderEnumPlugOperator


class RightFootIndex2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootIndex2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootIndex2RotateOrderEnumField(
    EnumField[RightFootIndex2RotateOrderEnumAttrOperator, RightFootIndex2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex2RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootIndex2RotateOrderEnumPlugOperator


class RightFootIndex3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootIndex3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootIndex3RotateOrderEnumField(
    EnumField[RightFootIndex3RotateOrderEnumAttrOperator, RightFootIndex3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex3RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootIndex3RotateOrderEnumPlugOperator


class RightFootIndex4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootIndex4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootIndex4RotateOrderEnumField(
    EnumField[RightFootIndex4RotateOrderEnumAttrOperator, RightFootIndex4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex4RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootIndex4RotateOrderEnumPlugOperator


class RightFootMiddle1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootMiddle1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootMiddle1RotateOrderEnumField(
    EnumField[RightFootMiddle1RotateOrderEnumAttrOperator, RightFootMiddle1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle1RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootMiddle1RotateOrderEnumPlugOperator


class RightFootMiddle2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootMiddle2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootMiddle2RotateOrderEnumField(
    EnumField[RightFootMiddle2RotateOrderEnumAttrOperator, RightFootMiddle2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle2RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootMiddle2RotateOrderEnumPlugOperator


class RightFootMiddle3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootMiddle3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootMiddle3RotateOrderEnumField(
    EnumField[RightFootMiddle3RotateOrderEnumAttrOperator, RightFootMiddle3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle3RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootMiddle3RotateOrderEnumPlugOperator


class RightFootMiddle4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootMiddle4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootMiddle4RotateOrderEnumField(
    EnumField[RightFootMiddle4RotateOrderEnumAttrOperator, RightFootMiddle4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle4RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootMiddle4RotateOrderEnumPlugOperator


class RightFootRing1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootRing1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootRing1RotateOrderEnumField(
    EnumField[RightFootRing1RotateOrderEnumAttrOperator, RightFootRing1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing1RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootRing1RotateOrderEnumPlugOperator


class RightFootRing2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootRing2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootRing2RotateOrderEnumField(
    EnumField[RightFootRing2RotateOrderEnumAttrOperator, RightFootRing2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing2RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootRing2RotateOrderEnumPlugOperator


class RightFootRing3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootRing3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootRing3RotateOrderEnumField(
    EnumField[RightFootRing3RotateOrderEnumAttrOperator, RightFootRing3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing3RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootRing3RotateOrderEnumPlugOperator


class RightFootRing4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootRing4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootRing4RotateOrderEnumField(
    EnumField[RightFootRing4RotateOrderEnumAttrOperator, RightFootRing4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing4RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootRing4RotateOrderEnumPlugOperator


class RightFootPinky1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootPinky1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootPinky1RotateOrderEnumField(
    EnumField[RightFootPinky1RotateOrderEnumAttrOperator, RightFootPinky1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky1RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootPinky1RotateOrderEnumPlugOperator


class RightFootPinky2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootPinky2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootPinky2RotateOrderEnumField(
    EnumField[RightFootPinky2RotateOrderEnumAttrOperator, RightFootPinky2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky2RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootPinky2RotateOrderEnumPlugOperator


class RightFootPinky3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootPinky3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootPinky3RotateOrderEnumField(
    EnumField[RightFootPinky3RotateOrderEnumAttrOperator, RightFootPinky3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky3RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootPinky3RotateOrderEnumPlugOperator


class RightFootPinky4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootPinky4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootPinky4RotateOrderEnumField(
    EnumField[RightFootPinky4RotateOrderEnumAttrOperator, RightFootPinky4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky4RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootPinky4RotateOrderEnumPlugOperator


class RightFootExtraFinger1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootExtraFinger1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootExtraFinger1RotateOrderEnumField(
    EnumField[RightFootExtraFinger1RotateOrderEnumAttrOperator, RightFootExtraFinger1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger1RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootExtraFinger1RotateOrderEnumPlugOperator


class RightFootExtraFinger2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootExtraFinger2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootExtraFinger2RotateOrderEnumField(
    EnumField[RightFootExtraFinger2RotateOrderEnumAttrOperator, RightFootExtraFinger2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger2RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootExtraFinger2RotateOrderEnumPlugOperator


class RightFootExtraFinger3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootExtraFinger3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootExtraFinger3RotateOrderEnumField(
    EnumField[RightFootExtraFinger3RotateOrderEnumAttrOperator, RightFootExtraFinger3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger3RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootExtraFinger3RotateOrderEnumPlugOperator


class RightFootExtraFinger4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightFootExtraFinger4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightFootExtraFinger4RotateOrderEnumField(
    EnumField[RightFootExtraFinger4RotateOrderEnumAttrOperator, RightFootExtraFinger4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger4RotateOrderEnumAttrOperator
    PLUG_CLS = RightFootExtraFinger4RotateOrderEnumPlugOperator


class LeftInHandThumbRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInHandThumbRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInHandThumbRotateOrderEnumField(
    EnumField[LeftInHandThumbRotateOrderEnumAttrOperator, LeftInHandThumbRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandThumbRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInHandThumbRotateOrderEnumPlugOperator


class LeftInHandIndexRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInHandIndexRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInHandIndexRotateOrderEnumField(
    EnumField[LeftInHandIndexRotateOrderEnumAttrOperator, LeftInHandIndexRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandIndexRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInHandIndexRotateOrderEnumPlugOperator


class LeftInHandMiddleRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInHandMiddleRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInHandMiddleRotateOrderEnumField(
    EnumField[LeftInHandMiddleRotateOrderEnumAttrOperator, LeftInHandMiddleRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandMiddleRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInHandMiddleRotateOrderEnumPlugOperator


class LeftInHandRingRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInHandRingRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInHandRingRotateOrderEnumField(
    EnumField[LeftInHandRingRotateOrderEnumAttrOperator, LeftInHandRingRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandRingRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInHandRingRotateOrderEnumPlugOperator


class LeftInHandPinkyRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInHandPinkyRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInHandPinkyRotateOrderEnumField(
    EnumField[LeftInHandPinkyRotateOrderEnumAttrOperator, LeftInHandPinkyRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandPinkyRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInHandPinkyRotateOrderEnumPlugOperator


class LeftInHandExtraFingerRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInHandExtraFingerRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInHandExtraFingerRotateOrderEnumField(
    EnumField[LeftInHandExtraFingerRotateOrderEnumAttrOperator, LeftInHandExtraFingerRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandExtraFingerRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInHandExtraFingerRotateOrderEnumPlugOperator


class RightInHandThumbRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInHandThumbRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInHandThumbRotateOrderEnumField(
    EnumField[RightInHandThumbRotateOrderEnumAttrOperator, RightInHandThumbRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandThumbRotateOrderEnumAttrOperator
    PLUG_CLS = RightInHandThumbRotateOrderEnumPlugOperator


class RightInHandIndexRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInHandIndexRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInHandIndexRotateOrderEnumField(
    EnumField[RightInHandIndexRotateOrderEnumAttrOperator, RightInHandIndexRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandIndexRotateOrderEnumAttrOperator
    PLUG_CLS = RightInHandIndexRotateOrderEnumPlugOperator


class RightInHandMiddleRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInHandMiddleRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInHandMiddleRotateOrderEnumField(
    EnumField[RightInHandMiddleRotateOrderEnumAttrOperator, RightInHandMiddleRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandMiddleRotateOrderEnumAttrOperator
    PLUG_CLS = RightInHandMiddleRotateOrderEnumPlugOperator


class RightInHandRingRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInHandRingRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInHandRingRotateOrderEnumField(
    EnumField[RightInHandRingRotateOrderEnumAttrOperator, RightInHandRingRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandRingRotateOrderEnumAttrOperator
    PLUG_CLS = RightInHandRingRotateOrderEnumPlugOperator


class RightInHandPinkyRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInHandPinkyRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInHandPinkyRotateOrderEnumField(
    EnumField[RightInHandPinkyRotateOrderEnumAttrOperator, RightInHandPinkyRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandPinkyRotateOrderEnumAttrOperator
    PLUG_CLS = RightInHandPinkyRotateOrderEnumPlugOperator


class RightInHandExtraFingerRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInHandExtraFingerRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInHandExtraFingerRotateOrderEnumField(
    EnumField[RightInHandExtraFingerRotateOrderEnumAttrOperator, RightInHandExtraFingerRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandExtraFingerRotateOrderEnumAttrOperator
    PLUG_CLS = RightInHandExtraFingerRotateOrderEnumPlugOperator


class LeftInFootThumbRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInFootThumbRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInFootThumbRotateOrderEnumField(
    EnumField[LeftInFootThumbRotateOrderEnumAttrOperator, LeftInFootThumbRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootThumbRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInFootThumbRotateOrderEnumPlugOperator


class LeftInFootIndexRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInFootIndexRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInFootIndexRotateOrderEnumField(
    EnumField[LeftInFootIndexRotateOrderEnumAttrOperator, LeftInFootIndexRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootIndexRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInFootIndexRotateOrderEnumPlugOperator


class LeftInFootMiddleRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInFootMiddleRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInFootMiddleRotateOrderEnumField(
    EnumField[LeftInFootMiddleRotateOrderEnumAttrOperator, LeftInFootMiddleRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootMiddleRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInFootMiddleRotateOrderEnumPlugOperator


class LeftInFootRingRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInFootRingRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInFootRingRotateOrderEnumField(
    EnumField[LeftInFootRingRotateOrderEnumAttrOperator, LeftInFootRingRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootRingRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInFootRingRotateOrderEnumPlugOperator


class LeftInFootPinkyRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInFootPinkyRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInFootPinkyRotateOrderEnumField(
    EnumField[LeftInFootPinkyRotateOrderEnumAttrOperator, LeftInFootPinkyRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootPinkyRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInFootPinkyRotateOrderEnumPlugOperator


class LeftInFootExtraFingerRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftInFootExtraFingerRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftInFootExtraFingerRotateOrderEnumField(
    EnumField[LeftInFootExtraFingerRotateOrderEnumAttrOperator, LeftInFootExtraFingerRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootExtraFingerRotateOrderEnumAttrOperator
    PLUG_CLS = LeftInFootExtraFingerRotateOrderEnumPlugOperator


class RightInFootThumbRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInFootThumbRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInFootThumbRotateOrderEnumField(
    EnumField[RightInFootThumbRotateOrderEnumAttrOperator, RightInFootThumbRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootThumbRotateOrderEnumAttrOperator
    PLUG_CLS = RightInFootThumbRotateOrderEnumPlugOperator


class RightInFootIndexRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInFootIndexRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInFootIndexRotateOrderEnumField(
    EnumField[RightInFootIndexRotateOrderEnumAttrOperator, RightInFootIndexRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootIndexRotateOrderEnumAttrOperator
    PLUG_CLS = RightInFootIndexRotateOrderEnumPlugOperator


class RightInFootMiddleRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInFootMiddleRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInFootMiddleRotateOrderEnumField(
    EnumField[RightInFootMiddleRotateOrderEnumAttrOperator, RightInFootMiddleRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootMiddleRotateOrderEnumAttrOperator
    PLUG_CLS = RightInFootMiddleRotateOrderEnumPlugOperator


class RightInFootRingRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInFootRingRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInFootRingRotateOrderEnumField(
    EnumField[RightInFootRingRotateOrderEnumAttrOperator, RightInFootRingRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootRingRotateOrderEnumAttrOperator
    PLUG_CLS = RightInFootRingRotateOrderEnumPlugOperator


class RightInFootPinkyRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInFootPinkyRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInFootPinkyRotateOrderEnumField(
    EnumField[RightInFootPinkyRotateOrderEnumAttrOperator, RightInFootPinkyRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootPinkyRotateOrderEnumAttrOperator
    PLUG_CLS = RightInFootPinkyRotateOrderEnumPlugOperator


class RightInFootExtraFingerRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightInFootExtraFingerRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightInFootExtraFingerRotateOrderEnumField(
    EnumField[RightInFootExtraFingerRotateOrderEnumAttrOperator, RightInFootExtraFingerRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootExtraFingerRotateOrderEnumAttrOperator
    PLUG_CLS = RightInFootExtraFingerRotateOrderEnumPlugOperator


class LeftShoulderExtraRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeftShoulderExtraRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeftShoulderExtraRotateOrderEnumField(
    EnumField[LeftShoulderExtraRotateOrderEnumAttrOperator, LeftShoulderExtraRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderExtraRotateOrderEnumAttrOperator
    PLUG_CLS = LeftShoulderExtraRotateOrderEnumPlugOperator


class RightShoulderExtraRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class RightShoulderExtraRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RightShoulderExtraRotateOrderEnumField(
    EnumField[RightShoulderExtraRotateOrderEnumAttrOperator, RightShoulderExtraRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderExtraRotateOrderEnumAttrOperator
    PLUG_CLS = RightShoulderExtraRotateOrderEnumPlugOperator


class LeafLeftUpLegRoll1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftUpLegRoll1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftUpLegRoll1RotateOrderEnumField(
    EnumField[LeafLeftUpLegRoll1RotateOrderEnumAttrOperator, LeafLeftUpLegRoll1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll1RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll1RotateOrderEnumPlugOperator


class LeafLeftLegRoll1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftLegRoll1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftLegRoll1RotateOrderEnumField(
    EnumField[LeafLeftLegRoll1RotateOrderEnumAttrOperator, LeafLeftLegRoll1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll1RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftLegRoll1RotateOrderEnumPlugOperator


class LeafRightUpLegRoll1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightUpLegRoll1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightUpLegRoll1RotateOrderEnumField(
    EnumField[LeafRightUpLegRoll1RotateOrderEnumAttrOperator, LeafRightUpLegRoll1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll1RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightUpLegRoll1RotateOrderEnumPlugOperator


class LeafRightLegRoll1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightLegRoll1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightLegRoll1RotateOrderEnumField(
    EnumField[LeafRightLegRoll1RotateOrderEnumAttrOperator, LeafRightLegRoll1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll1RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightLegRoll1RotateOrderEnumPlugOperator


class LeafLeftArmRoll1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftArmRoll1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftArmRoll1RotateOrderEnumField(
    EnumField[LeafLeftArmRoll1RotateOrderEnumAttrOperator, LeafLeftArmRoll1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll1RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftArmRoll1RotateOrderEnumPlugOperator


class LeafLeftForeArmRoll1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftForeArmRoll1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftForeArmRoll1RotateOrderEnumField(
    EnumField[LeafLeftForeArmRoll1RotateOrderEnumAttrOperator, LeafLeftForeArmRoll1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll1RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll1RotateOrderEnumPlugOperator


class LeafRightArmRoll1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightArmRoll1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightArmRoll1RotateOrderEnumField(
    EnumField[LeafRightArmRoll1RotateOrderEnumAttrOperator, LeafRightArmRoll1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll1RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightArmRoll1RotateOrderEnumPlugOperator


class LeafRightForeArmRoll1RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightForeArmRoll1RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightForeArmRoll1RotateOrderEnumField(
    EnumField[LeafRightForeArmRoll1RotateOrderEnumAttrOperator, LeafRightForeArmRoll1RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll1RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightForeArmRoll1RotateOrderEnumPlugOperator


class LeafLeftUpLegRoll2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftUpLegRoll2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftUpLegRoll2RotateOrderEnumField(
    EnumField[LeafLeftUpLegRoll2RotateOrderEnumAttrOperator, LeafLeftUpLegRoll2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll2RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll2RotateOrderEnumPlugOperator


class LeafLeftLegRoll2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftLegRoll2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftLegRoll2RotateOrderEnumField(
    EnumField[LeafLeftLegRoll2RotateOrderEnumAttrOperator, LeafLeftLegRoll2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll2RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftLegRoll2RotateOrderEnumPlugOperator


class LeafRightUpLegRoll2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightUpLegRoll2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightUpLegRoll2RotateOrderEnumField(
    EnumField[LeafRightUpLegRoll2RotateOrderEnumAttrOperator, LeafRightUpLegRoll2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll2RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightUpLegRoll2RotateOrderEnumPlugOperator


class LeafRightLegRoll2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightLegRoll2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightLegRoll2RotateOrderEnumField(
    EnumField[LeafRightLegRoll2RotateOrderEnumAttrOperator, LeafRightLegRoll2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll2RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightLegRoll2RotateOrderEnumPlugOperator


class LeafLeftArmRoll2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftArmRoll2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftArmRoll2RotateOrderEnumField(
    EnumField[LeafLeftArmRoll2RotateOrderEnumAttrOperator, LeafLeftArmRoll2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll2RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftArmRoll2RotateOrderEnumPlugOperator


class LeafLeftForeArmRoll2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftForeArmRoll2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftForeArmRoll2RotateOrderEnumField(
    EnumField[LeafLeftForeArmRoll2RotateOrderEnumAttrOperator, LeafLeftForeArmRoll2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll2RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll2RotateOrderEnumPlugOperator


class LeafRightArmRoll2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightArmRoll2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightArmRoll2RotateOrderEnumField(
    EnumField[LeafRightArmRoll2RotateOrderEnumAttrOperator, LeafRightArmRoll2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll2RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightArmRoll2RotateOrderEnumPlugOperator


class LeafRightForeArmRoll2RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightForeArmRoll2RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightForeArmRoll2RotateOrderEnumField(
    EnumField[LeafRightForeArmRoll2RotateOrderEnumAttrOperator, LeafRightForeArmRoll2RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll2RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightForeArmRoll2RotateOrderEnumPlugOperator


class LeafLeftUpLegRoll3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftUpLegRoll3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftUpLegRoll3RotateOrderEnumField(
    EnumField[LeafLeftUpLegRoll3RotateOrderEnumAttrOperator, LeafLeftUpLegRoll3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll3RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll3RotateOrderEnumPlugOperator


class LeafLeftLegRoll3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftLegRoll3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftLegRoll3RotateOrderEnumField(
    EnumField[LeafLeftLegRoll3RotateOrderEnumAttrOperator, LeafLeftLegRoll3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll3RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftLegRoll3RotateOrderEnumPlugOperator


class LeafRightUpLegRoll3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightUpLegRoll3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightUpLegRoll3RotateOrderEnumField(
    EnumField[LeafRightUpLegRoll3RotateOrderEnumAttrOperator, LeafRightUpLegRoll3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll3RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightUpLegRoll3RotateOrderEnumPlugOperator


class LeafRightLegRoll3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightLegRoll3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightLegRoll3RotateOrderEnumField(
    EnumField[LeafRightLegRoll3RotateOrderEnumAttrOperator, LeafRightLegRoll3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll3RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightLegRoll3RotateOrderEnumPlugOperator


class LeafLeftArmRoll3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftArmRoll3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftArmRoll3RotateOrderEnumField(
    EnumField[LeafLeftArmRoll3RotateOrderEnumAttrOperator, LeafLeftArmRoll3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll3RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftArmRoll3RotateOrderEnumPlugOperator


class LeafLeftForeArmRoll3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftForeArmRoll3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftForeArmRoll3RotateOrderEnumField(
    EnumField[LeafLeftForeArmRoll3RotateOrderEnumAttrOperator, LeafLeftForeArmRoll3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll3RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll3RotateOrderEnumPlugOperator


class LeafRightArmRoll3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightArmRoll3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightArmRoll3RotateOrderEnumField(
    EnumField[LeafRightArmRoll3RotateOrderEnumAttrOperator, LeafRightArmRoll3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll3RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightArmRoll3RotateOrderEnumPlugOperator


class LeafRightForeArmRoll3RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightForeArmRoll3RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightForeArmRoll3RotateOrderEnumField(
    EnumField[LeafRightForeArmRoll3RotateOrderEnumAttrOperator, LeafRightForeArmRoll3RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll3RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightForeArmRoll3RotateOrderEnumPlugOperator


class LeafLeftUpLegRoll4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftUpLegRoll4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftUpLegRoll4RotateOrderEnumField(
    EnumField[LeafLeftUpLegRoll4RotateOrderEnumAttrOperator, LeafLeftUpLegRoll4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll4RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll4RotateOrderEnumPlugOperator


class LeafLeftLegRoll4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftLegRoll4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftLegRoll4RotateOrderEnumField(
    EnumField[LeafLeftLegRoll4RotateOrderEnumAttrOperator, LeafLeftLegRoll4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll4RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftLegRoll4RotateOrderEnumPlugOperator


class LeafRightUpLegRoll4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightUpLegRoll4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightUpLegRoll4RotateOrderEnumField(
    EnumField[LeafRightUpLegRoll4RotateOrderEnumAttrOperator, LeafRightUpLegRoll4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll4RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightUpLegRoll4RotateOrderEnumPlugOperator


class LeafRightLegRoll4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightLegRoll4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightLegRoll4RotateOrderEnumField(
    EnumField[LeafRightLegRoll4RotateOrderEnumAttrOperator, LeafRightLegRoll4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll4RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightLegRoll4RotateOrderEnumPlugOperator


class LeafLeftArmRoll4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftArmRoll4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftArmRoll4RotateOrderEnumField(
    EnumField[LeafLeftArmRoll4RotateOrderEnumAttrOperator, LeafLeftArmRoll4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll4RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftArmRoll4RotateOrderEnumPlugOperator


class LeafLeftForeArmRoll4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftForeArmRoll4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftForeArmRoll4RotateOrderEnumField(
    EnumField[LeafLeftForeArmRoll4RotateOrderEnumAttrOperator, LeafLeftForeArmRoll4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll4RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll4RotateOrderEnumPlugOperator


class LeafRightArmRoll4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightArmRoll4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightArmRoll4RotateOrderEnumField(
    EnumField[LeafRightArmRoll4RotateOrderEnumAttrOperator, LeafRightArmRoll4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll4RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightArmRoll4RotateOrderEnumPlugOperator


class LeafRightForeArmRoll4RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightForeArmRoll4RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightForeArmRoll4RotateOrderEnumField(
    EnumField[LeafRightForeArmRoll4RotateOrderEnumAttrOperator, LeafRightForeArmRoll4RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll4RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightForeArmRoll4RotateOrderEnumPlugOperator


class LeafLeftUpLegRoll5RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftUpLegRoll5RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftUpLegRoll5RotateOrderEnumField(
    EnumField[LeafLeftUpLegRoll5RotateOrderEnumAttrOperator, LeafLeftUpLegRoll5RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll5RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll5RotateOrderEnumPlugOperator


class LeafLeftLegRoll5RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftLegRoll5RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftLegRoll5RotateOrderEnumField(
    EnumField[LeafLeftLegRoll5RotateOrderEnumAttrOperator, LeafLeftLegRoll5RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll5RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftLegRoll5RotateOrderEnumPlugOperator


class LeafRightUpLegRoll5RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightUpLegRoll5RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightUpLegRoll5RotateOrderEnumField(
    EnumField[LeafRightUpLegRoll5RotateOrderEnumAttrOperator, LeafRightUpLegRoll5RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll5RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightUpLegRoll5RotateOrderEnumPlugOperator


class LeafRightLegRoll5RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightLegRoll5RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightLegRoll5RotateOrderEnumField(
    EnumField[LeafRightLegRoll5RotateOrderEnumAttrOperator, LeafRightLegRoll5RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll5RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightLegRoll5RotateOrderEnumPlugOperator


class LeafLeftArmRoll5RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftArmRoll5RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftArmRoll5RotateOrderEnumField(
    EnumField[LeafLeftArmRoll5RotateOrderEnumAttrOperator, LeafLeftArmRoll5RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll5RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftArmRoll5RotateOrderEnumPlugOperator


class LeafLeftForeArmRoll5RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafLeftForeArmRoll5RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafLeftForeArmRoll5RotateOrderEnumField(
    EnumField[LeafLeftForeArmRoll5RotateOrderEnumAttrOperator, LeafLeftForeArmRoll5RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll5RotateOrderEnumAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll5RotateOrderEnumPlugOperator


class LeafRightArmRoll5RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightArmRoll5RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightArmRoll5RotateOrderEnumField(
    EnumField[LeafRightArmRoll5RotateOrderEnumAttrOperator, LeafRightArmRoll5RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll5RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightArmRoll5RotateOrderEnumPlugOperator


class LeafRightForeArmRoll5RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10


class LeafRightForeArmRoll5RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 2
    YZX = 4
    YXZ = 6
    ZXY = 8
    ZYX = 10

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YZX: "yzx",
        YXZ: "yxz",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class LeafRightForeArmRoll5RotateOrderEnumField(
    EnumField[LeafRightForeArmRoll5RotateOrderEnumAttrOperator, LeafRightForeArmRoll5RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll5RotateOrderEnumAttrOperator
    PLUG_CLS = LeafRightForeArmRoll5RotateOrderEnumPlugOperator


class HIKCharacterNode(DG):
    __slots__ = ()

    NODE_TYPE = "HIKCharacterNode"

    OutputCharacterDefinition = TypedField()

    propertyState = MessageField()

    SkeletonGenerator = MessageField()

    InputCharacterizationLock = BoolField(default_value=False)

    leftKneeInverted = BoolField(default_value=False)

    rightKneeInverted = BoolField(default_value=False)

    leftElbowInverted = BoolField(default_value=False)

    rightElbowInverted = BoolField(default_value=False)

    Reference = MessageField()

    ReferenceT = ReferenceTField(default_value=(0.0, 0.0, 0.0))
    ReferenceTx = ReferenceT.ReferenceTx
    ReferenceTy = ReferenceT.ReferenceTy
    ReferenceTz = ReferenceT.ReferenceTz

    ReferenceR = ReferenceRField(default_value=(0.0, 0.0, 0.0))
    ReferenceRx = ReferenceR.ReferenceRx
    ReferenceRy = ReferenceR.ReferenceRy
    ReferenceRz = ReferenceR.ReferenceRz

    ReferenceS = ReferenceSField(default_value=(1.0, 1.0, 1.0))
    ReferenceSx = ReferenceS.ReferenceSx
    ReferenceSy = ReferenceS.ReferenceSy
    ReferenceSz = ReferenceS.ReferenceSz

    ReferenceRotateOrder = ReferenceRotateOrderEnumField(default_value=0)

    ReferenceRotateAxis = ReferenceRotateAxisField(default_value=(0.0, 0.0, 0.0))
    ReferenceRotateAxisx = ReferenceRotateAxis.ReferenceRotateAxisx
    ReferenceRotateAxisy = ReferenceRotateAxis.ReferenceRotateAxisy
    ReferenceRotateAxisz = ReferenceRotateAxis.ReferenceRotateAxisz

    ReferenceJointOrient = ReferenceJointOrientField(default_value=(0.0, 0.0, 0.0))
    ReferenceJointOrientx = ReferenceJointOrient.ReferenceJointOrientx
    ReferenceJointOrienty = ReferenceJointOrient.ReferenceJointOrienty
    ReferenceJointOrientz = ReferenceJointOrient.ReferenceJointOrientz

    ReferenceMinRLimit = ReferenceMinRLimitField(default_value=(0.0, 0.0, 0.0))
    ReferenceMinRLimitx = ReferenceMinRLimit.ReferenceMinRLimitx
    ReferenceMinRLimity = ReferenceMinRLimit.ReferenceMinRLimity
    ReferenceMinRLimitz = ReferenceMinRLimit.ReferenceMinRLimitz

    ReferenceMaxRLimit = ReferenceMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    ReferenceMaxRLimitx = ReferenceMaxRLimit.ReferenceMaxRLimitx
    ReferenceMaxRLimity = ReferenceMaxRLimit.ReferenceMaxRLimity
    ReferenceMaxRLimitz = ReferenceMaxRLimit.ReferenceMaxRLimitz

    ReferenceMinRLimitEnablex = BoolField(default_value=False)

    ReferenceMinRLimitEnabley = BoolField(default_value=False)

    ReferenceMinRLimitEnablez = BoolField(default_value=False)

    ReferenceMaxRLimitEnablex = BoolField(default_value=False)

    ReferenceMaxRLimitEnabley = BoolField(default_value=False)

    ReferenceMaxRLimitEnablez = BoolField(default_value=False)

    Hips = MessageField()

    HipsT = HipsTField(default_value=(0.0, 0.0, 0.0))
    HipsTx = HipsT.HipsTx
    HipsTy = HipsT.HipsTy
    HipsTz = HipsT.HipsTz

    HipsR = HipsRField(default_value=(0.0, 0.0, 0.0))
    HipsRx = HipsR.HipsRx
    HipsRy = HipsR.HipsRy
    HipsRz = HipsR.HipsRz

    HipsS = HipsSField(default_value=(1.0, 1.0, 1.0))
    HipsSx = HipsS.HipsSx
    HipsSy = HipsS.HipsSy
    HipsSz = HipsS.HipsSz

    HipsRotateOrder = HipsRotateOrderEnumField(default_value=0)

    HipsRotateAxis = HipsRotateAxisField(default_value=(0.0, 0.0, 0.0))
    HipsRotateAxisx = HipsRotateAxis.HipsRotateAxisx
    HipsRotateAxisy = HipsRotateAxis.HipsRotateAxisy
    HipsRotateAxisz = HipsRotateAxis.HipsRotateAxisz

    HipsJointOrient = HipsJointOrientField(default_value=(0.0, 0.0, 0.0))
    HipsJointOrientx = HipsJointOrient.HipsJointOrientx
    HipsJointOrienty = HipsJointOrient.HipsJointOrienty
    HipsJointOrientz = HipsJointOrient.HipsJointOrientz

    HipsMinRLimit = HipsMinRLimitField(default_value=(0.0, 0.0, 0.0))
    HipsMinRLimitx = HipsMinRLimit.HipsMinRLimitx
    HipsMinRLimity = HipsMinRLimit.HipsMinRLimity
    HipsMinRLimitz = HipsMinRLimit.HipsMinRLimitz

    HipsMaxRLimit = HipsMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    HipsMaxRLimitx = HipsMaxRLimit.HipsMaxRLimitx
    HipsMaxRLimity = HipsMaxRLimit.HipsMaxRLimity
    HipsMaxRLimitz = HipsMaxRLimit.HipsMaxRLimitz

    HipsMinRLimitEnablex = BoolField(default_value=False)

    HipsMinRLimitEnabley = BoolField(default_value=False)

    HipsMinRLimitEnablez = BoolField(default_value=False)

    HipsMaxRLimitEnablex = BoolField(default_value=False)

    HipsMaxRLimitEnabley = BoolField(default_value=False)

    HipsMaxRLimitEnablez = BoolField(default_value=False)

    LeftUpLeg = MessageField()

    LeftUpLegT = LeftUpLegTField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegTx = LeftUpLegT.LeftUpLegTx
    LeftUpLegTy = LeftUpLegT.LeftUpLegTy
    LeftUpLegTz = LeftUpLegT.LeftUpLegTz

    LeftUpLegR = LeftUpLegRField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegRx = LeftUpLegR.LeftUpLegRx
    LeftUpLegRy = LeftUpLegR.LeftUpLegRy
    LeftUpLegRz = LeftUpLegR.LeftUpLegRz

    LeftUpLegS = LeftUpLegSField(default_value=(1.0, 1.0, 1.0))
    LeftUpLegSx = LeftUpLegS.LeftUpLegSx
    LeftUpLegSy = LeftUpLegS.LeftUpLegSy
    LeftUpLegSz = LeftUpLegS.LeftUpLegSz

    LeftUpLegRotateOrder = LeftUpLegRotateOrderEnumField(default_value=0)

    LeftUpLegRotateAxis = LeftUpLegRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegRotateAxisx = LeftUpLegRotateAxis.LeftUpLegRotateAxisx
    LeftUpLegRotateAxisy = LeftUpLegRotateAxis.LeftUpLegRotateAxisy
    LeftUpLegRotateAxisz = LeftUpLegRotateAxis.LeftUpLegRotateAxisz

    LeftUpLegJointOrient = LeftUpLegJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegJointOrientx = LeftUpLegJointOrient.LeftUpLegJointOrientx
    LeftUpLegJointOrienty = LeftUpLegJointOrient.LeftUpLegJointOrienty
    LeftUpLegJointOrientz = LeftUpLegJointOrient.LeftUpLegJointOrientz

    LeftUpLegMinRLimit = LeftUpLegMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegMinRLimitx = LeftUpLegMinRLimit.LeftUpLegMinRLimitx
    LeftUpLegMinRLimity = LeftUpLegMinRLimit.LeftUpLegMinRLimity
    LeftUpLegMinRLimitz = LeftUpLegMinRLimit.LeftUpLegMinRLimitz

    LeftUpLegMaxRLimit = LeftUpLegMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegMaxRLimitx = LeftUpLegMaxRLimit.LeftUpLegMaxRLimitx
    LeftUpLegMaxRLimity = LeftUpLegMaxRLimit.LeftUpLegMaxRLimity
    LeftUpLegMaxRLimitz = LeftUpLegMaxRLimit.LeftUpLegMaxRLimitz

    LeftUpLegMinRLimitEnablex = BoolField(default_value=False)

    LeftUpLegMinRLimitEnabley = BoolField(default_value=False)

    LeftUpLegMinRLimitEnablez = BoolField(default_value=False)

    LeftUpLegMaxRLimitEnablex = BoolField(default_value=False)

    LeftUpLegMaxRLimitEnabley = BoolField(default_value=False)

    LeftUpLegMaxRLimitEnablez = BoolField(default_value=False)

    LeftLeg = MessageField()

    LeftLegT = LeftLegTField(default_value=(0.0, 0.0, 0.0))
    LeftLegTx = LeftLegT.LeftLegTx
    LeftLegTy = LeftLegT.LeftLegTy
    LeftLegTz = LeftLegT.LeftLegTz

    LeftLegR = LeftLegRField(default_value=(0.0, 0.0, 0.0))
    LeftLegRx = LeftLegR.LeftLegRx
    LeftLegRy = LeftLegR.LeftLegRy
    LeftLegRz = LeftLegR.LeftLegRz

    LeftLegS = LeftLegSField(default_value=(1.0, 1.0, 1.0))
    LeftLegSx = LeftLegS.LeftLegSx
    LeftLegSy = LeftLegS.LeftLegSy
    LeftLegSz = LeftLegS.LeftLegSz

    LeftLegRotateOrder = LeftLegRotateOrderEnumField(default_value=0)

    LeftLegRotateAxis = LeftLegRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftLegRotateAxisx = LeftLegRotateAxis.LeftLegRotateAxisx
    LeftLegRotateAxisy = LeftLegRotateAxis.LeftLegRotateAxisy
    LeftLegRotateAxisz = LeftLegRotateAxis.LeftLegRotateAxisz

    LeftLegJointOrient = LeftLegJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftLegJointOrientx = LeftLegJointOrient.LeftLegJointOrientx
    LeftLegJointOrienty = LeftLegJointOrient.LeftLegJointOrienty
    LeftLegJointOrientz = LeftLegJointOrient.LeftLegJointOrientz

    LeftLegMinRLimit = LeftLegMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftLegMinRLimitx = LeftLegMinRLimit.LeftLegMinRLimitx
    LeftLegMinRLimity = LeftLegMinRLimit.LeftLegMinRLimity
    LeftLegMinRLimitz = LeftLegMinRLimit.LeftLegMinRLimitz

    LeftLegMaxRLimit = LeftLegMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftLegMaxRLimitx = LeftLegMaxRLimit.LeftLegMaxRLimitx
    LeftLegMaxRLimity = LeftLegMaxRLimit.LeftLegMaxRLimity
    LeftLegMaxRLimitz = LeftLegMaxRLimit.LeftLegMaxRLimitz

    LeftLegMinRLimitEnablex = BoolField(default_value=False)

    LeftLegMinRLimitEnabley = BoolField(default_value=False)

    LeftLegMinRLimitEnablez = BoolField(default_value=False)

    LeftLegMaxRLimitEnablex = BoolField(default_value=False)

    LeftLegMaxRLimitEnabley = BoolField(default_value=False)

    LeftLegMaxRLimitEnablez = BoolField(default_value=False)

    LeftFoot = MessageField()

    LeftFootT = LeftFootTField(default_value=(0.0, 0.0, 0.0))
    LeftFootTx = LeftFootT.LeftFootTx
    LeftFootTy = LeftFootT.LeftFootTy
    LeftFootTz = LeftFootT.LeftFootTz

    LeftFootR = LeftFootRField(default_value=(0.0, 0.0, 0.0))
    LeftFootRx = LeftFootR.LeftFootRx
    LeftFootRy = LeftFootR.LeftFootRy
    LeftFootRz = LeftFootR.LeftFootRz

    LeftFootS = LeftFootSField(default_value=(1.0, 1.0, 1.0))
    LeftFootSx = LeftFootS.LeftFootSx
    LeftFootSy = LeftFootS.LeftFootSy
    LeftFootSz = LeftFootS.LeftFootSz

    LeftFootRotateOrder = LeftFootRotateOrderEnumField(default_value=0)

    LeftFootRotateAxis = LeftFootRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootRotateAxisx = LeftFootRotateAxis.LeftFootRotateAxisx
    LeftFootRotateAxisy = LeftFootRotateAxis.LeftFootRotateAxisy
    LeftFootRotateAxisz = LeftFootRotateAxis.LeftFootRotateAxisz

    LeftFootJointOrient = LeftFootJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootJointOrientx = LeftFootJointOrient.LeftFootJointOrientx
    LeftFootJointOrienty = LeftFootJointOrient.LeftFootJointOrienty
    LeftFootJointOrientz = LeftFootJointOrient.LeftFootJointOrientz

    LeftFootMinRLimit = LeftFootMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootMinRLimitx = LeftFootMinRLimit.LeftFootMinRLimitx
    LeftFootMinRLimity = LeftFootMinRLimit.LeftFootMinRLimity
    LeftFootMinRLimitz = LeftFootMinRLimit.LeftFootMinRLimitz

    LeftFootMaxRLimit = LeftFootMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootMaxRLimitx = LeftFootMaxRLimit.LeftFootMaxRLimitx
    LeftFootMaxRLimity = LeftFootMaxRLimit.LeftFootMaxRLimity
    LeftFootMaxRLimitz = LeftFootMaxRLimit.LeftFootMaxRLimitz

    LeftFootMinRLimitEnablex = BoolField(default_value=False)

    LeftFootMinRLimitEnabley = BoolField(default_value=False)

    LeftFootMinRLimitEnablez = BoolField(default_value=False)

    LeftFootMaxRLimitEnablex = BoolField(default_value=False)

    LeftFootMaxRLimitEnabley = BoolField(default_value=False)

    LeftFootMaxRLimitEnablez = BoolField(default_value=False)

    RightUpLeg = MessageField()

    RightUpLegT = RightUpLegTField(default_value=(0.0, 0.0, 0.0))
    RightUpLegTx = RightUpLegT.RightUpLegTx
    RightUpLegTy = RightUpLegT.RightUpLegTy
    RightUpLegTz = RightUpLegT.RightUpLegTz

    RightUpLegR = RightUpLegRField(default_value=(0.0, 0.0, 0.0))
    RightUpLegRx = RightUpLegR.RightUpLegRx
    RightUpLegRy = RightUpLegR.RightUpLegRy
    RightUpLegRz = RightUpLegR.RightUpLegRz

    RightUpLegS = RightUpLegSField(default_value=(1.0, 1.0, 1.0))
    RightUpLegSx = RightUpLegS.RightUpLegSx
    RightUpLegSy = RightUpLegS.RightUpLegSy
    RightUpLegSz = RightUpLegS.RightUpLegSz

    RightUpLegRotateOrder = RightUpLegRotateOrderEnumField(default_value=0)

    RightUpLegRotateAxis = RightUpLegRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightUpLegRotateAxisx = RightUpLegRotateAxis.RightUpLegRotateAxisx
    RightUpLegRotateAxisy = RightUpLegRotateAxis.RightUpLegRotateAxisy
    RightUpLegRotateAxisz = RightUpLegRotateAxis.RightUpLegRotateAxisz

    RightUpLegJointOrient = RightUpLegJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightUpLegJointOrientx = RightUpLegJointOrient.RightUpLegJointOrientx
    RightUpLegJointOrienty = RightUpLegJointOrient.RightUpLegJointOrienty
    RightUpLegJointOrientz = RightUpLegJointOrient.RightUpLegJointOrientz

    RightUpLegMinRLimit = RightUpLegMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightUpLegMinRLimitx = RightUpLegMinRLimit.RightUpLegMinRLimitx
    RightUpLegMinRLimity = RightUpLegMinRLimit.RightUpLegMinRLimity
    RightUpLegMinRLimitz = RightUpLegMinRLimit.RightUpLegMinRLimitz

    RightUpLegMaxRLimit = RightUpLegMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightUpLegMaxRLimitx = RightUpLegMaxRLimit.RightUpLegMaxRLimitx
    RightUpLegMaxRLimity = RightUpLegMaxRLimit.RightUpLegMaxRLimity
    RightUpLegMaxRLimitz = RightUpLegMaxRLimit.RightUpLegMaxRLimitz

    RightUpLegMinRLimitEnablex = BoolField(default_value=False)

    RightUpLegMinRLimitEnabley = BoolField(default_value=False)

    RightUpLegMinRLimitEnablez = BoolField(default_value=False)

    RightUpLegMaxRLimitEnablex = BoolField(default_value=False)

    RightUpLegMaxRLimitEnabley = BoolField(default_value=False)

    RightUpLegMaxRLimitEnablez = BoolField(default_value=False)

    RightLeg = MessageField()

    RightLegT = RightLegTField(default_value=(0.0, 0.0, 0.0))
    RightLegTx = RightLegT.RightLegTx
    RightLegTy = RightLegT.RightLegTy
    RightLegTz = RightLegT.RightLegTz

    RightLegR = RightLegRField(default_value=(0.0, 0.0, 0.0))
    RightLegRx = RightLegR.RightLegRx
    RightLegRy = RightLegR.RightLegRy
    RightLegRz = RightLegR.RightLegRz

    RightLegS = RightLegSField(default_value=(1.0, 1.0, 1.0))
    RightLegSx = RightLegS.RightLegSx
    RightLegSy = RightLegS.RightLegSy
    RightLegSz = RightLegS.RightLegSz

    RightLegRotateOrder = RightLegRotateOrderEnumField(default_value=0)

    RightLegRotateAxis = RightLegRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightLegRotateAxisx = RightLegRotateAxis.RightLegRotateAxisx
    RightLegRotateAxisy = RightLegRotateAxis.RightLegRotateAxisy
    RightLegRotateAxisz = RightLegRotateAxis.RightLegRotateAxisz

    RightLegJointOrient = RightLegJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightLegJointOrientx = RightLegJointOrient.RightLegJointOrientx
    RightLegJointOrienty = RightLegJointOrient.RightLegJointOrienty
    RightLegJointOrientz = RightLegJointOrient.RightLegJointOrientz

    RightLegMinRLimit = RightLegMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightLegMinRLimitx = RightLegMinRLimit.RightLegMinRLimitx
    RightLegMinRLimity = RightLegMinRLimit.RightLegMinRLimity
    RightLegMinRLimitz = RightLegMinRLimit.RightLegMinRLimitz

    RightLegMaxRLimit = RightLegMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightLegMaxRLimitx = RightLegMaxRLimit.RightLegMaxRLimitx
    RightLegMaxRLimity = RightLegMaxRLimit.RightLegMaxRLimity
    RightLegMaxRLimitz = RightLegMaxRLimit.RightLegMaxRLimitz

    RightLegMinRLimitEnablex = BoolField(default_value=False)

    RightLegMinRLimitEnabley = BoolField(default_value=False)

    RightLegMinRLimitEnablez = BoolField(default_value=False)

    RightLegMaxRLimitEnablex = BoolField(default_value=False)

    RightLegMaxRLimitEnabley = BoolField(default_value=False)

    RightLegMaxRLimitEnablez = BoolField(default_value=False)

    RightFoot = MessageField()

    RightFootT = RightFootTField(default_value=(0.0, 0.0, 0.0))
    RightFootTx = RightFootT.RightFootTx
    RightFootTy = RightFootT.RightFootTy
    RightFootTz = RightFootT.RightFootTz

    RightFootR = RightFootRField(default_value=(0.0, 0.0, 0.0))
    RightFootRx = RightFootR.RightFootRx
    RightFootRy = RightFootR.RightFootRy
    RightFootRz = RightFootR.RightFootRz

    RightFootS = RightFootSField(default_value=(1.0, 1.0, 1.0))
    RightFootSx = RightFootS.RightFootSx
    RightFootSy = RightFootS.RightFootSy
    RightFootSz = RightFootS.RightFootSz

    RightFootRotateOrder = RightFootRotateOrderEnumField(default_value=0)

    RightFootRotateAxis = RightFootRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootRotateAxisx = RightFootRotateAxis.RightFootRotateAxisx
    RightFootRotateAxisy = RightFootRotateAxis.RightFootRotateAxisy
    RightFootRotateAxisz = RightFootRotateAxis.RightFootRotateAxisz

    RightFootJointOrient = RightFootJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootJointOrientx = RightFootJointOrient.RightFootJointOrientx
    RightFootJointOrienty = RightFootJointOrient.RightFootJointOrienty
    RightFootJointOrientz = RightFootJointOrient.RightFootJointOrientz

    RightFootMinRLimit = RightFootMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootMinRLimitx = RightFootMinRLimit.RightFootMinRLimitx
    RightFootMinRLimity = RightFootMinRLimit.RightFootMinRLimity
    RightFootMinRLimitz = RightFootMinRLimit.RightFootMinRLimitz

    RightFootMaxRLimit = RightFootMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootMaxRLimitx = RightFootMaxRLimit.RightFootMaxRLimitx
    RightFootMaxRLimity = RightFootMaxRLimit.RightFootMaxRLimity
    RightFootMaxRLimitz = RightFootMaxRLimit.RightFootMaxRLimitz

    RightFootMinRLimitEnablex = BoolField(default_value=False)

    RightFootMinRLimitEnabley = BoolField(default_value=False)

    RightFootMinRLimitEnablez = BoolField(default_value=False)

    RightFootMaxRLimitEnablex = BoolField(default_value=False)

    RightFootMaxRLimitEnabley = BoolField(default_value=False)

    RightFootMaxRLimitEnablez = BoolField(default_value=False)

    Spine = MessageField()

    SpineT = SpineTField(default_value=(0.0, 0.0, 0.0))
    SpineTx = SpineT.SpineTx
    SpineTy = SpineT.SpineTy
    SpineTz = SpineT.SpineTz

    SpineR = SpineRField(default_value=(0.0, 0.0, 0.0))
    SpineRx = SpineR.SpineRx
    SpineRy = SpineR.SpineRy
    SpineRz = SpineR.SpineRz

    SpineS = SpineSField(default_value=(1.0, 1.0, 1.0))
    SpineSx = SpineS.SpineSx
    SpineSy = SpineS.SpineSy
    SpineSz = SpineS.SpineSz

    SpineRotateOrder = SpineRotateOrderEnumField(default_value=0)

    SpineRotateAxis = SpineRotateAxisField(default_value=(0.0, 0.0, 0.0))
    SpineRotateAxisx = SpineRotateAxis.SpineRotateAxisx
    SpineRotateAxisy = SpineRotateAxis.SpineRotateAxisy
    SpineRotateAxisz = SpineRotateAxis.SpineRotateAxisz

    SpineJointOrient = SpineJointOrientField(default_value=(0.0, 0.0, 0.0))
    SpineJointOrientx = SpineJointOrient.SpineJointOrientx
    SpineJointOrienty = SpineJointOrient.SpineJointOrienty
    SpineJointOrientz = SpineJointOrient.SpineJointOrientz

    SpineMinRLimit = SpineMinRLimitField(default_value=(0.0, 0.0, 0.0))
    SpineMinRLimitx = SpineMinRLimit.SpineMinRLimitx
    SpineMinRLimity = SpineMinRLimit.SpineMinRLimity
    SpineMinRLimitz = SpineMinRLimit.SpineMinRLimitz

    SpineMaxRLimit = SpineMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    SpineMaxRLimitx = SpineMaxRLimit.SpineMaxRLimitx
    SpineMaxRLimity = SpineMaxRLimit.SpineMaxRLimity
    SpineMaxRLimitz = SpineMaxRLimit.SpineMaxRLimitz

    SpineMinRLimitEnablex = BoolField(default_value=False)

    SpineMinRLimitEnabley = BoolField(default_value=False)

    SpineMinRLimitEnablez = BoolField(default_value=False)

    SpineMaxRLimitEnablex = BoolField(default_value=False)

    SpineMaxRLimitEnabley = BoolField(default_value=False)

    SpineMaxRLimitEnablez = BoolField(default_value=False)

    LeftArm = MessageField()

    LeftArmT = LeftArmTField(default_value=(0.0, 0.0, 0.0))
    LeftArmTx = LeftArmT.LeftArmTx
    LeftArmTy = LeftArmT.LeftArmTy
    LeftArmTz = LeftArmT.LeftArmTz

    LeftArmR = LeftArmRField(default_value=(0.0, 0.0, 0.0))
    LeftArmRx = LeftArmR.LeftArmRx
    LeftArmRy = LeftArmR.LeftArmRy
    LeftArmRz = LeftArmR.LeftArmRz

    LeftArmS = LeftArmSField(default_value=(1.0, 1.0, 1.0))
    LeftArmSx = LeftArmS.LeftArmSx
    LeftArmSy = LeftArmS.LeftArmSy
    LeftArmSz = LeftArmS.LeftArmSz

    LeftArmRotateOrder = LeftArmRotateOrderEnumField(default_value=0)

    LeftArmRotateAxis = LeftArmRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftArmRotateAxisx = LeftArmRotateAxis.LeftArmRotateAxisx
    LeftArmRotateAxisy = LeftArmRotateAxis.LeftArmRotateAxisy
    LeftArmRotateAxisz = LeftArmRotateAxis.LeftArmRotateAxisz

    LeftArmJointOrient = LeftArmJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftArmJointOrientx = LeftArmJointOrient.LeftArmJointOrientx
    LeftArmJointOrienty = LeftArmJointOrient.LeftArmJointOrienty
    LeftArmJointOrientz = LeftArmJointOrient.LeftArmJointOrientz

    LeftArmMinRLimit = LeftArmMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftArmMinRLimitx = LeftArmMinRLimit.LeftArmMinRLimitx
    LeftArmMinRLimity = LeftArmMinRLimit.LeftArmMinRLimity
    LeftArmMinRLimitz = LeftArmMinRLimit.LeftArmMinRLimitz

    LeftArmMaxRLimit = LeftArmMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftArmMaxRLimitx = LeftArmMaxRLimit.LeftArmMaxRLimitx
    LeftArmMaxRLimity = LeftArmMaxRLimit.LeftArmMaxRLimity
    LeftArmMaxRLimitz = LeftArmMaxRLimit.LeftArmMaxRLimitz

    LeftArmMinRLimitEnablex = BoolField(default_value=False)

    LeftArmMinRLimitEnabley = BoolField(default_value=False)

    LeftArmMinRLimitEnablez = BoolField(default_value=False)

    LeftArmMaxRLimitEnablex = BoolField(default_value=False)

    LeftArmMaxRLimitEnabley = BoolField(default_value=False)

    LeftArmMaxRLimitEnablez = BoolField(default_value=False)

    LeftForeArm = MessageField()

    LeftForeArmT = LeftForeArmTField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmTx = LeftForeArmT.LeftForeArmTx
    LeftForeArmTy = LeftForeArmT.LeftForeArmTy
    LeftForeArmTz = LeftForeArmT.LeftForeArmTz

    LeftForeArmR = LeftForeArmRField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmRx = LeftForeArmR.LeftForeArmRx
    LeftForeArmRy = LeftForeArmR.LeftForeArmRy
    LeftForeArmRz = LeftForeArmR.LeftForeArmRz

    LeftForeArmS = LeftForeArmSField(default_value=(1.0, 1.0, 1.0))
    LeftForeArmSx = LeftForeArmS.LeftForeArmSx
    LeftForeArmSy = LeftForeArmS.LeftForeArmSy
    LeftForeArmSz = LeftForeArmS.LeftForeArmSz

    LeftForeArmRotateOrder = LeftForeArmRotateOrderEnumField(default_value=0)

    LeftForeArmRotateAxis = LeftForeArmRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmRotateAxisx = LeftForeArmRotateAxis.LeftForeArmRotateAxisx
    LeftForeArmRotateAxisy = LeftForeArmRotateAxis.LeftForeArmRotateAxisy
    LeftForeArmRotateAxisz = LeftForeArmRotateAxis.LeftForeArmRotateAxisz

    LeftForeArmJointOrient = LeftForeArmJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmJointOrientx = LeftForeArmJointOrient.LeftForeArmJointOrientx
    LeftForeArmJointOrienty = LeftForeArmJointOrient.LeftForeArmJointOrienty
    LeftForeArmJointOrientz = LeftForeArmJointOrient.LeftForeArmJointOrientz

    LeftForeArmMinRLimit = LeftForeArmMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmMinRLimitx = LeftForeArmMinRLimit.LeftForeArmMinRLimitx
    LeftForeArmMinRLimity = LeftForeArmMinRLimit.LeftForeArmMinRLimity
    LeftForeArmMinRLimitz = LeftForeArmMinRLimit.LeftForeArmMinRLimitz

    LeftForeArmMaxRLimit = LeftForeArmMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmMaxRLimitx = LeftForeArmMaxRLimit.LeftForeArmMaxRLimitx
    LeftForeArmMaxRLimity = LeftForeArmMaxRLimit.LeftForeArmMaxRLimity
    LeftForeArmMaxRLimitz = LeftForeArmMaxRLimit.LeftForeArmMaxRLimitz

    LeftForeArmMinRLimitEnablex = BoolField(default_value=False)

    LeftForeArmMinRLimitEnabley = BoolField(default_value=False)

    LeftForeArmMinRLimitEnablez = BoolField(default_value=False)

    LeftForeArmMaxRLimitEnablex = BoolField(default_value=False)

    LeftForeArmMaxRLimitEnabley = BoolField(default_value=False)

    LeftForeArmMaxRLimitEnablez = BoolField(default_value=False)

    LeftHand = MessageField()

    LeftHandT = LeftHandTField(default_value=(0.0, 0.0, 0.0))
    LeftHandTx = LeftHandT.LeftHandTx
    LeftHandTy = LeftHandT.LeftHandTy
    LeftHandTz = LeftHandT.LeftHandTz

    LeftHandR = LeftHandRField(default_value=(0.0, 0.0, 0.0))
    LeftHandRx = LeftHandR.LeftHandRx
    LeftHandRy = LeftHandR.LeftHandRy
    LeftHandRz = LeftHandR.LeftHandRz

    LeftHandS = LeftHandSField(default_value=(1.0, 1.0, 1.0))
    LeftHandSx = LeftHandS.LeftHandSx
    LeftHandSy = LeftHandS.LeftHandSy
    LeftHandSz = LeftHandS.LeftHandSz

    LeftHandRotateOrder = LeftHandRotateOrderEnumField(default_value=0)

    LeftHandRotateAxis = LeftHandRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandRotateAxisx = LeftHandRotateAxis.LeftHandRotateAxisx
    LeftHandRotateAxisy = LeftHandRotateAxis.LeftHandRotateAxisy
    LeftHandRotateAxisz = LeftHandRotateAxis.LeftHandRotateAxisz

    LeftHandJointOrient = LeftHandJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandJointOrientx = LeftHandJointOrient.LeftHandJointOrientx
    LeftHandJointOrienty = LeftHandJointOrient.LeftHandJointOrienty
    LeftHandJointOrientz = LeftHandJointOrient.LeftHandJointOrientz

    LeftHandMinRLimit = LeftHandMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandMinRLimitx = LeftHandMinRLimit.LeftHandMinRLimitx
    LeftHandMinRLimity = LeftHandMinRLimit.LeftHandMinRLimity
    LeftHandMinRLimitz = LeftHandMinRLimit.LeftHandMinRLimitz

    LeftHandMaxRLimit = LeftHandMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandMaxRLimitx = LeftHandMaxRLimit.LeftHandMaxRLimitx
    LeftHandMaxRLimity = LeftHandMaxRLimit.LeftHandMaxRLimity
    LeftHandMaxRLimitz = LeftHandMaxRLimit.LeftHandMaxRLimitz

    LeftHandMinRLimitEnablex = BoolField(default_value=False)

    LeftHandMinRLimitEnabley = BoolField(default_value=False)

    LeftHandMinRLimitEnablez = BoolField(default_value=False)

    LeftHandMaxRLimitEnablex = BoolField(default_value=False)

    LeftHandMaxRLimitEnabley = BoolField(default_value=False)

    LeftHandMaxRLimitEnablez = BoolField(default_value=False)

    RightArm = MessageField()

    RightArmT = RightArmTField(default_value=(0.0, 0.0, 0.0))
    RightArmTx = RightArmT.RightArmTx
    RightArmTy = RightArmT.RightArmTy
    RightArmTz = RightArmT.RightArmTz

    RightArmR = RightArmRField(default_value=(0.0, 0.0, 0.0))
    RightArmRx = RightArmR.RightArmRx
    RightArmRy = RightArmR.RightArmRy
    RightArmRz = RightArmR.RightArmRz

    RightArmS = RightArmSField(default_value=(1.0, 1.0, 1.0))
    RightArmSx = RightArmS.RightArmSx
    RightArmSy = RightArmS.RightArmSy
    RightArmSz = RightArmS.RightArmSz

    RightArmRotateOrder = RightArmRotateOrderEnumField(default_value=0)

    RightArmRotateAxis = RightArmRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightArmRotateAxisx = RightArmRotateAxis.RightArmRotateAxisx
    RightArmRotateAxisy = RightArmRotateAxis.RightArmRotateAxisy
    RightArmRotateAxisz = RightArmRotateAxis.RightArmRotateAxisz

    RightArmJointOrient = RightArmJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightArmJointOrientx = RightArmJointOrient.RightArmJointOrientx
    RightArmJointOrienty = RightArmJointOrient.RightArmJointOrienty
    RightArmJointOrientz = RightArmJointOrient.RightArmJointOrientz

    RightArmMinRLimit = RightArmMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightArmMinRLimitx = RightArmMinRLimit.RightArmMinRLimitx
    RightArmMinRLimity = RightArmMinRLimit.RightArmMinRLimity
    RightArmMinRLimitz = RightArmMinRLimit.RightArmMinRLimitz

    RightArmMaxRLimit = RightArmMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightArmMaxRLimitx = RightArmMaxRLimit.RightArmMaxRLimitx
    RightArmMaxRLimity = RightArmMaxRLimit.RightArmMaxRLimity
    RightArmMaxRLimitz = RightArmMaxRLimit.RightArmMaxRLimitz

    RightArmMinRLimitEnablex = BoolField(default_value=False)

    RightArmMinRLimitEnabley = BoolField(default_value=False)

    RightArmMinRLimitEnablez = BoolField(default_value=False)

    RightArmMaxRLimitEnablex = BoolField(default_value=False)

    RightArmMaxRLimitEnabley = BoolField(default_value=False)

    RightArmMaxRLimitEnablez = BoolField(default_value=False)

    RightForeArm = MessageField()

    RightForeArmT = RightForeArmTField(default_value=(0.0, 0.0, 0.0))
    RightForeArmTx = RightForeArmT.RightForeArmTx
    RightForeArmTy = RightForeArmT.RightForeArmTy
    RightForeArmTz = RightForeArmT.RightForeArmTz

    RightForeArmR = RightForeArmRField(default_value=(0.0, 0.0, 0.0))
    RightForeArmRx = RightForeArmR.RightForeArmRx
    RightForeArmRy = RightForeArmR.RightForeArmRy
    RightForeArmRz = RightForeArmR.RightForeArmRz

    RightForeArmS = RightForeArmSField(default_value=(1.0, 1.0, 1.0))
    RightForeArmSx = RightForeArmS.RightForeArmSx
    RightForeArmSy = RightForeArmS.RightForeArmSy
    RightForeArmSz = RightForeArmS.RightForeArmSz

    RightForeArmRotateOrder = RightForeArmRotateOrderEnumField(default_value=0)

    RightForeArmRotateAxis = RightForeArmRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightForeArmRotateAxisx = RightForeArmRotateAxis.RightForeArmRotateAxisx
    RightForeArmRotateAxisy = RightForeArmRotateAxis.RightForeArmRotateAxisy
    RightForeArmRotateAxisz = RightForeArmRotateAxis.RightForeArmRotateAxisz

    RightForeArmJointOrient = RightForeArmJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightForeArmJointOrientx = RightForeArmJointOrient.RightForeArmJointOrientx
    RightForeArmJointOrienty = RightForeArmJointOrient.RightForeArmJointOrienty
    RightForeArmJointOrientz = RightForeArmJointOrient.RightForeArmJointOrientz

    RightForeArmMinRLimit = RightForeArmMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightForeArmMinRLimitx = RightForeArmMinRLimit.RightForeArmMinRLimitx
    RightForeArmMinRLimity = RightForeArmMinRLimit.RightForeArmMinRLimity
    RightForeArmMinRLimitz = RightForeArmMinRLimit.RightForeArmMinRLimitz

    RightForeArmMaxRLimit = RightForeArmMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightForeArmMaxRLimitx = RightForeArmMaxRLimit.RightForeArmMaxRLimitx
    RightForeArmMaxRLimity = RightForeArmMaxRLimit.RightForeArmMaxRLimity
    RightForeArmMaxRLimitz = RightForeArmMaxRLimit.RightForeArmMaxRLimitz

    RightForeArmMinRLimitEnablex = BoolField(default_value=False)

    RightForeArmMinRLimitEnabley = BoolField(default_value=False)

    RightForeArmMinRLimitEnablez = BoolField(default_value=False)

    RightForeArmMaxRLimitEnablex = BoolField(default_value=False)

    RightForeArmMaxRLimitEnabley = BoolField(default_value=False)

    RightForeArmMaxRLimitEnablez = BoolField(default_value=False)

    RightHand = MessageField()

    RightHandT = RightHandTField(default_value=(0.0, 0.0, 0.0))
    RightHandTx = RightHandT.RightHandTx
    RightHandTy = RightHandT.RightHandTy
    RightHandTz = RightHandT.RightHandTz

    RightHandR = RightHandRField(default_value=(0.0, 0.0, 0.0))
    RightHandRx = RightHandR.RightHandRx
    RightHandRy = RightHandR.RightHandRy
    RightHandRz = RightHandR.RightHandRz

    RightHandS = RightHandSField(default_value=(1.0, 1.0, 1.0))
    RightHandSx = RightHandS.RightHandSx
    RightHandSy = RightHandS.RightHandSy
    RightHandSz = RightHandS.RightHandSz

    RightHandRotateOrder = RightHandRotateOrderEnumField(default_value=0)

    RightHandRotateAxis = RightHandRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandRotateAxisx = RightHandRotateAxis.RightHandRotateAxisx
    RightHandRotateAxisy = RightHandRotateAxis.RightHandRotateAxisy
    RightHandRotateAxisz = RightHandRotateAxis.RightHandRotateAxisz

    RightHandJointOrient = RightHandJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandJointOrientx = RightHandJointOrient.RightHandJointOrientx
    RightHandJointOrienty = RightHandJointOrient.RightHandJointOrienty
    RightHandJointOrientz = RightHandJointOrient.RightHandJointOrientz

    RightHandMinRLimit = RightHandMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandMinRLimitx = RightHandMinRLimit.RightHandMinRLimitx
    RightHandMinRLimity = RightHandMinRLimit.RightHandMinRLimity
    RightHandMinRLimitz = RightHandMinRLimit.RightHandMinRLimitz

    RightHandMaxRLimit = RightHandMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandMaxRLimitx = RightHandMaxRLimit.RightHandMaxRLimitx
    RightHandMaxRLimity = RightHandMaxRLimit.RightHandMaxRLimity
    RightHandMaxRLimitz = RightHandMaxRLimit.RightHandMaxRLimitz

    RightHandMinRLimitEnablex = BoolField(default_value=False)

    RightHandMinRLimitEnabley = BoolField(default_value=False)

    RightHandMinRLimitEnablez = BoolField(default_value=False)

    RightHandMaxRLimitEnablex = BoolField(default_value=False)

    RightHandMaxRLimitEnabley = BoolField(default_value=False)

    RightHandMaxRLimitEnablez = BoolField(default_value=False)

    Head = MessageField()

    HeadT = HeadTField(default_value=(0.0, 0.0, 0.0))
    HeadTx = HeadT.HeadTx
    HeadTy = HeadT.HeadTy
    HeadTz = HeadT.HeadTz

    HeadR = HeadRField(default_value=(0.0, 0.0, 0.0))
    HeadRx = HeadR.HeadRx
    HeadRy = HeadR.HeadRy
    HeadRz = HeadR.HeadRz

    HeadS = HeadSField(default_value=(1.0, 1.0, 1.0))
    HeadSx = HeadS.HeadSx
    HeadSy = HeadS.HeadSy
    HeadSz = HeadS.HeadSz

    HeadRotateOrder = HeadRotateOrderEnumField(default_value=0)

    HeadRotateAxis = HeadRotateAxisField(default_value=(0.0, 0.0, 0.0))
    HeadRotateAxisx = HeadRotateAxis.HeadRotateAxisx
    HeadRotateAxisy = HeadRotateAxis.HeadRotateAxisy
    HeadRotateAxisz = HeadRotateAxis.HeadRotateAxisz

    HeadJointOrient = HeadJointOrientField(default_value=(0.0, 0.0, 0.0))
    HeadJointOrientx = HeadJointOrient.HeadJointOrientx
    HeadJointOrienty = HeadJointOrient.HeadJointOrienty
    HeadJointOrientz = HeadJointOrient.HeadJointOrientz

    HeadMinRLimit = HeadMinRLimitField(default_value=(0.0, 0.0, 0.0))
    HeadMinRLimitx = HeadMinRLimit.HeadMinRLimitx
    HeadMinRLimity = HeadMinRLimit.HeadMinRLimity
    HeadMinRLimitz = HeadMinRLimit.HeadMinRLimitz

    HeadMaxRLimit = HeadMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    HeadMaxRLimitx = HeadMaxRLimit.HeadMaxRLimitx
    HeadMaxRLimity = HeadMaxRLimit.HeadMaxRLimity
    HeadMaxRLimitz = HeadMaxRLimit.HeadMaxRLimitz

    HeadMinRLimitEnablex = BoolField(default_value=False)

    HeadMinRLimitEnabley = BoolField(default_value=False)

    HeadMinRLimitEnablez = BoolField(default_value=False)

    HeadMaxRLimitEnablex = BoolField(default_value=False)

    HeadMaxRLimitEnabley = BoolField(default_value=False)

    HeadMaxRLimitEnablez = BoolField(default_value=False)

    LeftToeBase = MessageField()

    LeftToeBaseT = LeftToeBaseTField(default_value=(0.0, 0.0, 0.0))
    LeftToeBaseTx = LeftToeBaseT.LeftToeBaseTx
    LeftToeBaseTy = LeftToeBaseT.LeftToeBaseTy
    LeftToeBaseTz = LeftToeBaseT.LeftToeBaseTz

    LeftToeBaseR = LeftToeBaseRField(default_value=(0.0, 0.0, 0.0))
    LeftToeBaseRx = LeftToeBaseR.LeftToeBaseRx
    LeftToeBaseRy = LeftToeBaseR.LeftToeBaseRy
    LeftToeBaseRz = LeftToeBaseR.LeftToeBaseRz

    LeftToeBaseS = LeftToeBaseSField(default_value=(1.0, 1.0, 1.0))
    LeftToeBaseSx = LeftToeBaseS.LeftToeBaseSx
    LeftToeBaseSy = LeftToeBaseS.LeftToeBaseSy
    LeftToeBaseSz = LeftToeBaseS.LeftToeBaseSz

    LeftToeBaseRotateOrder = LeftToeBaseRotateOrderEnumField(default_value=0)

    LeftToeBaseRotateAxis = LeftToeBaseRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftToeBaseRotateAxisx = LeftToeBaseRotateAxis.LeftToeBaseRotateAxisx
    LeftToeBaseRotateAxisy = LeftToeBaseRotateAxis.LeftToeBaseRotateAxisy
    LeftToeBaseRotateAxisz = LeftToeBaseRotateAxis.LeftToeBaseRotateAxisz

    LeftToeBaseJointOrient = LeftToeBaseJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftToeBaseJointOrientx = LeftToeBaseJointOrient.LeftToeBaseJointOrientx
    LeftToeBaseJointOrienty = LeftToeBaseJointOrient.LeftToeBaseJointOrienty
    LeftToeBaseJointOrientz = LeftToeBaseJointOrient.LeftToeBaseJointOrientz

    LeftToeBaseMinRLimit = LeftToeBaseMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftToeBaseMinRLimitx = LeftToeBaseMinRLimit.LeftToeBaseMinRLimitx
    LeftToeBaseMinRLimity = LeftToeBaseMinRLimit.LeftToeBaseMinRLimity
    LeftToeBaseMinRLimitz = LeftToeBaseMinRLimit.LeftToeBaseMinRLimitz

    LeftToeBaseMaxRLimit = LeftToeBaseMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftToeBaseMaxRLimitx = LeftToeBaseMaxRLimit.LeftToeBaseMaxRLimitx
    LeftToeBaseMaxRLimity = LeftToeBaseMaxRLimit.LeftToeBaseMaxRLimity
    LeftToeBaseMaxRLimitz = LeftToeBaseMaxRLimit.LeftToeBaseMaxRLimitz

    LeftToeBaseMinRLimitEnablex = BoolField(default_value=False)

    LeftToeBaseMinRLimitEnabley = BoolField(default_value=False)

    LeftToeBaseMinRLimitEnablez = BoolField(default_value=False)

    LeftToeBaseMaxRLimitEnablex = BoolField(default_value=False)

    LeftToeBaseMaxRLimitEnabley = BoolField(default_value=False)

    LeftToeBaseMaxRLimitEnablez = BoolField(default_value=False)

    RightToeBase = MessageField()

    RightToeBaseT = RightToeBaseTField(default_value=(0.0, 0.0, 0.0))
    RightToeBaseTx = RightToeBaseT.RightToeBaseTx
    RightToeBaseTy = RightToeBaseT.RightToeBaseTy
    RightToeBaseTz = RightToeBaseT.RightToeBaseTz

    RightToeBaseR = RightToeBaseRField(default_value=(0.0, 0.0, 0.0))
    RightToeBaseRx = RightToeBaseR.RightToeBaseRx
    RightToeBaseRy = RightToeBaseR.RightToeBaseRy
    RightToeBaseRz = RightToeBaseR.RightToeBaseRz

    RightToeBaseS = RightToeBaseSField(default_value=(1.0, 1.0, 1.0))
    RightToeBaseSx = RightToeBaseS.RightToeBaseSx
    RightToeBaseSy = RightToeBaseS.RightToeBaseSy
    RightToeBaseSz = RightToeBaseS.RightToeBaseSz

    RightToeBaseRotateOrder = RightToeBaseRotateOrderEnumField(default_value=0)

    RightToeBaseRotateAxis = RightToeBaseRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightToeBaseRotateAxisx = RightToeBaseRotateAxis.RightToeBaseRotateAxisx
    RightToeBaseRotateAxisy = RightToeBaseRotateAxis.RightToeBaseRotateAxisy
    RightToeBaseRotateAxisz = RightToeBaseRotateAxis.RightToeBaseRotateAxisz

    RightToeBaseJointOrient = RightToeBaseJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightToeBaseJointOrientx = RightToeBaseJointOrient.RightToeBaseJointOrientx
    RightToeBaseJointOrienty = RightToeBaseJointOrient.RightToeBaseJointOrienty
    RightToeBaseJointOrientz = RightToeBaseJointOrient.RightToeBaseJointOrientz

    RightToeBaseMinRLimit = RightToeBaseMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightToeBaseMinRLimitx = RightToeBaseMinRLimit.RightToeBaseMinRLimitx
    RightToeBaseMinRLimity = RightToeBaseMinRLimit.RightToeBaseMinRLimity
    RightToeBaseMinRLimitz = RightToeBaseMinRLimit.RightToeBaseMinRLimitz

    RightToeBaseMaxRLimit = RightToeBaseMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightToeBaseMaxRLimitx = RightToeBaseMaxRLimit.RightToeBaseMaxRLimitx
    RightToeBaseMaxRLimity = RightToeBaseMaxRLimit.RightToeBaseMaxRLimity
    RightToeBaseMaxRLimitz = RightToeBaseMaxRLimit.RightToeBaseMaxRLimitz

    RightToeBaseMinRLimitEnablex = BoolField(default_value=False)

    RightToeBaseMinRLimitEnabley = BoolField(default_value=False)

    RightToeBaseMinRLimitEnablez = BoolField(default_value=False)

    RightToeBaseMaxRLimitEnablex = BoolField(default_value=False)

    RightToeBaseMaxRLimitEnabley = BoolField(default_value=False)

    RightToeBaseMaxRLimitEnablez = BoolField(default_value=False)

    LeftShoulder = MessageField()

    LeftShoulderT = LeftShoulderTField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderTx = LeftShoulderT.LeftShoulderTx
    LeftShoulderTy = LeftShoulderT.LeftShoulderTy
    LeftShoulderTz = LeftShoulderT.LeftShoulderTz

    LeftShoulderR = LeftShoulderRField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderRx = LeftShoulderR.LeftShoulderRx
    LeftShoulderRy = LeftShoulderR.LeftShoulderRy
    LeftShoulderRz = LeftShoulderR.LeftShoulderRz

    LeftShoulderS = LeftShoulderSField(default_value=(1.0, 1.0, 1.0))
    LeftShoulderSx = LeftShoulderS.LeftShoulderSx
    LeftShoulderSy = LeftShoulderS.LeftShoulderSy
    LeftShoulderSz = LeftShoulderS.LeftShoulderSz

    LeftShoulderRotateOrder = LeftShoulderRotateOrderEnumField(default_value=0)

    LeftShoulderRotateAxis = LeftShoulderRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderRotateAxisx = LeftShoulderRotateAxis.LeftShoulderRotateAxisx
    LeftShoulderRotateAxisy = LeftShoulderRotateAxis.LeftShoulderRotateAxisy
    LeftShoulderRotateAxisz = LeftShoulderRotateAxis.LeftShoulderRotateAxisz

    LeftShoulderJointOrient = LeftShoulderJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderJointOrientx = LeftShoulderJointOrient.LeftShoulderJointOrientx
    LeftShoulderJointOrienty = LeftShoulderJointOrient.LeftShoulderJointOrienty
    LeftShoulderJointOrientz = LeftShoulderJointOrient.LeftShoulderJointOrientz

    LeftShoulderMinRLimit = LeftShoulderMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderMinRLimitx = LeftShoulderMinRLimit.LeftShoulderMinRLimitx
    LeftShoulderMinRLimity = LeftShoulderMinRLimit.LeftShoulderMinRLimity
    LeftShoulderMinRLimitz = LeftShoulderMinRLimit.LeftShoulderMinRLimitz

    LeftShoulderMaxRLimit = LeftShoulderMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderMaxRLimitx = LeftShoulderMaxRLimit.LeftShoulderMaxRLimitx
    LeftShoulderMaxRLimity = LeftShoulderMaxRLimit.LeftShoulderMaxRLimity
    LeftShoulderMaxRLimitz = LeftShoulderMaxRLimit.LeftShoulderMaxRLimitz

    LeftShoulderMinRLimitEnablex = BoolField(default_value=False)

    LeftShoulderMinRLimitEnabley = BoolField(default_value=False)

    LeftShoulderMinRLimitEnablez = BoolField(default_value=False)

    LeftShoulderMaxRLimitEnablex = BoolField(default_value=False)

    LeftShoulderMaxRLimitEnabley = BoolField(default_value=False)

    LeftShoulderMaxRLimitEnablez = BoolField(default_value=False)

    RightShoulder = MessageField()

    RightShoulderT = RightShoulderTField(default_value=(0.0, 0.0, 0.0))
    RightShoulderTx = RightShoulderT.RightShoulderTx
    RightShoulderTy = RightShoulderT.RightShoulderTy
    RightShoulderTz = RightShoulderT.RightShoulderTz

    RightShoulderR = RightShoulderRField(default_value=(0.0, 0.0, 0.0))
    RightShoulderRx = RightShoulderR.RightShoulderRx
    RightShoulderRy = RightShoulderR.RightShoulderRy
    RightShoulderRz = RightShoulderR.RightShoulderRz

    RightShoulderS = RightShoulderSField(default_value=(1.0, 1.0, 1.0))
    RightShoulderSx = RightShoulderS.RightShoulderSx
    RightShoulderSy = RightShoulderS.RightShoulderSy
    RightShoulderSz = RightShoulderS.RightShoulderSz

    RightShoulderRotateOrder = RightShoulderRotateOrderEnumField(default_value=0)

    RightShoulderRotateAxis = RightShoulderRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightShoulderRotateAxisx = RightShoulderRotateAxis.RightShoulderRotateAxisx
    RightShoulderRotateAxisy = RightShoulderRotateAxis.RightShoulderRotateAxisy
    RightShoulderRotateAxisz = RightShoulderRotateAxis.RightShoulderRotateAxisz

    RightShoulderJointOrient = RightShoulderJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightShoulderJointOrientx = RightShoulderJointOrient.RightShoulderJointOrientx
    RightShoulderJointOrienty = RightShoulderJointOrient.RightShoulderJointOrienty
    RightShoulderJointOrientz = RightShoulderJointOrient.RightShoulderJointOrientz

    RightShoulderMinRLimit = RightShoulderMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightShoulderMinRLimitx = RightShoulderMinRLimit.RightShoulderMinRLimitx
    RightShoulderMinRLimity = RightShoulderMinRLimit.RightShoulderMinRLimity
    RightShoulderMinRLimitz = RightShoulderMinRLimit.RightShoulderMinRLimitz

    RightShoulderMaxRLimit = RightShoulderMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightShoulderMaxRLimitx = RightShoulderMaxRLimit.RightShoulderMaxRLimitx
    RightShoulderMaxRLimity = RightShoulderMaxRLimit.RightShoulderMaxRLimity
    RightShoulderMaxRLimitz = RightShoulderMaxRLimit.RightShoulderMaxRLimitz

    RightShoulderMinRLimitEnablex = BoolField(default_value=False)

    RightShoulderMinRLimitEnabley = BoolField(default_value=False)

    RightShoulderMinRLimitEnablez = BoolField(default_value=False)

    RightShoulderMaxRLimitEnablex = BoolField(default_value=False)

    RightShoulderMaxRLimitEnabley = BoolField(default_value=False)

    RightShoulderMaxRLimitEnablez = BoolField(default_value=False)

    Neck = MessageField()

    NeckT = NeckTField(default_value=(0.0, 0.0, 0.0))
    NeckTx = NeckT.NeckTx
    NeckTy = NeckT.NeckTy
    NeckTz = NeckT.NeckTz

    NeckR = NeckRField(default_value=(0.0, 0.0, 0.0))
    NeckRx = NeckR.NeckRx
    NeckRy = NeckR.NeckRy
    NeckRz = NeckR.NeckRz

    NeckS = NeckSField(default_value=(1.0, 1.0, 1.0))
    NeckSx = NeckS.NeckSx
    NeckSy = NeckS.NeckSy
    NeckSz = NeckS.NeckSz

    NeckRotateOrder = NeckRotateOrderEnumField(default_value=0)

    NeckRotateAxis = NeckRotateAxisField(default_value=(0.0, 0.0, 0.0))
    NeckRotateAxisx = NeckRotateAxis.NeckRotateAxisx
    NeckRotateAxisy = NeckRotateAxis.NeckRotateAxisy
    NeckRotateAxisz = NeckRotateAxis.NeckRotateAxisz

    NeckJointOrient = NeckJointOrientField(default_value=(0.0, 0.0, 0.0))
    NeckJointOrientx = NeckJointOrient.NeckJointOrientx
    NeckJointOrienty = NeckJointOrient.NeckJointOrienty
    NeckJointOrientz = NeckJointOrient.NeckJointOrientz

    NeckMinRLimit = NeckMinRLimitField(default_value=(0.0, 0.0, 0.0))
    NeckMinRLimitx = NeckMinRLimit.NeckMinRLimitx
    NeckMinRLimity = NeckMinRLimit.NeckMinRLimity
    NeckMinRLimitz = NeckMinRLimit.NeckMinRLimitz

    NeckMaxRLimit = NeckMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    NeckMaxRLimitx = NeckMaxRLimit.NeckMaxRLimitx
    NeckMaxRLimity = NeckMaxRLimit.NeckMaxRLimity
    NeckMaxRLimitz = NeckMaxRLimit.NeckMaxRLimitz

    NeckMinRLimitEnablex = BoolField(default_value=False)

    NeckMinRLimitEnabley = BoolField(default_value=False)

    NeckMinRLimitEnablez = BoolField(default_value=False)

    NeckMaxRLimitEnablex = BoolField(default_value=False)

    NeckMaxRLimitEnabley = BoolField(default_value=False)

    NeckMaxRLimitEnablez = BoolField(default_value=False)

    LeftFingerBase = MessageField()

    LeftFingerBaseT = LeftFingerBaseTField(default_value=(0.0, 0.0, 0.0))
    LeftFingerBaseTx = LeftFingerBaseT.LeftFingerBaseTx
    LeftFingerBaseTy = LeftFingerBaseT.LeftFingerBaseTy
    LeftFingerBaseTz = LeftFingerBaseT.LeftFingerBaseTz

    LeftFingerBaseR = LeftFingerBaseRField(default_value=(0.0, 0.0, 0.0))
    LeftFingerBaseRx = LeftFingerBaseR.LeftFingerBaseRx
    LeftFingerBaseRy = LeftFingerBaseR.LeftFingerBaseRy
    LeftFingerBaseRz = LeftFingerBaseR.LeftFingerBaseRz

    LeftFingerBaseS = LeftFingerBaseSField(default_value=(1.0, 1.0, 1.0))
    LeftFingerBaseSx = LeftFingerBaseS.LeftFingerBaseSx
    LeftFingerBaseSy = LeftFingerBaseS.LeftFingerBaseSy
    LeftFingerBaseSz = LeftFingerBaseS.LeftFingerBaseSz

    LeftFingerBaseRotateOrder = LeftFingerBaseRotateOrderEnumField(default_value=0)

    LeftFingerBaseRotateAxis = LeftFingerBaseRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFingerBaseRotateAxisx = LeftFingerBaseRotateAxis.LeftFingerBaseRotateAxisx
    LeftFingerBaseRotateAxisy = LeftFingerBaseRotateAxis.LeftFingerBaseRotateAxisy
    LeftFingerBaseRotateAxisz = LeftFingerBaseRotateAxis.LeftFingerBaseRotateAxisz

    LeftFingerBaseJointOrient = LeftFingerBaseJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFingerBaseJointOrientx = LeftFingerBaseJointOrient.LeftFingerBaseJointOrientx
    LeftFingerBaseJointOrienty = LeftFingerBaseJointOrient.LeftFingerBaseJointOrienty
    LeftFingerBaseJointOrientz = LeftFingerBaseJointOrient.LeftFingerBaseJointOrientz

    LeftFingerBaseMinRLimit = LeftFingerBaseMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFingerBaseMinRLimitx = LeftFingerBaseMinRLimit.LeftFingerBaseMinRLimitx
    LeftFingerBaseMinRLimity = LeftFingerBaseMinRLimit.LeftFingerBaseMinRLimity
    LeftFingerBaseMinRLimitz = LeftFingerBaseMinRLimit.LeftFingerBaseMinRLimitz

    LeftFingerBaseMaxRLimit = LeftFingerBaseMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFingerBaseMaxRLimitx = LeftFingerBaseMaxRLimit.LeftFingerBaseMaxRLimitx
    LeftFingerBaseMaxRLimity = LeftFingerBaseMaxRLimit.LeftFingerBaseMaxRLimity
    LeftFingerBaseMaxRLimitz = LeftFingerBaseMaxRLimit.LeftFingerBaseMaxRLimitz

    LeftFingerBaseMinRLimitEnablex = BoolField(default_value=False)

    LeftFingerBaseMinRLimitEnabley = BoolField(default_value=False)

    LeftFingerBaseMinRLimitEnablez = BoolField(default_value=False)

    LeftFingerBaseMaxRLimitEnablex = BoolField(default_value=False)

    LeftFingerBaseMaxRLimitEnabley = BoolField(default_value=False)

    LeftFingerBaseMaxRLimitEnablez = BoolField(default_value=False)

    RightFingerBase = MessageField()

    RightFingerBaseT = RightFingerBaseTField(default_value=(0.0, 0.0, 0.0))
    RightFingerBaseTx = RightFingerBaseT.RightFingerBaseTx
    RightFingerBaseTy = RightFingerBaseT.RightFingerBaseTy
    RightFingerBaseTz = RightFingerBaseT.RightFingerBaseTz

    RightFingerBaseR = RightFingerBaseRField(default_value=(0.0, 0.0, 0.0))
    RightFingerBaseRx = RightFingerBaseR.RightFingerBaseRx
    RightFingerBaseRy = RightFingerBaseR.RightFingerBaseRy
    RightFingerBaseRz = RightFingerBaseR.RightFingerBaseRz

    RightFingerBaseS = RightFingerBaseSField(default_value=(1.0, 1.0, 1.0))
    RightFingerBaseSx = RightFingerBaseS.RightFingerBaseSx
    RightFingerBaseSy = RightFingerBaseS.RightFingerBaseSy
    RightFingerBaseSz = RightFingerBaseS.RightFingerBaseSz

    RightFingerBaseRotateOrder = RightFingerBaseRotateOrderEnumField(default_value=0)

    RightFingerBaseRotateAxis = RightFingerBaseRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFingerBaseRotateAxisx = RightFingerBaseRotateAxis.RightFingerBaseRotateAxisx
    RightFingerBaseRotateAxisy = RightFingerBaseRotateAxis.RightFingerBaseRotateAxisy
    RightFingerBaseRotateAxisz = RightFingerBaseRotateAxis.RightFingerBaseRotateAxisz

    RightFingerBaseJointOrient = RightFingerBaseJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFingerBaseJointOrientx = RightFingerBaseJointOrient.RightFingerBaseJointOrientx
    RightFingerBaseJointOrienty = RightFingerBaseJointOrient.RightFingerBaseJointOrienty
    RightFingerBaseJointOrientz = RightFingerBaseJointOrient.RightFingerBaseJointOrientz

    RightFingerBaseMinRLimit = RightFingerBaseMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFingerBaseMinRLimitx = RightFingerBaseMinRLimit.RightFingerBaseMinRLimitx
    RightFingerBaseMinRLimity = RightFingerBaseMinRLimit.RightFingerBaseMinRLimity
    RightFingerBaseMinRLimitz = RightFingerBaseMinRLimit.RightFingerBaseMinRLimitz

    RightFingerBaseMaxRLimit = RightFingerBaseMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFingerBaseMaxRLimitx = RightFingerBaseMaxRLimit.RightFingerBaseMaxRLimitx
    RightFingerBaseMaxRLimity = RightFingerBaseMaxRLimit.RightFingerBaseMaxRLimity
    RightFingerBaseMaxRLimitz = RightFingerBaseMaxRLimit.RightFingerBaseMaxRLimitz

    RightFingerBaseMinRLimitEnablex = BoolField(default_value=False)

    RightFingerBaseMinRLimitEnabley = BoolField(default_value=False)

    RightFingerBaseMinRLimitEnablez = BoolField(default_value=False)

    RightFingerBaseMaxRLimitEnablex = BoolField(default_value=False)

    RightFingerBaseMaxRLimitEnabley = BoolField(default_value=False)

    RightFingerBaseMaxRLimitEnablez = BoolField(default_value=False)

    Spine1 = MessageField()

    Spine1T = Spine1TField(default_value=(0.0, 0.0, 0.0))
    Spine1Tx = Spine1T.Spine1Tx
    Spine1Ty = Spine1T.Spine1Ty
    Spine1Tz = Spine1T.Spine1Tz

    Spine1R = Spine1RField(default_value=(0.0, 0.0, 0.0))
    Spine1Rx = Spine1R.Spine1Rx
    Spine1Ry = Spine1R.Spine1Ry
    Spine1Rz = Spine1R.Spine1Rz

    Spine1S = Spine1SField(default_value=(1.0, 1.0, 1.0))
    Spine1Sx = Spine1S.Spine1Sx
    Spine1Sy = Spine1S.Spine1Sy
    Spine1Sz = Spine1S.Spine1Sz

    Spine1RotateOrder = Spine1RotateOrderEnumField(default_value=0)

    Spine1RotateAxis = Spine1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Spine1RotateAxisx = Spine1RotateAxis.Spine1RotateAxisx
    Spine1RotateAxisy = Spine1RotateAxis.Spine1RotateAxisy
    Spine1RotateAxisz = Spine1RotateAxis.Spine1RotateAxisz

    Spine1JointOrient = Spine1JointOrientField(default_value=(0.0, 0.0, 0.0))
    Spine1JointOrientx = Spine1JointOrient.Spine1JointOrientx
    Spine1JointOrienty = Spine1JointOrient.Spine1JointOrienty
    Spine1JointOrientz = Spine1JointOrient.Spine1JointOrientz

    Spine1MinRLimit = Spine1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine1MinRLimitx = Spine1MinRLimit.Spine1MinRLimitx
    Spine1MinRLimity = Spine1MinRLimit.Spine1MinRLimity
    Spine1MinRLimitz = Spine1MinRLimit.Spine1MinRLimitz

    Spine1MaxRLimit = Spine1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine1MaxRLimitx = Spine1MaxRLimit.Spine1MaxRLimitx
    Spine1MaxRLimity = Spine1MaxRLimit.Spine1MaxRLimity
    Spine1MaxRLimitz = Spine1MaxRLimit.Spine1MaxRLimitz

    Spine1MinRLimitEnablex = BoolField(default_value=False)

    Spine1MinRLimitEnabley = BoolField(default_value=False)

    Spine1MinRLimitEnablez = BoolField(default_value=False)

    Spine1MaxRLimitEnablex = BoolField(default_value=False)

    Spine1MaxRLimitEnabley = BoolField(default_value=False)

    Spine1MaxRLimitEnablez = BoolField(default_value=False)

    Spine2 = MessageField()

    Spine2T = Spine2TField(default_value=(0.0, 0.0, 0.0))
    Spine2Tx = Spine2T.Spine2Tx
    Spine2Ty = Spine2T.Spine2Ty
    Spine2Tz = Spine2T.Spine2Tz

    Spine2R = Spine2RField(default_value=(0.0, 0.0, 0.0))
    Spine2Rx = Spine2R.Spine2Rx
    Spine2Ry = Spine2R.Spine2Ry
    Spine2Rz = Spine2R.Spine2Rz

    Spine2S = Spine2SField(default_value=(1.0, 1.0, 1.0))
    Spine2Sx = Spine2S.Spine2Sx
    Spine2Sy = Spine2S.Spine2Sy
    Spine2Sz = Spine2S.Spine2Sz

    Spine2RotateOrder = Spine2RotateOrderEnumField(default_value=0)

    Spine2RotateAxis = Spine2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Spine2RotateAxisx = Spine2RotateAxis.Spine2RotateAxisx
    Spine2RotateAxisy = Spine2RotateAxis.Spine2RotateAxisy
    Spine2RotateAxisz = Spine2RotateAxis.Spine2RotateAxisz

    Spine2JointOrient = Spine2JointOrientField(default_value=(0.0, 0.0, 0.0))
    Spine2JointOrientx = Spine2JointOrient.Spine2JointOrientx
    Spine2JointOrienty = Spine2JointOrient.Spine2JointOrienty
    Spine2JointOrientz = Spine2JointOrient.Spine2JointOrientz

    Spine2MinRLimit = Spine2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine2MinRLimitx = Spine2MinRLimit.Spine2MinRLimitx
    Spine2MinRLimity = Spine2MinRLimit.Spine2MinRLimity
    Spine2MinRLimitz = Spine2MinRLimit.Spine2MinRLimitz

    Spine2MaxRLimit = Spine2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine2MaxRLimitx = Spine2MaxRLimit.Spine2MaxRLimitx
    Spine2MaxRLimity = Spine2MaxRLimit.Spine2MaxRLimity
    Spine2MaxRLimitz = Spine2MaxRLimit.Spine2MaxRLimitz

    Spine2MinRLimitEnablex = BoolField(default_value=False)

    Spine2MinRLimitEnabley = BoolField(default_value=False)

    Spine2MinRLimitEnablez = BoolField(default_value=False)

    Spine2MaxRLimitEnablex = BoolField(default_value=False)

    Spine2MaxRLimitEnabley = BoolField(default_value=False)

    Spine2MaxRLimitEnablez = BoolField(default_value=False)

    Spine3 = MessageField()

    Spine3T = Spine3TField(default_value=(0.0, 0.0, 0.0))
    Spine3Tx = Spine3T.Spine3Tx
    Spine3Ty = Spine3T.Spine3Ty
    Spine3Tz = Spine3T.Spine3Tz

    Spine3R = Spine3RField(default_value=(0.0, 0.0, 0.0))
    Spine3Rx = Spine3R.Spine3Rx
    Spine3Ry = Spine3R.Spine3Ry
    Spine3Rz = Spine3R.Spine3Rz

    Spine3S = Spine3SField(default_value=(1.0, 1.0, 1.0))
    Spine3Sx = Spine3S.Spine3Sx
    Spine3Sy = Spine3S.Spine3Sy
    Spine3Sz = Spine3S.Spine3Sz

    Spine3RotateOrder = Spine3RotateOrderEnumField(default_value=0)

    Spine3RotateAxis = Spine3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Spine3RotateAxisx = Spine3RotateAxis.Spine3RotateAxisx
    Spine3RotateAxisy = Spine3RotateAxis.Spine3RotateAxisy
    Spine3RotateAxisz = Spine3RotateAxis.Spine3RotateAxisz

    Spine3JointOrient = Spine3JointOrientField(default_value=(0.0, 0.0, 0.0))
    Spine3JointOrientx = Spine3JointOrient.Spine3JointOrientx
    Spine3JointOrienty = Spine3JointOrient.Spine3JointOrienty
    Spine3JointOrientz = Spine3JointOrient.Spine3JointOrientz

    Spine3MinRLimit = Spine3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine3MinRLimitx = Spine3MinRLimit.Spine3MinRLimitx
    Spine3MinRLimity = Spine3MinRLimit.Spine3MinRLimity
    Spine3MinRLimitz = Spine3MinRLimit.Spine3MinRLimitz

    Spine3MaxRLimit = Spine3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine3MaxRLimitx = Spine3MaxRLimit.Spine3MaxRLimitx
    Spine3MaxRLimity = Spine3MaxRLimit.Spine3MaxRLimity
    Spine3MaxRLimitz = Spine3MaxRLimit.Spine3MaxRLimitz

    Spine3MinRLimitEnablex = BoolField(default_value=False)

    Spine3MinRLimitEnabley = BoolField(default_value=False)

    Spine3MinRLimitEnablez = BoolField(default_value=False)

    Spine3MaxRLimitEnablex = BoolField(default_value=False)

    Spine3MaxRLimitEnabley = BoolField(default_value=False)

    Spine3MaxRLimitEnablez = BoolField(default_value=False)

    Spine4 = MessageField()

    Spine4T = Spine4TField(default_value=(0.0, 0.0, 0.0))
    Spine4Tx = Spine4T.Spine4Tx
    Spine4Ty = Spine4T.Spine4Ty
    Spine4Tz = Spine4T.Spine4Tz

    Spine4R = Spine4RField(default_value=(0.0, 0.0, 0.0))
    Spine4Rx = Spine4R.Spine4Rx
    Spine4Ry = Spine4R.Spine4Ry
    Spine4Rz = Spine4R.Spine4Rz

    Spine4S = Spine4SField(default_value=(1.0, 1.0, 1.0))
    Spine4Sx = Spine4S.Spine4Sx
    Spine4Sy = Spine4S.Spine4Sy
    Spine4Sz = Spine4S.Spine4Sz

    Spine4RotateOrder = Spine4RotateOrderEnumField(default_value=0)

    Spine4RotateAxis = Spine4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Spine4RotateAxisx = Spine4RotateAxis.Spine4RotateAxisx
    Spine4RotateAxisy = Spine4RotateAxis.Spine4RotateAxisy
    Spine4RotateAxisz = Spine4RotateAxis.Spine4RotateAxisz

    Spine4JointOrient = Spine4JointOrientField(default_value=(0.0, 0.0, 0.0))
    Spine4JointOrientx = Spine4JointOrient.Spine4JointOrientx
    Spine4JointOrienty = Spine4JointOrient.Spine4JointOrienty
    Spine4JointOrientz = Spine4JointOrient.Spine4JointOrientz

    Spine4MinRLimit = Spine4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine4MinRLimitx = Spine4MinRLimit.Spine4MinRLimitx
    Spine4MinRLimity = Spine4MinRLimit.Spine4MinRLimity
    Spine4MinRLimitz = Spine4MinRLimit.Spine4MinRLimitz

    Spine4MaxRLimit = Spine4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine4MaxRLimitx = Spine4MaxRLimit.Spine4MaxRLimitx
    Spine4MaxRLimity = Spine4MaxRLimit.Spine4MaxRLimity
    Spine4MaxRLimitz = Spine4MaxRLimit.Spine4MaxRLimitz

    Spine4MinRLimitEnablex = BoolField(default_value=False)

    Spine4MinRLimitEnabley = BoolField(default_value=False)

    Spine4MinRLimitEnablez = BoolField(default_value=False)

    Spine4MaxRLimitEnablex = BoolField(default_value=False)

    Spine4MaxRLimitEnabley = BoolField(default_value=False)

    Spine4MaxRLimitEnablez = BoolField(default_value=False)

    Spine5 = MessageField()

    Spine5T = Spine5TField(default_value=(0.0, 0.0, 0.0))
    Spine5Tx = Spine5T.Spine5Tx
    Spine5Ty = Spine5T.Spine5Ty
    Spine5Tz = Spine5T.Spine5Tz

    Spine5R = Spine5RField(default_value=(0.0, 0.0, 0.0))
    Spine5Rx = Spine5R.Spine5Rx
    Spine5Ry = Spine5R.Spine5Ry
    Spine5Rz = Spine5R.Spine5Rz

    Spine5S = Spine5SField(default_value=(1.0, 1.0, 1.0))
    Spine5Sx = Spine5S.Spine5Sx
    Spine5Sy = Spine5S.Spine5Sy
    Spine5Sz = Spine5S.Spine5Sz

    Spine5RotateOrder = Spine5RotateOrderEnumField(default_value=0)

    Spine5RotateAxis = Spine5RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Spine5RotateAxisx = Spine5RotateAxis.Spine5RotateAxisx
    Spine5RotateAxisy = Spine5RotateAxis.Spine5RotateAxisy
    Spine5RotateAxisz = Spine5RotateAxis.Spine5RotateAxisz

    Spine5JointOrient = Spine5JointOrientField(default_value=(0.0, 0.0, 0.0))
    Spine5JointOrientx = Spine5JointOrient.Spine5JointOrientx
    Spine5JointOrienty = Spine5JointOrient.Spine5JointOrienty
    Spine5JointOrientz = Spine5JointOrient.Spine5JointOrientz

    Spine5MinRLimit = Spine5MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine5MinRLimitx = Spine5MinRLimit.Spine5MinRLimitx
    Spine5MinRLimity = Spine5MinRLimit.Spine5MinRLimity
    Spine5MinRLimitz = Spine5MinRLimit.Spine5MinRLimitz

    Spine5MaxRLimit = Spine5MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine5MaxRLimitx = Spine5MaxRLimit.Spine5MaxRLimitx
    Spine5MaxRLimity = Spine5MaxRLimit.Spine5MaxRLimity
    Spine5MaxRLimitz = Spine5MaxRLimit.Spine5MaxRLimitz

    Spine5MinRLimitEnablex = BoolField(default_value=False)

    Spine5MinRLimitEnabley = BoolField(default_value=False)

    Spine5MinRLimitEnablez = BoolField(default_value=False)

    Spine5MaxRLimitEnablex = BoolField(default_value=False)

    Spine5MaxRLimitEnabley = BoolField(default_value=False)

    Spine5MaxRLimitEnablez = BoolField(default_value=False)

    Spine6 = MessageField()

    Spine6T = Spine6TField(default_value=(0.0, 0.0, 0.0))
    Spine6Tx = Spine6T.Spine6Tx
    Spine6Ty = Spine6T.Spine6Ty
    Spine6Tz = Spine6T.Spine6Tz

    Spine6R = Spine6RField(default_value=(0.0, 0.0, 0.0))
    Spine6Rx = Spine6R.Spine6Rx
    Spine6Ry = Spine6R.Spine6Ry
    Spine6Rz = Spine6R.Spine6Rz

    Spine6S = Spine6SField(default_value=(1.0, 1.0, 1.0))
    Spine6Sx = Spine6S.Spine6Sx
    Spine6Sy = Spine6S.Spine6Sy
    Spine6Sz = Spine6S.Spine6Sz

    Spine6RotateOrder = Spine6RotateOrderEnumField(default_value=0)

    Spine6RotateAxis = Spine6RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Spine6RotateAxisx = Spine6RotateAxis.Spine6RotateAxisx
    Spine6RotateAxisy = Spine6RotateAxis.Spine6RotateAxisy
    Spine6RotateAxisz = Spine6RotateAxis.Spine6RotateAxisz

    Spine6JointOrient = Spine6JointOrientField(default_value=(0.0, 0.0, 0.0))
    Spine6JointOrientx = Spine6JointOrient.Spine6JointOrientx
    Spine6JointOrienty = Spine6JointOrient.Spine6JointOrienty
    Spine6JointOrientz = Spine6JointOrient.Spine6JointOrientz

    Spine6MinRLimit = Spine6MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine6MinRLimitx = Spine6MinRLimit.Spine6MinRLimitx
    Spine6MinRLimity = Spine6MinRLimit.Spine6MinRLimity
    Spine6MinRLimitz = Spine6MinRLimit.Spine6MinRLimitz

    Spine6MaxRLimit = Spine6MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine6MaxRLimitx = Spine6MaxRLimit.Spine6MaxRLimitx
    Spine6MaxRLimity = Spine6MaxRLimit.Spine6MaxRLimity
    Spine6MaxRLimitz = Spine6MaxRLimit.Spine6MaxRLimitz

    Spine6MinRLimitEnablex = BoolField(default_value=False)

    Spine6MinRLimitEnabley = BoolField(default_value=False)

    Spine6MinRLimitEnablez = BoolField(default_value=False)

    Spine6MaxRLimitEnablex = BoolField(default_value=False)

    Spine6MaxRLimitEnabley = BoolField(default_value=False)

    Spine6MaxRLimitEnablez = BoolField(default_value=False)

    Spine7 = MessageField()

    Spine7T = Spine7TField(default_value=(0.0, 0.0, 0.0))
    Spine7Tx = Spine7T.Spine7Tx
    Spine7Ty = Spine7T.Spine7Ty
    Spine7Tz = Spine7T.Spine7Tz

    Spine7R = Spine7RField(default_value=(0.0, 0.0, 0.0))
    Spine7Rx = Spine7R.Spine7Rx
    Spine7Ry = Spine7R.Spine7Ry
    Spine7Rz = Spine7R.Spine7Rz

    Spine7S = Spine7SField(default_value=(1.0, 1.0, 1.0))
    Spine7Sx = Spine7S.Spine7Sx
    Spine7Sy = Spine7S.Spine7Sy
    Spine7Sz = Spine7S.Spine7Sz

    Spine7RotateOrder = Spine7RotateOrderEnumField(default_value=0)

    Spine7RotateAxis = Spine7RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Spine7RotateAxisx = Spine7RotateAxis.Spine7RotateAxisx
    Spine7RotateAxisy = Spine7RotateAxis.Spine7RotateAxisy
    Spine7RotateAxisz = Spine7RotateAxis.Spine7RotateAxisz

    Spine7JointOrient = Spine7JointOrientField(default_value=(0.0, 0.0, 0.0))
    Spine7JointOrientx = Spine7JointOrient.Spine7JointOrientx
    Spine7JointOrienty = Spine7JointOrient.Spine7JointOrienty
    Spine7JointOrientz = Spine7JointOrient.Spine7JointOrientz

    Spine7MinRLimit = Spine7MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine7MinRLimitx = Spine7MinRLimit.Spine7MinRLimitx
    Spine7MinRLimity = Spine7MinRLimit.Spine7MinRLimity
    Spine7MinRLimitz = Spine7MinRLimit.Spine7MinRLimitz

    Spine7MaxRLimit = Spine7MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine7MaxRLimitx = Spine7MaxRLimit.Spine7MaxRLimitx
    Spine7MaxRLimity = Spine7MaxRLimit.Spine7MaxRLimity
    Spine7MaxRLimitz = Spine7MaxRLimit.Spine7MaxRLimitz

    Spine7MinRLimitEnablex = BoolField(default_value=False)

    Spine7MinRLimitEnabley = BoolField(default_value=False)

    Spine7MinRLimitEnablez = BoolField(default_value=False)

    Spine7MaxRLimitEnablex = BoolField(default_value=False)

    Spine7MaxRLimitEnabley = BoolField(default_value=False)

    Spine7MaxRLimitEnablez = BoolField(default_value=False)

    Spine8 = MessageField()

    Spine8T = Spine8TField(default_value=(0.0, 0.0, 0.0))
    Spine8Tx = Spine8T.Spine8Tx
    Spine8Ty = Spine8T.Spine8Ty
    Spine8Tz = Spine8T.Spine8Tz

    Spine8R = Spine8RField(default_value=(0.0, 0.0, 0.0))
    Spine8Rx = Spine8R.Spine8Rx
    Spine8Ry = Spine8R.Spine8Ry
    Spine8Rz = Spine8R.Spine8Rz

    Spine8S = Spine8SField(default_value=(1.0, 1.0, 1.0))
    Spine8Sx = Spine8S.Spine8Sx
    Spine8Sy = Spine8S.Spine8Sy
    Spine8Sz = Spine8S.Spine8Sz

    Spine8RotateOrder = Spine8RotateOrderEnumField(default_value=0)

    Spine8RotateAxis = Spine8RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Spine8RotateAxisx = Spine8RotateAxis.Spine8RotateAxisx
    Spine8RotateAxisy = Spine8RotateAxis.Spine8RotateAxisy
    Spine8RotateAxisz = Spine8RotateAxis.Spine8RotateAxisz

    Spine8JointOrient = Spine8JointOrientField(default_value=(0.0, 0.0, 0.0))
    Spine8JointOrientx = Spine8JointOrient.Spine8JointOrientx
    Spine8JointOrienty = Spine8JointOrient.Spine8JointOrienty
    Spine8JointOrientz = Spine8JointOrient.Spine8JointOrientz

    Spine8MinRLimit = Spine8MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine8MinRLimitx = Spine8MinRLimit.Spine8MinRLimitx
    Spine8MinRLimity = Spine8MinRLimit.Spine8MinRLimity
    Spine8MinRLimitz = Spine8MinRLimit.Spine8MinRLimitz

    Spine8MaxRLimit = Spine8MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine8MaxRLimitx = Spine8MaxRLimit.Spine8MaxRLimitx
    Spine8MaxRLimity = Spine8MaxRLimit.Spine8MaxRLimity
    Spine8MaxRLimitz = Spine8MaxRLimit.Spine8MaxRLimitz

    Spine8MinRLimitEnablex = BoolField(default_value=False)

    Spine8MinRLimitEnabley = BoolField(default_value=False)

    Spine8MinRLimitEnablez = BoolField(default_value=False)

    Spine8MaxRLimitEnablex = BoolField(default_value=False)

    Spine8MaxRLimitEnabley = BoolField(default_value=False)

    Spine8MaxRLimitEnablez = BoolField(default_value=False)

    Spine9 = MessageField()

    Spine9T = Spine9TField(default_value=(0.0, 0.0, 0.0))
    Spine9Tx = Spine9T.Spine9Tx
    Spine9Ty = Spine9T.Spine9Ty
    Spine9Tz = Spine9T.Spine9Tz

    Spine9R = Spine9RField(default_value=(0.0, 0.0, 0.0))
    Spine9Rx = Spine9R.Spine9Rx
    Spine9Ry = Spine9R.Spine9Ry
    Spine9Rz = Spine9R.Spine9Rz

    Spine9S = Spine9SField(default_value=(1.0, 1.0, 1.0))
    Spine9Sx = Spine9S.Spine9Sx
    Spine9Sy = Spine9S.Spine9Sy
    Spine9Sz = Spine9S.Spine9Sz

    Spine9RotateOrder = Spine9RotateOrderEnumField(default_value=0)

    Spine9RotateAxis = Spine9RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Spine9RotateAxisx = Spine9RotateAxis.Spine9RotateAxisx
    Spine9RotateAxisy = Spine9RotateAxis.Spine9RotateAxisy
    Spine9RotateAxisz = Spine9RotateAxis.Spine9RotateAxisz

    Spine9JointOrient = Spine9JointOrientField(default_value=(0.0, 0.0, 0.0))
    Spine9JointOrientx = Spine9JointOrient.Spine9JointOrientx
    Spine9JointOrienty = Spine9JointOrient.Spine9JointOrienty
    Spine9JointOrientz = Spine9JointOrient.Spine9JointOrientz

    Spine9MinRLimit = Spine9MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine9MinRLimitx = Spine9MinRLimit.Spine9MinRLimitx
    Spine9MinRLimity = Spine9MinRLimit.Spine9MinRLimity
    Spine9MinRLimitz = Spine9MinRLimit.Spine9MinRLimitz

    Spine9MaxRLimit = Spine9MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Spine9MaxRLimitx = Spine9MaxRLimit.Spine9MaxRLimitx
    Spine9MaxRLimity = Spine9MaxRLimit.Spine9MaxRLimity
    Spine9MaxRLimitz = Spine9MaxRLimit.Spine9MaxRLimitz

    Spine9MinRLimitEnablex = BoolField(default_value=False)

    Spine9MinRLimitEnabley = BoolField(default_value=False)

    Spine9MinRLimitEnablez = BoolField(default_value=False)

    Spine9MaxRLimitEnablex = BoolField(default_value=False)

    Spine9MaxRLimitEnabley = BoolField(default_value=False)

    Spine9MaxRLimitEnablez = BoolField(default_value=False)

    Neck1 = MessageField()

    Neck1T = Neck1TField(default_value=(0.0, 0.0, 0.0))
    Neck1Tx = Neck1T.Neck1Tx
    Neck1Ty = Neck1T.Neck1Ty
    Neck1Tz = Neck1T.Neck1Tz

    Neck1R = Neck1RField(default_value=(0.0, 0.0, 0.0))
    Neck1Rx = Neck1R.Neck1Rx
    Neck1Ry = Neck1R.Neck1Ry
    Neck1Rz = Neck1R.Neck1Rz

    Neck1S = Neck1SField(default_value=(1.0, 1.0, 1.0))
    Neck1Sx = Neck1S.Neck1Sx
    Neck1Sy = Neck1S.Neck1Sy
    Neck1Sz = Neck1S.Neck1Sz

    Neck1RotateOrder = Neck1RotateOrderEnumField(default_value=0)

    Neck1RotateAxis = Neck1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Neck1RotateAxisx = Neck1RotateAxis.Neck1RotateAxisx
    Neck1RotateAxisy = Neck1RotateAxis.Neck1RotateAxisy
    Neck1RotateAxisz = Neck1RotateAxis.Neck1RotateAxisz

    Neck1JointOrient = Neck1JointOrientField(default_value=(0.0, 0.0, 0.0))
    Neck1JointOrientx = Neck1JointOrient.Neck1JointOrientx
    Neck1JointOrienty = Neck1JointOrient.Neck1JointOrienty
    Neck1JointOrientz = Neck1JointOrient.Neck1JointOrientz

    Neck1MinRLimit = Neck1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck1MinRLimitx = Neck1MinRLimit.Neck1MinRLimitx
    Neck1MinRLimity = Neck1MinRLimit.Neck1MinRLimity
    Neck1MinRLimitz = Neck1MinRLimit.Neck1MinRLimitz

    Neck1MaxRLimit = Neck1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck1MaxRLimitx = Neck1MaxRLimit.Neck1MaxRLimitx
    Neck1MaxRLimity = Neck1MaxRLimit.Neck1MaxRLimity
    Neck1MaxRLimitz = Neck1MaxRLimit.Neck1MaxRLimitz

    Neck1MinRLimitEnablex = BoolField(default_value=False)

    Neck1MinRLimitEnabley = BoolField(default_value=False)

    Neck1MinRLimitEnablez = BoolField(default_value=False)

    Neck1MaxRLimitEnablex = BoolField(default_value=False)

    Neck1MaxRLimitEnabley = BoolField(default_value=False)

    Neck1MaxRLimitEnablez = BoolField(default_value=False)

    Neck2 = MessageField()

    Neck2T = Neck2TField(default_value=(0.0, 0.0, 0.0))
    Neck2Tx = Neck2T.Neck2Tx
    Neck2Ty = Neck2T.Neck2Ty
    Neck2Tz = Neck2T.Neck2Tz

    Neck2R = Neck2RField(default_value=(0.0, 0.0, 0.0))
    Neck2Rx = Neck2R.Neck2Rx
    Neck2Ry = Neck2R.Neck2Ry
    Neck2Rz = Neck2R.Neck2Rz

    Neck2S = Neck2SField(default_value=(1.0, 1.0, 1.0))
    Neck2Sx = Neck2S.Neck2Sx
    Neck2Sy = Neck2S.Neck2Sy
    Neck2Sz = Neck2S.Neck2Sz

    Neck2RotateOrder = Neck2RotateOrderEnumField(default_value=0)

    Neck2RotateAxis = Neck2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Neck2RotateAxisx = Neck2RotateAxis.Neck2RotateAxisx
    Neck2RotateAxisy = Neck2RotateAxis.Neck2RotateAxisy
    Neck2RotateAxisz = Neck2RotateAxis.Neck2RotateAxisz

    Neck2JointOrient = Neck2JointOrientField(default_value=(0.0, 0.0, 0.0))
    Neck2JointOrientx = Neck2JointOrient.Neck2JointOrientx
    Neck2JointOrienty = Neck2JointOrient.Neck2JointOrienty
    Neck2JointOrientz = Neck2JointOrient.Neck2JointOrientz

    Neck2MinRLimit = Neck2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck2MinRLimitx = Neck2MinRLimit.Neck2MinRLimitx
    Neck2MinRLimity = Neck2MinRLimit.Neck2MinRLimity
    Neck2MinRLimitz = Neck2MinRLimit.Neck2MinRLimitz

    Neck2MaxRLimit = Neck2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck2MaxRLimitx = Neck2MaxRLimit.Neck2MaxRLimitx
    Neck2MaxRLimity = Neck2MaxRLimit.Neck2MaxRLimity
    Neck2MaxRLimitz = Neck2MaxRLimit.Neck2MaxRLimitz

    Neck2MinRLimitEnablex = BoolField(default_value=False)

    Neck2MinRLimitEnabley = BoolField(default_value=False)

    Neck2MinRLimitEnablez = BoolField(default_value=False)

    Neck2MaxRLimitEnablex = BoolField(default_value=False)

    Neck2MaxRLimitEnabley = BoolField(default_value=False)

    Neck2MaxRLimitEnablez = BoolField(default_value=False)

    Neck3 = MessageField()

    Neck3T = Neck3TField(default_value=(0.0, 0.0, 0.0))
    Neck3Tx = Neck3T.Neck3Tx
    Neck3Ty = Neck3T.Neck3Ty
    Neck3Tz = Neck3T.Neck3Tz

    Neck3R = Neck3RField(default_value=(0.0, 0.0, 0.0))
    Neck3Rx = Neck3R.Neck3Rx
    Neck3Ry = Neck3R.Neck3Ry
    Neck3Rz = Neck3R.Neck3Rz

    Neck3S = Neck3SField(default_value=(1.0, 1.0, 1.0))
    Neck3Sx = Neck3S.Neck3Sx
    Neck3Sy = Neck3S.Neck3Sy
    Neck3Sz = Neck3S.Neck3Sz

    Neck3RotateOrder = Neck3RotateOrderEnumField(default_value=0)

    Neck3RotateAxis = Neck3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Neck3RotateAxisx = Neck3RotateAxis.Neck3RotateAxisx
    Neck3RotateAxisy = Neck3RotateAxis.Neck3RotateAxisy
    Neck3RotateAxisz = Neck3RotateAxis.Neck3RotateAxisz

    Neck3JointOrient = Neck3JointOrientField(default_value=(0.0, 0.0, 0.0))
    Neck3JointOrientx = Neck3JointOrient.Neck3JointOrientx
    Neck3JointOrienty = Neck3JointOrient.Neck3JointOrienty
    Neck3JointOrientz = Neck3JointOrient.Neck3JointOrientz

    Neck3MinRLimit = Neck3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck3MinRLimitx = Neck3MinRLimit.Neck3MinRLimitx
    Neck3MinRLimity = Neck3MinRLimit.Neck3MinRLimity
    Neck3MinRLimitz = Neck3MinRLimit.Neck3MinRLimitz

    Neck3MaxRLimit = Neck3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck3MaxRLimitx = Neck3MaxRLimit.Neck3MaxRLimitx
    Neck3MaxRLimity = Neck3MaxRLimit.Neck3MaxRLimity
    Neck3MaxRLimitz = Neck3MaxRLimit.Neck3MaxRLimitz

    Neck3MinRLimitEnablex = BoolField(default_value=False)

    Neck3MinRLimitEnabley = BoolField(default_value=False)

    Neck3MinRLimitEnablez = BoolField(default_value=False)

    Neck3MaxRLimitEnablex = BoolField(default_value=False)

    Neck3MaxRLimitEnabley = BoolField(default_value=False)

    Neck3MaxRLimitEnablez = BoolField(default_value=False)

    Neck4 = MessageField()

    Neck4T = Neck4TField(default_value=(0.0, 0.0, 0.0))
    Neck4Tx = Neck4T.Neck4Tx
    Neck4Ty = Neck4T.Neck4Ty
    Neck4Tz = Neck4T.Neck4Tz

    Neck4R = Neck4RField(default_value=(0.0, 0.0, 0.0))
    Neck4Rx = Neck4R.Neck4Rx
    Neck4Ry = Neck4R.Neck4Ry
    Neck4Rz = Neck4R.Neck4Rz

    Neck4S = Neck4SField(default_value=(1.0, 1.0, 1.0))
    Neck4Sx = Neck4S.Neck4Sx
    Neck4Sy = Neck4S.Neck4Sy
    Neck4Sz = Neck4S.Neck4Sz

    Neck4RotateOrder = Neck4RotateOrderEnumField(default_value=0)

    Neck4RotateAxis = Neck4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Neck4RotateAxisx = Neck4RotateAxis.Neck4RotateAxisx
    Neck4RotateAxisy = Neck4RotateAxis.Neck4RotateAxisy
    Neck4RotateAxisz = Neck4RotateAxis.Neck4RotateAxisz

    Neck4JointOrient = Neck4JointOrientField(default_value=(0.0, 0.0, 0.0))
    Neck4JointOrientx = Neck4JointOrient.Neck4JointOrientx
    Neck4JointOrienty = Neck4JointOrient.Neck4JointOrienty
    Neck4JointOrientz = Neck4JointOrient.Neck4JointOrientz

    Neck4MinRLimit = Neck4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck4MinRLimitx = Neck4MinRLimit.Neck4MinRLimitx
    Neck4MinRLimity = Neck4MinRLimit.Neck4MinRLimity
    Neck4MinRLimitz = Neck4MinRLimit.Neck4MinRLimitz

    Neck4MaxRLimit = Neck4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck4MaxRLimitx = Neck4MaxRLimit.Neck4MaxRLimitx
    Neck4MaxRLimity = Neck4MaxRLimit.Neck4MaxRLimity
    Neck4MaxRLimitz = Neck4MaxRLimit.Neck4MaxRLimitz

    Neck4MinRLimitEnablex = BoolField(default_value=False)

    Neck4MinRLimitEnabley = BoolField(default_value=False)

    Neck4MinRLimitEnablez = BoolField(default_value=False)

    Neck4MaxRLimitEnablex = BoolField(default_value=False)

    Neck4MaxRLimitEnabley = BoolField(default_value=False)

    Neck4MaxRLimitEnablez = BoolField(default_value=False)

    Neck5 = MessageField()

    Neck5T = Neck5TField(default_value=(0.0, 0.0, 0.0))
    Neck5Tx = Neck5T.Neck5Tx
    Neck5Ty = Neck5T.Neck5Ty
    Neck5Tz = Neck5T.Neck5Tz

    Neck5R = Neck5RField(default_value=(0.0, 0.0, 0.0))
    Neck5Rx = Neck5R.Neck5Rx
    Neck5Ry = Neck5R.Neck5Ry
    Neck5Rz = Neck5R.Neck5Rz

    Neck5S = Neck5SField(default_value=(1.0, 1.0, 1.0))
    Neck5Sx = Neck5S.Neck5Sx
    Neck5Sy = Neck5S.Neck5Sy
    Neck5Sz = Neck5S.Neck5Sz

    Neck5RotateOrder = Neck5RotateOrderEnumField(default_value=0)

    Neck5RotateAxis = Neck5RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Neck5RotateAxisx = Neck5RotateAxis.Neck5RotateAxisx
    Neck5RotateAxisy = Neck5RotateAxis.Neck5RotateAxisy
    Neck5RotateAxisz = Neck5RotateAxis.Neck5RotateAxisz

    Neck5JointOrient = Neck5JointOrientField(default_value=(0.0, 0.0, 0.0))
    Neck5JointOrientx = Neck5JointOrient.Neck5JointOrientx
    Neck5JointOrienty = Neck5JointOrient.Neck5JointOrienty
    Neck5JointOrientz = Neck5JointOrient.Neck5JointOrientz

    Neck5MinRLimit = Neck5MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck5MinRLimitx = Neck5MinRLimit.Neck5MinRLimitx
    Neck5MinRLimity = Neck5MinRLimit.Neck5MinRLimity
    Neck5MinRLimitz = Neck5MinRLimit.Neck5MinRLimitz

    Neck5MaxRLimit = Neck5MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck5MaxRLimitx = Neck5MaxRLimit.Neck5MaxRLimitx
    Neck5MaxRLimity = Neck5MaxRLimit.Neck5MaxRLimity
    Neck5MaxRLimitz = Neck5MaxRLimit.Neck5MaxRLimitz

    Neck5MinRLimitEnablex = BoolField(default_value=False)

    Neck5MinRLimitEnabley = BoolField(default_value=False)

    Neck5MinRLimitEnablez = BoolField(default_value=False)

    Neck5MaxRLimitEnablex = BoolField(default_value=False)

    Neck5MaxRLimitEnabley = BoolField(default_value=False)

    Neck5MaxRLimitEnablez = BoolField(default_value=False)

    Neck6 = MessageField()

    Neck6T = Neck6TField(default_value=(0.0, 0.0, 0.0))
    Neck6Tx = Neck6T.Neck6Tx
    Neck6Ty = Neck6T.Neck6Ty
    Neck6Tz = Neck6T.Neck6Tz

    Neck6R = Neck6RField(default_value=(0.0, 0.0, 0.0))
    Neck6Rx = Neck6R.Neck6Rx
    Neck6Ry = Neck6R.Neck6Ry
    Neck6Rz = Neck6R.Neck6Rz

    Neck6S = Neck6SField(default_value=(1.0, 1.0, 1.0))
    Neck6Sx = Neck6S.Neck6Sx
    Neck6Sy = Neck6S.Neck6Sy
    Neck6Sz = Neck6S.Neck6Sz

    Neck6RotateOrder = Neck6RotateOrderEnumField(default_value=0)

    Neck6RotateAxis = Neck6RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Neck6RotateAxisx = Neck6RotateAxis.Neck6RotateAxisx
    Neck6RotateAxisy = Neck6RotateAxis.Neck6RotateAxisy
    Neck6RotateAxisz = Neck6RotateAxis.Neck6RotateAxisz

    Neck6JointOrient = Neck6JointOrientField(default_value=(0.0, 0.0, 0.0))
    Neck6JointOrientx = Neck6JointOrient.Neck6JointOrientx
    Neck6JointOrienty = Neck6JointOrient.Neck6JointOrienty
    Neck6JointOrientz = Neck6JointOrient.Neck6JointOrientz

    Neck6MinRLimit = Neck6MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck6MinRLimitx = Neck6MinRLimit.Neck6MinRLimitx
    Neck6MinRLimity = Neck6MinRLimit.Neck6MinRLimity
    Neck6MinRLimitz = Neck6MinRLimit.Neck6MinRLimitz

    Neck6MaxRLimit = Neck6MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck6MaxRLimitx = Neck6MaxRLimit.Neck6MaxRLimitx
    Neck6MaxRLimity = Neck6MaxRLimit.Neck6MaxRLimity
    Neck6MaxRLimitz = Neck6MaxRLimit.Neck6MaxRLimitz

    Neck6MinRLimitEnablex = BoolField(default_value=False)

    Neck6MinRLimitEnabley = BoolField(default_value=False)

    Neck6MinRLimitEnablez = BoolField(default_value=False)

    Neck6MaxRLimitEnablex = BoolField(default_value=False)

    Neck6MaxRLimitEnabley = BoolField(default_value=False)

    Neck6MaxRLimitEnablez = BoolField(default_value=False)

    Neck7 = MessageField()

    Neck7T = Neck7TField(default_value=(0.0, 0.0, 0.0))
    Neck7Tx = Neck7T.Neck7Tx
    Neck7Ty = Neck7T.Neck7Ty
    Neck7Tz = Neck7T.Neck7Tz

    Neck7R = Neck7RField(default_value=(0.0, 0.0, 0.0))
    Neck7Rx = Neck7R.Neck7Rx
    Neck7Ry = Neck7R.Neck7Ry
    Neck7Rz = Neck7R.Neck7Rz

    Neck7S = Neck7SField(default_value=(1.0, 1.0, 1.0))
    Neck7Sx = Neck7S.Neck7Sx
    Neck7Sy = Neck7S.Neck7Sy
    Neck7Sz = Neck7S.Neck7Sz

    Neck7RotateOrder = Neck7RotateOrderEnumField(default_value=0)

    Neck7RotateAxis = Neck7RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Neck7RotateAxisx = Neck7RotateAxis.Neck7RotateAxisx
    Neck7RotateAxisy = Neck7RotateAxis.Neck7RotateAxisy
    Neck7RotateAxisz = Neck7RotateAxis.Neck7RotateAxisz

    Neck7JointOrient = Neck7JointOrientField(default_value=(0.0, 0.0, 0.0))
    Neck7JointOrientx = Neck7JointOrient.Neck7JointOrientx
    Neck7JointOrienty = Neck7JointOrient.Neck7JointOrienty
    Neck7JointOrientz = Neck7JointOrient.Neck7JointOrientz

    Neck7MinRLimit = Neck7MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck7MinRLimitx = Neck7MinRLimit.Neck7MinRLimitx
    Neck7MinRLimity = Neck7MinRLimit.Neck7MinRLimity
    Neck7MinRLimitz = Neck7MinRLimit.Neck7MinRLimitz

    Neck7MaxRLimit = Neck7MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck7MaxRLimitx = Neck7MaxRLimit.Neck7MaxRLimitx
    Neck7MaxRLimity = Neck7MaxRLimit.Neck7MaxRLimity
    Neck7MaxRLimitz = Neck7MaxRLimit.Neck7MaxRLimitz

    Neck7MinRLimitEnablex = BoolField(default_value=False)

    Neck7MinRLimitEnabley = BoolField(default_value=False)

    Neck7MinRLimitEnablez = BoolField(default_value=False)

    Neck7MaxRLimitEnablex = BoolField(default_value=False)

    Neck7MaxRLimitEnabley = BoolField(default_value=False)

    Neck7MaxRLimitEnablez = BoolField(default_value=False)

    Neck8 = MessageField()

    Neck8T = Neck8TField(default_value=(0.0, 0.0, 0.0))
    Neck8Tx = Neck8T.Neck8Tx
    Neck8Ty = Neck8T.Neck8Ty
    Neck8Tz = Neck8T.Neck8Tz

    Neck8R = Neck8RField(default_value=(0.0, 0.0, 0.0))
    Neck8Rx = Neck8R.Neck8Rx
    Neck8Ry = Neck8R.Neck8Ry
    Neck8Rz = Neck8R.Neck8Rz

    Neck8S = Neck8SField(default_value=(1.0, 1.0, 1.0))
    Neck8Sx = Neck8S.Neck8Sx
    Neck8Sy = Neck8S.Neck8Sy
    Neck8Sz = Neck8S.Neck8Sz

    Neck8RotateOrder = Neck8RotateOrderEnumField(default_value=0)

    Neck8RotateAxis = Neck8RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Neck8RotateAxisx = Neck8RotateAxis.Neck8RotateAxisx
    Neck8RotateAxisy = Neck8RotateAxis.Neck8RotateAxisy
    Neck8RotateAxisz = Neck8RotateAxis.Neck8RotateAxisz

    Neck8JointOrient = Neck8JointOrientField(default_value=(0.0, 0.0, 0.0))
    Neck8JointOrientx = Neck8JointOrient.Neck8JointOrientx
    Neck8JointOrienty = Neck8JointOrient.Neck8JointOrienty
    Neck8JointOrientz = Neck8JointOrient.Neck8JointOrientz

    Neck8MinRLimit = Neck8MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck8MinRLimitx = Neck8MinRLimit.Neck8MinRLimitx
    Neck8MinRLimity = Neck8MinRLimit.Neck8MinRLimity
    Neck8MinRLimitz = Neck8MinRLimit.Neck8MinRLimitz

    Neck8MaxRLimit = Neck8MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck8MaxRLimitx = Neck8MaxRLimit.Neck8MaxRLimitx
    Neck8MaxRLimity = Neck8MaxRLimit.Neck8MaxRLimity
    Neck8MaxRLimitz = Neck8MaxRLimit.Neck8MaxRLimitz

    Neck8MinRLimitEnablex = BoolField(default_value=False)

    Neck8MinRLimitEnabley = BoolField(default_value=False)

    Neck8MinRLimitEnablez = BoolField(default_value=False)

    Neck8MaxRLimitEnablex = BoolField(default_value=False)

    Neck8MaxRLimitEnabley = BoolField(default_value=False)

    Neck8MaxRLimitEnablez = BoolField(default_value=False)

    Neck9 = MessageField()

    Neck9T = Neck9TField(default_value=(0.0, 0.0, 0.0))
    Neck9Tx = Neck9T.Neck9Tx
    Neck9Ty = Neck9T.Neck9Ty
    Neck9Tz = Neck9T.Neck9Tz

    Neck9R = Neck9RField(default_value=(0.0, 0.0, 0.0))
    Neck9Rx = Neck9R.Neck9Rx
    Neck9Ry = Neck9R.Neck9Ry
    Neck9Rz = Neck9R.Neck9Rz

    Neck9S = Neck9SField(default_value=(1.0, 1.0, 1.0))
    Neck9Sx = Neck9S.Neck9Sx
    Neck9Sy = Neck9S.Neck9Sy
    Neck9Sz = Neck9S.Neck9Sz

    Neck9RotateOrder = Neck9RotateOrderEnumField(default_value=0)

    Neck9RotateAxis = Neck9RotateAxisField(default_value=(0.0, 0.0, 0.0))
    Neck9RotateAxisx = Neck9RotateAxis.Neck9RotateAxisx
    Neck9RotateAxisy = Neck9RotateAxis.Neck9RotateAxisy
    Neck9RotateAxisz = Neck9RotateAxis.Neck9RotateAxisz

    Neck9JointOrient = Neck9JointOrientField(default_value=(0.0, 0.0, 0.0))
    Neck9JointOrientx = Neck9JointOrient.Neck9JointOrientx
    Neck9JointOrienty = Neck9JointOrient.Neck9JointOrienty
    Neck9JointOrientz = Neck9JointOrient.Neck9JointOrientz

    Neck9MinRLimit = Neck9MinRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck9MinRLimitx = Neck9MinRLimit.Neck9MinRLimitx
    Neck9MinRLimity = Neck9MinRLimit.Neck9MinRLimity
    Neck9MinRLimitz = Neck9MinRLimit.Neck9MinRLimitz

    Neck9MaxRLimit = Neck9MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    Neck9MaxRLimitx = Neck9MaxRLimit.Neck9MaxRLimitx
    Neck9MaxRLimity = Neck9MaxRLimit.Neck9MaxRLimity
    Neck9MaxRLimitz = Neck9MaxRLimit.Neck9MaxRLimitz

    Neck9MinRLimitEnablex = BoolField(default_value=False)

    Neck9MinRLimitEnabley = BoolField(default_value=False)

    Neck9MinRLimitEnablez = BoolField(default_value=False)

    Neck9MaxRLimitEnablex = BoolField(default_value=False)

    Neck9MaxRLimitEnabley = BoolField(default_value=False)

    Neck9MaxRLimitEnablez = BoolField(default_value=False)

    LeftUpLegRoll = MessageField()

    LeftUpLegRollT = LeftUpLegRollTField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegRollTx = LeftUpLegRollT.LeftUpLegRollTx
    LeftUpLegRollTy = LeftUpLegRollT.LeftUpLegRollTy
    LeftUpLegRollTz = LeftUpLegRollT.LeftUpLegRollTz

    LeftUpLegRollR = LeftUpLegRollRField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegRollRx = LeftUpLegRollR.LeftUpLegRollRx
    LeftUpLegRollRy = LeftUpLegRollR.LeftUpLegRollRy
    LeftUpLegRollRz = LeftUpLegRollR.LeftUpLegRollRz

    LeftUpLegRollS = LeftUpLegRollSField(default_value=(1.0, 1.0, 1.0))
    LeftUpLegRollSx = LeftUpLegRollS.LeftUpLegRollSx
    LeftUpLegRollSy = LeftUpLegRollS.LeftUpLegRollSy
    LeftUpLegRollSz = LeftUpLegRollS.LeftUpLegRollSz

    LeftUpLegRollRotateOrder = LeftUpLegRollRotateOrderEnumField(default_value=0)

    LeftUpLegRollRotateAxis = LeftUpLegRollRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegRollRotateAxisx = LeftUpLegRollRotateAxis.LeftUpLegRollRotateAxisx
    LeftUpLegRollRotateAxisy = LeftUpLegRollRotateAxis.LeftUpLegRollRotateAxisy
    LeftUpLegRollRotateAxisz = LeftUpLegRollRotateAxis.LeftUpLegRollRotateAxisz

    LeftUpLegRollJointOrient = LeftUpLegRollJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegRollJointOrientx = LeftUpLegRollJointOrient.LeftUpLegRollJointOrientx
    LeftUpLegRollJointOrienty = LeftUpLegRollJointOrient.LeftUpLegRollJointOrienty
    LeftUpLegRollJointOrientz = LeftUpLegRollJointOrient.LeftUpLegRollJointOrientz

    LeftUpLegRollMinRLimit = LeftUpLegRollMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegRollMinRLimitx = LeftUpLegRollMinRLimit.LeftUpLegRollMinRLimitx
    LeftUpLegRollMinRLimity = LeftUpLegRollMinRLimit.LeftUpLegRollMinRLimity
    LeftUpLegRollMinRLimitz = LeftUpLegRollMinRLimit.LeftUpLegRollMinRLimitz

    LeftUpLegRollMaxRLimit = LeftUpLegRollMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegRollMaxRLimitx = LeftUpLegRollMaxRLimit.LeftUpLegRollMaxRLimitx
    LeftUpLegRollMaxRLimity = LeftUpLegRollMaxRLimit.LeftUpLegRollMaxRLimity
    LeftUpLegRollMaxRLimitz = LeftUpLegRollMaxRLimit.LeftUpLegRollMaxRLimitz

    LeftUpLegRollMinRLimitEnablex = BoolField(default_value=False)

    LeftUpLegRollMinRLimitEnabley = BoolField(default_value=False)

    LeftUpLegRollMinRLimitEnablez = BoolField(default_value=False)

    LeftUpLegRollMaxRLimitEnablex = BoolField(default_value=False)

    LeftUpLegRollMaxRLimitEnabley = BoolField(default_value=False)

    LeftUpLegRollMaxRLimitEnablez = BoolField(default_value=False)

    LeftLegRoll = MessageField()

    LeftLegRollT = LeftLegRollTField(default_value=(0.0, 0.0, 0.0))
    LeftLegRollTx = LeftLegRollT.LeftLegRollTx
    LeftLegRollTy = LeftLegRollT.LeftLegRollTy
    LeftLegRollTz = LeftLegRollT.LeftLegRollTz

    LeftLegRollR = LeftLegRollRField(default_value=(0.0, 0.0, 0.0))
    LeftLegRollRx = LeftLegRollR.LeftLegRollRx
    LeftLegRollRy = LeftLegRollR.LeftLegRollRy
    LeftLegRollRz = LeftLegRollR.LeftLegRollRz

    LeftLegRollS = LeftLegRollSField(default_value=(1.0, 1.0, 1.0))
    LeftLegRollSx = LeftLegRollS.LeftLegRollSx
    LeftLegRollSy = LeftLegRollS.LeftLegRollSy
    LeftLegRollSz = LeftLegRollS.LeftLegRollSz

    LeftLegRollRotateOrder = LeftLegRollRotateOrderEnumField(default_value=0)

    LeftLegRollRotateAxis = LeftLegRollRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftLegRollRotateAxisx = LeftLegRollRotateAxis.LeftLegRollRotateAxisx
    LeftLegRollRotateAxisy = LeftLegRollRotateAxis.LeftLegRollRotateAxisy
    LeftLegRollRotateAxisz = LeftLegRollRotateAxis.LeftLegRollRotateAxisz

    LeftLegRollJointOrient = LeftLegRollJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftLegRollJointOrientx = LeftLegRollJointOrient.LeftLegRollJointOrientx
    LeftLegRollJointOrienty = LeftLegRollJointOrient.LeftLegRollJointOrienty
    LeftLegRollJointOrientz = LeftLegRollJointOrient.LeftLegRollJointOrientz

    LeftLegRollMinRLimit = LeftLegRollMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftLegRollMinRLimitx = LeftLegRollMinRLimit.LeftLegRollMinRLimitx
    LeftLegRollMinRLimity = LeftLegRollMinRLimit.LeftLegRollMinRLimity
    LeftLegRollMinRLimitz = LeftLegRollMinRLimit.LeftLegRollMinRLimitz

    LeftLegRollMaxRLimit = LeftLegRollMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftLegRollMaxRLimitx = LeftLegRollMaxRLimit.LeftLegRollMaxRLimitx
    LeftLegRollMaxRLimity = LeftLegRollMaxRLimit.LeftLegRollMaxRLimity
    LeftLegRollMaxRLimitz = LeftLegRollMaxRLimit.LeftLegRollMaxRLimitz

    LeftLegRollMinRLimitEnablex = BoolField(default_value=False)

    LeftLegRollMinRLimitEnabley = BoolField(default_value=False)

    LeftLegRollMinRLimitEnablez = BoolField(default_value=False)

    LeftLegRollMaxRLimitEnablex = BoolField(default_value=False)

    LeftLegRollMaxRLimitEnabley = BoolField(default_value=False)

    LeftLegRollMaxRLimitEnablez = BoolField(default_value=False)

    RightUpLegRoll = MessageField()

    RightUpLegRollT = RightUpLegRollTField(default_value=(0.0, 0.0, 0.0))
    RightUpLegRollTx = RightUpLegRollT.RightUpLegRollTx
    RightUpLegRollTy = RightUpLegRollT.RightUpLegRollTy
    RightUpLegRollTz = RightUpLegRollT.RightUpLegRollTz

    RightUpLegRollR = RightUpLegRollRField(default_value=(0.0, 0.0, 0.0))
    RightUpLegRollRx = RightUpLegRollR.RightUpLegRollRx
    RightUpLegRollRy = RightUpLegRollR.RightUpLegRollRy
    RightUpLegRollRz = RightUpLegRollR.RightUpLegRollRz

    RightUpLegRollS = RightUpLegRollSField(default_value=(1.0, 1.0, 1.0))
    RightUpLegRollSx = RightUpLegRollS.RightUpLegRollSx
    RightUpLegRollSy = RightUpLegRollS.RightUpLegRollSy
    RightUpLegRollSz = RightUpLegRollS.RightUpLegRollSz

    RightUpLegRollRotateOrder = RightUpLegRollRotateOrderEnumField(default_value=0)

    RightUpLegRollRotateAxis = RightUpLegRollRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightUpLegRollRotateAxisx = RightUpLegRollRotateAxis.RightUpLegRollRotateAxisx
    RightUpLegRollRotateAxisy = RightUpLegRollRotateAxis.RightUpLegRollRotateAxisy
    RightUpLegRollRotateAxisz = RightUpLegRollRotateAxis.RightUpLegRollRotateAxisz

    RightUpLegRollJointOrient = RightUpLegRollJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightUpLegRollJointOrientx = RightUpLegRollJointOrient.RightUpLegRollJointOrientx
    RightUpLegRollJointOrienty = RightUpLegRollJointOrient.RightUpLegRollJointOrienty
    RightUpLegRollJointOrientz = RightUpLegRollJointOrient.RightUpLegRollJointOrientz

    RightUpLegRollMinRLimit = RightUpLegRollMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightUpLegRollMinRLimitx = RightUpLegRollMinRLimit.RightUpLegRollMinRLimitx
    RightUpLegRollMinRLimity = RightUpLegRollMinRLimit.RightUpLegRollMinRLimity
    RightUpLegRollMinRLimitz = RightUpLegRollMinRLimit.RightUpLegRollMinRLimitz

    RightUpLegRollMaxRLimit = RightUpLegRollMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightUpLegRollMaxRLimitx = RightUpLegRollMaxRLimit.RightUpLegRollMaxRLimitx
    RightUpLegRollMaxRLimity = RightUpLegRollMaxRLimit.RightUpLegRollMaxRLimity
    RightUpLegRollMaxRLimitz = RightUpLegRollMaxRLimit.RightUpLegRollMaxRLimitz

    RightUpLegRollMinRLimitEnablex = BoolField(default_value=False)

    RightUpLegRollMinRLimitEnabley = BoolField(default_value=False)

    RightUpLegRollMinRLimitEnablez = BoolField(default_value=False)

    RightUpLegRollMaxRLimitEnablex = BoolField(default_value=False)

    RightUpLegRollMaxRLimitEnabley = BoolField(default_value=False)

    RightUpLegRollMaxRLimitEnablez = BoolField(default_value=False)

    RightLegRoll = MessageField()

    RightLegRollT = RightLegRollTField(default_value=(0.0, 0.0, 0.0))
    RightLegRollTx = RightLegRollT.RightLegRollTx
    RightLegRollTy = RightLegRollT.RightLegRollTy
    RightLegRollTz = RightLegRollT.RightLegRollTz

    RightLegRollR = RightLegRollRField(default_value=(0.0, 0.0, 0.0))
    RightLegRollRx = RightLegRollR.RightLegRollRx
    RightLegRollRy = RightLegRollR.RightLegRollRy
    RightLegRollRz = RightLegRollR.RightLegRollRz

    RightLegRollS = RightLegRollSField(default_value=(1.0, 1.0, 1.0))
    RightLegRollSx = RightLegRollS.RightLegRollSx
    RightLegRollSy = RightLegRollS.RightLegRollSy
    RightLegRollSz = RightLegRollS.RightLegRollSz

    RightLegRollRotateOrder = RightLegRollRotateOrderEnumField(default_value=0)

    RightLegRollRotateAxis = RightLegRollRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightLegRollRotateAxisx = RightLegRollRotateAxis.RightLegRollRotateAxisx
    RightLegRollRotateAxisy = RightLegRollRotateAxis.RightLegRollRotateAxisy
    RightLegRollRotateAxisz = RightLegRollRotateAxis.RightLegRollRotateAxisz

    RightLegRollJointOrient = RightLegRollJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightLegRollJointOrientx = RightLegRollJointOrient.RightLegRollJointOrientx
    RightLegRollJointOrienty = RightLegRollJointOrient.RightLegRollJointOrienty
    RightLegRollJointOrientz = RightLegRollJointOrient.RightLegRollJointOrientz

    RightLegRollMinRLimit = RightLegRollMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightLegRollMinRLimitx = RightLegRollMinRLimit.RightLegRollMinRLimitx
    RightLegRollMinRLimity = RightLegRollMinRLimit.RightLegRollMinRLimity
    RightLegRollMinRLimitz = RightLegRollMinRLimit.RightLegRollMinRLimitz

    RightLegRollMaxRLimit = RightLegRollMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightLegRollMaxRLimitx = RightLegRollMaxRLimit.RightLegRollMaxRLimitx
    RightLegRollMaxRLimity = RightLegRollMaxRLimit.RightLegRollMaxRLimity
    RightLegRollMaxRLimitz = RightLegRollMaxRLimit.RightLegRollMaxRLimitz

    RightLegRollMinRLimitEnablex = BoolField(default_value=False)

    RightLegRollMinRLimitEnabley = BoolField(default_value=False)

    RightLegRollMinRLimitEnablez = BoolField(default_value=False)

    RightLegRollMaxRLimitEnablex = BoolField(default_value=False)

    RightLegRollMaxRLimitEnabley = BoolField(default_value=False)

    RightLegRollMaxRLimitEnablez = BoolField(default_value=False)

    LeftArmRoll = MessageField()

    LeftArmRollT = LeftArmRollTField(default_value=(0.0, 0.0, 0.0))
    LeftArmRollTx = LeftArmRollT.LeftArmRollTx
    LeftArmRollTy = LeftArmRollT.LeftArmRollTy
    LeftArmRollTz = LeftArmRollT.LeftArmRollTz

    LeftArmRollR = LeftArmRollRField(default_value=(0.0, 0.0, 0.0))
    LeftArmRollRx = LeftArmRollR.LeftArmRollRx
    LeftArmRollRy = LeftArmRollR.LeftArmRollRy
    LeftArmRollRz = LeftArmRollR.LeftArmRollRz

    LeftArmRollS = LeftArmRollSField(default_value=(1.0, 1.0, 1.0))
    LeftArmRollSx = LeftArmRollS.LeftArmRollSx
    LeftArmRollSy = LeftArmRollS.LeftArmRollSy
    LeftArmRollSz = LeftArmRollS.LeftArmRollSz

    LeftArmRollRotateOrder = LeftArmRollRotateOrderEnumField(default_value=0)

    LeftArmRollRotateAxis = LeftArmRollRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftArmRollRotateAxisx = LeftArmRollRotateAxis.LeftArmRollRotateAxisx
    LeftArmRollRotateAxisy = LeftArmRollRotateAxis.LeftArmRollRotateAxisy
    LeftArmRollRotateAxisz = LeftArmRollRotateAxis.LeftArmRollRotateAxisz

    LeftArmRollJointOrient = LeftArmRollJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftArmRollJointOrientx = LeftArmRollJointOrient.LeftArmRollJointOrientx
    LeftArmRollJointOrienty = LeftArmRollJointOrient.LeftArmRollJointOrienty
    LeftArmRollJointOrientz = LeftArmRollJointOrient.LeftArmRollJointOrientz

    LeftArmRollMinRLimit = LeftArmRollMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftArmRollMinRLimitx = LeftArmRollMinRLimit.LeftArmRollMinRLimitx
    LeftArmRollMinRLimity = LeftArmRollMinRLimit.LeftArmRollMinRLimity
    LeftArmRollMinRLimitz = LeftArmRollMinRLimit.LeftArmRollMinRLimitz

    LeftArmRollMaxRLimit = LeftArmRollMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftArmRollMaxRLimitx = LeftArmRollMaxRLimit.LeftArmRollMaxRLimitx
    LeftArmRollMaxRLimity = LeftArmRollMaxRLimit.LeftArmRollMaxRLimity
    LeftArmRollMaxRLimitz = LeftArmRollMaxRLimit.LeftArmRollMaxRLimitz

    LeftArmRollMinRLimitEnablex = BoolField(default_value=False)

    LeftArmRollMinRLimitEnabley = BoolField(default_value=False)

    LeftArmRollMinRLimitEnablez = BoolField(default_value=False)

    LeftArmRollMaxRLimitEnablex = BoolField(default_value=False)

    LeftArmRollMaxRLimitEnabley = BoolField(default_value=False)

    LeftArmRollMaxRLimitEnablez = BoolField(default_value=False)

    LeftForeArmRoll = MessageField()

    LeftForeArmRollT = LeftForeArmRollTField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmRollTx = LeftForeArmRollT.LeftForeArmRollTx
    LeftForeArmRollTy = LeftForeArmRollT.LeftForeArmRollTy
    LeftForeArmRollTz = LeftForeArmRollT.LeftForeArmRollTz

    LeftForeArmRollR = LeftForeArmRollRField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmRollRx = LeftForeArmRollR.LeftForeArmRollRx
    LeftForeArmRollRy = LeftForeArmRollR.LeftForeArmRollRy
    LeftForeArmRollRz = LeftForeArmRollR.LeftForeArmRollRz

    LeftForeArmRollS = LeftForeArmRollSField(default_value=(1.0, 1.0, 1.0))
    LeftForeArmRollSx = LeftForeArmRollS.LeftForeArmRollSx
    LeftForeArmRollSy = LeftForeArmRollS.LeftForeArmRollSy
    LeftForeArmRollSz = LeftForeArmRollS.LeftForeArmRollSz

    LeftForeArmRollRotateOrder = LeftForeArmRollRotateOrderEnumField(default_value=0)

    LeftForeArmRollRotateAxis = LeftForeArmRollRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmRollRotateAxisx = LeftForeArmRollRotateAxis.LeftForeArmRollRotateAxisx
    LeftForeArmRollRotateAxisy = LeftForeArmRollRotateAxis.LeftForeArmRollRotateAxisy
    LeftForeArmRollRotateAxisz = LeftForeArmRollRotateAxis.LeftForeArmRollRotateAxisz

    LeftForeArmRollJointOrient = LeftForeArmRollJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmRollJointOrientx = LeftForeArmRollJointOrient.LeftForeArmRollJointOrientx
    LeftForeArmRollJointOrienty = LeftForeArmRollJointOrient.LeftForeArmRollJointOrienty
    LeftForeArmRollJointOrientz = LeftForeArmRollJointOrient.LeftForeArmRollJointOrientz

    LeftForeArmRollMinRLimit = LeftForeArmRollMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmRollMinRLimitx = LeftForeArmRollMinRLimit.LeftForeArmRollMinRLimitx
    LeftForeArmRollMinRLimity = LeftForeArmRollMinRLimit.LeftForeArmRollMinRLimity
    LeftForeArmRollMinRLimitz = LeftForeArmRollMinRLimit.LeftForeArmRollMinRLimitz

    LeftForeArmRollMaxRLimit = LeftForeArmRollMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmRollMaxRLimitx = LeftForeArmRollMaxRLimit.LeftForeArmRollMaxRLimitx
    LeftForeArmRollMaxRLimity = LeftForeArmRollMaxRLimit.LeftForeArmRollMaxRLimity
    LeftForeArmRollMaxRLimitz = LeftForeArmRollMaxRLimit.LeftForeArmRollMaxRLimitz

    LeftForeArmRollMinRLimitEnablex = BoolField(default_value=False)

    LeftForeArmRollMinRLimitEnabley = BoolField(default_value=False)

    LeftForeArmRollMinRLimitEnablez = BoolField(default_value=False)

    LeftForeArmRollMaxRLimitEnablex = BoolField(default_value=False)

    LeftForeArmRollMaxRLimitEnabley = BoolField(default_value=False)

    LeftForeArmRollMaxRLimitEnablez = BoolField(default_value=False)

    RightArmRoll = MessageField()

    RightArmRollT = RightArmRollTField(default_value=(0.0, 0.0, 0.0))
    RightArmRollTx = RightArmRollT.RightArmRollTx
    RightArmRollTy = RightArmRollT.RightArmRollTy
    RightArmRollTz = RightArmRollT.RightArmRollTz

    RightArmRollR = RightArmRollRField(default_value=(0.0, 0.0, 0.0))
    RightArmRollRx = RightArmRollR.RightArmRollRx
    RightArmRollRy = RightArmRollR.RightArmRollRy
    RightArmRollRz = RightArmRollR.RightArmRollRz

    RightArmRollS = RightArmRollSField(default_value=(1.0, 1.0, 1.0))
    RightArmRollSx = RightArmRollS.RightArmRollSx
    RightArmRollSy = RightArmRollS.RightArmRollSy
    RightArmRollSz = RightArmRollS.RightArmRollSz

    RightArmRollRotateOrder = RightArmRollRotateOrderEnumField(default_value=0)

    RightArmRollRotateAxis = RightArmRollRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightArmRollRotateAxisx = RightArmRollRotateAxis.RightArmRollRotateAxisx
    RightArmRollRotateAxisy = RightArmRollRotateAxis.RightArmRollRotateAxisy
    RightArmRollRotateAxisz = RightArmRollRotateAxis.RightArmRollRotateAxisz

    RightArmRollJointOrient = RightArmRollJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightArmRollJointOrientx = RightArmRollJointOrient.RightArmRollJointOrientx
    RightArmRollJointOrienty = RightArmRollJointOrient.RightArmRollJointOrienty
    RightArmRollJointOrientz = RightArmRollJointOrient.RightArmRollJointOrientz

    RightArmRollMinRLimit = RightArmRollMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightArmRollMinRLimitx = RightArmRollMinRLimit.RightArmRollMinRLimitx
    RightArmRollMinRLimity = RightArmRollMinRLimit.RightArmRollMinRLimity
    RightArmRollMinRLimitz = RightArmRollMinRLimit.RightArmRollMinRLimitz

    RightArmRollMaxRLimit = RightArmRollMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightArmRollMaxRLimitx = RightArmRollMaxRLimit.RightArmRollMaxRLimitx
    RightArmRollMaxRLimity = RightArmRollMaxRLimit.RightArmRollMaxRLimity
    RightArmRollMaxRLimitz = RightArmRollMaxRLimit.RightArmRollMaxRLimitz

    RightArmRollMinRLimitEnablex = BoolField(default_value=False)

    RightArmRollMinRLimitEnabley = BoolField(default_value=False)

    RightArmRollMinRLimitEnablez = BoolField(default_value=False)

    RightArmRollMaxRLimitEnablex = BoolField(default_value=False)

    RightArmRollMaxRLimitEnabley = BoolField(default_value=False)

    RightArmRollMaxRLimitEnablez = BoolField(default_value=False)

    RightForeArmRoll = MessageField()

    RightForeArmRollT = RightForeArmRollTField(default_value=(0.0, 0.0, 0.0))
    RightForeArmRollTx = RightForeArmRollT.RightForeArmRollTx
    RightForeArmRollTy = RightForeArmRollT.RightForeArmRollTy
    RightForeArmRollTz = RightForeArmRollT.RightForeArmRollTz

    RightForeArmRollR = RightForeArmRollRField(default_value=(0.0, 0.0, 0.0))
    RightForeArmRollRx = RightForeArmRollR.RightForeArmRollRx
    RightForeArmRollRy = RightForeArmRollR.RightForeArmRollRy
    RightForeArmRollRz = RightForeArmRollR.RightForeArmRollRz

    RightForeArmRollS = RightForeArmRollSField(default_value=(1.0, 1.0, 1.0))
    RightForeArmRollSx = RightForeArmRollS.RightForeArmRollSx
    RightForeArmRollSy = RightForeArmRollS.RightForeArmRollSy
    RightForeArmRollSz = RightForeArmRollS.RightForeArmRollSz

    RightForeArmRollRotateOrder = RightForeArmRollRotateOrderEnumField(default_value=0)

    RightForeArmRollRotateAxis = RightForeArmRollRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightForeArmRollRotateAxisx = RightForeArmRollRotateAxis.RightForeArmRollRotateAxisx
    RightForeArmRollRotateAxisy = RightForeArmRollRotateAxis.RightForeArmRollRotateAxisy
    RightForeArmRollRotateAxisz = RightForeArmRollRotateAxis.RightForeArmRollRotateAxisz

    RightForeArmRollJointOrient = RightForeArmRollJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightForeArmRollJointOrientx = RightForeArmRollJointOrient.RightForeArmRollJointOrientx
    RightForeArmRollJointOrienty = RightForeArmRollJointOrient.RightForeArmRollJointOrienty
    RightForeArmRollJointOrientz = RightForeArmRollJointOrient.RightForeArmRollJointOrientz

    RightForeArmRollMinRLimit = RightForeArmRollMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightForeArmRollMinRLimitx = RightForeArmRollMinRLimit.RightForeArmRollMinRLimitx
    RightForeArmRollMinRLimity = RightForeArmRollMinRLimit.RightForeArmRollMinRLimity
    RightForeArmRollMinRLimitz = RightForeArmRollMinRLimit.RightForeArmRollMinRLimitz

    RightForeArmRollMaxRLimit = RightForeArmRollMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightForeArmRollMaxRLimitx = RightForeArmRollMaxRLimit.RightForeArmRollMaxRLimitx
    RightForeArmRollMaxRLimity = RightForeArmRollMaxRLimit.RightForeArmRollMaxRLimity
    RightForeArmRollMaxRLimitz = RightForeArmRollMaxRLimit.RightForeArmRollMaxRLimitz

    RightForeArmRollMinRLimitEnablex = BoolField(default_value=False)

    RightForeArmRollMinRLimitEnabley = BoolField(default_value=False)

    RightForeArmRollMinRLimitEnablez = BoolField(default_value=False)

    RightForeArmRollMaxRLimitEnablex = BoolField(default_value=False)

    RightForeArmRollMaxRLimitEnabley = BoolField(default_value=False)

    RightForeArmRollMaxRLimitEnablez = BoolField(default_value=False)

    HipsTranslation = MessageField()

    HipsTranslationT = HipsTranslationTField(default_value=(0.0, 0.0, 0.0))
    HipsTranslationTx = HipsTranslationT.HipsTranslationTx
    HipsTranslationTy = HipsTranslationT.HipsTranslationTy
    HipsTranslationTz = HipsTranslationT.HipsTranslationTz

    HipsTranslationR = HipsTranslationRField(default_value=(0.0, 0.0, 0.0))
    HipsTranslationRx = HipsTranslationR.HipsTranslationRx
    HipsTranslationRy = HipsTranslationR.HipsTranslationRy
    HipsTranslationRz = HipsTranslationR.HipsTranslationRz

    HipsTranslationS = HipsTranslationSField(default_value=(1.0, 1.0, 1.0))
    HipsTranslationSx = HipsTranslationS.HipsTranslationSx
    HipsTranslationSy = HipsTranslationS.HipsTranslationSy
    HipsTranslationSz = HipsTranslationS.HipsTranslationSz

    HipsTranslationRotateOrder = HipsTranslationRotateOrderEnumField(default_value=0)

    HipsTranslationRotateAxis = HipsTranslationRotateAxisField(default_value=(0.0, 0.0, 0.0))
    HipsTranslationRotateAxisx = HipsTranslationRotateAxis.HipsTranslationRotateAxisx
    HipsTranslationRotateAxisy = HipsTranslationRotateAxis.HipsTranslationRotateAxisy
    HipsTranslationRotateAxisz = HipsTranslationRotateAxis.HipsTranslationRotateAxisz

    HipsTranslationJointOrient = HipsTranslationJointOrientField(default_value=(0.0, 0.0, 0.0))
    HipsTranslationJointOrientx = HipsTranslationJointOrient.HipsTranslationJointOrientx
    HipsTranslationJointOrienty = HipsTranslationJointOrient.HipsTranslationJointOrienty
    HipsTranslationJointOrientz = HipsTranslationJointOrient.HipsTranslationJointOrientz

    HipsTranslationMinRLimit = HipsTranslationMinRLimitField(default_value=(0.0, 0.0, 0.0))
    HipsTranslationMinRLimitx = HipsTranslationMinRLimit.HipsTranslationMinRLimitx
    HipsTranslationMinRLimity = HipsTranslationMinRLimit.HipsTranslationMinRLimity
    HipsTranslationMinRLimitz = HipsTranslationMinRLimit.HipsTranslationMinRLimitz

    HipsTranslationMaxRLimit = HipsTranslationMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    HipsTranslationMaxRLimitx = HipsTranslationMaxRLimit.HipsTranslationMaxRLimitx
    HipsTranslationMaxRLimity = HipsTranslationMaxRLimit.HipsTranslationMaxRLimity
    HipsTranslationMaxRLimitz = HipsTranslationMaxRLimit.HipsTranslationMaxRLimitz

    HipsTranslationMinRLimitEnablex = BoolField(default_value=False)

    HipsTranslationMinRLimitEnabley = BoolField(default_value=False)

    HipsTranslationMinRLimitEnablez = BoolField(default_value=False)

    HipsTranslationMaxRLimitEnablex = BoolField(default_value=False)

    HipsTranslationMaxRLimitEnabley = BoolField(default_value=False)

    HipsTranslationMaxRLimitEnablez = BoolField(default_value=False)

    LeftHandThumb1 = MessageField()

    LeftHandThumb1T = LeftHandThumb1TField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb1Tx = LeftHandThumb1T.LeftHandThumb1Tx
    LeftHandThumb1Ty = LeftHandThumb1T.LeftHandThumb1Ty
    LeftHandThumb1Tz = LeftHandThumb1T.LeftHandThumb1Tz

    LeftHandThumb1R = LeftHandThumb1RField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb1Rx = LeftHandThumb1R.LeftHandThumb1Rx
    LeftHandThumb1Ry = LeftHandThumb1R.LeftHandThumb1Ry
    LeftHandThumb1Rz = LeftHandThumb1R.LeftHandThumb1Rz

    LeftHandThumb1S = LeftHandThumb1SField(default_value=(1.0, 1.0, 1.0))
    LeftHandThumb1Sx = LeftHandThumb1S.LeftHandThumb1Sx
    LeftHandThumb1Sy = LeftHandThumb1S.LeftHandThumb1Sy
    LeftHandThumb1Sz = LeftHandThumb1S.LeftHandThumb1Sz

    LeftHandThumb1RotateOrder = LeftHandThumb1RotateOrderEnumField(default_value=0)

    LeftHandThumb1RotateAxis = LeftHandThumb1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb1RotateAxisx = LeftHandThumb1RotateAxis.LeftHandThumb1RotateAxisx
    LeftHandThumb1RotateAxisy = LeftHandThumb1RotateAxis.LeftHandThumb1RotateAxisy
    LeftHandThumb1RotateAxisz = LeftHandThumb1RotateAxis.LeftHandThumb1RotateAxisz

    LeftHandThumb1JointOrient = LeftHandThumb1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb1JointOrientx = LeftHandThumb1JointOrient.LeftHandThumb1JointOrientx
    LeftHandThumb1JointOrienty = LeftHandThumb1JointOrient.LeftHandThumb1JointOrienty
    LeftHandThumb1JointOrientz = LeftHandThumb1JointOrient.LeftHandThumb1JointOrientz

    LeftHandThumb1MinRLimit = LeftHandThumb1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb1MinRLimitx = LeftHandThumb1MinRLimit.LeftHandThumb1MinRLimitx
    LeftHandThumb1MinRLimity = LeftHandThumb1MinRLimit.LeftHandThumb1MinRLimity
    LeftHandThumb1MinRLimitz = LeftHandThumb1MinRLimit.LeftHandThumb1MinRLimitz

    LeftHandThumb1MaxRLimit = LeftHandThumb1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb1MaxRLimitx = LeftHandThumb1MaxRLimit.LeftHandThumb1MaxRLimitx
    LeftHandThumb1MaxRLimity = LeftHandThumb1MaxRLimit.LeftHandThumb1MaxRLimity
    LeftHandThumb1MaxRLimitz = LeftHandThumb1MaxRLimit.LeftHandThumb1MaxRLimitz

    LeftHandThumb1MinRLimitEnablex = BoolField(default_value=False)

    LeftHandThumb1MinRLimitEnabley = BoolField(default_value=False)

    LeftHandThumb1MinRLimitEnablez = BoolField(default_value=False)

    LeftHandThumb1MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandThumb1MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandThumb1MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandThumb2 = MessageField()

    LeftHandThumb2T = LeftHandThumb2TField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb2Tx = LeftHandThumb2T.LeftHandThumb2Tx
    LeftHandThumb2Ty = LeftHandThumb2T.LeftHandThumb2Ty
    LeftHandThumb2Tz = LeftHandThumb2T.LeftHandThumb2Tz

    LeftHandThumb2R = LeftHandThumb2RField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb2Rx = LeftHandThumb2R.LeftHandThumb2Rx
    LeftHandThumb2Ry = LeftHandThumb2R.LeftHandThumb2Ry
    LeftHandThumb2Rz = LeftHandThumb2R.LeftHandThumb2Rz

    LeftHandThumb2S = LeftHandThumb2SField(default_value=(1.0, 1.0, 1.0))
    LeftHandThumb2Sx = LeftHandThumb2S.LeftHandThumb2Sx
    LeftHandThumb2Sy = LeftHandThumb2S.LeftHandThumb2Sy
    LeftHandThumb2Sz = LeftHandThumb2S.LeftHandThumb2Sz

    LeftHandThumb2RotateOrder = LeftHandThumb2RotateOrderEnumField(default_value=0)

    LeftHandThumb2RotateAxis = LeftHandThumb2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb2RotateAxisx = LeftHandThumb2RotateAxis.LeftHandThumb2RotateAxisx
    LeftHandThumb2RotateAxisy = LeftHandThumb2RotateAxis.LeftHandThumb2RotateAxisy
    LeftHandThumb2RotateAxisz = LeftHandThumb2RotateAxis.LeftHandThumb2RotateAxisz

    LeftHandThumb2JointOrient = LeftHandThumb2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb2JointOrientx = LeftHandThumb2JointOrient.LeftHandThumb2JointOrientx
    LeftHandThumb2JointOrienty = LeftHandThumb2JointOrient.LeftHandThumb2JointOrienty
    LeftHandThumb2JointOrientz = LeftHandThumb2JointOrient.LeftHandThumb2JointOrientz

    LeftHandThumb2MinRLimit = LeftHandThumb2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb2MinRLimitx = LeftHandThumb2MinRLimit.LeftHandThumb2MinRLimitx
    LeftHandThumb2MinRLimity = LeftHandThumb2MinRLimit.LeftHandThumb2MinRLimity
    LeftHandThumb2MinRLimitz = LeftHandThumb2MinRLimit.LeftHandThumb2MinRLimitz

    LeftHandThumb2MaxRLimit = LeftHandThumb2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb2MaxRLimitx = LeftHandThumb2MaxRLimit.LeftHandThumb2MaxRLimitx
    LeftHandThumb2MaxRLimity = LeftHandThumb2MaxRLimit.LeftHandThumb2MaxRLimity
    LeftHandThumb2MaxRLimitz = LeftHandThumb2MaxRLimit.LeftHandThumb2MaxRLimitz

    LeftHandThumb2MinRLimitEnablex = BoolField(default_value=False)

    LeftHandThumb2MinRLimitEnabley = BoolField(default_value=False)

    LeftHandThumb2MinRLimitEnablez = BoolField(default_value=False)

    LeftHandThumb2MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandThumb2MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandThumb2MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandThumb3 = MessageField()

    LeftHandThumb3T = LeftHandThumb3TField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb3Tx = LeftHandThumb3T.LeftHandThumb3Tx
    LeftHandThumb3Ty = LeftHandThumb3T.LeftHandThumb3Ty
    LeftHandThumb3Tz = LeftHandThumb3T.LeftHandThumb3Tz

    LeftHandThumb3R = LeftHandThumb3RField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb3Rx = LeftHandThumb3R.LeftHandThumb3Rx
    LeftHandThumb3Ry = LeftHandThumb3R.LeftHandThumb3Ry
    LeftHandThumb3Rz = LeftHandThumb3R.LeftHandThumb3Rz

    LeftHandThumb3S = LeftHandThumb3SField(default_value=(1.0, 1.0, 1.0))
    LeftHandThumb3Sx = LeftHandThumb3S.LeftHandThumb3Sx
    LeftHandThumb3Sy = LeftHandThumb3S.LeftHandThumb3Sy
    LeftHandThumb3Sz = LeftHandThumb3S.LeftHandThumb3Sz

    LeftHandThumb3RotateOrder = LeftHandThumb3RotateOrderEnumField(default_value=0)

    LeftHandThumb3RotateAxis = LeftHandThumb3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb3RotateAxisx = LeftHandThumb3RotateAxis.LeftHandThumb3RotateAxisx
    LeftHandThumb3RotateAxisy = LeftHandThumb3RotateAxis.LeftHandThumb3RotateAxisy
    LeftHandThumb3RotateAxisz = LeftHandThumb3RotateAxis.LeftHandThumb3RotateAxisz

    LeftHandThumb3JointOrient = LeftHandThumb3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb3JointOrientx = LeftHandThumb3JointOrient.LeftHandThumb3JointOrientx
    LeftHandThumb3JointOrienty = LeftHandThumb3JointOrient.LeftHandThumb3JointOrienty
    LeftHandThumb3JointOrientz = LeftHandThumb3JointOrient.LeftHandThumb3JointOrientz

    LeftHandThumb3MinRLimit = LeftHandThumb3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb3MinRLimitx = LeftHandThumb3MinRLimit.LeftHandThumb3MinRLimitx
    LeftHandThumb3MinRLimity = LeftHandThumb3MinRLimit.LeftHandThumb3MinRLimity
    LeftHandThumb3MinRLimitz = LeftHandThumb3MinRLimit.LeftHandThumb3MinRLimitz

    LeftHandThumb3MaxRLimit = LeftHandThumb3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb3MaxRLimitx = LeftHandThumb3MaxRLimit.LeftHandThumb3MaxRLimitx
    LeftHandThumb3MaxRLimity = LeftHandThumb3MaxRLimit.LeftHandThumb3MaxRLimity
    LeftHandThumb3MaxRLimitz = LeftHandThumb3MaxRLimit.LeftHandThumb3MaxRLimitz

    LeftHandThumb3MinRLimitEnablex = BoolField(default_value=False)

    LeftHandThumb3MinRLimitEnabley = BoolField(default_value=False)

    LeftHandThumb3MinRLimitEnablez = BoolField(default_value=False)

    LeftHandThumb3MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandThumb3MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandThumb3MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandThumb4 = MessageField()

    LeftHandThumb4T = LeftHandThumb4TField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb4Tx = LeftHandThumb4T.LeftHandThumb4Tx
    LeftHandThumb4Ty = LeftHandThumb4T.LeftHandThumb4Ty
    LeftHandThumb4Tz = LeftHandThumb4T.LeftHandThumb4Tz

    LeftHandThumb4R = LeftHandThumb4RField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb4Rx = LeftHandThumb4R.LeftHandThumb4Rx
    LeftHandThumb4Ry = LeftHandThumb4R.LeftHandThumb4Ry
    LeftHandThumb4Rz = LeftHandThumb4R.LeftHandThumb4Rz

    LeftHandThumb4S = LeftHandThumb4SField(default_value=(1.0, 1.0, 1.0))
    LeftHandThumb4Sx = LeftHandThumb4S.LeftHandThumb4Sx
    LeftHandThumb4Sy = LeftHandThumb4S.LeftHandThumb4Sy
    LeftHandThumb4Sz = LeftHandThumb4S.LeftHandThumb4Sz

    LeftHandThumb4RotateOrder = LeftHandThumb4RotateOrderEnumField(default_value=0)

    LeftHandThumb4RotateAxis = LeftHandThumb4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb4RotateAxisx = LeftHandThumb4RotateAxis.LeftHandThumb4RotateAxisx
    LeftHandThumb4RotateAxisy = LeftHandThumb4RotateAxis.LeftHandThumb4RotateAxisy
    LeftHandThumb4RotateAxisz = LeftHandThumb4RotateAxis.LeftHandThumb4RotateAxisz

    LeftHandThumb4JointOrient = LeftHandThumb4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb4JointOrientx = LeftHandThumb4JointOrient.LeftHandThumb4JointOrientx
    LeftHandThumb4JointOrienty = LeftHandThumb4JointOrient.LeftHandThumb4JointOrienty
    LeftHandThumb4JointOrientz = LeftHandThumb4JointOrient.LeftHandThumb4JointOrientz

    LeftHandThumb4MinRLimit = LeftHandThumb4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb4MinRLimitx = LeftHandThumb4MinRLimit.LeftHandThumb4MinRLimitx
    LeftHandThumb4MinRLimity = LeftHandThumb4MinRLimit.LeftHandThumb4MinRLimity
    LeftHandThumb4MinRLimitz = LeftHandThumb4MinRLimit.LeftHandThumb4MinRLimitz

    LeftHandThumb4MaxRLimit = LeftHandThumb4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb4MaxRLimitx = LeftHandThumb4MaxRLimit.LeftHandThumb4MaxRLimitx
    LeftHandThumb4MaxRLimity = LeftHandThumb4MaxRLimit.LeftHandThumb4MaxRLimity
    LeftHandThumb4MaxRLimitz = LeftHandThumb4MaxRLimit.LeftHandThumb4MaxRLimitz

    LeftHandThumb4MinRLimitEnablex = BoolField(default_value=False)

    LeftHandThumb4MinRLimitEnabley = BoolField(default_value=False)

    LeftHandThumb4MinRLimitEnablez = BoolField(default_value=False)

    LeftHandThumb4MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandThumb4MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandThumb4MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandIndex1 = MessageField()

    LeftHandIndex1T = LeftHandIndex1TField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex1Tx = LeftHandIndex1T.LeftHandIndex1Tx
    LeftHandIndex1Ty = LeftHandIndex1T.LeftHandIndex1Ty
    LeftHandIndex1Tz = LeftHandIndex1T.LeftHandIndex1Tz

    LeftHandIndex1R = LeftHandIndex1RField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex1Rx = LeftHandIndex1R.LeftHandIndex1Rx
    LeftHandIndex1Ry = LeftHandIndex1R.LeftHandIndex1Ry
    LeftHandIndex1Rz = LeftHandIndex1R.LeftHandIndex1Rz

    LeftHandIndex1S = LeftHandIndex1SField(default_value=(1.0, 1.0, 1.0))
    LeftHandIndex1Sx = LeftHandIndex1S.LeftHandIndex1Sx
    LeftHandIndex1Sy = LeftHandIndex1S.LeftHandIndex1Sy
    LeftHandIndex1Sz = LeftHandIndex1S.LeftHandIndex1Sz

    LeftHandIndex1RotateOrder = LeftHandIndex1RotateOrderEnumField(default_value=0)

    LeftHandIndex1RotateAxis = LeftHandIndex1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex1RotateAxisx = LeftHandIndex1RotateAxis.LeftHandIndex1RotateAxisx
    LeftHandIndex1RotateAxisy = LeftHandIndex1RotateAxis.LeftHandIndex1RotateAxisy
    LeftHandIndex1RotateAxisz = LeftHandIndex1RotateAxis.LeftHandIndex1RotateAxisz

    LeftHandIndex1JointOrient = LeftHandIndex1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex1JointOrientx = LeftHandIndex1JointOrient.LeftHandIndex1JointOrientx
    LeftHandIndex1JointOrienty = LeftHandIndex1JointOrient.LeftHandIndex1JointOrienty
    LeftHandIndex1JointOrientz = LeftHandIndex1JointOrient.LeftHandIndex1JointOrientz

    LeftHandIndex1MinRLimit = LeftHandIndex1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex1MinRLimitx = LeftHandIndex1MinRLimit.LeftHandIndex1MinRLimitx
    LeftHandIndex1MinRLimity = LeftHandIndex1MinRLimit.LeftHandIndex1MinRLimity
    LeftHandIndex1MinRLimitz = LeftHandIndex1MinRLimit.LeftHandIndex1MinRLimitz

    LeftHandIndex1MaxRLimit = LeftHandIndex1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex1MaxRLimitx = LeftHandIndex1MaxRLimit.LeftHandIndex1MaxRLimitx
    LeftHandIndex1MaxRLimity = LeftHandIndex1MaxRLimit.LeftHandIndex1MaxRLimity
    LeftHandIndex1MaxRLimitz = LeftHandIndex1MaxRLimit.LeftHandIndex1MaxRLimitz

    LeftHandIndex1MinRLimitEnablex = BoolField(default_value=False)

    LeftHandIndex1MinRLimitEnabley = BoolField(default_value=False)

    LeftHandIndex1MinRLimitEnablez = BoolField(default_value=False)

    LeftHandIndex1MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandIndex1MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandIndex1MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandIndex2 = MessageField()

    LeftHandIndex2T = LeftHandIndex2TField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex2Tx = LeftHandIndex2T.LeftHandIndex2Tx
    LeftHandIndex2Ty = LeftHandIndex2T.LeftHandIndex2Ty
    LeftHandIndex2Tz = LeftHandIndex2T.LeftHandIndex2Tz

    LeftHandIndex2R = LeftHandIndex2RField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex2Rx = LeftHandIndex2R.LeftHandIndex2Rx
    LeftHandIndex2Ry = LeftHandIndex2R.LeftHandIndex2Ry
    LeftHandIndex2Rz = LeftHandIndex2R.LeftHandIndex2Rz

    LeftHandIndex2S = LeftHandIndex2SField(default_value=(1.0, 1.0, 1.0))
    LeftHandIndex2Sx = LeftHandIndex2S.LeftHandIndex2Sx
    LeftHandIndex2Sy = LeftHandIndex2S.LeftHandIndex2Sy
    LeftHandIndex2Sz = LeftHandIndex2S.LeftHandIndex2Sz

    LeftHandIndex2RotateOrder = LeftHandIndex2RotateOrderEnumField(default_value=0)

    LeftHandIndex2RotateAxis = LeftHandIndex2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex2RotateAxisx = LeftHandIndex2RotateAxis.LeftHandIndex2RotateAxisx
    LeftHandIndex2RotateAxisy = LeftHandIndex2RotateAxis.LeftHandIndex2RotateAxisy
    LeftHandIndex2RotateAxisz = LeftHandIndex2RotateAxis.LeftHandIndex2RotateAxisz

    LeftHandIndex2JointOrient = LeftHandIndex2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex2JointOrientx = LeftHandIndex2JointOrient.LeftHandIndex2JointOrientx
    LeftHandIndex2JointOrienty = LeftHandIndex2JointOrient.LeftHandIndex2JointOrienty
    LeftHandIndex2JointOrientz = LeftHandIndex2JointOrient.LeftHandIndex2JointOrientz

    LeftHandIndex2MinRLimit = LeftHandIndex2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex2MinRLimitx = LeftHandIndex2MinRLimit.LeftHandIndex2MinRLimitx
    LeftHandIndex2MinRLimity = LeftHandIndex2MinRLimit.LeftHandIndex2MinRLimity
    LeftHandIndex2MinRLimitz = LeftHandIndex2MinRLimit.LeftHandIndex2MinRLimitz

    LeftHandIndex2MaxRLimit = LeftHandIndex2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex2MaxRLimitx = LeftHandIndex2MaxRLimit.LeftHandIndex2MaxRLimitx
    LeftHandIndex2MaxRLimity = LeftHandIndex2MaxRLimit.LeftHandIndex2MaxRLimity
    LeftHandIndex2MaxRLimitz = LeftHandIndex2MaxRLimit.LeftHandIndex2MaxRLimitz

    LeftHandIndex2MinRLimitEnablex = BoolField(default_value=False)

    LeftHandIndex2MinRLimitEnabley = BoolField(default_value=False)

    LeftHandIndex2MinRLimitEnablez = BoolField(default_value=False)

    LeftHandIndex2MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandIndex2MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandIndex2MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandIndex3 = MessageField()

    LeftHandIndex3T = LeftHandIndex3TField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex3Tx = LeftHandIndex3T.LeftHandIndex3Tx
    LeftHandIndex3Ty = LeftHandIndex3T.LeftHandIndex3Ty
    LeftHandIndex3Tz = LeftHandIndex3T.LeftHandIndex3Tz

    LeftHandIndex3R = LeftHandIndex3RField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex3Rx = LeftHandIndex3R.LeftHandIndex3Rx
    LeftHandIndex3Ry = LeftHandIndex3R.LeftHandIndex3Ry
    LeftHandIndex3Rz = LeftHandIndex3R.LeftHandIndex3Rz

    LeftHandIndex3S = LeftHandIndex3SField(default_value=(1.0, 1.0, 1.0))
    LeftHandIndex3Sx = LeftHandIndex3S.LeftHandIndex3Sx
    LeftHandIndex3Sy = LeftHandIndex3S.LeftHandIndex3Sy
    LeftHandIndex3Sz = LeftHandIndex3S.LeftHandIndex3Sz

    LeftHandIndex3RotateOrder = LeftHandIndex3RotateOrderEnumField(default_value=0)

    LeftHandIndex3RotateAxis = LeftHandIndex3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex3RotateAxisx = LeftHandIndex3RotateAxis.LeftHandIndex3RotateAxisx
    LeftHandIndex3RotateAxisy = LeftHandIndex3RotateAxis.LeftHandIndex3RotateAxisy
    LeftHandIndex3RotateAxisz = LeftHandIndex3RotateAxis.LeftHandIndex3RotateAxisz

    LeftHandIndex3JointOrient = LeftHandIndex3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex3JointOrientx = LeftHandIndex3JointOrient.LeftHandIndex3JointOrientx
    LeftHandIndex3JointOrienty = LeftHandIndex3JointOrient.LeftHandIndex3JointOrienty
    LeftHandIndex3JointOrientz = LeftHandIndex3JointOrient.LeftHandIndex3JointOrientz

    LeftHandIndex3MinRLimit = LeftHandIndex3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex3MinRLimitx = LeftHandIndex3MinRLimit.LeftHandIndex3MinRLimitx
    LeftHandIndex3MinRLimity = LeftHandIndex3MinRLimit.LeftHandIndex3MinRLimity
    LeftHandIndex3MinRLimitz = LeftHandIndex3MinRLimit.LeftHandIndex3MinRLimitz

    LeftHandIndex3MaxRLimit = LeftHandIndex3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex3MaxRLimitx = LeftHandIndex3MaxRLimit.LeftHandIndex3MaxRLimitx
    LeftHandIndex3MaxRLimity = LeftHandIndex3MaxRLimit.LeftHandIndex3MaxRLimity
    LeftHandIndex3MaxRLimitz = LeftHandIndex3MaxRLimit.LeftHandIndex3MaxRLimitz

    LeftHandIndex3MinRLimitEnablex = BoolField(default_value=False)

    LeftHandIndex3MinRLimitEnabley = BoolField(default_value=False)

    LeftHandIndex3MinRLimitEnablez = BoolField(default_value=False)

    LeftHandIndex3MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandIndex3MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandIndex3MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandIndex4 = MessageField()

    LeftHandIndex4T = LeftHandIndex4TField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex4Tx = LeftHandIndex4T.LeftHandIndex4Tx
    LeftHandIndex4Ty = LeftHandIndex4T.LeftHandIndex4Ty
    LeftHandIndex4Tz = LeftHandIndex4T.LeftHandIndex4Tz

    LeftHandIndex4R = LeftHandIndex4RField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex4Rx = LeftHandIndex4R.LeftHandIndex4Rx
    LeftHandIndex4Ry = LeftHandIndex4R.LeftHandIndex4Ry
    LeftHandIndex4Rz = LeftHandIndex4R.LeftHandIndex4Rz

    LeftHandIndex4S = LeftHandIndex4SField(default_value=(1.0, 1.0, 1.0))
    LeftHandIndex4Sx = LeftHandIndex4S.LeftHandIndex4Sx
    LeftHandIndex4Sy = LeftHandIndex4S.LeftHandIndex4Sy
    LeftHandIndex4Sz = LeftHandIndex4S.LeftHandIndex4Sz

    LeftHandIndex4RotateOrder = LeftHandIndex4RotateOrderEnumField(default_value=0)

    LeftHandIndex4RotateAxis = LeftHandIndex4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex4RotateAxisx = LeftHandIndex4RotateAxis.LeftHandIndex4RotateAxisx
    LeftHandIndex4RotateAxisy = LeftHandIndex4RotateAxis.LeftHandIndex4RotateAxisy
    LeftHandIndex4RotateAxisz = LeftHandIndex4RotateAxis.LeftHandIndex4RotateAxisz

    LeftHandIndex4JointOrient = LeftHandIndex4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex4JointOrientx = LeftHandIndex4JointOrient.LeftHandIndex4JointOrientx
    LeftHandIndex4JointOrienty = LeftHandIndex4JointOrient.LeftHandIndex4JointOrienty
    LeftHandIndex4JointOrientz = LeftHandIndex4JointOrient.LeftHandIndex4JointOrientz

    LeftHandIndex4MinRLimit = LeftHandIndex4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex4MinRLimitx = LeftHandIndex4MinRLimit.LeftHandIndex4MinRLimitx
    LeftHandIndex4MinRLimity = LeftHandIndex4MinRLimit.LeftHandIndex4MinRLimity
    LeftHandIndex4MinRLimitz = LeftHandIndex4MinRLimit.LeftHandIndex4MinRLimitz

    LeftHandIndex4MaxRLimit = LeftHandIndex4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex4MaxRLimitx = LeftHandIndex4MaxRLimit.LeftHandIndex4MaxRLimitx
    LeftHandIndex4MaxRLimity = LeftHandIndex4MaxRLimit.LeftHandIndex4MaxRLimity
    LeftHandIndex4MaxRLimitz = LeftHandIndex4MaxRLimit.LeftHandIndex4MaxRLimitz

    LeftHandIndex4MinRLimitEnablex = BoolField(default_value=False)

    LeftHandIndex4MinRLimitEnabley = BoolField(default_value=False)

    LeftHandIndex4MinRLimitEnablez = BoolField(default_value=False)

    LeftHandIndex4MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandIndex4MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandIndex4MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandMiddle1 = MessageField()

    LeftHandMiddle1T = LeftHandMiddle1TField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle1Tx = LeftHandMiddle1T.LeftHandMiddle1Tx
    LeftHandMiddle1Ty = LeftHandMiddle1T.LeftHandMiddle1Ty
    LeftHandMiddle1Tz = LeftHandMiddle1T.LeftHandMiddle1Tz

    LeftHandMiddle1R = LeftHandMiddle1RField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle1Rx = LeftHandMiddle1R.LeftHandMiddle1Rx
    LeftHandMiddle1Ry = LeftHandMiddle1R.LeftHandMiddle1Ry
    LeftHandMiddle1Rz = LeftHandMiddle1R.LeftHandMiddle1Rz

    LeftHandMiddle1S = LeftHandMiddle1SField(default_value=(1.0, 1.0, 1.0))
    LeftHandMiddle1Sx = LeftHandMiddle1S.LeftHandMiddle1Sx
    LeftHandMiddle1Sy = LeftHandMiddle1S.LeftHandMiddle1Sy
    LeftHandMiddle1Sz = LeftHandMiddle1S.LeftHandMiddle1Sz

    LeftHandMiddle1RotateOrder = LeftHandMiddle1RotateOrderEnumField(default_value=0)

    LeftHandMiddle1RotateAxis = LeftHandMiddle1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle1RotateAxisx = LeftHandMiddle1RotateAxis.LeftHandMiddle1RotateAxisx
    LeftHandMiddle1RotateAxisy = LeftHandMiddle1RotateAxis.LeftHandMiddle1RotateAxisy
    LeftHandMiddle1RotateAxisz = LeftHandMiddle1RotateAxis.LeftHandMiddle1RotateAxisz

    LeftHandMiddle1JointOrient = LeftHandMiddle1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle1JointOrientx = LeftHandMiddle1JointOrient.LeftHandMiddle1JointOrientx
    LeftHandMiddle1JointOrienty = LeftHandMiddle1JointOrient.LeftHandMiddle1JointOrienty
    LeftHandMiddle1JointOrientz = LeftHandMiddle1JointOrient.LeftHandMiddle1JointOrientz

    LeftHandMiddle1MinRLimit = LeftHandMiddle1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle1MinRLimitx = LeftHandMiddle1MinRLimit.LeftHandMiddle1MinRLimitx
    LeftHandMiddle1MinRLimity = LeftHandMiddle1MinRLimit.LeftHandMiddle1MinRLimity
    LeftHandMiddle1MinRLimitz = LeftHandMiddle1MinRLimit.LeftHandMiddle1MinRLimitz

    LeftHandMiddle1MaxRLimit = LeftHandMiddle1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle1MaxRLimitx = LeftHandMiddle1MaxRLimit.LeftHandMiddle1MaxRLimitx
    LeftHandMiddle1MaxRLimity = LeftHandMiddle1MaxRLimit.LeftHandMiddle1MaxRLimity
    LeftHandMiddle1MaxRLimitz = LeftHandMiddle1MaxRLimit.LeftHandMiddle1MaxRLimitz

    LeftHandMiddle1MinRLimitEnablex = BoolField(default_value=False)

    LeftHandMiddle1MinRLimitEnabley = BoolField(default_value=False)

    LeftHandMiddle1MinRLimitEnablez = BoolField(default_value=False)

    LeftHandMiddle1MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandMiddle1MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandMiddle1MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandMiddle2 = MessageField()

    LeftHandMiddle2T = LeftHandMiddle2TField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle2Tx = LeftHandMiddle2T.LeftHandMiddle2Tx
    LeftHandMiddle2Ty = LeftHandMiddle2T.LeftHandMiddle2Ty
    LeftHandMiddle2Tz = LeftHandMiddle2T.LeftHandMiddle2Tz

    LeftHandMiddle2R = LeftHandMiddle2RField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle2Rx = LeftHandMiddle2R.LeftHandMiddle2Rx
    LeftHandMiddle2Ry = LeftHandMiddle2R.LeftHandMiddle2Ry
    LeftHandMiddle2Rz = LeftHandMiddle2R.LeftHandMiddle2Rz

    LeftHandMiddle2S = LeftHandMiddle2SField(default_value=(1.0, 1.0, 1.0))
    LeftHandMiddle2Sx = LeftHandMiddle2S.LeftHandMiddle2Sx
    LeftHandMiddle2Sy = LeftHandMiddle2S.LeftHandMiddle2Sy
    LeftHandMiddle2Sz = LeftHandMiddle2S.LeftHandMiddle2Sz

    LeftHandMiddle2RotateOrder = LeftHandMiddle2RotateOrderEnumField(default_value=0)

    LeftHandMiddle2RotateAxis = LeftHandMiddle2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle2RotateAxisx = LeftHandMiddle2RotateAxis.LeftHandMiddle2RotateAxisx
    LeftHandMiddle2RotateAxisy = LeftHandMiddle2RotateAxis.LeftHandMiddle2RotateAxisy
    LeftHandMiddle2RotateAxisz = LeftHandMiddle2RotateAxis.LeftHandMiddle2RotateAxisz

    LeftHandMiddle2JointOrient = LeftHandMiddle2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle2JointOrientx = LeftHandMiddle2JointOrient.LeftHandMiddle2JointOrientx
    LeftHandMiddle2JointOrienty = LeftHandMiddle2JointOrient.LeftHandMiddle2JointOrienty
    LeftHandMiddle2JointOrientz = LeftHandMiddle2JointOrient.LeftHandMiddle2JointOrientz

    LeftHandMiddle2MinRLimit = LeftHandMiddle2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle2MinRLimitx = LeftHandMiddle2MinRLimit.LeftHandMiddle2MinRLimitx
    LeftHandMiddle2MinRLimity = LeftHandMiddle2MinRLimit.LeftHandMiddle2MinRLimity
    LeftHandMiddle2MinRLimitz = LeftHandMiddle2MinRLimit.LeftHandMiddle2MinRLimitz

    LeftHandMiddle2MaxRLimit = LeftHandMiddle2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle2MaxRLimitx = LeftHandMiddle2MaxRLimit.LeftHandMiddle2MaxRLimitx
    LeftHandMiddle2MaxRLimity = LeftHandMiddle2MaxRLimit.LeftHandMiddle2MaxRLimity
    LeftHandMiddle2MaxRLimitz = LeftHandMiddle2MaxRLimit.LeftHandMiddle2MaxRLimitz

    LeftHandMiddle2MinRLimitEnablex = BoolField(default_value=False)

    LeftHandMiddle2MinRLimitEnabley = BoolField(default_value=False)

    LeftHandMiddle2MinRLimitEnablez = BoolField(default_value=False)

    LeftHandMiddle2MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandMiddle2MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandMiddle2MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandMiddle3 = MessageField()

    LeftHandMiddle3T = LeftHandMiddle3TField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle3Tx = LeftHandMiddle3T.LeftHandMiddle3Tx
    LeftHandMiddle3Ty = LeftHandMiddle3T.LeftHandMiddle3Ty
    LeftHandMiddle3Tz = LeftHandMiddle3T.LeftHandMiddle3Tz

    LeftHandMiddle3R = LeftHandMiddle3RField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle3Rx = LeftHandMiddle3R.LeftHandMiddle3Rx
    LeftHandMiddle3Ry = LeftHandMiddle3R.LeftHandMiddle3Ry
    LeftHandMiddle3Rz = LeftHandMiddle3R.LeftHandMiddle3Rz

    LeftHandMiddle3S = LeftHandMiddle3SField(default_value=(1.0, 1.0, 1.0))
    LeftHandMiddle3Sx = LeftHandMiddle3S.LeftHandMiddle3Sx
    LeftHandMiddle3Sy = LeftHandMiddle3S.LeftHandMiddle3Sy
    LeftHandMiddle3Sz = LeftHandMiddle3S.LeftHandMiddle3Sz

    LeftHandMiddle3RotateOrder = LeftHandMiddle3RotateOrderEnumField(default_value=0)

    LeftHandMiddle3RotateAxis = LeftHandMiddle3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle3RotateAxisx = LeftHandMiddle3RotateAxis.LeftHandMiddle3RotateAxisx
    LeftHandMiddle3RotateAxisy = LeftHandMiddle3RotateAxis.LeftHandMiddle3RotateAxisy
    LeftHandMiddle3RotateAxisz = LeftHandMiddle3RotateAxis.LeftHandMiddle3RotateAxisz

    LeftHandMiddle3JointOrient = LeftHandMiddle3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle3JointOrientx = LeftHandMiddle3JointOrient.LeftHandMiddle3JointOrientx
    LeftHandMiddle3JointOrienty = LeftHandMiddle3JointOrient.LeftHandMiddle3JointOrienty
    LeftHandMiddle3JointOrientz = LeftHandMiddle3JointOrient.LeftHandMiddle3JointOrientz

    LeftHandMiddle3MinRLimit = LeftHandMiddle3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle3MinRLimitx = LeftHandMiddle3MinRLimit.LeftHandMiddle3MinRLimitx
    LeftHandMiddle3MinRLimity = LeftHandMiddle3MinRLimit.LeftHandMiddle3MinRLimity
    LeftHandMiddle3MinRLimitz = LeftHandMiddle3MinRLimit.LeftHandMiddle3MinRLimitz

    LeftHandMiddle3MaxRLimit = LeftHandMiddle3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle3MaxRLimitx = LeftHandMiddle3MaxRLimit.LeftHandMiddle3MaxRLimitx
    LeftHandMiddle3MaxRLimity = LeftHandMiddle3MaxRLimit.LeftHandMiddle3MaxRLimity
    LeftHandMiddle3MaxRLimitz = LeftHandMiddle3MaxRLimit.LeftHandMiddle3MaxRLimitz

    LeftHandMiddle3MinRLimitEnablex = BoolField(default_value=False)

    LeftHandMiddle3MinRLimitEnabley = BoolField(default_value=False)

    LeftHandMiddle3MinRLimitEnablez = BoolField(default_value=False)

    LeftHandMiddle3MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandMiddle3MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandMiddle3MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandMiddle4 = MessageField()

    LeftHandMiddle4T = LeftHandMiddle4TField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle4Tx = LeftHandMiddle4T.LeftHandMiddle4Tx
    LeftHandMiddle4Ty = LeftHandMiddle4T.LeftHandMiddle4Ty
    LeftHandMiddle4Tz = LeftHandMiddle4T.LeftHandMiddle4Tz

    LeftHandMiddle4R = LeftHandMiddle4RField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle4Rx = LeftHandMiddle4R.LeftHandMiddle4Rx
    LeftHandMiddle4Ry = LeftHandMiddle4R.LeftHandMiddle4Ry
    LeftHandMiddle4Rz = LeftHandMiddle4R.LeftHandMiddle4Rz

    LeftHandMiddle4S = LeftHandMiddle4SField(default_value=(1.0, 1.0, 1.0))
    LeftHandMiddle4Sx = LeftHandMiddle4S.LeftHandMiddle4Sx
    LeftHandMiddle4Sy = LeftHandMiddle4S.LeftHandMiddle4Sy
    LeftHandMiddle4Sz = LeftHandMiddle4S.LeftHandMiddle4Sz

    LeftHandMiddle4RotateOrder = LeftHandMiddle4RotateOrderEnumField(default_value=0)

    LeftHandMiddle4RotateAxis = LeftHandMiddle4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle4RotateAxisx = LeftHandMiddle4RotateAxis.LeftHandMiddle4RotateAxisx
    LeftHandMiddle4RotateAxisy = LeftHandMiddle4RotateAxis.LeftHandMiddle4RotateAxisy
    LeftHandMiddle4RotateAxisz = LeftHandMiddle4RotateAxis.LeftHandMiddle4RotateAxisz

    LeftHandMiddle4JointOrient = LeftHandMiddle4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle4JointOrientx = LeftHandMiddle4JointOrient.LeftHandMiddle4JointOrientx
    LeftHandMiddle4JointOrienty = LeftHandMiddle4JointOrient.LeftHandMiddle4JointOrienty
    LeftHandMiddle4JointOrientz = LeftHandMiddle4JointOrient.LeftHandMiddle4JointOrientz

    LeftHandMiddle4MinRLimit = LeftHandMiddle4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle4MinRLimitx = LeftHandMiddle4MinRLimit.LeftHandMiddle4MinRLimitx
    LeftHandMiddle4MinRLimity = LeftHandMiddle4MinRLimit.LeftHandMiddle4MinRLimity
    LeftHandMiddle4MinRLimitz = LeftHandMiddle4MinRLimit.LeftHandMiddle4MinRLimitz

    LeftHandMiddle4MaxRLimit = LeftHandMiddle4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle4MaxRLimitx = LeftHandMiddle4MaxRLimit.LeftHandMiddle4MaxRLimitx
    LeftHandMiddle4MaxRLimity = LeftHandMiddle4MaxRLimit.LeftHandMiddle4MaxRLimity
    LeftHandMiddle4MaxRLimitz = LeftHandMiddle4MaxRLimit.LeftHandMiddle4MaxRLimitz

    LeftHandMiddle4MinRLimitEnablex = BoolField(default_value=False)

    LeftHandMiddle4MinRLimitEnabley = BoolField(default_value=False)

    LeftHandMiddle4MinRLimitEnablez = BoolField(default_value=False)

    LeftHandMiddle4MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandMiddle4MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandMiddle4MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandRing1 = MessageField()

    LeftHandRing1T = LeftHandRing1TField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing1Tx = LeftHandRing1T.LeftHandRing1Tx
    LeftHandRing1Ty = LeftHandRing1T.LeftHandRing1Ty
    LeftHandRing1Tz = LeftHandRing1T.LeftHandRing1Tz

    LeftHandRing1R = LeftHandRing1RField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing1Rx = LeftHandRing1R.LeftHandRing1Rx
    LeftHandRing1Ry = LeftHandRing1R.LeftHandRing1Ry
    LeftHandRing1Rz = LeftHandRing1R.LeftHandRing1Rz

    LeftHandRing1S = LeftHandRing1SField(default_value=(1.0, 1.0, 1.0))
    LeftHandRing1Sx = LeftHandRing1S.LeftHandRing1Sx
    LeftHandRing1Sy = LeftHandRing1S.LeftHandRing1Sy
    LeftHandRing1Sz = LeftHandRing1S.LeftHandRing1Sz

    LeftHandRing1RotateOrder = LeftHandRing1RotateOrderEnumField(default_value=0)

    LeftHandRing1RotateAxis = LeftHandRing1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing1RotateAxisx = LeftHandRing1RotateAxis.LeftHandRing1RotateAxisx
    LeftHandRing1RotateAxisy = LeftHandRing1RotateAxis.LeftHandRing1RotateAxisy
    LeftHandRing1RotateAxisz = LeftHandRing1RotateAxis.LeftHandRing1RotateAxisz

    LeftHandRing1JointOrient = LeftHandRing1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing1JointOrientx = LeftHandRing1JointOrient.LeftHandRing1JointOrientx
    LeftHandRing1JointOrienty = LeftHandRing1JointOrient.LeftHandRing1JointOrienty
    LeftHandRing1JointOrientz = LeftHandRing1JointOrient.LeftHandRing1JointOrientz

    LeftHandRing1MinRLimit = LeftHandRing1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing1MinRLimitx = LeftHandRing1MinRLimit.LeftHandRing1MinRLimitx
    LeftHandRing1MinRLimity = LeftHandRing1MinRLimit.LeftHandRing1MinRLimity
    LeftHandRing1MinRLimitz = LeftHandRing1MinRLimit.LeftHandRing1MinRLimitz

    LeftHandRing1MaxRLimit = LeftHandRing1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing1MaxRLimitx = LeftHandRing1MaxRLimit.LeftHandRing1MaxRLimitx
    LeftHandRing1MaxRLimity = LeftHandRing1MaxRLimit.LeftHandRing1MaxRLimity
    LeftHandRing1MaxRLimitz = LeftHandRing1MaxRLimit.LeftHandRing1MaxRLimitz

    LeftHandRing1MinRLimitEnablex = BoolField(default_value=False)

    LeftHandRing1MinRLimitEnabley = BoolField(default_value=False)

    LeftHandRing1MinRLimitEnablez = BoolField(default_value=False)

    LeftHandRing1MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandRing1MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandRing1MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandRing2 = MessageField()

    LeftHandRing2T = LeftHandRing2TField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing2Tx = LeftHandRing2T.LeftHandRing2Tx
    LeftHandRing2Ty = LeftHandRing2T.LeftHandRing2Ty
    LeftHandRing2Tz = LeftHandRing2T.LeftHandRing2Tz

    LeftHandRing2R = LeftHandRing2RField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing2Rx = LeftHandRing2R.LeftHandRing2Rx
    LeftHandRing2Ry = LeftHandRing2R.LeftHandRing2Ry
    LeftHandRing2Rz = LeftHandRing2R.LeftHandRing2Rz

    LeftHandRing2S = LeftHandRing2SField(default_value=(1.0, 1.0, 1.0))
    LeftHandRing2Sx = LeftHandRing2S.LeftHandRing2Sx
    LeftHandRing2Sy = LeftHandRing2S.LeftHandRing2Sy
    LeftHandRing2Sz = LeftHandRing2S.LeftHandRing2Sz

    LeftHandRing2RotateOrder = LeftHandRing2RotateOrderEnumField(default_value=0)

    LeftHandRing2RotateAxis = LeftHandRing2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing2RotateAxisx = LeftHandRing2RotateAxis.LeftHandRing2RotateAxisx
    LeftHandRing2RotateAxisy = LeftHandRing2RotateAxis.LeftHandRing2RotateAxisy
    LeftHandRing2RotateAxisz = LeftHandRing2RotateAxis.LeftHandRing2RotateAxisz

    LeftHandRing2JointOrient = LeftHandRing2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing2JointOrientx = LeftHandRing2JointOrient.LeftHandRing2JointOrientx
    LeftHandRing2JointOrienty = LeftHandRing2JointOrient.LeftHandRing2JointOrienty
    LeftHandRing2JointOrientz = LeftHandRing2JointOrient.LeftHandRing2JointOrientz

    LeftHandRing2MinRLimit = LeftHandRing2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing2MinRLimitx = LeftHandRing2MinRLimit.LeftHandRing2MinRLimitx
    LeftHandRing2MinRLimity = LeftHandRing2MinRLimit.LeftHandRing2MinRLimity
    LeftHandRing2MinRLimitz = LeftHandRing2MinRLimit.LeftHandRing2MinRLimitz

    LeftHandRing2MaxRLimit = LeftHandRing2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing2MaxRLimitx = LeftHandRing2MaxRLimit.LeftHandRing2MaxRLimitx
    LeftHandRing2MaxRLimity = LeftHandRing2MaxRLimit.LeftHandRing2MaxRLimity
    LeftHandRing2MaxRLimitz = LeftHandRing2MaxRLimit.LeftHandRing2MaxRLimitz

    LeftHandRing2MinRLimitEnablex = BoolField(default_value=False)

    LeftHandRing2MinRLimitEnabley = BoolField(default_value=False)

    LeftHandRing2MinRLimitEnablez = BoolField(default_value=False)

    LeftHandRing2MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandRing2MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandRing2MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandRing3 = MessageField()

    LeftHandRing3T = LeftHandRing3TField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing3Tx = LeftHandRing3T.LeftHandRing3Tx
    LeftHandRing3Ty = LeftHandRing3T.LeftHandRing3Ty
    LeftHandRing3Tz = LeftHandRing3T.LeftHandRing3Tz

    LeftHandRing3R = LeftHandRing3RField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing3Rx = LeftHandRing3R.LeftHandRing3Rx
    LeftHandRing3Ry = LeftHandRing3R.LeftHandRing3Ry
    LeftHandRing3Rz = LeftHandRing3R.LeftHandRing3Rz

    LeftHandRing3S = LeftHandRing3SField(default_value=(1.0, 1.0, 1.0))
    LeftHandRing3Sx = LeftHandRing3S.LeftHandRing3Sx
    LeftHandRing3Sy = LeftHandRing3S.LeftHandRing3Sy
    LeftHandRing3Sz = LeftHandRing3S.LeftHandRing3Sz

    LeftHandRing3RotateOrder = LeftHandRing3RotateOrderEnumField(default_value=0)

    LeftHandRing3RotateAxis = LeftHandRing3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing3RotateAxisx = LeftHandRing3RotateAxis.LeftHandRing3RotateAxisx
    LeftHandRing3RotateAxisy = LeftHandRing3RotateAxis.LeftHandRing3RotateAxisy
    LeftHandRing3RotateAxisz = LeftHandRing3RotateAxis.LeftHandRing3RotateAxisz

    LeftHandRing3JointOrient = LeftHandRing3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing3JointOrientx = LeftHandRing3JointOrient.LeftHandRing3JointOrientx
    LeftHandRing3JointOrienty = LeftHandRing3JointOrient.LeftHandRing3JointOrienty
    LeftHandRing3JointOrientz = LeftHandRing3JointOrient.LeftHandRing3JointOrientz

    LeftHandRing3MinRLimit = LeftHandRing3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing3MinRLimitx = LeftHandRing3MinRLimit.LeftHandRing3MinRLimitx
    LeftHandRing3MinRLimity = LeftHandRing3MinRLimit.LeftHandRing3MinRLimity
    LeftHandRing3MinRLimitz = LeftHandRing3MinRLimit.LeftHandRing3MinRLimitz

    LeftHandRing3MaxRLimit = LeftHandRing3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing3MaxRLimitx = LeftHandRing3MaxRLimit.LeftHandRing3MaxRLimitx
    LeftHandRing3MaxRLimity = LeftHandRing3MaxRLimit.LeftHandRing3MaxRLimity
    LeftHandRing3MaxRLimitz = LeftHandRing3MaxRLimit.LeftHandRing3MaxRLimitz

    LeftHandRing3MinRLimitEnablex = BoolField(default_value=False)

    LeftHandRing3MinRLimitEnabley = BoolField(default_value=False)

    LeftHandRing3MinRLimitEnablez = BoolField(default_value=False)

    LeftHandRing3MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandRing3MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandRing3MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandRing4 = MessageField()

    LeftHandRing4T = LeftHandRing4TField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing4Tx = LeftHandRing4T.LeftHandRing4Tx
    LeftHandRing4Ty = LeftHandRing4T.LeftHandRing4Ty
    LeftHandRing4Tz = LeftHandRing4T.LeftHandRing4Tz

    LeftHandRing4R = LeftHandRing4RField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing4Rx = LeftHandRing4R.LeftHandRing4Rx
    LeftHandRing4Ry = LeftHandRing4R.LeftHandRing4Ry
    LeftHandRing4Rz = LeftHandRing4R.LeftHandRing4Rz

    LeftHandRing4S = LeftHandRing4SField(default_value=(1.0, 1.0, 1.0))
    LeftHandRing4Sx = LeftHandRing4S.LeftHandRing4Sx
    LeftHandRing4Sy = LeftHandRing4S.LeftHandRing4Sy
    LeftHandRing4Sz = LeftHandRing4S.LeftHandRing4Sz

    LeftHandRing4RotateOrder = LeftHandRing4RotateOrderEnumField(default_value=0)

    LeftHandRing4RotateAxis = LeftHandRing4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing4RotateAxisx = LeftHandRing4RotateAxis.LeftHandRing4RotateAxisx
    LeftHandRing4RotateAxisy = LeftHandRing4RotateAxis.LeftHandRing4RotateAxisy
    LeftHandRing4RotateAxisz = LeftHandRing4RotateAxis.LeftHandRing4RotateAxisz

    LeftHandRing4JointOrient = LeftHandRing4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing4JointOrientx = LeftHandRing4JointOrient.LeftHandRing4JointOrientx
    LeftHandRing4JointOrienty = LeftHandRing4JointOrient.LeftHandRing4JointOrienty
    LeftHandRing4JointOrientz = LeftHandRing4JointOrient.LeftHandRing4JointOrientz

    LeftHandRing4MinRLimit = LeftHandRing4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing4MinRLimitx = LeftHandRing4MinRLimit.LeftHandRing4MinRLimitx
    LeftHandRing4MinRLimity = LeftHandRing4MinRLimit.LeftHandRing4MinRLimity
    LeftHandRing4MinRLimitz = LeftHandRing4MinRLimit.LeftHandRing4MinRLimitz

    LeftHandRing4MaxRLimit = LeftHandRing4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing4MaxRLimitx = LeftHandRing4MaxRLimit.LeftHandRing4MaxRLimitx
    LeftHandRing4MaxRLimity = LeftHandRing4MaxRLimit.LeftHandRing4MaxRLimity
    LeftHandRing4MaxRLimitz = LeftHandRing4MaxRLimit.LeftHandRing4MaxRLimitz

    LeftHandRing4MinRLimitEnablex = BoolField(default_value=False)

    LeftHandRing4MinRLimitEnabley = BoolField(default_value=False)

    LeftHandRing4MinRLimitEnablez = BoolField(default_value=False)

    LeftHandRing4MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandRing4MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandRing4MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandPinky1 = MessageField()

    LeftHandPinky1T = LeftHandPinky1TField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky1Tx = LeftHandPinky1T.LeftHandPinky1Tx
    LeftHandPinky1Ty = LeftHandPinky1T.LeftHandPinky1Ty
    LeftHandPinky1Tz = LeftHandPinky1T.LeftHandPinky1Tz

    LeftHandPinky1R = LeftHandPinky1RField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky1Rx = LeftHandPinky1R.LeftHandPinky1Rx
    LeftHandPinky1Ry = LeftHandPinky1R.LeftHandPinky1Ry
    LeftHandPinky1Rz = LeftHandPinky1R.LeftHandPinky1Rz

    LeftHandPinky1S = LeftHandPinky1SField(default_value=(1.0, 1.0, 1.0))
    LeftHandPinky1Sx = LeftHandPinky1S.LeftHandPinky1Sx
    LeftHandPinky1Sy = LeftHandPinky1S.LeftHandPinky1Sy
    LeftHandPinky1Sz = LeftHandPinky1S.LeftHandPinky1Sz

    LeftHandPinky1RotateOrder = LeftHandPinky1RotateOrderEnumField(default_value=0)

    LeftHandPinky1RotateAxis = LeftHandPinky1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky1RotateAxisx = LeftHandPinky1RotateAxis.LeftHandPinky1RotateAxisx
    LeftHandPinky1RotateAxisy = LeftHandPinky1RotateAxis.LeftHandPinky1RotateAxisy
    LeftHandPinky1RotateAxisz = LeftHandPinky1RotateAxis.LeftHandPinky1RotateAxisz

    LeftHandPinky1JointOrient = LeftHandPinky1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky1JointOrientx = LeftHandPinky1JointOrient.LeftHandPinky1JointOrientx
    LeftHandPinky1JointOrienty = LeftHandPinky1JointOrient.LeftHandPinky1JointOrienty
    LeftHandPinky1JointOrientz = LeftHandPinky1JointOrient.LeftHandPinky1JointOrientz

    LeftHandPinky1MinRLimit = LeftHandPinky1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky1MinRLimitx = LeftHandPinky1MinRLimit.LeftHandPinky1MinRLimitx
    LeftHandPinky1MinRLimity = LeftHandPinky1MinRLimit.LeftHandPinky1MinRLimity
    LeftHandPinky1MinRLimitz = LeftHandPinky1MinRLimit.LeftHandPinky1MinRLimitz

    LeftHandPinky1MaxRLimit = LeftHandPinky1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky1MaxRLimitx = LeftHandPinky1MaxRLimit.LeftHandPinky1MaxRLimitx
    LeftHandPinky1MaxRLimity = LeftHandPinky1MaxRLimit.LeftHandPinky1MaxRLimity
    LeftHandPinky1MaxRLimitz = LeftHandPinky1MaxRLimit.LeftHandPinky1MaxRLimitz

    LeftHandPinky1MinRLimitEnablex = BoolField(default_value=False)

    LeftHandPinky1MinRLimitEnabley = BoolField(default_value=False)

    LeftHandPinky1MinRLimitEnablez = BoolField(default_value=False)

    LeftHandPinky1MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandPinky1MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandPinky1MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandPinky2 = MessageField()

    LeftHandPinky2T = LeftHandPinky2TField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky2Tx = LeftHandPinky2T.LeftHandPinky2Tx
    LeftHandPinky2Ty = LeftHandPinky2T.LeftHandPinky2Ty
    LeftHandPinky2Tz = LeftHandPinky2T.LeftHandPinky2Tz

    LeftHandPinky2R = LeftHandPinky2RField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky2Rx = LeftHandPinky2R.LeftHandPinky2Rx
    LeftHandPinky2Ry = LeftHandPinky2R.LeftHandPinky2Ry
    LeftHandPinky2Rz = LeftHandPinky2R.LeftHandPinky2Rz

    LeftHandPinky2S = LeftHandPinky2SField(default_value=(1.0, 1.0, 1.0))
    LeftHandPinky2Sx = LeftHandPinky2S.LeftHandPinky2Sx
    LeftHandPinky2Sy = LeftHandPinky2S.LeftHandPinky2Sy
    LeftHandPinky2Sz = LeftHandPinky2S.LeftHandPinky2Sz

    LeftHandPinky2RotateOrder = LeftHandPinky2RotateOrderEnumField(default_value=0)

    LeftHandPinky2RotateAxis = LeftHandPinky2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky2RotateAxisx = LeftHandPinky2RotateAxis.LeftHandPinky2RotateAxisx
    LeftHandPinky2RotateAxisy = LeftHandPinky2RotateAxis.LeftHandPinky2RotateAxisy
    LeftHandPinky2RotateAxisz = LeftHandPinky2RotateAxis.LeftHandPinky2RotateAxisz

    LeftHandPinky2JointOrient = LeftHandPinky2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky2JointOrientx = LeftHandPinky2JointOrient.LeftHandPinky2JointOrientx
    LeftHandPinky2JointOrienty = LeftHandPinky2JointOrient.LeftHandPinky2JointOrienty
    LeftHandPinky2JointOrientz = LeftHandPinky2JointOrient.LeftHandPinky2JointOrientz

    LeftHandPinky2MinRLimit = LeftHandPinky2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky2MinRLimitx = LeftHandPinky2MinRLimit.LeftHandPinky2MinRLimitx
    LeftHandPinky2MinRLimity = LeftHandPinky2MinRLimit.LeftHandPinky2MinRLimity
    LeftHandPinky2MinRLimitz = LeftHandPinky2MinRLimit.LeftHandPinky2MinRLimitz

    LeftHandPinky2MaxRLimit = LeftHandPinky2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky2MaxRLimitx = LeftHandPinky2MaxRLimit.LeftHandPinky2MaxRLimitx
    LeftHandPinky2MaxRLimity = LeftHandPinky2MaxRLimit.LeftHandPinky2MaxRLimity
    LeftHandPinky2MaxRLimitz = LeftHandPinky2MaxRLimit.LeftHandPinky2MaxRLimitz

    LeftHandPinky2MinRLimitEnablex = BoolField(default_value=False)

    LeftHandPinky2MinRLimitEnabley = BoolField(default_value=False)

    LeftHandPinky2MinRLimitEnablez = BoolField(default_value=False)

    LeftHandPinky2MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandPinky2MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandPinky2MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandPinky3 = MessageField()

    LeftHandPinky3T = LeftHandPinky3TField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky3Tx = LeftHandPinky3T.LeftHandPinky3Tx
    LeftHandPinky3Ty = LeftHandPinky3T.LeftHandPinky3Ty
    LeftHandPinky3Tz = LeftHandPinky3T.LeftHandPinky3Tz

    LeftHandPinky3R = LeftHandPinky3RField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky3Rx = LeftHandPinky3R.LeftHandPinky3Rx
    LeftHandPinky3Ry = LeftHandPinky3R.LeftHandPinky3Ry
    LeftHandPinky3Rz = LeftHandPinky3R.LeftHandPinky3Rz

    LeftHandPinky3S = LeftHandPinky3SField(default_value=(1.0, 1.0, 1.0))
    LeftHandPinky3Sx = LeftHandPinky3S.LeftHandPinky3Sx
    LeftHandPinky3Sy = LeftHandPinky3S.LeftHandPinky3Sy
    LeftHandPinky3Sz = LeftHandPinky3S.LeftHandPinky3Sz

    LeftHandPinky3RotateOrder = LeftHandPinky3RotateOrderEnumField(default_value=0)

    LeftHandPinky3RotateAxis = LeftHandPinky3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky3RotateAxisx = LeftHandPinky3RotateAxis.LeftHandPinky3RotateAxisx
    LeftHandPinky3RotateAxisy = LeftHandPinky3RotateAxis.LeftHandPinky3RotateAxisy
    LeftHandPinky3RotateAxisz = LeftHandPinky3RotateAxis.LeftHandPinky3RotateAxisz

    LeftHandPinky3JointOrient = LeftHandPinky3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky3JointOrientx = LeftHandPinky3JointOrient.LeftHandPinky3JointOrientx
    LeftHandPinky3JointOrienty = LeftHandPinky3JointOrient.LeftHandPinky3JointOrienty
    LeftHandPinky3JointOrientz = LeftHandPinky3JointOrient.LeftHandPinky3JointOrientz

    LeftHandPinky3MinRLimit = LeftHandPinky3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky3MinRLimitx = LeftHandPinky3MinRLimit.LeftHandPinky3MinRLimitx
    LeftHandPinky3MinRLimity = LeftHandPinky3MinRLimit.LeftHandPinky3MinRLimity
    LeftHandPinky3MinRLimitz = LeftHandPinky3MinRLimit.LeftHandPinky3MinRLimitz

    LeftHandPinky3MaxRLimit = LeftHandPinky3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky3MaxRLimitx = LeftHandPinky3MaxRLimit.LeftHandPinky3MaxRLimitx
    LeftHandPinky3MaxRLimity = LeftHandPinky3MaxRLimit.LeftHandPinky3MaxRLimity
    LeftHandPinky3MaxRLimitz = LeftHandPinky3MaxRLimit.LeftHandPinky3MaxRLimitz

    LeftHandPinky3MinRLimitEnablex = BoolField(default_value=False)

    LeftHandPinky3MinRLimitEnabley = BoolField(default_value=False)

    LeftHandPinky3MinRLimitEnablez = BoolField(default_value=False)

    LeftHandPinky3MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandPinky3MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandPinky3MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandPinky4 = MessageField()

    LeftHandPinky4T = LeftHandPinky4TField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky4Tx = LeftHandPinky4T.LeftHandPinky4Tx
    LeftHandPinky4Ty = LeftHandPinky4T.LeftHandPinky4Ty
    LeftHandPinky4Tz = LeftHandPinky4T.LeftHandPinky4Tz

    LeftHandPinky4R = LeftHandPinky4RField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky4Rx = LeftHandPinky4R.LeftHandPinky4Rx
    LeftHandPinky4Ry = LeftHandPinky4R.LeftHandPinky4Ry
    LeftHandPinky4Rz = LeftHandPinky4R.LeftHandPinky4Rz

    LeftHandPinky4S = LeftHandPinky4SField(default_value=(1.0, 1.0, 1.0))
    LeftHandPinky4Sx = LeftHandPinky4S.LeftHandPinky4Sx
    LeftHandPinky4Sy = LeftHandPinky4S.LeftHandPinky4Sy
    LeftHandPinky4Sz = LeftHandPinky4S.LeftHandPinky4Sz

    LeftHandPinky4RotateOrder = LeftHandPinky4RotateOrderEnumField(default_value=0)

    LeftHandPinky4RotateAxis = LeftHandPinky4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky4RotateAxisx = LeftHandPinky4RotateAxis.LeftHandPinky4RotateAxisx
    LeftHandPinky4RotateAxisy = LeftHandPinky4RotateAxis.LeftHandPinky4RotateAxisy
    LeftHandPinky4RotateAxisz = LeftHandPinky4RotateAxis.LeftHandPinky4RotateAxisz

    LeftHandPinky4JointOrient = LeftHandPinky4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky4JointOrientx = LeftHandPinky4JointOrient.LeftHandPinky4JointOrientx
    LeftHandPinky4JointOrienty = LeftHandPinky4JointOrient.LeftHandPinky4JointOrienty
    LeftHandPinky4JointOrientz = LeftHandPinky4JointOrient.LeftHandPinky4JointOrientz

    LeftHandPinky4MinRLimit = LeftHandPinky4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky4MinRLimitx = LeftHandPinky4MinRLimit.LeftHandPinky4MinRLimitx
    LeftHandPinky4MinRLimity = LeftHandPinky4MinRLimit.LeftHandPinky4MinRLimity
    LeftHandPinky4MinRLimitz = LeftHandPinky4MinRLimit.LeftHandPinky4MinRLimitz

    LeftHandPinky4MaxRLimit = LeftHandPinky4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky4MaxRLimitx = LeftHandPinky4MaxRLimit.LeftHandPinky4MaxRLimitx
    LeftHandPinky4MaxRLimity = LeftHandPinky4MaxRLimit.LeftHandPinky4MaxRLimity
    LeftHandPinky4MaxRLimitz = LeftHandPinky4MaxRLimit.LeftHandPinky4MaxRLimitz

    LeftHandPinky4MinRLimitEnablex = BoolField(default_value=False)

    LeftHandPinky4MinRLimitEnabley = BoolField(default_value=False)

    LeftHandPinky4MinRLimitEnablez = BoolField(default_value=False)

    LeftHandPinky4MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandPinky4MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandPinky4MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandExtraFinger1 = MessageField()

    LeftHandExtraFinger1T = LeftHandExtraFinger1TField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger1Tx = LeftHandExtraFinger1T.LeftHandExtraFinger1Tx
    LeftHandExtraFinger1Ty = LeftHandExtraFinger1T.LeftHandExtraFinger1Ty
    LeftHandExtraFinger1Tz = LeftHandExtraFinger1T.LeftHandExtraFinger1Tz

    LeftHandExtraFinger1R = LeftHandExtraFinger1RField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger1Rx = LeftHandExtraFinger1R.LeftHandExtraFinger1Rx
    LeftHandExtraFinger1Ry = LeftHandExtraFinger1R.LeftHandExtraFinger1Ry
    LeftHandExtraFinger1Rz = LeftHandExtraFinger1R.LeftHandExtraFinger1Rz

    LeftHandExtraFinger1S = LeftHandExtraFinger1SField(default_value=(1.0, 1.0, 1.0))
    LeftHandExtraFinger1Sx = LeftHandExtraFinger1S.LeftHandExtraFinger1Sx
    LeftHandExtraFinger1Sy = LeftHandExtraFinger1S.LeftHandExtraFinger1Sy
    LeftHandExtraFinger1Sz = LeftHandExtraFinger1S.LeftHandExtraFinger1Sz

    LeftHandExtraFinger1RotateOrder = LeftHandExtraFinger1RotateOrderEnumField(default_value=0)

    LeftHandExtraFinger1RotateAxis = LeftHandExtraFinger1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger1RotateAxisx = LeftHandExtraFinger1RotateAxis.LeftHandExtraFinger1RotateAxisx
    LeftHandExtraFinger1RotateAxisy = LeftHandExtraFinger1RotateAxis.LeftHandExtraFinger1RotateAxisy
    LeftHandExtraFinger1RotateAxisz = LeftHandExtraFinger1RotateAxis.LeftHandExtraFinger1RotateAxisz

    LeftHandExtraFinger1JointOrient = LeftHandExtraFinger1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger1JointOrientx = LeftHandExtraFinger1JointOrient.LeftHandExtraFinger1JointOrientx
    LeftHandExtraFinger1JointOrienty = LeftHandExtraFinger1JointOrient.LeftHandExtraFinger1JointOrienty
    LeftHandExtraFinger1JointOrientz = LeftHandExtraFinger1JointOrient.LeftHandExtraFinger1JointOrientz

    LeftHandExtraFinger1MinRLimit = LeftHandExtraFinger1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger1MinRLimitx = LeftHandExtraFinger1MinRLimit.LeftHandExtraFinger1MinRLimitx
    LeftHandExtraFinger1MinRLimity = LeftHandExtraFinger1MinRLimit.LeftHandExtraFinger1MinRLimity
    LeftHandExtraFinger1MinRLimitz = LeftHandExtraFinger1MinRLimit.LeftHandExtraFinger1MinRLimitz

    LeftHandExtraFinger1MaxRLimit = LeftHandExtraFinger1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger1MaxRLimitx = LeftHandExtraFinger1MaxRLimit.LeftHandExtraFinger1MaxRLimitx
    LeftHandExtraFinger1MaxRLimity = LeftHandExtraFinger1MaxRLimit.LeftHandExtraFinger1MaxRLimity
    LeftHandExtraFinger1MaxRLimitz = LeftHandExtraFinger1MaxRLimit.LeftHandExtraFinger1MaxRLimitz

    LeftHandExtraFinger1MinRLimitEnablex = BoolField(default_value=False)

    LeftHandExtraFinger1MinRLimitEnabley = BoolField(default_value=False)

    LeftHandExtraFinger1MinRLimitEnablez = BoolField(default_value=False)

    LeftHandExtraFinger1MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandExtraFinger1MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandExtraFinger1MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandExtraFinger2 = MessageField()

    LeftHandExtraFinger2T = LeftHandExtraFinger2TField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger2Tx = LeftHandExtraFinger2T.LeftHandExtraFinger2Tx
    LeftHandExtraFinger2Ty = LeftHandExtraFinger2T.LeftHandExtraFinger2Ty
    LeftHandExtraFinger2Tz = LeftHandExtraFinger2T.LeftHandExtraFinger2Tz

    LeftHandExtraFinger2R = LeftHandExtraFinger2RField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger2Rx = LeftHandExtraFinger2R.LeftHandExtraFinger2Rx
    LeftHandExtraFinger2Ry = LeftHandExtraFinger2R.LeftHandExtraFinger2Ry
    LeftHandExtraFinger2Rz = LeftHandExtraFinger2R.LeftHandExtraFinger2Rz

    LeftHandExtraFinger2S = LeftHandExtraFinger2SField(default_value=(1.0, 1.0, 1.0))
    LeftHandExtraFinger2Sx = LeftHandExtraFinger2S.LeftHandExtraFinger2Sx
    LeftHandExtraFinger2Sy = LeftHandExtraFinger2S.LeftHandExtraFinger2Sy
    LeftHandExtraFinger2Sz = LeftHandExtraFinger2S.LeftHandExtraFinger2Sz

    LeftHandExtraFinger2RotateOrder = LeftHandExtraFinger2RotateOrderEnumField(default_value=0)

    LeftHandExtraFinger2RotateAxis = LeftHandExtraFinger2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger2RotateAxisx = LeftHandExtraFinger2RotateAxis.LeftHandExtraFinger2RotateAxisx
    LeftHandExtraFinger2RotateAxisy = LeftHandExtraFinger2RotateAxis.LeftHandExtraFinger2RotateAxisy
    LeftHandExtraFinger2RotateAxisz = LeftHandExtraFinger2RotateAxis.LeftHandExtraFinger2RotateAxisz

    LeftHandExtraFinger2JointOrient = LeftHandExtraFinger2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger2JointOrientx = LeftHandExtraFinger2JointOrient.LeftHandExtraFinger2JointOrientx
    LeftHandExtraFinger2JointOrienty = LeftHandExtraFinger2JointOrient.LeftHandExtraFinger2JointOrienty
    LeftHandExtraFinger2JointOrientz = LeftHandExtraFinger2JointOrient.LeftHandExtraFinger2JointOrientz

    LeftHandExtraFinger2MinRLimit = LeftHandExtraFinger2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger2MinRLimitx = LeftHandExtraFinger2MinRLimit.LeftHandExtraFinger2MinRLimitx
    LeftHandExtraFinger2MinRLimity = LeftHandExtraFinger2MinRLimit.LeftHandExtraFinger2MinRLimity
    LeftHandExtraFinger2MinRLimitz = LeftHandExtraFinger2MinRLimit.LeftHandExtraFinger2MinRLimitz

    LeftHandExtraFinger2MaxRLimit = LeftHandExtraFinger2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger2MaxRLimitx = LeftHandExtraFinger2MaxRLimit.LeftHandExtraFinger2MaxRLimitx
    LeftHandExtraFinger2MaxRLimity = LeftHandExtraFinger2MaxRLimit.LeftHandExtraFinger2MaxRLimity
    LeftHandExtraFinger2MaxRLimitz = LeftHandExtraFinger2MaxRLimit.LeftHandExtraFinger2MaxRLimitz

    LeftHandExtraFinger2MinRLimitEnablex = BoolField(default_value=False)

    LeftHandExtraFinger2MinRLimitEnabley = BoolField(default_value=False)

    LeftHandExtraFinger2MinRLimitEnablez = BoolField(default_value=False)

    LeftHandExtraFinger2MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandExtraFinger2MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandExtraFinger2MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandExtraFinger3 = MessageField()

    LeftHandExtraFinger3T = LeftHandExtraFinger3TField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger3Tx = LeftHandExtraFinger3T.LeftHandExtraFinger3Tx
    LeftHandExtraFinger3Ty = LeftHandExtraFinger3T.LeftHandExtraFinger3Ty
    LeftHandExtraFinger3Tz = LeftHandExtraFinger3T.LeftHandExtraFinger3Tz

    LeftHandExtraFinger3R = LeftHandExtraFinger3RField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger3Rx = LeftHandExtraFinger3R.LeftHandExtraFinger3Rx
    LeftHandExtraFinger3Ry = LeftHandExtraFinger3R.LeftHandExtraFinger3Ry
    LeftHandExtraFinger3Rz = LeftHandExtraFinger3R.LeftHandExtraFinger3Rz

    LeftHandExtraFinger3S = LeftHandExtraFinger3SField(default_value=(1.0, 1.0, 1.0))
    LeftHandExtraFinger3Sx = LeftHandExtraFinger3S.LeftHandExtraFinger3Sx
    LeftHandExtraFinger3Sy = LeftHandExtraFinger3S.LeftHandExtraFinger3Sy
    LeftHandExtraFinger3Sz = LeftHandExtraFinger3S.LeftHandExtraFinger3Sz

    LeftHandExtraFinger3RotateOrder = LeftHandExtraFinger3RotateOrderEnumField(default_value=0)

    LeftHandExtraFinger3RotateAxis = LeftHandExtraFinger3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger3RotateAxisx = LeftHandExtraFinger3RotateAxis.LeftHandExtraFinger3RotateAxisx
    LeftHandExtraFinger3RotateAxisy = LeftHandExtraFinger3RotateAxis.LeftHandExtraFinger3RotateAxisy
    LeftHandExtraFinger3RotateAxisz = LeftHandExtraFinger3RotateAxis.LeftHandExtraFinger3RotateAxisz

    LeftHandExtraFinger3JointOrient = LeftHandExtraFinger3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger3JointOrientx = LeftHandExtraFinger3JointOrient.LeftHandExtraFinger3JointOrientx
    LeftHandExtraFinger3JointOrienty = LeftHandExtraFinger3JointOrient.LeftHandExtraFinger3JointOrienty
    LeftHandExtraFinger3JointOrientz = LeftHandExtraFinger3JointOrient.LeftHandExtraFinger3JointOrientz

    LeftHandExtraFinger3MinRLimit = LeftHandExtraFinger3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger3MinRLimitx = LeftHandExtraFinger3MinRLimit.LeftHandExtraFinger3MinRLimitx
    LeftHandExtraFinger3MinRLimity = LeftHandExtraFinger3MinRLimit.LeftHandExtraFinger3MinRLimity
    LeftHandExtraFinger3MinRLimitz = LeftHandExtraFinger3MinRLimit.LeftHandExtraFinger3MinRLimitz

    LeftHandExtraFinger3MaxRLimit = LeftHandExtraFinger3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger3MaxRLimitx = LeftHandExtraFinger3MaxRLimit.LeftHandExtraFinger3MaxRLimitx
    LeftHandExtraFinger3MaxRLimity = LeftHandExtraFinger3MaxRLimit.LeftHandExtraFinger3MaxRLimity
    LeftHandExtraFinger3MaxRLimitz = LeftHandExtraFinger3MaxRLimit.LeftHandExtraFinger3MaxRLimitz

    LeftHandExtraFinger3MinRLimitEnablex = BoolField(default_value=False)

    LeftHandExtraFinger3MinRLimitEnabley = BoolField(default_value=False)

    LeftHandExtraFinger3MinRLimitEnablez = BoolField(default_value=False)

    LeftHandExtraFinger3MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandExtraFinger3MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandExtraFinger3MaxRLimitEnablez = BoolField(default_value=False)

    LeftHandExtraFinger4 = MessageField()

    LeftHandExtraFinger4T = LeftHandExtraFinger4TField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger4Tx = LeftHandExtraFinger4T.LeftHandExtraFinger4Tx
    LeftHandExtraFinger4Ty = LeftHandExtraFinger4T.LeftHandExtraFinger4Ty
    LeftHandExtraFinger4Tz = LeftHandExtraFinger4T.LeftHandExtraFinger4Tz

    LeftHandExtraFinger4R = LeftHandExtraFinger4RField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger4Rx = LeftHandExtraFinger4R.LeftHandExtraFinger4Rx
    LeftHandExtraFinger4Ry = LeftHandExtraFinger4R.LeftHandExtraFinger4Ry
    LeftHandExtraFinger4Rz = LeftHandExtraFinger4R.LeftHandExtraFinger4Rz

    LeftHandExtraFinger4S = LeftHandExtraFinger4SField(default_value=(1.0, 1.0, 1.0))
    LeftHandExtraFinger4Sx = LeftHandExtraFinger4S.LeftHandExtraFinger4Sx
    LeftHandExtraFinger4Sy = LeftHandExtraFinger4S.LeftHandExtraFinger4Sy
    LeftHandExtraFinger4Sz = LeftHandExtraFinger4S.LeftHandExtraFinger4Sz

    LeftHandExtraFinger4RotateOrder = LeftHandExtraFinger4RotateOrderEnumField(default_value=0)

    LeftHandExtraFinger4RotateAxis = LeftHandExtraFinger4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger4RotateAxisx = LeftHandExtraFinger4RotateAxis.LeftHandExtraFinger4RotateAxisx
    LeftHandExtraFinger4RotateAxisy = LeftHandExtraFinger4RotateAxis.LeftHandExtraFinger4RotateAxisy
    LeftHandExtraFinger4RotateAxisz = LeftHandExtraFinger4RotateAxis.LeftHandExtraFinger4RotateAxisz

    LeftHandExtraFinger4JointOrient = LeftHandExtraFinger4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger4JointOrientx = LeftHandExtraFinger4JointOrient.LeftHandExtraFinger4JointOrientx
    LeftHandExtraFinger4JointOrienty = LeftHandExtraFinger4JointOrient.LeftHandExtraFinger4JointOrienty
    LeftHandExtraFinger4JointOrientz = LeftHandExtraFinger4JointOrient.LeftHandExtraFinger4JointOrientz

    LeftHandExtraFinger4MinRLimit = LeftHandExtraFinger4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger4MinRLimitx = LeftHandExtraFinger4MinRLimit.LeftHandExtraFinger4MinRLimitx
    LeftHandExtraFinger4MinRLimity = LeftHandExtraFinger4MinRLimit.LeftHandExtraFinger4MinRLimity
    LeftHandExtraFinger4MinRLimitz = LeftHandExtraFinger4MinRLimit.LeftHandExtraFinger4MinRLimitz

    LeftHandExtraFinger4MaxRLimit = LeftHandExtraFinger4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger4MaxRLimitx = LeftHandExtraFinger4MaxRLimit.LeftHandExtraFinger4MaxRLimitx
    LeftHandExtraFinger4MaxRLimity = LeftHandExtraFinger4MaxRLimit.LeftHandExtraFinger4MaxRLimity
    LeftHandExtraFinger4MaxRLimitz = LeftHandExtraFinger4MaxRLimit.LeftHandExtraFinger4MaxRLimitz

    LeftHandExtraFinger4MinRLimitEnablex = BoolField(default_value=False)

    LeftHandExtraFinger4MinRLimitEnabley = BoolField(default_value=False)

    LeftHandExtraFinger4MinRLimitEnablez = BoolField(default_value=False)

    LeftHandExtraFinger4MaxRLimitEnablex = BoolField(default_value=False)

    LeftHandExtraFinger4MaxRLimitEnabley = BoolField(default_value=False)

    LeftHandExtraFinger4MaxRLimitEnablez = BoolField(default_value=False)

    RightHandThumb1 = MessageField()

    RightHandThumb1T = RightHandThumb1TField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb1Tx = RightHandThumb1T.RightHandThumb1Tx
    RightHandThumb1Ty = RightHandThumb1T.RightHandThumb1Ty
    RightHandThumb1Tz = RightHandThumb1T.RightHandThumb1Tz

    RightHandThumb1R = RightHandThumb1RField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb1Rx = RightHandThumb1R.RightHandThumb1Rx
    RightHandThumb1Ry = RightHandThumb1R.RightHandThumb1Ry
    RightHandThumb1Rz = RightHandThumb1R.RightHandThumb1Rz

    RightHandThumb1S = RightHandThumb1SField(default_value=(1.0, 1.0, 1.0))
    RightHandThumb1Sx = RightHandThumb1S.RightHandThumb1Sx
    RightHandThumb1Sy = RightHandThumb1S.RightHandThumb1Sy
    RightHandThumb1Sz = RightHandThumb1S.RightHandThumb1Sz

    RightHandThumb1RotateOrder = RightHandThumb1RotateOrderEnumField(default_value=0)

    RightHandThumb1RotateAxis = RightHandThumb1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb1RotateAxisx = RightHandThumb1RotateAxis.RightHandThumb1RotateAxisx
    RightHandThumb1RotateAxisy = RightHandThumb1RotateAxis.RightHandThumb1RotateAxisy
    RightHandThumb1RotateAxisz = RightHandThumb1RotateAxis.RightHandThumb1RotateAxisz

    RightHandThumb1JointOrient = RightHandThumb1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb1JointOrientx = RightHandThumb1JointOrient.RightHandThumb1JointOrientx
    RightHandThumb1JointOrienty = RightHandThumb1JointOrient.RightHandThumb1JointOrienty
    RightHandThumb1JointOrientz = RightHandThumb1JointOrient.RightHandThumb1JointOrientz

    RightHandThumb1MinRLimit = RightHandThumb1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb1MinRLimitx = RightHandThumb1MinRLimit.RightHandThumb1MinRLimitx
    RightHandThumb1MinRLimity = RightHandThumb1MinRLimit.RightHandThumb1MinRLimity
    RightHandThumb1MinRLimitz = RightHandThumb1MinRLimit.RightHandThumb1MinRLimitz

    RightHandThumb1MaxRLimit = RightHandThumb1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb1MaxRLimitx = RightHandThumb1MaxRLimit.RightHandThumb1MaxRLimitx
    RightHandThumb1MaxRLimity = RightHandThumb1MaxRLimit.RightHandThumb1MaxRLimity
    RightHandThumb1MaxRLimitz = RightHandThumb1MaxRLimit.RightHandThumb1MaxRLimitz

    RightHandThumb1MinRLimitEnablex = BoolField(default_value=False)

    RightHandThumb1MinRLimitEnabley = BoolField(default_value=False)

    RightHandThumb1MinRLimitEnablez = BoolField(default_value=False)

    RightHandThumb1MaxRLimitEnablex = BoolField(default_value=False)

    RightHandThumb1MaxRLimitEnabley = BoolField(default_value=False)

    RightHandThumb1MaxRLimitEnablez = BoolField(default_value=False)

    RightHandThumb2 = MessageField()

    RightHandThumb2T = RightHandThumb2TField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb2Tx = RightHandThumb2T.RightHandThumb2Tx
    RightHandThumb2Ty = RightHandThumb2T.RightHandThumb2Ty
    RightHandThumb2Tz = RightHandThumb2T.RightHandThumb2Tz

    RightHandThumb2R = RightHandThumb2RField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb2Rx = RightHandThumb2R.RightHandThumb2Rx
    RightHandThumb2Ry = RightHandThumb2R.RightHandThumb2Ry
    RightHandThumb2Rz = RightHandThumb2R.RightHandThumb2Rz

    RightHandThumb2S = RightHandThumb2SField(default_value=(1.0, 1.0, 1.0))
    RightHandThumb2Sx = RightHandThumb2S.RightHandThumb2Sx
    RightHandThumb2Sy = RightHandThumb2S.RightHandThumb2Sy
    RightHandThumb2Sz = RightHandThumb2S.RightHandThumb2Sz

    RightHandThumb2RotateOrder = RightHandThumb2RotateOrderEnumField(default_value=0)

    RightHandThumb2RotateAxis = RightHandThumb2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb2RotateAxisx = RightHandThumb2RotateAxis.RightHandThumb2RotateAxisx
    RightHandThumb2RotateAxisy = RightHandThumb2RotateAxis.RightHandThumb2RotateAxisy
    RightHandThumb2RotateAxisz = RightHandThumb2RotateAxis.RightHandThumb2RotateAxisz

    RightHandThumb2JointOrient = RightHandThumb2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb2JointOrientx = RightHandThumb2JointOrient.RightHandThumb2JointOrientx
    RightHandThumb2JointOrienty = RightHandThumb2JointOrient.RightHandThumb2JointOrienty
    RightHandThumb2JointOrientz = RightHandThumb2JointOrient.RightHandThumb2JointOrientz

    RightHandThumb2MinRLimit = RightHandThumb2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb2MinRLimitx = RightHandThumb2MinRLimit.RightHandThumb2MinRLimitx
    RightHandThumb2MinRLimity = RightHandThumb2MinRLimit.RightHandThumb2MinRLimity
    RightHandThumb2MinRLimitz = RightHandThumb2MinRLimit.RightHandThumb2MinRLimitz

    RightHandThumb2MaxRLimit = RightHandThumb2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb2MaxRLimitx = RightHandThumb2MaxRLimit.RightHandThumb2MaxRLimitx
    RightHandThumb2MaxRLimity = RightHandThumb2MaxRLimit.RightHandThumb2MaxRLimity
    RightHandThumb2MaxRLimitz = RightHandThumb2MaxRLimit.RightHandThumb2MaxRLimitz

    RightHandThumb2MinRLimitEnablex = BoolField(default_value=False)

    RightHandThumb2MinRLimitEnabley = BoolField(default_value=False)

    RightHandThumb2MinRLimitEnablez = BoolField(default_value=False)

    RightHandThumb2MaxRLimitEnablex = BoolField(default_value=False)

    RightHandThumb2MaxRLimitEnabley = BoolField(default_value=False)

    RightHandThumb2MaxRLimitEnablez = BoolField(default_value=False)

    RightHandThumb3 = MessageField()

    RightHandThumb3T = RightHandThumb3TField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb3Tx = RightHandThumb3T.RightHandThumb3Tx
    RightHandThumb3Ty = RightHandThumb3T.RightHandThumb3Ty
    RightHandThumb3Tz = RightHandThumb3T.RightHandThumb3Tz

    RightHandThumb3R = RightHandThumb3RField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb3Rx = RightHandThumb3R.RightHandThumb3Rx
    RightHandThumb3Ry = RightHandThumb3R.RightHandThumb3Ry
    RightHandThumb3Rz = RightHandThumb3R.RightHandThumb3Rz

    RightHandThumb3S = RightHandThumb3SField(default_value=(1.0, 1.0, 1.0))
    RightHandThumb3Sx = RightHandThumb3S.RightHandThumb3Sx
    RightHandThumb3Sy = RightHandThumb3S.RightHandThumb3Sy
    RightHandThumb3Sz = RightHandThumb3S.RightHandThumb3Sz

    RightHandThumb3RotateOrder = RightHandThumb3RotateOrderEnumField(default_value=0)

    RightHandThumb3RotateAxis = RightHandThumb3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb3RotateAxisx = RightHandThumb3RotateAxis.RightHandThumb3RotateAxisx
    RightHandThumb3RotateAxisy = RightHandThumb3RotateAxis.RightHandThumb3RotateAxisy
    RightHandThumb3RotateAxisz = RightHandThumb3RotateAxis.RightHandThumb3RotateAxisz

    RightHandThumb3JointOrient = RightHandThumb3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb3JointOrientx = RightHandThumb3JointOrient.RightHandThumb3JointOrientx
    RightHandThumb3JointOrienty = RightHandThumb3JointOrient.RightHandThumb3JointOrienty
    RightHandThumb3JointOrientz = RightHandThumb3JointOrient.RightHandThumb3JointOrientz

    RightHandThumb3MinRLimit = RightHandThumb3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb3MinRLimitx = RightHandThumb3MinRLimit.RightHandThumb3MinRLimitx
    RightHandThumb3MinRLimity = RightHandThumb3MinRLimit.RightHandThumb3MinRLimity
    RightHandThumb3MinRLimitz = RightHandThumb3MinRLimit.RightHandThumb3MinRLimitz

    RightHandThumb3MaxRLimit = RightHandThumb3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb3MaxRLimitx = RightHandThumb3MaxRLimit.RightHandThumb3MaxRLimitx
    RightHandThumb3MaxRLimity = RightHandThumb3MaxRLimit.RightHandThumb3MaxRLimity
    RightHandThumb3MaxRLimitz = RightHandThumb3MaxRLimit.RightHandThumb3MaxRLimitz

    RightHandThumb3MinRLimitEnablex = BoolField(default_value=False)

    RightHandThumb3MinRLimitEnabley = BoolField(default_value=False)

    RightHandThumb3MinRLimitEnablez = BoolField(default_value=False)

    RightHandThumb3MaxRLimitEnablex = BoolField(default_value=False)

    RightHandThumb3MaxRLimitEnabley = BoolField(default_value=False)

    RightHandThumb3MaxRLimitEnablez = BoolField(default_value=False)

    RightHandThumb4 = MessageField()

    RightHandThumb4T = RightHandThumb4TField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb4Tx = RightHandThumb4T.RightHandThumb4Tx
    RightHandThumb4Ty = RightHandThumb4T.RightHandThumb4Ty
    RightHandThumb4Tz = RightHandThumb4T.RightHandThumb4Tz

    RightHandThumb4R = RightHandThumb4RField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb4Rx = RightHandThumb4R.RightHandThumb4Rx
    RightHandThumb4Ry = RightHandThumb4R.RightHandThumb4Ry
    RightHandThumb4Rz = RightHandThumb4R.RightHandThumb4Rz

    RightHandThumb4S = RightHandThumb4SField(default_value=(1.0, 1.0, 1.0))
    RightHandThumb4Sx = RightHandThumb4S.RightHandThumb4Sx
    RightHandThumb4Sy = RightHandThumb4S.RightHandThumb4Sy
    RightHandThumb4Sz = RightHandThumb4S.RightHandThumb4Sz

    RightHandThumb4RotateOrder = RightHandThumb4RotateOrderEnumField(default_value=0)

    RightHandThumb4RotateAxis = RightHandThumb4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb4RotateAxisx = RightHandThumb4RotateAxis.RightHandThumb4RotateAxisx
    RightHandThumb4RotateAxisy = RightHandThumb4RotateAxis.RightHandThumb4RotateAxisy
    RightHandThumb4RotateAxisz = RightHandThumb4RotateAxis.RightHandThumb4RotateAxisz

    RightHandThumb4JointOrient = RightHandThumb4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb4JointOrientx = RightHandThumb4JointOrient.RightHandThumb4JointOrientx
    RightHandThumb4JointOrienty = RightHandThumb4JointOrient.RightHandThumb4JointOrienty
    RightHandThumb4JointOrientz = RightHandThumb4JointOrient.RightHandThumb4JointOrientz

    RightHandThumb4MinRLimit = RightHandThumb4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb4MinRLimitx = RightHandThumb4MinRLimit.RightHandThumb4MinRLimitx
    RightHandThumb4MinRLimity = RightHandThumb4MinRLimit.RightHandThumb4MinRLimity
    RightHandThumb4MinRLimitz = RightHandThumb4MinRLimit.RightHandThumb4MinRLimitz

    RightHandThumb4MaxRLimit = RightHandThumb4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb4MaxRLimitx = RightHandThumb4MaxRLimit.RightHandThumb4MaxRLimitx
    RightHandThumb4MaxRLimity = RightHandThumb4MaxRLimit.RightHandThumb4MaxRLimity
    RightHandThumb4MaxRLimitz = RightHandThumb4MaxRLimit.RightHandThumb4MaxRLimitz

    RightHandThumb4MinRLimitEnablex = BoolField(default_value=False)

    RightHandThumb4MinRLimitEnabley = BoolField(default_value=False)

    RightHandThumb4MinRLimitEnablez = BoolField(default_value=False)

    RightHandThumb4MaxRLimitEnablex = BoolField(default_value=False)

    RightHandThumb4MaxRLimitEnabley = BoolField(default_value=False)

    RightHandThumb4MaxRLimitEnablez = BoolField(default_value=False)

    RightHandIndex1 = MessageField()

    RightHandIndex1T = RightHandIndex1TField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex1Tx = RightHandIndex1T.RightHandIndex1Tx
    RightHandIndex1Ty = RightHandIndex1T.RightHandIndex1Ty
    RightHandIndex1Tz = RightHandIndex1T.RightHandIndex1Tz

    RightHandIndex1R = RightHandIndex1RField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex1Rx = RightHandIndex1R.RightHandIndex1Rx
    RightHandIndex1Ry = RightHandIndex1R.RightHandIndex1Ry
    RightHandIndex1Rz = RightHandIndex1R.RightHandIndex1Rz

    RightHandIndex1S = RightHandIndex1SField(default_value=(1.0, 1.0, 1.0))
    RightHandIndex1Sx = RightHandIndex1S.RightHandIndex1Sx
    RightHandIndex1Sy = RightHandIndex1S.RightHandIndex1Sy
    RightHandIndex1Sz = RightHandIndex1S.RightHandIndex1Sz

    RightHandIndex1RotateOrder = RightHandIndex1RotateOrderEnumField(default_value=0)

    RightHandIndex1RotateAxis = RightHandIndex1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex1RotateAxisx = RightHandIndex1RotateAxis.RightHandIndex1RotateAxisx
    RightHandIndex1RotateAxisy = RightHandIndex1RotateAxis.RightHandIndex1RotateAxisy
    RightHandIndex1RotateAxisz = RightHandIndex1RotateAxis.RightHandIndex1RotateAxisz

    RightHandIndex1JointOrient = RightHandIndex1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex1JointOrientx = RightHandIndex1JointOrient.RightHandIndex1JointOrientx
    RightHandIndex1JointOrienty = RightHandIndex1JointOrient.RightHandIndex1JointOrienty
    RightHandIndex1JointOrientz = RightHandIndex1JointOrient.RightHandIndex1JointOrientz

    RightHandIndex1MinRLimit = RightHandIndex1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex1MinRLimitx = RightHandIndex1MinRLimit.RightHandIndex1MinRLimitx
    RightHandIndex1MinRLimity = RightHandIndex1MinRLimit.RightHandIndex1MinRLimity
    RightHandIndex1MinRLimitz = RightHandIndex1MinRLimit.RightHandIndex1MinRLimitz

    RightHandIndex1MaxRLimit = RightHandIndex1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex1MaxRLimitx = RightHandIndex1MaxRLimit.RightHandIndex1MaxRLimitx
    RightHandIndex1MaxRLimity = RightHandIndex1MaxRLimit.RightHandIndex1MaxRLimity
    RightHandIndex1MaxRLimitz = RightHandIndex1MaxRLimit.RightHandIndex1MaxRLimitz

    RightHandIndex1MinRLimitEnablex = BoolField(default_value=False)

    RightHandIndex1MinRLimitEnabley = BoolField(default_value=False)

    RightHandIndex1MinRLimitEnablez = BoolField(default_value=False)

    RightHandIndex1MaxRLimitEnablex = BoolField(default_value=False)

    RightHandIndex1MaxRLimitEnabley = BoolField(default_value=False)

    RightHandIndex1MaxRLimitEnablez = BoolField(default_value=False)

    RightHandIndex2 = MessageField()

    RightHandIndex2T = RightHandIndex2TField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex2Tx = RightHandIndex2T.RightHandIndex2Tx
    RightHandIndex2Ty = RightHandIndex2T.RightHandIndex2Ty
    RightHandIndex2Tz = RightHandIndex2T.RightHandIndex2Tz

    RightHandIndex2R = RightHandIndex2RField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex2Rx = RightHandIndex2R.RightHandIndex2Rx
    RightHandIndex2Ry = RightHandIndex2R.RightHandIndex2Ry
    RightHandIndex2Rz = RightHandIndex2R.RightHandIndex2Rz

    RightHandIndex2S = RightHandIndex2SField(default_value=(1.0, 1.0, 1.0))
    RightHandIndex2Sx = RightHandIndex2S.RightHandIndex2Sx
    RightHandIndex2Sy = RightHandIndex2S.RightHandIndex2Sy
    RightHandIndex2Sz = RightHandIndex2S.RightHandIndex2Sz

    RightHandIndex2RotateOrder = RightHandIndex2RotateOrderEnumField(default_value=0)

    RightHandIndex2RotateAxis = RightHandIndex2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex2RotateAxisx = RightHandIndex2RotateAxis.RightHandIndex2RotateAxisx
    RightHandIndex2RotateAxisy = RightHandIndex2RotateAxis.RightHandIndex2RotateAxisy
    RightHandIndex2RotateAxisz = RightHandIndex2RotateAxis.RightHandIndex2RotateAxisz

    RightHandIndex2JointOrient = RightHandIndex2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex2JointOrientx = RightHandIndex2JointOrient.RightHandIndex2JointOrientx
    RightHandIndex2JointOrienty = RightHandIndex2JointOrient.RightHandIndex2JointOrienty
    RightHandIndex2JointOrientz = RightHandIndex2JointOrient.RightHandIndex2JointOrientz

    RightHandIndex2MinRLimit = RightHandIndex2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex2MinRLimitx = RightHandIndex2MinRLimit.RightHandIndex2MinRLimitx
    RightHandIndex2MinRLimity = RightHandIndex2MinRLimit.RightHandIndex2MinRLimity
    RightHandIndex2MinRLimitz = RightHandIndex2MinRLimit.RightHandIndex2MinRLimitz

    RightHandIndex2MaxRLimit = RightHandIndex2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex2MaxRLimitx = RightHandIndex2MaxRLimit.RightHandIndex2MaxRLimitx
    RightHandIndex2MaxRLimity = RightHandIndex2MaxRLimit.RightHandIndex2MaxRLimity
    RightHandIndex2MaxRLimitz = RightHandIndex2MaxRLimit.RightHandIndex2MaxRLimitz

    RightHandIndex2MinRLimitEnablex = BoolField(default_value=False)

    RightHandIndex2MinRLimitEnabley = BoolField(default_value=False)

    RightHandIndex2MinRLimitEnablez = BoolField(default_value=False)

    RightHandIndex2MaxRLimitEnablex = BoolField(default_value=False)

    RightHandIndex2MaxRLimitEnabley = BoolField(default_value=False)

    RightHandIndex2MaxRLimitEnablez = BoolField(default_value=False)

    RightHandIndex3 = MessageField()

    RightHandIndex3T = RightHandIndex3TField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex3Tx = RightHandIndex3T.RightHandIndex3Tx
    RightHandIndex3Ty = RightHandIndex3T.RightHandIndex3Ty
    RightHandIndex3Tz = RightHandIndex3T.RightHandIndex3Tz

    RightHandIndex3R = RightHandIndex3RField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex3Rx = RightHandIndex3R.RightHandIndex3Rx
    RightHandIndex3Ry = RightHandIndex3R.RightHandIndex3Ry
    RightHandIndex3Rz = RightHandIndex3R.RightHandIndex3Rz

    RightHandIndex3S = RightHandIndex3SField(default_value=(1.0, 1.0, 1.0))
    RightHandIndex3Sx = RightHandIndex3S.RightHandIndex3Sx
    RightHandIndex3Sy = RightHandIndex3S.RightHandIndex3Sy
    RightHandIndex3Sz = RightHandIndex3S.RightHandIndex3Sz

    RightHandIndex3RotateOrder = RightHandIndex3RotateOrderEnumField(default_value=0)

    RightHandIndex3RotateAxis = RightHandIndex3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex3RotateAxisx = RightHandIndex3RotateAxis.RightHandIndex3RotateAxisx
    RightHandIndex3RotateAxisy = RightHandIndex3RotateAxis.RightHandIndex3RotateAxisy
    RightHandIndex3RotateAxisz = RightHandIndex3RotateAxis.RightHandIndex3RotateAxisz

    RightHandIndex3JointOrient = RightHandIndex3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex3JointOrientx = RightHandIndex3JointOrient.RightHandIndex3JointOrientx
    RightHandIndex3JointOrienty = RightHandIndex3JointOrient.RightHandIndex3JointOrienty
    RightHandIndex3JointOrientz = RightHandIndex3JointOrient.RightHandIndex3JointOrientz

    RightHandIndex3MinRLimit = RightHandIndex3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex3MinRLimitx = RightHandIndex3MinRLimit.RightHandIndex3MinRLimitx
    RightHandIndex3MinRLimity = RightHandIndex3MinRLimit.RightHandIndex3MinRLimity
    RightHandIndex3MinRLimitz = RightHandIndex3MinRLimit.RightHandIndex3MinRLimitz

    RightHandIndex3MaxRLimit = RightHandIndex3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex3MaxRLimitx = RightHandIndex3MaxRLimit.RightHandIndex3MaxRLimitx
    RightHandIndex3MaxRLimity = RightHandIndex3MaxRLimit.RightHandIndex3MaxRLimity
    RightHandIndex3MaxRLimitz = RightHandIndex3MaxRLimit.RightHandIndex3MaxRLimitz

    RightHandIndex3MinRLimitEnablex = BoolField(default_value=False)

    RightHandIndex3MinRLimitEnabley = BoolField(default_value=False)

    RightHandIndex3MinRLimitEnablez = BoolField(default_value=False)

    RightHandIndex3MaxRLimitEnablex = BoolField(default_value=False)

    RightHandIndex3MaxRLimitEnabley = BoolField(default_value=False)

    RightHandIndex3MaxRLimitEnablez = BoolField(default_value=False)

    RightHandIndex4 = MessageField()

    RightHandIndex4T = RightHandIndex4TField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex4Tx = RightHandIndex4T.RightHandIndex4Tx
    RightHandIndex4Ty = RightHandIndex4T.RightHandIndex4Ty
    RightHandIndex4Tz = RightHandIndex4T.RightHandIndex4Tz

    RightHandIndex4R = RightHandIndex4RField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex4Rx = RightHandIndex4R.RightHandIndex4Rx
    RightHandIndex4Ry = RightHandIndex4R.RightHandIndex4Ry
    RightHandIndex4Rz = RightHandIndex4R.RightHandIndex4Rz

    RightHandIndex4S = RightHandIndex4SField(default_value=(1.0, 1.0, 1.0))
    RightHandIndex4Sx = RightHandIndex4S.RightHandIndex4Sx
    RightHandIndex4Sy = RightHandIndex4S.RightHandIndex4Sy
    RightHandIndex4Sz = RightHandIndex4S.RightHandIndex4Sz

    RightHandIndex4RotateOrder = RightHandIndex4RotateOrderEnumField(default_value=0)

    RightHandIndex4RotateAxis = RightHandIndex4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex4RotateAxisx = RightHandIndex4RotateAxis.RightHandIndex4RotateAxisx
    RightHandIndex4RotateAxisy = RightHandIndex4RotateAxis.RightHandIndex4RotateAxisy
    RightHandIndex4RotateAxisz = RightHandIndex4RotateAxis.RightHandIndex4RotateAxisz

    RightHandIndex4JointOrient = RightHandIndex4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex4JointOrientx = RightHandIndex4JointOrient.RightHandIndex4JointOrientx
    RightHandIndex4JointOrienty = RightHandIndex4JointOrient.RightHandIndex4JointOrienty
    RightHandIndex4JointOrientz = RightHandIndex4JointOrient.RightHandIndex4JointOrientz

    RightHandIndex4MinRLimit = RightHandIndex4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex4MinRLimitx = RightHandIndex4MinRLimit.RightHandIndex4MinRLimitx
    RightHandIndex4MinRLimity = RightHandIndex4MinRLimit.RightHandIndex4MinRLimity
    RightHandIndex4MinRLimitz = RightHandIndex4MinRLimit.RightHandIndex4MinRLimitz

    RightHandIndex4MaxRLimit = RightHandIndex4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex4MaxRLimitx = RightHandIndex4MaxRLimit.RightHandIndex4MaxRLimitx
    RightHandIndex4MaxRLimity = RightHandIndex4MaxRLimit.RightHandIndex4MaxRLimity
    RightHandIndex4MaxRLimitz = RightHandIndex4MaxRLimit.RightHandIndex4MaxRLimitz

    RightHandIndex4MinRLimitEnablex = BoolField(default_value=False)

    RightHandIndex4MinRLimitEnabley = BoolField(default_value=False)

    RightHandIndex4MinRLimitEnablez = BoolField(default_value=False)

    RightHandIndex4MaxRLimitEnablex = BoolField(default_value=False)

    RightHandIndex4MaxRLimitEnabley = BoolField(default_value=False)

    RightHandIndex4MaxRLimitEnablez = BoolField(default_value=False)

    RightHandMiddle1 = MessageField()

    RightHandMiddle1T = RightHandMiddle1TField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle1Tx = RightHandMiddle1T.RightHandMiddle1Tx
    RightHandMiddle1Ty = RightHandMiddle1T.RightHandMiddle1Ty
    RightHandMiddle1Tz = RightHandMiddle1T.RightHandMiddle1Tz

    RightHandMiddle1R = RightHandMiddle1RField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle1Rx = RightHandMiddle1R.RightHandMiddle1Rx
    RightHandMiddle1Ry = RightHandMiddle1R.RightHandMiddle1Ry
    RightHandMiddle1Rz = RightHandMiddle1R.RightHandMiddle1Rz

    RightHandMiddle1S = RightHandMiddle1SField(default_value=(1.0, 1.0, 1.0))
    RightHandMiddle1Sx = RightHandMiddle1S.RightHandMiddle1Sx
    RightHandMiddle1Sy = RightHandMiddle1S.RightHandMiddle1Sy
    RightHandMiddle1Sz = RightHandMiddle1S.RightHandMiddle1Sz

    RightHandMiddle1RotateOrder = RightHandMiddle1RotateOrderEnumField(default_value=0)

    RightHandMiddle1RotateAxis = RightHandMiddle1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle1RotateAxisx = RightHandMiddle1RotateAxis.RightHandMiddle1RotateAxisx
    RightHandMiddle1RotateAxisy = RightHandMiddle1RotateAxis.RightHandMiddle1RotateAxisy
    RightHandMiddle1RotateAxisz = RightHandMiddle1RotateAxis.RightHandMiddle1RotateAxisz

    RightHandMiddle1JointOrient = RightHandMiddle1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle1JointOrientx = RightHandMiddle1JointOrient.RightHandMiddle1JointOrientx
    RightHandMiddle1JointOrienty = RightHandMiddle1JointOrient.RightHandMiddle1JointOrienty
    RightHandMiddle1JointOrientz = RightHandMiddle1JointOrient.RightHandMiddle1JointOrientz

    RightHandMiddle1MinRLimit = RightHandMiddle1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle1MinRLimitx = RightHandMiddle1MinRLimit.RightHandMiddle1MinRLimitx
    RightHandMiddle1MinRLimity = RightHandMiddle1MinRLimit.RightHandMiddle1MinRLimity
    RightHandMiddle1MinRLimitz = RightHandMiddle1MinRLimit.RightHandMiddle1MinRLimitz

    RightHandMiddle1MaxRLimit = RightHandMiddle1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle1MaxRLimitx = RightHandMiddle1MaxRLimit.RightHandMiddle1MaxRLimitx
    RightHandMiddle1MaxRLimity = RightHandMiddle1MaxRLimit.RightHandMiddle1MaxRLimity
    RightHandMiddle1MaxRLimitz = RightHandMiddle1MaxRLimit.RightHandMiddle1MaxRLimitz

    RightHandMiddle1MinRLimitEnablex = BoolField(default_value=False)

    RightHandMiddle1MinRLimitEnabley = BoolField(default_value=False)

    RightHandMiddle1MinRLimitEnablez = BoolField(default_value=False)

    RightHandMiddle1MaxRLimitEnablex = BoolField(default_value=False)

    RightHandMiddle1MaxRLimitEnabley = BoolField(default_value=False)

    RightHandMiddle1MaxRLimitEnablez = BoolField(default_value=False)

    RightHandMiddle2 = MessageField()

    RightHandMiddle2T = RightHandMiddle2TField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle2Tx = RightHandMiddle2T.RightHandMiddle2Tx
    RightHandMiddle2Ty = RightHandMiddle2T.RightHandMiddle2Ty
    RightHandMiddle2Tz = RightHandMiddle2T.RightHandMiddle2Tz

    RightHandMiddle2R = RightHandMiddle2RField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle2Rx = RightHandMiddle2R.RightHandMiddle2Rx
    RightHandMiddle2Ry = RightHandMiddle2R.RightHandMiddle2Ry
    RightHandMiddle2Rz = RightHandMiddle2R.RightHandMiddle2Rz

    RightHandMiddle2S = RightHandMiddle2SField(default_value=(1.0, 1.0, 1.0))
    RightHandMiddle2Sx = RightHandMiddle2S.RightHandMiddle2Sx
    RightHandMiddle2Sy = RightHandMiddle2S.RightHandMiddle2Sy
    RightHandMiddle2Sz = RightHandMiddle2S.RightHandMiddle2Sz

    RightHandMiddle2RotateOrder = RightHandMiddle2RotateOrderEnumField(default_value=0)

    RightHandMiddle2RotateAxis = RightHandMiddle2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle2RotateAxisx = RightHandMiddle2RotateAxis.RightHandMiddle2RotateAxisx
    RightHandMiddle2RotateAxisy = RightHandMiddle2RotateAxis.RightHandMiddle2RotateAxisy
    RightHandMiddle2RotateAxisz = RightHandMiddle2RotateAxis.RightHandMiddle2RotateAxisz

    RightHandMiddle2JointOrient = RightHandMiddle2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle2JointOrientx = RightHandMiddle2JointOrient.RightHandMiddle2JointOrientx
    RightHandMiddle2JointOrienty = RightHandMiddle2JointOrient.RightHandMiddle2JointOrienty
    RightHandMiddle2JointOrientz = RightHandMiddle2JointOrient.RightHandMiddle2JointOrientz

    RightHandMiddle2MinRLimit = RightHandMiddle2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle2MinRLimitx = RightHandMiddle2MinRLimit.RightHandMiddle2MinRLimitx
    RightHandMiddle2MinRLimity = RightHandMiddle2MinRLimit.RightHandMiddle2MinRLimity
    RightHandMiddle2MinRLimitz = RightHandMiddle2MinRLimit.RightHandMiddle2MinRLimitz

    RightHandMiddle2MaxRLimit = RightHandMiddle2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle2MaxRLimitx = RightHandMiddle2MaxRLimit.RightHandMiddle2MaxRLimitx
    RightHandMiddle2MaxRLimity = RightHandMiddle2MaxRLimit.RightHandMiddle2MaxRLimity
    RightHandMiddle2MaxRLimitz = RightHandMiddle2MaxRLimit.RightHandMiddle2MaxRLimitz

    RightHandMiddle2MinRLimitEnablex = BoolField(default_value=False)

    RightHandMiddle2MinRLimitEnabley = BoolField(default_value=False)

    RightHandMiddle2MinRLimitEnablez = BoolField(default_value=False)

    RightHandMiddle2MaxRLimitEnablex = BoolField(default_value=False)

    RightHandMiddle2MaxRLimitEnabley = BoolField(default_value=False)

    RightHandMiddle2MaxRLimitEnablez = BoolField(default_value=False)

    RightHandMiddle3 = MessageField()

    RightHandMiddle3T = RightHandMiddle3TField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle3Tx = RightHandMiddle3T.RightHandMiddle3Tx
    RightHandMiddle3Ty = RightHandMiddle3T.RightHandMiddle3Ty
    RightHandMiddle3Tz = RightHandMiddle3T.RightHandMiddle3Tz

    RightHandMiddle3R = RightHandMiddle3RField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle3Rx = RightHandMiddle3R.RightHandMiddle3Rx
    RightHandMiddle3Ry = RightHandMiddle3R.RightHandMiddle3Ry
    RightHandMiddle3Rz = RightHandMiddle3R.RightHandMiddle3Rz

    RightHandMiddle3S = RightHandMiddle3SField(default_value=(1.0, 1.0, 1.0))
    RightHandMiddle3Sx = RightHandMiddle3S.RightHandMiddle3Sx
    RightHandMiddle3Sy = RightHandMiddle3S.RightHandMiddle3Sy
    RightHandMiddle3Sz = RightHandMiddle3S.RightHandMiddle3Sz

    RightHandMiddle3RotateOrder = RightHandMiddle3RotateOrderEnumField(default_value=0)

    RightHandMiddle3RotateAxis = RightHandMiddle3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle3RotateAxisx = RightHandMiddle3RotateAxis.RightHandMiddle3RotateAxisx
    RightHandMiddle3RotateAxisy = RightHandMiddle3RotateAxis.RightHandMiddle3RotateAxisy
    RightHandMiddle3RotateAxisz = RightHandMiddle3RotateAxis.RightHandMiddle3RotateAxisz

    RightHandMiddle3JointOrient = RightHandMiddle3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle3JointOrientx = RightHandMiddle3JointOrient.RightHandMiddle3JointOrientx
    RightHandMiddle3JointOrienty = RightHandMiddle3JointOrient.RightHandMiddle3JointOrienty
    RightHandMiddle3JointOrientz = RightHandMiddle3JointOrient.RightHandMiddle3JointOrientz

    RightHandMiddle3MinRLimit = RightHandMiddle3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle3MinRLimitx = RightHandMiddle3MinRLimit.RightHandMiddle3MinRLimitx
    RightHandMiddle3MinRLimity = RightHandMiddle3MinRLimit.RightHandMiddle3MinRLimity
    RightHandMiddle3MinRLimitz = RightHandMiddle3MinRLimit.RightHandMiddle3MinRLimitz

    RightHandMiddle3MaxRLimit = RightHandMiddle3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle3MaxRLimitx = RightHandMiddle3MaxRLimit.RightHandMiddle3MaxRLimitx
    RightHandMiddle3MaxRLimity = RightHandMiddle3MaxRLimit.RightHandMiddle3MaxRLimity
    RightHandMiddle3MaxRLimitz = RightHandMiddle3MaxRLimit.RightHandMiddle3MaxRLimitz

    RightHandMiddle3MinRLimitEnablex = BoolField(default_value=False)

    RightHandMiddle3MinRLimitEnabley = BoolField(default_value=False)

    RightHandMiddle3MinRLimitEnablez = BoolField(default_value=False)

    RightHandMiddle3MaxRLimitEnablex = BoolField(default_value=False)

    RightHandMiddle3MaxRLimitEnabley = BoolField(default_value=False)

    RightHandMiddle3MaxRLimitEnablez = BoolField(default_value=False)

    RightHandMiddle4 = MessageField()

    RightHandMiddle4T = RightHandMiddle4TField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle4Tx = RightHandMiddle4T.RightHandMiddle4Tx
    RightHandMiddle4Ty = RightHandMiddle4T.RightHandMiddle4Ty
    RightHandMiddle4Tz = RightHandMiddle4T.RightHandMiddle4Tz

    RightHandMiddle4R = RightHandMiddle4RField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle4Rx = RightHandMiddle4R.RightHandMiddle4Rx
    RightHandMiddle4Ry = RightHandMiddle4R.RightHandMiddle4Ry
    RightHandMiddle4Rz = RightHandMiddle4R.RightHandMiddle4Rz

    RightHandMiddle4S = RightHandMiddle4SField(default_value=(1.0, 1.0, 1.0))
    RightHandMiddle4Sx = RightHandMiddle4S.RightHandMiddle4Sx
    RightHandMiddle4Sy = RightHandMiddle4S.RightHandMiddle4Sy
    RightHandMiddle4Sz = RightHandMiddle4S.RightHandMiddle4Sz

    RightHandMiddle4RotateOrder = RightHandMiddle4RotateOrderEnumField(default_value=0)

    RightHandMiddle4RotateAxis = RightHandMiddle4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle4RotateAxisx = RightHandMiddle4RotateAxis.RightHandMiddle4RotateAxisx
    RightHandMiddle4RotateAxisy = RightHandMiddle4RotateAxis.RightHandMiddle4RotateAxisy
    RightHandMiddle4RotateAxisz = RightHandMiddle4RotateAxis.RightHandMiddle4RotateAxisz

    RightHandMiddle4JointOrient = RightHandMiddle4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle4JointOrientx = RightHandMiddle4JointOrient.RightHandMiddle4JointOrientx
    RightHandMiddle4JointOrienty = RightHandMiddle4JointOrient.RightHandMiddle4JointOrienty
    RightHandMiddle4JointOrientz = RightHandMiddle4JointOrient.RightHandMiddle4JointOrientz

    RightHandMiddle4MinRLimit = RightHandMiddle4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle4MinRLimitx = RightHandMiddle4MinRLimit.RightHandMiddle4MinRLimitx
    RightHandMiddle4MinRLimity = RightHandMiddle4MinRLimit.RightHandMiddle4MinRLimity
    RightHandMiddle4MinRLimitz = RightHandMiddle4MinRLimit.RightHandMiddle4MinRLimitz

    RightHandMiddle4MaxRLimit = RightHandMiddle4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle4MaxRLimitx = RightHandMiddle4MaxRLimit.RightHandMiddle4MaxRLimitx
    RightHandMiddle4MaxRLimity = RightHandMiddle4MaxRLimit.RightHandMiddle4MaxRLimity
    RightHandMiddle4MaxRLimitz = RightHandMiddle4MaxRLimit.RightHandMiddle4MaxRLimitz

    RightHandMiddle4MinRLimitEnablex = BoolField(default_value=False)

    RightHandMiddle4MinRLimitEnabley = BoolField(default_value=False)

    RightHandMiddle4MinRLimitEnablez = BoolField(default_value=False)

    RightHandMiddle4MaxRLimitEnablex = BoolField(default_value=False)

    RightHandMiddle4MaxRLimitEnabley = BoolField(default_value=False)

    RightHandMiddle4MaxRLimitEnablez = BoolField(default_value=False)

    RightHandRing1 = MessageField()

    RightHandRing1T = RightHandRing1TField(default_value=(0.0, 0.0, 0.0))
    RightHandRing1Tx = RightHandRing1T.RightHandRing1Tx
    RightHandRing1Ty = RightHandRing1T.RightHandRing1Ty
    RightHandRing1Tz = RightHandRing1T.RightHandRing1Tz

    RightHandRing1R = RightHandRing1RField(default_value=(0.0, 0.0, 0.0))
    RightHandRing1Rx = RightHandRing1R.RightHandRing1Rx
    RightHandRing1Ry = RightHandRing1R.RightHandRing1Ry
    RightHandRing1Rz = RightHandRing1R.RightHandRing1Rz

    RightHandRing1S = RightHandRing1SField(default_value=(1.0, 1.0, 1.0))
    RightHandRing1Sx = RightHandRing1S.RightHandRing1Sx
    RightHandRing1Sy = RightHandRing1S.RightHandRing1Sy
    RightHandRing1Sz = RightHandRing1S.RightHandRing1Sz

    RightHandRing1RotateOrder = RightHandRing1RotateOrderEnumField(default_value=0)

    RightHandRing1RotateAxis = RightHandRing1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandRing1RotateAxisx = RightHandRing1RotateAxis.RightHandRing1RotateAxisx
    RightHandRing1RotateAxisy = RightHandRing1RotateAxis.RightHandRing1RotateAxisy
    RightHandRing1RotateAxisz = RightHandRing1RotateAxis.RightHandRing1RotateAxisz

    RightHandRing1JointOrient = RightHandRing1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandRing1JointOrientx = RightHandRing1JointOrient.RightHandRing1JointOrientx
    RightHandRing1JointOrienty = RightHandRing1JointOrient.RightHandRing1JointOrienty
    RightHandRing1JointOrientz = RightHandRing1JointOrient.RightHandRing1JointOrientz

    RightHandRing1MinRLimit = RightHandRing1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandRing1MinRLimitx = RightHandRing1MinRLimit.RightHandRing1MinRLimitx
    RightHandRing1MinRLimity = RightHandRing1MinRLimit.RightHandRing1MinRLimity
    RightHandRing1MinRLimitz = RightHandRing1MinRLimit.RightHandRing1MinRLimitz

    RightHandRing1MaxRLimit = RightHandRing1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandRing1MaxRLimitx = RightHandRing1MaxRLimit.RightHandRing1MaxRLimitx
    RightHandRing1MaxRLimity = RightHandRing1MaxRLimit.RightHandRing1MaxRLimity
    RightHandRing1MaxRLimitz = RightHandRing1MaxRLimit.RightHandRing1MaxRLimitz

    RightHandRing1MinRLimitEnablex = BoolField(default_value=False)

    RightHandRing1MinRLimitEnabley = BoolField(default_value=False)

    RightHandRing1MinRLimitEnablez = BoolField(default_value=False)

    RightHandRing1MaxRLimitEnablex = BoolField(default_value=False)

    RightHandRing1MaxRLimitEnabley = BoolField(default_value=False)

    RightHandRing1MaxRLimitEnablez = BoolField(default_value=False)

    RightHandRing2 = MessageField()

    RightHandRing2T = RightHandRing2TField(default_value=(0.0, 0.0, 0.0))
    RightHandRing2Tx = RightHandRing2T.RightHandRing2Tx
    RightHandRing2Ty = RightHandRing2T.RightHandRing2Ty
    RightHandRing2Tz = RightHandRing2T.RightHandRing2Tz

    RightHandRing2R = RightHandRing2RField(default_value=(0.0, 0.0, 0.0))
    RightHandRing2Rx = RightHandRing2R.RightHandRing2Rx
    RightHandRing2Ry = RightHandRing2R.RightHandRing2Ry
    RightHandRing2Rz = RightHandRing2R.RightHandRing2Rz

    RightHandRing2S = RightHandRing2SField(default_value=(1.0, 1.0, 1.0))
    RightHandRing2Sx = RightHandRing2S.RightHandRing2Sx
    RightHandRing2Sy = RightHandRing2S.RightHandRing2Sy
    RightHandRing2Sz = RightHandRing2S.RightHandRing2Sz

    RightHandRing2RotateOrder = RightHandRing2RotateOrderEnumField(default_value=0)

    RightHandRing2RotateAxis = RightHandRing2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandRing2RotateAxisx = RightHandRing2RotateAxis.RightHandRing2RotateAxisx
    RightHandRing2RotateAxisy = RightHandRing2RotateAxis.RightHandRing2RotateAxisy
    RightHandRing2RotateAxisz = RightHandRing2RotateAxis.RightHandRing2RotateAxisz

    RightHandRing2JointOrient = RightHandRing2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandRing2JointOrientx = RightHandRing2JointOrient.RightHandRing2JointOrientx
    RightHandRing2JointOrienty = RightHandRing2JointOrient.RightHandRing2JointOrienty
    RightHandRing2JointOrientz = RightHandRing2JointOrient.RightHandRing2JointOrientz

    RightHandRing2MinRLimit = RightHandRing2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandRing2MinRLimitx = RightHandRing2MinRLimit.RightHandRing2MinRLimitx
    RightHandRing2MinRLimity = RightHandRing2MinRLimit.RightHandRing2MinRLimity
    RightHandRing2MinRLimitz = RightHandRing2MinRLimit.RightHandRing2MinRLimitz

    RightHandRing2MaxRLimit = RightHandRing2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandRing2MaxRLimitx = RightHandRing2MaxRLimit.RightHandRing2MaxRLimitx
    RightHandRing2MaxRLimity = RightHandRing2MaxRLimit.RightHandRing2MaxRLimity
    RightHandRing2MaxRLimitz = RightHandRing2MaxRLimit.RightHandRing2MaxRLimitz

    RightHandRing2MinRLimitEnablex = BoolField(default_value=False)

    RightHandRing2MinRLimitEnabley = BoolField(default_value=False)

    RightHandRing2MinRLimitEnablez = BoolField(default_value=False)

    RightHandRing2MaxRLimitEnablex = BoolField(default_value=False)

    RightHandRing2MaxRLimitEnabley = BoolField(default_value=False)

    RightHandRing2MaxRLimitEnablez = BoolField(default_value=False)

    RightHandRing3 = MessageField()

    RightHandRing3T = RightHandRing3TField(default_value=(0.0, 0.0, 0.0))
    RightHandRing3Tx = RightHandRing3T.RightHandRing3Tx
    RightHandRing3Ty = RightHandRing3T.RightHandRing3Ty
    RightHandRing3Tz = RightHandRing3T.RightHandRing3Tz

    RightHandRing3R = RightHandRing3RField(default_value=(0.0, 0.0, 0.0))
    RightHandRing3Rx = RightHandRing3R.RightHandRing3Rx
    RightHandRing3Ry = RightHandRing3R.RightHandRing3Ry
    RightHandRing3Rz = RightHandRing3R.RightHandRing3Rz

    RightHandRing3S = RightHandRing3SField(default_value=(1.0, 1.0, 1.0))
    RightHandRing3Sx = RightHandRing3S.RightHandRing3Sx
    RightHandRing3Sy = RightHandRing3S.RightHandRing3Sy
    RightHandRing3Sz = RightHandRing3S.RightHandRing3Sz

    RightHandRing3RotateOrder = RightHandRing3RotateOrderEnumField(default_value=0)

    RightHandRing3RotateAxis = RightHandRing3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandRing3RotateAxisx = RightHandRing3RotateAxis.RightHandRing3RotateAxisx
    RightHandRing3RotateAxisy = RightHandRing3RotateAxis.RightHandRing3RotateAxisy
    RightHandRing3RotateAxisz = RightHandRing3RotateAxis.RightHandRing3RotateAxisz

    RightHandRing3JointOrient = RightHandRing3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandRing3JointOrientx = RightHandRing3JointOrient.RightHandRing3JointOrientx
    RightHandRing3JointOrienty = RightHandRing3JointOrient.RightHandRing3JointOrienty
    RightHandRing3JointOrientz = RightHandRing3JointOrient.RightHandRing3JointOrientz

    RightHandRing3MinRLimit = RightHandRing3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandRing3MinRLimitx = RightHandRing3MinRLimit.RightHandRing3MinRLimitx
    RightHandRing3MinRLimity = RightHandRing3MinRLimit.RightHandRing3MinRLimity
    RightHandRing3MinRLimitz = RightHandRing3MinRLimit.RightHandRing3MinRLimitz

    RightHandRing3MaxRLimit = RightHandRing3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandRing3MaxRLimitx = RightHandRing3MaxRLimit.RightHandRing3MaxRLimitx
    RightHandRing3MaxRLimity = RightHandRing3MaxRLimit.RightHandRing3MaxRLimity
    RightHandRing3MaxRLimitz = RightHandRing3MaxRLimit.RightHandRing3MaxRLimitz

    RightHandRing3MinRLimitEnablex = BoolField(default_value=False)

    RightHandRing3MinRLimitEnabley = BoolField(default_value=False)

    RightHandRing3MinRLimitEnablez = BoolField(default_value=False)

    RightHandRing3MaxRLimitEnablex = BoolField(default_value=False)

    RightHandRing3MaxRLimitEnabley = BoolField(default_value=False)

    RightHandRing3MaxRLimitEnablez = BoolField(default_value=False)

    RightHandRing4 = MessageField()

    RightHandRing4T = RightHandRing4TField(default_value=(0.0, 0.0, 0.0))
    RightHandRing4Tx = RightHandRing4T.RightHandRing4Tx
    RightHandRing4Ty = RightHandRing4T.RightHandRing4Ty
    RightHandRing4Tz = RightHandRing4T.RightHandRing4Tz

    RightHandRing4R = RightHandRing4RField(default_value=(0.0, 0.0, 0.0))
    RightHandRing4Rx = RightHandRing4R.RightHandRing4Rx
    RightHandRing4Ry = RightHandRing4R.RightHandRing4Ry
    RightHandRing4Rz = RightHandRing4R.RightHandRing4Rz

    RightHandRing4S = RightHandRing4SField(default_value=(1.0, 1.0, 1.0))
    RightHandRing4Sx = RightHandRing4S.RightHandRing4Sx
    RightHandRing4Sy = RightHandRing4S.RightHandRing4Sy
    RightHandRing4Sz = RightHandRing4S.RightHandRing4Sz

    RightHandRing4RotateOrder = RightHandRing4RotateOrderEnumField(default_value=0)

    RightHandRing4RotateAxis = RightHandRing4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandRing4RotateAxisx = RightHandRing4RotateAxis.RightHandRing4RotateAxisx
    RightHandRing4RotateAxisy = RightHandRing4RotateAxis.RightHandRing4RotateAxisy
    RightHandRing4RotateAxisz = RightHandRing4RotateAxis.RightHandRing4RotateAxisz

    RightHandRing4JointOrient = RightHandRing4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandRing4JointOrientx = RightHandRing4JointOrient.RightHandRing4JointOrientx
    RightHandRing4JointOrienty = RightHandRing4JointOrient.RightHandRing4JointOrienty
    RightHandRing4JointOrientz = RightHandRing4JointOrient.RightHandRing4JointOrientz

    RightHandRing4MinRLimit = RightHandRing4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandRing4MinRLimitx = RightHandRing4MinRLimit.RightHandRing4MinRLimitx
    RightHandRing4MinRLimity = RightHandRing4MinRLimit.RightHandRing4MinRLimity
    RightHandRing4MinRLimitz = RightHandRing4MinRLimit.RightHandRing4MinRLimitz

    RightHandRing4MaxRLimit = RightHandRing4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandRing4MaxRLimitx = RightHandRing4MaxRLimit.RightHandRing4MaxRLimitx
    RightHandRing4MaxRLimity = RightHandRing4MaxRLimit.RightHandRing4MaxRLimity
    RightHandRing4MaxRLimitz = RightHandRing4MaxRLimit.RightHandRing4MaxRLimitz

    RightHandRing4MinRLimitEnablex = BoolField(default_value=False)

    RightHandRing4MinRLimitEnabley = BoolField(default_value=False)

    RightHandRing4MinRLimitEnablez = BoolField(default_value=False)

    RightHandRing4MaxRLimitEnablex = BoolField(default_value=False)

    RightHandRing4MaxRLimitEnabley = BoolField(default_value=False)

    RightHandRing4MaxRLimitEnablez = BoolField(default_value=False)

    RightHandPinky1 = MessageField()

    RightHandPinky1T = RightHandPinky1TField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky1Tx = RightHandPinky1T.RightHandPinky1Tx
    RightHandPinky1Ty = RightHandPinky1T.RightHandPinky1Ty
    RightHandPinky1Tz = RightHandPinky1T.RightHandPinky1Tz

    RightHandPinky1R = RightHandPinky1RField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky1Rx = RightHandPinky1R.RightHandPinky1Rx
    RightHandPinky1Ry = RightHandPinky1R.RightHandPinky1Ry
    RightHandPinky1Rz = RightHandPinky1R.RightHandPinky1Rz

    RightHandPinky1S = RightHandPinky1SField(default_value=(1.0, 1.0, 1.0))
    RightHandPinky1Sx = RightHandPinky1S.RightHandPinky1Sx
    RightHandPinky1Sy = RightHandPinky1S.RightHandPinky1Sy
    RightHandPinky1Sz = RightHandPinky1S.RightHandPinky1Sz

    RightHandPinky1RotateOrder = RightHandPinky1RotateOrderEnumField(default_value=0)

    RightHandPinky1RotateAxis = RightHandPinky1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky1RotateAxisx = RightHandPinky1RotateAxis.RightHandPinky1RotateAxisx
    RightHandPinky1RotateAxisy = RightHandPinky1RotateAxis.RightHandPinky1RotateAxisy
    RightHandPinky1RotateAxisz = RightHandPinky1RotateAxis.RightHandPinky1RotateAxisz

    RightHandPinky1JointOrient = RightHandPinky1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky1JointOrientx = RightHandPinky1JointOrient.RightHandPinky1JointOrientx
    RightHandPinky1JointOrienty = RightHandPinky1JointOrient.RightHandPinky1JointOrienty
    RightHandPinky1JointOrientz = RightHandPinky1JointOrient.RightHandPinky1JointOrientz

    RightHandPinky1MinRLimit = RightHandPinky1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky1MinRLimitx = RightHandPinky1MinRLimit.RightHandPinky1MinRLimitx
    RightHandPinky1MinRLimity = RightHandPinky1MinRLimit.RightHandPinky1MinRLimity
    RightHandPinky1MinRLimitz = RightHandPinky1MinRLimit.RightHandPinky1MinRLimitz

    RightHandPinky1MaxRLimit = RightHandPinky1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky1MaxRLimitx = RightHandPinky1MaxRLimit.RightHandPinky1MaxRLimitx
    RightHandPinky1MaxRLimity = RightHandPinky1MaxRLimit.RightHandPinky1MaxRLimity
    RightHandPinky1MaxRLimitz = RightHandPinky1MaxRLimit.RightHandPinky1MaxRLimitz

    RightHandPinky1MinRLimitEnablex = BoolField(default_value=False)

    RightHandPinky1MinRLimitEnabley = BoolField(default_value=False)

    RightHandPinky1MinRLimitEnablez = BoolField(default_value=False)

    RightHandPinky1MaxRLimitEnablex = BoolField(default_value=False)

    RightHandPinky1MaxRLimitEnabley = BoolField(default_value=False)

    RightHandPinky1MaxRLimitEnablez = BoolField(default_value=False)

    RightHandPinky2 = MessageField()

    RightHandPinky2T = RightHandPinky2TField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky2Tx = RightHandPinky2T.RightHandPinky2Tx
    RightHandPinky2Ty = RightHandPinky2T.RightHandPinky2Ty
    RightHandPinky2Tz = RightHandPinky2T.RightHandPinky2Tz

    RightHandPinky2R = RightHandPinky2RField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky2Rx = RightHandPinky2R.RightHandPinky2Rx
    RightHandPinky2Ry = RightHandPinky2R.RightHandPinky2Ry
    RightHandPinky2Rz = RightHandPinky2R.RightHandPinky2Rz

    RightHandPinky2S = RightHandPinky2SField(default_value=(1.0, 1.0, 1.0))
    RightHandPinky2Sx = RightHandPinky2S.RightHandPinky2Sx
    RightHandPinky2Sy = RightHandPinky2S.RightHandPinky2Sy
    RightHandPinky2Sz = RightHandPinky2S.RightHandPinky2Sz

    RightHandPinky2RotateOrder = RightHandPinky2RotateOrderEnumField(default_value=0)

    RightHandPinky2RotateAxis = RightHandPinky2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky2RotateAxisx = RightHandPinky2RotateAxis.RightHandPinky2RotateAxisx
    RightHandPinky2RotateAxisy = RightHandPinky2RotateAxis.RightHandPinky2RotateAxisy
    RightHandPinky2RotateAxisz = RightHandPinky2RotateAxis.RightHandPinky2RotateAxisz

    RightHandPinky2JointOrient = RightHandPinky2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky2JointOrientx = RightHandPinky2JointOrient.RightHandPinky2JointOrientx
    RightHandPinky2JointOrienty = RightHandPinky2JointOrient.RightHandPinky2JointOrienty
    RightHandPinky2JointOrientz = RightHandPinky2JointOrient.RightHandPinky2JointOrientz

    RightHandPinky2MinRLimit = RightHandPinky2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky2MinRLimitx = RightHandPinky2MinRLimit.RightHandPinky2MinRLimitx
    RightHandPinky2MinRLimity = RightHandPinky2MinRLimit.RightHandPinky2MinRLimity
    RightHandPinky2MinRLimitz = RightHandPinky2MinRLimit.RightHandPinky2MinRLimitz

    RightHandPinky2MaxRLimit = RightHandPinky2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky2MaxRLimitx = RightHandPinky2MaxRLimit.RightHandPinky2MaxRLimitx
    RightHandPinky2MaxRLimity = RightHandPinky2MaxRLimit.RightHandPinky2MaxRLimity
    RightHandPinky2MaxRLimitz = RightHandPinky2MaxRLimit.RightHandPinky2MaxRLimitz

    RightHandPinky2MinRLimitEnablex = BoolField(default_value=False)

    RightHandPinky2MinRLimitEnabley = BoolField(default_value=False)

    RightHandPinky2MinRLimitEnablez = BoolField(default_value=False)

    RightHandPinky2MaxRLimitEnablex = BoolField(default_value=False)

    RightHandPinky2MaxRLimitEnabley = BoolField(default_value=False)

    RightHandPinky2MaxRLimitEnablez = BoolField(default_value=False)

    RightHandPinky3 = MessageField()

    RightHandPinky3T = RightHandPinky3TField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky3Tx = RightHandPinky3T.RightHandPinky3Tx
    RightHandPinky3Ty = RightHandPinky3T.RightHandPinky3Ty
    RightHandPinky3Tz = RightHandPinky3T.RightHandPinky3Tz

    RightHandPinky3R = RightHandPinky3RField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky3Rx = RightHandPinky3R.RightHandPinky3Rx
    RightHandPinky3Ry = RightHandPinky3R.RightHandPinky3Ry
    RightHandPinky3Rz = RightHandPinky3R.RightHandPinky3Rz

    RightHandPinky3S = RightHandPinky3SField(default_value=(1.0, 1.0, 1.0))
    RightHandPinky3Sx = RightHandPinky3S.RightHandPinky3Sx
    RightHandPinky3Sy = RightHandPinky3S.RightHandPinky3Sy
    RightHandPinky3Sz = RightHandPinky3S.RightHandPinky3Sz

    RightHandPinky3RotateOrder = RightHandPinky3RotateOrderEnumField(default_value=0)

    RightHandPinky3RotateAxis = RightHandPinky3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky3RotateAxisx = RightHandPinky3RotateAxis.RightHandPinky3RotateAxisx
    RightHandPinky3RotateAxisy = RightHandPinky3RotateAxis.RightHandPinky3RotateAxisy
    RightHandPinky3RotateAxisz = RightHandPinky3RotateAxis.RightHandPinky3RotateAxisz

    RightHandPinky3JointOrient = RightHandPinky3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky3JointOrientx = RightHandPinky3JointOrient.RightHandPinky3JointOrientx
    RightHandPinky3JointOrienty = RightHandPinky3JointOrient.RightHandPinky3JointOrienty
    RightHandPinky3JointOrientz = RightHandPinky3JointOrient.RightHandPinky3JointOrientz

    RightHandPinky3MinRLimit = RightHandPinky3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky3MinRLimitx = RightHandPinky3MinRLimit.RightHandPinky3MinRLimitx
    RightHandPinky3MinRLimity = RightHandPinky3MinRLimit.RightHandPinky3MinRLimity
    RightHandPinky3MinRLimitz = RightHandPinky3MinRLimit.RightHandPinky3MinRLimitz

    RightHandPinky3MaxRLimit = RightHandPinky3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky3MaxRLimitx = RightHandPinky3MaxRLimit.RightHandPinky3MaxRLimitx
    RightHandPinky3MaxRLimity = RightHandPinky3MaxRLimit.RightHandPinky3MaxRLimity
    RightHandPinky3MaxRLimitz = RightHandPinky3MaxRLimit.RightHandPinky3MaxRLimitz

    RightHandPinky3MinRLimitEnablex = BoolField(default_value=False)

    RightHandPinky3MinRLimitEnabley = BoolField(default_value=False)

    RightHandPinky3MinRLimitEnablez = BoolField(default_value=False)

    RightHandPinky3MaxRLimitEnablex = BoolField(default_value=False)

    RightHandPinky3MaxRLimitEnabley = BoolField(default_value=False)

    RightHandPinky3MaxRLimitEnablez = BoolField(default_value=False)

    RightHandPinky4 = MessageField()

    RightHandPinky4T = RightHandPinky4TField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky4Tx = RightHandPinky4T.RightHandPinky4Tx
    RightHandPinky4Ty = RightHandPinky4T.RightHandPinky4Ty
    RightHandPinky4Tz = RightHandPinky4T.RightHandPinky4Tz

    RightHandPinky4R = RightHandPinky4RField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky4Rx = RightHandPinky4R.RightHandPinky4Rx
    RightHandPinky4Ry = RightHandPinky4R.RightHandPinky4Ry
    RightHandPinky4Rz = RightHandPinky4R.RightHandPinky4Rz

    RightHandPinky4S = RightHandPinky4SField(default_value=(1.0, 1.0, 1.0))
    RightHandPinky4Sx = RightHandPinky4S.RightHandPinky4Sx
    RightHandPinky4Sy = RightHandPinky4S.RightHandPinky4Sy
    RightHandPinky4Sz = RightHandPinky4S.RightHandPinky4Sz

    RightHandPinky4RotateOrder = RightHandPinky4RotateOrderEnumField(default_value=0)

    RightHandPinky4RotateAxis = RightHandPinky4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky4RotateAxisx = RightHandPinky4RotateAxis.RightHandPinky4RotateAxisx
    RightHandPinky4RotateAxisy = RightHandPinky4RotateAxis.RightHandPinky4RotateAxisy
    RightHandPinky4RotateAxisz = RightHandPinky4RotateAxis.RightHandPinky4RotateAxisz

    RightHandPinky4JointOrient = RightHandPinky4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky4JointOrientx = RightHandPinky4JointOrient.RightHandPinky4JointOrientx
    RightHandPinky4JointOrienty = RightHandPinky4JointOrient.RightHandPinky4JointOrienty
    RightHandPinky4JointOrientz = RightHandPinky4JointOrient.RightHandPinky4JointOrientz

    RightHandPinky4MinRLimit = RightHandPinky4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky4MinRLimitx = RightHandPinky4MinRLimit.RightHandPinky4MinRLimitx
    RightHandPinky4MinRLimity = RightHandPinky4MinRLimit.RightHandPinky4MinRLimity
    RightHandPinky4MinRLimitz = RightHandPinky4MinRLimit.RightHandPinky4MinRLimitz

    RightHandPinky4MaxRLimit = RightHandPinky4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky4MaxRLimitx = RightHandPinky4MaxRLimit.RightHandPinky4MaxRLimitx
    RightHandPinky4MaxRLimity = RightHandPinky4MaxRLimit.RightHandPinky4MaxRLimity
    RightHandPinky4MaxRLimitz = RightHandPinky4MaxRLimit.RightHandPinky4MaxRLimitz

    RightHandPinky4MinRLimitEnablex = BoolField(default_value=False)

    RightHandPinky4MinRLimitEnabley = BoolField(default_value=False)

    RightHandPinky4MinRLimitEnablez = BoolField(default_value=False)

    RightHandPinky4MaxRLimitEnablex = BoolField(default_value=False)

    RightHandPinky4MaxRLimitEnabley = BoolField(default_value=False)

    RightHandPinky4MaxRLimitEnablez = BoolField(default_value=False)

    RightHandExtraFinger1 = MessageField()

    RightHandExtraFinger1T = RightHandExtraFinger1TField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger1Tx = RightHandExtraFinger1T.RightHandExtraFinger1Tx
    RightHandExtraFinger1Ty = RightHandExtraFinger1T.RightHandExtraFinger1Ty
    RightHandExtraFinger1Tz = RightHandExtraFinger1T.RightHandExtraFinger1Tz

    RightHandExtraFinger1R = RightHandExtraFinger1RField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger1Rx = RightHandExtraFinger1R.RightHandExtraFinger1Rx
    RightHandExtraFinger1Ry = RightHandExtraFinger1R.RightHandExtraFinger1Ry
    RightHandExtraFinger1Rz = RightHandExtraFinger1R.RightHandExtraFinger1Rz

    RightHandExtraFinger1S = RightHandExtraFinger1SField(default_value=(1.0, 1.0, 1.0))
    RightHandExtraFinger1Sx = RightHandExtraFinger1S.RightHandExtraFinger1Sx
    RightHandExtraFinger1Sy = RightHandExtraFinger1S.RightHandExtraFinger1Sy
    RightHandExtraFinger1Sz = RightHandExtraFinger1S.RightHandExtraFinger1Sz

    RightHandExtraFinger1RotateOrder = RightHandExtraFinger1RotateOrderEnumField(default_value=0)

    RightHandExtraFinger1RotateAxis = RightHandExtraFinger1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger1RotateAxisx = RightHandExtraFinger1RotateAxis.RightHandExtraFinger1RotateAxisx
    RightHandExtraFinger1RotateAxisy = RightHandExtraFinger1RotateAxis.RightHandExtraFinger1RotateAxisy
    RightHandExtraFinger1RotateAxisz = RightHandExtraFinger1RotateAxis.RightHandExtraFinger1RotateAxisz

    RightHandExtraFinger1JointOrient = RightHandExtraFinger1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger1JointOrientx = RightHandExtraFinger1JointOrient.RightHandExtraFinger1JointOrientx
    RightHandExtraFinger1JointOrienty = RightHandExtraFinger1JointOrient.RightHandExtraFinger1JointOrienty
    RightHandExtraFinger1JointOrientz = RightHandExtraFinger1JointOrient.RightHandExtraFinger1JointOrientz

    RightHandExtraFinger1MinRLimit = RightHandExtraFinger1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger1MinRLimitx = RightHandExtraFinger1MinRLimit.RightHandExtraFinger1MinRLimitx
    RightHandExtraFinger1MinRLimity = RightHandExtraFinger1MinRLimit.RightHandExtraFinger1MinRLimity
    RightHandExtraFinger1MinRLimitz = RightHandExtraFinger1MinRLimit.RightHandExtraFinger1MinRLimitz

    RightHandExtraFinger1MaxRLimit = RightHandExtraFinger1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger1MaxRLimitx = RightHandExtraFinger1MaxRLimit.RightHandExtraFinger1MaxRLimitx
    RightHandExtraFinger1MaxRLimity = RightHandExtraFinger1MaxRLimit.RightHandExtraFinger1MaxRLimity
    RightHandExtraFinger1MaxRLimitz = RightHandExtraFinger1MaxRLimit.RightHandExtraFinger1MaxRLimitz

    RightHandExtraFinger1MinRLimitEnablex = BoolField(default_value=False)

    RightHandExtraFinger1MinRLimitEnabley = BoolField(default_value=False)

    RightHandExtraFinger1MinRLimitEnablez = BoolField(default_value=False)

    RightHandExtraFinger1MaxRLimitEnablex = BoolField(default_value=False)

    RightHandExtraFinger1MaxRLimitEnabley = BoolField(default_value=False)

    RightHandExtraFinger1MaxRLimitEnablez = BoolField(default_value=False)

    RightHandExtraFinger2 = MessageField()

    RightHandExtraFinger2T = RightHandExtraFinger2TField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger2Tx = RightHandExtraFinger2T.RightHandExtraFinger2Tx
    RightHandExtraFinger2Ty = RightHandExtraFinger2T.RightHandExtraFinger2Ty
    RightHandExtraFinger2Tz = RightHandExtraFinger2T.RightHandExtraFinger2Tz

    RightHandExtraFinger2R = RightHandExtraFinger2RField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger2Rx = RightHandExtraFinger2R.RightHandExtraFinger2Rx
    RightHandExtraFinger2Ry = RightHandExtraFinger2R.RightHandExtraFinger2Ry
    RightHandExtraFinger2Rz = RightHandExtraFinger2R.RightHandExtraFinger2Rz

    RightHandExtraFinger2S = RightHandExtraFinger2SField(default_value=(1.0, 1.0, 1.0))
    RightHandExtraFinger2Sx = RightHandExtraFinger2S.RightHandExtraFinger2Sx
    RightHandExtraFinger2Sy = RightHandExtraFinger2S.RightHandExtraFinger2Sy
    RightHandExtraFinger2Sz = RightHandExtraFinger2S.RightHandExtraFinger2Sz

    RightHandExtraFinger2RotateOrder = RightHandExtraFinger2RotateOrderEnumField(default_value=0)

    RightHandExtraFinger2RotateAxis = RightHandExtraFinger2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger2RotateAxisx = RightHandExtraFinger2RotateAxis.RightHandExtraFinger2RotateAxisx
    RightHandExtraFinger2RotateAxisy = RightHandExtraFinger2RotateAxis.RightHandExtraFinger2RotateAxisy
    RightHandExtraFinger2RotateAxisz = RightHandExtraFinger2RotateAxis.RightHandExtraFinger2RotateAxisz

    RightHandExtraFinger2JointOrient = RightHandExtraFinger2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger2JointOrientx = RightHandExtraFinger2JointOrient.RightHandExtraFinger2JointOrientx
    RightHandExtraFinger2JointOrienty = RightHandExtraFinger2JointOrient.RightHandExtraFinger2JointOrienty
    RightHandExtraFinger2JointOrientz = RightHandExtraFinger2JointOrient.RightHandExtraFinger2JointOrientz

    RightHandExtraFinger2MinRLimit = RightHandExtraFinger2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger2MinRLimitx = RightHandExtraFinger2MinRLimit.RightHandExtraFinger2MinRLimitx
    RightHandExtraFinger2MinRLimity = RightHandExtraFinger2MinRLimit.RightHandExtraFinger2MinRLimity
    RightHandExtraFinger2MinRLimitz = RightHandExtraFinger2MinRLimit.RightHandExtraFinger2MinRLimitz

    RightHandExtraFinger2MaxRLimit = RightHandExtraFinger2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger2MaxRLimitx = RightHandExtraFinger2MaxRLimit.RightHandExtraFinger2MaxRLimitx
    RightHandExtraFinger2MaxRLimity = RightHandExtraFinger2MaxRLimit.RightHandExtraFinger2MaxRLimity
    RightHandExtraFinger2MaxRLimitz = RightHandExtraFinger2MaxRLimit.RightHandExtraFinger2MaxRLimitz

    RightHandExtraFinger2MinRLimitEnablex = BoolField(default_value=False)

    RightHandExtraFinger2MinRLimitEnabley = BoolField(default_value=False)

    RightHandExtraFinger2MinRLimitEnablez = BoolField(default_value=False)

    RightHandExtraFinger2MaxRLimitEnablex = BoolField(default_value=False)

    RightHandExtraFinger2MaxRLimitEnabley = BoolField(default_value=False)

    RightHandExtraFinger2MaxRLimitEnablez = BoolField(default_value=False)

    RightHandExtraFinger3 = MessageField()

    RightHandExtraFinger3T = RightHandExtraFinger3TField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger3Tx = RightHandExtraFinger3T.RightHandExtraFinger3Tx
    RightHandExtraFinger3Ty = RightHandExtraFinger3T.RightHandExtraFinger3Ty
    RightHandExtraFinger3Tz = RightHandExtraFinger3T.RightHandExtraFinger3Tz

    RightHandExtraFinger3R = RightHandExtraFinger3RField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger3Rx = RightHandExtraFinger3R.RightHandExtraFinger3Rx
    RightHandExtraFinger3Ry = RightHandExtraFinger3R.RightHandExtraFinger3Ry
    RightHandExtraFinger3Rz = RightHandExtraFinger3R.RightHandExtraFinger3Rz

    RightHandExtraFinger3S = RightHandExtraFinger3SField(default_value=(1.0, 1.0, 1.0))
    RightHandExtraFinger3Sx = RightHandExtraFinger3S.RightHandExtraFinger3Sx
    RightHandExtraFinger3Sy = RightHandExtraFinger3S.RightHandExtraFinger3Sy
    RightHandExtraFinger3Sz = RightHandExtraFinger3S.RightHandExtraFinger3Sz

    RightHandExtraFinger3RotateOrder = RightHandExtraFinger3RotateOrderEnumField(default_value=0)

    RightHandExtraFinger3RotateAxis = RightHandExtraFinger3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger3RotateAxisx = RightHandExtraFinger3RotateAxis.RightHandExtraFinger3RotateAxisx
    RightHandExtraFinger3RotateAxisy = RightHandExtraFinger3RotateAxis.RightHandExtraFinger3RotateAxisy
    RightHandExtraFinger3RotateAxisz = RightHandExtraFinger3RotateAxis.RightHandExtraFinger3RotateAxisz

    RightHandExtraFinger3JointOrient = RightHandExtraFinger3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger3JointOrientx = RightHandExtraFinger3JointOrient.RightHandExtraFinger3JointOrientx
    RightHandExtraFinger3JointOrienty = RightHandExtraFinger3JointOrient.RightHandExtraFinger3JointOrienty
    RightHandExtraFinger3JointOrientz = RightHandExtraFinger3JointOrient.RightHandExtraFinger3JointOrientz

    RightHandExtraFinger3MinRLimit = RightHandExtraFinger3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger3MinRLimitx = RightHandExtraFinger3MinRLimit.RightHandExtraFinger3MinRLimitx
    RightHandExtraFinger3MinRLimity = RightHandExtraFinger3MinRLimit.RightHandExtraFinger3MinRLimity
    RightHandExtraFinger3MinRLimitz = RightHandExtraFinger3MinRLimit.RightHandExtraFinger3MinRLimitz

    RightHandExtraFinger3MaxRLimit = RightHandExtraFinger3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger3MaxRLimitx = RightHandExtraFinger3MaxRLimit.RightHandExtraFinger3MaxRLimitx
    RightHandExtraFinger3MaxRLimity = RightHandExtraFinger3MaxRLimit.RightHandExtraFinger3MaxRLimity
    RightHandExtraFinger3MaxRLimitz = RightHandExtraFinger3MaxRLimit.RightHandExtraFinger3MaxRLimitz

    RightHandExtraFinger3MinRLimitEnablex = BoolField(default_value=False)

    RightHandExtraFinger3MinRLimitEnabley = BoolField(default_value=False)

    RightHandExtraFinger3MinRLimitEnablez = BoolField(default_value=False)

    RightHandExtraFinger3MaxRLimitEnablex = BoolField(default_value=False)

    RightHandExtraFinger3MaxRLimitEnabley = BoolField(default_value=False)

    RightHandExtraFinger3MaxRLimitEnablez = BoolField(default_value=False)

    RightHandExtraFinger4 = MessageField()

    RightHandExtraFinger4T = RightHandExtraFinger4TField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger4Tx = RightHandExtraFinger4T.RightHandExtraFinger4Tx
    RightHandExtraFinger4Ty = RightHandExtraFinger4T.RightHandExtraFinger4Ty
    RightHandExtraFinger4Tz = RightHandExtraFinger4T.RightHandExtraFinger4Tz

    RightHandExtraFinger4R = RightHandExtraFinger4RField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger4Rx = RightHandExtraFinger4R.RightHandExtraFinger4Rx
    RightHandExtraFinger4Ry = RightHandExtraFinger4R.RightHandExtraFinger4Ry
    RightHandExtraFinger4Rz = RightHandExtraFinger4R.RightHandExtraFinger4Rz

    RightHandExtraFinger4S = RightHandExtraFinger4SField(default_value=(1.0, 1.0, 1.0))
    RightHandExtraFinger4Sx = RightHandExtraFinger4S.RightHandExtraFinger4Sx
    RightHandExtraFinger4Sy = RightHandExtraFinger4S.RightHandExtraFinger4Sy
    RightHandExtraFinger4Sz = RightHandExtraFinger4S.RightHandExtraFinger4Sz

    RightHandExtraFinger4RotateOrder = RightHandExtraFinger4RotateOrderEnumField(default_value=0)

    RightHandExtraFinger4RotateAxis = RightHandExtraFinger4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger4RotateAxisx = RightHandExtraFinger4RotateAxis.RightHandExtraFinger4RotateAxisx
    RightHandExtraFinger4RotateAxisy = RightHandExtraFinger4RotateAxis.RightHandExtraFinger4RotateAxisy
    RightHandExtraFinger4RotateAxisz = RightHandExtraFinger4RotateAxis.RightHandExtraFinger4RotateAxisz

    RightHandExtraFinger4JointOrient = RightHandExtraFinger4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger4JointOrientx = RightHandExtraFinger4JointOrient.RightHandExtraFinger4JointOrientx
    RightHandExtraFinger4JointOrienty = RightHandExtraFinger4JointOrient.RightHandExtraFinger4JointOrienty
    RightHandExtraFinger4JointOrientz = RightHandExtraFinger4JointOrient.RightHandExtraFinger4JointOrientz

    RightHandExtraFinger4MinRLimit = RightHandExtraFinger4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger4MinRLimitx = RightHandExtraFinger4MinRLimit.RightHandExtraFinger4MinRLimitx
    RightHandExtraFinger4MinRLimity = RightHandExtraFinger4MinRLimit.RightHandExtraFinger4MinRLimity
    RightHandExtraFinger4MinRLimitz = RightHandExtraFinger4MinRLimit.RightHandExtraFinger4MinRLimitz

    RightHandExtraFinger4MaxRLimit = RightHandExtraFinger4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger4MaxRLimitx = RightHandExtraFinger4MaxRLimit.RightHandExtraFinger4MaxRLimitx
    RightHandExtraFinger4MaxRLimity = RightHandExtraFinger4MaxRLimit.RightHandExtraFinger4MaxRLimity
    RightHandExtraFinger4MaxRLimitz = RightHandExtraFinger4MaxRLimit.RightHandExtraFinger4MaxRLimitz

    RightHandExtraFinger4MinRLimitEnablex = BoolField(default_value=False)

    RightHandExtraFinger4MinRLimitEnabley = BoolField(default_value=False)

    RightHandExtraFinger4MinRLimitEnablez = BoolField(default_value=False)

    RightHandExtraFinger4MaxRLimitEnablex = BoolField(default_value=False)

    RightHandExtraFinger4MaxRLimitEnabley = BoolField(default_value=False)

    RightHandExtraFinger4MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootThumb1 = MessageField()

    LeftFootThumb1T = LeftFootThumb1TField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb1Tx = LeftFootThumb1T.LeftFootThumb1Tx
    LeftFootThumb1Ty = LeftFootThumb1T.LeftFootThumb1Ty
    LeftFootThumb1Tz = LeftFootThumb1T.LeftFootThumb1Tz

    LeftFootThumb1R = LeftFootThumb1RField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb1Rx = LeftFootThumb1R.LeftFootThumb1Rx
    LeftFootThumb1Ry = LeftFootThumb1R.LeftFootThumb1Ry
    LeftFootThumb1Rz = LeftFootThumb1R.LeftFootThumb1Rz

    LeftFootThumb1S = LeftFootThumb1SField(default_value=(1.0, 1.0, 1.0))
    LeftFootThumb1Sx = LeftFootThumb1S.LeftFootThumb1Sx
    LeftFootThumb1Sy = LeftFootThumb1S.LeftFootThumb1Sy
    LeftFootThumb1Sz = LeftFootThumb1S.LeftFootThumb1Sz

    LeftFootThumb1RotateOrder = LeftFootThumb1RotateOrderEnumField(default_value=0)

    LeftFootThumb1RotateAxis = LeftFootThumb1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb1RotateAxisx = LeftFootThumb1RotateAxis.LeftFootThumb1RotateAxisx
    LeftFootThumb1RotateAxisy = LeftFootThumb1RotateAxis.LeftFootThumb1RotateAxisy
    LeftFootThumb1RotateAxisz = LeftFootThumb1RotateAxis.LeftFootThumb1RotateAxisz

    LeftFootThumb1JointOrient = LeftFootThumb1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb1JointOrientx = LeftFootThumb1JointOrient.LeftFootThumb1JointOrientx
    LeftFootThumb1JointOrienty = LeftFootThumb1JointOrient.LeftFootThumb1JointOrienty
    LeftFootThumb1JointOrientz = LeftFootThumb1JointOrient.LeftFootThumb1JointOrientz

    LeftFootThumb1MinRLimit = LeftFootThumb1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb1MinRLimitx = LeftFootThumb1MinRLimit.LeftFootThumb1MinRLimitx
    LeftFootThumb1MinRLimity = LeftFootThumb1MinRLimit.LeftFootThumb1MinRLimity
    LeftFootThumb1MinRLimitz = LeftFootThumb1MinRLimit.LeftFootThumb1MinRLimitz

    LeftFootThumb1MaxRLimit = LeftFootThumb1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb1MaxRLimitx = LeftFootThumb1MaxRLimit.LeftFootThumb1MaxRLimitx
    LeftFootThumb1MaxRLimity = LeftFootThumb1MaxRLimit.LeftFootThumb1MaxRLimity
    LeftFootThumb1MaxRLimitz = LeftFootThumb1MaxRLimit.LeftFootThumb1MaxRLimitz

    LeftFootThumb1MinRLimitEnablex = BoolField(default_value=False)

    LeftFootThumb1MinRLimitEnabley = BoolField(default_value=False)

    LeftFootThumb1MinRLimitEnablez = BoolField(default_value=False)

    LeftFootThumb1MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootThumb1MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootThumb1MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootThumb2 = MessageField()

    LeftFootThumb2T = LeftFootThumb2TField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb2Tx = LeftFootThumb2T.LeftFootThumb2Tx
    LeftFootThumb2Ty = LeftFootThumb2T.LeftFootThumb2Ty
    LeftFootThumb2Tz = LeftFootThumb2T.LeftFootThumb2Tz

    LeftFootThumb2R = LeftFootThumb2RField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb2Rx = LeftFootThumb2R.LeftFootThumb2Rx
    LeftFootThumb2Ry = LeftFootThumb2R.LeftFootThumb2Ry
    LeftFootThumb2Rz = LeftFootThumb2R.LeftFootThumb2Rz

    LeftFootThumb2S = LeftFootThumb2SField(default_value=(1.0, 1.0, 1.0))
    LeftFootThumb2Sx = LeftFootThumb2S.LeftFootThumb2Sx
    LeftFootThumb2Sy = LeftFootThumb2S.LeftFootThumb2Sy
    LeftFootThumb2Sz = LeftFootThumb2S.LeftFootThumb2Sz

    LeftFootThumb2RotateOrder = LeftFootThumb2RotateOrderEnumField(default_value=0)

    LeftFootThumb2RotateAxis = LeftFootThumb2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb2RotateAxisx = LeftFootThumb2RotateAxis.LeftFootThumb2RotateAxisx
    LeftFootThumb2RotateAxisy = LeftFootThumb2RotateAxis.LeftFootThumb2RotateAxisy
    LeftFootThumb2RotateAxisz = LeftFootThumb2RotateAxis.LeftFootThumb2RotateAxisz

    LeftFootThumb2JointOrient = LeftFootThumb2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb2JointOrientx = LeftFootThumb2JointOrient.LeftFootThumb2JointOrientx
    LeftFootThumb2JointOrienty = LeftFootThumb2JointOrient.LeftFootThumb2JointOrienty
    LeftFootThumb2JointOrientz = LeftFootThumb2JointOrient.LeftFootThumb2JointOrientz

    LeftFootThumb2MinRLimit = LeftFootThumb2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb2MinRLimitx = LeftFootThumb2MinRLimit.LeftFootThumb2MinRLimitx
    LeftFootThumb2MinRLimity = LeftFootThumb2MinRLimit.LeftFootThumb2MinRLimity
    LeftFootThumb2MinRLimitz = LeftFootThumb2MinRLimit.LeftFootThumb2MinRLimitz

    LeftFootThumb2MaxRLimit = LeftFootThumb2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb2MaxRLimitx = LeftFootThumb2MaxRLimit.LeftFootThumb2MaxRLimitx
    LeftFootThumb2MaxRLimity = LeftFootThumb2MaxRLimit.LeftFootThumb2MaxRLimity
    LeftFootThumb2MaxRLimitz = LeftFootThumb2MaxRLimit.LeftFootThumb2MaxRLimitz

    LeftFootThumb2MinRLimitEnablex = BoolField(default_value=False)

    LeftFootThumb2MinRLimitEnabley = BoolField(default_value=False)

    LeftFootThumb2MinRLimitEnablez = BoolField(default_value=False)

    LeftFootThumb2MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootThumb2MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootThumb2MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootThumb3 = MessageField()

    LeftFootThumb3T = LeftFootThumb3TField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb3Tx = LeftFootThumb3T.LeftFootThumb3Tx
    LeftFootThumb3Ty = LeftFootThumb3T.LeftFootThumb3Ty
    LeftFootThumb3Tz = LeftFootThumb3T.LeftFootThumb3Tz

    LeftFootThumb3R = LeftFootThumb3RField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb3Rx = LeftFootThumb3R.LeftFootThumb3Rx
    LeftFootThumb3Ry = LeftFootThumb3R.LeftFootThumb3Ry
    LeftFootThumb3Rz = LeftFootThumb3R.LeftFootThumb3Rz

    LeftFootThumb3S = LeftFootThumb3SField(default_value=(1.0, 1.0, 1.0))
    LeftFootThumb3Sx = LeftFootThumb3S.LeftFootThumb3Sx
    LeftFootThumb3Sy = LeftFootThumb3S.LeftFootThumb3Sy
    LeftFootThumb3Sz = LeftFootThumb3S.LeftFootThumb3Sz

    LeftFootThumb3RotateOrder = LeftFootThumb3RotateOrderEnumField(default_value=0)

    LeftFootThumb3RotateAxis = LeftFootThumb3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb3RotateAxisx = LeftFootThumb3RotateAxis.LeftFootThumb3RotateAxisx
    LeftFootThumb3RotateAxisy = LeftFootThumb3RotateAxis.LeftFootThumb3RotateAxisy
    LeftFootThumb3RotateAxisz = LeftFootThumb3RotateAxis.LeftFootThumb3RotateAxisz

    LeftFootThumb3JointOrient = LeftFootThumb3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb3JointOrientx = LeftFootThumb3JointOrient.LeftFootThumb3JointOrientx
    LeftFootThumb3JointOrienty = LeftFootThumb3JointOrient.LeftFootThumb3JointOrienty
    LeftFootThumb3JointOrientz = LeftFootThumb3JointOrient.LeftFootThumb3JointOrientz

    LeftFootThumb3MinRLimit = LeftFootThumb3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb3MinRLimitx = LeftFootThumb3MinRLimit.LeftFootThumb3MinRLimitx
    LeftFootThumb3MinRLimity = LeftFootThumb3MinRLimit.LeftFootThumb3MinRLimity
    LeftFootThumb3MinRLimitz = LeftFootThumb3MinRLimit.LeftFootThumb3MinRLimitz

    LeftFootThumb3MaxRLimit = LeftFootThumb3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb3MaxRLimitx = LeftFootThumb3MaxRLimit.LeftFootThumb3MaxRLimitx
    LeftFootThumb3MaxRLimity = LeftFootThumb3MaxRLimit.LeftFootThumb3MaxRLimity
    LeftFootThumb3MaxRLimitz = LeftFootThumb3MaxRLimit.LeftFootThumb3MaxRLimitz

    LeftFootThumb3MinRLimitEnablex = BoolField(default_value=False)

    LeftFootThumb3MinRLimitEnabley = BoolField(default_value=False)

    LeftFootThumb3MinRLimitEnablez = BoolField(default_value=False)

    LeftFootThumb3MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootThumb3MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootThumb3MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootThumb4 = MessageField()

    LeftFootThumb4T = LeftFootThumb4TField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb4Tx = LeftFootThumb4T.LeftFootThumb4Tx
    LeftFootThumb4Ty = LeftFootThumb4T.LeftFootThumb4Ty
    LeftFootThumb4Tz = LeftFootThumb4T.LeftFootThumb4Tz

    LeftFootThumb4R = LeftFootThumb4RField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb4Rx = LeftFootThumb4R.LeftFootThumb4Rx
    LeftFootThumb4Ry = LeftFootThumb4R.LeftFootThumb4Ry
    LeftFootThumb4Rz = LeftFootThumb4R.LeftFootThumb4Rz

    LeftFootThumb4S = LeftFootThumb4SField(default_value=(1.0, 1.0, 1.0))
    LeftFootThumb4Sx = LeftFootThumb4S.LeftFootThumb4Sx
    LeftFootThumb4Sy = LeftFootThumb4S.LeftFootThumb4Sy
    LeftFootThumb4Sz = LeftFootThumb4S.LeftFootThumb4Sz

    LeftFootThumb4RotateOrder = LeftFootThumb4RotateOrderEnumField(default_value=0)

    LeftFootThumb4RotateAxis = LeftFootThumb4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb4RotateAxisx = LeftFootThumb4RotateAxis.LeftFootThumb4RotateAxisx
    LeftFootThumb4RotateAxisy = LeftFootThumb4RotateAxis.LeftFootThumb4RotateAxisy
    LeftFootThumb4RotateAxisz = LeftFootThumb4RotateAxis.LeftFootThumb4RotateAxisz

    LeftFootThumb4JointOrient = LeftFootThumb4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb4JointOrientx = LeftFootThumb4JointOrient.LeftFootThumb4JointOrientx
    LeftFootThumb4JointOrienty = LeftFootThumb4JointOrient.LeftFootThumb4JointOrienty
    LeftFootThumb4JointOrientz = LeftFootThumb4JointOrient.LeftFootThumb4JointOrientz

    LeftFootThumb4MinRLimit = LeftFootThumb4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb4MinRLimitx = LeftFootThumb4MinRLimit.LeftFootThumb4MinRLimitx
    LeftFootThumb4MinRLimity = LeftFootThumb4MinRLimit.LeftFootThumb4MinRLimity
    LeftFootThumb4MinRLimitz = LeftFootThumb4MinRLimit.LeftFootThumb4MinRLimitz

    LeftFootThumb4MaxRLimit = LeftFootThumb4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb4MaxRLimitx = LeftFootThumb4MaxRLimit.LeftFootThumb4MaxRLimitx
    LeftFootThumb4MaxRLimity = LeftFootThumb4MaxRLimit.LeftFootThumb4MaxRLimity
    LeftFootThumb4MaxRLimitz = LeftFootThumb4MaxRLimit.LeftFootThumb4MaxRLimitz

    LeftFootThumb4MinRLimitEnablex = BoolField(default_value=False)

    LeftFootThumb4MinRLimitEnabley = BoolField(default_value=False)

    LeftFootThumb4MinRLimitEnablez = BoolField(default_value=False)

    LeftFootThumb4MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootThumb4MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootThumb4MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootIndex1 = MessageField()

    LeftFootIndex1T = LeftFootIndex1TField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex1Tx = LeftFootIndex1T.LeftFootIndex1Tx
    LeftFootIndex1Ty = LeftFootIndex1T.LeftFootIndex1Ty
    LeftFootIndex1Tz = LeftFootIndex1T.LeftFootIndex1Tz

    LeftFootIndex1R = LeftFootIndex1RField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex1Rx = LeftFootIndex1R.LeftFootIndex1Rx
    LeftFootIndex1Ry = LeftFootIndex1R.LeftFootIndex1Ry
    LeftFootIndex1Rz = LeftFootIndex1R.LeftFootIndex1Rz

    LeftFootIndex1S = LeftFootIndex1SField(default_value=(1.0, 1.0, 1.0))
    LeftFootIndex1Sx = LeftFootIndex1S.LeftFootIndex1Sx
    LeftFootIndex1Sy = LeftFootIndex1S.LeftFootIndex1Sy
    LeftFootIndex1Sz = LeftFootIndex1S.LeftFootIndex1Sz

    LeftFootIndex1RotateOrder = LeftFootIndex1RotateOrderEnumField(default_value=0)

    LeftFootIndex1RotateAxis = LeftFootIndex1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex1RotateAxisx = LeftFootIndex1RotateAxis.LeftFootIndex1RotateAxisx
    LeftFootIndex1RotateAxisy = LeftFootIndex1RotateAxis.LeftFootIndex1RotateAxisy
    LeftFootIndex1RotateAxisz = LeftFootIndex1RotateAxis.LeftFootIndex1RotateAxisz

    LeftFootIndex1JointOrient = LeftFootIndex1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex1JointOrientx = LeftFootIndex1JointOrient.LeftFootIndex1JointOrientx
    LeftFootIndex1JointOrienty = LeftFootIndex1JointOrient.LeftFootIndex1JointOrienty
    LeftFootIndex1JointOrientz = LeftFootIndex1JointOrient.LeftFootIndex1JointOrientz

    LeftFootIndex1MinRLimit = LeftFootIndex1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex1MinRLimitx = LeftFootIndex1MinRLimit.LeftFootIndex1MinRLimitx
    LeftFootIndex1MinRLimity = LeftFootIndex1MinRLimit.LeftFootIndex1MinRLimity
    LeftFootIndex1MinRLimitz = LeftFootIndex1MinRLimit.LeftFootIndex1MinRLimitz

    LeftFootIndex1MaxRLimit = LeftFootIndex1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex1MaxRLimitx = LeftFootIndex1MaxRLimit.LeftFootIndex1MaxRLimitx
    LeftFootIndex1MaxRLimity = LeftFootIndex1MaxRLimit.LeftFootIndex1MaxRLimity
    LeftFootIndex1MaxRLimitz = LeftFootIndex1MaxRLimit.LeftFootIndex1MaxRLimitz

    LeftFootIndex1MinRLimitEnablex = BoolField(default_value=False)

    LeftFootIndex1MinRLimitEnabley = BoolField(default_value=False)

    LeftFootIndex1MinRLimitEnablez = BoolField(default_value=False)

    LeftFootIndex1MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootIndex1MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootIndex1MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootIndex2 = MessageField()

    LeftFootIndex2T = LeftFootIndex2TField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex2Tx = LeftFootIndex2T.LeftFootIndex2Tx
    LeftFootIndex2Ty = LeftFootIndex2T.LeftFootIndex2Ty
    LeftFootIndex2Tz = LeftFootIndex2T.LeftFootIndex2Tz

    LeftFootIndex2R = LeftFootIndex2RField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex2Rx = LeftFootIndex2R.LeftFootIndex2Rx
    LeftFootIndex2Ry = LeftFootIndex2R.LeftFootIndex2Ry
    LeftFootIndex2Rz = LeftFootIndex2R.LeftFootIndex2Rz

    LeftFootIndex2S = LeftFootIndex2SField(default_value=(1.0, 1.0, 1.0))
    LeftFootIndex2Sx = LeftFootIndex2S.LeftFootIndex2Sx
    LeftFootIndex2Sy = LeftFootIndex2S.LeftFootIndex2Sy
    LeftFootIndex2Sz = LeftFootIndex2S.LeftFootIndex2Sz

    LeftFootIndex2RotateOrder = LeftFootIndex2RotateOrderEnumField(default_value=0)

    LeftFootIndex2RotateAxis = LeftFootIndex2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex2RotateAxisx = LeftFootIndex2RotateAxis.LeftFootIndex2RotateAxisx
    LeftFootIndex2RotateAxisy = LeftFootIndex2RotateAxis.LeftFootIndex2RotateAxisy
    LeftFootIndex2RotateAxisz = LeftFootIndex2RotateAxis.LeftFootIndex2RotateAxisz

    LeftFootIndex2JointOrient = LeftFootIndex2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex2JointOrientx = LeftFootIndex2JointOrient.LeftFootIndex2JointOrientx
    LeftFootIndex2JointOrienty = LeftFootIndex2JointOrient.LeftFootIndex2JointOrienty
    LeftFootIndex2JointOrientz = LeftFootIndex2JointOrient.LeftFootIndex2JointOrientz

    LeftFootIndex2MinRLimit = LeftFootIndex2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex2MinRLimitx = LeftFootIndex2MinRLimit.LeftFootIndex2MinRLimitx
    LeftFootIndex2MinRLimity = LeftFootIndex2MinRLimit.LeftFootIndex2MinRLimity
    LeftFootIndex2MinRLimitz = LeftFootIndex2MinRLimit.LeftFootIndex2MinRLimitz

    LeftFootIndex2MaxRLimit = LeftFootIndex2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex2MaxRLimitx = LeftFootIndex2MaxRLimit.LeftFootIndex2MaxRLimitx
    LeftFootIndex2MaxRLimity = LeftFootIndex2MaxRLimit.LeftFootIndex2MaxRLimity
    LeftFootIndex2MaxRLimitz = LeftFootIndex2MaxRLimit.LeftFootIndex2MaxRLimitz

    LeftFootIndex2MinRLimitEnablex = BoolField(default_value=False)

    LeftFootIndex2MinRLimitEnabley = BoolField(default_value=False)

    LeftFootIndex2MinRLimitEnablez = BoolField(default_value=False)

    LeftFootIndex2MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootIndex2MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootIndex2MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootIndex3 = MessageField()

    LeftFootIndex3T = LeftFootIndex3TField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex3Tx = LeftFootIndex3T.LeftFootIndex3Tx
    LeftFootIndex3Ty = LeftFootIndex3T.LeftFootIndex3Ty
    LeftFootIndex3Tz = LeftFootIndex3T.LeftFootIndex3Tz

    LeftFootIndex3R = LeftFootIndex3RField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex3Rx = LeftFootIndex3R.LeftFootIndex3Rx
    LeftFootIndex3Ry = LeftFootIndex3R.LeftFootIndex3Ry
    LeftFootIndex3Rz = LeftFootIndex3R.LeftFootIndex3Rz

    LeftFootIndex3S = LeftFootIndex3SField(default_value=(1.0, 1.0, 1.0))
    LeftFootIndex3Sx = LeftFootIndex3S.LeftFootIndex3Sx
    LeftFootIndex3Sy = LeftFootIndex3S.LeftFootIndex3Sy
    LeftFootIndex3Sz = LeftFootIndex3S.LeftFootIndex3Sz

    LeftFootIndex3RotateOrder = LeftFootIndex3RotateOrderEnumField(default_value=0)

    LeftFootIndex3RotateAxis = LeftFootIndex3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex3RotateAxisx = LeftFootIndex3RotateAxis.LeftFootIndex3RotateAxisx
    LeftFootIndex3RotateAxisy = LeftFootIndex3RotateAxis.LeftFootIndex3RotateAxisy
    LeftFootIndex3RotateAxisz = LeftFootIndex3RotateAxis.LeftFootIndex3RotateAxisz

    LeftFootIndex3JointOrient = LeftFootIndex3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex3JointOrientx = LeftFootIndex3JointOrient.LeftFootIndex3JointOrientx
    LeftFootIndex3JointOrienty = LeftFootIndex3JointOrient.LeftFootIndex3JointOrienty
    LeftFootIndex3JointOrientz = LeftFootIndex3JointOrient.LeftFootIndex3JointOrientz

    LeftFootIndex3MinRLimit = LeftFootIndex3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex3MinRLimitx = LeftFootIndex3MinRLimit.LeftFootIndex3MinRLimitx
    LeftFootIndex3MinRLimity = LeftFootIndex3MinRLimit.LeftFootIndex3MinRLimity
    LeftFootIndex3MinRLimitz = LeftFootIndex3MinRLimit.LeftFootIndex3MinRLimitz

    LeftFootIndex3MaxRLimit = LeftFootIndex3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex3MaxRLimitx = LeftFootIndex3MaxRLimit.LeftFootIndex3MaxRLimitx
    LeftFootIndex3MaxRLimity = LeftFootIndex3MaxRLimit.LeftFootIndex3MaxRLimity
    LeftFootIndex3MaxRLimitz = LeftFootIndex3MaxRLimit.LeftFootIndex3MaxRLimitz

    LeftFootIndex3MinRLimitEnablex = BoolField(default_value=False)

    LeftFootIndex3MinRLimitEnabley = BoolField(default_value=False)

    LeftFootIndex3MinRLimitEnablez = BoolField(default_value=False)

    LeftFootIndex3MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootIndex3MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootIndex3MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootIndex4 = MessageField()

    LeftFootIndex4T = LeftFootIndex4TField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex4Tx = LeftFootIndex4T.LeftFootIndex4Tx
    LeftFootIndex4Ty = LeftFootIndex4T.LeftFootIndex4Ty
    LeftFootIndex4Tz = LeftFootIndex4T.LeftFootIndex4Tz

    LeftFootIndex4R = LeftFootIndex4RField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex4Rx = LeftFootIndex4R.LeftFootIndex4Rx
    LeftFootIndex4Ry = LeftFootIndex4R.LeftFootIndex4Ry
    LeftFootIndex4Rz = LeftFootIndex4R.LeftFootIndex4Rz

    LeftFootIndex4S = LeftFootIndex4SField(default_value=(1.0, 1.0, 1.0))
    LeftFootIndex4Sx = LeftFootIndex4S.LeftFootIndex4Sx
    LeftFootIndex4Sy = LeftFootIndex4S.LeftFootIndex4Sy
    LeftFootIndex4Sz = LeftFootIndex4S.LeftFootIndex4Sz

    LeftFootIndex4RotateOrder = LeftFootIndex4RotateOrderEnumField(default_value=0)

    LeftFootIndex4RotateAxis = LeftFootIndex4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex4RotateAxisx = LeftFootIndex4RotateAxis.LeftFootIndex4RotateAxisx
    LeftFootIndex4RotateAxisy = LeftFootIndex4RotateAxis.LeftFootIndex4RotateAxisy
    LeftFootIndex4RotateAxisz = LeftFootIndex4RotateAxis.LeftFootIndex4RotateAxisz

    LeftFootIndex4JointOrient = LeftFootIndex4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex4JointOrientx = LeftFootIndex4JointOrient.LeftFootIndex4JointOrientx
    LeftFootIndex4JointOrienty = LeftFootIndex4JointOrient.LeftFootIndex4JointOrienty
    LeftFootIndex4JointOrientz = LeftFootIndex4JointOrient.LeftFootIndex4JointOrientz

    LeftFootIndex4MinRLimit = LeftFootIndex4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex4MinRLimitx = LeftFootIndex4MinRLimit.LeftFootIndex4MinRLimitx
    LeftFootIndex4MinRLimity = LeftFootIndex4MinRLimit.LeftFootIndex4MinRLimity
    LeftFootIndex4MinRLimitz = LeftFootIndex4MinRLimit.LeftFootIndex4MinRLimitz

    LeftFootIndex4MaxRLimit = LeftFootIndex4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex4MaxRLimitx = LeftFootIndex4MaxRLimit.LeftFootIndex4MaxRLimitx
    LeftFootIndex4MaxRLimity = LeftFootIndex4MaxRLimit.LeftFootIndex4MaxRLimity
    LeftFootIndex4MaxRLimitz = LeftFootIndex4MaxRLimit.LeftFootIndex4MaxRLimitz

    LeftFootIndex4MinRLimitEnablex = BoolField(default_value=False)

    LeftFootIndex4MinRLimitEnabley = BoolField(default_value=False)

    LeftFootIndex4MinRLimitEnablez = BoolField(default_value=False)

    LeftFootIndex4MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootIndex4MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootIndex4MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootMiddle1 = MessageField()

    LeftFootMiddle1T = LeftFootMiddle1TField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle1Tx = LeftFootMiddle1T.LeftFootMiddle1Tx
    LeftFootMiddle1Ty = LeftFootMiddle1T.LeftFootMiddle1Ty
    LeftFootMiddle1Tz = LeftFootMiddle1T.LeftFootMiddle1Tz

    LeftFootMiddle1R = LeftFootMiddle1RField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle1Rx = LeftFootMiddle1R.LeftFootMiddle1Rx
    LeftFootMiddle1Ry = LeftFootMiddle1R.LeftFootMiddle1Ry
    LeftFootMiddle1Rz = LeftFootMiddle1R.LeftFootMiddle1Rz

    LeftFootMiddle1S = LeftFootMiddle1SField(default_value=(1.0, 1.0, 1.0))
    LeftFootMiddle1Sx = LeftFootMiddle1S.LeftFootMiddle1Sx
    LeftFootMiddle1Sy = LeftFootMiddle1S.LeftFootMiddle1Sy
    LeftFootMiddle1Sz = LeftFootMiddle1S.LeftFootMiddle1Sz

    LeftFootMiddle1RotateOrder = LeftFootMiddle1RotateOrderEnumField(default_value=0)

    LeftFootMiddle1RotateAxis = LeftFootMiddle1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle1RotateAxisx = LeftFootMiddle1RotateAxis.LeftFootMiddle1RotateAxisx
    LeftFootMiddle1RotateAxisy = LeftFootMiddle1RotateAxis.LeftFootMiddle1RotateAxisy
    LeftFootMiddle1RotateAxisz = LeftFootMiddle1RotateAxis.LeftFootMiddle1RotateAxisz

    LeftFootMiddle1JointOrient = LeftFootMiddle1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle1JointOrientx = LeftFootMiddle1JointOrient.LeftFootMiddle1JointOrientx
    LeftFootMiddle1JointOrienty = LeftFootMiddle1JointOrient.LeftFootMiddle1JointOrienty
    LeftFootMiddle1JointOrientz = LeftFootMiddle1JointOrient.LeftFootMiddle1JointOrientz

    LeftFootMiddle1MinRLimit = LeftFootMiddle1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle1MinRLimitx = LeftFootMiddle1MinRLimit.LeftFootMiddle1MinRLimitx
    LeftFootMiddle1MinRLimity = LeftFootMiddle1MinRLimit.LeftFootMiddle1MinRLimity
    LeftFootMiddle1MinRLimitz = LeftFootMiddle1MinRLimit.LeftFootMiddle1MinRLimitz

    LeftFootMiddle1MaxRLimit = LeftFootMiddle1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle1MaxRLimitx = LeftFootMiddle1MaxRLimit.LeftFootMiddle1MaxRLimitx
    LeftFootMiddle1MaxRLimity = LeftFootMiddle1MaxRLimit.LeftFootMiddle1MaxRLimity
    LeftFootMiddle1MaxRLimitz = LeftFootMiddle1MaxRLimit.LeftFootMiddle1MaxRLimitz

    LeftFootMiddle1MinRLimitEnablex = BoolField(default_value=False)

    LeftFootMiddle1MinRLimitEnabley = BoolField(default_value=False)

    LeftFootMiddle1MinRLimitEnablez = BoolField(default_value=False)

    LeftFootMiddle1MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootMiddle1MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootMiddle1MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootMiddle2 = MessageField()

    LeftFootMiddle2T = LeftFootMiddle2TField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle2Tx = LeftFootMiddle2T.LeftFootMiddle2Tx
    LeftFootMiddle2Ty = LeftFootMiddle2T.LeftFootMiddle2Ty
    LeftFootMiddle2Tz = LeftFootMiddle2T.LeftFootMiddle2Tz

    LeftFootMiddle2R = LeftFootMiddle2RField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle2Rx = LeftFootMiddle2R.LeftFootMiddle2Rx
    LeftFootMiddle2Ry = LeftFootMiddle2R.LeftFootMiddle2Ry
    LeftFootMiddle2Rz = LeftFootMiddle2R.LeftFootMiddle2Rz

    LeftFootMiddle2S = LeftFootMiddle2SField(default_value=(1.0, 1.0, 1.0))
    LeftFootMiddle2Sx = LeftFootMiddle2S.LeftFootMiddle2Sx
    LeftFootMiddle2Sy = LeftFootMiddle2S.LeftFootMiddle2Sy
    LeftFootMiddle2Sz = LeftFootMiddle2S.LeftFootMiddle2Sz

    LeftFootMiddle2RotateOrder = LeftFootMiddle2RotateOrderEnumField(default_value=0)

    LeftFootMiddle2RotateAxis = LeftFootMiddle2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle2RotateAxisx = LeftFootMiddle2RotateAxis.LeftFootMiddle2RotateAxisx
    LeftFootMiddle2RotateAxisy = LeftFootMiddle2RotateAxis.LeftFootMiddle2RotateAxisy
    LeftFootMiddle2RotateAxisz = LeftFootMiddle2RotateAxis.LeftFootMiddle2RotateAxisz

    LeftFootMiddle2JointOrient = LeftFootMiddle2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle2JointOrientx = LeftFootMiddle2JointOrient.LeftFootMiddle2JointOrientx
    LeftFootMiddle2JointOrienty = LeftFootMiddle2JointOrient.LeftFootMiddle2JointOrienty
    LeftFootMiddle2JointOrientz = LeftFootMiddle2JointOrient.LeftFootMiddle2JointOrientz

    LeftFootMiddle2MinRLimit = LeftFootMiddle2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle2MinRLimitx = LeftFootMiddle2MinRLimit.LeftFootMiddle2MinRLimitx
    LeftFootMiddle2MinRLimity = LeftFootMiddle2MinRLimit.LeftFootMiddle2MinRLimity
    LeftFootMiddle2MinRLimitz = LeftFootMiddle2MinRLimit.LeftFootMiddle2MinRLimitz

    LeftFootMiddle2MaxRLimit = LeftFootMiddle2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle2MaxRLimitx = LeftFootMiddle2MaxRLimit.LeftFootMiddle2MaxRLimitx
    LeftFootMiddle2MaxRLimity = LeftFootMiddle2MaxRLimit.LeftFootMiddle2MaxRLimity
    LeftFootMiddle2MaxRLimitz = LeftFootMiddle2MaxRLimit.LeftFootMiddle2MaxRLimitz

    LeftFootMiddle2MinRLimitEnablex = BoolField(default_value=False)

    LeftFootMiddle2MinRLimitEnabley = BoolField(default_value=False)

    LeftFootMiddle2MinRLimitEnablez = BoolField(default_value=False)

    LeftFootMiddle2MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootMiddle2MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootMiddle2MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootMiddle3 = MessageField()

    LeftFootMiddle3T = LeftFootMiddle3TField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle3Tx = LeftFootMiddle3T.LeftFootMiddle3Tx
    LeftFootMiddle3Ty = LeftFootMiddle3T.LeftFootMiddle3Ty
    LeftFootMiddle3Tz = LeftFootMiddle3T.LeftFootMiddle3Tz

    LeftFootMiddle3R = LeftFootMiddle3RField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle3Rx = LeftFootMiddle3R.LeftFootMiddle3Rx
    LeftFootMiddle3Ry = LeftFootMiddle3R.LeftFootMiddle3Ry
    LeftFootMiddle3Rz = LeftFootMiddle3R.LeftFootMiddle3Rz

    LeftFootMiddle3S = LeftFootMiddle3SField(default_value=(1.0, 1.0, 1.0))
    LeftFootMiddle3Sx = LeftFootMiddle3S.LeftFootMiddle3Sx
    LeftFootMiddle3Sy = LeftFootMiddle3S.LeftFootMiddle3Sy
    LeftFootMiddle3Sz = LeftFootMiddle3S.LeftFootMiddle3Sz

    LeftFootMiddle3RotateOrder = LeftFootMiddle3RotateOrderEnumField(default_value=0)

    LeftFootMiddle3RotateAxis = LeftFootMiddle3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle3RotateAxisx = LeftFootMiddle3RotateAxis.LeftFootMiddle3RotateAxisx
    LeftFootMiddle3RotateAxisy = LeftFootMiddle3RotateAxis.LeftFootMiddle3RotateAxisy
    LeftFootMiddle3RotateAxisz = LeftFootMiddle3RotateAxis.LeftFootMiddle3RotateAxisz

    LeftFootMiddle3JointOrient = LeftFootMiddle3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle3JointOrientx = LeftFootMiddle3JointOrient.LeftFootMiddle3JointOrientx
    LeftFootMiddle3JointOrienty = LeftFootMiddle3JointOrient.LeftFootMiddle3JointOrienty
    LeftFootMiddle3JointOrientz = LeftFootMiddle3JointOrient.LeftFootMiddle3JointOrientz

    LeftFootMiddle3MinRLimit = LeftFootMiddle3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle3MinRLimitx = LeftFootMiddle3MinRLimit.LeftFootMiddle3MinRLimitx
    LeftFootMiddle3MinRLimity = LeftFootMiddle3MinRLimit.LeftFootMiddle3MinRLimity
    LeftFootMiddle3MinRLimitz = LeftFootMiddle3MinRLimit.LeftFootMiddle3MinRLimitz

    LeftFootMiddle3MaxRLimit = LeftFootMiddle3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle3MaxRLimitx = LeftFootMiddle3MaxRLimit.LeftFootMiddle3MaxRLimitx
    LeftFootMiddle3MaxRLimity = LeftFootMiddle3MaxRLimit.LeftFootMiddle3MaxRLimity
    LeftFootMiddle3MaxRLimitz = LeftFootMiddle3MaxRLimit.LeftFootMiddle3MaxRLimitz

    LeftFootMiddle3MinRLimitEnablex = BoolField(default_value=False)

    LeftFootMiddle3MinRLimitEnabley = BoolField(default_value=False)

    LeftFootMiddle3MinRLimitEnablez = BoolField(default_value=False)

    LeftFootMiddle3MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootMiddle3MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootMiddle3MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootMiddle4 = MessageField()

    LeftFootMiddle4T = LeftFootMiddle4TField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle4Tx = LeftFootMiddle4T.LeftFootMiddle4Tx
    LeftFootMiddle4Ty = LeftFootMiddle4T.LeftFootMiddle4Ty
    LeftFootMiddle4Tz = LeftFootMiddle4T.LeftFootMiddle4Tz

    LeftFootMiddle4R = LeftFootMiddle4RField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle4Rx = LeftFootMiddle4R.LeftFootMiddle4Rx
    LeftFootMiddle4Ry = LeftFootMiddle4R.LeftFootMiddle4Ry
    LeftFootMiddle4Rz = LeftFootMiddle4R.LeftFootMiddle4Rz

    LeftFootMiddle4S = LeftFootMiddle4SField(default_value=(1.0, 1.0, 1.0))
    LeftFootMiddle4Sx = LeftFootMiddle4S.LeftFootMiddle4Sx
    LeftFootMiddle4Sy = LeftFootMiddle4S.LeftFootMiddle4Sy
    LeftFootMiddle4Sz = LeftFootMiddle4S.LeftFootMiddle4Sz

    LeftFootMiddle4RotateOrder = LeftFootMiddle4RotateOrderEnumField(default_value=0)

    LeftFootMiddle4RotateAxis = LeftFootMiddle4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle4RotateAxisx = LeftFootMiddle4RotateAxis.LeftFootMiddle4RotateAxisx
    LeftFootMiddle4RotateAxisy = LeftFootMiddle4RotateAxis.LeftFootMiddle4RotateAxisy
    LeftFootMiddle4RotateAxisz = LeftFootMiddle4RotateAxis.LeftFootMiddle4RotateAxisz

    LeftFootMiddle4JointOrient = LeftFootMiddle4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle4JointOrientx = LeftFootMiddle4JointOrient.LeftFootMiddle4JointOrientx
    LeftFootMiddle4JointOrienty = LeftFootMiddle4JointOrient.LeftFootMiddle4JointOrienty
    LeftFootMiddle4JointOrientz = LeftFootMiddle4JointOrient.LeftFootMiddle4JointOrientz

    LeftFootMiddle4MinRLimit = LeftFootMiddle4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle4MinRLimitx = LeftFootMiddle4MinRLimit.LeftFootMiddle4MinRLimitx
    LeftFootMiddle4MinRLimity = LeftFootMiddle4MinRLimit.LeftFootMiddle4MinRLimity
    LeftFootMiddle4MinRLimitz = LeftFootMiddle4MinRLimit.LeftFootMiddle4MinRLimitz

    LeftFootMiddle4MaxRLimit = LeftFootMiddle4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle4MaxRLimitx = LeftFootMiddle4MaxRLimit.LeftFootMiddle4MaxRLimitx
    LeftFootMiddle4MaxRLimity = LeftFootMiddle4MaxRLimit.LeftFootMiddle4MaxRLimity
    LeftFootMiddle4MaxRLimitz = LeftFootMiddle4MaxRLimit.LeftFootMiddle4MaxRLimitz

    LeftFootMiddle4MinRLimitEnablex = BoolField(default_value=False)

    LeftFootMiddle4MinRLimitEnabley = BoolField(default_value=False)

    LeftFootMiddle4MinRLimitEnablez = BoolField(default_value=False)

    LeftFootMiddle4MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootMiddle4MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootMiddle4MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootRing1 = MessageField()

    LeftFootRing1T = LeftFootRing1TField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing1Tx = LeftFootRing1T.LeftFootRing1Tx
    LeftFootRing1Ty = LeftFootRing1T.LeftFootRing1Ty
    LeftFootRing1Tz = LeftFootRing1T.LeftFootRing1Tz

    LeftFootRing1R = LeftFootRing1RField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing1Rx = LeftFootRing1R.LeftFootRing1Rx
    LeftFootRing1Ry = LeftFootRing1R.LeftFootRing1Ry
    LeftFootRing1Rz = LeftFootRing1R.LeftFootRing1Rz

    LeftFootRing1S = LeftFootRing1SField(default_value=(1.0, 1.0, 1.0))
    LeftFootRing1Sx = LeftFootRing1S.LeftFootRing1Sx
    LeftFootRing1Sy = LeftFootRing1S.LeftFootRing1Sy
    LeftFootRing1Sz = LeftFootRing1S.LeftFootRing1Sz

    LeftFootRing1RotateOrder = LeftFootRing1RotateOrderEnumField(default_value=0)

    LeftFootRing1RotateAxis = LeftFootRing1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing1RotateAxisx = LeftFootRing1RotateAxis.LeftFootRing1RotateAxisx
    LeftFootRing1RotateAxisy = LeftFootRing1RotateAxis.LeftFootRing1RotateAxisy
    LeftFootRing1RotateAxisz = LeftFootRing1RotateAxis.LeftFootRing1RotateAxisz

    LeftFootRing1JointOrient = LeftFootRing1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing1JointOrientx = LeftFootRing1JointOrient.LeftFootRing1JointOrientx
    LeftFootRing1JointOrienty = LeftFootRing1JointOrient.LeftFootRing1JointOrienty
    LeftFootRing1JointOrientz = LeftFootRing1JointOrient.LeftFootRing1JointOrientz

    LeftFootRing1MinRLimit = LeftFootRing1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing1MinRLimitx = LeftFootRing1MinRLimit.LeftFootRing1MinRLimitx
    LeftFootRing1MinRLimity = LeftFootRing1MinRLimit.LeftFootRing1MinRLimity
    LeftFootRing1MinRLimitz = LeftFootRing1MinRLimit.LeftFootRing1MinRLimitz

    LeftFootRing1MaxRLimit = LeftFootRing1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing1MaxRLimitx = LeftFootRing1MaxRLimit.LeftFootRing1MaxRLimitx
    LeftFootRing1MaxRLimity = LeftFootRing1MaxRLimit.LeftFootRing1MaxRLimity
    LeftFootRing1MaxRLimitz = LeftFootRing1MaxRLimit.LeftFootRing1MaxRLimitz

    LeftFootRing1MinRLimitEnablex = BoolField(default_value=False)

    LeftFootRing1MinRLimitEnabley = BoolField(default_value=False)

    LeftFootRing1MinRLimitEnablez = BoolField(default_value=False)

    LeftFootRing1MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootRing1MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootRing1MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootRing2 = MessageField()

    LeftFootRing2T = LeftFootRing2TField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing2Tx = LeftFootRing2T.LeftFootRing2Tx
    LeftFootRing2Ty = LeftFootRing2T.LeftFootRing2Ty
    LeftFootRing2Tz = LeftFootRing2T.LeftFootRing2Tz

    LeftFootRing2R = LeftFootRing2RField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing2Rx = LeftFootRing2R.LeftFootRing2Rx
    LeftFootRing2Ry = LeftFootRing2R.LeftFootRing2Ry
    LeftFootRing2Rz = LeftFootRing2R.LeftFootRing2Rz

    LeftFootRing2S = LeftFootRing2SField(default_value=(1.0, 1.0, 1.0))
    LeftFootRing2Sx = LeftFootRing2S.LeftFootRing2Sx
    LeftFootRing2Sy = LeftFootRing2S.LeftFootRing2Sy
    LeftFootRing2Sz = LeftFootRing2S.LeftFootRing2Sz

    LeftFootRing2RotateOrder = LeftFootRing2RotateOrderEnumField(default_value=0)

    LeftFootRing2RotateAxis = LeftFootRing2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing2RotateAxisx = LeftFootRing2RotateAxis.LeftFootRing2RotateAxisx
    LeftFootRing2RotateAxisy = LeftFootRing2RotateAxis.LeftFootRing2RotateAxisy
    LeftFootRing2RotateAxisz = LeftFootRing2RotateAxis.LeftFootRing2RotateAxisz

    LeftFootRing2JointOrient = LeftFootRing2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing2JointOrientx = LeftFootRing2JointOrient.LeftFootRing2JointOrientx
    LeftFootRing2JointOrienty = LeftFootRing2JointOrient.LeftFootRing2JointOrienty
    LeftFootRing2JointOrientz = LeftFootRing2JointOrient.LeftFootRing2JointOrientz

    LeftFootRing2MinRLimit = LeftFootRing2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing2MinRLimitx = LeftFootRing2MinRLimit.LeftFootRing2MinRLimitx
    LeftFootRing2MinRLimity = LeftFootRing2MinRLimit.LeftFootRing2MinRLimity
    LeftFootRing2MinRLimitz = LeftFootRing2MinRLimit.LeftFootRing2MinRLimitz

    LeftFootRing2MaxRLimit = LeftFootRing2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing2MaxRLimitx = LeftFootRing2MaxRLimit.LeftFootRing2MaxRLimitx
    LeftFootRing2MaxRLimity = LeftFootRing2MaxRLimit.LeftFootRing2MaxRLimity
    LeftFootRing2MaxRLimitz = LeftFootRing2MaxRLimit.LeftFootRing2MaxRLimitz

    LeftFootRing2MinRLimitEnablex = BoolField(default_value=False)

    LeftFootRing2MinRLimitEnabley = BoolField(default_value=False)

    LeftFootRing2MinRLimitEnablez = BoolField(default_value=False)

    LeftFootRing2MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootRing2MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootRing2MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootRing3 = MessageField()

    LeftFootRing3T = LeftFootRing3TField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing3Tx = LeftFootRing3T.LeftFootRing3Tx
    LeftFootRing3Ty = LeftFootRing3T.LeftFootRing3Ty
    LeftFootRing3Tz = LeftFootRing3T.LeftFootRing3Tz

    LeftFootRing3R = LeftFootRing3RField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing3Rx = LeftFootRing3R.LeftFootRing3Rx
    LeftFootRing3Ry = LeftFootRing3R.LeftFootRing3Ry
    LeftFootRing3Rz = LeftFootRing3R.LeftFootRing3Rz

    LeftFootRing3S = LeftFootRing3SField(default_value=(1.0, 1.0, 1.0))
    LeftFootRing3Sx = LeftFootRing3S.LeftFootRing3Sx
    LeftFootRing3Sy = LeftFootRing3S.LeftFootRing3Sy
    LeftFootRing3Sz = LeftFootRing3S.LeftFootRing3Sz

    LeftFootRing3RotateOrder = LeftFootRing3RotateOrderEnumField(default_value=0)

    LeftFootRing3RotateAxis = LeftFootRing3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing3RotateAxisx = LeftFootRing3RotateAxis.LeftFootRing3RotateAxisx
    LeftFootRing3RotateAxisy = LeftFootRing3RotateAxis.LeftFootRing3RotateAxisy
    LeftFootRing3RotateAxisz = LeftFootRing3RotateAxis.LeftFootRing3RotateAxisz

    LeftFootRing3JointOrient = LeftFootRing3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing3JointOrientx = LeftFootRing3JointOrient.LeftFootRing3JointOrientx
    LeftFootRing3JointOrienty = LeftFootRing3JointOrient.LeftFootRing3JointOrienty
    LeftFootRing3JointOrientz = LeftFootRing3JointOrient.LeftFootRing3JointOrientz

    LeftFootRing3MinRLimit = LeftFootRing3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing3MinRLimitx = LeftFootRing3MinRLimit.LeftFootRing3MinRLimitx
    LeftFootRing3MinRLimity = LeftFootRing3MinRLimit.LeftFootRing3MinRLimity
    LeftFootRing3MinRLimitz = LeftFootRing3MinRLimit.LeftFootRing3MinRLimitz

    LeftFootRing3MaxRLimit = LeftFootRing3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing3MaxRLimitx = LeftFootRing3MaxRLimit.LeftFootRing3MaxRLimitx
    LeftFootRing3MaxRLimity = LeftFootRing3MaxRLimit.LeftFootRing3MaxRLimity
    LeftFootRing3MaxRLimitz = LeftFootRing3MaxRLimit.LeftFootRing3MaxRLimitz

    LeftFootRing3MinRLimitEnablex = BoolField(default_value=False)

    LeftFootRing3MinRLimitEnabley = BoolField(default_value=False)

    LeftFootRing3MinRLimitEnablez = BoolField(default_value=False)

    LeftFootRing3MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootRing3MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootRing3MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootRing4 = MessageField()

    LeftFootRing4T = LeftFootRing4TField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing4Tx = LeftFootRing4T.LeftFootRing4Tx
    LeftFootRing4Ty = LeftFootRing4T.LeftFootRing4Ty
    LeftFootRing4Tz = LeftFootRing4T.LeftFootRing4Tz

    LeftFootRing4R = LeftFootRing4RField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing4Rx = LeftFootRing4R.LeftFootRing4Rx
    LeftFootRing4Ry = LeftFootRing4R.LeftFootRing4Ry
    LeftFootRing4Rz = LeftFootRing4R.LeftFootRing4Rz

    LeftFootRing4S = LeftFootRing4SField(default_value=(1.0, 1.0, 1.0))
    LeftFootRing4Sx = LeftFootRing4S.LeftFootRing4Sx
    LeftFootRing4Sy = LeftFootRing4S.LeftFootRing4Sy
    LeftFootRing4Sz = LeftFootRing4S.LeftFootRing4Sz

    LeftFootRing4RotateOrder = LeftFootRing4RotateOrderEnumField(default_value=0)

    LeftFootRing4RotateAxis = LeftFootRing4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing4RotateAxisx = LeftFootRing4RotateAxis.LeftFootRing4RotateAxisx
    LeftFootRing4RotateAxisy = LeftFootRing4RotateAxis.LeftFootRing4RotateAxisy
    LeftFootRing4RotateAxisz = LeftFootRing4RotateAxis.LeftFootRing4RotateAxisz

    LeftFootRing4JointOrient = LeftFootRing4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing4JointOrientx = LeftFootRing4JointOrient.LeftFootRing4JointOrientx
    LeftFootRing4JointOrienty = LeftFootRing4JointOrient.LeftFootRing4JointOrienty
    LeftFootRing4JointOrientz = LeftFootRing4JointOrient.LeftFootRing4JointOrientz

    LeftFootRing4MinRLimit = LeftFootRing4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing4MinRLimitx = LeftFootRing4MinRLimit.LeftFootRing4MinRLimitx
    LeftFootRing4MinRLimity = LeftFootRing4MinRLimit.LeftFootRing4MinRLimity
    LeftFootRing4MinRLimitz = LeftFootRing4MinRLimit.LeftFootRing4MinRLimitz

    LeftFootRing4MaxRLimit = LeftFootRing4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing4MaxRLimitx = LeftFootRing4MaxRLimit.LeftFootRing4MaxRLimitx
    LeftFootRing4MaxRLimity = LeftFootRing4MaxRLimit.LeftFootRing4MaxRLimity
    LeftFootRing4MaxRLimitz = LeftFootRing4MaxRLimit.LeftFootRing4MaxRLimitz

    LeftFootRing4MinRLimitEnablex = BoolField(default_value=False)

    LeftFootRing4MinRLimitEnabley = BoolField(default_value=False)

    LeftFootRing4MinRLimitEnablez = BoolField(default_value=False)

    LeftFootRing4MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootRing4MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootRing4MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootPinky1 = MessageField()

    LeftFootPinky1T = LeftFootPinky1TField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky1Tx = LeftFootPinky1T.LeftFootPinky1Tx
    LeftFootPinky1Ty = LeftFootPinky1T.LeftFootPinky1Ty
    LeftFootPinky1Tz = LeftFootPinky1T.LeftFootPinky1Tz

    LeftFootPinky1R = LeftFootPinky1RField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky1Rx = LeftFootPinky1R.LeftFootPinky1Rx
    LeftFootPinky1Ry = LeftFootPinky1R.LeftFootPinky1Ry
    LeftFootPinky1Rz = LeftFootPinky1R.LeftFootPinky1Rz

    LeftFootPinky1S = LeftFootPinky1SField(default_value=(1.0, 1.0, 1.0))
    LeftFootPinky1Sx = LeftFootPinky1S.LeftFootPinky1Sx
    LeftFootPinky1Sy = LeftFootPinky1S.LeftFootPinky1Sy
    LeftFootPinky1Sz = LeftFootPinky1S.LeftFootPinky1Sz

    LeftFootPinky1RotateOrder = LeftFootPinky1RotateOrderEnumField(default_value=0)

    LeftFootPinky1RotateAxis = LeftFootPinky1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky1RotateAxisx = LeftFootPinky1RotateAxis.LeftFootPinky1RotateAxisx
    LeftFootPinky1RotateAxisy = LeftFootPinky1RotateAxis.LeftFootPinky1RotateAxisy
    LeftFootPinky1RotateAxisz = LeftFootPinky1RotateAxis.LeftFootPinky1RotateAxisz

    LeftFootPinky1JointOrient = LeftFootPinky1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky1JointOrientx = LeftFootPinky1JointOrient.LeftFootPinky1JointOrientx
    LeftFootPinky1JointOrienty = LeftFootPinky1JointOrient.LeftFootPinky1JointOrienty
    LeftFootPinky1JointOrientz = LeftFootPinky1JointOrient.LeftFootPinky1JointOrientz

    LeftFootPinky1MinRLimit = LeftFootPinky1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky1MinRLimitx = LeftFootPinky1MinRLimit.LeftFootPinky1MinRLimitx
    LeftFootPinky1MinRLimity = LeftFootPinky1MinRLimit.LeftFootPinky1MinRLimity
    LeftFootPinky1MinRLimitz = LeftFootPinky1MinRLimit.LeftFootPinky1MinRLimitz

    LeftFootPinky1MaxRLimit = LeftFootPinky1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky1MaxRLimitx = LeftFootPinky1MaxRLimit.LeftFootPinky1MaxRLimitx
    LeftFootPinky1MaxRLimity = LeftFootPinky1MaxRLimit.LeftFootPinky1MaxRLimity
    LeftFootPinky1MaxRLimitz = LeftFootPinky1MaxRLimit.LeftFootPinky1MaxRLimitz

    LeftFootPinky1MinRLimitEnablex = BoolField(default_value=False)

    LeftFootPinky1MinRLimitEnabley = BoolField(default_value=False)

    LeftFootPinky1MinRLimitEnablez = BoolField(default_value=False)

    LeftFootPinky1MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootPinky1MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootPinky1MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootPinky2 = MessageField()

    LeftFootPinky2T = LeftFootPinky2TField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky2Tx = LeftFootPinky2T.LeftFootPinky2Tx
    LeftFootPinky2Ty = LeftFootPinky2T.LeftFootPinky2Ty
    LeftFootPinky2Tz = LeftFootPinky2T.LeftFootPinky2Tz

    LeftFootPinky2R = LeftFootPinky2RField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky2Rx = LeftFootPinky2R.LeftFootPinky2Rx
    LeftFootPinky2Ry = LeftFootPinky2R.LeftFootPinky2Ry
    LeftFootPinky2Rz = LeftFootPinky2R.LeftFootPinky2Rz

    LeftFootPinky2S = LeftFootPinky2SField(default_value=(1.0, 1.0, 1.0))
    LeftFootPinky2Sx = LeftFootPinky2S.LeftFootPinky2Sx
    LeftFootPinky2Sy = LeftFootPinky2S.LeftFootPinky2Sy
    LeftFootPinky2Sz = LeftFootPinky2S.LeftFootPinky2Sz

    LeftFootPinky2RotateOrder = LeftFootPinky2RotateOrderEnumField(default_value=0)

    LeftFootPinky2RotateAxis = LeftFootPinky2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky2RotateAxisx = LeftFootPinky2RotateAxis.LeftFootPinky2RotateAxisx
    LeftFootPinky2RotateAxisy = LeftFootPinky2RotateAxis.LeftFootPinky2RotateAxisy
    LeftFootPinky2RotateAxisz = LeftFootPinky2RotateAxis.LeftFootPinky2RotateAxisz

    LeftFootPinky2JointOrient = LeftFootPinky2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky2JointOrientx = LeftFootPinky2JointOrient.LeftFootPinky2JointOrientx
    LeftFootPinky2JointOrienty = LeftFootPinky2JointOrient.LeftFootPinky2JointOrienty
    LeftFootPinky2JointOrientz = LeftFootPinky2JointOrient.LeftFootPinky2JointOrientz

    LeftFootPinky2MinRLimit = LeftFootPinky2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky2MinRLimitx = LeftFootPinky2MinRLimit.LeftFootPinky2MinRLimitx
    LeftFootPinky2MinRLimity = LeftFootPinky2MinRLimit.LeftFootPinky2MinRLimity
    LeftFootPinky2MinRLimitz = LeftFootPinky2MinRLimit.LeftFootPinky2MinRLimitz

    LeftFootPinky2MaxRLimit = LeftFootPinky2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky2MaxRLimitx = LeftFootPinky2MaxRLimit.LeftFootPinky2MaxRLimitx
    LeftFootPinky2MaxRLimity = LeftFootPinky2MaxRLimit.LeftFootPinky2MaxRLimity
    LeftFootPinky2MaxRLimitz = LeftFootPinky2MaxRLimit.LeftFootPinky2MaxRLimitz

    LeftFootPinky2MinRLimitEnablex = BoolField(default_value=False)

    LeftFootPinky2MinRLimitEnabley = BoolField(default_value=False)

    LeftFootPinky2MinRLimitEnablez = BoolField(default_value=False)

    LeftFootPinky2MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootPinky2MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootPinky2MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootPinky3 = MessageField()

    LeftFootPinky3T = LeftFootPinky3TField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky3Tx = LeftFootPinky3T.LeftFootPinky3Tx
    LeftFootPinky3Ty = LeftFootPinky3T.LeftFootPinky3Ty
    LeftFootPinky3Tz = LeftFootPinky3T.LeftFootPinky3Tz

    LeftFootPinky3R = LeftFootPinky3RField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky3Rx = LeftFootPinky3R.LeftFootPinky3Rx
    LeftFootPinky3Ry = LeftFootPinky3R.LeftFootPinky3Ry
    LeftFootPinky3Rz = LeftFootPinky3R.LeftFootPinky3Rz

    LeftFootPinky3S = LeftFootPinky3SField(default_value=(1.0, 1.0, 1.0))
    LeftFootPinky3Sx = LeftFootPinky3S.LeftFootPinky3Sx
    LeftFootPinky3Sy = LeftFootPinky3S.LeftFootPinky3Sy
    LeftFootPinky3Sz = LeftFootPinky3S.LeftFootPinky3Sz

    LeftFootPinky3RotateOrder = LeftFootPinky3RotateOrderEnumField(default_value=0)

    LeftFootPinky3RotateAxis = LeftFootPinky3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky3RotateAxisx = LeftFootPinky3RotateAxis.LeftFootPinky3RotateAxisx
    LeftFootPinky3RotateAxisy = LeftFootPinky3RotateAxis.LeftFootPinky3RotateAxisy
    LeftFootPinky3RotateAxisz = LeftFootPinky3RotateAxis.LeftFootPinky3RotateAxisz

    LeftFootPinky3JointOrient = LeftFootPinky3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky3JointOrientx = LeftFootPinky3JointOrient.LeftFootPinky3JointOrientx
    LeftFootPinky3JointOrienty = LeftFootPinky3JointOrient.LeftFootPinky3JointOrienty
    LeftFootPinky3JointOrientz = LeftFootPinky3JointOrient.LeftFootPinky3JointOrientz

    LeftFootPinky3MinRLimit = LeftFootPinky3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky3MinRLimitx = LeftFootPinky3MinRLimit.LeftFootPinky3MinRLimitx
    LeftFootPinky3MinRLimity = LeftFootPinky3MinRLimit.LeftFootPinky3MinRLimity
    LeftFootPinky3MinRLimitz = LeftFootPinky3MinRLimit.LeftFootPinky3MinRLimitz

    LeftFootPinky3MaxRLimit = LeftFootPinky3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky3MaxRLimitx = LeftFootPinky3MaxRLimit.LeftFootPinky3MaxRLimitx
    LeftFootPinky3MaxRLimity = LeftFootPinky3MaxRLimit.LeftFootPinky3MaxRLimity
    LeftFootPinky3MaxRLimitz = LeftFootPinky3MaxRLimit.LeftFootPinky3MaxRLimitz

    LeftFootPinky3MinRLimitEnablex = BoolField(default_value=False)

    LeftFootPinky3MinRLimitEnabley = BoolField(default_value=False)

    LeftFootPinky3MinRLimitEnablez = BoolField(default_value=False)

    LeftFootPinky3MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootPinky3MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootPinky3MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootPinky4 = MessageField()

    LeftFootPinky4T = LeftFootPinky4TField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky4Tx = LeftFootPinky4T.LeftFootPinky4Tx
    LeftFootPinky4Ty = LeftFootPinky4T.LeftFootPinky4Ty
    LeftFootPinky4Tz = LeftFootPinky4T.LeftFootPinky4Tz

    LeftFootPinky4R = LeftFootPinky4RField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky4Rx = LeftFootPinky4R.LeftFootPinky4Rx
    LeftFootPinky4Ry = LeftFootPinky4R.LeftFootPinky4Ry
    LeftFootPinky4Rz = LeftFootPinky4R.LeftFootPinky4Rz

    LeftFootPinky4S = LeftFootPinky4SField(default_value=(1.0, 1.0, 1.0))
    LeftFootPinky4Sx = LeftFootPinky4S.LeftFootPinky4Sx
    LeftFootPinky4Sy = LeftFootPinky4S.LeftFootPinky4Sy
    LeftFootPinky4Sz = LeftFootPinky4S.LeftFootPinky4Sz

    LeftFootPinky4RotateOrder = LeftFootPinky4RotateOrderEnumField(default_value=0)

    LeftFootPinky4RotateAxis = LeftFootPinky4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky4RotateAxisx = LeftFootPinky4RotateAxis.LeftFootPinky4RotateAxisx
    LeftFootPinky4RotateAxisy = LeftFootPinky4RotateAxis.LeftFootPinky4RotateAxisy
    LeftFootPinky4RotateAxisz = LeftFootPinky4RotateAxis.LeftFootPinky4RotateAxisz

    LeftFootPinky4JointOrient = LeftFootPinky4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky4JointOrientx = LeftFootPinky4JointOrient.LeftFootPinky4JointOrientx
    LeftFootPinky4JointOrienty = LeftFootPinky4JointOrient.LeftFootPinky4JointOrienty
    LeftFootPinky4JointOrientz = LeftFootPinky4JointOrient.LeftFootPinky4JointOrientz

    LeftFootPinky4MinRLimit = LeftFootPinky4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky4MinRLimitx = LeftFootPinky4MinRLimit.LeftFootPinky4MinRLimitx
    LeftFootPinky4MinRLimity = LeftFootPinky4MinRLimit.LeftFootPinky4MinRLimity
    LeftFootPinky4MinRLimitz = LeftFootPinky4MinRLimit.LeftFootPinky4MinRLimitz

    LeftFootPinky4MaxRLimit = LeftFootPinky4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky4MaxRLimitx = LeftFootPinky4MaxRLimit.LeftFootPinky4MaxRLimitx
    LeftFootPinky4MaxRLimity = LeftFootPinky4MaxRLimit.LeftFootPinky4MaxRLimity
    LeftFootPinky4MaxRLimitz = LeftFootPinky4MaxRLimit.LeftFootPinky4MaxRLimitz

    LeftFootPinky4MinRLimitEnablex = BoolField(default_value=False)

    LeftFootPinky4MinRLimitEnabley = BoolField(default_value=False)

    LeftFootPinky4MinRLimitEnablez = BoolField(default_value=False)

    LeftFootPinky4MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootPinky4MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootPinky4MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootExtraFinger1 = MessageField()

    LeftFootExtraFinger1T = LeftFootExtraFinger1TField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger1Tx = LeftFootExtraFinger1T.LeftFootExtraFinger1Tx
    LeftFootExtraFinger1Ty = LeftFootExtraFinger1T.LeftFootExtraFinger1Ty
    LeftFootExtraFinger1Tz = LeftFootExtraFinger1T.LeftFootExtraFinger1Tz

    LeftFootExtraFinger1R = LeftFootExtraFinger1RField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger1Rx = LeftFootExtraFinger1R.LeftFootExtraFinger1Rx
    LeftFootExtraFinger1Ry = LeftFootExtraFinger1R.LeftFootExtraFinger1Ry
    LeftFootExtraFinger1Rz = LeftFootExtraFinger1R.LeftFootExtraFinger1Rz

    LeftFootExtraFinger1S = LeftFootExtraFinger1SField(default_value=(1.0, 1.0, 1.0))
    LeftFootExtraFinger1Sx = LeftFootExtraFinger1S.LeftFootExtraFinger1Sx
    LeftFootExtraFinger1Sy = LeftFootExtraFinger1S.LeftFootExtraFinger1Sy
    LeftFootExtraFinger1Sz = LeftFootExtraFinger1S.LeftFootExtraFinger1Sz

    LeftFootExtraFinger1RotateOrder = LeftFootExtraFinger1RotateOrderEnumField(default_value=0)

    LeftFootExtraFinger1RotateAxis = LeftFootExtraFinger1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger1RotateAxisx = LeftFootExtraFinger1RotateAxis.LeftFootExtraFinger1RotateAxisx
    LeftFootExtraFinger1RotateAxisy = LeftFootExtraFinger1RotateAxis.LeftFootExtraFinger1RotateAxisy
    LeftFootExtraFinger1RotateAxisz = LeftFootExtraFinger1RotateAxis.LeftFootExtraFinger1RotateAxisz

    LeftFootExtraFinger1JointOrient = LeftFootExtraFinger1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger1JointOrientx = LeftFootExtraFinger1JointOrient.LeftFootExtraFinger1JointOrientx
    LeftFootExtraFinger1JointOrienty = LeftFootExtraFinger1JointOrient.LeftFootExtraFinger1JointOrienty
    LeftFootExtraFinger1JointOrientz = LeftFootExtraFinger1JointOrient.LeftFootExtraFinger1JointOrientz

    LeftFootExtraFinger1MinRLimit = LeftFootExtraFinger1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger1MinRLimitx = LeftFootExtraFinger1MinRLimit.LeftFootExtraFinger1MinRLimitx
    LeftFootExtraFinger1MinRLimity = LeftFootExtraFinger1MinRLimit.LeftFootExtraFinger1MinRLimity
    LeftFootExtraFinger1MinRLimitz = LeftFootExtraFinger1MinRLimit.LeftFootExtraFinger1MinRLimitz

    LeftFootExtraFinger1MaxRLimit = LeftFootExtraFinger1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger1MaxRLimitx = LeftFootExtraFinger1MaxRLimit.LeftFootExtraFinger1MaxRLimitx
    LeftFootExtraFinger1MaxRLimity = LeftFootExtraFinger1MaxRLimit.LeftFootExtraFinger1MaxRLimity
    LeftFootExtraFinger1MaxRLimitz = LeftFootExtraFinger1MaxRLimit.LeftFootExtraFinger1MaxRLimitz

    LeftFootExtraFinger1MinRLimitEnablex = BoolField(default_value=False)

    LeftFootExtraFinger1MinRLimitEnabley = BoolField(default_value=False)

    LeftFootExtraFinger1MinRLimitEnablez = BoolField(default_value=False)

    LeftFootExtraFinger1MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootExtraFinger1MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootExtraFinger1MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootExtraFinger2 = MessageField()

    LeftFootExtraFinger2T = LeftFootExtraFinger2TField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger2Tx = LeftFootExtraFinger2T.LeftFootExtraFinger2Tx
    LeftFootExtraFinger2Ty = LeftFootExtraFinger2T.LeftFootExtraFinger2Ty
    LeftFootExtraFinger2Tz = LeftFootExtraFinger2T.LeftFootExtraFinger2Tz

    LeftFootExtraFinger2R = LeftFootExtraFinger2RField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger2Rx = LeftFootExtraFinger2R.LeftFootExtraFinger2Rx
    LeftFootExtraFinger2Ry = LeftFootExtraFinger2R.LeftFootExtraFinger2Ry
    LeftFootExtraFinger2Rz = LeftFootExtraFinger2R.LeftFootExtraFinger2Rz

    LeftFootExtraFinger2S = LeftFootExtraFinger2SField(default_value=(1.0, 1.0, 1.0))
    LeftFootExtraFinger2Sx = LeftFootExtraFinger2S.LeftFootExtraFinger2Sx
    LeftFootExtraFinger2Sy = LeftFootExtraFinger2S.LeftFootExtraFinger2Sy
    LeftFootExtraFinger2Sz = LeftFootExtraFinger2S.LeftFootExtraFinger2Sz

    LeftFootExtraFinger2RotateOrder = LeftFootExtraFinger2RotateOrderEnumField(default_value=0)

    LeftFootExtraFinger2RotateAxis = LeftFootExtraFinger2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger2RotateAxisx = LeftFootExtraFinger2RotateAxis.LeftFootExtraFinger2RotateAxisx
    LeftFootExtraFinger2RotateAxisy = LeftFootExtraFinger2RotateAxis.LeftFootExtraFinger2RotateAxisy
    LeftFootExtraFinger2RotateAxisz = LeftFootExtraFinger2RotateAxis.LeftFootExtraFinger2RotateAxisz

    LeftFootExtraFinger2JointOrient = LeftFootExtraFinger2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger2JointOrientx = LeftFootExtraFinger2JointOrient.LeftFootExtraFinger2JointOrientx
    LeftFootExtraFinger2JointOrienty = LeftFootExtraFinger2JointOrient.LeftFootExtraFinger2JointOrienty
    LeftFootExtraFinger2JointOrientz = LeftFootExtraFinger2JointOrient.LeftFootExtraFinger2JointOrientz

    LeftFootExtraFinger2MinRLimit = LeftFootExtraFinger2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger2MinRLimitx = LeftFootExtraFinger2MinRLimit.LeftFootExtraFinger2MinRLimitx
    LeftFootExtraFinger2MinRLimity = LeftFootExtraFinger2MinRLimit.LeftFootExtraFinger2MinRLimity
    LeftFootExtraFinger2MinRLimitz = LeftFootExtraFinger2MinRLimit.LeftFootExtraFinger2MinRLimitz

    LeftFootExtraFinger2MaxRLimit = LeftFootExtraFinger2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger2MaxRLimitx = LeftFootExtraFinger2MaxRLimit.LeftFootExtraFinger2MaxRLimitx
    LeftFootExtraFinger2MaxRLimity = LeftFootExtraFinger2MaxRLimit.LeftFootExtraFinger2MaxRLimity
    LeftFootExtraFinger2MaxRLimitz = LeftFootExtraFinger2MaxRLimit.LeftFootExtraFinger2MaxRLimitz

    LeftFootExtraFinger2MinRLimitEnablex = BoolField(default_value=False)

    LeftFootExtraFinger2MinRLimitEnabley = BoolField(default_value=False)

    LeftFootExtraFinger2MinRLimitEnablez = BoolField(default_value=False)

    LeftFootExtraFinger2MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootExtraFinger2MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootExtraFinger2MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootExtraFinger3 = MessageField()

    LeftFootExtraFinger3T = LeftFootExtraFinger3TField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger3Tx = LeftFootExtraFinger3T.LeftFootExtraFinger3Tx
    LeftFootExtraFinger3Ty = LeftFootExtraFinger3T.LeftFootExtraFinger3Ty
    LeftFootExtraFinger3Tz = LeftFootExtraFinger3T.LeftFootExtraFinger3Tz

    LeftFootExtraFinger3R = LeftFootExtraFinger3RField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger3Rx = LeftFootExtraFinger3R.LeftFootExtraFinger3Rx
    LeftFootExtraFinger3Ry = LeftFootExtraFinger3R.LeftFootExtraFinger3Ry
    LeftFootExtraFinger3Rz = LeftFootExtraFinger3R.LeftFootExtraFinger3Rz

    LeftFootExtraFinger3S = LeftFootExtraFinger3SField(default_value=(1.0, 1.0, 1.0))
    LeftFootExtraFinger3Sx = LeftFootExtraFinger3S.LeftFootExtraFinger3Sx
    LeftFootExtraFinger3Sy = LeftFootExtraFinger3S.LeftFootExtraFinger3Sy
    LeftFootExtraFinger3Sz = LeftFootExtraFinger3S.LeftFootExtraFinger3Sz

    LeftFootExtraFinger3RotateOrder = LeftFootExtraFinger3RotateOrderEnumField(default_value=0)

    LeftFootExtraFinger3RotateAxis = LeftFootExtraFinger3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger3RotateAxisx = LeftFootExtraFinger3RotateAxis.LeftFootExtraFinger3RotateAxisx
    LeftFootExtraFinger3RotateAxisy = LeftFootExtraFinger3RotateAxis.LeftFootExtraFinger3RotateAxisy
    LeftFootExtraFinger3RotateAxisz = LeftFootExtraFinger3RotateAxis.LeftFootExtraFinger3RotateAxisz

    LeftFootExtraFinger3JointOrient = LeftFootExtraFinger3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger3JointOrientx = LeftFootExtraFinger3JointOrient.LeftFootExtraFinger3JointOrientx
    LeftFootExtraFinger3JointOrienty = LeftFootExtraFinger3JointOrient.LeftFootExtraFinger3JointOrienty
    LeftFootExtraFinger3JointOrientz = LeftFootExtraFinger3JointOrient.LeftFootExtraFinger3JointOrientz

    LeftFootExtraFinger3MinRLimit = LeftFootExtraFinger3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger3MinRLimitx = LeftFootExtraFinger3MinRLimit.LeftFootExtraFinger3MinRLimitx
    LeftFootExtraFinger3MinRLimity = LeftFootExtraFinger3MinRLimit.LeftFootExtraFinger3MinRLimity
    LeftFootExtraFinger3MinRLimitz = LeftFootExtraFinger3MinRLimit.LeftFootExtraFinger3MinRLimitz

    LeftFootExtraFinger3MaxRLimit = LeftFootExtraFinger3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger3MaxRLimitx = LeftFootExtraFinger3MaxRLimit.LeftFootExtraFinger3MaxRLimitx
    LeftFootExtraFinger3MaxRLimity = LeftFootExtraFinger3MaxRLimit.LeftFootExtraFinger3MaxRLimity
    LeftFootExtraFinger3MaxRLimitz = LeftFootExtraFinger3MaxRLimit.LeftFootExtraFinger3MaxRLimitz

    LeftFootExtraFinger3MinRLimitEnablex = BoolField(default_value=False)

    LeftFootExtraFinger3MinRLimitEnabley = BoolField(default_value=False)

    LeftFootExtraFinger3MinRLimitEnablez = BoolField(default_value=False)

    LeftFootExtraFinger3MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootExtraFinger3MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootExtraFinger3MaxRLimitEnablez = BoolField(default_value=False)

    LeftFootExtraFinger4 = MessageField()

    LeftFootExtraFinger4T = LeftFootExtraFinger4TField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger4Tx = LeftFootExtraFinger4T.LeftFootExtraFinger4Tx
    LeftFootExtraFinger4Ty = LeftFootExtraFinger4T.LeftFootExtraFinger4Ty
    LeftFootExtraFinger4Tz = LeftFootExtraFinger4T.LeftFootExtraFinger4Tz

    LeftFootExtraFinger4R = LeftFootExtraFinger4RField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger4Rx = LeftFootExtraFinger4R.LeftFootExtraFinger4Rx
    LeftFootExtraFinger4Ry = LeftFootExtraFinger4R.LeftFootExtraFinger4Ry
    LeftFootExtraFinger4Rz = LeftFootExtraFinger4R.LeftFootExtraFinger4Rz

    LeftFootExtraFinger4S = LeftFootExtraFinger4SField(default_value=(1.0, 1.0, 1.0))
    LeftFootExtraFinger4Sx = LeftFootExtraFinger4S.LeftFootExtraFinger4Sx
    LeftFootExtraFinger4Sy = LeftFootExtraFinger4S.LeftFootExtraFinger4Sy
    LeftFootExtraFinger4Sz = LeftFootExtraFinger4S.LeftFootExtraFinger4Sz

    LeftFootExtraFinger4RotateOrder = LeftFootExtraFinger4RotateOrderEnumField(default_value=0)

    LeftFootExtraFinger4RotateAxis = LeftFootExtraFinger4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger4RotateAxisx = LeftFootExtraFinger4RotateAxis.LeftFootExtraFinger4RotateAxisx
    LeftFootExtraFinger4RotateAxisy = LeftFootExtraFinger4RotateAxis.LeftFootExtraFinger4RotateAxisy
    LeftFootExtraFinger4RotateAxisz = LeftFootExtraFinger4RotateAxis.LeftFootExtraFinger4RotateAxisz

    LeftFootExtraFinger4JointOrient = LeftFootExtraFinger4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger4JointOrientx = LeftFootExtraFinger4JointOrient.LeftFootExtraFinger4JointOrientx
    LeftFootExtraFinger4JointOrienty = LeftFootExtraFinger4JointOrient.LeftFootExtraFinger4JointOrienty
    LeftFootExtraFinger4JointOrientz = LeftFootExtraFinger4JointOrient.LeftFootExtraFinger4JointOrientz

    LeftFootExtraFinger4MinRLimit = LeftFootExtraFinger4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger4MinRLimitx = LeftFootExtraFinger4MinRLimit.LeftFootExtraFinger4MinRLimitx
    LeftFootExtraFinger4MinRLimity = LeftFootExtraFinger4MinRLimit.LeftFootExtraFinger4MinRLimity
    LeftFootExtraFinger4MinRLimitz = LeftFootExtraFinger4MinRLimit.LeftFootExtraFinger4MinRLimitz

    LeftFootExtraFinger4MaxRLimit = LeftFootExtraFinger4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger4MaxRLimitx = LeftFootExtraFinger4MaxRLimit.LeftFootExtraFinger4MaxRLimitx
    LeftFootExtraFinger4MaxRLimity = LeftFootExtraFinger4MaxRLimit.LeftFootExtraFinger4MaxRLimity
    LeftFootExtraFinger4MaxRLimitz = LeftFootExtraFinger4MaxRLimit.LeftFootExtraFinger4MaxRLimitz

    LeftFootExtraFinger4MinRLimitEnablex = BoolField(default_value=False)

    LeftFootExtraFinger4MinRLimitEnabley = BoolField(default_value=False)

    LeftFootExtraFinger4MinRLimitEnablez = BoolField(default_value=False)

    LeftFootExtraFinger4MaxRLimitEnablex = BoolField(default_value=False)

    LeftFootExtraFinger4MaxRLimitEnabley = BoolField(default_value=False)

    LeftFootExtraFinger4MaxRLimitEnablez = BoolField(default_value=False)

    RightFootThumb1 = MessageField()

    RightFootThumb1T = RightFootThumb1TField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb1Tx = RightFootThumb1T.RightFootThumb1Tx
    RightFootThumb1Ty = RightFootThumb1T.RightFootThumb1Ty
    RightFootThumb1Tz = RightFootThumb1T.RightFootThumb1Tz

    RightFootThumb1R = RightFootThumb1RField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb1Rx = RightFootThumb1R.RightFootThumb1Rx
    RightFootThumb1Ry = RightFootThumb1R.RightFootThumb1Ry
    RightFootThumb1Rz = RightFootThumb1R.RightFootThumb1Rz

    RightFootThumb1S = RightFootThumb1SField(default_value=(1.0, 1.0, 1.0))
    RightFootThumb1Sx = RightFootThumb1S.RightFootThumb1Sx
    RightFootThumb1Sy = RightFootThumb1S.RightFootThumb1Sy
    RightFootThumb1Sz = RightFootThumb1S.RightFootThumb1Sz

    RightFootThumb1RotateOrder = RightFootThumb1RotateOrderEnumField(default_value=0)

    RightFootThumb1RotateAxis = RightFootThumb1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb1RotateAxisx = RightFootThumb1RotateAxis.RightFootThumb1RotateAxisx
    RightFootThumb1RotateAxisy = RightFootThumb1RotateAxis.RightFootThumb1RotateAxisy
    RightFootThumb1RotateAxisz = RightFootThumb1RotateAxis.RightFootThumb1RotateAxisz

    RightFootThumb1JointOrient = RightFootThumb1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb1JointOrientx = RightFootThumb1JointOrient.RightFootThumb1JointOrientx
    RightFootThumb1JointOrienty = RightFootThumb1JointOrient.RightFootThumb1JointOrienty
    RightFootThumb1JointOrientz = RightFootThumb1JointOrient.RightFootThumb1JointOrientz

    RightFootThumb1MinRLimit = RightFootThumb1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb1MinRLimitx = RightFootThumb1MinRLimit.RightFootThumb1MinRLimitx
    RightFootThumb1MinRLimity = RightFootThumb1MinRLimit.RightFootThumb1MinRLimity
    RightFootThumb1MinRLimitz = RightFootThumb1MinRLimit.RightFootThumb1MinRLimitz

    RightFootThumb1MaxRLimit = RightFootThumb1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb1MaxRLimitx = RightFootThumb1MaxRLimit.RightFootThumb1MaxRLimitx
    RightFootThumb1MaxRLimity = RightFootThumb1MaxRLimit.RightFootThumb1MaxRLimity
    RightFootThumb1MaxRLimitz = RightFootThumb1MaxRLimit.RightFootThumb1MaxRLimitz

    RightFootThumb1MinRLimitEnablex = BoolField(default_value=False)

    RightFootThumb1MinRLimitEnabley = BoolField(default_value=False)

    RightFootThumb1MinRLimitEnablez = BoolField(default_value=False)

    RightFootThumb1MaxRLimitEnablex = BoolField(default_value=False)

    RightFootThumb1MaxRLimitEnabley = BoolField(default_value=False)

    RightFootThumb1MaxRLimitEnablez = BoolField(default_value=False)

    RightFootThumb2 = MessageField()

    RightFootThumb2T = RightFootThumb2TField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb2Tx = RightFootThumb2T.RightFootThumb2Tx
    RightFootThumb2Ty = RightFootThumb2T.RightFootThumb2Ty
    RightFootThumb2Tz = RightFootThumb2T.RightFootThumb2Tz

    RightFootThumb2R = RightFootThumb2RField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb2Rx = RightFootThumb2R.RightFootThumb2Rx
    RightFootThumb2Ry = RightFootThumb2R.RightFootThumb2Ry
    RightFootThumb2Rz = RightFootThumb2R.RightFootThumb2Rz

    RightFootThumb2S = RightFootThumb2SField(default_value=(1.0, 1.0, 1.0))
    RightFootThumb2Sx = RightFootThumb2S.RightFootThumb2Sx
    RightFootThumb2Sy = RightFootThumb2S.RightFootThumb2Sy
    RightFootThumb2Sz = RightFootThumb2S.RightFootThumb2Sz

    RightFootThumb2RotateOrder = RightFootThumb2RotateOrderEnumField(default_value=0)

    RightFootThumb2RotateAxis = RightFootThumb2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb2RotateAxisx = RightFootThumb2RotateAxis.RightFootThumb2RotateAxisx
    RightFootThumb2RotateAxisy = RightFootThumb2RotateAxis.RightFootThumb2RotateAxisy
    RightFootThumb2RotateAxisz = RightFootThumb2RotateAxis.RightFootThumb2RotateAxisz

    RightFootThumb2JointOrient = RightFootThumb2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb2JointOrientx = RightFootThumb2JointOrient.RightFootThumb2JointOrientx
    RightFootThumb2JointOrienty = RightFootThumb2JointOrient.RightFootThumb2JointOrienty
    RightFootThumb2JointOrientz = RightFootThumb2JointOrient.RightFootThumb2JointOrientz

    RightFootThumb2MinRLimit = RightFootThumb2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb2MinRLimitx = RightFootThumb2MinRLimit.RightFootThumb2MinRLimitx
    RightFootThumb2MinRLimity = RightFootThumb2MinRLimit.RightFootThumb2MinRLimity
    RightFootThumb2MinRLimitz = RightFootThumb2MinRLimit.RightFootThumb2MinRLimitz

    RightFootThumb2MaxRLimit = RightFootThumb2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb2MaxRLimitx = RightFootThumb2MaxRLimit.RightFootThumb2MaxRLimitx
    RightFootThumb2MaxRLimity = RightFootThumb2MaxRLimit.RightFootThumb2MaxRLimity
    RightFootThumb2MaxRLimitz = RightFootThumb2MaxRLimit.RightFootThumb2MaxRLimitz

    RightFootThumb2MinRLimitEnablex = BoolField(default_value=False)

    RightFootThumb2MinRLimitEnabley = BoolField(default_value=False)

    RightFootThumb2MinRLimitEnablez = BoolField(default_value=False)

    RightFootThumb2MaxRLimitEnablex = BoolField(default_value=False)

    RightFootThumb2MaxRLimitEnabley = BoolField(default_value=False)

    RightFootThumb2MaxRLimitEnablez = BoolField(default_value=False)

    RightFootThumb3 = MessageField()

    RightFootThumb3T = RightFootThumb3TField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb3Tx = RightFootThumb3T.RightFootThumb3Tx
    RightFootThumb3Ty = RightFootThumb3T.RightFootThumb3Ty
    RightFootThumb3Tz = RightFootThumb3T.RightFootThumb3Tz

    RightFootThumb3R = RightFootThumb3RField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb3Rx = RightFootThumb3R.RightFootThumb3Rx
    RightFootThumb3Ry = RightFootThumb3R.RightFootThumb3Ry
    RightFootThumb3Rz = RightFootThumb3R.RightFootThumb3Rz

    RightFootThumb3S = RightFootThumb3SField(default_value=(1.0, 1.0, 1.0))
    RightFootThumb3Sx = RightFootThumb3S.RightFootThumb3Sx
    RightFootThumb3Sy = RightFootThumb3S.RightFootThumb3Sy
    RightFootThumb3Sz = RightFootThumb3S.RightFootThumb3Sz

    RightFootThumb3RotateOrder = RightFootThumb3RotateOrderEnumField(default_value=0)

    RightFootThumb3RotateAxis = RightFootThumb3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb3RotateAxisx = RightFootThumb3RotateAxis.RightFootThumb3RotateAxisx
    RightFootThumb3RotateAxisy = RightFootThumb3RotateAxis.RightFootThumb3RotateAxisy
    RightFootThumb3RotateAxisz = RightFootThumb3RotateAxis.RightFootThumb3RotateAxisz

    RightFootThumb3JointOrient = RightFootThumb3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb3JointOrientx = RightFootThumb3JointOrient.RightFootThumb3JointOrientx
    RightFootThumb3JointOrienty = RightFootThumb3JointOrient.RightFootThumb3JointOrienty
    RightFootThumb3JointOrientz = RightFootThumb3JointOrient.RightFootThumb3JointOrientz

    RightFootThumb3MinRLimit = RightFootThumb3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb3MinRLimitx = RightFootThumb3MinRLimit.RightFootThumb3MinRLimitx
    RightFootThumb3MinRLimity = RightFootThumb3MinRLimit.RightFootThumb3MinRLimity
    RightFootThumb3MinRLimitz = RightFootThumb3MinRLimit.RightFootThumb3MinRLimitz

    RightFootThumb3MaxRLimit = RightFootThumb3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb3MaxRLimitx = RightFootThumb3MaxRLimit.RightFootThumb3MaxRLimitx
    RightFootThumb3MaxRLimity = RightFootThumb3MaxRLimit.RightFootThumb3MaxRLimity
    RightFootThumb3MaxRLimitz = RightFootThumb3MaxRLimit.RightFootThumb3MaxRLimitz

    RightFootThumb3MinRLimitEnablex = BoolField(default_value=False)

    RightFootThumb3MinRLimitEnabley = BoolField(default_value=False)

    RightFootThumb3MinRLimitEnablez = BoolField(default_value=False)

    RightFootThumb3MaxRLimitEnablex = BoolField(default_value=False)

    RightFootThumb3MaxRLimitEnabley = BoolField(default_value=False)

    RightFootThumb3MaxRLimitEnablez = BoolField(default_value=False)

    RightFootThumb4 = MessageField()

    RightFootThumb4T = RightFootThumb4TField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb4Tx = RightFootThumb4T.RightFootThumb4Tx
    RightFootThumb4Ty = RightFootThumb4T.RightFootThumb4Ty
    RightFootThumb4Tz = RightFootThumb4T.RightFootThumb4Tz

    RightFootThumb4R = RightFootThumb4RField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb4Rx = RightFootThumb4R.RightFootThumb4Rx
    RightFootThumb4Ry = RightFootThumb4R.RightFootThumb4Ry
    RightFootThumb4Rz = RightFootThumb4R.RightFootThumb4Rz

    RightFootThumb4S = RightFootThumb4SField(default_value=(1.0, 1.0, 1.0))
    RightFootThumb4Sx = RightFootThumb4S.RightFootThumb4Sx
    RightFootThumb4Sy = RightFootThumb4S.RightFootThumb4Sy
    RightFootThumb4Sz = RightFootThumb4S.RightFootThumb4Sz

    RightFootThumb4RotateOrder = RightFootThumb4RotateOrderEnumField(default_value=0)

    RightFootThumb4RotateAxis = RightFootThumb4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb4RotateAxisx = RightFootThumb4RotateAxis.RightFootThumb4RotateAxisx
    RightFootThumb4RotateAxisy = RightFootThumb4RotateAxis.RightFootThumb4RotateAxisy
    RightFootThumb4RotateAxisz = RightFootThumb4RotateAxis.RightFootThumb4RotateAxisz

    RightFootThumb4JointOrient = RightFootThumb4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb4JointOrientx = RightFootThumb4JointOrient.RightFootThumb4JointOrientx
    RightFootThumb4JointOrienty = RightFootThumb4JointOrient.RightFootThumb4JointOrienty
    RightFootThumb4JointOrientz = RightFootThumb4JointOrient.RightFootThumb4JointOrientz

    RightFootThumb4MinRLimit = RightFootThumb4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb4MinRLimitx = RightFootThumb4MinRLimit.RightFootThumb4MinRLimitx
    RightFootThumb4MinRLimity = RightFootThumb4MinRLimit.RightFootThumb4MinRLimity
    RightFootThumb4MinRLimitz = RightFootThumb4MinRLimit.RightFootThumb4MinRLimitz

    RightFootThumb4MaxRLimit = RightFootThumb4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb4MaxRLimitx = RightFootThumb4MaxRLimit.RightFootThumb4MaxRLimitx
    RightFootThumb4MaxRLimity = RightFootThumb4MaxRLimit.RightFootThumb4MaxRLimity
    RightFootThumb4MaxRLimitz = RightFootThumb4MaxRLimit.RightFootThumb4MaxRLimitz

    RightFootThumb4MinRLimitEnablex = BoolField(default_value=False)

    RightFootThumb4MinRLimitEnabley = BoolField(default_value=False)

    RightFootThumb4MinRLimitEnablez = BoolField(default_value=False)

    RightFootThumb4MaxRLimitEnablex = BoolField(default_value=False)

    RightFootThumb4MaxRLimitEnabley = BoolField(default_value=False)

    RightFootThumb4MaxRLimitEnablez = BoolField(default_value=False)

    RightFootIndex1 = MessageField()

    RightFootIndex1T = RightFootIndex1TField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex1Tx = RightFootIndex1T.RightFootIndex1Tx
    RightFootIndex1Ty = RightFootIndex1T.RightFootIndex1Ty
    RightFootIndex1Tz = RightFootIndex1T.RightFootIndex1Tz

    RightFootIndex1R = RightFootIndex1RField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex1Rx = RightFootIndex1R.RightFootIndex1Rx
    RightFootIndex1Ry = RightFootIndex1R.RightFootIndex1Ry
    RightFootIndex1Rz = RightFootIndex1R.RightFootIndex1Rz

    RightFootIndex1S = RightFootIndex1SField(default_value=(1.0, 1.0, 1.0))
    RightFootIndex1Sx = RightFootIndex1S.RightFootIndex1Sx
    RightFootIndex1Sy = RightFootIndex1S.RightFootIndex1Sy
    RightFootIndex1Sz = RightFootIndex1S.RightFootIndex1Sz

    RightFootIndex1RotateOrder = RightFootIndex1RotateOrderEnumField(default_value=0)

    RightFootIndex1RotateAxis = RightFootIndex1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex1RotateAxisx = RightFootIndex1RotateAxis.RightFootIndex1RotateAxisx
    RightFootIndex1RotateAxisy = RightFootIndex1RotateAxis.RightFootIndex1RotateAxisy
    RightFootIndex1RotateAxisz = RightFootIndex1RotateAxis.RightFootIndex1RotateAxisz

    RightFootIndex1JointOrient = RightFootIndex1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex1JointOrientx = RightFootIndex1JointOrient.RightFootIndex1JointOrientx
    RightFootIndex1JointOrienty = RightFootIndex1JointOrient.RightFootIndex1JointOrienty
    RightFootIndex1JointOrientz = RightFootIndex1JointOrient.RightFootIndex1JointOrientz

    RightFootIndex1MinRLimit = RightFootIndex1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex1MinRLimitx = RightFootIndex1MinRLimit.RightFootIndex1MinRLimitx
    RightFootIndex1MinRLimity = RightFootIndex1MinRLimit.RightFootIndex1MinRLimity
    RightFootIndex1MinRLimitz = RightFootIndex1MinRLimit.RightFootIndex1MinRLimitz

    RightFootIndex1MaxRLimit = RightFootIndex1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex1MaxRLimitx = RightFootIndex1MaxRLimit.RightFootIndex1MaxRLimitx
    RightFootIndex1MaxRLimity = RightFootIndex1MaxRLimit.RightFootIndex1MaxRLimity
    RightFootIndex1MaxRLimitz = RightFootIndex1MaxRLimit.RightFootIndex1MaxRLimitz

    RightFootIndex1MinRLimitEnablex = BoolField(default_value=False)

    RightFootIndex1MinRLimitEnabley = BoolField(default_value=False)

    RightFootIndex1MinRLimitEnablez = BoolField(default_value=False)

    RightFootIndex1MaxRLimitEnablex = BoolField(default_value=False)

    RightFootIndex1MaxRLimitEnabley = BoolField(default_value=False)

    RightFootIndex1MaxRLimitEnablez = BoolField(default_value=False)

    RightFootIndex2 = MessageField()

    RightFootIndex2T = RightFootIndex2TField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex2Tx = RightFootIndex2T.RightFootIndex2Tx
    RightFootIndex2Ty = RightFootIndex2T.RightFootIndex2Ty
    RightFootIndex2Tz = RightFootIndex2T.RightFootIndex2Tz

    RightFootIndex2R = RightFootIndex2RField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex2Rx = RightFootIndex2R.RightFootIndex2Rx
    RightFootIndex2Ry = RightFootIndex2R.RightFootIndex2Ry
    RightFootIndex2Rz = RightFootIndex2R.RightFootIndex2Rz

    RightFootIndex2S = RightFootIndex2SField(default_value=(1.0, 1.0, 1.0))
    RightFootIndex2Sx = RightFootIndex2S.RightFootIndex2Sx
    RightFootIndex2Sy = RightFootIndex2S.RightFootIndex2Sy
    RightFootIndex2Sz = RightFootIndex2S.RightFootIndex2Sz

    RightFootIndex2RotateOrder = RightFootIndex2RotateOrderEnumField(default_value=0)

    RightFootIndex2RotateAxis = RightFootIndex2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex2RotateAxisx = RightFootIndex2RotateAxis.RightFootIndex2RotateAxisx
    RightFootIndex2RotateAxisy = RightFootIndex2RotateAxis.RightFootIndex2RotateAxisy
    RightFootIndex2RotateAxisz = RightFootIndex2RotateAxis.RightFootIndex2RotateAxisz

    RightFootIndex2JointOrient = RightFootIndex2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex2JointOrientx = RightFootIndex2JointOrient.RightFootIndex2JointOrientx
    RightFootIndex2JointOrienty = RightFootIndex2JointOrient.RightFootIndex2JointOrienty
    RightFootIndex2JointOrientz = RightFootIndex2JointOrient.RightFootIndex2JointOrientz

    RightFootIndex2MinRLimit = RightFootIndex2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex2MinRLimitx = RightFootIndex2MinRLimit.RightFootIndex2MinRLimitx
    RightFootIndex2MinRLimity = RightFootIndex2MinRLimit.RightFootIndex2MinRLimity
    RightFootIndex2MinRLimitz = RightFootIndex2MinRLimit.RightFootIndex2MinRLimitz

    RightFootIndex2MaxRLimit = RightFootIndex2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex2MaxRLimitx = RightFootIndex2MaxRLimit.RightFootIndex2MaxRLimitx
    RightFootIndex2MaxRLimity = RightFootIndex2MaxRLimit.RightFootIndex2MaxRLimity
    RightFootIndex2MaxRLimitz = RightFootIndex2MaxRLimit.RightFootIndex2MaxRLimitz

    RightFootIndex2MinRLimitEnablex = BoolField(default_value=False)

    RightFootIndex2MinRLimitEnabley = BoolField(default_value=False)

    RightFootIndex2MinRLimitEnablez = BoolField(default_value=False)

    RightFootIndex2MaxRLimitEnablex = BoolField(default_value=False)

    RightFootIndex2MaxRLimitEnabley = BoolField(default_value=False)

    RightFootIndex2MaxRLimitEnablez = BoolField(default_value=False)

    RightFootIndex3 = MessageField()

    RightFootIndex3T = RightFootIndex3TField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex3Tx = RightFootIndex3T.RightFootIndex3Tx
    RightFootIndex3Ty = RightFootIndex3T.RightFootIndex3Ty
    RightFootIndex3Tz = RightFootIndex3T.RightFootIndex3Tz

    RightFootIndex3R = RightFootIndex3RField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex3Rx = RightFootIndex3R.RightFootIndex3Rx
    RightFootIndex3Ry = RightFootIndex3R.RightFootIndex3Ry
    RightFootIndex3Rz = RightFootIndex3R.RightFootIndex3Rz

    RightFootIndex3S = RightFootIndex3SField(default_value=(1.0, 1.0, 1.0))
    RightFootIndex3Sx = RightFootIndex3S.RightFootIndex3Sx
    RightFootIndex3Sy = RightFootIndex3S.RightFootIndex3Sy
    RightFootIndex3Sz = RightFootIndex3S.RightFootIndex3Sz

    RightFootIndex3RotateOrder = RightFootIndex3RotateOrderEnumField(default_value=0)

    RightFootIndex3RotateAxis = RightFootIndex3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex3RotateAxisx = RightFootIndex3RotateAxis.RightFootIndex3RotateAxisx
    RightFootIndex3RotateAxisy = RightFootIndex3RotateAxis.RightFootIndex3RotateAxisy
    RightFootIndex3RotateAxisz = RightFootIndex3RotateAxis.RightFootIndex3RotateAxisz

    RightFootIndex3JointOrient = RightFootIndex3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex3JointOrientx = RightFootIndex3JointOrient.RightFootIndex3JointOrientx
    RightFootIndex3JointOrienty = RightFootIndex3JointOrient.RightFootIndex3JointOrienty
    RightFootIndex3JointOrientz = RightFootIndex3JointOrient.RightFootIndex3JointOrientz

    RightFootIndex3MinRLimit = RightFootIndex3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex3MinRLimitx = RightFootIndex3MinRLimit.RightFootIndex3MinRLimitx
    RightFootIndex3MinRLimity = RightFootIndex3MinRLimit.RightFootIndex3MinRLimity
    RightFootIndex3MinRLimitz = RightFootIndex3MinRLimit.RightFootIndex3MinRLimitz

    RightFootIndex3MaxRLimit = RightFootIndex3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex3MaxRLimitx = RightFootIndex3MaxRLimit.RightFootIndex3MaxRLimitx
    RightFootIndex3MaxRLimity = RightFootIndex3MaxRLimit.RightFootIndex3MaxRLimity
    RightFootIndex3MaxRLimitz = RightFootIndex3MaxRLimit.RightFootIndex3MaxRLimitz

    RightFootIndex3MinRLimitEnablex = BoolField(default_value=False)

    RightFootIndex3MinRLimitEnabley = BoolField(default_value=False)

    RightFootIndex3MinRLimitEnablez = BoolField(default_value=False)

    RightFootIndex3MaxRLimitEnablex = BoolField(default_value=False)

    RightFootIndex3MaxRLimitEnabley = BoolField(default_value=False)

    RightFootIndex3MaxRLimitEnablez = BoolField(default_value=False)

    RightFootIndex4 = MessageField()

    RightFootIndex4T = RightFootIndex4TField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex4Tx = RightFootIndex4T.RightFootIndex4Tx
    RightFootIndex4Ty = RightFootIndex4T.RightFootIndex4Ty
    RightFootIndex4Tz = RightFootIndex4T.RightFootIndex4Tz

    RightFootIndex4R = RightFootIndex4RField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex4Rx = RightFootIndex4R.RightFootIndex4Rx
    RightFootIndex4Ry = RightFootIndex4R.RightFootIndex4Ry
    RightFootIndex4Rz = RightFootIndex4R.RightFootIndex4Rz

    RightFootIndex4S = RightFootIndex4SField(default_value=(1.0, 1.0, 1.0))
    RightFootIndex4Sx = RightFootIndex4S.RightFootIndex4Sx
    RightFootIndex4Sy = RightFootIndex4S.RightFootIndex4Sy
    RightFootIndex4Sz = RightFootIndex4S.RightFootIndex4Sz

    RightFootIndex4RotateOrder = RightFootIndex4RotateOrderEnumField(default_value=0)

    RightFootIndex4RotateAxis = RightFootIndex4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex4RotateAxisx = RightFootIndex4RotateAxis.RightFootIndex4RotateAxisx
    RightFootIndex4RotateAxisy = RightFootIndex4RotateAxis.RightFootIndex4RotateAxisy
    RightFootIndex4RotateAxisz = RightFootIndex4RotateAxis.RightFootIndex4RotateAxisz

    RightFootIndex4JointOrient = RightFootIndex4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex4JointOrientx = RightFootIndex4JointOrient.RightFootIndex4JointOrientx
    RightFootIndex4JointOrienty = RightFootIndex4JointOrient.RightFootIndex4JointOrienty
    RightFootIndex4JointOrientz = RightFootIndex4JointOrient.RightFootIndex4JointOrientz

    RightFootIndex4MinRLimit = RightFootIndex4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex4MinRLimitx = RightFootIndex4MinRLimit.RightFootIndex4MinRLimitx
    RightFootIndex4MinRLimity = RightFootIndex4MinRLimit.RightFootIndex4MinRLimity
    RightFootIndex4MinRLimitz = RightFootIndex4MinRLimit.RightFootIndex4MinRLimitz

    RightFootIndex4MaxRLimit = RightFootIndex4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex4MaxRLimitx = RightFootIndex4MaxRLimit.RightFootIndex4MaxRLimitx
    RightFootIndex4MaxRLimity = RightFootIndex4MaxRLimit.RightFootIndex4MaxRLimity
    RightFootIndex4MaxRLimitz = RightFootIndex4MaxRLimit.RightFootIndex4MaxRLimitz

    RightFootIndex4MinRLimitEnablex = BoolField(default_value=False)

    RightFootIndex4MinRLimitEnabley = BoolField(default_value=False)

    RightFootIndex4MinRLimitEnablez = BoolField(default_value=False)

    RightFootIndex4MaxRLimitEnablex = BoolField(default_value=False)

    RightFootIndex4MaxRLimitEnabley = BoolField(default_value=False)

    RightFootIndex4MaxRLimitEnablez = BoolField(default_value=False)

    RightFootMiddle1 = MessageField()

    RightFootMiddle1T = RightFootMiddle1TField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle1Tx = RightFootMiddle1T.RightFootMiddle1Tx
    RightFootMiddle1Ty = RightFootMiddle1T.RightFootMiddle1Ty
    RightFootMiddle1Tz = RightFootMiddle1T.RightFootMiddle1Tz

    RightFootMiddle1R = RightFootMiddle1RField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle1Rx = RightFootMiddle1R.RightFootMiddle1Rx
    RightFootMiddle1Ry = RightFootMiddle1R.RightFootMiddle1Ry
    RightFootMiddle1Rz = RightFootMiddle1R.RightFootMiddle1Rz

    RightFootMiddle1S = RightFootMiddle1SField(default_value=(1.0, 1.0, 1.0))
    RightFootMiddle1Sx = RightFootMiddle1S.RightFootMiddle1Sx
    RightFootMiddle1Sy = RightFootMiddle1S.RightFootMiddle1Sy
    RightFootMiddle1Sz = RightFootMiddle1S.RightFootMiddle1Sz

    RightFootMiddle1RotateOrder = RightFootMiddle1RotateOrderEnumField(default_value=0)

    RightFootMiddle1RotateAxis = RightFootMiddle1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle1RotateAxisx = RightFootMiddle1RotateAxis.RightFootMiddle1RotateAxisx
    RightFootMiddle1RotateAxisy = RightFootMiddle1RotateAxis.RightFootMiddle1RotateAxisy
    RightFootMiddle1RotateAxisz = RightFootMiddle1RotateAxis.RightFootMiddle1RotateAxisz

    RightFootMiddle1JointOrient = RightFootMiddle1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle1JointOrientx = RightFootMiddle1JointOrient.RightFootMiddle1JointOrientx
    RightFootMiddle1JointOrienty = RightFootMiddle1JointOrient.RightFootMiddle1JointOrienty
    RightFootMiddle1JointOrientz = RightFootMiddle1JointOrient.RightFootMiddle1JointOrientz

    RightFootMiddle1MinRLimit = RightFootMiddle1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle1MinRLimitx = RightFootMiddle1MinRLimit.RightFootMiddle1MinRLimitx
    RightFootMiddle1MinRLimity = RightFootMiddle1MinRLimit.RightFootMiddle1MinRLimity
    RightFootMiddle1MinRLimitz = RightFootMiddle1MinRLimit.RightFootMiddle1MinRLimitz

    RightFootMiddle1MaxRLimit = RightFootMiddle1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle1MaxRLimitx = RightFootMiddle1MaxRLimit.RightFootMiddle1MaxRLimitx
    RightFootMiddle1MaxRLimity = RightFootMiddle1MaxRLimit.RightFootMiddle1MaxRLimity
    RightFootMiddle1MaxRLimitz = RightFootMiddle1MaxRLimit.RightFootMiddle1MaxRLimitz

    RightFootMiddle1MinRLimitEnablex = BoolField(default_value=False)

    RightFootMiddle1MinRLimitEnabley = BoolField(default_value=False)

    RightFootMiddle1MinRLimitEnablez = BoolField(default_value=False)

    RightFootMiddle1MaxRLimitEnablex = BoolField(default_value=False)

    RightFootMiddle1MaxRLimitEnabley = BoolField(default_value=False)

    RightFootMiddle1MaxRLimitEnablez = BoolField(default_value=False)

    RightFootMiddle2 = MessageField()

    RightFootMiddle2T = RightFootMiddle2TField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle2Tx = RightFootMiddle2T.RightFootMiddle2Tx
    RightFootMiddle2Ty = RightFootMiddle2T.RightFootMiddle2Ty
    RightFootMiddle2Tz = RightFootMiddle2T.RightFootMiddle2Tz

    RightFootMiddle2R = RightFootMiddle2RField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle2Rx = RightFootMiddle2R.RightFootMiddle2Rx
    RightFootMiddle2Ry = RightFootMiddle2R.RightFootMiddle2Ry
    RightFootMiddle2Rz = RightFootMiddle2R.RightFootMiddle2Rz

    RightFootMiddle2S = RightFootMiddle2SField(default_value=(1.0, 1.0, 1.0))
    RightFootMiddle2Sx = RightFootMiddle2S.RightFootMiddle2Sx
    RightFootMiddle2Sy = RightFootMiddle2S.RightFootMiddle2Sy
    RightFootMiddle2Sz = RightFootMiddle2S.RightFootMiddle2Sz

    RightFootMiddle2RotateOrder = RightFootMiddle2RotateOrderEnumField(default_value=0)

    RightFootMiddle2RotateAxis = RightFootMiddle2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle2RotateAxisx = RightFootMiddle2RotateAxis.RightFootMiddle2RotateAxisx
    RightFootMiddle2RotateAxisy = RightFootMiddle2RotateAxis.RightFootMiddle2RotateAxisy
    RightFootMiddle2RotateAxisz = RightFootMiddle2RotateAxis.RightFootMiddle2RotateAxisz

    RightFootMiddle2JointOrient = RightFootMiddle2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle2JointOrientx = RightFootMiddle2JointOrient.RightFootMiddle2JointOrientx
    RightFootMiddle2JointOrienty = RightFootMiddle2JointOrient.RightFootMiddle2JointOrienty
    RightFootMiddle2JointOrientz = RightFootMiddle2JointOrient.RightFootMiddle2JointOrientz

    RightFootMiddle2MinRLimit = RightFootMiddle2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle2MinRLimitx = RightFootMiddle2MinRLimit.RightFootMiddle2MinRLimitx
    RightFootMiddle2MinRLimity = RightFootMiddle2MinRLimit.RightFootMiddle2MinRLimity
    RightFootMiddle2MinRLimitz = RightFootMiddle2MinRLimit.RightFootMiddle2MinRLimitz

    RightFootMiddle2MaxRLimit = RightFootMiddle2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle2MaxRLimitx = RightFootMiddle2MaxRLimit.RightFootMiddle2MaxRLimitx
    RightFootMiddle2MaxRLimity = RightFootMiddle2MaxRLimit.RightFootMiddle2MaxRLimity
    RightFootMiddle2MaxRLimitz = RightFootMiddle2MaxRLimit.RightFootMiddle2MaxRLimitz

    RightFootMiddle2MinRLimitEnablex = BoolField(default_value=False)

    RightFootMiddle2MinRLimitEnabley = BoolField(default_value=False)

    RightFootMiddle2MinRLimitEnablez = BoolField(default_value=False)

    RightFootMiddle2MaxRLimitEnablex = BoolField(default_value=False)

    RightFootMiddle2MaxRLimitEnabley = BoolField(default_value=False)

    RightFootMiddle2MaxRLimitEnablez = BoolField(default_value=False)

    RightFootMiddle3 = MessageField()

    RightFootMiddle3T = RightFootMiddle3TField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle3Tx = RightFootMiddle3T.RightFootMiddle3Tx
    RightFootMiddle3Ty = RightFootMiddle3T.RightFootMiddle3Ty
    RightFootMiddle3Tz = RightFootMiddle3T.RightFootMiddle3Tz

    RightFootMiddle3R = RightFootMiddle3RField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle3Rx = RightFootMiddle3R.RightFootMiddle3Rx
    RightFootMiddle3Ry = RightFootMiddle3R.RightFootMiddle3Ry
    RightFootMiddle3Rz = RightFootMiddle3R.RightFootMiddle3Rz

    RightFootMiddle3S = RightFootMiddle3SField(default_value=(1.0, 1.0, 1.0))
    RightFootMiddle3Sx = RightFootMiddle3S.RightFootMiddle3Sx
    RightFootMiddle3Sy = RightFootMiddle3S.RightFootMiddle3Sy
    RightFootMiddle3Sz = RightFootMiddle3S.RightFootMiddle3Sz

    RightFootMiddle3RotateOrder = RightFootMiddle3RotateOrderEnumField(default_value=0)

    RightFootMiddle3RotateAxis = RightFootMiddle3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle3RotateAxisx = RightFootMiddle3RotateAxis.RightFootMiddle3RotateAxisx
    RightFootMiddle3RotateAxisy = RightFootMiddle3RotateAxis.RightFootMiddle3RotateAxisy
    RightFootMiddle3RotateAxisz = RightFootMiddle3RotateAxis.RightFootMiddle3RotateAxisz

    RightFootMiddle3JointOrient = RightFootMiddle3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle3JointOrientx = RightFootMiddle3JointOrient.RightFootMiddle3JointOrientx
    RightFootMiddle3JointOrienty = RightFootMiddle3JointOrient.RightFootMiddle3JointOrienty
    RightFootMiddle3JointOrientz = RightFootMiddle3JointOrient.RightFootMiddle3JointOrientz

    RightFootMiddle3MinRLimit = RightFootMiddle3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle3MinRLimitx = RightFootMiddle3MinRLimit.RightFootMiddle3MinRLimitx
    RightFootMiddle3MinRLimity = RightFootMiddle3MinRLimit.RightFootMiddle3MinRLimity
    RightFootMiddle3MinRLimitz = RightFootMiddle3MinRLimit.RightFootMiddle3MinRLimitz

    RightFootMiddle3MaxRLimit = RightFootMiddle3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle3MaxRLimitx = RightFootMiddle3MaxRLimit.RightFootMiddle3MaxRLimitx
    RightFootMiddle3MaxRLimity = RightFootMiddle3MaxRLimit.RightFootMiddle3MaxRLimity
    RightFootMiddle3MaxRLimitz = RightFootMiddle3MaxRLimit.RightFootMiddle3MaxRLimitz

    RightFootMiddle3MinRLimitEnablex = BoolField(default_value=False)

    RightFootMiddle3MinRLimitEnabley = BoolField(default_value=False)

    RightFootMiddle3MinRLimitEnablez = BoolField(default_value=False)

    RightFootMiddle3MaxRLimitEnablex = BoolField(default_value=False)

    RightFootMiddle3MaxRLimitEnabley = BoolField(default_value=False)

    RightFootMiddle3MaxRLimitEnablez = BoolField(default_value=False)

    RightFootMiddle4 = MessageField()

    RightFootMiddle4T = RightFootMiddle4TField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle4Tx = RightFootMiddle4T.RightFootMiddle4Tx
    RightFootMiddle4Ty = RightFootMiddle4T.RightFootMiddle4Ty
    RightFootMiddle4Tz = RightFootMiddle4T.RightFootMiddle4Tz

    RightFootMiddle4R = RightFootMiddle4RField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle4Rx = RightFootMiddle4R.RightFootMiddle4Rx
    RightFootMiddle4Ry = RightFootMiddle4R.RightFootMiddle4Ry
    RightFootMiddle4Rz = RightFootMiddle4R.RightFootMiddle4Rz

    RightFootMiddle4S = RightFootMiddle4SField(default_value=(1.0, 1.0, 1.0))
    RightFootMiddle4Sx = RightFootMiddle4S.RightFootMiddle4Sx
    RightFootMiddle4Sy = RightFootMiddle4S.RightFootMiddle4Sy
    RightFootMiddle4Sz = RightFootMiddle4S.RightFootMiddle4Sz

    RightFootMiddle4RotateOrder = RightFootMiddle4RotateOrderEnumField(default_value=0)

    RightFootMiddle4RotateAxis = RightFootMiddle4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle4RotateAxisx = RightFootMiddle4RotateAxis.RightFootMiddle4RotateAxisx
    RightFootMiddle4RotateAxisy = RightFootMiddle4RotateAxis.RightFootMiddle4RotateAxisy
    RightFootMiddle4RotateAxisz = RightFootMiddle4RotateAxis.RightFootMiddle4RotateAxisz

    RightFootMiddle4JointOrient = RightFootMiddle4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle4JointOrientx = RightFootMiddle4JointOrient.RightFootMiddle4JointOrientx
    RightFootMiddle4JointOrienty = RightFootMiddle4JointOrient.RightFootMiddle4JointOrienty
    RightFootMiddle4JointOrientz = RightFootMiddle4JointOrient.RightFootMiddle4JointOrientz

    RightFootMiddle4MinRLimit = RightFootMiddle4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle4MinRLimitx = RightFootMiddle4MinRLimit.RightFootMiddle4MinRLimitx
    RightFootMiddle4MinRLimity = RightFootMiddle4MinRLimit.RightFootMiddle4MinRLimity
    RightFootMiddle4MinRLimitz = RightFootMiddle4MinRLimit.RightFootMiddle4MinRLimitz

    RightFootMiddle4MaxRLimit = RightFootMiddle4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle4MaxRLimitx = RightFootMiddle4MaxRLimit.RightFootMiddle4MaxRLimitx
    RightFootMiddle4MaxRLimity = RightFootMiddle4MaxRLimit.RightFootMiddle4MaxRLimity
    RightFootMiddle4MaxRLimitz = RightFootMiddle4MaxRLimit.RightFootMiddle4MaxRLimitz

    RightFootMiddle4MinRLimitEnablex = BoolField(default_value=False)

    RightFootMiddle4MinRLimitEnabley = BoolField(default_value=False)

    RightFootMiddle4MinRLimitEnablez = BoolField(default_value=False)

    RightFootMiddle4MaxRLimitEnablex = BoolField(default_value=False)

    RightFootMiddle4MaxRLimitEnabley = BoolField(default_value=False)

    RightFootMiddle4MaxRLimitEnablez = BoolField(default_value=False)

    RightFootRing1 = MessageField()

    RightFootRing1T = RightFootRing1TField(default_value=(0.0, 0.0, 0.0))
    RightFootRing1Tx = RightFootRing1T.RightFootRing1Tx
    RightFootRing1Ty = RightFootRing1T.RightFootRing1Ty
    RightFootRing1Tz = RightFootRing1T.RightFootRing1Tz

    RightFootRing1R = RightFootRing1RField(default_value=(0.0, 0.0, 0.0))
    RightFootRing1Rx = RightFootRing1R.RightFootRing1Rx
    RightFootRing1Ry = RightFootRing1R.RightFootRing1Ry
    RightFootRing1Rz = RightFootRing1R.RightFootRing1Rz

    RightFootRing1S = RightFootRing1SField(default_value=(1.0, 1.0, 1.0))
    RightFootRing1Sx = RightFootRing1S.RightFootRing1Sx
    RightFootRing1Sy = RightFootRing1S.RightFootRing1Sy
    RightFootRing1Sz = RightFootRing1S.RightFootRing1Sz

    RightFootRing1RotateOrder = RightFootRing1RotateOrderEnumField(default_value=0)

    RightFootRing1RotateAxis = RightFootRing1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootRing1RotateAxisx = RightFootRing1RotateAxis.RightFootRing1RotateAxisx
    RightFootRing1RotateAxisy = RightFootRing1RotateAxis.RightFootRing1RotateAxisy
    RightFootRing1RotateAxisz = RightFootRing1RotateAxis.RightFootRing1RotateAxisz

    RightFootRing1JointOrient = RightFootRing1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootRing1JointOrientx = RightFootRing1JointOrient.RightFootRing1JointOrientx
    RightFootRing1JointOrienty = RightFootRing1JointOrient.RightFootRing1JointOrienty
    RightFootRing1JointOrientz = RightFootRing1JointOrient.RightFootRing1JointOrientz

    RightFootRing1MinRLimit = RightFootRing1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootRing1MinRLimitx = RightFootRing1MinRLimit.RightFootRing1MinRLimitx
    RightFootRing1MinRLimity = RightFootRing1MinRLimit.RightFootRing1MinRLimity
    RightFootRing1MinRLimitz = RightFootRing1MinRLimit.RightFootRing1MinRLimitz

    RightFootRing1MaxRLimit = RightFootRing1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootRing1MaxRLimitx = RightFootRing1MaxRLimit.RightFootRing1MaxRLimitx
    RightFootRing1MaxRLimity = RightFootRing1MaxRLimit.RightFootRing1MaxRLimity
    RightFootRing1MaxRLimitz = RightFootRing1MaxRLimit.RightFootRing1MaxRLimitz

    RightFootRing1MinRLimitEnablex = BoolField(default_value=False)

    RightFootRing1MinRLimitEnabley = BoolField(default_value=False)

    RightFootRing1MinRLimitEnablez = BoolField(default_value=False)

    RightFootRing1MaxRLimitEnablex = BoolField(default_value=False)

    RightFootRing1MaxRLimitEnabley = BoolField(default_value=False)

    RightFootRing1MaxRLimitEnablez = BoolField(default_value=False)

    RightFootRing2 = MessageField()

    RightFootRing2T = RightFootRing2TField(default_value=(0.0, 0.0, 0.0))
    RightFootRing2Tx = RightFootRing2T.RightFootRing2Tx
    RightFootRing2Ty = RightFootRing2T.RightFootRing2Ty
    RightFootRing2Tz = RightFootRing2T.RightFootRing2Tz

    RightFootRing2R = RightFootRing2RField(default_value=(0.0, 0.0, 0.0))
    RightFootRing2Rx = RightFootRing2R.RightFootRing2Rx
    RightFootRing2Ry = RightFootRing2R.RightFootRing2Ry
    RightFootRing2Rz = RightFootRing2R.RightFootRing2Rz

    RightFootRing2S = RightFootRing2SField(default_value=(1.0, 1.0, 1.0))
    RightFootRing2Sx = RightFootRing2S.RightFootRing2Sx
    RightFootRing2Sy = RightFootRing2S.RightFootRing2Sy
    RightFootRing2Sz = RightFootRing2S.RightFootRing2Sz

    RightFootRing2RotateOrder = RightFootRing2RotateOrderEnumField(default_value=0)

    RightFootRing2RotateAxis = RightFootRing2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootRing2RotateAxisx = RightFootRing2RotateAxis.RightFootRing2RotateAxisx
    RightFootRing2RotateAxisy = RightFootRing2RotateAxis.RightFootRing2RotateAxisy
    RightFootRing2RotateAxisz = RightFootRing2RotateAxis.RightFootRing2RotateAxisz

    RightFootRing2JointOrient = RightFootRing2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootRing2JointOrientx = RightFootRing2JointOrient.RightFootRing2JointOrientx
    RightFootRing2JointOrienty = RightFootRing2JointOrient.RightFootRing2JointOrienty
    RightFootRing2JointOrientz = RightFootRing2JointOrient.RightFootRing2JointOrientz

    RightFootRing2MinRLimit = RightFootRing2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootRing2MinRLimitx = RightFootRing2MinRLimit.RightFootRing2MinRLimitx
    RightFootRing2MinRLimity = RightFootRing2MinRLimit.RightFootRing2MinRLimity
    RightFootRing2MinRLimitz = RightFootRing2MinRLimit.RightFootRing2MinRLimitz

    RightFootRing2MaxRLimit = RightFootRing2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootRing2MaxRLimitx = RightFootRing2MaxRLimit.RightFootRing2MaxRLimitx
    RightFootRing2MaxRLimity = RightFootRing2MaxRLimit.RightFootRing2MaxRLimity
    RightFootRing2MaxRLimitz = RightFootRing2MaxRLimit.RightFootRing2MaxRLimitz

    RightFootRing2MinRLimitEnablex = BoolField(default_value=False)

    RightFootRing2MinRLimitEnabley = BoolField(default_value=False)

    RightFootRing2MinRLimitEnablez = BoolField(default_value=False)

    RightFootRing2MaxRLimitEnablex = BoolField(default_value=False)

    RightFootRing2MaxRLimitEnabley = BoolField(default_value=False)

    RightFootRing2MaxRLimitEnablez = BoolField(default_value=False)

    RightFootRing3 = MessageField()

    RightFootRing3T = RightFootRing3TField(default_value=(0.0, 0.0, 0.0))
    RightFootRing3Tx = RightFootRing3T.RightFootRing3Tx
    RightFootRing3Ty = RightFootRing3T.RightFootRing3Ty
    RightFootRing3Tz = RightFootRing3T.RightFootRing3Tz

    RightFootRing3R = RightFootRing3RField(default_value=(0.0, 0.0, 0.0))
    RightFootRing3Rx = RightFootRing3R.RightFootRing3Rx
    RightFootRing3Ry = RightFootRing3R.RightFootRing3Ry
    RightFootRing3Rz = RightFootRing3R.RightFootRing3Rz

    RightFootRing3S = RightFootRing3SField(default_value=(1.0, 1.0, 1.0))
    RightFootRing3Sx = RightFootRing3S.RightFootRing3Sx
    RightFootRing3Sy = RightFootRing3S.RightFootRing3Sy
    RightFootRing3Sz = RightFootRing3S.RightFootRing3Sz

    RightFootRing3RotateOrder = RightFootRing3RotateOrderEnumField(default_value=0)

    RightFootRing3RotateAxis = RightFootRing3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootRing3RotateAxisx = RightFootRing3RotateAxis.RightFootRing3RotateAxisx
    RightFootRing3RotateAxisy = RightFootRing3RotateAxis.RightFootRing3RotateAxisy
    RightFootRing3RotateAxisz = RightFootRing3RotateAxis.RightFootRing3RotateAxisz

    RightFootRing3JointOrient = RightFootRing3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootRing3JointOrientx = RightFootRing3JointOrient.RightFootRing3JointOrientx
    RightFootRing3JointOrienty = RightFootRing3JointOrient.RightFootRing3JointOrienty
    RightFootRing3JointOrientz = RightFootRing3JointOrient.RightFootRing3JointOrientz

    RightFootRing3MinRLimit = RightFootRing3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootRing3MinRLimitx = RightFootRing3MinRLimit.RightFootRing3MinRLimitx
    RightFootRing3MinRLimity = RightFootRing3MinRLimit.RightFootRing3MinRLimity
    RightFootRing3MinRLimitz = RightFootRing3MinRLimit.RightFootRing3MinRLimitz

    RightFootRing3MaxRLimit = RightFootRing3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootRing3MaxRLimitx = RightFootRing3MaxRLimit.RightFootRing3MaxRLimitx
    RightFootRing3MaxRLimity = RightFootRing3MaxRLimit.RightFootRing3MaxRLimity
    RightFootRing3MaxRLimitz = RightFootRing3MaxRLimit.RightFootRing3MaxRLimitz

    RightFootRing3MinRLimitEnablex = BoolField(default_value=False)

    RightFootRing3MinRLimitEnabley = BoolField(default_value=False)

    RightFootRing3MinRLimitEnablez = BoolField(default_value=False)

    RightFootRing3MaxRLimitEnablex = BoolField(default_value=False)

    RightFootRing3MaxRLimitEnabley = BoolField(default_value=False)

    RightFootRing3MaxRLimitEnablez = BoolField(default_value=False)

    RightFootRing4 = MessageField()

    RightFootRing4T = RightFootRing4TField(default_value=(0.0, 0.0, 0.0))
    RightFootRing4Tx = RightFootRing4T.RightFootRing4Tx
    RightFootRing4Ty = RightFootRing4T.RightFootRing4Ty
    RightFootRing4Tz = RightFootRing4T.RightFootRing4Tz

    RightFootRing4R = RightFootRing4RField(default_value=(0.0, 0.0, 0.0))
    RightFootRing4Rx = RightFootRing4R.RightFootRing4Rx
    RightFootRing4Ry = RightFootRing4R.RightFootRing4Ry
    RightFootRing4Rz = RightFootRing4R.RightFootRing4Rz

    RightFootRing4S = RightFootRing4SField(default_value=(1.0, 1.0, 1.0))
    RightFootRing4Sx = RightFootRing4S.RightFootRing4Sx
    RightFootRing4Sy = RightFootRing4S.RightFootRing4Sy
    RightFootRing4Sz = RightFootRing4S.RightFootRing4Sz

    RightFootRing4RotateOrder = RightFootRing4RotateOrderEnumField(default_value=0)

    RightFootRing4RotateAxis = RightFootRing4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootRing4RotateAxisx = RightFootRing4RotateAxis.RightFootRing4RotateAxisx
    RightFootRing4RotateAxisy = RightFootRing4RotateAxis.RightFootRing4RotateAxisy
    RightFootRing4RotateAxisz = RightFootRing4RotateAxis.RightFootRing4RotateAxisz

    RightFootRing4JointOrient = RightFootRing4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootRing4JointOrientx = RightFootRing4JointOrient.RightFootRing4JointOrientx
    RightFootRing4JointOrienty = RightFootRing4JointOrient.RightFootRing4JointOrienty
    RightFootRing4JointOrientz = RightFootRing4JointOrient.RightFootRing4JointOrientz

    RightFootRing4MinRLimit = RightFootRing4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootRing4MinRLimitx = RightFootRing4MinRLimit.RightFootRing4MinRLimitx
    RightFootRing4MinRLimity = RightFootRing4MinRLimit.RightFootRing4MinRLimity
    RightFootRing4MinRLimitz = RightFootRing4MinRLimit.RightFootRing4MinRLimitz

    RightFootRing4MaxRLimit = RightFootRing4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootRing4MaxRLimitx = RightFootRing4MaxRLimit.RightFootRing4MaxRLimitx
    RightFootRing4MaxRLimity = RightFootRing4MaxRLimit.RightFootRing4MaxRLimity
    RightFootRing4MaxRLimitz = RightFootRing4MaxRLimit.RightFootRing4MaxRLimitz

    RightFootRing4MinRLimitEnablex = BoolField(default_value=False)

    RightFootRing4MinRLimitEnabley = BoolField(default_value=False)

    RightFootRing4MinRLimitEnablez = BoolField(default_value=False)

    RightFootRing4MaxRLimitEnablex = BoolField(default_value=False)

    RightFootRing4MaxRLimitEnabley = BoolField(default_value=False)

    RightFootRing4MaxRLimitEnablez = BoolField(default_value=False)

    RightFootPinky1 = MessageField()

    RightFootPinky1T = RightFootPinky1TField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky1Tx = RightFootPinky1T.RightFootPinky1Tx
    RightFootPinky1Ty = RightFootPinky1T.RightFootPinky1Ty
    RightFootPinky1Tz = RightFootPinky1T.RightFootPinky1Tz

    RightFootPinky1R = RightFootPinky1RField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky1Rx = RightFootPinky1R.RightFootPinky1Rx
    RightFootPinky1Ry = RightFootPinky1R.RightFootPinky1Ry
    RightFootPinky1Rz = RightFootPinky1R.RightFootPinky1Rz

    RightFootPinky1S = RightFootPinky1SField(default_value=(1.0, 1.0, 1.0))
    RightFootPinky1Sx = RightFootPinky1S.RightFootPinky1Sx
    RightFootPinky1Sy = RightFootPinky1S.RightFootPinky1Sy
    RightFootPinky1Sz = RightFootPinky1S.RightFootPinky1Sz

    RightFootPinky1RotateOrder = RightFootPinky1RotateOrderEnumField(default_value=0)

    RightFootPinky1RotateAxis = RightFootPinky1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky1RotateAxisx = RightFootPinky1RotateAxis.RightFootPinky1RotateAxisx
    RightFootPinky1RotateAxisy = RightFootPinky1RotateAxis.RightFootPinky1RotateAxisy
    RightFootPinky1RotateAxisz = RightFootPinky1RotateAxis.RightFootPinky1RotateAxisz

    RightFootPinky1JointOrient = RightFootPinky1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky1JointOrientx = RightFootPinky1JointOrient.RightFootPinky1JointOrientx
    RightFootPinky1JointOrienty = RightFootPinky1JointOrient.RightFootPinky1JointOrienty
    RightFootPinky1JointOrientz = RightFootPinky1JointOrient.RightFootPinky1JointOrientz

    RightFootPinky1MinRLimit = RightFootPinky1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky1MinRLimitx = RightFootPinky1MinRLimit.RightFootPinky1MinRLimitx
    RightFootPinky1MinRLimity = RightFootPinky1MinRLimit.RightFootPinky1MinRLimity
    RightFootPinky1MinRLimitz = RightFootPinky1MinRLimit.RightFootPinky1MinRLimitz

    RightFootPinky1MaxRLimit = RightFootPinky1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky1MaxRLimitx = RightFootPinky1MaxRLimit.RightFootPinky1MaxRLimitx
    RightFootPinky1MaxRLimity = RightFootPinky1MaxRLimit.RightFootPinky1MaxRLimity
    RightFootPinky1MaxRLimitz = RightFootPinky1MaxRLimit.RightFootPinky1MaxRLimitz

    RightFootPinky1MinRLimitEnablex = BoolField(default_value=False)

    RightFootPinky1MinRLimitEnabley = BoolField(default_value=False)

    RightFootPinky1MinRLimitEnablez = BoolField(default_value=False)

    RightFootPinky1MaxRLimitEnablex = BoolField(default_value=False)

    RightFootPinky1MaxRLimitEnabley = BoolField(default_value=False)

    RightFootPinky1MaxRLimitEnablez = BoolField(default_value=False)

    RightFootPinky2 = MessageField()

    RightFootPinky2T = RightFootPinky2TField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky2Tx = RightFootPinky2T.RightFootPinky2Tx
    RightFootPinky2Ty = RightFootPinky2T.RightFootPinky2Ty
    RightFootPinky2Tz = RightFootPinky2T.RightFootPinky2Tz

    RightFootPinky2R = RightFootPinky2RField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky2Rx = RightFootPinky2R.RightFootPinky2Rx
    RightFootPinky2Ry = RightFootPinky2R.RightFootPinky2Ry
    RightFootPinky2Rz = RightFootPinky2R.RightFootPinky2Rz

    RightFootPinky2S = RightFootPinky2SField(default_value=(1.0, 1.0, 1.0))
    RightFootPinky2Sx = RightFootPinky2S.RightFootPinky2Sx
    RightFootPinky2Sy = RightFootPinky2S.RightFootPinky2Sy
    RightFootPinky2Sz = RightFootPinky2S.RightFootPinky2Sz

    RightFootPinky2RotateOrder = RightFootPinky2RotateOrderEnumField(default_value=0)

    RightFootPinky2RotateAxis = RightFootPinky2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky2RotateAxisx = RightFootPinky2RotateAxis.RightFootPinky2RotateAxisx
    RightFootPinky2RotateAxisy = RightFootPinky2RotateAxis.RightFootPinky2RotateAxisy
    RightFootPinky2RotateAxisz = RightFootPinky2RotateAxis.RightFootPinky2RotateAxisz

    RightFootPinky2JointOrient = RightFootPinky2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky2JointOrientx = RightFootPinky2JointOrient.RightFootPinky2JointOrientx
    RightFootPinky2JointOrienty = RightFootPinky2JointOrient.RightFootPinky2JointOrienty
    RightFootPinky2JointOrientz = RightFootPinky2JointOrient.RightFootPinky2JointOrientz

    RightFootPinky2MinRLimit = RightFootPinky2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky2MinRLimitx = RightFootPinky2MinRLimit.RightFootPinky2MinRLimitx
    RightFootPinky2MinRLimity = RightFootPinky2MinRLimit.RightFootPinky2MinRLimity
    RightFootPinky2MinRLimitz = RightFootPinky2MinRLimit.RightFootPinky2MinRLimitz

    RightFootPinky2MaxRLimit = RightFootPinky2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky2MaxRLimitx = RightFootPinky2MaxRLimit.RightFootPinky2MaxRLimitx
    RightFootPinky2MaxRLimity = RightFootPinky2MaxRLimit.RightFootPinky2MaxRLimity
    RightFootPinky2MaxRLimitz = RightFootPinky2MaxRLimit.RightFootPinky2MaxRLimitz

    RightFootPinky2MinRLimitEnablex = BoolField(default_value=False)

    RightFootPinky2MinRLimitEnabley = BoolField(default_value=False)

    RightFootPinky2MinRLimitEnablez = BoolField(default_value=False)

    RightFootPinky2MaxRLimitEnablex = BoolField(default_value=False)

    RightFootPinky2MaxRLimitEnabley = BoolField(default_value=False)

    RightFootPinky2MaxRLimitEnablez = BoolField(default_value=False)

    RightFootPinky3 = MessageField()

    RightFootPinky3T = RightFootPinky3TField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky3Tx = RightFootPinky3T.RightFootPinky3Tx
    RightFootPinky3Ty = RightFootPinky3T.RightFootPinky3Ty
    RightFootPinky3Tz = RightFootPinky3T.RightFootPinky3Tz

    RightFootPinky3R = RightFootPinky3RField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky3Rx = RightFootPinky3R.RightFootPinky3Rx
    RightFootPinky3Ry = RightFootPinky3R.RightFootPinky3Ry
    RightFootPinky3Rz = RightFootPinky3R.RightFootPinky3Rz

    RightFootPinky3S = RightFootPinky3SField(default_value=(1.0, 1.0, 1.0))
    RightFootPinky3Sx = RightFootPinky3S.RightFootPinky3Sx
    RightFootPinky3Sy = RightFootPinky3S.RightFootPinky3Sy
    RightFootPinky3Sz = RightFootPinky3S.RightFootPinky3Sz

    RightFootPinky3RotateOrder = RightFootPinky3RotateOrderEnumField(default_value=0)

    RightFootPinky3RotateAxis = RightFootPinky3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky3RotateAxisx = RightFootPinky3RotateAxis.RightFootPinky3RotateAxisx
    RightFootPinky3RotateAxisy = RightFootPinky3RotateAxis.RightFootPinky3RotateAxisy
    RightFootPinky3RotateAxisz = RightFootPinky3RotateAxis.RightFootPinky3RotateAxisz

    RightFootPinky3JointOrient = RightFootPinky3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky3JointOrientx = RightFootPinky3JointOrient.RightFootPinky3JointOrientx
    RightFootPinky3JointOrienty = RightFootPinky3JointOrient.RightFootPinky3JointOrienty
    RightFootPinky3JointOrientz = RightFootPinky3JointOrient.RightFootPinky3JointOrientz

    RightFootPinky3MinRLimit = RightFootPinky3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky3MinRLimitx = RightFootPinky3MinRLimit.RightFootPinky3MinRLimitx
    RightFootPinky3MinRLimity = RightFootPinky3MinRLimit.RightFootPinky3MinRLimity
    RightFootPinky3MinRLimitz = RightFootPinky3MinRLimit.RightFootPinky3MinRLimitz

    RightFootPinky3MaxRLimit = RightFootPinky3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky3MaxRLimitx = RightFootPinky3MaxRLimit.RightFootPinky3MaxRLimitx
    RightFootPinky3MaxRLimity = RightFootPinky3MaxRLimit.RightFootPinky3MaxRLimity
    RightFootPinky3MaxRLimitz = RightFootPinky3MaxRLimit.RightFootPinky3MaxRLimitz

    RightFootPinky3MinRLimitEnablex = BoolField(default_value=False)

    RightFootPinky3MinRLimitEnabley = BoolField(default_value=False)

    RightFootPinky3MinRLimitEnablez = BoolField(default_value=False)

    RightFootPinky3MaxRLimitEnablex = BoolField(default_value=False)

    RightFootPinky3MaxRLimitEnabley = BoolField(default_value=False)

    RightFootPinky3MaxRLimitEnablez = BoolField(default_value=False)

    RightFootPinky4 = MessageField()

    RightFootPinky4T = RightFootPinky4TField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky4Tx = RightFootPinky4T.RightFootPinky4Tx
    RightFootPinky4Ty = RightFootPinky4T.RightFootPinky4Ty
    RightFootPinky4Tz = RightFootPinky4T.RightFootPinky4Tz

    RightFootPinky4R = RightFootPinky4RField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky4Rx = RightFootPinky4R.RightFootPinky4Rx
    RightFootPinky4Ry = RightFootPinky4R.RightFootPinky4Ry
    RightFootPinky4Rz = RightFootPinky4R.RightFootPinky4Rz

    RightFootPinky4S = RightFootPinky4SField(default_value=(1.0, 1.0, 1.0))
    RightFootPinky4Sx = RightFootPinky4S.RightFootPinky4Sx
    RightFootPinky4Sy = RightFootPinky4S.RightFootPinky4Sy
    RightFootPinky4Sz = RightFootPinky4S.RightFootPinky4Sz

    RightFootPinky4RotateOrder = RightFootPinky4RotateOrderEnumField(default_value=0)

    RightFootPinky4RotateAxis = RightFootPinky4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky4RotateAxisx = RightFootPinky4RotateAxis.RightFootPinky4RotateAxisx
    RightFootPinky4RotateAxisy = RightFootPinky4RotateAxis.RightFootPinky4RotateAxisy
    RightFootPinky4RotateAxisz = RightFootPinky4RotateAxis.RightFootPinky4RotateAxisz

    RightFootPinky4JointOrient = RightFootPinky4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky4JointOrientx = RightFootPinky4JointOrient.RightFootPinky4JointOrientx
    RightFootPinky4JointOrienty = RightFootPinky4JointOrient.RightFootPinky4JointOrienty
    RightFootPinky4JointOrientz = RightFootPinky4JointOrient.RightFootPinky4JointOrientz

    RightFootPinky4MinRLimit = RightFootPinky4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky4MinRLimitx = RightFootPinky4MinRLimit.RightFootPinky4MinRLimitx
    RightFootPinky4MinRLimity = RightFootPinky4MinRLimit.RightFootPinky4MinRLimity
    RightFootPinky4MinRLimitz = RightFootPinky4MinRLimit.RightFootPinky4MinRLimitz

    RightFootPinky4MaxRLimit = RightFootPinky4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky4MaxRLimitx = RightFootPinky4MaxRLimit.RightFootPinky4MaxRLimitx
    RightFootPinky4MaxRLimity = RightFootPinky4MaxRLimit.RightFootPinky4MaxRLimity
    RightFootPinky4MaxRLimitz = RightFootPinky4MaxRLimit.RightFootPinky4MaxRLimitz

    RightFootPinky4MinRLimitEnablex = BoolField(default_value=False)

    RightFootPinky4MinRLimitEnabley = BoolField(default_value=False)

    RightFootPinky4MinRLimitEnablez = BoolField(default_value=False)

    RightFootPinky4MaxRLimitEnablex = BoolField(default_value=False)

    RightFootPinky4MaxRLimitEnabley = BoolField(default_value=False)

    RightFootPinky4MaxRLimitEnablez = BoolField(default_value=False)

    RightFootExtraFinger1 = MessageField()

    RightFootExtraFinger1T = RightFootExtraFinger1TField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger1Tx = RightFootExtraFinger1T.RightFootExtraFinger1Tx
    RightFootExtraFinger1Ty = RightFootExtraFinger1T.RightFootExtraFinger1Ty
    RightFootExtraFinger1Tz = RightFootExtraFinger1T.RightFootExtraFinger1Tz

    RightFootExtraFinger1R = RightFootExtraFinger1RField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger1Rx = RightFootExtraFinger1R.RightFootExtraFinger1Rx
    RightFootExtraFinger1Ry = RightFootExtraFinger1R.RightFootExtraFinger1Ry
    RightFootExtraFinger1Rz = RightFootExtraFinger1R.RightFootExtraFinger1Rz

    RightFootExtraFinger1S = RightFootExtraFinger1SField(default_value=(1.0, 1.0, 1.0))
    RightFootExtraFinger1Sx = RightFootExtraFinger1S.RightFootExtraFinger1Sx
    RightFootExtraFinger1Sy = RightFootExtraFinger1S.RightFootExtraFinger1Sy
    RightFootExtraFinger1Sz = RightFootExtraFinger1S.RightFootExtraFinger1Sz

    RightFootExtraFinger1RotateOrder = RightFootExtraFinger1RotateOrderEnumField(default_value=0)

    RightFootExtraFinger1RotateAxis = RightFootExtraFinger1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger1RotateAxisx = RightFootExtraFinger1RotateAxis.RightFootExtraFinger1RotateAxisx
    RightFootExtraFinger1RotateAxisy = RightFootExtraFinger1RotateAxis.RightFootExtraFinger1RotateAxisy
    RightFootExtraFinger1RotateAxisz = RightFootExtraFinger1RotateAxis.RightFootExtraFinger1RotateAxisz

    RightFootExtraFinger1JointOrient = RightFootExtraFinger1JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger1JointOrientx = RightFootExtraFinger1JointOrient.RightFootExtraFinger1JointOrientx
    RightFootExtraFinger1JointOrienty = RightFootExtraFinger1JointOrient.RightFootExtraFinger1JointOrienty
    RightFootExtraFinger1JointOrientz = RightFootExtraFinger1JointOrient.RightFootExtraFinger1JointOrientz

    RightFootExtraFinger1MinRLimit = RightFootExtraFinger1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger1MinRLimitx = RightFootExtraFinger1MinRLimit.RightFootExtraFinger1MinRLimitx
    RightFootExtraFinger1MinRLimity = RightFootExtraFinger1MinRLimit.RightFootExtraFinger1MinRLimity
    RightFootExtraFinger1MinRLimitz = RightFootExtraFinger1MinRLimit.RightFootExtraFinger1MinRLimitz

    RightFootExtraFinger1MaxRLimit = RightFootExtraFinger1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger1MaxRLimitx = RightFootExtraFinger1MaxRLimit.RightFootExtraFinger1MaxRLimitx
    RightFootExtraFinger1MaxRLimity = RightFootExtraFinger1MaxRLimit.RightFootExtraFinger1MaxRLimity
    RightFootExtraFinger1MaxRLimitz = RightFootExtraFinger1MaxRLimit.RightFootExtraFinger1MaxRLimitz

    RightFootExtraFinger1MinRLimitEnablex = BoolField(default_value=False)

    RightFootExtraFinger1MinRLimitEnabley = BoolField(default_value=False)

    RightFootExtraFinger1MinRLimitEnablez = BoolField(default_value=False)

    RightFootExtraFinger1MaxRLimitEnablex = BoolField(default_value=False)

    RightFootExtraFinger1MaxRLimitEnabley = BoolField(default_value=False)

    RightFootExtraFinger1MaxRLimitEnablez = BoolField(default_value=False)

    RightFootExtraFinger2 = MessageField()

    RightFootExtraFinger2T = RightFootExtraFinger2TField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger2Tx = RightFootExtraFinger2T.RightFootExtraFinger2Tx
    RightFootExtraFinger2Ty = RightFootExtraFinger2T.RightFootExtraFinger2Ty
    RightFootExtraFinger2Tz = RightFootExtraFinger2T.RightFootExtraFinger2Tz

    RightFootExtraFinger2R = RightFootExtraFinger2RField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger2Rx = RightFootExtraFinger2R.RightFootExtraFinger2Rx
    RightFootExtraFinger2Ry = RightFootExtraFinger2R.RightFootExtraFinger2Ry
    RightFootExtraFinger2Rz = RightFootExtraFinger2R.RightFootExtraFinger2Rz

    RightFootExtraFinger2S = RightFootExtraFinger2SField(default_value=(1.0, 1.0, 1.0))
    RightFootExtraFinger2Sx = RightFootExtraFinger2S.RightFootExtraFinger2Sx
    RightFootExtraFinger2Sy = RightFootExtraFinger2S.RightFootExtraFinger2Sy
    RightFootExtraFinger2Sz = RightFootExtraFinger2S.RightFootExtraFinger2Sz

    RightFootExtraFinger2RotateOrder = RightFootExtraFinger2RotateOrderEnumField(default_value=0)

    RightFootExtraFinger2RotateAxis = RightFootExtraFinger2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger2RotateAxisx = RightFootExtraFinger2RotateAxis.RightFootExtraFinger2RotateAxisx
    RightFootExtraFinger2RotateAxisy = RightFootExtraFinger2RotateAxis.RightFootExtraFinger2RotateAxisy
    RightFootExtraFinger2RotateAxisz = RightFootExtraFinger2RotateAxis.RightFootExtraFinger2RotateAxisz

    RightFootExtraFinger2JointOrient = RightFootExtraFinger2JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger2JointOrientx = RightFootExtraFinger2JointOrient.RightFootExtraFinger2JointOrientx
    RightFootExtraFinger2JointOrienty = RightFootExtraFinger2JointOrient.RightFootExtraFinger2JointOrienty
    RightFootExtraFinger2JointOrientz = RightFootExtraFinger2JointOrient.RightFootExtraFinger2JointOrientz

    RightFootExtraFinger2MinRLimit = RightFootExtraFinger2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger2MinRLimitx = RightFootExtraFinger2MinRLimit.RightFootExtraFinger2MinRLimitx
    RightFootExtraFinger2MinRLimity = RightFootExtraFinger2MinRLimit.RightFootExtraFinger2MinRLimity
    RightFootExtraFinger2MinRLimitz = RightFootExtraFinger2MinRLimit.RightFootExtraFinger2MinRLimitz

    RightFootExtraFinger2MaxRLimit = RightFootExtraFinger2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger2MaxRLimitx = RightFootExtraFinger2MaxRLimit.RightFootExtraFinger2MaxRLimitx
    RightFootExtraFinger2MaxRLimity = RightFootExtraFinger2MaxRLimit.RightFootExtraFinger2MaxRLimity
    RightFootExtraFinger2MaxRLimitz = RightFootExtraFinger2MaxRLimit.RightFootExtraFinger2MaxRLimitz

    RightFootExtraFinger2MinRLimitEnablex = BoolField(default_value=False)

    RightFootExtraFinger2MinRLimitEnabley = BoolField(default_value=False)

    RightFootExtraFinger2MinRLimitEnablez = BoolField(default_value=False)

    RightFootExtraFinger2MaxRLimitEnablex = BoolField(default_value=False)

    RightFootExtraFinger2MaxRLimitEnabley = BoolField(default_value=False)

    RightFootExtraFinger2MaxRLimitEnablez = BoolField(default_value=False)

    RightFootExtraFinger3 = MessageField()

    RightFootExtraFinger3T = RightFootExtraFinger3TField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger3Tx = RightFootExtraFinger3T.RightFootExtraFinger3Tx
    RightFootExtraFinger3Ty = RightFootExtraFinger3T.RightFootExtraFinger3Ty
    RightFootExtraFinger3Tz = RightFootExtraFinger3T.RightFootExtraFinger3Tz

    RightFootExtraFinger3R = RightFootExtraFinger3RField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger3Rx = RightFootExtraFinger3R.RightFootExtraFinger3Rx
    RightFootExtraFinger3Ry = RightFootExtraFinger3R.RightFootExtraFinger3Ry
    RightFootExtraFinger3Rz = RightFootExtraFinger3R.RightFootExtraFinger3Rz

    RightFootExtraFinger3S = RightFootExtraFinger3SField(default_value=(1.0, 1.0, 1.0))
    RightFootExtraFinger3Sx = RightFootExtraFinger3S.RightFootExtraFinger3Sx
    RightFootExtraFinger3Sy = RightFootExtraFinger3S.RightFootExtraFinger3Sy
    RightFootExtraFinger3Sz = RightFootExtraFinger3S.RightFootExtraFinger3Sz

    RightFootExtraFinger3RotateOrder = RightFootExtraFinger3RotateOrderEnumField(default_value=0)

    RightFootExtraFinger3RotateAxis = RightFootExtraFinger3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger3RotateAxisx = RightFootExtraFinger3RotateAxis.RightFootExtraFinger3RotateAxisx
    RightFootExtraFinger3RotateAxisy = RightFootExtraFinger3RotateAxis.RightFootExtraFinger3RotateAxisy
    RightFootExtraFinger3RotateAxisz = RightFootExtraFinger3RotateAxis.RightFootExtraFinger3RotateAxisz

    RightFootExtraFinger3JointOrient = RightFootExtraFinger3JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger3JointOrientx = RightFootExtraFinger3JointOrient.RightFootExtraFinger3JointOrientx
    RightFootExtraFinger3JointOrienty = RightFootExtraFinger3JointOrient.RightFootExtraFinger3JointOrienty
    RightFootExtraFinger3JointOrientz = RightFootExtraFinger3JointOrient.RightFootExtraFinger3JointOrientz

    RightFootExtraFinger3MinRLimit = RightFootExtraFinger3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger3MinRLimitx = RightFootExtraFinger3MinRLimit.RightFootExtraFinger3MinRLimitx
    RightFootExtraFinger3MinRLimity = RightFootExtraFinger3MinRLimit.RightFootExtraFinger3MinRLimity
    RightFootExtraFinger3MinRLimitz = RightFootExtraFinger3MinRLimit.RightFootExtraFinger3MinRLimitz

    RightFootExtraFinger3MaxRLimit = RightFootExtraFinger3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger3MaxRLimitx = RightFootExtraFinger3MaxRLimit.RightFootExtraFinger3MaxRLimitx
    RightFootExtraFinger3MaxRLimity = RightFootExtraFinger3MaxRLimit.RightFootExtraFinger3MaxRLimity
    RightFootExtraFinger3MaxRLimitz = RightFootExtraFinger3MaxRLimit.RightFootExtraFinger3MaxRLimitz

    RightFootExtraFinger3MinRLimitEnablex = BoolField(default_value=False)

    RightFootExtraFinger3MinRLimitEnabley = BoolField(default_value=False)

    RightFootExtraFinger3MinRLimitEnablez = BoolField(default_value=False)

    RightFootExtraFinger3MaxRLimitEnablex = BoolField(default_value=False)

    RightFootExtraFinger3MaxRLimitEnabley = BoolField(default_value=False)

    RightFootExtraFinger3MaxRLimitEnablez = BoolField(default_value=False)

    RightFootExtraFinger4 = MessageField()

    RightFootExtraFinger4T = RightFootExtraFinger4TField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger4Tx = RightFootExtraFinger4T.RightFootExtraFinger4Tx
    RightFootExtraFinger4Ty = RightFootExtraFinger4T.RightFootExtraFinger4Ty
    RightFootExtraFinger4Tz = RightFootExtraFinger4T.RightFootExtraFinger4Tz

    RightFootExtraFinger4R = RightFootExtraFinger4RField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger4Rx = RightFootExtraFinger4R.RightFootExtraFinger4Rx
    RightFootExtraFinger4Ry = RightFootExtraFinger4R.RightFootExtraFinger4Ry
    RightFootExtraFinger4Rz = RightFootExtraFinger4R.RightFootExtraFinger4Rz

    RightFootExtraFinger4S = RightFootExtraFinger4SField(default_value=(1.0, 1.0, 1.0))
    RightFootExtraFinger4Sx = RightFootExtraFinger4S.RightFootExtraFinger4Sx
    RightFootExtraFinger4Sy = RightFootExtraFinger4S.RightFootExtraFinger4Sy
    RightFootExtraFinger4Sz = RightFootExtraFinger4S.RightFootExtraFinger4Sz

    RightFootExtraFinger4RotateOrder = RightFootExtraFinger4RotateOrderEnumField(default_value=0)

    RightFootExtraFinger4RotateAxis = RightFootExtraFinger4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger4RotateAxisx = RightFootExtraFinger4RotateAxis.RightFootExtraFinger4RotateAxisx
    RightFootExtraFinger4RotateAxisy = RightFootExtraFinger4RotateAxis.RightFootExtraFinger4RotateAxisy
    RightFootExtraFinger4RotateAxisz = RightFootExtraFinger4RotateAxis.RightFootExtraFinger4RotateAxisz

    RightFootExtraFinger4JointOrient = RightFootExtraFinger4JointOrientField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger4JointOrientx = RightFootExtraFinger4JointOrient.RightFootExtraFinger4JointOrientx
    RightFootExtraFinger4JointOrienty = RightFootExtraFinger4JointOrient.RightFootExtraFinger4JointOrienty
    RightFootExtraFinger4JointOrientz = RightFootExtraFinger4JointOrient.RightFootExtraFinger4JointOrientz

    RightFootExtraFinger4MinRLimit = RightFootExtraFinger4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger4MinRLimitx = RightFootExtraFinger4MinRLimit.RightFootExtraFinger4MinRLimitx
    RightFootExtraFinger4MinRLimity = RightFootExtraFinger4MinRLimit.RightFootExtraFinger4MinRLimity
    RightFootExtraFinger4MinRLimitz = RightFootExtraFinger4MinRLimit.RightFootExtraFinger4MinRLimitz

    RightFootExtraFinger4MaxRLimit = RightFootExtraFinger4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger4MaxRLimitx = RightFootExtraFinger4MaxRLimit.RightFootExtraFinger4MaxRLimitx
    RightFootExtraFinger4MaxRLimity = RightFootExtraFinger4MaxRLimit.RightFootExtraFinger4MaxRLimity
    RightFootExtraFinger4MaxRLimitz = RightFootExtraFinger4MaxRLimit.RightFootExtraFinger4MaxRLimitz

    RightFootExtraFinger4MinRLimitEnablex = BoolField(default_value=False)

    RightFootExtraFinger4MinRLimitEnabley = BoolField(default_value=False)

    RightFootExtraFinger4MinRLimitEnablez = BoolField(default_value=False)

    RightFootExtraFinger4MaxRLimitEnablex = BoolField(default_value=False)

    RightFootExtraFinger4MaxRLimitEnabley = BoolField(default_value=False)

    RightFootExtraFinger4MaxRLimitEnablez = BoolField(default_value=False)

    LeftInHandThumb = MessageField()

    LeftInHandThumbT = LeftInHandThumbTField(default_value=(0.0, 0.0, 0.0))
    LeftInHandThumbTx = LeftInHandThumbT.LeftInHandThumbTx
    LeftInHandThumbTy = LeftInHandThumbT.LeftInHandThumbTy
    LeftInHandThumbTz = LeftInHandThumbT.LeftInHandThumbTz

    LeftInHandThumbR = LeftInHandThumbRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandThumbRx = LeftInHandThumbR.LeftInHandThumbRx
    LeftInHandThumbRy = LeftInHandThumbR.LeftInHandThumbRy
    LeftInHandThumbRz = LeftInHandThumbR.LeftInHandThumbRz

    LeftInHandThumbS = LeftInHandThumbSField(default_value=(1.0, 1.0, 1.0))
    LeftInHandThumbSx = LeftInHandThumbS.LeftInHandThumbSx
    LeftInHandThumbSy = LeftInHandThumbS.LeftInHandThumbSy
    LeftInHandThumbSz = LeftInHandThumbS.LeftInHandThumbSz

    LeftInHandThumbRotateOrder = LeftInHandThumbRotateOrderEnumField(default_value=0)

    LeftInHandThumbRotateAxis = LeftInHandThumbRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInHandThumbRotateAxisx = LeftInHandThumbRotateAxis.LeftInHandThumbRotateAxisx
    LeftInHandThumbRotateAxisy = LeftInHandThumbRotateAxis.LeftInHandThumbRotateAxisy
    LeftInHandThumbRotateAxisz = LeftInHandThumbRotateAxis.LeftInHandThumbRotateAxisz

    LeftInHandThumbJointOrient = LeftInHandThumbJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInHandThumbJointOrientx = LeftInHandThumbJointOrient.LeftInHandThumbJointOrientx
    LeftInHandThumbJointOrienty = LeftInHandThumbJointOrient.LeftInHandThumbJointOrienty
    LeftInHandThumbJointOrientz = LeftInHandThumbJointOrient.LeftInHandThumbJointOrientz

    LeftInHandThumbMinRLimit = LeftInHandThumbMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandThumbMinRLimitx = LeftInHandThumbMinRLimit.LeftInHandThumbMinRLimitx
    LeftInHandThumbMinRLimity = LeftInHandThumbMinRLimit.LeftInHandThumbMinRLimity
    LeftInHandThumbMinRLimitz = LeftInHandThumbMinRLimit.LeftInHandThumbMinRLimitz

    LeftInHandThumbMaxRLimit = LeftInHandThumbMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandThumbMaxRLimitx = LeftInHandThumbMaxRLimit.LeftInHandThumbMaxRLimitx
    LeftInHandThumbMaxRLimity = LeftInHandThumbMaxRLimit.LeftInHandThumbMaxRLimity
    LeftInHandThumbMaxRLimitz = LeftInHandThumbMaxRLimit.LeftInHandThumbMaxRLimitz

    LeftInHandThumbMinRLimitEnablex = BoolField(default_value=False)

    LeftInHandThumbMinRLimitEnabley = BoolField(default_value=False)

    LeftInHandThumbMinRLimitEnablez = BoolField(default_value=False)

    LeftInHandThumbMaxRLimitEnablex = BoolField(default_value=False)

    LeftInHandThumbMaxRLimitEnabley = BoolField(default_value=False)

    LeftInHandThumbMaxRLimitEnablez = BoolField(default_value=False)

    LeftInHandIndex = MessageField()

    LeftInHandIndexT = LeftInHandIndexTField(default_value=(0.0, 0.0, 0.0))
    LeftInHandIndexTx = LeftInHandIndexT.LeftInHandIndexTx
    LeftInHandIndexTy = LeftInHandIndexT.LeftInHandIndexTy
    LeftInHandIndexTz = LeftInHandIndexT.LeftInHandIndexTz

    LeftInHandIndexR = LeftInHandIndexRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandIndexRx = LeftInHandIndexR.LeftInHandIndexRx
    LeftInHandIndexRy = LeftInHandIndexR.LeftInHandIndexRy
    LeftInHandIndexRz = LeftInHandIndexR.LeftInHandIndexRz

    LeftInHandIndexS = LeftInHandIndexSField(default_value=(1.0, 1.0, 1.0))
    LeftInHandIndexSx = LeftInHandIndexS.LeftInHandIndexSx
    LeftInHandIndexSy = LeftInHandIndexS.LeftInHandIndexSy
    LeftInHandIndexSz = LeftInHandIndexS.LeftInHandIndexSz

    LeftInHandIndexRotateOrder = LeftInHandIndexRotateOrderEnumField(default_value=0)

    LeftInHandIndexRotateAxis = LeftInHandIndexRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInHandIndexRotateAxisx = LeftInHandIndexRotateAxis.LeftInHandIndexRotateAxisx
    LeftInHandIndexRotateAxisy = LeftInHandIndexRotateAxis.LeftInHandIndexRotateAxisy
    LeftInHandIndexRotateAxisz = LeftInHandIndexRotateAxis.LeftInHandIndexRotateAxisz

    LeftInHandIndexJointOrient = LeftInHandIndexJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInHandIndexJointOrientx = LeftInHandIndexJointOrient.LeftInHandIndexJointOrientx
    LeftInHandIndexJointOrienty = LeftInHandIndexJointOrient.LeftInHandIndexJointOrienty
    LeftInHandIndexJointOrientz = LeftInHandIndexJointOrient.LeftInHandIndexJointOrientz

    LeftInHandIndexMinRLimit = LeftInHandIndexMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandIndexMinRLimitx = LeftInHandIndexMinRLimit.LeftInHandIndexMinRLimitx
    LeftInHandIndexMinRLimity = LeftInHandIndexMinRLimit.LeftInHandIndexMinRLimity
    LeftInHandIndexMinRLimitz = LeftInHandIndexMinRLimit.LeftInHandIndexMinRLimitz

    LeftInHandIndexMaxRLimit = LeftInHandIndexMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandIndexMaxRLimitx = LeftInHandIndexMaxRLimit.LeftInHandIndexMaxRLimitx
    LeftInHandIndexMaxRLimity = LeftInHandIndexMaxRLimit.LeftInHandIndexMaxRLimity
    LeftInHandIndexMaxRLimitz = LeftInHandIndexMaxRLimit.LeftInHandIndexMaxRLimitz

    LeftInHandIndexMinRLimitEnablex = BoolField(default_value=False)

    LeftInHandIndexMinRLimitEnabley = BoolField(default_value=False)

    LeftInHandIndexMinRLimitEnablez = BoolField(default_value=False)

    LeftInHandIndexMaxRLimitEnablex = BoolField(default_value=False)

    LeftInHandIndexMaxRLimitEnabley = BoolField(default_value=False)

    LeftInHandIndexMaxRLimitEnablez = BoolField(default_value=False)

    LeftInHandMiddle = MessageField()

    LeftInHandMiddleT = LeftInHandMiddleTField(default_value=(0.0, 0.0, 0.0))
    LeftInHandMiddleTx = LeftInHandMiddleT.LeftInHandMiddleTx
    LeftInHandMiddleTy = LeftInHandMiddleT.LeftInHandMiddleTy
    LeftInHandMiddleTz = LeftInHandMiddleT.LeftInHandMiddleTz

    LeftInHandMiddleR = LeftInHandMiddleRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandMiddleRx = LeftInHandMiddleR.LeftInHandMiddleRx
    LeftInHandMiddleRy = LeftInHandMiddleR.LeftInHandMiddleRy
    LeftInHandMiddleRz = LeftInHandMiddleR.LeftInHandMiddleRz

    LeftInHandMiddleS = LeftInHandMiddleSField(default_value=(1.0, 1.0, 1.0))
    LeftInHandMiddleSx = LeftInHandMiddleS.LeftInHandMiddleSx
    LeftInHandMiddleSy = LeftInHandMiddleS.LeftInHandMiddleSy
    LeftInHandMiddleSz = LeftInHandMiddleS.LeftInHandMiddleSz

    LeftInHandMiddleRotateOrder = LeftInHandMiddleRotateOrderEnumField(default_value=0)

    LeftInHandMiddleRotateAxis = LeftInHandMiddleRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInHandMiddleRotateAxisx = LeftInHandMiddleRotateAxis.LeftInHandMiddleRotateAxisx
    LeftInHandMiddleRotateAxisy = LeftInHandMiddleRotateAxis.LeftInHandMiddleRotateAxisy
    LeftInHandMiddleRotateAxisz = LeftInHandMiddleRotateAxis.LeftInHandMiddleRotateAxisz

    LeftInHandMiddleJointOrient = LeftInHandMiddleJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInHandMiddleJointOrientx = LeftInHandMiddleJointOrient.LeftInHandMiddleJointOrientx
    LeftInHandMiddleJointOrienty = LeftInHandMiddleJointOrient.LeftInHandMiddleJointOrienty
    LeftInHandMiddleJointOrientz = LeftInHandMiddleJointOrient.LeftInHandMiddleJointOrientz

    LeftInHandMiddleMinRLimit = LeftInHandMiddleMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandMiddleMinRLimitx = LeftInHandMiddleMinRLimit.LeftInHandMiddleMinRLimitx
    LeftInHandMiddleMinRLimity = LeftInHandMiddleMinRLimit.LeftInHandMiddleMinRLimity
    LeftInHandMiddleMinRLimitz = LeftInHandMiddleMinRLimit.LeftInHandMiddleMinRLimitz

    LeftInHandMiddleMaxRLimit = LeftInHandMiddleMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandMiddleMaxRLimitx = LeftInHandMiddleMaxRLimit.LeftInHandMiddleMaxRLimitx
    LeftInHandMiddleMaxRLimity = LeftInHandMiddleMaxRLimit.LeftInHandMiddleMaxRLimity
    LeftInHandMiddleMaxRLimitz = LeftInHandMiddleMaxRLimit.LeftInHandMiddleMaxRLimitz

    LeftInHandMiddleMinRLimitEnablex = BoolField(default_value=False)

    LeftInHandMiddleMinRLimitEnabley = BoolField(default_value=False)

    LeftInHandMiddleMinRLimitEnablez = BoolField(default_value=False)

    LeftInHandMiddleMaxRLimitEnablex = BoolField(default_value=False)

    LeftInHandMiddleMaxRLimitEnabley = BoolField(default_value=False)

    LeftInHandMiddleMaxRLimitEnablez = BoolField(default_value=False)

    LeftInHandRing = MessageField()

    LeftInHandRingT = LeftInHandRingTField(default_value=(0.0, 0.0, 0.0))
    LeftInHandRingTx = LeftInHandRingT.LeftInHandRingTx
    LeftInHandRingTy = LeftInHandRingT.LeftInHandRingTy
    LeftInHandRingTz = LeftInHandRingT.LeftInHandRingTz

    LeftInHandRingR = LeftInHandRingRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandRingRx = LeftInHandRingR.LeftInHandRingRx
    LeftInHandRingRy = LeftInHandRingR.LeftInHandRingRy
    LeftInHandRingRz = LeftInHandRingR.LeftInHandRingRz

    LeftInHandRingS = LeftInHandRingSField(default_value=(1.0, 1.0, 1.0))
    LeftInHandRingSx = LeftInHandRingS.LeftInHandRingSx
    LeftInHandRingSy = LeftInHandRingS.LeftInHandRingSy
    LeftInHandRingSz = LeftInHandRingS.LeftInHandRingSz

    LeftInHandRingRotateOrder = LeftInHandRingRotateOrderEnumField(default_value=0)

    LeftInHandRingRotateAxis = LeftInHandRingRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInHandRingRotateAxisx = LeftInHandRingRotateAxis.LeftInHandRingRotateAxisx
    LeftInHandRingRotateAxisy = LeftInHandRingRotateAxis.LeftInHandRingRotateAxisy
    LeftInHandRingRotateAxisz = LeftInHandRingRotateAxis.LeftInHandRingRotateAxisz

    LeftInHandRingJointOrient = LeftInHandRingJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInHandRingJointOrientx = LeftInHandRingJointOrient.LeftInHandRingJointOrientx
    LeftInHandRingJointOrienty = LeftInHandRingJointOrient.LeftInHandRingJointOrienty
    LeftInHandRingJointOrientz = LeftInHandRingJointOrient.LeftInHandRingJointOrientz

    LeftInHandRingMinRLimit = LeftInHandRingMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandRingMinRLimitx = LeftInHandRingMinRLimit.LeftInHandRingMinRLimitx
    LeftInHandRingMinRLimity = LeftInHandRingMinRLimit.LeftInHandRingMinRLimity
    LeftInHandRingMinRLimitz = LeftInHandRingMinRLimit.LeftInHandRingMinRLimitz

    LeftInHandRingMaxRLimit = LeftInHandRingMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandRingMaxRLimitx = LeftInHandRingMaxRLimit.LeftInHandRingMaxRLimitx
    LeftInHandRingMaxRLimity = LeftInHandRingMaxRLimit.LeftInHandRingMaxRLimity
    LeftInHandRingMaxRLimitz = LeftInHandRingMaxRLimit.LeftInHandRingMaxRLimitz

    LeftInHandRingMinRLimitEnablex = BoolField(default_value=False)

    LeftInHandRingMinRLimitEnabley = BoolField(default_value=False)

    LeftInHandRingMinRLimitEnablez = BoolField(default_value=False)

    LeftInHandRingMaxRLimitEnablex = BoolField(default_value=False)

    LeftInHandRingMaxRLimitEnabley = BoolField(default_value=False)

    LeftInHandRingMaxRLimitEnablez = BoolField(default_value=False)

    LeftInHandPinky = MessageField()

    LeftInHandPinkyT = LeftInHandPinkyTField(default_value=(0.0, 0.0, 0.0))
    LeftInHandPinkyTx = LeftInHandPinkyT.LeftInHandPinkyTx
    LeftInHandPinkyTy = LeftInHandPinkyT.LeftInHandPinkyTy
    LeftInHandPinkyTz = LeftInHandPinkyT.LeftInHandPinkyTz

    LeftInHandPinkyR = LeftInHandPinkyRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandPinkyRx = LeftInHandPinkyR.LeftInHandPinkyRx
    LeftInHandPinkyRy = LeftInHandPinkyR.LeftInHandPinkyRy
    LeftInHandPinkyRz = LeftInHandPinkyR.LeftInHandPinkyRz

    LeftInHandPinkyS = LeftInHandPinkySField(default_value=(1.0, 1.0, 1.0))
    LeftInHandPinkySx = LeftInHandPinkyS.LeftInHandPinkySx
    LeftInHandPinkySy = LeftInHandPinkyS.LeftInHandPinkySy
    LeftInHandPinkySz = LeftInHandPinkyS.LeftInHandPinkySz

    LeftInHandPinkyRotateOrder = LeftInHandPinkyRotateOrderEnumField(default_value=0)

    LeftInHandPinkyRotateAxis = LeftInHandPinkyRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInHandPinkyRotateAxisx = LeftInHandPinkyRotateAxis.LeftInHandPinkyRotateAxisx
    LeftInHandPinkyRotateAxisy = LeftInHandPinkyRotateAxis.LeftInHandPinkyRotateAxisy
    LeftInHandPinkyRotateAxisz = LeftInHandPinkyRotateAxis.LeftInHandPinkyRotateAxisz

    LeftInHandPinkyJointOrient = LeftInHandPinkyJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInHandPinkyJointOrientx = LeftInHandPinkyJointOrient.LeftInHandPinkyJointOrientx
    LeftInHandPinkyJointOrienty = LeftInHandPinkyJointOrient.LeftInHandPinkyJointOrienty
    LeftInHandPinkyJointOrientz = LeftInHandPinkyJointOrient.LeftInHandPinkyJointOrientz

    LeftInHandPinkyMinRLimit = LeftInHandPinkyMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandPinkyMinRLimitx = LeftInHandPinkyMinRLimit.LeftInHandPinkyMinRLimitx
    LeftInHandPinkyMinRLimity = LeftInHandPinkyMinRLimit.LeftInHandPinkyMinRLimity
    LeftInHandPinkyMinRLimitz = LeftInHandPinkyMinRLimit.LeftInHandPinkyMinRLimitz

    LeftInHandPinkyMaxRLimit = LeftInHandPinkyMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandPinkyMaxRLimitx = LeftInHandPinkyMaxRLimit.LeftInHandPinkyMaxRLimitx
    LeftInHandPinkyMaxRLimity = LeftInHandPinkyMaxRLimit.LeftInHandPinkyMaxRLimity
    LeftInHandPinkyMaxRLimitz = LeftInHandPinkyMaxRLimit.LeftInHandPinkyMaxRLimitz

    LeftInHandPinkyMinRLimitEnablex = BoolField(default_value=False)

    LeftInHandPinkyMinRLimitEnabley = BoolField(default_value=False)

    LeftInHandPinkyMinRLimitEnablez = BoolField(default_value=False)

    LeftInHandPinkyMaxRLimitEnablex = BoolField(default_value=False)

    LeftInHandPinkyMaxRLimitEnabley = BoolField(default_value=False)

    LeftInHandPinkyMaxRLimitEnablez = BoolField(default_value=False)

    LeftInHandExtraFinger = MessageField()

    LeftInHandExtraFingerT = LeftInHandExtraFingerTField(default_value=(0.0, 0.0, 0.0))
    LeftInHandExtraFingerTx = LeftInHandExtraFingerT.LeftInHandExtraFingerTx
    LeftInHandExtraFingerTy = LeftInHandExtraFingerT.LeftInHandExtraFingerTy
    LeftInHandExtraFingerTz = LeftInHandExtraFingerT.LeftInHandExtraFingerTz

    LeftInHandExtraFingerR = LeftInHandExtraFingerRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandExtraFingerRx = LeftInHandExtraFingerR.LeftInHandExtraFingerRx
    LeftInHandExtraFingerRy = LeftInHandExtraFingerR.LeftInHandExtraFingerRy
    LeftInHandExtraFingerRz = LeftInHandExtraFingerR.LeftInHandExtraFingerRz

    LeftInHandExtraFingerS = LeftInHandExtraFingerSField(default_value=(1.0, 1.0, 1.0))
    LeftInHandExtraFingerSx = LeftInHandExtraFingerS.LeftInHandExtraFingerSx
    LeftInHandExtraFingerSy = LeftInHandExtraFingerS.LeftInHandExtraFingerSy
    LeftInHandExtraFingerSz = LeftInHandExtraFingerS.LeftInHandExtraFingerSz

    LeftInHandExtraFingerRotateOrder = LeftInHandExtraFingerRotateOrderEnumField(default_value=0)

    LeftInHandExtraFingerRotateAxis = LeftInHandExtraFingerRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInHandExtraFingerRotateAxisx = LeftInHandExtraFingerRotateAxis.LeftInHandExtraFingerRotateAxisx
    LeftInHandExtraFingerRotateAxisy = LeftInHandExtraFingerRotateAxis.LeftInHandExtraFingerRotateAxisy
    LeftInHandExtraFingerRotateAxisz = LeftInHandExtraFingerRotateAxis.LeftInHandExtraFingerRotateAxisz

    LeftInHandExtraFingerJointOrient = LeftInHandExtraFingerJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInHandExtraFingerJointOrientx = LeftInHandExtraFingerJointOrient.LeftInHandExtraFingerJointOrientx
    LeftInHandExtraFingerJointOrienty = LeftInHandExtraFingerJointOrient.LeftInHandExtraFingerJointOrienty
    LeftInHandExtraFingerJointOrientz = LeftInHandExtraFingerJointOrient.LeftInHandExtraFingerJointOrientz

    LeftInHandExtraFingerMinRLimit = LeftInHandExtraFingerMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandExtraFingerMinRLimitx = LeftInHandExtraFingerMinRLimit.LeftInHandExtraFingerMinRLimitx
    LeftInHandExtraFingerMinRLimity = LeftInHandExtraFingerMinRLimit.LeftInHandExtraFingerMinRLimity
    LeftInHandExtraFingerMinRLimitz = LeftInHandExtraFingerMinRLimit.LeftInHandExtraFingerMinRLimitz

    LeftInHandExtraFingerMaxRLimit = LeftInHandExtraFingerMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInHandExtraFingerMaxRLimitx = LeftInHandExtraFingerMaxRLimit.LeftInHandExtraFingerMaxRLimitx
    LeftInHandExtraFingerMaxRLimity = LeftInHandExtraFingerMaxRLimit.LeftInHandExtraFingerMaxRLimity
    LeftInHandExtraFingerMaxRLimitz = LeftInHandExtraFingerMaxRLimit.LeftInHandExtraFingerMaxRLimitz

    LeftInHandExtraFingerMinRLimitEnablex = BoolField(default_value=False)

    LeftInHandExtraFingerMinRLimitEnabley = BoolField(default_value=False)

    LeftInHandExtraFingerMinRLimitEnablez = BoolField(default_value=False)

    LeftInHandExtraFingerMaxRLimitEnablex = BoolField(default_value=False)

    LeftInHandExtraFingerMaxRLimitEnabley = BoolField(default_value=False)

    LeftInHandExtraFingerMaxRLimitEnablez = BoolField(default_value=False)

    RightInHandThumb = MessageField()

    RightInHandThumbT = RightInHandThumbTField(default_value=(0.0, 0.0, 0.0))
    RightInHandThumbTx = RightInHandThumbT.RightInHandThumbTx
    RightInHandThumbTy = RightInHandThumbT.RightInHandThumbTy
    RightInHandThumbTz = RightInHandThumbT.RightInHandThumbTz

    RightInHandThumbR = RightInHandThumbRField(default_value=(0.0, 0.0, 0.0))
    RightInHandThumbRx = RightInHandThumbR.RightInHandThumbRx
    RightInHandThumbRy = RightInHandThumbR.RightInHandThumbRy
    RightInHandThumbRz = RightInHandThumbR.RightInHandThumbRz

    RightInHandThumbS = RightInHandThumbSField(default_value=(1.0, 1.0, 1.0))
    RightInHandThumbSx = RightInHandThumbS.RightInHandThumbSx
    RightInHandThumbSy = RightInHandThumbS.RightInHandThumbSy
    RightInHandThumbSz = RightInHandThumbS.RightInHandThumbSz

    RightInHandThumbRotateOrder = RightInHandThumbRotateOrderEnumField(default_value=0)

    RightInHandThumbRotateAxis = RightInHandThumbRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInHandThumbRotateAxisx = RightInHandThumbRotateAxis.RightInHandThumbRotateAxisx
    RightInHandThumbRotateAxisy = RightInHandThumbRotateAxis.RightInHandThumbRotateAxisy
    RightInHandThumbRotateAxisz = RightInHandThumbRotateAxis.RightInHandThumbRotateAxisz

    RightInHandThumbJointOrient = RightInHandThumbJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInHandThumbJointOrientx = RightInHandThumbJointOrient.RightInHandThumbJointOrientx
    RightInHandThumbJointOrienty = RightInHandThumbJointOrient.RightInHandThumbJointOrienty
    RightInHandThumbJointOrientz = RightInHandThumbJointOrient.RightInHandThumbJointOrientz

    RightInHandThumbMinRLimit = RightInHandThumbMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandThumbMinRLimitx = RightInHandThumbMinRLimit.RightInHandThumbMinRLimitx
    RightInHandThumbMinRLimity = RightInHandThumbMinRLimit.RightInHandThumbMinRLimity
    RightInHandThumbMinRLimitz = RightInHandThumbMinRLimit.RightInHandThumbMinRLimitz

    RightInHandThumbMaxRLimit = RightInHandThumbMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandThumbMaxRLimitx = RightInHandThumbMaxRLimit.RightInHandThumbMaxRLimitx
    RightInHandThumbMaxRLimity = RightInHandThumbMaxRLimit.RightInHandThumbMaxRLimity
    RightInHandThumbMaxRLimitz = RightInHandThumbMaxRLimit.RightInHandThumbMaxRLimitz

    RightInHandThumbMinRLimitEnablex = BoolField(default_value=False)

    RightInHandThumbMinRLimitEnabley = BoolField(default_value=False)

    RightInHandThumbMinRLimitEnablez = BoolField(default_value=False)

    RightInHandThumbMaxRLimitEnablex = BoolField(default_value=False)

    RightInHandThumbMaxRLimitEnabley = BoolField(default_value=False)

    RightInHandThumbMaxRLimitEnablez = BoolField(default_value=False)

    RightInHandIndex = MessageField()

    RightInHandIndexT = RightInHandIndexTField(default_value=(0.0, 0.0, 0.0))
    RightInHandIndexTx = RightInHandIndexT.RightInHandIndexTx
    RightInHandIndexTy = RightInHandIndexT.RightInHandIndexTy
    RightInHandIndexTz = RightInHandIndexT.RightInHandIndexTz

    RightInHandIndexR = RightInHandIndexRField(default_value=(0.0, 0.0, 0.0))
    RightInHandIndexRx = RightInHandIndexR.RightInHandIndexRx
    RightInHandIndexRy = RightInHandIndexR.RightInHandIndexRy
    RightInHandIndexRz = RightInHandIndexR.RightInHandIndexRz

    RightInHandIndexS = RightInHandIndexSField(default_value=(1.0, 1.0, 1.0))
    RightInHandIndexSx = RightInHandIndexS.RightInHandIndexSx
    RightInHandIndexSy = RightInHandIndexS.RightInHandIndexSy
    RightInHandIndexSz = RightInHandIndexS.RightInHandIndexSz

    RightInHandIndexRotateOrder = RightInHandIndexRotateOrderEnumField(default_value=0)

    RightInHandIndexRotateAxis = RightInHandIndexRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInHandIndexRotateAxisx = RightInHandIndexRotateAxis.RightInHandIndexRotateAxisx
    RightInHandIndexRotateAxisy = RightInHandIndexRotateAxis.RightInHandIndexRotateAxisy
    RightInHandIndexRotateAxisz = RightInHandIndexRotateAxis.RightInHandIndexRotateAxisz

    RightInHandIndexJointOrient = RightInHandIndexJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInHandIndexJointOrientx = RightInHandIndexJointOrient.RightInHandIndexJointOrientx
    RightInHandIndexJointOrienty = RightInHandIndexJointOrient.RightInHandIndexJointOrienty
    RightInHandIndexJointOrientz = RightInHandIndexJointOrient.RightInHandIndexJointOrientz

    RightInHandIndexMinRLimit = RightInHandIndexMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandIndexMinRLimitx = RightInHandIndexMinRLimit.RightInHandIndexMinRLimitx
    RightInHandIndexMinRLimity = RightInHandIndexMinRLimit.RightInHandIndexMinRLimity
    RightInHandIndexMinRLimitz = RightInHandIndexMinRLimit.RightInHandIndexMinRLimitz

    RightInHandIndexMaxRLimit = RightInHandIndexMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandIndexMaxRLimitx = RightInHandIndexMaxRLimit.RightInHandIndexMaxRLimitx
    RightInHandIndexMaxRLimity = RightInHandIndexMaxRLimit.RightInHandIndexMaxRLimity
    RightInHandIndexMaxRLimitz = RightInHandIndexMaxRLimit.RightInHandIndexMaxRLimitz

    RightInHandIndexMinRLimitEnablex = BoolField(default_value=False)

    RightInHandIndexMinRLimitEnabley = BoolField(default_value=False)

    RightInHandIndexMinRLimitEnablez = BoolField(default_value=False)

    RightInHandIndexMaxRLimitEnablex = BoolField(default_value=False)

    RightInHandIndexMaxRLimitEnabley = BoolField(default_value=False)

    RightInHandIndexMaxRLimitEnablez = BoolField(default_value=False)

    RightInHandMiddle = MessageField()

    RightInHandMiddleT = RightInHandMiddleTField(default_value=(0.0, 0.0, 0.0))
    RightInHandMiddleTx = RightInHandMiddleT.RightInHandMiddleTx
    RightInHandMiddleTy = RightInHandMiddleT.RightInHandMiddleTy
    RightInHandMiddleTz = RightInHandMiddleT.RightInHandMiddleTz

    RightInHandMiddleR = RightInHandMiddleRField(default_value=(0.0, 0.0, 0.0))
    RightInHandMiddleRx = RightInHandMiddleR.RightInHandMiddleRx
    RightInHandMiddleRy = RightInHandMiddleR.RightInHandMiddleRy
    RightInHandMiddleRz = RightInHandMiddleR.RightInHandMiddleRz

    RightInHandMiddleS = RightInHandMiddleSField(default_value=(1.0, 1.0, 1.0))
    RightInHandMiddleSx = RightInHandMiddleS.RightInHandMiddleSx
    RightInHandMiddleSy = RightInHandMiddleS.RightInHandMiddleSy
    RightInHandMiddleSz = RightInHandMiddleS.RightInHandMiddleSz

    RightInHandMiddleRotateOrder = RightInHandMiddleRotateOrderEnumField(default_value=0)

    RightInHandMiddleRotateAxis = RightInHandMiddleRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInHandMiddleRotateAxisx = RightInHandMiddleRotateAxis.RightInHandMiddleRotateAxisx
    RightInHandMiddleRotateAxisy = RightInHandMiddleRotateAxis.RightInHandMiddleRotateAxisy
    RightInHandMiddleRotateAxisz = RightInHandMiddleRotateAxis.RightInHandMiddleRotateAxisz

    RightInHandMiddleJointOrient = RightInHandMiddleJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInHandMiddleJointOrientx = RightInHandMiddleJointOrient.RightInHandMiddleJointOrientx
    RightInHandMiddleJointOrienty = RightInHandMiddleJointOrient.RightInHandMiddleJointOrienty
    RightInHandMiddleJointOrientz = RightInHandMiddleJointOrient.RightInHandMiddleJointOrientz

    RightInHandMiddleMinRLimit = RightInHandMiddleMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandMiddleMinRLimitx = RightInHandMiddleMinRLimit.RightInHandMiddleMinRLimitx
    RightInHandMiddleMinRLimity = RightInHandMiddleMinRLimit.RightInHandMiddleMinRLimity
    RightInHandMiddleMinRLimitz = RightInHandMiddleMinRLimit.RightInHandMiddleMinRLimitz

    RightInHandMiddleMaxRLimit = RightInHandMiddleMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandMiddleMaxRLimitx = RightInHandMiddleMaxRLimit.RightInHandMiddleMaxRLimitx
    RightInHandMiddleMaxRLimity = RightInHandMiddleMaxRLimit.RightInHandMiddleMaxRLimity
    RightInHandMiddleMaxRLimitz = RightInHandMiddleMaxRLimit.RightInHandMiddleMaxRLimitz

    RightInHandMiddleMinRLimitEnablex = BoolField(default_value=False)

    RightInHandMiddleMinRLimitEnabley = BoolField(default_value=False)

    RightInHandMiddleMinRLimitEnablez = BoolField(default_value=False)

    RightInHandMiddleMaxRLimitEnablex = BoolField(default_value=False)

    RightInHandMiddleMaxRLimitEnabley = BoolField(default_value=False)

    RightInHandMiddleMaxRLimitEnablez = BoolField(default_value=False)

    RightInHandRing = MessageField()

    RightInHandRingT = RightInHandRingTField(default_value=(0.0, 0.0, 0.0))
    RightInHandRingTx = RightInHandRingT.RightInHandRingTx
    RightInHandRingTy = RightInHandRingT.RightInHandRingTy
    RightInHandRingTz = RightInHandRingT.RightInHandRingTz

    RightInHandRingR = RightInHandRingRField(default_value=(0.0, 0.0, 0.0))
    RightInHandRingRx = RightInHandRingR.RightInHandRingRx
    RightInHandRingRy = RightInHandRingR.RightInHandRingRy
    RightInHandRingRz = RightInHandRingR.RightInHandRingRz

    RightInHandRingS = RightInHandRingSField(default_value=(1.0, 1.0, 1.0))
    RightInHandRingSx = RightInHandRingS.RightInHandRingSx
    RightInHandRingSy = RightInHandRingS.RightInHandRingSy
    RightInHandRingSz = RightInHandRingS.RightInHandRingSz

    RightInHandRingRotateOrder = RightInHandRingRotateOrderEnumField(default_value=0)

    RightInHandRingRotateAxis = RightInHandRingRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInHandRingRotateAxisx = RightInHandRingRotateAxis.RightInHandRingRotateAxisx
    RightInHandRingRotateAxisy = RightInHandRingRotateAxis.RightInHandRingRotateAxisy
    RightInHandRingRotateAxisz = RightInHandRingRotateAxis.RightInHandRingRotateAxisz

    RightInHandRingJointOrient = RightInHandRingJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInHandRingJointOrientx = RightInHandRingJointOrient.RightInHandRingJointOrientx
    RightInHandRingJointOrienty = RightInHandRingJointOrient.RightInHandRingJointOrienty
    RightInHandRingJointOrientz = RightInHandRingJointOrient.RightInHandRingJointOrientz

    RightInHandRingMinRLimit = RightInHandRingMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandRingMinRLimitx = RightInHandRingMinRLimit.RightInHandRingMinRLimitx
    RightInHandRingMinRLimity = RightInHandRingMinRLimit.RightInHandRingMinRLimity
    RightInHandRingMinRLimitz = RightInHandRingMinRLimit.RightInHandRingMinRLimitz

    RightInHandRingMaxRLimit = RightInHandRingMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandRingMaxRLimitx = RightInHandRingMaxRLimit.RightInHandRingMaxRLimitx
    RightInHandRingMaxRLimity = RightInHandRingMaxRLimit.RightInHandRingMaxRLimity
    RightInHandRingMaxRLimitz = RightInHandRingMaxRLimit.RightInHandRingMaxRLimitz

    RightInHandRingMinRLimitEnablex = BoolField(default_value=False)

    RightInHandRingMinRLimitEnabley = BoolField(default_value=False)

    RightInHandRingMinRLimitEnablez = BoolField(default_value=False)

    RightInHandRingMaxRLimitEnablex = BoolField(default_value=False)

    RightInHandRingMaxRLimitEnabley = BoolField(default_value=False)

    RightInHandRingMaxRLimitEnablez = BoolField(default_value=False)

    RightInHandPinky = MessageField()

    RightInHandPinkyT = RightInHandPinkyTField(default_value=(0.0, 0.0, 0.0))
    RightInHandPinkyTx = RightInHandPinkyT.RightInHandPinkyTx
    RightInHandPinkyTy = RightInHandPinkyT.RightInHandPinkyTy
    RightInHandPinkyTz = RightInHandPinkyT.RightInHandPinkyTz

    RightInHandPinkyR = RightInHandPinkyRField(default_value=(0.0, 0.0, 0.0))
    RightInHandPinkyRx = RightInHandPinkyR.RightInHandPinkyRx
    RightInHandPinkyRy = RightInHandPinkyR.RightInHandPinkyRy
    RightInHandPinkyRz = RightInHandPinkyR.RightInHandPinkyRz

    RightInHandPinkyS = RightInHandPinkySField(default_value=(1.0, 1.0, 1.0))
    RightInHandPinkySx = RightInHandPinkyS.RightInHandPinkySx
    RightInHandPinkySy = RightInHandPinkyS.RightInHandPinkySy
    RightInHandPinkySz = RightInHandPinkyS.RightInHandPinkySz

    RightInHandPinkyRotateOrder = RightInHandPinkyRotateOrderEnumField(default_value=0)

    RightInHandPinkyRotateAxis = RightInHandPinkyRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInHandPinkyRotateAxisx = RightInHandPinkyRotateAxis.RightInHandPinkyRotateAxisx
    RightInHandPinkyRotateAxisy = RightInHandPinkyRotateAxis.RightInHandPinkyRotateAxisy
    RightInHandPinkyRotateAxisz = RightInHandPinkyRotateAxis.RightInHandPinkyRotateAxisz

    RightInHandPinkyJointOrient = RightInHandPinkyJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInHandPinkyJointOrientx = RightInHandPinkyJointOrient.RightInHandPinkyJointOrientx
    RightInHandPinkyJointOrienty = RightInHandPinkyJointOrient.RightInHandPinkyJointOrienty
    RightInHandPinkyJointOrientz = RightInHandPinkyJointOrient.RightInHandPinkyJointOrientz

    RightInHandPinkyMinRLimit = RightInHandPinkyMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandPinkyMinRLimitx = RightInHandPinkyMinRLimit.RightInHandPinkyMinRLimitx
    RightInHandPinkyMinRLimity = RightInHandPinkyMinRLimit.RightInHandPinkyMinRLimity
    RightInHandPinkyMinRLimitz = RightInHandPinkyMinRLimit.RightInHandPinkyMinRLimitz

    RightInHandPinkyMaxRLimit = RightInHandPinkyMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandPinkyMaxRLimitx = RightInHandPinkyMaxRLimit.RightInHandPinkyMaxRLimitx
    RightInHandPinkyMaxRLimity = RightInHandPinkyMaxRLimit.RightInHandPinkyMaxRLimity
    RightInHandPinkyMaxRLimitz = RightInHandPinkyMaxRLimit.RightInHandPinkyMaxRLimitz

    RightInHandPinkyMinRLimitEnablex = BoolField(default_value=False)

    RightInHandPinkyMinRLimitEnabley = BoolField(default_value=False)

    RightInHandPinkyMinRLimitEnablez = BoolField(default_value=False)

    RightInHandPinkyMaxRLimitEnablex = BoolField(default_value=False)

    RightInHandPinkyMaxRLimitEnabley = BoolField(default_value=False)

    RightInHandPinkyMaxRLimitEnablez = BoolField(default_value=False)

    RightInHandExtraFinger = MessageField()

    RightInHandExtraFingerT = RightInHandExtraFingerTField(default_value=(0.0, 0.0, 0.0))
    RightInHandExtraFingerTx = RightInHandExtraFingerT.RightInHandExtraFingerTx
    RightInHandExtraFingerTy = RightInHandExtraFingerT.RightInHandExtraFingerTy
    RightInHandExtraFingerTz = RightInHandExtraFingerT.RightInHandExtraFingerTz

    RightInHandExtraFingerR = RightInHandExtraFingerRField(default_value=(0.0, 0.0, 0.0))
    RightInHandExtraFingerRx = RightInHandExtraFingerR.RightInHandExtraFingerRx
    RightInHandExtraFingerRy = RightInHandExtraFingerR.RightInHandExtraFingerRy
    RightInHandExtraFingerRz = RightInHandExtraFingerR.RightInHandExtraFingerRz

    RightInHandExtraFingerS = RightInHandExtraFingerSField(default_value=(1.0, 1.0, 1.0))
    RightInHandExtraFingerSx = RightInHandExtraFingerS.RightInHandExtraFingerSx
    RightInHandExtraFingerSy = RightInHandExtraFingerS.RightInHandExtraFingerSy
    RightInHandExtraFingerSz = RightInHandExtraFingerS.RightInHandExtraFingerSz

    RightInHandExtraFingerRotateOrder = RightInHandExtraFingerRotateOrderEnumField(default_value=0)

    RightInHandExtraFingerRotateAxis = RightInHandExtraFingerRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInHandExtraFingerRotateAxisx = RightInHandExtraFingerRotateAxis.RightInHandExtraFingerRotateAxisx
    RightInHandExtraFingerRotateAxisy = RightInHandExtraFingerRotateAxis.RightInHandExtraFingerRotateAxisy
    RightInHandExtraFingerRotateAxisz = RightInHandExtraFingerRotateAxis.RightInHandExtraFingerRotateAxisz

    RightInHandExtraFingerJointOrient = RightInHandExtraFingerJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInHandExtraFingerJointOrientx = RightInHandExtraFingerJointOrient.RightInHandExtraFingerJointOrientx
    RightInHandExtraFingerJointOrienty = RightInHandExtraFingerJointOrient.RightInHandExtraFingerJointOrienty
    RightInHandExtraFingerJointOrientz = RightInHandExtraFingerJointOrient.RightInHandExtraFingerJointOrientz

    RightInHandExtraFingerMinRLimit = RightInHandExtraFingerMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandExtraFingerMinRLimitx = RightInHandExtraFingerMinRLimit.RightInHandExtraFingerMinRLimitx
    RightInHandExtraFingerMinRLimity = RightInHandExtraFingerMinRLimit.RightInHandExtraFingerMinRLimity
    RightInHandExtraFingerMinRLimitz = RightInHandExtraFingerMinRLimit.RightInHandExtraFingerMinRLimitz

    RightInHandExtraFingerMaxRLimit = RightInHandExtraFingerMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInHandExtraFingerMaxRLimitx = RightInHandExtraFingerMaxRLimit.RightInHandExtraFingerMaxRLimitx
    RightInHandExtraFingerMaxRLimity = RightInHandExtraFingerMaxRLimit.RightInHandExtraFingerMaxRLimity
    RightInHandExtraFingerMaxRLimitz = RightInHandExtraFingerMaxRLimit.RightInHandExtraFingerMaxRLimitz

    RightInHandExtraFingerMinRLimitEnablex = BoolField(default_value=False)

    RightInHandExtraFingerMinRLimitEnabley = BoolField(default_value=False)

    RightInHandExtraFingerMinRLimitEnablez = BoolField(default_value=False)

    RightInHandExtraFingerMaxRLimitEnablex = BoolField(default_value=False)

    RightInHandExtraFingerMaxRLimitEnabley = BoolField(default_value=False)

    RightInHandExtraFingerMaxRLimitEnablez = BoolField(default_value=False)

    LeftInFootThumb = MessageField()

    LeftInFootThumbT = LeftInFootThumbTField(default_value=(0.0, 0.0, 0.0))
    LeftInFootThumbTx = LeftInFootThumbT.LeftInFootThumbTx
    LeftInFootThumbTy = LeftInFootThumbT.LeftInFootThumbTy
    LeftInFootThumbTz = LeftInFootThumbT.LeftInFootThumbTz

    LeftInFootThumbR = LeftInFootThumbRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootThumbRx = LeftInFootThumbR.LeftInFootThumbRx
    LeftInFootThumbRy = LeftInFootThumbR.LeftInFootThumbRy
    LeftInFootThumbRz = LeftInFootThumbR.LeftInFootThumbRz

    LeftInFootThumbS = LeftInFootThumbSField(default_value=(1.0, 1.0, 1.0))
    LeftInFootThumbSx = LeftInFootThumbS.LeftInFootThumbSx
    LeftInFootThumbSy = LeftInFootThumbS.LeftInFootThumbSy
    LeftInFootThumbSz = LeftInFootThumbS.LeftInFootThumbSz

    LeftInFootThumbRotateOrder = LeftInFootThumbRotateOrderEnumField(default_value=0)

    LeftInFootThumbRotateAxis = LeftInFootThumbRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInFootThumbRotateAxisx = LeftInFootThumbRotateAxis.LeftInFootThumbRotateAxisx
    LeftInFootThumbRotateAxisy = LeftInFootThumbRotateAxis.LeftInFootThumbRotateAxisy
    LeftInFootThumbRotateAxisz = LeftInFootThumbRotateAxis.LeftInFootThumbRotateAxisz

    LeftInFootThumbJointOrient = LeftInFootThumbJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInFootThumbJointOrientx = LeftInFootThumbJointOrient.LeftInFootThumbJointOrientx
    LeftInFootThumbJointOrienty = LeftInFootThumbJointOrient.LeftInFootThumbJointOrienty
    LeftInFootThumbJointOrientz = LeftInFootThumbJointOrient.LeftInFootThumbJointOrientz

    LeftInFootThumbMinRLimit = LeftInFootThumbMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootThumbMinRLimitx = LeftInFootThumbMinRLimit.LeftInFootThumbMinRLimitx
    LeftInFootThumbMinRLimity = LeftInFootThumbMinRLimit.LeftInFootThumbMinRLimity
    LeftInFootThumbMinRLimitz = LeftInFootThumbMinRLimit.LeftInFootThumbMinRLimitz

    LeftInFootThumbMaxRLimit = LeftInFootThumbMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootThumbMaxRLimitx = LeftInFootThumbMaxRLimit.LeftInFootThumbMaxRLimitx
    LeftInFootThumbMaxRLimity = LeftInFootThumbMaxRLimit.LeftInFootThumbMaxRLimity
    LeftInFootThumbMaxRLimitz = LeftInFootThumbMaxRLimit.LeftInFootThumbMaxRLimitz

    LeftInFootThumbMinRLimitEnablex = BoolField(default_value=False)

    LeftInFootThumbMinRLimitEnabley = BoolField(default_value=False)

    LeftInFootThumbMinRLimitEnablez = BoolField(default_value=False)

    LeftInFootThumbMaxRLimitEnablex = BoolField(default_value=False)

    LeftInFootThumbMaxRLimitEnabley = BoolField(default_value=False)

    LeftInFootThumbMaxRLimitEnablez = BoolField(default_value=False)

    LeftInFootIndex = MessageField()

    LeftInFootIndexT = LeftInFootIndexTField(default_value=(0.0, 0.0, 0.0))
    LeftInFootIndexTx = LeftInFootIndexT.LeftInFootIndexTx
    LeftInFootIndexTy = LeftInFootIndexT.LeftInFootIndexTy
    LeftInFootIndexTz = LeftInFootIndexT.LeftInFootIndexTz

    LeftInFootIndexR = LeftInFootIndexRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootIndexRx = LeftInFootIndexR.LeftInFootIndexRx
    LeftInFootIndexRy = LeftInFootIndexR.LeftInFootIndexRy
    LeftInFootIndexRz = LeftInFootIndexR.LeftInFootIndexRz

    LeftInFootIndexS = LeftInFootIndexSField(default_value=(1.0, 1.0, 1.0))
    LeftInFootIndexSx = LeftInFootIndexS.LeftInFootIndexSx
    LeftInFootIndexSy = LeftInFootIndexS.LeftInFootIndexSy
    LeftInFootIndexSz = LeftInFootIndexS.LeftInFootIndexSz

    LeftInFootIndexRotateOrder = LeftInFootIndexRotateOrderEnumField(default_value=0)

    LeftInFootIndexRotateAxis = LeftInFootIndexRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInFootIndexRotateAxisx = LeftInFootIndexRotateAxis.LeftInFootIndexRotateAxisx
    LeftInFootIndexRotateAxisy = LeftInFootIndexRotateAxis.LeftInFootIndexRotateAxisy
    LeftInFootIndexRotateAxisz = LeftInFootIndexRotateAxis.LeftInFootIndexRotateAxisz

    LeftInFootIndexJointOrient = LeftInFootIndexJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInFootIndexJointOrientx = LeftInFootIndexJointOrient.LeftInFootIndexJointOrientx
    LeftInFootIndexJointOrienty = LeftInFootIndexJointOrient.LeftInFootIndexJointOrienty
    LeftInFootIndexJointOrientz = LeftInFootIndexJointOrient.LeftInFootIndexJointOrientz

    LeftInFootIndexMinRLimit = LeftInFootIndexMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootIndexMinRLimitx = LeftInFootIndexMinRLimit.LeftInFootIndexMinRLimitx
    LeftInFootIndexMinRLimity = LeftInFootIndexMinRLimit.LeftInFootIndexMinRLimity
    LeftInFootIndexMinRLimitz = LeftInFootIndexMinRLimit.LeftInFootIndexMinRLimitz

    LeftInFootIndexMaxRLimit = LeftInFootIndexMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootIndexMaxRLimitx = LeftInFootIndexMaxRLimit.LeftInFootIndexMaxRLimitx
    LeftInFootIndexMaxRLimity = LeftInFootIndexMaxRLimit.LeftInFootIndexMaxRLimity
    LeftInFootIndexMaxRLimitz = LeftInFootIndexMaxRLimit.LeftInFootIndexMaxRLimitz

    LeftInFootIndexMinRLimitEnablex = BoolField(default_value=False)

    LeftInFootIndexMinRLimitEnabley = BoolField(default_value=False)

    LeftInFootIndexMinRLimitEnablez = BoolField(default_value=False)

    LeftInFootIndexMaxRLimitEnablex = BoolField(default_value=False)

    LeftInFootIndexMaxRLimitEnabley = BoolField(default_value=False)

    LeftInFootIndexMaxRLimitEnablez = BoolField(default_value=False)

    LeftInFootMiddle = MessageField()

    LeftInFootMiddleT = LeftInFootMiddleTField(default_value=(0.0, 0.0, 0.0))
    LeftInFootMiddleTx = LeftInFootMiddleT.LeftInFootMiddleTx
    LeftInFootMiddleTy = LeftInFootMiddleT.LeftInFootMiddleTy
    LeftInFootMiddleTz = LeftInFootMiddleT.LeftInFootMiddleTz

    LeftInFootMiddleR = LeftInFootMiddleRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootMiddleRx = LeftInFootMiddleR.LeftInFootMiddleRx
    LeftInFootMiddleRy = LeftInFootMiddleR.LeftInFootMiddleRy
    LeftInFootMiddleRz = LeftInFootMiddleR.LeftInFootMiddleRz

    LeftInFootMiddleS = LeftInFootMiddleSField(default_value=(1.0, 1.0, 1.0))
    LeftInFootMiddleSx = LeftInFootMiddleS.LeftInFootMiddleSx
    LeftInFootMiddleSy = LeftInFootMiddleS.LeftInFootMiddleSy
    LeftInFootMiddleSz = LeftInFootMiddleS.LeftInFootMiddleSz

    LeftInFootMiddleRotateOrder = LeftInFootMiddleRotateOrderEnumField(default_value=0)

    LeftInFootMiddleRotateAxis = LeftInFootMiddleRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInFootMiddleRotateAxisx = LeftInFootMiddleRotateAxis.LeftInFootMiddleRotateAxisx
    LeftInFootMiddleRotateAxisy = LeftInFootMiddleRotateAxis.LeftInFootMiddleRotateAxisy
    LeftInFootMiddleRotateAxisz = LeftInFootMiddleRotateAxis.LeftInFootMiddleRotateAxisz

    LeftInFootMiddleJointOrient = LeftInFootMiddleJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInFootMiddleJointOrientx = LeftInFootMiddleJointOrient.LeftInFootMiddleJointOrientx
    LeftInFootMiddleJointOrienty = LeftInFootMiddleJointOrient.LeftInFootMiddleJointOrienty
    LeftInFootMiddleJointOrientz = LeftInFootMiddleJointOrient.LeftInFootMiddleJointOrientz

    LeftInFootMiddleMinRLimit = LeftInFootMiddleMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootMiddleMinRLimitx = LeftInFootMiddleMinRLimit.LeftInFootMiddleMinRLimitx
    LeftInFootMiddleMinRLimity = LeftInFootMiddleMinRLimit.LeftInFootMiddleMinRLimity
    LeftInFootMiddleMinRLimitz = LeftInFootMiddleMinRLimit.LeftInFootMiddleMinRLimitz

    LeftInFootMiddleMaxRLimit = LeftInFootMiddleMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootMiddleMaxRLimitx = LeftInFootMiddleMaxRLimit.LeftInFootMiddleMaxRLimitx
    LeftInFootMiddleMaxRLimity = LeftInFootMiddleMaxRLimit.LeftInFootMiddleMaxRLimity
    LeftInFootMiddleMaxRLimitz = LeftInFootMiddleMaxRLimit.LeftInFootMiddleMaxRLimitz

    LeftInFootMiddleMinRLimitEnablex = BoolField(default_value=False)

    LeftInFootMiddleMinRLimitEnabley = BoolField(default_value=False)

    LeftInFootMiddleMinRLimitEnablez = BoolField(default_value=False)

    LeftInFootMiddleMaxRLimitEnablex = BoolField(default_value=False)

    LeftInFootMiddleMaxRLimitEnabley = BoolField(default_value=False)

    LeftInFootMiddleMaxRLimitEnablez = BoolField(default_value=False)

    LeftInFootRing = MessageField()

    LeftInFootRingT = LeftInFootRingTField(default_value=(0.0, 0.0, 0.0))
    LeftInFootRingTx = LeftInFootRingT.LeftInFootRingTx
    LeftInFootRingTy = LeftInFootRingT.LeftInFootRingTy
    LeftInFootRingTz = LeftInFootRingT.LeftInFootRingTz

    LeftInFootRingR = LeftInFootRingRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootRingRx = LeftInFootRingR.LeftInFootRingRx
    LeftInFootRingRy = LeftInFootRingR.LeftInFootRingRy
    LeftInFootRingRz = LeftInFootRingR.LeftInFootRingRz

    LeftInFootRingS = LeftInFootRingSField(default_value=(1.0, 1.0, 1.0))
    LeftInFootRingSx = LeftInFootRingS.LeftInFootRingSx
    LeftInFootRingSy = LeftInFootRingS.LeftInFootRingSy
    LeftInFootRingSz = LeftInFootRingS.LeftInFootRingSz

    LeftInFootRingRotateOrder = LeftInFootRingRotateOrderEnumField(default_value=0)

    LeftInFootRingRotateAxis = LeftInFootRingRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInFootRingRotateAxisx = LeftInFootRingRotateAxis.LeftInFootRingRotateAxisx
    LeftInFootRingRotateAxisy = LeftInFootRingRotateAxis.LeftInFootRingRotateAxisy
    LeftInFootRingRotateAxisz = LeftInFootRingRotateAxis.LeftInFootRingRotateAxisz

    LeftInFootRingJointOrient = LeftInFootRingJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInFootRingJointOrientx = LeftInFootRingJointOrient.LeftInFootRingJointOrientx
    LeftInFootRingJointOrienty = LeftInFootRingJointOrient.LeftInFootRingJointOrienty
    LeftInFootRingJointOrientz = LeftInFootRingJointOrient.LeftInFootRingJointOrientz

    LeftInFootRingMinRLimit = LeftInFootRingMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootRingMinRLimitx = LeftInFootRingMinRLimit.LeftInFootRingMinRLimitx
    LeftInFootRingMinRLimity = LeftInFootRingMinRLimit.LeftInFootRingMinRLimity
    LeftInFootRingMinRLimitz = LeftInFootRingMinRLimit.LeftInFootRingMinRLimitz

    LeftInFootRingMaxRLimit = LeftInFootRingMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootRingMaxRLimitx = LeftInFootRingMaxRLimit.LeftInFootRingMaxRLimitx
    LeftInFootRingMaxRLimity = LeftInFootRingMaxRLimit.LeftInFootRingMaxRLimity
    LeftInFootRingMaxRLimitz = LeftInFootRingMaxRLimit.LeftInFootRingMaxRLimitz

    LeftInFootRingMinRLimitEnablex = BoolField(default_value=False)

    LeftInFootRingMinRLimitEnabley = BoolField(default_value=False)

    LeftInFootRingMinRLimitEnablez = BoolField(default_value=False)

    LeftInFootRingMaxRLimitEnablex = BoolField(default_value=False)

    LeftInFootRingMaxRLimitEnabley = BoolField(default_value=False)

    LeftInFootRingMaxRLimitEnablez = BoolField(default_value=False)

    LeftInFootPinky = MessageField()

    LeftInFootPinkyT = LeftInFootPinkyTField(default_value=(0.0, 0.0, 0.0))
    LeftInFootPinkyTx = LeftInFootPinkyT.LeftInFootPinkyTx
    LeftInFootPinkyTy = LeftInFootPinkyT.LeftInFootPinkyTy
    LeftInFootPinkyTz = LeftInFootPinkyT.LeftInFootPinkyTz

    LeftInFootPinkyR = LeftInFootPinkyRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootPinkyRx = LeftInFootPinkyR.LeftInFootPinkyRx
    LeftInFootPinkyRy = LeftInFootPinkyR.LeftInFootPinkyRy
    LeftInFootPinkyRz = LeftInFootPinkyR.LeftInFootPinkyRz

    LeftInFootPinkyS = LeftInFootPinkySField(default_value=(1.0, 1.0, 1.0))
    LeftInFootPinkySx = LeftInFootPinkyS.LeftInFootPinkySx
    LeftInFootPinkySy = LeftInFootPinkyS.LeftInFootPinkySy
    LeftInFootPinkySz = LeftInFootPinkyS.LeftInFootPinkySz

    LeftInFootPinkyRotateOrder = LeftInFootPinkyRotateOrderEnumField(default_value=0)

    LeftInFootPinkyRotateAxis = LeftInFootPinkyRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInFootPinkyRotateAxisx = LeftInFootPinkyRotateAxis.LeftInFootPinkyRotateAxisx
    LeftInFootPinkyRotateAxisy = LeftInFootPinkyRotateAxis.LeftInFootPinkyRotateAxisy
    LeftInFootPinkyRotateAxisz = LeftInFootPinkyRotateAxis.LeftInFootPinkyRotateAxisz

    LeftInFootPinkyJointOrient = LeftInFootPinkyJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInFootPinkyJointOrientx = LeftInFootPinkyJointOrient.LeftInFootPinkyJointOrientx
    LeftInFootPinkyJointOrienty = LeftInFootPinkyJointOrient.LeftInFootPinkyJointOrienty
    LeftInFootPinkyJointOrientz = LeftInFootPinkyJointOrient.LeftInFootPinkyJointOrientz

    LeftInFootPinkyMinRLimit = LeftInFootPinkyMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootPinkyMinRLimitx = LeftInFootPinkyMinRLimit.LeftInFootPinkyMinRLimitx
    LeftInFootPinkyMinRLimity = LeftInFootPinkyMinRLimit.LeftInFootPinkyMinRLimity
    LeftInFootPinkyMinRLimitz = LeftInFootPinkyMinRLimit.LeftInFootPinkyMinRLimitz

    LeftInFootPinkyMaxRLimit = LeftInFootPinkyMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootPinkyMaxRLimitx = LeftInFootPinkyMaxRLimit.LeftInFootPinkyMaxRLimitx
    LeftInFootPinkyMaxRLimity = LeftInFootPinkyMaxRLimit.LeftInFootPinkyMaxRLimity
    LeftInFootPinkyMaxRLimitz = LeftInFootPinkyMaxRLimit.LeftInFootPinkyMaxRLimitz

    LeftInFootPinkyMinRLimitEnablex = BoolField(default_value=False)

    LeftInFootPinkyMinRLimitEnabley = BoolField(default_value=False)

    LeftInFootPinkyMinRLimitEnablez = BoolField(default_value=False)

    LeftInFootPinkyMaxRLimitEnablex = BoolField(default_value=False)

    LeftInFootPinkyMaxRLimitEnabley = BoolField(default_value=False)

    LeftInFootPinkyMaxRLimitEnablez = BoolField(default_value=False)

    LeftInFootExtraFinger = MessageField()

    LeftInFootExtraFingerT = LeftInFootExtraFingerTField(default_value=(0.0, 0.0, 0.0))
    LeftInFootExtraFingerTx = LeftInFootExtraFingerT.LeftInFootExtraFingerTx
    LeftInFootExtraFingerTy = LeftInFootExtraFingerT.LeftInFootExtraFingerTy
    LeftInFootExtraFingerTz = LeftInFootExtraFingerT.LeftInFootExtraFingerTz

    LeftInFootExtraFingerR = LeftInFootExtraFingerRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootExtraFingerRx = LeftInFootExtraFingerR.LeftInFootExtraFingerRx
    LeftInFootExtraFingerRy = LeftInFootExtraFingerR.LeftInFootExtraFingerRy
    LeftInFootExtraFingerRz = LeftInFootExtraFingerR.LeftInFootExtraFingerRz

    LeftInFootExtraFingerS = LeftInFootExtraFingerSField(default_value=(1.0, 1.0, 1.0))
    LeftInFootExtraFingerSx = LeftInFootExtraFingerS.LeftInFootExtraFingerSx
    LeftInFootExtraFingerSy = LeftInFootExtraFingerS.LeftInFootExtraFingerSy
    LeftInFootExtraFingerSz = LeftInFootExtraFingerS.LeftInFootExtraFingerSz

    LeftInFootExtraFingerRotateOrder = LeftInFootExtraFingerRotateOrderEnumField(default_value=0)

    LeftInFootExtraFingerRotateAxis = LeftInFootExtraFingerRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftInFootExtraFingerRotateAxisx = LeftInFootExtraFingerRotateAxis.LeftInFootExtraFingerRotateAxisx
    LeftInFootExtraFingerRotateAxisy = LeftInFootExtraFingerRotateAxis.LeftInFootExtraFingerRotateAxisy
    LeftInFootExtraFingerRotateAxisz = LeftInFootExtraFingerRotateAxis.LeftInFootExtraFingerRotateAxisz

    LeftInFootExtraFingerJointOrient = LeftInFootExtraFingerJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftInFootExtraFingerJointOrientx = LeftInFootExtraFingerJointOrient.LeftInFootExtraFingerJointOrientx
    LeftInFootExtraFingerJointOrienty = LeftInFootExtraFingerJointOrient.LeftInFootExtraFingerJointOrienty
    LeftInFootExtraFingerJointOrientz = LeftInFootExtraFingerJointOrient.LeftInFootExtraFingerJointOrientz

    LeftInFootExtraFingerMinRLimit = LeftInFootExtraFingerMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootExtraFingerMinRLimitx = LeftInFootExtraFingerMinRLimit.LeftInFootExtraFingerMinRLimitx
    LeftInFootExtraFingerMinRLimity = LeftInFootExtraFingerMinRLimit.LeftInFootExtraFingerMinRLimity
    LeftInFootExtraFingerMinRLimitz = LeftInFootExtraFingerMinRLimit.LeftInFootExtraFingerMinRLimitz

    LeftInFootExtraFingerMaxRLimit = LeftInFootExtraFingerMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftInFootExtraFingerMaxRLimitx = LeftInFootExtraFingerMaxRLimit.LeftInFootExtraFingerMaxRLimitx
    LeftInFootExtraFingerMaxRLimity = LeftInFootExtraFingerMaxRLimit.LeftInFootExtraFingerMaxRLimity
    LeftInFootExtraFingerMaxRLimitz = LeftInFootExtraFingerMaxRLimit.LeftInFootExtraFingerMaxRLimitz

    LeftInFootExtraFingerMinRLimitEnablex = BoolField(default_value=False)

    LeftInFootExtraFingerMinRLimitEnabley = BoolField(default_value=False)

    LeftInFootExtraFingerMinRLimitEnablez = BoolField(default_value=False)

    LeftInFootExtraFingerMaxRLimitEnablex = BoolField(default_value=False)

    LeftInFootExtraFingerMaxRLimitEnabley = BoolField(default_value=False)

    LeftInFootExtraFingerMaxRLimitEnablez = BoolField(default_value=False)

    RightInFootThumb = MessageField()

    RightInFootThumbT = RightInFootThumbTField(default_value=(0.0, 0.0, 0.0))
    RightInFootThumbTx = RightInFootThumbT.RightInFootThumbTx
    RightInFootThumbTy = RightInFootThumbT.RightInFootThumbTy
    RightInFootThumbTz = RightInFootThumbT.RightInFootThumbTz

    RightInFootThumbR = RightInFootThumbRField(default_value=(0.0, 0.0, 0.0))
    RightInFootThumbRx = RightInFootThumbR.RightInFootThumbRx
    RightInFootThumbRy = RightInFootThumbR.RightInFootThumbRy
    RightInFootThumbRz = RightInFootThumbR.RightInFootThumbRz

    RightInFootThumbS = RightInFootThumbSField(default_value=(1.0, 1.0, 1.0))
    RightInFootThumbSx = RightInFootThumbS.RightInFootThumbSx
    RightInFootThumbSy = RightInFootThumbS.RightInFootThumbSy
    RightInFootThumbSz = RightInFootThumbS.RightInFootThumbSz

    RightInFootThumbRotateOrder = RightInFootThumbRotateOrderEnumField(default_value=0)

    RightInFootThumbRotateAxis = RightInFootThumbRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInFootThumbRotateAxisx = RightInFootThumbRotateAxis.RightInFootThumbRotateAxisx
    RightInFootThumbRotateAxisy = RightInFootThumbRotateAxis.RightInFootThumbRotateAxisy
    RightInFootThumbRotateAxisz = RightInFootThumbRotateAxis.RightInFootThumbRotateAxisz

    RightInFootThumbJointOrient = RightInFootThumbJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInFootThumbJointOrientx = RightInFootThumbJointOrient.RightInFootThumbJointOrientx
    RightInFootThumbJointOrienty = RightInFootThumbJointOrient.RightInFootThumbJointOrienty
    RightInFootThumbJointOrientz = RightInFootThumbJointOrient.RightInFootThumbJointOrientz

    RightInFootThumbMinRLimit = RightInFootThumbMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootThumbMinRLimitx = RightInFootThumbMinRLimit.RightInFootThumbMinRLimitx
    RightInFootThumbMinRLimity = RightInFootThumbMinRLimit.RightInFootThumbMinRLimity
    RightInFootThumbMinRLimitz = RightInFootThumbMinRLimit.RightInFootThumbMinRLimitz

    RightInFootThumbMaxRLimit = RightInFootThumbMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootThumbMaxRLimitx = RightInFootThumbMaxRLimit.RightInFootThumbMaxRLimitx
    RightInFootThumbMaxRLimity = RightInFootThumbMaxRLimit.RightInFootThumbMaxRLimity
    RightInFootThumbMaxRLimitz = RightInFootThumbMaxRLimit.RightInFootThumbMaxRLimitz

    RightInFootThumbMinRLimitEnablex = BoolField(default_value=False)

    RightInFootThumbMinRLimitEnabley = BoolField(default_value=False)

    RightInFootThumbMinRLimitEnablez = BoolField(default_value=False)

    RightInFootThumbMaxRLimitEnablex = BoolField(default_value=False)

    RightInFootThumbMaxRLimitEnabley = BoolField(default_value=False)

    RightInFootThumbMaxRLimitEnablez = BoolField(default_value=False)

    RightInFootIndex = MessageField()

    RightInFootIndexT = RightInFootIndexTField(default_value=(0.0, 0.0, 0.0))
    RightInFootIndexTx = RightInFootIndexT.RightInFootIndexTx
    RightInFootIndexTy = RightInFootIndexT.RightInFootIndexTy
    RightInFootIndexTz = RightInFootIndexT.RightInFootIndexTz

    RightInFootIndexR = RightInFootIndexRField(default_value=(0.0, 0.0, 0.0))
    RightInFootIndexRx = RightInFootIndexR.RightInFootIndexRx
    RightInFootIndexRy = RightInFootIndexR.RightInFootIndexRy
    RightInFootIndexRz = RightInFootIndexR.RightInFootIndexRz

    RightInFootIndexS = RightInFootIndexSField(default_value=(1.0, 1.0, 1.0))
    RightInFootIndexSx = RightInFootIndexS.RightInFootIndexSx
    RightInFootIndexSy = RightInFootIndexS.RightInFootIndexSy
    RightInFootIndexSz = RightInFootIndexS.RightInFootIndexSz

    RightInFootIndexRotateOrder = RightInFootIndexRotateOrderEnumField(default_value=0)

    RightInFootIndexRotateAxis = RightInFootIndexRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInFootIndexRotateAxisx = RightInFootIndexRotateAxis.RightInFootIndexRotateAxisx
    RightInFootIndexRotateAxisy = RightInFootIndexRotateAxis.RightInFootIndexRotateAxisy
    RightInFootIndexRotateAxisz = RightInFootIndexRotateAxis.RightInFootIndexRotateAxisz

    RightInFootIndexJointOrient = RightInFootIndexJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInFootIndexJointOrientx = RightInFootIndexJointOrient.RightInFootIndexJointOrientx
    RightInFootIndexJointOrienty = RightInFootIndexJointOrient.RightInFootIndexJointOrienty
    RightInFootIndexJointOrientz = RightInFootIndexJointOrient.RightInFootIndexJointOrientz

    RightInFootIndexMinRLimit = RightInFootIndexMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootIndexMinRLimitx = RightInFootIndexMinRLimit.RightInFootIndexMinRLimitx
    RightInFootIndexMinRLimity = RightInFootIndexMinRLimit.RightInFootIndexMinRLimity
    RightInFootIndexMinRLimitz = RightInFootIndexMinRLimit.RightInFootIndexMinRLimitz

    RightInFootIndexMaxRLimit = RightInFootIndexMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootIndexMaxRLimitx = RightInFootIndexMaxRLimit.RightInFootIndexMaxRLimitx
    RightInFootIndexMaxRLimity = RightInFootIndexMaxRLimit.RightInFootIndexMaxRLimity
    RightInFootIndexMaxRLimitz = RightInFootIndexMaxRLimit.RightInFootIndexMaxRLimitz

    RightInFootIndexMinRLimitEnablex = BoolField(default_value=False)

    RightInFootIndexMinRLimitEnabley = BoolField(default_value=False)

    RightInFootIndexMinRLimitEnablez = BoolField(default_value=False)

    RightInFootIndexMaxRLimitEnablex = BoolField(default_value=False)

    RightInFootIndexMaxRLimitEnabley = BoolField(default_value=False)

    RightInFootIndexMaxRLimitEnablez = BoolField(default_value=False)

    RightInFootMiddle = MessageField()

    RightInFootMiddleT = RightInFootMiddleTField(default_value=(0.0, 0.0, 0.0))
    RightInFootMiddleTx = RightInFootMiddleT.RightInFootMiddleTx
    RightInFootMiddleTy = RightInFootMiddleT.RightInFootMiddleTy
    RightInFootMiddleTz = RightInFootMiddleT.RightInFootMiddleTz

    RightInFootMiddleR = RightInFootMiddleRField(default_value=(0.0, 0.0, 0.0))
    RightInFootMiddleRx = RightInFootMiddleR.RightInFootMiddleRx
    RightInFootMiddleRy = RightInFootMiddleR.RightInFootMiddleRy
    RightInFootMiddleRz = RightInFootMiddleR.RightInFootMiddleRz

    RightInFootMiddleS = RightInFootMiddleSField(default_value=(1.0, 1.0, 1.0))
    RightInFootMiddleSx = RightInFootMiddleS.RightInFootMiddleSx
    RightInFootMiddleSy = RightInFootMiddleS.RightInFootMiddleSy
    RightInFootMiddleSz = RightInFootMiddleS.RightInFootMiddleSz

    RightInFootMiddleRotateOrder = RightInFootMiddleRotateOrderEnumField(default_value=0)

    RightInFootMiddleRotateAxis = RightInFootMiddleRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInFootMiddleRotateAxisx = RightInFootMiddleRotateAxis.RightInFootMiddleRotateAxisx
    RightInFootMiddleRotateAxisy = RightInFootMiddleRotateAxis.RightInFootMiddleRotateAxisy
    RightInFootMiddleRotateAxisz = RightInFootMiddleRotateAxis.RightInFootMiddleRotateAxisz

    RightInFootMiddleJointOrient = RightInFootMiddleJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInFootMiddleJointOrientx = RightInFootMiddleJointOrient.RightInFootMiddleJointOrientx
    RightInFootMiddleJointOrienty = RightInFootMiddleJointOrient.RightInFootMiddleJointOrienty
    RightInFootMiddleJointOrientz = RightInFootMiddleJointOrient.RightInFootMiddleJointOrientz

    RightInFootMiddleMinRLimit = RightInFootMiddleMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootMiddleMinRLimitx = RightInFootMiddleMinRLimit.RightInFootMiddleMinRLimitx
    RightInFootMiddleMinRLimity = RightInFootMiddleMinRLimit.RightInFootMiddleMinRLimity
    RightInFootMiddleMinRLimitz = RightInFootMiddleMinRLimit.RightInFootMiddleMinRLimitz

    RightInFootMiddleMaxRLimit = RightInFootMiddleMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootMiddleMaxRLimitx = RightInFootMiddleMaxRLimit.RightInFootMiddleMaxRLimitx
    RightInFootMiddleMaxRLimity = RightInFootMiddleMaxRLimit.RightInFootMiddleMaxRLimity
    RightInFootMiddleMaxRLimitz = RightInFootMiddleMaxRLimit.RightInFootMiddleMaxRLimitz

    RightInFootMiddleMinRLimitEnablex = BoolField(default_value=False)

    RightInFootMiddleMinRLimitEnabley = BoolField(default_value=False)

    RightInFootMiddleMinRLimitEnablez = BoolField(default_value=False)

    RightInFootMiddleMaxRLimitEnablex = BoolField(default_value=False)

    RightInFootMiddleMaxRLimitEnabley = BoolField(default_value=False)

    RightInFootMiddleMaxRLimitEnablez = BoolField(default_value=False)

    RightInFootRing = MessageField()

    RightInFootRingT = RightInFootRingTField(default_value=(0.0, 0.0, 0.0))
    RightInFootRingTx = RightInFootRingT.RightInFootRingTx
    RightInFootRingTy = RightInFootRingT.RightInFootRingTy
    RightInFootRingTz = RightInFootRingT.RightInFootRingTz

    RightInFootRingR = RightInFootRingRField(default_value=(0.0, 0.0, 0.0))
    RightInFootRingRx = RightInFootRingR.RightInFootRingRx
    RightInFootRingRy = RightInFootRingR.RightInFootRingRy
    RightInFootRingRz = RightInFootRingR.RightInFootRingRz

    RightInFootRingS = RightInFootRingSField(default_value=(1.0, 1.0, 1.0))
    RightInFootRingSx = RightInFootRingS.RightInFootRingSx
    RightInFootRingSy = RightInFootRingS.RightInFootRingSy
    RightInFootRingSz = RightInFootRingS.RightInFootRingSz

    RightInFootRingRotateOrder = RightInFootRingRotateOrderEnumField(default_value=0)

    RightInFootRingRotateAxis = RightInFootRingRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInFootRingRotateAxisx = RightInFootRingRotateAxis.RightInFootRingRotateAxisx
    RightInFootRingRotateAxisy = RightInFootRingRotateAxis.RightInFootRingRotateAxisy
    RightInFootRingRotateAxisz = RightInFootRingRotateAxis.RightInFootRingRotateAxisz

    RightInFootRingJointOrient = RightInFootRingJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInFootRingJointOrientx = RightInFootRingJointOrient.RightInFootRingJointOrientx
    RightInFootRingJointOrienty = RightInFootRingJointOrient.RightInFootRingJointOrienty
    RightInFootRingJointOrientz = RightInFootRingJointOrient.RightInFootRingJointOrientz

    RightInFootRingMinRLimit = RightInFootRingMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootRingMinRLimitx = RightInFootRingMinRLimit.RightInFootRingMinRLimitx
    RightInFootRingMinRLimity = RightInFootRingMinRLimit.RightInFootRingMinRLimity
    RightInFootRingMinRLimitz = RightInFootRingMinRLimit.RightInFootRingMinRLimitz

    RightInFootRingMaxRLimit = RightInFootRingMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootRingMaxRLimitx = RightInFootRingMaxRLimit.RightInFootRingMaxRLimitx
    RightInFootRingMaxRLimity = RightInFootRingMaxRLimit.RightInFootRingMaxRLimity
    RightInFootRingMaxRLimitz = RightInFootRingMaxRLimit.RightInFootRingMaxRLimitz

    RightInFootRingMinRLimitEnablex = BoolField(default_value=False)

    RightInFootRingMinRLimitEnabley = BoolField(default_value=False)

    RightInFootRingMinRLimitEnablez = BoolField(default_value=False)

    RightInFootRingMaxRLimitEnablex = BoolField(default_value=False)

    RightInFootRingMaxRLimitEnabley = BoolField(default_value=False)

    RightInFootRingMaxRLimitEnablez = BoolField(default_value=False)

    RightInFootPinky = MessageField()

    RightInFootPinkyT = RightInFootPinkyTField(default_value=(0.0, 0.0, 0.0))
    RightInFootPinkyTx = RightInFootPinkyT.RightInFootPinkyTx
    RightInFootPinkyTy = RightInFootPinkyT.RightInFootPinkyTy
    RightInFootPinkyTz = RightInFootPinkyT.RightInFootPinkyTz

    RightInFootPinkyR = RightInFootPinkyRField(default_value=(0.0, 0.0, 0.0))
    RightInFootPinkyRx = RightInFootPinkyR.RightInFootPinkyRx
    RightInFootPinkyRy = RightInFootPinkyR.RightInFootPinkyRy
    RightInFootPinkyRz = RightInFootPinkyR.RightInFootPinkyRz

    RightInFootPinkyS = RightInFootPinkySField(default_value=(1.0, 1.0, 1.0))
    RightInFootPinkySx = RightInFootPinkyS.RightInFootPinkySx
    RightInFootPinkySy = RightInFootPinkyS.RightInFootPinkySy
    RightInFootPinkySz = RightInFootPinkyS.RightInFootPinkySz

    RightInFootPinkyRotateOrder = RightInFootPinkyRotateOrderEnumField(default_value=0)

    RightInFootPinkyRotateAxis = RightInFootPinkyRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInFootPinkyRotateAxisx = RightInFootPinkyRotateAxis.RightInFootPinkyRotateAxisx
    RightInFootPinkyRotateAxisy = RightInFootPinkyRotateAxis.RightInFootPinkyRotateAxisy
    RightInFootPinkyRotateAxisz = RightInFootPinkyRotateAxis.RightInFootPinkyRotateAxisz

    RightInFootPinkyJointOrient = RightInFootPinkyJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInFootPinkyJointOrientx = RightInFootPinkyJointOrient.RightInFootPinkyJointOrientx
    RightInFootPinkyJointOrienty = RightInFootPinkyJointOrient.RightInFootPinkyJointOrienty
    RightInFootPinkyJointOrientz = RightInFootPinkyJointOrient.RightInFootPinkyJointOrientz

    RightInFootPinkyMinRLimit = RightInFootPinkyMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootPinkyMinRLimitx = RightInFootPinkyMinRLimit.RightInFootPinkyMinRLimitx
    RightInFootPinkyMinRLimity = RightInFootPinkyMinRLimit.RightInFootPinkyMinRLimity
    RightInFootPinkyMinRLimitz = RightInFootPinkyMinRLimit.RightInFootPinkyMinRLimitz

    RightInFootPinkyMaxRLimit = RightInFootPinkyMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootPinkyMaxRLimitx = RightInFootPinkyMaxRLimit.RightInFootPinkyMaxRLimitx
    RightInFootPinkyMaxRLimity = RightInFootPinkyMaxRLimit.RightInFootPinkyMaxRLimity
    RightInFootPinkyMaxRLimitz = RightInFootPinkyMaxRLimit.RightInFootPinkyMaxRLimitz

    RightInFootPinkyMinRLimitEnablex = BoolField(default_value=False)

    RightInFootPinkyMinRLimitEnabley = BoolField(default_value=False)

    RightInFootPinkyMinRLimitEnablez = BoolField(default_value=False)

    RightInFootPinkyMaxRLimitEnablex = BoolField(default_value=False)

    RightInFootPinkyMaxRLimitEnabley = BoolField(default_value=False)

    RightInFootPinkyMaxRLimitEnablez = BoolField(default_value=False)

    RightInFootExtraFinger = MessageField()

    RightInFootExtraFingerT = RightInFootExtraFingerTField(default_value=(0.0, 0.0, 0.0))
    RightInFootExtraFingerTx = RightInFootExtraFingerT.RightInFootExtraFingerTx
    RightInFootExtraFingerTy = RightInFootExtraFingerT.RightInFootExtraFingerTy
    RightInFootExtraFingerTz = RightInFootExtraFingerT.RightInFootExtraFingerTz

    RightInFootExtraFingerR = RightInFootExtraFingerRField(default_value=(0.0, 0.0, 0.0))
    RightInFootExtraFingerRx = RightInFootExtraFingerR.RightInFootExtraFingerRx
    RightInFootExtraFingerRy = RightInFootExtraFingerR.RightInFootExtraFingerRy
    RightInFootExtraFingerRz = RightInFootExtraFingerR.RightInFootExtraFingerRz

    RightInFootExtraFingerS = RightInFootExtraFingerSField(default_value=(1.0, 1.0, 1.0))
    RightInFootExtraFingerSx = RightInFootExtraFingerS.RightInFootExtraFingerSx
    RightInFootExtraFingerSy = RightInFootExtraFingerS.RightInFootExtraFingerSy
    RightInFootExtraFingerSz = RightInFootExtraFingerS.RightInFootExtraFingerSz

    RightInFootExtraFingerRotateOrder = RightInFootExtraFingerRotateOrderEnumField(default_value=0)

    RightInFootExtraFingerRotateAxis = RightInFootExtraFingerRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightInFootExtraFingerRotateAxisx = RightInFootExtraFingerRotateAxis.RightInFootExtraFingerRotateAxisx
    RightInFootExtraFingerRotateAxisy = RightInFootExtraFingerRotateAxis.RightInFootExtraFingerRotateAxisy
    RightInFootExtraFingerRotateAxisz = RightInFootExtraFingerRotateAxis.RightInFootExtraFingerRotateAxisz

    RightInFootExtraFingerJointOrient = RightInFootExtraFingerJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightInFootExtraFingerJointOrientx = RightInFootExtraFingerJointOrient.RightInFootExtraFingerJointOrientx
    RightInFootExtraFingerJointOrienty = RightInFootExtraFingerJointOrient.RightInFootExtraFingerJointOrienty
    RightInFootExtraFingerJointOrientz = RightInFootExtraFingerJointOrient.RightInFootExtraFingerJointOrientz

    RightInFootExtraFingerMinRLimit = RightInFootExtraFingerMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootExtraFingerMinRLimitx = RightInFootExtraFingerMinRLimit.RightInFootExtraFingerMinRLimitx
    RightInFootExtraFingerMinRLimity = RightInFootExtraFingerMinRLimit.RightInFootExtraFingerMinRLimity
    RightInFootExtraFingerMinRLimitz = RightInFootExtraFingerMinRLimit.RightInFootExtraFingerMinRLimitz

    RightInFootExtraFingerMaxRLimit = RightInFootExtraFingerMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightInFootExtraFingerMaxRLimitx = RightInFootExtraFingerMaxRLimit.RightInFootExtraFingerMaxRLimitx
    RightInFootExtraFingerMaxRLimity = RightInFootExtraFingerMaxRLimit.RightInFootExtraFingerMaxRLimity
    RightInFootExtraFingerMaxRLimitz = RightInFootExtraFingerMaxRLimit.RightInFootExtraFingerMaxRLimitz

    RightInFootExtraFingerMinRLimitEnablex = BoolField(default_value=False)

    RightInFootExtraFingerMinRLimitEnabley = BoolField(default_value=False)

    RightInFootExtraFingerMinRLimitEnablez = BoolField(default_value=False)

    RightInFootExtraFingerMaxRLimitEnablex = BoolField(default_value=False)

    RightInFootExtraFingerMaxRLimitEnabley = BoolField(default_value=False)

    RightInFootExtraFingerMaxRLimitEnablez = BoolField(default_value=False)

    LeftShoulderExtra = MessageField()

    LeftShoulderExtraT = LeftShoulderExtraTField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderExtraTx = LeftShoulderExtraT.LeftShoulderExtraTx
    LeftShoulderExtraTy = LeftShoulderExtraT.LeftShoulderExtraTy
    LeftShoulderExtraTz = LeftShoulderExtraT.LeftShoulderExtraTz

    LeftShoulderExtraR = LeftShoulderExtraRField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderExtraRx = LeftShoulderExtraR.LeftShoulderExtraRx
    LeftShoulderExtraRy = LeftShoulderExtraR.LeftShoulderExtraRy
    LeftShoulderExtraRz = LeftShoulderExtraR.LeftShoulderExtraRz

    LeftShoulderExtraS = LeftShoulderExtraSField(default_value=(1.0, 1.0, 1.0))
    LeftShoulderExtraSx = LeftShoulderExtraS.LeftShoulderExtraSx
    LeftShoulderExtraSy = LeftShoulderExtraS.LeftShoulderExtraSy
    LeftShoulderExtraSz = LeftShoulderExtraS.LeftShoulderExtraSz

    LeftShoulderExtraRotateOrder = LeftShoulderExtraRotateOrderEnumField(default_value=0)

    LeftShoulderExtraRotateAxis = LeftShoulderExtraRotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderExtraRotateAxisx = LeftShoulderExtraRotateAxis.LeftShoulderExtraRotateAxisx
    LeftShoulderExtraRotateAxisy = LeftShoulderExtraRotateAxis.LeftShoulderExtraRotateAxisy
    LeftShoulderExtraRotateAxisz = LeftShoulderExtraRotateAxis.LeftShoulderExtraRotateAxisz

    LeftShoulderExtraJointOrient = LeftShoulderExtraJointOrientField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderExtraJointOrientx = LeftShoulderExtraJointOrient.LeftShoulderExtraJointOrientx
    LeftShoulderExtraJointOrienty = LeftShoulderExtraJointOrient.LeftShoulderExtraJointOrienty
    LeftShoulderExtraJointOrientz = LeftShoulderExtraJointOrient.LeftShoulderExtraJointOrientz

    LeftShoulderExtraMinRLimit = LeftShoulderExtraMinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderExtraMinRLimitx = LeftShoulderExtraMinRLimit.LeftShoulderExtraMinRLimitx
    LeftShoulderExtraMinRLimity = LeftShoulderExtraMinRLimit.LeftShoulderExtraMinRLimity
    LeftShoulderExtraMinRLimitz = LeftShoulderExtraMinRLimit.LeftShoulderExtraMinRLimitz

    LeftShoulderExtraMaxRLimit = LeftShoulderExtraMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderExtraMaxRLimitx = LeftShoulderExtraMaxRLimit.LeftShoulderExtraMaxRLimitx
    LeftShoulderExtraMaxRLimity = LeftShoulderExtraMaxRLimit.LeftShoulderExtraMaxRLimity
    LeftShoulderExtraMaxRLimitz = LeftShoulderExtraMaxRLimit.LeftShoulderExtraMaxRLimitz

    LeftShoulderExtraMinRLimitEnablex = BoolField(default_value=False)

    LeftShoulderExtraMinRLimitEnabley = BoolField(default_value=False)

    LeftShoulderExtraMinRLimitEnablez = BoolField(default_value=False)

    LeftShoulderExtraMaxRLimitEnablex = BoolField(default_value=False)

    LeftShoulderExtraMaxRLimitEnabley = BoolField(default_value=False)

    LeftShoulderExtraMaxRLimitEnablez = BoolField(default_value=False)

    RightShoulderExtra = MessageField()

    RightShoulderExtraT = RightShoulderExtraTField(default_value=(0.0, 0.0, 0.0))
    RightShoulderExtraTx = RightShoulderExtraT.RightShoulderExtraTx
    RightShoulderExtraTy = RightShoulderExtraT.RightShoulderExtraTy
    RightShoulderExtraTz = RightShoulderExtraT.RightShoulderExtraTz

    RightShoulderExtraR = RightShoulderExtraRField(default_value=(0.0, 0.0, 0.0))
    RightShoulderExtraRx = RightShoulderExtraR.RightShoulderExtraRx
    RightShoulderExtraRy = RightShoulderExtraR.RightShoulderExtraRy
    RightShoulderExtraRz = RightShoulderExtraR.RightShoulderExtraRz

    RightShoulderExtraS = RightShoulderExtraSField(default_value=(1.0, 1.0, 1.0))
    RightShoulderExtraSx = RightShoulderExtraS.RightShoulderExtraSx
    RightShoulderExtraSy = RightShoulderExtraS.RightShoulderExtraSy
    RightShoulderExtraSz = RightShoulderExtraS.RightShoulderExtraSz

    RightShoulderExtraRotateOrder = RightShoulderExtraRotateOrderEnumField(default_value=0)

    RightShoulderExtraRotateAxis = RightShoulderExtraRotateAxisField(default_value=(0.0, 0.0, 0.0))
    RightShoulderExtraRotateAxisx = RightShoulderExtraRotateAxis.RightShoulderExtraRotateAxisx
    RightShoulderExtraRotateAxisy = RightShoulderExtraRotateAxis.RightShoulderExtraRotateAxisy
    RightShoulderExtraRotateAxisz = RightShoulderExtraRotateAxis.RightShoulderExtraRotateAxisz

    RightShoulderExtraJointOrient = RightShoulderExtraJointOrientField(default_value=(0.0, 0.0, 0.0))
    RightShoulderExtraJointOrientx = RightShoulderExtraJointOrient.RightShoulderExtraJointOrientx
    RightShoulderExtraJointOrienty = RightShoulderExtraJointOrient.RightShoulderExtraJointOrienty
    RightShoulderExtraJointOrientz = RightShoulderExtraJointOrient.RightShoulderExtraJointOrientz

    RightShoulderExtraMinRLimit = RightShoulderExtraMinRLimitField(default_value=(0.0, 0.0, 0.0))
    RightShoulderExtraMinRLimitx = RightShoulderExtraMinRLimit.RightShoulderExtraMinRLimitx
    RightShoulderExtraMinRLimity = RightShoulderExtraMinRLimit.RightShoulderExtraMinRLimity
    RightShoulderExtraMinRLimitz = RightShoulderExtraMinRLimit.RightShoulderExtraMinRLimitz

    RightShoulderExtraMaxRLimit = RightShoulderExtraMaxRLimitField(default_value=(0.0, 0.0, 0.0))
    RightShoulderExtraMaxRLimitx = RightShoulderExtraMaxRLimit.RightShoulderExtraMaxRLimitx
    RightShoulderExtraMaxRLimity = RightShoulderExtraMaxRLimit.RightShoulderExtraMaxRLimity
    RightShoulderExtraMaxRLimitz = RightShoulderExtraMaxRLimit.RightShoulderExtraMaxRLimitz

    RightShoulderExtraMinRLimitEnablex = BoolField(default_value=False)

    RightShoulderExtraMinRLimitEnabley = BoolField(default_value=False)

    RightShoulderExtraMinRLimitEnablez = BoolField(default_value=False)

    RightShoulderExtraMaxRLimitEnablex = BoolField(default_value=False)

    RightShoulderExtraMaxRLimitEnabley = BoolField(default_value=False)

    RightShoulderExtraMaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftUpLegRoll1 = MessageField()

    LeafLeftUpLegRoll1T = LeafLeftUpLegRoll1TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll1Tx = LeafLeftUpLegRoll1T.LeafLeftUpLegRoll1Tx
    LeafLeftUpLegRoll1Ty = LeafLeftUpLegRoll1T.LeafLeftUpLegRoll1Ty
    LeafLeftUpLegRoll1Tz = LeafLeftUpLegRoll1T.LeafLeftUpLegRoll1Tz

    LeafLeftUpLegRoll1R = LeafLeftUpLegRoll1RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll1Rx = LeafLeftUpLegRoll1R.LeafLeftUpLegRoll1Rx
    LeafLeftUpLegRoll1Ry = LeafLeftUpLegRoll1R.LeafLeftUpLegRoll1Ry
    LeafLeftUpLegRoll1Rz = LeafLeftUpLegRoll1R.LeafLeftUpLegRoll1Rz

    LeafLeftUpLegRoll1S = LeafLeftUpLegRoll1SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftUpLegRoll1Sx = LeafLeftUpLegRoll1S.LeafLeftUpLegRoll1Sx
    LeafLeftUpLegRoll1Sy = LeafLeftUpLegRoll1S.LeafLeftUpLegRoll1Sy
    LeafLeftUpLegRoll1Sz = LeafLeftUpLegRoll1S.LeafLeftUpLegRoll1Sz

    LeafLeftUpLegRoll1RotateOrder = LeafLeftUpLegRoll1RotateOrderEnumField(default_value=0)

    LeafLeftUpLegRoll1RotateAxis = LeafLeftUpLegRoll1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll1RotateAxisx = LeafLeftUpLegRoll1RotateAxis.LeafLeftUpLegRoll1RotateAxisx
    LeafLeftUpLegRoll1RotateAxisy = LeafLeftUpLegRoll1RotateAxis.LeafLeftUpLegRoll1RotateAxisy
    LeafLeftUpLegRoll1RotateAxisz = LeafLeftUpLegRoll1RotateAxis.LeafLeftUpLegRoll1RotateAxisz

    LeafLeftUpLegRoll1JointOrient = LeafLeftUpLegRoll1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll1JointOrientx = LeafLeftUpLegRoll1JointOrient.LeafLeftUpLegRoll1JointOrientx
    LeafLeftUpLegRoll1JointOrienty = LeafLeftUpLegRoll1JointOrient.LeafLeftUpLegRoll1JointOrienty
    LeafLeftUpLegRoll1JointOrientz = LeafLeftUpLegRoll1JointOrient.LeafLeftUpLegRoll1JointOrientz

    LeafLeftUpLegRoll1MinRLimit = LeafLeftUpLegRoll1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll1MinRLimitx = LeafLeftUpLegRoll1MinRLimit.LeafLeftUpLegRoll1MinRLimitx
    LeafLeftUpLegRoll1MinRLimity = LeafLeftUpLegRoll1MinRLimit.LeafLeftUpLegRoll1MinRLimity
    LeafLeftUpLegRoll1MinRLimitz = LeafLeftUpLegRoll1MinRLimit.LeafLeftUpLegRoll1MinRLimitz

    LeafLeftUpLegRoll1MaxRLimit = LeafLeftUpLegRoll1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll1MaxRLimitx = LeafLeftUpLegRoll1MaxRLimit.LeafLeftUpLegRoll1MaxRLimitx
    LeafLeftUpLegRoll1MaxRLimity = LeafLeftUpLegRoll1MaxRLimit.LeafLeftUpLegRoll1MaxRLimity
    LeafLeftUpLegRoll1MaxRLimitz = LeafLeftUpLegRoll1MaxRLimit.LeafLeftUpLegRoll1MaxRLimitz

    LeafLeftUpLegRoll1MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftUpLegRoll1MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftUpLegRoll1MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftUpLegRoll1MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftUpLegRoll1MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftUpLegRoll1MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftLegRoll1 = MessageField()

    LeafLeftLegRoll1T = LeafLeftLegRoll1TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll1Tx = LeafLeftLegRoll1T.LeafLeftLegRoll1Tx
    LeafLeftLegRoll1Ty = LeafLeftLegRoll1T.LeafLeftLegRoll1Ty
    LeafLeftLegRoll1Tz = LeafLeftLegRoll1T.LeafLeftLegRoll1Tz

    LeafLeftLegRoll1R = LeafLeftLegRoll1RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll1Rx = LeafLeftLegRoll1R.LeafLeftLegRoll1Rx
    LeafLeftLegRoll1Ry = LeafLeftLegRoll1R.LeafLeftLegRoll1Ry
    LeafLeftLegRoll1Rz = LeafLeftLegRoll1R.LeafLeftLegRoll1Rz

    LeafLeftLegRoll1S = LeafLeftLegRoll1SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftLegRoll1Sx = LeafLeftLegRoll1S.LeafLeftLegRoll1Sx
    LeafLeftLegRoll1Sy = LeafLeftLegRoll1S.LeafLeftLegRoll1Sy
    LeafLeftLegRoll1Sz = LeafLeftLegRoll1S.LeafLeftLegRoll1Sz

    LeafLeftLegRoll1RotateOrder = LeafLeftLegRoll1RotateOrderEnumField(default_value=0)

    LeafLeftLegRoll1RotateAxis = LeafLeftLegRoll1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll1RotateAxisx = LeafLeftLegRoll1RotateAxis.LeafLeftLegRoll1RotateAxisx
    LeafLeftLegRoll1RotateAxisy = LeafLeftLegRoll1RotateAxis.LeafLeftLegRoll1RotateAxisy
    LeafLeftLegRoll1RotateAxisz = LeafLeftLegRoll1RotateAxis.LeafLeftLegRoll1RotateAxisz

    LeafLeftLegRoll1JointOrient = LeafLeftLegRoll1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll1JointOrientx = LeafLeftLegRoll1JointOrient.LeafLeftLegRoll1JointOrientx
    LeafLeftLegRoll1JointOrienty = LeafLeftLegRoll1JointOrient.LeafLeftLegRoll1JointOrienty
    LeafLeftLegRoll1JointOrientz = LeafLeftLegRoll1JointOrient.LeafLeftLegRoll1JointOrientz

    LeafLeftLegRoll1MinRLimit = LeafLeftLegRoll1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll1MinRLimitx = LeafLeftLegRoll1MinRLimit.LeafLeftLegRoll1MinRLimitx
    LeafLeftLegRoll1MinRLimity = LeafLeftLegRoll1MinRLimit.LeafLeftLegRoll1MinRLimity
    LeafLeftLegRoll1MinRLimitz = LeafLeftLegRoll1MinRLimit.LeafLeftLegRoll1MinRLimitz

    LeafLeftLegRoll1MaxRLimit = LeafLeftLegRoll1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll1MaxRLimitx = LeafLeftLegRoll1MaxRLimit.LeafLeftLegRoll1MaxRLimitx
    LeafLeftLegRoll1MaxRLimity = LeafLeftLegRoll1MaxRLimit.LeafLeftLegRoll1MaxRLimity
    LeafLeftLegRoll1MaxRLimitz = LeafLeftLegRoll1MaxRLimit.LeafLeftLegRoll1MaxRLimitz

    LeafLeftLegRoll1MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftLegRoll1MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftLegRoll1MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftLegRoll1MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftLegRoll1MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftLegRoll1MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightUpLegRoll1 = MessageField()

    LeafRightUpLegRoll1T = LeafRightUpLegRoll1TField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll1Tx = LeafRightUpLegRoll1T.LeafRightUpLegRoll1Tx
    LeafRightUpLegRoll1Ty = LeafRightUpLegRoll1T.LeafRightUpLegRoll1Ty
    LeafRightUpLegRoll1Tz = LeafRightUpLegRoll1T.LeafRightUpLegRoll1Tz

    LeafRightUpLegRoll1R = LeafRightUpLegRoll1RField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll1Rx = LeafRightUpLegRoll1R.LeafRightUpLegRoll1Rx
    LeafRightUpLegRoll1Ry = LeafRightUpLegRoll1R.LeafRightUpLegRoll1Ry
    LeafRightUpLegRoll1Rz = LeafRightUpLegRoll1R.LeafRightUpLegRoll1Rz

    LeafRightUpLegRoll1S = LeafRightUpLegRoll1SField(default_value=(1.0, 1.0, 1.0))
    LeafRightUpLegRoll1Sx = LeafRightUpLegRoll1S.LeafRightUpLegRoll1Sx
    LeafRightUpLegRoll1Sy = LeafRightUpLegRoll1S.LeafRightUpLegRoll1Sy
    LeafRightUpLegRoll1Sz = LeafRightUpLegRoll1S.LeafRightUpLegRoll1Sz

    LeafRightUpLegRoll1RotateOrder = LeafRightUpLegRoll1RotateOrderEnumField(default_value=0)

    LeafRightUpLegRoll1RotateAxis = LeafRightUpLegRoll1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll1RotateAxisx = LeafRightUpLegRoll1RotateAxis.LeafRightUpLegRoll1RotateAxisx
    LeafRightUpLegRoll1RotateAxisy = LeafRightUpLegRoll1RotateAxis.LeafRightUpLegRoll1RotateAxisy
    LeafRightUpLegRoll1RotateAxisz = LeafRightUpLegRoll1RotateAxis.LeafRightUpLegRoll1RotateAxisz

    LeafRightUpLegRoll1JointOrient = LeafRightUpLegRoll1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll1JointOrientx = LeafRightUpLegRoll1JointOrient.LeafRightUpLegRoll1JointOrientx
    LeafRightUpLegRoll1JointOrienty = LeafRightUpLegRoll1JointOrient.LeafRightUpLegRoll1JointOrienty
    LeafRightUpLegRoll1JointOrientz = LeafRightUpLegRoll1JointOrient.LeafRightUpLegRoll1JointOrientz

    LeafRightUpLegRoll1MinRLimit = LeafRightUpLegRoll1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll1MinRLimitx = LeafRightUpLegRoll1MinRLimit.LeafRightUpLegRoll1MinRLimitx
    LeafRightUpLegRoll1MinRLimity = LeafRightUpLegRoll1MinRLimit.LeafRightUpLegRoll1MinRLimity
    LeafRightUpLegRoll1MinRLimitz = LeafRightUpLegRoll1MinRLimit.LeafRightUpLegRoll1MinRLimitz

    LeafRightUpLegRoll1MaxRLimit = LeafRightUpLegRoll1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll1MaxRLimitx = LeafRightUpLegRoll1MaxRLimit.LeafRightUpLegRoll1MaxRLimitx
    LeafRightUpLegRoll1MaxRLimity = LeafRightUpLegRoll1MaxRLimit.LeafRightUpLegRoll1MaxRLimity
    LeafRightUpLegRoll1MaxRLimitz = LeafRightUpLegRoll1MaxRLimit.LeafRightUpLegRoll1MaxRLimitz

    LeafRightUpLegRoll1MinRLimitEnablex = BoolField(default_value=False)

    LeafRightUpLegRoll1MinRLimitEnabley = BoolField(default_value=False)

    LeafRightUpLegRoll1MinRLimitEnablez = BoolField(default_value=False)

    LeafRightUpLegRoll1MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightUpLegRoll1MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightUpLegRoll1MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightLegRoll1 = MessageField()

    LeafRightLegRoll1T = LeafRightLegRoll1TField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll1Tx = LeafRightLegRoll1T.LeafRightLegRoll1Tx
    LeafRightLegRoll1Ty = LeafRightLegRoll1T.LeafRightLegRoll1Ty
    LeafRightLegRoll1Tz = LeafRightLegRoll1T.LeafRightLegRoll1Tz

    LeafRightLegRoll1R = LeafRightLegRoll1RField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll1Rx = LeafRightLegRoll1R.LeafRightLegRoll1Rx
    LeafRightLegRoll1Ry = LeafRightLegRoll1R.LeafRightLegRoll1Ry
    LeafRightLegRoll1Rz = LeafRightLegRoll1R.LeafRightLegRoll1Rz

    LeafRightLegRoll1S = LeafRightLegRoll1SField(default_value=(1.0, 1.0, 1.0))
    LeafRightLegRoll1Sx = LeafRightLegRoll1S.LeafRightLegRoll1Sx
    LeafRightLegRoll1Sy = LeafRightLegRoll1S.LeafRightLegRoll1Sy
    LeafRightLegRoll1Sz = LeafRightLegRoll1S.LeafRightLegRoll1Sz

    LeafRightLegRoll1RotateOrder = LeafRightLegRoll1RotateOrderEnumField(default_value=0)

    LeafRightLegRoll1RotateAxis = LeafRightLegRoll1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll1RotateAxisx = LeafRightLegRoll1RotateAxis.LeafRightLegRoll1RotateAxisx
    LeafRightLegRoll1RotateAxisy = LeafRightLegRoll1RotateAxis.LeafRightLegRoll1RotateAxisy
    LeafRightLegRoll1RotateAxisz = LeafRightLegRoll1RotateAxis.LeafRightLegRoll1RotateAxisz

    LeafRightLegRoll1JointOrient = LeafRightLegRoll1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll1JointOrientx = LeafRightLegRoll1JointOrient.LeafRightLegRoll1JointOrientx
    LeafRightLegRoll1JointOrienty = LeafRightLegRoll1JointOrient.LeafRightLegRoll1JointOrienty
    LeafRightLegRoll1JointOrientz = LeafRightLegRoll1JointOrient.LeafRightLegRoll1JointOrientz

    LeafRightLegRoll1MinRLimit = LeafRightLegRoll1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll1MinRLimitx = LeafRightLegRoll1MinRLimit.LeafRightLegRoll1MinRLimitx
    LeafRightLegRoll1MinRLimity = LeafRightLegRoll1MinRLimit.LeafRightLegRoll1MinRLimity
    LeafRightLegRoll1MinRLimitz = LeafRightLegRoll1MinRLimit.LeafRightLegRoll1MinRLimitz

    LeafRightLegRoll1MaxRLimit = LeafRightLegRoll1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll1MaxRLimitx = LeafRightLegRoll1MaxRLimit.LeafRightLegRoll1MaxRLimitx
    LeafRightLegRoll1MaxRLimity = LeafRightLegRoll1MaxRLimit.LeafRightLegRoll1MaxRLimity
    LeafRightLegRoll1MaxRLimitz = LeafRightLegRoll1MaxRLimit.LeafRightLegRoll1MaxRLimitz

    LeafRightLegRoll1MinRLimitEnablex = BoolField(default_value=False)

    LeafRightLegRoll1MinRLimitEnabley = BoolField(default_value=False)

    LeafRightLegRoll1MinRLimitEnablez = BoolField(default_value=False)

    LeafRightLegRoll1MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightLegRoll1MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightLegRoll1MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftArmRoll1 = MessageField()

    LeafLeftArmRoll1T = LeafLeftArmRoll1TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll1Tx = LeafLeftArmRoll1T.LeafLeftArmRoll1Tx
    LeafLeftArmRoll1Ty = LeafLeftArmRoll1T.LeafLeftArmRoll1Ty
    LeafLeftArmRoll1Tz = LeafLeftArmRoll1T.LeafLeftArmRoll1Tz

    LeafLeftArmRoll1R = LeafLeftArmRoll1RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll1Rx = LeafLeftArmRoll1R.LeafLeftArmRoll1Rx
    LeafLeftArmRoll1Ry = LeafLeftArmRoll1R.LeafLeftArmRoll1Ry
    LeafLeftArmRoll1Rz = LeafLeftArmRoll1R.LeafLeftArmRoll1Rz

    LeafLeftArmRoll1S = LeafLeftArmRoll1SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftArmRoll1Sx = LeafLeftArmRoll1S.LeafLeftArmRoll1Sx
    LeafLeftArmRoll1Sy = LeafLeftArmRoll1S.LeafLeftArmRoll1Sy
    LeafLeftArmRoll1Sz = LeafLeftArmRoll1S.LeafLeftArmRoll1Sz

    LeafLeftArmRoll1RotateOrder = LeafLeftArmRoll1RotateOrderEnumField(default_value=0)

    LeafLeftArmRoll1RotateAxis = LeafLeftArmRoll1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll1RotateAxisx = LeafLeftArmRoll1RotateAxis.LeafLeftArmRoll1RotateAxisx
    LeafLeftArmRoll1RotateAxisy = LeafLeftArmRoll1RotateAxis.LeafLeftArmRoll1RotateAxisy
    LeafLeftArmRoll1RotateAxisz = LeafLeftArmRoll1RotateAxis.LeafLeftArmRoll1RotateAxisz

    LeafLeftArmRoll1JointOrient = LeafLeftArmRoll1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll1JointOrientx = LeafLeftArmRoll1JointOrient.LeafLeftArmRoll1JointOrientx
    LeafLeftArmRoll1JointOrienty = LeafLeftArmRoll1JointOrient.LeafLeftArmRoll1JointOrienty
    LeafLeftArmRoll1JointOrientz = LeafLeftArmRoll1JointOrient.LeafLeftArmRoll1JointOrientz

    LeafLeftArmRoll1MinRLimit = LeafLeftArmRoll1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll1MinRLimitx = LeafLeftArmRoll1MinRLimit.LeafLeftArmRoll1MinRLimitx
    LeafLeftArmRoll1MinRLimity = LeafLeftArmRoll1MinRLimit.LeafLeftArmRoll1MinRLimity
    LeafLeftArmRoll1MinRLimitz = LeafLeftArmRoll1MinRLimit.LeafLeftArmRoll1MinRLimitz

    LeafLeftArmRoll1MaxRLimit = LeafLeftArmRoll1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll1MaxRLimitx = LeafLeftArmRoll1MaxRLimit.LeafLeftArmRoll1MaxRLimitx
    LeafLeftArmRoll1MaxRLimity = LeafLeftArmRoll1MaxRLimit.LeafLeftArmRoll1MaxRLimity
    LeafLeftArmRoll1MaxRLimitz = LeafLeftArmRoll1MaxRLimit.LeafLeftArmRoll1MaxRLimitz

    LeafLeftArmRoll1MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftArmRoll1MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftArmRoll1MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftArmRoll1MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftArmRoll1MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftArmRoll1MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftForeArmRoll1 = MessageField()

    LeafLeftForeArmRoll1T = LeafLeftForeArmRoll1TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll1Tx = LeafLeftForeArmRoll1T.LeafLeftForeArmRoll1Tx
    LeafLeftForeArmRoll1Ty = LeafLeftForeArmRoll1T.LeafLeftForeArmRoll1Ty
    LeafLeftForeArmRoll1Tz = LeafLeftForeArmRoll1T.LeafLeftForeArmRoll1Tz

    LeafLeftForeArmRoll1R = LeafLeftForeArmRoll1RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll1Rx = LeafLeftForeArmRoll1R.LeafLeftForeArmRoll1Rx
    LeafLeftForeArmRoll1Ry = LeafLeftForeArmRoll1R.LeafLeftForeArmRoll1Ry
    LeafLeftForeArmRoll1Rz = LeafLeftForeArmRoll1R.LeafLeftForeArmRoll1Rz

    LeafLeftForeArmRoll1S = LeafLeftForeArmRoll1SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftForeArmRoll1Sx = LeafLeftForeArmRoll1S.LeafLeftForeArmRoll1Sx
    LeafLeftForeArmRoll1Sy = LeafLeftForeArmRoll1S.LeafLeftForeArmRoll1Sy
    LeafLeftForeArmRoll1Sz = LeafLeftForeArmRoll1S.LeafLeftForeArmRoll1Sz

    LeafLeftForeArmRoll1RotateOrder = LeafLeftForeArmRoll1RotateOrderEnumField(default_value=0)

    LeafLeftForeArmRoll1RotateAxis = LeafLeftForeArmRoll1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll1RotateAxisx = LeafLeftForeArmRoll1RotateAxis.LeafLeftForeArmRoll1RotateAxisx
    LeafLeftForeArmRoll1RotateAxisy = LeafLeftForeArmRoll1RotateAxis.LeafLeftForeArmRoll1RotateAxisy
    LeafLeftForeArmRoll1RotateAxisz = LeafLeftForeArmRoll1RotateAxis.LeafLeftForeArmRoll1RotateAxisz

    LeafLeftForeArmRoll1JointOrient = LeafLeftForeArmRoll1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll1JointOrientx = LeafLeftForeArmRoll1JointOrient.LeafLeftForeArmRoll1JointOrientx
    LeafLeftForeArmRoll1JointOrienty = LeafLeftForeArmRoll1JointOrient.LeafLeftForeArmRoll1JointOrienty
    LeafLeftForeArmRoll1JointOrientz = LeafLeftForeArmRoll1JointOrient.LeafLeftForeArmRoll1JointOrientz

    LeafLeftForeArmRoll1MinRLimit = LeafLeftForeArmRoll1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll1MinRLimitx = LeafLeftForeArmRoll1MinRLimit.LeafLeftForeArmRoll1MinRLimitx
    LeafLeftForeArmRoll1MinRLimity = LeafLeftForeArmRoll1MinRLimit.LeafLeftForeArmRoll1MinRLimity
    LeafLeftForeArmRoll1MinRLimitz = LeafLeftForeArmRoll1MinRLimit.LeafLeftForeArmRoll1MinRLimitz

    LeafLeftForeArmRoll1MaxRLimit = LeafLeftForeArmRoll1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll1MaxRLimitx = LeafLeftForeArmRoll1MaxRLimit.LeafLeftForeArmRoll1MaxRLimitx
    LeafLeftForeArmRoll1MaxRLimity = LeafLeftForeArmRoll1MaxRLimit.LeafLeftForeArmRoll1MaxRLimity
    LeafLeftForeArmRoll1MaxRLimitz = LeafLeftForeArmRoll1MaxRLimit.LeafLeftForeArmRoll1MaxRLimitz

    LeafLeftForeArmRoll1MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftForeArmRoll1MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftForeArmRoll1MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftForeArmRoll1MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftForeArmRoll1MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftForeArmRoll1MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightArmRoll1 = MessageField()

    LeafRightArmRoll1T = LeafRightArmRoll1TField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll1Tx = LeafRightArmRoll1T.LeafRightArmRoll1Tx
    LeafRightArmRoll1Ty = LeafRightArmRoll1T.LeafRightArmRoll1Ty
    LeafRightArmRoll1Tz = LeafRightArmRoll1T.LeafRightArmRoll1Tz

    LeafRightArmRoll1R = LeafRightArmRoll1RField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll1Rx = LeafRightArmRoll1R.LeafRightArmRoll1Rx
    LeafRightArmRoll1Ry = LeafRightArmRoll1R.LeafRightArmRoll1Ry
    LeafRightArmRoll1Rz = LeafRightArmRoll1R.LeafRightArmRoll1Rz

    LeafRightArmRoll1S = LeafRightArmRoll1SField(default_value=(1.0, 1.0, 1.0))
    LeafRightArmRoll1Sx = LeafRightArmRoll1S.LeafRightArmRoll1Sx
    LeafRightArmRoll1Sy = LeafRightArmRoll1S.LeafRightArmRoll1Sy
    LeafRightArmRoll1Sz = LeafRightArmRoll1S.LeafRightArmRoll1Sz

    LeafRightArmRoll1RotateOrder = LeafRightArmRoll1RotateOrderEnumField(default_value=0)

    LeafRightArmRoll1RotateAxis = LeafRightArmRoll1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll1RotateAxisx = LeafRightArmRoll1RotateAxis.LeafRightArmRoll1RotateAxisx
    LeafRightArmRoll1RotateAxisy = LeafRightArmRoll1RotateAxis.LeafRightArmRoll1RotateAxisy
    LeafRightArmRoll1RotateAxisz = LeafRightArmRoll1RotateAxis.LeafRightArmRoll1RotateAxisz

    LeafRightArmRoll1JointOrient = LeafRightArmRoll1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll1JointOrientx = LeafRightArmRoll1JointOrient.LeafRightArmRoll1JointOrientx
    LeafRightArmRoll1JointOrienty = LeafRightArmRoll1JointOrient.LeafRightArmRoll1JointOrienty
    LeafRightArmRoll1JointOrientz = LeafRightArmRoll1JointOrient.LeafRightArmRoll1JointOrientz

    LeafRightArmRoll1MinRLimit = LeafRightArmRoll1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll1MinRLimitx = LeafRightArmRoll1MinRLimit.LeafRightArmRoll1MinRLimitx
    LeafRightArmRoll1MinRLimity = LeafRightArmRoll1MinRLimit.LeafRightArmRoll1MinRLimity
    LeafRightArmRoll1MinRLimitz = LeafRightArmRoll1MinRLimit.LeafRightArmRoll1MinRLimitz

    LeafRightArmRoll1MaxRLimit = LeafRightArmRoll1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll1MaxRLimitx = LeafRightArmRoll1MaxRLimit.LeafRightArmRoll1MaxRLimitx
    LeafRightArmRoll1MaxRLimity = LeafRightArmRoll1MaxRLimit.LeafRightArmRoll1MaxRLimity
    LeafRightArmRoll1MaxRLimitz = LeafRightArmRoll1MaxRLimit.LeafRightArmRoll1MaxRLimitz

    LeafRightArmRoll1MinRLimitEnablex = BoolField(default_value=False)

    LeafRightArmRoll1MinRLimitEnabley = BoolField(default_value=False)

    LeafRightArmRoll1MinRLimitEnablez = BoolField(default_value=False)

    LeafRightArmRoll1MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightArmRoll1MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightArmRoll1MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightForeArmRoll1 = MessageField()

    LeafRightForeArmRoll1T = LeafRightForeArmRoll1TField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll1Tx = LeafRightForeArmRoll1T.LeafRightForeArmRoll1Tx
    LeafRightForeArmRoll1Ty = LeafRightForeArmRoll1T.LeafRightForeArmRoll1Ty
    LeafRightForeArmRoll1Tz = LeafRightForeArmRoll1T.LeafRightForeArmRoll1Tz

    LeafRightForeArmRoll1R = LeafRightForeArmRoll1RField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll1Rx = LeafRightForeArmRoll1R.LeafRightForeArmRoll1Rx
    LeafRightForeArmRoll1Ry = LeafRightForeArmRoll1R.LeafRightForeArmRoll1Ry
    LeafRightForeArmRoll1Rz = LeafRightForeArmRoll1R.LeafRightForeArmRoll1Rz

    LeafRightForeArmRoll1S = LeafRightForeArmRoll1SField(default_value=(1.0, 1.0, 1.0))
    LeafRightForeArmRoll1Sx = LeafRightForeArmRoll1S.LeafRightForeArmRoll1Sx
    LeafRightForeArmRoll1Sy = LeafRightForeArmRoll1S.LeafRightForeArmRoll1Sy
    LeafRightForeArmRoll1Sz = LeafRightForeArmRoll1S.LeafRightForeArmRoll1Sz

    LeafRightForeArmRoll1RotateOrder = LeafRightForeArmRoll1RotateOrderEnumField(default_value=0)

    LeafRightForeArmRoll1RotateAxis = LeafRightForeArmRoll1RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll1RotateAxisx = LeafRightForeArmRoll1RotateAxis.LeafRightForeArmRoll1RotateAxisx
    LeafRightForeArmRoll1RotateAxisy = LeafRightForeArmRoll1RotateAxis.LeafRightForeArmRoll1RotateAxisy
    LeafRightForeArmRoll1RotateAxisz = LeafRightForeArmRoll1RotateAxis.LeafRightForeArmRoll1RotateAxisz

    LeafRightForeArmRoll1JointOrient = LeafRightForeArmRoll1JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll1JointOrientx = LeafRightForeArmRoll1JointOrient.LeafRightForeArmRoll1JointOrientx
    LeafRightForeArmRoll1JointOrienty = LeafRightForeArmRoll1JointOrient.LeafRightForeArmRoll1JointOrienty
    LeafRightForeArmRoll1JointOrientz = LeafRightForeArmRoll1JointOrient.LeafRightForeArmRoll1JointOrientz

    LeafRightForeArmRoll1MinRLimit = LeafRightForeArmRoll1MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll1MinRLimitx = LeafRightForeArmRoll1MinRLimit.LeafRightForeArmRoll1MinRLimitx
    LeafRightForeArmRoll1MinRLimity = LeafRightForeArmRoll1MinRLimit.LeafRightForeArmRoll1MinRLimity
    LeafRightForeArmRoll1MinRLimitz = LeafRightForeArmRoll1MinRLimit.LeafRightForeArmRoll1MinRLimitz

    LeafRightForeArmRoll1MaxRLimit = LeafRightForeArmRoll1MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll1MaxRLimitx = LeafRightForeArmRoll1MaxRLimit.LeafRightForeArmRoll1MaxRLimitx
    LeafRightForeArmRoll1MaxRLimity = LeafRightForeArmRoll1MaxRLimit.LeafRightForeArmRoll1MaxRLimity
    LeafRightForeArmRoll1MaxRLimitz = LeafRightForeArmRoll1MaxRLimit.LeafRightForeArmRoll1MaxRLimitz

    LeafRightForeArmRoll1MinRLimitEnablex = BoolField(default_value=False)

    LeafRightForeArmRoll1MinRLimitEnabley = BoolField(default_value=False)

    LeafRightForeArmRoll1MinRLimitEnablez = BoolField(default_value=False)

    LeafRightForeArmRoll1MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightForeArmRoll1MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightForeArmRoll1MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftUpLegRoll2 = MessageField()

    LeafLeftUpLegRoll2T = LeafLeftUpLegRoll2TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll2Tx = LeafLeftUpLegRoll2T.LeafLeftUpLegRoll2Tx
    LeafLeftUpLegRoll2Ty = LeafLeftUpLegRoll2T.LeafLeftUpLegRoll2Ty
    LeafLeftUpLegRoll2Tz = LeafLeftUpLegRoll2T.LeafLeftUpLegRoll2Tz

    LeafLeftUpLegRoll2R = LeafLeftUpLegRoll2RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll2Rx = LeafLeftUpLegRoll2R.LeafLeftUpLegRoll2Rx
    LeafLeftUpLegRoll2Ry = LeafLeftUpLegRoll2R.LeafLeftUpLegRoll2Ry
    LeafLeftUpLegRoll2Rz = LeafLeftUpLegRoll2R.LeafLeftUpLegRoll2Rz

    LeafLeftUpLegRoll2S = LeafLeftUpLegRoll2SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftUpLegRoll2Sx = LeafLeftUpLegRoll2S.LeafLeftUpLegRoll2Sx
    LeafLeftUpLegRoll2Sy = LeafLeftUpLegRoll2S.LeafLeftUpLegRoll2Sy
    LeafLeftUpLegRoll2Sz = LeafLeftUpLegRoll2S.LeafLeftUpLegRoll2Sz

    LeafLeftUpLegRoll2RotateOrder = LeafLeftUpLegRoll2RotateOrderEnumField(default_value=0)

    LeafLeftUpLegRoll2RotateAxis = LeafLeftUpLegRoll2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll2RotateAxisx = LeafLeftUpLegRoll2RotateAxis.LeafLeftUpLegRoll2RotateAxisx
    LeafLeftUpLegRoll2RotateAxisy = LeafLeftUpLegRoll2RotateAxis.LeafLeftUpLegRoll2RotateAxisy
    LeafLeftUpLegRoll2RotateAxisz = LeafLeftUpLegRoll2RotateAxis.LeafLeftUpLegRoll2RotateAxisz

    LeafLeftUpLegRoll2JointOrient = LeafLeftUpLegRoll2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll2JointOrientx = LeafLeftUpLegRoll2JointOrient.LeafLeftUpLegRoll2JointOrientx
    LeafLeftUpLegRoll2JointOrienty = LeafLeftUpLegRoll2JointOrient.LeafLeftUpLegRoll2JointOrienty
    LeafLeftUpLegRoll2JointOrientz = LeafLeftUpLegRoll2JointOrient.LeafLeftUpLegRoll2JointOrientz

    LeafLeftUpLegRoll2MinRLimit = LeafLeftUpLegRoll2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll2MinRLimitx = LeafLeftUpLegRoll2MinRLimit.LeafLeftUpLegRoll2MinRLimitx
    LeafLeftUpLegRoll2MinRLimity = LeafLeftUpLegRoll2MinRLimit.LeafLeftUpLegRoll2MinRLimity
    LeafLeftUpLegRoll2MinRLimitz = LeafLeftUpLegRoll2MinRLimit.LeafLeftUpLegRoll2MinRLimitz

    LeafLeftUpLegRoll2MaxRLimit = LeafLeftUpLegRoll2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll2MaxRLimitx = LeafLeftUpLegRoll2MaxRLimit.LeafLeftUpLegRoll2MaxRLimitx
    LeafLeftUpLegRoll2MaxRLimity = LeafLeftUpLegRoll2MaxRLimit.LeafLeftUpLegRoll2MaxRLimity
    LeafLeftUpLegRoll2MaxRLimitz = LeafLeftUpLegRoll2MaxRLimit.LeafLeftUpLegRoll2MaxRLimitz

    LeafLeftUpLegRoll2MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftUpLegRoll2MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftUpLegRoll2MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftUpLegRoll2MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftUpLegRoll2MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftUpLegRoll2MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftLegRoll2 = MessageField()

    LeafLeftLegRoll2T = LeafLeftLegRoll2TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll2Tx = LeafLeftLegRoll2T.LeafLeftLegRoll2Tx
    LeafLeftLegRoll2Ty = LeafLeftLegRoll2T.LeafLeftLegRoll2Ty
    LeafLeftLegRoll2Tz = LeafLeftLegRoll2T.LeafLeftLegRoll2Tz

    LeafLeftLegRoll2R = LeafLeftLegRoll2RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll2Rx = LeafLeftLegRoll2R.LeafLeftLegRoll2Rx
    LeafLeftLegRoll2Ry = LeafLeftLegRoll2R.LeafLeftLegRoll2Ry
    LeafLeftLegRoll2Rz = LeafLeftLegRoll2R.LeafLeftLegRoll2Rz

    LeafLeftLegRoll2S = LeafLeftLegRoll2SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftLegRoll2Sx = LeafLeftLegRoll2S.LeafLeftLegRoll2Sx
    LeafLeftLegRoll2Sy = LeafLeftLegRoll2S.LeafLeftLegRoll2Sy
    LeafLeftLegRoll2Sz = LeafLeftLegRoll2S.LeafLeftLegRoll2Sz

    LeafLeftLegRoll2RotateOrder = LeafLeftLegRoll2RotateOrderEnumField(default_value=0)

    LeafLeftLegRoll2RotateAxis = LeafLeftLegRoll2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll2RotateAxisx = LeafLeftLegRoll2RotateAxis.LeafLeftLegRoll2RotateAxisx
    LeafLeftLegRoll2RotateAxisy = LeafLeftLegRoll2RotateAxis.LeafLeftLegRoll2RotateAxisy
    LeafLeftLegRoll2RotateAxisz = LeafLeftLegRoll2RotateAxis.LeafLeftLegRoll2RotateAxisz

    LeafLeftLegRoll2JointOrient = LeafLeftLegRoll2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll2JointOrientx = LeafLeftLegRoll2JointOrient.LeafLeftLegRoll2JointOrientx
    LeafLeftLegRoll2JointOrienty = LeafLeftLegRoll2JointOrient.LeafLeftLegRoll2JointOrienty
    LeafLeftLegRoll2JointOrientz = LeafLeftLegRoll2JointOrient.LeafLeftLegRoll2JointOrientz

    LeafLeftLegRoll2MinRLimit = LeafLeftLegRoll2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll2MinRLimitx = LeafLeftLegRoll2MinRLimit.LeafLeftLegRoll2MinRLimitx
    LeafLeftLegRoll2MinRLimity = LeafLeftLegRoll2MinRLimit.LeafLeftLegRoll2MinRLimity
    LeafLeftLegRoll2MinRLimitz = LeafLeftLegRoll2MinRLimit.LeafLeftLegRoll2MinRLimitz

    LeafLeftLegRoll2MaxRLimit = LeafLeftLegRoll2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll2MaxRLimitx = LeafLeftLegRoll2MaxRLimit.LeafLeftLegRoll2MaxRLimitx
    LeafLeftLegRoll2MaxRLimity = LeafLeftLegRoll2MaxRLimit.LeafLeftLegRoll2MaxRLimity
    LeafLeftLegRoll2MaxRLimitz = LeafLeftLegRoll2MaxRLimit.LeafLeftLegRoll2MaxRLimitz

    LeafLeftLegRoll2MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftLegRoll2MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftLegRoll2MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftLegRoll2MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftLegRoll2MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftLegRoll2MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightUpLegRoll2 = MessageField()

    LeafRightUpLegRoll2T = LeafRightUpLegRoll2TField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll2Tx = LeafRightUpLegRoll2T.LeafRightUpLegRoll2Tx
    LeafRightUpLegRoll2Ty = LeafRightUpLegRoll2T.LeafRightUpLegRoll2Ty
    LeafRightUpLegRoll2Tz = LeafRightUpLegRoll2T.LeafRightUpLegRoll2Tz

    LeafRightUpLegRoll2R = LeafRightUpLegRoll2RField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll2Rx = LeafRightUpLegRoll2R.LeafRightUpLegRoll2Rx
    LeafRightUpLegRoll2Ry = LeafRightUpLegRoll2R.LeafRightUpLegRoll2Ry
    LeafRightUpLegRoll2Rz = LeafRightUpLegRoll2R.LeafRightUpLegRoll2Rz

    LeafRightUpLegRoll2S = LeafRightUpLegRoll2SField(default_value=(1.0, 1.0, 1.0))
    LeafRightUpLegRoll2Sx = LeafRightUpLegRoll2S.LeafRightUpLegRoll2Sx
    LeafRightUpLegRoll2Sy = LeafRightUpLegRoll2S.LeafRightUpLegRoll2Sy
    LeafRightUpLegRoll2Sz = LeafRightUpLegRoll2S.LeafRightUpLegRoll2Sz

    LeafRightUpLegRoll2RotateOrder = LeafRightUpLegRoll2RotateOrderEnumField(default_value=0)

    LeafRightUpLegRoll2RotateAxis = LeafRightUpLegRoll2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll2RotateAxisx = LeafRightUpLegRoll2RotateAxis.LeafRightUpLegRoll2RotateAxisx
    LeafRightUpLegRoll2RotateAxisy = LeafRightUpLegRoll2RotateAxis.LeafRightUpLegRoll2RotateAxisy
    LeafRightUpLegRoll2RotateAxisz = LeafRightUpLegRoll2RotateAxis.LeafRightUpLegRoll2RotateAxisz

    LeafRightUpLegRoll2JointOrient = LeafRightUpLegRoll2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll2JointOrientx = LeafRightUpLegRoll2JointOrient.LeafRightUpLegRoll2JointOrientx
    LeafRightUpLegRoll2JointOrienty = LeafRightUpLegRoll2JointOrient.LeafRightUpLegRoll2JointOrienty
    LeafRightUpLegRoll2JointOrientz = LeafRightUpLegRoll2JointOrient.LeafRightUpLegRoll2JointOrientz

    LeafRightUpLegRoll2MinRLimit = LeafRightUpLegRoll2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll2MinRLimitx = LeafRightUpLegRoll2MinRLimit.LeafRightUpLegRoll2MinRLimitx
    LeafRightUpLegRoll2MinRLimity = LeafRightUpLegRoll2MinRLimit.LeafRightUpLegRoll2MinRLimity
    LeafRightUpLegRoll2MinRLimitz = LeafRightUpLegRoll2MinRLimit.LeafRightUpLegRoll2MinRLimitz

    LeafRightUpLegRoll2MaxRLimit = LeafRightUpLegRoll2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll2MaxRLimitx = LeafRightUpLegRoll2MaxRLimit.LeafRightUpLegRoll2MaxRLimitx
    LeafRightUpLegRoll2MaxRLimity = LeafRightUpLegRoll2MaxRLimit.LeafRightUpLegRoll2MaxRLimity
    LeafRightUpLegRoll2MaxRLimitz = LeafRightUpLegRoll2MaxRLimit.LeafRightUpLegRoll2MaxRLimitz

    LeafRightUpLegRoll2MinRLimitEnablex = BoolField(default_value=False)

    LeafRightUpLegRoll2MinRLimitEnabley = BoolField(default_value=False)

    LeafRightUpLegRoll2MinRLimitEnablez = BoolField(default_value=False)

    LeafRightUpLegRoll2MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightUpLegRoll2MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightUpLegRoll2MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightLegRoll2 = MessageField()

    LeafRightLegRoll2T = LeafRightLegRoll2TField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll2Tx = LeafRightLegRoll2T.LeafRightLegRoll2Tx
    LeafRightLegRoll2Ty = LeafRightLegRoll2T.LeafRightLegRoll2Ty
    LeafRightLegRoll2Tz = LeafRightLegRoll2T.LeafRightLegRoll2Tz

    LeafRightLegRoll2R = LeafRightLegRoll2RField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll2Rx = LeafRightLegRoll2R.LeafRightLegRoll2Rx
    LeafRightLegRoll2Ry = LeafRightLegRoll2R.LeafRightLegRoll2Ry
    LeafRightLegRoll2Rz = LeafRightLegRoll2R.LeafRightLegRoll2Rz

    LeafRightLegRoll2S = LeafRightLegRoll2SField(default_value=(1.0, 1.0, 1.0))
    LeafRightLegRoll2Sx = LeafRightLegRoll2S.LeafRightLegRoll2Sx
    LeafRightLegRoll2Sy = LeafRightLegRoll2S.LeafRightLegRoll2Sy
    LeafRightLegRoll2Sz = LeafRightLegRoll2S.LeafRightLegRoll2Sz

    LeafRightLegRoll2RotateOrder = LeafRightLegRoll2RotateOrderEnumField(default_value=0)

    LeafRightLegRoll2RotateAxis = LeafRightLegRoll2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll2RotateAxisx = LeafRightLegRoll2RotateAxis.LeafRightLegRoll2RotateAxisx
    LeafRightLegRoll2RotateAxisy = LeafRightLegRoll2RotateAxis.LeafRightLegRoll2RotateAxisy
    LeafRightLegRoll2RotateAxisz = LeafRightLegRoll2RotateAxis.LeafRightLegRoll2RotateAxisz

    LeafRightLegRoll2JointOrient = LeafRightLegRoll2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll2JointOrientx = LeafRightLegRoll2JointOrient.LeafRightLegRoll2JointOrientx
    LeafRightLegRoll2JointOrienty = LeafRightLegRoll2JointOrient.LeafRightLegRoll2JointOrienty
    LeafRightLegRoll2JointOrientz = LeafRightLegRoll2JointOrient.LeafRightLegRoll2JointOrientz

    LeafRightLegRoll2MinRLimit = LeafRightLegRoll2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll2MinRLimitx = LeafRightLegRoll2MinRLimit.LeafRightLegRoll2MinRLimitx
    LeafRightLegRoll2MinRLimity = LeafRightLegRoll2MinRLimit.LeafRightLegRoll2MinRLimity
    LeafRightLegRoll2MinRLimitz = LeafRightLegRoll2MinRLimit.LeafRightLegRoll2MinRLimitz

    LeafRightLegRoll2MaxRLimit = LeafRightLegRoll2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll2MaxRLimitx = LeafRightLegRoll2MaxRLimit.LeafRightLegRoll2MaxRLimitx
    LeafRightLegRoll2MaxRLimity = LeafRightLegRoll2MaxRLimit.LeafRightLegRoll2MaxRLimity
    LeafRightLegRoll2MaxRLimitz = LeafRightLegRoll2MaxRLimit.LeafRightLegRoll2MaxRLimitz

    LeafRightLegRoll2MinRLimitEnablex = BoolField(default_value=False)

    LeafRightLegRoll2MinRLimitEnabley = BoolField(default_value=False)

    LeafRightLegRoll2MinRLimitEnablez = BoolField(default_value=False)

    LeafRightLegRoll2MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightLegRoll2MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightLegRoll2MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftArmRoll2 = MessageField()

    LeafLeftArmRoll2T = LeafLeftArmRoll2TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll2Tx = LeafLeftArmRoll2T.LeafLeftArmRoll2Tx
    LeafLeftArmRoll2Ty = LeafLeftArmRoll2T.LeafLeftArmRoll2Ty
    LeafLeftArmRoll2Tz = LeafLeftArmRoll2T.LeafLeftArmRoll2Tz

    LeafLeftArmRoll2R = LeafLeftArmRoll2RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll2Rx = LeafLeftArmRoll2R.LeafLeftArmRoll2Rx
    LeafLeftArmRoll2Ry = LeafLeftArmRoll2R.LeafLeftArmRoll2Ry
    LeafLeftArmRoll2Rz = LeafLeftArmRoll2R.LeafLeftArmRoll2Rz

    LeafLeftArmRoll2S = LeafLeftArmRoll2SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftArmRoll2Sx = LeafLeftArmRoll2S.LeafLeftArmRoll2Sx
    LeafLeftArmRoll2Sy = LeafLeftArmRoll2S.LeafLeftArmRoll2Sy
    LeafLeftArmRoll2Sz = LeafLeftArmRoll2S.LeafLeftArmRoll2Sz

    LeafLeftArmRoll2RotateOrder = LeafLeftArmRoll2RotateOrderEnumField(default_value=0)

    LeafLeftArmRoll2RotateAxis = LeafLeftArmRoll2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll2RotateAxisx = LeafLeftArmRoll2RotateAxis.LeafLeftArmRoll2RotateAxisx
    LeafLeftArmRoll2RotateAxisy = LeafLeftArmRoll2RotateAxis.LeafLeftArmRoll2RotateAxisy
    LeafLeftArmRoll2RotateAxisz = LeafLeftArmRoll2RotateAxis.LeafLeftArmRoll2RotateAxisz

    LeafLeftArmRoll2JointOrient = LeafLeftArmRoll2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll2JointOrientx = LeafLeftArmRoll2JointOrient.LeafLeftArmRoll2JointOrientx
    LeafLeftArmRoll2JointOrienty = LeafLeftArmRoll2JointOrient.LeafLeftArmRoll2JointOrienty
    LeafLeftArmRoll2JointOrientz = LeafLeftArmRoll2JointOrient.LeafLeftArmRoll2JointOrientz

    LeafLeftArmRoll2MinRLimit = LeafLeftArmRoll2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll2MinRLimitx = LeafLeftArmRoll2MinRLimit.LeafLeftArmRoll2MinRLimitx
    LeafLeftArmRoll2MinRLimity = LeafLeftArmRoll2MinRLimit.LeafLeftArmRoll2MinRLimity
    LeafLeftArmRoll2MinRLimitz = LeafLeftArmRoll2MinRLimit.LeafLeftArmRoll2MinRLimitz

    LeafLeftArmRoll2MaxRLimit = LeafLeftArmRoll2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll2MaxRLimitx = LeafLeftArmRoll2MaxRLimit.LeafLeftArmRoll2MaxRLimitx
    LeafLeftArmRoll2MaxRLimity = LeafLeftArmRoll2MaxRLimit.LeafLeftArmRoll2MaxRLimity
    LeafLeftArmRoll2MaxRLimitz = LeafLeftArmRoll2MaxRLimit.LeafLeftArmRoll2MaxRLimitz

    LeafLeftArmRoll2MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftArmRoll2MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftArmRoll2MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftArmRoll2MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftArmRoll2MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftArmRoll2MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftForeArmRoll2 = MessageField()

    LeafLeftForeArmRoll2T = LeafLeftForeArmRoll2TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll2Tx = LeafLeftForeArmRoll2T.LeafLeftForeArmRoll2Tx
    LeafLeftForeArmRoll2Ty = LeafLeftForeArmRoll2T.LeafLeftForeArmRoll2Ty
    LeafLeftForeArmRoll2Tz = LeafLeftForeArmRoll2T.LeafLeftForeArmRoll2Tz

    LeafLeftForeArmRoll2R = LeafLeftForeArmRoll2RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll2Rx = LeafLeftForeArmRoll2R.LeafLeftForeArmRoll2Rx
    LeafLeftForeArmRoll2Ry = LeafLeftForeArmRoll2R.LeafLeftForeArmRoll2Ry
    LeafLeftForeArmRoll2Rz = LeafLeftForeArmRoll2R.LeafLeftForeArmRoll2Rz

    LeafLeftForeArmRoll2S = LeafLeftForeArmRoll2SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftForeArmRoll2Sx = LeafLeftForeArmRoll2S.LeafLeftForeArmRoll2Sx
    LeafLeftForeArmRoll2Sy = LeafLeftForeArmRoll2S.LeafLeftForeArmRoll2Sy
    LeafLeftForeArmRoll2Sz = LeafLeftForeArmRoll2S.LeafLeftForeArmRoll2Sz

    LeafLeftForeArmRoll2RotateOrder = LeafLeftForeArmRoll2RotateOrderEnumField(default_value=0)

    LeafLeftForeArmRoll2RotateAxis = LeafLeftForeArmRoll2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll2RotateAxisx = LeafLeftForeArmRoll2RotateAxis.LeafLeftForeArmRoll2RotateAxisx
    LeafLeftForeArmRoll2RotateAxisy = LeafLeftForeArmRoll2RotateAxis.LeafLeftForeArmRoll2RotateAxisy
    LeafLeftForeArmRoll2RotateAxisz = LeafLeftForeArmRoll2RotateAxis.LeafLeftForeArmRoll2RotateAxisz

    LeafLeftForeArmRoll2JointOrient = LeafLeftForeArmRoll2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll2JointOrientx = LeafLeftForeArmRoll2JointOrient.LeafLeftForeArmRoll2JointOrientx
    LeafLeftForeArmRoll2JointOrienty = LeafLeftForeArmRoll2JointOrient.LeafLeftForeArmRoll2JointOrienty
    LeafLeftForeArmRoll2JointOrientz = LeafLeftForeArmRoll2JointOrient.LeafLeftForeArmRoll2JointOrientz

    LeafLeftForeArmRoll2MinRLimit = LeafLeftForeArmRoll2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll2MinRLimitx = LeafLeftForeArmRoll2MinRLimit.LeafLeftForeArmRoll2MinRLimitx
    LeafLeftForeArmRoll2MinRLimity = LeafLeftForeArmRoll2MinRLimit.LeafLeftForeArmRoll2MinRLimity
    LeafLeftForeArmRoll2MinRLimitz = LeafLeftForeArmRoll2MinRLimit.LeafLeftForeArmRoll2MinRLimitz

    LeafLeftForeArmRoll2MaxRLimit = LeafLeftForeArmRoll2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll2MaxRLimitx = LeafLeftForeArmRoll2MaxRLimit.LeafLeftForeArmRoll2MaxRLimitx
    LeafLeftForeArmRoll2MaxRLimity = LeafLeftForeArmRoll2MaxRLimit.LeafLeftForeArmRoll2MaxRLimity
    LeafLeftForeArmRoll2MaxRLimitz = LeafLeftForeArmRoll2MaxRLimit.LeafLeftForeArmRoll2MaxRLimitz

    LeafLeftForeArmRoll2MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftForeArmRoll2MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftForeArmRoll2MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftForeArmRoll2MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftForeArmRoll2MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftForeArmRoll2MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightArmRoll2 = MessageField()

    LeafRightArmRoll2T = LeafRightArmRoll2TField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll2Tx = LeafRightArmRoll2T.LeafRightArmRoll2Tx
    LeafRightArmRoll2Ty = LeafRightArmRoll2T.LeafRightArmRoll2Ty
    LeafRightArmRoll2Tz = LeafRightArmRoll2T.LeafRightArmRoll2Tz

    LeafRightArmRoll2R = LeafRightArmRoll2RField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll2Rx = LeafRightArmRoll2R.LeafRightArmRoll2Rx
    LeafRightArmRoll2Ry = LeafRightArmRoll2R.LeafRightArmRoll2Ry
    LeafRightArmRoll2Rz = LeafRightArmRoll2R.LeafRightArmRoll2Rz

    LeafRightArmRoll2S = LeafRightArmRoll2SField(default_value=(1.0, 1.0, 1.0))
    LeafRightArmRoll2Sx = LeafRightArmRoll2S.LeafRightArmRoll2Sx
    LeafRightArmRoll2Sy = LeafRightArmRoll2S.LeafRightArmRoll2Sy
    LeafRightArmRoll2Sz = LeafRightArmRoll2S.LeafRightArmRoll2Sz

    LeafRightArmRoll2RotateOrder = LeafRightArmRoll2RotateOrderEnumField(default_value=0)

    LeafRightArmRoll2RotateAxis = LeafRightArmRoll2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll2RotateAxisx = LeafRightArmRoll2RotateAxis.LeafRightArmRoll2RotateAxisx
    LeafRightArmRoll2RotateAxisy = LeafRightArmRoll2RotateAxis.LeafRightArmRoll2RotateAxisy
    LeafRightArmRoll2RotateAxisz = LeafRightArmRoll2RotateAxis.LeafRightArmRoll2RotateAxisz

    LeafRightArmRoll2JointOrient = LeafRightArmRoll2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll2JointOrientx = LeafRightArmRoll2JointOrient.LeafRightArmRoll2JointOrientx
    LeafRightArmRoll2JointOrienty = LeafRightArmRoll2JointOrient.LeafRightArmRoll2JointOrienty
    LeafRightArmRoll2JointOrientz = LeafRightArmRoll2JointOrient.LeafRightArmRoll2JointOrientz

    LeafRightArmRoll2MinRLimit = LeafRightArmRoll2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll2MinRLimitx = LeafRightArmRoll2MinRLimit.LeafRightArmRoll2MinRLimitx
    LeafRightArmRoll2MinRLimity = LeafRightArmRoll2MinRLimit.LeafRightArmRoll2MinRLimity
    LeafRightArmRoll2MinRLimitz = LeafRightArmRoll2MinRLimit.LeafRightArmRoll2MinRLimitz

    LeafRightArmRoll2MaxRLimit = LeafRightArmRoll2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll2MaxRLimitx = LeafRightArmRoll2MaxRLimit.LeafRightArmRoll2MaxRLimitx
    LeafRightArmRoll2MaxRLimity = LeafRightArmRoll2MaxRLimit.LeafRightArmRoll2MaxRLimity
    LeafRightArmRoll2MaxRLimitz = LeafRightArmRoll2MaxRLimit.LeafRightArmRoll2MaxRLimitz

    LeafRightArmRoll2MinRLimitEnablex = BoolField(default_value=False)

    LeafRightArmRoll2MinRLimitEnabley = BoolField(default_value=False)

    LeafRightArmRoll2MinRLimitEnablez = BoolField(default_value=False)

    LeafRightArmRoll2MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightArmRoll2MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightArmRoll2MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightForeArmRoll2 = MessageField()

    LeafRightForeArmRoll2T = LeafRightForeArmRoll2TField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll2Tx = LeafRightForeArmRoll2T.LeafRightForeArmRoll2Tx
    LeafRightForeArmRoll2Ty = LeafRightForeArmRoll2T.LeafRightForeArmRoll2Ty
    LeafRightForeArmRoll2Tz = LeafRightForeArmRoll2T.LeafRightForeArmRoll2Tz

    LeafRightForeArmRoll2R = LeafRightForeArmRoll2RField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll2Rx = LeafRightForeArmRoll2R.LeafRightForeArmRoll2Rx
    LeafRightForeArmRoll2Ry = LeafRightForeArmRoll2R.LeafRightForeArmRoll2Ry
    LeafRightForeArmRoll2Rz = LeafRightForeArmRoll2R.LeafRightForeArmRoll2Rz

    LeafRightForeArmRoll2S = LeafRightForeArmRoll2SField(default_value=(1.0, 1.0, 1.0))
    LeafRightForeArmRoll2Sx = LeafRightForeArmRoll2S.LeafRightForeArmRoll2Sx
    LeafRightForeArmRoll2Sy = LeafRightForeArmRoll2S.LeafRightForeArmRoll2Sy
    LeafRightForeArmRoll2Sz = LeafRightForeArmRoll2S.LeafRightForeArmRoll2Sz

    LeafRightForeArmRoll2RotateOrder = LeafRightForeArmRoll2RotateOrderEnumField(default_value=0)

    LeafRightForeArmRoll2RotateAxis = LeafRightForeArmRoll2RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll2RotateAxisx = LeafRightForeArmRoll2RotateAxis.LeafRightForeArmRoll2RotateAxisx
    LeafRightForeArmRoll2RotateAxisy = LeafRightForeArmRoll2RotateAxis.LeafRightForeArmRoll2RotateAxisy
    LeafRightForeArmRoll2RotateAxisz = LeafRightForeArmRoll2RotateAxis.LeafRightForeArmRoll2RotateAxisz

    LeafRightForeArmRoll2JointOrient = LeafRightForeArmRoll2JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll2JointOrientx = LeafRightForeArmRoll2JointOrient.LeafRightForeArmRoll2JointOrientx
    LeafRightForeArmRoll2JointOrienty = LeafRightForeArmRoll2JointOrient.LeafRightForeArmRoll2JointOrienty
    LeafRightForeArmRoll2JointOrientz = LeafRightForeArmRoll2JointOrient.LeafRightForeArmRoll2JointOrientz

    LeafRightForeArmRoll2MinRLimit = LeafRightForeArmRoll2MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll2MinRLimitx = LeafRightForeArmRoll2MinRLimit.LeafRightForeArmRoll2MinRLimitx
    LeafRightForeArmRoll2MinRLimity = LeafRightForeArmRoll2MinRLimit.LeafRightForeArmRoll2MinRLimity
    LeafRightForeArmRoll2MinRLimitz = LeafRightForeArmRoll2MinRLimit.LeafRightForeArmRoll2MinRLimitz

    LeafRightForeArmRoll2MaxRLimit = LeafRightForeArmRoll2MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll2MaxRLimitx = LeafRightForeArmRoll2MaxRLimit.LeafRightForeArmRoll2MaxRLimitx
    LeafRightForeArmRoll2MaxRLimity = LeafRightForeArmRoll2MaxRLimit.LeafRightForeArmRoll2MaxRLimity
    LeafRightForeArmRoll2MaxRLimitz = LeafRightForeArmRoll2MaxRLimit.LeafRightForeArmRoll2MaxRLimitz

    LeafRightForeArmRoll2MinRLimitEnablex = BoolField(default_value=False)

    LeafRightForeArmRoll2MinRLimitEnabley = BoolField(default_value=False)

    LeafRightForeArmRoll2MinRLimitEnablez = BoolField(default_value=False)

    LeafRightForeArmRoll2MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightForeArmRoll2MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightForeArmRoll2MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftUpLegRoll3 = MessageField()

    LeafLeftUpLegRoll3T = LeafLeftUpLegRoll3TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll3Tx = LeafLeftUpLegRoll3T.LeafLeftUpLegRoll3Tx
    LeafLeftUpLegRoll3Ty = LeafLeftUpLegRoll3T.LeafLeftUpLegRoll3Ty
    LeafLeftUpLegRoll3Tz = LeafLeftUpLegRoll3T.LeafLeftUpLegRoll3Tz

    LeafLeftUpLegRoll3R = LeafLeftUpLegRoll3RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll3Rx = LeafLeftUpLegRoll3R.LeafLeftUpLegRoll3Rx
    LeafLeftUpLegRoll3Ry = LeafLeftUpLegRoll3R.LeafLeftUpLegRoll3Ry
    LeafLeftUpLegRoll3Rz = LeafLeftUpLegRoll3R.LeafLeftUpLegRoll3Rz

    LeafLeftUpLegRoll3S = LeafLeftUpLegRoll3SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftUpLegRoll3Sx = LeafLeftUpLegRoll3S.LeafLeftUpLegRoll3Sx
    LeafLeftUpLegRoll3Sy = LeafLeftUpLegRoll3S.LeafLeftUpLegRoll3Sy
    LeafLeftUpLegRoll3Sz = LeafLeftUpLegRoll3S.LeafLeftUpLegRoll3Sz

    LeafLeftUpLegRoll3RotateOrder = LeafLeftUpLegRoll3RotateOrderEnumField(default_value=0)

    LeafLeftUpLegRoll3RotateAxis = LeafLeftUpLegRoll3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll3RotateAxisx = LeafLeftUpLegRoll3RotateAxis.LeafLeftUpLegRoll3RotateAxisx
    LeafLeftUpLegRoll3RotateAxisy = LeafLeftUpLegRoll3RotateAxis.LeafLeftUpLegRoll3RotateAxisy
    LeafLeftUpLegRoll3RotateAxisz = LeafLeftUpLegRoll3RotateAxis.LeafLeftUpLegRoll3RotateAxisz

    LeafLeftUpLegRoll3JointOrient = LeafLeftUpLegRoll3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll3JointOrientx = LeafLeftUpLegRoll3JointOrient.LeafLeftUpLegRoll3JointOrientx
    LeafLeftUpLegRoll3JointOrienty = LeafLeftUpLegRoll3JointOrient.LeafLeftUpLegRoll3JointOrienty
    LeafLeftUpLegRoll3JointOrientz = LeafLeftUpLegRoll3JointOrient.LeafLeftUpLegRoll3JointOrientz

    LeafLeftUpLegRoll3MinRLimit = LeafLeftUpLegRoll3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll3MinRLimitx = LeafLeftUpLegRoll3MinRLimit.LeafLeftUpLegRoll3MinRLimitx
    LeafLeftUpLegRoll3MinRLimity = LeafLeftUpLegRoll3MinRLimit.LeafLeftUpLegRoll3MinRLimity
    LeafLeftUpLegRoll3MinRLimitz = LeafLeftUpLegRoll3MinRLimit.LeafLeftUpLegRoll3MinRLimitz

    LeafLeftUpLegRoll3MaxRLimit = LeafLeftUpLegRoll3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll3MaxRLimitx = LeafLeftUpLegRoll3MaxRLimit.LeafLeftUpLegRoll3MaxRLimitx
    LeafLeftUpLegRoll3MaxRLimity = LeafLeftUpLegRoll3MaxRLimit.LeafLeftUpLegRoll3MaxRLimity
    LeafLeftUpLegRoll3MaxRLimitz = LeafLeftUpLegRoll3MaxRLimit.LeafLeftUpLegRoll3MaxRLimitz

    LeafLeftUpLegRoll3MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftUpLegRoll3MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftUpLegRoll3MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftUpLegRoll3MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftUpLegRoll3MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftUpLegRoll3MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftLegRoll3 = MessageField()

    LeafLeftLegRoll3T = LeafLeftLegRoll3TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll3Tx = LeafLeftLegRoll3T.LeafLeftLegRoll3Tx
    LeafLeftLegRoll3Ty = LeafLeftLegRoll3T.LeafLeftLegRoll3Ty
    LeafLeftLegRoll3Tz = LeafLeftLegRoll3T.LeafLeftLegRoll3Tz

    LeafLeftLegRoll3R = LeafLeftLegRoll3RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll3Rx = LeafLeftLegRoll3R.LeafLeftLegRoll3Rx
    LeafLeftLegRoll3Ry = LeafLeftLegRoll3R.LeafLeftLegRoll3Ry
    LeafLeftLegRoll3Rz = LeafLeftLegRoll3R.LeafLeftLegRoll3Rz

    LeafLeftLegRoll3S = LeafLeftLegRoll3SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftLegRoll3Sx = LeafLeftLegRoll3S.LeafLeftLegRoll3Sx
    LeafLeftLegRoll3Sy = LeafLeftLegRoll3S.LeafLeftLegRoll3Sy
    LeafLeftLegRoll3Sz = LeafLeftLegRoll3S.LeafLeftLegRoll3Sz

    LeafLeftLegRoll3RotateOrder = LeafLeftLegRoll3RotateOrderEnumField(default_value=0)

    LeafLeftLegRoll3RotateAxis = LeafLeftLegRoll3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll3RotateAxisx = LeafLeftLegRoll3RotateAxis.LeafLeftLegRoll3RotateAxisx
    LeafLeftLegRoll3RotateAxisy = LeafLeftLegRoll3RotateAxis.LeafLeftLegRoll3RotateAxisy
    LeafLeftLegRoll3RotateAxisz = LeafLeftLegRoll3RotateAxis.LeafLeftLegRoll3RotateAxisz

    LeafLeftLegRoll3JointOrient = LeafLeftLegRoll3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll3JointOrientx = LeafLeftLegRoll3JointOrient.LeafLeftLegRoll3JointOrientx
    LeafLeftLegRoll3JointOrienty = LeafLeftLegRoll3JointOrient.LeafLeftLegRoll3JointOrienty
    LeafLeftLegRoll3JointOrientz = LeafLeftLegRoll3JointOrient.LeafLeftLegRoll3JointOrientz

    LeafLeftLegRoll3MinRLimit = LeafLeftLegRoll3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll3MinRLimitx = LeafLeftLegRoll3MinRLimit.LeafLeftLegRoll3MinRLimitx
    LeafLeftLegRoll3MinRLimity = LeafLeftLegRoll3MinRLimit.LeafLeftLegRoll3MinRLimity
    LeafLeftLegRoll3MinRLimitz = LeafLeftLegRoll3MinRLimit.LeafLeftLegRoll3MinRLimitz

    LeafLeftLegRoll3MaxRLimit = LeafLeftLegRoll3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll3MaxRLimitx = LeafLeftLegRoll3MaxRLimit.LeafLeftLegRoll3MaxRLimitx
    LeafLeftLegRoll3MaxRLimity = LeafLeftLegRoll3MaxRLimit.LeafLeftLegRoll3MaxRLimity
    LeafLeftLegRoll3MaxRLimitz = LeafLeftLegRoll3MaxRLimit.LeafLeftLegRoll3MaxRLimitz

    LeafLeftLegRoll3MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftLegRoll3MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftLegRoll3MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftLegRoll3MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftLegRoll3MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftLegRoll3MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightUpLegRoll3 = MessageField()

    LeafRightUpLegRoll3T = LeafRightUpLegRoll3TField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll3Tx = LeafRightUpLegRoll3T.LeafRightUpLegRoll3Tx
    LeafRightUpLegRoll3Ty = LeafRightUpLegRoll3T.LeafRightUpLegRoll3Ty
    LeafRightUpLegRoll3Tz = LeafRightUpLegRoll3T.LeafRightUpLegRoll3Tz

    LeafRightUpLegRoll3R = LeafRightUpLegRoll3RField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll3Rx = LeafRightUpLegRoll3R.LeafRightUpLegRoll3Rx
    LeafRightUpLegRoll3Ry = LeafRightUpLegRoll3R.LeafRightUpLegRoll3Ry
    LeafRightUpLegRoll3Rz = LeafRightUpLegRoll3R.LeafRightUpLegRoll3Rz

    LeafRightUpLegRoll3S = LeafRightUpLegRoll3SField(default_value=(1.0, 1.0, 1.0))
    LeafRightUpLegRoll3Sx = LeafRightUpLegRoll3S.LeafRightUpLegRoll3Sx
    LeafRightUpLegRoll3Sy = LeafRightUpLegRoll3S.LeafRightUpLegRoll3Sy
    LeafRightUpLegRoll3Sz = LeafRightUpLegRoll3S.LeafRightUpLegRoll3Sz

    LeafRightUpLegRoll3RotateOrder = LeafRightUpLegRoll3RotateOrderEnumField(default_value=0)

    LeafRightUpLegRoll3RotateAxis = LeafRightUpLegRoll3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll3RotateAxisx = LeafRightUpLegRoll3RotateAxis.LeafRightUpLegRoll3RotateAxisx
    LeafRightUpLegRoll3RotateAxisy = LeafRightUpLegRoll3RotateAxis.LeafRightUpLegRoll3RotateAxisy
    LeafRightUpLegRoll3RotateAxisz = LeafRightUpLegRoll3RotateAxis.LeafRightUpLegRoll3RotateAxisz

    LeafRightUpLegRoll3JointOrient = LeafRightUpLegRoll3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll3JointOrientx = LeafRightUpLegRoll3JointOrient.LeafRightUpLegRoll3JointOrientx
    LeafRightUpLegRoll3JointOrienty = LeafRightUpLegRoll3JointOrient.LeafRightUpLegRoll3JointOrienty
    LeafRightUpLegRoll3JointOrientz = LeafRightUpLegRoll3JointOrient.LeafRightUpLegRoll3JointOrientz

    LeafRightUpLegRoll3MinRLimit = LeafRightUpLegRoll3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll3MinRLimitx = LeafRightUpLegRoll3MinRLimit.LeafRightUpLegRoll3MinRLimitx
    LeafRightUpLegRoll3MinRLimity = LeafRightUpLegRoll3MinRLimit.LeafRightUpLegRoll3MinRLimity
    LeafRightUpLegRoll3MinRLimitz = LeafRightUpLegRoll3MinRLimit.LeafRightUpLegRoll3MinRLimitz

    LeafRightUpLegRoll3MaxRLimit = LeafRightUpLegRoll3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll3MaxRLimitx = LeafRightUpLegRoll3MaxRLimit.LeafRightUpLegRoll3MaxRLimitx
    LeafRightUpLegRoll3MaxRLimity = LeafRightUpLegRoll3MaxRLimit.LeafRightUpLegRoll3MaxRLimity
    LeafRightUpLegRoll3MaxRLimitz = LeafRightUpLegRoll3MaxRLimit.LeafRightUpLegRoll3MaxRLimitz

    LeafRightUpLegRoll3MinRLimitEnablex = BoolField(default_value=False)

    LeafRightUpLegRoll3MinRLimitEnabley = BoolField(default_value=False)

    LeafRightUpLegRoll3MinRLimitEnablez = BoolField(default_value=False)

    LeafRightUpLegRoll3MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightUpLegRoll3MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightUpLegRoll3MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightLegRoll3 = MessageField()

    LeafRightLegRoll3T = LeafRightLegRoll3TField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll3Tx = LeafRightLegRoll3T.LeafRightLegRoll3Tx
    LeafRightLegRoll3Ty = LeafRightLegRoll3T.LeafRightLegRoll3Ty
    LeafRightLegRoll3Tz = LeafRightLegRoll3T.LeafRightLegRoll3Tz

    LeafRightLegRoll3R = LeafRightLegRoll3RField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll3Rx = LeafRightLegRoll3R.LeafRightLegRoll3Rx
    LeafRightLegRoll3Ry = LeafRightLegRoll3R.LeafRightLegRoll3Ry
    LeafRightLegRoll3Rz = LeafRightLegRoll3R.LeafRightLegRoll3Rz

    LeafRightLegRoll3S = LeafRightLegRoll3SField(default_value=(1.0, 1.0, 1.0))
    LeafRightLegRoll3Sx = LeafRightLegRoll3S.LeafRightLegRoll3Sx
    LeafRightLegRoll3Sy = LeafRightLegRoll3S.LeafRightLegRoll3Sy
    LeafRightLegRoll3Sz = LeafRightLegRoll3S.LeafRightLegRoll3Sz

    LeafRightLegRoll3RotateOrder = LeafRightLegRoll3RotateOrderEnumField(default_value=0)

    LeafRightLegRoll3RotateAxis = LeafRightLegRoll3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll3RotateAxisx = LeafRightLegRoll3RotateAxis.LeafRightLegRoll3RotateAxisx
    LeafRightLegRoll3RotateAxisy = LeafRightLegRoll3RotateAxis.LeafRightLegRoll3RotateAxisy
    LeafRightLegRoll3RotateAxisz = LeafRightLegRoll3RotateAxis.LeafRightLegRoll3RotateAxisz

    LeafRightLegRoll3JointOrient = LeafRightLegRoll3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll3JointOrientx = LeafRightLegRoll3JointOrient.LeafRightLegRoll3JointOrientx
    LeafRightLegRoll3JointOrienty = LeafRightLegRoll3JointOrient.LeafRightLegRoll3JointOrienty
    LeafRightLegRoll3JointOrientz = LeafRightLegRoll3JointOrient.LeafRightLegRoll3JointOrientz

    LeafRightLegRoll3MinRLimit = LeafRightLegRoll3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll3MinRLimitx = LeafRightLegRoll3MinRLimit.LeafRightLegRoll3MinRLimitx
    LeafRightLegRoll3MinRLimity = LeafRightLegRoll3MinRLimit.LeafRightLegRoll3MinRLimity
    LeafRightLegRoll3MinRLimitz = LeafRightLegRoll3MinRLimit.LeafRightLegRoll3MinRLimitz

    LeafRightLegRoll3MaxRLimit = LeafRightLegRoll3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll3MaxRLimitx = LeafRightLegRoll3MaxRLimit.LeafRightLegRoll3MaxRLimitx
    LeafRightLegRoll3MaxRLimity = LeafRightLegRoll3MaxRLimit.LeafRightLegRoll3MaxRLimity
    LeafRightLegRoll3MaxRLimitz = LeafRightLegRoll3MaxRLimit.LeafRightLegRoll3MaxRLimitz

    LeafRightLegRoll3MinRLimitEnablex = BoolField(default_value=False)

    LeafRightLegRoll3MinRLimitEnabley = BoolField(default_value=False)

    LeafRightLegRoll3MinRLimitEnablez = BoolField(default_value=False)

    LeafRightLegRoll3MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightLegRoll3MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightLegRoll3MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftArmRoll3 = MessageField()

    LeafLeftArmRoll3T = LeafLeftArmRoll3TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll3Tx = LeafLeftArmRoll3T.LeafLeftArmRoll3Tx
    LeafLeftArmRoll3Ty = LeafLeftArmRoll3T.LeafLeftArmRoll3Ty
    LeafLeftArmRoll3Tz = LeafLeftArmRoll3T.LeafLeftArmRoll3Tz

    LeafLeftArmRoll3R = LeafLeftArmRoll3RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll3Rx = LeafLeftArmRoll3R.LeafLeftArmRoll3Rx
    LeafLeftArmRoll3Ry = LeafLeftArmRoll3R.LeafLeftArmRoll3Ry
    LeafLeftArmRoll3Rz = LeafLeftArmRoll3R.LeafLeftArmRoll3Rz

    LeafLeftArmRoll3S = LeafLeftArmRoll3SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftArmRoll3Sx = LeafLeftArmRoll3S.LeafLeftArmRoll3Sx
    LeafLeftArmRoll3Sy = LeafLeftArmRoll3S.LeafLeftArmRoll3Sy
    LeafLeftArmRoll3Sz = LeafLeftArmRoll3S.LeafLeftArmRoll3Sz

    LeafLeftArmRoll3RotateOrder = LeafLeftArmRoll3RotateOrderEnumField(default_value=0)

    LeafLeftArmRoll3RotateAxis = LeafLeftArmRoll3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll3RotateAxisx = LeafLeftArmRoll3RotateAxis.LeafLeftArmRoll3RotateAxisx
    LeafLeftArmRoll3RotateAxisy = LeafLeftArmRoll3RotateAxis.LeafLeftArmRoll3RotateAxisy
    LeafLeftArmRoll3RotateAxisz = LeafLeftArmRoll3RotateAxis.LeafLeftArmRoll3RotateAxisz

    LeafLeftArmRoll3JointOrient = LeafLeftArmRoll3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll3JointOrientx = LeafLeftArmRoll3JointOrient.LeafLeftArmRoll3JointOrientx
    LeafLeftArmRoll3JointOrienty = LeafLeftArmRoll3JointOrient.LeafLeftArmRoll3JointOrienty
    LeafLeftArmRoll3JointOrientz = LeafLeftArmRoll3JointOrient.LeafLeftArmRoll3JointOrientz

    LeafLeftArmRoll3MinRLimit = LeafLeftArmRoll3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll3MinRLimitx = LeafLeftArmRoll3MinRLimit.LeafLeftArmRoll3MinRLimitx
    LeafLeftArmRoll3MinRLimity = LeafLeftArmRoll3MinRLimit.LeafLeftArmRoll3MinRLimity
    LeafLeftArmRoll3MinRLimitz = LeafLeftArmRoll3MinRLimit.LeafLeftArmRoll3MinRLimitz

    LeafLeftArmRoll3MaxRLimit = LeafLeftArmRoll3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll3MaxRLimitx = LeafLeftArmRoll3MaxRLimit.LeafLeftArmRoll3MaxRLimitx
    LeafLeftArmRoll3MaxRLimity = LeafLeftArmRoll3MaxRLimit.LeafLeftArmRoll3MaxRLimity
    LeafLeftArmRoll3MaxRLimitz = LeafLeftArmRoll3MaxRLimit.LeafLeftArmRoll3MaxRLimitz

    LeafLeftArmRoll3MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftArmRoll3MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftArmRoll3MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftArmRoll3MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftArmRoll3MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftArmRoll3MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftForeArmRoll3 = MessageField()

    LeafLeftForeArmRoll3T = LeafLeftForeArmRoll3TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll3Tx = LeafLeftForeArmRoll3T.LeafLeftForeArmRoll3Tx
    LeafLeftForeArmRoll3Ty = LeafLeftForeArmRoll3T.LeafLeftForeArmRoll3Ty
    LeafLeftForeArmRoll3Tz = LeafLeftForeArmRoll3T.LeafLeftForeArmRoll3Tz

    LeafLeftForeArmRoll3R = LeafLeftForeArmRoll3RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll3Rx = LeafLeftForeArmRoll3R.LeafLeftForeArmRoll3Rx
    LeafLeftForeArmRoll3Ry = LeafLeftForeArmRoll3R.LeafLeftForeArmRoll3Ry
    LeafLeftForeArmRoll3Rz = LeafLeftForeArmRoll3R.LeafLeftForeArmRoll3Rz

    LeafLeftForeArmRoll3S = LeafLeftForeArmRoll3SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftForeArmRoll3Sx = LeafLeftForeArmRoll3S.LeafLeftForeArmRoll3Sx
    LeafLeftForeArmRoll3Sy = LeafLeftForeArmRoll3S.LeafLeftForeArmRoll3Sy
    LeafLeftForeArmRoll3Sz = LeafLeftForeArmRoll3S.LeafLeftForeArmRoll3Sz

    LeafLeftForeArmRoll3RotateOrder = LeafLeftForeArmRoll3RotateOrderEnumField(default_value=0)

    LeafLeftForeArmRoll3RotateAxis = LeafLeftForeArmRoll3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll3RotateAxisx = LeafLeftForeArmRoll3RotateAxis.LeafLeftForeArmRoll3RotateAxisx
    LeafLeftForeArmRoll3RotateAxisy = LeafLeftForeArmRoll3RotateAxis.LeafLeftForeArmRoll3RotateAxisy
    LeafLeftForeArmRoll3RotateAxisz = LeafLeftForeArmRoll3RotateAxis.LeafLeftForeArmRoll3RotateAxisz

    LeafLeftForeArmRoll3JointOrient = LeafLeftForeArmRoll3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll3JointOrientx = LeafLeftForeArmRoll3JointOrient.LeafLeftForeArmRoll3JointOrientx
    LeafLeftForeArmRoll3JointOrienty = LeafLeftForeArmRoll3JointOrient.LeafLeftForeArmRoll3JointOrienty
    LeafLeftForeArmRoll3JointOrientz = LeafLeftForeArmRoll3JointOrient.LeafLeftForeArmRoll3JointOrientz

    LeafLeftForeArmRoll3MinRLimit = LeafLeftForeArmRoll3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll3MinRLimitx = LeafLeftForeArmRoll3MinRLimit.LeafLeftForeArmRoll3MinRLimitx
    LeafLeftForeArmRoll3MinRLimity = LeafLeftForeArmRoll3MinRLimit.LeafLeftForeArmRoll3MinRLimity
    LeafLeftForeArmRoll3MinRLimitz = LeafLeftForeArmRoll3MinRLimit.LeafLeftForeArmRoll3MinRLimitz

    LeafLeftForeArmRoll3MaxRLimit = LeafLeftForeArmRoll3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll3MaxRLimitx = LeafLeftForeArmRoll3MaxRLimit.LeafLeftForeArmRoll3MaxRLimitx
    LeafLeftForeArmRoll3MaxRLimity = LeafLeftForeArmRoll3MaxRLimit.LeafLeftForeArmRoll3MaxRLimity
    LeafLeftForeArmRoll3MaxRLimitz = LeafLeftForeArmRoll3MaxRLimit.LeafLeftForeArmRoll3MaxRLimitz

    LeafLeftForeArmRoll3MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftForeArmRoll3MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftForeArmRoll3MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftForeArmRoll3MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftForeArmRoll3MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftForeArmRoll3MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightArmRoll3 = MessageField()

    LeafRightArmRoll3T = LeafRightArmRoll3TField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll3Tx = LeafRightArmRoll3T.LeafRightArmRoll3Tx
    LeafRightArmRoll3Ty = LeafRightArmRoll3T.LeafRightArmRoll3Ty
    LeafRightArmRoll3Tz = LeafRightArmRoll3T.LeafRightArmRoll3Tz

    LeafRightArmRoll3R = LeafRightArmRoll3RField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll3Rx = LeafRightArmRoll3R.LeafRightArmRoll3Rx
    LeafRightArmRoll3Ry = LeafRightArmRoll3R.LeafRightArmRoll3Ry
    LeafRightArmRoll3Rz = LeafRightArmRoll3R.LeafRightArmRoll3Rz

    LeafRightArmRoll3S = LeafRightArmRoll3SField(default_value=(1.0, 1.0, 1.0))
    LeafRightArmRoll3Sx = LeafRightArmRoll3S.LeafRightArmRoll3Sx
    LeafRightArmRoll3Sy = LeafRightArmRoll3S.LeafRightArmRoll3Sy
    LeafRightArmRoll3Sz = LeafRightArmRoll3S.LeafRightArmRoll3Sz

    LeafRightArmRoll3RotateOrder = LeafRightArmRoll3RotateOrderEnumField(default_value=0)

    LeafRightArmRoll3RotateAxis = LeafRightArmRoll3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll3RotateAxisx = LeafRightArmRoll3RotateAxis.LeafRightArmRoll3RotateAxisx
    LeafRightArmRoll3RotateAxisy = LeafRightArmRoll3RotateAxis.LeafRightArmRoll3RotateAxisy
    LeafRightArmRoll3RotateAxisz = LeafRightArmRoll3RotateAxis.LeafRightArmRoll3RotateAxisz

    LeafRightArmRoll3JointOrient = LeafRightArmRoll3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll3JointOrientx = LeafRightArmRoll3JointOrient.LeafRightArmRoll3JointOrientx
    LeafRightArmRoll3JointOrienty = LeafRightArmRoll3JointOrient.LeafRightArmRoll3JointOrienty
    LeafRightArmRoll3JointOrientz = LeafRightArmRoll3JointOrient.LeafRightArmRoll3JointOrientz

    LeafRightArmRoll3MinRLimit = LeafRightArmRoll3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll3MinRLimitx = LeafRightArmRoll3MinRLimit.LeafRightArmRoll3MinRLimitx
    LeafRightArmRoll3MinRLimity = LeafRightArmRoll3MinRLimit.LeafRightArmRoll3MinRLimity
    LeafRightArmRoll3MinRLimitz = LeafRightArmRoll3MinRLimit.LeafRightArmRoll3MinRLimitz

    LeafRightArmRoll3MaxRLimit = LeafRightArmRoll3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll3MaxRLimitx = LeafRightArmRoll3MaxRLimit.LeafRightArmRoll3MaxRLimitx
    LeafRightArmRoll3MaxRLimity = LeafRightArmRoll3MaxRLimit.LeafRightArmRoll3MaxRLimity
    LeafRightArmRoll3MaxRLimitz = LeafRightArmRoll3MaxRLimit.LeafRightArmRoll3MaxRLimitz

    LeafRightArmRoll3MinRLimitEnablex = BoolField(default_value=False)

    LeafRightArmRoll3MinRLimitEnabley = BoolField(default_value=False)

    LeafRightArmRoll3MinRLimitEnablez = BoolField(default_value=False)

    LeafRightArmRoll3MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightArmRoll3MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightArmRoll3MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightForeArmRoll3 = MessageField()

    LeafRightForeArmRoll3T = LeafRightForeArmRoll3TField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll3Tx = LeafRightForeArmRoll3T.LeafRightForeArmRoll3Tx
    LeafRightForeArmRoll3Ty = LeafRightForeArmRoll3T.LeafRightForeArmRoll3Ty
    LeafRightForeArmRoll3Tz = LeafRightForeArmRoll3T.LeafRightForeArmRoll3Tz

    LeafRightForeArmRoll3R = LeafRightForeArmRoll3RField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll3Rx = LeafRightForeArmRoll3R.LeafRightForeArmRoll3Rx
    LeafRightForeArmRoll3Ry = LeafRightForeArmRoll3R.LeafRightForeArmRoll3Ry
    LeafRightForeArmRoll3Rz = LeafRightForeArmRoll3R.LeafRightForeArmRoll3Rz

    LeafRightForeArmRoll3S = LeafRightForeArmRoll3SField(default_value=(1.0, 1.0, 1.0))
    LeafRightForeArmRoll3Sx = LeafRightForeArmRoll3S.LeafRightForeArmRoll3Sx
    LeafRightForeArmRoll3Sy = LeafRightForeArmRoll3S.LeafRightForeArmRoll3Sy
    LeafRightForeArmRoll3Sz = LeafRightForeArmRoll3S.LeafRightForeArmRoll3Sz

    LeafRightForeArmRoll3RotateOrder = LeafRightForeArmRoll3RotateOrderEnumField(default_value=0)

    LeafRightForeArmRoll3RotateAxis = LeafRightForeArmRoll3RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll3RotateAxisx = LeafRightForeArmRoll3RotateAxis.LeafRightForeArmRoll3RotateAxisx
    LeafRightForeArmRoll3RotateAxisy = LeafRightForeArmRoll3RotateAxis.LeafRightForeArmRoll3RotateAxisy
    LeafRightForeArmRoll3RotateAxisz = LeafRightForeArmRoll3RotateAxis.LeafRightForeArmRoll3RotateAxisz

    LeafRightForeArmRoll3JointOrient = LeafRightForeArmRoll3JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll3JointOrientx = LeafRightForeArmRoll3JointOrient.LeafRightForeArmRoll3JointOrientx
    LeafRightForeArmRoll3JointOrienty = LeafRightForeArmRoll3JointOrient.LeafRightForeArmRoll3JointOrienty
    LeafRightForeArmRoll3JointOrientz = LeafRightForeArmRoll3JointOrient.LeafRightForeArmRoll3JointOrientz

    LeafRightForeArmRoll3MinRLimit = LeafRightForeArmRoll3MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll3MinRLimitx = LeafRightForeArmRoll3MinRLimit.LeafRightForeArmRoll3MinRLimitx
    LeafRightForeArmRoll3MinRLimity = LeafRightForeArmRoll3MinRLimit.LeafRightForeArmRoll3MinRLimity
    LeafRightForeArmRoll3MinRLimitz = LeafRightForeArmRoll3MinRLimit.LeafRightForeArmRoll3MinRLimitz

    LeafRightForeArmRoll3MaxRLimit = LeafRightForeArmRoll3MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll3MaxRLimitx = LeafRightForeArmRoll3MaxRLimit.LeafRightForeArmRoll3MaxRLimitx
    LeafRightForeArmRoll3MaxRLimity = LeafRightForeArmRoll3MaxRLimit.LeafRightForeArmRoll3MaxRLimity
    LeafRightForeArmRoll3MaxRLimitz = LeafRightForeArmRoll3MaxRLimit.LeafRightForeArmRoll3MaxRLimitz

    LeafRightForeArmRoll3MinRLimitEnablex = BoolField(default_value=False)

    LeafRightForeArmRoll3MinRLimitEnabley = BoolField(default_value=False)

    LeafRightForeArmRoll3MinRLimitEnablez = BoolField(default_value=False)

    LeafRightForeArmRoll3MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightForeArmRoll3MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightForeArmRoll3MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftUpLegRoll4 = MessageField()

    LeafLeftUpLegRoll4T = LeafLeftUpLegRoll4TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll4Tx = LeafLeftUpLegRoll4T.LeafLeftUpLegRoll4Tx
    LeafLeftUpLegRoll4Ty = LeafLeftUpLegRoll4T.LeafLeftUpLegRoll4Ty
    LeafLeftUpLegRoll4Tz = LeafLeftUpLegRoll4T.LeafLeftUpLegRoll4Tz

    LeafLeftUpLegRoll4R = LeafLeftUpLegRoll4RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll4Rx = LeafLeftUpLegRoll4R.LeafLeftUpLegRoll4Rx
    LeafLeftUpLegRoll4Ry = LeafLeftUpLegRoll4R.LeafLeftUpLegRoll4Ry
    LeafLeftUpLegRoll4Rz = LeafLeftUpLegRoll4R.LeafLeftUpLegRoll4Rz

    LeafLeftUpLegRoll4S = LeafLeftUpLegRoll4SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftUpLegRoll4Sx = LeafLeftUpLegRoll4S.LeafLeftUpLegRoll4Sx
    LeafLeftUpLegRoll4Sy = LeafLeftUpLegRoll4S.LeafLeftUpLegRoll4Sy
    LeafLeftUpLegRoll4Sz = LeafLeftUpLegRoll4S.LeafLeftUpLegRoll4Sz

    LeafLeftUpLegRoll4RotateOrder = LeafLeftUpLegRoll4RotateOrderEnumField(default_value=0)

    LeafLeftUpLegRoll4RotateAxis = LeafLeftUpLegRoll4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll4RotateAxisx = LeafLeftUpLegRoll4RotateAxis.LeafLeftUpLegRoll4RotateAxisx
    LeafLeftUpLegRoll4RotateAxisy = LeafLeftUpLegRoll4RotateAxis.LeafLeftUpLegRoll4RotateAxisy
    LeafLeftUpLegRoll4RotateAxisz = LeafLeftUpLegRoll4RotateAxis.LeafLeftUpLegRoll4RotateAxisz

    LeafLeftUpLegRoll4JointOrient = LeafLeftUpLegRoll4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll4JointOrientx = LeafLeftUpLegRoll4JointOrient.LeafLeftUpLegRoll4JointOrientx
    LeafLeftUpLegRoll4JointOrienty = LeafLeftUpLegRoll4JointOrient.LeafLeftUpLegRoll4JointOrienty
    LeafLeftUpLegRoll4JointOrientz = LeafLeftUpLegRoll4JointOrient.LeafLeftUpLegRoll4JointOrientz

    LeafLeftUpLegRoll4MinRLimit = LeafLeftUpLegRoll4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll4MinRLimitx = LeafLeftUpLegRoll4MinRLimit.LeafLeftUpLegRoll4MinRLimitx
    LeafLeftUpLegRoll4MinRLimity = LeafLeftUpLegRoll4MinRLimit.LeafLeftUpLegRoll4MinRLimity
    LeafLeftUpLegRoll4MinRLimitz = LeafLeftUpLegRoll4MinRLimit.LeafLeftUpLegRoll4MinRLimitz

    LeafLeftUpLegRoll4MaxRLimit = LeafLeftUpLegRoll4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll4MaxRLimitx = LeafLeftUpLegRoll4MaxRLimit.LeafLeftUpLegRoll4MaxRLimitx
    LeafLeftUpLegRoll4MaxRLimity = LeafLeftUpLegRoll4MaxRLimit.LeafLeftUpLegRoll4MaxRLimity
    LeafLeftUpLegRoll4MaxRLimitz = LeafLeftUpLegRoll4MaxRLimit.LeafLeftUpLegRoll4MaxRLimitz

    LeafLeftUpLegRoll4MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftUpLegRoll4MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftUpLegRoll4MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftUpLegRoll4MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftUpLegRoll4MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftUpLegRoll4MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftLegRoll4 = MessageField()

    LeafLeftLegRoll4T = LeafLeftLegRoll4TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll4Tx = LeafLeftLegRoll4T.LeafLeftLegRoll4Tx
    LeafLeftLegRoll4Ty = LeafLeftLegRoll4T.LeafLeftLegRoll4Ty
    LeafLeftLegRoll4Tz = LeafLeftLegRoll4T.LeafLeftLegRoll4Tz

    LeafLeftLegRoll4R = LeafLeftLegRoll4RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll4Rx = LeafLeftLegRoll4R.LeafLeftLegRoll4Rx
    LeafLeftLegRoll4Ry = LeafLeftLegRoll4R.LeafLeftLegRoll4Ry
    LeafLeftLegRoll4Rz = LeafLeftLegRoll4R.LeafLeftLegRoll4Rz

    LeafLeftLegRoll4S = LeafLeftLegRoll4SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftLegRoll4Sx = LeafLeftLegRoll4S.LeafLeftLegRoll4Sx
    LeafLeftLegRoll4Sy = LeafLeftLegRoll4S.LeafLeftLegRoll4Sy
    LeafLeftLegRoll4Sz = LeafLeftLegRoll4S.LeafLeftLegRoll4Sz

    LeafLeftLegRoll4RotateOrder = LeafLeftLegRoll4RotateOrderEnumField(default_value=0)

    LeafLeftLegRoll4RotateAxis = LeafLeftLegRoll4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll4RotateAxisx = LeafLeftLegRoll4RotateAxis.LeafLeftLegRoll4RotateAxisx
    LeafLeftLegRoll4RotateAxisy = LeafLeftLegRoll4RotateAxis.LeafLeftLegRoll4RotateAxisy
    LeafLeftLegRoll4RotateAxisz = LeafLeftLegRoll4RotateAxis.LeafLeftLegRoll4RotateAxisz

    LeafLeftLegRoll4JointOrient = LeafLeftLegRoll4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll4JointOrientx = LeafLeftLegRoll4JointOrient.LeafLeftLegRoll4JointOrientx
    LeafLeftLegRoll4JointOrienty = LeafLeftLegRoll4JointOrient.LeafLeftLegRoll4JointOrienty
    LeafLeftLegRoll4JointOrientz = LeafLeftLegRoll4JointOrient.LeafLeftLegRoll4JointOrientz

    LeafLeftLegRoll4MinRLimit = LeafLeftLegRoll4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll4MinRLimitx = LeafLeftLegRoll4MinRLimit.LeafLeftLegRoll4MinRLimitx
    LeafLeftLegRoll4MinRLimity = LeafLeftLegRoll4MinRLimit.LeafLeftLegRoll4MinRLimity
    LeafLeftLegRoll4MinRLimitz = LeafLeftLegRoll4MinRLimit.LeafLeftLegRoll4MinRLimitz

    LeafLeftLegRoll4MaxRLimit = LeafLeftLegRoll4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll4MaxRLimitx = LeafLeftLegRoll4MaxRLimit.LeafLeftLegRoll4MaxRLimitx
    LeafLeftLegRoll4MaxRLimity = LeafLeftLegRoll4MaxRLimit.LeafLeftLegRoll4MaxRLimity
    LeafLeftLegRoll4MaxRLimitz = LeafLeftLegRoll4MaxRLimit.LeafLeftLegRoll4MaxRLimitz

    LeafLeftLegRoll4MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftLegRoll4MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftLegRoll4MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftLegRoll4MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftLegRoll4MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftLegRoll4MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightUpLegRoll4 = MessageField()

    LeafRightUpLegRoll4T = LeafRightUpLegRoll4TField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll4Tx = LeafRightUpLegRoll4T.LeafRightUpLegRoll4Tx
    LeafRightUpLegRoll4Ty = LeafRightUpLegRoll4T.LeafRightUpLegRoll4Ty
    LeafRightUpLegRoll4Tz = LeafRightUpLegRoll4T.LeafRightUpLegRoll4Tz

    LeafRightUpLegRoll4R = LeafRightUpLegRoll4RField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll4Rx = LeafRightUpLegRoll4R.LeafRightUpLegRoll4Rx
    LeafRightUpLegRoll4Ry = LeafRightUpLegRoll4R.LeafRightUpLegRoll4Ry
    LeafRightUpLegRoll4Rz = LeafRightUpLegRoll4R.LeafRightUpLegRoll4Rz

    LeafRightUpLegRoll4S = LeafRightUpLegRoll4SField(default_value=(1.0, 1.0, 1.0))
    LeafRightUpLegRoll4Sx = LeafRightUpLegRoll4S.LeafRightUpLegRoll4Sx
    LeafRightUpLegRoll4Sy = LeafRightUpLegRoll4S.LeafRightUpLegRoll4Sy
    LeafRightUpLegRoll4Sz = LeafRightUpLegRoll4S.LeafRightUpLegRoll4Sz

    LeafRightUpLegRoll4RotateOrder = LeafRightUpLegRoll4RotateOrderEnumField(default_value=0)

    LeafRightUpLegRoll4RotateAxis = LeafRightUpLegRoll4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll4RotateAxisx = LeafRightUpLegRoll4RotateAxis.LeafRightUpLegRoll4RotateAxisx
    LeafRightUpLegRoll4RotateAxisy = LeafRightUpLegRoll4RotateAxis.LeafRightUpLegRoll4RotateAxisy
    LeafRightUpLegRoll4RotateAxisz = LeafRightUpLegRoll4RotateAxis.LeafRightUpLegRoll4RotateAxisz

    LeafRightUpLegRoll4JointOrient = LeafRightUpLegRoll4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll4JointOrientx = LeafRightUpLegRoll4JointOrient.LeafRightUpLegRoll4JointOrientx
    LeafRightUpLegRoll4JointOrienty = LeafRightUpLegRoll4JointOrient.LeafRightUpLegRoll4JointOrienty
    LeafRightUpLegRoll4JointOrientz = LeafRightUpLegRoll4JointOrient.LeafRightUpLegRoll4JointOrientz

    LeafRightUpLegRoll4MinRLimit = LeafRightUpLegRoll4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll4MinRLimitx = LeafRightUpLegRoll4MinRLimit.LeafRightUpLegRoll4MinRLimitx
    LeafRightUpLegRoll4MinRLimity = LeafRightUpLegRoll4MinRLimit.LeafRightUpLegRoll4MinRLimity
    LeafRightUpLegRoll4MinRLimitz = LeafRightUpLegRoll4MinRLimit.LeafRightUpLegRoll4MinRLimitz

    LeafRightUpLegRoll4MaxRLimit = LeafRightUpLegRoll4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll4MaxRLimitx = LeafRightUpLegRoll4MaxRLimit.LeafRightUpLegRoll4MaxRLimitx
    LeafRightUpLegRoll4MaxRLimity = LeafRightUpLegRoll4MaxRLimit.LeafRightUpLegRoll4MaxRLimity
    LeafRightUpLegRoll4MaxRLimitz = LeafRightUpLegRoll4MaxRLimit.LeafRightUpLegRoll4MaxRLimitz

    LeafRightUpLegRoll4MinRLimitEnablex = BoolField(default_value=False)

    LeafRightUpLegRoll4MinRLimitEnabley = BoolField(default_value=False)

    LeafRightUpLegRoll4MinRLimitEnablez = BoolField(default_value=False)

    LeafRightUpLegRoll4MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightUpLegRoll4MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightUpLegRoll4MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightLegRoll4 = MessageField()

    LeafRightLegRoll4T = LeafRightLegRoll4TField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll4Tx = LeafRightLegRoll4T.LeafRightLegRoll4Tx
    LeafRightLegRoll4Ty = LeafRightLegRoll4T.LeafRightLegRoll4Ty
    LeafRightLegRoll4Tz = LeafRightLegRoll4T.LeafRightLegRoll4Tz

    LeafRightLegRoll4R = LeafRightLegRoll4RField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll4Rx = LeafRightLegRoll4R.LeafRightLegRoll4Rx
    LeafRightLegRoll4Ry = LeafRightLegRoll4R.LeafRightLegRoll4Ry
    LeafRightLegRoll4Rz = LeafRightLegRoll4R.LeafRightLegRoll4Rz

    LeafRightLegRoll4S = LeafRightLegRoll4SField(default_value=(1.0, 1.0, 1.0))
    LeafRightLegRoll4Sx = LeafRightLegRoll4S.LeafRightLegRoll4Sx
    LeafRightLegRoll4Sy = LeafRightLegRoll4S.LeafRightLegRoll4Sy
    LeafRightLegRoll4Sz = LeafRightLegRoll4S.LeafRightLegRoll4Sz

    LeafRightLegRoll4RotateOrder = LeafRightLegRoll4RotateOrderEnumField(default_value=0)

    LeafRightLegRoll4RotateAxis = LeafRightLegRoll4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll4RotateAxisx = LeafRightLegRoll4RotateAxis.LeafRightLegRoll4RotateAxisx
    LeafRightLegRoll4RotateAxisy = LeafRightLegRoll4RotateAxis.LeafRightLegRoll4RotateAxisy
    LeafRightLegRoll4RotateAxisz = LeafRightLegRoll4RotateAxis.LeafRightLegRoll4RotateAxisz

    LeafRightLegRoll4JointOrient = LeafRightLegRoll4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll4JointOrientx = LeafRightLegRoll4JointOrient.LeafRightLegRoll4JointOrientx
    LeafRightLegRoll4JointOrienty = LeafRightLegRoll4JointOrient.LeafRightLegRoll4JointOrienty
    LeafRightLegRoll4JointOrientz = LeafRightLegRoll4JointOrient.LeafRightLegRoll4JointOrientz

    LeafRightLegRoll4MinRLimit = LeafRightLegRoll4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll4MinRLimitx = LeafRightLegRoll4MinRLimit.LeafRightLegRoll4MinRLimitx
    LeafRightLegRoll4MinRLimity = LeafRightLegRoll4MinRLimit.LeafRightLegRoll4MinRLimity
    LeafRightLegRoll4MinRLimitz = LeafRightLegRoll4MinRLimit.LeafRightLegRoll4MinRLimitz

    LeafRightLegRoll4MaxRLimit = LeafRightLegRoll4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll4MaxRLimitx = LeafRightLegRoll4MaxRLimit.LeafRightLegRoll4MaxRLimitx
    LeafRightLegRoll4MaxRLimity = LeafRightLegRoll4MaxRLimit.LeafRightLegRoll4MaxRLimity
    LeafRightLegRoll4MaxRLimitz = LeafRightLegRoll4MaxRLimit.LeafRightLegRoll4MaxRLimitz

    LeafRightLegRoll4MinRLimitEnablex = BoolField(default_value=False)

    LeafRightLegRoll4MinRLimitEnabley = BoolField(default_value=False)

    LeafRightLegRoll4MinRLimitEnablez = BoolField(default_value=False)

    LeafRightLegRoll4MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightLegRoll4MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightLegRoll4MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftArmRoll4 = MessageField()

    LeafLeftArmRoll4T = LeafLeftArmRoll4TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll4Tx = LeafLeftArmRoll4T.LeafLeftArmRoll4Tx
    LeafLeftArmRoll4Ty = LeafLeftArmRoll4T.LeafLeftArmRoll4Ty
    LeafLeftArmRoll4Tz = LeafLeftArmRoll4T.LeafLeftArmRoll4Tz

    LeafLeftArmRoll4R = LeafLeftArmRoll4RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll4Rx = LeafLeftArmRoll4R.LeafLeftArmRoll4Rx
    LeafLeftArmRoll4Ry = LeafLeftArmRoll4R.LeafLeftArmRoll4Ry
    LeafLeftArmRoll4Rz = LeafLeftArmRoll4R.LeafLeftArmRoll4Rz

    LeafLeftArmRoll4S = LeafLeftArmRoll4SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftArmRoll4Sx = LeafLeftArmRoll4S.LeafLeftArmRoll4Sx
    LeafLeftArmRoll4Sy = LeafLeftArmRoll4S.LeafLeftArmRoll4Sy
    LeafLeftArmRoll4Sz = LeafLeftArmRoll4S.LeafLeftArmRoll4Sz

    LeafLeftArmRoll4RotateOrder = LeafLeftArmRoll4RotateOrderEnumField(default_value=0)

    LeafLeftArmRoll4RotateAxis = LeafLeftArmRoll4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll4RotateAxisx = LeafLeftArmRoll4RotateAxis.LeafLeftArmRoll4RotateAxisx
    LeafLeftArmRoll4RotateAxisy = LeafLeftArmRoll4RotateAxis.LeafLeftArmRoll4RotateAxisy
    LeafLeftArmRoll4RotateAxisz = LeafLeftArmRoll4RotateAxis.LeafLeftArmRoll4RotateAxisz

    LeafLeftArmRoll4JointOrient = LeafLeftArmRoll4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll4JointOrientx = LeafLeftArmRoll4JointOrient.LeafLeftArmRoll4JointOrientx
    LeafLeftArmRoll4JointOrienty = LeafLeftArmRoll4JointOrient.LeafLeftArmRoll4JointOrienty
    LeafLeftArmRoll4JointOrientz = LeafLeftArmRoll4JointOrient.LeafLeftArmRoll4JointOrientz

    LeafLeftArmRoll4MinRLimit = LeafLeftArmRoll4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll4MinRLimitx = LeafLeftArmRoll4MinRLimit.LeafLeftArmRoll4MinRLimitx
    LeafLeftArmRoll4MinRLimity = LeafLeftArmRoll4MinRLimit.LeafLeftArmRoll4MinRLimity
    LeafLeftArmRoll4MinRLimitz = LeafLeftArmRoll4MinRLimit.LeafLeftArmRoll4MinRLimitz

    LeafLeftArmRoll4MaxRLimit = LeafLeftArmRoll4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll4MaxRLimitx = LeafLeftArmRoll4MaxRLimit.LeafLeftArmRoll4MaxRLimitx
    LeafLeftArmRoll4MaxRLimity = LeafLeftArmRoll4MaxRLimit.LeafLeftArmRoll4MaxRLimity
    LeafLeftArmRoll4MaxRLimitz = LeafLeftArmRoll4MaxRLimit.LeafLeftArmRoll4MaxRLimitz

    LeafLeftArmRoll4MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftArmRoll4MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftArmRoll4MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftArmRoll4MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftArmRoll4MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftArmRoll4MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftForeArmRoll4 = MessageField()

    LeafLeftForeArmRoll4T = LeafLeftForeArmRoll4TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll4Tx = LeafLeftForeArmRoll4T.LeafLeftForeArmRoll4Tx
    LeafLeftForeArmRoll4Ty = LeafLeftForeArmRoll4T.LeafLeftForeArmRoll4Ty
    LeafLeftForeArmRoll4Tz = LeafLeftForeArmRoll4T.LeafLeftForeArmRoll4Tz

    LeafLeftForeArmRoll4R = LeafLeftForeArmRoll4RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll4Rx = LeafLeftForeArmRoll4R.LeafLeftForeArmRoll4Rx
    LeafLeftForeArmRoll4Ry = LeafLeftForeArmRoll4R.LeafLeftForeArmRoll4Ry
    LeafLeftForeArmRoll4Rz = LeafLeftForeArmRoll4R.LeafLeftForeArmRoll4Rz

    LeafLeftForeArmRoll4S = LeafLeftForeArmRoll4SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftForeArmRoll4Sx = LeafLeftForeArmRoll4S.LeafLeftForeArmRoll4Sx
    LeafLeftForeArmRoll4Sy = LeafLeftForeArmRoll4S.LeafLeftForeArmRoll4Sy
    LeafLeftForeArmRoll4Sz = LeafLeftForeArmRoll4S.LeafLeftForeArmRoll4Sz

    LeafLeftForeArmRoll4RotateOrder = LeafLeftForeArmRoll4RotateOrderEnumField(default_value=0)

    LeafLeftForeArmRoll4RotateAxis = LeafLeftForeArmRoll4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll4RotateAxisx = LeafLeftForeArmRoll4RotateAxis.LeafLeftForeArmRoll4RotateAxisx
    LeafLeftForeArmRoll4RotateAxisy = LeafLeftForeArmRoll4RotateAxis.LeafLeftForeArmRoll4RotateAxisy
    LeafLeftForeArmRoll4RotateAxisz = LeafLeftForeArmRoll4RotateAxis.LeafLeftForeArmRoll4RotateAxisz

    LeafLeftForeArmRoll4JointOrient = LeafLeftForeArmRoll4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll4JointOrientx = LeafLeftForeArmRoll4JointOrient.LeafLeftForeArmRoll4JointOrientx
    LeafLeftForeArmRoll4JointOrienty = LeafLeftForeArmRoll4JointOrient.LeafLeftForeArmRoll4JointOrienty
    LeafLeftForeArmRoll4JointOrientz = LeafLeftForeArmRoll4JointOrient.LeafLeftForeArmRoll4JointOrientz

    LeafLeftForeArmRoll4MinRLimit = LeafLeftForeArmRoll4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll4MinRLimitx = LeafLeftForeArmRoll4MinRLimit.LeafLeftForeArmRoll4MinRLimitx
    LeafLeftForeArmRoll4MinRLimity = LeafLeftForeArmRoll4MinRLimit.LeafLeftForeArmRoll4MinRLimity
    LeafLeftForeArmRoll4MinRLimitz = LeafLeftForeArmRoll4MinRLimit.LeafLeftForeArmRoll4MinRLimitz

    LeafLeftForeArmRoll4MaxRLimit = LeafLeftForeArmRoll4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll4MaxRLimitx = LeafLeftForeArmRoll4MaxRLimit.LeafLeftForeArmRoll4MaxRLimitx
    LeafLeftForeArmRoll4MaxRLimity = LeafLeftForeArmRoll4MaxRLimit.LeafLeftForeArmRoll4MaxRLimity
    LeafLeftForeArmRoll4MaxRLimitz = LeafLeftForeArmRoll4MaxRLimit.LeafLeftForeArmRoll4MaxRLimitz

    LeafLeftForeArmRoll4MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftForeArmRoll4MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftForeArmRoll4MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftForeArmRoll4MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftForeArmRoll4MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftForeArmRoll4MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightArmRoll4 = MessageField()

    LeafRightArmRoll4T = LeafRightArmRoll4TField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll4Tx = LeafRightArmRoll4T.LeafRightArmRoll4Tx
    LeafRightArmRoll4Ty = LeafRightArmRoll4T.LeafRightArmRoll4Ty
    LeafRightArmRoll4Tz = LeafRightArmRoll4T.LeafRightArmRoll4Tz

    LeafRightArmRoll4R = LeafRightArmRoll4RField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll4Rx = LeafRightArmRoll4R.LeafRightArmRoll4Rx
    LeafRightArmRoll4Ry = LeafRightArmRoll4R.LeafRightArmRoll4Ry
    LeafRightArmRoll4Rz = LeafRightArmRoll4R.LeafRightArmRoll4Rz

    LeafRightArmRoll4S = LeafRightArmRoll4SField(default_value=(1.0, 1.0, 1.0))
    LeafRightArmRoll4Sx = LeafRightArmRoll4S.LeafRightArmRoll4Sx
    LeafRightArmRoll4Sy = LeafRightArmRoll4S.LeafRightArmRoll4Sy
    LeafRightArmRoll4Sz = LeafRightArmRoll4S.LeafRightArmRoll4Sz

    LeafRightArmRoll4RotateOrder = LeafRightArmRoll4RotateOrderEnumField(default_value=0)

    LeafRightArmRoll4RotateAxis = LeafRightArmRoll4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll4RotateAxisx = LeafRightArmRoll4RotateAxis.LeafRightArmRoll4RotateAxisx
    LeafRightArmRoll4RotateAxisy = LeafRightArmRoll4RotateAxis.LeafRightArmRoll4RotateAxisy
    LeafRightArmRoll4RotateAxisz = LeafRightArmRoll4RotateAxis.LeafRightArmRoll4RotateAxisz

    LeafRightArmRoll4JointOrient = LeafRightArmRoll4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll4JointOrientx = LeafRightArmRoll4JointOrient.LeafRightArmRoll4JointOrientx
    LeafRightArmRoll4JointOrienty = LeafRightArmRoll4JointOrient.LeafRightArmRoll4JointOrienty
    LeafRightArmRoll4JointOrientz = LeafRightArmRoll4JointOrient.LeafRightArmRoll4JointOrientz

    LeafRightArmRoll4MinRLimit = LeafRightArmRoll4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll4MinRLimitx = LeafRightArmRoll4MinRLimit.LeafRightArmRoll4MinRLimitx
    LeafRightArmRoll4MinRLimity = LeafRightArmRoll4MinRLimit.LeafRightArmRoll4MinRLimity
    LeafRightArmRoll4MinRLimitz = LeafRightArmRoll4MinRLimit.LeafRightArmRoll4MinRLimitz

    LeafRightArmRoll4MaxRLimit = LeafRightArmRoll4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll4MaxRLimitx = LeafRightArmRoll4MaxRLimit.LeafRightArmRoll4MaxRLimitx
    LeafRightArmRoll4MaxRLimity = LeafRightArmRoll4MaxRLimit.LeafRightArmRoll4MaxRLimity
    LeafRightArmRoll4MaxRLimitz = LeafRightArmRoll4MaxRLimit.LeafRightArmRoll4MaxRLimitz

    LeafRightArmRoll4MinRLimitEnablex = BoolField(default_value=False)

    LeafRightArmRoll4MinRLimitEnabley = BoolField(default_value=False)

    LeafRightArmRoll4MinRLimitEnablez = BoolField(default_value=False)

    LeafRightArmRoll4MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightArmRoll4MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightArmRoll4MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightForeArmRoll4 = MessageField()

    LeafRightForeArmRoll4T = LeafRightForeArmRoll4TField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll4Tx = LeafRightForeArmRoll4T.LeafRightForeArmRoll4Tx
    LeafRightForeArmRoll4Ty = LeafRightForeArmRoll4T.LeafRightForeArmRoll4Ty
    LeafRightForeArmRoll4Tz = LeafRightForeArmRoll4T.LeafRightForeArmRoll4Tz

    LeafRightForeArmRoll4R = LeafRightForeArmRoll4RField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll4Rx = LeafRightForeArmRoll4R.LeafRightForeArmRoll4Rx
    LeafRightForeArmRoll4Ry = LeafRightForeArmRoll4R.LeafRightForeArmRoll4Ry
    LeafRightForeArmRoll4Rz = LeafRightForeArmRoll4R.LeafRightForeArmRoll4Rz

    LeafRightForeArmRoll4S = LeafRightForeArmRoll4SField(default_value=(1.0, 1.0, 1.0))
    LeafRightForeArmRoll4Sx = LeafRightForeArmRoll4S.LeafRightForeArmRoll4Sx
    LeafRightForeArmRoll4Sy = LeafRightForeArmRoll4S.LeafRightForeArmRoll4Sy
    LeafRightForeArmRoll4Sz = LeafRightForeArmRoll4S.LeafRightForeArmRoll4Sz

    LeafRightForeArmRoll4RotateOrder = LeafRightForeArmRoll4RotateOrderEnumField(default_value=0)

    LeafRightForeArmRoll4RotateAxis = LeafRightForeArmRoll4RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll4RotateAxisx = LeafRightForeArmRoll4RotateAxis.LeafRightForeArmRoll4RotateAxisx
    LeafRightForeArmRoll4RotateAxisy = LeafRightForeArmRoll4RotateAxis.LeafRightForeArmRoll4RotateAxisy
    LeafRightForeArmRoll4RotateAxisz = LeafRightForeArmRoll4RotateAxis.LeafRightForeArmRoll4RotateAxisz

    LeafRightForeArmRoll4JointOrient = LeafRightForeArmRoll4JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll4JointOrientx = LeafRightForeArmRoll4JointOrient.LeafRightForeArmRoll4JointOrientx
    LeafRightForeArmRoll4JointOrienty = LeafRightForeArmRoll4JointOrient.LeafRightForeArmRoll4JointOrienty
    LeafRightForeArmRoll4JointOrientz = LeafRightForeArmRoll4JointOrient.LeafRightForeArmRoll4JointOrientz

    LeafRightForeArmRoll4MinRLimit = LeafRightForeArmRoll4MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll4MinRLimitx = LeafRightForeArmRoll4MinRLimit.LeafRightForeArmRoll4MinRLimitx
    LeafRightForeArmRoll4MinRLimity = LeafRightForeArmRoll4MinRLimit.LeafRightForeArmRoll4MinRLimity
    LeafRightForeArmRoll4MinRLimitz = LeafRightForeArmRoll4MinRLimit.LeafRightForeArmRoll4MinRLimitz

    LeafRightForeArmRoll4MaxRLimit = LeafRightForeArmRoll4MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll4MaxRLimitx = LeafRightForeArmRoll4MaxRLimit.LeafRightForeArmRoll4MaxRLimitx
    LeafRightForeArmRoll4MaxRLimity = LeafRightForeArmRoll4MaxRLimit.LeafRightForeArmRoll4MaxRLimity
    LeafRightForeArmRoll4MaxRLimitz = LeafRightForeArmRoll4MaxRLimit.LeafRightForeArmRoll4MaxRLimitz

    LeafRightForeArmRoll4MinRLimitEnablex = BoolField(default_value=False)

    LeafRightForeArmRoll4MinRLimitEnabley = BoolField(default_value=False)

    LeafRightForeArmRoll4MinRLimitEnablez = BoolField(default_value=False)

    LeafRightForeArmRoll4MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightForeArmRoll4MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightForeArmRoll4MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftUpLegRoll5 = MessageField()

    LeafLeftUpLegRoll5T = LeafLeftUpLegRoll5TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll5Tx = LeafLeftUpLegRoll5T.LeafLeftUpLegRoll5Tx
    LeafLeftUpLegRoll5Ty = LeafLeftUpLegRoll5T.LeafLeftUpLegRoll5Ty
    LeafLeftUpLegRoll5Tz = LeafLeftUpLegRoll5T.LeafLeftUpLegRoll5Tz

    LeafLeftUpLegRoll5R = LeafLeftUpLegRoll5RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll5Rx = LeafLeftUpLegRoll5R.LeafLeftUpLegRoll5Rx
    LeafLeftUpLegRoll5Ry = LeafLeftUpLegRoll5R.LeafLeftUpLegRoll5Ry
    LeafLeftUpLegRoll5Rz = LeafLeftUpLegRoll5R.LeafLeftUpLegRoll5Rz

    LeafLeftUpLegRoll5S = LeafLeftUpLegRoll5SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftUpLegRoll5Sx = LeafLeftUpLegRoll5S.LeafLeftUpLegRoll5Sx
    LeafLeftUpLegRoll5Sy = LeafLeftUpLegRoll5S.LeafLeftUpLegRoll5Sy
    LeafLeftUpLegRoll5Sz = LeafLeftUpLegRoll5S.LeafLeftUpLegRoll5Sz

    LeafLeftUpLegRoll5RotateOrder = LeafLeftUpLegRoll5RotateOrderEnumField(default_value=0)

    LeafLeftUpLegRoll5RotateAxis = LeafLeftUpLegRoll5RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll5RotateAxisx = LeafLeftUpLegRoll5RotateAxis.LeafLeftUpLegRoll5RotateAxisx
    LeafLeftUpLegRoll5RotateAxisy = LeafLeftUpLegRoll5RotateAxis.LeafLeftUpLegRoll5RotateAxisy
    LeafLeftUpLegRoll5RotateAxisz = LeafLeftUpLegRoll5RotateAxis.LeafLeftUpLegRoll5RotateAxisz

    LeafLeftUpLegRoll5JointOrient = LeafLeftUpLegRoll5JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll5JointOrientx = LeafLeftUpLegRoll5JointOrient.LeafLeftUpLegRoll5JointOrientx
    LeafLeftUpLegRoll5JointOrienty = LeafLeftUpLegRoll5JointOrient.LeafLeftUpLegRoll5JointOrienty
    LeafLeftUpLegRoll5JointOrientz = LeafLeftUpLegRoll5JointOrient.LeafLeftUpLegRoll5JointOrientz

    LeafLeftUpLegRoll5MinRLimit = LeafLeftUpLegRoll5MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll5MinRLimitx = LeafLeftUpLegRoll5MinRLimit.LeafLeftUpLegRoll5MinRLimitx
    LeafLeftUpLegRoll5MinRLimity = LeafLeftUpLegRoll5MinRLimit.LeafLeftUpLegRoll5MinRLimity
    LeafLeftUpLegRoll5MinRLimitz = LeafLeftUpLegRoll5MinRLimit.LeafLeftUpLegRoll5MinRLimitz

    LeafLeftUpLegRoll5MaxRLimit = LeafLeftUpLegRoll5MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll5MaxRLimitx = LeafLeftUpLegRoll5MaxRLimit.LeafLeftUpLegRoll5MaxRLimitx
    LeafLeftUpLegRoll5MaxRLimity = LeafLeftUpLegRoll5MaxRLimit.LeafLeftUpLegRoll5MaxRLimity
    LeafLeftUpLegRoll5MaxRLimitz = LeafLeftUpLegRoll5MaxRLimit.LeafLeftUpLegRoll5MaxRLimitz

    LeafLeftUpLegRoll5MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftUpLegRoll5MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftUpLegRoll5MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftUpLegRoll5MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftUpLegRoll5MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftUpLegRoll5MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftLegRoll5 = MessageField()

    LeafLeftLegRoll5T = LeafLeftLegRoll5TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll5Tx = LeafLeftLegRoll5T.LeafLeftLegRoll5Tx
    LeafLeftLegRoll5Ty = LeafLeftLegRoll5T.LeafLeftLegRoll5Ty
    LeafLeftLegRoll5Tz = LeafLeftLegRoll5T.LeafLeftLegRoll5Tz

    LeafLeftLegRoll5R = LeafLeftLegRoll5RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll5Rx = LeafLeftLegRoll5R.LeafLeftLegRoll5Rx
    LeafLeftLegRoll5Ry = LeafLeftLegRoll5R.LeafLeftLegRoll5Ry
    LeafLeftLegRoll5Rz = LeafLeftLegRoll5R.LeafLeftLegRoll5Rz

    LeafLeftLegRoll5S = LeafLeftLegRoll5SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftLegRoll5Sx = LeafLeftLegRoll5S.LeafLeftLegRoll5Sx
    LeafLeftLegRoll5Sy = LeafLeftLegRoll5S.LeafLeftLegRoll5Sy
    LeafLeftLegRoll5Sz = LeafLeftLegRoll5S.LeafLeftLegRoll5Sz

    LeafLeftLegRoll5RotateOrder = LeafLeftLegRoll5RotateOrderEnumField(default_value=0)

    LeafLeftLegRoll5RotateAxis = LeafLeftLegRoll5RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll5RotateAxisx = LeafLeftLegRoll5RotateAxis.LeafLeftLegRoll5RotateAxisx
    LeafLeftLegRoll5RotateAxisy = LeafLeftLegRoll5RotateAxis.LeafLeftLegRoll5RotateAxisy
    LeafLeftLegRoll5RotateAxisz = LeafLeftLegRoll5RotateAxis.LeafLeftLegRoll5RotateAxisz

    LeafLeftLegRoll5JointOrient = LeafLeftLegRoll5JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll5JointOrientx = LeafLeftLegRoll5JointOrient.LeafLeftLegRoll5JointOrientx
    LeafLeftLegRoll5JointOrienty = LeafLeftLegRoll5JointOrient.LeafLeftLegRoll5JointOrienty
    LeafLeftLegRoll5JointOrientz = LeafLeftLegRoll5JointOrient.LeafLeftLegRoll5JointOrientz

    LeafLeftLegRoll5MinRLimit = LeafLeftLegRoll5MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll5MinRLimitx = LeafLeftLegRoll5MinRLimit.LeafLeftLegRoll5MinRLimitx
    LeafLeftLegRoll5MinRLimity = LeafLeftLegRoll5MinRLimit.LeafLeftLegRoll5MinRLimity
    LeafLeftLegRoll5MinRLimitz = LeafLeftLegRoll5MinRLimit.LeafLeftLegRoll5MinRLimitz

    LeafLeftLegRoll5MaxRLimit = LeafLeftLegRoll5MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll5MaxRLimitx = LeafLeftLegRoll5MaxRLimit.LeafLeftLegRoll5MaxRLimitx
    LeafLeftLegRoll5MaxRLimity = LeafLeftLegRoll5MaxRLimit.LeafLeftLegRoll5MaxRLimity
    LeafLeftLegRoll5MaxRLimitz = LeafLeftLegRoll5MaxRLimit.LeafLeftLegRoll5MaxRLimitz

    LeafLeftLegRoll5MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftLegRoll5MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftLegRoll5MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftLegRoll5MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftLegRoll5MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftLegRoll5MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightUpLegRoll5 = MessageField()

    LeafRightUpLegRoll5T = LeafRightUpLegRoll5TField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll5Tx = LeafRightUpLegRoll5T.LeafRightUpLegRoll5Tx
    LeafRightUpLegRoll5Ty = LeafRightUpLegRoll5T.LeafRightUpLegRoll5Ty
    LeafRightUpLegRoll5Tz = LeafRightUpLegRoll5T.LeafRightUpLegRoll5Tz

    LeafRightUpLegRoll5R = LeafRightUpLegRoll5RField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll5Rx = LeafRightUpLegRoll5R.LeafRightUpLegRoll5Rx
    LeafRightUpLegRoll5Ry = LeafRightUpLegRoll5R.LeafRightUpLegRoll5Ry
    LeafRightUpLegRoll5Rz = LeafRightUpLegRoll5R.LeafRightUpLegRoll5Rz

    LeafRightUpLegRoll5S = LeafRightUpLegRoll5SField(default_value=(1.0, 1.0, 1.0))
    LeafRightUpLegRoll5Sx = LeafRightUpLegRoll5S.LeafRightUpLegRoll5Sx
    LeafRightUpLegRoll5Sy = LeafRightUpLegRoll5S.LeafRightUpLegRoll5Sy
    LeafRightUpLegRoll5Sz = LeafRightUpLegRoll5S.LeafRightUpLegRoll5Sz

    LeafRightUpLegRoll5RotateOrder = LeafRightUpLegRoll5RotateOrderEnumField(default_value=0)

    LeafRightUpLegRoll5RotateAxis = LeafRightUpLegRoll5RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll5RotateAxisx = LeafRightUpLegRoll5RotateAxis.LeafRightUpLegRoll5RotateAxisx
    LeafRightUpLegRoll5RotateAxisy = LeafRightUpLegRoll5RotateAxis.LeafRightUpLegRoll5RotateAxisy
    LeafRightUpLegRoll5RotateAxisz = LeafRightUpLegRoll5RotateAxis.LeafRightUpLegRoll5RotateAxisz

    LeafRightUpLegRoll5JointOrient = LeafRightUpLegRoll5JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll5JointOrientx = LeafRightUpLegRoll5JointOrient.LeafRightUpLegRoll5JointOrientx
    LeafRightUpLegRoll5JointOrienty = LeafRightUpLegRoll5JointOrient.LeafRightUpLegRoll5JointOrienty
    LeafRightUpLegRoll5JointOrientz = LeafRightUpLegRoll5JointOrient.LeafRightUpLegRoll5JointOrientz

    LeafRightUpLegRoll5MinRLimit = LeafRightUpLegRoll5MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll5MinRLimitx = LeafRightUpLegRoll5MinRLimit.LeafRightUpLegRoll5MinRLimitx
    LeafRightUpLegRoll5MinRLimity = LeafRightUpLegRoll5MinRLimit.LeafRightUpLegRoll5MinRLimity
    LeafRightUpLegRoll5MinRLimitz = LeafRightUpLegRoll5MinRLimit.LeafRightUpLegRoll5MinRLimitz

    LeafRightUpLegRoll5MaxRLimit = LeafRightUpLegRoll5MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll5MaxRLimitx = LeafRightUpLegRoll5MaxRLimit.LeafRightUpLegRoll5MaxRLimitx
    LeafRightUpLegRoll5MaxRLimity = LeafRightUpLegRoll5MaxRLimit.LeafRightUpLegRoll5MaxRLimity
    LeafRightUpLegRoll5MaxRLimitz = LeafRightUpLegRoll5MaxRLimit.LeafRightUpLegRoll5MaxRLimitz

    LeafRightUpLegRoll5MinRLimitEnablex = BoolField(default_value=False)

    LeafRightUpLegRoll5MinRLimitEnabley = BoolField(default_value=False)

    LeafRightUpLegRoll5MinRLimitEnablez = BoolField(default_value=False)

    LeafRightUpLegRoll5MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightUpLegRoll5MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightUpLegRoll5MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightLegRoll5 = MessageField()

    LeafRightLegRoll5T = LeafRightLegRoll5TField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll5Tx = LeafRightLegRoll5T.LeafRightLegRoll5Tx
    LeafRightLegRoll5Ty = LeafRightLegRoll5T.LeafRightLegRoll5Ty
    LeafRightLegRoll5Tz = LeafRightLegRoll5T.LeafRightLegRoll5Tz

    LeafRightLegRoll5R = LeafRightLegRoll5RField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll5Rx = LeafRightLegRoll5R.LeafRightLegRoll5Rx
    LeafRightLegRoll5Ry = LeafRightLegRoll5R.LeafRightLegRoll5Ry
    LeafRightLegRoll5Rz = LeafRightLegRoll5R.LeafRightLegRoll5Rz

    LeafRightLegRoll5S = LeafRightLegRoll5SField(default_value=(1.0, 1.0, 1.0))
    LeafRightLegRoll5Sx = LeafRightLegRoll5S.LeafRightLegRoll5Sx
    LeafRightLegRoll5Sy = LeafRightLegRoll5S.LeafRightLegRoll5Sy
    LeafRightLegRoll5Sz = LeafRightLegRoll5S.LeafRightLegRoll5Sz

    LeafRightLegRoll5RotateOrder = LeafRightLegRoll5RotateOrderEnumField(default_value=0)

    LeafRightLegRoll5RotateAxis = LeafRightLegRoll5RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll5RotateAxisx = LeafRightLegRoll5RotateAxis.LeafRightLegRoll5RotateAxisx
    LeafRightLegRoll5RotateAxisy = LeafRightLegRoll5RotateAxis.LeafRightLegRoll5RotateAxisy
    LeafRightLegRoll5RotateAxisz = LeafRightLegRoll5RotateAxis.LeafRightLegRoll5RotateAxisz

    LeafRightLegRoll5JointOrient = LeafRightLegRoll5JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll5JointOrientx = LeafRightLegRoll5JointOrient.LeafRightLegRoll5JointOrientx
    LeafRightLegRoll5JointOrienty = LeafRightLegRoll5JointOrient.LeafRightLegRoll5JointOrienty
    LeafRightLegRoll5JointOrientz = LeafRightLegRoll5JointOrient.LeafRightLegRoll5JointOrientz

    LeafRightLegRoll5MinRLimit = LeafRightLegRoll5MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll5MinRLimitx = LeafRightLegRoll5MinRLimit.LeafRightLegRoll5MinRLimitx
    LeafRightLegRoll5MinRLimity = LeafRightLegRoll5MinRLimit.LeafRightLegRoll5MinRLimity
    LeafRightLegRoll5MinRLimitz = LeafRightLegRoll5MinRLimit.LeafRightLegRoll5MinRLimitz

    LeafRightLegRoll5MaxRLimit = LeafRightLegRoll5MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll5MaxRLimitx = LeafRightLegRoll5MaxRLimit.LeafRightLegRoll5MaxRLimitx
    LeafRightLegRoll5MaxRLimity = LeafRightLegRoll5MaxRLimit.LeafRightLegRoll5MaxRLimity
    LeafRightLegRoll5MaxRLimitz = LeafRightLegRoll5MaxRLimit.LeafRightLegRoll5MaxRLimitz

    LeafRightLegRoll5MinRLimitEnablex = BoolField(default_value=False)

    LeafRightLegRoll5MinRLimitEnabley = BoolField(default_value=False)

    LeafRightLegRoll5MinRLimitEnablez = BoolField(default_value=False)

    LeafRightLegRoll5MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightLegRoll5MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightLegRoll5MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftArmRoll5 = MessageField()

    LeafLeftArmRoll5T = LeafLeftArmRoll5TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll5Tx = LeafLeftArmRoll5T.LeafLeftArmRoll5Tx
    LeafLeftArmRoll5Ty = LeafLeftArmRoll5T.LeafLeftArmRoll5Ty
    LeafLeftArmRoll5Tz = LeafLeftArmRoll5T.LeafLeftArmRoll5Tz

    LeafLeftArmRoll5R = LeafLeftArmRoll5RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll5Rx = LeafLeftArmRoll5R.LeafLeftArmRoll5Rx
    LeafLeftArmRoll5Ry = LeafLeftArmRoll5R.LeafLeftArmRoll5Ry
    LeafLeftArmRoll5Rz = LeafLeftArmRoll5R.LeafLeftArmRoll5Rz

    LeafLeftArmRoll5S = LeafLeftArmRoll5SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftArmRoll5Sx = LeafLeftArmRoll5S.LeafLeftArmRoll5Sx
    LeafLeftArmRoll5Sy = LeafLeftArmRoll5S.LeafLeftArmRoll5Sy
    LeafLeftArmRoll5Sz = LeafLeftArmRoll5S.LeafLeftArmRoll5Sz

    LeafLeftArmRoll5RotateOrder = LeafLeftArmRoll5RotateOrderEnumField(default_value=0)

    LeafLeftArmRoll5RotateAxis = LeafLeftArmRoll5RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll5RotateAxisx = LeafLeftArmRoll5RotateAxis.LeafLeftArmRoll5RotateAxisx
    LeafLeftArmRoll5RotateAxisy = LeafLeftArmRoll5RotateAxis.LeafLeftArmRoll5RotateAxisy
    LeafLeftArmRoll5RotateAxisz = LeafLeftArmRoll5RotateAxis.LeafLeftArmRoll5RotateAxisz

    LeafLeftArmRoll5JointOrient = LeafLeftArmRoll5JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll5JointOrientx = LeafLeftArmRoll5JointOrient.LeafLeftArmRoll5JointOrientx
    LeafLeftArmRoll5JointOrienty = LeafLeftArmRoll5JointOrient.LeafLeftArmRoll5JointOrienty
    LeafLeftArmRoll5JointOrientz = LeafLeftArmRoll5JointOrient.LeafLeftArmRoll5JointOrientz

    LeafLeftArmRoll5MinRLimit = LeafLeftArmRoll5MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll5MinRLimitx = LeafLeftArmRoll5MinRLimit.LeafLeftArmRoll5MinRLimitx
    LeafLeftArmRoll5MinRLimity = LeafLeftArmRoll5MinRLimit.LeafLeftArmRoll5MinRLimity
    LeafLeftArmRoll5MinRLimitz = LeafLeftArmRoll5MinRLimit.LeafLeftArmRoll5MinRLimitz

    LeafLeftArmRoll5MaxRLimit = LeafLeftArmRoll5MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll5MaxRLimitx = LeafLeftArmRoll5MaxRLimit.LeafLeftArmRoll5MaxRLimitx
    LeafLeftArmRoll5MaxRLimity = LeafLeftArmRoll5MaxRLimit.LeafLeftArmRoll5MaxRLimity
    LeafLeftArmRoll5MaxRLimitz = LeafLeftArmRoll5MaxRLimit.LeafLeftArmRoll5MaxRLimitz

    LeafLeftArmRoll5MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftArmRoll5MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftArmRoll5MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftArmRoll5MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftArmRoll5MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftArmRoll5MaxRLimitEnablez = BoolField(default_value=False)

    LeafLeftForeArmRoll5 = MessageField()

    LeafLeftForeArmRoll5T = LeafLeftForeArmRoll5TField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll5Tx = LeafLeftForeArmRoll5T.LeafLeftForeArmRoll5Tx
    LeafLeftForeArmRoll5Ty = LeafLeftForeArmRoll5T.LeafLeftForeArmRoll5Ty
    LeafLeftForeArmRoll5Tz = LeafLeftForeArmRoll5T.LeafLeftForeArmRoll5Tz

    LeafLeftForeArmRoll5R = LeafLeftForeArmRoll5RField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll5Rx = LeafLeftForeArmRoll5R.LeafLeftForeArmRoll5Rx
    LeafLeftForeArmRoll5Ry = LeafLeftForeArmRoll5R.LeafLeftForeArmRoll5Ry
    LeafLeftForeArmRoll5Rz = LeafLeftForeArmRoll5R.LeafLeftForeArmRoll5Rz

    LeafLeftForeArmRoll5S = LeafLeftForeArmRoll5SField(default_value=(1.0, 1.0, 1.0))
    LeafLeftForeArmRoll5Sx = LeafLeftForeArmRoll5S.LeafLeftForeArmRoll5Sx
    LeafLeftForeArmRoll5Sy = LeafLeftForeArmRoll5S.LeafLeftForeArmRoll5Sy
    LeafLeftForeArmRoll5Sz = LeafLeftForeArmRoll5S.LeafLeftForeArmRoll5Sz

    LeafLeftForeArmRoll5RotateOrder = LeafLeftForeArmRoll5RotateOrderEnumField(default_value=0)

    LeafLeftForeArmRoll5RotateAxis = LeafLeftForeArmRoll5RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll5RotateAxisx = LeafLeftForeArmRoll5RotateAxis.LeafLeftForeArmRoll5RotateAxisx
    LeafLeftForeArmRoll5RotateAxisy = LeafLeftForeArmRoll5RotateAxis.LeafLeftForeArmRoll5RotateAxisy
    LeafLeftForeArmRoll5RotateAxisz = LeafLeftForeArmRoll5RotateAxis.LeafLeftForeArmRoll5RotateAxisz

    LeafLeftForeArmRoll5JointOrient = LeafLeftForeArmRoll5JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll5JointOrientx = LeafLeftForeArmRoll5JointOrient.LeafLeftForeArmRoll5JointOrientx
    LeafLeftForeArmRoll5JointOrienty = LeafLeftForeArmRoll5JointOrient.LeafLeftForeArmRoll5JointOrienty
    LeafLeftForeArmRoll5JointOrientz = LeafLeftForeArmRoll5JointOrient.LeafLeftForeArmRoll5JointOrientz

    LeafLeftForeArmRoll5MinRLimit = LeafLeftForeArmRoll5MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll5MinRLimitx = LeafLeftForeArmRoll5MinRLimit.LeafLeftForeArmRoll5MinRLimitx
    LeafLeftForeArmRoll5MinRLimity = LeafLeftForeArmRoll5MinRLimit.LeafLeftForeArmRoll5MinRLimity
    LeafLeftForeArmRoll5MinRLimitz = LeafLeftForeArmRoll5MinRLimit.LeafLeftForeArmRoll5MinRLimitz

    LeafLeftForeArmRoll5MaxRLimit = LeafLeftForeArmRoll5MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll5MaxRLimitx = LeafLeftForeArmRoll5MaxRLimit.LeafLeftForeArmRoll5MaxRLimitx
    LeafLeftForeArmRoll5MaxRLimity = LeafLeftForeArmRoll5MaxRLimit.LeafLeftForeArmRoll5MaxRLimity
    LeafLeftForeArmRoll5MaxRLimitz = LeafLeftForeArmRoll5MaxRLimit.LeafLeftForeArmRoll5MaxRLimitz

    LeafLeftForeArmRoll5MinRLimitEnablex = BoolField(default_value=False)

    LeafLeftForeArmRoll5MinRLimitEnabley = BoolField(default_value=False)

    LeafLeftForeArmRoll5MinRLimitEnablez = BoolField(default_value=False)

    LeafLeftForeArmRoll5MaxRLimitEnablex = BoolField(default_value=False)

    LeafLeftForeArmRoll5MaxRLimitEnabley = BoolField(default_value=False)

    LeafLeftForeArmRoll5MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightArmRoll5 = MessageField()

    LeafRightArmRoll5T = LeafRightArmRoll5TField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll5Tx = LeafRightArmRoll5T.LeafRightArmRoll5Tx
    LeafRightArmRoll5Ty = LeafRightArmRoll5T.LeafRightArmRoll5Ty
    LeafRightArmRoll5Tz = LeafRightArmRoll5T.LeafRightArmRoll5Tz

    LeafRightArmRoll5R = LeafRightArmRoll5RField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll5Rx = LeafRightArmRoll5R.LeafRightArmRoll5Rx
    LeafRightArmRoll5Ry = LeafRightArmRoll5R.LeafRightArmRoll5Ry
    LeafRightArmRoll5Rz = LeafRightArmRoll5R.LeafRightArmRoll5Rz

    LeafRightArmRoll5S = LeafRightArmRoll5SField(default_value=(1.0, 1.0, 1.0))
    LeafRightArmRoll5Sx = LeafRightArmRoll5S.LeafRightArmRoll5Sx
    LeafRightArmRoll5Sy = LeafRightArmRoll5S.LeafRightArmRoll5Sy
    LeafRightArmRoll5Sz = LeafRightArmRoll5S.LeafRightArmRoll5Sz

    LeafRightArmRoll5RotateOrder = LeafRightArmRoll5RotateOrderEnumField(default_value=0)

    LeafRightArmRoll5RotateAxis = LeafRightArmRoll5RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll5RotateAxisx = LeafRightArmRoll5RotateAxis.LeafRightArmRoll5RotateAxisx
    LeafRightArmRoll5RotateAxisy = LeafRightArmRoll5RotateAxis.LeafRightArmRoll5RotateAxisy
    LeafRightArmRoll5RotateAxisz = LeafRightArmRoll5RotateAxis.LeafRightArmRoll5RotateAxisz

    LeafRightArmRoll5JointOrient = LeafRightArmRoll5JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll5JointOrientx = LeafRightArmRoll5JointOrient.LeafRightArmRoll5JointOrientx
    LeafRightArmRoll5JointOrienty = LeafRightArmRoll5JointOrient.LeafRightArmRoll5JointOrienty
    LeafRightArmRoll5JointOrientz = LeafRightArmRoll5JointOrient.LeafRightArmRoll5JointOrientz

    LeafRightArmRoll5MinRLimit = LeafRightArmRoll5MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll5MinRLimitx = LeafRightArmRoll5MinRLimit.LeafRightArmRoll5MinRLimitx
    LeafRightArmRoll5MinRLimity = LeafRightArmRoll5MinRLimit.LeafRightArmRoll5MinRLimity
    LeafRightArmRoll5MinRLimitz = LeafRightArmRoll5MinRLimit.LeafRightArmRoll5MinRLimitz

    LeafRightArmRoll5MaxRLimit = LeafRightArmRoll5MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll5MaxRLimitx = LeafRightArmRoll5MaxRLimit.LeafRightArmRoll5MaxRLimitx
    LeafRightArmRoll5MaxRLimity = LeafRightArmRoll5MaxRLimit.LeafRightArmRoll5MaxRLimity
    LeafRightArmRoll5MaxRLimitz = LeafRightArmRoll5MaxRLimit.LeafRightArmRoll5MaxRLimitz

    LeafRightArmRoll5MinRLimitEnablex = BoolField(default_value=False)

    LeafRightArmRoll5MinRLimitEnabley = BoolField(default_value=False)

    LeafRightArmRoll5MinRLimitEnablez = BoolField(default_value=False)

    LeafRightArmRoll5MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightArmRoll5MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightArmRoll5MaxRLimitEnablez = BoolField(default_value=False)

    LeafRightForeArmRoll5 = MessageField()

    LeafRightForeArmRoll5T = LeafRightForeArmRoll5TField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll5Tx = LeafRightForeArmRoll5T.LeafRightForeArmRoll5Tx
    LeafRightForeArmRoll5Ty = LeafRightForeArmRoll5T.LeafRightForeArmRoll5Ty
    LeafRightForeArmRoll5Tz = LeafRightForeArmRoll5T.LeafRightForeArmRoll5Tz

    LeafRightForeArmRoll5R = LeafRightForeArmRoll5RField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll5Rx = LeafRightForeArmRoll5R.LeafRightForeArmRoll5Rx
    LeafRightForeArmRoll5Ry = LeafRightForeArmRoll5R.LeafRightForeArmRoll5Ry
    LeafRightForeArmRoll5Rz = LeafRightForeArmRoll5R.LeafRightForeArmRoll5Rz

    LeafRightForeArmRoll5S = LeafRightForeArmRoll5SField(default_value=(1.0, 1.0, 1.0))
    LeafRightForeArmRoll5Sx = LeafRightForeArmRoll5S.LeafRightForeArmRoll5Sx
    LeafRightForeArmRoll5Sy = LeafRightForeArmRoll5S.LeafRightForeArmRoll5Sy
    LeafRightForeArmRoll5Sz = LeafRightForeArmRoll5S.LeafRightForeArmRoll5Sz

    LeafRightForeArmRoll5RotateOrder = LeafRightForeArmRoll5RotateOrderEnumField(default_value=0)

    LeafRightForeArmRoll5RotateAxis = LeafRightForeArmRoll5RotateAxisField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll5RotateAxisx = LeafRightForeArmRoll5RotateAxis.LeafRightForeArmRoll5RotateAxisx
    LeafRightForeArmRoll5RotateAxisy = LeafRightForeArmRoll5RotateAxis.LeafRightForeArmRoll5RotateAxisy
    LeafRightForeArmRoll5RotateAxisz = LeafRightForeArmRoll5RotateAxis.LeafRightForeArmRoll5RotateAxisz

    LeafRightForeArmRoll5JointOrient = LeafRightForeArmRoll5JointOrientField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll5JointOrientx = LeafRightForeArmRoll5JointOrient.LeafRightForeArmRoll5JointOrientx
    LeafRightForeArmRoll5JointOrienty = LeafRightForeArmRoll5JointOrient.LeafRightForeArmRoll5JointOrienty
    LeafRightForeArmRoll5JointOrientz = LeafRightForeArmRoll5JointOrient.LeafRightForeArmRoll5JointOrientz

    LeafRightForeArmRoll5MinRLimit = LeafRightForeArmRoll5MinRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll5MinRLimitx = LeafRightForeArmRoll5MinRLimit.LeafRightForeArmRoll5MinRLimitx
    LeafRightForeArmRoll5MinRLimity = LeafRightForeArmRoll5MinRLimit.LeafRightForeArmRoll5MinRLimity
    LeafRightForeArmRoll5MinRLimitz = LeafRightForeArmRoll5MinRLimit.LeafRightForeArmRoll5MinRLimitz

    LeafRightForeArmRoll5MaxRLimit = LeafRightForeArmRoll5MaxRLimitField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll5MaxRLimitx = LeafRightForeArmRoll5MaxRLimit.LeafRightForeArmRoll5MaxRLimitx
    LeafRightForeArmRoll5MaxRLimity = LeafRightForeArmRoll5MaxRLimit.LeafRightForeArmRoll5MaxRLimity
    LeafRightForeArmRoll5MaxRLimitz = LeafRightForeArmRoll5MaxRLimit.LeafRightForeArmRoll5MaxRLimitz

    LeafRightForeArmRoll5MinRLimitEnablex = BoolField(default_value=False)

    LeafRightForeArmRoll5MinRLimitEnabley = BoolField(default_value=False)

    LeafRightForeArmRoll5MinRLimitEnablez = BoolField(default_value=False)

    LeafRightForeArmRoll5MaxRLimitEnablex = BoolField(default_value=False)

    LeafRightForeArmRoll5MaxRLimitEnabley = BoolField(default_value=False)

    LeafRightForeArmRoll5MaxRLimitEnablez = BoolField(default_value=False)
