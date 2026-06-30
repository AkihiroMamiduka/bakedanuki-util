# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_normal_map import (
    InputField,
    NormalField,
    OutTransparencyField,
    OutValueField,
    TangentField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class OrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 1
    YXZ = 2
    YZX = 3
    ZXY = 4
    ZYX = 5


class OrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    XZY = 1
    YXZ = 2
    YZX = 3
    ZXY = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "XYZ",
        XZY: "XZY",
        YXZ: "YXZ",
        YZX: "YZX",
        ZXY: "ZXY",
        ZYX: "ZYX",
    }


class OrderEnumField(
    EnumField[OrderEnumAttrOperator, OrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OrderEnumAttrOperator
    PLUG_CLS = OrderEnumPlugOperator


class AiNormalMap(DG):
    __slots__ = ()

    NODE_TYPE = "aiNormalMap"

    outValue = OutValueField()
    out = outValue
    outValueX = outValue.outValueX
    outx = outValueX
    outValueY = outValue.outValueY
    outy = outValueY
    outValueZ = outValue.outValueZ
    outz = outValueZ

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = InputField()
    inputX = input.inputX
    inputx = inputX
    inputY = input.inputY
    inputy = inputY
    inputZ = input.inputZ
    inputz = inputZ

    tangent = TangentField()
    tangentX = tangent.tangentX
    tangentx = tangentX
    tangentY = tangent.tangentY
    tangenty = tangentY
    tangentZ = tangent.tangentZ
    tangentz = tangentZ

    normal = NormalField()
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ

    order = OrderEnumField()

    invertX = BoolField()
    invert_x = invertX

    invertY = BoolField()
    invert_y = invertY

    invertZ = BoolField()
    invert_z = invertZ

    colorToSigned = BoolField()
    color_to_signed = colorToSigned

    tangentSpace = BoolField()
    tangent_space = tangentSpace

    strength = FloatField()
