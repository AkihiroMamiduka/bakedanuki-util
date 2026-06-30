# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.compose_matrix import (
    InputQuatField,
    InputRotateField,
    InputScaleField,
    InputShearField,
    InputTranslateField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class InputRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class InputRotateOrderEnumAttrOperator(EnumAttrOperator):
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


class InputRotateOrderEnumField(
    EnumField[InputRotateOrderEnumAttrOperator, InputRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputRotateOrderEnumAttrOperator
    PLUG_CLS = InputRotateOrderEnumPlugOperator


class ComposeMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "composeMatrix"

    outputMatrix = MatrixField()
    omat = outputMatrix

    inputRotateOrder = InputRotateOrderEnumField()
    ro = inputRotateOrder

    useEulerRotation = BoolField()
    uer = useEulerRotation

    inputTranslate = InputTranslateField()
    it = inputTranslate
    inputTranslateX = inputTranslate.inputTranslateX
    itx = inputTranslateX
    inputTranslateY = inputTranslate.inputTranslateY
    ity = inputTranslateY
    inputTranslateZ = inputTranslate.inputTranslateZ
    itz = inputTranslateZ

    inputRotate = InputRotateField()
    ir = inputRotate
    inputRotateX = inputRotate.inputRotateX
    irx = inputRotateX
    inputRotateY = inputRotate.inputRotateY
    iry = inputRotateY
    inputRotateZ = inputRotate.inputRotateZ
    irz = inputRotateZ

    inputScale = InputScaleField()
    is_ = inputScale
    inputScaleX = inputScale.inputScaleX
    isx = inputScaleX
    inputScaleY = inputScale.inputScaleY
    isy = inputScaleY
    inputScaleZ = inputScale.inputScaleZ
    isz = inputScaleZ

    inputShear = InputShearField()
    ish = inputShear
    inputShearX = inputShear.inputShearX
    ishx = inputShearX
    inputShearY = inputShear.inputShearY
    ishy = inputShearY
    inputShearZ = inputShear.inputShearZ
    ishz = inputShearZ

    inputQuat = InputQuatField()
    iq = inputQuat
    inputQuatX = inputQuat.inputQuatX
    iqwx = inputQuatX
    inputQuatY = inputQuat.inputQuatY
    iqwy = inputQuatY
    inputQuatZ = inputQuat.inputQuatZ
    iqwz = inputQuatZ
    inputQuatW = inputQuat.inputQuatW
    iqw = inputQuatW
