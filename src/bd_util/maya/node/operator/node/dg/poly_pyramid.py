# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_pyramid import AxisField
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


class NumberOfSidesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _3 = 3
    _4 = 4
    _5 = 5


class NumberOfSidesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _3 = 3
    _4 = 4
    _5 = 5

    NAME_MAP = {
        _3: "3",
        _4: "4",
        _5: "5",
    }


class NumberOfSidesEnumField(
    EnumField[NumberOfSidesEnumAttrOperator, NumberOfSidesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NumberOfSidesEnumAttrOperator
    PLUG_CLS = NumberOfSidesEnumPlugOperator


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


class PolyPyramid(DG):
    __slots__ = ()

    NODE_TYPE = "polyPyramid"

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

    sideLength = DoubleLinearField()
    w = sideLength

    numberOfSides = NumberOfSidesEnumField()
    ns = numberOfSides

    subdivisionsHeight = LongField()
    sh = subdivisionsHeight

    subdivisionsCaps = LongField()
    sc = subdivisionsCaps

    texture = BoolField()
    tx = texture

    createUVs = CreateUVsEnumField()
    cuv = createUVs
