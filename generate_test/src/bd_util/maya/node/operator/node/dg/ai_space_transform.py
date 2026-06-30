# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_space_transform import (
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


class TypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POINT = 0
    VECTOR = 1
    NORMAL = 2


class TypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POINT = 0
    VECTOR = 1
    NORMAL = 2

    NAME_MAP = {
        POINT: "point",
        VECTOR: "vector",
        NORMAL: "normal",
    }


class TypeEnumField(
    EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class FromEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    CAMERA = 2
    SCREEN = 3
    TANGENT = 4


class FromEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    CAMERA = 2
    SCREEN = 3
    TANGENT = 4

    NAME_MAP = {
        WORLD: "world",
        OBJECT: "object",
        CAMERA: "camera",
        SCREEN: "screen",
        TANGENT: "tangent",
    }


class FromEnumField(
    EnumField[FromEnumAttrOperator, FromEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FromEnumAttrOperator
    PLUG_CLS = FromEnumPlugOperator


class ToEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    CAMERA = 2
    SCREEN = 3
    TANGENT = 4


class ToEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    CAMERA = 2
    SCREEN = 3
    TANGENT = 4

    NAME_MAP = {
        WORLD: "world",
        OBJECT: "object",
        CAMERA: "camera",
        SCREEN: "screen",
        TANGENT: "tangent",
    }


class ToEnumField(
    EnumField[ToEnumAttrOperator, ToEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ToEnumAttrOperator
    PLUG_CLS = ToEnumPlugOperator


class AiSpaceTransform(DG):
    __slots__ = ()

    NODE_TYPE = "aiSpaceTransform"

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

    type = TypeEnumField()

    from_ = FromEnumField()

    to = ToEnumField()

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

    normalize = BoolField()

    scale = FloatField()
