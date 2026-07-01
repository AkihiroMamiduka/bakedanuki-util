# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class OutParticleEmissionPlugOperator(
    Float3CompoundBasePlugOperator["OutParticleEmissionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outParticleEmissionR", "oer"),
        ("outParticleEmissionG", "oeg"),
        ("outParticleEmissionB", "oeb"),
    )

    outParticleEmissionR = FloatField()
    oer = outParticleEmissionR

    outParticleEmissionG = FloatField()
    oeg = outParticleEmissionG

    outParticleEmissionB = FloatField()
    oeb = outParticleEmissionB


class OutParticleEmissionAttrOperator(
    Float3CompoundBaseAttrOperator[OutParticleEmissionPlugOperator]
):
    __slots__ = ()

    outParticleEmissionR = FloatField()
    oer = outParticleEmissionR

    outParticleEmissionG = FloatField()
    oeg = outParticleEmissionG

    outParticleEmissionB = FloatField()
    oeb = outParticleEmissionB


class OutParticleEmissionField(
    Float3CompoundBaseField[OutParticleEmissionAttrOperator, OutParticleEmissionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutParticleEmissionAttrOperator
    PLUG_CLS = OutParticleEmissionPlugOperator

    outParticleEmissionR = FloatField()
    oer = outParticleEmissionR

    outParticleEmissionG = FloatField()
    oeg = outParticleEmissionG

    outParticleEmissionB = FloatField()
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

    outColorR = FloatField()
    oir = outColorR

    outColorG = FloatField()
    oig = outColorG

    outColorB = FloatField()
    oib = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    oir = outColorR

    outColorG = FloatField()
    oig = outColorG

    outColorB = FloatField()
    oib = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    oir = outColorR

    outColorG = FloatField()
    oig = outColorG

    outColorB = FloatField()
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

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


class OutGlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutGlowColorPlugOperator]
):
    __slots__ = ()

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
    ogb = outGlowColorB


class OutGlowColorField(
    Float3CompoundBaseField[OutGlowColorAttrOperator, OutGlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutGlowColorAttrOperator
    PLUG_CLS = OutGlowColorPlugOperator

    outGlowColorR = FloatField()
    ogr = outGlowColorR

    outGlowColorG = FloatField()
    ogg = outGlowColorG

    outGlowColorB = FloatField()
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

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
    cb = colorB


class ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
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

    transparencyR = FloatField()
    tr = transparencyR

    transparencyG = FloatField()
    tg = transparencyG

    transparencyB = FloatField()
    tb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField()
    tr = transparencyR

    transparencyG = FloatField()
    tg = transparencyG

    transparencyB = FloatField()
    tb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField()
    tr = transparencyR

    transparencyG = FloatField()
    tg = transparencyG

    transparencyB = FloatField()
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

    incandescenceR = FloatField()
    ir = incandescenceR

    incandescenceG = FloatField()
    ig = incandescenceG

    incandescenceB = FloatField()
    ib = incandescenceB


class IncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescenceR = FloatField()
    ir = incandescenceR

    incandescenceG = FloatField()
    ig = incandescenceG

    incandescenceB = FloatField()
    ib = incandescenceB


class IncandescenceField(
    Float3CompoundBaseField[IncandescenceAttrOperator, IncandescencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator

    incandescenceR = FloatField()
    ir = incandescenceR

    incandescenceG = FloatField()
    ig = incandescenceG

    incandescenceB = FloatField()
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

    particleEmissionR = FloatField()
    er = particleEmissionR

    particleEmissionG = FloatField()
    eg = particleEmissionG

    particleEmissionB = FloatField()
    eb = particleEmissionB


class ParticleEmissionAttrOperator(
    Float3CompoundBaseAttrOperator[ParticleEmissionPlugOperator]
):
    __slots__ = ()

    particleEmissionR = FloatField()
    er = particleEmissionR

    particleEmissionG = FloatField()
    eg = particleEmissionG

    particleEmissionB = FloatField()
    eb = particleEmissionB


class ParticleEmissionField(
    Float3CompoundBaseField[ParticleEmissionAttrOperator, ParticleEmissionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParticleEmissionAttrOperator
    PLUG_CLS = ParticleEmissionPlugOperator

    particleEmissionR = FloatField()
    er = particleEmissionR

    particleEmissionG = FloatField()
    eg = particleEmissionG

    particleEmissionB = FloatField()
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

    blobMapR = FloatField()
    mr = blobMapR

    blobMapG = FloatField()
    mg = blobMapG

    blobMapB = FloatField()
    mb = blobMapB


class BlobMapAttrOperator(
    Float3CompoundBaseAttrOperator[BlobMapPlugOperator]
):
    __slots__ = ()

    blobMapR = FloatField()
    mr = blobMapR

    blobMapG = FloatField()
    mg = blobMapG

    blobMapB = FloatField()
    mb = blobMapB


class BlobMapField(
    Float3CompoundBaseField[BlobMapAttrOperator, BlobMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlobMapAttrOperator
    PLUG_CLS = BlobMapPlugOperator

    blobMapR = FloatField()
    mr = blobMapR

    blobMapG = FloatField()
    mg = blobMapG

    blobMapB = FloatField()
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

    lightDirection = Float3Field()
    ld = lightDirection

    lightIntensity = Float3Field()
    li = lightIntensity

    lightAmbient = BoolField()
    la = lightAmbient

    lightDiffuse = BoolField()
    ldf = lightDiffuse

    lightSpecular = BoolField()
    ls = lightSpecular

    lightShadowFraction = FloatField()
    lsf = lightShadowFraction

    preShadowIntensity = FloatField()
    psi = preShadowIntensity

    lightBlindData = AddrField()
    lbd = lightBlindData


class LightDataArrayAttrOperator(
    LightDataAttrOperator[LightDataArrayPlugOperator]
):
    __slots__ = ()

    lightDirection = Float3Field()
    ld = lightDirection

    lightIntensity = Float3Field()
    li = lightIntensity

    lightAmbient = BoolField()
    la = lightAmbient

    lightDiffuse = BoolField()
    ldf = lightDiffuse

    lightSpecular = BoolField()
    ls = lightSpecular

    lightShadowFraction = FloatField()
    lsf = lightShadowFraction

    preShadowIntensity = FloatField()
    psi = preShadowIntensity

    lightBlindData = AddrField()
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

    pointObjX = FloatField()
    px = pointObjX

    pointObjY = FloatField()
    py = pointObjY

    pointObjZ = FloatField()
    pz = pointObjZ


class PointObjAttrOperator(
    Float3CompoundBaseAttrOperator[PointObjPlugOperator]
):
    __slots__ = ()

    pointObjX = FloatField()
    px = pointObjX

    pointObjY = FloatField()
    py = pointObjY

    pointObjZ = FloatField()
    pz = pointObjZ


class PointObjField(
    Float3CompoundBaseField[PointObjAttrOperator, PointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointObjAttrOperator
    PLUG_CLS = PointObjPlugOperator

    pointObjX = FloatField()
    px = pointObjX

    pointObjY = FloatField()
    py = pointObjY

    pointObjZ = FloatField()
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

    normalCameraX = FloatField()
    ncx = normalCameraX

    normalCameraY = FloatField()
    ncy = normalCameraY

    normalCameraZ = FloatField()
    ncz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField()
    ncx = normalCameraX

    normalCameraY = FloatField()
    ncy = normalCameraY

    normalCameraZ = FloatField()
    ncz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField()
    ncx = normalCameraX

    normalCameraY = FloatField()
    ncy = normalCameraY

    normalCameraZ = FloatField()
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

    surfaceColorR = FloatField()
    scr = surfaceColorR

    surfaceColorG = FloatField()
    scg = surfaceColorG

    surfaceColorB = FloatField()
    scb = surfaceColorB


class SurfaceColorAttrOperator(
    Float3CompoundBaseAttrOperator[SurfaceColorPlugOperator]
):
    __slots__ = ()

    surfaceColorR = FloatField()
    scr = surfaceColorR

    surfaceColorG = FloatField()
    scg = surfaceColorG

    surfaceColorB = FloatField()
    scb = surfaceColorB


class SurfaceColorField(
    Float3CompoundBaseField[SurfaceColorAttrOperator, SurfaceColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SurfaceColorAttrOperator
    PLUG_CLS = SurfaceColorPlugOperator

    surfaceColorR = FloatField()
    scr = surfaceColorR

    surfaceColorG = FloatField()
    scg = surfaceColorG

    surfaceColorB = FloatField()
    scb = surfaceColorB
