# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.dt.matrix import DataMatrixField
from ..custom import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class Target_targetRotateOrderEnumPlugOperator(
    EnumPlugOperator["Target_targetRotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Target_targetRotateOrderEnumAttrOperator(
    EnumAttrOperator[Target_targetRotateOrderEnumPlugOperator]
):
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


class Target_targetRotateOrderEnumField(
    EnumField[
        Target_targetRotateOrderEnumAttrOperator,
        Target_targetRotateOrderEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotateOrderEnumAttrOperator
    PLUG_CLS = Target_targetRotateOrderEnumPlugOperator


class Target_targetRotateCachedPlugOperator(
    DoubleAngle3CompoundBasePlugOperator[
        "Target_targetRotateCachedAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotateCachedX", "ctrx"),
        ("targetRotateCachedY", "ctry"),
        ("targetRotateCachedZ", "ctrz"),
    )

    targetRotateCachedX = DoubleAngleField(default_value=0.0)
    ctrx = targetRotateCachedX

    targetRotateCachedY = DoubleAngleField(default_value=0.0)
    ctry = targetRotateCachedY

    targetRotateCachedZ = DoubleAngleField(default_value=0.0)
    ctrz = targetRotateCachedZ


class Target_targetRotateCachedAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[Target_targetRotateCachedPlugOperator]
):
    __slots__ = ()

    targetRotateCachedX = DoubleAngleField(default_value=0.0)
    ctrx = targetRotateCachedX

    targetRotateCachedY = DoubleAngleField(default_value=0.0)
    ctry = targetRotateCachedY

    targetRotateCachedZ = DoubleAngleField(default_value=0.0)
    ctrz = targetRotateCachedZ


class Target_targetRotateCachedField(
    DoubleAngle3CompoundBaseField[
        Target_targetRotateCachedAttrOperator,
        Target_targetRotateCachedPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotateCachedAttrOperator
    PLUG_CLS = Target_targetRotateCachedPlugOperator

    targetRotateCachedX = DoubleAngleField(default_value=0.0)
    ctrx = targetRotateCachedX

    targetRotateCachedY = DoubleAngleField(default_value=0.0)
    ctry = targetRotateCachedY

    targetRotateCachedZ = DoubleAngleField(default_value=0.0)
    ctrz = targetRotateCachedZ


class Target_targetTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Target_targetTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetTranslateX", "ttx"),
        ("targetTranslateY", "tty"),
        ("targetTranslateZ", "ttz"),
    )

    targetTranslateX = DoubleLinearField(default_value=0.0)
    ttx = targetTranslateX

    targetTranslateY = DoubleLinearField(default_value=0.0)
    tty = targetTranslateY

    targetTranslateZ = DoubleLinearField(default_value=0.0)
    ttz = targetTranslateZ


class Target_targetTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Target_targetTranslatePlugOperator]
):
    __slots__ = ()

    targetTranslateX = DoubleLinearField(default_value=0.0)
    ttx = targetTranslateX

    targetTranslateY = DoubleLinearField(default_value=0.0)
    tty = targetTranslateY

    targetTranslateZ = DoubleLinearField(default_value=0.0)
    ttz = targetTranslateZ


class Target_targetTranslateField(
    DoubleLinear3CompoundBaseField[
        Target_targetTranslateAttrOperator, Target_targetTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetTranslateAttrOperator
    PLUG_CLS = Target_targetTranslatePlugOperator

    targetTranslateX = DoubleLinearField(default_value=0.0)
    ttx = targetTranslateX

    targetTranslateY = DoubleLinearField(default_value=0.0)
    tty = targetTranslateY

    targetTranslateZ = DoubleLinearField(default_value=0.0)
    ttz = targetTranslateZ


class Target_targetRotatePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "Target_targetRotatePivotAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotatePivotX", "trpx"),
        ("targetRotatePivotY", "trpy"),
        ("targetRotatePivotZ", "trpz"),
    )

    targetRotatePivotX = DoubleLinearField(default_value=0.0)
    trpx = targetRotatePivotX

    targetRotatePivotY = DoubleLinearField(default_value=0.0)
    trpy = targetRotatePivotY

    targetRotatePivotZ = DoubleLinearField(default_value=0.0)
    trpz = targetRotatePivotZ


class Target_targetRotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Target_targetRotatePivotPlugOperator]
):
    __slots__ = ()

    targetRotatePivotX = DoubleLinearField(default_value=0.0)
    trpx = targetRotatePivotX

    targetRotatePivotY = DoubleLinearField(default_value=0.0)
    trpy = targetRotatePivotY

    targetRotatePivotZ = DoubleLinearField(default_value=0.0)
    trpz = targetRotatePivotZ


class Target_targetRotatePivotField(
    DoubleLinear3CompoundBaseField[
        Target_targetRotatePivotAttrOperator,
        Target_targetRotatePivotPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotatePivotAttrOperator
    PLUG_CLS = Target_targetRotatePivotPlugOperator

    targetRotatePivotX = DoubleLinearField(default_value=0.0)
    trpx = targetRotatePivotX

    targetRotatePivotY = DoubleLinearField(default_value=0.0)
    trpy = targetRotatePivotY

    targetRotatePivotZ = DoubleLinearField(default_value=0.0)
    trpz = targetRotatePivotZ


class Target_targetRotateTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "Target_targetRotateTranslateAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotateTranslateX", "trtx"),
        ("targetRotateTranslateY", "trty"),
        ("targetRotateTranslateZ", "trtz"),
    )

    targetRotateTranslateX = DoubleLinearField(default_value=0.0)
    trtx = targetRotateTranslateX

    targetRotateTranslateY = DoubleLinearField(default_value=0.0)
    trty = targetRotateTranslateY

    targetRotateTranslateZ = DoubleLinearField(default_value=0.0)
    trtz = targetRotateTranslateZ


class Target_targetRotateTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[
        Target_targetRotateTranslatePlugOperator
    ]
):
    __slots__ = ()

    targetRotateTranslateX = DoubleLinearField(default_value=0.0)
    trtx = targetRotateTranslateX

    targetRotateTranslateY = DoubleLinearField(default_value=0.0)
    trty = targetRotateTranslateY

    targetRotateTranslateZ = DoubleLinearField(default_value=0.0)
    trtz = targetRotateTranslateZ


class Target_targetRotateTranslateField(
    DoubleLinear3CompoundBaseField[
        Target_targetRotateTranslateAttrOperator,
        Target_targetRotateTranslatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotateTranslateAttrOperator
    PLUG_CLS = Target_targetRotateTranslatePlugOperator

    targetRotateTranslateX = DoubleLinearField(default_value=0.0)
    trtx = targetRotateTranslateX

    targetRotateTranslateY = DoubleLinearField(default_value=0.0)
    trty = targetRotateTranslateY

    targetRotateTranslateZ = DoubleLinearField(default_value=0.0)
    trtz = targetRotateTranslateZ


class Target_targetOffsetTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "Target_targetOffsetTranslateAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetOffsetTranslateX", "totx"),
        ("targetOffsetTranslateY", "toty"),
        ("targetOffsetTranslateZ", "totz"),
    )

    targetOffsetTranslateX = DoubleLinearField(default_value=0.0)
    totx = targetOffsetTranslateX

    targetOffsetTranslateY = DoubleLinearField(default_value=0.0)
    toty = targetOffsetTranslateY

    targetOffsetTranslateZ = DoubleLinearField(default_value=0.0)
    totz = targetOffsetTranslateZ


class Target_targetOffsetTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[
        Target_targetOffsetTranslatePlugOperator
    ]
):
    __slots__ = ()

    targetOffsetTranslateX = DoubleLinearField(default_value=0.0)
    totx = targetOffsetTranslateX

    targetOffsetTranslateY = DoubleLinearField(default_value=0.0)
    toty = targetOffsetTranslateY

    targetOffsetTranslateZ = DoubleLinearField(default_value=0.0)
    totz = targetOffsetTranslateZ


class Target_targetOffsetTranslateField(
    DoubleLinear3CompoundBaseField[
        Target_targetOffsetTranslateAttrOperator,
        Target_targetOffsetTranslatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetOffsetTranslateAttrOperator
    PLUG_CLS = Target_targetOffsetTranslatePlugOperator

    targetOffsetTranslateX = DoubleLinearField(default_value=0.0)
    totx = targetOffsetTranslateX

    targetOffsetTranslateY = DoubleLinearField(default_value=0.0)
    toty = targetOffsetTranslateY

    targetOffsetTranslateZ = DoubleLinearField(default_value=0.0)
    totz = targetOffsetTranslateZ


class Target_targetRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["Target_targetRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotateX", "trx"),
        ("targetRotateY", "try"),
        ("targetRotateZ", "trz"),
    )

    targetRotateX = DoubleAngleField(default_value=0.0)
    trx = targetRotateX

    targetRotateY = DoubleAngleField(default_value=0.0)
    try_ = targetRotateY

    targetRotateZ = DoubleAngleField(default_value=0.0)
    trz = targetRotateZ


class Target_targetRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[Target_targetRotatePlugOperator]
):
    __slots__ = ()

    targetRotateX = DoubleAngleField(default_value=0.0)
    trx = targetRotateX

    targetRotateY = DoubleAngleField(default_value=0.0)
    try_ = targetRotateY

    targetRotateZ = DoubleAngleField(default_value=0.0)
    trz = targetRotateZ


class Target_targetRotateField(
    DoubleAngle3CompoundBaseField[
        Target_targetRotateAttrOperator, Target_targetRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotateAttrOperator
    PLUG_CLS = Target_targetRotatePlugOperator

    targetRotateX = DoubleAngleField(default_value=0.0)
    trx = targetRotateX

    targetRotateY = DoubleAngleField(default_value=0.0)
    try_ = targetRotateY

    targetRotateZ = DoubleAngleField(default_value=0.0)
    trz = targetRotateZ


class Target_targetJointOrientPlugOperator(
    DoubleAngle3CompoundBasePlugOperator[
        "Target_targetJointOrientAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetJointOrientX", "tjox"),
        ("targetJointOrientY", "tjoy"),
        ("targetJointOrientZ", "tjoz"),
    )

    targetJointOrientX = DoubleAngleField(default_value=0.0)
    tjox = targetJointOrientX

    targetJointOrientY = DoubleAngleField(default_value=0.0)
    tjoy = targetJointOrientY

    targetJointOrientZ = DoubleAngleField(default_value=0.0)
    tjoz = targetJointOrientZ


class Target_targetJointOrientAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[Target_targetJointOrientPlugOperator]
):
    __slots__ = ()

    targetJointOrientX = DoubleAngleField(default_value=0.0)
    tjox = targetJointOrientX

    targetJointOrientY = DoubleAngleField(default_value=0.0)
    tjoy = targetJointOrientY

    targetJointOrientZ = DoubleAngleField(default_value=0.0)
    tjoz = targetJointOrientZ


class Target_targetJointOrientField(
    DoubleAngle3CompoundBaseField[
        Target_targetJointOrientAttrOperator,
        Target_targetJointOrientPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetJointOrientAttrOperator
    PLUG_CLS = Target_targetJointOrientPlugOperator

    targetJointOrientX = DoubleAngleField(default_value=0.0)
    tjox = targetJointOrientX

    targetJointOrientY = DoubleAngleField(default_value=0.0)
    tjoy = targetJointOrientY

    targetJointOrientZ = DoubleAngleField(default_value=0.0)
    tjoz = targetJointOrientZ


class Target_targetOffsetRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator[
        "Target_targetOffsetRotateAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetOffsetRotateX", "torx"),
        ("targetOffsetRotateY", "tory"),
        ("targetOffsetRotateZ", "torz"),
    )

    targetOffsetRotateX = DoubleAngleField(default_value=0.0)
    torx = targetOffsetRotateX

    targetOffsetRotateY = DoubleAngleField(default_value=0.0)
    tory = targetOffsetRotateY

    targetOffsetRotateZ = DoubleAngleField(default_value=0.0)
    torz = targetOffsetRotateZ


class Target_targetOffsetRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[Target_targetOffsetRotatePlugOperator]
):
    __slots__ = ()

    targetOffsetRotateX = DoubleAngleField(default_value=0.0)
    torx = targetOffsetRotateX

    targetOffsetRotateY = DoubleAngleField(default_value=0.0)
    tory = targetOffsetRotateY

    targetOffsetRotateZ = DoubleAngleField(default_value=0.0)
    torz = targetOffsetRotateZ


class Target_targetOffsetRotateField(
    DoubleAngle3CompoundBaseField[
        Target_targetOffsetRotateAttrOperator,
        Target_targetOffsetRotatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetOffsetRotateAttrOperator
    PLUG_CLS = Target_targetOffsetRotatePlugOperator

    targetOffsetRotateX = DoubleAngleField(default_value=0.0)
    torx = targetOffsetRotateX

    targetOffsetRotateY = DoubleAngleField(default_value=0.0)
    tory = targetOffsetRotateY

    targetOffsetRotateZ = DoubleAngleField(default_value=0.0)
    torz = targetOffsetRotateZ


class Target_targetInverseScalePlugOperator(
    Double3CompoundBasePlugOperator["Target_targetInverseScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetInverseScaleX", "tisx"),
        ("targetInverseScaleY", "tisy"),
        ("targetInverseScaleZ", "tisz"),
    )

    targetInverseScaleX = DoubleField(default_value=1.0)
    tisx = targetInverseScaleX

    targetInverseScaleY = DoubleField(default_value=1.0)
    tisy = targetInverseScaleY

    targetInverseScaleZ = DoubleField(default_value=1.0)
    tisz = targetInverseScaleZ


class Target_targetInverseScaleAttrOperator(
    Double3CompoundBaseAttrOperator[Target_targetInverseScalePlugOperator]
):
    __slots__ = ()

    targetInverseScaleX = DoubleField(default_value=1.0)
    tisx = targetInverseScaleX

    targetInverseScaleY = DoubleField(default_value=1.0)
    tisy = targetInverseScaleY

    targetInverseScaleZ = DoubleField(default_value=1.0)
    tisz = targetInverseScaleZ


class Target_targetInverseScaleField(
    Double3CompoundBaseField[
        Target_targetInverseScaleAttrOperator,
        Target_targetInverseScalePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetInverseScaleAttrOperator
    PLUG_CLS = Target_targetInverseScalePlugOperator

    targetInverseScaleX = DoubleField(default_value=1.0)
    tisx = targetInverseScaleX

    targetInverseScaleY = DoubleField(default_value=1.0)
    tisy = targetInverseScaleY

    targetInverseScaleZ = DoubleField(default_value=1.0)
    tisz = targetInverseScaleZ


class Target_targetScalePlugOperator(
    Double3CompoundBasePlugOperator["Target_targetScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetScaleX", "tsx"),
        ("targetScaleY", "tsy"),
        ("targetScaleZ", "tsz"),
    )

    targetScaleX = DoubleField(default_value=1.0)
    tsx = targetScaleX

    targetScaleY = DoubleField(default_value=1.0)
    tsy = targetScaleY

    targetScaleZ = DoubleField(default_value=1.0)
    tsz = targetScaleZ


class Target_targetScaleAttrOperator(
    Double3CompoundBaseAttrOperator[Target_targetScalePlugOperator]
):
    __slots__ = ()

    targetScaleX = DoubleField(default_value=1.0)
    tsx = targetScaleX

    targetScaleY = DoubleField(default_value=1.0)
    tsy = targetScaleY

    targetScaleZ = DoubleField(default_value=1.0)
    tsz = targetScaleZ


class Target_targetScaleField(
    Double3CompoundBaseField[
        Target_targetScaleAttrOperator, Target_targetScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetScaleAttrOperator
    PLUG_CLS = Target_targetScalePlugOperator

    targetScaleX = DoubleField(default_value=1.0)
    tsx = targetScaleX

    targetScaleY = DoubleField(default_value=1.0)
    tsy = targetScaleY

    targetScaleZ = DoubleField(default_value=1.0)
    tsz = targetScaleZ


class TargetPlugOperator(CompoundPlugOperator["TargetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetParentMatrix", "tpm"),
        ("targetWeight", "tw"),
        ("targetRotateCached", "ctr"),
        ("targetTranslate", "tt"),
        ("targetRotatePivot", "trp"),
        ("targetRotateTranslate", "trt"),
        ("targetOffsetTranslate", "tot"),
        ("targetRotate", "tr"),
        ("targetRotateOrder", "tro"),
        ("targetJointOrient", "tjo"),
        ("targetOffsetRotate", "tor"),
        ("targetScaleCompensate", "tsc"),
        ("targetInverseScale", "tis"),
        ("targetScale", "ts"),
    )

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight

    targetRotateCached = Target_targetRotateCachedField(
        default_value=(0.0, 0.0, 0.0)
    )
    ctr = targetRotateCached

    targetTranslate = Target_targetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tt = targetTranslate

    targetRotatePivot = Target_targetRotatePivotField(
        default_value=(0.0, 0.0, 0.0)
    )
    trp = targetRotatePivot

    targetRotateTranslate = Target_targetRotateTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    trt = targetRotateTranslate

    targetOffsetTranslate = Target_targetOffsetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tot = targetOffsetTranslate

    targetRotate = Target_targetRotateField(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetRotateOrder = Target_targetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrient = Target_targetJointOrientField(
        default_value=(0.0, 0.0, 0.0)
    )
    tjo = targetJointOrient

    targetOffsetRotate = Target_targetOffsetRotateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tor = targetOffsetRotate

    targetScaleCompensate = BoolField(default_value=True)
    tsc = targetScaleCompensate

    targetInverseScale = Target_targetInverseScaleField(
        default_value=(1.0, 1.0, 1.0)
    )
    tis = targetInverseScale

    targetScale = Target_targetScaleField(default_value=(1.0, 1.0, 1.0))
    ts = targetScale


class TargetAttrOperator(CompoundAttrOperator[TargetPlugOperator]):
    __slots__ = ()

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight

    targetRotateCached = Target_targetRotateCachedField(
        default_value=(0.0, 0.0, 0.0)
    )
    ctr = targetRotateCached

    targetTranslate = Target_targetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tt = targetTranslate

    targetRotatePivot = Target_targetRotatePivotField(
        default_value=(0.0, 0.0, 0.0)
    )
    trp = targetRotatePivot

    targetRotateTranslate = Target_targetRotateTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    trt = targetRotateTranslate

    targetOffsetTranslate = Target_targetOffsetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tot = targetOffsetTranslate

    targetRotate = Target_targetRotateField(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetRotateOrder = Target_targetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrient = Target_targetJointOrientField(
        default_value=(0.0, 0.0, 0.0)
    )
    tjo = targetJointOrient

    targetOffsetRotate = Target_targetOffsetRotateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tor = targetOffsetRotate

    targetScaleCompensate = BoolField(default_value=True)
    tsc = targetScaleCompensate

    targetInverseScale = Target_targetInverseScaleField(
        default_value=(1.0, 1.0, 1.0)
    )
    tis = targetInverseScale

    targetScale = Target_targetScaleField(default_value=(1.0, 1.0, 1.0))
    ts = targetScale


class TargetField(CompoundField[TargetAttrOperator, TargetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator


class LastTargetRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["LastTargetRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lastTargetRotateX", "lrx"),
        ("lastTargetRotateY", "lry"),
        ("lastTargetRotateZ", "lrz"),
    )

    lastTargetRotateX = DoubleAngleField(default_value=0.0)
    lrx = lastTargetRotateX

    lastTargetRotateY = DoubleAngleField(default_value=0.0)
    lry = lastTargetRotateY

    lastTargetRotateZ = DoubleAngleField(default_value=0.0)
    lrz = lastTargetRotateZ


class LastTargetRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[LastTargetRotatePlugOperator]
):
    __slots__ = ()

    lastTargetRotateX = DoubleAngleField(default_value=0.0)
    lrx = lastTargetRotateX

    lastTargetRotateY = DoubleAngleField(default_value=0.0)
    lry = lastTargetRotateY

    lastTargetRotateZ = DoubleAngleField(default_value=0.0)
    lrz = lastTargetRotateZ


class LastTargetRotateField(
    DoubleAngle3CompoundBaseField[
        LastTargetRotateAttrOperator, LastTargetRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LastTargetRotateAttrOperator
    PLUG_CLS = LastTargetRotatePlugOperator

    lastTargetRotateX = DoubleAngleField(default_value=0.0)
    lrx = lastTargetRotateX

    lastTargetRotateY = DoubleAngleField(default_value=0.0)
    lry = lastTargetRotateY

    lastTargetRotateZ = DoubleAngleField(default_value=0.0)
    lrz = lastTargetRotateZ


class ConstraintRotatePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintRotatePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotatePivotX", "crpx"),
        ("constraintRotatePivotY", "crpy"),
        ("constraintRotatePivotZ", "crpz"),
    )

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintRotatePivotPlugOperator]
):
    __slots__ = ()

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotatePivotField(
    DoubleLinear3CompoundBaseField[
        ConstraintRotatePivotAttrOperator, ConstraintRotatePivotPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotatePivotAttrOperator
    PLUG_CLS = ConstraintRotatePivotPlugOperator

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotateTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "ConstraintRotateTranslateAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotateTranslateX", "crtx"),
        ("constraintRotateTranslateY", "crty"),
        ("constraintRotateTranslateZ", "crtz"),
    )

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintRotateTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[
        ConstraintRotateTranslatePlugOperator
    ]
):
    __slots__ = ()

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintRotateTranslateField(
    DoubleLinear3CompoundBaseField[
        ConstraintRotateTranslateAttrOperator,
        ConstraintRotateTranslatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateTranslateAttrOperator
    PLUG_CLS = ConstraintRotateTranslatePlugOperator

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintTranslateX", "ctx"),
        ("constraintTranslateY", "cty"),
        ("constraintTranslateZ", "ctz"),
    )

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class ConstraintTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintTranslatePlugOperator]
):
    __slots__ = ()

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class ConstraintTranslateField(
    DoubleLinear3CompoundBaseField[
        ConstraintTranslateAttrOperator, ConstraintTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintTranslateAttrOperator
    PLUG_CLS = ConstraintTranslatePlugOperator

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class RestTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["RestTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("restTranslateX", "rtx"),
        ("restTranslateY", "rty"),
        ("restTranslateZ", "rtz"),
    )

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


class RestTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[RestTranslatePlugOperator]
):
    __slots__ = ()

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


class RestTranslateField(
    DoubleLinear3CompoundBaseField[
        RestTranslateAttrOperator, RestTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RestTranslateAttrOperator
    PLUG_CLS = RestTranslatePlugOperator

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


class ConstraintJointOrientPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["ConstraintJointOrientAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintJointOrientX", "cjox"),
        ("constraintJointOrientY", "cjoy"),
        ("constraintJointOrientZ", "cjoz"),
    )

    constraintJointOrientX = DoubleAngleField(default_value=0.0)
    cjox = constraintJointOrientX

    constraintJointOrientY = DoubleAngleField(default_value=0.0)
    cjoy = constraintJointOrientY

    constraintJointOrientZ = DoubleAngleField(default_value=0.0)
    cjoz = constraintJointOrientZ


class ConstraintJointOrientAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[ConstraintJointOrientPlugOperator]
):
    __slots__ = ()

    constraintJointOrientX = DoubleAngleField(default_value=0.0)
    cjox = constraintJointOrientX

    constraintJointOrientY = DoubleAngleField(default_value=0.0)
    cjoy = constraintJointOrientY

    constraintJointOrientZ = DoubleAngleField(default_value=0.0)
    cjoz = constraintJointOrientZ


class ConstraintJointOrientField(
    DoubleAngle3CompoundBaseField[
        ConstraintJointOrientAttrOperator, ConstraintJointOrientPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintJointOrientAttrOperator
    PLUG_CLS = ConstraintJointOrientPlugOperator

    constraintJointOrientX = DoubleAngleField(default_value=0.0)
    cjox = constraintJointOrientX

    constraintJointOrientY = DoubleAngleField(default_value=0.0)
    cjoy = constraintJointOrientY

    constraintJointOrientZ = DoubleAngleField(default_value=0.0)
    cjoz = constraintJointOrientZ


class ConstraintRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["ConstraintRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotateX", "crx"),
        ("constraintRotateY", "cry"),
        ("constraintRotateZ", "crz"),
    )

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ


class ConstraintRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[ConstraintRotatePlugOperator]
):
    __slots__ = ()

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ


class ConstraintRotateField(
    DoubleAngle3CompoundBaseField[
        ConstraintRotateAttrOperator, ConstraintRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateAttrOperator
    PLUG_CLS = ConstraintRotatePlugOperator

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ


class RestRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RestRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("restRotateX", "rrx"),
        ("restRotateY", "rry"),
        ("restRotateZ", "rrz"),
    )

    restRotateX = DoubleAngleField(default_value=0.0)
    rrx = restRotateX

    restRotateY = DoubleAngleField(default_value=0.0)
    rry = restRotateY

    restRotateZ = DoubleAngleField(default_value=0.0)
    rrz = restRotateZ


class RestRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RestRotatePlugOperator]
):
    __slots__ = ()

    restRotateX = DoubleAngleField(default_value=0.0)
    rrx = restRotateX

    restRotateY = DoubleAngleField(default_value=0.0)
    rry = restRotateY

    restRotateZ = DoubleAngleField(default_value=0.0)
    rrz = restRotateZ


class RestRotateField(
    DoubleAngle3CompoundBaseField[
        RestRotateAttrOperator, RestRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RestRotateAttrOperator
    PLUG_CLS = RestRotatePlugOperator

    restRotateX = DoubleAngleField(default_value=0.0)
    rrx = restRotateX

    restRotateY = DoubleAngleField(default_value=0.0)
    rry = restRotateY

    restRotateZ = DoubleAngleField(default_value=0.0)
    rrz = restRotateZ


class RotationDecompositionTargetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "RotationDecompositionTargetAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationDecompositionTargetX", "rdtx"),
        ("rotationDecompositionTargetY", "rdty"),
        ("rotationDecompositionTargetZ", "rdtz"),
    )

    rotationDecompositionTargetX = DoubleLinearField(default_value=0.0)
    rdtx = rotationDecompositionTargetX

    rotationDecompositionTargetY = DoubleLinearField(default_value=0.0)
    rdty = rotationDecompositionTargetY

    rotationDecompositionTargetZ = DoubleLinearField(default_value=0.0)
    rdtz = rotationDecompositionTargetZ


class RotationDecompositionTargetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[
        RotationDecompositionTargetPlugOperator
    ]
):
    __slots__ = ()

    rotationDecompositionTargetX = DoubleLinearField(default_value=0.0)
    rdtx = rotationDecompositionTargetX

    rotationDecompositionTargetY = DoubleLinearField(default_value=0.0)
    rdty = rotationDecompositionTargetY

    rotationDecompositionTargetZ = DoubleLinearField(default_value=0.0)
    rdtz = rotationDecompositionTargetZ


class RotationDecompositionTargetField(
    DoubleLinear3CompoundBaseField[
        RotationDecompositionTargetAttrOperator,
        RotationDecompositionTargetPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = RotationDecompositionTargetAttrOperator
    PLUG_CLS = RotationDecompositionTargetPlugOperator

    rotationDecompositionTargetX = DoubleLinearField(default_value=0.0)
    rdtx = rotationDecompositionTargetX

    rotationDecompositionTargetY = DoubleLinearField(default_value=0.0)
    rdty = rotationDecompositionTargetY

    rotationDecompositionTargetZ = DoubleLinearField(default_value=0.0)
    rdtz = rotationDecompositionTargetZ
