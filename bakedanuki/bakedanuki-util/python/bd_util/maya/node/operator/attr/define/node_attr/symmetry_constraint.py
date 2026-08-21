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
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.dt.matrix import DataMatrixField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
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


class Target_targetJointOrientTypeEnumPlugOperator(
    EnumPlugOperator["Target_targetJointOrientTypeEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Target_targetJointOrientTypeEnumAttrOperator(
    EnumAttrOperator[Target_targetJointOrientTypeEnumPlugOperator]
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


class Target_targetJointOrientTypeEnumField(
    EnumField[
        Target_targetJointOrientTypeEnumAttrOperator,
        Target_targetJointOrientTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetJointOrientTypeEnumAttrOperator
    PLUG_CLS = Target_targetJointOrientTypeEnumPlugOperator


class Constrained_constraintRotateOrderEnumPlugOperator(
    EnumPlugOperator["Constrained_constraintRotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Constrained_constraintRotateOrderEnumAttrOperator(
    EnumAttrOperator[Constrained_constraintRotateOrderEnumPlugOperator]
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


class Constrained_constraintRotateOrderEnumField(
    EnumField[
        Constrained_constraintRotateOrderEnumAttrOperator,
        Constrained_constraintRotateOrderEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Constrained_constraintRotateOrderEnumAttrOperator
    PLUG_CLS = Constrained_constraintRotateOrderEnumPlugOperator


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


class Target_targetScalePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Target_targetScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetScaleX", "tsx"),
        ("targetScaleY", "tsy"),
        ("targetScaleZ", "tsz"),
    )

    targetScaleX = DoubleLinearField(default_value=0.0)
    tsx = targetScaleX

    targetScaleY = DoubleLinearField(default_value=0.0)
    tsy = targetScaleY

    targetScaleZ = DoubleLinearField(default_value=0.0)
    tsz = targetScaleZ


class Target_targetScaleAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Target_targetScalePlugOperator]
):
    __slots__ = ()

    targetScaleX = DoubleLinearField(default_value=0.0)
    tsx = targetScaleX

    targetScaleY = DoubleLinearField(default_value=0.0)
    tsy = targetScaleY

    targetScaleZ = DoubleLinearField(default_value=0.0)
    tsz = targetScaleZ


class Target_targetScaleField(
    DoubleLinear3CompoundBaseField[
        Target_targetScaleAttrOperator, Target_targetScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetScaleAttrOperator
    PLUG_CLS = Target_targetScalePlugOperator

    targetScaleX = DoubleLinearField(default_value=0.0)
    tsx = targetScaleX

    targetScaleY = DoubleLinearField(default_value=0.0)
    tsy = targetScaleY

    targetScaleZ = DoubleLinearField(default_value=0.0)
    tsz = targetScaleZ


class Target_targetJointOrientPlugOperator(
    DoubleAngle3CompoundBasePlugOperator[
        "Target_targetJointOrientAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetJointOrientX", "tjx"),
        ("targetJointOrientY", "tjy"),
        ("targetJointOrientZ", "tjz"),
    )

    targetJointOrientX = DoubleAngleField(default_value=0.0)
    tjx = targetJointOrientX

    targetJointOrientY = DoubleAngleField(default_value=0.0)
    tjy = targetJointOrientY

    targetJointOrientZ = DoubleAngleField(default_value=0.0)
    tjz = targetJointOrientZ


class Target_targetJointOrientAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[Target_targetJointOrientPlugOperator]
):
    __slots__ = ()

    targetJointOrientX = DoubleAngleField(default_value=0.0)
    tjx = targetJointOrientX

    targetJointOrientY = DoubleAngleField(default_value=0.0)
    tjy = targetJointOrientY

    targetJointOrientZ = DoubleAngleField(default_value=0.0)
    tjz = targetJointOrientZ


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
    tjx = targetJointOrientX

    targetJointOrientY = DoubleAngleField(default_value=0.0)
    tjy = targetJointOrientY

    targetJointOrientZ = DoubleAngleField(default_value=0.0)
    tjz = targetJointOrientZ


class Target_targetChildTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "Target_targetChildTranslateAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetChildTranslateX", "tcx"),
        ("targetChildTranslateY", "tcy"),
        ("targetChildTranslateZ", "tcz"),
    )

    targetChildTranslateX = DoubleLinearField(default_value=0.0)
    tcx = targetChildTranslateX

    targetChildTranslateY = DoubleLinearField(default_value=0.0)
    tcy = targetChildTranslateY

    targetChildTranslateZ = DoubleLinearField(default_value=0.0)
    tcz = targetChildTranslateZ


class Target_targetChildTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[
        Target_targetChildTranslatePlugOperator
    ]
):
    __slots__ = ()

    targetChildTranslateX = DoubleLinearField(default_value=0.0)
    tcx = targetChildTranslateX

    targetChildTranslateY = DoubleLinearField(default_value=0.0)
    tcy = targetChildTranslateY

    targetChildTranslateZ = DoubleLinearField(default_value=0.0)
    tcz = targetChildTranslateZ


class Target_targetChildTranslateField(
    DoubleLinear3CompoundBaseField[
        Target_targetChildTranslateAttrOperator,
        Target_targetChildTranslatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetChildTranslateAttrOperator
    PLUG_CLS = Target_targetChildTranslatePlugOperator

    targetChildTranslateX = DoubleLinearField(default_value=0.0)
    tcx = targetChildTranslateX

    targetChildTranslateY = DoubleLinearField(default_value=0.0)
    tcy = targetChildTranslateY

    targetChildTranslateZ = DoubleLinearField(default_value=0.0)
    tcz = targetChildTranslateZ


class Constrained_constraintTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "Constrained_constraintTranslateAttrOperator"
    ]
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


class Constrained_constraintTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[
        Constrained_constraintTranslatePlugOperator
    ]
):
    __slots__ = ()

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class Constrained_constraintTranslateField(
    DoubleLinear3CompoundBaseField[
        Constrained_constraintTranslateAttrOperator,
        Constrained_constraintTranslatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Constrained_constraintTranslateAttrOperator
    PLUG_CLS = Constrained_constraintTranslatePlugOperator

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class Constrained_constraintJointOrientPlugOperator(
    DoubleAngle3CompoundBasePlugOperator[
        "Constrained_constraintJointOrientAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintJointOrientX", "cjx"),
        ("constraintJointOrientY", "cjy"),
        ("constraintJointOrientZ", "cjz"),
    )

    constraintJointOrientX = DoubleAngleField(
        default_value=0.0, writable=False
    )
    cjx = constraintJointOrientX

    constraintJointOrientY = DoubleAngleField(
        default_value=0.0, writable=False
    )
    cjy = constraintJointOrientY

    constraintJointOrientZ = DoubleAngleField(
        default_value=0.0, writable=False
    )
    cjz = constraintJointOrientZ


class Constrained_constraintJointOrientAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[
        Constrained_constraintJointOrientPlugOperator
    ]
):
    __slots__ = ()

    constraintJointOrientX = DoubleAngleField(
        default_value=0.0, writable=False
    )
    cjx = constraintJointOrientX

    constraintJointOrientY = DoubleAngleField(
        default_value=0.0, writable=False
    )
    cjy = constraintJointOrientY

    constraintJointOrientZ = DoubleAngleField(
        default_value=0.0, writable=False
    )
    cjz = constraintJointOrientZ


class Constrained_constraintJointOrientField(
    DoubleAngle3CompoundBaseField[
        Constrained_constraintJointOrientAttrOperator,
        Constrained_constraintJointOrientPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Constrained_constraintJointOrientAttrOperator
    PLUG_CLS = Constrained_constraintJointOrientPlugOperator

    constraintJointOrientX = DoubleAngleField(
        default_value=0.0, writable=False
    )
    cjx = constraintJointOrientX

    constraintJointOrientY = DoubleAngleField(
        default_value=0.0, writable=False
    )
    cjy = constraintJointOrientY

    constraintJointOrientZ = DoubleAngleField(
        default_value=0.0, writable=False
    )
    cjz = constraintJointOrientZ


class Constrained_constraintRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator[
        "Constrained_constraintRotateAttrOperator"
    ]
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


class Constrained_constraintRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[
        Constrained_constraintRotatePlugOperator
    ]
):
    __slots__ = ()

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ


class Constrained_constraintRotateField(
    DoubleAngle3CompoundBaseField[
        Constrained_constraintRotateAttrOperator,
        Constrained_constraintRotatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Constrained_constraintRotateAttrOperator
    PLUG_CLS = Constrained_constraintRotatePlugOperator

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ


class Constrained_constraintScalePlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "Constrained_constraintScaleAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintScaleX", "csx"),
        ("constraintScaleY", "csy"),
        ("constraintScaleZ", "csz"),
    )

    constraintScaleX = DoubleLinearField(default_value=0.0, writable=False)
    csx = constraintScaleX

    constraintScaleY = DoubleLinearField(default_value=0.0, writable=False)
    csy = constraintScaleY

    constraintScaleZ = DoubleLinearField(default_value=0.0, writable=False)
    csz = constraintScaleZ


class Constrained_constraintScaleAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[
        Constrained_constraintScalePlugOperator
    ]
):
    __slots__ = ()

    constraintScaleX = DoubleLinearField(default_value=0.0, writable=False)
    csx = constraintScaleX

    constraintScaleY = DoubleLinearField(default_value=0.0, writable=False)
    csy = constraintScaleY

    constraintScaleZ = DoubleLinearField(default_value=0.0, writable=False)
    csz = constraintScaleZ


class Constrained_constraintScaleField(
    DoubleLinear3CompoundBaseField[
        Constrained_constraintScaleAttrOperator,
        Constrained_constraintScalePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Constrained_constraintScaleAttrOperator
    PLUG_CLS = Constrained_constraintScalePlugOperator

    constraintScaleX = DoubleLinearField(default_value=0.0, writable=False)
    csx = constraintScaleX

    constraintScaleY = DoubleLinearField(default_value=0.0, writable=False)
    csy = constraintScaleY

    constraintScaleZ = DoubleLinearField(default_value=0.0, writable=False)
    csz = constraintScaleZ


class TargetPlugOperator(CompoundPlugOperator["TargetAttrOperator"]):
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

    targetTranslate = Target_targetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tt = targetTranslate

    targetRotate = Target_targetRotateField(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetScale = Target_targetScaleField(default_value=(0.0, 0.0, 0.0))
    ts = targetScale

    targetRotateOrder = Target_targetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrientType = Target_targetJointOrientTypeEnumField(
        default_value=0
    )
    tjt = targetJointOrientType

    targetJointOrient = Target_targetJointOrientField(
        default_value=(0.0, 0.0, 0.0)
    )
    tjo = targetJointOrient

    targetChildTranslate = Target_targetChildTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tct = targetChildTranslate

    targetWorldMatrix = DataMatrixField()
    twm = targetWorldMatrix

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix


class TargetAttrOperator(CompoundAttrOperator[TargetPlugOperator]):
    __slots__ = ()

    targetTranslate = Target_targetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tt = targetTranslate

    targetRotate = Target_targetRotateField(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetScale = Target_targetScaleField(default_value=(0.0, 0.0, 0.0))
    ts = targetScale

    targetRotateOrder = Target_targetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrientType = Target_targetJointOrientTypeEnumField(
        default_value=0
    )
    tjt = targetJointOrientType

    targetJointOrient = Target_targetJointOrientField(
        default_value=(0.0, 0.0, 0.0)
    )
    tjo = targetJointOrient

    targetChildTranslate = Target_targetChildTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tct = targetChildTranslate

    targetWorldMatrix = DataMatrixField()
    twm = targetWorldMatrix

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix


class TargetField(CompoundField[TargetAttrOperator, TargetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator

    targetTranslate = Target_targetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tt = targetTranslate

    targetRotate = Target_targetRotateField(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetScale = Target_targetScaleField(default_value=(0.0, 0.0, 0.0))
    ts = targetScale

    targetRotateOrder = Target_targetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrientType = Target_targetJointOrientTypeEnumField(
        default_value=0
    )
    tjt = targetJointOrientType

    targetJointOrient = Target_targetJointOrientField(
        default_value=(0.0, 0.0, 0.0)
    )
    tjo = targetJointOrient

    targetChildTranslate = Target_targetChildTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
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
    DoubleLinear3CompoundBaseField[
        SymmetryRootOffsetAttrOperator, SymmetryRootOffsetPlugOperator
    ]
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
    DoubleLinear3CompoundBaseField[
        SymmetryMiddlePointAttrOperator, SymmetryMiddlePointPlugOperator
    ]
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


class ConstrainedPlugOperator(CompoundPlugOperator["ConstrainedAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintTranslate", "ct"),
        ("constraintRotateOrder", "cro"),
        ("constraintJointOrient", "cjo"),
        ("constraintRotate", "cr"),
        ("constraintScale", "cs"),
    )

    constraintTranslate = Constrained_constraintTranslateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ct = constraintTranslate

    constraintRotateOrder = Constrained_constraintRotateOrderEnumField(
        default_value=0, writable=False
    )
    cro = constraintRotateOrder

    constraintJointOrient = Constrained_constraintJointOrientField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cjo = constraintJointOrient

    constraintRotate = Constrained_constraintRotateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cr = constraintRotate

    constraintScale = Constrained_constraintScaleField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cs = constraintScale


class ConstrainedAttrOperator(CompoundAttrOperator[ConstrainedPlugOperator]):
    __slots__ = ()

    constraintTranslate = Constrained_constraintTranslateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ct = constraintTranslate

    constraintRotateOrder = Constrained_constraintRotateOrderEnumField(
        default_value=0, writable=False
    )
    cro = constraintRotateOrder

    constraintJointOrient = Constrained_constraintJointOrientField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cjo = constraintJointOrient

    constraintRotate = Constrained_constraintRotateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cr = constraintRotate

    constraintScale = Constrained_constraintScaleField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cs = constraintScale


class ConstrainedField(
    CompoundField[ConstrainedAttrOperator, ConstrainedPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstrainedAttrOperator
    PLUG_CLS = ConstrainedPlugOperator

    constraintTranslate = Constrained_constraintTranslateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ct = constraintTranslate

    constraintRotateOrder = Constrained_constraintRotateOrderEnumField(
        default_value=0, writable=False
    )
    cro = constraintRotateOrder

    constraintJointOrient = Constrained_constraintJointOrientField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cjo = constraintJointOrient

    constraintRotate = Constrained_constraintRotateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cr = constraintRotate

    constraintScale = Constrained_constraintScaleField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cs = constraintScale
