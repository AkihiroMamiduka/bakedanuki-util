# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.compose_matrix import (
    InputQuatField,
    InputRotateField,
    InputScaleField,
    InputShearField,
    InputTranslateField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField


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


class GeneratedComposeMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "composeMatrix"

    outputMatrix = MatrixField(writable=False)
    omat = outputMatrix

    inputRotateOrder = InputRotateOrderEnumField(default_value=0)
    ro = inputRotateOrder

    useEulerRotation = BoolField(default_value=True)
    uer = useEulerRotation

    inputTranslate = InputTranslateField(default_value=(0.0, 0.0, 0.0))
    it = inputTranslate
    inputTranslateX = inputTranslate.inputTranslateX
    itx = inputTranslateX
    inputTranslateY = inputTranslate.inputTranslateY
    ity = inputTranslateY
    inputTranslateZ = inputTranslate.inputTranslateZ
    itz = inputTranslateZ

    inputRotate = InputRotateField(default_value=(0.0, 0.0, 0.0))
    ir = inputRotate
    inputRotateX = inputRotate.inputRotateX
    irx = inputRotateX
    inputRotateY = inputRotate.inputRotateY
    iry = inputRotateY
    inputRotateZ = inputRotate.inputRotateZ
    irz = inputRotateZ

    inputScale = InputScaleField(default_value=(1.0, 1.0, 1.0))
    is_ = inputScale
    inputScaleX = inputScale.inputScaleX
    isx = inputScaleX
    inputScaleY = inputScale.inputScaleY
    isy = inputScaleY
    inputScaleZ = inputScale.inputScaleZ
    isz = inputScaleZ

    inputShear = InputShearField(default_value=(0.0, 0.0, 0.0))
    ish = inputShear
    inputShearX = inputShear.inputShearX
    ishx = inputShearX
    inputShearY = inputShear.inputShearY
    ishy = inputShearY
    inputShearZ = inputShear.inputShearZ
    ishz = inputShearZ

    inputQuat = InputQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    iq = inputQuat
    inputQuatX = inputQuat.inputQuatX
    iqwx = inputQuatX
    inputQuatY = inputQuat.inputQuatY
    iqwy = inputQuatY
    inputQuatZ = inputQuat.inputQuatZ
    iqwz = inputQuatZ
    inputQuatW = inputQuat.inputQuatW
    iqw = inputQuatW
