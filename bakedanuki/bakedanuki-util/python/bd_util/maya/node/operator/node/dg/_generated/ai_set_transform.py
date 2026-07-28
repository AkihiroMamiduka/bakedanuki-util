# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_set_transform import (
    RotateField,
    ScaleField,
    TranslateField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class TransformOrderEnumPlugOperator(EnumPlugOperator["TransformOrderEnumAttrOperator"]):
    __slots__ = ()

    SRT = 0
    STR = 1
    TSR = 2
    TRS = 3
    RST = 4
    RTS = 5


class TransformOrderEnumAttrOperator(EnumAttrOperator[TransformOrderEnumPlugOperator]):
    __slots__ = ()

    SRT = 0
    STR = 1
    TSR = 2
    TRS = 3
    RST = 4
    RTS = 5

    NAME_MAP = {
        SRT: "srt",
        STR: "str",
        TSR: "tsr",
        TRS: "trs",
        RST: "rst",
        RTS: "rts",
    }


class TransformOrderEnumField(
    EnumField[TransformOrderEnumAttrOperator, TransformOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransformOrderEnumAttrOperator
    PLUG_CLS = TransformOrderEnumPlugOperator


class RotateOrderEnumPlugOperator(EnumPlugOperator["RotateOrderEnumAttrOperator"]):
    __slots__ = ()

    XYZ = 0
    XZY = 1
    YXZ = 2
    YZX = 3
    ZXY = 4
    ZYX = 5


class RotateOrderEnumAttrOperator(EnumAttrOperator[RotateOrderEnumPlugOperator]):
    __slots__ = ()

    XYZ = 0
    XZY = 1
    YXZ = 2
    YZX = 3
    ZXY = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        XZY: "xzy",
        YXZ: "yxz",
        YZX: "yzx",
        ZXY: "zxy",
        ZYX: "zyx",
    }


class RotateOrderEnumField(
    EnumField[RotateOrderEnumAttrOperator, RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateOrderEnumAttrOperator
    PLUG_CLS = RotateOrderEnumPlugOperator


class ModeEnumPlugOperator(EnumPlugOperator["ModeEnumAttrOperator"]):
    __slots__ = ()

    APPEND = 0
    REPLACE = 1


class ModeEnumAttrOperator(EnumAttrOperator[ModeEnumPlugOperator]):
    __slots__ = ()

    APPEND = 0
    REPLACE = 1

    NAME_MAP = {
        APPEND: "append",
        REPLACE: "replace",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class GeneratedAiSetTransform(DG):
    __slots__ = ()

    NODE_TYPE = "aiSetTransform"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    inputs = MessageField(multi=True)

    selection = DataStringField()

    translate = TranslateField(default_value=(0.0, 0.0, 0.0))
    translateX = translate.translateX
    translatex = translateX
    translateY = translate.translateY
    translatey = translateY
    translateZ = translate.translateZ
    translatez = translateZ

    rotate = RotateField(default_value=(0.0, 0.0, 0.0))
    rotateX = rotate.rotateX
    rotatex = rotateX
    rotateY = rotate.rotateY
    rotatey = rotateY
    rotateZ = rotate.rotateZ
    rotatez = rotateZ

    scale = ScaleField(default_value=(1.0, 1.0, 1.0))
    scaleX = scale.scaleX
    scalex = scaleX
    scaleY = scale.scaleY
    scaley = scaleY
    scaleZ = scale.scaleZ
    scalez = scaleZ

    matrix = FltMatrixField()

    transformOrder = TransformOrderEnumField(default_value=0)
    transform_order = transformOrder

    rotateOrder = RotateOrderEnumField(default_value=0)
    rotate_order = rotateOrder

    mode = ModeEnumField(default_value=0)
