# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.unit_scalar.time import TimeField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class FalloffCurve_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class FalloffCurve_InterpEnumAttrOperator(EnumAttrOperator):
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


class FalloffCurve_InterpEnumField(
    EnumField[FalloffCurve_InterpEnumAttrOperator, FalloffCurve_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffCurve_InterpEnumAttrOperator
    PLUG_CLS = FalloffCurve_InterpEnumPlugOperator


class AxialMagnitude_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class AxialMagnitude_InterpEnumAttrOperator(EnumAttrOperator):
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


class AxialMagnitude_InterpEnumField(
    EnumField[AxialMagnitude_InterpEnumAttrOperator, AxialMagnitude_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxialMagnitude_InterpEnumAttrOperator
    PLUG_CLS = AxialMagnitude_InterpEnumPlugOperator


class CurveRadius_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CurveRadius_InterpEnumAttrOperator(EnumAttrOperator):
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


class CurveRadius_InterpEnumField(
    EnumField[CurveRadius_InterpEnumAttrOperator, CurveRadius_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurveRadius_InterpEnumAttrOperator
    PLUG_CLS = CurveRadius_InterpEnumPlugOperator


class OwnerCentroidPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OwnerCentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ownerCentroidX", "ocx"),
        ("ownerCentroidY", "ocy"),
        ("ownerCentroidZ", "ocz"),
    )

    ownerCentroidX = DoubleLinearField(default_value=0.0)
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField(default_value=0.0)
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField(default_value=0.0)
    ocz = ownerCentroidZ


class OwnerCentroidAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OwnerCentroidPlugOperator]
):
    __slots__ = ()

    ownerCentroidX = DoubleLinearField(default_value=0.0)
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField(default_value=0.0)
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField(default_value=0.0)
    ocz = ownerCentroidZ


class OwnerCentroidField(
    DoubleLinear3CompoundBaseField[OwnerCentroidAttrOperator, OwnerCentroidPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OwnerCentroidAttrOperator
    PLUG_CLS = OwnerCentroidPlugOperator

    ownerCentroidX = DoubleLinearField(default_value=0.0)
    ocx = ownerCentroidX

    ownerCentroidY = DoubleLinearField(default_value=0.0)
    ocy = ownerCentroidY

    ownerCentroidZ = DoubleLinearField(default_value=0.0)
    ocz = ownerCentroidZ


class InputDataPlugOperator(
    CompoundPlugOperator["InputDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputPositions", "inp"),
        ("inputVelocities", "inv"),
        ("inputMass", "inm"),
        ("deltaTime", "dt"),
    )

    inputPositions = DataVectorArrayField()
    inp = inputPositions

    inputVelocities = DataVectorArrayField()
    inv = inputVelocities

    inputMass = DataDoubleArrayField()
    inm = inputMass

    deltaTime = TimeField(default_value=0.0)
    dt = deltaTime


class InputDataAttrOperator(
    CompoundAttrOperator[InputDataPlugOperator]
):
    __slots__ = ()

    inputPositions = DataVectorArrayField()
    inp = inputPositions

    inputVelocities = DataVectorArrayField()
    inv = inputVelocities

    inputMass = DataDoubleArrayField()
    inm = inputMass

    deltaTime = TimeField(default_value=0.0)
    dt = deltaTime


class InputDataField(
    CompoundField[InputDataAttrOperator, InputDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputDataAttrOperator
    PLUG_CLS = InputDataPlugOperator


class VolumeOffsetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["VolumeOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("volumeOffsetX", "vox"),
        ("volumeOffsetY", "voy"),
        ("volumeOffsetZ", "voz"),
    )

    volumeOffsetX = DoubleLinearField(default_value=0.0)
    vox = volumeOffsetX

    volumeOffsetY = DoubleLinearField(default_value=0.0)
    voy = volumeOffsetY

    volumeOffsetZ = DoubleLinearField(default_value=0.0)
    voz = volumeOffsetZ


class VolumeOffsetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[VolumeOffsetPlugOperator]
):
    __slots__ = ()

    volumeOffsetX = DoubleLinearField(default_value=0.0)
    vox = volumeOffsetX

    volumeOffsetY = DoubleLinearField(default_value=0.0)
    voy = volumeOffsetY

    volumeOffsetZ = DoubleLinearField(default_value=0.0)
    voz = volumeOffsetZ


class VolumeOffsetField(
    DoubleLinear3CompoundBaseField[VolumeOffsetAttrOperator, VolumeOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VolumeOffsetAttrOperator
    PLUG_CLS = VolumeOffsetPlugOperator

    volumeOffsetX = DoubleLinearField(default_value=0.0)
    vox = volumeOffsetX

    volumeOffsetY = DoubleLinearField(default_value=0.0)
    voy = volumeOffsetY

    volumeOffsetZ = DoubleLinearField(default_value=0.0)
    voz = volumeOffsetZ


class FalloffCurvePlugOperator(
    CompoundPlugOperator["FalloffCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffCurve_Position", "fcp"),
        ("falloffCurve_FloatValue", "fcfv"),
        ("falloffCurve_Interp", "fci"),
    )

    falloffCurve_Position = FloatField(default_value=0.0)
    fcp = falloffCurve_Position

    falloffCurve_FloatValue = FloatField(default_value=0.0)
    fcfv = falloffCurve_FloatValue

    falloffCurve_Interp = FalloffCurve_InterpEnumField(default_value=0)
    fci = falloffCurve_Interp


class FalloffCurveAttrOperator(
    CompoundAttrOperator[FalloffCurvePlugOperator]
):
    __slots__ = ()

    falloffCurve_Position = FloatField(default_value=0.0)
    fcp = falloffCurve_Position

    falloffCurve_FloatValue = FloatField(default_value=0.0)
    fcfv = falloffCurve_FloatValue

    falloffCurve_Interp = FalloffCurve_InterpEnumField(default_value=0)
    fci = falloffCurve_Interp


class FalloffCurveField(
    CompoundField[FalloffCurveAttrOperator, FalloffCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffCurveAttrOperator
    PLUG_CLS = FalloffCurvePlugOperator


class AxialMagnitudePlugOperator(
    CompoundPlugOperator["AxialMagnitudeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axialMagnitude_Position", "amagp"),
        ("axialMagnitude_FloatValue", "amagfv"),
        ("axialMagnitude_Interp", "amagi"),
    )

    axialMagnitude_Position = FloatField(default_value=0.0)
    amagp = axialMagnitude_Position

    axialMagnitude_FloatValue = FloatField(default_value=0.0)
    amagfv = axialMagnitude_FloatValue

    axialMagnitude_Interp = AxialMagnitude_InterpEnumField(default_value=0)
    amagi = axialMagnitude_Interp


class AxialMagnitudeAttrOperator(
    CompoundAttrOperator[AxialMagnitudePlugOperator]
):
    __slots__ = ()

    axialMagnitude_Position = FloatField(default_value=0.0)
    amagp = axialMagnitude_Position

    axialMagnitude_FloatValue = FloatField(default_value=0.0)
    amagfv = axialMagnitude_FloatValue

    axialMagnitude_Interp = AxialMagnitude_InterpEnumField(default_value=0)
    amagi = axialMagnitude_Interp


class AxialMagnitudeField(
    CompoundField[AxialMagnitudeAttrOperator, AxialMagnitudePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxialMagnitudeAttrOperator
    PLUG_CLS = AxialMagnitudePlugOperator


class CurveRadiusPlugOperator(
    CompoundPlugOperator["CurveRadiusAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("curveRadius_Position", "cradp"),
        ("curveRadius_FloatValue", "cradfv"),
        ("curveRadius_Interp", "cradi"),
    )

    curveRadius_Position = FloatField(default_value=0.0)
    cradp = curveRadius_Position

    curveRadius_FloatValue = FloatField(default_value=0.0)
    cradfv = curveRadius_FloatValue

    curveRadius_Interp = CurveRadius_InterpEnumField(default_value=0)
    cradi = curveRadius_Interp


class CurveRadiusAttrOperator(
    CompoundAttrOperator[CurveRadiusPlugOperator]
):
    __slots__ = ()

    curveRadius_Position = FloatField(default_value=0.0)
    cradp = curveRadius_Position

    curveRadius_FloatValue = FloatField(default_value=0.0)
    cradfv = curveRadius_FloatValue

    curveRadius_Interp = CurveRadius_InterpEnumField(default_value=0)
    cradi = curveRadius_Interp


class CurveRadiusField(
    CompoundField[CurveRadiusAttrOperator, CurveRadiusPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurveRadiusAttrOperator
    PLUG_CLS = CurveRadiusPlugOperator


class DirectionPlugOperator(
    Double3CompoundBasePlugOperator["DirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("directionX", "dx"),
        ("directionY", "dy"),
        ("directionZ", "dz"),
    )

    directionX = DoubleField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    dx = directionX

    directionY = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    dy = directionY

    directionZ = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    dz = directionZ


class DirectionAttrOperator(
    Double3CompoundBaseAttrOperator[DirectionPlugOperator]
):
    __slots__ = ()

    directionX = DoubleField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    dx = directionX

    directionY = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    dy = directionY

    directionZ = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    dz = directionZ


class DirectionField(
    Double3CompoundBaseField[DirectionAttrOperator, DirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionAttrOperator
    PLUG_CLS = DirectionPlugOperator

    directionX = DoubleField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    dx = directionX

    directionY = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    dy = directionY

    directionZ = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    dz = directionZ


class TurbulenceFrequencyPlugOperator(
    Double3CompoundBasePlugOperator["TurbulenceFrequencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("turbulenceFrequencyX", "tfx"),
        ("turbulenceFrequencyY", "tfy"),
        ("turbulenceFrequencyZ", "tfz"),
    )

    turbulenceFrequencyX = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    tfx = turbulenceFrequencyX

    turbulenceFrequencyY = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    tfy = turbulenceFrequencyY

    turbulenceFrequencyZ = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    tfz = turbulenceFrequencyZ


class TurbulenceFrequencyAttrOperator(
    Double3CompoundBaseAttrOperator[TurbulenceFrequencyPlugOperator]
):
    __slots__ = ()

    turbulenceFrequencyX = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    tfx = turbulenceFrequencyX

    turbulenceFrequencyY = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    tfy = turbulenceFrequencyY

    turbulenceFrequencyZ = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    tfz = turbulenceFrequencyZ


class TurbulenceFrequencyField(
    Double3CompoundBaseField[TurbulenceFrequencyAttrOperator, TurbulenceFrequencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TurbulenceFrequencyAttrOperator
    PLUG_CLS = TurbulenceFrequencyPlugOperator

    turbulenceFrequencyX = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    tfx = turbulenceFrequencyX

    turbulenceFrequencyY = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    tfy = turbulenceFrequencyY

    turbulenceFrequencyZ = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    tfz = turbulenceFrequencyZ


class TurbulenceOffsetPlugOperator(
    Double3CompoundBasePlugOperator["TurbulenceOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("turbulenceOffsetX", "tox"),
        ("turbulenceOffsetY", "toy"),
        ("turbulenceOffsetZ", "toz"),
    )

    turbulenceOffsetX = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    tox = turbulenceOffsetX

    turbulenceOffsetY = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toy = turbulenceOffsetY

    turbulenceOffsetZ = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toz = turbulenceOffsetZ


class TurbulenceOffsetAttrOperator(
    Double3CompoundBaseAttrOperator[TurbulenceOffsetPlugOperator]
):
    __slots__ = ()

    turbulenceOffsetX = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    tox = turbulenceOffsetX

    turbulenceOffsetY = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toy = turbulenceOffsetY

    turbulenceOffsetZ = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toz = turbulenceOffsetZ


class TurbulenceOffsetField(
    Double3CompoundBaseField[TurbulenceOffsetAttrOperator, TurbulenceOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TurbulenceOffsetAttrOperator
    PLUG_CLS = TurbulenceOffsetPlugOperator

    turbulenceOffsetX = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    tox = turbulenceOffsetX

    turbulenceOffsetY = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toy = turbulenceOffsetY

    turbulenceOffsetZ = DoubleField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    toz = turbulenceOffsetZ
