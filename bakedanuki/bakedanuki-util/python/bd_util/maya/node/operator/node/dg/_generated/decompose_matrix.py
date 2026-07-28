# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.decompose_matrix import (
    OutputQuatField,
    OutputRotateField,
    OutputScaleField,
    OutputShearField,
    OutputTranslateField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField


class InputRotateOrderEnumPlugOperator(EnumPlugOperator["InputRotateOrderEnumAttrOperator"]):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class InputRotateOrderEnumAttrOperator(EnumAttrOperator[InputRotateOrderEnumPlugOperator]):
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


class GeneratedDecomposeMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "decomposeMatrix"

    inputMatrix = MatrixField()
    imat = inputMatrix

    inputRotateOrder = InputRotateOrderEnumField(default_value=0)
    ro = inputRotateOrder

    outputTranslate = OutputTranslateField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outputTranslate
    outputTranslateX = outputTranslate.outputTranslateX
    otx = outputTranslateX
    outputTranslateY = outputTranslate.outputTranslateY
    oty = outputTranslateY
    outputTranslateZ = outputTranslate.outputTranslateZ
    otz = outputTranslateZ

    outputRotate = OutputRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    or_ = outputRotate
    outputRotateX = outputRotate.outputRotateX
    orx = outputRotateX
    outputRotateY = outputRotate.outputRotateY
    ory = outputRotateY
    outputRotateZ = outputRotate.outputRotateZ
    orz = outputRotateZ

    outputScale = OutputScaleField(default_value=(0.0, 0.0, 0.0), writable=False)
    os = outputScale
    outputScaleX = outputScale.outputScaleX
    osx = outputScaleX
    outputScaleY = outputScale.outputScaleY
    osy = outputScaleY
    outputScaleZ = outputScale.outputScaleZ
    osz = outputScaleZ

    outputShear = OutputShearField(default_value=(0.0, 0.0, 0.0), writable=False)
    osh = outputShear
    outputShearX = outputShear.outputShearX
    oshx = outputShearX
    outputShearY = outputShear.outputShearY
    oshy = outputShearY
    outputShearZ = outputShear.outputShearZ
    oshz = outputShearZ

    outputQuat = OutputQuatField(default_value=(0.0, 0.0, 0.0, 0.0), writable=False)
    oq = outputQuat
    outputQuatX = outputQuat.outputQuatX
    oqx = outputQuatX
    outputQuatY = outputQuat.outputQuatY
    oqy = outputQuatY
    outputQuatZ = outputQuat.outputQuatZ
    oqz = outputQuatZ
    outputQuatW = outputQuat.outputQuatW
    oqw = outputQuatW
