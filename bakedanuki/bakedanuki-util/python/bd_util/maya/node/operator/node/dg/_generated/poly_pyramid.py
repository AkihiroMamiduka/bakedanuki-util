# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_pyramid import AxisField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class NumberOfSidesEnumPlugOperator(EnumPlugOperator["NumberOfSidesEnumAttrOperator"]):
    __slots__ = ()

    _3 = 3
    _4 = 4
    _5 = 5


class NumberOfSidesEnumAttrOperator(EnumAttrOperator[NumberOfSidesEnumPlugOperator]):
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


class CreateUVsEnumPlugOperator(EnumPlugOperator["CreateUVsEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    NORMALIZATION_OFF = 1
    NORMALIZE = 2
    NORMALIZE_AND_PRESERVE_ASPECT_RATIO = 3


class CreateUVsEnumAttrOperator(EnumAttrOperator[CreateUVsEnumPlugOperator]):
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


class GeneratedPolyPyramid(DG):
    __slots__ = ()

    NODE_TYPE = "polyPyramid"

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

    sideLength = DoubleLinearField(default_value=1.0, min_value=0.01, soft_max_value=100.0)
    w = sideLength

    numberOfSides = NumberOfSidesEnumField(default_value=4)
    ns = numberOfSides

    subdivisionsHeight = LongField(default_value=1, min_value=1, soft_max_value=50)
    sh = subdivisionsHeight

    subdivisionsCaps = LongField(default_value=0, min_value=0, soft_max_value=50)
    sc = subdivisionsCaps

    texture = BoolField(default_value=True)
    tx = texture

    createUVs = CreateUVsEnumField(default_value=2)
    cuv = createUVs
