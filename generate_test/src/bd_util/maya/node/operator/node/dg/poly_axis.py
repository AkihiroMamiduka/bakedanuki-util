# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_axis import AxisField
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


class FrameTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AXIS = 0
    WEDGE = 1
    LOCATOR = 2


class FrameTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AXIS = 0
    WEDGE = 1
    LOCATOR = 2

    NAME_MAP = {
        AXIS: "Axis",
        WEDGE: "Wedge",
        LOCATOR: "Locator",
    }


class FrameTypeEnumField(
    EnumField[FrameTypeEnumAttrOperator, FrameTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrameTypeEnumAttrOperator
    PLUG_CLS = FrameTypeEnumPlugOperator


class ArrowTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    ROUNDED = 1
    CONE = 2


class ArrowTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    ROUNDED = 1
    CONE = 2

    NAME_MAP = {
        NONE: "None",
        ROUNDED: "Rounded",
        CONE: "Cone",
    }


class ArrowTypeEnumField(
    EnumField[ArrowTypeEnumAttrOperator, ArrowTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ArrowTypeEnumAttrOperator
    PLUG_CLS = ArrowTypeEnumPlugOperator


class PolyAxis(DG):
    __slots__ = ()

    NODE_TYPE = "polyAxis"

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

    frameType = FrameTypeEnumField()
    ftp = frameType

    scale = DoubleLinearField()
    sca = scale

    radius = DoubleLinearField()
    r = radius

    lengthX = DoubleLinearField()
    lx = lengthX

    lengthY = DoubleLinearField()
    ly = lengthY

    lengthZ = DoubleLinearField()
    lz = lengthZ

    arrowType = ArrowTypeEnumField()
    arw = arrowType

    subdivisionsAxis = LongField()
    sa = subdivisionsAxis

    rightHanded = BoolField()
    rhd = rightHanded
