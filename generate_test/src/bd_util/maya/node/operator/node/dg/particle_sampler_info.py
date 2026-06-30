# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.particle_sampler_info import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.addr import AddrField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.char import CharField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


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


class ParticleSamplerInfo(DG):
    __slots__ = ()

    NODE_TYPE = "particleSamplerInfo"

    particleAttrArray = AddrField()
    paa = particleAttrArray

    particleOrder = LongField()
    podr = particleOrder

    objectType = CharField()
    otyp = objectType

    particleColor = ParticleColorField()
    pc = particleColor
    particleColorR = particleColor.particleColorR
    pcr = particleColorR
    particleColorG = particleColor.particleColorG
    pcg = particleColorG
    particleColorB = particleColor.particleColorB
    pcb = particleColorB

    particleTransparency = ParticleTransparencyField()
    pt = particleTransparency
    particleTransparencyR = particleTransparency.particleTransparencyR
    ptr = particleTransparencyR
    particleTransparencyG = particleTransparency.particleTransparencyG
    ptg = particleTransparencyG
    particleTransparencyB = particleTransparency.particleTransparencyB
    ptb = particleTransparencyB

    particleIncandescence = ParticleIncandescenceField()
    pi = particleIncandescence
    particleIncandescenceR = particleIncandescence.particleIncandescenceR
    pir = particleIncandescenceR
    particleIncandescenceG = particleIncandescence.particleIncandescenceG
    pig = particleIncandescenceG
    particleIncandescenceB = particleIncandescence.particleIncandescenceB
    pib = particleIncandescenceB

    particleAge = FloatField()
    pa = particleAge

    particleLifespan = FloatField()
    pls = particleLifespan

    outUvCoord = OutUvCoordField()
    ouv = outUvCoord
    outUCoord = outUvCoord.outUCoord
    ouc = outUCoord
    outVCoord = outUvCoord.outVCoord
    ovc = outVCoord

    outUvType = OutUvTypeEnumField()
    ouvt = outUvType

    normalizationValue = FloatField()
    nlv = normalizationValue

    normalizationMethod = NormalizationMethodEnumField()
    nlm = normalizationMethod

    inverseOutUv = BoolField()
    iouv = inverseOutUv

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    outIncandescence = OutIncandescenceField()
    oi = outIncandescence
    outIncandescenceR = outIncandescence.outIncandescenceR
    oicr = outIncandescenceR
    outIncandescenceG = outIncandescence.outIncandescenceG
    oicg = outIncandescenceG
    outIncandescenceB = outIncandescence.outIncandescenceB
    oicb = outIncandescenceB

    finalLifespanPP = FloatField()
    flp = finalLifespanPP

    ageNormalized = FloatField()
    anl = ageNormalized

    particleId = LongField()
    pid = particleId

    age = FloatField()
    ag = age

    lifespan = FloatField()
    lsp = lifespan

    lifespanPP = FloatField()
    lpp = lifespanPP

    acceleration = AccelerationField()
    acc = acceleration
    accelerationX = acceleration.accelerationX
    accx = accelerationX
    accelerationY = acceleration.accelerationY
    accy = accelerationY
    accelerationZ = acceleration.accelerationZ
    accz = accelerationZ

    birthTime = FloatField()
    bt = birthTime

    force = ForceField()
    frc = force
    forceX = force.forceX
    frx = forceX
    forceY = force.forceY
    fry = forceY
    forceZ = force.forceZ
    frz = forceZ

    position = PositionField()
    pos = position
    positionX = position.positionX
    posx = positionX
    positionY = position.positionY
    posy = positionY
    positionZ = position.positionZ
    posz = positionZ

    birthPosition = BirthPositionField()
    bpos = birthPosition
    birthPositionX = birthPosition.birthPositionX
    bpox = birthPositionX
    birthPositionY = birthPosition.birthPositionY
    bpoy = birthPositionY
    birthPositionZ = birthPosition.birthPositionZ
    bpoz = birthPositionZ

    birthWorldPosition = BirthWorldPositionField()
    bwpo = birthWorldPosition
    birthWorldPositionX = birthWorldPosition.birthWorldPositionX
    bwpx = birthWorldPositionX
    birthWorldPositionY = birthWorldPosition.birthWorldPositionY
    bwpy = birthWorldPositionY
    birthWorldPositionZ = birthWorldPosition.birthWorldPositionZ
    bwpz = birthWorldPositionZ

    velocity = VelocityField()
    vel = velocity
    velocityX = velocity.velocityX
    velx = velocityX
    velocityY = velocity.velocityY
    vely = velocityY
    velocityZ = velocity.velocityZ
    velz = velocityZ

    worldPosition = WorldPositionField()
    wps = worldPosition
    worldPositionX = worldPosition.worldPositionX
    wpsx = worldPositionX
    worldPositionY = worldPosition.worldPositionY
    wpsy = worldPositionY
    worldPositionZ = worldPosition.worldPositionZ
    wpsz = worldPositionZ

    worldVelocity = WorldVelocityField()
    wvl = worldVelocity
    worldVelocityX = worldVelocity.worldVelocityX
    wvlx = worldVelocityX
    worldVelocityY = worldVelocity.worldVelocityY
    wvly = worldVelocityY
    worldVelocityZ = worldVelocity.worldVelocityZ
    wvlz = worldVelocityZ

    parentU = FloatField()
    pau = parentU

    parentV = FloatField()
    pav = parentV

    collisionU = FloatField()
    clu = collisionU

    collisionV = FloatField()
    clv = collisionV

    colorRed = FloatField()
    cr = colorRed

    colorGreen = FloatField()
    cg = colorGreen

    colorBlue = FloatField()
    cb = colorBlue

    rgbPP = RgbPPField()
    rgb = rgbPP
    rPP = rgbPP.rPP
    rpp = rPP
    gPP = rgbPP.gPP
    gpp = gPP
    bPP = rgbPP.bPP
    bpp = bPP

    incandescencePP = IncandescencePPField()
    oipp = incandescencePP
    incandescencePPR = incandescencePP.incandescencePPR
    ippr = incandescencePPR
    incandescencePPG = incandescencePP.incandescencePPG
    ippg = incandescencePPG
    incandescencePPB = incandescencePP.incandescencePPB
    ippb = incandescencePPB

    incandescence = IncandescenceField()
    in_ = incandescence
    incandescenceR = incandescence.incandescenceR
    inr = incandescenceR
    incandescenceG = incandescence.incandescenceG
    ing = incandescenceG
    incandescenceB = incandescence.incandescenceB
    inb = incandescenceB

    opacity = FloatField()
    op = opacity

    opacityPP = FloatField()
    opp = opacityPP

    radius = FloatField()
    rds = radius

    radiusPP = FloatField()
    rdp = radiusPP

    userScalar1PP = FloatField()
    uds1 = userScalar1PP

    userScalar2PP = FloatField()
    uds2 = userScalar2PP

    userScalar3PP = FloatField()
    uds3 = userScalar3PP

    userScalar4PP = FloatField()
    uds4 = userScalar4PP

    userScalar5PP = FloatField()
    uds5 = userScalar5PP

    userVector1PP = UserVector1PPField()
    udv1 = userVector1PP
    userVector1PPX = userVector1PP.userVector1PPX
    uv1x = userVector1PPX
    userVector1PPY = userVector1PP.userVector1PPY
    uv1y = userVector1PPY
    userVector1PPZ = userVector1PP.userVector1PPZ
    uv1z = userVector1PPZ

    userVector2PP = UserVector2PPField()
    udv2 = userVector2PP
    userVector2PPX = userVector2PP.userVector2PPX
    uv2x = userVector2PPX
    userVector2PPY = userVector2PP.userVector2PPY
    uv2y = userVector2PPY
    userVector2PPZ = userVector2PP.userVector2PPZ
    uv2z = userVector2PPZ

    userVector3PP = UserVector3PPField()
    udv3 = userVector3PP
    userVector3PPX = userVector3PP.userVector3PPX
    uv3x = userVector3PPX
    userVector3PPY = userVector3PP.userVector3PPY
    uv3y = userVector3PPY
    userVector3PPZ = userVector3PP.userVector3PPZ
    uv3z = userVector3PPZ

    userVector4PP = UserVector4PPField()
    udv4 = userVector4PP
    userVector4PPX = userVector4PP.userVector4PPX
    uv4x = userVector4PPX
    userVector4PPY = userVector4PP.userVector4PPY
    uv4y = userVector4PPY
    userVector4PPZ = userVector4PP.userVector4PPZ
    uv4z = userVector4PPZ

    userVector5PP = UserVector5PPField()
    udv5 = userVector5PP
    userVector5PPX = userVector5PP.userVector5PPX
    uv5x = userVector5PPX
    userVector5PPY = userVector5PP.userVector5PPY
    uv5y = userVector5PPY
    userVector5PPZ = userVector5PP.userVector5PPZ
    uv5z = userVector5PPZ
