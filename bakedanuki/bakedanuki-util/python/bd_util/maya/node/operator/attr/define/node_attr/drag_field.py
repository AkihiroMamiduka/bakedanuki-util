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
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.scalar.unit.time import TimeField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class FalloffCurve_falloffCurve_InterpEnumPlugOperator(
    EnumPlugOperator["FalloffCurve_falloffCurve_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class FalloffCurve_falloffCurve_InterpEnumAttrOperator(
    EnumAttrOperator[FalloffCurve_falloffCurve_InterpEnumPlugOperator]
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


class FalloffCurve_falloffCurve_InterpEnumField(
    EnumField[
        FalloffCurve_falloffCurve_InterpEnumAttrOperator,
        FalloffCurve_falloffCurve_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FalloffCurve_falloffCurve_InterpEnumAttrOperator
    PLUG_CLS = FalloffCurve_falloffCurve_InterpEnumPlugOperator


class AxialMagnitude_axialMagnitude_InterpEnumPlugOperator(
    EnumPlugOperator["AxialMagnitude_axialMagnitude_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class AxialMagnitude_axialMagnitude_InterpEnumAttrOperator(
    EnumAttrOperator[AxialMagnitude_axialMagnitude_InterpEnumPlugOperator]
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


class AxialMagnitude_axialMagnitude_InterpEnumField(
    EnumField[
        AxialMagnitude_axialMagnitude_InterpEnumAttrOperator,
        AxialMagnitude_axialMagnitude_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AxialMagnitude_axialMagnitude_InterpEnumAttrOperator
    PLUG_CLS = AxialMagnitude_axialMagnitude_InterpEnumPlugOperator


class CurveRadius_curveRadius_InterpEnumPlugOperator(
    EnumPlugOperator["CurveRadius_curveRadius_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CurveRadius_curveRadius_InterpEnumAttrOperator(
    EnumAttrOperator[CurveRadius_curveRadius_InterpEnumPlugOperator]
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


class CurveRadius_curveRadius_InterpEnumField(
    EnumField[
        CurveRadius_curveRadius_InterpEnumAttrOperator,
        CurveRadius_curveRadius_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CurveRadius_curveRadius_InterpEnumAttrOperator
    PLUG_CLS = CurveRadius_curveRadius_InterpEnumPlugOperator


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
    DoubleLinear3CompoundBaseField[
        OwnerCentroidAttrOperator, OwnerCentroidPlugOperator
    ]
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


class InputDataPlugOperator(CompoundPlugOperator["InputDataAttrOperator"]):
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


class InputDataAttrOperator(CompoundAttrOperator[InputDataPlugOperator]):
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
    DoubleLinear3CompoundBaseField[
        VolumeOffsetAttrOperator, VolumeOffsetPlugOperator
    ]
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

    falloffCurve_Interp = FalloffCurve_falloffCurve_InterpEnumField(
        default_value=0
    )
    fci = falloffCurve_Interp


class FalloffCurveAttrOperator(CompoundAttrOperator[FalloffCurvePlugOperator]):
    __slots__ = ()

    falloffCurve_Position = FloatField(default_value=0.0)
    fcp = falloffCurve_Position

    falloffCurve_FloatValue = FloatField(default_value=0.0)
    fcfv = falloffCurve_FloatValue

    falloffCurve_Interp = FalloffCurve_falloffCurve_InterpEnumField(
        default_value=0
    )
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

    axialMagnitude_Interp = AxialMagnitude_axialMagnitude_InterpEnumField(
        default_value=0
    )
    amagi = axialMagnitude_Interp


class AxialMagnitudeAttrOperator(
    CompoundAttrOperator[AxialMagnitudePlugOperator]
):
    __slots__ = ()

    axialMagnitude_Position = FloatField(default_value=0.0)
    amagp = axialMagnitude_Position

    axialMagnitude_FloatValue = FloatField(default_value=0.0)
    amagfv = axialMagnitude_FloatValue

    axialMagnitude_Interp = AxialMagnitude_axialMagnitude_InterpEnumField(
        default_value=0
    )
    amagi = axialMagnitude_Interp


class AxialMagnitudeField(
    CompoundField[AxialMagnitudeAttrOperator, AxialMagnitudePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxialMagnitudeAttrOperator
    PLUG_CLS = AxialMagnitudePlugOperator


class CurveRadiusPlugOperator(CompoundPlugOperator["CurveRadiusAttrOperator"]):
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

    curveRadius_Interp = CurveRadius_curveRadius_InterpEnumField(
        default_value=0
    )
    cradi = curveRadius_Interp


class CurveRadiusAttrOperator(CompoundAttrOperator[CurveRadiusPlugOperator]):
    __slots__ = ()

    curveRadius_Position = FloatField(default_value=0.0)
    cradp = curveRadius_Position

    curveRadius_FloatValue = FloatField(default_value=0.0)
    cradfv = curveRadius_FloatValue

    curveRadius_Interp = CurveRadius_curveRadius_InterpEnumField(
        default_value=0
    )
    cradi = curveRadius_Interp


class CurveRadiusField(
    CompoundField[CurveRadiusAttrOperator, CurveRadiusPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurveRadiusAttrOperator
    PLUG_CLS = CurveRadiusPlugOperator


class DirectionPlugOperator(CompoundPlugOperator["DirectionAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("directionX", "dx"),
        ("directionY", "dy"),
        ("directionZ", "dz"),
    )

    directionX = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    dx = directionX

    directionY = DoubleField(default_value=0.0)
    dy = directionY

    directionZ = DoubleField(default_value=0.0)
    dz = directionZ


class DirectionAttrOperator(CompoundAttrOperator[DirectionPlugOperator]):
    __slots__ = ()

    directionX = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    dx = directionX

    directionY = DoubleField(default_value=0.0)
    dy = directionY

    directionZ = DoubleField(default_value=0.0)
    dz = directionZ


class DirectionField(
    CompoundField[DirectionAttrOperator, DirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionAttrOperator
    PLUG_CLS = DirectionPlugOperator

    directionX = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    dx = directionX

    directionY = DoubleField(default_value=0.0)
    dy = directionY

    directionZ = DoubleField(default_value=0.0)
    dz = directionZ
