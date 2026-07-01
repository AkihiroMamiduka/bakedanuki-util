# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.particle_cloud import (
    BlobMapField,
    ColorField,
    IncandescenceField,
    LightDataArrayField,
    NormalCameraField,
    OutColorField,
    OutGlowColorField,
    OutParticleEmissionField,
    OutTransparencyField,
    ParticleEmissionField,
    PointObjField,
    SurfaceColorField,
    TransparencyField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class ParticleCloud(DG):
    __slots__ = ()

    NODE_TYPE = "particleCloud"

    outParticleEmission = OutParticleEmissionField()
    oe = outParticleEmission
    outParticleEmissionR = outParticleEmission.outParticleEmissionR
    oer = outParticleEmissionR
    outParticleEmissionG = outParticleEmission.outParticleEmissionG
    oeg = outParticleEmissionG
    outParticleEmissionB = outParticleEmission.outParticleEmissionB
    oeb = outParticleEmissionB

    outColor = OutColorField()
    oi = outColor
    outColorR = outColor.outColorR
    oir = outColorR
    outColorG = outColor.outColorG
    oig = outColorG
    outColorB = outColor.outColorB
    oib = outColorB

    outGlowColor = OutGlowColorField()
    ogi = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    color = ColorField()
    c = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    transparency = TransparencyField()
    t = transparency
    transparencyR = transparency.transparencyR
    tr = transparencyR
    transparencyG = transparency.transparencyG
    tg = transparencyG
    transparencyB = transparency.transparencyB
    tb = transparencyB

    incandescence = IncandescenceField()
    i = incandescence
    incandescenceR = incandescence.incandescenceR
    ir = incandescenceR
    incandescenceG = incandescence.incandescenceG
    ig = incandescenceG
    incandescenceB = incandescence.incandescenceB
    ib = incandescenceB

    density = FloatField()
    d = density

    glowIntensity = FloatField()
    gi = glowIntensity

    noise = FloatField()
    n = noise

    noiseFreq = FloatField()
    nf = noiseFreq

    noiseAspect = FloatField()
    na = noiseAspect

    particleWeight = FloatField()
    w = particleWeight

    particleEmission = ParticleEmissionField()
    e = particleEmission
    particleEmissionR = particleEmission.particleEmissionR
    er = particleEmissionR
    particleEmissionG = particleEmission.particleEmissionG
    eg = particleEmissionG
    particleEmissionB = particleEmission.particleEmissionB
    eb = particleEmissionB

    blobMap = BlobMapField()
    m = blobMap
    blobMapR = blobMap.blobMapR
    mr = blobMapR
    blobMapG = blobMap.blobMapG
    mg = blobMapG
    blobMapB = blobMap.blobMapB
    mb = blobMapB

    lightDataArray = LightDataArrayField(multi=True)
    ltd = lightDataArray

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ

    lightIntensityR = FloatField()
    lir = lightIntensityR

    lightIntensityG = FloatField()
    lig = lightIntensityG

    lightIntensityB = FloatField()
    lib = lightIntensityB

    pointObj = PointObjField()
    p = pointObj
    pointObjX = pointObj.pointObjX
    px = pointObjX
    pointObjY = pointObj.pointObjY
    py = pointObjY
    pointObjZ = pointObj.pointObjZ
    pz = pointObjZ

    normalCamera = NormalCameraField()
    nc = normalCamera
    normalCameraX = normalCamera.normalCameraX
    ncx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ncy = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    ncz = normalCameraZ

    translucenceCoeff = FloatField()
    tc = translucenceCoeff

    diffuseCoeff = FloatField()
    dc = diffuseCoeff

    surfaceShadingShadow = BoolField()
    sss = surfaceShadingShadow

    surfaceColor = SurfaceColorField()
    sc = surfaceColor
    surfaceColorR = surfaceColor.surfaceColorR
    scr = surfaceColorR
    surfaceColorG = surfaceColor.surfaceColorG
    scg = surfaceColorG
    surfaceColorB = surfaceColor.surfaceColorB
    scb = surfaceColorB

    solidCoreSize = FloatField()
    scs = solidCoreSize

    translucence = FloatField()
    trsl = translucence

    noiseAnimRate = FloatField()
    nanr = noiseAnimRate

    roundness = FloatField()
    rdns = roundness

    rayDepth = ShortField()
    rd = rayDepth

    particleOrder = LongField()
    podr = particleOrder

    filterRadius = FloatField()
    flrs = filterRadius

    renderState = LongField()
    rdst = renderState
