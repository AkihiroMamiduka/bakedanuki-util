# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_cone import AxisField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


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


class PolyCone(DG):
    __slots__ = ()

    NODE_TYPE = "polyCone"

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

    height = DoubleLinearField()
    h = height

    subdivisionsAxis = LongField()
    sa = subdivisionsAxis

    subdivisionsHeight = LongField()
    sh = subdivisionsHeight

    subdivisionsCap = LongField()
    sc = subdivisionsCap

    texture = BoolField()
    tx = texture

    createUVs = CreateUVsEnumField()
    cuv = createUVs

    roundCap = BoolField()
    rcp = roundCap
