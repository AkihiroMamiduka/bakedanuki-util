# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_primitive_misc import AxisField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


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


class GeneratedPolyPrimitiveMisc(DG):
    __slots__ = ()

    NODE_TYPE = "polyPrimitiveMisc"

    output = DataMeshField(writable=False)
    out = output

    axis = AxisField(default_value=(0.0, 1.0, 0.0))
    ax = axis
    axisX = axis.axisX
    axx = axisX
    axisY = axis.axisY
    axy = axisY
    axisZ = axis.axisZ
    axz = axisZ

    heightBaseline = DoubleLinearField(default_value=0.0, min_value=-1.0, max_value=1.0)
    hbl = heightBaseline

    paramWarn = BoolField(default_value=True)
    pw = paramWarn

    uvSetName = DataStringField()
    uvs = uvSetName

    componentTagCreate = BoolField(default_value=True)
    ctc = componentTagCreate

    componentTagPrefix = DataStringField()
    pfx = componentTagPrefix

    componentTagSuffix = DataStringField()
    sfx = componentTagSuffix

    radius = DoubleLinearField(default_value=1.0, min_value=0.01, soft_max_value=100.0)
    r = radius

    sideLength = DoubleLinearField(default_value=0.0, min_value=0.01, soft_max_value=100.0)
    l = sideLength

    polyType = PolyTypeEnumField(default_value=0)
    pt = polyType

    texture = TextureEnumField(default_value=2)
    tx = texture

    createUVs = CreateUVsEnumField(default_value=3)
    cuv = createUVs
