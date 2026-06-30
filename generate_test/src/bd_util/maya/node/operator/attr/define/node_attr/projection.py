# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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


class PointObjPlugOperator(
    Float3CompoundBasePlugOperator["PointObjAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointObjX", "pox"),
        ("pointObjY", "poy"),
        ("pointObjZ", "poz"),
    )

    pointObjX = FloatField()
    pox = pointObjX

    pointObjY = FloatField()
    poy = pointObjY

    pointObjZ = FloatField()
    poz = pointObjZ


class PointObjAttrOperator(
    Float3CompoundBaseAttrOperator[PointObjPlugOperator]
):
    __slots__ = ()

    pointObjX = FloatField()
    pox = pointObjX

    pointObjY = FloatField()
    poy = pointObjY

    pointObjZ = FloatField()
    poz = pointObjZ


class PointObjField(
    Float3CompoundBaseField[PointObjAttrOperator, PointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointObjAttrOperator
    PLUG_CLS = PointObjPlugOperator

    pointObjX = FloatField()
    pox = pointObjX

    pointObjY = FloatField()
    poy = pointObjY

    pointObjZ = FloatField()
    poz = pointObjZ


class PointCameraPlugOperator(
    Float3CompoundBasePlugOperator["PointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointCameraX", "px"),
        ("pointCameraY", "py"),
        ("pointCameraZ", "pz"),
    )

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField()
    px = pointCameraX

    pointCameraY = FloatField()
    py = pointCameraY

    pointCameraZ = FloatField()
    pz = pointCameraZ


class FilterSizePlugOperator(
    Float3CompoundBasePlugOperator["FilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("filterSizeX", "fsx"),
        ("filterSizeY", "fsy"),
        ("filterSizeZ", "fsz"),
    )

    filterSizeX = FloatField()
    fsx = filterSizeX

    filterSizeY = FloatField()
    fsy = filterSizeY

    filterSizeZ = FloatField()
    fsz = filterSizeZ


class FilterSizeAttrOperator(
    Float3CompoundBaseAttrOperator[FilterSizePlugOperator]
):
    __slots__ = ()

    filterSizeX = FloatField()
    fsx = filterSizeX

    filterSizeY = FloatField()
    fsy = filterSizeY

    filterSizeZ = FloatField()
    fsz = filterSizeZ


class FilterSizeField(
    Float3CompoundBaseField[FilterSizeAttrOperator, FilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterSizeAttrOperator
    PLUG_CLS = FilterSizePlugOperator

    filterSizeX = FloatField()
    fsx = filterSizeX

    filterSizeY = FloatField()
    fsy = filterSizeY

    filterSizeZ = FloatField()
    fsz = filterSizeZ


class ColorGainPlugOperator(
    Float3CompoundBasePlugOperator["ColorGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorGainR", "cgr"),
        ("colorGainG", "cgg"),
        ("colorGainB", "cgb"),
    )

    colorGainR = FloatField()
    cgr = colorGainR

    colorGainG = FloatField()
    cgg = colorGainG

    colorGainB = FloatField()
    cgb = colorGainB


class ColorGainAttrOperator(
    Float3CompoundBaseAttrOperator[ColorGainPlugOperator]
):
    __slots__ = ()

    colorGainR = FloatField()
    cgr = colorGainR

    colorGainG = FloatField()
    cgg = colorGainG

    colorGainB = FloatField()
    cgb = colorGainB


class ColorGainField(
    Float3CompoundBaseField[ColorGainAttrOperator, ColorGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorGainAttrOperator
    PLUG_CLS = ColorGainPlugOperator

    colorGainR = FloatField()
    cgr = colorGainR

    colorGainG = FloatField()
    cgg = colorGainG

    colorGainB = FloatField()
    cgb = colorGainB


class ColorOffsetPlugOperator(
    Float3CompoundBasePlugOperator["ColorOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorOffsetR", "cor"),
        ("colorOffsetG", "cog"),
        ("colorOffsetB", "cob"),
    )

    colorOffsetR = FloatField()
    cor = colorOffsetR

    colorOffsetG = FloatField()
    cog = colorOffsetG

    colorOffsetB = FloatField()
    cob = colorOffsetB


class ColorOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ColorOffsetPlugOperator]
):
    __slots__ = ()

    colorOffsetR = FloatField()
    cor = colorOffsetR

    colorOffsetG = FloatField()
    cog = colorOffsetG

    colorOffsetB = FloatField()
    cob = colorOffsetB


class ColorOffsetField(
    Float3CompoundBaseField[ColorOffsetAttrOperator, ColorOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorOffsetAttrOperator
    PLUG_CLS = ColorOffsetPlugOperator

    colorOffsetR = FloatField()
    cor = colorOffsetR

    colorOffsetG = FloatField()
    cog = colorOffsetG

    colorOffsetB = FloatField()
    cob = colorOffsetB


class DefaultColorPlugOperator(
    Float3CompoundBasePlugOperator["DefaultColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("defaultColorR", "dcr"),
        ("defaultColorG", "dcg"),
        ("defaultColorB", "dcb"),
    )

    defaultColorR = FloatField()
    dcr = defaultColorR

    defaultColorG = FloatField()
    dcg = defaultColorG

    defaultColorB = FloatField()
    dcb = defaultColorB


class DefaultColorAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultColorPlugOperator]
):
    __slots__ = ()

    defaultColorR = FloatField()
    dcr = defaultColorR

    defaultColorG = FloatField()
    dcg = defaultColorG

    defaultColorB = FloatField()
    dcb = defaultColorB


class DefaultColorField(
    Float3CompoundBaseField[DefaultColorAttrOperator, DefaultColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultColorAttrOperator
    PLUG_CLS = DefaultColorPlugOperator

    defaultColorR = FloatField()
    dcr = defaultColorR

    defaultColorG = FloatField()
    dcg = defaultColorG

    defaultColorB = FloatField()
    dcb = defaultColorB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class NormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["NormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalCameraX", "nx"),
        ("normalCameraY", "ny"),
        ("normalCameraZ", "nz"),
    )

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField()
    nx = normalCameraX

    normalCameraY = FloatField()
    ny = normalCameraY

    normalCameraZ = FloatField()
    nz = normalCameraZ


class SrfNormalPlugOperator(
    Float3CompoundBasePlugOperator["SrfNormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("srfNormalX", "snx"),
        ("srfNormalY", "sny"),
        ("srfNormalZ", "snz"),
    )

    srfNormalX = FloatField()
    snx = srfNormalX

    srfNormalY = FloatField()
    sny = srfNormalY

    srfNormalZ = FloatField()
    snz = srfNormalZ


class SrfNormalAttrOperator(
    Float3CompoundBaseAttrOperator[SrfNormalPlugOperator]
):
    __slots__ = ()

    srfNormalX = FloatField()
    snx = srfNormalX

    srfNormalY = FloatField()
    sny = srfNormalY

    srfNormalZ = FloatField()
    snz = srfNormalZ


class SrfNormalField(
    Float3CompoundBaseField[SrfNormalAttrOperator, SrfNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SrfNormalAttrOperator
    PLUG_CLS = SrfNormalPlugOperator

    srfNormalX = FloatField()
    snx = srfNormalX

    srfNormalY = FloatField()
    sny = srfNormalY

    srfNormalZ = FloatField()
    snz = srfNormalZ


class RefPointObjPlugOperator(
    Float3CompoundBasePlugOperator["RefPointObjAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("refPointObjX", "rox"),
        ("refPointObjY", "roy"),
        ("refPointObjZ", "roz"),
    )

    refPointObjX = FloatField()
    rox = refPointObjX

    refPointObjY = FloatField()
    roy = refPointObjY

    refPointObjZ = FloatField()
    roz = refPointObjZ


class RefPointObjAttrOperator(
    Float3CompoundBaseAttrOperator[RefPointObjPlugOperator]
):
    __slots__ = ()

    refPointObjX = FloatField()
    rox = refPointObjX

    refPointObjY = FloatField()
    roy = refPointObjY

    refPointObjZ = FloatField()
    roz = refPointObjZ


class RefPointObjField(
    Float3CompoundBaseField[RefPointObjAttrOperator, RefPointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RefPointObjAttrOperator
    PLUG_CLS = RefPointObjPlugOperator

    refPointObjX = FloatField()
    rox = refPointObjX

    refPointObjY = FloatField()
    roy = refPointObjY

    refPointObjZ = FloatField()
    roz = refPointObjZ


class RefPointCameraPlugOperator(
    Float3CompoundBasePlugOperator["RefPointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("refPointCameraX", "rcx"),
        ("refPointCameraY", "rcy"),
        ("refPointCameraZ", "rcz"),
    )

    refPointCameraX = FloatField()
    rcx = refPointCameraX

    refPointCameraY = FloatField()
    rcy = refPointCameraY

    refPointCameraZ = FloatField()
    rcz = refPointCameraZ


class RefPointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[RefPointCameraPlugOperator]
):
    __slots__ = ()

    refPointCameraX = FloatField()
    rcx = refPointCameraX

    refPointCameraY = FloatField()
    rcy = refPointCameraY

    refPointCameraZ = FloatField()
    rcz = refPointCameraZ


class RefPointCameraField(
    Float3CompoundBaseField[RefPointCameraAttrOperator, RefPointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RefPointCameraAttrOperator
    PLUG_CLS = RefPointCameraPlugOperator

    refPointCameraX = FloatField()
    rcx = refPointCameraX

    refPointCameraY = FloatField()
    rcy = refPointCameraY

    refPointCameraZ = FloatField()
    rcz = refPointCameraZ


class ImagePlugOperator(
    Float3CompoundBasePlugOperator["ImageAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("imageR", "imr"),
        ("imageG", "img"),
        ("imageB", "imb"),
    )

    imageR = FloatField()
    imr = imageR

    imageG = FloatField()
    img = imageG

    imageB = FloatField()
    imb = imageB


class ImageAttrOperator(
    Float3CompoundBaseAttrOperator[ImagePlugOperator]
):
    __slots__ = ()

    imageR = FloatField()
    imr = imageR

    imageG = FloatField()
    img = imageG

    imageB = FloatField()
    imb = imageB


class ImageField(
    Float3CompoundBaseField[ImageAttrOperator, ImagePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageAttrOperator
    PLUG_CLS = ImagePlugOperator

    imageR = FloatField()
    imr = imageR

    imageG = FloatField()
    img = imageG

    imageB = FloatField()
    imb = imageB


class TransparencyPlugOperator(
    Float3CompoundBasePlugOperator["TransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparencyR", "itr"),
        ("transparencyG", "itg"),
        ("transparencyB", "itb"),
    )

    transparencyR = FloatField()
    itr = transparencyR

    transparencyG = FloatField()
    itg = transparencyG

    transparencyB = FloatField()
    itb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField()
    itr = transparencyR

    transparencyG = FloatField()
    itg = transparencyG

    transparencyB = FloatField()
    itb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField()
    itr = transparencyR

    transparencyG = FloatField()
    itg = transparencyG

    transparencyB = FloatField()
    itb = transparencyB


class RipplesPlugOperator(
    Float3CompoundBasePlugOperator["RipplesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ripplesX", "rx"),
        ("ripplesY", "ry"),
        ("ripplesZ", "rz"),
    )

    ripplesX = FloatField()
    rx = ripplesX

    ripplesY = FloatField()
    ry = ripplesY

    ripplesZ = FloatField()
    rz = ripplesZ


class RipplesAttrOperator(
    Float3CompoundBaseAttrOperator[RipplesPlugOperator]
):
    __slots__ = ()

    ripplesX = FloatField()
    rx = ripplesX

    ripplesY = FloatField()
    ry = ripplesY

    ripplesZ = FloatField()
    rz = ripplesZ


class RipplesField(
    Float3CompoundBaseField[RipplesAttrOperator, RipplesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RipplesAttrOperator
    PLUG_CLS = RipplesPlugOperator

    ripplesX = FloatField()
    rx = ripplesX

    ripplesY = FloatField()
    ry = ripplesY

    ripplesZ = FloatField()
    rz = ripplesZ


class DepthPlugOperator(
    Float2CompoundBasePlugOperator["DepthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("depthMin", "dmn"),
        ("depthMax", "dmx"),
    )

    depthMin = FloatField()
    dmn = depthMin

    depthMax = FloatField()
    dmx = depthMax


class DepthAttrOperator(
    Float2CompoundBaseAttrOperator[DepthPlugOperator]
):
    __slots__ = ()

    depthMin = FloatField()
    dmn = depthMin

    depthMax = FloatField()
    dmx = depthMax


class DepthField(
    Float2CompoundBaseField[DepthAttrOperator, DepthPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DepthAttrOperator
    PLUG_CLS = DepthPlugOperator

    depthMin = FloatField()
    dmn = depthMin

    depthMax = FloatField()
    dmx = depthMax


class CamPosPlugOperator(
    Float3CompoundBasePlugOperator["CamPosAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("camPsX", "cpx"),
        ("camPsY", "cpy"),
        ("camPsZ", "cpz"),
    )

    camPsX = FloatField()
    cpx = camPsX

    camPsY = FloatField()
    cpy = camPsY

    camPsZ = FloatField()
    cpz = camPsZ


class CamPosAttrOperator(
    Float3CompoundBaseAttrOperator[CamPosPlugOperator]
):
    __slots__ = ()

    camPsX = FloatField()
    cpx = camPsX

    camPsY = FloatField()
    cpy = camPsY

    camPsZ = FloatField()
    cpz = camPsZ


class CamPosField(
    Float3CompoundBaseField[CamPosAttrOperator, CamPosPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CamPosAttrOperator
    PLUG_CLS = CamPosPlugOperator

    camPsX = FloatField()
    cpx = camPsX

    camPsY = FloatField()
    cpy = camPsY

    camPsZ = FloatField()
    cpz = camPsZ


class CamAgPlugOperator(
    Float3CompoundBasePlugOperator["CamAgAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("camAngX", "cax"),
        ("camAngY", "cay"),
        ("camAngZ", "caz"),
    )

    camAngX = FloatField()
    cax = camAngX

    camAngY = FloatField()
    cay = camAngY

    camAngZ = FloatField()
    caz = camAngZ


class CamAgAttrOperator(
    Float3CompoundBaseAttrOperator[CamAgPlugOperator]
):
    __slots__ = ()

    camAngX = FloatField()
    cax = camAngX

    camAngY = FloatField()
    cay = camAngY

    camAngZ = FloatField()
    caz = camAngZ


class CamAgField(
    Float3CompoundBaseField[CamAgAttrOperator, CamAgPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CamAgAttrOperator
    PLUG_CLS = CamAgPlugOperator

    camAngX = FloatField()
    cax = camAngX

    camAngY = FloatField()
    cay = camAngY

    camAngZ = FloatField()
    caz = camAngZ


class TransparencyGainPlugOperator(
    Float3CompoundBasePlugOperator["TransparencyGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparencyGainR", "tgr"),
        ("transparencyGainG", "tgg"),
        ("transparencyGainB", "tgb"),
    )

    transparencyGainR = FloatField()
    tgr = transparencyGainR

    transparencyGainG = FloatField()
    tgg = transparencyGainG

    transparencyGainB = FloatField()
    tgb = transparencyGainB


class TransparencyGainAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyGainPlugOperator]
):
    __slots__ = ()

    transparencyGainR = FloatField()
    tgr = transparencyGainR

    transparencyGainG = FloatField()
    tgg = transparencyGainG

    transparencyGainB = FloatField()
    tgb = transparencyGainB


class TransparencyGainField(
    Float3CompoundBaseField[TransparencyGainAttrOperator, TransparencyGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyGainAttrOperator
    PLUG_CLS = TransparencyGainPlugOperator

    transparencyGainR = FloatField()
    tgr = transparencyGainR

    transparencyGainG = FloatField()
    tgg = transparencyGainG

    transparencyGainB = FloatField()
    tgb = transparencyGainB


class TransparencyOffsetPlugOperator(
    Float3CompoundBasePlugOperator["TransparencyOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparencyOffsetR", "tor"),
        ("transparencyOffsetG", "tog"),
        ("transparencyOffsetB", "tob"),
    )

    transparencyOffsetR = FloatField()
    tor = transparencyOffsetR

    transparencyOffsetG = FloatField()
    tog = transparencyOffsetG

    transparencyOffsetB = FloatField()
    tob = transparencyOffsetB


class TransparencyOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyOffsetPlugOperator]
):
    __slots__ = ()

    transparencyOffsetR = FloatField()
    tor = transparencyOffsetR

    transparencyOffsetG = FloatField()
    tog = transparencyOffsetG

    transparencyOffsetB = FloatField()
    tob = transparencyOffsetB


class TransparencyOffsetField(
    Float3CompoundBaseField[TransparencyOffsetAttrOperator, TransparencyOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyOffsetAttrOperator
    PLUG_CLS = TransparencyOffsetPlugOperator

    transparencyOffsetR = FloatField()
    tor = transparencyOffsetR

    transparencyOffsetG = FloatField()
    tog = transparencyOffsetG

    transparencyOffsetB = FloatField()
    tob = transparencyOffsetB


class DefaultTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["DefaultTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("defaultTransparencyR", "dtr"),
        ("defaultTransparencyG", "dtg"),
        ("defaultTransparencyB", "dtb"),
    )

    defaultTransparencyR = FloatField()
    dtr = defaultTransparencyR

    defaultTransparencyG = FloatField()
    dtg = defaultTransparencyG

    defaultTransparencyB = FloatField()
    dtb = defaultTransparencyB


class DefaultTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultTransparencyPlugOperator]
):
    __slots__ = ()

    defaultTransparencyR = FloatField()
    dtr = defaultTransparencyR

    defaultTransparencyG = FloatField()
    dtg = defaultTransparencyG

    defaultTransparencyB = FloatField()
    dtb = defaultTransparencyB


class DefaultTransparencyField(
    Float3CompoundBaseField[DefaultTransparencyAttrOperator, DefaultTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultTransparencyAttrOperator
    PLUG_CLS = DefaultTransparencyPlugOperator

    defaultTransparencyR = FloatField()
    dtr = defaultTransparencyR

    defaultTransparencyG = FloatField()
    dtg = defaultTransparencyG

    defaultTransparencyB = FloatField()
    dtb = defaultTransparencyB


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


class UvCoordPlugOperator(
    Float2CompoundBasePlugOperator["UvCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uCoord", "u"),
        ("vCoord", "v"),
    )

    uCoord = FloatField()
    u = uCoord

    vCoord = FloatField()
    v = vCoord


class UvCoordAttrOperator(
    Float2CompoundBaseAttrOperator[UvCoordPlugOperator]
):
    __slots__ = ()

    uCoord = FloatField()
    u = uCoord

    vCoord = FloatField()
    v = vCoord


class UvCoordField(
    Float2CompoundBaseField[UvCoordAttrOperator, UvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvCoordAttrOperator
    PLUG_CLS = UvCoordPlugOperator

    uCoord = FloatField()
    u = uCoord

    vCoord = FloatField()
    v = vCoord


class VertexCameraOnePlugOperator(
    Float3CompoundBasePlugOperator["VertexCameraOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexCameraOneX", "c1x"),
        ("vertexCameraOneY", "c1y"),
        ("vertexCameraOneZ", "c1z"),
    )

    vertexCameraOneX = FloatField()
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField()
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField()
    c1z = vertexCameraOneZ


class VertexCameraOneAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraOnePlugOperator]
):
    __slots__ = ()

    vertexCameraOneX = FloatField()
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField()
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField()
    c1z = vertexCameraOneZ


class VertexCameraOneField(
    Float3CompoundBaseField[VertexCameraOneAttrOperator, VertexCameraOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraOneAttrOperator
    PLUG_CLS = VertexCameraOnePlugOperator

    vertexCameraOneX = FloatField()
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField()
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField()
    c1z = vertexCameraOneZ


class VertexCameraTwoPlugOperator(
    Float3CompoundBasePlugOperator["VertexCameraTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexCameraTwoX", "c2x"),
        ("vertexCameraTwoY", "c2y"),
        ("vertexCameraTwoZ", "c2z"),
    )

    vertexCameraTwoX = FloatField()
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField()
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField()
    c2z = vertexCameraTwoZ


class VertexCameraTwoAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraTwoPlugOperator]
):
    __slots__ = ()

    vertexCameraTwoX = FloatField()
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField()
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField()
    c2z = vertexCameraTwoZ


class VertexCameraTwoField(
    Float3CompoundBaseField[VertexCameraTwoAttrOperator, VertexCameraTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraTwoAttrOperator
    PLUG_CLS = VertexCameraTwoPlugOperator

    vertexCameraTwoX = FloatField()
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField()
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField()
    c2z = vertexCameraTwoZ


class VertexCameraThreePlugOperator(
    Float3CompoundBasePlugOperator["VertexCameraThreeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexCameraThreeX", "c3x"),
        ("vertexCameraThreeY", "c3y"),
        ("vertexCameraThreeZ", "c3z"),
    )

    vertexCameraThreeX = FloatField()
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField()
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField()
    c3z = vertexCameraThreeZ


class VertexCameraThreeAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraThreePlugOperator]
):
    __slots__ = ()

    vertexCameraThreeX = FloatField()
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField()
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField()
    c3z = vertexCameraThreeZ


class VertexCameraThreeField(
    Float3CompoundBaseField[VertexCameraThreeAttrOperator, VertexCameraThreePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraThreeAttrOperator
    PLUG_CLS = VertexCameraThreePlugOperator

    vertexCameraThreeX = FloatField()
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField()
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField()
    c3z = vertexCameraThreeZ


class VertexUvOnePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvOneU", "t1u"),
        ("vertexUvOneV", "t1v"),
    )

    vertexUvOneU = FloatField()
    t1u = vertexUvOneU

    vertexUvOneV = FloatField()
    t1v = vertexUvOneV


class VertexUvOneAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvOnePlugOperator]
):
    __slots__ = ()

    vertexUvOneU = FloatField()
    t1u = vertexUvOneU

    vertexUvOneV = FloatField()
    t1v = vertexUvOneV


class VertexUvOneField(
    Float2CompoundBaseField[VertexUvOneAttrOperator, VertexUvOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvOneAttrOperator
    PLUG_CLS = VertexUvOnePlugOperator

    vertexUvOneU = FloatField()
    t1u = vertexUvOneU

    vertexUvOneV = FloatField()
    t1v = vertexUvOneV


class VertexUvTwoPlugOperator(
    Float2CompoundBasePlugOperator["VertexUvTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvTwoU", "t2u"),
        ("vertexUvTwoV", "t2v"),
    )

    vertexUvTwoU = FloatField()
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField()
    t2v = vertexUvTwoV


class VertexUvTwoAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvTwoPlugOperator]
):
    __slots__ = ()

    vertexUvTwoU = FloatField()
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField()
    t2v = vertexUvTwoV


class VertexUvTwoField(
    Float2CompoundBaseField[VertexUvTwoAttrOperator, VertexUvTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvTwoAttrOperator
    PLUG_CLS = VertexUvTwoPlugOperator

    vertexUvTwoU = FloatField()
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField()
    t2v = vertexUvTwoV


class VertexUvThreePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvThreeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvThreeU", "t3u"),
        ("vertexUvThreeV", "t3v"),
    )

    vertexUvThreeU = FloatField()
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField()
    t3v = vertexUvThreeV


class VertexUvThreeAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvThreePlugOperator]
):
    __slots__ = ()

    vertexUvThreeU = FloatField()
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField()
    t3v = vertexUvThreeV


class VertexUvThreeField(
    Float2CompoundBaseField[VertexUvThreeAttrOperator, VertexUvThreePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvThreeAttrOperator
    PLUG_CLS = VertexUvThreePlugOperator

    vertexUvThreeU = FloatField()
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField()
    t3v = vertexUvThreeV


class UvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["UvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvFilterSizeX", "ufx"),
        ("uvFilterSizeY", "ufy"),
    )

    uvFilterSizeX = FloatField()
    ufx = uvFilterSizeX

    uvFilterSizeY = FloatField()
    ufy = uvFilterSizeY


class UvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[UvFilterSizePlugOperator]
):
    __slots__ = ()

    uvFilterSizeX = FloatField()
    ufx = uvFilterSizeX

    uvFilterSizeY = FloatField()
    ufy = uvFilterSizeY


class UvFilterSizeField(
    Float2CompoundBaseField[UvFilterSizeAttrOperator, UvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvFilterSizeAttrOperator
    PLUG_CLS = UvFilterSizePlugOperator

    uvFilterSizeX = FloatField()
    ufx = uvFilterSizeX

    uvFilterSizeY = FloatField()
    ufy = uvFilterSizeY


class TangentUCameraPlugOperator(
    Float3CompoundBasePlugOperator["TangentUCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tangentUx", "tux"),
        ("tangentUy", "tuy"),
        ("tangentUz", "tuz"),
    )

    tangentUx = FloatField()
    tux = tangentUx

    tangentUy = FloatField()
    tuy = tangentUy

    tangentUz = FloatField()
    tuz = tangentUz


class TangentUCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TangentUCameraPlugOperator]
):
    __slots__ = ()

    tangentUx = FloatField()
    tux = tangentUx

    tangentUy = FloatField()
    tuy = tangentUy

    tangentUz = FloatField()
    tuz = tangentUz


class TangentUCameraField(
    Float3CompoundBaseField[TangentUCameraAttrOperator, TangentUCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentUCameraAttrOperator
    PLUG_CLS = TangentUCameraPlugOperator

    tangentUx = FloatField()
    tux = tangentUx

    tangentUy = FloatField()
    tuy = tangentUy

    tangentUz = FloatField()
    tuz = tangentUz


class TangentVCameraPlugOperator(
    Float3CompoundBasePlugOperator["TangentVCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tangentVx", "tvx"),
        ("tangentVy", "tvy"),
        ("tangentVz", "tvz"),
    )

    tangentVx = FloatField()
    tvx = tangentVx

    tangentVy = FloatField()
    tvy = tangentVy

    tangentVz = FloatField()
    tvz = tangentVz


class TangentVCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TangentVCameraPlugOperator]
):
    __slots__ = ()

    tangentVx = FloatField()
    tvx = tangentVx

    tangentVy = FloatField()
    tvy = tangentVy

    tangentVz = FloatField()
    tvz = tangentVz


class TangentVCameraField(
    Float3CompoundBaseField[TangentVCameraAttrOperator, TangentVCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentVCameraAttrOperator
    PLUG_CLS = TangentVCameraPlugOperator

    tangentVx = FloatField()
    tvx = tangentVx

    tangentVy = FloatField()
    tvy = tangentVy

    tangentVz = FloatField()
    tvz = tangentVz
