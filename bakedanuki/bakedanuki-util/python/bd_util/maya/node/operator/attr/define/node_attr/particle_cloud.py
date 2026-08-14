# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float3Field,
)


class OutParticleEmissionPlugOperator(
    Float3CompoundBasePlugOperator["OutParticleEmissionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outParticleEmissionR", "oer"),
        ("outParticleEmissionG", "oeg"),
        ("outParticleEmissionB", "oeb"),
    )

    outParticleEmissionR = FloatField(default_value=0.0, writable=False)
    oer = outParticleEmissionR

    outParticleEmissionG = FloatField(default_value=0.0, writable=False)
    oeg = outParticleEmissionG

    outParticleEmissionB = FloatField(default_value=0.0, writable=False)
    oeb = outParticleEmissionB


class OutParticleEmissionAttrOperator(
    Float3CompoundBaseAttrOperator[OutParticleEmissionPlugOperator]
):
    __slots__ = ()

    outParticleEmissionR = FloatField(default_value=0.0, writable=False)
    oer = outParticleEmissionR

    outParticleEmissionG = FloatField(default_value=0.0, writable=False)
    oeg = outParticleEmissionG

    outParticleEmissionB = FloatField(default_value=0.0, writable=False)
    oeb = outParticleEmissionB


class OutParticleEmissionField(
    Float3CompoundBaseField[
        OutParticleEmissionAttrOperator, OutParticleEmissionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutParticleEmissionAttrOperator
    PLUG_CLS = OutParticleEmissionPlugOperator

    outParticleEmissionR = FloatField(default_value=0.0, writable=False)
    oer = outParticleEmissionR

    outParticleEmissionG = FloatField(default_value=0.0, writable=False)
    oeg = outParticleEmissionG

    outParticleEmissionB = FloatField(default_value=0.0, writable=False)
    oeb = outParticleEmissionB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "oir"),
        ("outColorG", "oig"),
        ("outColorB", "oib"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    oir = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    oig = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    oib = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    oir = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    oig = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    oib = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    oir = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    oig = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    oib = outColorB


class OutGlowColorPlugOperator(
    Float3CompoundBasePlugOperator["OutGlowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outGlowColorR", "ogr"),
        ("outGlowColorG", "ogg"),
        ("outGlowColorB", "ogb"),
    )

    outGlowColorR = FloatField(default_value=0.0, writable=False)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0, writable=False)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0, writable=False)
    ogb = outGlowColorB


class OutGlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutGlowColorPlugOperator]
):
    __slots__ = ()

    outGlowColorR = FloatField(default_value=0.0, writable=False)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0, writable=False)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0, writable=False)
    ogb = outGlowColorB


class OutGlowColorField(
    Float3CompoundBaseField[OutGlowColorAttrOperator, OutGlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutGlowColorAttrOperator
    PLUG_CLS = OutGlowColorPlugOperator

    outGlowColorR = FloatField(default_value=0.0, writable=False)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0, writable=False)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0, writable=False)
    ogb = outGlowColorB


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


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField(default_value=0.0)
    cr = colorR

    colorG = FloatField(default_value=0.5882400274276733)
    cg = colorG

    colorB = FloatField(default_value=0.6439999938011169)
    cb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.0)
    cr = colorR

    colorG = FloatField(default_value=0.5882400274276733)
    cg = colorG

    colorB = FloatField(default_value=0.6439999938011169)
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=0.0)
    cr = colorR

    colorG = FloatField(default_value=0.5882400274276733)
    cg = colorG

    colorB = FloatField(default_value=0.6439999938011169)
    cb = colorB


class TransparencyPlugOperator(
    Float3CompoundBasePlugOperator["TransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparencyR", "tr"),
        ("transparencyG", "tg"),
        ("transparencyB", "tb"),
    )

    transparencyR = FloatField(default_value=0.5)
    tr = transparencyR

    transparencyG = FloatField(default_value=0.5)
    tg = transparencyG

    transparencyB = FloatField(default_value=0.5)
    tb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField(default_value=0.5)
    tr = transparencyR

    transparencyG = FloatField(default_value=0.5)
    tg = transparencyG

    transparencyB = FloatField(default_value=0.5)
    tb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField(default_value=0.5)
    tr = transparencyR

    transparencyG = FloatField(default_value=0.5)
    tg = transparencyG

    transparencyB = FloatField(default_value=0.5)
    tb = transparencyB


class IncandescencePlugOperator(
    Float3CompoundBasePlugOperator["IncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescenceR", "ir"),
        ("incandescenceG", "ig"),
        ("incandescenceB", "ib"),
    )

    incandescenceR = FloatField(default_value=0.0)
    ir = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    ig = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    ib = incandescenceB


class IncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescenceR = FloatField(default_value=0.0)
    ir = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    ig = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    ib = incandescenceB


class IncandescenceField(
    Float3CompoundBaseField[
        IncandescenceAttrOperator, IncandescencePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator

    incandescenceR = FloatField(default_value=0.0)
    ir = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    ig = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    ib = incandescenceB


class ParticleEmissionPlugOperator(
    Float3CompoundBasePlugOperator["ParticleEmissionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("particleEmissionR", "er"),
        ("particleEmissionG", "eg"),
        ("particleEmissionB", "eb"),
    )

    particleEmissionR = FloatField(default_value=0.0)
    er = particleEmissionR

    particleEmissionG = FloatField(default_value=0.0)
    eg = particleEmissionG

    particleEmissionB = FloatField(default_value=0.0)
    eb = particleEmissionB


class ParticleEmissionAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleEmissionPlugOperator]
):
    __slots__ = ()

    particleEmissionR = FloatField(default_value=0.0)
    er = particleEmissionR

    particleEmissionG = FloatField(default_value=0.0)
    eg = particleEmissionG

    particleEmissionB = FloatField(default_value=0.0)
    eb = particleEmissionB


class ParticleEmissionField(
    Float3CompoundBaseField[
        ParticleEmissionAttrOperator, ParticleEmissionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ParticleEmissionAttrOperator
    PLUG_CLS = ParticleEmissionPlugOperator

    particleEmissionR = FloatField(default_value=0.0)
    er = particleEmissionR

    particleEmissionG = FloatField(default_value=0.0)
    eg = particleEmissionG

    particleEmissionB = FloatField(default_value=0.0)
    eb = particleEmissionB


class BlobMapPlugOperator(
    Float3CompoundBasePlugOperator["BlobMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("blobMapR", "mr"),
        ("blobMapG", "mg"),
        ("blobMapB", "mb"),
    )

    blobMapR = FloatField(default_value=1.0)
    mr = blobMapR

    blobMapG = FloatField(default_value=1.0)
    mg = blobMapG

    blobMapB = FloatField(default_value=1.0)
    mb = blobMapB


class BlobMapAttrOperator(Float3CompoundBaseAttrOperator[BlobMapPlugOperator]):
    __slots__ = ()

    blobMapR = FloatField(default_value=1.0)
    mr = blobMapR

    blobMapG = FloatField(default_value=1.0)
    mg = blobMapG

    blobMapB = FloatField(default_value=1.0)
    mb = blobMapB


class BlobMapField(
    Float3CompoundBaseField[BlobMapAttrOperator, BlobMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlobMapAttrOperator
    PLUG_CLS = BlobMapPlugOperator

    blobMapR = FloatField(default_value=1.0)
    mr = blobMapR

    blobMapG = FloatField(default_value=1.0)
    mg = blobMapG

    blobMapB = FloatField(default_value=1.0)
    mb = blobMapB


class LightDataArrayPlugOperator(
    LightDataPlugOperator["LightDataArrayAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirection", "ld"),
        ("lightIntensity", "li"),
        ("lightAmbient", "la"),
        ("lightDiffuse", "ldf"),
        ("lightSpecular", "ls"),
        ("lightShadowFraction", "lsf"),
        ("preShadowIntensity", "psi"),
        ("lightBlindData", "lbd"),
    )

    lightDirection = Float3Field(default_value=(0.0, 0.0, 0.0))
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(1.0, 1.0, 1.0))
    li = lightIntensity

    lightAmbient = BoolField(default_value=True)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=True)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=1.0)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0)
    lbd = lightBlindData


class LightDataArrayAttrOperator(
    LightDataAttrOperator[LightDataArrayPlugOperator]
):
    __slots__ = ()

    lightDirection = Float3Field(default_value=(0.0, 0.0, 0.0))
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(1.0, 1.0, 1.0))
    li = lightIntensity

    lightAmbient = BoolField(default_value=True)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=True)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=1.0)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0)
    lbd = lightBlindData


class LightDataArrayField(
    LightDataField[LightDataArrayAttrOperator, LightDataArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataArrayAttrOperator
    PLUG_CLS = LightDataArrayPlugOperator


class PointObjPlugOperator(
    Float3CompoundBasePlugOperator["PointObjAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointObjX", "px"),
        ("pointObjY", "py"),
        ("pointObjZ", "pz"),
    )

    pointObjX = FloatField(default_value=0.0)
    px = pointObjX

    pointObjY = FloatField(default_value=0.0)
    py = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    pz = pointObjZ


class PointObjAttrOperator(
    Float3CompoundBaseAttrOperator[PointObjPlugOperator]
):
    __slots__ = ()

    pointObjX = FloatField(default_value=0.0)
    px = pointObjX

    pointObjY = FloatField(default_value=0.0)
    py = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    pz = pointObjZ


class PointObjField(
    Float3CompoundBaseField[PointObjAttrOperator, PointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointObjAttrOperator
    PLUG_CLS = PointObjPlugOperator

    pointObjX = FloatField(default_value=0.0)
    px = pointObjX

    pointObjY = FloatField(default_value=0.0)
    py = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    pz = pointObjZ


class NormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["NormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalCameraX", "ncx"),
        ("normalCameraY", "ncy"),
        ("normalCameraZ", "ncz"),
    )

    normalCameraX = FloatField(default_value=1.0)
    ncx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ncy = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    ncz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField(default_value=1.0)
    ncx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ncy = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    ncz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField(default_value=1.0)
    ncx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ncy = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    ncz = normalCameraZ


class SurfaceColorPlugOperator(
    Float3CompoundBasePlugOperator["SurfaceColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("surfaceColorR", "scr"),
        ("surfaceColorG", "scg"),
        ("surfaceColorB", "scb"),
    )

    surfaceColorR = FloatField(default_value=0.4000000059604645)
    scr = surfaceColorR

    surfaceColorG = FloatField(default_value=0.4000000059604645)
    scg = surfaceColorG

    surfaceColorB = FloatField(default_value=0.4000000059604645)
    scb = surfaceColorB


class SurfaceColorAttrOperator(
    Float3CompoundBaseAttrOperator[SurfaceColorPlugOperator]
):
    __slots__ = ()

    surfaceColorR = FloatField(default_value=0.4000000059604645)
    scr = surfaceColorR

    surfaceColorG = FloatField(default_value=0.4000000059604645)
    scg = surfaceColorG

    surfaceColorB = FloatField(default_value=0.4000000059604645)
    scb = surfaceColorB


class SurfaceColorField(
    Float3CompoundBaseField[SurfaceColorAttrOperator, SurfaceColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SurfaceColorAttrOperator
    PLUG_CLS = SurfaceColorPlugOperator

    surfaceColorR = FloatField(default_value=0.4000000059604645)
    scr = surfaceColorR

    surfaceColorG = FloatField(default_value=0.4000000059604645)
    scg = surfaceColorG

    surfaceColorB = FloatField(default_value=0.4000000059604645)
    scb = surfaceColorB
