# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_normal_map import (
    InputField,
    NormalField,
    OutTransparencyField,
    OutValueField,
    TangentField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class OrderEnumPlugOperator(EnumPlugOperator["OrderEnumAttrOperator"]):
    __slots__ = ()

    XYZ = 0
    XZY = 1
    YXZ = 2
    YZX = 3
    ZXY = 4
    ZYX = 5


class OrderEnumAttrOperator(EnumAttrOperator[OrderEnumPlugOperator]):
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


class OrderEnumField(EnumField[OrderEnumAttrOperator, OrderEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = OrderEnumAttrOperator
    PLUG_CLS = OrderEnumPlugOperator


class GeneratedAiNormalMap(DG):
    __slots__ = ()

    NODE_TYPE = "aiNormalMap"

    outValue = OutValueField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outValue
    outValueX = outValue.outValueX
    outx = outValueX
    outValueY = outValue.outValueY
    outy = outValueY
    outValueZ = outValue.outValueZ
    outz = outValueZ

    outTransparency = OutTransparencyField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = InputField(default_value=(0.0, 0.0, 0.0))
    inputX = input.inputX
    inputx = inputX
    inputY = input.inputY
    inputy = inputY
    inputZ = input.inputZ
    inputz = inputZ

    tangent = TangentField(default_value=(0.0, 0.0, 0.0))
    tangentX = tangent.tangentX
    tangentx = tangentX
    tangentY = tangent.tangentY
    tangenty = tangentY
    tangentZ = tangent.tangentZ
    tangentz = tangentZ

    normal = NormalField(default_value=(0.0, 0.0, 0.0))
    normalX = normal.normalX
    normalx = normalX
    normalY = normal.normalY
    normaly = normalY
    normalZ = normal.normalZ
    normalz = normalZ

    order = OrderEnumField(default_value=0)

    invertX = BoolField(default_value=False)
    invert_x = invertX

    invertY = BoolField(default_value=False)
    invert_y = invertY

    invertZ = BoolField(default_value=False)
    invert_z = invertZ

    colorToSigned = BoolField(default_value=True)
    color_to_signed = colorToSigned

    tangentSpace = BoolField(default_value=True)
    tangent_space = tangentSpace

    strength = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)
