# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.character_offset import (
    InRootRotateField,
    InRootTranslateField,
    InitialOffsetRootTranslateField,
    OffsetRootRotateField,
    OffsetRootRotatePivotField,
    OffsetRootTranslateField,
    OutRootRotateField,
    OutRootTranslateField,
    RootJointOrientField,
    RotateControlScaleField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.matrix import DataMatrixField


class RootRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RootRotateOrderEnumAttrOperator(EnumAttrOperator):
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


class RootRotateOrderEnumField(
    EnumField[RootRotateOrderEnumAttrOperator, RootRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RootRotateOrderEnumAttrOperator
    PLUG_CLS = RootRotateOrderEnumPlugOperator


class OffsetRootRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class OffsetRootRotateOrderEnumAttrOperator(EnumAttrOperator):
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


class OffsetRootRotateOrderEnumField(
    EnumField[OffsetRootRotateOrderEnumAttrOperator, OffsetRootRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetRootRotateOrderEnumAttrOperator
    PLUG_CLS = OffsetRootRotateOrderEnumPlugOperator


class CharacterOffset(DG):
    __slots__ = ()

    NODE_TYPE = "characterOffset"

    inRootTranslate = InRootTranslateField()
    rti = inRootTranslate
    inRootTranslateX = inRootTranslate.inRootTranslateX
    rtix = inRootTranslateX
    inRootTranslateY = inRootTranslate.inRootTranslateY
    rtiy = inRootTranslateY
    inRootTranslateZ = inRootTranslate.inRootTranslateZ
    rtiz = inRootTranslateZ

    inRootRotate = InRootRotateField()
    rri = inRootRotate
    inRootRotateX = inRootRotate.inRootRotateX
    rrix = inRootRotateX
    inRootRotateY = inRootRotate.inRootRotateY
    rriy = inRootRotateY
    inRootRotateZ = inRootRotate.inRootRotateZ
    rriz = inRootRotateZ

    rootRotateOrder = RootRotateOrderEnumField()
    rror = rootRotateOrder

    rootJointOrient = RootJointOrientField()
    rjo = rootJointOrient
    rootJointOrientX = rootJointOrient.rootJointOrientX
    rjox = rootJointOrientX
    rootJointOrientY = rootJointOrient.rootJointOrientY
    rjoy = rootJointOrientY
    rootJointOrientZ = rootJointOrient.rootJointOrientZ
    rjoz = rootJointOrientZ

    rootParentMatrix = DataMatrixField()
    rpm = rootParentMatrix

    rootParentInverseMatrix = DataMatrixField()
    rpim = rootParentInverseMatrix

    applyControlParentTransform = BoolField()
    acpx = applyControlParentTransform

    enable = BoolField()
    nabl = enable

    offsetRootTranslate = OffsetRootTranslateField()
    rtf = offsetRootTranslate
    offsetRootTranslateX = offsetRootTranslate.offsetRootTranslateX
    rtfx = offsetRootTranslateX
    offsetRootTranslateY = offsetRootTranslate.offsetRootTranslateY
    rtfy = offsetRootTranslateY
    offsetRootTranslateZ = offsetRootTranslate.offsetRootTranslateZ
    rtfz = offsetRootTranslateZ

    initialOffsetRootTranslate = InitialOffsetRootTranslateField()
    itf = initialOffsetRootTranslate
    initialOffsetRootTranslateX = initialOffsetRootTranslate.initialOffsetRootTranslateX
    itfx = initialOffsetRootTranslateX
    initialOffsetRootTranslateY = initialOffsetRootTranslate.initialOffsetRootTranslateY
    itfy = initialOffsetRootTranslateY
    initialOffsetRootTranslateZ = initialOffsetRootTranslate.initialOffsetRootTranslateZ
    itfz = initialOffsetRootTranslateZ

    rotateControlScale = RotateControlScaleField()
    rcs = rotateControlScale
    rotateControlScaleX = rotateControlScale.rotateControlScaleX
    rcsx = rotateControlScaleX
    rotateControlScaleY = rotateControlScale.rotateControlScaleY
    rcsy = rotateControlScaleY
    rotateControlScaleZ = rotateControlScale.rotateControlScaleZ
    rcsz = rotateControlScaleZ

    rotateControlParentMatrix = DataMatrixField()
    rcpm = rotateControlParentMatrix

    offsetRootRotate = OffsetRootRotateField()
    rrf = offsetRootRotate
    offsetRootRotateX = offsetRootRotate.offsetRootRotateX
    rrfx = offsetRootRotateX
    offsetRootRotateY = offsetRootRotate.offsetRootRotateY
    rrfy = offsetRootRotateY
    offsetRootRotateZ = offsetRootRotate.offsetRootRotateZ
    rrfz = offsetRootRotateZ

    offsetRootRotateOrder = OffsetRootRotateOrderEnumField()
    rfor = offsetRootRotateOrder

    offsetRootRotatePivot = OffsetRootRotatePivotField()
    rpf = offsetRootRotatePivot
    offsetRootRotatePivotX = offsetRootRotatePivot.offsetRootRotatePivotX
    rppfx = offsetRootRotatePivotX
    offsetRootRotatePivotY = offsetRootRotatePivot.offsetRootRotatePivotY
    rppfy = offsetRootRotatePivotY
    offsetRootRotatePivotZ = offsetRootRotatePivot.offsetRootRotatePivotZ
    rppfz = offsetRootRotatePivotZ

    outRootTranslate = OutRootTranslateField()
    rto = outRootTranslate
    outRootTranslateX = outRootTranslate.outRootTranslateX
    rtox = outRootTranslateX
    outRootTranslateY = outRootTranslate.outRootTranslateY
    rtoy = outRootTranslateY
    outRootTranslateZ = outRootTranslate.outRootTranslateZ
    rtoz = outRootTranslateZ

    outRootRotate = OutRootRotateField()
    rro = outRootRotate
    outRootRotateX = outRootRotate.outRootRotateX
    rrox = outRootRotateX
    outRootRotateY = outRootRotate.outRootRotateY
    rroy = outRootRotateY
    outRootRotateZ = outRootRotate.outRootRotateZ
    rroz = outRootRotateZ
