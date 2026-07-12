# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.hik_handle import (
    ChestField,
    ContactsPositionField,
    DTwistRampField,
    DTwistStartEndField,
    DWorldUpVectorEndField,
    DWorldUpVectorField,
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
    PoleVectorField,
    RightArmField,
    RightLegField,
    RollExtractionField,
    SolvingField,
    StiffnessField,
    ToeTipsSizesField,
    ToesFloorContactSetupField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar.time import TimeField
from ....attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class StickinessEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    STICKY = 1


class StickinessEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    STICKY = 1

    NAME_MAP = {
        OFF: "off",
        STICKY: "sticky",
    }


class StickinessEnumField(
    EnumField[StickinessEnumAttrOperator, StickinessEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickinessEnumAttrOperator
    PLUG_CLS = StickinessEnumPlugOperator


class TwistTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    EASE_IN = 1
    EASE_OUT = 2
    EASE_IN_OUT = 3


class TwistTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 0
    EASE_IN = 1
    EASE_OUT = 2
    EASE_IN_OUT = 3

    NAME_MAP = {
        LINEAR: "Linear",
        EASE_IN: "Ease In",
        EASE_OUT: "Ease Out",
        EASE_IN_OUT: "Ease In Out",
    }


class TwistTypeEnumField(
    EnumField[TwistTypeEnumAttrOperator, TwistTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TwistTypeEnumAttrOperator
    PLUG_CLS = TwistTypeEnumPlugOperator


class DWorldUpTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SCENE_UP = 0
    OBJECT_UP = 1
    OBJECT_UP_START_SLASH_END = 2
    OBJECT_ROTATION_UP = 3
    OBJECT_ROTATION_UP_START_SLASH_END = 4
    VECTOR = 5
    VECTOR_START_SLASH_END = 6
    RELATIVE = 7


class DWorldUpTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SCENE_UP = 0
    OBJECT_UP = 1
    OBJECT_UP_START_SLASH_END = 2
    OBJECT_ROTATION_UP = 3
    OBJECT_ROTATION_UP_START_SLASH_END = 4
    VECTOR = 5
    VECTOR_START_SLASH_END = 6
    RELATIVE = 7

    NAME_MAP = {
        SCENE_UP: "Scene Up",
        OBJECT_UP: "Object Up",
        OBJECT_UP_START_SLASH_END: "Object Up (Start/End)",
        OBJECT_ROTATION_UP: "Object Rotation Up",
        OBJECT_ROTATION_UP_START_SLASH_END: "Object Rotation Up (Start/End)",
        VECTOR: "Vector",
        VECTOR_START_SLASH_END: "Vector (Start/End)",
        RELATIVE: "Relative",
    }


class DWorldUpTypeEnumField(
    EnumField[DWorldUpTypeEnumAttrOperator, DWorldUpTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DWorldUpTypeEnumAttrOperator
    PLUG_CLS = DWorldUpTypeEnumPlugOperator


class DForwardAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POSITIVE_X = 0
    NEGATIVE_X = 1
    POSITIVE_Y = 2
    NEGATIVE_Y = 3
    POSITIVE_Z = 4
    NEGATIVE_Z = 5


class DForwardAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POSITIVE_X = 0
    NEGATIVE_X = 1
    POSITIVE_Y = 2
    NEGATIVE_Y = 3
    POSITIVE_Z = 4
    NEGATIVE_Z = 5

    NAME_MAP = {
        POSITIVE_X: "Positive X",
        NEGATIVE_X: "Negative X",
        POSITIVE_Y: "Positive Y",
        NEGATIVE_Y: "Negative Y",
        POSITIVE_Z: "Positive Z",
        NEGATIVE_Z: "Negative Z",
    }


class DForwardAxisEnumField(
    EnumField[DForwardAxisEnumAttrOperator, DForwardAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DForwardAxisEnumAttrOperator
    PLUG_CLS = DForwardAxisEnumPlugOperator


class DWorldUpAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POSITIVE_Y = 0
    NEGATIVE_Y = 1
    CLOSEST_Y = 2
    POSITIVE_Z = 3
    NEGATIVE_Z = 4
    CLOSEST_Z = 5
    POSITIVE_X = 6
    NEGATIVE_X = 7
    CLOSEST_X = 8


class DWorldUpAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POSITIVE_Y = 0
    NEGATIVE_Y = 1
    CLOSEST_Y = 2
    POSITIVE_Z = 3
    NEGATIVE_Z = 4
    CLOSEST_Z = 5
    POSITIVE_X = 6
    NEGATIVE_X = 7
    CLOSEST_X = 8

    NAME_MAP = {
        POSITIVE_Y: "Positive Y",
        NEGATIVE_Y: "Negative Y",
        CLOSEST_Y: "Closest Y",
        POSITIVE_Z: "Positive Z",
        NEGATIVE_Z: "Negative Z",
        CLOSEST_Z: "Closest Z",
        POSITIVE_X: "Positive X",
        NEGATIVE_X: "Negative X",
        CLOSEST_X: "Closest X",
    }


class DWorldUpAxisEnumField(
    EnumField[DWorldUpAxisEnumAttrOperator, DWorldUpAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DWorldUpAxisEnumAttrOperator
    PLUG_CLS = DWorldUpAxisEnumPlugOperator


class DTwistValueTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TOTAL = 0
    START_SLASH_END = 1
    RAMP = 2


class DTwistValueTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TOTAL = 0
    START_SLASH_END = 1
    RAMP = 2

    NAME_MAP = {
        TOTAL: "Total",
        START_SLASH_END: "Start/End",
        RAMP: "Ramp",
    }


class DTwistValueTypeEnumField(
    EnumField[DTwistValueTypeEnumAttrOperator, DTwistValueTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DTwistValueTypeEnumAttrOperator
    PLUG_CLS = DTwistValueTypeEnumPlugOperator


class HikHandle(Transform):
    __slots__ = ()

    NODE_TYPE = "hikHandle"

    startJoint = MessageField()
    hsj = startJoint

    endEffector = MessageField()
    hee = endEffector

    ikSolver = MessageField()
    hsv = ikSolver

    snapEnable = BoolField(default_value=True)
    hsh = snapEnable

    stickiness = StickinessEnumField(default_value=0)
    hs = stickiness

    priority = LongField(default_value=1, min_value=1, soft_max_value=20)
    hpr = priority

    weight = DoubleField(default_value=1.0, min_value=0.0, soft_max_value=100.0)
    hw = weight

    poWeight = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    hpo = poWeight

    poleVector = PoleVectorField(default_value=(0.0, 0.0, 1.0))
    pv = poleVector
    poleVectorX = poleVector.poleVectorX
    pvx = poleVectorX
    poleVectorY = poleVector.poleVectorY
    pvy = poleVectorY
    poleVectorZ = poleVector.poleVectorZ
    pvz = poleVectorZ

    inCurve = DataNurbsCurveField()
    ic = inCurve

    offset = DoubleField(default_value=0.0)
    off = offset

    roll = DoubleAngleField(default_value=0.0)
    rol = roll

    twist = DoubleAngleField(default_value=0.0)
    twi = twist

    rootOnCurve = BoolField(default_value=False)
    roc = rootOnCurve

    twistType = TwistTypeEnumField(default_value=0)
    twt = twistType

    rootTwistMode = BoolField(default_value=False)
    rtm = rootTwistMode

    ikBlend = DoubleField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    ikb = ikBlend

    handleDirtyFlag = BoolField(default_value=False)
    hdf = handleDirtyFlag

    checkSnappingFlag = BoolField(default_value=False)
    csf = checkSnappingFlag

    owningHandleGroup = TypedField()
    ohg = owningHandleGroup

    dofList = TypedField()
    dfl = dofList

    dofListDirtyFlag = BoolField(default_value=False)
    dld = dofListDirtyFlag

    skeletonDirtyFlag = BoolField(default_value=False)
    ods = skeletonDirtyFlag

    ikFkManipulation = BoolField(default_value=False)
    eik = ikFkManipulation

    dWorldUpType = DWorldUpTypeEnumField(default_value=0)
    dwut = dWorldUpType

    dForwardAxis = DForwardAxisEnumField(default_value=0)
    dpa = dForwardAxis

    dWorldUpAxis = DWorldUpAxisEnumField(default_value=0)
    dwua = dWorldUpAxis

    dWorldUpVector = DWorldUpVectorField(default_value=(0.0, 1.0, 0.0))
    dwuv = dWorldUpVector
    dWorldUpVectorX = dWorldUpVector.dWorldUpVectorX
    dwux = dWorldUpVectorX
    dWorldUpVectorY = dWorldUpVector.dWorldUpVectorY
    dwuy = dWorldUpVectorY
    dWorldUpVectorZ = dWorldUpVector.dWorldUpVectorZ
    dwuz = dWorldUpVectorZ

    dWorldUpVectorEnd = DWorldUpVectorEndField(default_value=(0.0, 1.0, 0.0))
    dwve = dWorldUpVectorEnd
    dWorldUpVectorEndX = dWorldUpVectorEnd.dWorldUpVectorEndX
    dwvx = dWorldUpVectorEndX
    dWorldUpVectorEndY = dWorldUpVectorEnd.dWorldUpVectorEndY
    dwvy = dWorldUpVectorEndY
    dWorldUpVectorEndZ = dWorldUpVectorEnd.dWorldUpVectorEndZ
    dwvz = dWorldUpVectorEndZ

    dWorldUpMatrix = MatrixField()
    dwum = dWorldUpMatrix

    dWorldUpMatrixEnd = MatrixField()
    dwue = dWorldUpMatrixEnd

    dTwistValueType = DTwistValueTypeEnumField(default_value=0)
    dtvt = dTwistValueType

    dTwistStartEnd = DTwistStartEndField(default_value=(0.0, 0.0))
    dtse = dTwistStartEnd
    dTwistStart = dTwistStartEnd.dTwistStart
    dtst = dTwistStart
    dTwistEnd = dTwistStartEnd.dTwistEnd
    dten = dTwistEnd

    dTwistRamp = DTwistRampField(default_value=(0.0, 0.0, 0.0))
    dtra = dTwistRamp
    dTwistRampR = dTwistRamp.dTwistRampR
    dtrr = dTwistRampR
    dTwistRampG = dTwistRamp.dTwistRampG
    dtrg = dTwistRampG
    dTwistRampB = dTwistRamp.dTwistRampB
    dtrb = dTwistRampB

    dTwistRampMult = DoubleField(default_value=90.0)
    dtrm = dTwistRampMult

    dTwistControlEnable = BoolField(default_value=False)
    dtce = dTwistControlEnable

    splineIkOldStyle = BoolField(default_value=False)
    sio = splineIkOldStyle

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

    solving = SolvingField(default_value=(0.0, 0.0, 0.0, 1.0, 0.0), min_value=(0.0, 0.0, 0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0, 1.0, 1.0))
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

    floorContacts = FloorContactsField(default_value=(0.0, 0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0, 1.0))
    fc = floorContacts
    handsFloorContact = floorContacts.handsFloorContact
    hfc = handsFloorContact
    feetFloorContact = floorContacts.feetFloorContact
    fec = feetFloorContact
    fingersFloorContact = floorContacts.fingersFloorContact
    fic = fingersFloorContact
    toesFloorContact = floorContacts.toesFloorContact
    tfc = toesFloorContact

    handsFloorContactSetup = HandsFloorContactSetupField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 3.0, 1.0))
    flc = handsFloorContactSetup
    handsFloorPivot = handsFloorContactSetup.handsFloorPivot
    hfp = handsFloorPivot
    handsContactType = handsFloorContactSetup.handsContactType
    hct = handsContactType
    handsContactStiffness = handsFloorContactSetup.handsContactStiffness
    hcs = handsContactStiffness

    contactsPosition = ContactsPositionField(default_value=(7.5, 4.5, 13.0, 7.0, 5.0, 5.0), min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), max_value=(10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0))
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

    feetFloorContactSetup = FeetFloorContactSetupField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 3.0, 1.0))
    fle = feetFloorContactSetup
    feetFloorPivot = feetFloorContactSetup.feetFloorPivot
    fpv = feetFloorPivot
    feetContactType = feetFloorContactSetup.feetContactType
    fct = feetContactType
    feetContactStiffness = feetFloorContactSetup.feetContactStiffness
    fcs = feetContactStiffness

    feetContactPosition = FeetContactPositionField(default_value=(7.5, 4.5, 13.0, 7.0, 5.0, 5.0), min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), max_value=(10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0))
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

    fingersFloorContactSetup = FingersFloorContactSetupField(default_value=(1.0, 0.0), min_value=(0.0, 0.0), max_value=(2.0, 1.0))
    flg = fingersFloorContactSetup
    fingersContactType = fingersFloorContactSetup.fingersContactType
    fcm = fingersContactType
    fingersContactRollStiffness = fingersFloorContactSetup.fingersContactRollStiffness
    hcr = fingersContactRollStiffness

    fingerTipsSizes = FingerTipsSizesField(default_value=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), max_value=(1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0))
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

    toesFloorContactSetup = ToesFloorContactSetupField(default_value=(1.0, 0.0), min_value=(0.0, 0.0), max_value=(2.0, 1.0))
    fli = toesFloorContactSetup
    toesContactType = toesFloorContactSetup.toesContactType
    tct = toesContactType
    toesContactRollStiffness = toesFloorContactSetup.toesContactRollStiffness
    fcr = toesContactRollStiffness

    toeTipsSizes = ToeTipsSizesField(default_value=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), max_value=(1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0))
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

    leftArm = LeftArmField(default_value=(0.0, 1.0, 1.0, 0.0), min_value=(0.0, 0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0, 1.0))
    flm = leftArm
    leftElbowPull = leftArm.leftElbowPull
    ple = leftElbowPull
    leftHandPullChest = leftArm.leftHandPullChest
    cpl = leftHandPullChest
    leftHandPullHips = leftArm.leftHandPullHips
    plh = leftHandPullHips
    leftFingerBasePull = leftArm.leftFingerBasePull
    plb = leftFingerBasePull

    rightArm = RightArmField(default_value=(0.0, 1.0, 1.0, 0.0), min_value=(0.0, 0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0, 1.0))
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

    leftLeg = LeftLegField(default_value=(0.0, 1.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    flq = leftLeg
    leftKneePull = leftLeg.leftKneePull
    plk = leftKneePull
    leftFootPull = leftLeg.leftFootPull
    plf = leftFootPull
    leftToeBasePull = leftLeg.leftToeBasePull
    plt = leftToeBasePull

    rightLeg = RightLegField(default_value=(0.0, 1.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
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

    stiffness = StiffnessField(default_value=(0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6000000238418579, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0))
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

    killPitch = KillPitchField(default_value=(0.0, 0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0, 1.0))
    kp = killPitch
    leftElbowKillPitch = killPitch.leftElbowKillPitch
    lek = leftElbowKillPitch
    rightElbowKillPitch = killPitch.rightElbowKillPitch
    rek = rightElbowKillPitch
    leftKneeKillPitch = killPitch.leftKneeKillPitch
    lkk = leftKneeKillPitch
    rightKneeKillPitch = killPitch.rightKneeKillPitch
    rkk = rightKneeKillPitch

    rollExtraction = RollExtractionField(default_value=(0.0, 0.0, 0.6000000238418579, 0.0, 0.6000000238418579, 0.0, 0.6000000238418579, 0.0, 0.6000000238418579, 0.0, 0.6000000238418579, 0.0, 0.6000000238418579, 0.0, 0.6000000238418579, 0.0, 0.6000000238418579), min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0))
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
