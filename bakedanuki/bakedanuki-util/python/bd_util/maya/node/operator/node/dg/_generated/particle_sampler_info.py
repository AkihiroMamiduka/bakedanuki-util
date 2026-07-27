# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.particle_sampler_info import (
    AccelerationField,
    BirthPositionField,
    BirthWorldPositionField,
    ForceField,
    IncandescenceField,
    IncandescencePPField,
    OutColorField,
    OutIncandescenceField,
    OutTransparencyField,
    OutUvCoordField,
    ParticleColorField,
    ParticleIncandescenceField,
    ParticleTransparencyField,
    PositionField,
    RgbPPField,
    UserVector1PPField,
    UserVector2PPField,
    UserVector3PPField,
    UserVector4PPField,
    UserVector5PPField,
    VelocityField,
    WorldPositionField,
    WorldVelocityField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.addr import AddrField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.char import CharField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class OutUvTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMALIZED_AGE = 0
    ABSOLUTE_AGE = 1
    PARENT_UV = 2
    COLLISION_UV = 3


class OutUvTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMALIZED_AGE = 0
    ABSOLUTE_AGE = 1
    PARENT_UV = 2
    COLLISION_UV = 3

    NAME_MAP = {
        NORMALIZED_AGE: "Normalized Age",
        ABSOLUTE_AGE: "Absolute Age",
        PARENT_UV: "Parent UV",
        COLLISION_UV: "Collision UV",
    }


class OutUvTypeEnumField(
    EnumField[OutUvTypeEnumAttrOperator, OutUvTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutUvTypeEnumAttrOperator
    PLUG_CLS = OutUvTypeEnumPlugOperator


class NormalizationMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OSCILLATE = 0
    CLAMP = 1


class NormalizationMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OSCILLATE = 0
    CLAMP = 1

    NAME_MAP = {
        OSCILLATE: "Oscillate",
        CLAMP: "Clamp",
    }


class NormalizationMethodEnumField(
    EnumField[NormalizationMethodEnumAttrOperator, NormalizationMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalizationMethodEnumAttrOperator
    PLUG_CLS = NormalizationMethodEnumPlugOperator


class GeneratedParticleSamplerInfo(DG):
    __slots__ = ()

    NODE_TYPE = "particleSamplerInfo"

    particleAttrArray = AddrField(default_value=0.0, readable=False)
    paa = particleAttrArray

    particleOrder = LongField(default_value=0, readable=False)
    podr = particleOrder

    objectType = CharField(default_value=4, min_value=0, max_value=255, readable=False)
    otyp = objectType

    particleColor = ParticleColorField(default_value=(0.0, 0.0, 0.0), readable=False)
    pc = particleColor
    particleColorR = particleColor.particleColorR
    pcr = particleColorR
    particleColorG = particleColor.particleColorG
    pcg = particleColorG
    particleColorB = particleColor.particleColorB
    pcb = particleColorB

    particleTransparency = ParticleTransparencyField(default_value=(0.0, 0.0, 0.0), readable=False)
    pt = particleTransparency
    particleTransparencyR = particleTransparency.particleTransparencyR
    ptr = particleTransparencyR
    particleTransparencyG = particleTransparency.particleTransparencyG
    ptg = particleTransparencyG
    particleTransparencyB = particleTransparency.particleTransparencyB
    ptb = particleTransparencyB

    particleIncandescence = ParticleIncandescenceField(default_value=(0.0, 0.0, 0.0), readable=False)
    pi = particleIncandescence
    particleIncandescenceR = particleIncandescence.particleIncandescenceR
    pir = particleIncandescenceR
    particleIncandescenceG = particleIncandescence.particleIncandescenceG
    pig = particleIncandescenceG
    particleIncandescenceB = particleIncandescence.particleIncandescenceB
    pib = particleIncandescenceB

    particleAge = FloatField(default_value=0.0, readable=False)
    pa = particleAge

    particleLifespan = FloatField(default_value=0.0, readable=False)
    pls = particleLifespan

    outUvCoord = OutUvCoordField(default_value=(0.5, 0.5), writable=False)
    ouv = outUvCoord
    outUCoord = outUvCoord.outUCoord
    ouc = outUCoord
    outVCoord = outUvCoord.outVCoord
    ovc = outVCoord

    outUvType = OutUvTypeEnumField(default_value=0)
    ouvt = outUvType

    normalizationValue = FloatField(default_value=1.0, min_value=-3.4028234663852886e+38)
    nlv = normalizationValue

    normalizationMethod = NormalizationMethodEnumField(default_value=0)
    nlm = normalizationMethod

    inverseOutUv = BoolField(default_value=False)
    iouv = inverseOutUv

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    outIncandescence = OutIncandescenceField(default_value=(0.0, 0.0, 0.0), writable=False)
    oi = outIncandescence
    outIncandescenceR = outIncandescence.outIncandescenceR
    oicr = outIncandescenceR
    outIncandescenceG = outIncandescence.outIncandescenceG
    oicg = outIncandescenceG
    outIncandescenceB = outIncandescence.outIncandescenceB
    oicb = outIncandescenceB

    finalLifespanPP = FloatField(default_value=1.0, writable=False)
    flp = finalLifespanPP

    ageNormalized = FloatField(default_value=0.5, writable=False)
    anl = ageNormalized

    particleId = LongField(default_value=0, writable=False)
    pid = particleId

    age = FloatField(default_value=0.5, writable=False)
    ag = age

    lifespan = FloatField(default_value=0.5, writable=False)
    lsp = lifespan

    lifespanPP = FloatField(default_value=0.5, writable=False)
    lpp = lifespanPP

    acceleration = AccelerationField(default_value=(0.5, 0.5, 0.5), writable=False)
    acc = acceleration
    accelerationX = acceleration.accelerationX
    accx = accelerationX
    accelerationY = acceleration.accelerationY
    accy = accelerationY
    accelerationZ = acceleration.accelerationZ
    accz = accelerationZ

    birthTime = FloatField(default_value=0.5, writable=False)
    bt = birthTime

    force = ForceField(default_value=(0.5, 0.5, 0.5), writable=False)
    frc = force
    forceX = force.forceX
    frx = forceX
    forceY = force.forceY
    fry = forceY
    forceZ = force.forceZ
    frz = forceZ

    position = PositionField(default_value=(0.5, 0.5, 0.5), writable=False)
    pos = position
    positionX = position.positionX
    posx = positionX
    positionY = position.positionY
    posy = positionY
    positionZ = position.positionZ
    posz = positionZ

    birthPosition = BirthPositionField(default_value=(0.5, 0.5, 0.5), writable=False)
    bpos = birthPosition
    birthPositionX = birthPosition.birthPositionX
    bpox = birthPositionX
    birthPositionY = birthPosition.birthPositionY
    bpoy = birthPositionY
    birthPositionZ = birthPosition.birthPositionZ
    bpoz = birthPositionZ

    birthWorldPosition = BirthWorldPositionField(default_value=(0.5, 0.5, 0.5), writable=False)
    bwpo = birthWorldPosition
    birthWorldPositionX = birthWorldPosition.birthWorldPositionX
    bwpx = birthWorldPositionX
    birthWorldPositionY = birthWorldPosition.birthWorldPositionY
    bwpy = birthWorldPositionY
    birthWorldPositionZ = birthWorldPosition.birthWorldPositionZ
    bwpz = birthWorldPositionZ

    velocity = VelocityField(default_value=(0.5, 0.5, 0.5), writable=False)
    vel = velocity
    velocityX = velocity.velocityX
    velx = velocityX
    velocityY = velocity.velocityY
    vely = velocityY
    velocityZ = velocity.velocityZ
    velz = velocityZ

    worldPosition = WorldPositionField(default_value=(0.5, 0.5, 0.5), writable=False)
    wps = worldPosition
    worldPositionX = worldPosition.worldPositionX
    wpsx = worldPositionX
    worldPositionY = worldPosition.worldPositionY
    wpsy = worldPositionY
    worldPositionZ = worldPosition.worldPositionZ
    wpsz = worldPositionZ

    worldVelocity = WorldVelocityField(default_value=(0.5, 0.5, 0.5), writable=False)
    wvl = worldVelocity
    worldVelocityX = worldVelocity.worldVelocityX
    wvlx = worldVelocityX
    worldVelocityY = worldVelocity.worldVelocityY
    wvly = worldVelocityY
    worldVelocityZ = worldVelocity.worldVelocityZ
    wvlz = worldVelocityZ

    parentU = FloatField(default_value=0.5, writable=False)
    pau = parentU

    parentV = FloatField(default_value=0.5, writable=False)
    pav = parentV

    collisionU = FloatField(default_value=0.5, writable=False)
    clu = collisionU

    collisionV = FloatField(default_value=0.5, writable=False)
    clv = collisionV

    colorRed = FloatField(default_value=0.5, writable=False)
    cr = colorRed

    colorGreen = FloatField(default_value=0.5, writable=False)
    cg = colorGreen

    colorBlue = FloatField(default_value=0.5, writable=False)
    cb = colorBlue

    rgbPP = RgbPPField(default_value=(0.5, 0.5, 0.5), writable=False)
    rgb = rgbPP
    rPP = rgbPP.rPP
    rpp = rPP
    gPP = rgbPP.gPP
    gpp = gPP
    bPP = rgbPP.bPP
    bpp = bPP

    incandescencePP = IncandescencePPField(default_value=(0.5, 0.5, 0.5), writable=False)
    oipp = incandescencePP
    incandescencePPR = incandescencePP.incandescencePPR
    ippr = incandescencePPR
    incandescencePPG = incandescencePP.incandescencePPG
    ippg = incandescencePPG
    incandescencePPB = incandescencePP.incandescencePPB
    ippb = incandescencePPB

    incandescence = IncandescenceField(default_value=(0.5, 0.5, 0.5), writable=False)
    in_ = incandescence
    incandescenceR = incandescence.incandescenceR
    inr = incandescenceR
    incandescenceG = incandescence.incandescenceG
    ing = incandescenceG
    incandescenceB = incandescence.incandescenceB
    inb = incandescenceB

    opacity = FloatField(default_value=0.5, writable=False)
    op = opacity

    opacityPP = FloatField(default_value=0.5, writable=False)
    opp = opacityPP

    radius = FloatField(default_value=1.0, writable=False)
    rds = radius

    radiusPP = FloatField(default_value=1.0, writable=False)
    rdp = radiusPP

    userScalar1PP = FloatField(default_value=0.0, writable=False)
    uds1 = userScalar1PP

    userScalar2PP = FloatField(default_value=0.0, writable=False)
    uds2 = userScalar2PP

    userScalar3PP = FloatField(default_value=0.0, writable=False)
    uds3 = userScalar3PP

    userScalar4PP = FloatField(default_value=0.0, writable=False)
    uds4 = userScalar4PP

    userScalar5PP = FloatField(default_value=0.0, writable=False)
    uds5 = userScalar5PP

    userVector1PP = UserVector1PPField(default_value=(0.0, 0.0, 0.0), writable=False)
    udv1 = userVector1PP
    userVector1PPX = userVector1PP.userVector1PPX
    uv1x = userVector1PPX
    userVector1PPY = userVector1PP.userVector1PPY
    uv1y = userVector1PPY
    userVector1PPZ = userVector1PP.userVector1PPZ
    uv1z = userVector1PPZ

    userVector2PP = UserVector2PPField(default_value=(0.0, 0.0, 0.0), writable=False)
    udv2 = userVector2PP
    userVector2PPX = userVector2PP.userVector2PPX
    uv2x = userVector2PPX
    userVector2PPY = userVector2PP.userVector2PPY
    uv2y = userVector2PPY
    userVector2PPZ = userVector2PP.userVector2PPZ
    uv2z = userVector2PPZ

    userVector3PP = UserVector3PPField(default_value=(0.0, 0.0, 0.0), writable=False)
    udv3 = userVector3PP
    userVector3PPX = userVector3PP.userVector3PPX
    uv3x = userVector3PPX
    userVector3PPY = userVector3PP.userVector3PPY
    uv3y = userVector3PPY
    userVector3PPZ = userVector3PP.userVector3PPZ
    uv3z = userVector3PPZ

    userVector4PP = UserVector4PPField(default_value=(0.0, 0.0, 0.0), writable=False)
    udv4 = userVector4PP
    userVector4PPX = userVector4PP.userVector4PPX
    uv4x = userVector4PPX
    userVector4PPY = userVector4PP.userVector4PPY
    uv4y = userVector4PPY
    userVector4PPZ = userVector4PP.userVector4PPZ
    uv4z = userVector4PPZ

    userVector5PP = UserVector5PPField(default_value=(0.0, 0.0, 0.0), writable=False)
    udv5 = userVector5PP
    userVector5PPX = userVector5PP.userVector5PPX
    uv5x = userVector5PPX
    userVector5PPY = userVector5PP.userVector5PPY
    uv5y = userVector5PPY
    userVector5PPZ = userVector5PP.userVector5PPZ
    uv5z = userVector5PPZ
