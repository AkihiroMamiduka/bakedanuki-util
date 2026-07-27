# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_matrix_transform import (
    AxisField,
    OutTransparencyField,
    PivotField,
    RotationField,
    ScaleField,
    TranslateField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class TransformOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SRT = 0
    STR = 1
    RST = 2
    RTS = 3
    TSR = 4
    TRS = 5


class TransformOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SRT = 0
    STR = 1
    RST = 2
    RTS = 3
    TSR = 4
    TRS = 5

    NAME_MAP = {
        SRT: "srt",
        STR: "str",
        RST: "rst",
        RTS: "rts",
        TSR: "tsr",
        TRS: "trs",
    }


class TransformOrderEnumField(
    EnumField[TransformOrderEnumAttrOperator, TransformOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransformOrderEnumAttrOperator
    PLUG_CLS = TransformOrderEnumPlugOperator


class RotationTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    EULER = 0
    AXIS = 1


class RotationTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    EULER = 0
    AXIS = 1

    NAME_MAP = {
        EULER: "euler",
        AXIS: "axis",
    }


class RotationTypeEnumField(
    EnumField[RotationTypeEnumAttrOperator, RotationTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationTypeEnumAttrOperator
    PLUG_CLS = RotationTypeEnumPlugOperator


class UnitsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RADIANS = 0
    DEGREES = 1


class UnitsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RADIANS = 0
    DEGREES = 1

    NAME_MAP = {
        RADIANS: "radians",
        DEGREES: "degrees",
    }


class UnitsEnumField(
    EnumField[UnitsEnumAttrOperator, UnitsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UnitsEnumAttrOperator
    PLUG_CLS = UnitsEnumPlugOperator


class RotationOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 1
    YXZ = 2
    YZX = 3
    ZXY = 4
    ZYX = 5


class RotationOrderEnumAttrOperator(EnumAttrOperator):
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


class RotationOrderEnumField(
    EnumField[RotationOrderEnumAttrOperator, RotationOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationOrderEnumAttrOperator
    PLUG_CLS = RotationOrderEnumPlugOperator


class GeneratedAiMatrixTransform(DG):
    __slots__ = ()

    NODE_TYPE = "aiMatrixTransform"

    outValue = FltMatrixField(writable=False)
    out = outValue

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    transformOrder = TransformOrderEnumField(default_value=0)
    transform_order = transformOrder

    rotationType = RotationTypeEnumField(default_value=0)
    rotation_type = rotationType

    units = UnitsEnumField(default_value=1)

    rotationOrder = RotationOrderEnumField(default_value=0)
    rotation_order = rotationOrder

    rotation = RotationField(default_value=(0.0, 0.0, 0.0))
    rotationX = rotation.rotationX
    rotationx = rotationX
    rotationY = rotation.rotationY
    rotationy = rotationY
    rotationZ = rotation.rotationZ
    rotationz = rotationZ

    axis = AxisField(default_value=(1.0, 0.0, 0.0))
    axisX = axis.axisX
    axisx = axisX
    axisY = axis.axisY
    axisy = axisY
    axisZ = axis.axisZ
    axisz = axisZ

    angle = FloatField(default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0)

    translate = TranslateField(default_value=(0.0, 0.0, 0.0))
    translateX = translate.translateX
    translatex = translateX
    translateY = translate.translateY
    translatey = translateY
    translateZ = translate.translateZ
    translatez = translateZ

    scale = ScaleField(default_value=(1.0, 1.0, 1.0))
    scaleX = scale.scaleX
    scalex = scaleX
    scaleY = scale.scaleY
    scaley = scaleY
    scaleZ = scale.scaleZ
    scalez = scaleZ

    pivot = PivotField(default_value=(0.0, 0.0, 0.0))
    pivotX = pivot.pivotX
    pivotx = pivotX
    pivotY = pivot.pivotY
    pivoty = pivotY
    pivotZ = pivot.pivotZ
    pivotz = pivotZ
