# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.mesh import DataMeshField


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


class _GeneratedPolySuperShape(DG):
    __slots__ = ()

    NODE_TYPE = "polySuperShape"

    output = DataMeshField(writable=False)

    radius = FloatField(default_value=1.0, min_value=0.001, soft_max_value=100.0)

    heightBaseline = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)

    shape = ShapeEnumField(default_value=0)

    uvMode = UvModeEnumField(default_value=2)

    ellipse0 = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)

    ellipse1 = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)

    harmonics0 = FloatField(default_value=0.0, soft_min_value=-20.0, soft_max_value=20.0)

    harmonics1 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)

    harmonics2 = FloatField(default_value=0.0, soft_min_value=-20.0, soft_max_value=20.0)

    harmonics3 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)

    harmonics4 = FloatField(default_value=0.0, soft_min_value=-20.0, soft_max_value=20.0)

    harmonics5 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)

    harmonics6 = FloatField(default_value=0.0, soft_min_value=-20.0, soft_max_value=20.0)

    harmonics7 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)

    ultra0 = FloatField(default_value=0.0, soft_min_value=-30.0, soft_max_value=30.0)

    ultra1 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)

    ultra2 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)

    ultra3 = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)

    ultra4 = FloatField(default_value=0.0, soft_min_value=-30.0, soft_max_value=30.0)

    ultra5 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)

    ultra6 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)

    ultra7 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)

    ultra8 = FloatField(default_value=0.0, soft_min_value=-30.0, soft_max_value=30.0)

    ultra9 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)

    ultra10 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)

    ultra11 = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)

    ultra12 = FloatField(default_value=0.0, soft_min_value=-30.0, soft_max_value=30.0)

    ultra13 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)

    ultra14 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)

    ultra15 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=4.0)

    ellipseMirror = BoolField(default_value=True)

    ultraMirror = BoolField(default_value=False)

    horizontalDivisions = LongField(default_value=16, min_value=1, soft_max_value=40)

    verticalDivisions = LongField(default_value=16, min_value=1, soft_max_value=40)

    mergeVertices = BoolField(default_value=True)

    horizontalRevolutions = FloatField(default_value=1.0, min_value=0.0, soft_max_value=20.0)

    verticalRevolutions = FloatField(default_value=1.0, min_value=0.0, soft_max_value=20.0)

    verticalOffset = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    internalRadius = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    xOffset = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    zOffset = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)
