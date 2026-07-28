# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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


class ParticleColorPlugOperator(
    Float3CompoundBasePlugOperator["ParticleColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("particleColorR", "pcr"),
        ("particleColorG", "pcg"),
        ("particleColorB", "pcb"),
    )

    particleColorR = FloatField(default_value=0.0, readable=False)
    pcr = particleColorR

    particleColorG = FloatField(default_value=0.0, readable=False)
    pcg = particleColorG

    particleColorB = FloatField(default_value=0.0, readable=False)
    pcb = particleColorB


class ParticleColorAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleColorPlugOperator]
):
    __slots__ = ()

    particleColorR = FloatField(default_value=0.0, readable=False)
    pcr = particleColorR

    particleColorG = FloatField(default_value=0.0, readable=False)
    pcg = particleColorG

    particleColorB = FloatField(default_value=0.0, readable=False)
    pcb = particleColorB


class ParticleColorField(
    Float3CompoundBaseField[
        ParticleColorAttrOperator, ParticleColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ParticleColorAttrOperator
    PLUG_CLS = ParticleColorPlugOperator

    particleColorR = FloatField(default_value=0.0, readable=False)
    pcr = particleColorR

    particleColorG = FloatField(default_value=0.0, readable=False)
    pcg = particleColorG

    particleColorB = FloatField(default_value=0.0, readable=False)
    pcb = particleColorB


class ParticleTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["ParticleTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("particleTransparencyR", "ptr"),
        ("particleTransparencyG", "ptg"),
        ("particleTransparencyB", "ptb"),
    )

    particleTransparencyR = FloatField(default_value=0.0, readable=False)
    ptr = particleTransparencyR

    particleTransparencyG = FloatField(default_value=0.0, readable=False)
    ptg = particleTransparencyG

    particleTransparencyB = FloatField(default_value=0.0, readable=False)
    ptb = particleTransparencyB


class ParticleTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleTransparencyPlugOperator]
):
    __slots__ = ()

    particleTransparencyR = FloatField(default_value=0.0, readable=False)
    ptr = particleTransparencyR

    particleTransparencyG = FloatField(default_value=0.0, readable=False)
    ptg = particleTransparencyG

    particleTransparencyB = FloatField(default_value=0.0, readable=False)
    ptb = particleTransparencyB


class ParticleTransparencyField(
    Float3CompoundBaseField[
        ParticleTransparencyAttrOperator, ParticleTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ParticleTransparencyAttrOperator
    PLUG_CLS = ParticleTransparencyPlugOperator

    particleTransparencyR = FloatField(default_value=0.0, readable=False)
    ptr = particleTransparencyR

    particleTransparencyG = FloatField(default_value=0.0, readable=False)
    ptg = particleTransparencyG

    particleTransparencyB = FloatField(default_value=0.0, readable=False)
    ptb = particleTransparencyB


class ParticleIncandescencePlugOperator(
    Float3CompoundBasePlugOperator["ParticleIncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("particleIncandescenceR", "pir"),
        ("particleIncandescenceG", "pig"),
        ("particleIncandescenceB", "pib"),
    )

    particleIncandescenceR = FloatField(default_value=0.0, readable=False)
    pir = particleIncandescenceR

    particleIncandescenceG = FloatField(default_value=0.0, readable=False)
    pig = particleIncandescenceG

    particleIncandescenceB = FloatField(default_value=0.0, readable=False)
    pib = particleIncandescenceB


class ParticleIncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleIncandescencePlugOperator]
):
    __slots__ = ()

    particleIncandescenceR = FloatField(default_value=0.0, readable=False)
    pir = particleIncandescenceR

    particleIncandescenceG = FloatField(default_value=0.0, readable=False)
    pig = particleIncandescenceG

    particleIncandescenceB = FloatField(default_value=0.0, readable=False)
    pib = particleIncandescenceB


class ParticleIncandescenceField(
    Float3CompoundBaseField[
        ParticleIncandescenceAttrOperator, ParticleIncandescencePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ParticleIncandescenceAttrOperator
    PLUG_CLS = ParticleIncandescencePlugOperator

    particleIncandescenceR = FloatField(default_value=0.0, readable=False)
    pir = particleIncandescenceR

    particleIncandescenceG = FloatField(default_value=0.0, readable=False)
    pig = particleIncandescenceG

    particleIncandescenceB = FloatField(default_value=0.0, readable=False)
    pib = particleIncandescenceB


class OutUvCoordPlugOperator(
    Float2CompoundBasePlugOperator["OutUvCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outUCoord", "ouc"),
        ("outVCoord", "ovc"),
    )

    outUCoord = FloatField(default_value=0.5, writable=False)
    ouc = outUCoord

    outVCoord = FloatField(default_value=0.5, writable=False)
    ovc = outVCoord


class OutUvCoordAttrOperator(
    Float2CompoundBaseAttrOperator[OutUvCoordPlugOperator]
):
    __slots__ = ()

    outUCoord = FloatField(default_value=0.5, writable=False)
    ouc = outUCoord

    outVCoord = FloatField(default_value=0.5, writable=False)
    ovc = outVCoord


class OutUvCoordField(
    Float2CompoundBaseField[OutUvCoordAttrOperator, OutUvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutUvCoordAttrOperator
    PLUG_CLS = OutUvCoordPlugOperator

    outUCoord = FloatField(default_value=0.5, writable=False)
    ouc = outUCoord

    outVCoord = FloatField(default_value=0.5, writable=False)
    ovc = outVCoord


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutIncandescencePlugOperator(
    Float3CompoundBasePlugOperator["OutIncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outIncandescenceR", "oicr"),
        ("outIncandescenceG", "oicg"),
        ("outIncandescenceB", "oicb"),
    )

    outIncandescenceR = FloatField(default_value=0.0, writable=False)
    oicr = outIncandescenceR

    outIncandescenceG = FloatField(default_value=0.0, writable=False)
    oicg = outIncandescenceG

    outIncandescenceB = FloatField(default_value=0.0, writable=False)
    oicb = outIncandescenceB


class OutIncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[OutIncandescencePlugOperator]
):
    __slots__ = ()

    outIncandescenceR = FloatField(default_value=0.0, writable=False)
    oicr = outIncandescenceR

    outIncandescenceG = FloatField(default_value=0.0, writable=False)
    oicg = outIncandescenceG

    outIncandescenceB = FloatField(default_value=0.0, writable=False)
    oicb = outIncandescenceB


class OutIncandescenceField(
    Float3CompoundBaseField[
        OutIncandescenceAttrOperator, OutIncandescencePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutIncandescenceAttrOperator
    PLUG_CLS = OutIncandescencePlugOperator

    outIncandescenceR = FloatField(default_value=0.0, writable=False)
    oicr = outIncandescenceR

    outIncandescenceG = FloatField(default_value=0.0, writable=False)
    oicg = outIncandescenceG

    outIncandescenceB = FloatField(default_value=0.0, writable=False)
    oicb = outIncandescenceB


class AccelerationPlugOperator(
    Float3CompoundBasePlugOperator["AccelerationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("accelerationX", "accx"),
        ("accelerationY", "accy"),
        ("accelerationZ", "accz"),
    )

    accelerationX = FloatField(default_value=0.5, writable=False)
    accx = accelerationX

    accelerationY = FloatField(default_value=0.5, writable=False)
    accy = accelerationY

    accelerationZ = FloatField(default_value=0.5, writable=False)
    accz = accelerationZ


class AccelerationAttrOperator(
    Float3CompoundBaseAttrOperator[AccelerationPlugOperator]
):
    __slots__ = ()

    accelerationX = FloatField(default_value=0.5, writable=False)
    accx = accelerationX

    accelerationY = FloatField(default_value=0.5, writable=False)
    accy = accelerationY

    accelerationZ = FloatField(default_value=0.5, writable=False)
    accz = accelerationZ


class AccelerationField(
    Float3CompoundBaseField[AccelerationAttrOperator, AccelerationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AccelerationAttrOperator
    PLUG_CLS = AccelerationPlugOperator

    accelerationX = FloatField(default_value=0.5, writable=False)
    accx = accelerationX

    accelerationY = FloatField(default_value=0.5, writable=False)
    accy = accelerationY

    accelerationZ = FloatField(default_value=0.5, writable=False)
    accz = accelerationZ


class ForcePlugOperator(Float3CompoundBasePlugOperator["ForceAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("forceX", "frx"),
        ("forceY", "fry"),
        ("forceZ", "frz"),
    )

    forceX = FloatField(default_value=0.5, writable=False)
    frx = forceX

    forceY = FloatField(default_value=0.5, writable=False)
    fry = forceY

    forceZ = FloatField(default_value=0.5, writable=False)
    frz = forceZ


class ForceAttrOperator(Float3CompoundBaseAttrOperator[ForcePlugOperator]):
    __slots__ = ()

    forceX = FloatField(default_value=0.5, writable=False)
    frx = forceX

    forceY = FloatField(default_value=0.5, writable=False)
    fry = forceY

    forceZ = FloatField(default_value=0.5, writable=False)
    frz = forceZ


class ForceField(
    Float3CompoundBaseField[ForceAttrOperator, ForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForceAttrOperator
    PLUG_CLS = ForcePlugOperator

    forceX = FloatField(default_value=0.5, writable=False)
    frx = forceX

    forceY = FloatField(default_value=0.5, writable=False)
    fry = forceY

    forceZ = FloatField(default_value=0.5, writable=False)
    frz = forceZ


class PositionPlugOperator(
    Float3CompoundBasePlugOperator["PositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionX", "posx"),
        ("positionY", "posy"),
        ("positionZ", "posz"),
    )

    positionX = FloatField(default_value=0.5, writable=False)
    posx = positionX

    positionY = FloatField(default_value=0.5, writable=False)
    posy = positionY

    positionZ = FloatField(default_value=0.5, writable=False)
    posz = positionZ


class PositionAttrOperator(
    Float3CompoundBaseAttrOperator[PositionPlugOperator]
):
    __slots__ = ()

    positionX = FloatField(default_value=0.5, writable=False)
    posx = positionX

    positionY = FloatField(default_value=0.5, writable=False)
    posy = positionY

    positionZ = FloatField(default_value=0.5, writable=False)
    posz = positionZ


class PositionField(
    Float3CompoundBaseField[PositionAttrOperator, PositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionAttrOperator
    PLUG_CLS = PositionPlugOperator

    positionX = FloatField(default_value=0.5, writable=False)
    posx = positionX

    positionY = FloatField(default_value=0.5, writable=False)
    posy = positionY

    positionZ = FloatField(default_value=0.5, writable=False)
    posz = positionZ


class BirthPositionPlugOperator(
    Float3CompoundBasePlugOperator["BirthPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("birthPositionX", "bpox"),
        ("birthPositionY", "bpoy"),
        ("birthPositionZ", "bpoz"),
    )

    birthPositionX = FloatField(default_value=0.5, writable=False)
    bpox = birthPositionX

    birthPositionY = FloatField(default_value=0.5, writable=False)
    bpoy = birthPositionY

    birthPositionZ = FloatField(default_value=0.5, writable=False)
    bpoz = birthPositionZ


class BirthPositionAttrOperator(
    Float3CompoundBaseAttrOperator[BirthPositionPlugOperator]
):
    __slots__ = ()

    birthPositionX = FloatField(default_value=0.5, writable=False)
    bpox = birthPositionX

    birthPositionY = FloatField(default_value=0.5, writable=False)
    bpoy = birthPositionY

    birthPositionZ = FloatField(default_value=0.5, writable=False)
    bpoz = birthPositionZ


class BirthPositionField(
    Float3CompoundBaseField[
        BirthPositionAttrOperator, BirthPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BirthPositionAttrOperator
    PLUG_CLS = BirthPositionPlugOperator

    birthPositionX = FloatField(default_value=0.5, writable=False)
    bpox = birthPositionX

    birthPositionY = FloatField(default_value=0.5, writable=False)
    bpoy = birthPositionY

    birthPositionZ = FloatField(default_value=0.5, writable=False)
    bpoz = birthPositionZ


class BirthWorldPositionPlugOperator(
    Float3CompoundBasePlugOperator["BirthWorldPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("birthWorldPositionX", "bwpx"),
        ("birthWorldPositionY", "bwpy"),
        ("birthWorldPositionZ", "bwpz"),
    )

    birthWorldPositionX = FloatField(default_value=0.5, writable=False)
    bwpx = birthWorldPositionX

    birthWorldPositionY = FloatField(default_value=0.5, writable=False)
    bwpy = birthWorldPositionY

    birthWorldPositionZ = FloatField(default_value=0.5, writable=False)
    bwpz = birthWorldPositionZ


class BirthWorldPositionAttrOperator(
    Float3CompoundBaseAttrOperator[BirthWorldPositionPlugOperator]
):
    __slots__ = ()

    birthWorldPositionX = FloatField(default_value=0.5, writable=False)
    bwpx = birthWorldPositionX

    birthWorldPositionY = FloatField(default_value=0.5, writable=False)
    bwpy = birthWorldPositionY

    birthWorldPositionZ = FloatField(default_value=0.5, writable=False)
    bwpz = birthWorldPositionZ


class BirthWorldPositionField(
    Float3CompoundBaseField[
        BirthWorldPositionAttrOperator, BirthWorldPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BirthWorldPositionAttrOperator
    PLUG_CLS = BirthWorldPositionPlugOperator

    birthWorldPositionX = FloatField(default_value=0.5, writable=False)
    bwpx = birthWorldPositionX

    birthWorldPositionY = FloatField(default_value=0.5, writable=False)
    bwpy = birthWorldPositionY

    birthWorldPositionZ = FloatField(default_value=0.5, writable=False)
    bwpz = birthWorldPositionZ


class VelocityPlugOperator(
    Float3CompoundBasePlugOperator["VelocityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("velocityX", "velx"),
        ("velocityY", "vely"),
        ("velocityZ", "velz"),
    )

    velocityX = FloatField(default_value=0.5, writable=False)
    velx = velocityX

    velocityY = FloatField(default_value=0.5, writable=False)
    vely = velocityY

    velocityZ = FloatField(default_value=0.5, writable=False)
    velz = velocityZ


class VelocityAttrOperator(
    Float3CompoundBaseAttrOperator[VelocityPlugOperator]
):
    __slots__ = ()

    velocityX = FloatField(default_value=0.5, writable=False)
    velx = velocityX

    velocityY = FloatField(default_value=0.5, writable=False)
    vely = velocityY

    velocityZ = FloatField(default_value=0.5, writable=False)
    velz = velocityZ


class VelocityField(
    Float3CompoundBaseField[VelocityAttrOperator, VelocityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VelocityAttrOperator
    PLUG_CLS = VelocityPlugOperator

    velocityX = FloatField(default_value=0.5, writable=False)
    velx = velocityX

    velocityY = FloatField(default_value=0.5, writable=False)
    vely = velocityY

    velocityZ = FloatField(default_value=0.5, writable=False)
    velz = velocityZ


class WorldPositionPlugOperator(
    Float3CompoundBasePlugOperator["WorldPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldPositionX", "wpsx"),
        ("worldPositionY", "wpsy"),
        ("worldPositionZ", "wpsz"),
    )

    worldPositionX = FloatField(default_value=0.5, writable=False)
    wpsx = worldPositionX

    worldPositionY = FloatField(default_value=0.5, writable=False)
    wpsy = worldPositionY

    worldPositionZ = FloatField(default_value=0.5, writable=False)
    wpsz = worldPositionZ


class WorldPositionAttrOperator(
    Float3CompoundBaseAttrOperator[WorldPositionPlugOperator]
):
    __slots__ = ()

    worldPositionX = FloatField(default_value=0.5, writable=False)
    wpsx = worldPositionX

    worldPositionY = FloatField(default_value=0.5, writable=False)
    wpsy = worldPositionY

    worldPositionZ = FloatField(default_value=0.5, writable=False)
    wpsz = worldPositionZ


class WorldPositionField(
    Float3CompoundBaseField[
        WorldPositionAttrOperator, WorldPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WorldPositionAttrOperator
    PLUG_CLS = WorldPositionPlugOperator

    worldPositionX = FloatField(default_value=0.5, writable=False)
    wpsx = worldPositionX

    worldPositionY = FloatField(default_value=0.5, writable=False)
    wpsy = worldPositionY

    worldPositionZ = FloatField(default_value=0.5, writable=False)
    wpsz = worldPositionZ


class WorldVelocityPlugOperator(
    Float3CompoundBasePlugOperator["WorldVelocityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldVelocityX", "wvlx"),
        ("worldVelocityY", "wvly"),
        ("worldVelocityZ", "wvlz"),
    )

    worldVelocityX = FloatField(default_value=0.5, writable=False)
    wvlx = worldVelocityX

    worldVelocityY = FloatField(default_value=0.5, writable=False)
    wvly = worldVelocityY

    worldVelocityZ = FloatField(default_value=0.5, writable=False)
    wvlz = worldVelocityZ


class WorldVelocityAttrOperator(
    Float3CompoundBaseAttrOperator[WorldVelocityPlugOperator]
):
    __slots__ = ()

    worldVelocityX = FloatField(default_value=0.5, writable=False)
    wvlx = worldVelocityX

    worldVelocityY = FloatField(default_value=0.5, writable=False)
    wvly = worldVelocityY

    worldVelocityZ = FloatField(default_value=0.5, writable=False)
    wvlz = worldVelocityZ


class WorldVelocityField(
    Float3CompoundBaseField[
        WorldVelocityAttrOperator, WorldVelocityPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WorldVelocityAttrOperator
    PLUG_CLS = WorldVelocityPlugOperator

    worldVelocityX = FloatField(default_value=0.5, writable=False)
    wvlx = worldVelocityX

    worldVelocityY = FloatField(default_value=0.5, writable=False)
    wvly = worldVelocityY

    worldVelocityZ = FloatField(default_value=0.5, writable=False)
    wvlz = worldVelocityZ


class RgbPPPlugOperator(Float3CompoundBasePlugOperator["RgbPPAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rPP", "rpp"),
        ("gPP", "gpp"),
        ("bPP", "bpp"),
    )

    rPP = FloatField(default_value=0.5, writable=False)
    rpp = rPP

    gPP = FloatField(default_value=0.5, writable=False)
    gpp = gPP

    bPP = FloatField(default_value=0.5, writable=False)
    bpp = bPP


class RgbPPAttrOperator(Float3CompoundBaseAttrOperator[RgbPPPlugOperator]):
    __slots__ = ()

    rPP = FloatField(default_value=0.5, writable=False)
    rpp = rPP

    gPP = FloatField(default_value=0.5, writable=False)
    gpp = gPP

    bPP = FloatField(default_value=0.5, writable=False)
    bpp = bPP


class RgbPPField(
    Float3CompoundBaseField[RgbPPAttrOperator, RgbPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RgbPPAttrOperator
    PLUG_CLS = RgbPPPlugOperator

    rPP = FloatField(default_value=0.5, writable=False)
    rpp = rPP

    gPP = FloatField(default_value=0.5, writable=False)
    gpp = gPP

    bPP = FloatField(default_value=0.5, writable=False)
    bpp = bPP


class IncandescencePPPlugOperator(
    Float3CompoundBasePlugOperator["IncandescencePPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescencePPR", "ippr"),
        ("incandescencePPG", "ippg"),
        ("incandescencePPB", "ippb"),
    )

    incandescencePPR = FloatField(default_value=0.5, writable=False)
    ippr = incandescencePPR

    incandescencePPG = FloatField(default_value=0.5, writable=False)
    ippg = incandescencePPG

    incandescencePPB = FloatField(default_value=0.5, writable=False)
    ippb = incandescencePPB


class IncandescencePPAttrOperator(
    Float3CompoundBaseAttrOperator[IncandescencePPPlugOperator]
):
    __slots__ = ()

    incandescencePPR = FloatField(default_value=0.5, writable=False)
    ippr = incandescencePPR

    incandescencePPG = FloatField(default_value=0.5, writable=False)
    ippg = incandescencePPG

    incandescencePPB = FloatField(default_value=0.5, writable=False)
    ippb = incandescencePPB


class IncandescencePPField(
    Float3CompoundBaseField[
        IncandescencePPAttrOperator, IncandescencePPPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = IncandescencePPAttrOperator
    PLUG_CLS = IncandescencePPPlugOperator

    incandescencePPR = FloatField(default_value=0.5, writable=False)
    ippr = incandescencePPR

    incandescencePPG = FloatField(default_value=0.5, writable=False)
    ippg = incandescencePPG

    incandescencePPB = FloatField(default_value=0.5, writable=False)
    ippb = incandescencePPB


class IncandescencePlugOperator(
    Float3CompoundBasePlugOperator["IncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescenceR", "inr"),
        ("incandescenceG", "ing"),
        ("incandescenceB", "inb"),
    )

    incandescenceR = FloatField(default_value=0.5, writable=False)
    inr = incandescenceR

    incandescenceG = FloatField(default_value=0.5, writable=False)
    ing = incandescenceG

    incandescenceB = FloatField(default_value=0.5, writable=False)
    inb = incandescenceB


class IncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescenceR = FloatField(default_value=0.5, writable=False)
    inr = incandescenceR

    incandescenceG = FloatField(default_value=0.5, writable=False)
    ing = incandescenceG

    incandescenceB = FloatField(default_value=0.5, writable=False)
    inb = incandescenceB


class IncandescenceField(
    Float3CompoundBaseField[
        IncandescenceAttrOperator, IncandescencePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator

    incandescenceR = FloatField(default_value=0.5, writable=False)
    inr = incandescenceR

    incandescenceG = FloatField(default_value=0.5, writable=False)
    ing = incandescenceG

    incandescenceB = FloatField(default_value=0.5, writable=False)
    inb = incandescenceB


class UserVector1PPPlugOperator(
    Float3CompoundBasePlugOperator["UserVector1PPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("userVector1PPX", "uv1x"),
        ("userVector1PPY", "uv1y"),
        ("userVector1PPZ", "uv1z"),
    )

    userVector1PPX = FloatField(default_value=0.0, writable=False)
    uv1x = userVector1PPX

    userVector1PPY = FloatField(default_value=0.0, writable=False)
    uv1y = userVector1PPY

    userVector1PPZ = FloatField(default_value=0.0, writable=False)
    uv1z = userVector1PPZ


class UserVector1PPAttrOperator(
    Float3CompoundBaseAttrOperator[UserVector1PPPlugOperator]
):
    __slots__ = ()

    userVector1PPX = FloatField(default_value=0.0, writable=False)
    uv1x = userVector1PPX

    userVector1PPY = FloatField(default_value=0.0, writable=False)
    uv1y = userVector1PPY

    userVector1PPZ = FloatField(default_value=0.0, writable=False)
    uv1z = userVector1PPZ


class UserVector1PPField(
    Float3CompoundBaseField[
        UserVector1PPAttrOperator, UserVector1PPPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = UserVector1PPAttrOperator
    PLUG_CLS = UserVector1PPPlugOperator

    userVector1PPX = FloatField(default_value=0.0, writable=False)
    uv1x = userVector1PPX

    userVector1PPY = FloatField(default_value=0.0, writable=False)
    uv1y = userVector1PPY

    userVector1PPZ = FloatField(default_value=0.0, writable=False)
    uv1z = userVector1PPZ


class UserVector2PPPlugOperator(
    Float3CompoundBasePlugOperator["UserVector2PPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("userVector2PPX", "uv2x"),
        ("userVector2PPY", "uv2y"),
        ("userVector2PPZ", "uv2z"),
    )

    userVector2PPX = FloatField(default_value=0.0, writable=False)
    uv2x = userVector2PPX

    userVector2PPY = FloatField(default_value=0.0, writable=False)
    uv2y = userVector2PPY

    userVector2PPZ = FloatField(default_value=0.0, writable=False)
    uv2z = userVector2PPZ


class UserVector2PPAttrOperator(
    Float3CompoundBaseAttrOperator[UserVector2PPPlugOperator]
):
    __slots__ = ()

    userVector2PPX = FloatField(default_value=0.0, writable=False)
    uv2x = userVector2PPX

    userVector2PPY = FloatField(default_value=0.0, writable=False)
    uv2y = userVector2PPY

    userVector2PPZ = FloatField(default_value=0.0, writable=False)
    uv2z = userVector2PPZ


class UserVector2PPField(
    Float3CompoundBaseField[
        UserVector2PPAttrOperator, UserVector2PPPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = UserVector2PPAttrOperator
    PLUG_CLS = UserVector2PPPlugOperator

    userVector2PPX = FloatField(default_value=0.0, writable=False)
    uv2x = userVector2PPX

    userVector2PPY = FloatField(default_value=0.0, writable=False)
    uv2y = userVector2PPY

    userVector2PPZ = FloatField(default_value=0.0, writable=False)
    uv2z = userVector2PPZ


class UserVector3PPPlugOperator(
    Float3CompoundBasePlugOperator["UserVector3PPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("userVector3PPX", "uv3x"),
        ("userVector3PPY", "uv3y"),
        ("userVector3PPZ", "uv3z"),
    )

    userVector3PPX = FloatField(default_value=0.0, writable=False)
    uv3x = userVector3PPX

    userVector3PPY = FloatField(default_value=0.0, writable=False)
    uv3y = userVector3PPY

    userVector3PPZ = FloatField(default_value=0.0, writable=False)
    uv3z = userVector3PPZ


class UserVector3PPAttrOperator(
    Float3CompoundBaseAttrOperator[UserVector3PPPlugOperator]
):
    __slots__ = ()

    userVector3PPX = FloatField(default_value=0.0, writable=False)
    uv3x = userVector3PPX

    userVector3PPY = FloatField(default_value=0.0, writable=False)
    uv3y = userVector3PPY

    userVector3PPZ = FloatField(default_value=0.0, writable=False)
    uv3z = userVector3PPZ


class UserVector3PPField(
    Float3CompoundBaseField[
        UserVector3PPAttrOperator, UserVector3PPPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = UserVector3PPAttrOperator
    PLUG_CLS = UserVector3PPPlugOperator

    userVector3PPX = FloatField(default_value=0.0, writable=False)
    uv3x = userVector3PPX

    userVector3PPY = FloatField(default_value=0.0, writable=False)
    uv3y = userVector3PPY

    userVector3PPZ = FloatField(default_value=0.0, writable=False)
    uv3z = userVector3PPZ


class UserVector4PPPlugOperator(
    Float3CompoundBasePlugOperator["UserVector4PPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("userVector4PPX", "uv4x"),
        ("userVector4PPY", "uv4y"),
        ("userVector4PPZ", "uv4z"),
    )

    userVector4PPX = FloatField(default_value=0.0, writable=False)
    uv4x = userVector4PPX

    userVector4PPY = FloatField(default_value=0.0, writable=False)
    uv4y = userVector4PPY

    userVector4PPZ = FloatField(default_value=0.0, writable=False)
    uv4z = userVector4PPZ


class UserVector4PPAttrOperator(
    Float3CompoundBaseAttrOperator[UserVector4PPPlugOperator]
):
    __slots__ = ()

    userVector4PPX = FloatField(default_value=0.0, writable=False)
    uv4x = userVector4PPX

    userVector4PPY = FloatField(default_value=0.0, writable=False)
    uv4y = userVector4PPY

    userVector4PPZ = FloatField(default_value=0.0, writable=False)
    uv4z = userVector4PPZ


class UserVector4PPField(
    Float3CompoundBaseField[
        UserVector4PPAttrOperator, UserVector4PPPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = UserVector4PPAttrOperator
    PLUG_CLS = UserVector4PPPlugOperator

    userVector4PPX = FloatField(default_value=0.0, writable=False)
    uv4x = userVector4PPX

    userVector4PPY = FloatField(default_value=0.0, writable=False)
    uv4y = userVector4PPY

    userVector4PPZ = FloatField(default_value=0.0, writable=False)
    uv4z = userVector4PPZ


class UserVector5PPPlugOperator(
    Float3CompoundBasePlugOperator["UserVector5PPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("userVector5PPX", "uv5x"),
        ("userVector5PPY", "uv5y"),
        ("userVector5PPZ", "uv5z"),
    )

    userVector5PPX = FloatField(default_value=0.0, writable=False)
    uv5x = userVector5PPX

    userVector5PPY = FloatField(default_value=0.0, writable=False)
    uv5y = userVector5PPY

    userVector5PPZ = FloatField(default_value=0.0, writable=False)
    uv5z = userVector5PPZ


class UserVector5PPAttrOperator(
    Float3CompoundBaseAttrOperator[UserVector5PPPlugOperator]
):
    __slots__ = ()

    userVector5PPX = FloatField(default_value=0.0, writable=False)
    uv5x = userVector5PPX

    userVector5PPY = FloatField(default_value=0.0, writable=False)
    uv5y = userVector5PPY

    userVector5PPZ = FloatField(default_value=0.0, writable=False)
    uv5z = userVector5PPZ


class UserVector5PPField(
    Float3CompoundBaseField[
        UserVector5PPAttrOperator, UserVector5PPPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = UserVector5PPAttrOperator
    PLUG_CLS = UserVector5PPPlugOperator

    userVector5PPX = FloatField(default_value=0.0, writable=False)
    uv5x = userVector5PPX

    userVector5PPY = FloatField(default_value=0.0, writable=False)
    uv5y = userVector5PPY

    userVector5PPZ = FloatField(default_value=0.0, writable=False)
    uv5z = userVector5PPZ
