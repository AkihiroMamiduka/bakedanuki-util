# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_axis import AxisField
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


class GeneratedPolyAxis(DG):
    __slots__ = ()

    NODE_TYPE = "polyAxis"

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

    frameType = FrameTypeEnumField(default_value=0)
    ftp = frameType

    scale = DoubleLinearField(default_value=1.0, min_value=0.01, soft_max_value=100.0)
    sca = scale

    radius = DoubleLinearField(default_value=0.05, min_value=0.001, soft_max_value=100.0)
    r = radius

    lengthX = DoubleLinearField(default_value=1.0, min_value=0.01, soft_max_value=100.0)
    lx = lengthX

    lengthY = DoubleLinearField(default_value=1.0, min_value=0.01, soft_max_value=100.0)
    ly = lengthY

    lengthZ = DoubleLinearField(default_value=1.0, min_value=0.01, soft_max_value=100.0)
    lz = lengthZ

    arrowType = ArrowTypeEnumField(default_value=1)
    arw = arrowType

    subdivisionsAxis = LongField(default_value=10, min_value=3, soft_max_value=50)
    sa = subdivisionsAxis

    rightHanded = BoolField(default_value=True)
    rhd = rightHanded
