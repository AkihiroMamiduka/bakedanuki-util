# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.character_offset import (
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
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.matrix import DataMatrixField


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


class _GeneratedCharacterOffset(DG):
    __slots__ = ()

    NODE_TYPE = "characterOffset"

    inRootTranslate = InRootTranslateField(default_value=(0.0, 0.0, 0.0))
    rti = inRootTranslate
    inRootTranslateX = inRootTranslate.inRootTranslateX
    rtix = inRootTranslateX
    inRootTranslateY = inRootTranslate.inRootTranslateY
    rtiy = inRootTranslateY
    inRootTranslateZ = inRootTranslate.inRootTranslateZ
    rtiz = inRootTranslateZ

    inRootRotate = InRootRotateField(default_value=(0.0, 0.0, 0.0))
    rri = inRootRotate
    inRootRotateX = inRootRotate.inRootRotateX
    rrix = inRootRotateX
    inRootRotateY = inRootRotate.inRootRotateY
    rriy = inRootRotateY
    inRootRotateZ = inRootRotate.inRootRotateZ
    rriz = inRootRotateZ

    rootRotateOrder = RootRotateOrderEnumField(default_value=0)
    rror = rootRotateOrder

    rootJointOrient = RootJointOrientField(default_value=(0.0, 0.0, 0.0))
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

    applyControlParentTransform = BoolField(default_value=False)
    acpx = applyControlParentTransform

    enable = BoolField(default_value=True)
    nabl = enable

    offsetRootTranslate = OffsetRootTranslateField(default_value=(0.0, 0.0, 0.0))
    rtf = offsetRootTranslate
    offsetRootTranslateX = offsetRootTranslate.offsetRootTranslateX
    rtfx = offsetRootTranslateX
    offsetRootTranslateY = offsetRootTranslate.offsetRootTranslateY
    rtfy = offsetRootTranslateY
    offsetRootTranslateZ = offsetRootTranslate.offsetRootTranslateZ
    rtfz = offsetRootTranslateZ

    initialOffsetRootTranslate = InitialOffsetRootTranslateField(default_value=(0.0, 0.0, 0.0))
    itf = initialOffsetRootTranslate
    initialOffsetRootTranslateX = initialOffsetRootTranslate.initialOffsetRootTranslateX
    itfx = initialOffsetRootTranslateX
    initialOffsetRootTranslateY = initialOffsetRootTranslate.initialOffsetRootTranslateY
    itfy = initialOffsetRootTranslateY
    initialOffsetRootTranslateZ = initialOffsetRootTranslate.initialOffsetRootTranslateZ
    itfz = initialOffsetRootTranslateZ

    rotateControlScale = RotateControlScaleField(default_value=(1.0, 1.0, 1.0))
    rcs = rotateControlScale
    rotateControlScaleX = rotateControlScale.rotateControlScaleX
    rcsx = rotateControlScaleX
    rotateControlScaleY = rotateControlScale.rotateControlScaleY
    rcsy = rotateControlScaleY
    rotateControlScaleZ = rotateControlScale.rotateControlScaleZ
    rcsz = rotateControlScaleZ

    rotateControlParentMatrix = DataMatrixField()
    rcpm = rotateControlParentMatrix

    offsetRootRotate = OffsetRootRotateField(default_value=(0.0, 0.0, 0.0))
    rrf = offsetRootRotate
    offsetRootRotateX = offsetRootRotate.offsetRootRotateX
    rrfx = offsetRootRotateX
    offsetRootRotateY = offsetRootRotate.offsetRootRotateY
    rrfy = offsetRootRotateY
    offsetRootRotateZ = offsetRootRotate.offsetRootRotateZ
    rrfz = offsetRootRotateZ

    offsetRootRotateOrder = OffsetRootRotateOrderEnumField(default_value=0)
    rfor = offsetRootRotateOrder

    offsetRootRotatePivot = OffsetRootRotatePivotField(default_value=(0.0, 0.0, 0.0))
    rpf = offsetRootRotatePivot
    offsetRootRotatePivotX = offsetRootRotatePivot.offsetRootRotatePivotX
    rppfx = offsetRootRotatePivotX
    offsetRootRotatePivotY = offsetRootRotatePivot.offsetRootRotatePivotY
    rppfy = offsetRootRotatePivotY
    offsetRootRotatePivotZ = offsetRootRotatePivot.offsetRootRotatePivotZ
    rppfz = offsetRootRotatePivotZ

    outRootTranslate = OutRootTranslateField(default_value=(0.0, 0.0, 0.0), writable=False)
    rto = outRootTranslate
    outRootTranslateX = outRootTranslate.outRootTranslateX
    rtox = outRootTranslateX
    outRootTranslateY = outRootTranslate.outRootTranslateY
    rtoy = outRootTranslateY
    outRootTranslateZ = outRootTranslate.outRootTranslateZ
    rtoz = outRootTranslateZ

    outRootRotate = OutRootRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    rro = outRootRotate
    outRootRotateX = outRootRotate.outRootRotateX
    rrox = outRootRotateX
    outRootRotateY = outRootRotate.outRootRotateY
    rroy = outRootRotateY
    outRootRotateZ = outRootRotate.outRootRotateZ
    rroz = outRootRotateZ
