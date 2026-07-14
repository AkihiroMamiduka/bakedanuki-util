# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.displacement_shader import (
    TangentField,
    VectorDisplacementField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class DisplacementModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    VECTOR_TANGENT_SPACE = 1
    VECTOR_OBJECT_SPACE = 2
    VECTOR_WORLD_SPACE = 3


class DisplacementModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    VECTOR_TANGENT_SPACE = 1
    VECTOR_OBJECT_SPACE = 2
    VECTOR_WORLD_SPACE = 3

    NAME_MAP = {
        NORMAL: "Normal",
        VECTOR_TANGENT_SPACE: "Vector, Tangent Space",
        VECTOR_OBJECT_SPACE: "Vector, Object Space",
        VECTOR_WORLD_SPACE: "Vector, World Space",
    }


class DisplacementModeEnumField(
    EnumField[DisplacementModeEnumAttrOperator, DisplacementModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplacementModeEnumAttrOperator
    PLUG_CLS = DisplacementModeEnumPlugOperator


class VectorEncodingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FLOATING_MINUS_POINT_ABSOLUTE = 0
    SIGNED_ENCODING = 1


class VectorEncodingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FLOATING_MINUS_POINT_ABSOLUTE = 0
    SIGNED_ENCODING = 1

    NAME_MAP = {
        FLOATING_MINUS_POINT_ABSOLUTE: "Floating-Point Absolute",
        SIGNED_ENCODING: "Signed Encoding",
    }


class VectorEncodingEnumField(
    EnumField[VectorEncodingEnumAttrOperator, VectorEncodingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VectorEncodingEnumAttrOperator
    PLUG_CLS = VectorEncodingEnumPlugOperator


class VectorSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    TANGENT = 2


class VectorSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    TANGENT = 2

    NAME_MAP = {
        WORLD: "World",
        OBJECT: "Object",
        TANGENT: "Tangent",
    }


class VectorSpaceEnumField(
    EnumField[VectorSpaceEnumAttrOperator, VectorSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VectorSpaceEnumAttrOperator
    PLUG_CLS = VectorSpaceEnumPlugOperator


class DisplacementShader(DG):
    __slots__ = ()

    NODE_TYPE = "displacementShader"

    displacementMode = DisplacementModeEnumField(default_value=0)
    dm = displacementMode

    displacement = FloatField(default_value=0.0)
    d = displacement

    vectorDisplacement = VectorDisplacementField(default_value=(0.0, 0.0, 0.0))
    vd = vectorDisplacement
    vectorDisplacementX = vectorDisplacement.vectorDisplacementX
    vdx = vectorDisplacementX
    vectorDisplacementY = vectorDisplacement.vectorDisplacementY
    vdy = vectorDisplacementY
    vectorDisplacementZ = vectorDisplacement.vectorDisplacementZ
    vdz = vectorDisplacementZ

    scale = FloatField(default_value=1.0)
    scl = scale

    vectorEncoding = VectorEncodingEnumField(default_value=0)
    ve = vectorEncoding

    vectorSpace = VectorSpaceEnumField(default_value=1)
    vs = vectorSpace

    yIsUp = BoolField(default_value=True)
    yup = yIsUp

    tangent = TangentField(default_value=(0.0, 0.0, 0.0))
    tan = tangent
    tangentX = tangent.tangentX
    tx = tangentX
    tangentY = tangent.tangentY
    ty = tangentY
    tangentZ = tangent.tangentZ
    tz = tangentZ

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiDisplacementPadding = FloatField(default_value=0.0, category="arnold")
    ai_displacement_padding = aiDisplacementPadding

    aiDisplacementZeroValue = FloatField(default_value=0.0, category="arnold")
    ai_displacement_zero_value = aiDisplacementZeroValue

    aiDisplacementAutoBump = BoolField(default_value=True, category="arnold")
    ai_displacement_auto_bump = aiDisplacementAutoBump
