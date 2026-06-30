# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
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


class MColourPlugOperator(
    Float3CompoundBasePlugOperator["MColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mColourR", "mcr"),
        ("mColourG", "mcg"),
        ("mColourB", "mcb"),
    )

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourAttrOperator(
    Float3CompoundBaseAttrOperator[MColourPlugOperator]
):
    __slots__ = ()

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
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

    avoidanceRamp_Position = FloatField()
    avoidanceRampp = avoidanceRamp_Position

    avoidanceRamp_FloatValue = FloatField()
    avoidanceRampfv = avoidanceRamp_FloatValue

    avoidanceRamp_Interp = EnumField()
    avoidanceRampi = avoidanceRamp_Interp


class AvoidanceRampAttrOperator(
    CompoundAttrOperator[AvoidanceRampPlugOperator]
):
    __slots__ = ()

    avoidanceRamp_Position = FloatField()
    avoidanceRampp = avoidanceRamp_Position

    avoidanceRamp_FloatValue = FloatField()
    avoidanceRampfv = avoidanceRamp_FloatValue

    avoidanceRamp_Interp = EnumField()
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

    randomRotateX = DoubleAngleField()

    randomRotateY = DoubleAngleField()

    randomRotateZ = DoubleAngleField()


class RandomRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RandomRotatePlugOperator]
):
    __slots__ = ()

    randomRotateX = DoubleAngleField()

    randomRotateY = DoubleAngleField()

    randomRotateZ = DoubleAngleField()


class RandomRotateField(
    DoubleAngle3CompoundBaseField[RandomRotateAttrOperator, RandomRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RandomRotateAttrOperator
    PLUG_CLS = RandomRotatePlugOperator

    randomRotateX = DoubleAngleField()

    randomRotateY = DoubleAngleField()

    randomRotateZ = DoubleAngleField()


class ScaleMapPlugOperator(
    Float3CompoundBasePlugOperator["ScaleMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleMapR", "scaleMapr"),
        ("scaleMapG", "scaleMapg"),
        ("scaleMapB", "scaleMapb"),
    )

    scaleMapR = FloatField()
    scaleMapr = scaleMapR

    scaleMapG = FloatField()
    scaleMapg = scaleMapG

    scaleMapB = FloatField()
    scaleMapb = scaleMapB


class ScaleMapAttrOperator(
    Float3CompoundBaseAttrOperator[ScaleMapPlugOperator]
):
    __slots__ = ()

    scaleMapR = FloatField()
    scaleMapr = scaleMapR

    scaleMapG = FloatField()
    scaleMapg = scaleMapG

    scaleMapB = FloatField()
    scaleMapb = scaleMapB


class ScaleMapField(
    Float3CompoundBaseField[ScaleMapAttrOperator, ScaleMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleMapAttrOperator
    PLUG_CLS = ScaleMapPlugOperator

    scaleMapR = FloatField()
    scaleMapr = scaleMapR

    scaleMapG = FloatField()
    scaleMapg = scaleMapG

    scaleMapB = FloatField()
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

    upVector0 = FloatField()

    upVector1 = FloatField()

    upVector2 = FloatField()


class UpVectorAttrOperator(
    Float3CompoundBaseAttrOperator[UpVectorPlugOperator]
):
    __slots__ = ()

    upVector0 = FloatField()

    upVector1 = FloatField()

    upVector2 = FloatField()


class UpVectorField(
    Float3CompoundBaseField[UpVectorAttrOperator, UpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpVectorAttrOperator
    PLUG_CLS = UpVectorPlugOperator

    upVector0 = FloatField()

    upVector1 = FloatField()

    upVector2 = FloatField()


class PruningStrengthMapPlugOperator(
    Float3CompoundBasePlugOperator["PruningStrengthMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pruningStrengthMapR", "pruningStrengthMapr"),
        ("pruningStrengthMapG", "pruningStrengthMapg"),
        ("pruningStrengthMapB", "pruningStrengthMapb"),
    )

    pruningStrengthMapR = FloatField()
    pruningStrengthMapr = pruningStrengthMapR

    pruningStrengthMapG = FloatField()
    pruningStrengthMapg = pruningStrengthMapG

    pruningStrengthMapB = FloatField()
    pruningStrengthMapb = pruningStrengthMapB


class PruningStrengthMapAttrOperator(
    Float3CompoundBaseAttrOperator[PruningStrengthMapPlugOperator]
):
    __slots__ = ()

    pruningStrengthMapR = FloatField()
    pruningStrengthMapr = pruningStrengthMapR

    pruningStrengthMapG = FloatField()
    pruningStrengthMapg = pruningStrengthMapG

    pruningStrengthMapB = FloatField()
    pruningStrengthMapb = pruningStrengthMapB


class PruningStrengthMapField(
    Float3CompoundBaseField[PruningStrengthMapAttrOperator, PruningStrengthMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PruningStrengthMapAttrOperator
    PLUG_CLS = PruningStrengthMapPlugOperator

    pruningStrengthMapR = FloatField()
    pruningStrengthMapr = pruningStrengthMapR

    pruningStrengthMapG = FloatField()
    pruningStrengthMapg = pruningStrengthMapG

    pruningStrengthMapB = FloatField()
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

    terrainConditionsMapR = FloatField()
    terrainConditionsMapr = terrainConditionsMapR

    terrainConditionsMapG = FloatField()
    terrainConditionsMapg = terrainConditionsMapG

    terrainConditionsMapB = FloatField()
    terrainConditionsMapb = terrainConditionsMapB


class TerrainConditionsMapAttrOperator(
    Float3CompoundBaseAttrOperator[TerrainConditionsMapPlugOperator]
):
    __slots__ = ()

    terrainConditionsMapR = FloatField()
    terrainConditionsMapr = terrainConditionsMapR

    terrainConditionsMapG = FloatField()
    terrainConditionsMapg = terrainConditionsMapG

    terrainConditionsMapB = FloatField()
    terrainConditionsMapb = terrainConditionsMapB


class TerrainConditionsMapField(
    Float3CompoundBaseField[TerrainConditionsMapAttrOperator, TerrainConditionsMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TerrainConditionsMapAttrOperator
    PLUG_CLS = TerrainConditionsMapPlugOperator

    terrainConditionsMapR = FloatField()
    terrainConditionsMapr = terrainConditionsMapR

    terrainConditionsMapG = FloatField()
    terrainConditionsMapg = terrainConditionsMapG

    terrainConditionsMapB = FloatField()
    terrainConditionsMapb = terrainConditionsMapB


class IdMapPlugOperator(
    Float3CompoundBasePlugOperator["IdMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("idMapR", "idMapr"),
        ("idMapG", "idMapg"),
        ("idMapB", "idMapb"),
    )

    idMapR = FloatField()
    idMapr = idMapR

    idMapG = FloatField()
    idMapg = idMapG

    idMapB = FloatField()
    idMapb = idMapB


class IdMapAttrOperator(
    Float3CompoundBaseAttrOperator[IdMapPlugOperator]
):
    __slots__ = ()

    idMapR = FloatField()
    idMapr = idMapR

    idMapG = FloatField()
    idMapg = idMapG

    idMapB = FloatField()
    idMapb = idMapB


class IdMapField(
    Float3CompoundBaseField[IdMapAttrOperator, IdMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdMapAttrOperator
    PLUG_CLS = IdMapPlugOperator

    idMapR = FloatField()
    idMapr = idMapR

    idMapG = FloatField()
    idMapg = idMapG

    idMapB = FloatField()
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

    poleDirectionX = FloatField()
    poleDirectionx = poleDirectionX

    poleDirectionY = FloatField()
    poleDirectiony = poleDirectionY

    poleDirectionZ = FloatField()
    poleDirectionz = poleDirectionZ


class PoleDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[PoleDirectionPlugOperator]
):
    __slots__ = ()

    poleDirectionX = FloatField()
    poleDirectionx = poleDirectionX

    poleDirectionY = FloatField()
    poleDirectiony = poleDirectionY

    poleDirectionZ = FloatField()
    poleDirectionz = poleDirectionZ


class PoleDirectionField(
    Float3CompoundBaseField[PoleDirectionAttrOperator, PoleDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PoleDirectionAttrOperator
    PLUG_CLS = PoleDirectionPlugOperator

    poleDirectionX = FloatField()
    poleDirectionx = poleDirectionX

    poleDirectionY = FloatField()
    poleDirectiony = poleDirectionY

    poleDirectionZ = FloatField()
    poleDirectionz = poleDirectionZ


class TimeRangePlugOperator(
    Float2CompoundBasePlugOperator["TimeRangeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("timeRange0", "timeRange0"),
        ("timeRange1", "timeRange1"),
    )

    timeRange0 = FloatField()

    timeRange1 = FloatField()


class TimeRangeAttrOperator(
    Float2CompoundBaseAttrOperator[TimeRangePlugOperator]
):
    __slots__ = ()

    timeRange0 = FloatField()

    timeRange1 = FloatField()


class TimeRangeField(
    Float2CompoundBaseField[TimeRangeAttrOperator, TimeRangePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TimeRangeAttrOperator
    PLUG_CLS = TimeRangePlugOperator

    timeRange0 = FloatField()

    timeRange1 = FloatField()
