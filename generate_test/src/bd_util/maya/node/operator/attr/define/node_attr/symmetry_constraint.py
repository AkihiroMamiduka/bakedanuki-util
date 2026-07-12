# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.matrix import DataMatrixField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class TargetRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class TargetRotateOrderEnumAttrOperator(EnumAttrOperator):
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


class TargetRotateOrderEnumField(
    EnumField[TargetRotateOrderEnumAttrOperator, TargetRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetRotateOrderEnumAttrOperator
    PLUG_CLS = TargetRotateOrderEnumPlugOperator


class TargetJointOrientTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class TargetJointOrientTypeEnumAttrOperator(EnumAttrOperator):
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


class TargetJointOrientTypeEnumField(
    EnumField[TargetJointOrientTypeEnumAttrOperator, TargetJointOrientTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetJointOrientTypeEnumAttrOperator
    PLUG_CLS = TargetJointOrientTypeEnumPlugOperator


class ConstraintRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class ConstraintRotateOrderEnumAttrOperator(EnumAttrOperator):
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


class ConstraintRotateOrderEnumField(
    EnumField[ConstraintRotateOrderEnumAttrOperator, ConstraintRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateOrderEnumAttrOperator
    PLUG_CLS = ConstraintRotateOrderEnumPlugOperator


class TargetPlugOperator(
    CompoundPlugOperator["TargetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetTranslate", "tt"),
        ("targetRotate", "tr"),
        ("targetScale", "ts"),
        ("targetRotateOrder", "tro"),
        ("targetJointOrientType", "tjt"),
        ("targetJointOrient", "tjo"),
        ("targetChildTranslate", "tct"),
        ("targetWorldMatrix", "twm"),
        ("targetParentMatrix", "tpm"),
    )

    targetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tt = targetTranslate

    targetRotate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetScale = Double3Field(default_value=(0.0, 0.0, 0.0))
    ts = targetScale

    targetRotateOrder = TargetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrientType = TargetJointOrientTypeEnumField(default_value=0)
    tjt = targetJointOrientType

    targetJointOrient = Double3Field(default_value=(0.0, 0.0, 0.0))
    tjo = targetJointOrient

    targetChildTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tct = targetChildTranslate

    targetWorldMatrix = DataMatrixField()
    twm = targetWorldMatrix

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    targetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tt = targetTranslate

    targetRotate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetScale = Double3Field(default_value=(0.0, 0.0, 0.0))
    ts = targetScale

    targetRotateOrder = TargetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrientType = TargetJointOrientTypeEnumField(default_value=0)
    tjt = targetJointOrientType

    targetJointOrient = Double3Field(default_value=(0.0, 0.0, 0.0))
    tjo = targetJointOrient

    targetChildTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tct = targetChildTranslate

    targetWorldMatrix = DataMatrixField()
    twm = targetWorldMatrix

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix


class TargetField(
    CompoundField[TargetAttrOperator, TargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator

    targetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tt = targetTranslate

    targetRotate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetScale = Double3Field(default_value=(0.0, 0.0, 0.0))
    ts = targetScale

    targetRotateOrder = TargetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrientType = TargetJointOrientTypeEnumField(default_value=0)
    tjt = targetJointOrientType

    targetJointOrient = Double3Field(default_value=(0.0, 0.0, 0.0))
    tjo = targetJointOrient

    targetChildTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tct = targetChildTranslate

    targetWorldMatrix = DataMatrixField()
    twm = targetWorldMatrix

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix


class SymmetryRootOffsetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["SymmetryRootOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("symmetryRootOffsetX", "srox"),
        ("symmetryRootOffsetY", "sroy"),
        ("symmetryRootOffsetZ", "sroz"),
    )

    symmetryRootOffsetX = DoubleLinearField(default_value=0.0)
    srox = symmetryRootOffsetX

    symmetryRootOffsetY = DoubleLinearField(default_value=0.0)
    sroy = symmetryRootOffsetY

    symmetryRootOffsetZ = DoubleLinearField(default_value=0.0)
    sroz = symmetryRootOffsetZ


class SymmetryRootOffsetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[SymmetryRootOffsetPlugOperator]
):
    __slots__ = ()

    symmetryRootOffsetX = DoubleLinearField(default_value=0.0)
    srox = symmetryRootOffsetX

    symmetryRootOffsetY = DoubleLinearField(default_value=0.0)
    sroy = symmetryRootOffsetY

    symmetryRootOffsetZ = DoubleLinearField(default_value=0.0)
    sroz = symmetryRootOffsetZ


class SymmetryRootOffsetField(
    DoubleLinear3CompoundBaseField[SymmetryRootOffsetAttrOperator, SymmetryRootOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SymmetryRootOffsetAttrOperator
    PLUG_CLS = SymmetryRootOffsetPlugOperator

    symmetryRootOffsetX = DoubleLinearField(default_value=0.0)
    srox = symmetryRootOffsetX

    symmetryRootOffsetY = DoubleLinearField(default_value=0.0)
    sroy = symmetryRootOffsetY

    symmetryRootOffsetZ = DoubleLinearField(default_value=0.0)
    sroz = symmetryRootOffsetZ


class SymmetryMiddlePointPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["SymmetryMiddlePointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("symmetryMiddlePointX", "cmpx"),
        ("symmetryMiddlePointY", "cmpy"),
        ("symmetryMiddlePointZ", "cmpz"),
    )

    symmetryMiddlePointX = DoubleLinearField(default_value=0.0, writable=False)
    cmpx = symmetryMiddlePointX

    symmetryMiddlePointY = DoubleLinearField(default_value=0.0, writable=False)
    cmpy = symmetryMiddlePointY

    symmetryMiddlePointZ = DoubleLinearField(default_value=0.0, writable=False)
    cmpz = symmetryMiddlePointZ


class SymmetryMiddlePointAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[SymmetryMiddlePointPlugOperator]
):
    __slots__ = ()

    symmetryMiddlePointX = DoubleLinearField(default_value=0.0, writable=False)
    cmpx = symmetryMiddlePointX

    symmetryMiddlePointY = DoubleLinearField(default_value=0.0, writable=False)
    cmpy = symmetryMiddlePointY

    symmetryMiddlePointZ = DoubleLinearField(default_value=0.0, writable=False)
    cmpz = symmetryMiddlePointZ


class SymmetryMiddlePointField(
    DoubleLinear3CompoundBaseField[SymmetryMiddlePointAttrOperator, SymmetryMiddlePointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SymmetryMiddlePointAttrOperator
    PLUG_CLS = SymmetryMiddlePointPlugOperator

    symmetryMiddlePointX = DoubleLinearField(default_value=0.0, writable=False)
    cmpx = symmetryMiddlePointX

    symmetryMiddlePointY = DoubleLinearField(default_value=0.0, writable=False)
    cmpy = symmetryMiddlePointY

    symmetryMiddlePointZ = DoubleLinearField(default_value=0.0, writable=False)
    cmpz = symmetryMiddlePointZ


class ConstrainedPlugOperator(
    CompoundPlugOperator["ConstrainedAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintTranslate", "ct"),
        ("constraintRotateOrder", "cro"),
        ("constraintJointOrient", "cjo"),
        ("constraintRotate", "cr"),
        ("constraintScale", "cs"),
    )

    constraintTranslate = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    ct = constraintTranslate

    constraintRotateOrder = ConstraintRotateOrderEnumField(default_value=0, writable=False)
    cro = constraintRotateOrder

    constraintJointOrient = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cjo = constraintJointOrient

    constraintRotate = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cr = constraintRotate

    constraintScale = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cs = constraintScale


class ConstrainedAttrOperator(
    CompoundAttrOperator[ConstrainedPlugOperator]
):
    __slots__ = ()

    constraintTranslate = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    ct = constraintTranslate

    constraintRotateOrder = ConstraintRotateOrderEnumField(default_value=0, writable=False)
    cro = constraintRotateOrder

    constraintJointOrient = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cjo = constraintJointOrient

    constraintRotate = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cr = constraintRotate

    constraintScale = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cs = constraintScale


class ConstrainedField(
    CompoundField[ConstrainedAttrOperator, ConstrainedPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstrainedAttrOperator
    PLUG_CLS = ConstrainedPlugOperator

    constraintTranslate = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    ct = constraintTranslate

    constraintRotateOrder = ConstraintRotateOrderEnumField(default_value=0, writable=False)
    cro = constraintRotateOrder

    constraintJointOrient = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cjo = constraintJointOrient

    constraintRotate = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cr = constraintRotate

    constraintScale = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    cs = constraintScale
