# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.hik_state2_sk import (
    HeadISField,
    HeadPostRField,
    HeadPreRField,
    HeadRField,
    HeadSField,
    HeadTField,
    HipsISField,
    HipsPostRField,
    HipsPreRField,
    HipsRField,
    HipsSField,
    HipsTField,
    HipsTranslationISField,
    HipsTranslationPostRField,
    HipsTranslationPreRField,
    HipsTranslationRField,
    HipsTranslationSField,
    HipsTranslationTField,
    LeafLeftArmRoll1ISField,
    LeafLeftArmRoll1PostRField,
    LeafLeftArmRoll1PreRField,
    LeafLeftArmRoll1RField,
    LeafLeftArmRoll1SField,
    LeafLeftArmRoll1TField,
    LeafLeftArmRoll2ISField,
    LeafLeftArmRoll2PostRField,
    LeafLeftArmRoll2PreRField,
    LeafLeftArmRoll2RField,
    LeafLeftArmRoll2SField,
    LeafLeftArmRoll2TField,
    LeafLeftArmRoll3ISField,
    LeafLeftArmRoll3PostRField,
    LeafLeftArmRoll3PreRField,
    LeafLeftArmRoll3RField,
    LeafLeftArmRoll3SField,
    LeafLeftArmRoll3TField,
    LeafLeftArmRoll4ISField,
    LeafLeftArmRoll4PostRField,
    LeafLeftArmRoll4PreRField,
    LeafLeftArmRoll4RField,
    LeafLeftArmRoll4SField,
    LeafLeftArmRoll4TField,
    LeafLeftArmRoll5ISField,
    LeafLeftArmRoll5PostRField,
    LeafLeftArmRoll5PreRField,
    LeafLeftArmRoll5RField,
    LeafLeftArmRoll5SField,
    LeafLeftArmRoll5TField,
    LeafLeftForeArmRoll1ISField,
    LeafLeftForeArmRoll1PostRField,
    LeafLeftForeArmRoll1PreRField,
    LeafLeftForeArmRoll1RField,
    LeafLeftForeArmRoll1SField,
    LeafLeftForeArmRoll1TField,
    LeafLeftForeArmRoll2ISField,
    LeafLeftForeArmRoll2PostRField,
    LeafLeftForeArmRoll2PreRField,
    LeafLeftForeArmRoll2RField,
    LeafLeftForeArmRoll2SField,
    LeafLeftForeArmRoll2TField,
    LeafLeftForeArmRoll3ISField,
    LeafLeftForeArmRoll3PostRField,
    LeafLeftForeArmRoll3PreRField,
    LeafLeftForeArmRoll3RField,
    LeafLeftForeArmRoll3SField,
    LeafLeftForeArmRoll3TField,
    LeafLeftForeArmRoll4ISField,
    LeafLeftForeArmRoll4PostRField,
    LeafLeftForeArmRoll4PreRField,
    LeafLeftForeArmRoll4RField,
    LeafLeftForeArmRoll4SField,
    LeafLeftForeArmRoll4TField,
    LeafLeftForeArmRoll5ISField,
    LeafLeftForeArmRoll5PostRField,
    LeafLeftForeArmRoll5PreRField,
    LeafLeftForeArmRoll5RField,
    LeafLeftForeArmRoll5SField,
    LeafLeftForeArmRoll5TField,
    LeafLeftLegRoll1ISField,
    LeafLeftLegRoll1PostRField,
    LeafLeftLegRoll1PreRField,
    LeafLeftLegRoll1RField,
    LeafLeftLegRoll1SField,
    LeafLeftLegRoll1TField,
    LeafLeftLegRoll2ISField,
    LeafLeftLegRoll2PostRField,
    LeafLeftLegRoll2PreRField,
    LeafLeftLegRoll2RField,
    LeafLeftLegRoll2SField,
    LeafLeftLegRoll2TField,
    LeafLeftLegRoll3ISField,
    LeafLeftLegRoll3PostRField,
    LeafLeftLegRoll3PreRField,
    LeafLeftLegRoll3RField,
    LeafLeftLegRoll3SField,
    LeafLeftLegRoll3TField,
    LeafLeftLegRoll4ISField,
    LeafLeftLegRoll4PostRField,
    LeafLeftLegRoll4PreRField,
    LeafLeftLegRoll4RField,
    LeafLeftLegRoll4SField,
    LeafLeftLegRoll4TField,
    LeafLeftLegRoll5ISField,
    LeafLeftLegRoll5PostRField,
    LeafLeftLegRoll5PreRField,
    LeafLeftLegRoll5RField,
    LeafLeftLegRoll5SField,
    LeafLeftLegRoll5TField,
    LeafLeftUpLegRoll1ISField,
    LeafLeftUpLegRoll1PostRField,
    LeafLeftUpLegRoll1PreRField,
    LeafLeftUpLegRoll1RField,
    LeafLeftUpLegRoll1SField,
    LeafLeftUpLegRoll1TField,
    LeafLeftUpLegRoll2ISField,
    LeafLeftUpLegRoll2PostRField,
    LeafLeftUpLegRoll2PreRField,
    LeafLeftUpLegRoll2RField,
    LeafLeftUpLegRoll2SField,
    LeafLeftUpLegRoll2TField,
    LeafLeftUpLegRoll3ISField,
    LeafLeftUpLegRoll3PostRField,
    LeafLeftUpLegRoll3PreRField,
    LeafLeftUpLegRoll3RField,
    LeafLeftUpLegRoll3SField,
    LeafLeftUpLegRoll3TField,
    LeafLeftUpLegRoll4ISField,
    LeafLeftUpLegRoll4PostRField,
    LeafLeftUpLegRoll4PreRField,
    LeafLeftUpLegRoll4RField,
    LeafLeftUpLegRoll4SField,
    LeafLeftUpLegRoll4TField,
    LeafLeftUpLegRoll5ISField,
    LeafLeftUpLegRoll5PostRField,
    LeafLeftUpLegRoll5PreRField,
    LeafLeftUpLegRoll5RField,
    LeafLeftUpLegRoll5SField,
    LeafLeftUpLegRoll5TField,
    LeafRightArmRoll1ISField,
    LeafRightArmRoll1PostRField,
    LeafRightArmRoll1PreRField,
    LeafRightArmRoll1RField,
    LeafRightArmRoll1SField,
    LeafRightArmRoll1TField,
    LeafRightArmRoll2ISField,
    LeafRightArmRoll2PostRField,
    LeafRightArmRoll2PreRField,
    LeafRightArmRoll2RField,
    LeafRightArmRoll2SField,
    LeafRightArmRoll2TField,
    LeafRightArmRoll3ISField,
    LeafRightArmRoll3PostRField,
    LeafRightArmRoll3PreRField,
    LeafRightArmRoll3RField,
    LeafRightArmRoll3SField,
    LeafRightArmRoll3TField,
    LeafRightArmRoll4ISField,
    LeafRightArmRoll4PostRField,
    LeafRightArmRoll4PreRField,
    LeafRightArmRoll4RField,
    LeafRightArmRoll4SField,
    LeafRightArmRoll4TField,
    LeafRightArmRoll5ISField,
    LeafRightArmRoll5PostRField,
    LeafRightArmRoll5PreRField,
    LeafRightArmRoll5RField,
    LeafRightArmRoll5SField,
    LeafRightArmRoll5TField,
    LeafRightForeArmRoll1ISField,
    LeafRightForeArmRoll1PostRField,
    LeafRightForeArmRoll1PreRField,
    LeafRightForeArmRoll1RField,
    LeafRightForeArmRoll1SField,
    LeafRightForeArmRoll1TField,
    LeafRightForeArmRoll2ISField,
    LeafRightForeArmRoll2PostRField,
    LeafRightForeArmRoll2PreRField,
    LeafRightForeArmRoll2RField,
    LeafRightForeArmRoll2SField,
    LeafRightForeArmRoll2TField,
    LeafRightForeArmRoll3ISField,
    LeafRightForeArmRoll3PostRField,
    LeafRightForeArmRoll3PreRField,
    LeafRightForeArmRoll3RField,
    LeafRightForeArmRoll3SField,
    LeafRightForeArmRoll3TField,
    LeafRightForeArmRoll4ISField,
    LeafRightForeArmRoll4PostRField,
    LeafRightForeArmRoll4PreRField,
    LeafRightForeArmRoll4RField,
    LeafRightForeArmRoll4SField,
    LeafRightForeArmRoll4TField,
    LeafRightForeArmRoll5ISField,
    LeafRightForeArmRoll5PostRField,
    LeafRightForeArmRoll5PreRField,
    LeafRightForeArmRoll5RField,
    LeafRightForeArmRoll5SField,
    LeafRightForeArmRoll5TField,
    LeafRightLegRoll1ISField,
    LeafRightLegRoll1PostRField,
    LeafRightLegRoll1PreRField,
    LeafRightLegRoll1RField,
    LeafRightLegRoll1SField,
    LeafRightLegRoll1TField,
    LeafRightLegRoll2ISField,
    LeafRightLegRoll2PostRField,
    LeafRightLegRoll2PreRField,
    LeafRightLegRoll2RField,
    LeafRightLegRoll2SField,
    LeafRightLegRoll2TField,
    LeafRightLegRoll3ISField,
    LeafRightLegRoll3PostRField,
    LeafRightLegRoll3PreRField,
    LeafRightLegRoll3RField,
    LeafRightLegRoll3SField,
    LeafRightLegRoll3TField,
    LeafRightLegRoll4ISField,
    LeafRightLegRoll4PostRField,
    LeafRightLegRoll4PreRField,
    LeafRightLegRoll4RField,
    LeafRightLegRoll4SField,
    LeafRightLegRoll4TField,
    LeafRightLegRoll5ISField,
    LeafRightLegRoll5PostRField,
    LeafRightLegRoll5PreRField,
    LeafRightLegRoll5RField,
    LeafRightLegRoll5SField,
    LeafRightLegRoll5TField,
    LeafRightUpLegRoll1ISField,
    LeafRightUpLegRoll1PostRField,
    LeafRightUpLegRoll1PreRField,
    LeafRightUpLegRoll1RField,
    LeafRightUpLegRoll1SField,
    LeafRightUpLegRoll1TField,
    LeafRightUpLegRoll2ISField,
    LeafRightUpLegRoll2PostRField,
    LeafRightUpLegRoll2PreRField,
    LeafRightUpLegRoll2RField,
    LeafRightUpLegRoll2SField,
    LeafRightUpLegRoll2TField,
    LeafRightUpLegRoll3ISField,
    LeafRightUpLegRoll3PostRField,
    LeafRightUpLegRoll3PreRField,
    LeafRightUpLegRoll3RField,
    LeafRightUpLegRoll3SField,
    LeafRightUpLegRoll3TField,
    LeafRightUpLegRoll4ISField,
    LeafRightUpLegRoll4PostRField,
    LeafRightUpLegRoll4PreRField,
    LeafRightUpLegRoll4RField,
    LeafRightUpLegRoll4SField,
    LeafRightUpLegRoll4TField,
    LeafRightUpLegRoll5ISField,
    LeafRightUpLegRoll5PostRField,
    LeafRightUpLegRoll5PreRField,
    LeafRightUpLegRoll5RField,
    LeafRightUpLegRoll5SField,
    LeafRightUpLegRoll5TField,
    LeftArmISField,
    LeftArmPostRField,
    LeftArmPreRField,
    LeftArmRField,
    LeftArmRollISField,
    LeftArmRollPostRField,
    LeftArmRollPreRField,
    LeftArmRollRField,
    LeftArmRollSField,
    LeftArmRollTField,
    LeftArmSField,
    LeftArmTField,
    LeftFingerBaseISField,
    LeftFingerBasePostRField,
    LeftFingerBasePreRField,
    LeftFingerBaseRField,
    LeftFingerBaseSField,
    LeftFingerBaseTField,
    LeftFootExtraFinger1ISField,
    LeftFootExtraFinger1PostRField,
    LeftFootExtraFinger1PreRField,
    LeftFootExtraFinger1RField,
    LeftFootExtraFinger1SField,
    LeftFootExtraFinger1TField,
    LeftFootExtraFinger2ISField,
    LeftFootExtraFinger2PostRField,
    LeftFootExtraFinger2PreRField,
    LeftFootExtraFinger2RField,
    LeftFootExtraFinger2SField,
    LeftFootExtraFinger2TField,
    LeftFootExtraFinger3ISField,
    LeftFootExtraFinger3PostRField,
    LeftFootExtraFinger3PreRField,
    LeftFootExtraFinger3RField,
    LeftFootExtraFinger3SField,
    LeftFootExtraFinger3TField,
    LeftFootExtraFinger4ISField,
    LeftFootExtraFinger4PostRField,
    LeftFootExtraFinger4PreRField,
    LeftFootExtraFinger4RField,
    LeftFootExtraFinger4SField,
    LeftFootExtraFinger4TField,
    LeftFootISField,
    LeftFootIndex1ISField,
    LeftFootIndex1PostRField,
    LeftFootIndex1PreRField,
    LeftFootIndex1RField,
    LeftFootIndex1SField,
    LeftFootIndex1TField,
    LeftFootIndex2ISField,
    LeftFootIndex2PostRField,
    LeftFootIndex2PreRField,
    LeftFootIndex2RField,
    LeftFootIndex2SField,
    LeftFootIndex2TField,
    LeftFootIndex3ISField,
    LeftFootIndex3PostRField,
    LeftFootIndex3PreRField,
    LeftFootIndex3RField,
    LeftFootIndex3SField,
    LeftFootIndex3TField,
    LeftFootIndex4ISField,
    LeftFootIndex4PostRField,
    LeftFootIndex4PreRField,
    LeftFootIndex4RField,
    LeftFootIndex4SField,
    LeftFootIndex4TField,
    LeftFootMiddle1ISField,
    LeftFootMiddle1PostRField,
    LeftFootMiddle1PreRField,
    LeftFootMiddle1RField,
    LeftFootMiddle1SField,
    LeftFootMiddle1TField,
    LeftFootMiddle2ISField,
    LeftFootMiddle2PostRField,
    LeftFootMiddle2PreRField,
    LeftFootMiddle2RField,
    LeftFootMiddle2SField,
    LeftFootMiddle2TField,
    LeftFootMiddle3ISField,
    LeftFootMiddle3PostRField,
    LeftFootMiddle3PreRField,
    LeftFootMiddle3RField,
    LeftFootMiddle3SField,
    LeftFootMiddle3TField,
    LeftFootMiddle4ISField,
    LeftFootMiddle4PostRField,
    LeftFootMiddle4PreRField,
    LeftFootMiddle4RField,
    LeftFootMiddle4SField,
    LeftFootMiddle4TField,
    LeftFootPinky1ISField,
    LeftFootPinky1PostRField,
    LeftFootPinky1PreRField,
    LeftFootPinky1RField,
    LeftFootPinky1SField,
    LeftFootPinky1TField,
    LeftFootPinky2ISField,
    LeftFootPinky2PostRField,
    LeftFootPinky2PreRField,
    LeftFootPinky2RField,
    LeftFootPinky2SField,
    LeftFootPinky2TField,
    LeftFootPinky3ISField,
    LeftFootPinky3PostRField,
    LeftFootPinky3PreRField,
    LeftFootPinky3RField,
    LeftFootPinky3SField,
    LeftFootPinky3TField,
    LeftFootPinky4ISField,
    LeftFootPinky4PostRField,
    LeftFootPinky4PreRField,
    LeftFootPinky4RField,
    LeftFootPinky4SField,
    LeftFootPinky4TField,
    LeftFootPostRField,
    LeftFootPreRField,
    LeftFootRField,
    LeftFootRing1ISField,
    LeftFootRing1PostRField,
    LeftFootRing1PreRField,
    LeftFootRing1RField,
    LeftFootRing1SField,
    LeftFootRing1TField,
    LeftFootRing2ISField,
    LeftFootRing2PostRField,
    LeftFootRing2PreRField,
    LeftFootRing2RField,
    LeftFootRing2SField,
    LeftFootRing2TField,
    LeftFootRing3ISField,
    LeftFootRing3PostRField,
    LeftFootRing3PreRField,
    LeftFootRing3RField,
    LeftFootRing3SField,
    LeftFootRing3TField,
    LeftFootRing4ISField,
    LeftFootRing4PostRField,
    LeftFootRing4PreRField,
    LeftFootRing4RField,
    LeftFootRing4SField,
    LeftFootRing4TField,
    LeftFootSField,
    LeftFootTField,
    LeftFootThumb1ISField,
    LeftFootThumb1PostRField,
    LeftFootThumb1PreRField,
    LeftFootThumb1RField,
    LeftFootThumb1SField,
    LeftFootThumb1TField,
    LeftFootThumb2ISField,
    LeftFootThumb2PostRField,
    LeftFootThumb2PreRField,
    LeftFootThumb2RField,
    LeftFootThumb2SField,
    LeftFootThumb2TField,
    LeftFootThumb3ISField,
    LeftFootThumb3PostRField,
    LeftFootThumb3PreRField,
    LeftFootThumb3RField,
    LeftFootThumb3SField,
    LeftFootThumb3TField,
    LeftFootThumb4ISField,
    LeftFootThumb4PostRField,
    LeftFootThumb4PreRField,
    LeftFootThumb4RField,
    LeftFootThumb4SField,
    LeftFootThumb4TField,
    LeftForeArmISField,
    LeftForeArmPostRField,
    LeftForeArmPreRField,
    LeftForeArmRField,
    LeftForeArmRollISField,
    LeftForeArmRollPostRField,
    LeftForeArmRollPreRField,
    LeftForeArmRollRField,
    LeftForeArmRollSField,
    LeftForeArmRollTField,
    LeftForeArmSField,
    LeftForeArmTField,
    LeftHandExtraFinger1ISField,
    LeftHandExtraFinger1PostRField,
    LeftHandExtraFinger1PreRField,
    LeftHandExtraFinger1RField,
    LeftHandExtraFinger1SField,
    LeftHandExtraFinger1TField,
    LeftHandExtraFinger2ISField,
    LeftHandExtraFinger2PostRField,
    LeftHandExtraFinger2PreRField,
    LeftHandExtraFinger2RField,
    LeftHandExtraFinger2SField,
    LeftHandExtraFinger2TField,
    LeftHandExtraFinger3ISField,
    LeftHandExtraFinger3PostRField,
    LeftHandExtraFinger3PreRField,
    LeftHandExtraFinger3RField,
    LeftHandExtraFinger3SField,
    LeftHandExtraFinger3TField,
    LeftHandExtraFinger4ISField,
    LeftHandExtraFinger4PostRField,
    LeftHandExtraFinger4PreRField,
    LeftHandExtraFinger4RField,
    LeftHandExtraFinger4SField,
    LeftHandExtraFinger4TField,
    LeftHandISField,
    LeftHandIndex1ISField,
    LeftHandIndex1PostRField,
    LeftHandIndex1PreRField,
    LeftHandIndex1RField,
    LeftHandIndex1SField,
    LeftHandIndex1TField,
    LeftHandIndex2ISField,
    LeftHandIndex2PostRField,
    LeftHandIndex2PreRField,
    LeftHandIndex2RField,
    LeftHandIndex2SField,
    LeftHandIndex2TField,
    LeftHandIndex3ISField,
    LeftHandIndex3PostRField,
    LeftHandIndex3PreRField,
    LeftHandIndex3RField,
    LeftHandIndex3SField,
    LeftHandIndex3TField,
    LeftHandIndex4ISField,
    LeftHandIndex4PostRField,
    LeftHandIndex4PreRField,
    LeftHandIndex4RField,
    LeftHandIndex4SField,
    LeftHandIndex4TField,
    LeftHandMiddle1ISField,
    LeftHandMiddle1PostRField,
    LeftHandMiddle1PreRField,
    LeftHandMiddle1RField,
    LeftHandMiddle1SField,
    LeftHandMiddle1TField,
    LeftHandMiddle2ISField,
    LeftHandMiddle2PostRField,
    LeftHandMiddle2PreRField,
    LeftHandMiddle2RField,
    LeftHandMiddle2SField,
    LeftHandMiddle2TField,
    LeftHandMiddle3ISField,
    LeftHandMiddle3PostRField,
    LeftHandMiddle3PreRField,
    LeftHandMiddle3RField,
    LeftHandMiddle3SField,
    LeftHandMiddle3TField,
    LeftHandMiddle4ISField,
    LeftHandMiddle4PostRField,
    LeftHandMiddle4PreRField,
    LeftHandMiddle4RField,
    LeftHandMiddle4SField,
    LeftHandMiddle4TField,
    LeftHandPinky1ISField,
    LeftHandPinky1PostRField,
    LeftHandPinky1PreRField,
    LeftHandPinky1RField,
    LeftHandPinky1SField,
    LeftHandPinky1TField,
    LeftHandPinky2ISField,
    LeftHandPinky2PostRField,
    LeftHandPinky2PreRField,
    LeftHandPinky2RField,
    LeftHandPinky2SField,
    LeftHandPinky2TField,
    LeftHandPinky3ISField,
    LeftHandPinky3PostRField,
    LeftHandPinky3PreRField,
    LeftHandPinky3RField,
    LeftHandPinky3SField,
    LeftHandPinky3TField,
    LeftHandPinky4ISField,
    LeftHandPinky4PostRField,
    LeftHandPinky4PreRField,
    LeftHandPinky4RField,
    LeftHandPinky4SField,
    LeftHandPinky4TField,
    LeftHandPostRField,
    LeftHandPreRField,
    LeftHandRField,
    LeftHandRing1ISField,
    LeftHandRing1PostRField,
    LeftHandRing1PreRField,
    LeftHandRing1RField,
    LeftHandRing1SField,
    LeftHandRing1TField,
    LeftHandRing2ISField,
    LeftHandRing2PostRField,
    LeftHandRing2PreRField,
    LeftHandRing2RField,
    LeftHandRing2SField,
    LeftHandRing2TField,
    LeftHandRing3ISField,
    LeftHandRing3PostRField,
    LeftHandRing3PreRField,
    LeftHandRing3RField,
    LeftHandRing3SField,
    LeftHandRing3TField,
    LeftHandRing4ISField,
    LeftHandRing4PostRField,
    LeftHandRing4PreRField,
    LeftHandRing4RField,
    LeftHandRing4SField,
    LeftHandRing4TField,
    LeftHandSField,
    LeftHandTField,
    LeftHandThumb1ISField,
    LeftHandThumb1PostRField,
    LeftHandThumb1PreRField,
    LeftHandThumb1RField,
    LeftHandThumb1SField,
    LeftHandThumb1TField,
    LeftHandThumb2ISField,
    LeftHandThumb2PostRField,
    LeftHandThumb2PreRField,
    LeftHandThumb2RField,
    LeftHandThumb2SField,
    LeftHandThumb2TField,
    LeftHandThumb3ISField,
    LeftHandThumb3PostRField,
    LeftHandThumb3PreRField,
    LeftHandThumb3RField,
    LeftHandThumb3SField,
    LeftHandThumb3TField,
    LeftHandThumb4ISField,
    LeftHandThumb4PostRField,
    LeftHandThumb4PreRField,
    LeftHandThumb4RField,
    LeftHandThumb4SField,
    LeftHandThumb4TField,
    LeftInFootExtraFingerISField,
    LeftInFootExtraFingerPostRField,
    LeftInFootExtraFingerPreRField,
    LeftInFootExtraFingerRField,
    LeftInFootExtraFingerSField,
    LeftInFootExtraFingerTField,
    LeftInFootIndexISField,
    LeftInFootIndexPostRField,
    LeftInFootIndexPreRField,
    LeftInFootIndexRField,
    LeftInFootIndexSField,
    LeftInFootIndexTField,
    LeftInFootMiddleISField,
    LeftInFootMiddlePostRField,
    LeftInFootMiddlePreRField,
    LeftInFootMiddleRField,
    LeftInFootMiddleSField,
    LeftInFootMiddleTField,
    LeftInFootPinkyISField,
    LeftInFootPinkyPostRField,
    LeftInFootPinkyPreRField,
    LeftInFootPinkyRField,
    LeftInFootPinkySField,
    LeftInFootPinkyTField,
    LeftInFootRingISField,
    LeftInFootRingPostRField,
    LeftInFootRingPreRField,
    LeftInFootRingRField,
    LeftInFootRingSField,
    LeftInFootRingTField,
    LeftInFootThumbISField,
    LeftInFootThumbPostRField,
    LeftInFootThumbPreRField,
    LeftInFootThumbRField,
    LeftInFootThumbSField,
    LeftInFootThumbTField,
    LeftInHandExtraFingerISField,
    LeftInHandExtraFingerPostRField,
    LeftInHandExtraFingerPreRField,
    LeftInHandExtraFingerRField,
    LeftInHandExtraFingerSField,
    LeftInHandExtraFingerTField,
    LeftInHandIndexISField,
    LeftInHandIndexPostRField,
    LeftInHandIndexPreRField,
    LeftInHandIndexRField,
    LeftInHandIndexSField,
    LeftInHandIndexTField,
    LeftInHandMiddleISField,
    LeftInHandMiddlePostRField,
    LeftInHandMiddlePreRField,
    LeftInHandMiddleRField,
    LeftInHandMiddleSField,
    LeftInHandMiddleTField,
    LeftInHandPinkyISField,
    LeftInHandPinkyPostRField,
    LeftInHandPinkyPreRField,
    LeftInHandPinkyRField,
    LeftInHandPinkySField,
    LeftInHandPinkyTField,
    LeftInHandRingISField,
    LeftInHandRingPostRField,
    LeftInHandRingPreRField,
    LeftInHandRingRField,
    LeftInHandRingSField,
    LeftInHandRingTField,
    LeftInHandThumbISField,
    LeftInHandThumbPostRField,
    LeftInHandThumbPreRField,
    LeftInHandThumbRField,
    LeftInHandThumbSField,
    LeftInHandThumbTField,
    LeftLegISField,
    LeftLegPostRField,
    LeftLegPreRField,
    LeftLegRField,
    LeftLegRollISField,
    LeftLegRollPostRField,
    LeftLegRollPreRField,
    LeftLegRollRField,
    LeftLegRollSField,
    LeftLegRollTField,
    LeftLegSField,
    LeftLegTField,
    LeftShoulderExtraISField,
    LeftShoulderExtraPostRField,
    LeftShoulderExtraPreRField,
    LeftShoulderExtraRField,
    LeftShoulderExtraSField,
    LeftShoulderExtraTField,
    LeftShoulderISField,
    LeftShoulderPostRField,
    LeftShoulderPreRField,
    LeftShoulderRField,
    LeftShoulderSField,
    LeftShoulderTField,
    LeftToeBaseISField,
    LeftToeBasePostRField,
    LeftToeBasePreRField,
    LeftToeBaseRField,
    LeftToeBaseSField,
    LeftToeBaseTField,
    LeftUpLegISField,
    LeftUpLegPostRField,
    LeftUpLegPreRField,
    LeftUpLegRField,
    LeftUpLegRollISField,
    LeftUpLegRollPostRField,
    LeftUpLegRollPreRField,
    LeftUpLegRollRField,
    LeftUpLegRollSField,
    LeftUpLegRollTField,
    LeftUpLegSField,
    LeftUpLegTField,
    Neck1ISField,
    Neck1PostRField,
    Neck1PreRField,
    Neck1RField,
    Neck1SField,
    Neck1TField,
    Neck2ISField,
    Neck2PostRField,
    Neck2PreRField,
    Neck2RField,
    Neck2SField,
    Neck2TField,
    Neck3ISField,
    Neck3PostRField,
    Neck3PreRField,
    Neck3RField,
    Neck3SField,
    Neck3TField,
    Neck4ISField,
    Neck4PostRField,
    Neck4PreRField,
    Neck4RField,
    Neck4SField,
    Neck4TField,
    Neck5ISField,
    Neck5PostRField,
    Neck5PreRField,
    Neck5RField,
    Neck5SField,
    Neck5TField,
    Neck6ISField,
    Neck6PostRField,
    Neck6PreRField,
    Neck6RField,
    Neck6SField,
    Neck6TField,
    Neck7ISField,
    Neck7PostRField,
    Neck7PreRField,
    Neck7RField,
    Neck7SField,
    Neck7TField,
    Neck8ISField,
    Neck8PostRField,
    Neck8PreRField,
    Neck8RField,
    Neck8SField,
    Neck8TField,
    Neck9ISField,
    Neck9PostRField,
    Neck9PreRField,
    Neck9RField,
    Neck9SField,
    Neck9TField,
    NeckISField,
    NeckPostRField,
    NeckPreRField,
    NeckRField,
    NeckSField,
    NeckTField,
    ReferenceISField,
    ReferencePostRField,
    ReferencePreRField,
    ReferenceRField,
    ReferenceSField,
    ReferenceTField,
    RightArmISField,
    RightArmPostRField,
    RightArmPreRField,
    RightArmRField,
    RightArmRollISField,
    RightArmRollPostRField,
    RightArmRollPreRField,
    RightArmRollRField,
    RightArmRollSField,
    RightArmRollTField,
    RightArmSField,
    RightArmTField,
    RightFingerBaseISField,
    RightFingerBasePostRField,
    RightFingerBasePreRField,
    RightFingerBaseRField,
    RightFingerBaseSField,
    RightFingerBaseTField,
    RightFootExtraFinger1ISField,
    RightFootExtraFinger1PostRField,
    RightFootExtraFinger1PreRField,
    RightFootExtraFinger1RField,
    RightFootExtraFinger1SField,
    RightFootExtraFinger1TField,
    RightFootExtraFinger2ISField,
    RightFootExtraFinger2PostRField,
    RightFootExtraFinger2PreRField,
    RightFootExtraFinger2RField,
    RightFootExtraFinger2SField,
    RightFootExtraFinger2TField,
    RightFootExtraFinger3ISField,
    RightFootExtraFinger3PostRField,
    RightFootExtraFinger3PreRField,
    RightFootExtraFinger3RField,
    RightFootExtraFinger3SField,
    RightFootExtraFinger3TField,
    RightFootExtraFinger4ISField,
    RightFootExtraFinger4PostRField,
    RightFootExtraFinger4PreRField,
    RightFootExtraFinger4RField,
    RightFootExtraFinger4SField,
    RightFootExtraFinger4TField,
    RightFootISField,
    RightFootIndex1ISField,
    RightFootIndex1PostRField,
    RightFootIndex1PreRField,
    RightFootIndex1RField,
    RightFootIndex1SField,
    RightFootIndex1TField,
    RightFootIndex2ISField,
    RightFootIndex2PostRField,
    RightFootIndex2PreRField,
    RightFootIndex2RField,
    RightFootIndex2SField,
    RightFootIndex2TField,
    RightFootIndex3ISField,
    RightFootIndex3PostRField,
    RightFootIndex3PreRField,
    RightFootIndex3RField,
    RightFootIndex3SField,
    RightFootIndex3TField,
    RightFootIndex4ISField,
    RightFootIndex4PostRField,
    RightFootIndex4PreRField,
    RightFootIndex4RField,
    RightFootIndex4SField,
    RightFootIndex4TField,
    RightFootMiddle1ISField,
    RightFootMiddle1PostRField,
    RightFootMiddle1PreRField,
    RightFootMiddle1RField,
    RightFootMiddle1SField,
    RightFootMiddle1TField,
    RightFootMiddle2ISField,
    RightFootMiddle2PostRField,
    RightFootMiddle2PreRField,
    RightFootMiddle2RField,
    RightFootMiddle2SField,
    RightFootMiddle2TField,
    RightFootMiddle3ISField,
    RightFootMiddle3PostRField,
    RightFootMiddle3PreRField,
    RightFootMiddle3RField,
    RightFootMiddle3SField,
    RightFootMiddle3TField,
    RightFootMiddle4ISField,
    RightFootMiddle4PostRField,
    RightFootMiddle4PreRField,
    RightFootMiddle4RField,
    RightFootMiddle4SField,
    RightFootMiddle4TField,
    RightFootPinky1ISField,
    RightFootPinky1PostRField,
    RightFootPinky1PreRField,
    RightFootPinky1RField,
    RightFootPinky1SField,
    RightFootPinky1TField,
    RightFootPinky2ISField,
    RightFootPinky2PostRField,
    RightFootPinky2PreRField,
    RightFootPinky2RField,
    RightFootPinky2SField,
    RightFootPinky2TField,
    RightFootPinky3ISField,
    RightFootPinky3PostRField,
    RightFootPinky3PreRField,
    RightFootPinky3RField,
    RightFootPinky3SField,
    RightFootPinky3TField,
    RightFootPinky4ISField,
    RightFootPinky4PostRField,
    RightFootPinky4PreRField,
    RightFootPinky4RField,
    RightFootPinky4SField,
    RightFootPinky4TField,
    RightFootPostRField,
    RightFootPreRField,
    RightFootRField,
    RightFootRing1ISField,
    RightFootRing1PostRField,
    RightFootRing1PreRField,
    RightFootRing1RField,
    RightFootRing1SField,
    RightFootRing1TField,
    RightFootRing2ISField,
    RightFootRing2PostRField,
    RightFootRing2PreRField,
    RightFootRing2RField,
    RightFootRing2SField,
    RightFootRing2TField,
    RightFootRing3ISField,
    RightFootRing3PostRField,
    RightFootRing3PreRField,
    RightFootRing3RField,
    RightFootRing3SField,
    RightFootRing3TField,
    RightFootRing4ISField,
    RightFootRing4PostRField,
    RightFootRing4PreRField,
    RightFootRing4RField,
    RightFootRing4SField,
    RightFootRing4TField,
    RightFootSField,
    RightFootTField,
    RightFootThumb1ISField,
    RightFootThumb1PostRField,
    RightFootThumb1PreRField,
    RightFootThumb1RField,
    RightFootThumb1SField,
    RightFootThumb1TField,
    RightFootThumb2ISField,
    RightFootThumb2PostRField,
    RightFootThumb2PreRField,
    RightFootThumb2RField,
    RightFootThumb2SField,
    RightFootThumb2TField,
    RightFootThumb3ISField,
    RightFootThumb3PostRField,
    RightFootThumb3PreRField,
    RightFootThumb3RField,
    RightFootThumb3SField,
    RightFootThumb3TField,
    RightFootThumb4ISField,
    RightFootThumb4PostRField,
    RightFootThumb4PreRField,
    RightFootThumb4RField,
    RightFootThumb4SField,
    RightFootThumb4TField,
    RightForeArmISField,
    RightForeArmPostRField,
    RightForeArmPreRField,
    RightForeArmRField,
    RightForeArmRollISField,
    RightForeArmRollPostRField,
    RightForeArmRollPreRField,
    RightForeArmRollRField,
    RightForeArmRollSField,
    RightForeArmRollTField,
    RightForeArmSField,
    RightForeArmTField,
    RightHandExtraFinger1ISField,
    RightHandExtraFinger1PostRField,
    RightHandExtraFinger1PreRField,
    RightHandExtraFinger1RField,
    RightHandExtraFinger1SField,
    RightHandExtraFinger1TField,
    RightHandExtraFinger2ISField,
    RightHandExtraFinger2PostRField,
    RightHandExtraFinger2PreRField,
    RightHandExtraFinger2RField,
    RightHandExtraFinger2SField,
    RightHandExtraFinger2TField,
    RightHandExtraFinger3ISField,
    RightHandExtraFinger3PostRField,
    RightHandExtraFinger3PreRField,
    RightHandExtraFinger3RField,
    RightHandExtraFinger3SField,
    RightHandExtraFinger3TField,
    RightHandExtraFinger4ISField,
    RightHandExtraFinger4PostRField,
    RightHandExtraFinger4PreRField,
    RightHandExtraFinger4RField,
    RightHandExtraFinger4SField,
    RightHandExtraFinger4TField,
    RightHandISField,
    RightHandIndex1ISField,
    RightHandIndex1PostRField,
    RightHandIndex1PreRField,
    RightHandIndex1RField,
    RightHandIndex1SField,
    RightHandIndex1TField,
    RightHandIndex2ISField,
    RightHandIndex2PostRField,
    RightHandIndex2PreRField,
    RightHandIndex2RField,
    RightHandIndex2SField,
    RightHandIndex2TField,
    RightHandIndex3ISField,
    RightHandIndex3PostRField,
    RightHandIndex3PreRField,
    RightHandIndex3RField,
    RightHandIndex3SField,
    RightHandIndex3TField,
    RightHandIndex4ISField,
    RightHandIndex4PostRField,
    RightHandIndex4PreRField,
    RightHandIndex4RField,
    RightHandIndex4SField,
    RightHandIndex4TField,
    RightHandMiddle1ISField,
    RightHandMiddle1PostRField,
    RightHandMiddle1PreRField,
    RightHandMiddle1RField,
    RightHandMiddle1SField,
    RightHandMiddle1TField,
    RightHandMiddle2ISField,
    RightHandMiddle2PostRField,
    RightHandMiddle2PreRField,
    RightHandMiddle2RField,
    RightHandMiddle2SField,
    RightHandMiddle2TField,
    RightHandMiddle3ISField,
    RightHandMiddle3PostRField,
    RightHandMiddle3PreRField,
    RightHandMiddle3RField,
    RightHandMiddle3SField,
    RightHandMiddle3TField,
    RightHandMiddle4ISField,
    RightHandMiddle4PostRField,
    RightHandMiddle4PreRField,
    RightHandMiddle4RField,
    RightHandMiddle4SField,
    RightHandMiddle4TField,
    RightHandPinky1ISField,
    RightHandPinky1PostRField,
    RightHandPinky1PreRField,
    RightHandPinky1RField,
    RightHandPinky1SField,
    RightHandPinky1TField,
    RightHandPinky2ISField,
    RightHandPinky2PostRField,
    RightHandPinky2PreRField,
    RightHandPinky2RField,
    RightHandPinky2SField,
    RightHandPinky2TField,
    RightHandPinky3ISField,
    RightHandPinky3PostRField,
    RightHandPinky3PreRField,
    RightHandPinky3RField,
    RightHandPinky3SField,
    RightHandPinky3TField,
    RightHandPinky4ISField,
    RightHandPinky4PostRField,
    RightHandPinky4PreRField,
    RightHandPinky4RField,
    RightHandPinky4SField,
    RightHandPinky4TField,
    RightHandPostRField,
    RightHandPreRField,
    RightHandRField,
    RightHandRing1ISField,
    RightHandRing1PostRField,
    RightHandRing1PreRField,
    RightHandRing1RField,
    RightHandRing1SField,
    RightHandRing1TField,
    RightHandRing2ISField,
    RightHandRing2PostRField,
    RightHandRing2PreRField,
    RightHandRing2RField,
    RightHandRing2SField,
    RightHandRing2TField,
    RightHandRing3ISField,
    RightHandRing3PostRField,
    RightHandRing3PreRField,
    RightHandRing3RField,
    RightHandRing3SField,
    RightHandRing3TField,
    RightHandRing4ISField,
    RightHandRing4PostRField,
    RightHandRing4PreRField,
    RightHandRing4RField,
    RightHandRing4SField,
    RightHandRing4TField,
    RightHandSField,
    RightHandTField,
    RightHandThumb1ISField,
    RightHandThumb1PostRField,
    RightHandThumb1PreRField,
    RightHandThumb1RField,
    RightHandThumb1SField,
    RightHandThumb1TField,
    RightHandThumb2ISField,
    RightHandThumb2PostRField,
    RightHandThumb2PreRField,
    RightHandThumb2RField,
    RightHandThumb2SField,
    RightHandThumb2TField,
    RightHandThumb3ISField,
    RightHandThumb3PostRField,
    RightHandThumb3PreRField,
    RightHandThumb3RField,
    RightHandThumb3SField,
    RightHandThumb3TField,
    RightHandThumb4ISField,
    RightHandThumb4PostRField,
    RightHandThumb4PreRField,
    RightHandThumb4RField,
    RightHandThumb4SField,
    RightHandThumb4TField,
    RightInFootExtraFingerISField,
    RightInFootExtraFingerPostRField,
    RightInFootExtraFingerPreRField,
    RightInFootExtraFingerRField,
    RightInFootExtraFingerSField,
    RightInFootExtraFingerTField,
    RightInFootIndexISField,
    RightInFootIndexPostRField,
    RightInFootIndexPreRField,
    RightInFootIndexRField,
    RightInFootIndexSField,
    RightInFootIndexTField,
    RightInFootMiddleISField,
    RightInFootMiddlePostRField,
    RightInFootMiddlePreRField,
    RightInFootMiddleRField,
    RightInFootMiddleSField,
    RightInFootMiddleTField,
    RightInFootPinkyISField,
    RightInFootPinkyPostRField,
    RightInFootPinkyPreRField,
    RightInFootPinkyRField,
    RightInFootPinkySField,
    RightInFootPinkyTField,
    RightInFootRingISField,
    RightInFootRingPostRField,
    RightInFootRingPreRField,
    RightInFootRingRField,
    RightInFootRingSField,
    RightInFootRingTField,
    RightInFootThumbISField,
    RightInFootThumbPostRField,
    RightInFootThumbPreRField,
    RightInFootThumbRField,
    RightInFootThumbSField,
    RightInFootThumbTField,
    RightInHandExtraFingerISField,
    RightInHandExtraFingerPostRField,
    RightInHandExtraFingerPreRField,
    RightInHandExtraFingerRField,
    RightInHandExtraFingerSField,
    RightInHandExtraFingerTField,
    RightInHandIndexISField,
    RightInHandIndexPostRField,
    RightInHandIndexPreRField,
    RightInHandIndexRField,
    RightInHandIndexSField,
    RightInHandIndexTField,
    RightInHandMiddleISField,
    RightInHandMiddlePostRField,
    RightInHandMiddlePreRField,
    RightInHandMiddleRField,
    RightInHandMiddleSField,
    RightInHandMiddleTField,
    RightInHandPinkyISField,
    RightInHandPinkyPostRField,
    RightInHandPinkyPreRField,
    RightInHandPinkyRField,
    RightInHandPinkySField,
    RightInHandPinkyTField,
    RightInHandRingISField,
    RightInHandRingPostRField,
    RightInHandRingPreRField,
    RightInHandRingRField,
    RightInHandRingSField,
    RightInHandRingTField,
    RightInHandThumbISField,
    RightInHandThumbPostRField,
    RightInHandThumbPreRField,
    RightInHandThumbRField,
    RightInHandThumbSField,
    RightInHandThumbTField,
    RightLegISField,
    RightLegPostRField,
    RightLegPreRField,
    RightLegRField,
    RightLegRollISField,
    RightLegRollPostRField,
    RightLegRollPreRField,
    RightLegRollRField,
    RightLegRollSField,
    RightLegRollTField,
    RightLegSField,
    RightLegTField,
    RightShoulderExtraISField,
    RightShoulderExtraPostRField,
    RightShoulderExtraPreRField,
    RightShoulderExtraRField,
    RightShoulderExtraSField,
    RightShoulderExtraTField,
    RightShoulderISField,
    RightShoulderPostRField,
    RightShoulderPreRField,
    RightShoulderRField,
    RightShoulderSField,
    RightShoulderTField,
    RightToeBaseISField,
    RightToeBasePostRField,
    RightToeBasePreRField,
    RightToeBaseRField,
    RightToeBaseSField,
    RightToeBaseTField,
    RightUpLegISField,
    RightUpLegPostRField,
    RightUpLegPreRField,
    RightUpLegRField,
    RightUpLegRollISField,
    RightUpLegRollPostRField,
    RightUpLegRollPreRField,
    RightUpLegRollRField,
    RightUpLegRollSField,
    RightUpLegRollTField,
    RightUpLegSField,
    RightUpLegTField,
    Spine1ISField,
    Spine1PostRField,
    Spine1PreRField,
    Spine1RField,
    Spine1SField,
    Spine1TField,
    Spine2ISField,
    Spine2PostRField,
    Spine2PreRField,
    Spine2RField,
    Spine2SField,
    Spine2TField,
    Spine3ISField,
    Spine3PostRField,
    Spine3PreRField,
    Spine3RField,
    Spine3SField,
    Spine3TField,
    Spine4ISField,
    Spine4PostRField,
    Spine4PreRField,
    Spine4RField,
    Spine4SField,
    Spine4TField,
    Spine5ISField,
    Spine5PostRField,
    Spine5PreRField,
    Spine5RField,
    Spine5SField,
    Spine5TField,
    Spine6ISField,
    Spine6PostRField,
    Spine6PreRField,
    Spine6RField,
    Spine6SField,
    Spine6TField,
    Spine7ISField,
    Spine7PostRField,
    Spine7PreRField,
    Spine7RField,
    Spine7SField,
    Spine7TField,
    Spine8ISField,
    Spine8PostRField,
    Spine8PreRField,
    Spine8RField,
    Spine8SField,
    Spine8TField,
    Spine9ISField,
    Spine9PostRField,
    Spine9PreRField,
    Spine9RField,
    Spine9SField,
    Spine9TField,
    SpineISField,
    SpinePostRField,
    SpinePreRField,
    SpineRField,
    SpineSField,
    SpineTField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.typed import TypedField


class ReferenceROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class ReferenceROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class ReferenceROrderEnumField(
    EnumField[ReferenceROrderEnumAttrOperator, ReferenceROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReferenceROrderEnumAttrOperator
    PLUG_CLS = ReferenceROrderEnumPlugOperator


class HipsROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class HipsROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class HipsROrderEnumField(
    EnumField[HipsROrderEnumAttrOperator, HipsROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsROrderEnumAttrOperator
    PLUG_CLS = HipsROrderEnumPlugOperator


class LeftUpLegROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftUpLegROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftUpLegROrderEnumField(
    EnumField[LeftUpLegROrderEnumAttrOperator, LeftUpLegROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegROrderEnumAttrOperator
    PLUG_CLS = LeftUpLegROrderEnumPlugOperator


class LeftLegROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftLegROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftLegROrderEnumField(
    EnumField[LeftLegROrderEnumAttrOperator, LeftLegROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegROrderEnumAttrOperator
    PLUG_CLS = LeftLegROrderEnumPlugOperator


class LeftFootROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootROrderEnumField(
    EnumField[LeftFootROrderEnumAttrOperator, LeftFootROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootROrderEnumAttrOperator
    PLUG_CLS = LeftFootROrderEnumPlugOperator


class RightUpLegROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightUpLegROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightUpLegROrderEnumField(
    EnumField[RightUpLegROrderEnumAttrOperator, RightUpLegROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegROrderEnumAttrOperator
    PLUG_CLS = RightUpLegROrderEnumPlugOperator


class RightLegROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightLegROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightLegROrderEnumField(
    EnumField[RightLegROrderEnumAttrOperator, RightLegROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegROrderEnumAttrOperator
    PLUG_CLS = RightLegROrderEnumPlugOperator


class RightFootROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootROrderEnumField(
    EnumField[RightFootROrderEnumAttrOperator, RightFootROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootROrderEnumAttrOperator
    PLUG_CLS = RightFootROrderEnumPlugOperator


class SpineROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class SpineROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class SpineROrderEnumField(
    EnumField[SpineROrderEnumAttrOperator, SpineROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpineROrderEnumAttrOperator
    PLUG_CLS = SpineROrderEnumPlugOperator


class LeftArmROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftArmROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftArmROrderEnumField(
    EnumField[LeftArmROrderEnumAttrOperator, LeftArmROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmROrderEnumAttrOperator
    PLUG_CLS = LeftArmROrderEnumPlugOperator


class LeftForeArmROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftForeArmROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftForeArmROrderEnumField(
    EnumField[LeftForeArmROrderEnumAttrOperator, LeftForeArmROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmROrderEnumAttrOperator
    PLUG_CLS = LeftForeArmROrderEnumPlugOperator


class LeftHandROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandROrderEnumField(
    EnumField[LeftHandROrderEnumAttrOperator, LeftHandROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandROrderEnumAttrOperator
    PLUG_CLS = LeftHandROrderEnumPlugOperator


class RightArmROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightArmROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightArmROrderEnumField(
    EnumField[RightArmROrderEnumAttrOperator, RightArmROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmROrderEnumAttrOperator
    PLUG_CLS = RightArmROrderEnumPlugOperator


class RightForeArmROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightForeArmROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightForeArmROrderEnumField(
    EnumField[RightForeArmROrderEnumAttrOperator, RightForeArmROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmROrderEnumAttrOperator
    PLUG_CLS = RightForeArmROrderEnumPlugOperator


class RightHandROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandROrderEnumField(
    EnumField[RightHandROrderEnumAttrOperator, RightHandROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandROrderEnumAttrOperator
    PLUG_CLS = RightHandROrderEnumPlugOperator


class HeadROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class HeadROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class HeadROrderEnumField(
    EnumField[HeadROrderEnumAttrOperator, HeadROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HeadROrderEnumAttrOperator
    PLUG_CLS = HeadROrderEnumPlugOperator


class LeftToeBaseROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftToeBaseROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftToeBaseROrderEnumField(
    EnumField[LeftToeBaseROrderEnumAttrOperator, LeftToeBaseROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftToeBaseROrderEnumAttrOperator
    PLUG_CLS = LeftToeBaseROrderEnumPlugOperator


class RightToeBaseROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightToeBaseROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightToeBaseROrderEnumField(
    EnumField[RightToeBaseROrderEnumAttrOperator, RightToeBaseROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightToeBaseROrderEnumAttrOperator
    PLUG_CLS = RightToeBaseROrderEnumPlugOperator


class LeftShoulderROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftShoulderROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftShoulderROrderEnumField(
    EnumField[LeftShoulderROrderEnumAttrOperator, LeftShoulderROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderROrderEnumAttrOperator
    PLUG_CLS = LeftShoulderROrderEnumPlugOperator


class RightShoulderROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightShoulderROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightShoulderROrderEnumField(
    EnumField[RightShoulderROrderEnumAttrOperator, RightShoulderROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderROrderEnumAttrOperator
    PLUG_CLS = RightShoulderROrderEnumPlugOperator


class NeckROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class NeckROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class NeckROrderEnumField(
    EnumField[NeckROrderEnumAttrOperator, NeckROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NeckROrderEnumAttrOperator
    PLUG_CLS = NeckROrderEnumPlugOperator


class LeftFingerBaseROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFingerBaseROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFingerBaseROrderEnumField(
    EnumField[LeftFingerBaseROrderEnumAttrOperator, LeftFingerBaseROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFingerBaseROrderEnumAttrOperator
    PLUG_CLS = LeftFingerBaseROrderEnumPlugOperator


class RightFingerBaseROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFingerBaseROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFingerBaseROrderEnumField(
    EnumField[RightFingerBaseROrderEnumAttrOperator, RightFingerBaseROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFingerBaseROrderEnumAttrOperator
    PLUG_CLS = RightFingerBaseROrderEnumPlugOperator


class Spine1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Spine1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Spine1ROrderEnumField(
    EnumField[Spine1ROrderEnumAttrOperator, Spine1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine1ROrderEnumAttrOperator
    PLUG_CLS = Spine1ROrderEnumPlugOperator


class Spine2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Spine2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Spine2ROrderEnumField(
    EnumField[Spine2ROrderEnumAttrOperator, Spine2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine2ROrderEnumAttrOperator
    PLUG_CLS = Spine2ROrderEnumPlugOperator


class Spine3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Spine3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Spine3ROrderEnumField(
    EnumField[Spine3ROrderEnumAttrOperator, Spine3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine3ROrderEnumAttrOperator
    PLUG_CLS = Spine3ROrderEnumPlugOperator


class Spine4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Spine4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Spine4ROrderEnumField(
    EnumField[Spine4ROrderEnumAttrOperator, Spine4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine4ROrderEnumAttrOperator
    PLUG_CLS = Spine4ROrderEnumPlugOperator


class Spine5ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Spine5ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Spine5ROrderEnumField(
    EnumField[Spine5ROrderEnumAttrOperator, Spine5ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine5ROrderEnumAttrOperator
    PLUG_CLS = Spine5ROrderEnumPlugOperator


class Spine6ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Spine6ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Spine6ROrderEnumField(
    EnumField[Spine6ROrderEnumAttrOperator, Spine6ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine6ROrderEnumAttrOperator
    PLUG_CLS = Spine6ROrderEnumPlugOperator


class Spine7ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Spine7ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Spine7ROrderEnumField(
    EnumField[Spine7ROrderEnumAttrOperator, Spine7ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine7ROrderEnumAttrOperator
    PLUG_CLS = Spine7ROrderEnumPlugOperator


class Spine8ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Spine8ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Spine8ROrderEnumField(
    EnumField[Spine8ROrderEnumAttrOperator, Spine8ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine8ROrderEnumAttrOperator
    PLUG_CLS = Spine8ROrderEnumPlugOperator


class Spine9ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Spine9ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Spine9ROrderEnumField(
    EnumField[Spine9ROrderEnumAttrOperator, Spine9ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine9ROrderEnumAttrOperator
    PLUG_CLS = Spine9ROrderEnumPlugOperator


class Neck1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Neck1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Neck1ROrderEnumField(
    EnumField[Neck1ROrderEnumAttrOperator, Neck1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck1ROrderEnumAttrOperator
    PLUG_CLS = Neck1ROrderEnumPlugOperator


class Neck2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Neck2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Neck2ROrderEnumField(
    EnumField[Neck2ROrderEnumAttrOperator, Neck2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck2ROrderEnumAttrOperator
    PLUG_CLS = Neck2ROrderEnumPlugOperator


class Neck3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Neck3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Neck3ROrderEnumField(
    EnumField[Neck3ROrderEnumAttrOperator, Neck3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck3ROrderEnumAttrOperator
    PLUG_CLS = Neck3ROrderEnumPlugOperator


class Neck4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Neck4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Neck4ROrderEnumField(
    EnumField[Neck4ROrderEnumAttrOperator, Neck4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck4ROrderEnumAttrOperator
    PLUG_CLS = Neck4ROrderEnumPlugOperator


class Neck5ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Neck5ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Neck5ROrderEnumField(
    EnumField[Neck5ROrderEnumAttrOperator, Neck5ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck5ROrderEnumAttrOperator
    PLUG_CLS = Neck5ROrderEnumPlugOperator


class Neck6ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Neck6ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Neck6ROrderEnumField(
    EnumField[Neck6ROrderEnumAttrOperator, Neck6ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck6ROrderEnumAttrOperator
    PLUG_CLS = Neck6ROrderEnumPlugOperator


class Neck7ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Neck7ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Neck7ROrderEnumField(
    EnumField[Neck7ROrderEnumAttrOperator, Neck7ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck7ROrderEnumAttrOperator
    PLUG_CLS = Neck7ROrderEnumPlugOperator


class Neck8ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Neck8ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Neck8ROrderEnumField(
    EnumField[Neck8ROrderEnumAttrOperator, Neck8ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck8ROrderEnumAttrOperator
    PLUG_CLS = Neck8ROrderEnumPlugOperator


class Neck9ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Neck9ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class Neck9ROrderEnumField(
    EnumField[Neck9ROrderEnumAttrOperator, Neck9ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck9ROrderEnumAttrOperator
    PLUG_CLS = Neck9ROrderEnumPlugOperator


class LeftUpLegRollROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftUpLegRollROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftUpLegRollROrderEnumField(
    EnumField[LeftUpLegRollROrderEnumAttrOperator, LeftUpLegRollROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegRollROrderEnumAttrOperator
    PLUG_CLS = LeftUpLegRollROrderEnumPlugOperator


class LeftLegRollROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftLegRollROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftLegRollROrderEnumField(
    EnumField[LeftLegRollROrderEnumAttrOperator, LeftLegRollROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegRollROrderEnumAttrOperator
    PLUG_CLS = LeftLegRollROrderEnumPlugOperator


class RightUpLegRollROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightUpLegRollROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightUpLegRollROrderEnumField(
    EnumField[RightUpLegRollROrderEnumAttrOperator, RightUpLegRollROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegRollROrderEnumAttrOperator
    PLUG_CLS = RightUpLegRollROrderEnumPlugOperator


class RightLegRollROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightLegRollROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightLegRollROrderEnumField(
    EnumField[RightLegRollROrderEnumAttrOperator, RightLegRollROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegRollROrderEnumAttrOperator
    PLUG_CLS = RightLegRollROrderEnumPlugOperator


class LeftArmRollROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftArmRollROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftArmRollROrderEnumField(
    EnumField[LeftArmRollROrderEnumAttrOperator, LeftArmRollROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmRollROrderEnumAttrOperator
    PLUG_CLS = LeftArmRollROrderEnumPlugOperator


class LeftForeArmRollROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftForeArmRollROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftForeArmRollROrderEnumField(
    EnumField[LeftForeArmRollROrderEnumAttrOperator, LeftForeArmRollROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmRollROrderEnumAttrOperator
    PLUG_CLS = LeftForeArmRollROrderEnumPlugOperator


class RightArmRollROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightArmRollROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightArmRollROrderEnumField(
    EnumField[RightArmRollROrderEnumAttrOperator, RightArmRollROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmRollROrderEnumAttrOperator
    PLUG_CLS = RightArmRollROrderEnumPlugOperator


class RightForeArmRollROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightForeArmRollROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightForeArmRollROrderEnumField(
    EnumField[RightForeArmRollROrderEnumAttrOperator, RightForeArmRollROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmRollROrderEnumAttrOperator
    PLUG_CLS = RightForeArmRollROrderEnumPlugOperator


class HipsTranslationROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class HipsTranslationROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class HipsTranslationROrderEnumField(
    EnumField[HipsTranslationROrderEnumAttrOperator, HipsTranslationROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsTranslationROrderEnumAttrOperator
    PLUG_CLS = HipsTranslationROrderEnumPlugOperator


class LeftHandThumb1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandThumb1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandThumb1ROrderEnumField(
    EnumField[LeftHandThumb1ROrderEnumAttrOperator, LeftHandThumb1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb1ROrderEnumAttrOperator
    PLUG_CLS = LeftHandThumb1ROrderEnumPlugOperator


class LeftHandThumb2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandThumb2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandThumb2ROrderEnumField(
    EnumField[LeftHandThumb2ROrderEnumAttrOperator, LeftHandThumb2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb2ROrderEnumAttrOperator
    PLUG_CLS = LeftHandThumb2ROrderEnumPlugOperator


class LeftHandThumb3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandThumb3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandThumb3ROrderEnumField(
    EnumField[LeftHandThumb3ROrderEnumAttrOperator, LeftHandThumb3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb3ROrderEnumAttrOperator
    PLUG_CLS = LeftHandThumb3ROrderEnumPlugOperator


class LeftHandThumb4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandThumb4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandThumb4ROrderEnumField(
    EnumField[LeftHandThumb4ROrderEnumAttrOperator, LeftHandThumb4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb4ROrderEnumAttrOperator
    PLUG_CLS = LeftHandThumb4ROrderEnumPlugOperator


class LeftHandIndex1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandIndex1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandIndex1ROrderEnumField(
    EnumField[LeftHandIndex1ROrderEnumAttrOperator, LeftHandIndex1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex1ROrderEnumAttrOperator
    PLUG_CLS = LeftHandIndex1ROrderEnumPlugOperator


class LeftHandIndex2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandIndex2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandIndex2ROrderEnumField(
    EnumField[LeftHandIndex2ROrderEnumAttrOperator, LeftHandIndex2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex2ROrderEnumAttrOperator
    PLUG_CLS = LeftHandIndex2ROrderEnumPlugOperator


class LeftHandIndex3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandIndex3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandIndex3ROrderEnumField(
    EnumField[LeftHandIndex3ROrderEnumAttrOperator, LeftHandIndex3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex3ROrderEnumAttrOperator
    PLUG_CLS = LeftHandIndex3ROrderEnumPlugOperator


class LeftHandIndex4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandIndex4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandIndex4ROrderEnumField(
    EnumField[LeftHandIndex4ROrderEnumAttrOperator, LeftHandIndex4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex4ROrderEnumAttrOperator
    PLUG_CLS = LeftHandIndex4ROrderEnumPlugOperator


class LeftHandMiddle1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandMiddle1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandMiddle1ROrderEnumField(
    EnumField[LeftHandMiddle1ROrderEnumAttrOperator, LeftHandMiddle1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle1ROrderEnumAttrOperator
    PLUG_CLS = LeftHandMiddle1ROrderEnumPlugOperator


class LeftHandMiddle2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandMiddle2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandMiddle2ROrderEnumField(
    EnumField[LeftHandMiddle2ROrderEnumAttrOperator, LeftHandMiddle2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle2ROrderEnumAttrOperator
    PLUG_CLS = LeftHandMiddle2ROrderEnumPlugOperator


class LeftHandMiddle3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandMiddle3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandMiddle3ROrderEnumField(
    EnumField[LeftHandMiddle3ROrderEnumAttrOperator, LeftHandMiddle3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle3ROrderEnumAttrOperator
    PLUG_CLS = LeftHandMiddle3ROrderEnumPlugOperator


class LeftHandMiddle4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandMiddle4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandMiddle4ROrderEnumField(
    EnumField[LeftHandMiddle4ROrderEnumAttrOperator, LeftHandMiddle4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle4ROrderEnumAttrOperator
    PLUG_CLS = LeftHandMiddle4ROrderEnumPlugOperator


class LeftHandRing1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandRing1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandRing1ROrderEnumField(
    EnumField[LeftHandRing1ROrderEnumAttrOperator, LeftHandRing1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing1ROrderEnumAttrOperator
    PLUG_CLS = LeftHandRing1ROrderEnumPlugOperator


class LeftHandRing2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandRing2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandRing2ROrderEnumField(
    EnumField[LeftHandRing2ROrderEnumAttrOperator, LeftHandRing2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing2ROrderEnumAttrOperator
    PLUG_CLS = LeftHandRing2ROrderEnumPlugOperator


class LeftHandRing3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandRing3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandRing3ROrderEnumField(
    EnumField[LeftHandRing3ROrderEnumAttrOperator, LeftHandRing3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing3ROrderEnumAttrOperator
    PLUG_CLS = LeftHandRing3ROrderEnumPlugOperator


class LeftHandRing4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandRing4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandRing4ROrderEnumField(
    EnumField[LeftHandRing4ROrderEnumAttrOperator, LeftHandRing4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing4ROrderEnumAttrOperator
    PLUG_CLS = LeftHandRing4ROrderEnumPlugOperator


class LeftHandPinky1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandPinky1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandPinky1ROrderEnumField(
    EnumField[LeftHandPinky1ROrderEnumAttrOperator, LeftHandPinky1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky1ROrderEnumAttrOperator
    PLUG_CLS = LeftHandPinky1ROrderEnumPlugOperator


class LeftHandPinky2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandPinky2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandPinky2ROrderEnumField(
    EnumField[LeftHandPinky2ROrderEnumAttrOperator, LeftHandPinky2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky2ROrderEnumAttrOperator
    PLUG_CLS = LeftHandPinky2ROrderEnumPlugOperator


class LeftHandPinky3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandPinky3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandPinky3ROrderEnumField(
    EnumField[LeftHandPinky3ROrderEnumAttrOperator, LeftHandPinky3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky3ROrderEnumAttrOperator
    PLUG_CLS = LeftHandPinky3ROrderEnumPlugOperator


class LeftHandPinky4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandPinky4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandPinky4ROrderEnumField(
    EnumField[LeftHandPinky4ROrderEnumAttrOperator, LeftHandPinky4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky4ROrderEnumAttrOperator
    PLUG_CLS = LeftHandPinky4ROrderEnumPlugOperator


class LeftHandExtraFinger1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandExtraFinger1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandExtraFinger1ROrderEnumField(
    EnumField[LeftHandExtraFinger1ROrderEnumAttrOperator, LeftHandExtraFinger1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger1ROrderEnumAttrOperator
    PLUG_CLS = LeftHandExtraFinger1ROrderEnumPlugOperator


class LeftHandExtraFinger2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandExtraFinger2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandExtraFinger2ROrderEnumField(
    EnumField[LeftHandExtraFinger2ROrderEnumAttrOperator, LeftHandExtraFinger2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger2ROrderEnumAttrOperator
    PLUG_CLS = LeftHandExtraFinger2ROrderEnumPlugOperator


class LeftHandExtraFinger3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandExtraFinger3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandExtraFinger3ROrderEnumField(
    EnumField[LeftHandExtraFinger3ROrderEnumAttrOperator, LeftHandExtraFinger3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger3ROrderEnumAttrOperator
    PLUG_CLS = LeftHandExtraFinger3ROrderEnumPlugOperator


class LeftHandExtraFinger4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftHandExtraFinger4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftHandExtraFinger4ROrderEnumField(
    EnumField[LeftHandExtraFinger4ROrderEnumAttrOperator, LeftHandExtraFinger4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger4ROrderEnumAttrOperator
    PLUG_CLS = LeftHandExtraFinger4ROrderEnumPlugOperator


class RightHandThumb1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandThumb1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandThumb1ROrderEnumField(
    EnumField[RightHandThumb1ROrderEnumAttrOperator, RightHandThumb1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb1ROrderEnumAttrOperator
    PLUG_CLS = RightHandThumb1ROrderEnumPlugOperator


class RightHandThumb2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandThumb2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandThumb2ROrderEnumField(
    EnumField[RightHandThumb2ROrderEnumAttrOperator, RightHandThumb2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb2ROrderEnumAttrOperator
    PLUG_CLS = RightHandThumb2ROrderEnumPlugOperator


class RightHandThumb3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandThumb3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandThumb3ROrderEnumField(
    EnumField[RightHandThumb3ROrderEnumAttrOperator, RightHandThumb3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb3ROrderEnumAttrOperator
    PLUG_CLS = RightHandThumb3ROrderEnumPlugOperator


class RightHandThumb4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandThumb4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandThumb4ROrderEnumField(
    EnumField[RightHandThumb4ROrderEnumAttrOperator, RightHandThumb4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb4ROrderEnumAttrOperator
    PLUG_CLS = RightHandThumb4ROrderEnumPlugOperator


class RightHandIndex1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandIndex1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandIndex1ROrderEnumField(
    EnumField[RightHandIndex1ROrderEnumAttrOperator, RightHandIndex1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex1ROrderEnumAttrOperator
    PLUG_CLS = RightHandIndex1ROrderEnumPlugOperator


class RightHandIndex2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandIndex2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandIndex2ROrderEnumField(
    EnumField[RightHandIndex2ROrderEnumAttrOperator, RightHandIndex2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex2ROrderEnumAttrOperator
    PLUG_CLS = RightHandIndex2ROrderEnumPlugOperator


class RightHandIndex3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandIndex3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandIndex3ROrderEnumField(
    EnumField[RightHandIndex3ROrderEnumAttrOperator, RightHandIndex3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex3ROrderEnumAttrOperator
    PLUG_CLS = RightHandIndex3ROrderEnumPlugOperator


class RightHandIndex4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandIndex4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandIndex4ROrderEnumField(
    EnumField[RightHandIndex4ROrderEnumAttrOperator, RightHandIndex4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex4ROrderEnumAttrOperator
    PLUG_CLS = RightHandIndex4ROrderEnumPlugOperator


class RightHandMiddle1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandMiddle1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandMiddle1ROrderEnumField(
    EnumField[RightHandMiddle1ROrderEnumAttrOperator, RightHandMiddle1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle1ROrderEnumAttrOperator
    PLUG_CLS = RightHandMiddle1ROrderEnumPlugOperator


class RightHandMiddle2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandMiddle2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandMiddle2ROrderEnumField(
    EnumField[RightHandMiddle2ROrderEnumAttrOperator, RightHandMiddle2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle2ROrderEnumAttrOperator
    PLUG_CLS = RightHandMiddle2ROrderEnumPlugOperator


class RightHandMiddle3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandMiddle3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandMiddle3ROrderEnumField(
    EnumField[RightHandMiddle3ROrderEnumAttrOperator, RightHandMiddle3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle3ROrderEnumAttrOperator
    PLUG_CLS = RightHandMiddle3ROrderEnumPlugOperator


class RightHandMiddle4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandMiddle4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandMiddle4ROrderEnumField(
    EnumField[RightHandMiddle4ROrderEnumAttrOperator, RightHandMiddle4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle4ROrderEnumAttrOperator
    PLUG_CLS = RightHandMiddle4ROrderEnumPlugOperator


class RightHandRing1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandRing1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandRing1ROrderEnumField(
    EnumField[RightHandRing1ROrderEnumAttrOperator, RightHandRing1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing1ROrderEnumAttrOperator
    PLUG_CLS = RightHandRing1ROrderEnumPlugOperator


class RightHandRing2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandRing2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandRing2ROrderEnumField(
    EnumField[RightHandRing2ROrderEnumAttrOperator, RightHandRing2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing2ROrderEnumAttrOperator
    PLUG_CLS = RightHandRing2ROrderEnumPlugOperator


class RightHandRing3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandRing3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandRing3ROrderEnumField(
    EnumField[RightHandRing3ROrderEnumAttrOperator, RightHandRing3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing3ROrderEnumAttrOperator
    PLUG_CLS = RightHandRing3ROrderEnumPlugOperator


class RightHandRing4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandRing4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandRing4ROrderEnumField(
    EnumField[RightHandRing4ROrderEnumAttrOperator, RightHandRing4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing4ROrderEnumAttrOperator
    PLUG_CLS = RightHandRing4ROrderEnumPlugOperator


class RightHandPinky1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandPinky1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandPinky1ROrderEnumField(
    EnumField[RightHandPinky1ROrderEnumAttrOperator, RightHandPinky1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky1ROrderEnumAttrOperator
    PLUG_CLS = RightHandPinky1ROrderEnumPlugOperator


class RightHandPinky2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandPinky2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandPinky2ROrderEnumField(
    EnumField[RightHandPinky2ROrderEnumAttrOperator, RightHandPinky2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky2ROrderEnumAttrOperator
    PLUG_CLS = RightHandPinky2ROrderEnumPlugOperator


class RightHandPinky3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandPinky3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandPinky3ROrderEnumField(
    EnumField[RightHandPinky3ROrderEnumAttrOperator, RightHandPinky3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky3ROrderEnumAttrOperator
    PLUG_CLS = RightHandPinky3ROrderEnumPlugOperator


class RightHandPinky4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandPinky4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandPinky4ROrderEnumField(
    EnumField[RightHandPinky4ROrderEnumAttrOperator, RightHandPinky4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky4ROrderEnumAttrOperator
    PLUG_CLS = RightHandPinky4ROrderEnumPlugOperator


class RightHandExtraFinger1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandExtraFinger1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandExtraFinger1ROrderEnumField(
    EnumField[RightHandExtraFinger1ROrderEnumAttrOperator, RightHandExtraFinger1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger1ROrderEnumAttrOperator
    PLUG_CLS = RightHandExtraFinger1ROrderEnumPlugOperator


class RightHandExtraFinger2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandExtraFinger2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandExtraFinger2ROrderEnumField(
    EnumField[RightHandExtraFinger2ROrderEnumAttrOperator, RightHandExtraFinger2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger2ROrderEnumAttrOperator
    PLUG_CLS = RightHandExtraFinger2ROrderEnumPlugOperator


class RightHandExtraFinger3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandExtraFinger3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandExtraFinger3ROrderEnumField(
    EnumField[RightHandExtraFinger3ROrderEnumAttrOperator, RightHandExtraFinger3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger3ROrderEnumAttrOperator
    PLUG_CLS = RightHandExtraFinger3ROrderEnumPlugOperator


class RightHandExtraFinger4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightHandExtraFinger4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightHandExtraFinger4ROrderEnumField(
    EnumField[RightHandExtraFinger4ROrderEnumAttrOperator, RightHandExtraFinger4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger4ROrderEnumAttrOperator
    PLUG_CLS = RightHandExtraFinger4ROrderEnumPlugOperator


class LeftFootThumb1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootThumb1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootThumb1ROrderEnumField(
    EnumField[LeftFootThumb1ROrderEnumAttrOperator, LeftFootThumb1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb1ROrderEnumAttrOperator
    PLUG_CLS = LeftFootThumb1ROrderEnumPlugOperator


class LeftFootThumb2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootThumb2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootThumb2ROrderEnumField(
    EnumField[LeftFootThumb2ROrderEnumAttrOperator, LeftFootThumb2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb2ROrderEnumAttrOperator
    PLUG_CLS = LeftFootThumb2ROrderEnumPlugOperator


class LeftFootThumb3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootThumb3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootThumb3ROrderEnumField(
    EnumField[LeftFootThumb3ROrderEnumAttrOperator, LeftFootThumb3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb3ROrderEnumAttrOperator
    PLUG_CLS = LeftFootThumb3ROrderEnumPlugOperator


class LeftFootThumb4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootThumb4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootThumb4ROrderEnumField(
    EnumField[LeftFootThumb4ROrderEnumAttrOperator, LeftFootThumb4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb4ROrderEnumAttrOperator
    PLUG_CLS = LeftFootThumb4ROrderEnumPlugOperator


class LeftFootIndex1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootIndex1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootIndex1ROrderEnumField(
    EnumField[LeftFootIndex1ROrderEnumAttrOperator, LeftFootIndex1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex1ROrderEnumAttrOperator
    PLUG_CLS = LeftFootIndex1ROrderEnumPlugOperator


class LeftFootIndex2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootIndex2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootIndex2ROrderEnumField(
    EnumField[LeftFootIndex2ROrderEnumAttrOperator, LeftFootIndex2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex2ROrderEnumAttrOperator
    PLUG_CLS = LeftFootIndex2ROrderEnumPlugOperator


class LeftFootIndex3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootIndex3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootIndex3ROrderEnumField(
    EnumField[LeftFootIndex3ROrderEnumAttrOperator, LeftFootIndex3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex3ROrderEnumAttrOperator
    PLUG_CLS = LeftFootIndex3ROrderEnumPlugOperator


class LeftFootIndex4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootIndex4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootIndex4ROrderEnumField(
    EnumField[LeftFootIndex4ROrderEnumAttrOperator, LeftFootIndex4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex4ROrderEnumAttrOperator
    PLUG_CLS = LeftFootIndex4ROrderEnumPlugOperator


class LeftFootMiddle1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootMiddle1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootMiddle1ROrderEnumField(
    EnumField[LeftFootMiddle1ROrderEnumAttrOperator, LeftFootMiddle1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle1ROrderEnumAttrOperator
    PLUG_CLS = LeftFootMiddle1ROrderEnumPlugOperator


class LeftFootMiddle2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootMiddle2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootMiddle2ROrderEnumField(
    EnumField[LeftFootMiddle2ROrderEnumAttrOperator, LeftFootMiddle2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle2ROrderEnumAttrOperator
    PLUG_CLS = LeftFootMiddle2ROrderEnumPlugOperator


class LeftFootMiddle3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootMiddle3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootMiddle3ROrderEnumField(
    EnumField[LeftFootMiddle3ROrderEnumAttrOperator, LeftFootMiddle3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle3ROrderEnumAttrOperator
    PLUG_CLS = LeftFootMiddle3ROrderEnumPlugOperator


class LeftFootMiddle4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootMiddle4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootMiddle4ROrderEnumField(
    EnumField[LeftFootMiddle4ROrderEnumAttrOperator, LeftFootMiddle4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle4ROrderEnumAttrOperator
    PLUG_CLS = LeftFootMiddle4ROrderEnumPlugOperator


class LeftFootRing1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootRing1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootRing1ROrderEnumField(
    EnumField[LeftFootRing1ROrderEnumAttrOperator, LeftFootRing1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing1ROrderEnumAttrOperator
    PLUG_CLS = LeftFootRing1ROrderEnumPlugOperator


class LeftFootRing2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootRing2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootRing2ROrderEnumField(
    EnumField[LeftFootRing2ROrderEnumAttrOperator, LeftFootRing2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing2ROrderEnumAttrOperator
    PLUG_CLS = LeftFootRing2ROrderEnumPlugOperator


class LeftFootRing3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootRing3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootRing3ROrderEnumField(
    EnumField[LeftFootRing3ROrderEnumAttrOperator, LeftFootRing3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing3ROrderEnumAttrOperator
    PLUG_CLS = LeftFootRing3ROrderEnumPlugOperator


class LeftFootRing4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootRing4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootRing4ROrderEnumField(
    EnumField[LeftFootRing4ROrderEnumAttrOperator, LeftFootRing4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing4ROrderEnumAttrOperator
    PLUG_CLS = LeftFootRing4ROrderEnumPlugOperator


class LeftFootPinky1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootPinky1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootPinky1ROrderEnumField(
    EnumField[LeftFootPinky1ROrderEnumAttrOperator, LeftFootPinky1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky1ROrderEnumAttrOperator
    PLUG_CLS = LeftFootPinky1ROrderEnumPlugOperator


class LeftFootPinky2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootPinky2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootPinky2ROrderEnumField(
    EnumField[LeftFootPinky2ROrderEnumAttrOperator, LeftFootPinky2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky2ROrderEnumAttrOperator
    PLUG_CLS = LeftFootPinky2ROrderEnumPlugOperator


class LeftFootPinky3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootPinky3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootPinky3ROrderEnumField(
    EnumField[LeftFootPinky3ROrderEnumAttrOperator, LeftFootPinky3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky3ROrderEnumAttrOperator
    PLUG_CLS = LeftFootPinky3ROrderEnumPlugOperator


class LeftFootPinky4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootPinky4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootPinky4ROrderEnumField(
    EnumField[LeftFootPinky4ROrderEnumAttrOperator, LeftFootPinky4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky4ROrderEnumAttrOperator
    PLUG_CLS = LeftFootPinky4ROrderEnumPlugOperator


class LeftFootExtraFinger1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootExtraFinger1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootExtraFinger1ROrderEnumField(
    EnumField[LeftFootExtraFinger1ROrderEnumAttrOperator, LeftFootExtraFinger1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger1ROrderEnumAttrOperator
    PLUG_CLS = LeftFootExtraFinger1ROrderEnumPlugOperator


class LeftFootExtraFinger2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootExtraFinger2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootExtraFinger2ROrderEnumField(
    EnumField[LeftFootExtraFinger2ROrderEnumAttrOperator, LeftFootExtraFinger2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger2ROrderEnumAttrOperator
    PLUG_CLS = LeftFootExtraFinger2ROrderEnumPlugOperator


class LeftFootExtraFinger3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootExtraFinger3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootExtraFinger3ROrderEnumField(
    EnumField[LeftFootExtraFinger3ROrderEnumAttrOperator, LeftFootExtraFinger3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger3ROrderEnumAttrOperator
    PLUG_CLS = LeftFootExtraFinger3ROrderEnumPlugOperator


class LeftFootExtraFinger4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftFootExtraFinger4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftFootExtraFinger4ROrderEnumField(
    EnumField[LeftFootExtraFinger4ROrderEnumAttrOperator, LeftFootExtraFinger4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger4ROrderEnumAttrOperator
    PLUG_CLS = LeftFootExtraFinger4ROrderEnumPlugOperator


class RightFootThumb1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootThumb1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootThumb1ROrderEnumField(
    EnumField[RightFootThumb1ROrderEnumAttrOperator, RightFootThumb1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb1ROrderEnumAttrOperator
    PLUG_CLS = RightFootThumb1ROrderEnumPlugOperator


class RightFootThumb2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootThumb2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootThumb2ROrderEnumField(
    EnumField[RightFootThumb2ROrderEnumAttrOperator, RightFootThumb2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb2ROrderEnumAttrOperator
    PLUG_CLS = RightFootThumb2ROrderEnumPlugOperator


class RightFootThumb3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootThumb3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootThumb3ROrderEnumField(
    EnumField[RightFootThumb3ROrderEnumAttrOperator, RightFootThumb3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb3ROrderEnumAttrOperator
    PLUG_CLS = RightFootThumb3ROrderEnumPlugOperator


class RightFootThumb4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootThumb4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootThumb4ROrderEnumField(
    EnumField[RightFootThumb4ROrderEnumAttrOperator, RightFootThumb4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb4ROrderEnumAttrOperator
    PLUG_CLS = RightFootThumb4ROrderEnumPlugOperator


class RightFootIndex1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootIndex1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootIndex1ROrderEnumField(
    EnumField[RightFootIndex1ROrderEnumAttrOperator, RightFootIndex1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex1ROrderEnumAttrOperator
    PLUG_CLS = RightFootIndex1ROrderEnumPlugOperator


class RightFootIndex2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootIndex2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootIndex2ROrderEnumField(
    EnumField[RightFootIndex2ROrderEnumAttrOperator, RightFootIndex2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex2ROrderEnumAttrOperator
    PLUG_CLS = RightFootIndex2ROrderEnumPlugOperator


class RightFootIndex3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootIndex3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootIndex3ROrderEnumField(
    EnumField[RightFootIndex3ROrderEnumAttrOperator, RightFootIndex3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex3ROrderEnumAttrOperator
    PLUG_CLS = RightFootIndex3ROrderEnumPlugOperator


class RightFootIndex4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootIndex4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootIndex4ROrderEnumField(
    EnumField[RightFootIndex4ROrderEnumAttrOperator, RightFootIndex4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex4ROrderEnumAttrOperator
    PLUG_CLS = RightFootIndex4ROrderEnumPlugOperator


class RightFootMiddle1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootMiddle1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootMiddle1ROrderEnumField(
    EnumField[RightFootMiddle1ROrderEnumAttrOperator, RightFootMiddle1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle1ROrderEnumAttrOperator
    PLUG_CLS = RightFootMiddle1ROrderEnumPlugOperator


class RightFootMiddle2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootMiddle2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootMiddle2ROrderEnumField(
    EnumField[RightFootMiddle2ROrderEnumAttrOperator, RightFootMiddle2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle2ROrderEnumAttrOperator
    PLUG_CLS = RightFootMiddle2ROrderEnumPlugOperator


class RightFootMiddle3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootMiddle3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootMiddle3ROrderEnumField(
    EnumField[RightFootMiddle3ROrderEnumAttrOperator, RightFootMiddle3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle3ROrderEnumAttrOperator
    PLUG_CLS = RightFootMiddle3ROrderEnumPlugOperator


class RightFootMiddle4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootMiddle4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootMiddle4ROrderEnumField(
    EnumField[RightFootMiddle4ROrderEnumAttrOperator, RightFootMiddle4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle4ROrderEnumAttrOperator
    PLUG_CLS = RightFootMiddle4ROrderEnumPlugOperator


class RightFootRing1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootRing1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootRing1ROrderEnumField(
    EnumField[RightFootRing1ROrderEnumAttrOperator, RightFootRing1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing1ROrderEnumAttrOperator
    PLUG_CLS = RightFootRing1ROrderEnumPlugOperator


class RightFootRing2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootRing2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootRing2ROrderEnumField(
    EnumField[RightFootRing2ROrderEnumAttrOperator, RightFootRing2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing2ROrderEnumAttrOperator
    PLUG_CLS = RightFootRing2ROrderEnumPlugOperator


class RightFootRing3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootRing3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootRing3ROrderEnumField(
    EnumField[RightFootRing3ROrderEnumAttrOperator, RightFootRing3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing3ROrderEnumAttrOperator
    PLUG_CLS = RightFootRing3ROrderEnumPlugOperator


class RightFootRing4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootRing4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootRing4ROrderEnumField(
    EnumField[RightFootRing4ROrderEnumAttrOperator, RightFootRing4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing4ROrderEnumAttrOperator
    PLUG_CLS = RightFootRing4ROrderEnumPlugOperator


class RightFootPinky1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootPinky1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootPinky1ROrderEnumField(
    EnumField[RightFootPinky1ROrderEnumAttrOperator, RightFootPinky1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky1ROrderEnumAttrOperator
    PLUG_CLS = RightFootPinky1ROrderEnumPlugOperator


class RightFootPinky2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootPinky2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootPinky2ROrderEnumField(
    EnumField[RightFootPinky2ROrderEnumAttrOperator, RightFootPinky2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky2ROrderEnumAttrOperator
    PLUG_CLS = RightFootPinky2ROrderEnumPlugOperator


class RightFootPinky3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootPinky3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootPinky3ROrderEnumField(
    EnumField[RightFootPinky3ROrderEnumAttrOperator, RightFootPinky3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky3ROrderEnumAttrOperator
    PLUG_CLS = RightFootPinky3ROrderEnumPlugOperator


class RightFootPinky4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootPinky4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootPinky4ROrderEnumField(
    EnumField[RightFootPinky4ROrderEnumAttrOperator, RightFootPinky4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky4ROrderEnumAttrOperator
    PLUG_CLS = RightFootPinky4ROrderEnumPlugOperator


class RightFootExtraFinger1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootExtraFinger1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootExtraFinger1ROrderEnumField(
    EnumField[RightFootExtraFinger1ROrderEnumAttrOperator, RightFootExtraFinger1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger1ROrderEnumAttrOperator
    PLUG_CLS = RightFootExtraFinger1ROrderEnumPlugOperator


class RightFootExtraFinger2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootExtraFinger2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootExtraFinger2ROrderEnumField(
    EnumField[RightFootExtraFinger2ROrderEnumAttrOperator, RightFootExtraFinger2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger2ROrderEnumAttrOperator
    PLUG_CLS = RightFootExtraFinger2ROrderEnumPlugOperator


class RightFootExtraFinger3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootExtraFinger3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootExtraFinger3ROrderEnumField(
    EnumField[RightFootExtraFinger3ROrderEnumAttrOperator, RightFootExtraFinger3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger3ROrderEnumAttrOperator
    PLUG_CLS = RightFootExtraFinger3ROrderEnumPlugOperator


class RightFootExtraFinger4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightFootExtraFinger4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightFootExtraFinger4ROrderEnumField(
    EnumField[RightFootExtraFinger4ROrderEnumAttrOperator, RightFootExtraFinger4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger4ROrderEnumAttrOperator
    PLUG_CLS = RightFootExtraFinger4ROrderEnumPlugOperator


class LeftInHandThumbROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInHandThumbROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInHandThumbROrderEnumField(
    EnumField[LeftInHandThumbROrderEnumAttrOperator, LeftInHandThumbROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandThumbROrderEnumAttrOperator
    PLUG_CLS = LeftInHandThumbROrderEnumPlugOperator


class LeftInHandIndexROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInHandIndexROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInHandIndexROrderEnumField(
    EnumField[LeftInHandIndexROrderEnumAttrOperator, LeftInHandIndexROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandIndexROrderEnumAttrOperator
    PLUG_CLS = LeftInHandIndexROrderEnumPlugOperator


class LeftInHandMiddleROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInHandMiddleROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInHandMiddleROrderEnumField(
    EnumField[LeftInHandMiddleROrderEnumAttrOperator, LeftInHandMiddleROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandMiddleROrderEnumAttrOperator
    PLUG_CLS = LeftInHandMiddleROrderEnumPlugOperator


class LeftInHandRingROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInHandRingROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInHandRingROrderEnumField(
    EnumField[LeftInHandRingROrderEnumAttrOperator, LeftInHandRingROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandRingROrderEnumAttrOperator
    PLUG_CLS = LeftInHandRingROrderEnumPlugOperator


class LeftInHandPinkyROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInHandPinkyROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInHandPinkyROrderEnumField(
    EnumField[LeftInHandPinkyROrderEnumAttrOperator, LeftInHandPinkyROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandPinkyROrderEnumAttrOperator
    PLUG_CLS = LeftInHandPinkyROrderEnumPlugOperator


class LeftInHandExtraFingerROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInHandExtraFingerROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInHandExtraFingerROrderEnumField(
    EnumField[LeftInHandExtraFingerROrderEnumAttrOperator, LeftInHandExtraFingerROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandExtraFingerROrderEnumAttrOperator
    PLUG_CLS = LeftInHandExtraFingerROrderEnumPlugOperator


class RightInHandThumbROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInHandThumbROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInHandThumbROrderEnumField(
    EnumField[RightInHandThumbROrderEnumAttrOperator, RightInHandThumbROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandThumbROrderEnumAttrOperator
    PLUG_CLS = RightInHandThumbROrderEnumPlugOperator


class RightInHandIndexROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInHandIndexROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInHandIndexROrderEnumField(
    EnumField[RightInHandIndexROrderEnumAttrOperator, RightInHandIndexROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandIndexROrderEnumAttrOperator
    PLUG_CLS = RightInHandIndexROrderEnumPlugOperator


class RightInHandMiddleROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInHandMiddleROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInHandMiddleROrderEnumField(
    EnumField[RightInHandMiddleROrderEnumAttrOperator, RightInHandMiddleROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandMiddleROrderEnumAttrOperator
    PLUG_CLS = RightInHandMiddleROrderEnumPlugOperator


class RightInHandRingROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInHandRingROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInHandRingROrderEnumField(
    EnumField[RightInHandRingROrderEnumAttrOperator, RightInHandRingROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandRingROrderEnumAttrOperator
    PLUG_CLS = RightInHandRingROrderEnumPlugOperator


class RightInHandPinkyROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInHandPinkyROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInHandPinkyROrderEnumField(
    EnumField[RightInHandPinkyROrderEnumAttrOperator, RightInHandPinkyROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandPinkyROrderEnumAttrOperator
    PLUG_CLS = RightInHandPinkyROrderEnumPlugOperator


class RightInHandExtraFingerROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInHandExtraFingerROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInHandExtraFingerROrderEnumField(
    EnumField[RightInHandExtraFingerROrderEnumAttrOperator, RightInHandExtraFingerROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandExtraFingerROrderEnumAttrOperator
    PLUG_CLS = RightInHandExtraFingerROrderEnumPlugOperator


class LeftInFootThumbROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInFootThumbROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInFootThumbROrderEnumField(
    EnumField[LeftInFootThumbROrderEnumAttrOperator, LeftInFootThumbROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootThumbROrderEnumAttrOperator
    PLUG_CLS = LeftInFootThumbROrderEnumPlugOperator


class LeftInFootIndexROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInFootIndexROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInFootIndexROrderEnumField(
    EnumField[LeftInFootIndexROrderEnumAttrOperator, LeftInFootIndexROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootIndexROrderEnumAttrOperator
    PLUG_CLS = LeftInFootIndexROrderEnumPlugOperator


class LeftInFootMiddleROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInFootMiddleROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInFootMiddleROrderEnumField(
    EnumField[LeftInFootMiddleROrderEnumAttrOperator, LeftInFootMiddleROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootMiddleROrderEnumAttrOperator
    PLUG_CLS = LeftInFootMiddleROrderEnumPlugOperator


class LeftInFootRingROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInFootRingROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInFootRingROrderEnumField(
    EnumField[LeftInFootRingROrderEnumAttrOperator, LeftInFootRingROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootRingROrderEnumAttrOperator
    PLUG_CLS = LeftInFootRingROrderEnumPlugOperator


class LeftInFootPinkyROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInFootPinkyROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInFootPinkyROrderEnumField(
    EnumField[LeftInFootPinkyROrderEnumAttrOperator, LeftInFootPinkyROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootPinkyROrderEnumAttrOperator
    PLUG_CLS = LeftInFootPinkyROrderEnumPlugOperator


class LeftInFootExtraFingerROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftInFootExtraFingerROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftInFootExtraFingerROrderEnumField(
    EnumField[LeftInFootExtraFingerROrderEnumAttrOperator, LeftInFootExtraFingerROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootExtraFingerROrderEnumAttrOperator
    PLUG_CLS = LeftInFootExtraFingerROrderEnumPlugOperator


class RightInFootThumbROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInFootThumbROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInFootThumbROrderEnumField(
    EnumField[RightInFootThumbROrderEnumAttrOperator, RightInFootThumbROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootThumbROrderEnumAttrOperator
    PLUG_CLS = RightInFootThumbROrderEnumPlugOperator


class RightInFootIndexROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInFootIndexROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInFootIndexROrderEnumField(
    EnumField[RightInFootIndexROrderEnumAttrOperator, RightInFootIndexROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootIndexROrderEnumAttrOperator
    PLUG_CLS = RightInFootIndexROrderEnumPlugOperator


class RightInFootMiddleROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInFootMiddleROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInFootMiddleROrderEnumField(
    EnumField[RightInFootMiddleROrderEnumAttrOperator, RightInFootMiddleROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootMiddleROrderEnumAttrOperator
    PLUG_CLS = RightInFootMiddleROrderEnumPlugOperator


class RightInFootRingROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInFootRingROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInFootRingROrderEnumField(
    EnumField[RightInFootRingROrderEnumAttrOperator, RightInFootRingROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootRingROrderEnumAttrOperator
    PLUG_CLS = RightInFootRingROrderEnumPlugOperator


class RightInFootPinkyROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInFootPinkyROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInFootPinkyROrderEnumField(
    EnumField[RightInFootPinkyROrderEnumAttrOperator, RightInFootPinkyROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootPinkyROrderEnumAttrOperator
    PLUG_CLS = RightInFootPinkyROrderEnumPlugOperator


class RightInFootExtraFingerROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightInFootExtraFingerROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightInFootExtraFingerROrderEnumField(
    EnumField[RightInFootExtraFingerROrderEnumAttrOperator, RightInFootExtraFingerROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootExtraFingerROrderEnumAttrOperator
    PLUG_CLS = RightInFootExtraFingerROrderEnumPlugOperator


class LeftShoulderExtraROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeftShoulderExtraROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeftShoulderExtraROrderEnumField(
    EnumField[LeftShoulderExtraROrderEnumAttrOperator, LeftShoulderExtraROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderExtraROrderEnumAttrOperator
    PLUG_CLS = LeftShoulderExtraROrderEnumPlugOperator


class RightShoulderExtraROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RightShoulderExtraROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RightShoulderExtraROrderEnumField(
    EnumField[RightShoulderExtraROrderEnumAttrOperator, RightShoulderExtraROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderExtraROrderEnumAttrOperator
    PLUG_CLS = RightShoulderExtraROrderEnumPlugOperator


class LeafLeftUpLegRoll1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftUpLegRoll1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftUpLegRoll1ROrderEnumField(
    EnumField[LeafLeftUpLegRoll1ROrderEnumAttrOperator, LeafLeftUpLegRoll1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll1ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll1ROrderEnumPlugOperator


class LeafLeftLegRoll1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftLegRoll1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftLegRoll1ROrderEnumField(
    EnumField[LeafLeftLegRoll1ROrderEnumAttrOperator, LeafLeftLegRoll1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll1ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftLegRoll1ROrderEnumPlugOperator


class LeafRightUpLegRoll1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightUpLegRoll1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightUpLegRoll1ROrderEnumField(
    EnumField[LeafRightUpLegRoll1ROrderEnumAttrOperator, LeafRightUpLegRoll1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll1ROrderEnumAttrOperator
    PLUG_CLS = LeafRightUpLegRoll1ROrderEnumPlugOperator


class LeafRightLegRoll1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightLegRoll1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightLegRoll1ROrderEnumField(
    EnumField[LeafRightLegRoll1ROrderEnumAttrOperator, LeafRightLegRoll1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll1ROrderEnumAttrOperator
    PLUG_CLS = LeafRightLegRoll1ROrderEnumPlugOperator


class LeafLeftArmRoll1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftArmRoll1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftArmRoll1ROrderEnumField(
    EnumField[LeafLeftArmRoll1ROrderEnumAttrOperator, LeafLeftArmRoll1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll1ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftArmRoll1ROrderEnumPlugOperator


class LeafLeftForeArmRoll1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftForeArmRoll1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftForeArmRoll1ROrderEnumField(
    EnumField[LeafLeftForeArmRoll1ROrderEnumAttrOperator, LeafLeftForeArmRoll1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll1ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll1ROrderEnumPlugOperator


class LeafRightArmRoll1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightArmRoll1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightArmRoll1ROrderEnumField(
    EnumField[LeafRightArmRoll1ROrderEnumAttrOperator, LeafRightArmRoll1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll1ROrderEnumAttrOperator
    PLUG_CLS = LeafRightArmRoll1ROrderEnumPlugOperator


class LeafRightForeArmRoll1ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightForeArmRoll1ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightForeArmRoll1ROrderEnumField(
    EnumField[LeafRightForeArmRoll1ROrderEnumAttrOperator, LeafRightForeArmRoll1ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll1ROrderEnumAttrOperator
    PLUG_CLS = LeafRightForeArmRoll1ROrderEnumPlugOperator


class LeafLeftUpLegRoll2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftUpLegRoll2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftUpLegRoll2ROrderEnumField(
    EnumField[LeafLeftUpLegRoll2ROrderEnumAttrOperator, LeafLeftUpLegRoll2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll2ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll2ROrderEnumPlugOperator


class LeafLeftLegRoll2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftLegRoll2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftLegRoll2ROrderEnumField(
    EnumField[LeafLeftLegRoll2ROrderEnumAttrOperator, LeafLeftLegRoll2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll2ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftLegRoll2ROrderEnumPlugOperator


class LeafRightUpLegRoll2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightUpLegRoll2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightUpLegRoll2ROrderEnumField(
    EnumField[LeafRightUpLegRoll2ROrderEnumAttrOperator, LeafRightUpLegRoll2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll2ROrderEnumAttrOperator
    PLUG_CLS = LeafRightUpLegRoll2ROrderEnumPlugOperator


class LeafRightLegRoll2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightLegRoll2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightLegRoll2ROrderEnumField(
    EnumField[LeafRightLegRoll2ROrderEnumAttrOperator, LeafRightLegRoll2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll2ROrderEnumAttrOperator
    PLUG_CLS = LeafRightLegRoll2ROrderEnumPlugOperator


class LeafLeftArmRoll2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftArmRoll2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftArmRoll2ROrderEnumField(
    EnumField[LeafLeftArmRoll2ROrderEnumAttrOperator, LeafLeftArmRoll2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll2ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftArmRoll2ROrderEnumPlugOperator


class LeafLeftForeArmRoll2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftForeArmRoll2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftForeArmRoll2ROrderEnumField(
    EnumField[LeafLeftForeArmRoll2ROrderEnumAttrOperator, LeafLeftForeArmRoll2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll2ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll2ROrderEnumPlugOperator


class LeafRightArmRoll2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightArmRoll2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightArmRoll2ROrderEnumField(
    EnumField[LeafRightArmRoll2ROrderEnumAttrOperator, LeafRightArmRoll2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll2ROrderEnumAttrOperator
    PLUG_CLS = LeafRightArmRoll2ROrderEnumPlugOperator


class LeafRightForeArmRoll2ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightForeArmRoll2ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightForeArmRoll2ROrderEnumField(
    EnumField[LeafRightForeArmRoll2ROrderEnumAttrOperator, LeafRightForeArmRoll2ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll2ROrderEnumAttrOperator
    PLUG_CLS = LeafRightForeArmRoll2ROrderEnumPlugOperator


class LeafLeftUpLegRoll3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftUpLegRoll3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftUpLegRoll3ROrderEnumField(
    EnumField[LeafLeftUpLegRoll3ROrderEnumAttrOperator, LeafLeftUpLegRoll3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll3ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll3ROrderEnumPlugOperator


class LeafLeftLegRoll3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftLegRoll3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftLegRoll3ROrderEnumField(
    EnumField[LeafLeftLegRoll3ROrderEnumAttrOperator, LeafLeftLegRoll3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll3ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftLegRoll3ROrderEnumPlugOperator


class LeafRightUpLegRoll3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightUpLegRoll3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightUpLegRoll3ROrderEnumField(
    EnumField[LeafRightUpLegRoll3ROrderEnumAttrOperator, LeafRightUpLegRoll3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll3ROrderEnumAttrOperator
    PLUG_CLS = LeafRightUpLegRoll3ROrderEnumPlugOperator


class LeafRightLegRoll3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightLegRoll3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightLegRoll3ROrderEnumField(
    EnumField[LeafRightLegRoll3ROrderEnumAttrOperator, LeafRightLegRoll3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll3ROrderEnumAttrOperator
    PLUG_CLS = LeafRightLegRoll3ROrderEnumPlugOperator


class LeafLeftArmRoll3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftArmRoll3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftArmRoll3ROrderEnumField(
    EnumField[LeafLeftArmRoll3ROrderEnumAttrOperator, LeafLeftArmRoll3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll3ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftArmRoll3ROrderEnumPlugOperator


class LeafLeftForeArmRoll3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftForeArmRoll3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftForeArmRoll3ROrderEnumField(
    EnumField[LeafLeftForeArmRoll3ROrderEnumAttrOperator, LeafLeftForeArmRoll3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll3ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll3ROrderEnumPlugOperator


class LeafRightArmRoll3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightArmRoll3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightArmRoll3ROrderEnumField(
    EnumField[LeafRightArmRoll3ROrderEnumAttrOperator, LeafRightArmRoll3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll3ROrderEnumAttrOperator
    PLUG_CLS = LeafRightArmRoll3ROrderEnumPlugOperator


class LeafRightForeArmRoll3ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightForeArmRoll3ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightForeArmRoll3ROrderEnumField(
    EnumField[LeafRightForeArmRoll3ROrderEnumAttrOperator, LeafRightForeArmRoll3ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll3ROrderEnumAttrOperator
    PLUG_CLS = LeafRightForeArmRoll3ROrderEnumPlugOperator


class LeafLeftUpLegRoll4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftUpLegRoll4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftUpLegRoll4ROrderEnumField(
    EnumField[LeafLeftUpLegRoll4ROrderEnumAttrOperator, LeafLeftUpLegRoll4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll4ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll4ROrderEnumPlugOperator


class LeafLeftLegRoll4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftLegRoll4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftLegRoll4ROrderEnumField(
    EnumField[LeafLeftLegRoll4ROrderEnumAttrOperator, LeafLeftLegRoll4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll4ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftLegRoll4ROrderEnumPlugOperator


class LeafRightUpLegRoll4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightUpLegRoll4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightUpLegRoll4ROrderEnumField(
    EnumField[LeafRightUpLegRoll4ROrderEnumAttrOperator, LeafRightUpLegRoll4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll4ROrderEnumAttrOperator
    PLUG_CLS = LeafRightUpLegRoll4ROrderEnumPlugOperator


class LeafRightLegRoll4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightLegRoll4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightLegRoll4ROrderEnumField(
    EnumField[LeafRightLegRoll4ROrderEnumAttrOperator, LeafRightLegRoll4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll4ROrderEnumAttrOperator
    PLUG_CLS = LeafRightLegRoll4ROrderEnumPlugOperator


class LeafLeftArmRoll4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftArmRoll4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftArmRoll4ROrderEnumField(
    EnumField[LeafLeftArmRoll4ROrderEnumAttrOperator, LeafLeftArmRoll4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll4ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftArmRoll4ROrderEnumPlugOperator


class LeafLeftForeArmRoll4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftForeArmRoll4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftForeArmRoll4ROrderEnumField(
    EnumField[LeafLeftForeArmRoll4ROrderEnumAttrOperator, LeafLeftForeArmRoll4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll4ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll4ROrderEnumPlugOperator


class LeafRightArmRoll4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightArmRoll4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightArmRoll4ROrderEnumField(
    EnumField[LeafRightArmRoll4ROrderEnumAttrOperator, LeafRightArmRoll4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll4ROrderEnumAttrOperator
    PLUG_CLS = LeafRightArmRoll4ROrderEnumPlugOperator


class LeafRightForeArmRoll4ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightForeArmRoll4ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightForeArmRoll4ROrderEnumField(
    EnumField[LeafRightForeArmRoll4ROrderEnumAttrOperator, LeafRightForeArmRoll4ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll4ROrderEnumAttrOperator
    PLUG_CLS = LeafRightForeArmRoll4ROrderEnumPlugOperator


class LeafLeftUpLegRoll5ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftUpLegRoll5ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftUpLegRoll5ROrderEnumField(
    EnumField[LeafLeftUpLegRoll5ROrderEnumAttrOperator, LeafLeftUpLegRoll5ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll5ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll5ROrderEnumPlugOperator


class LeafLeftLegRoll5ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftLegRoll5ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftLegRoll5ROrderEnumField(
    EnumField[LeafLeftLegRoll5ROrderEnumAttrOperator, LeafLeftLegRoll5ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll5ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftLegRoll5ROrderEnumPlugOperator


class LeafRightUpLegRoll5ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightUpLegRoll5ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightUpLegRoll5ROrderEnumField(
    EnumField[LeafRightUpLegRoll5ROrderEnumAttrOperator, LeafRightUpLegRoll5ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll5ROrderEnumAttrOperator
    PLUG_CLS = LeafRightUpLegRoll5ROrderEnumPlugOperator


class LeafRightLegRoll5ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightLegRoll5ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightLegRoll5ROrderEnumField(
    EnumField[LeafRightLegRoll5ROrderEnumAttrOperator, LeafRightLegRoll5ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll5ROrderEnumAttrOperator
    PLUG_CLS = LeafRightLegRoll5ROrderEnumPlugOperator


class LeafLeftArmRoll5ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftArmRoll5ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftArmRoll5ROrderEnumField(
    EnumField[LeafLeftArmRoll5ROrderEnumAttrOperator, LeafLeftArmRoll5ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll5ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftArmRoll5ROrderEnumPlugOperator


class LeafLeftForeArmRoll5ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafLeftForeArmRoll5ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafLeftForeArmRoll5ROrderEnumField(
    EnumField[LeafLeftForeArmRoll5ROrderEnumAttrOperator, LeafLeftForeArmRoll5ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll5ROrderEnumAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll5ROrderEnumPlugOperator


class LeafRightArmRoll5ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightArmRoll5ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightArmRoll5ROrderEnumField(
    EnumField[LeafRightArmRoll5ROrderEnumAttrOperator, LeafRightArmRoll5ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll5ROrderEnumAttrOperator
    PLUG_CLS = LeafRightArmRoll5ROrderEnumPlugOperator


class LeafRightForeArmRoll5ROrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class LeafRightForeArmRoll5ROrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class LeafRightForeArmRoll5ROrderEnumField(
    EnumField[LeafRightForeArmRoll5ROrderEnumAttrOperator, LeafRightForeArmRoll5ROrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll5ROrderEnumAttrOperator
    PLUG_CLS = LeafRightForeArmRoll5ROrderEnumPlugOperator


class _GeneratedHIKState2SK(DG):
    __slots__ = ()

    NODE_TYPE = "HIKState2SK"

    InputCharacterState = TypedField()

    InputCharacterDefinition = TypedField()

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

    ReferencePGX = MatrixField()

    ReferenceROrder = ReferenceROrderEnumField(default_value=0)

    ReferenceSC = BoolField(default_value=False)

    ReferenceIS = ReferenceISField(default_value=(1.0, 1.0, 1.0))
    ReferenceISx = ReferenceIS.ReferenceISx
    ReferenceISy = ReferenceIS.ReferenceISy
    ReferenceISz = ReferenceIS.ReferenceISz

    ReferencePreR = ReferencePreRField(default_value=(0.0, 0.0, 0.0))
    ReferencePreRx = ReferencePreR.ReferencePreRx
    ReferencePreRy = ReferencePreR.ReferencePreRy
    ReferencePreRz = ReferencePreR.ReferencePreRz

    ReferencePostR = ReferencePostRField(default_value=(0.0, 0.0, 0.0))
    ReferencePostRx = ReferencePostR.ReferencePostRx
    ReferencePostRy = ReferencePostR.ReferencePostRy
    ReferencePostRz = ReferencePostR.ReferencePostRz

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

    HipsPGX = MatrixField()

    HipsROrder = HipsROrderEnumField(default_value=0)

    HipsSC = BoolField(default_value=False)

    HipsIS = HipsISField(default_value=(1.0, 1.0, 1.0))
    HipsISx = HipsIS.HipsISx
    HipsISy = HipsIS.HipsISy
    HipsISz = HipsIS.HipsISz

    HipsPreR = HipsPreRField(default_value=(0.0, 0.0, 0.0))
    HipsPreRx = HipsPreR.HipsPreRx
    HipsPreRy = HipsPreR.HipsPreRy
    HipsPreRz = HipsPreR.HipsPreRz

    HipsPostR = HipsPostRField(default_value=(0.0, 0.0, 0.0))
    HipsPostRx = HipsPostR.HipsPostRx
    HipsPostRy = HipsPostR.HipsPostRy
    HipsPostRz = HipsPostR.HipsPostRz

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

    LeftUpLegPGX = MatrixField()

    LeftUpLegROrder = LeftUpLegROrderEnumField(default_value=0)

    LeftUpLegSC = BoolField(default_value=False)

    LeftUpLegIS = LeftUpLegISField(default_value=(1.0, 1.0, 1.0))
    LeftUpLegISx = LeftUpLegIS.LeftUpLegISx
    LeftUpLegISy = LeftUpLegIS.LeftUpLegISy
    LeftUpLegISz = LeftUpLegIS.LeftUpLegISz

    LeftUpLegPreR = LeftUpLegPreRField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegPreRx = LeftUpLegPreR.LeftUpLegPreRx
    LeftUpLegPreRy = LeftUpLegPreR.LeftUpLegPreRy
    LeftUpLegPreRz = LeftUpLegPreR.LeftUpLegPreRz

    LeftUpLegPostR = LeftUpLegPostRField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegPostRx = LeftUpLegPostR.LeftUpLegPostRx
    LeftUpLegPostRy = LeftUpLegPostR.LeftUpLegPostRy
    LeftUpLegPostRz = LeftUpLegPostR.LeftUpLegPostRz

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

    LeftLegPGX = MatrixField()

    LeftLegROrder = LeftLegROrderEnumField(default_value=0)

    LeftLegSC = BoolField(default_value=False)

    LeftLegIS = LeftLegISField(default_value=(1.0, 1.0, 1.0))
    LeftLegISx = LeftLegIS.LeftLegISx
    LeftLegISy = LeftLegIS.LeftLegISy
    LeftLegISz = LeftLegIS.LeftLegISz

    LeftLegPreR = LeftLegPreRField(default_value=(0.0, 0.0, 0.0))
    LeftLegPreRx = LeftLegPreR.LeftLegPreRx
    LeftLegPreRy = LeftLegPreR.LeftLegPreRy
    LeftLegPreRz = LeftLegPreR.LeftLegPreRz

    LeftLegPostR = LeftLegPostRField(default_value=(0.0, 0.0, 0.0))
    LeftLegPostRx = LeftLegPostR.LeftLegPostRx
    LeftLegPostRy = LeftLegPostR.LeftLegPostRy
    LeftLegPostRz = LeftLegPostR.LeftLegPostRz

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

    LeftFootPGX = MatrixField()

    LeftFootROrder = LeftFootROrderEnumField(default_value=0)

    LeftFootSC = BoolField(default_value=False)

    LeftFootIS = LeftFootISField(default_value=(1.0, 1.0, 1.0))
    LeftFootISx = LeftFootIS.LeftFootISx
    LeftFootISy = LeftFootIS.LeftFootISy
    LeftFootISz = LeftFootIS.LeftFootISz

    LeftFootPreR = LeftFootPreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootPreRx = LeftFootPreR.LeftFootPreRx
    LeftFootPreRy = LeftFootPreR.LeftFootPreRy
    LeftFootPreRz = LeftFootPreR.LeftFootPreRz

    LeftFootPostR = LeftFootPostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootPostRx = LeftFootPostR.LeftFootPostRx
    LeftFootPostRy = LeftFootPostR.LeftFootPostRy
    LeftFootPostRz = LeftFootPostR.LeftFootPostRz

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

    RightUpLegPGX = MatrixField()

    RightUpLegROrder = RightUpLegROrderEnumField(default_value=0)

    RightUpLegSC = BoolField(default_value=False)

    RightUpLegIS = RightUpLegISField(default_value=(1.0, 1.0, 1.0))
    RightUpLegISx = RightUpLegIS.RightUpLegISx
    RightUpLegISy = RightUpLegIS.RightUpLegISy
    RightUpLegISz = RightUpLegIS.RightUpLegISz

    RightUpLegPreR = RightUpLegPreRField(default_value=(0.0, 0.0, 0.0))
    RightUpLegPreRx = RightUpLegPreR.RightUpLegPreRx
    RightUpLegPreRy = RightUpLegPreR.RightUpLegPreRy
    RightUpLegPreRz = RightUpLegPreR.RightUpLegPreRz

    RightUpLegPostR = RightUpLegPostRField(default_value=(0.0, 0.0, 0.0))
    RightUpLegPostRx = RightUpLegPostR.RightUpLegPostRx
    RightUpLegPostRy = RightUpLegPostR.RightUpLegPostRy
    RightUpLegPostRz = RightUpLegPostR.RightUpLegPostRz

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

    RightLegPGX = MatrixField()

    RightLegROrder = RightLegROrderEnumField(default_value=0)

    RightLegSC = BoolField(default_value=False)

    RightLegIS = RightLegISField(default_value=(1.0, 1.0, 1.0))
    RightLegISx = RightLegIS.RightLegISx
    RightLegISy = RightLegIS.RightLegISy
    RightLegISz = RightLegIS.RightLegISz

    RightLegPreR = RightLegPreRField(default_value=(0.0, 0.0, 0.0))
    RightLegPreRx = RightLegPreR.RightLegPreRx
    RightLegPreRy = RightLegPreR.RightLegPreRy
    RightLegPreRz = RightLegPreR.RightLegPreRz

    RightLegPostR = RightLegPostRField(default_value=(0.0, 0.0, 0.0))
    RightLegPostRx = RightLegPostR.RightLegPostRx
    RightLegPostRy = RightLegPostR.RightLegPostRy
    RightLegPostRz = RightLegPostR.RightLegPostRz

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

    RightFootPGX = MatrixField()

    RightFootROrder = RightFootROrderEnumField(default_value=0)

    RightFootSC = BoolField(default_value=False)

    RightFootIS = RightFootISField(default_value=(1.0, 1.0, 1.0))
    RightFootISx = RightFootIS.RightFootISx
    RightFootISy = RightFootIS.RightFootISy
    RightFootISz = RightFootIS.RightFootISz

    RightFootPreR = RightFootPreRField(default_value=(0.0, 0.0, 0.0))
    RightFootPreRx = RightFootPreR.RightFootPreRx
    RightFootPreRy = RightFootPreR.RightFootPreRy
    RightFootPreRz = RightFootPreR.RightFootPreRz

    RightFootPostR = RightFootPostRField(default_value=(0.0, 0.0, 0.0))
    RightFootPostRx = RightFootPostR.RightFootPostRx
    RightFootPostRy = RightFootPostR.RightFootPostRy
    RightFootPostRz = RightFootPostR.RightFootPostRz

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

    SpinePGX = MatrixField()

    SpineROrder = SpineROrderEnumField(default_value=0)

    SpineSC = BoolField(default_value=False)

    SpineIS = SpineISField(default_value=(1.0, 1.0, 1.0))
    SpineISx = SpineIS.SpineISx
    SpineISy = SpineIS.SpineISy
    SpineISz = SpineIS.SpineISz

    SpinePreR = SpinePreRField(default_value=(0.0, 0.0, 0.0))
    SpinePreRx = SpinePreR.SpinePreRx
    SpinePreRy = SpinePreR.SpinePreRy
    SpinePreRz = SpinePreR.SpinePreRz

    SpinePostR = SpinePostRField(default_value=(0.0, 0.0, 0.0))
    SpinePostRx = SpinePostR.SpinePostRx
    SpinePostRy = SpinePostR.SpinePostRy
    SpinePostRz = SpinePostR.SpinePostRz

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

    LeftArmPGX = MatrixField()

    LeftArmROrder = LeftArmROrderEnumField(default_value=0)

    LeftArmSC = BoolField(default_value=False)

    LeftArmIS = LeftArmISField(default_value=(1.0, 1.0, 1.0))
    LeftArmISx = LeftArmIS.LeftArmISx
    LeftArmISy = LeftArmIS.LeftArmISy
    LeftArmISz = LeftArmIS.LeftArmISz

    LeftArmPreR = LeftArmPreRField(default_value=(0.0, 0.0, 0.0))
    LeftArmPreRx = LeftArmPreR.LeftArmPreRx
    LeftArmPreRy = LeftArmPreR.LeftArmPreRy
    LeftArmPreRz = LeftArmPreR.LeftArmPreRz

    LeftArmPostR = LeftArmPostRField(default_value=(0.0, 0.0, 0.0))
    LeftArmPostRx = LeftArmPostR.LeftArmPostRx
    LeftArmPostRy = LeftArmPostR.LeftArmPostRy
    LeftArmPostRz = LeftArmPostR.LeftArmPostRz

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

    LeftForeArmPGX = MatrixField()

    LeftForeArmROrder = LeftForeArmROrderEnumField(default_value=0)

    LeftForeArmSC = BoolField(default_value=False)

    LeftForeArmIS = LeftForeArmISField(default_value=(1.0, 1.0, 1.0))
    LeftForeArmISx = LeftForeArmIS.LeftForeArmISx
    LeftForeArmISy = LeftForeArmIS.LeftForeArmISy
    LeftForeArmISz = LeftForeArmIS.LeftForeArmISz

    LeftForeArmPreR = LeftForeArmPreRField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmPreRx = LeftForeArmPreR.LeftForeArmPreRx
    LeftForeArmPreRy = LeftForeArmPreR.LeftForeArmPreRy
    LeftForeArmPreRz = LeftForeArmPreR.LeftForeArmPreRz

    LeftForeArmPostR = LeftForeArmPostRField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmPostRx = LeftForeArmPostR.LeftForeArmPostRx
    LeftForeArmPostRy = LeftForeArmPostR.LeftForeArmPostRy
    LeftForeArmPostRz = LeftForeArmPostR.LeftForeArmPostRz

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

    LeftHandPGX = MatrixField()

    LeftHandROrder = LeftHandROrderEnumField(default_value=0)

    LeftHandSC = BoolField(default_value=False)

    LeftHandIS = LeftHandISField(default_value=(1.0, 1.0, 1.0))
    LeftHandISx = LeftHandIS.LeftHandISx
    LeftHandISy = LeftHandIS.LeftHandISy
    LeftHandISz = LeftHandIS.LeftHandISz

    LeftHandPreR = LeftHandPreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandPreRx = LeftHandPreR.LeftHandPreRx
    LeftHandPreRy = LeftHandPreR.LeftHandPreRy
    LeftHandPreRz = LeftHandPreR.LeftHandPreRz

    LeftHandPostR = LeftHandPostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandPostRx = LeftHandPostR.LeftHandPostRx
    LeftHandPostRy = LeftHandPostR.LeftHandPostRy
    LeftHandPostRz = LeftHandPostR.LeftHandPostRz

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

    RightArmPGX = MatrixField()

    RightArmROrder = RightArmROrderEnumField(default_value=0)

    RightArmSC = BoolField(default_value=False)

    RightArmIS = RightArmISField(default_value=(1.0, 1.0, 1.0))
    RightArmISx = RightArmIS.RightArmISx
    RightArmISy = RightArmIS.RightArmISy
    RightArmISz = RightArmIS.RightArmISz

    RightArmPreR = RightArmPreRField(default_value=(0.0, 0.0, 0.0))
    RightArmPreRx = RightArmPreR.RightArmPreRx
    RightArmPreRy = RightArmPreR.RightArmPreRy
    RightArmPreRz = RightArmPreR.RightArmPreRz

    RightArmPostR = RightArmPostRField(default_value=(0.0, 0.0, 0.0))
    RightArmPostRx = RightArmPostR.RightArmPostRx
    RightArmPostRy = RightArmPostR.RightArmPostRy
    RightArmPostRz = RightArmPostR.RightArmPostRz

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

    RightForeArmPGX = MatrixField()

    RightForeArmROrder = RightForeArmROrderEnumField(default_value=0)

    RightForeArmSC = BoolField(default_value=False)

    RightForeArmIS = RightForeArmISField(default_value=(1.0, 1.0, 1.0))
    RightForeArmISx = RightForeArmIS.RightForeArmISx
    RightForeArmISy = RightForeArmIS.RightForeArmISy
    RightForeArmISz = RightForeArmIS.RightForeArmISz

    RightForeArmPreR = RightForeArmPreRField(default_value=(0.0, 0.0, 0.0))
    RightForeArmPreRx = RightForeArmPreR.RightForeArmPreRx
    RightForeArmPreRy = RightForeArmPreR.RightForeArmPreRy
    RightForeArmPreRz = RightForeArmPreR.RightForeArmPreRz

    RightForeArmPostR = RightForeArmPostRField(default_value=(0.0, 0.0, 0.0))
    RightForeArmPostRx = RightForeArmPostR.RightForeArmPostRx
    RightForeArmPostRy = RightForeArmPostR.RightForeArmPostRy
    RightForeArmPostRz = RightForeArmPostR.RightForeArmPostRz

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

    RightHandPGX = MatrixField()

    RightHandROrder = RightHandROrderEnumField(default_value=0)

    RightHandSC = BoolField(default_value=False)

    RightHandIS = RightHandISField(default_value=(1.0, 1.0, 1.0))
    RightHandISx = RightHandIS.RightHandISx
    RightHandISy = RightHandIS.RightHandISy
    RightHandISz = RightHandIS.RightHandISz

    RightHandPreR = RightHandPreRField(default_value=(0.0, 0.0, 0.0))
    RightHandPreRx = RightHandPreR.RightHandPreRx
    RightHandPreRy = RightHandPreR.RightHandPreRy
    RightHandPreRz = RightHandPreR.RightHandPreRz

    RightHandPostR = RightHandPostRField(default_value=(0.0, 0.0, 0.0))
    RightHandPostRx = RightHandPostR.RightHandPostRx
    RightHandPostRy = RightHandPostR.RightHandPostRy
    RightHandPostRz = RightHandPostR.RightHandPostRz

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

    HeadPGX = MatrixField()

    HeadROrder = HeadROrderEnumField(default_value=0)

    HeadSC = BoolField(default_value=False)

    HeadIS = HeadISField(default_value=(1.0, 1.0, 1.0))
    HeadISx = HeadIS.HeadISx
    HeadISy = HeadIS.HeadISy
    HeadISz = HeadIS.HeadISz

    HeadPreR = HeadPreRField(default_value=(0.0, 0.0, 0.0))
    HeadPreRx = HeadPreR.HeadPreRx
    HeadPreRy = HeadPreR.HeadPreRy
    HeadPreRz = HeadPreR.HeadPreRz

    HeadPostR = HeadPostRField(default_value=(0.0, 0.0, 0.0))
    HeadPostRx = HeadPostR.HeadPostRx
    HeadPostRy = HeadPostR.HeadPostRy
    HeadPostRz = HeadPostR.HeadPostRz

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

    LeftToeBasePGX = MatrixField()

    LeftToeBaseROrder = LeftToeBaseROrderEnumField(default_value=0)

    LeftToeBaseSC = BoolField(default_value=False)

    LeftToeBaseIS = LeftToeBaseISField(default_value=(1.0, 1.0, 1.0))
    LeftToeBaseISx = LeftToeBaseIS.LeftToeBaseISx
    LeftToeBaseISy = LeftToeBaseIS.LeftToeBaseISy
    LeftToeBaseISz = LeftToeBaseIS.LeftToeBaseISz

    LeftToeBasePreR = LeftToeBasePreRField(default_value=(0.0, 0.0, 0.0))
    LeftToeBasePreRx = LeftToeBasePreR.LeftToeBasePreRx
    LeftToeBasePreRy = LeftToeBasePreR.LeftToeBasePreRy
    LeftToeBasePreRz = LeftToeBasePreR.LeftToeBasePreRz

    LeftToeBasePostR = LeftToeBasePostRField(default_value=(0.0, 0.0, 0.0))
    LeftToeBasePostRx = LeftToeBasePostR.LeftToeBasePostRx
    LeftToeBasePostRy = LeftToeBasePostR.LeftToeBasePostRy
    LeftToeBasePostRz = LeftToeBasePostR.LeftToeBasePostRz

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

    RightToeBasePGX = MatrixField()

    RightToeBaseROrder = RightToeBaseROrderEnumField(default_value=0)

    RightToeBaseSC = BoolField(default_value=False)

    RightToeBaseIS = RightToeBaseISField(default_value=(1.0, 1.0, 1.0))
    RightToeBaseISx = RightToeBaseIS.RightToeBaseISx
    RightToeBaseISy = RightToeBaseIS.RightToeBaseISy
    RightToeBaseISz = RightToeBaseIS.RightToeBaseISz

    RightToeBasePreR = RightToeBasePreRField(default_value=(0.0, 0.0, 0.0))
    RightToeBasePreRx = RightToeBasePreR.RightToeBasePreRx
    RightToeBasePreRy = RightToeBasePreR.RightToeBasePreRy
    RightToeBasePreRz = RightToeBasePreR.RightToeBasePreRz

    RightToeBasePostR = RightToeBasePostRField(default_value=(0.0, 0.0, 0.0))
    RightToeBasePostRx = RightToeBasePostR.RightToeBasePostRx
    RightToeBasePostRy = RightToeBasePostR.RightToeBasePostRy
    RightToeBasePostRz = RightToeBasePostR.RightToeBasePostRz

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

    LeftShoulderPGX = MatrixField()

    LeftShoulderROrder = LeftShoulderROrderEnumField(default_value=0)

    LeftShoulderSC = BoolField(default_value=False)

    LeftShoulderIS = LeftShoulderISField(default_value=(1.0, 1.0, 1.0))
    LeftShoulderISx = LeftShoulderIS.LeftShoulderISx
    LeftShoulderISy = LeftShoulderIS.LeftShoulderISy
    LeftShoulderISz = LeftShoulderIS.LeftShoulderISz

    LeftShoulderPreR = LeftShoulderPreRField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderPreRx = LeftShoulderPreR.LeftShoulderPreRx
    LeftShoulderPreRy = LeftShoulderPreR.LeftShoulderPreRy
    LeftShoulderPreRz = LeftShoulderPreR.LeftShoulderPreRz

    LeftShoulderPostR = LeftShoulderPostRField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderPostRx = LeftShoulderPostR.LeftShoulderPostRx
    LeftShoulderPostRy = LeftShoulderPostR.LeftShoulderPostRy
    LeftShoulderPostRz = LeftShoulderPostR.LeftShoulderPostRz

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

    RightShoulderPGX = MatrixField()

    RightShoulderROrder = RightShoulderROrderEnumField(default_value=0)

    RightShoulderSC = BoolField(default_value=False)

    RightShoulderIS = RightShoulderISField(default_value=(1.0, 1.0, 1.0))
    RightShoulderISx = RightShoulderIS.RightShoulderISx
    RightShoulderISy = RightShoulderIS.RightShoulderISy
    RightShoulderISz = RightShoulderIS.RightShoulderISz

    RightShoulderPreR = RightShoulderPreRField(default_value=(0.0, 0.0, 0.0))
    RightShoulderPreRx = RightShoulderPreR.RightShoulderPreRx
    RightShoulderPreRy = RightShoulderPreR.RightShoulderPreRy
    RightShoulderPreRz = RightShoulderPreR.RightShoulderPreRz

    RightShoulderPostR = RightShoulderPostRField(default_value=(0.0, 0.0, 0.0))
    RightShoulderPostRx = RightShoulderPostR.RightShoulderPostRx
    RightShoulderPostRy = RightShoulderPostR.RightShoulderPostRy
    RightShoulderPostRz = RightShoulderPostR.RightShoulderPostRz

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

    NeckPGX = MatrixField()

    NeckROrder = NeckROrderEnumField(default_value=0)

    NeckSC = BoolField(default_value=False)

    NeckIS = NeckISField(default_value=(1.0, 1.0, 1.0))
    NeckISx = NeckIS.NeckISx
    NeckISy = NeckIS.NeckISy
    NeckISz = NeckIS.NeckISz

    NeckPreR = NeckPreRField(default_value=(0.0, 0.0, 0.0))
    NeckPreRx = NeckPreR.NeckPreRx
    NeckPreRy = NeckPreR.NeckPreRy
    NeckPreRz = NeckPreR.NeckPreRz

    NeckPostR = NeckPostRField(default_value=(0.0, 0.0, 0.0))
    NeckPostRx = NeckPostR.NeckPostRx
    NeckPostRy = NeckPostR.NeckPostRy
    NeckPostRz = NeckPostR.NeckPostRz

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

    LeftFingerBasePGX = MatrixField()

    LeftFingerBaseROrder = LeftFingerBaseROrderEnumField(default_value=0)

    LeftFingerBaseSC = BoolField(default_value=False)

    LeftFingerBaseIS = LeftFingerBaseISField(default_value=(1.0, 1.0, 1.0))
    LeftFingerBaseISx = LeftFingerBaseIS.LeftFingerBaseISx
    LeftFingerBaseISy = LeftFingerBaseIS.LeftFingerBaseISy
    LeftFingerBaseISz = LeftFingerBaseIS.LeftFingerBaseISz

    LeftFingerBasePreR = LeftFingerBasePreRField(default_value=(0.0, 0.0, 0.0))
    LeftFingerBasePreRx = LeftFingerBasePreR.LeftFingerBasePreRx
    LeftFingerBasePreRy = LeftFingerBasePreR.LeftFingerBasePreRy
    LeftFingerBasePreRz = LeftFingerBasePreR.LeftFingerBasePreRz

    LeftFingerBasePostR = LeftFingerBasePostRField(default_value=(0.0, 0.0, 0.0))
    LeftFingerBasePostRx = LeftFingerBasePostR.LeftFingerBasePostRx
    LeftFingerBasePostRy = LeftFingerBasePostR.LeftFingerBasePostRy
    LeftFingerBasePostRz = LeftFingerBasePostR.LeftFingerBasePostRz

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

    RightFingerBasePGX = MatrixField()

    RightFingerBaseROrder = RightFingerBaseROrderEnumField(default_value=0)

    RightFingerBaseSC = BoolField(default_value=False)

    RightFingerBaseIS = RightFingerBaseISField(default_value=(1.0, 1.0, 1.0))
    RightFingerBaseISx = RightFingerBaseIS.RightFingerBaseISx
    RightFingerBaseISy = RightFingerBaseIS.RightFingerBaseISy
    RightFingerBaseISz = RightFingerBaseIS.RightFingerBaseISz

    RightFingerBasePreR = RightFingerBasePreRField(default_value=(0.0, 0.0, 0.0))
    RightFingerBasePreRx = RightFingerBasePreR.RightFingerBasePreRx
    RightFingerBasePreRy = RightFingerBasePreR.RightFingerBasePreRy
    RightFingerBasePreRz = RightFingerBasePreR.RightFingerBasePreRz

    RightFingerBasePostR = RightFingerBasePostRField(default_value=(0.0, 0.0, 0.0))
    RightFingerBasePostRx = RightFingerBasePostR.RightFingerBasePostRx
    RightFingerBasePostRy = RightFingerBasePostR.RightFingerBasePostRy
    RightFingerBasePostRz = RightFingerBasePostR.RightFingerBasePostRz

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

    Spine1PGX = MatrixField()

    Spine1ROrder = Spine1ROrderEnumField(default_value=0)

    Spine1SC = BoolField(default_value=False)

    Spine1IS = Spine1ISField(default_value=(1.0, 1.0, 1.0))
    Spine1ISx = Spine1IS.Spine1ISx
    Spine1ISy = Spine1IS.Spine1ISy
    Spine1ISz = Spine1IS.Spine1ISz

    Spine1PreR = Spine1PreRField(default_value=(0.0, 0.0, 0.0))
    Spine1PreRx = Spine1PreR.Spine1PreRx
    Spine1PreRy = Spine1PreR.Spine1PreRy
    Spine1PreRz = Spine1PreR.Spine1PreRz

    Spine1PostR = Spine1PostRField(default_value=(0.0, 0.0, 0.0))
    Spine1PostRx = Spine1PostR.Spine1PostRx
    Spine1PostRy = Spine1PostR.Spine1PostRy
    Spine1PostRz = Spine1PostR.Spine1PostRz

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

    Spine2PGX = MatrixField()

    Spine2ROrder = Spine2ROrderEnumField(default_value=0)

    Spine2SC = BoolField(default_value=False)

    Spine2IS = Spine2ISField(default_value=(1.0, 1.0, 1.0))
    Spine2ISx = Spine2IS.Spine2ISx
    Spine2ISy = Spine2IS.Spine2ISy
    Spine2ISz = Spine2IS.Spine2ISz

    Spine2PreR = Spine2PreRField(default_value=(0.0, 0.0, 0.0))
    Spine2PreRx = Spine2PreR.Spine2PreRx
    Spine2PreRy = Spine2PreR.Spine2PreRy
    Spine2PreRz = Spine2PreR.Spine2PreRz

    Spine2PostR = Spine2PostRField(default_value=(0.0, 0.0, 0.0))
    Spine2PostRx = Spine2PostR.Spine2PostRx
    Spine2PostRy = Spine2PostR.Spine2PostRy
    Spine2PostRz = Spine2PostR.Spine2PostRz

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

    Spine3PGX = MatrixField()

    Spine3ROrder = Spine3ROrderEnumField(default_value=0)

    Spine3SC = BoolField(default_value=False)

    Spine3IS = Spine3ISField(default_value=(1.0, 1.0, 1.0))
    Spine3ISx = Spine3IS.Spine3ISx
    Spine3ISy = Spine3IS.Spine3ISy
    Spine3ISz = Spine3IS.Spine3ISz

    Spine3PreR = Spine3PreRField(default_value=(0.0, 0.0, 0.0))
    Spine3PreRx = Spine3PreR.Spine3PreRx
    Spine3PreRy = Spine3PreR.Spine3PreRy
    Spine3PreRz = Spine3PreR.Spine3PreRz

    Spine3PostR = Spine3PostRField(default_value=(0.0, 0.0, 0.0))
    Spine3PostRx = Spine3PostR.Spine3PostRx
    Spine3PostRy = Spine3PostR.Spine3PostRy
    Spine3PostRz = Spine3PostR.Spine3PostRz

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

    Spine4PGX = MatrixField()

    Spine4ROrder = Spine4ROrderEnumField(default_value=0)

    Spine4SC = BoolField(default_value=False)

    Spine4IS = Spine4ISField(default_value=(1.0, 1.0, 1.0))
    Spine4ISx = Spine4IS.Spine4ISx
    Spine4ISy = Spine4IS.Spine4ISy
    Spine4ISz = Spine4IS.Spine4ISz

    Spine4PreR = Spine4PreRField(default_value=(0.0, 0.0, 0.0))
    Spine4PreRx = Spine4PreR.Spine4PreRx
    Spine4PreRy = Spine4PreR.Spine4PreRy
    Spine4PreRz = Spine4PreR.Spine4PreRz

    Spine4PostR = Spine4PostRField(default_value=(0.0, 0.0, 0.0))
    Spine4PostRx = Spine4PostR.Spine4PostRx
    Spine4PostRy = Spine4PostR.Spine4PostRy
    Spine4PostRz = Spine4PostR.Spine4PostRz

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

    Spine5PGX = MatrixField()

    Spine5ROrder = Spine5ROrderEnumField(default_value=0)

    Spine5SC = BoolField(default_value=False)

    Spine5IS = Spine5ISField(default_value=(1.0, 1.0, 1.0))
    Spine5ISx = Spine5IS.Spine5ISx
    Spine5ISy = Spine5IS.Spine5ISy
    Spine5ISz = Spine5IS.Spine5ISz

    Spine5PreR = Spine5PreRField(default_value=(0.0, 0.0, 0.0))
    Spine5PreRx = Spine5PreR.Spine5PreRx
    Spine5PreRy = Spine5PreR.Spine5PreRy
    Spine5PreRz = Spine5PreR.Spine5PreRz

    Spine5PostR = Spine5PostRField(default_value=(0.0, 0.0, 0.0))
    Spine5PostRx = Spine5PostR.Spine5PostRx
    Spine5PostRy = Spine5PostR.Spine5PostRy
    Spine5PostRz = Spine5PostR.Spine5PostRz

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

    Spine6PGX = MatrixField()

    Spine6ROrder = Spine6ROrderEnumField(default_value=0)

    Spine6SC = BoolField(default_value=False)

    Spine6IS = Spine6ISField(default_value=(1.0, 1.0, 1.0))
    Spine6ISx = Spine6IS.Spine6ISx
    Spine6ISy = Spine6IS.Spine6ISy
    Spine6ISz = Spine6IS.Spine6ISz

    Spine6PreR = Spine6PreRField(default_value=(0.0, 0.0, 0.0))
    Spine6PreRx = Spine6PreR.Spine6PreRx
    Spine6PreRy = Spine6PreR.Spine6PreRy
    Spine6PreRz = Spine6PreR.Spine6PreRz

    Spine6PostR = Spine6PostRField(default_value=(0.0, 0.0, 0.0))
    Spine6PostRx = Spine6PostR.Spine6PostRx
    Spine6PostRy = Spine6PostR.Spine6PostRy
    Spine6PostRz = Spine6PostR.Spine6PostRz

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

    Spine7PGX = MatrixField()

    Spine7ROrder = Spine7ROrderEnumField(default_value=0)

    Spine7SC = BoolField(default_value=False)

    Spine7IS = Spine7ISField(default_value=(1.0, 1.0, 1.0))
    Spine7ISx = Spine7IS.Spine7ISx
    Spine7ISy = Spine7IS.Spine7ISy
    Spine7ISz = Spine7IS.Spine7ISz

    Spine7PreR = Spine7PreRField(default_value=(0.0, 0.0, 0.0))
    Spine7PreRx = Spine7PreR.Spine7PreRx
    Spine7PreRy = Spine7PreR.Spine7PreRy
    Spine7PreRz = Spine7PreR.Spine7PreRz

    Spine7PostR = Spine7PostRField(default_value=(0.0, 0.0, 0.0))
    Spine7PostRx = Spine7PostR.Spine7PostRx
    Spine7PostRy = Spine7PostR.Spine7PostRy
    Spine7PostRz = Spine7PostR.Spine7PostRz

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

    Spine8PGX = MatrixField()

    Spine8ROrder = Spine8ROrderEnumField(default_value=0)

    Spine8SC = BoolField(default_value=False)

    Spine8IS = Spine8ISField(default_value=(1.0, 1.0, 1.0))
    Spine8ISx = Spine8IS.Spine8ISx
    Spine8ISy = Spine8IS.Spine8ISy
    Spine8ISz = Spine8IS.Spine8ISz

    Spine8PreR = Spine8PreRField(default_value=(0.0, 0.0, 0.0))
    Spine8PreRx = Spine8PreR.Spine8PreRx
    Spine8PreRy = Spine8PreR.Spine8PreRy
    Spine8PreRz = Spine8PreR.Spine8PreRz

    Spine8PostR = Spine8PostRField(default_value=(0.0, 0.0, 0.0))
    Spine8PostRx = Spine8PostR.Spine8PostRx
    Spine8PostRy = Spine8PostR.Spine8PostRy
    Spine8PostRz = Spine8PostR.Spine8PostRz

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

    Spine9PGX = MatrixField()

    Spine9ROrder = Spine9ROrderEnumField(default_value=0)

    Spine9SC = BoolField(default_value=False)

    Spine9IS = Spine9ISField(default_value=(1.0, 1.0, 1.0))
    Spine9ISx = Spine9IS.Spine9ISx
    Spine9ISy = Spine9IS.Spine9ISy
    Spine9ISz = Spine9IS.Spine9ISz

    Spine9PreR = Spine9PreRField(default_value=(0.0, 0.0, 0.0))
    Spine9PreRx = Spine9PreR.Spine9PreRx
    Spine9PreRy = Spine9PreR.Spine9PreRy
    Spine9PreRz = Spine9PreR.Spine9PreRz

    Spine9PostR = Spine9PostRField(default_value=(0.0, 0.0, 0.0))
    Spine9PostRx = Spine9PostR.Spine9PostRx
    Spine9PostRy = Spine9PostR.Spine9PostRy
    Spine9PostRz = Spine9PostR.Spine9PostRz

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

    Neck1PGX = MatrixField()

    Neck1ROrder = Neck1ROrderEnumField(default_value=0)

    Neck1SC = BoolField(default_value=False)

    Neck1IS = Neck1ISField(default_value=(1.0, 1.0, 1.0))
    Neck1ISx = Neck1IS.Neck1ISx
    Neck1ISy = Neck1IS.Neck1ISy
    Neck1ISz = Neck1IS.Neck1ISz

    Neck1PreR = Neck1PreRField(default_value=(0.0, 0.0, 0.0))
    Neck1PreRx = Neck1PreR.Neck1PreRx
    Neck1PreRy = Neck1PreR.Neck1PreRy
    Neck1PreRz = Neck1PreR.Neck1PreRz

    Neck1PostR = Neck1PostRField(default_value=(0.0, 0.0, 0.0))
    Neck1PostRx = Neck1PostR.Neck1PostRx
    Neck1PostRy = Neck1PostR.Neck1PostRy
    Neck1PostRz = Neck1PostR.Neck1PostRz

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

    Neck2PGX = MatrixField()

    Neck2ROrder = Neck2ROrderEnumField(default_value=0)

    Neck2SC = BoolField(default_value=False)

    Neck2IS = Neck2ISField(default_value=(1.0, 1.0, 1.0))
    Neck2ISx = Neck2IS.Neck2ISx
    Neck2ISy = Neck2IS.Neck2ISy
    Neck2ISz = Neck2IS.Neck2ISz

    Neck2PreR = Neck2PreRField(default_value=(0.0, 0.0, 0.0))
    Neck2PreRx = Neck2PreR.Neck2PreRx
    Neck2PreRy = Neck2PreR.Neck2PreRy
    Neck2PreRz = Neck2PreR.Neck2PreRz

    Neck2PostR = Neck2PostRField(default_value=(0.0, 0.0, 0.0))
    Neck2PostRx = Neck2PostR.Neck2PostRx
    Neck2PostRy = Neck2PostR.Neck2PostRy
    Neck2PostRz = Neck2PostR.Neck2PostRz

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

    Neck3PGX = MatrixField()

    Neck3ROrder = Neck3ROrderEnumField(default_value=0)

    Neck3SC = BoolField(default_value=False)

    Neck3IS = Neck3ISField(default_value=(1.0, 1.0, 1.0))
    Neck3ISx = Neck3IS.Neck3ISx
    Neck3ISy = Neck3IS.Neck3ISy
    Neck3ISz = Neck3IS.Neck3ISz

    Neck3PreR = Neck3PreRField(default_value=(0.0, 0.0, 0.0))
    Neck3PreRx = Neck3PreR.Neck3PreRx
    Neck3PreRy = Neck3PreR.Neck3PreRy
    Neck3PreRz = Neck3PreR.Neck3PreRz

    Neck3PostR = Neck3PostRField(default_value=(0.0, 0.0, 0.0))
    Neck3PostRx = Neck3PostR.Neck3PostRx
    Neck3PostRy = Neck3PostR.Neck3PostRy
    Neck3PostRz = Neck3PostR.Neck3PostRz

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

    Neck4PGX = MatrixField()

    Neck4ROrder = Neck4ROrderEnumField(default_value=0)

    Neck4SC = BoolField(default_value=False)

    Neck4IS = Neck4ISField(default_value=(1.0, 1.0, 1.0))
    Neck4ISx = Neck4IS.Neck4ISx
    Neck4ISy = Neck4IS.Neck4ISy
    Neck4ISz = Neck4IS.Neck4ISz

    Neck4PreR = Neck4PreRField(default_value=(0.0, 0.0, 0.0))
    Neck4PreRx = Neck4PreR.Neck4PreRx
    Neck4PreRy = Neck4PreR.Neck4PreRy
    Neck4PreRz = Neck4PreR.Neck4PreRz

    Neck4PostR = Neck4PostRField(default_value=(0.0, 0.0, 0.0))
    Neck4PostRx = Neck4PostR.Neck4PostRx
    Neck4PostRy = Neck4PostR.Neck4PostRy
    Neck4PostRz = Neck4PostR.Neck4PostRz

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

    Neck5PGX = MatrixField()

    Neck5ROrder = Neck5ROrderEnumField(default_value=0)

    Neck5SC = BoolField(default_value=False)

    Neck5IS = Neck5ISField(default_value=(1.0, 1.0, 1.0))
    Neck5ISx = Neck5IS.Neck5ISx
    Neck5ISy = Neck5IS.Neck5ISy
    Neck5ISz = Neck5IS.Neck5ISz

    Neck5PreR = Neck5PreRField(default_value=(0.0, 0.0, 0.0))
    Neck5PreRx = Neck5PreR.Neck5PreRx
    Neck5PreRy = Neck5PreR.Neck5PreRy
    Neck5PreRz = Neck5PreR.Neck5PreRz

    Neck5PostR = Neck5PostRField(default_value=(0.0, 0.0, 0.0))
    Neck5PostRx = Neck5PostR.Neck5PostRx
    Neck5PostRy = Neck5PostR.Neck5PostRy
    Neck5PostRz = Neck5PostR.Neck5PostRz

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

    Neck6PGX = MatrixField()

    Neck6ROrder = Neck6ROrderEnumField(default_value=0)

    Neck6SC = BoolField(default_value=False)

    Neck6IS = Neck6ISField(default_value=(1.0, 1.0, 1.0))
    Neck6ISx = Neck6IS.Neck6ISx
    Neck6ISy = Neck6IS.Neck6ISy
    Neck6ISz = Neck6IS.Neck6ISz

    Neck6PreR = Neck6PreRField(default_value=(0.0, 0.0, 0.0))
    Neck6PreRx = Neck6PreR.Neck6PreRx
    Neck6PreRy = Neck6PreR.Neck6PreRy
    Neck6PreRz = Neck6PreR.Neck6PreRz

    Neck6PostR = Neck6PostRField(default_value=(0.0, 0.0, 0.0))
    Neck6PostRx = Neck6PostR.Neck6PostRx
    Neck6PostRy = Neck6PostR.Neck6PostRy
    Neck6PostRz = Neck6PostR.Neck6PostRz

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

    Neck7PGX = MatrixField()

    Neck7ROrder = Neck7ROrderEnumField(default_value=0)

    Neck7SC = BoolField(default_value=False)

    Neck7IS = Neck7ISField(default_value=(1.0, 1.0, 1.0))
    Neck7ISx = Neck7IS.Neck7ISx
    Neck7ISy = Neck7IS.Neck7ISy
    Neck7ISz = Neck7IS.Neck7ISz

    Neck7PreR = Neck7PreRField(default_value=(0.0, 0.0, 0.0))
    Neck7PreRx = Neck7PreR.Neck7PreRx
    Neck7PreRy = Neck7PreR.Neck7PreRy
    Neck7PreRz = Neck7PreR.Neck7PreRz

    Neck7PostR = Neck7PostRField(default_value=(0.0, 0.0, 0.0))
    Neck7PostRx = Neck7PostR.Neck7PostRx
    Neck7PostRy = Neck7PostR.Neck7PostRy
    Neck7PostRz = Neck7PostR.Neck7PostRz

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

    Neck8PGX = MatrixField()

    Neck8ROrder = Neck8ROrderEnumField(default_value=0)

    Neck8SC = BoolField(default_value=False)

    Neck8IS = Neck8ISField(default_value=(1.0, 1.0, 1.0))
    Neck8ISx = Neck8IS.Neck8ISx
    Neck8ISy = Neck8IS.Neck8ISy
    Neck8ISz = Neck8IS.Neck8ISz

    Neck8PreR = Neck8PreRField(default_value=(0.0, 0.0, 0.0))
    Neck8PreRx = Neck8PreR.Neck8PreRx
    Neck8PreRy = Neck8PreR.Neck8PreRy
    Neck8PreRz = Neck8PreR.Neck8PreRz

    Neck8PostR = Neck8PostRField(default_value=(0.0, 0.0, 0.0))
    Neck8PostRx = Neck8PostR.Neck8PostRx
    Neck8PostRy = Neck8PostR.Neck8PostRy
    Neck8PostRz = Neck8PostR.Neck8PostRz

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

    Neck9PGX = MatrixField()

    Neck9ROrder = Neck9ROrderEnumField(default_value=0)

    Neck9SC = BoolField(default_value=False)

    Neck9IS = Neck9ISField(default_value=(1.0, 1.0, 1.0))
    Neck9ISx = Neck9IS.Neck9ISx
    Neck9ISy = Neck9IS.Neck9ISy
    Neck9ISz = Neck9IS.Neck9ISz

    Neck9PreR = Neck9PreRField(default_value=(0.0, 0.0, 0.0))
    Neck9PreRx = Neck9PreR.Neck9PreRx
    Neck9PreRy = Neck9PreR.Neck9PreRy
    Neck9PreRz = Neck9PreR.Neck9PreRz

    Neck9PostR = Neck9PostRField(default_value=(0.0, 0.0, 0.0))
    Neck9PostRx = Neck9PostR.Neck9PostRx
    Neck9PostRy = Neck9PostR.Neck9PostRy
    Neck9PostRz = Neck9PostR.Neck9PostRz

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

    LeftUpLegRollPGX = MatrixField()

    LeftUpLegRollROrder = LeftUpLegRollROrderEnumField(default_value=0)

    LeftUpLegRollSC = BoolField(default_value=False)

    LeftUpLegRollIS = LeftUpLegRollISField(default_value=(1.0, 1.0, 1.0))
    LeftUpLegRollISx = LeftUpLegRollIS.LeftUpLegRollISx
    LeftUpLegRollISy = LeftUpLegRollIS.LeftUpLegRollISy
    LeftUpLegRollISz = LeftUpLegRollIS.LeftUpLegRollISz

    LeftUpLegRollPreR = LeftUpLegRollPreRField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegRollPreRx = LeftUpLegRollPreR.LeftUpLegRollPreRx
    LeftUpLegRollPreRy = LeftUpLegRollPreR.LeftUpLegRollPreRy
    LeftUpLegRollPreRz = LeftUpLegRollPreR.LeftUpLegRollPreRz

    LeftUpLegRollPostR = LeftUpLegRollPostRField(default_value=(0.0, 0.0, 0.0))
    LeftUpLegRollPostRx = LeftUpLegRollPostR.LeftUpLegRollPostRx
    LeftUpLegRollPostRy = LeftUpLegRollPostR.LeftUpLegRollPostRy
    LeftUpLegRollPostRz = LeftUpLegRollPostR.LeftUpLegRollPostRz

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

    LeftLegRollPGX = MatrixField()

    LeftLegRollROrder = LeftLegRollROrderEnumField(default_value=0)

    LeftLegRollSC = BoolField(default_value=False)

    LeftLegRollIS = LeftLegRollISField(default_value=(1.0, 1.0, 1.0))
    LeftLegRollISx = LeftLegRollIS.LeftLegRollISx
    LeftLegRollISy = LeftLegRollIS.LeftLegRollISy
    LeftLegRollISz = LeftLegRollIS.LeftLegRollISz

    LeftLegRollPreR = LeftLegRollPreRField(default_value=(0.0, 0.0, 0.0))
    LeftLegRollPreRx = LeftLegRollPreR.LeftLegRollPreRx
    LeftLegRollPreRy = LeftLegRollPreR.LeftLegRollPreRy
    LeftLegRollPreRz = LeftLegRollPreR.LeftLegRollPreRz

    LeftLegRollPostR = LeftLegRollPostRField(default_value=(0.0, 0.0, 0.0))
    LeftLegRollPostRx = LeftLegRollPostR.LeftLegRollPostRx
    LeftLegRollPostRy = LeftLegRollPostR.LeftLegRollPostRy
    LeftLegRollPostRz = LeftLegRollPostR.LeftLegRollPostRz

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

    RightUpLegRollPGX = MatrixField()

    RightUpLegRollROrder = RightUpLegRollROrderEnumField(default_value=0)

    RightUpLegRollSC = BoolField(default_value=False)

    RightUpLegRollIS = RightUpLegRollISField(default_value=(1.0, 1.0, 1.0))
    RightUpLegRollISx = RightUpLegRollIS.RightUpLegRollISx
    RightUpLegRollISy = RightUpLegRollIS.RightUpLegRollISy
    RightUpLegRollISz = RightUpLegRollIS.RightUpLegRollISz

    RightUpLegRollPreR = RightUpLegRollPreRField(default_value=(0.0, 0.0, 0.0))
    RightUpLegRollPreRx = RightUpLegRollPreR.RightUpLegRollPreRx
    RightUpLegRollPreRy = RightUpLegRollPreR.RightUpLegRollPreRy
    RightUpLegRollPreRz = RightUpLegRollPreR.RightUpLegRollPreRz

    RightUpLegRollPostR = RightUpLegRollPostRField(default_value=(0.0, 0.0, 0.0))
    RightUpLegRollPostRx = RightUpLegRollPostR.RightUpLegRollPostRx
    RightUpLegRollPostRy = RightUpLegRollPostR.RightUpLegRollPostRy
    RightUpLegRollPostRz = RightUpLegRollPostR.RightUpLegRollPostRz

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

    RightLegRollPGX = MatrixField()

    RightLegRollROrder = RightLegRollROrderEnumField(default_value=0)

    RightLegRollSC = BoolField(default_value=False)

    RightLegRollIS = RightLegRollISField(default_value=(1.0, 1.0, 1.0))
    RightLegRollISx = RightLegRollIS.RightLegRollISx
    RightLegRollISy = RightLegRollIS.RightLegRollISy
    RightLegRollISz = RightLegRollIS.RightLegRollISz

    RightLegRollPreR = RightLegRollPreRField(default_value=(0.0, 0.0, 0.0))
    RightLegRollPreRx = RightLegRollPreR.RightLegRollPreRx
    RightLegRollPreRy = RightLegRollPreR.RightLegRollPreRy
    RightLegRollPreRz = RightLegRollPreR.RightLegRollPreRz

    RightLegRollPostR = RightLegRollPostRField(default_value=(0.0, 0.0, 0.0))
    RightLegRollPostRx = RightLegRollPostR.RightLegRollPostRx
    RightLegRollPostRy = RightLegRollPostR.RightLegRollPostRy
    RightLegRollPostRz = RightLegRollPostR.RightLegRollPostRz

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

    LeftArmRollPGX = MatrixField()

    LeftArmRollROrder = LeftArmRollROrderEnumField(default_value=0)

    LeftArmRollSC = BoolField(default_value=False)

    LeftArmRollIS = LeftArmRollISField(default_value=(1.0, 1.0, 1.0))
    LeftArmRollISx = LeftArmRollIS.LeftArmRollISx
    LeftArmRollISy = LeftArmRollIS.LeftArmRollISy
    LeftArmRollISz = LeftArmRollIS.LeftArmRollISz

    LeftArmRollPreR = LeftArmRollPreRField(default_value=(0.0, 0.0, 0.0))
    LeftArmRollPreRx = LeftArmRollPreR.LeftArmRollPreRx
    LeftArmRollPreRy = LeftArmRollPreR.LeftArmRollPreRy
    LeftArmRollPreRz = LeftArmRollPreR.LeftArmRollPreRz

    LeftArmRollPostR = LeftArmRollPostRField(default_value=(0.0, 0.0, 0.0))
    LeftArmRollPostRx = LeftArmRollPostR.LeftArmRollPostRx
    LeftArmRollPostRy = LeftArmRollPostR.LeftArmRollPostRy
    LeftArmRollPostRz = LeftArmRollPostR.LeftArmRollPostRz

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

    LeftForeArmRollPGX = MatrixField()

    LeftForeArmRollROrder = LeftForeArmRollROrderEnumField(default_value=0)

    LeftForeArmRollSC = BoolField(default_value=False)

    LeftForeArmRollIS = LeftForeArmRollISField(default_value=(1.0, 1.0, 1.0))
    LeftForeArmRollISx = LeftForeArmRollIS.LeftForeArmRollISx
    LeftForeArmRollISy = LeftForeArmRollIS.LeftForeArmRollISy
    LeftForeArmRollISz = LeftForeArmRollIS.LeftForeArmRollISz

    LeftForeArmRollPreR = LeftForeArmRollPreRField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmRollPreRx = LeftForeArmRollPreR.LeftForeArmRollPreRx
    LeftForeArmRollPreRy = LeftForeArmRollPreR.LeftForeArmRollPreRy
    LeftForeArmRollPreRz = LeftForeArmRollPreR.LeftForeArmRollPreRz

    LeftForeArmRollPostR = LeftForeArmRollPostRField(default_value=(0.0, 0.0, 0.0))
    LeftForeArmRollPostRx = LeftForeArmRollPostR.LeftForeArmRollPostRx
    LeftForeArmRollPostRy = LeftForeArmRollPostR.LeftForeArmRollPostRy
    LeftForeArmRollPostRz = LeftForeArmRollPostR.LeftForeArmRollPostRz

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

    RightArmRollPGX = MatrixField()

    RightArmRollROrder = RightArmRollROrderEnumField(default_value=0)

    RightArmRollSC = BoolField(default_value=False)

    RightArmRollIS = RightArmRollISField(default_value=(1.0, 1.0, 1.0))
    RightArmRollISx = RightArmRollIS.RightArmRollISx
    RightArmRollISy = RightArmRollIS.RightArmRollISy
    RightArmRollISz = RightArmRollIS.RightArmRollISz

    RightArmRollPreR = RightArmRollPreRField(default_value=(0.0, 0.0, 0.0))
    RightArmRollPreRx = RightArmRollPreR.RightArmRollPreRx
    RightArmRollPreRy = RightArmRollPreR.RightArmRollPreRy
    RightArmRollPreRz = RightArmRollPreR.RightArmRollPreRz

    RightArmRollPostR = RightArmRollPostRField(default_value=(0.0, 0.0, 0.0))
    RightArmRollPostRx = RightArmRollPostR.RightArmRollPostRx
    RightArmRollPostRy = RightArmRollPostR.RightArmRollPostRy
    RightArmRollPostRz = RightArmRollPostR.RightArmRollPostRz

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

    RightForeArmRollPGX = MatrixField()

    RightForeArmRollROrder = RightForeArmRollROrderEnumField(default_value=0)

    RightForeArmRollSC = BoolField(default_value=False)

    RightForeArmRollIS = RightForeArmRollISField(default_value=(1.0, 1.0, 1.0))
    RightForeArmRollISx = RightForeArmRollIS.RightForeArmRollISx
    RightForeArmRollISy = RightForeArmRollIS.RightForeArmRollISy
    RightForeArmRollISz = RightForeArmRollIS.RightForeArmRollISz

    RightForeArmRollPreR = RightForeArmRollPreRField(default_value=(0.0, 0.0, 0.0))
    RightForeArmRollPreRx = RightForeArmRollPreR.RightForeArmRollPreRx
    RightForeArmRollPreRy = RightForeArmRollPreR.RightForeArmRollPreRy
    RightForeArmRollPreRz = RightForeArmRollPreR.RightForeArmRollPreRz

    RightForeArmRollPostR = RightForeArmRollPostRField(default_value=(0.0, 0.0, 0.0))
    RightForeArmRollPostRx = RightForeArmRollPostR.RightForeArmRollPostRx
    RightForeArmRollPostRy = RightForeArmRollPostR.RightForeArmRollPostRy
    RightForeArmRollPostRz = RightForeArmRollPostR.RightForeArmRollPostRz

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

    HipsTranslationPGX = MatrixField()

    HipsTranslationROrder = HipsTranslationROrderEnumField(default_value=0)

    HipsTranslationSC = BoolField(default_value=False)

    HipsTranslationIS = HipsTranslationISField(default_value=(1.0, 1.0, 1.0))
    HipsTranslationISx = HipsTranslationIS.HipsTranslationISx
    HipsTranslationISy = HipsTranslationIS.HipsTranslationISy
    HipsTranslationISz = HipsTranslationIS.HipsTranslationISz

    HipsTranslationPreR = HipsTranslationPreRField(default_value=(0.0, 0.0, 0.0))
    HipsTranslationPreRx = HipsTranslationPreR.HipsTranslationPreRx
    HipsTranslationPreRy = HipsTranslationPreR.HipsTranslationPreRy
    HipsTranslationPreRz = HipsTranslationPreR.HipsTranslationPreRz

    HipsTranslationPostR = HipsTranslationPostRField(default_value=(0.0, 0.0, 0.0))
    HipsTranslationPostRx = HipsTranslationPostR.HipsTranslationPostRx
    HipsTranslationPostRy = HipsTranslationPostR.HipsTranslationPostRy
    HipsTranslationPostRz = HipsTranslationPostR.HipsTranslationPostRz

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

    LeftHandThumb1PGX = MatrixField()

    LeftHandThumb1ROrder = LeftHandThumb1ROrderEnumField(default_value=0)

    LeftHandThumb1SC = BoolField(default_value=False)

    LeftHandThumb1IS = LeftHandThumb1ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandThumb1ISx = LeftHandThumb1IS.LeftHandThumb1ISx
    LeftHandThumb1ISy = LeftHandThumb1IS.LeftHandThumb1ISy
    LeftHandThumb1ISz = LeftHandThumb1IS.LeftHandThumb1ISz

    LeftHandThumb1PreR = LeftHandThumb1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb1PreRx = LeftHandThumb1PreR.LeftHandThumb1PreRx
    LeftHandThumb1PreRy = LeftHandThumb1PreR.LeftHandThumb1PreRy
    LeftHandThumb1PreRz = LeftHandThumb1PreR.LeftHandThumb1PreRz

    LeftHandThumb1PostR = LeftHandThumb1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb1PostRx = LeftHandThumb1PostR.LeftHandThumb1PostRx
    LeftHandThumb1PostRy = LeftHandThumb1PostR.LeftHandThumb1PostRy
    LeftHandThumb1PostRz = LeftHandThumb1PostR.LeftHandThumb1PostRz

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

    LeftHandThumb2PGX = MatrixField()

    LeftHandThumb2ROrder = LeftHandThumb2ROrderEnumField(default_value=0)

    LeftHandThumb2SC = BoolField(default_value=False)

    LeftHandThumb2IS = LeftHandThumb2ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandThumb2ISx = LeftHandThumb2IS.LeftHandThumb2ISx
    LeftHandThumb2ISy = LeftHandThumb2IS.LeftHandThumb2ISy
    LeftHandThumb2ISz = LeftHandThumb2IS.LeftHandThumb2ISz

    LeftHandThumb2PreR = LeftHandThumb2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb2PreRx = LeftHandThumb2PreR.LeftHandThumb2PreRx
    LeftHandThumb2PreRy = LeftHandThumb2PreR.LeftHandThumb2PreRy
    LeftHandThumb2PreRz = LeftHandThumb2PreR.LeftHandThumb2PreRz

    LeftHandThumb2PostR = LeftHandThumb2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb2PostRx = LeftHandThumb2PostR.LeftHandThumb2PostRx
    LeftHandThumb2PostRy = LeftHandThumb2PostR.LeftHandThumb2PostRy
    LeftHandThumb2PostRz = LeftHandThumb2PostR.LeftHandThumb2PostRz

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

    LeftHandThumb3PGX = MatrixField()

    LeftHandThumb3ROrder = LeftHandThumb3ROrderEnumField(default_value=0)

    LeftHandThumb3SC = BoolField(default_value=False)

    LeftHandThumb3IS = LeftHandThumb3ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandThumb3ISx = LeftHandThumb3IS.LeftHandThumb3ISx
    LeftHandThumb3ISy = LeftHandThumb3IS.LeftHandThumb3ISy
    LeftHandThumb3ISz = LeftHandThumb3IS.LeftHandThumb3ISz

    LeftHandThumb3PreR = LeftHandThumb3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb3PreRx = LeftHandThumb3PreR.LeftHandThumb3PreRx
    LeftHandThumb3PreRy = LeftHandThumb3PreR.LeftHandThumb3PreRy
    LeftHandThumb3PreRz = LeftHandThumb3PreR.LeftHandThumb3PreRz

    LeftHandThumb3PostR = LeftHandThumb3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb3PostRx = LeftHandThumb3PostR.LeftHandThumb3PostRx
    LeftHandThumb3PostRy = LeftHandThumb3PostR.LeftHandThumb3PostRy
    LeftHandThumb3PostRz = LeftHandThumb3PostR.LeftHandThumb3PostRz

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

    LeftHandThumb4PGX = MatrixField()

    LeftHandThumb4ROrder = LeftHandThumb4ROrderEnumField(default_value=0)

    LeftHandThumb4SC = BoolField(default_value=False)

    LeftHandThumb4IS = LeftHandThumb4ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandThumb4ISx = LeftHandThumb4IS.LeftHandThumb4ISx
    LeftHandThumb4ISy = LeftHandThumb4IS.LeftHandThumb4ISy
    LeftHandThumb4ISz = LeftHandThumb4IS.LeftHandThumb4ISz

    LeftHandThumb4PreR = LeftHandThumb4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb4PreRx = LeftHandThumb4PreR.LeftHandThumb4PreRx
    LeftHandThumb4PreRy = LeftHandThumb4PreR.LeftHandThumb4PreRy
    LeftHandThumb4PreRz = LeftHandThumb4PreR.LeftHandThumb4PreRz

    LeftHandThumb4PostR = LeftHandThumb4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandThumb4PostRx = LeftHandThumb4PostR.LeftHandThumb4PostRx
    LeftHandThumb4PostRy = LeftHandThumb4PostR.LeftHandThumb4PostRy
    LeftHandThumb4PostRz = LeftHandThumb4PostR.LeftHandThumb4PostRz

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

    LeftHandIndex1PGX = MatrixField()

    LeftHandIndex1ROrder = LeftHandIndex1ROrderEnumField(default_value=0)

    LeftHandIndex1SC = BoolField(default_value=False)

    LeftHandIndex1IS = LeftHandIndex1ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandIndex1ISx = LeftHandIndex1IS.LeftHandIndex1ISx
    LeftHandIndex1ISy = LeftHandIndex1IS.LeftHandIndex1ISy
    LeftHandIndex1ISz = LeftHandIndex1IS.LeftHandIndex1ISz

    LeftHandIndex1PreR = LeftHandIndex1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex1PreRx = LeftHandIndex1PreR.LeftHandIndex1PreRx
    LeftHandIndex1PreRy = LeftHandIndex1PreR.LeftHandIndex1PreRy
    LeftHandIndex1PreRz = LeftHandIndex1PreR.LeftHandIndex1PreRz

    LeftHandIndex1PostR = LeftHandIndex1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex1PostRx = LeftHandIndex1PostR.LeftHandIndex1PostRx
    LeftHandIndex1PostRy = LeftHandIndex1PostR.LeftHandIndex1PostRy
    LeftHandIndex1PostRz = LeftHandIndex1PostR.LeftHandIndex1PostRz

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

    LeftHandIndex2PGX = MatrixField()

    LeftHandIndex2ROrder = LeftHandIndex2ROrderEnumField(default_value=0)

    LeftHandIndex2SC = BoolField(default_value=False)

    LeftHandIndex2IS = LeftHandIndex2ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandIndex2ISx = LeftHandIndex2IS.LeftHandIndex2ISx
    LeftHandIndex2ISy = LeftHandIndex2IS.LeftHandIndex2ISy
    LeftHandIndex2ISz = LeftHandIndex2IS.LeftHandIndex2ISz

    LeftHandIndex2PreR = LeftHandIndex2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex2PreRx = LeftHandIndex2PreR.LeftHandIndex2PreRx
    LeftHandIndex2PreRy = LeftHandIndex2PreR.LeftHandIndex2PreRy
    LeftHandIndex2PreRz = LeftHandIndex2PreR.LeftHandIndex2PreRz

    LeftHandIndex2PostR = LeftHandIndex2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex2PostRx = LeftHandIndex2PostR.LeftHandIndex2PostRx
    LeftHandIndex2PostRy = LeftHandIndex2PostR.LeftHandIndex2PostRy
    LeftHandIndex2PostRz = LeftHandIndex2PostR.LeftHandIndex2PostRz

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

    LeftHandIndex3PGX = MatrixField()

    LeftHandIndex3ROrder = LeftHandIndex3ROrderEnumField(default_value=0)

    LeftHandIndex3SC = BoolField(default_value=False)

    LeftHandIndex3IS = LeftHandIndex3ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandIndex3ISx = LeftHandIndex3IS.LeftHandIndex3ISx
    LeftHandIndex3ISy = LeftHandIndex3IS.LeftHandIndex3ISy
    LeftHandIndex3ISz = LeftHandIndex3IS.LeftHandIndex3ISz

    LeftHandIndex3PreR = LeftHandIndex3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex3PreRx = LeftHandIndex3PreR.LeftHandIndex3PreRx
    LeftHandIndex3PreRy = LeftHandIndex3PreR.LeftHandIndex3PreRy
    LeftHandIndex3PreRz = LeftHandIndex3PreR.LeftHandIndex3PreRz

    LeftHandIndex3PostR = LeftHandIndex3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex3PostRx = LeftHandIndex3PostR.LeftHandIndex3PostRx
    LeftHandIndex3PostRy = LeftHandIndex3PostR.LeftHandIndex3PostRy
    LeftHandIndex3PostRz = LeftHandIndex3PostR.LeftHandIndex3PostRz

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

    LeftHandIndex4PGX = MatrixField()

    LeftHandIndex4ROrder = LeftHandIndex4ROrderEnumField(default_value=0)

    LeftHandIndex4SC = BoolField(default_value=False)

    LeftHandIndex4IS = LeftHandIndex4ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandIndex4ISx = LeftHandIndex4IS.LeftHandIndex4ISx
    LeftHandIndex4ISy = LeftHandIndex4IS.LeftHandIndex4ISy
    LeftHandIndex4ISz = LeftHandIndex4IS.LeftHandIndex4ISz

    LeftHandIndex4PreR = LeftHandIndex4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex4PreRx = LeftHandIndex4PreR.LeftHandIndex4PreRx
    LeftHandIndex4PreRy = LeftHandIndex4PreR.LeftHandIndex4PreRy
    LeftHandIndex4PreRz = LeftHandIndex4PreR.LeftHandIndex4PreRz

    LeftHandIndex4PostR = LeftHandIndex4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandIndex4PostRx = LeftHandIndex4PostR.LeftHandIndex4PostRx
    LeftHandIndex4PostRy = LeftHandIndex4PostR.LeftHandIndex4PostRy
    LeftHandIndex4PostRz = LeftHandIndex4PostR.LeftHandIndex4PostRz

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

    LeftHandMiddle1PGX = MatrixField()

    LeftHandMiddle1ROrder = LeftHandMiddle1ROrderEnumField(default_value=0)

    LeftHandMiddle1SC = BoolField(default_value=False)

    LeftHandMiddle1IS = LeftHandMiddle1ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandMiddle1ISx = LeftHandMiddle1IS.LeftHandMiddle1ISx
    LeftHandMiddle1ISy = LeftHandMiddle1IS.LeftHandMiddle1ISy
    LeftHandMiddle1ISz = LeftHandMiddle1IS.LeftHandMiddle1ISz

    LeftHandMiddle1PreR = LeftHandMiddle1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle1PreRx = LeftHandMiddle1PreR.LeftHandMiddle1PreRx
    LeftHandMiddle1PreRy = LeftHandMiddle1PreR.LeftHandMiddle1PreRy
    LeftHandMiddle1PreRz = LeftHandMiddle1PreR.LeftHandMiddle1PreRz

    LeftHandMiddle1PostR = LeftHandMiddle1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle1PostRx = LeftHandMiddle1PostR.LeftHandMiddle1PostRx
    LeftHandMiddle1PostRy = LeftHandMiddle1PostR.LeftHandMiddle1PostRy
    LeftHandMiddle1PostRz = LeftHandMiddle1PostR.LeftHandMiddle1PostRz

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

    LeftHandMiddle2PGX = MatrixField()

    LeftHandMiddle2ROrder = LeftHandMiddle2ROrderEnumField(default_value=0)

    LeftHandMiddle2SC = BoolField(default_value=False)

    LeftHandMiddle2IS = LeftHandMiddle2ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandMiddle2ISx = LeftHandMiddle2IS.LeftHandMiddle2ISx
    LeftHandMiddle2ISy = LeftHandMiddle2IS.LeftHandMiddle2ISy
    LeftHandMiddle2ISz = LeftHandMiddle2IS.LeftHandMiddle2ISz

    LeftHandMiddle2PreR = LeftHandMiddle2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle2PreRx = LeftHandMiddle2PreR.LeftHandMiddle2PreRx
    LeftHandMiddle2PreRy = LeftHandMiddle2PreR.LeftHandMiddle2PreRy
    LeftHandMiddle2PreRz = LeftHandMiddle2PreR.LeftHandMiddle2PreRz

    LeftHandMiddle2PostR = LeftHandMiddle2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle2PostRx = LeftHandMiddle2PostR.LeftHandMiddle2PostRx
    LeftHandMiddle2PostRy = LeftHandMiddle2PostR.LeftHandMiddle2PostRy
    LeftHandMiddle2PostRz = LeftHandMiddle2PostR.LeftHandMiddle2PostRz

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

    LeftHandMiddle3PGX = MatrixField()

    LeftHandMiddle3ROrder = LeftHandMiddle3ROrderEnumField(default_value=0)

    LeftHandMiddle3SC = BoolField(default_value=False)

    LeftHandMiddle3IS = LeftHandMiddle3ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandMiddle3ISx = LeftHandMiddle3IS.LeftHandMiddle3ISx
    LeftHandMiddle3ISy = LeftHandMiddle3IS.LeftHandMiddle3ISy
    LeftHandMiddle3ISz = LeftHandMiddle3IS.LeftHandMiddle3ISz

    LeftHandMiddle3PreR = LeftHandMiddle3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle3PreRx = LeftHandMiddle3PreR.LeftHandMiddle3PreRx
    LeftHandMiddle3PreRy = LeftHandMiddle3PreR.LeftHandMiddle3PreRy
    LeftHandMiddle3PreRz = LeftHandMiddle3PreR.LeftHandMiddle3PreRz

    LeftHandMiddle3PostR = LeftHandMiddle3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle3PostRx = LeftHandMiddle3PostR.LeftHandMiddle3PostRx
    LeftHandMiddle3PostRy = LeftHandMiddle3PostR.LeftHandMiddle3PostRy
    LeftHandMiddle3PostRz = LeftHandMiddle3PostR.LeftHandMiddle3PostRz

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

    LeftHandMiddle4PGX = MatrixField()

    LeftHandMiddle4ROrder = LeftHandMiddle4ROrderEnumField(default_value=0)

    LeftHandMiddle4SC = BoolField(default_value=False)

    LeftHandMiddle4IS = LeftHandMiddle4ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandMiddle4ISx = LeftHandMiddle4IS.LeftHandMiddle4ISx
    LeftHandMiddle4ISy = LeftHandMiddle4IS.LeftHandMiddle4ISy
    LeftHandMiddle4ISz = LeftHandMiddle4IS.LeftHandMiddle4ISz

    LeftHandMiddle4PreR = LeftHandMiddle4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle4PreRx = LeftHandMiddle4PreR.LeftHandMiddle4PreRx
    LeftHandMiddle4PreRy = LeftHandMiddle4PreR.LeftHandMiddle4PreRy
    LeftHandMiddle4PreRz = LeftHandMiddle4PreR.LeftHandMiddle4PreRz

    LeftHandMiddle4PostR = LeftHandMiddle4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandMiddle4PostRx = LeftHandMiddle4PostR.LeftHandMiddle4PostRx
    LeftHandMiddle4PostRy = LeftHandMiddle4PostR.LeftHandMiddle4PostRy
    LeftHandMiddle4PostRz = LeftHandMiddle4PostR.LeftHandMiddle4PostRz

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

    LeftHandRing1PGX = MatrixField()

    LeftHandRing1ROrder = LeftHandRing1ROrderEnumField(default_value=0)

    LeftHandRing1SC = BoolField(default_value=False)

    LeftHandRing1IS = LeftHandRing1ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandRing1ISx = LeftHandRing1IS.LeftHandRing1ISx
    LeftHandRing1ISy = LeftHandRing1IS.LeftHandRing1ISy
    LeftHandRing1ISz = LeftHandRing1IS.LeftHandRing1ISz

    LeftHandRing1PreR = LeftHandRing1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing1PreRx = LeftHandRing1PreR.LeftHandRing1PreRx
    LeftHandRing1PreRy = LeftHandRing1PreR.LeftHandRing1PreRy
    LeftHandRing1PreRz = LeftHandRing1PreR.LeftHandRing1PreRz

    LeftHandRing1PostR = LeftHandRing1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing1PostRx = LeftHandRing1PostR.LeftHandRing1PostRx
    LeftHandRing1PostRy = LeftHandRing1PostR.LeftHandRing1PostRy
    LeftHandRing1PostRz = LeftHandRing1PostR.LeftHandRing1PostRz

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

    LeftHandRing2PGX = MatrixField()

    LeftHandRing2ROrder = LeftHandRing2ROrderEnumField(default_value=0)

    LeftHandRing2SC = BoolField(default_value=False)

    LeftHandRing2IS = LeftHandRing2ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandRing2ISx = LeftHandRing2IS.LeftHandRing2ISx
    LeftHandRing2ISy = LeftHandRing2IS.LeftHandRing2ISy
    LeftHandRing2ISz = LeftHandRing2IS.LeftHandRing2ISz

    LeftHandRing2PreR = LeftHandRing2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing2PreRx = LeftHandRing2PreR.LeftHandRing2PreRx
    LeftHandRing2PreRy = LeftHandRing2PreR.LeftHandRing2PreRy
    LeftHandRing2PreRz = LeftHandRing2PreR.LeftHandRing2PreRz

    LeftHandRing2PostR = LeftHandRing2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing2PostRx = LeftHandRing2PostR.LeftHandRing2PostRx
    LeftHandRing2PostRy = LeftHandRing2PostR.LeftHandRing2PostRy
    LeftHandRing2PostRz = LeftHandRing2PostR.LeftHandRing2PostRz

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

    LeftHandRing3PGX = MatrixField()

    LeftHandRing3ROrder = LeftHandRing3ROrderEnumField(default_value=0)

    LeftHandRing3SC = BoolField(default_value=False)

    LeftHandRing3IS = LeftHandRing3ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandRing3ISx = LeftHandRing3IS.LeftHandRing3ISx
    LeftHandRing3ISy = LeftHandRing3IS.LeftHandRing3ISy
    LeftHandRing3ISz = LeftHandRing3IS.LeftHandRing3ISz

    LeftHandRing3PreR = LeftHandRing3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing3PreRx = LeftHandRing3PreR.LeftHandRing3PreRx
    LeftHandRing3PreRy = LeftHandRing3PreR.LeftHandRing3PreRy
    LeftHandRing3PreRz = LeftHandRing3PreR.LeftHandRing3PreRz

    LeftHandRing3PostR = LeftHandRing3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing3PostRx = LeftHandRing3PostR.LeftHandRing3PostRx
    LeftHandRing3PostRy = LeftHandRing3PostR.LeftHandRing3PostRy
    LeftHandRing3PostRz = LeftHandRing3PostR.LeftHandRing3PostRz

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

    LeftHandRing4PGX = MatrixField()

    LeftHandRing4ROrder = LeftHandRing4ROrderEnumField(default_value=0)

    LeftHandRing4SC = BoolField(default_value=False)

    LeftHandRing4IS = LeftHandRing4ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandRing4ISx = LeftHandRing4IS.LeftHandRing4ISx
    LeftHandRing4ISy = LeftHandRing4IS.LeftHandRing4ISy
    LeftHandRing4ISz = LeftHandRing4IS.LeftHandRing4ISz

    LeftHandRing4PreR = LeftHandRing4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing4PreRx = LeftHandRing4PreR.LeftHandRing4PreRx
    LeftHandRing4PreRy = LeftHandRing4PreR.LeftHandRing4PreRy
    LeftHandRing4PreRz = LeftHandRing4PreR.LeftHandRing4PreRz

    LeftHandRing4PostR = LeftHandRing4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandRing4PostRx = LeftHandRing4PostR.LeftHandRing4PostRx
    LeftHandRing4PostRy = LeftHandRing4PostR.LeftHandRing4PostRy
    LeftHandRing4PostRz = LeftHandRing4PostR.LeftHandRing4PostRz

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

    LeftHandPinky1PGX = MatrixField()

    LeftHandPinky1ROrder = LeftHandPinky1ROrderEnumField(default_value=0)

    LeftHandPinky1SC = BoolField(default_value=False)

    LeftHandPinky1IS = LeftHandPinky1ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandPinky1ISx = LeftHandPinky1IS.LeftHandPinky1ISx
    LeftHandPinky1ISy = LeftHandPinky1IS.LeftHandPinky1ISy
    LeftHandPinky1ISz = LeftHandPinky1IS.LeftHandPinky1ISz

    LeftHandPinky1PreR = LeftHandPinky1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky1PreRx = LeftHandPinky1PreR.LeftHandPinky1PreRx
    LeftHandPinky1PreRy = LeftHandPinky1PreR.LeftHandPinky1PreRy
    LeftHandPinky1PreRz = LeftHandPinky1PreR.LeftHandPinky1PreRz

    LeftHandPinky1PostR = LeftHandPinky1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky1PostRx = LeftHandPinky1PostR.LeftHandPinky1PostRx
    LeftHandPinky1PostRy = LeftHandPinky1PostR.LeftHandPinky1PostRy
    LeftHandPinky1PostRz = LeftHandPinky1PostR.LeftHandPinky1PostRz

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

    LeftHandPinky2PGX = MatrixField()

    LeftHandPinky2ROrder = LeftHandPinky2ROrderEnumField(default_value=0)

    LeftHandPinky2SC = BoolField(default_value=False)

    LeftHandPinky2IS = LeftHandPinky2ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandPinky2ISx = LeftHandPinky2IS.LeftHandPinky2ISx
    LeftHandPinky2ISy = LeftHandPinky2IS.LeftHandPinky2ISy
    LeftHandPinky2ISz = LeftHandPinky2IS.LeftHandPinky2ISz

    LeftHandPinky2PreR = LeftHandPinky2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky2PreRx = LeftHandPinky2PreR.LeftHandPinky2PreRx
    LeftHandPinky2PreRy = LeftHandPinky2PreR.LeftHandPinky2PreRy
    LeftHandPinky2PreRz = LeftHandPinky2PreR.LeftHandPinky2PreRz

    LeftHandPinky2PostR = LeftHandPinky2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky2PostRx = LeftHandPinky2PostR.LeftHandPinky2PostRx
    LeftHandPinky2PostRy = LeftHandPinky2PostR.LeftHandPinky2PostRy
    LeftHandPinky2PostRz = LeftHandPinky2PostR.LeftHandPinky2PostRz

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

    LeftHandPinky3PGX = MatrixField()

    LeftHandPinky3ROrder = LeftHandPinky3ROrderEnumField(default_value=0)

    LeftHandPinky3SC = BoolField(default_value=False)

    LeftHandPinky3IS = LeftHandPinky3ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandPinky3ISx = LeftHandPinky3IS.LeftHandPinky3ISx
    LeftHandPinky3ISy = LeftHandPinky3IS.LeftHandPinky3ISy
    LeftHandPinky3ISz = LeftHandPinky3IS.LeftHandPinky3ISz

    LeftHandPinky3PreR = LeftHandPinky3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky3PreRx = LeftHandPinky3PreR.LeftHandPinky3PreRx
    LeftHandPinky3PreRy = LeftHandPinky3PreR.LeftHandPinky3PreRy
    LeftHandPinky3PreRz = LeftHandPinky3PreR.LeftHandPinky3PreRz

    LeftHandPinky3PostR = LeftHandPinky3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky3PostRx = LeftHandPinky3PostR.LeftHandPinky3PostRx
    LeftHandPinky3PostRy = LeftHandPinky3PostR.LeftHandPinky3PostRy
    LeftHandPinky3PostRz = LeftHandPinky3PostR.LeftHandPinky3PostRz

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

    LeftHandPinky4PGX = MatrixField()

    LeftHandPinky4ROrder = LeftHandPinky4ROrderEnumField(default_value=0)

    LeftHandPinky4SC = BoolField(default_value=False)

    LeftHandPinky4IS = LeftHandPinky4ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandPinky4ISx = LeftHandPinky4IS.LeftHandPinky4ISx
    LeftHandPinky4ISy = LeftHandPinky4IS.LeftHandPinky4ISy
    LeftHandPinky4ISz = LeftHandPinky4IS.LeftHandPinky4ISz

    LeftHandPinky4PreR = LeftHandPinky4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky4PreRx = LeftHandPinky4PreR.LeftHandPinky4PreRx
    LeftHandPinky4PreRy = LeftHandPinky4PreR.LeftHandPinky4PreRy
    LeftHandPinky4PreRz = LeftHandPinky4PreR.LeftHandPinky4PreRz

    LeftHandPinky4PostR = LeftHandPinky4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandPinky4PostRx = LeftHandPinky4PostR.LeftHandPinky4PostRx
    LeftHandPinky4PostRy = LeftHandPinky4PostR.LeftHandPinky4PostRy
    LeftHandPinky4PostRz = LeftHandPinky4PostR.LeftHandPinky4PostRz

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

    LeftHandExtraFinger1PGX = MatrixField()

    LeftHandExtraFinger1ROrder = LeftHandExtraFinger1ROrderEnumField(default_value=0)

    LeftHandExtraFinger1SC = BoolField(default_value=False)

    LeftHandExtraFinger1IS = LeftHandExtraFinger1ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandExtraFinger1ISx = LeftHandExtraFinger1IS.LeftHandExtraFinger1ISx
    LeftHandExtraFinger1ISy = LeftHandExtraFinger1IS.LeftHandExtraFinger1ISy
    LeftHandExtraFinger1ISz = LeftHandExtraFinger1IS.LeftHandExtraFinger1ISz

    LeftHandExtraFinger1PreR = LeftHandExtraFinger1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger1PreRx = LeftHandExtraFinger1PreR.LeftHandExtraFinger1PreRx
    LeftHandExtraFinger1PreRy = LeftHandExtraFinger1PreR.LeftHandExtraFinger1PreRy
    LeftHandExtraFinger1PreRz = LeftHandExtraFinger1PreR.LeftHandExtraFinger1PreRz

    LeftHandExtraFinger1PostR = LeftHandExtraFinger1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger1PostRx = LeftHandExtraFinger1PostR.LeftHandExtraFinger1PostRx
    LeftHandExtraFinger1PostRy = LeftHandExtraFinger1PostR.LeftHandExtraFinger1PostRy
    LeftHandExtraFinger1PostRz = LeftHandExtraFinger1PostR.LeftHandExtraFinger1PostRz

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

    LeftHandExtraFinger2PGX = MatrixField()

    LeftHandExtraFinger2ROrder = LeftHandExtraFinger2ROrderEnumField(default_value=0)

    LeftHandExtraFinger2SC = BoolField(default_value=False)

    LeftHandExtraFinger2IS = LeftHandExtraFinger2ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandExtraFinger2ISx = LeftHandExtraFinger2IS.LeftHandExtraFinger2ISx
    LeftHandExtraFinger2ISy = LeftHandExtraFinger2IS.LeftHandExtraFinger2ISy
    LeftHandExtraFinger2ISz = LeftHandExtraFinger2IS.LeftHandExtraFinger2ISz

    LeftHandExtraFinger2PreR = LeftHandExtraFinger2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger2PreRx = LeftHandExtraFinger2PreR.LeftHandExtraFinger2PreRx
    LeftHandExtraFinger2PreRy = LeftHandExtraFinger2PreR.LeftHandExtraFinger2PreRy
    LeftHandExtraFinger2PreRz = LeftHandExtraFinger2PreR.LeftHandExtraFinger2PreRz

    LeftHandExtraFinger2PostR = LeftHandExtraFinger2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger2PostRx = LeftHandExtraFinger2PostR.LeftHandExtraFinger2PostRx
    LeftHandExtraFinger2PostRy = LeftHandExtraFinger2PostR.LeftHandExtraFinger2PostRy
    LeftHandExtraFinger2PostRz = LeftHandExtraFinger2PostR.LeftHandExtraFinger2PostRz

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

    LeftHandExtraFinger3PGX = MatrixField()

    LeftHandExtraFinger3ROrder = LeftHandExtraFinger3ROrderEnumField(default_value=0)

    LeftHandExtraFinger3SC = BoolField(default_value=False)

    LeftHandExtraFinger3IS = LeftHandExtraFinger3ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandExtraFinger3ISx = LeftHandExtraFinger3IS.LeftHandExtraFinger3ISx
    LeftHandExtraFinger3ISy = LeftHandExtraFinger3IS.LeftHandExtraFinger3ISy
    LeftHandExtraFinger3ISz = LeftHandExtraFinger3IS.LeftHandExtraFinger3ISz

    LeftHandExtraFinger3PreR = LeftHandExtraFinger3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger3PreRx = LeftHandExtraFinger3PreR.LeftHandExtraFinger3PreRx
    LeftHandExtraFinger3PreRy = LeftHandExtraFinger3PreR.LeftHandExtraFinger3PreRy
    LeftHandExtraFinger3PreRz = LeftHandExtraFinger3PreR.LeftHandExtraFinger3PreRz

    LeftHandExtraFinger3PostR = LeftHandExtraFinger3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger3PostRx = LeftHandExtraFinger3PostR.LeftHandExtraFinger3PostRx
    LeftHandExtraFinger3PostRy = LeftHandExtraFinger3PostR.LeftHandExtraFinger3PostRy
    LeftHandExtraFinger3PostRz = LeftHandExtraFinger3PostR.LeftHandExtraFinger3PostRz

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

    LeftHandExtraFinger4PGX = MatrixField()

    LeftHandExtraFinger4ROrder = LeftHandExtraFinger4ROrderEnumField(default_value=0)

    LeftHandExtraFinger4SC = BoolField(default_value=False)

    LeftHandExtraFinger4IS = LeftHandExtraFinger4ISField(default_value=(1.0, 1.0, 1.0))
    LeftHandExtraFinger4ISx = LeftHandExtraFinger4IS.LeftHandExtraFinger4ISx
    LeftHandExtraFinger4ISy = LeftHandExtraFinger4IS.LeftHandExtraFinger4ISy
    LeftHandExtraFinger4ISz = LeftHandExtraFinger4IS.LeftHandExtraFinger4ISz

    LeftHandExtraFinger4PreR = LeftHandExtraFinger4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger4PreRx = LeftHandExtraFinger4PreR.LeftHandExtraFinger4PreRx
    LeftHandExtraFinger4PreRy = LeftHandExtraFinger4PreR.LeftHandExtraFinger4PreRy
    LeftHandExtraFinger4PreRz = LeftHandExtraFinger4PreR.LeftHandExtraFinger4PreRz

    LeftHandExtraFinger4PostR = LeftHandExtraFinger4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftHandExtraFinger4PostRx = LeftHandExtraFinger4PostR.LeftHandExtraFinger4PostRx
    LeftHandExtraFinger4PostRy = LeftHandExtraFinger4PostR.LeftHandExtraFinger4PostRy
    LeftHandExtraFinger4PostRz = LeftHandExtraFinger4PostR.LeftHandExtraFinger4PostRz

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

    RightHandThumb1PGX = MatrixField()

    RightHandThumb1ROrder = RightHandThumb1ROrderEnumField(default_value=0)

    RightHandThumb1SC = BoolField(default_value=False)

    RightHandThumb1IS = RightHandThumb1ISField(default_value=(1.0, 1.0, 1.0))
    RightHandThumb1ISx = RightHandThumb1IS.RightHandThumb1ISx
    RightHandThumb1ISy = RightHandThumb1IS.RightHandThumb1ISy
    RightHandThumb1ISz = RightHandThumb1IS.RightHandThumb1ISz

    RightHandThumb1PreR = RightHandThumb1PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb1PreRx = RightHandThumb1PreR.RightHandThumb1PreRx
    RightHandThumb1PreRy = RightHandThumb1PreR.RightHandThumb1PreRy
    RightHandThumb1PreRz = RightHandThumb1PreR.RightHandThumb1PreRz

    RightHandThumb1PostR = RightHandThumb1PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb1PostRx = RightHandThumb1PostR.RightHandThumb1PostRx
    RightHandThumb1PostRy = RightHandThumb1PostR.RightHandThumb1PostRy
    RightHandThumb1PostRz = RightHandThumb1PostR.RightHandThumb1PostRz

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

    RightHandThumb2PGX = MatrixField()

    RightHandThumb2ROrder = RightHandThumb2ROrderEnumField(default_value=0)

    RightHandThumb2SC = BoolField(default_value=False)

    RightHandThumb2IS = RightHandThumb2ISField(default_value=(1.0, 1.0, 1.0))
    RightHandThumb2ISx = RightHandThumb2IS.RightHandThumb2ISx
    RightHandThumb2ISy = RightHandThumb2IS.RightHandThumb2ISy
    RightHandThumb2ISz = RightHandThumb2IS.RightHandThumb2ISz

    RightHandThumb2PreR = RightHandThumb2PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb2PreRx = RightHandThumb2PreR.RightHandThumb2PreRx
    RightHandThumb2PreRy = RightHandThumb2PreR.RightHandThumb2PreRy
    RightHandThumb2PreRz = RightHandThumb2PreR.RightHandThumb2PreRz

    RightHandThumb2PostR = RightHandThumb2PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb2PostRx = RightHandThumb2PostR.RightHandThumb2PostRx
    RightHandThumb2PostRy = RightHandThumb2PostR.RightHandThumb2PostRy
    RightHandThumb2PostRz = RightHandThumb2PostR.RightHandThumb2PostRz

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

    RightHandThumb3PGX = MatrixField()

    RightHandThumb3ROrder = RightHandThumb3ROrderEnumField(default_value=0)

    RightHandThumb3SC = BoolField(default_value=False)

    RightHandThumb3IS = RightHandThumb3ISField(default_value=(1.0, 1.0, 1.0))
    RightHandThumb3ISx = RightHandThumb3IS.RightHandThumb3ISx
    RightHandThumb3ISy = RightHandThumb3IS.RightHandThumb3ISy
    RightHandThumb3ISz = RightHandThumb3IS.RightHandThumb3ISz

    RightHandThumb3PreR = RightHandThumb3PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb3PreRx = RightHandThumb3PreR.RightHandThumb3PreRx
    RightHandThumb3PreRy = RightHandThumb3PreR.RightHandThumb3PreRy
    RightHandThumb3PreRz = RightHandThumb3PreR.RightHandThumb3PreRz

    RightHandThumb3PostR = RightHandThumb3PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb3PostRx = RightHandThumb3PostR.RightHandThumb3PostRx
    RightHandThumb3PostRy = RightHandThumb3PostR.RightHandThumb3PostRy
    RightHandThumb3PostRz = RightHandThumb3PostR.RightHandThumb3PostRz

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

    RightHandThumb4PGX = MatrixField()

    RightHandThumb4ROrder = RightHandThumb4ROrderEnumField(default_value=0)

    RightHandThumb4SC = BoolField(default_value=False)

    RightHandThumb4IS = RightHandThumb4ISField(default_value=(1.0, 1.0, 1.0))
    RightHandThumb4ISx = RightHandThumb4IS.RightHandThumb4ISx
    RightHandThumb4ISy = RightHandThumb4IS.RightHandThumb4ISy
    RightHandThumb4ISz = RightHandThumb4IS.RightHandThumb4ISz

    RightHandThumb4PreR = RightHandThumb4PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb4PreRx = RightHandThumb4PreR.RightHandThumb4PreRx
    RightHandThumb4PreRy = RightHandThumb4PreR.RightHandThumb4PreRy
    RightHandThumb4PreRz = RightHandThumb4PreR.RightHandThumb4PreRz

    RightHandThumb4PostR = RightHandThumb4PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandThumb4PostRx = RightHandThumb4PostR.RightHandThumb4PostRx
    RightHandThumb4PostRy = RightHandThumb4PostR.RightHandThumb4PostRy
    RightHandThumb4PostRz = RightHandThumb4PostR.RightHandThumb4PostRz

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

    RightHandIndex1PGX = MatrixField()

    RightHandIndex1ROrder = RightHandIndex1ROrderEnumField(default_value=0)

    RightHandIndex1SC = BoolField(default_value=False)

    RightHandIndex1IS = RightHandIndex1ISField(default_value=(1.0, 1.0, 1.0))
    RightHandIndex1ISx = RightHandIndex1IS.RightHandIndex1ISx
    RightHandIndex1ISy = RightHandIndex1IS.RightHandIndex1ISy
    RightHandIndex1ISz = RightHandIndex1IS.RightHandIndex1ISz

    RightHandIndex1PreR = RightHandIndex1PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex1PreRx = RightHandIndex1PreR.RightHandIndex1PreRx
    RightHandIndex1PreRy = RightHandIndex1PreR.RightHandIndex1PreRy
    RightHandIndex1PreRz = RightHandIndex1PreR.RightHandIndex1PreRz

    RightHandIndex1PostR = RightHandIndex1PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex1PostRx = RightHandIndex1PostR.RightHandIndex1PostRx
    RightHandIndex1PostRy = RightHandIndex1PostR.RightHandIndex1PostRy
    RightHandIndex1PostRz = RightHandIndex1PostR.RightHandIndex1PostRz

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

    RightHandIndex2PGX = MatrixField()

    RightHandIndex2ROrder = RightHandIndex2ROrderEnumField(default_value=0)

    RightHandIndex2SC = BoolField(default_value=False)

    RightHandIndex2IS = RightHandIndex2ISField(default_value=(1.0, 1.0, 1.0))
    RightHandIndex2ISx = RightHandIndex2IS.RightHandIndex2ISx
    RightHandIndex2ISy = RightHandIndex2IS.RightHandIndex2ISy
    RightHandIndex2ISz = RightHandIndex2IS.RightHandIndex2ISz

    RightHandIndex2PreR = RightHandIndex2PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex2PreRx = RightHandIndex2PreR.RightHandIndex2PreRx
    RightHandIndex2PreRy = RightHandIndex2PreR.RightHandIndex2PreRy
    RightHandIndex2PreRz = RightHandIndex2PreR.RightHandIndex2PreRz

    RightHandIndex2PostR = RightHandIndex2PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex2PostRx = RightHandIndex2PostR.RightHandIndex2PostRx
    RightHandIndex2PostRy = RightHandIndex2PostR.RightHandIndex2PostRy
    RightHandIndex2PostRz = RightHandIndex2PostR.RightHandIndex2PostRz

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

    RightHandIndex3PGX = MatrixField()

    RightHandIndex3ROrder = RightHandIndex3ROrderEnumField(default_value=0)

    RightHandIndex3SC = BoolField(default_value=False)

    RightHandIndex3IS = RightHandIndex3ISField(default_value=(1.0, 1.0, 1.0))
    RightHandIndex3ISx = RightHandIndex3IS.RightHandIndex3ISx
    RightHandIndex3ISy = RightHandIndex3IS.RightHandIndex3ISy
    RightHandIndex3ISz = RightHandIndex3IS.RightHandIndex3ISz

    RightHandIndex3PreR = RightHandIndex3PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex3PreRx = RightHandIndex3PreR.RightHandIndex3PreRx
    RightHandIndex3PreRy = RightHandIndex3PreR.RightHandIndex3PreRy
    RightHandIndex3PreRz = RightHandIndex3PreR.RightHandIndex3PreRz

    RightHandIndex3PostR = RightHandIndex3PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex3PostRx = RightHandIndex3PostR.RightHandIndex3PostRx
    RightHandIndex3PostRy = RightHandIndex3PostR.RightHandIndex3PostRy
    RightHandIndex3PostRz = RightHandIndex3PostR.RightHandIndex3PostRz

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

    RightHandIndex4PGX = MatrixField()

    RightHandIndex4ROrder = RightHandIndex4ROrderEnumField(default_value=0)

    RightHandIndex4SC = BoolField(default_value=False)

    RightHandIndex4IS = RightHandIndex4ISField(default_value=(1.0, 1.0, 1.0))
    RightHandIndex4ISx = RightHandIndex4IS.RightHandIndex4ISx
    RightHandIndex4ISy = RightHandIndex4IS.RightHandIndex4ISy
    RightHandIndex4ISz = RightHandIndex4IS.RightHandIndex4ISz

    RightHandIndex4PreR = RightHandIndex4PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex4PreRx = RightHandIndex4PreR.RightHandIndex4PreRx
    RightHandIndex4PreRy = RightHandIndex4PreR.RightHandIndex4PreRy
    RightHandIndex4PreRz = RightHandIndex4PreR.RightHandIndex4PreRz

    RightHandIndex4PostR = RightHandIndex4PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandIndex4PostRx = RightHandIndex4PostR.RightHandIndex4PostRx
    RightHandIndex4PostRy = RightHandIndex4PostR.RightHandIndex4PostRy
    RightHandIndex4PostRz = RightHandIndex4PostR.RightHandIndex4PostRz

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

    RightHandMiddle1PGX = MatrixField()

    RightHandMiddle1ROrder = RightHandMiddle1ROrderEnumField(default_value=0)

    RightHandMiddle1SC = BoolField(default_value=False)

    RightHandMiddle1IS = RightHandMiddle1ISField(default_value=(1.0, 1.0, 1.0))
    RightHandMiddle1ISx = RightHandMiddle1IS.RightHandMiddle1ISx
    RightHandMiddle1ISy = RightHandMiddle1IS.RightHandMiddle1ISy
    RightHandMiddle1ISz = RightHandMiddle1IS.RightHandMiddle1ISz

    RightHandMiddle1PreR = RightHandMiddle1PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle1PreRx = RightHandMiddle1PreR.RightHandMiddle1PreRx
    RightHandMiddle1PreRy = RightHandMiddle1PreR.RightHandMiddle1PreRy
    RightHandMiddle1PreRz = RightHandMiddle1PreR.RightHandMiddle1PreRz

    RightHandMiddle1PostR = RightHandMiddle1PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle1PostRx = RightHandMiddle1PostR.RightHandMiddle1PostRx
    RightHandMiddle1PostRy = RightHandMiddle1PostR.RightHandMiddle1PostRy
    RightHandMiddle1PostRz = RightHandMiddle1PostR.RightHandMiddle1PostRz

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

    RightHandMiddle2PGX = MatrixField()

    RightHandMiddle2ROrder = RightHandMiddle2ROrderEnumField(default_value=0)

    RightHandMiddle2SC = BoolField(default_value=False)

    RightHandMiddle2IS = RightHandMiddle2ISField(default_value=(1.0, 1.0, 1.0))
    RightHandMiddle2ISx = RightHandMiddle2IS.RightHandMiddle2ISx
    RightHandMiddle2ISy = RightHandMiddle2IS.RightHandMiddle2ISy
    RightHandMiddle2ISz = RightHandMiddle2IS.RightHandMiddle2ISz

    RightHandMiddle2PreR = RightHandMiddle2PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle2PreRx = RightHandMiddle2PreR.RightHandMiddle2PreRx
    RightHandMiddle2PreRy = RightHandMiddle2PreR.RightHandMiddle2PreRy
    RightHandMiddle2PreRz = RightHandMiddle2PreR.RightHandMiddle2PreRz

    RightHandMiddle2PostR = RightHandMiddle2PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle2PostRx = RightHandMiddle2PostR.RightHandMiddle2PostRx
    RightHandMiddle2PostRy = RightHandMiddle2PostR.RightHandMiddle2PostRy
    RightHandMiddle2PostRz = RightHandMiddle2PostR.RightHandMiddle2PostRz

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

    RightHandMiddle3PGX = MatrixField()

    RightHandMiddle3ROrder = RightHandMiddle3ROrderEnumField(default_value=0)

    RightHandMiddle3SC = BoolField(default_value=False)

    RightHandMiddle3IS = RightHandMiddle3ISField(default_value=(1.0, 1.0, 1.0))
    RightHandMiddle3ISx = RightHandMiddle3IS.RightHandMiddle3ISx
    RightHandMiddle3ISy = RightHandMiddle3IS.RightHandMiddle3ISy
    RightHandMiddle3ISz = RightHandMiddle3IS.RightHandMiddle3ISz

    RightHandMiddle3PreR = RightHandMiddle3PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle3PreRx = RightHandMiddle3PreR.RightHandMiddle3PreRx
    RightHandMiddle3PreRy = RightHandMiddle3PreR.RightHandMiddle3PreRy
    RightHandMiddle3PreRz = RightHandMiddle3PreR.RightHandMiddle3PreRz

    RightHandMiddle3PostR = RightHandMiddle3PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle3PostRx = RightHandMiddle3PostR.RightHandMiddle3PostRx
    RightHandMiddle3PostRy = RightHandMiddle3PostR.RightHandMiddle3PostRy
    RightHandMiddle3PostRz = RightHandMiddle3PostR.RightHandMiddle3PostRz

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

    RightHandMiddle4PGX = MatrixField()

    RightHandMiddle4ROrder = RightHandMiddle4ROrderEnumField(default_value=0)

    RightHandMiddle4SC = BoolField(default_value=False)

    RightHandMiddle4IS = RightHandMiddle4ISField(default_value=(1.0, 1.0, 1.0))
    RightHandMiddle4ISx = RightHandMiddle4IS.RightHandMiddle4ISx
    RightHandMiddle4ISy = RightHandMiddle4IS.RightHandMiddle4ISy
    RightHandMiddle4ISz = RightHandMiddle4IS.RightHandMiddle4ISz

    RightHandMiddle4PreR = RightHandMiddle4PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle4PreRx = RightHandMiddle4PreR.RightHandMiddle4PreRx
    RightHandMiddle4PreRy = RightHandMiddle4PreR.RightHandMiddle4PreRy
    RightHandMiddle4PreRz = RightHandMiddle4PreR.RightHandMiddle4PreRz

    RightHandMiddle4PostR = RightHandMiddle4PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandMiddle4PostRx = RightHandMiddle4PostR.RightHandMiddle4PostRx
    RightHandMiddle4PostRy = RightHandMiddle4PostR.RightHandMiddle4PostRy
    RightHandMiddle4PostRz = RightHandMiddle4PostR.RightHandMiddle4PostRz

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

    RightHandRing1PGX = MatrixField()

    RightHandRing1ROrder = RightHandRing1ROrderEnumField(default_value=0)

    RightHandRing1SC = BoolField(default_value=False)

    RightHandRing1IS = RightHandRing1ISField(default_value=(1.0, 1.0, 1.0))
    RightHandRing1ISx = RightHandRing1IS.RightHandRing1ISx
    RightHandRing1ISy = RightHandRing1IS.RightHandRing1ISy
    RightHandRing1ISz = RightHandRing1IS.RightHandRing1ISz

    RightHandRing1PreR = RightHandRing1PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandRing1PreRx = RightHandRing1PreR.RightHandRing1PreRx
    RightHandRing1PreRy = RightHandRing1PreR.RightHandRing1PreRy
    RightHandRing1PreRz = RightHandRing1PreR.RightHandRing1PreRz

    RightHandRing1PostR = RightHandRing1PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandRing1PostRx = RightHandRing1PostR.RightHandRing1PostRx
    RightHandRing1PostRy = RightHandRing1PostR.RightHandRing1PostRy
    RightHandRing1PostRz = RightHandRing1PostR.RightHandRing1PostRz

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

    RightHandRing2PGX = MatrixField()

    RightHandRing2ROrder = RightHandRing2ROrderEnumField(default_value=0)

    RightHandRing2SC = BoolField(default_value=False)

    RightHandRing2IS = RightHandRing2ISField(default_value=(1.0, 1.0, 1.0))
    RightHandRing2ISx = RightHandRing2IS.RightHandRing2ISx
    RightHandRing2ISy = RightHandRing2IS.RightHandRing2ISy
    RightHandRing2ISz = RightHandRing2IS.RightHandRing2ISz

    RightHandRing2PreR = RightHandRing2PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandRing2PreRx = RightHandRing2PreR.RightHandRing2PreRx
    RightHandRing2PreRy = RightHandRing2PreR.RightHandRing2PreRy
    RightHandRing2PreRz = RightHandRing2PreR.RightHandRing2PreRz

    RightHandRing2PostR = RightHandRing2PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandRing2PostRx = RightHandRing2PostR.RightHandRing2PostRx
    RightHandRing2PostRy = RightHandRing2PostR.RightHandRing2PostRy
    RightHandRing2PostRz = RightHandRing2PostR.RightHandRing2PostRz

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

    RightHandRing3PGX = MatrixField()

    RightHandRing3ROrder = RightHandRing3ROrderEnumField(default_value=0)

    RightHandRing3SC = BoolField(default_value=False)

    RightHandRing3IS = RightHandRing3ISField(default_value=(1.0, 1.0, 1.0))
    RightHandRing3ISx = RightHandRing3IS.RightHandRing3ISx
    RightHandRing3ISy = RightHandRing3IS.RightHandRing3ISy
    RightHandRing3ISz = RightHandRing3IS.RightHandRing3ISz

    RightHandRing3PreR = RightHandRing3PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandRing3PreRx = RightHandRing3PreR.RightHandRing3PreRx
    RightHandRing3PreRy = RightHandRing3PreR.RightHandRing3PreRy
    RightHandRing3PreRz = RightHandRing3PreR.RightHandRing3PreRz

    RightHandRing3PostR = RightHandRing3PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandRing3PostRx = RightHandRing3PostR.RightHandRing3PostRx
    RightHandRing3PostRy = RightHandRing3PostR.RightHandRing3PostRy
    RightHandRing3PostRz = RightHandRing3PostR.RightHandRing3PostRz

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

    RightHandRing4PGX = MatrixField()

    RightHandRing4ROrder = RightHandRing4ROrderEnumField(default_value=0)

    RightHandRing4SC = BoolField(default_value=False)

    RightHandRing4IS = RightHandRing4ISField(default_value=(1.0, 1.0, 1.0))
    RightHandRing4ISx = RightHandRing4IS.RightHandRing4ISx
    RightHandRing4ISy = RightHandRing4IS.RightHandRing4ISy
    RightHandRing4ISz = RightHandRing4IS.RightHandRing4ISz

    RightHandRing4PreR = RightHandRing4PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandRing4PreRx = RightHandRing4PreR.RightHandRing4PreRx
    RightHandRing4PreRy = RightHandRing4PreR.RightHandRing4PreRy
    RightHandRing4PreRz = RightHandRing4PreR.RightHandRing4PreRz

    RightHandRing4PostR = RightHandRing4PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandRing4PostRx = RightHandRing4PostR.RightHandRing4PostRx
    RightHandRing4PostRy = RightHandRing4PostR.RightHandRing4PostRy
    RightHandRing4PostRz = RightHandRing4PostR.RightHandRing4PostRz

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

    RightHandPinky1PGX = MatrixField()

    RightHandPinky1ROrder = RightHandPinky1ROrderEnumField(default_value=0)

    RightHandPinky1SC = BoolField(default_value=False)

    RightHandPinky1IS = RightHandPinky1ISField(default_value=(1.0, 1.0, 1.0))
    RightHandPinky1ISx = RightHandPinky1IS.RightHandPinky1ISx
    RightHandPinky1ISy = RightHandPinky1IS.RightHandPinky1ISy
    RightHandPinky1ISz = RightHandPinky1IS.RightHandPinky1ISz

    RightHandPinky1PreR = RightHandPinky1PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky1PreRx = RightHandPinky1PreR.RightHandPinky1PreRx
    RightHandPinky1PreRy = RightHandPinky1PreR.RightHandPinky1PreRy
    RightHandPinky1PreRz = RightHandPinky1PreR.RightHandPinky1PreRz

    RightHandPinky1PostR = RightHandPinky1PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky1PostRx = RightHandPinky1PostR.RightHandPinky1PostRx
    RightHandPinky1PostRy = RightHandPinky1PostR.RightHandPinky1PostRy
    RightHandPinky1PostRz = RightHandPinky1PostR.RightHandPinky1PostRz

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

    RightHandPinky2PGX = MatrixField()

    RightHandPinky2ROrder = RightHandPinky2ROrderEnumField(default_value=0)

    RightHandPinky2SC = BoolField(default_value=False)

    RightHandPinky2IS = RightHandPinky2ISField(default_value=(1.0, 1.0, 1.0))
    RightHandPinky2ISx = RightHandPinky2IS.RightHandPinky2ISx
    RightHandPinky2ISy = RightHandPinky2IS.RightHandPinky2ISy
    RightHandPinky2ISz = RightHandPinky2IS.RightHandPinky2ISz

    RightHandPinky2PreR = RightHandPinky2PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky2PreRx = RightHandPinky2PreR.RightHandPinky2PreRx
    RightHandPinky2PreRy = RightHandPinky2PreR.RightHandPinky2PreRy
    RightHandPinky2PreRz = RightHandPinky2PreR.RightHandPinky2PreRz

    RightHandPinky2PostR = RightHandPinky2PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky2PostRx = RightHandPinky2PostR.RightHandPinky2PostRx
    RightHandPinky2PostRy = RightHandPinky2PostR.RightHandPinky2PostRy
    RightHandPinky2PostRz = RightHandPinky2PostR.RightHandPinky2PostRz

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

    RightHandPinky3PGX = MatrixField()

    RightHandPinky3ROrder = RightHandPinky3ROrderEnumField(default_value=0)

    RightHandPinky3SC = BoolField(default_value=False)

    RightHandPinky3IS = RightHandPinky3ISField(default_value=(1.0, 1.0, 1.0))
    RightHandPinky3ISx = RightHandPinky3IS.RightHandPinky3ISx
    RightHandPinky3ISy = RightHandPinky3IS.RightHandPinky3ISy
    RightHandPinky3ISz = RightHandPinky3IS.RightHandPinky3ISz

    RightHandPinky3PreR = RightHandPinky3PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky3PreRx = RightHandPinky3PreR.RightHandPinky3PreRx
    RightHandPinky3PreRy = RightHandPinky3PreR.RightHandPinky3PreRy
    RightHandPinky3PreRz = RightHandPinky3PreR.RightHandPinky3PreRz

    RightHandPinky3PostR = RightHandPinky3PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky3PostRx = RightHandPinky3PostR.RightHandPinky3PostRx
    RightHandPinky3PostRy = RightHandPinky3PostR.RightHandPinky3PostRy
    RightHandPinky3PostRz = RightHandPinky3PostR.RightHandPinky3PostRz

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

    RightHandPinky4PGX = MatrixField()

    RightHandPinky4ROrder = RightHandPinky4ROrderEnumField(default_value=0)

    RightHandPinky4SC = BoolField(default_value=False)

    RightHandPinky4IS = RightHandPinky4ISField(default_value=(1.0, 1.0, 1.0))
    RightHandPinky4ISx = RightHandPinky4IS.RightHandPinky4ISx
    RightHandPinky4ISy = RightHandPinky4IS.RightHandPinky4ISy
    RightHandPinky4ISz = RightHandPinky4IS.RightHandPinky4ISz

    RightHandPinky4PreR = RightHandPinky4PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky4PreRx = RightHandPinky4PreR.RightHandPinky4PreRx
    RightHandPinky4PreRy = RightHandPinky4PreR.RightHandPinky4PreRy
    RightHandPinky4PreRz = RightHandPinky4PreR.RightHandPinky4PreRz

    RightHandPinky4PostR = RightHandPinky4PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandPinky4PostRx = RightHandPinky4PostR.RightHandPinky4PostRx
    RightHandPinky4PostRy = RightHandPinky4PostR.RightHandPinky4PostRy
    RightHandPinky4PostRz = RightHandPinky4PostR.RightHandPinky4PostRz

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

    RightHandExtraFinger1PGX = MatrixField()

    RightHandExtraFinger1ROrder = RightHandExtraFinger1ROrderEnumField(default_value=0)

    RightHandExtraFinger1SC = BoolField(default_value=False)

    RightHandExtraFinger1IS = RightHandExtraFinger1ISField(default_value=(1.0, 1.0, 1.0))
    RightHandExtraFinger1ISx = RightHandExtraFinger1IS.RightHandExtraFinger1ISx
    RightHandExtraFinger1ISy = RightHandExtraFinger1IS.RightHandExtraFinger1ISy
    RightHandExtraFinger1ISz = RightHandExtraFinger1IS.RightHandExtraFinger1ISz

    RightHandExtraFinger1PreR = RightHandExtraFinger1PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger1PreRx = RightHandExtraFinger1PreR.RightHandExtraFinger1PreRx
    RightHandExtraFinger1PreRy = RightHandExtraFinger1PreR.RightHandExtraFinger1PreRy
    RightHandExtraFinger1PreRz = RightHandExtraFinger1PreR.RightHandExtraFinger1PreRz

    RightHandExtraFinger1PostR = RightHandExtraFinger1PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger1PostRx = RightHandExtraFinger1PostR.RightHandExtraFinger1PostRx
    RightHandExtraFinger1PostRy = RightHandExtraFinger1PostR.RightHandExtraFinger1PostRy
    RightHandExtraFinger1PostRz = RightHandExtraFinger1PostR.RightHandExtraFinger1PostRz

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

    RightHandExtraFinger2PGX = MatrixField()

    RightHandExtraFinger2ROrder = RightHandExtraFinger2ROrderEnumField(default_value=0)

    RightHandExtraFinger2SC = BoolField(default_value=False)

    RightHandExtraFinger2IS = RightHandExtraFinger2ISField(default_value=(1.0, 1.0, 1.0))
    RightHandExtraFinger2ISx = RightHandExtraFinger2IS.RightHandExtraFinger2ISx
    RightHandExtraFinger2ISy = RightHandExtraFinger2IS.RightHandExtraFinger2ISy
    RightHandExtraFinger2ISz = RightHandExtraFinger2IS.RightHandExtraFinger2ISz

    RightHandExtraFinger2PreR = RightHandExtraFinger2PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger2PreRx = RightHandExtraFinger2PreR.RightHandExtraFinger2PreRx
    RightHandExtraFinger2PreRy = RightHandExtraFinger2PreR.RightHandExtraFinger2PreRy
    RightHandExtraFinger2PreRz = RightHandExtraFinger2PreR.RightHandExtraFinger2PreRz

    RightHandExtraFinger2PostR = RightHandExtraFinger2PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger2PostRx = RightHandExtraFinger2PostR.RightHandExtraFinger2PostRx
    RightHandExtraFinger2PostRy = RightHandExtraFinger2PostR.RightHandExtraFinger2PostRy
    RightHandExtraFinger2PostRz = RightHandExtraFinger2PostR.RightHandExtraFinger2PostRz

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

    RightHandExtraFinger3PGX = MatrixField()

    RightHandExtraFinger3ROrder = RightHandExtraFinger3ROrderEnumField(default_value=0)

    RightHandExtraFinger3SC = BoolField(default_value=False)

    RightHandExtraFinger3IS = RightHandExtraFinger3ISField(default_value=(1.0, 1.0, 1.0))
    RightHandExtraFinger3ISx = RightHandExtraFinger3IS.RightHandExtraFinger3ISx
    RightHandExtraFinger3ISy = RightHandExtraFinger3IS.RightHandExtraFinger3ISy
    RightHandExtraFinger3ISz = RightHandExtraFinger3IS.RightHandExtraFinger3ISz

    RightHandExtraFinger3PreR = RightHandExtraFinger3PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger3PreRx = RightHandExtraFinger3PreR.RightHandExtraFinger3PreRx
    RightHandExtraFinger3PreRy = RightHandExtraFinger3PreR.RightHandExtraFinger3PreRy
    RightHandExtraFinger3PreRz = RightHandExtraFinger3PreR.RightHandExtraFinger3PreRz

    RightHandExtraFinger3PostR = RightHandExtraFinger3PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger3PostRx = RightHandExtraFinger3PostR.RightHandExtraFinger3PostRx
    RightHandExtraFinger3PostRy = RightHandExtraFinger3PostR.RightHandExtraFinger3PostRy
    RightHandExtraFinger3PostRz = RightHandExtraFinger3PostR.RightHandExtraFinger3PostRz

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

    RightHandExtraFinger4PGX = MatrixField()

    RightHandExtraFinger4ROrder = RightHandExtraFinger4ROrderEnumField(default_value=0)

    RightHandExtraFinger4SC = BoolField(default_value=False)

    RightHandExtraFinger4IS = RightHandExtraFinger4ISField(default_value=(1.0, 1.0, 1.0))
    RightHandExtraFinger4ISx = RightHandExtraFinger4IS.RightHandExtraFinger4ISx
    RightHandExtraFinger4ISy = RightHandExtraFinger4IS.RightHandExtraFinger4ISy
    RightHandExtraFinger4ISz = RightHandExtraFinger4IS.RightHandExtraFinger4ISz

    RightHandExtraFinger4PreR = RightHandExtraFinger4PreRField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger4PreRx = RightHandExtraFinger4PreR.RightHandExtraFinger4PreRx
    RightHandExtraFinger4PreRy = RightHandExtraFinger4PreR.RightHandExtraFinger4PreRy
    RightHandExtraFinger4PreRz = RightHandExtraFinger4PreR.RightHandExtraFinger4PreRz

    RightHandExtraFinger4PostR = RightHandExtraFinger4PostRField(default_value=(0.0, 0.0, 0.0))
    RightHandExtraFinger4PostRx = RightHandExtraFinger4PostR.RightHandExtraFinger4PostRx
    RightHandExtraFinger4PostRy = RightHandExtraFinger4PostR.RightHandExtraFinger4PostRy
    RightHandExtraFinger4PostRz = RightHandExtraFinger4PostR.RightHandExtraFinger4PostRz

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

    LeftFootThumb1PGX = MatrixField()

    LeftFootThumb1ROrder = LeftFootThumb1ROrderEnumField(default_value=0)

    LeftFootThumb1SC = BoolField(default_value=False)

    LeftFootThumb1IS = LeftFootThumb1ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootThumb1ISx = LeftFootThumb1IS.LeftFootThumb1ISx
    LeftFootThumb1ISy = LeftFootThumb1IS.LeftFootThumb1ISy
    LeftFootThumb1ISz = LeftFootThumb1IS.LeftFootThumb1ISz

    LeftFootThumb1PreR = LeftFootThumb1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb1PreRx = LeftFootThumb1PreR.LeftFootThumb1PreRx
    LeftFootThumb1PreRy = LeftFootThumb1PreR.LeftFootThumb1PreRy
    LeftFootThumb1PreRz = LeftFootThumb1PreR.LeftFootThumb1PreRz

    LeftFootThumb1PostR = LeftFootThumb1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb1PostRx = LeftFootThumb1PostR.LeftFootThumb1PostRx
    LeftFootThumb1PostRy = LeftFootThumb1PostR.LeftFootThumb1PostRy
    LeftFootThumb1PostRz = LeftFootThumb1PostR.LeftFootThumb1PostRz

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

    LeftFootThumb2PGX = MatrixField()

    LeftFootThumb2ROrder = LeftFootThumb2ROrderEnumField(default_value=0)

    LeftFootThumb2SC = BoolField(default_value=False)

    LeftFootThumb2IS = LeftFootThumb2ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootThumb2ISx = LeftFootThumb2IS.LeftFootThumb2ISx
    LeftFootThumb2ISy = LeftFootThumb2IS.LeftFootThumb2ISy
    LeftFootThumb2ISz = LeftFootThumb2IS.LeftFootThumb2ISz

    LeftFootThumb2PreR = LeftFootThumb2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb2PreRx = LeftFootThumb2PreR.LeftFootThumb2PreRx
    LeftFootThumb2PreRy = LeftFootThumb2PreR.LeftFootThumb2PreRy
    LeftFootThumb2PreRz = LeftFootThumb2PreR.LeftFootThumb2PreRz

    LeftFootThumb2PostR = LeftFootThumb2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb2PostRx = LeftFootThumb2PostR.LeftFootThumb2PostRx
    LeftFootThumb2PostRy = LeftFootThumb2PostR.LeftFootThumb2PostRy
    LeftFootThumb2PostRz = LeftFootThumb2PostR.LeftFootThumb2PostRz

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

    LeftFootThumb3PGX = MatrixField()

    LeftFootThumb3ROrder = LeftFootThumb3ROrderEnumField(default_value=0)

    LeftFootThumb3SC = BoolField(default_value=False)

    LeftFootThumb3IS = LeftFootThumb3ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootThumb3ISx = LeftFootThumb3IS.LeftFootThumb3ISx
    LeftFootThumb3ISy = LeftFootThumb3IS.LeftFootThumb3ISy
    LeftFootThumb3ISz = LeftFootThumb3IS.LeftFootThumb3ISz

    LeftFootThumb3PreR = LeftFootThumb3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb3PreRx = LeftFootThumb3PreR.LeftFootThumb3PreRx
    LeftFootThumb3PreRy = LeftFootThumb3PreR.LeftFootThumb3PreRy
    LeftFootThumb3PreRz = LeftFootThumb3PreR.LeftFootThumb3PreRz

    LeftFootThumb3PostR = LeftFootThumb3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb3PostRx = LeftFootThumb3PostR.LeftFootThumb3PostRx
    LeftFootThumb3PostRy = LeftFootThumb3PostR.LeftFootThumb3PostRy
    LeftFootThumb3PostRz = LeftFootThumb3PostR.LeftFootThumb3PostRz

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

    LeftFootThumb4PGX = MatrixField()

    LeftFootThumb4ROrder = LeftFootThumb4ROrderEnumField(default_value=0)

    LeftFootThumb4SC = BoolField(default_value=False)

    LeftFootThumb4IS = LeftFootThumb4ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootThumb4ISx = LeftFootThumb4IS.LeftFootThumb4ISx
    LeftFootThumb4ISy = LeftFootThumb4IS.LeftFootThumb4ISy
    LeftFootThumb4ISz = LeftFootThumb4IS.LeftFootThumb4ISz

    LeftFootThumb4PreR = LeftFootThumb4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb4PreRx = LeftFootThumb4PreR.LeftFootThumb4PreRx
    LeftFootThumb4PreRy = LeftFootThumb4PreR.LeftFootThumb4PreRy
    LeftFootThumb4PreRz = LeftFootThumb4PreR.LeftFootThumb4PreRz

    LeftFootThumb4PostR = LeftFootThumb4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootThumb4PostRx = LeftFootThumb4PostR.LeftFootThumb4PostRx
    LeftFootThumb4PostRy = LeftFootThumb4PostR.LeftFootThumb4PostRy
    LeftFootThumb4PostRz = LeftFootThumb4PostR.LeftFootThumb4PostRz

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

    LeftFootIndex1PGX = MatrixField()

    LeftFootIndex1ROrder = LeftFootIndex1ROrderEnumField(default_value=0)

    LeftFootIndex1SC = BoolField(default_value=False)

    LeftFootIndex1IS = LeftFootIndex1ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootIndex1ISx = LeftFootIndex1IS.LeftFootIndex1ISx
    LeftFootIndex1ISy = LeftFootIndex1IS.LeftFootIndex1ISy
    LeftFootIndex1ISz = LeftFootIndex1IS.LeftFootIndex1ISz

    LeftFootIndex1PreR = LeftFootIndex1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex1PreRx = LeftFootIndex1PreR.LeftFootIndex1PreRx
    LeftFootIndex1PreRy = LeftFootIndex1PreR.LeftFootIndex1PreRy
    LeftFootIndex1PreRz = LeftFootIndex1PreR.LeftFootIndex1PreRz

    LeftFootIndex1PostR = LeftFootIndex1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex1PostRx = LeftFootIndex1PostR.LeftFootIndex1PostRx
    LeftFootIndex1PostRy = LeftFootIndex1PostR.LeftFootIndex1PostRy
    LeftFootIndex1PostRz = LeftFootIndex1PostR.LeftFootIndex1PostRz

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

    LeftFootIndex2PGX = MatrixField()

    LeftFootIndex2ROrder = LeftFootIndex2ROrderEnumField(default_value=0)

    LeftFootIndex2SC = BoolField(default_value=False)

    LeftFootIndex2IS = LeftFootIndex2ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootIndex2ISx = LeftFootIndex2IS.LeftFootIndex2ISx
    LeftFootIndex2ISy = LeftFootIndex2IS.LeftFootIndex2ISy
    LeftFootIndex2ISz = LeftFootIndex2IS.LeftFootIndex2ISz

    LeftFootIndex2PreR = LeftFootIndex2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex2PreRx = LeftFootIndex2PreR.LeftFootIndex2PreRx
    LeftFootIndex2PreRy = LeftFootIndex2PreR.LeftFootIndex2PreRy
    LeftFootIndex2PreRz = LeftFootIndex2PreR.LeftFootIndex2PreRz

    LeftFootIndex2PostR = LeftFootIndex2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex2PostRx = LeftFootIndex2PostR.LeftFootIndex2PostRx
    LeftFootIndex2PostRy = LeftFootIndex2PostR.LeftFootIndex2PostRy
    LeftFootIndex2PostRz = LeftFootIndex2PostR.LeftFootIndex2PostRz

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

    LeftFootIndex3PGX = MatrixField()

    LeftFootIndex3ROrder = LeftFootIndex3ROrderEnumField(default_value=0)

    LeftFootIndex3SC = BoolField(default_value=False)

    LeftFootIndex3IS = LeftFootIndex3ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootIndex3ISx = LeftFootIndex3IS.LeftFootIndex3ISx
    LeftFootIndex3ISy = LeftFootIndex3IS.LeftFootIndex3ISy
    LeftFootIndex3ISz = LeftFootIndex3IS.LeftFootIndex3ISz

    LeftFootIndex3PreR = LeftFootIndex3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex3PreRx = LeftFootIndex3PreR.LeftFootIndex3PreRx
    LeftFootIndex3PreRy = LeftFootIndex3PreR.LeftFootIndex3PreRy
    LeftFootIndex3PreRz = LeftFootIndex3PreR.LeftFootIndex3PreRz

    LeftFootIndex3PostR = LeftFootIndex3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex3PostRx = LeftFootIndex3PostR.LeftFootIndex3PostRx
    LeftFootIndex3PostRy = LeftFootIndex3PostR.LeftFootIndex3PostRy
    LeftFootIndex3PostRz = LeftFootIndex3PostR.LeftFootIndex3PostRz

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

    LeftFootIndex4PGX = MatrixField()

    LeftFootIndex4ROrder = LeftFootIndex4ROrderEnumField(default_value=0)

    LeftFootIndex4SC = BoolField(default_value=False)

    LeftFootIndex4IS = LeftFootIndex4ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootIndex4ISx = LeftFootIndex4IS.LeftFootIndex4ISx
    LeftFootIndex4ISy = LeftFootIndex4IS.LeftFootIndex4ISy
    LeftFootIndex4ISz = LeftFootIndex4IS.LeftFootIndex4ISz

    LeftFootIndex4PreR = LeftFootIndex4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex4PreRx = LeftFootIndex4PreR.LeftFootIndex4PreRx
    LeftFootIndex4PreRy = LeftFootIndex4PreR.LeftFootIndex4PreRy
    LeftFootIndex4PreRz = LeftFootIndex4PreR.LeftFootIndex4PreRz

    LeftFootIndex4PostR = LeftFootIndex4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootIndex4PostRx = LeftFootIndex4PostR.LeftFootIndex4PostRx
    LeftFootIndex4PostRy = LeftFootIndex4PostR.LeftFootIndex4PostRy
    LeftFootIndex4PostRz = LeftFootIndex4PostR.LeftFootIndex4PostRz

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

    LeftFootMiddle1PGX = MatrixField()

    LeftFootMiddle1ROrder = LeftFootMiddle1ROrderEnumField(default_value=0)

    LeftFootMiddle1SC = BoolField(default_value=False)

    LeftFootMiddle1IS = LeftFootMiddle1ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootMiddle1ISx = LeftFootMiddle1IS.LeftFootMiddle1ISx
    LeftFootMiddle1ISy = LeftFootMiddle1IS.LeftFootMiddle1ISy
    LeftFootMiddle1ISz = LeftFootMiddle1IS.LeftFootMiddle1ISz

    LeftFootMiddle1PreR = LeftFootMiddle1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle1PreRx = LeftFootMiddle1PreR.LeftFootMiddle1PreRx
    LeftFootMiddle1PreRy = LeftFootMiddle1PreR.LeftFootMiddle1PreRy
    LeftFootMiddle1PreRz = LeftFootMiddle1PreR.LeftFootMiddle1PreRz

    LeftFootMiddle1PostR = LeftFootMiddle1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle1PostRx = LeftFootMiddle1PostR.LeftFootMiddle1PostRx
    LeftFootMiddle1PostRy = LeftFootMiddle1PostR.LeftFootMiddle1PostRy
    LeftFootMiddle1PostRz = LeftFootMiddle1PostR.LeftFootMiddle1PostRz

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

    LeftFootMiddle2PGX = MatrixField()

    LeftFootMiddle2ROrder = LeftFootMiddle2ROrderEnumField(default_value=0)

    LeftFootMiddle2SC = BoolField(default_value=False)

    LeftFootMiddle2IS = LeftFootMiddle2ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootMiddle2ISx = LeftFootMiddle2IS.LeftFootMiddle2ISx
    LeftFootMiddle2ISy = LeftFootMiddle2IS.LeftFootMiddle2ISy
    LeftFootMiddle2ISz = LeftFootMiddle2IS.LeftFootMiddle2ISz

    LeftFootMiddle2PreR = LeftFootMiddle2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle2PreRx = LeftFootMiddle2PreR.LeftFootMiddle2PreRx
    LeftFootMiddle2PreRy = LeftFootMiddle2PreR.LeftFootMiddle2PreRy
    LeftFootMiddle2PreRz = LeftFootMiddle2PreR.LeftFootMiddle2PreRz

    LeftFootMiddle2PostR = LeftFootMiddle2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle2PostRx = LeftFootMiddle2PostR.LeftFootMiddle2PostRx
    LeftFootMiddle2PostRy = LeftFootMiddle2PostR.LeftFootMiddle2PostRy
    LeftFootMiddle2PostRz = LeftFootMiddle2PostR.LeftFootMiddle2PostRz

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

    LeftFootMiddle3PGX = MatrixField()

    LeftFootMiddle3ROrder = LeftFootMiddle3ROrderEnumField(default_value=0)

    LeftFootMiddle3SC = BoolField(default_value=False)

    LeftFootMiddle3IS = LeftFootMiddle3ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootMiddle3ISx = LeftFootMiddle3IS.LeftFootMiddle3ISx
    LeftFootMiddle3ISy = LeftFootMiddle3IS.LeftFootMiddle3ISy
    LeftFootMiddle3ISz = LeftFootMiddle3IS.LeftFootMiddle3ISz

    LeftFootMiddle3PreR = LeftFootMiddle3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle3PreRx = LeftFootMiddle3PreR.LeftFootMiddle3PreRx
    LeftFootMiddle3PreRy = LeftFootMiddle3PreR.LeftFootMiddle3PreRy
    LeftFootMiddle3PreRz = LeftFootMiddle3PreR.LeftFootMiddle3PreRz

    LeftFootMiddle3PostR = LeftFootMiddle3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle3PostRx = LeftFootMiddle3PostR.LeftFootMiddle3PostRx
    LeftFootMiddle3PostRy = LeftFootMiddle3PostR.LeftFootMiddle3PostRy
    LeftFootMiddle3PostRz = LeftFootMiddle3PostR.LeftFootMiddle3PostRz

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

    LeftFootMiddle4PGX = MatrixField()

    LeftFootMiddle4ROrder = LeftFootMiddle4ROrderEnumField(default_value=0)

    LeftFootMiddle4SC = BoolField(default_value=False)

    LeftFootMiddle4IS = LeftFootMiddle4ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootMiddle4ISx = LeftFootMiddle4IS.LeftFootMiddle4ISx
    LeftFootMiddle4ISy = LeftFootMiddle4IS.LeftFootMiddle4ISy
    LeftFootMiddle4ISz = LeftFootMiddle4IS.LeftFootMiddle4ISz

    LeftFootMiddle4PreR = LeftFootMiddle4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle4PreRx = LeftFootMiddle4PreR.LeftFootMiddle4PreRx
    LeftFootMiddle4PreRy = LeftFootMiddle4PreR.LeftFootMiddle4PreRy
    LeftFootMiddle4PreRz = LeftFootMiddle4PreR.LeftFootMiddle4PreRz

    LeftFootMiddle4PostR = LeftFootMiddle4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootMiddle4PostRx = LeftFootMiddle4PostR.LeftFootMiddle4PostRx
    LeftFootMiddle4PostRy = LeftFootMiddle4PostR.LeftFootMiddle4PostRy
    LeftFootMiddle4PostRz = LeftFootMiddle4PostR.LeftFootMiddle4PostRz

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

    LeftFootRing1PGX = MatrixField()

    LeftFootRing1ROrder = LeftFootRing1ROrderEnumField(default_value=0)

    LeftFootRing1SC = BoolField(default_value=False)

    LeftFootRing1IS = LeftFootRing1ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootRing1ISx = LeftFootRing1IS.LeftFootRing1ISx
    LeftFootRing1ISy = LeftFootRing1IS.LeftFootRing1ISy
    LeftFootRing1ISz = LeftFootRing1IS.LeftFootRing1ISz

    LeftFootRing1PreR = LeftFootRing1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing1PreRx = LeftFootRing1PreR.LeftFootRing1PreRx
    LeftFootRing1PreRy = LeftFootRing1PreR.LeftFootRing1PreRy
    LeftFootRing1PreRz = LeftFootRing1PreR.LeftFootRing1PreRz

    LeftFootRing1PostR = LeftFootRing1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing1PostRx = LeftFootRing1PostR.LeftFootRing1PostRx
    LeftFootRing1PostRy = LeftFootRing1PostR.LeftFootRing1PostRy
    LeftFootRing1PostRz = LeftFootRing1PostR.LeftFootRing1PostRz

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

    LeftFootRing2PGX = MatrixField()

    LeftFootRing2ROrder = LeftFootRing2ROrderEnumField(default_value=0)

    LeftFootRing2SC = BoolField(default_value=False)

    LeftFootRing2IS = LeftFootRing2ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootRing2ISx = LeftFootRing2IS.LeftFootRing2ISx
    LeftFootRing2ISy = LeftFootRing2IS.LeftFootRing2ISy
    LeftFootRing2ISz = LeftFootRing2IS.LeftFootRing2ISz

    LeftFootRing2PreR = LeftFootRing2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing2PreRx = LeftFootRing2PreR.LeftFootRing2PreRx
    LeftFootRing2PreRy = LeftFootRing2PreR.LeftFootRing2PreRy
    LeftFootRing2PreRz = LeftFootRing2PreR.LeftFootRing2PreRz

    LeftFootRing2PostR = LeftFootRing2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing2PostRx = LeftFootRing2PostR.LeftFootRing2PostRx
    LeftFootRing2PostRy = LeftFootRing2PostR.LeftFootRing2PostRy
    LeftFootRing2PostRz = LeftFootRing2PostR.LeftFootRing2PostRz

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

    LeftFootRing3PGX = MatrixField()

    LeftFootRing3ROrder = LeftFootRing3ROrderEnumField(default_value=0)

    LeftFootRing3SC = BoolField(default_value=False)

    LeftFootRing3IS = LeftFootRing3ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootRing3ISx = LeftFootRing3IS.LeftFootRing3ISx
    LeftFootRing3ISy = LeftFootRing3IS.LeftFootRing3ISy
    LeftFootRing3ISz = LeftFootRing3IS.LeftFootRing3ISz

    LeftFootRing3PreR = LeftFootRing3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing3PreRx = LeftFootRing3PreR.LeftFootRing3PreRx
    LeftFootRing3PreRy = LeftFootRing3PreR.LeftFootRing3PreRy
    LeftFootRing3PreRz = LeftFootRing3PreR.LeftFootRing3PreRz

    LeftFootRing3PostR = LeftFootRing3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing3PostRx = LeftFootRing3PostR.LeftFootRing3PostRx
    LeftFootRing3PostRy = LeftFootRing3PostR.LeftFootRing3PostRy
    LeftFootRing3PostRz = LeftFootRing3PostR.LeftFootRing3PostRz

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

    LeftFootRing4PGX = MatrixField()

    LeftFootRing4ROrder = LeftFootRing4ROrderEnumField(default_value=0)

    LeftFootRing4SC = BoolField(default_value=False)

    LeftFootRing4IS = LeftFootRing4ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootRing4ISx = LeftFootRing4IS.LeftFootRing4ISx
    LeftFootRing4ISy = LeftFootRing4IS.LeftFootRing4ISy
    LeftFootRing4ISz = LeftFootRing4IS.LeftFootRing4ISz

    LeftFootRing4PreR = LeftFootRing4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing4PreRx = LeftFootRing4PreR.LeftFootRing4PreRx
    LeftFootRing4PreRy = LeftFootRing4PreR.LeftFootRing4PreRy
    LeftFootRing4PreRz = LeftFootRing4PreR.LeftFootRing4PreRz

    LeftFootRing4PostR = LeftFootRing4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootRing4PostRx = LeftFootRing4PostR.LeftFootRing4PostRx
    LeftFootRing4PostRy = LeftFootRing4PostR.LeftFootRing4PostRy
    LeftFootRing4PostRz = LeftFootRing4PostR.LeftFootRing4PostRz

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

    LeftFootPinky1PGX = MatrixField()

    LeftFootPinky1ROrder = LeftFootPinky1ROrderEnumField(default_value=0)

    LeftFootPinky1SC = BoolField(default_value=False)

    LeftFootPinky1IS = LeftFootPinky1ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootPinky1ISx = LeftFootPinky1IS.LeftFootPinky1ISx
    LeftFootPinky1ISy = LeftFootPinky1IS.LeftFootPinky1ISy
    LeftFootPinky1ISz = LeftFootPinky1IS.LeftFootPinky1ISz

    LeftFootPinky1PreR = LeftFootPinky1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky1PreRx = LeftFootPinky1PreR.LeftFootPinky1PreRx
    LeftFootPinky1PreRy = LeftFootPinky1PreR.LeftFootPinky1PreRy
    LeftFootPinky1PreRz = LeftFootPinky1PreR.LeftFootPinky1PreRz

    LeftFootPinky1PostR = LeftFootPinky1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky1PostRx = LeftFootPinky1PostR.LeftFootPinky1PostRx
    LeftFootPinky1PostRy = LeftFootPinky1PostR.LeftFootPinky1PostRy
    LeftFootPinky1PostRz = LeftFootPinky1PostR.LeftFootPinky1PostRz

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

    LeftFootPinky2PGX = MatrixField()

    LeftFootPinky2ROrder = LeftFootPinky2ROrderEnumField(default_value=0)

    LeftFootPinky2SC = BoolField(default_value=False)

    LeftFootPinky2IS = LeftFootPinky2ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootPinky2ISx = LeftFootPinky2IS.LeftFootPinky2ISx
    LeftFootPinky2ISy = LeftFootPinky2IS.LeftFootPinky2ISy
    LeftFootPinky2ISz = LeftFootPinky2IS.LeftFootPinky2ISz

    LeftFootPinky2PreR = LeftFootPinky2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky2PreRx = LeftFootPinky2PreR.LeftFootPinky2PreRx
    LeftFootPinky2PreRy = LeftFootPinky2PreR.LeftFootPinky2PreRy
    LeftFootPinky2PreRz = LeftFootPinky2PreR.LeftFootPinky2PreRz

    LeftFootPinky2PostR = LeftFootPinky2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky2PostRx = LeftFootPinky2PostR.LeftFootPinky2PostRx
    LeftFootPinky2PostRy = LeftFootPinky2PostR.LeftFootPinky2PostRy
    LeftFootPinky2PostRz = LeftFootPinky2PostR.LeftFootPinky2PostRz

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

    LeftFootPinky3PGX = MatrixField()

    LeftFootPinky3ROrder = LeftFootPinky3ROrderEnumField(default_value=0)

    LeftFootPinky3SC = BoolField(default_value=False)

    LeftFootPinky3IS = LeftFootPinky3ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootPinky3ISx = LeftFootPinky3IS.LeftFootPinky3ISx
    LeftFootPinky3ISy = LeftFootPinky3IS.LeftFootPinky3ISy
    LeftFootPinky3ISz = LeftFootPinky3IS.LeftFootPinky3ISz

    LeftFootPinky3PreR = LeftFootPinky3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky3PreRx = LeftFootPinky3PreR.LeftFootPinky3PreRx
    LeftFootPinky3PreRy = LeftFootPinky3PreR.LeftFootPinky3PreRy
    LeftFootPinky3PreRz = LeftFootPinky3PreR.LeftFootPinky3PreRz

    LeftFootPinky3PostR = LeftFootPinky3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky3PostRx = LeftFootPinky3PostR.LeftFootPinky3PostRx
    LeftFootPinky3PostRy = LeftFootPinky3PostR.LeftFootPinky3PostRy
    LeftFootPinky3PostRz = LeftFootPinky3PostR.LeftFootPinky3PostRz

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

    LeftFootPinky4PGX = MatrixField()

    LeftFootPinky4ROrder = LeftFootPinky4ROrderEnumField(default_value=0)

    LeftFootPinky4SC = BoolField(default_value=False)

    LeftFootPinky4IS = LeftFootPinky4ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootPinky4ISx = LeftFootPinky4IS.LeftFootPinky4ISx
    LeftFootPinky4ISy = LeftFootPinky4IS.LeftFootPinky4ISy
    LeftFootPinky4ISz = LeftFootPinky4IS.LeftFootPinky4ISz

    LeftFootPinky4PreR = LeftFootPinky4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky4PreRx = LeftFootPinky4PreR.LeftFootPinky4PreRx
    LeftFootPinky4PreRy = LeftFootPinky4PreR.LeftFootPinky4PreRy
    LeftFootPinky4PreRz = LeftFootPinky4PreR.LeftFootPinky4PreRz

    LeftFootPinky4PostR = LeftFootPinky4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootPinky4PostRx = LeftFootPinky4PostR.LeftFootPinky4PostRx
    LeftFootPinky4PostRy = LeftFootPinky4PostR.LeftFootPinky4PostRy
    LeftFootPinky4PostRz = LeftFootPinky4PostR.LeftFootPinky4PostRz

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

    LeftFootExtraFinger1PGX = MatrixField()

    LeftFootExtraFinger1ROrder = LeftFootExtraFinger1ROrderEnumField(default_value=0)

    LeftFootExtraFinger1SC = BoolField(default_value=False)

    LeftFootExtraFinger1IS = LeftFootExtraFinger1ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootExtraFinger1ISx = LeftFootExtraFinger1IS.LeftFootExtraFinger1ISx
    LeftFootExtraFinger1ISy = LeftFootExtraFinger1IS.LeftFootExtraFinger1ISy
    LeftFootExtraFinger1ISz = LeftFootExtraFinger1IS.LeftFootExtraFinger1ISz

    LeftFootExtraFinger1PreR = LeftFootExtraFinger1PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger1PreRx = LeftFootExtraFinger1PreR.LeftFootExtraFinger1PreRx
    LeftFootExtraFinger1PreRy = LeftFootExtraFinger1PreR.LeftFootExtraFinger1PreRy
    LeftFootExtraFinger1PreRz = LeftFootExtraFinger1PreR.LeftFootExtraFinger1PreRz

    LeftFootExtraFinger1PostR = LeftFootExtraFinger1PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger1PostRx = LeftFootExtraFinger1PostR.LeftFootExtraFinger1PostRx
    LeftFootExtraFinger1PostRy = LeftFootExtraFinger1PostR.LeftFootExtraFinger1PostRy
    LeftFootExtraFinger1PostRz = LeftFootExtraFinger1PostR.LeftFootExtraFinger1PostRz

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

    LeftFootExtraFinger2PGX = MatrixField()

    LeftFootExtraFinger2ROrder = LeftFootExtraFinger2ROrderEnumField(default_value=0)

    LeftFootExtraFinger2SC = BoolField(default_value=False)

    LeftFootExtraFinger2IS = LeftFootExtraFinger2ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootExtraFinger2ISx = LeftFootExtraFinger2IS.LeftFootExtraFinger2ISx
    LeftFootExtraFinger2ISy = LeftFootExtraFinger2IS.LeftFootExtraFinger2ISy
    LeftFootExtraFinger2ISz = LeftFootExtraFinger2IS.LeftFootExtraFinger2ISz

    LeftFootExtraFinger2PreR = LeftFootExtraFinger2PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger2PreRx = LeftFootExtraFinger2PreR.LeftFootExtraFinger2PreRx
    LeftFootExtraFinger2PreRy = LeftFootExtraFinger2PreR.LeftFootExtraFinger2PreRy
    LeftFootExtraFinger2PreRz = LeftFootExtraFinger2PreR.LeftFootExtraFinger2PreRz

    LeftFootExtraFinger2PostR = LeftFootExtraFinger2PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger2PostRx = LeftFootExtraFinger2PostR.LeftFootExtraFinger2PostRx
    LeftFootExtraFinger2PostRy = LeftFootExtraFinger2PostR.LeftFootExtraFinger2PostRy
    LeftFootExtraFinger2PostRz = LeftFootExtraFinger2PostR.LeftFootExtraFinger2PostRz

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

    LeftFootExtraFinger3PGX = MatrixField()

    LeftFootExtraFinger3ROrder = LeftFootExtraFinger3ROrderEnumField(default_value=0)

    LeftFootExtraFinger3SC = BoolField(default_value=False)

    LeftFootExtraFinger3IS = LeftFootExtraFinger3ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootExtraFinger3ISx = LeftFootExtraFinger3IS.LeftFootExtraFinger3ISx
    LeftFootExtraFinger3ISy = LeftFootExtraFinger3IS.LeftFootExtraFinger3ISy
    LeftFootExtraFinger3ISz = LeftFootExtraFinger3IS.LeftFootExtraFinger3ISz

    LeftFootExtraFinger3PreR = LeftFootExtraFinger3PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger3PreRx = LeftFootExtraFinger3PreR.LeftFootExtraFinger3PreRx
    LeftFootExtraFinger3PreRy = LeftFootExtraFinger3PreR.LeftFootExtraFinger3PreRy
    LeftFootExtraFinger3PreRz = LeftFootExtraFinger3PreR.LeftFootExtraFinger3PreRz

    LeftFootExtraFinger3PostR = LeftFootExtraFinger3PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger3PostRx = LeftFootExtraFinger3PostR.LeftFootExtraFinger3PostRx
    LeftFootExtraFinger3PostRy = LeftFootExtraFinger3PostR.LeftFootExtraFinger3PostRy
    LeftFootExtraFinger3PostRz = LeftFootExtraFinger3PostR.LeftFootExtraFinger3PostRz

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

    LeftFootExtraFinger4PGX = MatrixField()

    LeftFootExtraFinger4ROrder = LeftFootExtraFinger4ROrderEnumField(default_value=0)

    LeftFootExtraFinger4SC = BoolField(default_value=False)

    LeftFootExtraFinger4IS = LeftFootExtraFinger4ISField(default_value=(1.0, 1.0, 1.0))
    LeftFootExtraFinger4ISx = LeftFootExtraFinger4IS.LeftFootExtraFinger4ISx
    LeftFootExtraFinger4ISy = LeftFootExtraFinger4IS.LeftFootExtraFinger4ISy
    LeftFootExtraFinger4ISz = LeftFootExtraFinger4IS.LeftFootExtraFinger4ISz

    LeftFootExtraFinger4PreR = LeftFootExtraFinger4PreRField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger4PreRx = LeftFootExtraFinger4PreR.LeftFootExtraFinger4PreRx
    LeftFootExtraFinger4PreRy = LeftFootExtraFinger4PreR.LeftFootExtraFinger4PreRy
    LeftFootExtraFinger4PreRz = LeftFootExtraFinger4PreR.LeftFootExtraFinger4PreRz

    LeftFootExtraFinger4PostR = LeftFootExtraFinger4PostRField(default_value=(0.0, 0.0, 0.0))
    LeftFootExtraFinger4PostRx = LeftFootExtraFinger4PostR.LeftFootExtraFinger4PostRx
    LeftFootExtraFinger4PostRy = LeftFootExtraFinger4PostR.LeftFootExtraFinger4PostRy
    LeftFootExtraFinger4PostRz = LeftFootExtraFinger4PostR.LeftFootExtraFinger4PostRz

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

    RightFootThumb1PGX = MatrixField()

    RightFootThumb1ROrder = RightFootThumb1ROrderEnumField(default_value=0)

    RightFootThumb1SC = BoolField(default_value=False)

    RightFootThumb1IS = RightFootThumb1ISField(default_value=(1.0, 1.0, 1.0))
    RightFootThumb1ISx = RightFootThumb1IS.RightFootThumb1ISx
    RightFootThumb1ISy = RightFootThumb1IS.RightFootThumb1ISy
    RightFootThumb1ISz = RightFootThumb1IS.RightFootThumb1ISz

    RightFootThumb1PreR = RightFootThumb1PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb1PreRx = RightFootThumb1PreR.RightFootThumb1PreRx
    RightFootThumb1PreRy = RightFootThumb1PreR.RightFootThumb1PreRy
    RightFootThumb1PreRz = RightFootThumb1PreR.RightFootThumb1PreRz

    RightFootThumb1PostR = RightFootThumb1PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb1PostRx = RightFootThumb1PostR.RightFootThumb1PostRx
    RightFootThumb1PostRy = RightFootThumb1PostR.RightFootThumb1PostRy
    RightFootThumb1PostRz = RightFootThumb1PostR.RightFootThumb1PostRz

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

    RightFootThumb2PGX = MatrixField()

    RightFootThumb2ROrder = RightFootThumb2ROrderEnumField(default_value=0)

    RightFootThumb2SC = BoolField(default_value=False)

    RightFootThumb2IS = RightFootThumb2ISField(default_value=(1.0, 1.0, 1.0))
    RightFootThumb2ISx = RightFootThumb2IS.RightFootThumb2ISx
    RightFootThumb2ISy = RightFootThumb2IS.RightFootThumb2ISy
    RightFootThumb2ISz = RightFootThumb2IS.RightFootThumb2ISz

    RightFootThumb2PreR = RightFootThumb2PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb2PreRx = RightFootThumb2PreR.RightFootThumb2PreRx
    RightFootThumb2PreRy = RightFootThumb2PreR.RightFootThumb2PreRy
    RightFootThumb2PreRz = RightFootThumb2PreR.RightFootThumb2PreRz

    RightFootThumb2PostR = RightFootThumb2PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb2PostRx = RightFootThumb2PostR.RightFootThumb2PostRx
    RightFootThumb2PostRy = RightFootThumb2PostR.RightFootThumb2PostRy
    RightFootThumb2PostRz = RightFootThumb2PostR.RightFootThumb2PostRz

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

    RightFootThumb3PGX = MatrixField()

    RightFootThumb3ROrder = RightFootThumb3ROrderEnumField(default_value=0)

    RightFootThumb3SC = BoolField(default_value=False)

    RightFootThumb3IS = RightFootThumb3ISField(default_value=(1.0, 1.0, 1.0))
    RightFootThumb3ISx = RightFootThumb3IS.RightFootThumb3ISx
    RightFootThumb3ISy = RightFootThumb3IS.RightFootThumb3ISy
    RightFootThumb3ISz = RightFootThumb3IS.RightFootThumb3ISz

    RightFootThumb3PreR = RightFootThumb3PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb3PreRx = RightFootThumb3PreR.RightFootThumb3PreRx
    RightFootThumb3PreRy = RightFootThumb3PreR.RightFootThumb3PreRy
    RightFootThumb3PreRz = RightFootThumb3PreR.RightFootThumb3PreRz

    RightFootThumb3PostR = RightFootThumb3PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb3PostRx = RightFootThumb3PostR.RightFootThumb3PostRx
    RightFootThumb3PostRy = RightFootThumb3PostR.RightFootThumb3PostRy
    RightFootThumb3PostRz = RightFootThumb3PostR.RightFootThumb3PostRz

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

    RightFootThumb4PGX = MatrixField()

    RightFootThumb4ROrder = RightFootThumb4ROrderEnumField(default_value=0)

    RightFootThumb4SC = BoolField(default_value=False)

    RightFootThumb4IS = RightFootThumb4ISField(default_value=(1.0, 1.0, 1.0))
    RightFootThumb4ISx = RightFootThumb4IS.RightFootThumb4ISx
    RightFootThumb4ISy = RightFootThumb4IS.RightFootThumb4ISy
    RightFootThumb4ISz = RightFootThumb4IS.RightFootThumb4ISz

    RightFootThumb4PreR = RightFootThumb4PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb4PreRx = RightFootThumb4PreR.RightFootThumb4PreRx
    RightFootThumb4PreRy = RightFootThumb4PreR.RightFootThumb4PreRy
    RightFootThumb4PreRz = RightFootThumb4PreR.RightFootThumb4PreRz

    RightFootThumb4PostR = RightFootThumb4PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootThumb4PostRx = RightFootThumb4PostR.RightFootThumb4PostRx
    RightFootThumb4PostRy = RightFootThumb4PostR.RightFootThumb4PostRy
    RightFootThumb4PostRz = RightFootThumb4PostR.RightFootThumb4PostRz

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

    RightFootIndex1PGX = MatrixField()

    RightFootIndex1ROrder = RightFootIndex1ROrderEnumField(default_value=0)

    RightFootIndex1SC = BoolField(default_value=False)

    RightFootIndex1IS = RightFootIndex1ISField(default_value=(1.0, 1.0, 1.0))
    RightFootIndex1ISx = RightFootIndex1IS.RightFootIndex1ISx
    RightFootIndex1ISy = RightFootIndex1IS.RightFootIndex1ISy
    RightFootIndex1ISz = RightFootIndex1IS.RightFootIndex1ISz

    RightFootIndex1PreR = RightFootIndex1PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex1PreRx = RightFootIndex1PreR.RightFootIndex1PreRx
    RightFootIndex1PreRy = RightFootIndex1PreR.RightFootIndex1PreRy
    RightFootIndex1PreRz = RightFootIndex1PreR.RightFootIndex1PreRz

    RightFootIndex1PostR = RightFootIndex1PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex1PostRx = RightFootIndex1PostR.RightFootIndex1PostRx
    RightFootIndex1PostRy = RightFootIndex1PostR.RightFootIndex1PostRy
    RightFootIndex1PostRz = RightFootIndex1PostR.RightFootIndex1PostRz

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

    RightFootIndex2PGX = MatrixField()

    RightFootIndex2ROrder = RightFootIndex2ROrderEnumField(default_value=0)

    RightFootIndex2SC = BoolField(default_value=False)

    RightFootIndex2IS = RightFootIndex2ISField(default_value=(1.0, 1.0, 1.0))
    RightFootIndex2ISx = RightFootIndex2IS.RightFootIndex2ISx
    RightFootIndex2ISy = RightFootIndex2IS.RightFootIndex2ISy
    RightFootIndex2ISz = RightFootIndex2IS.RightFootIndex2ISz

    RightFootIndex2PreR = RightFootIndex2PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex2PreRx = RightFootIndex2PreR.RightFootIndex2PreRx
    RightFootIndex2PreRy = RightFootIndex2PreR.RightFootIndex2PreRy
    RightFootIndex2PreRz = RightFootIndex2PreR.RightFootIndex2PreRz

    RightFootIndex2PostR = RightFootIndex2PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex2PostRx = RightFootIndex2PostR.RightFootIndex2PostRx
    RightFootIndex2PostRy = RightFootIndex2PostR.RightFootIndex2PostRy
    RightFootIndex2PostRz = RightFootIndex2PostR.RightFootIndex2PostRz

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

    RightFootIndex3PGX = MatrixField()

    RightFootIndex3ROrder = RightFootIndex3ROrderEnumField(default_value=0)

    RightFootIndex3SC = BoolField(default_value=False)

    RightFootIndex3IS = RightFootIndex3ISField(default_value=(1.0, 1.0, 1.0))
    RightFootIndex3ISx = RightFootIndex3IS.RightFootIndex3ISx
    RightFootIndex3ISy = RightFootIndex3IS.RightFootIndex3ISy
    RightFootIndex3ISz = RightFootIndex3IS.RightFootIndex3ISz

    RightFootIndex3PreR = RightFootIndex3PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex3PreRx = RightFootIndex3PreR.RightFootIndex3PreRx
    RightFootIndex3PreRy = RightFootIndex3PreR.RightFootIndex3PreRy
    RightFootIndex3PreRz = RightFootIndex3PreR.RightFootIndex3PreRz

    RightFootIndex3PostR = RightFootIndex3PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex3PostRx = RightFootIndex3PostR.RightFootIndex3PostRx
    RightFootIndex3PostRy = RightFootIndex3PostR.RightFootIndex3PostRy
    RightFootIndex3PostRz = RightFootIndex3PostR.RightFootIndex3PostRz

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

    RightFootIndex4PGX = MatrixField()

    RightFootIndex4ROrder = RightFootIndex4ROrderEnumField(default_value=0)

    RightFootIndex4SC = BoolField(default_value=False)

    RightFootIndex4IS = RightFootIndex4ISField(default_value=(1.0, 1.0, 1.0))
    RightFootIndex4ISx = RightFootIndex4IS.RightFootIndex4ISx
    RightFootIndex4ISy = RightFootIndex4IS.RightFootIndex4ISy
    RightFootIndex4ISz = RightFootIndex4IS.RightFootIndex4ISz

    RightFootIndex4PreR = RightFootIndex4PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex4PreRx = RightFootIndex4PreR.RightFootIndex4PreRx
    RightFootIndex4PreRy = RightFootIndex4PreR.RightFootIndex4PreRy
    RightFootIndex4PreRz = RightFootIndex4PreR.RightFootIndex4PreRz

    RightFootIndex4PostR = RightFootIndex4PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootIndex4PostRx = RightFootIndex4PostR.RightFootIndex4PostRx
    RightFootIndex4PostRy = RightFootIndex4PostR.RightFootIndex4PostRy
    RightFootIndex4PostRz = RightFootIndex4PostR.RightFootIndex4PostRz

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

    RightFootMiddle1PGX = MatrixField()

    RightFootMiddle1ROrder = RightFootMiddle1ROrderEnumField(default_value=0)

    RightFootMiddle1SC = BoolField(default_value=False)

    RightFootMiddle1IS = RightFootMiddle1ISField(default_value=(1.0, 1.0, 1.0))
    RightFootMiddle1ISx = RightFootMiddle1IS.RightFootMiddle1ISx
    RightFootMiddle1ISy = RightFootMiddle1IS.RightFootMiddle1ISy
    RightFootMiddle1ISz = RightFootMiddle1IS.RightFootMiddle1ISz

    RightFootMiddle1PreR = RightFootMiddle1PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle1PreRx = RightFootMiddle1PreR.RightFootMiddle1PreRx
    RightFootMiddle1PreRy = RightFootMiddle1PreR.RightFootMiddle1PreRy
    RightFootMiddle1PreRz = RightFootMiddle1PreR.RightFootMiddle1PreRz

    RightFootMiddle1PostR = RightFootMiddle1PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle1PostRx = RightFootMiddle1PostR.RightFootMiddle1PostRx
    RightFootMiddle1PostRy = RightFootMiddle1PostR.RightFootMiddle1PostRy
    RightFootMiddle1PostRz = RightFootMiddle1PostR.RightFootMiddle1PostRz

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

    RightFootMiddle2PGX = MatrixField()

    RightFootMiddle2ROrder = RightFootMiddle2ROrderEnumField(default_value=0)

    RightFootMiddle2SC = BoolField(default_value=False)

    RightFootMiddle2IS = RightFootMiddle2ISField(default_value=(1.0, 1.0, 1.0))
    RightFootMiddle2ISx = RightFootMiddle2IS.RightFootMiddle2ISx
    RightFootMiddle2ISy = RightFootMiddle2IS.RightFootMiddle2ISy
    RightFootMiddle2ISz = RightFootMiddle2IS.RightFootMiddle2ISz

    RightFootMiddle2PreR = RightFootMiddle2PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle2PreRx = RightFootMiddle2PreR.RightFootMiddle2PreRx
    RightFootMiddle2PreRy = RightFootMiddle2PreR.RightFootMiddle2PreRy
    RightFootMiddle2PreRz = RightFootMiddle2PreR.RightFootMiddle2PreRz

    RightFootMiddle2PostR = RightFootMiddle2PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle2PostRx = RightFootMiddle2PostR.RightFootMiddle2PostRx
    RightFootMiddle2PostRy = RightFootMiddle2PostR.RightFootMiddle2PostRy
    RightFootMiddle2PostRz = RightFootMiddle2PostR.RightFootMiddle2PostRz

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

    RightFootMiddle3PGX = MatrixField()

    RightFootMiddle3ROrder = RightFootMiddle3ROrderEnumField(default_value=0)

    RightFootMiddle3SC = BoolField(default_value=False)

    RightFootMiddle3IS = RightFootMiddle3ISField(default_value=(1.0, 1.0, 1.0))
    RightFootMiddle3ISx = RightFootMiddle3IS.RightFootMiddle3ISx
    RightFootMiddle3ISy = RightFootMiddle3IS.RightFootMiddle3ISy
    RightFootMiddle3ISz = RightFootMiddle3IS.RightFootMiddle3ISz

    RightFootMiddle3PreR = RightFootMiddle3PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle3PreRx = RightFootMiddle3PreR.RightFootMiddle3PreRx
    RightFootMiddle3PreRy = RightFootMiddle3PreR.RightFootMiddle3PreRy
    RightFootMiddle3PreRz = RightFootMiddle3PreR.RightFootMiddle3PreRz

    RightFootMiddle3PostR = RightFootMiddle3PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle3PostRx = RightFootMiddle3PostR.RightFootMiddle3PostRx
    RightFootMiddle3PostRy = RightFootMiddle3PostR.RightFootMiddle3PostRy
    RightFootMiddle3PostRz = RightFootMiddle3PostR.RightFootMiddle3PostRz

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

    RightFootMiddle4PGX = MatrixField()

    RightFootMiddle4ROrder = RightFootMiddle4ROrderEnumField(default_value=0)

    RightFootMiddle4SC = BoolField(default_value=False)

    RightFootMiddle4IS = RightFootMiddle4ISField(default_value=(1.0, 1.0, 1.0))
    RightFootMiddle4ISx = RightFootMiddle4IS.RightFootMiddle4ISx
    RightFootMiddle4ISy = RightFootMiddle4IS.RightFootMiddle4ISy
    RightFootMiddle4ISz = RightFootMiddle4IS.RightFootMiddle4ISz

    RightFootMiddle4PreR = RightFootMiddle4PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle4PreRx = RightFootMiddle4PreR.RightFootMiddle4PreRx
    RightFootMiddle4PreRy = RightFootMiddle4PreR.RightFootMiddle4PreRy
    RightFootMiddle4PreRz = RightFootMiddle4PreR.RightFootMiddle4PreRz

    RightFootMiddle4PostR = RightFootMiddle4PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootMiddle4PostRx = RightFootMiddle4PostR.RightFootMiddle4PostRx
    RightFootMiddle4PostRy = RightFootMiddle4PostR.RightFootMiddle4PostRy
    RightFootMiddle4PostRz = RightFootMiddle4PostR.RightFootMiddle4PostRz

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

    RightFootRing1PGX = MatrixField()

    RightFootRing1ROrder = RightFootRing1ROrderEnumField(default_value=0)

    RightFootRing1SC = BoolField(default_value=False)

    RightFootRing1IS = RightFootRing1ISField(default_value=(1.0, 1.0, 1.0))
    RightFootRing1ISx = RightFootRing1IS.RightFootRing1ISx
    RightFootRing1ISy = RightFootRing1IS.RightFootRing1ISy
    RightFootRing1ISz = RightFootRing1IS.RightFootRing1ISz

    RightFootRing1PreR = RightFootRing1PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootRing1PreRx = RightFootRing1PreR.RightFootRing1PreRx
    RightFootRing1PreRy = RightFootRing1PreR.RightFootRing1PreRy
    RightFootRing1PreRz = RightFootRing1PreR.RightFootRing1PreRz

    RightFootRing1PostR = RightFootRing1PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootRing1PostRx = RightFootRing1PostR.RightFootRing1PostRx
    RightFootRing1PostRy = RightFootRing1PostR.RightFootRing1PostRy
    RightFootRing1PostRz = RightFootRing1PostR.RightFootRing1PostRz

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

    RightFootRing2PGX = MatrixField()

    RightFootRing2ROrder = RightFootRing2ROrderEnumField(default_value=0)

    RightFootRing2SC = BoolField(default_value=False)

    RightFootRing2IS = RightFootRing2ISField(default_value=(1.0, 1.0, 1.0))
    RightFootRing2ISx = RightFootRing2IS.RightFootRing2ISx
    RightFootRing2ISy = RightFootRing2IS.RightFootRing2ISy
    RightFootRing2ISz = RightFootRing2IS.RightFootRing2ISz

    RightFootRing2PreR = RightFootRing2PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootRing2PreRx = RightFootRing2PreR.RightFootRing2PreRx
    RightFootRing2PreRy = RightFootRing2PreR.RightFootRing2PreRy
    RightFootRing2PreRz = RightFootRing2PreR.RightFootRing2PreRz

    RightFootRing2PostR = RightFootRing2PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootRing2PostRx = RightFootRing2PostR.RightFootRing2PostRx
    RightFootRing2PostRy = RightFootRing2PostR.RightFootRing2PostRy
    RightFootRing2PostRz = RightFootRing2PostR.RightFootRing2PostRz

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

    RightFootRing3PGX = MatrixField()

    RightFootRing3ROrder = RightFootRing3ROrderEnumField(default_value=0)

    RightFootRing3SC = BoolField(default_value=False)

    RightFootRing3IS = RightFootRing3ISField(default_value=(1.0, 1.0, 1.0))
    RightFootRing3ISx = RightFootRing3IS.RightFootRing3ISx
    RightFootRing3ISy = RightFootRing3IS.RightFootRing3ISy
    RightFootRing3ISz = RightFootRing3IS.RightFootRing3ISz

    RightFootRing3PreR = RightFootRing3PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootRing3PreRx = RightFootRing3PreR.RightFootRing3PreRx
    RightFootRing3PreRy = RightFootRing3PreR.RightFootRing3PreRy
    RightFootRing3PreRz = RightFootRing3PreR.RightFootRing3PreRz

    RightFootRing3PostR = RightFootRing3PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootRing3PostRx = RightFootRing3PostR.RightFootRing3PostRx
    RightFootRing3PostRy = RightFootRing3PostR.RightFootRing3PostRy
    RightFootRing3PostRz = RightFootRing3PostR.RightFootRing3PostRz

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

    RightFootRing4PGX = MatrixField()

    RightFootRing4ROrder = RightFootRing4ROrderEnumField(default_value=0)

    RightFootRing4SC = BoolField(default_value=False)

    RightFootRing4IS = RightFootRing4ISField(default_value=(1.0, 1.0, 1.0))
    RightFootRing4ISx = RightFootRing4IS.RightFootRing4ISx
    RightFootRing4ISy = RightFootRing4IS.RightFootRing4ISy
    RightFootRing4ISz = RightFootRing4IS.RightFootRing4ISz

    RightFootRing4PreR = RightFootRing4PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootRing4PreRx = RightFootRing4PreR.RightFootRing4PreRx
    RightFootRing4PreRy = RightFootRing4PreR.RightFootRing4PreRy
    RightFootRing4PreRz = RightFootRing4PreR.RightFootRing4PreRz

    RightFootRing4PostR = RightFootRing4PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootRing4PostRx = RightFootRing4PostR.RightFootRing4PostRx
    RightFootRing4PostRy = RightFootRing4PostR.RightFootRing4PostRy
    RightFootRing4PostRz = RightFootRing4PostR.RightFootRing4PostRz

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

    RightFootPinky1PGX = MatrixField()

    RightFootPinky1ROrder = RightFootPinky1ROrderEnumField(default_value=0)

    RightFootPinky1SC = BoolField(default_value=False)

    RightFootPinky1IS = RightFootPinky1ISField(default_value=(1.0, 1.0, 1.0))
    RightFootPinky1ISx = RightFootPinky1IS.RightFootPinky1ISx
    RightFootPinky1ISy = RightFootPinky1IS.RightFootPinky1ISy
    RightFootPinky1ISz = RightFootPinky1IS.RightFootPinky1ISz

    RightFootPinky1PreR = RightFootPinky1PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky1PreRx = RightFootPinky1PreR.RightFootPinky1PreRx
    RightFootPinky1PreRy = RightFootPinky1PreR.RightFootPinky1PreRy
    RightFootPinky1PreRz = RightFootPinky1PreR.RightFootPinky1PreRz

    RightFootPinky1PostR = RightFootPinky1PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky1PostRx = RightFootPinky1PostR.RightFootPinky1PostRx
    RightFootPinky1PostRy = RightFootPinky1PostR.RightFootPinky1PostRy
    RightFootPinky1PostRz = RightFootPinky1PostR.RightFootPinky1PostRz

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

    RightFootPinky2PGX = MatrixField()

    RightFootPinky2ROrder = RightFootPinky2ROrderEnumField(default_value=0)

    RightFootPinky2SC = BoolField(default_value=False)

    RightFootPinky2IS = RightFootPinky2ISField(default_value=(1.0, 1.0, 1.0))
    RightFootPinky2ISx = RightFootPinky2IS.RightFootPinky2ISx
    RightFootPinky2ISy = RightFootPinky2IS.RightFootPinky2ISy
    RightFootPinky2ISz = RightFootPinky2IS.RightFootPinky2ISz

    RightFootPinky2PreR = RightFootPinky2PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky2PreRx = RightFootPinky2PreR.RightFootPinky2PreRx
    RightFootPinky2PreRy = RightFootPinky2PreR.RightFootPinky2PreRy
    RightFootPinky2PreRz = RightFootPinky2PreR.RightFootPinky2PreRz

    RightFootPinky2PostR = RightFootPinky2PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky2PostRx = RightFootPinky2PostR.RightFootPinky2PostRx
    RightFootPinky2PostRy = RightFootPinky2PostR.RightFootPinky2PostRy
    RightFootPinky2PostRz = RightFootPinky2PostR.RightFootPinky2PostRz

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

    RightFootPinky3PGX = MatrixField()

    RightFootPinky3ROrder = RightFootPinky3ROrderEnumField(default_value=0)

    RightFootPinky3SC = BoolField(default_value=False)

    RightFootPinky3IS = RightFootPinky3ISField(default_value=(1.0, 1.0, 1.0))
    RightFootPinky3ISx = RightFootPinky3IS.RightFootPinky3ISx
    RightFootPinky3ISy = RightFootPinky3IS.RightFootPinky3ISy
    RightFootPinky3ISz = RightFootPinky3IS.RightFootPinky3ISz

    RightFootPinky3PreR = RightFootPinky3PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky3PreRx = RightFootPinky3PreR.RightFootPinky3PreRx
    RightFootPinky3PreRy = RightFootPinky3PreR.RightFootPinky3PreRy
    RightFootPinky3PreRz = RightFootPinky3PreR.RightFootPinky3PreRz

    RightFootPinky3PostR = RightFootPinky3PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky3PostRx = RightFootPinky3PostR.RightFootPinky3PostRx
    RightFootPinky3PostRy = RightFootPinky3PostR.RightFootPinky3PostRy
    RightFootPinky3PostRz = RightFootPinky3PostR.RightFootPinky3PostRz

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

    RightFootPinky4PGX = MatrixField()

    RightFootPinky4ROrder = RightFootPinky4ROrderEnumField(default_value=0)

    RightFootPinky4SC = BoolField(default_value=False)

    RightFootPinky4IS = RightFootPinky4ISField(default_value=(1.0, 1.0, 1.0))
    RightFootPinky4ISx = RightFootPinky4IS.RightFootPinky4ISx
    RightFootPinky4ISy = RightFootPinky4IS.RightFootPinky4ISy
    RightFootPinky4ISz = RightFootPinky4IS.RightFootPinky4ISz

    RightFootPinky4PreR = RightFootPinky4PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky4PreRx = RightFootPinky4PreR.RightFootPinky4PreRx
    RightFootPinky4PreRy = RightFootPinky4PreR.RightFootPinky4PreRy
    RightFootPinky4PreRz = RightFootPinky4PreR.RightFootPinky4PreRz

    RightFootPinky4PostR = RightFootPinky4PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootPinky4PostRx = RightFootPinky4PostR.RightFootPinky4PostRx
    RightFootPinky4PostRy = RightFootPinky4PostR.RightFootPinky4PostRy
    RightFootPinky4PostRz = RightFootPinky4PostR.RightFootPinky4PostRz

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

    RightFootExtraFinger1PGX = MatrixField()

    RightFootExtraFinger1ROrder = RightFootExtraFinger1ROrderEnumField(default_value=0)

    RightFootExtraFinger1SC = BoolField(default_value=False)

    RightFootExtraFinger1IS = RightFootExtraFinger1ISField(default_value=(1.0, 1.0, 1.0))
    RightFootExtraFinger1ISx = RightFootExtraFinger1IS.RightFootExtraFinger1ISx
    RightFootExtraFinger1ISy = RightFootExtraFinger1IS.RightFootExtraFinger1ISy
    RightFootExtraFinger1ISz = RightFootExtraFinger1IS.RightFootExtraFinger1ISz

    RightFootExtraFinger1PreR = RightFootExtraFinger1PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger1PreRx = RightFootExtraFinger1PreR.RightFootExtraFinger1PreRx
    RightFootExtraFinger1PreRy = RightFootExtraFinger1PreR.RightFootExtraFinger1PreRy
    RightFootExtraFinger1PreRz = RightFootExtraFinger1PreR.RightFootExtraFinger1PreRz

    RightFootExtraFinger1PostR = RightFootExtraFinger1PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger1PostRx = RightFootExtraFinger1PostR.RightFootExtraFinger1PostRx
    RightFootExtraFinger1PostRy = RightFootExtraFinger1PostR.RightFootExtraFinger1PostRy
    RightFootExtraFinger1PostRz = RightFootExtraFinger1PostR.RightFootExtraFinger1PostRz

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

    RightFootExtraFinger2PGX = MatrixField()

    RightFootExtraFinger2ROrder = RightFootExtraFinger2ROrderEnumField(default_value=0)

    RightFootExtraFinger2SC = BoolField(default_value=False)

    RightFootExtraFinger2IS = RightFootExtraFinger2ISField(default_value=(1.0, 1.0, 1.0))
    RightFootExtraFinger2ISx = RightFootExtraFinger2IS.RightFootExtraFinger2ISx
    RightFootExtraFinger2ISy = RightFootExtraFinger2IS.RightFootExtraFinger2ISy
    RightFootExtraFinger2ISz = RightFootExtraFinger2IS.RightFootExtraFinger2ISz

    RightFootExtraFinger2PreR = RightFootExtraFinger2PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger2PreRx = RightFootExtraFinger2PreR.RightFootExtraFinger2PreRx
    RightFootExtraFinger2PreRy = RightFootExtraFinger2PreR.RightFootExtraFinger2PreRy
    RightFootExtraFinger2PreRz = RightFootExtraFinger2PreR.RightFootExtraFinger2PreRz

    RightFootExtraFinger2PostR = RightFootExtraFinger2PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger2PostRx = RightFootExtraFinger2PostR.RightFootExtraFinger2PostRx
    RightFootExtraFinger2PostRy = RightFootExtraFinger2PostR.RightFootExtraFinger2PostRy
    RightFootExtraFinger2PostRz = RightFootExtraFinger2PostR.RightFootExtraFinger2PostRz

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

    RightFootExtraFinger3PGX = MatrixField()

    RightFootExtraFinger3ROrder = RightFootExtraFinger3ROrderEnumField(default_value=0)

    RightFootExtraFinger3SC = BoolField(default_value=False)

    RightFootExtraFinger3IS = RightFootExtraFinger3ISField(default_value=(1.0, 1.0, 1.0))
    RightFootExtraFinger3ISx = RightFootExtraFinger3IS.RightFootExtraFinger3ISx
    RightFootExtraFinger3ISy = RightFootExtraFinger3IS.RightFootExtraFinger3ISy
    RightFootExtraFinger3ISz = RightFootExtraFinger3IS.RightFootExtraFinger3ISz

    RightFootExtraFinger3PreR = RightFootExtraFinger3PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger3PreRx = RightFootExtraFinger3PreR.RightFootExtraFinger3PreRx
    RightFootExtraFinger3PreRy = RightFootExtraFinger3PreR.RightFootExtraFinger3PreRy
    RightFootExtraFinger3PreRz = RightFootExtraFinger3PreR.RightFootExtraFinger3PreRz

    RightFootExtraFinger3PostR = RightFootExtraFinger3PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger3PostRx = RightFootExtraFinger3PostR.RightFootExtraFinger3PostRx
    RightFootExtraFinger3PostRy = RightFootExtraFinger3PostR.RightFootExtraFinger3PostRy
    RightFootExtraFinger3PostRz = RightFootExtraFinger3PostR.RightFootExtraFinger3PostRz

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

    RightFootExtraFinger4PGX = MatrixField()

    RightFootExtraFinger4ROrder = RightFootExtraFinger4ROrderEnumField(default_value=0)

    RightFootExtraFinger4SC = BoolField(default_value=False)

    RightFootExtraFinger4IS = RightFootExtraFinger4ISField(default_value=(1.0, 1.0, 1.0))
    RightFootExtraFinger4ISx = RightFootExtraFinger4IS.RightFootExtraFinger4ISx
    RightFootExtraFinger4ISy = RightFootExtraFinger4IS.RightFootExtraFinger4ISy
    RightFootExtraFinger4ISz = RightFootExtraFinger4IS.RightFootExtraFinger4ISz

    RightFootExtraFinger4PreR = RightFootExtraFinger4PreRField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger4PreRx = RightFootExtraFinger4PreR.RightFootExtraFinger4PreRx
    RightFootExtraFinger4PreRy = RightFootExtraFinger4PreR.RightFootExtraFinger4PreRy
    RightFootExtraFinger4PreRz = RightFootExtraFinger4PreR.RightFootExtraFinger4PreRz

    RightFootExtraFinger4PostR = RightFootExtraFinger4PostRField(default_value=(0.0, 0.0, 0.0))
    RightFootExtraFinger4PostRx = RightFootExtraFinger4PostR.RightFootExtraFinger4PostRx
    RightFootExtraFinger4PostRy = RightFootExtraFinger4PostR.RightFootExtraFinger4PostRy
    RightFootExtraFinger4PostRz = RightFootExtraFinger4PostR.RightFootExtraFinger4PostRz

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

    LeftInHandThumbPGX = MatrixField()

    LeftInHandThumbROrder = LeftInHandThumbROrderEnumField(default_value=0)

    LeftInHandThumbSC = BoolField(default_value=False)

    LeftInHandThumbIS = LeftInHandThumbISField(default_value=(1.0, 1.0, 1.0))
    LeftInHandThumbISx = LeftInHandThumbIS.LeftInHandThumbISx
    LeftInHandThumbISy = LeftInHandThumbIS.LeftInHandThumbISy
    LeftInHandThumbISz = LeftInHandThumbIS.LeftInHandThumbISz

    LeftInHandThumbPreR = LeftInHandThumbPreRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandThumbPreRx = LeftInHandThumbPreR.LeftInHandThumbPreRx
    LeftInHandThumbPreRy = LeftInHandThumbPreR.LeftInHandThumbPreRy
    LeftInHandThumbPreRz = LeftInHandThumbPreR.LeftInHandThumbPreRz

    LeftInHandThumbPostR = LeftInHandThumbPostRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandThumbPostRx = LeftInHandThumbPostR.LeftInHandThumbPostRx
    LeftInHandThumbPostRy = LeftInHandThumbPostR.LeftInHandThumbPostRy
    LeftInHandThumbPostRz = LeftInHandThumbPostR.LeftInHandThumbPostRz

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

    LeftInHandIndexPGX = MatrixField()

    LeftInHandIndexROrder = LeftInHandIndexROrderEnumField(default_value=0)

    LeftInHandIndexSC = BoolField(default_value=False)

    LeftInHandIndexIS = LeftInHandIndexISField(default_value=(1.0, 1.0, 1.0))
    LeftInHandIndexISx = LeftInHandIndexIS.LeftInHandIndexISx
    LeftInHandIndexISy = LeftInHandIndexIS.LeftInHandIndexISy
    LeftInHandIndexISz = LeftInHandIndexIS.LeftInHandIndexISz

    LeftInHandIndexPreR = LeftInHandIndexPreRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandIndexPreRx = LeftInHandIndexPreR.LeftInHandIndexPreRx
    LeftInHandIndexPreRy = LeftInHandIndexPreR.LeftInHandIndexPreRy
    LeftInHandIndexPreRz = LeftInHandIndexPreR.LeftInHandIndexPreRz

    LeftInHandIndexPostR = LeftInHandIndexPostRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandIndexPostRx = LeftInHandIndexPostR.LeftInHandIndexPostRx
    LeftInHandIndexPostRy = LeftInHandIndexPostR.LeftInHandIndexPostRy
    LeftInHandIndexPostRz = LeftInHandIndexPostR.LeftInHandIndexPostRz

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

    LeftInHandMiddlePGX = MatrixField()

    LeftInHandMiddleROrder = LeftInHandMiddleROrderEnumField(default_value=0)

    LeftInHandMiddleSC = BoolField(default_value=False)

    LeftInHandMiddleIS = LeftInHandMiddleISField(default_value=(1.0, 1.0, 1.0))
    LeftInHandMiddleISx = LeftInHandMiddleIS.LeftInHandMiddleISx
    LeftInHandMiddleISy = LeftInHandMiddleIS.LeftInHandMiddleISy
    LeftInHandMiddleISz = LeftInHandMiddleIS.LeftInHandMiddleISz

    LeftInHandMiddlePreR = LeftInHandMiddlePreRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandMiddlePreRx = LeftInHandMiddlePreR.LeftInHandMiddlePreRx
    LeftInHandMiddlePreRy = LeftInHandMiddlePreR.LeftInHandMiddlePreRy
    LeftInHandMiddlePreRz = LeftInHandMiddlePreR.LeftInHandMiddlePreRz

    LeftInHandMiddlePostR = LeftInHandMiddlePostRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandMiddlePostRx = LeftInHandMiddlePostR.LeftInHandMiddlePostRx
    LeftInHandMiddlePostRy = LeftInHandMiddlePostR.LeftInHandMiddlePostRy
    LeftInHandMiddlePostRz = LeftInHandMiddlePostR.LeftInHandMiddlePostRz

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

    LeftInHandRingPGX = MatrixField()

    LeftInHandRingROrder = LeftInHandRingROrderEnumField(default_value=0)

    LeftInHandRingSC = BoolField(default_value=False)

    LeftInHandRingIS = LeftInHandRingISField(default_value=(1.0, 1.0, 1.0))
    LeftInHandRingISx = LeftInHandRingIS.LeftInHandRingISx
    LeftInHandRingISy = LeftInHandRingIS.LeftInHandRingISy
    LeftInHandRingISz = LeftInHandRingIS.LeftInHandRingISz

    LeftInHandRingPreR = LeftInHandRingPreRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandRingPreRx = LeftInHandRingPreR.LeftInHandRingPreRx
    LeftInHandRingPreRy = LeftInHandRingPreR.LeftInHandRingPreRy
    LeftInHandRingPreRz = LeftInHandRingPreR.LeftInHandRingPreRz

    LeftInHandRingPostR = LeftInHandRingPostRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandRingPostRx = LeftInHandRingPostR.LeftInHandRingPostRx
    LeftInHandRingPostRy = LeftInHandRingPostR.LeftInHandRingPostRy
    LeftInHandRingPostRz = LeftInHandRingPostR.LeftInHandRingPostRz

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

    LeftInHandPinkyPGX = MatrixField()

    LeftInHandPinkyROrder = LeftInHandPinkyROrderEnumField(default_value=0)

    LeftInHandPinkySC = BoolField(default_value=False)

    LeftInHandPinkyIS = LeftInHandPinkyISField(default_value=(1.0, 1.0, 1.0))
    LeftInHandPinkyISx = LeftInHandPinkyIS.LeftInHandPinkyISx
    LeftInHandPinkyISy = LeftInHandPinkyIS.LeftInHandPinkyISy
    LeftInHandPinkyISz = LeftInHandPinkyIS.LeftInHandPinkyISz

    LeftInHandPinkyPreR = LeftInHandPinkyPreRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandPinkyPreRx = LeftInHandPinkyPreR.LeftInHandPinkyPreRx
    LeftInHandPinkyPreRy = LeftInHandPinkyPreR.LeftInHandPinkyPreRy
    LeftInHandPinkyPreRz = LeftInHandPinkyPreR.LeftInHandPinkyPreRz

    LeftInHandPinkyPostR = LeftInHandPinkyPostRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandPinkyPostRx = LeftInHandPinkyPostR.LeftInHandPinkyPostRx
    LeftInHandPinkyPostRy = LeftInHandPinkyPostR.LeftInHandPinkyPostRy
    LeftInHandPinkyPostRz = LeftInHandPinkyPostR.LeftInHandPinkyPostRz

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

    LeftInHandExtraFingerPGX = MatrixField()

    LeftInHandExtraFingerROrder = LeftInHandExtraFingerROrderEnumField(default_value=0)

    LeftInHandExtraFingerSC = BoolField(default_value=False)

    LeftInHandExtraFingerIS = LeftInHandExtraFingerISField(default_value=(1.0, 1.0, 1.0))
    LeftInHandExtraFingerISx = LeftInHandExtraFingerIS.LeftInHandExtraFingerISx
    LeftInHandExtraFingerISy = LeftInHandExtraFingerIS.LeftInHandExtraFingerISy
    LeftInHandExtraFingerISz = LeftInHandExtraFingerIS.LeftInHandExtraFingerISz

    LeftInHandExtraFingerPreR = LeftInHandExtraFingerPreRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandExtraFingerPreRx = LeftInHandExtraFingerPreR.LeftInHandExtraFingerPreRx
    LeftInHandExtraFingerPreRy = LeftInHandExtraFingerPreR.LeftInHandExtraFingerPreRy
    LeftInHandExtraFingerPreRz = LeftInHandExtraFingerPreR.LeftInHandExtraFingerPreRz

    LeftInHandExtraFingerPostR = LeftInHandExtraFingerPostRField(default_value=(0.0, 0.0, 0.0))
    LeftInHandExtraFingerPostRx = LeftInHandExtraFingerPostR.LeftInHandExtraFingerPostRx
    LeftInHandExtraFingerPostRy = LeftInHandExtraFingerPostR.LeftInHandExtraFingerPostRy
    LeftInHandExtraFingerPostRz = LeftInHandExtraFingerPostR.LeftInHandExtraFingerPostRz

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

    RightInHandThumbPGX = MatrixField()

    RightInHandThumbROrder = RightInHandThumbROrderEnumField(default_value=0)

    RightInHandThumbSC = BoolField(default_value=False)

    RightInHandThumbIS = RightInHandThumbISField(default_value=(1.0, 1.0, 1.0))
    RightInHandThumbISx = RightInHandThumbIS.RightInHandThumbISx
    RightInHandThumbISy = RightInHandThumbIS.RightInHandThumbISy
    RightInHandThumbISz = RightInHandThumbIS.RightInHandThumbISz

    RightInHandThumbPreR = RightInHandThumbPreRField(default_value=(0.0, 0.0, 0.0))
    RightInHandThumbPreRx = RightInHandThumbPreR.RightInHandThumbPreRx
    RightInHandThumbPreRy = RightInHandThumbPreR.RightInHandThumbPreRy
    RightInHandThumbPreRz = RightInHandThumbPreR.RightInHandThumbPreRz

    RightInHandThumbPostR = RightInHandThumbPostRField(default_value=(0.0, 0.0, 0.0))
    RightInHandThumbPostRx = RightInHandThumbPostR.RightInHandThumbPostRx
    RightInHandThumbPostRy = RightInHandThumbPostR.RightInHandThumbPostRy
    RightInHandThumbPostRz = RightInHandThumbPostR.RightInHandThumbPostRz

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

    RightInHandIndexPGX = MatrixField()

    RightInHandIndexROrder = RightInHandIndexROrderEnumField(default_value=0)

    RightInHandIndexSC = BoolField(default_value=False)

    RightInHandIndexIS = RightInHandIndexISField(default_value=(1.0, 1.0, 1.0))
    RightInHandIndexISx = RightInHandIndexIS.RightInHandIndexISx
    RightInHandIndexISy = RightInHandIndexIS.RightInHandIndexISy
    RightInHandIndexISz = RightInHandIndexIS.RightInHandIndexISz

    RightInHandIndexPreR = RightInHandIndexPreRField(default_value=(0.0, 0.0, 0.0))
    RightInHandIndexPreRx = RightInHandIndexPreR.RightInHandIndexPreRx
    RightInHandIndexPreRy = RightInHandIndexPreR.RightInHandIndexPreRy
    RightInHandIndexPreRz = RightInHandIndexPreR.RightInHandIndexPreRz

    RightInHandIndexPostR = RightInHandIndexPostRField(default_value=(0.0, 0.0, 0.0))
    RightInHandIndexPostRx = RightInHandIndexPostR.RightInHandIndexPostRx
    RightInHandIndexPostRy = RightInHandIndexPostR.RightInHandIndexPostRy
    RightInHandIndexPostRz = RightInHandIndexPostR.RightInHandIndexPostRz

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

    RightInHandMiddlePGX = MatrixField()

    RightInHandMiddleROrder = RightInHandMiddleROrderEnumField(default_value=0)

    RightInHandMiddleSC = BoolField(default_value=False)

    RightInHandMiddleIS = RightInHandMiddleISField(default_value=(1.0, 1.0, 1.0))
    RightInHandMiddleISx = RightInHandMiddleIS.RightInHandMiddleISx
    RightInHandMiddleISy = RightInHandMiddleIS.RightInHandMiddleISy
    RightInHandMiddleISz = RightInHandMiddleIS.RightInHandMiddleISz

    RightInHandMiddlePreR = RightInHandMiddlePreRField(default_value=(0.0, 0.0, 0.0))
    RightInHandMiddlePreRx = RightInHandMiddlePreR.RightInHandMiddlePreRx
    RightInHandMiddlePreRy = RightInHandMiddlePreR.RightInHandMiddlePreRy
    RightInHandMiddlePreRz = RightInHandMiddlePreR.RightInHandMiddlePreRz

    RightInHandMiddlePostR = RightInHandMiddlePostRField(default_value=(0.0, 0.0, 0.0))
    RightInHandMiddlePostRx = RightInHandMiddlePostR.RightInHandMiddlePostRx
    RightInHandMiddlePostRy = RightInHandMiddlePostR.RightInHandMiddlePostRy
    RightInHandMiddlePostRz = RightInHandMiddlePostR.RightInHandMiddlePostRz

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

    RightInHandRingPGX = MatrixField()

    RightInHandRingROrder = RightInHandRingROrderEnumField(default_value=0)

    RightInHandRingSC = BoolField(default_value=False)

    RightInHandRingIS = RightInHandRingISField(default_value=(1.0, 1.0, 1.0))
    RightInHandRingISx = RightInHandRingIS.RightInHandRingISx
    RightInHandRingISy = RightInHandRingIS.RightInHandRingISy
    RightInHandRingISz = RightInHandRingIS.RightInHandRingISz

    RightInHandRingPreR = RightInHandRingPreRField(default_value=(0.0, 0.0, 0.0))
    RightInHandRingPreRx = RightInHandRingPreR.RightInHandRingPreRx
    RightInHandRingPreRy = RightInHandRingPreR.RightInHandRingPreRy
    RightInHandRingPreRz = RightInHandRingPreR.RightInHandRingPreRz

    RightInHandRingPostR = RightInHandRingPostRField(default_value=(0.0, 0.0, 0.0))
    RightInHandRingPostRx = RightInHandRingPostR.RightInHandRingPostRx
    RightInHandRingPostRy = RightInHandRingPostR.RightInHandRingPostRy
    RightInHandRingPostRz = RightInHandRingPostR.RightInHandRingPostRz

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

    RightInHandPinkyPGX = MatrixField()

    RightInHandPinkyROrder = RightInHandPinkyROrderEnumField(default_value=0)

    RightInHandPinkySC = BoolField(default_value=False)

    RightInHandPinkyIS = RightInHandPinkyISField(default_value=(1.0, 1.0, 1.0))
    RightInHandPinkyISx = RightInHandPinkyIS.RightInHandPinkyISx
    RightInHandPinkyISy = RightInHandPinkyIS.RightInHandPinkyISy
    RightInHandPinkyISz = RightInHandPinkyIS.RightInHandPinkyISz

    RightInHandPinkyPreR = RightInHandPinkyPreRField(default_value=(0.0, 0.0, 0.0))
    RightInHandPinkyPreRx = RightInHandPinkyPreR.RightInHandPinkyPreRx
    RightInHandPinkyPreRy = RightInHandPinkyPreR.RightInHandPinkyPreRy
    RightInHandPinkyPreRz = RightInHandPinkyPreR.RightInHandPinkyPreRz

    RightInHandPinkyPostR = RightInHandPinkyPostRField(default_value=(0.0, 0.0, 0.0))
    RightInHandPinkyPostRx = RightInHandPinkyPostR.RightInHandPinkyPostRx
    RightInHandPinkyPostRy = RightInHandPinkyPostR.RightInHandPinkyPostRy
    RightInHandPinkyPostRz = RightInHandPinkyPostR.RightInHandPinkyPostRz

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

    RightInHandExtraFingerPGX = MatrixField()

    RightInHandExtraFingerROrder = RightInHandExtraFingerROrderEnumField(default_value=0)

    RightInHandExtraFingerSC = BoolField(default_value=False)

    RightInHandExtraFingerIS = RightInHandExtraFingerISField(default_value=(1.0, 1.0, 1.0))
    RightInHandExtraFingerISx = RightInHandExtraFingerIS.RightInHandExtraFingerISx
    RightInHandExtraFingerISy = RightInHandExtraFingerIS.RightInHandExtraFingerISy
    RightInHandExtraFingerISz = RightInHandExtraFingerIS.RightInHandExtraFingerISz

    RightInHandExtraFingerPreR = RightInHandExtraFingerPreRField(default_value=(0.0, 0.0, 0.0))
    RightInHandExtraFingerPreRx = RightInHandExtraFingerPreR.RightInHandExtraFingerPreRx
    RightInHandExtraFingerPreRy = RightInHandExtraFingerPreR.RightInHandExtraFingerPreRy
    RightInHandExtraFingerPreRz = RightInHandExtraFingerPreR.RightInHandExtraFingerPreRz

    RightInHandExtraFingerPostR = RightInHandExtraFingerPostRField(default_value=(0.0, 0.0, 0.0))
    RightInHandExtraFingerPostRx = RightInHandExtraFingerPostR.RightInHandExtraFingerPostRx
    RightInHandExtraFingerPostRy = RightInHandExtraFingerPostR.RightInHandExtraFingerPostRy
    RightInHandExtraFingerPostRz = RightInHandExtraFingerPostR.RightInHandExtraFingerPostRz

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

    LeftInFootThumbPGX = MatrixField()

    LeftInFootThumbROrder = LeftInFootThumbROrderEnumField(default_value=0)

    LeftInFootThumbSC = BoolField(default_value=False)

    LeftInFootThumbIS = LeftInFootThumbISField(default_value=(1.0, 1.0, 1.0))
    LeftInFootThumbISx = LeftInFootThumbIS.LeftInFootThumbISx
    LeftInFootThumbISy = LeftInFootThumbIS.LeftInFootThumbISy
    LeftInFootThumbISz = LeftInFootThumbIS.LeftInFootThumbISz

    LeftInFootThumbPreR = LeftInFootThumbPreRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootThumbPreRx = LeftInFootThumbPreR.LeftInFootThumbPreRx
    LeftInFootThumbPreRy = LeftInFootThumbPreR.LeftInFootThumbPreRy
    LeftInFootThumbPreRz = LeftInFootThumbPreR.LeftInFootThumbPreRz

    LeftInFootThumbPostR = LeftInFootThumbPostRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootThumbPostRx = LeftInFootThumbPostR.LeftInFootThumbPostRx
    LeftInFootThumbPostRy = LeftInFootThumbPostR.LeftInFootThumbPostRy
    LeftInFootThumbPostRz = LeftInFootThumbPostR.LeftInFootThumbPostRz

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

    LeftInFootIndexPGX = MatrixField()

    LeftInFootIndexROrder = LeftInFootIndexROrderEnumField(default_value=0)

    LeftInFootIndexSC = BoolField(default_value=False)

    LeftInFootIndexIS = LeftInFootIndexISField(default_value=(1.0, 1.0, 1.0))
    LeftInFootIndexISx = LeftInFootIndexIS.LeftInFootIndexISx
    LeftInFootIndexISy = LeftInFootIndexIS.LeftInFootIndexISy
    LeftInFootIndexISz = LeftInFootIndexIS.LeftInFootIndexISz

    LeftInFootIndexPreR = LeftInFootIndexPreRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootIndexPreRx = LeftInFootIndexPreR.LeftInFootIndexPreRx
    LeftInFootIndexPreRy = LeftInFootIndexPreR.LeftInFootIndexPreRy
    LeftInFootIndexPreRz = LeftInFootIndexPreR.LeftInFootIndexPreRz

    LeftInFootIndexPostR = LeftInFootIndexPostRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootIndexPostRx = LeftInFootIndexPostR.LeftInFootIndexPostRx
    LeftInFootIndexPostRy = LeftInFootIndexPostR.LeftInFootIndexPostRy
    LeftInFootIndexPostRz = LeftInFootIndexPostR.LeftInFootIndexPostRz

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

    LeftInFootMiddlePGX = MatrixField()

    LeftInFootMiddleROrder = LeftInFootMiddleROrderEnumField(default_value=0)

    LeftInFootMiddleSC = BoolField(default_value=False)

    LeftInFootMiddleIS = LeftInFootMiddleISField(default_value=(1.0, 1.0, 1.0))
    LeftInFootMiddleISx = LeftInFootMiddleIS.LeftInFootMiddleISx
    LeftInFootMiddleISy = LeftInFootMiddleIS.LeftInFootMiddleISy
    LeftInFootMiddleISz = LeftInFootMiddleIS.LeftInFootMiddleISz

    LeftInFootMiddlePreR = LeftInFootMiddlePreRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootMiddlePreRx = LeftInFootMiddlePreR.LeftInFootMiddlePreRx
    LeftInFootMiddlePreRy = LeftInFootMiddlePreR.LeftInFootMiddlePreRy
    LeftInFootMiddlePreRz = LeftInFootMiddlePreR.LeftInFootMiddlePreRz

    LeftInFootMiddlePostR = LeftInFootMiddlePostRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootMiddlePostRx = LeftInFootMiddlePostR.LeftInFootMiddlePostRx
    LeftInFootMiddlePostRy = LeftInFootMiddlePostR.LeftInFootMiddlePostRy
    LeftInFootMiddlePostRz = LeftInFootMiddlePostR.LeftInFootMiddlePostRz

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

    LeftInFootRingPGX = MatrixField()

    LeftInFootRingROrder = LeftInFootRingROrderEnumField(default_value=0)

    LeftInFootRingSC = BoolField(default_value=False)

    LeftInFootRingIS = LeftInFootRingISField(default_value=(1.0, 1.0, 1.0))
    LeftInFootRingISx = LeftInFootRingIS.LeftInFootRingISx
    LeftInFootRingISy = LeftInFootRingIS.LeftInFootRingISy
    LeftInFootRingISz = LeftInFootRingIS.LeftInFootRingISz

    LeftInFootRingPreR = LeftInFootRingPreRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootRingPreRx = LeftInFootRingPreR.LeftInFootRingPreRx
    LeftInFootRingPreRy = LeftInFootRingPreR.LeftInFootRingPreRy
    LeftInFootRingPreRz = LeftInFootRingPreR.LeftInFootRingPreRz

    LeftInFootRingPostR = LeftInFootRingPostRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootRingPostRx = LeftInFootRingPostR.LeftInFootRingPostRx
    LeftInFootRingPostRy = LeftInFootRingPostR.LeftInFootRingPostRy
    LeftInFootRingPostRz = LeftInFootRingPostR.LeftInFootRingPostRz

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

    LeftInFootPinkyPGX = MatrixField()

    LeftInFootPinkyROrder = LeftInFootPinkyROrderEnumField(default_value=0)

    LeftInFootPinkySC = BoolField(default_value=False)

    LeftInFootPinkyIS = LeftInFootPinkyISField(default_value=(1.0, 1.0, 1.0))
    LeftInFootPinkyISx = LeftInFootPinkyIS.LeftInFootPinkyISx
    LeftInFootPinkyISy = LeftInFootPinkyIS.LeftInFootPinkyISy
    LeftInFootPinkyISz = LeftInFootPinkyIS.LeftInFootPinkyISz

    LeftInFootPinkyPreR = LeftInFootPinkyPreRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootPinkyPreRx = LeftInFootPinkyPreR.LeftInFootPinkyPreRx
    LeftInFootPinkyPreRy = LeftInFootPinkyPreR.LeftInFootPinkyPreRy
    LeftInFootPinkyPreRz = LeftInFootPinkyPreR.LeftInFootPinkyPreRz

    LeftInFootPinkyPostR = LeftInFootPinkyPostRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootPinkyPostRx = LeftInFootPinkyPostR.LeftInFootPinkyPostRx
    LeftInFootPinkyPostRy = LeftInFootPinkyPostR.LeftInFootPinkyPostRy
    LeftInFootPinkyPostRz = LeftInFootPinkyPostR.LeftInFootPinkyPostRz

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

    LeftInFootExtraFingerPGX = MatrixField()

    LeftInFootExtraFingerROrder = LeftInFootExtraFingerROrderEnumField(default_value=0)

    LeftInFootExtraFingerSC = BoolField(default_value=False)

    LeftInFootExtraFingerIS = LeftInFootExtraFingerISField(default_value=(1.0, 1.0, 1.0))
    LeftInFootExtraFingerISx = LeftInFootExtraFingerIS.LeftInFootExtraFingerISx
    LeftInFootExtraFingerISy = LeftInFootExtraFingerIS.LeftInFootExtraFingerISy
    LeftInFootExtraFingerISz = LeftInFootExtraFingerIS.LeftInFootExtraFingerISz

    LeftInFootExtraFingerPreR = LeftInFootExtraFingerPreRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootExtraFingerPreRx = LeftInFootExtraFingerPreR.LeftInFootExtraFingerPreRx
    LeftInFootExtraFingerPreRy = LeftInFootExtraFingerPreR.LeftInFootExtraFingerPreRy
    LeftInFootExtraFingerPreRz = LeftInFootExtraFingerPreR.LeftInFootExtraFingerPreRz

    LeftInFootExtraFingerPostR = LeftInFootExtraFingerPostRField(default_value=(0.0, 0.0, 0.0))
    LeftInFootExtraFingerPostRx = LeftInFootExtraFingerPostR.LeftInFootExtraFingerPostRx
    LeftInFootExtraFingerPostRy = LeftInFootExtraFingerPostR.LeftInFootExtraFingerPostRy
    LeftInFootExtraFingerPostRz = LeftInFootExtraFingerPostR.LeftInFootExtraFingerPostRz

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

    RightInFootThumbPGX = MatrixField()

    RightInFootThumbROrder = RightInFootThumbROrderEnumField(default_value=0)

    RightInFootThumbSC = BoolField(default_value=False)

    RightInFootThumbIS = RightInFootThumbISField(default_value=(1.0, 1.0, 1.0))
    RightInFootThumbISx = RightInFootThumbIS.RightInFootThumbISx
    RightInFootThumbISy = RightInFootThumbIS.RightInFootThumbISy
    RightInFootThumbISz = RightInFootThumbIS.RightInFootThumbISz

    RightInFootThumbPreR = RightInFootThumbPreRField(default_value=(0.0, 0.0, 0.0))
    RightInFootThumbPreRx = RightInFootThumbPreR.RightInFootThumbPreRx
    RightInFootThumbPreRy = RightInFootThumbPreR.RightInFootThumbPreRy
    RightInFootThumbPreRz = RightInFootThumbPreR.RightInFootThumbPreRz

    RightInFootThumbPostR = RightInFootThumbPostRField(default_value=(0.0, 0.0, 0.0))
    RightInFootThumbPostRx = RightInFootThumbPostR.RightInFootThumbPostRx
    RightInFootThumbPostRy = RightInFootThumbPostR.RightInFootThumbPostRy
    RightInFootThumbPostRz = RightInFootThumbPostR.RightInFootThumbPostRz

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

    RightInFootIndexPGX = MatrixField()

    RightInFootIndexROrder = RightInFootIndexROrderEnumField(default_value=0)

    RightInFootIndexSC = BoolField(default_value=False)

    RightInFootIndexIS = RightInFootIndexISField(default_value=(1.0, 1.0, 1.0))
    RightInFootIndexISx = RightInFootIndexIS.RightInFootIndexISx
    RightInFootIndexISy = RightInFootIndexIS.RightInFootIndexISy
    RightInFootIndexISz = RightInFootIndexIS.RightInFootIndexISz

    RightInFootIndexPreR = RightInFootIndexPreRField(default_value=(0.0, 0.0, 0.0))
    RightInFootIndexPreRx = RightInFootIndexPreR.RightInFootIndexPreRx
    RightInFootIndexPreRy = RightInFootIndexPreR.RightInFootIndexPreRy
    RightInFootIndexPreRz = RightInFootIndexPreR.RightInFootIndexPreRz

    RightInFootIndexPostR = RightInFootIndexPostRField(default_value=(0.0, 0.0, 0.0))
    RightInFootIndexPostRx = RightInFootIndexPostR.RightInFootIndexPostRx
    RightInFootIndexPostRy = RightInFootIndexPostR.RightInFootIndexPostRy
    RightInFootIndexPostRz = RightInFootIndexPostR.RightInFootIndexPostRz

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

    RightInFootMiddlePGX = MatrixField()

    RightInFootMiddleROrder = RightInFootMiddleROrderEnumField(default_value=0)

    RightInFootMiddleSC = BoolField(default_value=False)

    RightInFootMiddleIS = RightInFootMiddleISField(default_value=(1.0, 1.0, 1.0))
    RightInFootMiddleISx = RightInFootMiddleIS.RightInFootMiddleISx
    RightInFootMiddleISy = RightInFootMiddleIS.RightInFootMiddleISy
    RightInFootMiddleISz = RightInFootMiddleIS.RightInFootMiddleISz

    RightInFootMiddlePreR = RightInFootMiddlePreRField(default_value=(0.0, 0.0, 0.0))
    RightInFootMiddlePreRx = RightInFootMiddlePreR.RightInFootMiddlePreRx
    RightInFootMiddlePreRy = RightInFootMiddlePreR.RightInFootMiddlePreRy
    RightInFootMiddlePreRz = RightInFootMiddlePreR.RightInFootMiddlePreRz

    RightInFootMiddlePostR = RightInFootMiddlePostRField(default_value=(0.0, 0.0, 0.0))
    RightInFootMiddlePostRx = RightInFootMiddlePostR.RightInFootMiddlePostRx
    RightInFootMiddlePostRy = RightInFootMiddlePostR.RightInFootMiddlePostRy
    RightInFootMiddlePostRz = RightInFootMiddlePostR.RightInFootMiddlePostRz

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

    RightInFootRingPGX = MatrixField()

    RightInFootRingROrder = RightInFootRingROrderEnumField(default_value=0)

    RightInFootRingSC = BoolField(default_value=False)

    RightInFootRingIS = RightInFootRingISField(default_value=(1.0, 1.0, 1.0))
    RightInFootRingISx = RightInFootRingIS.RightInFootRingISx
    RightInFootRingISy = RightInFootRingIS.RightInFootRingISy
    RightInFootRingISz = RightInFootRingIS.RightInFootRingISz

    RightInFootRingPreR = RightInFootRingPreRField(default_value=(0.0, 0.0, 0.0))
    RightInFootRingPreRx = RightInFootRingPreR.RightInFootRingPreRx
    RightInFootRingPreRy = RightInFootRingPreR.RightInFootRingPreRy
    RightInFootRingPreRz = RightInFootRingPreR.RightInFootRingPreRz

    RightInFootRingPostR = RightInFootRingPostRField(default_value=(0.0, 0.0, 0.0))
    RightInFootRingPostRx = RightInFootRingPostR.RightInFootRingPostRx
    RightInFootRingPostRy = RightInFootRingPostR.RightInFootRingPostRy
    RightInFootRingPostRz = RightInFootRingPostR.RightInFootRingPostRz

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

    RightInFootPinkyPGX = MatrixField()

    RightInFootPinkyROrder = RightInFootPinkyROrderEnumField(default_value=0)

    RightInFootPinkySC = BoolField(default_value=False)

    RightInFootPinkyIS = RightInFootPinkyISField(default_value=(1.0, 1.0, 1.0))
    RightInFootPinkyISx = RightInFootPinkyIS.RightInFootPinkyISx
    RightInFootPinkyISy = RightInFootPinkyIS.RightInFootPinkyISy
    RightInFootPinkyISz = RightInFootPinkyIS.RightInFootPinkyISz

    RightInFootPinkyPreR = RightInFootPinkyPreRField(default_value=(0.0, 0.0, 0.0))
    RightInFootPinkyPreRx = RightInFootPinkyPreR.RightInFootPinkyPreRx
    RightInFootPinkyPreRy = RightInFootPinkyPreR.RightInFootPinkyPreRy
    RightInFootPinkyPreRz = RightInFootPinkyPreR.RightInFootPinkyPreRz

    RightInFootPinkyPostR = RightInFootPinkyPostRField(default_value=(0.0, 0.0, 0.0))
    RightInFootPinkyPostRx = RightInFootPinkyPostR.RightInFootPinkyPostRx
    RightInFootPinkyPostRy = RightInFootPinkyPostR.RightInFootPinkyPostRy
    RightInFootPinkyPostRz = RightInFootPinkyPostR.RightInFootPinkyPostRz

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

    RightInFootExtraFingerPGX = MatrixField()

    RightInFootExtraFingerROrder = RightInFootExtraFingerROrderEnumField(default_value=0)

    RightInFootExtraFingerSC = BoolField(default_value=False)

    RightInFootExtraFingerIS = RightInFootExtraFingerISField(default_value=(1.0, 1.0, 1.0))
    RightInFootExtraFingerISx = RightInFootExtraFingerIS.RightInFootExtraFingerISx
    RightInFootExtraFingerISy = RightInFootExtraFingerIS.RightInFootExtraFingerISy
    RightInFootExtraFingerISz = RightInFootExtraFingerIS.RightInFootExtraFingerISz

    RightInFootExtraFingerPreR = RightInFootExtraFingerPreRField(default_value=(0.0, 0.0, 0.0))
    RightInFootExtraFingerPreRx = RightInFootExtraFingerPreR.RightInFootExtraFingerPreRx
    RightInFootExtraFingerPreRy = RightInFootExtraFingerPreR.RightInFootExtraFingerPreRy
    RightInFootExtraFingerPreRz = RightInFootExtraFingerPreR.RightInFootExtraFingerPreRz

    RightInFootExtraFingerPostR = RightInFootExtraFingerPostRField(default_value=(0.0, 0.0, 0.0))
    RightInFootExtraFingerPostRx = RightInFootExtraFingerPostR.RightInFootExtraFingerPostRx
    RightInFootExtraFingerPostRy = RightInFootExtraFingerPostR.RightInFootExtraFingerPostRy
    RightInFootExtraFingerPostRz = RightInFootExtraFingerPostR.RightInFootExtraFingerPostRz

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

    LeftShoulderExtraPGX = MatrixField()

    LeftShoulderExtraROrder = LeftShoulderExtraROrderEnumField(default_value=0)

    LeftShoulderExtraSC = BoolField(default_value=False)

    LeftShoulderExtraIS = LeftShoulderExtraISField(default_value=(1.0, 1.0, 1.0))
    LeftShoulderExtraISx = LeftShoulderExtraIS.LeftShoulderExtraISx
    LeftShoulderExtraISy = LeftShoulderExtraIS.LeftShoulderExtraISy
    LeftShoulderExtraISz = LeftShoulderExtraIS.LeftShoulderExtraISz

    LeftShoulderExtraPreR = LeftShoulderExtraPreRField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderExtraPreRx = LeftShoulderExtraPreR.LeftShoulderExtraPreRx
    LeftShoulderExtraPreRy = LeftShoulderExtraPreR.LeftShoulderExtraPreRy
    LeftShoulderExtraPreRz = LeftShoulderExtraPreR.LeftShoulderExtraPreRz

    LeftShoulderExtraPostR = LeftShoulderExtraPostRField(default_value=(0.0, 0.0, 0.0))
    LeftShoulderExtraPostRx = LeftShoulderExtraPostR.LeftShoulderExtraPostRx
    LeftShoulderExtraPostRy = LeftShoulderExtraPostR.LeftShoulderExtraPostRy
    LeftShoulderExtraPostRz = LeftShoulderExtraPostR.LeftShoulderExtraPostRz

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

    RightShoulderExtraPGX = MatrixField()

    RightShoulderExtraROrder = RightShoulderExtraROrderEnumField(default_value=0)

    RightShoulderExtraSC = BoolField(default_value=False)

    RightShoulderExtraIS = RightShoulderExtraISField(default_value=(1.0, 1.0, 1.0))
    RightShoulderExtraISx = RightShoulderExtraIS.RightShoulderExtraISx
    RightShoulderExtraISy = RightShoulderExtraIS.RightShoulderExtraISy
    RightShoulderExtraISz = RightShoulderExtraIS.RightShoulderExtraISz

    RightShoulderExtraPreR = RightShoulderExtraPreRField(default_value=(0.0, 0.0, 0.0))
    RightShoulderExtraPreRx = RightShoulderExtraPreR.RightShoulderExtraPreRx
    RightShoulderExtraPreRy = RightShoulderExtraPreR.RightShoulderExtraPreRy
    RightShoulderExtraPreRz = RightShoulderExtraPreR.RightShoulderExtraPreRz

    RightShoulderExtraPostR = RightShoulderExtraPostRField(default_value=(0.0, 0.0, 0.0))
    RightShoulderExtraPostRx = RightShoulderExtraPostR.RightShoulderExtraPostRx
    RightShoulderExtraPostRy = RightShoulderExtraPostR.RightShoulderExtraPostRy
    RightShoulderExtraPostRz = RightShoulderExtraPostR.RightShoulderExtraPostRz

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

    LeafLeftUpLegRoll1PGX = MatrixField()

    LeafLeftUpLegRoll1ROrder = LeafLeftUpLegRoll1ROrderEnumField(default_value=0)

    LeafLeftUpLegRoll1SC = BoolField(default_value=False)

    LeafLeftUpLegRoll1IS = LeafLeftUpLegRoll1ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftUpLegRoll1ISx = LeafLeftUpLegRoll1IS.LeafLeftUpLegRoll1ISx
    LeafLeftUpLegRoll1ISy = LeafLeftUpLegRoll1IS.LeafLeftUpLegRoll1ISy
    LeafLeftUpLegRoll1ISz = LeafLeftUpLegRoll1IS.LeafLeftUpLegRoll1ISz

    LeafLeftUpLegRoll1PreR = LeafLeftUpLegRoll1PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll1PreRx = LeafLeftUpLegRoll1PreR.LeafLeftUpLegRoll1PreRx
    LeafLeftUpLegRoll1PreRy = LeafLeftUpLegRoll1PreR.LeafLeftUpLegRoll1PreRy
    LeafLeftUpLegRoll1PreRz = LeafLeftUpLegRoll1PreR.LeafLeftUpLegRoll1PreRz

    LeafLeftUpLegRoll1PostR = LeafLeftUpLegRoll1PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll1PostRx = LeafLeftUpLegRoll1PostR.LeafLeftUpLegRoll1PostRx
    LeafLeftUpLegRoll1PostRy = LeafLeftUpLegRoll1PostR.LeafLeftUpLegRoll1PostRy
    LeafLeftUpLegRoll1PostRz = LeafLeftUpLegRoll1PostR.LeafLeftUpLegRoll1PostRz

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

    LeafLeftLegRoll1PGX = MatrixField()

    LeafLeftLegRoll1ROrder = LeafLeftLegRoll1ROrderEnumField(default_value=0)

    LeafLeftLegRoll1SC = BoolField(default_value=False)

    LeafLeftLegRoll1IS = LeafLeftLegRoll1ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftLegRoll1ISx = LeafLeftLegRoll1IS.LeafLeftLegRoll1ISx
    LeafLeftLegRoll1ISy = LeafLeftLegRoll1IS.LeafLeftLegRoll1ISy
    LeafLeftLegRoll1ISz = LeafLeftLegRoll1IS.LeafLeftLegRoll1ISz

    LeafLeftLegRoll1PreR = LeafLeftLegRoll1PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll1PreRx = LeafLeftLegRoll1PreR.LeafLeftLegRoll1PreRx
    LeafLeftLegRoll1PreRy = LeafLeftLegRoll1PreR.LeafLeftLegRoll1PreRy
    LeafLeftLegRoll1PreRz = LeafLeftLegRoll1PreR.LeafLeftLegRoll1PreRz

    LeafLeftLegRoll1PostR = LeafLeftLegRoll1PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll1PostRx = LeafLeftLegRoll1PostR.LeafLeftLegRoll1PostRx
    LeafLeftLegRoll1PostRy = LeafLeftLegRoll1PostR.LeafLeftLegRoll1PostRy
    LeafLeftLegRoll1PostRz = LeafLeftLegRoll1PostR.LeafLeftLegRoll1PostRz

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

    LeafRightUpLegRoll1PGX = MatrixField()

    LeafRightUpLegRoll1ROrder = LeafRightUpLegRoll1ROrderEnumField(default_value=0)

    LeafRightUpLegRoll1SC = BoolField(default_value=False)

    LeafRightUpLegRoll1IS = LeafRightUpLegRoll1ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightUpLegRoll1ISx = LeafRightUpLegRoll1IS.LeafRightUpLegRoll1ISx
    LeafRightUpLegRoll1ISy = LeafRightUpLegRoll1IS.LeafRightUpLegRoll1ISy
    LeafRightUpLegRoll1ISz = LeafRightUpLegRoll1IS.LeafRightUpLegRoll1ISz

    LeafRightUpLegRoll1PreR = LeafRightUpLegRoll1PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll1PreRx = LeafRightUpLegRoll1PreR.LeafRightUpLegRoll1PreRx
    LeafRightUpLegRoll1PreRy = LeafRightUpLegRoll1PreR.LeafRightUpLegRoll1PreRy
    LeafRightUpLegRoll1PreRz = LeafRightUpLegRoll1PreR.LeafRightUpLegRoll1PreRz

    LeafRightUpLegRoll1PostR = LeafRightUpLegRoll1PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll1PostRx = LeafRightUpLegRoll1PostR.LeafRightUpLegRoll1PostRx
    LeafRightUpLegRoll1PostRy = LeafRightUpLegRoll1PostR.LeafRightUpLegRoll1PostRy
    LeafRightUpLegRoll1PostRz = LeafRightUpLegRoll1PostR.LeafRightUpLegRoll1PostRz

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

    LeafRightLegRoll1PGX = MatrixField()

    LeafRightLegRoll1ROrder = LeafRightLegRoll1ROrderEnumField(default_value=0)

    LeafRightLegRoll1SC = BoolField(default_value=False)

    LeafRightLegRoll1IS = LeafRightLegRoll1ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightLegRoll1ISx = LeafRightLegRoll1IS.LeafRightLegRoll1ISx
    LeafRightLegRoll1ISy = LeafRightLegRoll1IS.LeafRightLegRoll1ISy
    LeafRightLegRoll1ISz = LeafRightLegRoll1IS.LeafRightLegRoll1ISz

    LeafRightLegRoll1PreR = LeafRightLegRoll1PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll1PreRx = LeafRightLegRoll1PreR.LeafRightLegRoll1PreRx
    LeafRightLegRoll1PreRy = LeafRightLegRoll1PreR.LeafRightLegRoll1PreRy
    LeafRightLegRoll1PreRz = LeafRightLegRoll1PreR.LeafRightLegRoll1PreRz

    LeafRightLegRoll1PostR = LeafRightLegRoll1PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll1PostRx = LeafRightLegRoll1PostR.LeafRightLegRoll1PostRx
    LeafRightLegRoll1PostRy = LeafRightLegRoll1PostR.LeafRightLegRoll1PostRy
    LeafRightLegRoll1PostRz = LeafRightLegRoll1PostR.LeafRightLegRoll1PostRz

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

    LeafLeftArmRoll1PGX = MatrixField()

    LeafLeftArmRoll1ROrder = LeafLeftArmRoll1ROrderEnumField(default_value=0)

    LeafLeftArmRoll1SC = BoolField(default_value=False)

    LeafLeftArmRoll1IS = LeafLeftArmRoll1ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftArmRoll1ISx = LeafLeftArmRoll1IS.LeafLeftArmRoll1ISx
    LeafLeftArmRoll1ISy = LeafLeftArmRoll1IS.LeafLeftArmRoll1ISy
    LeafLeftArmRoll1ISz = LeafLeftArmRoll1IS.LeafLeftArmRoll1ISz

    LeafLeftArmRoll1PreR = LeafLeftArmRoll1PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll1PreRx = LeafLeftArmRoll1PreR.LeafLeftArmRoll1PreRx
    LeafLeftArmRoll1PreRy = LeafLeftArmRoll1PreR.LeafLeftArmRoll1PreRy
    LeafLeftArmRoll1PreRz = LeafLeftArmRoll1PreR.LeafLeftArmRoll1PreRz

    LeafLeftArmRoll1PostR = LeafLeftArmRoll1PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll1PostRx = LeafLeftArmRoll1PostR.LeafLeftArmRoll1PostRx
    LeafLeftArmRoll1PostRy = LeafLeftArmRoll1PostR.LeafLeftArmRoll1PostRy
    LeafLeftArmRoll1PostRz = LeafLeftArmRoll1PostR.LeafLeftArmRoll1PostRz

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

    LeafLeftForeArmRoll1PGX = MatrixField()

    LeafLeftForeArmRoll1ROrder = LeafLeftForeArmRoll1ROrderEnumField(default_value=0)

    LeafLeftForeArmRoll1SC = BoolField(default_value=False)

    LeafLeftForeArmRoll1IS = LeafLeftForeArmRoll1ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftForeArmRoll1ISx = LeafLeftForeArmRoll1IS.LeafLeftForeArmRoll1ISx
    LeafLeftForeArmRoll1ISy = LeafLeftForeArmRoll1IS.LeafLeftForeArmRoll1ISy
    LeafLeftForeArmRoll1ISz = LeafLeftForeArmRoll1IS.LeafLeftForeArmRoll1ISz

    LeafLeftForeArmRoll1PreR = LeafLeftForeArmRoll1PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll1PreRx = LeafLeftForeArmRoll1PreR.LeafLeftForeArmRoll1PreRx
    LeafLeftForeArmRoll1PreRy = LeafLeftForeArmRoll1PreR.LeafLeftForeArmRoll1PreRy
    LeafLeftForeArmRoll1PreRz = LeafLeftForeArmRoll1PreR.LeafLeftForeArmRoll1PreRz

    LeafLeftForeArmRoll1PostR = LeafLeftForeArmRoll1PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll1PostRx = LeafLeftForeArmRoll1PostR.LeafLeftForeArmRoll1PostRx
    LeafLeftForeArmRoll1PostRy = LeafLeftForeArmRoll1PostR.LeafLeftForeArmRoll1PostRy
    LeafLeftForeArmRoll1PostRz = LeafLeftForeArmRoll1PostR.LeafLeftForeArmRoll1PostRz

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

    LeafRightArmRoll1PGX = MatrixField()

    LeafRightArmRoll1ROrder = LeafRightArmRoll1ROrderEnumField(default_value=0)

    LeafRightArmRoll1SC = BoolField(default_value=False)

    LeafRightArmRoll1IS = LeafRightArmRoll1ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightArmRoll1ISx = LeafRightArmRoll1IS.LeafRightArmRoll1ISx
    LeafRightArmRoll1ISy = LeafRightArmRoll1IS.LeafRightArmRoll1ISy
    LeafRightArmRoll1ISz = LeafRightArmRoll1IS.LeafRightArmRoll1ISz

    LeafRightArmRoll1PreR = LeafRightArmRoll1PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll1PreRx = LeafRightArmRoll1PreR.LeafRightArmRoll1PreRx
    LeafRightArmRoll1PreRy = LeafRightArmRoll1PreR.LeafRightArmRoll1PreRy
    LeafRightArmRoll1PreRz = LeafRightArmRoll1PreR.LeafRightArmRoll1PreRz

    LeafRightArmRoll1PostR = LeafRightArmRoll1PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll1PostRx = LeafRightArmRoll1PostR.LeafRightArmRoll1PostRx
    LeafRightArmRoll1PostRy = LeafRightArmRoll1PostR.LeafRightArmRoll1PostRy
    LeafRightArmRoll1PostRz = LeafRightArmRoll1PostR.LeafRightArmRoll1PostRz

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

    LeafRightForeArmRoll1PGX = MatrixField()

    LeafRightForeArmRoll1ROrder = LeafRightForeArmRoll1ROrderEnumField(default_value=0)

    LeafRightForeArmRoll1SC = BoolField(default_value=False)

    LeafRightForeArmRoll1IS = LeafRightForeArmRoll1ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightForeArmRoll1ISx = LeafRightForeArmRoll1IS.LeafRightForeArmRoll1ISx
    LeafRightForeArmRoll1ISy = LeafRightForeArmRoll1IS.LeafRightForeArmRoll1ISy
    LeafRightForeArmRoll1ISz = LeafRightForeArmRoll1IS.LeafRightForeArmRoll1ISz

    LeafRightForeArmRoll1PreR = LeafRightForeArmRoll1PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll1PreRx = LeafRightForeArmRoll1PreR.LeafRightForeArmRoll1PreRx
    LeafRightForeArmRoll1PreRy = LeafRightForeArmRoll1PreR.LeafRightForeArmRoll1PreRy
    LeafRightForeArmRoll1PreRz = LeafRightForeArmRoll1PreR.LeafRightForeArmRoll1PreRz

    LeafRightForeArmRoll1PostR = LeafRightForeArmRoll1PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll1PostRx = LeafRightForeArmRoll1PostR.LeafRightForeArmRoll1PostRx
    LeafRightForeArmRoll1PostRy = LeafRightForeArmRoll1PostR.LeafRightForeArmRoll1PostRy
    LeafRightForeArmRoll1PostRz = LeafRightForeArmRoll1PostR.LeafRightForeArmRoll1PostRz

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

    LeafLeftUpLegRoll2PGX = MatrixField()

    LeafLeftUpLegRoll2ROrder = LeafLeftUpLegRoll2ROrderEnumField(default_value=0)

    LeafLeftUpLegRoll2SC = BoolField(default_value=False)

    LeafLeftUpLegRoll2IS = LeafLeftUpLegRoll2ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftUpLegRoll2ISx = LeafLeftUpLegRoll2IS.LeafLeftUpLegRoll2ISx
    LeafLeftUpLegRoll2ISy = LeafLeftUpLegRoll2IS.LeafLeftUpLegRoll2ISy
    LeafLeftUpLegRoll2ISz = LeafLeftUpLegRoll2IS.LeafLeftUpLegRoll2ISz

    LeafLeftUpLegRoll2PreR = LeafLeftUpLegRoll2PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll2PreRx = LeafLeftUpLegRoll2PreR.LeafLeftUpLegRoll2PreRx
    LeafLeftUpLegRoll2PreRy = LeafLeftUpLegRoll2PreR.LeafLeftUpLegRoll2PreRy
    LeafLeftUpLegRoll2PreRz = LeafLeftUpLegRoll2PreR.LeafLeftUpLegRoll2PreRz

    LeafLeftUpLegRoll2PostR = LeafLeftUpLegRoll2PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll2PostRx = LeafLeftUpLegRoll2PostR.LeafLeftUpLegRoll2PostRx
    LeafLeftUpLegRoll2PostRy = LeafLeftUpLegRoll2PostR.LeafLeftUpLegRoll2PostRy
    LeafLeftUpLegRoll2PostRz = LeafLeftUpLegRoll2PostR.LeafLeftUpLegRoll2PostRz

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

    LeafLeftLegRoll2PGX = MatrixField()

    LeafLeftLegRoll2ROrder = LeafLeftLegRoll2ROrderEnumField(default_value=0)

    LeafLeftLegRoll2SC = BoolField(default_value=False)

    LeafLeftLegRoll2IS = LeafLeftLegRoll2ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftLegRoll2ISx = LeafLeftLegRoll2IS.LeafLeftLegRoll2ISx
    LeafLeftLegRoll2ISy = LeafLeftLegRoll2IS.LeafLeftLegRoll2ISy
    LeafLeftLegRoll2ISz = LeafLeftLegRoll2IS.LeafLeftLegRoll2ISz

    LeafLeftLegRoll2PreR = LeafLeftLegRoll2PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll2PreRx = LeafLeftLegRoll2PreR.LeafLeftLegRoll2PreRx
    LeafLeftLegRoll2PreRy = LeafLeftLegRoll2PreR.LeafLeftLegRoll2PreRy
    LeafLeftLegRoll2PreRz = LeafLeftLegRoll2PreR.LeafLeftLegRoll2PreRz

    LeafLeftLegRoll2PostR = LeafLeftLegRoll2PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll2PostRx = LeafLeftLegRoll2PostR.LeafLeftLegRoll2PostRx
    LeafLeftLegRoll2PostRy = LeafLeftLegRoll2PostR.LeafLeftLegRoll2PostRy
    LeafLeftLegRoll2PostRz = LeafLeftLegRoll2PostR.LeafLeftLegRoll2PostRz

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

    LeafRightUpLegRoll2PGX = MatrixField()

    LeafRightUpLegRoll2ROrder = LeafRightUpLegRoll2ROrderEnumField(default_value=0)

    LeafRightUpLegRoll2SC = BoolField(default_value=False)

    LeafRightUpLegRoll2IS = LeafRightUpLegRoll2ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightUpLegRoll2ISx = LeafRightUpLegRoll2IS.LeafRightUpLegRoll2ISx
    LeafRightUpLegRoll2ISy = LeafRightUpLegRoll2IS.LeafRightUpLegRoll2ISy
    LeafRightUpLegRoll2ISz = LeafRightUpLegRoll2IS.LeafRightUpLegRoll2ISz

    LeafRightUpLegRoll2PreR = LeafRightUpLegRoll2PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll2PreRx = LeafRightUpLegRoll2PreR.LeafRightUpLegRoll2PreRx
    LeafRightUpLegRoll2PreRy = LeafRightUpLegRoll2PreR.LeafRightUpLegRoll2PreRy
    LeafRightUpLegRoll2PreRz = LeafRightUpLegRoll2PreR.LeafRightUpLegRoll2PreRz

    LeafRightUpLegRoll2PostR = LeafRightUpLegRoll2PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll2PostRx = LeafRightUpLegRoll2PostR.LeafRightUpLegRoll2PostRx
    LeafRightUpLegRoll2PostRy = LeafRightUpLegRoll2PostR.LeafRightUpLegRoll2PostRy
    LeafRightUpLegRoll2PostRz = LeafRightUpLegRoll2PostR.LeafRightUpLegRoll2PostRz

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

    LeafRightLegRoll2PGX = MatrixField()

    LeafRightLegRoll2ROrder = LeafRightLegRoll2ROrderEnumField(default_value=0)

    LeafRightLegRoll2SC = BoolField(default_value=False)

    LeafRightLegRoll2IS = LeafRightLegRoll2ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightLegRoll2ISx = LeafRightLegRoll2IS.LeafRightLegRoll2ISx
    LeafRightLegRoll2ISy = LeafRightLegRoll2IS.LeafRightLegRoll2ISy
    LeafRightLegRoll2ISz = LeafRightLegRoll2IS.LeafRightLegRoll2ISz

    LeafRightLegRoll2PreR = LeafRightLegRoll2PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll2PreRx = LeafRightLegRoll2PreR.LeafRightLegRoll2PreRx
    LeafRightLegRoll2PreRy = LeafRightLegRoll2PreR.LeafRightLegRoll2PreRy
    LeafRightLegRoll2PreRz = LeafRightLegRoll2PreR.LeafRightLegRoll2PreRz

    LeafRightLegRoll2PostR = LeafRightLegRoll2PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll2PostRx = LeafRightLegRoll2PostR.LeafRightLegRoll2PostRx
    LeafRightLegRoll2PostRy = LeafRightLegRoll2PostR.LeafRightLegRoll2PostRy
    LeafRightLegRoll2PostRz = LeafRightLegRoll2PostR.LeafRightLegRoll2PostRz

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

    LeafLeftArmRoll2PGX = MatrixField()

    LeafLeftArmRoll2ROrder = LeafLeftArmRoll2ROrderEnumField(default_value=0)

    LeafLeftArmRoll2SC = BoolField(default_value=False)

    LeafLeftArmRoll2IS = LeafLeftArmRoll2ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftArmRoll2ISx = LeafLeftArmRoll2IS.LeafLeftArmRoll2ISx
    LeafLeftArmRoll2ISy = LeafLeftArmRoll2IS.LeafLeftArmRoll2ISy
    LeafLeftArmRoll2ISz = LeafLeftArmRoll2IS.LeafLeftArmRoll2ISz

    LeafLeftArmRoll2PreR = LeafLeftArmRoll2PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll2PreRx = LeafLeftArmRoll2PreR.LeafLeftArmRoll2PreRx
    LeafLeftArmRoll2PreRy = LeafLeftArmRoll2PreR.LeafLeftArmRoll2PreRy
    LeafLeftArmRoll2PreRz = LeafLeftArmRoll2PreR.LeafLeftArmRoll2PreRz

    LeafLeftArmRoll2PostR = LeafLeftArmRoll2PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll2PostRx = LeafLeftArmRoll2PostR.LeafLeftArmRoll2PostRx
    LeafLeftArmRoll2PostRy = LeafLeftArmRoll2PostR.LeafLeftArmRoll2PostRy
    LeafLeftArmRoll2PostRz = LeafLeftArmRoll2PostR.LeafLeftArmRoll2PostRz

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

    LeafLeftForeArmRoll2PGX = MatrixField()

    LeafLeftForeArmRoll2ROrder = LeafLeftForeArmRoll2ROrderEnumField(default_value=0)

    LeafLeftForeArmRoll2SC = BoolField(default_value=False)

    LeafLeftForeArmRoll2IS = LeafLeftForeArmRoll2ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftForeArmRoll2ISx = LeafLeftForeArmRoll2IS.LeafLeftForeArmRoll2ISx
    LeafLeftForeArmRoll2ISy = LeafLeftForeArmRoll2IS.LeafLeftForeArmRoll2ISy
    LeafLeftForeArmRoll2ISz = LeafLeftForeArmRoll2IS.LeafLeftForeArmRoll2ISz

    LeafLeftForeArmRoll2PreR = LeafLeftForeArmRoll2PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll2PreRx = LeafLeftForeArmRoll2PreR.LeafLeftForeArmRoll2PreRx
    LeafLeftForeArmRoll2PreRy = LeafLeftForeArmRoll2PreR.LeafLeftForeArmRoll2PreRy
    LeafLeftForeArmRoll2PreRz = LeafLeftForeArmRoll2PreR.LeafLeftForeArmRoll2PreRz

    LeafLeftForeArmRoll2PostR = LeafLeftForeArmRoll2PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll2PostRx = LeafLeftForeArmRoll2PostR.LeafLeftForeArmRoll2PostRx
    LeafLeftForeArmRoll2PostRy = LeafLeftForeArmRoll2PostR.LeafLeftForeArmRoll2PostRy
    LeafLeftForeArmRoll2PostRz = LeafLeftForeArmRoll2PostR.LeafLeftForeArmRoll2PostRz

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

    LeafRightArmRoll2PGX = MatrixField()

    LeafRightArmRoll2ROrder = LeafRightArmRoll2ROrderEnumField(default_value=0)

    LeafRightArmRoll2SC = BoolField(default_value=False)

    LeafRightArmRoll2IS = LeafRightArmRoll2ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightArmRoll2ISx = LeafRightArmRoll2IS.LeafRightArmRoll2ISx
    LeafRightArmRoll2ISy = LeafRightArmRoll2IS.LeafRightArmRoll2ISy
    LeafRightArmRoll2ISz = LeafRightArmRoll2IS.LeafRightArmRoll2ISz

    LeafRightArmRoll2PreR = LeafRightArmRoll2PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll2PreRx = LeafRightArmRoll2PreR.LeafRightArmRoll2PreRx
    LeafRightArmRoll2PreRy = LeafRightArmRoll2PreR.LeafRightArmRoll2PreRy
    LeafRightArmRoll2PreRz = LeafRightArmRoll2PreR.LeafRightArmRoll2PreRz

    LeafRightArmRoll2PostR = LeafRightArmRoll2PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll2PostRx = LeafRightArmRoll2PostR.LeafRightArmRoll2PostRx
    LeafRightArmRoll2PostRy = LeafRightArmRoll2PostR.LeafRightArmRoll2PostRy
    LeafRightArmRoll2PostRz = LeafRightArmRoll2PostR.LeafRightArmRoll2PostRz

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

    LeafRightForeArmRoll2PGX = MatrixField()

    LeafRightForeArmRoll2ROrder = LeafRightForeArmRoll2ROrderEnumField(default_value=0)

    LeafRightForeArmRoll2SC = BoolField(default_value=False)

    LeafRightForeArmRoll2IS = LeafRightForeArmRoll2ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightForeArmRoll2ISx = LeafRightForeArmRoll2IS.LeafRightForeArmRoll2ISx
    LeafRightForeArmRoll2ISy = LeafRightForeArmRoll2IS.LeafRightForeArmRoll2ISy
    LeafRightForeArmRoll2ISz = LeafRightForeArmRoll2IS.LeafRightForeArmRoll2ISz

    LeafRightForeArmRoll2PreR = LeafRightForeArmRoll2PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll2PreRx = LeafRightForeArmRoll2PreR.LeafRightForeArmRoll2PreRx
    LeafRightForeArmRoll2PreRy = LeafRightForeArmRoll2PreR.LeafRightForeArmRoll2PreRy
    LeafRightForeArmRoll2PreRz = LeafRightForeArmRoll2PreR.LeafRightForeArmRoll2PreRz

    LeafRightForeArmRoll2PostR = LeafRightForeArmRoll2PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll2PostRx = LeafRightForeArmRoll2PostR.LeafRightForeArmRoll2PostRx
    LeafRightForeArmRoll2PostRy = LeafRightForeArmRoll2PostR.LeafRightForeArmRoll2PostRy
    LeafRightForeArmRoll2PostRz = LeafRightForeArmRoll2PostR.LeafRightForeArmRoll2PostRz

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

    LeafLeftUpLegRoll3PGX = MatrixField()

    LeafLeftUpLegRoll3ROrder = LeafLeftUpLegRoll3ROrderEnumField(default_value=0)

    LeafLeftUpLegRoll3SC = BoolField(default_value=False)

    LeafLeftUpLegRoll3IS = LeafLeftUpLegRoll3ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftUpLegRoll3ISx = LeafLeftUpLegRoll3IS.LeafLeftUpLegRoll3ISx
    LeafLeftUpLegRoll3ISy = LeafLeftUpLegRoll3IS.LeafLeftUpLegRoll3ISy
    LeafLeftUpLegRoll3ISz = LeafLeftUpLegRoll3IS.LeafLeftUpLegRoll3ISz

    LeafLeftUpLegRoll3PreR = LeafLeftUpLegRoll3PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll3PreRx = LeafLeftUpLegRoll3PreR.LeafLeftUpLegRoll3PreRx
    LeafLeftUpLegRoll3PreRy = LeafLeftUpLegRoll3PreR.LeafLeftUpLegRoll3PreRy
    LeafLeftUpLegRoll3PreRz = LeafLeftUpLegRoll3PreR.LeafLeftUpLegRoll3PreRz

    LeafLeftUpLegRoll3PostR = LeafLeftUpLegRoll3PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll3PostRx = LeafLeftUpLegRoll3PostR.LeafLeftUpLegRoll3PostRx
    LeafLeftUpLegRoll3PostRy = LeafLeftUpLegRoll3PostR.LeafLeftUpLegRoll3PostRy
    LeafLeftUpLegRoll3PostRz = LeafLeftUpLegRoll3PostR.LeafLeftUpLegRoll3PostRz

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

    LeafLeftLegRoll3PGX = MatrixField()

    LeafLeftLegRoll3ROrder = LeafLeftLegRoll3ROrderEnumField(default_value=0)

    LeafLeftLegRoll3SC = BoolField(default_value=False)

    LeafLeftLegRoll3IS = LeafLeftLegRoll3ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftLegRoll3ISx = LeafLeftLegRoll3IS.LeafLeftLegRoll3ISx
    LeafLeftLegRoll3ISy = LeafLeftLegRoll3IS.LeafLeftLegRoll3ISy
    LeafLeftLegRoll3ISz = LeafLeftLegRoll3IS.LeafLeftLegRoll3ISz

    LeafLeftLegRoll3PreR = LeafLeftLegRoll3PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll3PreRx = LeafLeftLegRoll3PreR.LeafLeftLegRoll3PreRx
    LeafLeftLegRoll3PreRy = LeafLeftLegRoll3PreR.LeafLeftLegRoll3PreRy
    LeafLeftLegRoll3PreRz = LeafLeftLegRoll3PreR.LeafLeftLegRoll3PreRz

    LeafLeftLegRoll3PostR = LeafLeftLegRoll3PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll3PostRx = LeafLeftLegRoll3PostR.LeafLeftLegRoll3PostRx
    LeafLeftLegRoll3PostRy = LeafLeftLegRoll3PostR.LeafLeftLegRoll3PostRy
    LeafLeftLegRoll3PostRz = LeafLeftLegRoll3PostR.LeafLeftLegRoll3PostRz

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

    LeafRightUpLegRoll3PGX = MatrixField()

    LeafRightUpLegRoll3ROrder = LeafRightUpLegRoll3ROrderEnumField(default_value=0)

    LeafRightUpLegRoll3SC = BoolField(default_value=False)

    LeafRightUpLegRoll3IS = LeafRightUpLegRoll3ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightUpLegRoll3ISx = LeafRightUpLegRoll3IS.LeafRightUpLegRoll3ISx
    LeafRightUpLegRoll3ISy = LeafRightUpLegRoll3IS.LeafRightUpLegRoll3ISy
    LeafRightUpLegRoll3ISz = LeafRightUpLegRoll3IS.LeafRightUpLegRoll3ISz

    LeafRightUpLegRoll3PreR = LeafRightUpLegRoll3PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll3PreRx = LeafRightUpLegRoll3PreR.LeafRightUpLegRoll3PreRx
    LeafRightUpLegRoll3PreRy = LeafRightUpLegRoll3PreR.LeafRightUpLegRoll3PreRy
    LeafRightUpLegRoll3PreRz = LeafRightUpLegRoll3PreR.LeafRightUpLegRoll3PreRz

    LeafRightUpLegRoll3PostR = LeafRightUpLegRoll3PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll3PostRx = LeafRightUpLegRoll3PostR.LeafRightUpLegRoll3PostRx
    LeafRightUpLegRoll3PostRy = LeafRightUpLegRoll3PostR.LeafRightUpLegRoll3PostRy
    LeafRightUpLegRoll3PostRz = LeafRightUpLegRoll3PostR.LeafRightUpLegRoll3PostRz

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

    LeafRightLegRoll3PGX = MatrixField()

    LeafRightLegRoll3ROrder = LeafRightLegRoll3ROrderEnumField(default_value=0)

    LeafRightLegRoll3SC = BoolField(default_value=False)

    LeafRightLegRoll3IS = LeafRightLegRoll3ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightLegRoll3ISx = LeafRightLegRoll3IS.LeafRightLegRoll3ISx
    LeafRightLegRoll3ISy = LeafRightLegRoll3IS.LeafRightLegRoll3ISy
    LeafRightLegRoll3ISz = LeafRightLegRoll3IS.LeafRightLegRoll3ISz

    LeafRightLegRoll3PreR = LeafRightLegRoll3PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll3PreRx = LeafRightLegRoll3PreR.LeafRightLegRoll3PreRx
    LeafRightLegRoll3PreRy = LeafRightLegRoll3PreR.LeafRightLegRoll3PreRy
    LeafRightLegRoll3PreRz = LeafRightLegRoll3PreR.LeafRightLegRoll3PreRz

    LeafRightLegRoll3PostR = LeafRightLegRoll3PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll3PostRx = LeafRightLegRoll3PostR.LeafRightLegRoll3PostRx
    LeafRightLegRoll3PostRy = LeafRightLegRoll3PostR.LeafRightLegRoll3PostRy
    LeafRightLegRoll3PostRz = LeafRightLegRoll3PostR.LeafRightLegRoll3PostRz

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

    LeafLeftArmRoll3PGX = MatrixField()

    LeafLeftArmRoll3ROrder = LeafLeftArmRoll3ROrderEnumField(default_value=0)

    LeafLeftArmRoll3SC = BoolField(default_value=False)

    LeafLeftArmRoll3IS = LeafLeftArmRoll3ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftArmRoll3ISx = LeafLeftArmRoll3IS.LeafLeftArmRoll3ISx
    LeafLeftArmRoll3ISy = LeafLeftArmRoll3IS.LeafLeftArmRoll3ISy
    LeafLeftArmRoll3ISz = LeafLeftArmRoll3IS.LeafLeftArmRoll3ISz

    LeafLeftArmRoll3PreR = LeafLeftArmRoll3PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll3PreRx = LeafLeftArmRoll3PreR.LeafLeftArmRoll3PreRx
    LeafLeftArmRoll3PreRy = LeafLeftArmRoll3PreR.LeafLeftArmRoll3PreRy
    LeafLeftArmRoll3PreRz = LeafLeftArmRoll3PreR.LeafLeftArmRoll3PreRz

    LeafLeftArmRoll3PostR = LeafLeftArmRoll3PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll3PostRx = LeafLeftArmRoll3PostR.LeafLeftArmRoll3PostRx
    LeafLeftArmRoll3PostRy = LeafLeftArmRoll3PostR.LeafLeftArmRoll3PostRy
    LeafLeftArmRoll3PostRz = LeafLeftArmRoll3PostR.LeafLeftArmRoll3PostRz

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

    LeafLeftForeArmRoll3PGX = MatrixField()

    LeafLeftForeArmRoll3ROrder = LeafLeftForeArmRoll3ROrderEnumField(default_value=0)

    LeafLeftForeArmRoll3SC = BoolField(default_value=False)

    LeafLeftForeArmRoll3IS = LeafLeftForeArmRoll3ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftForeArmRoll3ISx = LeafLeftForeArmRoll3IS.LeafLeftForeArmRoll3ISx
    LeafLeftForeArmRoll3ISy = LeafLeftForeArmRoll3IS.LeafLeftForeArmRoll3ISy
    LeafLeftForeArmRoll3ISz = LeafLeftForeArmRoll3IS.LeafLeftForeArmRoll3ISz

    LeafLeftForeArmRoll3PreR = LeafLeftForeArmRoll3PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll3PreRx = LeafLeftForeArmRoll3PreR.LeafLeftForeArmRoll3PreRx
    LeafLeftForeArmRoll3PreRy = LeafLeftForeArmRoll3PreR.LeafLeftForeArmRoll3PreRy
    LeafLeftForeArmRoll3PreRz = LeafLeftForeArmRoll3PreR.LeafLeftForeArmRoll3PreRz

    LeafLeftForeArmRoll3PostR = LeafLeftForeArmRoll3PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll3PostRx = LeafLeftForeArmRoll3PostR.LeafLeftForeArmRoll3PostRx
    LeafLeftForeArmRoll3PostRy = LeafLeftForeArmRoll3PostR.LeafLeftForeArmRoll3PostRy
    LeafLeftForeArmRoll3PostRz = LeafLeftForeArmRoll3PostR.LeafLeftForeArmRoll3PostRz

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

    LeafRightArmRoll3PGX = MatrixField()

    LeafRightArmRoll3ROrder = LeafRightArmRoll3ROrderEnumField(default_value=0)

    LeafRightArmRoll3SC = BoolField(default_value=False)

    LeafRightArmRoll3IS = LeafRightArmRoll3ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightArmRoll3ISx = LeafRightArmRoll3IS.LeafRightArmRoll3ISx
    LeafRightArmRoll3ISy = LeafRightArmRoll3IS.LeafRightArmRoll3ISy
    LeafRightArmRoll3ISz = LeafRightArmRoll3IS.LeafRightArmRoll3ISz

    LeafRightArmRoll3PreR = LeafRightArmRoll3PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll3PreRx = LeafRightArmRoll3PreR.LeafRightArmRoll3PreRx
    LeafRightArmRoll3PreRy = LeafRightArmRoll3PreR.LeafRightArmRoll3PreRy
    LeafRightArmRoll3PreRz = LeafRightArmRoll3PreR.LeafRightArmRoll3PreRz

    LeafRightArmRoll3PostR = LeafRightArmRoll3PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll3PostRx = LeafRightArmRoll3PostR.LeafRightArmRoll3PostRx
    LeafRightArmRoll3PostRy = LeafRightArmRoll3PostR.LeafRightArmRoll3PostRy
    LeafRightArmRoll3PostRz = LeafRightArmRoll3PostR.LeafRightArmRoll3PostRz

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

    LeafRightForeArmRoll3PGX = MatrixField()

    LeafRightForeArmRoll3ROrder = LeafRightForeArmRoll3ROrderEnumField(default_value=0)

    LeafRightForeArmRoll3SC = BoolField(default_value=False)

    LeafRightForeArmRoll3IS = LeafRightForeArmRoll3ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightForeArmRoll3ISx = LeafRightForeArmRoll3IS.LeafRightForeArmRoll3ISx
    LeafRightForeArmRoll3ISy = LeafRightForeArmRoll3IS.LeafRightForeArmRoll3ISy
    LeafRightForeArmRoll3ISz = LeafRightForeArmRoll3IS.LeafRightForeArmRoll3ISz

    LeafRightForeArmRoll3PreR = LeafRightForeArmRoll3PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll3PreRx = LeafRightForeArmRoll3PreR.LeafRightForeArmRoll3PreRx
    LeafRightForeArmRoll3PreRy = LeafRightForeArmRoll3PreR.LeafRightForeArmRoll3PreRy
    LeafRightForeArmRoll3PreRz = LeafRightForeArmRoll3PreR.LeafRightForeArmRoll3PreRz

    LeafRightForeArmRoll3PostR = LeafRightForeArmRoll3PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll3PostRx = LeafRightForeArmRoll3PostR.LeafRightForeArmRoll3PostRx
    LeafRightForeArmRoll3PostRy = LeafRightForeArmRoll3PostR.LeafRightForeArmRoll3PostRy
    LeafRightForeArmRoll3PostRz = LeafRightForeArmRoll3PostR.LeafRightForeArmRoll3PostRz

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

    LeafLeftUpLegRoll4PGX = MatrixField()

    LeafLeftUpLegRoll4ROrder = LeafLeftUpLegRoll4ROrderEnumField(default_value=0)

    LeafLeftUpLegRoll4SC = BoolField(default_value=False)

    LeafLeftUpLegRoll4IS = LeafLeftUpLegRoll4ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftUpLegRoll4ISx = LeafLeftUpLegRoll4IS.LeafLeftUpLegRoll4ISx
    LeafLeftUpLegRoll4ISy = LeafLeftUpLegRoll4IS.LeafLeftUpLegRoll4ISy
    LeafLeftUpLegRoll4ISz = LeafLeftUpLegRoll4IS.LeafLeftUpLegRoll4ISz

    LeafLeftUpLegRoll4PreR = LeafLeftUpLegRoll4PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll4PreRx = LeafLeftUpLegRoll4PreR.LeafLeftUpLegRoll4PreRx
    LeafLeftUpLegRoll4PreRy = LeafLeftUpLegRoll4PreR.LeafLeftUpLegRoll4PreRy
    LeafLeftUpLegRoll4PreRz = LeafLeftUpLegRoll4PreR.LeafLeftUpLegRoll4PreRz

    LeafLeftUpLegRoll4PostR = LeafLeftUpLegRoll4PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll4PostRx = LeafLeftUpLegRoll4PostR.LeafLeftUpLegRoll4PostRx
    LeafLeftUpLegRoll4PostRy = LeafLeftUpLegRoll4PostR.LeafLeftUpLegRoll4PostRy
    LeafLeftUpLegRoll4PostRz = LeafLeftUpLegRoll4PostR.LeafLeftUpLegRoll4PostRz

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

    LeafLeftLegRoll4PGX = MatrixField()

    LeafLeftLegRoll4ROrder = LeafLeftLegRoll4ROrderEnumField(default_value=0)

    LeafLeftLegRoll4SC = BoolField(default_value=False)

    LeafLeftLegRoll4IS = LeafLeftLegRoll4ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftLegRoll4ISx = LeafLeftLegRoll4IS.LeafLeftLegRoll4ISx
    LeafLeftLegRoll4ISy = LeafLeftLegRoll4IS.LeafLeftLegRoll4ISy
    LeafLeftLegRoll4ISz = LeafLeftLegRoll4IS.LeafLeftLegRoll4ISz

    LeafLeftLegRoll4PreR = LeafLeftLegRoll4PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll4PreRx = LeafLeftLegRoll4PreR.LeafLeftLegRoll4PreRx
    LeafLeftLegRoll4PreRy = LeafLeftLegRoll4PreR.LeafLeftLegRoll4PreRy
    LeafLeftLegRoll4PreRz = LeafLeftLegRoll4PreR.LeafLeftLegRoll4PreRz

    LeafLeftLegRoll4PostR = LeafLeftLegRoll4PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll4PostRx = LeafLeftLegRoll4PostR.LeafLeftLegRoll4PostRx
    LeafLeftLegRoll4PostRy = LeafLeftLegRoll4PostR.LeafLeftLegRoll4PostRy
    LeafLeftLegRoll4PostRz = LeafLeftLegRoll4PostR.LeafLeftLegRoll4PostRz

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

    LeafRightUpLegRoll4PGX = MatrixField()

    LeafRightUpLegRoll4ROrder = LeafRightUpLegRoll4ROrderEnumField(default_value=0)

    LeafRightUpLegRoll4SC = BoolField(default_value=False)

    LeafRightUpLegRoll4IS = LeafRightUpLegRoll4ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightUpLegRoll4ISx = LeafRightUpLegRoll4IS.LeafRightUpLegRoll4ISx
    LeafRightUpLegRoll4ISy = LeafRightUpLegRoll4IS.LeafRightUpLegRoll4ISy
    LeafRightUpLegRoll4ISz = LeafRightUpLegRoll4IS.LeafRightUpLegRoll4ISz

    LeafRightUpLegRoll4PreR = LeafRightUpLegRoll4PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll4PreRx = LeafRightUpLegRoll4PreR.LeafRightUpLegRoll4PreRx
    LeafRightUpLegRoll4PreRy = LeafRightUpLegRoll4PreR.LeafRightUpLegRoll4PreRy
    LeafRightUpLegRoll4PreRz = LeafRightUpLegRoll4PreR.LeafRightUpLegRoll4PreRz

    LeafRightUpLegRoll4PostR = LeafRightUpLegRoll4PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll4PostRx = LeafRightUpLegRoll4PostR.LeafRightUpLegRoll4PostRx
    LeafRightUpLegRoll4PostRy = LeafRightUpLegRoll4PostR.LeafRightUpLegRoll4PostRy
    LeafRightUpLegRoll4PostRz = LeafRightUpLegRoll4PostR.LeafRightUpLegRoll4PostRz

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

    LeafRightLegRoll4PGX = MatrixField()

    LeafRightLegRoll4ROrder = LeafRightLegRoll4ROrderEnumField(default_value=0)

    LeafRightLegRoll4SC = BoolField(default_value=False)

    LeafRightLegRoll4IS = LeafRightLegRoll4ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightLegRoll4ISx = LeafRightLegRoll4IS.LeafRightLegRoll4ISx
    LeafRightLegRoll4ISy = LeafRightLegRoll4IS.LeafRightLegRoll4ISy
    LeafRightLegRoll4ISz = LeafRightLegRoll4IS.LeafRightLegRoll4ISz

    LeafRightLegRoll4PreR = LeafRightLegRoll4PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll4PreRx = LeafRightLegRoll4PreR.LeafRightLegRoll4PreRx
    LeafRightLegRoll4PreRy = LeafRightLegRoll4PreR.LeafRightLegRoll4PreRy
    LeafRightLegRoll4PreRz = LeafRightLegRoll4PreR.LeafRightLegRoll4PreRz

    LeafRightLegRoll4PostR = LeafRightLegRoll4PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll4PostRx = LeafRightLegRoll4PostR.LeafRightLegRoll4PostRx
    LeafRightLegRoll4PostRy = LeafRightLegRoll4PostR.LeafRightLegRoll4PostRy
    LeafRightLegRoll4PostRz = LeafRightLegRoll4PostR.LeafRightLegRoll4PostRz

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

    LeafLeftArmRoll4PGX = MatrixField()

    LeafLeftArmRoll4ROrder = LeafLeftArmRoll4ROrderEnumField(default_value=0)

    LeafLeftArmRoll4SC = BoolField(default_value=False)

    LeafLeftArmRoll4IS = LeafLeftArmRoll4ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftArmRoll4ISx = LeafLeftArmRoll4IS.LeafLeftArmRoll4ISx
    LeafLeftArmRoll4ISy = LeafLeftArmRoll4IS.LeafLeftArmRoll4ISy
    LeafLeftArmRoll4ISz = LeafLeftArmRoll4IS.LeafLeftArmRoll4ISz

    LeafLeftArmRoll4PreR = LeafLeftArmRoll4PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll4PreRx = LeafLeftArmRoll4PreR.LeafLeftArmRoll4PreRx
    LeafLeftArmRoll4PreRy = LeafLeftArmRoll4PreR.LeafLeftArmRoll4PreRy
    LeafLeftArmRoll4PreRz = LeafLeftArmRoll4PreR.LeafLeftArmRoll4PreRz

    LeafLeftArmRoll4PostR = LeafLeftArmRoll4PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll4PostRx = LeafLeftArmRoll4PostR.LeafLeftArmRoll4PostRx
    LeafLeftArmRoll4PostRy = LeafLeftArmRoll4PostR.LeafLeftArmRoll4PostRy
    LeafLeftArmRoll4PostRz = LeafLeftArmRoll4PostR.LeafLeftArmRoll4PostRz

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

    LeafLeftForeArmRoll4PGX = MatrixField()

    LeafLeftForeArmRoll4ROrder = LeafLeftForeArmRoll4ROrderEnumField(default_value=0)

    LeafLeftForeArmRoll4SC = BoolField(default_value=False)

    LeafLeftForeArmRoll4IS = LeafLeftForeArmRoll4ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftForeArmRoll4ISx = LeafLeftForeArmRoll4IS.LeafLeftForeArmRoll4ISx
    LeafLeftForeArmRoll4ISy = LeafLeftForeArmRoll4IS.LeafLeftForeArmRoll4ISy
    LeafLeftForeArmRoll4ISz = LeafLeftForeArmRoll4IS.LeafLeftForeArmRoll4ISz

    LeafLeftForeArmRoll4PreR = LeafLeftForeArmRoll4PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll4PreRx = LeafLeftForeArmRoll4PreR.LeafLeftForeArmRoll4PreRx
    LeafLeftForeArmRoll4PreRy = LeafLeftForeArmRoll4PreR.LeafLeftForeArmRoll4PreRy
    LeafLeftForeArmRoll4PreRz = LeafLeftForeArmRoll4PreR.LeafLeftForeArmRoll4PreRz

    LeafLeftForeArmRoll4PostR = LeafLeftForeArmRoll4PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll4PostRx = LeafLeftForeArmRoll4PostR.LeafLeftForeArmRoll4PostRx
    LeafLeftForeArmRoll4PostRy = LeafLeftForeArmRoll4PostR.LeafLeftForeArmRoll4PostRy
    LeafLeftForeArmRoll4PostRz = LeafLeftForeArmRoll4PostR.LeafLeftForeArmRoll4PostRz

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

    LeafRightArmRoll4PGX = MatrixField()

    LeafRightArmRoll4ROrder = LeafRightArmRoll4ROrderEnumField(default_value=0)

    LeafRightArmRoll4SC = BoolField(default_value=False)

    LeafRightArmRoll4IS = LeafRightArmRoll4ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightArmRoll4ISx = LeafRightArmRoll4IS.LeafRightArmRoll4ISx
    LeafRightArmRoll4ISy = LeafRightArmRoll4IS.LeafRightArmRoll4ISy
    LeafRightArmRoll4ISz = LeafRightArmRoll4IS.LeafRightArmRoll4ISz

    LeafRightArmRoll4PreR = LeafRightArmRoll4PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll4PreRx = LeafRightArmRoll4PreR.LeafRightArmRoll4PreRx
    LeafRightArmRoll4PreRy = LeafRightArmRoll4PreR.LeafRightArmRoll4PreRy
    LeafRightArmRoll4PreRz = LeafRightArmRoll4PreR.LeafRightArmRoll4PreRz

    LeafRightArmRoll4PostR = LeafRightArmRoll4PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll4PostRx = LeafRightArmRoll4PostR.LeafRightArmRoll4PostRx
    LeafRightArmRoll4PostRy = LeafRightArmRoll4PostR.LeafRightArmRoll4PostRy
    LeafRightArmRoll4PostRz = LeafRightArmRoll4PostR.LeafRightArmRoll4PostRz

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

    LeafRightForeArmRoll4PGX = MatrixField()

    LeafRightForeArmRoll4ROrder = LeafRightForeArmRoll4ROrderEnumField(default_value=0)

    LeafRightForeArmRoll4SC = BoolField(default_value=False)

    LeafRightForeArmRoll4IS = LeafRightForeArmRoll4ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightForeArmRoll4ISx = LeafRightForeArmRoll4IS.LeafRightForeArmRoll4ISx
    LeafRightForeArmRoll4ISy = LeafRightForeArmRoll4IS.LeafRightForeArmRoll4ISy
    LeafRightForeArmRoll4ISz = LeafRightForeArmRoll4IS.LeafRightForeArmRoll4ISz

    LeafRightForeArmRoll4PreR = LeafRightForeArmRoll4PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll4PreRx = LeafRightForeArmRoll4PreR.LeafRightForeArmRoll4PreRx
    LeafRightForeArmRoll4PreRy = LeafRightForeArmRoll4PreR.LeafRightForeArmRoll4PreRy
    LeafRightForeArmRoll4PreRz = LeafRightForeArmRoll4PreR.LeafRightForeArmRoll4PreRz

    LeafRightForeArmRoll4PostR = LeafRightForeArmRoll4PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll4PostRx = LeafRightForeArmRoll4PostR.LeafRightForeArmRoll4PostRx
    LeafRightForeArmRoll4PostRy = LeafRightForeArmRoll4PostR.LeafRightForeArmRoll4PostRy
    LeafRightForeArmRoll4PostRz = LeafRightForeArmRoll4PostR.LeafRightForeArmRoll4PostRz

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

    LeafLeftUpLegRoll5PGX = MatrixField()

    LeafLeftUpLegRoll5ROrder = LeafLeftUpLegRoll5ROrderEnumField(default_value=0)

    LeafLeftUpLegRoll5SC = BoolField(default_value=False)

    LeafLeftUpLegRoll5IS = LeafLeftUpLegRoll5ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftUpLegRoll5ISx = LeafLeftUpLegRoll5IS.LeafLeftUpLegRoll5ISx
    LeafLeftUpLegRoll5ISy = LeafLeftUpLegRoll5IS.LeafLeftUpLegRoll5ISy
    LeafLeftUpLegRoll5ISz = LeafLeftUpLegRoll5IS.LeafLeftUpLegRoll5ISz

    LeafLeftUpLegRoll5PreR = LeafLeftUpLegRoll5PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll5PreRx = LeafLeftUpLegRoll5PreR.LeafLeftUpLegRoll5PreRx
    LeafLeftUpLegRoll5PreRy = LeafLeftUpLegRoll5PreR.LeafLeftUpLegRoll5PreRy
    LeafLeftUpLegRoll5PreRz = LeafLeftUpLegRoll5PreR.LeafLeftUpLegRoll5PreRz

    LeafLeftUpLegRoll5PostR = LeafLeftUpLegRoll5PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftUpLegRoll5PostRx = LeafLeftUpLegRoll5PostR.LeafLeftUpLegRoll5PostRx
    LeafLeftUpLegRoll5PostRy = LeafLeftUpLegRoll5PostR.LeafLeftUpLegRoll5PostRy
    LeafLeftUpLegRoll5PostRz = LeafLeftUpLegRoll5PostR.LeafLeftUpLegRoll5PostRz

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

    LeafLeftLegRoll5PGX = MatrixField()

    LeafLeftLegRoll5ROrder = LeafLeftLegRoll5ROrderEnumField(default_value=0)

    LeafLeftLegRoll5SC = BoolField(default_value=False)

    LeafLeftLegRoll5IS = LeafLeftLegRoll5ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftLegRoll5ISx = LeafLeftLegRoll5IS.LeafLeftLegRoll5ISx
    LeafLeftLegRoll5ISy = LeafLeftLegRoll5IS.LeafLeftLegRoll5ISy
    LeafLeftLegRoll5ISz = LeafLeftLegRoll5IS.LeafLeftLegRoll5ISz

    LeafLeftLegRoll5PreR = LeafLeftLegRoll5PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll5PreRx = LeafLeftLegRoll5PreR.LeafLeftLegRoll5PreRx
    LeafLeftLegRoll5PreRy = LeafLeftLegRoll5PreR.LeafLeftLegRoll5PreRy
    LeafLeftLegRoll5PreRz = LeafLeftLegRoll5PreR.LeafLeftLegRoll5PreRz

    LeafLeftLegRoll5PostR = LeafLeftLegRoll5PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftLegRoll5PostRx = LeafLeftLegRoll5PostR.LeafLeftLegRoll5PostRx
    LeafLeftLegRoll5PostRy = LeafLeftLegRoll5PostR.LeafLeftLegRoll5PostRy
    LeafLeftLegRoll5PostRz = LeafLeftLegRoll5PostR.LeafLeftLegRoll5PostRz

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

    LeafRightUpLegRoll5PGX = MatrixField()

    LeafRightUpLegRoll5ROrder = LeafRightUpLegRoll5ROrderEnumField(default_value=0)

    LeafRightUpLegRoll5SC = BoolField(default_value=False)

    LeafRightUpLegRoll5IS = LeafRightUpLegRoll5ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightUpLegRoll5ISx = LeafRightUpLegRoll5IS.LeafRightUpLegRoll5ISx
    LeafRightUpLegRoll5ISy = LeafRightUpLegRoll5IS.LeafRightUpLegRoll5ISy
    LeafRightUpLegRoll5ISz = LeafRightUpLegRoll5IS.LeafRightUpLegRoll5ISz

    LeafRightUpLegRoll5PreR = LeafRightUpLegRoll5PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll5PreRx = LeafRightUpLegRoll5PreR.LeafRightUpLegRoll5PreRx
    LeafRightUpLegRoll5PreRy = LeafRightUpLegRoll5PreR.LeafRightUpLegRoll5PreRy
    LeafRightUpLegRoll5PreRz = LeafRightUpLegRoll5PreR.LeafRightUpLegRoll5PreRz

    LeafRightUpLegRoll5PostR = LeafRightUpLegRoll5PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightUpLegRoll5PostRx = LeafRightUpLegRoll5PostR.LeafRightUpLegRoll5PostRx
    LeafRightUpLegRoll5PostRy = LeafRightUpLegRoll5PostR.LeafRightUpLegRoll5PostRy
    LeafRightUpLegRoll5PostRz = LeafRightUpLegRoll5PostR.LeafRightUpLegRoll5PostRz

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

    LeafRightLegRoll5PGX = MatrixField()

    LeafRightLegRoll5ROrder = LeafRightLegRoll5ROrderEnumField(default_value=0)

    LeafRightLegRoll5SC = BoolField(default_value=False)

    LeafRightLegRoll5IS = LeafRightLegRoll5ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightLegRoll5ISx = LeafRightLegRoll5IS.LeafRightLegRoll5ISx
    LeafRightLegRoll5ISy = LeafRightLegRoll5IS.LeafRightLegRoll5ISy
    LeafRightLegRoll5ISz = LeafRightLegRoll5IS.LeafRightLegRoll5ISz

    LeafRightLegRoll5PreR = LeafRightLegRoll5PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll5PreRx = LeafRightLegRoll5PreR.LeafRightLegRoll5PreRx
    LeafRightLegRoll5PreRy = LeafRightLegRoll5PreR.LeafRightLegRoll5PreRy
    LeafRightLegRoll5PreRz = LeafRightLegRoll5PreR.LeafRightLegRoll5PreRz

    LeafRightLegRoll5PostR = LeafRightLegRoll5PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightLegRoll5PostRx = LeafRightLegRoll5PostR.LeafRightLegRoll5PostRx
    LeafRightLegRoll5PostRy = LeafRightLegRoll5PostR.LeafRightLegRoll5PostRy
    LeafRightLegRoll5PostRz = LeafRightLegRoll5PostR.LeafRightLegRoll5PostRz

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

    LeafLeftArmRoll5PGX = MatrixField()

    LeafLeftArmRoll5ROrder = LeafLeftArmRoll5ROrderEnumField(default_value=0)

    LeafLeftArmRoll5SC = BoolField(default_value=False)

    LeafLeftArmRoll5IS = LeafLeftArmRoll5ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftArmRoll5ISx = LeafLeftArmRoll5IS.LeafLeftArmRoll5ISx
    LeafLeftArmRoll5ISy = LeafLeftArmRoll5IS.LeafLeftArmRoll5ISy
    LeafLeftArmRoll5ISz = LeafLeftArmRoll5IS.LeafLeftArmRoll5ISz

    LeafLeftArmRoll5PreR = LeafLeftArmRoll5PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll5PreRx = LeafLeftArmRoll5PreR.LeafLeftArmRoll5PreRx
    LeafLeftArmRoll5PreRy = LeafLeftArmRoll5PreR.LeafLeftArmRoll5PreRy
    LeafLeftArmRoll5PreRz = LeafLeftArmRoll5PreR.LeafLeftArmRoll5PreRz

    LeafLeftArmRoll5PostR = LeafLeftArmRoll5PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftArmRoll5PostRx = LeafLeftArmRoll5PostR.LeafLeftArmRoll5PostRx
    LeafLeftArmRoll5PostRy = LeafLeftArmRoll5PostR.LeafLeftArmRoll5PostRy
    LeafLeftArmRoll5PostRz = LeafLeftArmRoll5PostR.LeafLeftArmRoll5PostRz

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

    LeafLeftForeArmRoll5PGX = MatrixField()

    LeafLeftForeArmRoll5ROrder = LeafLeftForeArmRoll5ROrderEnumField(default_value=0)

    LeafLeftForeArmRoll5SC = BoolField(default_value=False)

    LeafLeftForeArmRoll5IS = LeafLeftForeArmRoll5ISField(default_value=(1.0, 1.0, 1.0))
    LeafLeftForeArmRoll5ISx = LeafLeftForeArmRoll5IS.LeafLeftForeArmRoll5ISx
    LeafLeftForeArmRoll5ISy = LeafLeftForeArmRoll5IS.LeafLeftForeArmRoll5ISy
    LeafLeftForeArmRoll5ISz = LeafLeftForeArmRoll5IS.LeafLeftForeArmRoll5ISz

    LeafLeftForeArmRoll5PreR = LeafLeftForeArmRoll5PreRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll5PreRx = LeafLeftForeArmRoll5PreR.LeafLeftForeArmRoll5PreRx
    LeafLeftForeArmRoll5PreRy = LeafLeftForeArmRoll5PreR.LeafLeftForeArmRoll5PreRy
    LeafLeftForeArmRoll5PreRz = LeafLeftForeArmRoll5PreR.LeafLeftForeArmRoll5PreRz

    LeafLeftForeArmRoll5PostR = LeafLeftForeArmRoll5PostRField(default_value=(0.0, 0.0, 0.0))
    LeafLeftForeArmRoll5PostRx = LeafLeftForeArmRoll5PostR.LeafLeftForeArmRoll5PostRx
    LeafLeftForeArmRoll5PostRy = LeafLeftForeArmRoll5PostR.LeafLeftForeArmRoll5PostRy
    LeafLeftForeArmRoll5PostRz = LeafLeftForeArmRoll5PostR.LeafLeftForeArmRoll5PostRz

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

    LeafRightArmRoll5PGX = MatrixField()

    LeafRightArmRoll5ROrder = LeafRightArmRoll5ROrderEnumField(default_value=0)

    LeafRightArmRoll5SC = BoolField(default_value=False)

    LeafRightArmRoll5IS = LeafRightArmRoll5ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightArmRoll5ISx = LeafRightArmRoll5IS.LeafRightArmRoll5ISx
    LeafRightArmRoll5ISy = LeafRightArmRoll5IS.LeafRightArmRoll5ISy
    LeafRightArmRoll5ISz = LeafRightArmRoll5IS.LeafRightArmRoll5ISz

    LeafRightArmRoll5PreR = LeafRightArmRoll5PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll5PreRx = LeafRightArmRoll5PreR.LeafRightArmRoll5PreRx
    LeafRightArmRoll5PreRy = LeafRightArmRoll5PreR.LeafRightArmRoll5PreRy
    LeafRightArmRoll5PreRz = LeafRightArmRoll5PreR.LeafRightArmRoll5PreRz

    LeafRightArmRoll5PostR = LeafRightArmRoll5PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightArmRoll5PostRx = LeafRightArmRoll5PostR.LeafRightArmRoll5PostRx
    LeafRightArmRoll5PostRy = LeafRightArmRoll5PostR.LeafRightArmRoll5PostRy
    LeafRightArmRoll5PostRz = LeafRightArmRoll5PostR.LeafRightArmRoll5PostRz

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

    LeafRightForeArmRoll5PGX = MatrixField()

    LeafRightForeArmRoll5ROrder = LeafRightForeArmRoll5ROrderEnumField(default_value=0)

    LeafRightForeArmRoll5SC = BoolField(default_value=False)

    LeafRightForeArmRoll5IS = LeafRightForeArmRoll5ISField(default_value=(1.0, 1.0, 1.0))
    LeafRightForeArmRoll5ISx = LeafRightForeArmRoll5IS.LeafRightForeArmRoll5ISx
    LeafRightForeArmRoll5ISy = LeafRightForeArmRoll5IS.LeafRightForeArmRoll5ISy
    LeafRightForeArmRoll5ISz = LeafRightForeArmRoll5IS.LeafRightForeArmRoll5ISz

    LeafRightForeArmRoll5PreR = LeafRightForeArmRoll5PreRField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll5PreRx = LeafRightForeArmRoll5PreR.LeafRightForeArmRoll5PreRx
    LeafRightForeArmRoll5PreRy = LeafRightForeArmRoll5PreR.LeafRightForeArmRoll5PreRy
    LeafRightForeArmRoll5PreRz = LeafRightForeArmRoll5PreR.LeafRightForeArmRoll5PreRz

    LeafRightForeArmRoll5PostR = LeafRightForeArmRoll5PostRField(default_value=(0.0, 0.0, 0.0))
    LeafRightForeArmRoll5PostRx = LeafRightForeArmRoll5PostR.LeafRightForeArmRoll5PostRx
    LeafRightForeArmRoll5PostRy = LeafRightForeArmRoll5PostR.LeafRightForeArmRoll5PostRy
    LeafRightForeArmRoll5PostRz = LeafRightForeArmRoll5PostR.LeafRightForeArmRoll5PostRz
