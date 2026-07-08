# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.pair_blend import (
    InRotate1Field,
    InRotate2Field,
    InTranslate1Field,
    InTranslate2Field,
    OutRotateField,
    OutTranslateField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField


class CurrentDriverEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    INPUT_1 = 1
    INPUT_2 = 2


class CurrentDriverEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    INPUT_1 = 1
    INPUT_2 = 2

    NAME_MAP = {
        INPUT_1: "Input 1",
        INPUT_2: "Input 2",
    }


class CurrentDriverEnumField(
    EnumField[CurrentDriverEnumAttrOperator, CurrentDriverEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurrentDriverEnumAttrOperator
    PLUG_CLS = CurrentDriverEnumPlugOperator


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


class TranslateXModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLEND_INPUTS = 0
    INPUT_1_ONLY = 1
    INPUT_2_ONLY = 2


class TranslateXModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLEND_INPUTS = 0
    INPUT_1_ONLY = 1
    INPUT_2_ONLY = 2

    NAME_MAP = {
        BLEND_INPUTS: "Blend Inputs",
        INPUT_1_ONLY: "Input 1 Only",
        INPUT_2_ONLY: "Input 2 Only",
    }


class TranslateXModeEnumField(
    EnumField[TranslateXModeEnumAttrOperator, TranslateXModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateXModeEnumAttrOperator
    PLUG_CLS = TranslateXModeEnumPlugOperator


class TranslateYModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLEND_INPUTS = 0
    INPUT_1_ONLY = 1
    INPUT_2_ONLY = 2


class TranslateYModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLEND_INPUTS = 0
    INPUT_1_ONLY = 1
    INPUT_2_ONLY = 2

    NAME_MAP = {
        BLEND_INPUTS: "Blend Inputs",
        INPUT_1_ONLY: "Input 1 Only",
        INPUT_2_ONLY: "Input 2 Only",
    }


class TranslateYModeEnumField(
    EnumField[TranslateYModeEnumAttrOperator, TranslateYModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateYModeEnumAttrOperator
    PLUG_CLS = TranslateYModeEnumPlugOperator


class TranslateZModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLEND_INPUTS = 0
    INPUT_1_ONLY = 1
    INPUT_2_ONLY = 2


class TranslateZModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLEND_INPUTS = 0
    INPUT_1_ONLY = 1
    INPUT_2_ONLY = 2

    NAME_MAP = {
        BLEND_INPUTS: "Blend Inputs",
        INPUT_1_ONLY: "Input 1 Only",
        INPUT_2_ONLY: "Input 2 Only",
    }


class TranslateZModeEnumField(
    EnumField[TranslateZModeEnumAttrOperator, TranslateZModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateZModeEnumAttrOperator
    PLUG_CLS = TranslateZModeEnumPlugOperator


class RotateModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLEND_INPUTS = 0
    INPUT_1_ONLY = 1
    INPUT_2_ONLY = 2


class RotateModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLEND_INPUTS = 0
    INPUT_1_ONLY = 1
    INPUT_2_ONLY = 2

    NAME_MAP = {
        BLEND_INPUTS: "Blend Inputs",
        INPUT_1_ONLY: "Input 1 Only",
        INPUT_2_ONLY: "Input 2 Only",
    }


class RotateModeEnumField(
    EnumField[RotateModeEnumAttrOperator, RotateModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateModeEnumAttrOperator
    PLUG_CLS = RotateModeEnumPlugOperator


class RotInterpolationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    EULER_ANGLES = 0
    QUATERNIONS = 1


class RotInterpolationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    EULER_ANGLES = 0
    QUATERNIONS = 1

    NAME_MAP = {
        EULER_ANGLES: "Euler angles",
        QUATERNIONS: "Quaternions",
    }


class RotInterpolationEnumField(
    EnumField[RotInterpolationEnumAttrOperator, RotInterpolationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotInterpolationEnumAttrOperator
    PLUG_CLS = RotInterpolationEnumPlugOperator


class PairBlend(DG):
    __slots__ = ()

    NODE_TYPE = "pairBlend"

    currentDriver = CurrentDriverEnumField(default_value=1)
    c = currentDriver

    inTranslate1 = InTranslate1Field(default_value=(0.0, 0.0, 0.0))
    it1 = inTranslate1
    inTranslateX1 = inTranslate1.inTranslateX1
    itx1 = inTranslateX1
    inTranslateY1 = inTranslate1.inTranslateY1
    ity1 = inTranslateY1
    inTranslateZ1 = inTranslate1.inTranslateZ1
    itz1 = inTranslateZ1

    inRotate1 = InRotate1Field(default_value=(0.0, 0.0, 0.0))
    ir1 = inRotate1
    inRotateX1 = inRotate1.inRotateX1
    irx1 = inRotateX1
    inRotateY1 = inRotate1.inRotateY1
    iry1 = inRotateY1
    inRotateZ1 = inRotate1.inRotateZ1
    irz1 = inRotateZ1

    inTranslate2 = InTranslate2Field(default_value=(0.0, 0.0, 0.0))
    it2 = inTranslate2
    inTranslateX2 = inTranslate2.inTranslateX2
    itx2 = inTranslateX2
    inTranslateY2 = inTranslate2.inTranslateY2
    ity2 = inTranslateY2
    inTranslateZ2 = inTranslate2.inTranslateZ2
    itz2 = inTranslateZ2

    inRotate2 = InRotate2Field(default_value=(0.0, 0.0, 0.0))
    ir2 = inRotate2
    inRotateX2 = inRotate2.inRotateX2
    irx2 = inRotateX2
    inRotateY2 = inRotate2.inRotateY2
    iry2 = inRotateY2
    inRotateZ2 = inRotate2.inRotateZ2
    irz2 = inRotateZ2

    weight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    w = weight

    rotateOrder = RotateOrderEnumField(default_value=0)
    ro = rotateOrder

    translateXMode = TranslateXModeEnumField(default_value=0)
    txm = translateXMode

    translateYMode = TranslateYModeEnumField(default_value=0)
    tym = translateYMode

    translateZMode = TranslateZModeEnumField(default_value=0)
    tzm = translateZMode

    rotateMode = RotateModeEnumField(default_value=0)
    rm = rotateMode

    rotInterpolation = RotInterpolationEnumField(default_value=0)
    ri = rotInterpolation

    outTranslate = OutTranslateField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTranslate
    outTranslateX = outTranslate.outTranslateX
    otx = outTranslateX
    outTranslateY = outTranslate.outTranslateY
    oty = outTranslateY
    outTranslateZ = outTranslate.outTranslateZ
    otz = outTranslateZ

    outRotate = OutRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    or_ = outRotate
    outRotateX = outRotate.outRotateX
    orx = outRotateX
    outRotateY = outRotate.outRotateY
    ory = outRotateY
    outRotateZ = outRotate.outRotateZ
    orz = outRotateZ
