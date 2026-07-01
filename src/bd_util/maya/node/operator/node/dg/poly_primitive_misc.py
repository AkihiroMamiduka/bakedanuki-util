# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_primitive_misc import AxisField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class PolyTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SOCCER_BALL = 0


class PolyTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SOCCER_BALL = 0

    NAME_MAP = {
        SOCCER_BALL: "Soccer Ball",
    }


class PolyTypeEnumField(
    EnumField[PolyTypeEnumAttrOperator, PolyTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PolyTypeEnumAttrOperator
    PLUG_CLS = PolyTypeEnumPlugOperator


class TextureEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    OBJECT = 1
    FACE = 2


class TextureEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    OBJECT = 1
    FACE = 2

    NAME_MAP = {
        NONE: "none",
        OBJECT: "object",
        FACE: "face",
    }


class TextureEnumField(
    EnumField[TextureEnumAttrOperator, TextureEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureEnumAttrOperator
    PLUG_CLS = TextureEnumPlugOperator


class CreateUVsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    NORMALIZATION_OFF = 1
    NORMALIZE_EACH_FACE_SEPARATELY = 2
    NORMALIZE_COLLECTIVELY = 3
    NORMALIZE_COLLECTIVELY_AND_PRESERVE_ASPECT_RATIO = 4


class CreateUVsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    NORMALIZATION_OFF = 1
    NORMALIZE_EACH_FACE_SEPARATELY = 2
    NORMALIZE_COLLECTIVELY = 3
    NORMALIZE_COLLECTIVELY_AND_PRESERVE_ASPECT_RATIO = 4

    NAME_MAP = {
        NONE: "None",
        NORMALIZATION_OFF: "Normalization Off",
        NORMALIZE_EACH_FACE_SEPARATELY: "Normalize Each Face Separately",
        NORMALIZE_COLLECTIVELY: "Normalize Collectively",
        NORMALIZE_COLLECTIVELY_AND_PRESERVE_ASPECT_RATIO: "Normalize Collectively and Preserve Aspect Ratio",
    }


class CreateUVsEnumField(
    EnumField[CreateUVsEnumAttrOperator, CreateUVsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CreateUVsEnumAttrOperator
    PLUG_CLS = CreateUVsEnumPlugOperator


class PolyPrimitiveMisc(DG):
    __slots__ = ()

    NODE_TYPE = "polyPrimitiveMisc"

    output = DataMeshField()
    out = output

    axis = AxisField()
    ax = axis
    axisX = axis.axisX
    axx = axisX
    axisY = axis.axisY
    axy = axisY
    axisZ = axis.axisZ
    axz = axisZ

    heightBaseline = DoubleLinearField()
    hbl = heightBaseline

    paramWarn = BoolField()
    pw = paramWarn

    uvSetName = DataStringField()
    uvs = uvSetName

    componentTagCreate = BoolField()
    ctc = componentTagCreate

    componentTagPrefix = DataStringField()
    pfx = componentTagPrefix

    componentTagSuffix = DataStringField()
    sfx = componentTagSuffix

    radius = DoubleLinearField()
    r = radius

    sideLength = DoubleLinearField()
    l = sideLength

    polyType = PolyTypeEnumField()
    pt = polyType

    texture = TextureEnumField()
    tx = texture

    createUVs = CreateUVsEnumField()
    cuv = createUVs
