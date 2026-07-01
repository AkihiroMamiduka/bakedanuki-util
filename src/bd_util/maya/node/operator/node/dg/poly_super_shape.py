# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.mesh import DataMeshField


class ShapeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SUPER_ELLIPSE = 0
    SPHERICAL_HARMONICS = 1
    ULTRA = 2


class ShapeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SUPER_ELLIPSE = 0
    SPHERICAL_HARMONICS = 1
    ULTRA = 2

    NAME_MAP = {
        SUPER_ELLIPSE: "Super Ellipse",
        SPHERICAL_HARMONICS: "Spherical Harmonics",
        ULTRA: "Ultra",
    }


class ShapeEnumField(
    EnumField[ShapeEnumAttrOperator, ShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShapeEnumAttrOperator
    PLUG_CLS = ShapeEnumPlugOperator


class UvModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PINCHED_AT_POLE = 1
    SAWTOOTH_AT_POLE = 2


class UvModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    PINCHED_AT_POLE = 1
    SAWTOOTH_AT_POLE = 2

    NAME_MAP = {
        NONE: "None",
        PINCHED_AT_POLE: "Pinched at pole",
        SAWTOOTH_AT_POLE: "Sawtooth at pole",
    }


class UvModeEnumField(
    EnumField[UvModeEnumAttrOperator, UvModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvModeEnumAttrOperator
    PLUG_CLS = UvModeEnumPlugOperator


class PolySuperShape(DG):
    __slots__ = ()

    NODE_TYPE = "polySuperShape"

    output = DataMeshField()

    radius = FloatField()

    heightBaseline = FloatField()

    shape = ShapeEnumField()

    uvMode = UvModeEnumField()

    ellipse0 = FloatField()

    ellipse1 = FloatField()

    harmonics0 = FloatField()

    harmonics1 = FloatField()

    harmonics2 = FloatField()

    harmonics3 = FloatField()

    harmonics4 = FloatField()

    harmonics5 = FloatField()

    harmonics6 = FloatField()

    harmonics7 = FloatField()

    ultra0 = FloatField()

    ultra1 = FloatField()

    ultra2 = FloatField()

    ultra3 = FloatField()

    ultra4 = FloatField()

    ultra5 = FloatField()

    ultra6 = FloatField()

    ultra7 = FloatField()

    ultra8 = FloatField()

    ultra9 = FloatField()

    ultra10 = FloatField()

    ultra11 = FloatField()

    ultra12 = FloatField()

    ultra13 = FloatField()

    ultra14 = FloatField()

    ultra15 = FloatField()

    ellipseMirror = BoolField()

    ultraMirror = BoolField()

    horizontalDivisions = LongField()

    verticalDivisions = LongField()

    mergeVertices = BoolField()

    horizontalRevolutions = FloatField()

    verticalRevolutions = FloatField()

    verticalOffset = FloatField()

    internalRadius = FloatField()

    xOffset = FloatField()

    zOffset = FloatField()
