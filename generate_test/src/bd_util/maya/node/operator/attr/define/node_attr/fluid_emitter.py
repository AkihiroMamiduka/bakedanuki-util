# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


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


class RandStatePlugOperator(
    Long3CompoundBasePlugOperator["RandStateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("randStateX", "rstx"),
        ("randStateY", "rsty"),
        ("randStateZ", "rstz"),
    )

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


class RandStateAttrOperator(
    Long3CompoundBaseAttrOperator[RandStatePlugOperator]
):
    __slots__ = ()

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


class RandStateField(
    Long3CompoundBaseField[RandStateAttrOperator, RandStatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RandStateAttrOperator
    PLUG_CLS = RandStatePlugOperator


class TextureRatePlugOperator(
    Float3CompoundBasePlugOperator["TextureRateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("textureRateR", "txrr"),
        ("textureRateG", "txrg"),
        ("textureRateB", "txrb"),
    )

    textureRateR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    txrr = textureRateR

    textureRateG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    txrg = textureRateG

    textureRateB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    txrb = textureRateB


class TextureRateAttrOperator(
    Float3CompoundBaseAttrOperator[TextureRatePlugOperator]
):
    __slots__ = ()

    textureRateR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    txrr = textureRateR

    textureRateG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    txrg = textureRateG

    textureRateB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    txrb = textureRateB


class TextureRateField(
    Float3CompoundBaseField[TextureRateAttrOperator, TextureRatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureRateAttrOperator
    PLUG_CLS = TextureRatePlugOperator

    textureRateR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    txrr = textureRateR

    textureRateG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    txrg = textureRateG

    textureRateB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    txrb = textureRateB


class ParticleColorPlugOperator(
    Float3CompoundBasePlugOperator["ParticleColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("particleColorR", "pcr"),
        ("particleColorG", "pcg"),
        ("particleColorB", "pcb"),
    )

    particleColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    pcr = particleColorR

    particleColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    pcg = particleColorG

    particleColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    pcb = particleColorB


class ParticleColorAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleColorPlugOperator]
):
    __slots__ = ()

    particleColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    pcr = particleColorR

    particleColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    pcg = particleColorG

    particleColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    pcb = particleColorB


class ParticleColorField(
    Float3CompoundBaseField[ParticleColorAttrOperator, ParticleColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParticleColorAttrOperator
    PLUG_CLS = ParticleColorPlugOperator

    particleColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    pcr = particleColorR

    particleColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    pcg = particleColorG

    particleColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    pcb = particleColorB


class VolumeOffsetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["VolumeOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("volumeOffsetX", "vfx"),
        ("volumeOffsetY", "vfy"),
        ("volumeOffsetZ", "vfz"),
    )

    volumeOffsetX = DoubleLinearField(default_value=0.0)
    vfx = volumeOffsetX

    volumeOffsetY = DoubleLinearField(default_value=0.0)
    vfy = volumeOffsetY

    volumeOffsetZ = DoubleLinearField(default_value=0.0)
    vfz = volumeOffsetZ


class VolumeOffsetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[VolumeOffsetPlugOperator]
):
    __slots__ = ()

    volumeOffsetX = DoubleLinearField(default_value=0.0)
    vfx = volumeOffsetX

    volumeOffsetY = DoubleLinearField(default_value=0.0)
    vfy = volumeOffsetY

    volumeOffsetZ = DoubleLinearField(default_value=0.0)
    vfz = volumeOffsetZ


class VolumeOffsetField(
    DoubleLinear3CompoundBaseField[VolumeOffsetAttrOperator, VolumeOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VolumeOffsetAttrOperator
    PLUG_CLS = VolumeOffsetPlugOperator

    volumeOffsetX = DoubleLinearField(default_value=0.0)
    vfx = volumeOffsetX

    volumeOffsetY = DoubleLinearField(default_value=0.0)
    vfy = volumeOffsetY

    volumeOffsetZ = DoubleLinearField(default_value=0.0)
    vfz = volumeOffsetZ


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
