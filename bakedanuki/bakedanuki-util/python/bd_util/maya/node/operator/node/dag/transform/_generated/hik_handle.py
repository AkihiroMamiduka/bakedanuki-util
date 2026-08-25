# coding: utf-8
from ..ik_handle import IkHandle
from .....attr.define.node_attr.hik_handle import (
    ChestField,
    ContactsPositionField,
    ExtraField,
    FeetContactPositionField,
    FeetFloorContactSetupField,
    FingerTipsSizesField,
    FingersFloorContactSetupField,
    FloorContactsField,
    HandsFloorContactSetupField,
    HeadField,
    HipsField,
    KillPitchField,
    LeftArmField,
    LeftLegField,
    RightArmField,
    RightLegField,
    RollExtractionField,
    SolvingField,
    StiffnessField,
    ToeTipsSizesField,
    ToesFloorContactSetupField,
)
from .....attr.define.std.at.matrix import MatrixField
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.unit.time import TimeField


class GeneratedHikHandle(IkHandle):
    __slots__ = ()

    NODE_TYPE = "hikHandle"

    effectors = BoolField(multi=True, default_value=False)
    eff = effectors

    leftFootGroundPlane = DoubleField(default_value=0.0)
    lfg = leftFootGroundPlane

    rightFootGroundPlane = DoubleField(default_value=0.0)
    rfg = rightFootGroundPlane

    rightFootOrientedGroundPlane = MatrixField()
    rog = rightFootOrientedGroundPlane

    leftFootOrientedGroundPlane = MatrixField()
    log = leftFootOrientedGroundPlane

    leftHandGroundPlane = DoubleField(default_value=0.0)
    lhg = leftHandGroundPlane

    rightHandGroundPlane = DoubleField(default_value=0.0)
    rhg = rightHandGroundPlane

    leftHandOrientedGroundPlane = MatrixField()
    loh = leftHandOrientedGroundPlane

    rightHandOrientedGroundPlane = MatrixField()
    roh = rightHandOrientedGroundPlane

    joints = MessageField(multi=True)
    jt = joints

    fkjoints = MessageField(multi=True)
    fj = fkjoints

    fkmatrix = MatrixField(multi=True)
    fm = fkmatrix

    time = TimeField(default_value=0.0)
    tim = time

    defaultMatrix = MatrixField(multi=True)
    dm = defaultMatrix

    stancePoseMatrix = MatrixField(multi=True)
    sm = stancePoseMatrix

    usingMB55Rig = BoolField(default_value=False)
    m55 = usingMB55Rig

    activate = BoolField(default_value=True)
    act = activate

    convertScale = BoolField(default_value=True)
    cs = convertScale

    propertyChanged = MessageField()
    pc = propertyChanged

    solving = SolvingField(
        default_value=(0, False, 0.0, True, 0),
        min_value=(0.0, 0.0, 0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0, 1.0, 1.0),
    )
    sol = solving
    postureType = solving.postureType
    pt = postureType
    expertMode = solving.expertMode
    exp = expertMode
    realisticShoulderSolving = solving.realisticShoulderSolving
    rss = realisticShoulderSolving
    solveFingers = solving.solveFingers
    sf = solveFingers
    hipTranslationMode = solving.hipTranslationMode
    htm = hipTranslationMode

    floorContacts = FloorContactsField(
        default_value=(False, False, False, False),
        min_value=(0.0, 0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0, 1.0),
    )
    fc = floorContacts
    handsFloorContact = floorContacts.handsFloorContact
    hfc = handsFloorContact
    feetFloorContact = floorContacts.feetFloorContact
    fec = feetFloorContact
    fingersFloorContact = floorContacts.fingersFloorContact
    fic = fingersFloorContact
    toesFloorContact = floorContacts.toesFloorContact
    tfc = toesFloorContact

    handsFloorContactSetup = HandsFloorContactSetupField(
        default_value=(0, 0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(2.0, 3.0, 1.0),
    )
    flc = handsFloorContactSetup
    handsFloorPivot = handsFloorContactSetup.handsFloorPivot
    hfp = handsFloorPivot
    handsContactType = handsFloorContactSetup.handsContactType
    hct = handsContactType
    handsContactStiffness = handsFloorContactSetup.handsContactStiffness
    hcs = handsContactStiffness

    contactsPosition = ContactsPositionField(
        default_value=(7.5, 4.5, 13.0, 7.0, 5.0, 5.0),
        min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        max_value=(10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0),
    )
    cp = contactsPosition
    handHeight = contactsPosition.handHeight
    hh = handHeight
    handBack = contactsPosition.handBack
    hb = handBack
    handMiddle = contactsPosition.handMiddle
    hm = handMiddle
    handFront = contactsPosition.handFront
    hf = handFront
    handInSide = contactsPosition.handInSide
    his = handInSide
    handOutSide = contactsPosition.handOutSide
    hos = handOutSide

    feetFloorContactSetup = FeetFloorContactSetupField(
        default_value=(0, 0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(2.0, 3.0, 1.0),
    )
    fle = feetFloorContactSetup
    feetFloorPivot = feetFloorContactSetup.feetFloorPivot
    fpv = feetFloorPivot
    feetContactType = feetFloorContactSetup.feetContactType
    fct = feetContactType
    feetContactStiffness = feetFloorContactSetup.feetContactStiffness
    fcs = feetContactStiffness

    feetContactPosition = FeetContactPositionField(
        default_value=(7.5, 4.5, 13.0, 7.0, 5.0, 5.0),
        min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        max_value=(10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0),
    )
    flf = feetContactPosition
    footHeight = feetContactPosition.footHeight
    fh = footHeight
    footBack = feetContactPosition.footBack
    fra = footBack
    footMiddle = feetContactPosition.footMiddle
    fma = footMiddle
    footFront = feetContactPosition.footFront
    ffm = footFront
    footInSide = feetContactPosition.footInSide
    fia = footInSide
    footOutSide = feetContactPosition.footOutSide
    foa = footOutSide

    fingersFloorContactSetup = FingersFloorContactSetupField(
        default_value=(1, 0.0), min_value=(0.0, 0.0), max_value=(2.0, 1.0)
    )
    flg = fingersFloorContactSetup
    fingersContactType = fingersFloorContactSetup.fingersContactType
    fcm = fingersContactType
    fingersContactRollStiffness = (
        fingersFloorContactSetup.fingersContactRollStiffness
    )
    hcr = fingersContactRollStiffness

    fingerTipsSizes = FingerTipsSizesField(
        default_value=(
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
        ),
        min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        max_value=(
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
        ),
    )
    fts = fingerTipsSizes
    leftHandThumbTip = fingerTipsSizes.leftHandThumbTip
    ltt = leftHandThumbTip
    leftHandIndexTip = fingerTipsSizes.leftHandIndexTip
    lit = leftHandIndexTip
    leftHandMiddleTip = fingerTipsSizes.leftHandMiddleTip
    lmt = leftHandMiddleTip
    leftHandRingTip = fingerTipsSizes.leftHandRingTip
    lrt = leftHandRingTip
    leftHandPinkyTip = fingerTipsSizes.leftHandPinkyTip
    lpt = leftHandPinkyTip
    leftHandExtraFingerTip = fingerTipsSizes.leftHandExtraFingerTip
    lxt = leftHandExtraFingerTip
    rightHandThumbTip = fingerTipsSizes.rightHandThumbTip
    rtt = rightHandThumbTip
    rightHandIndexTip = fingerTipsSizes.rightHandIndexTip
    rit = rightHandIndexTip
    rightHandMiddleTip = fingerTipsSizes.rightHandMiddleTip
    rmt = rightHandMiddleTip
    rightHandRingTip = fingerTipsSizes.rightHandRingTip
    rrt = rightHandRingTip
    rightHandPinkyTip = fingerTipsSizes.rightHandPinkyTip
    rpp = rightHandPinkyTip
    rightHandExtraFingerTip = fingerTipsSizes.rightHandExtraFingerTip
    rxt = rightHandExtraFingerTip

    toesFloorContactSetup = ToesFloorContactSetupField(
        default_value=(1, 0.0), min_value=(0.0, 0.0), max_value=(2.0, 1.0)
    )
    fli = toesFloorContactSetup
    toesContactType = toesFloorContactSetup.toesContactType
    tct = toesContactType
    toesContactRollStiffness = toesFloorContactSetup.toesContactRollStiffness
    fcr = toesContactRollStiffness

    toeTipsSizes = ToeTipsSizesField(
        default_value=(
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
        ),
        min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        max_value=(
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
            1000.0,
        ),
    )
    flj = toeTipsSizes
    leftFootThumbTip = toeTipsSizes.leftFootThumbTip
    ttl = leftFootThumbTip
    leftFootIndexTip = toeTipsSizes.leftFootIndexTip
    til = leftFootIndexTip
    leftFootMiddleTip = toeTipsSizes.leftFootMiddleTip
    tml = leftFootMiddleTip
    leftFootRingTip = toeTipsSizes.leftFootRingTip
    trl = leftFootRingTip
    leftFootPinkyTip = toeTipsSizes.leftFootPinkyTip
    tpl = leftFootPinkyTip
    leftFootExtraFingerTip = toeTipsSizes.leftFootExtraFingerTip
    txl = leftFootExtraFingerTip
    rightFootThumbTip = toeTipsSizes.rightFootThumbTip
    ttr = rightFootThumbTip
    rightFootIndexTip = toeTipsSizes.rightFootIndexTip
    tir = rightFootIndexTip
    rightFootMiddleTip = toeTipsSizes.rightFootMiddleTip
    tmr = rightFootMiddleTip
    rightFootRingTip = toeTipsSizes.rightFootRingTip
    trr = rightFootRingTip
    rightFootPinkyTip = toeTipsSizes.rightFootPinkyTip
    tpr = rightFootPinkyTip
    rightFootExtraFingerTip = toeTipsSizes.rightFootExtraFingerTip
    txr = rightFootExtraFingerTip

    head = HeadField(default_value=0.0, min_value=0.0, max_value=1.0)
    fll = head
    headPull = head.headPull
    phd = headPull

    leftArm = LeftArmField(
        default_value=(0.0, 1.0, 1.0, 0.0),
        min_value=(0.0, 0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0, 1.0),
    )
    flm = leftArm
    leftElbowPull = leftArm.leftElbowPull
    ple = leftElbowPull
    leftHandPullChest = leftArm.leftHandPullChest
    cpl = leftHandPullChest
    leftHandPullHips = leftArm.leftHandPullHips
    plh = leftHandPullHips
    leftFingerBasePull = leftArm.leftFingerBasePull
    plb = leftFingerBasePull

    rightArm = RightArmField(
        default_value=(0.0, 1.0, 1.0, 0.0),
        min_value=(0.0, 0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0, 1.0),
    )
    fln = rightArm
    rightElbowPull = rightArm.rightElbowPull
    pre = rightElbowPull
    rightHandPullChest = rightArm.rightHandPullChest
    cpr = rightHandPullChest
    rightHandPullHips = rightArm.rightHandPullHips
    prh = rightHandPullHips
    rightFingerBasePull = rightArm.rightFingerBasePull
    prb = rightFingerBasePull

    chest = ChestField(default_value=0.0, min_value=0.0, max_value=1.0)
    flo = chest
    chestPull = chest.chestPull
    rcp = chestPull

    hips = HipsField(default_value=0.0, min_value=0.0, max_value=1.0)
    flp = hips
    hipsPull = hips.hipsPull
    chp = hipsPull

    leftLeg = LeftLegField(
        default_value=(0.0, 1.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    flq = leftLeg
    leftKneePull = leftLeg.leftKneePull
    plk = leftKneePull
    leftFootPull = leftLeg.leftFootPull
    plf = leftFootPull
    leftToeBasePull = leftLeg.leftToeBasePull
    plt = leftToeBasePull

    rightLeg = RightLegField(
        default_value=(0.0, 1.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    flr = rightLeg
    rightKneePull = rightLeg.rightKneePull
    prk = rightKneePull
    rightFootPull = rightLeg.rightFootPull
    prf = rightFootPull
    rightToeBasePull = rightLeg.rightToeBasePull
    prt = rightToeBasePull

    extra = ExtraField(default_value=10.0, min_value=0.0, max_value=30.0)
    ex = extra
    pullIterationCount = extra.pullIterationCount
    pic = pullIterationCount

    stiffness = StiffnessField(
        default_value=(
            0.0,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.6000000238418579,
            0.0,
            0.0,
            0.0,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
            0.5,
        ),
        min_value=(
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ),
        max_value=(
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
        ),
    )
    st = stiffness
    neckStiffness = stiffness.neckStiffness
    nst = neckStiffness
    leftShoulderStiffness = stiffness.leftShoulderStiffness
    rlco = leftShoulderStiffness
    leftArmStiffness = stiffness.leftArmStiffness
    rle = leftArmStiffness
    leftElbowMaxExtension = stiffness.leftElbowMaxExtension
    mle = leftElbowMaxExtension
    leftElbowCompressionFactor = stiffness.leftElbowCompressionFactor
    cle = leftElbowCompressionFactor
    rightShoulderStiffness = stiffness.rightShoulderStiffness
    rrc = rightShoulderStiffness
    rightArmStiffness = stiffness.rightArmStiffness
    rre = rightArmStiffness
    rightElbowMaxExtension = stiffness.rightElbowMaxExtension
    mre = rightElbowMaxExtension
    rightElbowCompressionFactor = stiffness.rightElbowCompressionFactor
    cre = rightElbowCompressionFactor
    hipsEnforceGravity = stiffness.hipsEnforceGravity
    egr = hipsEnforceGravity
    chestStiffness = stiffness.chestStiffness
    rco = chestStiffness
    spineStiffness = stiffness.spineStiffness
    sst = spineStiffness
    hipsStiffness = stiffness.hipsStiffness
    rho = hipsStiffness
    leftKneeMaxExtension = stiffness.leftKneeMaxExtension
    mlk = leftKneeMaxExtension
    leftLegStiffness = stiffness.leftLegStiffness
    rlk = leftLegStiffness
    leftKneeCompressionFactor = stiffness.leftKneeCompressionFactor
    clk = leftKneeCompressionFactor
    rightLegStiffness = stiffness.rightLegStiffness
    rrk = rightLegStiffness
    rightKneeMaxExtension = stiffness.rightKneeMaxExtension
    mrk = rightKneeMaxExtension
    rightKneeCompressionFactor = stiffness.rightKneeCompressionFactor
    crk = rightKneeCompressionFactor

    killPitch = KillPitchField(
        default_value=(False, False, False, False),
        min_value=(0.0, 0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0, 1.0),
    )
    kp = killPitch
    leftElbowKillPitch = killPitch.leftElbowKillPitch
    lek = leftElbowKillPitch
    rightElbowKillPitch = killPitch.rightElbowKillPitch
    rek = rightElbowKillPitch
    leftKneeKillPitch = killPitch.leftKneeKillPitch
    lkk = leftKneeKillPitch
    rightKneeKillPitch = killPitch.rightKneeKillPitch
    rkk = rightKneeKillPitch

    rollExtraction = RollExtractionField(
        default_value=(
            0,
            False,
            0.6000000238418579,
            False,
            0.6000000238418579,
            False,
            0.6000000238418579,
            False,
            0.6000000238418579,
            False,
            0.6000000238418579,
            False,
            0.6000000238418579,
            False,
            0.6000000238418579,
            False,
            0.6000000238418579,
        ),
        min_value=(
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ),
        max_value=(
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
        ),
    )
    re = rollExtraction
    rollExtractionMode = rollExtraction.rollExtractionMode
    rem = rollExtractionMode
    leftArmRollMode = rollExtraction.leftArmRollMode
    larm = leftArmRollMode
    leftArmRoll = rollExtraction.leftArmRoll
    lar = leftArmRoll
    leftForeArmRollMode = rollExtraction.leftForeArmRollMode
    lfrm = leftForeArmRollMode
    leftForeArmRoll = rollExtraction.leftForeArmRoll
    lfr = leftForeArmRoll
    rightArmRollMode = rollExtraction.rightArmRollMode
    rarm = rightArmRollMode
    rightArmRoll = rollExtraction.rightArmRoll
    rar = rightArmRoll
    rightForeArmRollMode = rollExtraction.rightForeArmRollMode
    rfrm = rightForeArmRollMode
    rightForeArmRoll = rollExtraction.rightForeArmRoll
    rfr = rightForeArmRoll
    leftUpLegRollMode = rollExtraction.leftUpLegRollMode
    lurm = leftUpLegRollMode
    leftUpLegRoll = rollExtraction.leftUpLegRoll
    lur = leftUpLegRoll
    leftLegRollMode = rollExtraction.leftLegRollMode
    llrm = leftLegRollMode
    leftLegRoll = rollExtraction.leftLegRoll
    llr = leftLegRoll
    rightUpLegRollMode = rollExtraction.rightUpLegRollMode
    rurm = rightUpLegRollMode
    rightUpLegRoll = rollExtraction.rightUpLegRoll
    rur = rightUpLegRoll
    rightLegRollMode = rollExtraction.rightLegRollMode
    rlrm = rightLegRollMode
    rightLegRoll = rollExtraction.rightLegRoll
    rlro = rightLegRoll
