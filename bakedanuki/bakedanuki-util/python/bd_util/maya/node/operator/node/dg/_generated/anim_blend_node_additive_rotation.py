# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.anim_blend_node_additive_rotation import (
    InputAField,
    InputBField,
    OutputField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.string import DataStringField


class AccumulationModeEnumPlugOperator(
    EnumPlugOperator["AccumulationModeEnumAttrOperator"]
):
    __slots__ = ()

    BY_COMPONENT = 0
    BY_LAYER_CUMULATIVE = 1
    BY_LAYER_BLENDED = 2


class AccumulationModeEnumAttrOperator(
    EnumAttrOperator[AccumulationModeEnumPlugOperator]
):
    __slots__ = ()

    BY_COMPONENT = 0
    BY_LAYER_CUMULATIVE = 1
    BY_LAYER_BLENDED = 2

    NAME_MAP = {
        BY_COMPONENT: "by Component",
        BY_LAYER_CUMULATIVE: "by Layer Cumulative",
        BY_LAYER_BLENDED: "by Layer Blended",
    }


class AccumulationModeEnumField(
    EnumField[
        AccumulationModeEnumAttrOperator, AccumulationModeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AccumulationModeEnumAttrOperator
    PLUG_CLS = AccumulationModeEnumPlugOperator


class RotateOrderEnumPlugOperator(
    EnumPlugOperator["RotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RotateOrderEnumAttrOperator(
    EnumAttrOperator[RotateOrderEnumPlugOperator]
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


class RotateOrderEnumField(
    EnumField[RotateOrderEnumAttrOperator, RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateOrderEnumAttrOperator
    PLUG_CLS = RotateOrderEnumPlugOperator


class RotationInterpolationEnumPlugOperator(
    EnumPlugOperator["RotationInterpolationEnumAttrOperator"]
):
    __slots__ = ()

    EULER = 0
    QUATERNION_SLERP = 1


class RotationInterpolationEnumAttrOperator(
    EnumAttrOperator[RotationInterpolationEnumPlugOperator]
):
    __slots__ = ()

    EULER = 0
    QUATERNION_SLERP = 1

    NAME_MAP = {
        EULER: "Euler",
        QUATERNION_SLERP: "Quaternion Slerp",
    }


class RotationInterpolationEnumField(
    EnumField[
        RotationInterpolationEnumAttrOperator,
        RotationInterpolationEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = RotationInterpolationEnumAttrOperator
    PLUG_CLS = RotationInterpolationEnumPlugOperator


class GeneratedAnimBlendNodeAdditiveRotation(DG):
    __slots__ = ()

    NODE_TYPE = "animBlendNodeAdditiveRotation"

    weightA = DoubleField(default_value=1.0)
    wa = weightA

    weightB = DoubleField(default_value=1.0)
    wb = weightB

    destinationPlug = DataStringField(multi=True)
    dp = destinationPlug

    inputA = InputAField(default_value=(0.0, 0.0, 0.0))
    ia = inputA
    inputAX = inputA.inputAX
    iax = inputAX
    inputAY = inputA.inputAY
    iay = inputAY
    inputAZ = inputA.inputAZ
    iaz = inputAZ

    inputB = InputBField(default_value=(0.0, 0.0, 0.0))
    ib = inputB
    inputBX = inputB.inputBX
    ibx = inputBX
    inputBY = inputB.inputBY
    iby = inputBY
    inputBZ = inputB.inputBZ
    ibz = inputBZ

    accumulationMode = AccumulationModeEnumField(default_value=0)
    acm = accumulationMode

    byLayerAccLegacyMode = BoolField(default_value=False)
    bllm = byLayerAccLegacyMode

    rotateOrder = RotateOrderEnumField(default_value=0)
    ro = rotateOrder

    rotationInterpolation = RotationInterpolationEnumField(default_value=0)
    ri = rotationInterpolation

    output = OutputField(default_value=(0.0, 0.0, 0.0))
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
