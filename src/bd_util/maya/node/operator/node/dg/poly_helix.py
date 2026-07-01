# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_helix import AxisField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class DirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1


class DirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1

    NAME_MAP = {
        CLOCKWISE: "Clockwise",
        COUNTERCLOCKWISE: "Counterclockwise",
    }


class DirectionEnumField(
    EnumField[DirectionEnumAttrOperator, DirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionEnumAttrOperator
    PLUG_CLS = DirectionEnumPlugOperator


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
    NORMALIZE = 2
    NORMALIZE_AND_PRESERVE_ASPECT_RATIO = 3


class CreateUVsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    NORMALIZATION_OFF = 1
    NORMALIZE = 2
    NORMALIZE_AND_PRESERVE_ASPECT_RATIO = 3

    NAME_MAP = {
        NONE: "None",
        NORMALIZATION_OFF: "Normalization Off",
        NORMALIZE: "Normalize",
        NORMALIZE_AND_PRESERVE_ASPECT_RATIO: "Normalize and Preserve Aspect Ratio",
    }


class CreateUVsEnumField(
    EnumField[CreateUVsEnumAttrOperator, CreateUVsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CreateUVsEnumAttrOperator
    PLUG_CLS = CreateUVsEnumPlugOperator


class PolyHelix(DG):
    __slots__ = ()

    NODE_TYPE = "polyHelix"

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

    coils = DoubleField()
    c = coils

    height = DoubleLinearField()
    h = height

    width = DoubleLinearField()
    w = width

    radius = DoubleLinearField()
    r = radius

    direction = DirectionEnumField()
    d = direction

    subdivisionsAxis = LongField()
    sa = subdivisionsAxis

    subdivisionsCoil = LongField()
    sco = subdivisionsCoil

    subdivisionsCaps = LongField()
    sc = subdivisionsCaps

    texture = TextureEnumField()
    tx = texture

    createUVs = CreateUVsEnumField()
    cuv = createUVs

    roundCap = BoolField()
    rcp = roundCap

    useOldInitBehaviour = BoolField()
    oib = useOldInitBehaviour

    maya2022UVs = BoolField()
    ouv = maya2022UVs
