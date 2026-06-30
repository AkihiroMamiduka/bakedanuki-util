# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.decompose_matrix import (
    OutputQuatField,
    OutputRotateField,
    OutputScaleField,
    OutputShearField,
    OutputTranslateField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField


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


class DecomposeMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "decomposeMatrix"

    inputMatrix = MatrixField()
    imat = inputMatrix

    inputRotateOrder = InputRotateOrderEnumField()
    ro = inputRotateOrder

    outputTranslate = OutputTranslateField()
    ot = outputTranslate
    outputTranslateX = outputTranslate.outputTranslateX
    otx = outputTranslateX
    outputTranslateY = outputTranslate.outputTranslateY
    oty = outputTranslateY
    outputTranslateZ = outputTranslate.outputTranslateZ
    otz = outputTranslateZ

    outputRotate = OutputRotateField()
    or_ = outputRotate
    outputRotateX = outputRotate.outputRotateX
    orx = outputRotateX
    outputRotateY = outputRotate.outputRotateY
    ory = outputRotateY
    outputRotateZ = outputRotate.outputRotateZ
    orz = outputRotateZ

    outputScale = OutputScaleField()
    os = outputScale
    outputScaleX = outputScale.outputScaleX
    osx = outputScaleX
    outputScaleY = outputScale.outputScaleY
    osy = outputScaleY
    outputScaleZ = outputScale.outputScaleZ
    osz = outputScaleZ

    outputShear = OutputShearField()
    osh = outputShear
    outputShearX = outputShear.outputShearX
    oshx = outputShearX
    outputShearY = outputShear.outputShearY
    oshy = outputShearY
    outputShearZ = outputShear.outputShearZ
    oshz = outputShearZ

    outputQuat = OutputQuatField()
    oq = outputQuat
    outputQuatX = outputQuat.outputQuatX
    oqx = outputQuatX
    outputQuatY = outputQuat.outputQuatY
    oqy = outputQuatY
    outputQuatZ = outputQuat.outputQuatZ
    oqz = outputQuatZ
    outputQuatW = outputQuat.outputQuatW
    oqw = outputQuatW
