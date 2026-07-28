# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class AvoidanceRamp_InterpEnumPlugOperator(
    EnumPlugOperator["AvoidanceRamp_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class AvoidanceRamp_InterpEnumAttrOperator(
    EnumAttrOperator[AvoidanceRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class AvoidanceRamp_InterpEnumField(
    EnumField[
        AvoidanceRamp_InterpEnumAttrOperator,
        AvoidanceRamp_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AvoidanceRamp_InterpEnumAttrOperator
    PLUG_CLS = AvoidanceRamp_InterpEnumPlugOperator


class MColourPlugOperator(
    Float3CompoundBasePlugOperator["MColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mColourR", "mcr"),
        ("mColourG", "mcg"),
        ("mColourB", "mcb"),
    )

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourAttrOperator(Float3CompoundBaseAttrOperator[MColourPlugOperator]):
    __slots__ = ()

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class AvoidanceRampPlugOperator(
    CompoundPlugOperator["AvoidanceRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("avoidanceRamp_Position", "avoidanceRampp"),
        ("avoidanceRamp_FloatValue", "avoidanceRampfv"),
        ("avoidanceRamp_Interp", "avoidanceRampi"),
    )

    avoidanceRamp_Position = FloatField(default_value=0.0)
    avoidanceRampp = avoidanceRamp_Position

    avoidanceRamp_FloatValue = FloatField(default_value=0.0)
    avoidanceRampfv = avoidanceRamp_FloatValue

    avoidanceRamp_Interp = AvoidanceRamp_InterpEnumField(default_value=1)
    avoidanceRampi = avoidanceRamp_Interp


class AvoidanceRampAttrOperator(
    CompoundAttrOperator[AvoidanceRampPlugOperator]
):
    __slots__ = ()

    avoidanceRamp_Position = FloatField(default_value=0.0)
    avoidanceRampp = avoidanceRamp_Position

    avoidanceRamp_FloatValue = FloatField(default_value=0.0)
    avoidanceRampfv = avoidanceRamp_FloatValue

    avoidanceRamp_Interp = AvoidanceRamp_InterpEnumField(default_value=1)
    avoidanceRampi = avoidanceRamp_Interp


class AvoidanceRampField(
    CompoundField[AvoidanceRampAttrOperator, AvoidanceRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AvoidanceRampAttrOperator
    PLUG_CLS = AvoidanceRampPlugOperator


class RandomRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RandomRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("randomRotateX", "randomRotateX"),
        ("randomRotateY", "randomRotateY"),
        ("randomRotateZ", "randomRotateZ"),
    )

    randomRotateX = DoubleAngleField(default_value=0.0)

    randomRotateY = DoubleAngleField(default_value=360.00026887880375)

    randomRotateZ = DoubleAngleField(default_value=0.0)


class RandomRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RandomRotatePlugOperator]
):
    __slots__ = ()

    randomRotateX = DoubleAngleField(default_value=0.0)

    randomRotateY = DoubleAngleField(default_value=360.00026887880375)

    randomRotateZ = DoubleAngleField(default_value=0.0)


class RandomRotateField(
    DoubleAngle3CompoundBaseField[
        RandomRotateAttrOperator, RandomRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RandomRotateAttrOperator
    PLUG_CLS = RandomRotatePlugOperator

    randomRotateX = DoubleAngleField(default_value=0.0)

    randomRotateY = DoubleAngleField(default_value=360.00026887880375)

    randomRotateZ = DoubleAngleField(default_value=0.0)


class ScaleMapPlugOperator(
    Float3CompoundBasePlugOperator["ScaleMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleMapR", "scaleMapr"),
        ("scaleMapG", "scaleMapg"),
        ("scaleMapB", "scaleMapb"),
    )

    scaleMapR = FloatField(default_value=1.0)
    scaleMapr = scaleMapR

    scaleMapG = FloatField(default_value=1.0)
    scaleMapg = scaleMapG

    scaleMapB = FloatField(default_value=1.0)
    scaleMapb = scaleMapB


class ScaleMapAttrOperator(
    Float3CompoundBaseAttrOperator[ScaleMapPlugOperator]
):
    __slots__ = ()

    scaleMapR = FloatField(default_value=1.0)
    scaleMapr = scaleMapR

    scaleMapG = FloatField(default_value=1.0)
    scaleMapg = scaleMapG

    scaleMapB = FloatField(default_value=1.0)
    scaleMapb = scaleMapB


class ScaleMapField(
    Float3CompoundBaseField[ScaleMapAttrOperator, ScaleMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleMapAttrOperator
    PLUG_CLS = ScaleMapPlugOperator

    scaleMapR = FloatField(default_value=1.0)
    scaleMapr = scaleMapR

    scaleMapG = FloatField(default_value=1.0)
    scaleMapg = scaleMapG

    scaleMapB = FloatField(default_value=1.0)
    scaleMapb = scaleMapB


class UpVectorPlugOperator(
    Float3CompoundBasePlugOperator["UpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("upVector0", "upVector0"),
        ("upVector1", "upVector1"),
        ("upVector2", "upVector2"),
    )

    upVector0 = FloatField(default_value=0.0)

    upVector1 = FloatField(default_value=1.0)

    upVector2 = FloatField(default_value=0.0)


class UpVectorAttrOperator(
    Float3CompoundBaseAttrOperator[UpVectorPlugOperator]
):
    __slots__ = ()

    upVector0 = FloatField(default_value=0.0)

    upVector1 = FloatField(default_value=1.0)

    upVector2 = FloatField(default_value=0.0)


class UpVectorField(
    Float3CompoundBaseField[UpVectorAttrOperator, UpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpVectorAttrOperator
    PLUG_CLS = UpVectorPlugOperator

    upVector0 = FloatField(default_value=0.0)

    upVector1 = FloatField(default_value=1.0)

    upVector2 = FloatField(default_value=0.0)


class PruningStrengthMapPlugOperator(
    Float3CompoundBasePlugOperator["PruningStrengthMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pruningStrengthMapR", "pruningStrengthMapr"),
        ("pruningStrengthMapG", "pruningStrengthMapg"),
        ("pruningStrengthMapB", "pruningStrengthMapb"),
    )

    pruningStrengthMapR = FloatField(default_value=1.0)
    pruningStrengthMapr = pruningStrengthMapR

    pruningStrengthMapG = FloatField(default_value=1.0)
    pruningStrengthMapg = pruningStrengthMapG

    pruningStrengthMapB = FloatField(default_value=1.0)
    pruningStrengthMapb = pruningStrengthMapB


class PruningStrengthMapAttrOperator(
    Float3CompoundBaseAttrOperator[PruningStrengthMapPlugOperator]
):
    __slots__ = ()

    pruningStrengthMapR = FloatField(default_value=1.0)
    pruningStrengthMapr = pruningStrengthMapR

    pruningStrengthMapG = FloatField(default_value=1.0)
    pruningStrengthMapg = pruningStrengthMapG

    pruningStrengthMapB = FloatField(default_value=1.0)
    pruningStrengthMapb = pruningStrengthMapB


class PruningStrengthMapField(
    Float3CompoundBaseField[
        PruningStrengthMapAttrOperator, PruningStrengthMapPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PruningStrengthMapAttrOperator
    PLUG_CLS = PruningStrengthMapPlugOperator

    pruningStrengthMapR = FloatField(default_value=1.0)
    pruningStrengthMapr = pruningStrengthMapR

    pruningStrengthMapG = FloatField(default_value=1.0)
    pruningStrengthMapg = pruningStrengthMapG

    pruningStrengthMapB = FloatField(default_value=1.0)
    pruningStrengthMapb = pruningStrengthMapB


class TerrainConditionsMapPlugOperator(
    Float3CompoundBasePlugOperator["TerrainConditionsMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("terrainConditionsMapR", "terrainConditionsMapr"),
        ("terrainConditionsMapG", "terrainConditionsMapg"),
        ("terrainConditionsMapB", "terrainConditionsMapb"),
    )

    terrainConditionsMapR = FloatField(default_value=0.5)
    terrainConditionsMapr = terrainConditionsMapR

    terrainConditionsMapG = FloatField(default_value=0.5)
    terrainConditionsMapg = terrainConditionsMapG

    terrainConditionsMapB = FloatField(default_value=0.5)
    terrainConditionsMapb = terrainConditionsMapB


class TerrainConditionsMapAttrOperator(
    Float3CompoundBaseAttrOperator[TerrainConditionsMapPlugOperator]
):
    __slots__ = ()

    terrainConditionsMapR = FloatField(default_value=0.5)
    terrainConditionsMapr = terrainConditionsMapR

    terrainConditionsMapG = FloatField(default_value=0.5)
    terrainConditionsMapg = terrainConditionsMapG

    terrainConditionsMapB = FloatField(default_value=0.5)
    terrainConditionsMapb = terrainConditionsMapB


class TerrainConditionsMapField(
    Float3CompoundBaseField[
        TerrainConditionsMapAttrOperator, TerrainConditionsMapPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TerrainConditionsMapAttrOperator
    PLUG_CLS = TerrainConditionsMapPlugOperator

    terrainConditionsMapR = FloatField(default_value=0.5)
    terrainConditionsMapr = terrainConditionsMapR

    terrainConditionsMapG = FloatField(default_value=0.5)
    terrainConditionsMapg = terrainConditionsMapG

    terrainConditionsMapB = FloatField(default_value=0.5)
    terrainConditionsMapb = terrainConditionsMapB


class IdMapPlugOperator(Float3CompoundBasePlugOperator["IdMapAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("idMapR", "idMapr"),
        ("idMapG", "idMapg"),
        ("idMapB", "idMapb"),
    )

    idMapR = FloatField(default_value=0.5)
    idMapr = idMapR

    idMapG = FloatField(default_value=0.5)
    idMapg = idMapG

    idMapB = FloatField(default_value=0.5)
    idMapb = idMapB


class IdMapAttrOperator(Float3CompoundBaseAttrOperator[IdMapPlugOperator]):
    __slots__ = ()

    idMapR = FloatField(default_value=0.5)
    idMapr = idMapR

    idMapG = FloatField(default_value=0.5)
    idMapg = idMapG

    idMapB = FloatField(default_value=0.5)
    idMapb = idMapB


class IdMapField(
    Float3CompoundBaseField[IdMapAttrOperator, IdMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdMapAttrOperator
    PLUG_CLS = IdMapPlugOperator

    idMapR = FloatField(default_value=0.5)
    idMapr = idMapR

    idMapG = FloatField(default_value=0.5)
    idMapg = idMapG

    idMapB = FloatField(default_value=0.5)
    idMapb = idMapB


class PoleDirectionPlugOperator(
    Float3CompoundBasePlugOperator["PoleDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("poleDirectionX", "poleDirectionx"),
        ("poleDirectionY", "poleDirectiony"),
        ("poleDirectionZ", "poleDirectionz"),
    )

    poleDirectionX = FloatField(default_value=0.0)
    poleDirectionx = poleDirectionX

    poleDirectionY = FloatField(default_value=0.0)
    poleDirectiony = poleDirectionY

    poleDirectionZ = FloatField(default_value=0.0)
    poleDirectionz = poleDirectionZ


class PoleDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[PoleDirectionPlugOperator]
):
    __slots__ = ()

    poleDirectionX = FloatField(default_value=0.0)
    poleDirectionx = poleDirectionX

    poleDirectionY = FloatField(default_value=0.0)
    poleDirectiony = poleDirectionY

    poleDirectionZ = FloatField(default_value=0.0)
    poleDirectionz = poleDirectionZ


class PoleDirectionField(
    Float3CompoundBaseField[
        PoleDirectionAttrOperator, PoleDirectionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PoleDirectionAttrOperator
    PLUG_CLS = PoleDirectionPlugOperator

    poleDirectionX = FloatField(default_value=0.0)
    poleDirectionx = poleDirectionX

    poleDirectionY = FloatField(default_value=0.0)
    poleDirectiony = poleDirectionY

    poleDirectionZ = FloatField(default_value=0.0)
    poleDirectionz = poleDirectionZ


class TimeRangePlugOperator(
    Float2CompoundBasePlugOperator["TimeRangeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("timeRange0", "timeRange0"),
        ("timeRange1", "timeRange1"),
    )

    timeRange0 = FloatField(default_value=0.0, min_value=0.0)

    timeRange1 = FloatField(default_value=120.0, min_value=0.0)


class TimeRangeAttrOperator(
    Float2CompoundBaseAttrOperator[TimeRangePlugOperator]
):
    __slots__ = ()

    timeRange0 = FloatField(default_value=0.0, min_value=0.0)

    timeRange1 = FloatField(default_value=120.0, min_value=0.0)


class TimeRangeField(
    Float2CompoundBaseField[TimeRangeAttrOperator, TimeRangePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TimeRangeAttrOperator
    PLUG_CLS = TimeRangePlugOperator

    timeRange0 = FloatField(default_value=0.0, min_value=0.0)

    timeRange1 = FloatField(default_value=120.0, min_value=0.0)
