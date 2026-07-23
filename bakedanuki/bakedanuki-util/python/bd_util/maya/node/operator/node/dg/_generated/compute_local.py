# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.compute_local import (
    PostRField,
    PreRField,
    RotateField,
    ScaleField,
    TranslateField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField


class RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RotateOrderEnumAttrOperator(EnumAttrOperator):
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


class RotateOrderEnumField(
    EnumField[RotateOrderEnumAttrOperator, RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateOrderEnumAttrOperator
    PLUG_CLS = RotateOrderEnumPlugOperator


class _GeneratedComputeLocal(DG):
    __slots__ = ()

    NODE_TYPE = "ComputeLocal"

    translate = TranslateField(default_value=(0.0, 0.0, 0.0))
    T = translate
    translateX = translate.translateX
    tx = translateX
    translateY = translate.translateY
    ty = translateY
    translateZ = translate.translateZ
    tz = translateZ

    rotate = RotateField(default_value=(0.0, 0.0, 0.0))
    R = rotate
    rotateX = rotate.rotateX
    rx = rotateX
    rotateY = rotate.rotateY
    ry = rotateY
    rotateZ = rotate.rotateZ
    rz = rotateZ

    scale = ScaleField(default_value=(0.0, 0.0, 0.0))
    S = scale
    scaleX = scale.scaleX
    sx = scaleX
    scaleY = scale.scaleY
    sy = scaleY
    scaleZ = scale.scaleZ
    sz = scaleZ

    PreR = PreRField(default_value=(0.0, 0.0, 0.0))
    PreRx = PreR.PreRx
    PreRy = PreR.PreRy
    PreRz = PreR.PreRz

    PostR = PostRField(default_value=(0.0, 0.0, 0.0))
    PostRx = PostR.PostRx
    PostRy = PostR.PostRy
    PostRz = PostR.PostRz

    PGX = MatrixField()

    GX = MatrixField()

    rotateOrder = RotateOrderEnumField(default_value=0)
    ro = rotateOrder
