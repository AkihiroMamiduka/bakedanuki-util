# coding: utf-8
from .._core import Transform
from .....attr.define.node_attr.joint import (
    BindInverseScaleField,
    BindJointOrientField,
    BindRotateAxisField,
    BindRotationField,
    BindScaleField,
    FkRotateField,
    IkRotateField,
    InverseScaleField,
    JointOrientField,
    MaxRotateDampRangeField,
    MaxRotateDampStrengthField,
    MinRotateDampRangeField,
    MinRotateDampStrengthField,
    PreferredAngleField,
    StiffnessField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.dt.matrix import DataMatrixField
from .....attr.define.std.dt.string import DataStringField


class DrawStyleEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BONE = 0
    MULTI_MINUS_CHILD_AS_BOX = 1
    NONE = 2
    JOINT = 3


class DrawStyleEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BONE = 0
    MULTI_MINUS_CHILD_AS_BOX = 1
    NONE = 2
    JOINT = 3

    NAME_MAP = {
        BONE: "Bone",
        MULTI_MINUS_CHILD_AS_BOX: "Multi-child as Box",
        NONE: "None",
        JOINT: "Joint",
    }


class DrawStyleEnumField(
    EnumField[DrawStyleEnumAttrOperator, DrawStyleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DrawStyleEnumAttrOperator
    PLUG_CLS = DrawStyleEnumPlugOperator


class SideEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CENTER = 0
    LEFT = 1
    RIGHT = 2
    NONE = 3


class SideEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CENTER = 0
    LEFT = 1
    RIGHT = 2
    NONE = 3

    NAME_MAP = {
        CENTER: "Center",
        LEFT: "Left",
        RIGHT: "Right",
        NONE: "None",
    }


class SideEnumField(
    EnumField[SideEnumAttrOperator, SideEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SideEnumAttrOperator
    PLUG_CLS = SideEnumPlugOperator


class TypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    ROOT = 1
    HIP = 2
    KNEE = 3
    FOOT = 4
    TOE = 5
    SPINE = 6
    NECK = 7
    HEAD = 8
    COLLAR = 9
    SHOULDER = 10
    ELBOW = 11
    HAND = 12
    FINGER = 13
    THUMB = 14
    PROPA = 15
    PROPB = 16
    PROPC = 17
    OTHER = 18
    INDEX_FINGER = 19
    MIDDLE_FINGER = 20
    RING_FINGER = 21
    PINKY_FINGER = 22
    EXTRA_FINGER = 23
    BIG_TOE = 24
    INDEX_TOE = 25
    MIDDLE_TOE = 26
    RING_TOE = 27
    PINKY_TOE = 28
    FOOT_THUMB = 29


class TypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    ROOT = 1
    HIP = 2
    KNEE = 3
    FOOT = 4
    TOE = 5
    SPINE = 6
    NECK = 7
    HEAD = 8
    COLLAR = 9
    SHOULDER = 10
    ELBOW = 11
    HAND = 12
    FINGER = 13
    THUMB = 14
    PROPA = 15
    PROPB = 16
    PROPC = 17
    OTHER = 18
    INDEX_FINGER = 19
    MIDDLE_FINGER = 20
    RING_FINGER = 21
    PINKY_FINGER = 22
    EXTRA_FINGER = 23
    BIG_TOE = 24
    INDEX_TOE = 25
    MIDDLE_TOE = 26
    RING_TOE = 27
    PINKY_TOE = 28
    FOOT_THUMB = 29

    NAME_MAP = {
        NONE: "None",
        ROOT: "Root",
        HIP: "Hip",
        KNEE: "Knee",
        FOOT: "Foot",
        TOE: "Toe",
        SPINE: "Spine",
        NECK: "Neck",
        HEAD: "Head",
        COLLAR: "Collar",
        SHOULDER: "Shoulder",
        ELBOW: "Elbow",
        HAND: "Hand",
        FINGER: "Finger",
        THUMB: "Thumb",
        PROPA: "PropA",
        PROPB: "PropB",
        PROPC: "PropC",
        OTHER: "Other",
        INDEX_FINGER: "Index Finger",
        MIDDLE_FINGER: "Middle Finger",
        RING_FINGER: "Ring Finger",
        PINKY_FINGER: "Pinky Finger",
        EXTRA_FINGER: "Extra Finger",
        BIG_TOE: "Big Toe",
        INDEX_TOE: "Index Toe",
        MIDDLE_TOE: "Middle Toe",
        RING_TOE: "Ring Toe",
        PINKY_TOE: "Pinky Toe",
        FOOT_THUMB: "Foot Thumb",
    }


class TypeEnumField(
    EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class _GeneratedJoint(Transform):
    __slots__ = ()

    NODE_TYPE = "joint"

    jointOrientType = DataStringField()
    jot = jointOrientType

    jointType = DataStringField()
    jt = jointType

    jointTypeX = BoolField(default_value=True)
    jtx = jointTypeX

    jointTypeY = BoolField(default_value=True)
    jty = jointTypeY

    jointTypeZ = BoolField(default_value=True)
    jtz = jointTypeZ

    dofMask = LongField(default_value=2021227011, writable=False)
    dm = dofMask

    jointOrient = JointOrientField(default_value=(0.0, 0.0, 0.0))
    jo = jointOrient
    jointOrientX = jointOrient.jointOrientX
    jox = jointOrientX
    jointOrientY = jointOrient.jointOrientY
    joy = jointOrientY
    jointOrientZ = jointOrient.jointOrientZ
    joz = jointOrientZ

    segmentScaleCompensate = BoolField(default_value=True)
    ssc = segmentScaleCompensate

    inverseScale = InverseScaleField(default_value=(1.0, 1.0, 1.0))
    is_ = inverseScale
    inverseScaleX = inverseScale.inverseScaleX
    isx = inverseScaleX
    inverseScaleY = inverseScale.inverseScaleY
    isy = inverseScaleY
    inverseScaleZ = inverseScale.inverseScaleZ
    isz = inverseScaleZ

    stiffness = StiffnessField(default_value=(0.0, 0.0, 0.0))
    st = stiffness
    stiffnessX = stiffness.stiffnessX
    stx = stiffnessX
    stiffnessY = stiffness.stiffnessY
    sty = stiffnessY
    stiffnessZ = stiffness.stiffnessZ
    stz = stiffnessZ

    preferredAngle = PreferredAngleField(default_value=(0.0, 0.0, 0.0))
    pa = preferredAngle
    preferredAngleX = preferredAngle.preferredAngleX
    pax = preferredAngleX
    preferredAngleY = preferredAngle.preferredAngleY
    pay = preferredAngleY
    preferredAngleZ = preferredAngle.preferredAngleZ
    paz = preferredAngleZ

    minRotateDampRange = MinRotateDampRangeField(default_value=(0.0, 0.0, 0.0))
    ndr = minRotateDampRange
    minRotateDampRangeX = minRotateDampRange.minRotateDampRangeX
    ndx = minRotateDampRangeX
    minRotateDampRangeY = minRotateDampRange.minRotateDampRangeY
    ndy = minRotateDampRangeY
    minRotateDampRangeZ = minRotateDampRange.minRotateDampRangeZ
    ndz = minRotateDampRangeZ

    minRotateDampStrength = MinRotateDampStrengthField(default_value=(0.0, 0.0, 0.0))
    nst = minRotateDampStrength
    minRotateDampStrengthX = minRotateDampStrength.minRotateDampStrengthX
    nstx = minRotateDampStrengthX
    minRotateDampStrengthY = minRotateDampStrength.minRotateDampStrengthY
    nsty = minRotateDampStrengthY
    minRotateDampStrengthZ = minRotateDampStrength.minRotateDampStrengthZ
    nstz = minRotateDampStrengthZ

    maxRotateDampRange = MaxRotateDampRangeField(default_value=(0.0, 0.0, 0.0))
    xdr = maxRotateDampRange
    maxRotateDampRangeX = maxRotateDampRange.maxRotateDampRangeX
    xdx = maxRotateDampRangeX
    maxRotateDampRangeY = maxRotateDampRange.maxRotateDampRangeY
    xdy = maxRotateDampRangeY
    maxRotateDampRangeZ = maxRotateDampRange.maxRotateDampRangeZ
    xdz = maxRotateDampRangeZ

    maxRotateDampStrength = MaxRotateDampStrengthField(default_value=(0.0, 0.0, 0.0))
    xst = maxRotateDampStrength
    maxRotateDampStrengthX = maxRotateDampStrength.maxRotateDampStrengthX
    xstx = maxRotateDampStrengthX
    maxRotateDampStrengthY = maxRotateDampStrength.maxRotateDampStrengthY
    xsty = maxRotateDampStrengthY
    maxRotateDampStrengthZ = maxRotateDampStrength.maxRotateDampStrengthZ
    xstz = maxRotateDampStrengthZ

    bindPose = DataMatrixField()
    bps = bindPose

    bindRotation = BindRotationField(default_value=(0.0, 0.0, 0.0))
    br = bindRotation
    bindRotationX = bindRotation.bindRotationX
    brx = bindRotationX
    bindRotationY = bindRotation.bindRotationY
    bry = bindRotationY
    bindRotationZ = bindRotation.bindRotationZ
    brz = bindRotationZ

    bindJointOrient = BindJointOrientField(default_value=(0.0, 0.0, 0.0))
    bjo = bindJointOrient
    bindJointOrientX = bindJointOrient.bindJointOrientX
    bjx = bindJointOrientX
    bindJointOrientY = bindJointOrient.bindJointOrientY
    bjy = bindJointOrientY
    bindJointOrientZ = bindJointOrient.bindJointOrientZ
    bjz = bindJointOrientZ

    bindRotateAxis = BindRotateAxisField(default_value=(0.0, 0.0, 0.0))
    bra = bindRotateAxis
    bindRotateAxisX = bindRotateAxis.bindRotateAxisX
    brax = bindRotateAxisX
    bindRotateAxisY = bindRotateAxis.bindRotateAxisY
    bray = bindRotateAxisY
    bindRotateAxisZ = bindRotateAxis.bindRotateAxisZ
    braz = bindRotateAxisZ

    bindScale = BindScaleField(default_value=(1.0, 1.0, 1.0))
    bs = bindScale
    bindScaleX = bindScale.bindScaleX
    bsx = bindScaleX
    bindScaleY = bindScale.bindScaleY
    bsy = bindScaleY
    bindScaleZ = bindScale.bindScaleZ
    bsz = bindScaleZ

    bindInverseScale = BindInverseScaleField(default_value=(1.0, 1.0, 1.0))
    bis = bindInverseScale
    bindInverseScaleX = bindInverseScale.bindInverseScaleX
    bix = bindInverseScaleX
    bindInverseScaleY = bindInverseScale.bindInverseScaleY
    biy = bindInverseScaleY
    bindInverseScaleZ = bindInverseScale.bindInverseScaleZ
    biz = bindInverseScaleZ

    bindSegmentScaleCompensate = BoolField(default_value=True)
    bsc = bindSegmentScaleCompensate

    isIKDirtyFlag = BoolField(default_value=False)
    idf = isIKDirtyFlag

    inIKSolveFlag = BoolField(default_value=False)
    isf = inIKSolveFlag

    drawStyle = DrawStyleEnumField(default_value=0)
    ds = drawStyle

    drawLabel = BoolField(default_value=False)
    dl = drawLabel

    side = SideEnumField(default_value=0)
    sd = side

    type = TypeEnumField(default_value=0)
    typ = type

    otherType = DataStringField()
    otp = otherType

    ikRotate = IkRotateField(default_value=(0.0, 0.0, 0.0))
    ikr = ikRotate
    ikRotateX = ikRotate.ikRotateX
    irx = ikRotateX
    ikRotateY = ikRotate.ikRotateY
    iry = ikRotateY
    ikRotateZ = ikRotate.ikRotateZ
    irz = ikRotateZ

    fkRotate = FkRotateField(default_value=(0.0, 0.0, 0.0))
    fkr = fkRotate
    fkRotateX = fkRotate.fkRotateX
    frx = fkRotateX
    fkRotateY = fkRotate.fkRotateY
    fry = fkRotateY
    fkRotateZ = fkRotate.fkRotateZ
    frz = fkRotateZ

    radius = DoubleField(default_value=1.0)
    radi = radius

    hikNodeID = LongField(default_value=-1)
    hni = hikNodeID

    hikFkJoint = MessageField()
    hfk = hikFkJoint
