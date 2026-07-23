# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.particle_cloud import (
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
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField


class _GeneratedParticleCloud(DG):
    __slots__ = ()

    NODE_TYPE = "particleCloud"

    outParticleEmission = OutParticleEmissionField(default_value=(0.0, 0.0, 0.0), writable=False)
    oe = outParticleEmission
    outParticleEmissionR = outParticleEmission.outParticleEmissionR
    oer = outParticleEmissionR
    outParticleEmissionG = outParticleEmission.outParticleEmissionG
    oeg = outParticleEmissionG
    outParticleEmissionB = outParticleEmission.outParticleEmissionB
    oeb = outParticleEmissionB

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oi = outColor
    outColorR = outColor.outColorR
    oir = outColorR
    outColorG = outColor.outColorG
    oig = outColorG
    outColorB = outColor.outColorB
    oib = outColorB

    outGlowColor = OutGlowColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ogi = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    color = ColorField(default_value=(0.0, 0.5882400274276733, 0.6439999938011169))
    c = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    transparency = TransparencyField(default_value=(0.5, 0.5, 0.5))
    t = transparency
    transparencyR = transparency.transparencyR
    tr = transparencyR
    transparencyG = transparency.transparencyG
    tg = transparencyG
    transparencyB = transparency.transparencyB
    tb = transparencyB

    incandescence = IncandescenceField(default_value=(0.0, 0.0, 0.0))
    i = incandescence
    incandescenceR = incandescence.incandescenceR
    ir = incandescenceR
    incandescenceG = incandescence.incandescenceG
    ig = incandescenceG
    incandescenceB = incandescence.incandescenceB
    ib = incandescenceB

    density = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    d = density

    glowIntensity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gi = glowIntensity

    noise = FloatField(default_value=0.75, soft_min_value=0.0, soft_max_value=1.0)
    n = noise

    noiseFreq = FloatField(default_value=0.15000000596046448, soft_min_value=0.0, soft_max_value=1.0)
    nf = noiseFreq

    noiseAspect = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    na = noiseAspect

    particleWeight = FloatField(default_value=0.0)
    w = particleWeight

    particleEmission = ParticleEmissionField(default_value=(0.0, 0.0, 0.0))
    e = particleEmission
    particleEmissionR = particleEmission.particleEmissionR
    er = particleEmissionR
    particleEmissionG = particleEmission.particleEmissionG
    eg = particleEmissionG
    particleEmissionB = particleEmission.particleEmissionB
    eb = particleEmissionB

    blobMap = BlobMapField(default_value=(1.0, 1.0, 1.0))
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

    pointObj = PointObjField(default_value=(0.0, 0.0, 0.0))
    p = pointObj
    pointObjX = pointObj.pointObjX
    px = pointObjX
    pointObjY = pointObj.pointObjY
    py = pointObjY
    pointObjZ = pointObj.pointObjZ
    pz = pointObjZ

    normalCamera = NormalCameraField(default_value=(1.0, 1.0, 1.0))
    nc = normalCamera
    normalCameraX = normalCamera.normalCameraX
    ncx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ncy = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    ncz = normalCameraZ

    translucenceCoeff = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    tc = translucenceCoeff

    diffuseCoeff = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)
    dc = diffuseCoeff

    surfaceShadingShadow = BoolField(default_value=False)
    sss = surfaceShadingShadow

    surfaceColor = SurfaceColorField(default_value=(0.4000000059604645, 0.4000000059604645, 0.4000000059604645))
    sc = surfaceColor
    surfaceColorR = surfaceColor.surfaceColorR
    scr = surfaceColorR
    surfaceColorG = surfaceColor.surfaceColorG
    scg = surfaceColorG
    surfaceColorB = surfaceColor.surfaceColorB
    scb = surfaceColorB

    solidCoreSize = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    scs = solidCoreSize

    translucence = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    trsl = translucence

    noiseAnimRate = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    nanr = noiseAnimRate

    roundness = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    rdns = roundness

    rayDepth = ShortField(default_value=0)
    rd = rayDepth

    particleOrder = LongField(default_value=0)
    podr = particleOrder

    filterRadius = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    flrs = filterRadius

    renderState = LongField(default_value=0, readable=False)
    rdst = renderState
