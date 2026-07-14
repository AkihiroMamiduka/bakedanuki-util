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

    coils = DoubleField(default_value=3.0, min_value=0.5, soft_max_value=20.0)
    c = coils

    height = DoubleLinearField(default_value=2.0, min_value=0.01, soft_max_value=100.0)
    h = height

    width = DoubleLinearField(default_value=2.0, min_value=0.01, soft_max_value=100.0)
    w = width

    radius = DoubleLinearField(default_value=0.4, min_value=0.01, soft_max_value=20.0)
    r = radius

    direction = DirectionEnumField(default_value=1)
    d = direction

    subdivisionsAxis = LongField(default_value=8, min_value=3, max_value=1001, soft_max_value=100)
    sa = subdivisionsAxis

    subdivisionsCoil = LongField(default_value=50, min_value=2, max_value=10001, soft_max_value=1000)
    sco = subdivisionsCoil

    subdivisionsCaps = LongField(default_value=0, min_value=0, max_value=1001, soft_max_value=50)
    sc = subdivisionsCaps

    texture = TextureEnumField(default_value=2)
    tx = texture

    createUVs = CreateUVsEnumField(default_value=2)
    cuv = createUVs

    roundCap = BoolField(default_value=False)
    rcp = roundCap

    useOldInitBehaviour = BoolField(default_value=False)
    oib = useOldInitBehaviour

    maya2022UVs = BoolField(default_value=False)
    ouv = maya2022UVs
