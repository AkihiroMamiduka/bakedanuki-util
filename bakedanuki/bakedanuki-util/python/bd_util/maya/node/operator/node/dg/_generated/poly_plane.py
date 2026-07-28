# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_plane import AxisField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class TextureEnumPlugOperator(EnumPlugOperator["TextureEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    STRETCH_TO_FIT = 1
    PRESERVE_ASPECT_RATIO = 2


class TextureEnumAttrOperator(EnumAttrOperator[TextureEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    STRETCH_TO_FIT = 1
    PRESERVE_ASPECT_RATIO = 2

    NAME_MAP = {
        NONE: "none",
        STRETCH_TO_FIT: "Stretch to fit",
        PRESERVE_ASPECT_RATIO: "Preserve Aspect Ratio",
    }


class TextureEnumField(
    EnumField[TextureEnumAttrOperator, TextureEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureEnumAttrOperator
    PLUG_CLS = TextureEnumPlugOperator


class CreateUVsEnumPlugOperator(EnumPlugOperator["CreateUVsEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    NORMALIZATION_OFF = 1
    NORMALIZE_AND_PRESERVE_ASPECT_RATIO = 2


class CreateUVsEnumAttrOperator(EnumAttrOperator[CreateUVsEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    NORMALIZATION_OFF = 1
    NORMALIZE_AND_PRESERVE_ASPECT_RATIO = 2

    NAME_MAP = {
        NONE: "None",
        NORMALIZATION_OFF: "Normalization Off",
        NORMALIZE_AND_PRESERVE_ASPECT_RATIO: "Normalize and Preserve Aspect Ratio",
    }


class CreateUVsEnumField(
    EnumField[CreateUVsEnumAttrOperator, CreateUVsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CreateUVsEnumAttrOperator
    PLUG_CLS = CreateUVsEnumPlugOperator


class GeneratedPolyPlane(DG):
    __slots__ = ()

    NODE_TYPE = "polyPlane"

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

    heightBaseline = DoubleLinearField(
        default_value=0.0, min_value=-1.0, max_value=1.0
    )
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

    width = DoubleLinearField(
        default_value=1.0, min_value=0.01, soft_max_value=100.0
    )
    w = width

    height = DoubleLinearField(
        default_value=1.0, min_value=0.01, soft_max_value=100.0
    )
    h = height

    subdivisionsWidth = LongField(
        default_value=10, min_value=1, soft_max_value=50
    )
    sw = subdivisionsWidth

    subdivisionsHeight = LongField(
        default_value=10, min_value=1, soft_max_value=50
    )
    sh = subdivisionsHeight

    texture = TextureEnumField(default_value=1)
    tx = texture

    createUVs = CreateUVsEnumField(default_value=1)
    cuv = createUVs
