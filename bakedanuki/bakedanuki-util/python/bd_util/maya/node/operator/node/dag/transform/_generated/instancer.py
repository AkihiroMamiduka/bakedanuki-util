# coding: utf-8
from .._core import Transform
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.matrix import DataMatrixField


class RotationOrderEnumPlugOperator(
    EnumPlugOperator["RotationOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    XZY = 1
    YXZ = 2
    YZX = 3
    ZXY = 4
    ZYX = 5


class RotationOrderEnumAttrOperator(
    EnumAttrOperator[RotationOrderEnumPlugOperator]
):
    __slots__ = ()

    XYZ = 0
    XZY = 1
    YXZ = 2
    YZX = 3
    ZXY = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "XYZ",
        XZY: "XZY",
        YXZ: "YXZ",
        YZX: "YZX",
        ZXY: "ZXY",
        ZYX: "ZYX",
    }


class RotationOrderEnumField(
    EnumField[RotationOrderEnumAttrOperator, RotationOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationOrderEnumAttrOperator
    PLUG_CLS = RotationOrderEnumPlugOperator


class RotationAngleUnitsEnumPlugOperator(
    EnumPlugOperator["RotationAngleUnitsEnumAttrOperator"]
):
    __slots__ = ()

    DEGREES = 0
    RADIANS = 1


class RotationAngleUnitsEnumAttrOperator(
    EnumAttrOperator[RotationAngleUnitsEnumPlugOperator]
):
    __slots__ = ()

    DEGREES = 0
    RADIANS = 1

    NAME_MAP = {
        DEGREES: "Degrees",
        RADIANS: "Radians",
    }


class RotationAngleUnitsEnumField(
    EnumField[
        RotationAngleUnitsEnumAttrOperator, RotationAngleUnitsEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RotationAngleUnitsEnumAttrOperator
    PLUG_CLS = RotationAngleUnitsEnumPlugOperator


class CycleEnumPlugOperator(EnumPlugOperator["CycleEnumAttrOperator"]):
    __slots__ = ()

    NONE = 0
    SEQUENTIAL = 1


class CycleEnumAttrOperator(EnumAttrOperator[CycleEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    SEQUENTIAL = 1

    NAME_MAP = {
        NONE: "None",
        SEQUENTIAL: "Sequential",
    }


class CycleEnumField(EnumField[CycleEnumAttrOperator, CycleEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = CycleEnumAttrOperator
    PLUG_CLS = CycleEnumPlugOperator


class CycleStepUnitEnumPlugOperator(
    EnumPlugOperator["CycleStepUnitEnumAttrOperator"]
):
    __slots__ = ()

    FRAMES = 0
    SECONDS = 1


class CycleStepUnitEnumAttrOperator(
    EnumAttrOperator[CycleStepUnitEnumPlugOperator]
):
    __slots__ = ()

    FRAMES = 0
    SECONDS = 1

    NAME_MAP = {
        FRAMES: "Frames",
        SECONDS: "Seconds",
    }


class CycleStepUnitEnumField(
    EnumField[CycleStepUnitEnumAttrOperator, CycleStepUnitEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CycleStepUnitEnumAttrOperator
    PLUG_CLS = CycleStepUnitEnumPlugOperator


class LevelOfDetailEnumPlugOperator(
    EnumPlugOperator["LevelOfDetailEnumAttrOperator"]
):
    __slots__ = ()

    GEOMETRY = 0
    BOUNDINGBOXES = 1
    BOUNDINGBOX = 2


class LevelOfDetailEnumAttrOperator(
    EnumAttrOperator[LevelOfDetailEnumPlugOperator]
):
    __slots__ = ()

    GEOMETRY = 0
    BOUNDINGBOXES = 1
    BOUNDINGBOX = 2

    NAME_MAP = {
        GEOMETRY: "Geometry",
        BOUNDINGBOXES: "BoundingBoxes",
        BOUNDINGBOX: "BoundingBox",
    }


class LevelOfDetailEnumField(
    EnumField[LevelOfDetailEnumAttrOperator, LevelOfDetailEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LevelOfDetailEnumAttrOperator
    PLUG_CLS = LevelOfDetailEnumPlugOperator


class GeneratedInstancer(Transform):
    __slots__ = ()

    NODE_TYPE = "instancer"

    inputPoints = TypedField()
    inp = inputPoints

    inputHierarchy = DataMatrixField(multi=True, readable=False)
    inh = inputHierarchy

    rotationOrder = RotationOrderEnumField(default_value=0)
    ror = rotationOrder

    rotationAngleUnits = RotationAngleUnitsEnumField(default_value=0)
    rau = rotationAngleUnits

    cycle = CycleEnumField(default_value=0)
    cyc = cycle

    cycleStep = DoubleField(default_value=1.0)
    cs = cycleStep

    cycleStepUnit = CycleStepUnitEnumField(default_value=0)
    csu = cycleStepUnit

    displayPercentage = DoubleField(
        default_value=100.0,
        min_value=0.0,
        max_value=100.0,
        soft_min_value=0.0,
        soft_max_value=100.0,
    )
    dp = displayPercentage

    levelOfDetail = LevelOfDetailEnumField(default_value=0)
    lod = levelOfDetail

    instanceCount = LongField(default_value=0, writable=False)
    ic = instanceCount

    fillArray = BoolField(default_value=False, readable=False, writable=False)
    fa = fillArray

    hierarchyCount = LongField(default_value=0, writable=False)
    hc = hierarchyCount
