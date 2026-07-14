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

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    poz = pointObjZ


class PointObjAttrOperator(
    Float3CompoundBaseAttrOperator[PointObjPlugOperator]
):
    __slots__ = ()

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    poz = pointObjZ


class PointObjField(
    Float3CompoundBaseField[PointObjAttrOperator, PointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointObjAttrOperator
    PLUG_CLS = PointObjPlugOperator

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
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

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField(default_value=0.0)
    px = pointCameraX

    pointCameraY = FloatField(default_value=0.0)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=0.0)
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

    filterSizeX = FloatField(default_value=0.0)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0)
    fsz = filterSizeZ


class FilterSizeAttrOperator(
    Float3CompoundBaseAttrOperator[FilterSizePlugOperator]
):
    __slots__ = ()

    filterSizeX = FloatField(default_value=0.0)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0)
    fsz = filterSizeZ


class FilterSizeField(
    Float3CompoundBaseField[FilterSizeAttrOperator, FilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterSizeAttrOperator
    PLUG_CLS = FilterSizePlugOperator

    filterSizeX = FloatField(default_value=0.0)
    fsx = filterSizeX

    filterSizeY = FloatField(default_value=0.0)
    fsy = filterSizeY

    filterSizeZ = FloatField(default_value=0.0)
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

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgb = colorGainB


class ColorGainAttrOperator(
    Float3CompoundBaseAttrOperator[ColorGainPlugOperator]
):
    __slots__ = ()

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgb = colorGainB


class ColorGainField(
    Float3CompoundBaseField[ColorGainAttrOperator, ColorGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorGainAttrOperator
    PLUG_CLS = ColorGainPlugOperator

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
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

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cob = colorOffsetB


class ColorOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ColorOffsetPlugOperator]
):
    __slots__ = ()

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cob = colorOffsetB


class ColorOffsetField(
    Float3CompoundBaseField[ColorOffsetAttrOperator, ColorOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorOffsetAttrOperator
    PLUG_CLS = ColorOffsetPlugOperator

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
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

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcb = defaultColorB


class DefaultColorAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultColorPlugOperator]
):
    __slots__ = ()

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcb = defaultColorB


class DefaultColorField(
    Float3CompoundBaseField[DefaultColorAttrOperator, DefaultColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultColorAttrOperator
    PLUG_CLS = DefaultColorPlugOperator

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
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


class NormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["NormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalCameraX", "nx"),
        ("normalCameraY", "ny"),
        ("normalCameraZ", "nz"),
    )

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField(default_value=0.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=0.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
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

    srfNormalX = FloatField(default_value=0.0)
    snx = srfNormalX

    srfNormalY = FloatField(default_value=0.0)
    sny = srfNormalY

    srfNormalZ = FloatField(default_value=1.0)
    snz = srfNormalZ


class SrfNormalAttrOperator(
    Float3CompoundBaseAttrOperator[SrfNormalPlugOperator]
):
    __slots__ = ()

    srfNormalX = FloatField(default_value=0.0)
    snx = srfNormalX

    srfNormalY = FloatField(default_value=0.0)
    sny = srfNormalY

    srfNormalZ = FloatField(default_value=1.0)
    snz = srfNormalZ


class SrfNormalField(
    Float3CompoundBaseField[SrfNormalAttrOperator, SrfNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SrfNormalAttrOperator
    PLUG_CLS = SrfNormalPlugOperator

    srfNormalX = FloatField(default_value=0.0)
    snx = srfNormalX

    srfNormalY = FloatField(default_value=0.0)
    sny = srfNormalY

    srfNormalZ = FloatField(default_value=1.0)
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

    refPointObjX = FloatField(default_value=0.0)
    rox = refPointObjX

    refPointObjY = FloatField(default_value=0.0)
    roy = refPointObjY

    refPointObjZ = FloatField(default_value=0.0)
    roz = refPointObjZ


class RefPointObjAttrOperator(
    Float3CompoundBaseAttrOperator[RefPointObjPlugOperator]
):
    __slots__ = ()

    refPointObjX = FloatField(default_value=0.0)
    rox = refPointObjX

    refPointObjY = FloatField(default_value=0.0)
    roy = refPointObjY

    refPointObjZ = FloatField(default_value=0.0)
    roz = refPointObjZ


class RefPointObjField(
    Float3CompoundBaseField[RefPointObjAttrOperator, RefPointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RefPointObjAttrOperator
    PLUG_CLS = RefPointObjPlugOperator

    refPointObjX = FloatField(default_value=0.0)
    rox = refPointObjX

    refPointObjY = FloatField(default_value=0.0)
    roy = refPointObjY

    refPointObjZ = FloatField(default_value=0.0)
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

    refPointCameraX = FloatField(default_value=0.0)
    rcx = refPointCameraX

    refPointCameraY = FloatField(default_value=0.0)
    rcy = refPointCameraY

    refPointCameraZ = FloatField(default_value=0.0)
    rcz = refPointCameraZ


class RefPointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[RefPointCameraPlugOperator]
):
    __slots__ = ()

    refPointCameraX = FloatField(default_value=0.0)
    rcx = refPointCameraX

    refPointCameraY = FloatField(default_value=0.0)
    rcy = refPointCameraY

    refPointCameraZ = FloatField(default_value=0.0)
    rcz = refPointCameraZ


class RefPointCameraField(
    Float3CompoundBaseField[RefPointCameraAttrOperator, RefPointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RefPointCameraAttrOperator
    PLUG_CLS = RefPointCameraPlugOperator

    refPointCameraX = FloatField(default_value=0.0)
    rcx = refPointCameraX

    refPointCameraY = FloatField(default_value=0.0)
    rcy = refPointCameraY

    refPointCameraZ = FloatField(default_value=0.0)
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

    imageR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    imr = imageR

    imageG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    img = imageG

    imageB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    imb = imageB


class ImageAttrOperator(
    Float3CompoundBaseAttrOperator[ImagePlugOperator]
):
    __slots__ = ()

    imageR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    imr = imageR

    imageG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    img = imageG

    imageB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    imb = imageB


class ImageField(
    Float3CompoundBaseField[ImageAttrOperator, ImagePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageAttrOperator
    PLUG_CLS = ImagePlugOperator

    imageR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    imr = imageR

    imageG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    img = imageG

    imageB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
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

    transparencyR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    itr = transparencyR

    transparencyG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    itg = transparencyG

    transparencyB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    itb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    itr = transparencyR

    transparencyG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    itg = transparencyG

    transparencyB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    itb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    itr = transparencyR

    transparencyG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    itg = transparencyG

    transparencyB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
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

    ripplesX = FloatField(default_value=1.0, min_value=0.0, max_value=20.0)
    rx = ripplesX

    ripplesY = FloatField(default_value=1.0, min_value=0.0, max_value=20.0)
    ry = ripplesY

    ripplesZ = FloatField(default_value=1.0, min_value=0.0, max_value=20.0)
    rz = ripplesZ


class RipplesAttrOperator(
    Float3CompoundBaseAttrOperator[RipplesPlugOperator]
):
    __slots__ = ()

    ripplesX = FloatField(default_value=1.0, min_value=0.0, max_value=20.0)
    rx = ripplesX

    ripplesY = FloatField(default_value=1.0, min_value=0.0, max_value=20.0)
    ry = ripplesY

    ripplesZ = FloatField(default_value=1.0, min_value=0.0, max_value=20.0)
    rz = ripplesZ


class RipplesField(
    Float3CompoundBaseField[RipplesAttrOperator, RipplesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RipplesAttrOperator
    PLUG_CLS = RipplesPlugOperator

    ripplesX = FloatField(default_value=1.0, min_value=0.0, max_value=20.0)
    rx = ripplesX

    ripplesY = FloatField(default_value=1.0, min_value=0.0, max_value=20.0)
    ry = ripplesY

    ripplesZ = FloatField(default_value=1.0, min_value=0.0, max_value=20.0)
    rz = ripplesZ


class DepthPlugOperator(
    Float2CompoundBasePlugOperator["DepthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("depthMin", "dmn"),
        ("depthMax", "dmx"),
    )

    depthMin = FloatField(default_value=0.0, min_value=0.0, max_value=25.0)
    dmn = depthMin

    depthMax = FloatField(default_value=10.0, min_value=0.0, max_value=25.0)
    dmx = depthMax


class DepthAttrOperator(
    Float2CompoundBaseAttrOperator[DepthPlugOperator]
):
    __slots__ = ()

    depthMin = FloatField(default_value=0.0, min_value=0.0, max_value=25.0)
    dmn = depthMin

    depthMax = FloatField(default_value=10.0, min_value=0.0, max_value=25.0)
    dmx = depthMax


class DepthField(
    Float2CompoundBaseField[DepthAttrOperator, DepthPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DepthAttrOperator
    PLUG_CLS = DepthPlugOperator

    depthMin = FloatField(default_value=0.0, min_value=0.0, max_value=25.0)
    dmn = depthMin

    depthMax = FloatField(default_value=10.0, min_value=0.0, max_value=25.0)
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

    camPsX = FloatField(default_value=0.0)
    cpx = camPsX

    camPsY = FloatField(default_value=0.0)
    cpy = camPsY

    camPsZ = FloatField(default_value=0.0)
    cpz = camPsZ


class CamPosAttrOperator(
    Float3CompoundBaseAttrOperator[CamPosPlugOperator]
):
    __slots__ = ()

    camPsX = FloatField(default_value=0.0)
    cpx = camPsX

    camPsY = FloatField(default_value=0.0)
    cpy = camPsY

    camPsZ = FloatField(default_value=0.0)
    cpz = camPsZ


class CamPosField(
    Float3CompoundBaseField[CamPosAttrOperator, CamPosPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CamPosAttrOperator
    PLUG_CLS = CamPosPlugOperator

    camPsX = FloatField(default_value=0.0)
    cpx = camPsX

    camPsY = FloatField(default_value=0.0)
    cpy = camPsY

    camPsZ = FloatField(default_value=0.0)
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

    camAngX = FloatField(default_value=0.0)
    cax = camAngX

    camAngY = FloatField(default_value=0.0)
    cay = camAngY

    camAngZ = FloatField(default_value=0.0)
    caz = camAngZ


class CamAgAttrOperator(
    Float3CompoundBaseAttrOperator[CamAgPlugOperator]
):
    __slots__ = ()

    camAngX = FloatField(default_value=0.0)
    cax = camAngX

    camAngY = FloatField(default_value=0.0)
    cay = camAngY

    camAngZ = FloatField(default_value=0.0)
    caz = camAngZ


class CamAgField(
    Float3CompoundBaseField[CamAgAttrOperator, CamAgPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CamAgAttrOperator
    PLUG_CLS = CamAgPlugOperator

    camAngX = FloatField(default_value=0.0)
    cax = camAngX

    camAngY = FloatField(default_value=0.0)
    cay = camAngY

    camAngZ = FloatField(default_value=0.0)
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

    transparencyGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    tgr = transparencyGainR

    transparencyGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    tgg = transparencyGainG

    transparencyGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    tgb = transparencyGainB


class TransparencyGainAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyGainPlugOperator]
):
    __slots__ = ()

    transparencyGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    tgr = transparencyGainR

    transparencyGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    tgg = transparencyGainG

    transparencyGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    tgb = transparencyGainB


class TransparencyGainField(
    Float3CompoundBaseField[TransparencyGainAttrOperator, TransparencyGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyGainAttrOperator
    PLUG_CLS = TransparencyGainPlugOperator

    transparencyGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    tgr = transparencyGainR

    transparencyGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    tgg = transparencyGainG

    transparencyGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
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

    transparencyOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    tor = transparencyOffsetR

    transparencyOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    tog = transparencyOffsetG

    transparencyOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    tob = transparencyOffsetB


class TransparencyOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyOffsetPlugOperator]
):
    __slots__ = ()

    transparencyOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    tor = transparencyOffsetR

    transparencyOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    tog = transparencyOffsetG

    transparencyOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    tob = transparencyOffsetB


class TransparencyOffsetField(
    Float3CompoundBaseField[TransparencyOffsetAttrOperator, TransparencyOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyOffsetAttrOperator
    PLUG_CLS = TransparencyOffsetPlugOperator

    transparencyOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    tor = transparencyOffsetR

    transparencyOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    tog = transparencyOffsetG

    transparencyOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
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

    defaultTransparencyR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    dtr = defaultTransparencyR

    defaultTransparencyG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    dtg = defaultTransparencyG

    defaultTransparencyB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    dtb = defaultTransparencyB


class DefaultTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultTransparencyPlugOperator]
):
    __slots__ = ()

    defaultTransparencyR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    dtr = defaultTransparencyR

    defaultTransparencyG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    dtg = defaultTransparencyG

    defaultTransparencyB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    dtb = defaultTransparencyB


class DefaultTransparencyField(
    Float3CompoundBaseField[DefaultTransparencyAttrOperator, DefaultTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultTransparencyAttrOperator
    PLUG_CLS = DefaultTransparencyPlugOperator

    defaultTransparencyR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    dtr = defaultTransparencyR

    defaultTransparencyG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    dtg = defaultTransparencyG

    defaultTransparencyB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
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
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
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


class UvCoordPlugOperator(
    Float2CompoundBasePlugOperator["UvCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uCoord", "u"),
        ("vCoord", "v"),
    )

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvCoordAttrOperator(
    Float2CompoundBaseAttrOperator[UvCoordPlugOperator]
):
    __slots__ = ()

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvCoordField(
    Float2CompoundBaseField[UvCoordAttrOperator, UvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvCoordAttrOperator
    PLUG_CLS = UvCoordPlugOperator

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
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

    vertexCameraOneX = FloatField(default_value=0.0)
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField(default_value=0.0)
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField(default_value=0.0)
    c1z = vertexCameraOneZ


class VertexCameraOneAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraOnePlugOperator]
):
    __slots__ = ()

    vertexCameraOneX = FloatField(default_value=0.0)
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField(default_value=0.0)
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField(default_value=0.0)
    c1z = vertexCameraOneZ


class VertexCameraOneField(
    Float3CompoundBaseField[VertexCameraOneAttrOperator, VertexCameraOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraOneAttrOperator
    PLUG_CLS = VertexCameraOnePlugOperator

    vertexCameraOneX = FloatField(default_value=0.0)
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField(default_value=0.0)
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField(default_value=0.0)
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

    vertexCameraTwoX = FloatField(default_value=0.0)
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField(default_value=0.0)
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField(default_value=0.0)
    c2z = vertexCameraTwoZ


class VertexCameraTwoAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraTwoPlugOperator]
):
    __slots__ = ()

    vertexCameraTwoX = FloatField(default_value=0.0)
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField(default_value=0.0)
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField(default_value=0.0)
    c2z = vertexCameraTwoZ


class VertexCameraTwoField(
    Float3CompoundBaseField[VertexCameraTwoAttrOperator, VertexCameraTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraTwoAttrOperator
    PLUG_CLS = VertexCameraTwoPlugOperator

    vertexCameraTwoX = FloatField(default_value=0.0)
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField(default_value=0.0)
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField(default_value=0.0)
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

    vertexCameraThreeX = FloatField(default_value=0.0)
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField(default_value=0.0)
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField(default_value=0.0)
    c3z = vertexCameraThreeZ


class VertexCameraThreeAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraThreePlugOperator]
):
    __slots__ = ()

    vertexCameraThreeX = FloatField(default_value=0.0)
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField(default_value=0.0)
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField(default_value=0.0)
    c3z = vertexCameraThreeZ


class VertexCameraThreeField(
    Float3CompoundBaseField[VertexCameraThreeAttrOperator, VertexCameraThreePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraThreeAttrOperator
    PLUG_CLS = VertexCameraThreePlugOperator

    vertexCameraThreeX = FloatField(default_value=0.0)
    c3x = vertexCameraThreeX

    vertexCameraThreeY = FloatField(default_value=0.0)
    c3y = vertexCameraThreeY

    vertexCameraThreeZ = FloatField(default_value=0.0)
    c3z = vertexCameraThreeZ


class VertexUvOnePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvOneU", "t1u"),
        ("vertexUvOneV", "t1v"),
    )

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvOneAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvOnePlugOperator]
):
    __slots__ = ()

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvOneField(
    Float2CompoundBaseField[VertexUvOneAttrOperator, VertexUvOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvOneAttrOperator
    PLUG_CLS = VertexUvOnePlugOperator

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvTwoPlugOperator(
    Float2CompoundBasePlugOperator["VertexUvTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvTwoU", "t2u"),
        ("vertexUvTwoV", "t2v"),
    )

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvTwoAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvTwoPlugOperator]
):
    __slots__ = ()

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvTwoField(
    Float2CompoundBaseField[VertexUvTwoAttrOperator, VertexUvTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvTwoAttrOperator
    PLUG_CLS = VertexUvTwoPlugOperator

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvThreePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvThreeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvThreeU", "t3u"),
        ("vertexUvThreeV", "t3v"),
    )

    vertexUvThreeU = FloatField(default_value=0.0)
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField(default_value=0.0)
    t3v = vertexUvThreeV


class VertexUvThreeAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvThreePlugOperator]
):
    __slots__ = ()

    vertexUvThreeU = FloatField(default_value=0.0)
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField(default_value=0.0)
    t3v = vertexUvThreeV


class VertexUvThreeField(
    Float2CompoundBaseField[VertexUvThreeAttrOperator, VertexUvThreePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvThreeAttrOperator
    PLUG_CLS = VertexUvThreePlugOperator

    vertexUvThreeU = FloatField(default_value=0.0)
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField(default_value=0.0)
    t3v = vertexUvThreeV


class UvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["UvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvFilterSizeX", "ufx"),
        ("uvFilterSizeY", "ufy"),
    )

    uvFilterSizeX = FloatField(default_value=0.0)
    ufx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    ufy = uvFilterSizeY


class UvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[UvFilterSizePlugOperator]
):
    __slots__ = ()

    uvFilterSizeX = FloatField(default_value=0.0)
    ufx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    ufy = uvFilterSizeY


class UvFilterSizeField(
    Float2CompoundBaseField[UvFilterSizeAttrOperator, UvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvFilterSizeAttrOperator
    PLUG_CLS = UvFilterSizePlugOperator

    uvFilterSizeX = FloatField(default_value=0.0)
    ufx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
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

    tangentUx = FloatField(default_value=1.0)
    tux = tangentUx

    tangentUy = FloatField(default_value=0.0)
    tuy = tangentUy

    tangentUz = FloatField(default_value=0.0)
    tuz = tangentUz


class TangentUCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TangentUCameraPlugOperator]
):
    __slots__ = ()

    tangentUx = FloatField(default_value=1.0)
    tux = tangentUx

    tangentUy = FloatField(default_value=0.0)
    tuy = tangentUy

    tangentUz = FloatField(default_value=0.0)
    tuz = tangentUz


class TangentUCameraField(
    Float3CompoundBaseField[TangentUCameraAttrOperator, TangentUCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentUCameraAttrOperator
    PLUG_CLS = TangentUCameraPlugOperator

    tangentUx = FloatField(default_value=1.0)
    tux = tangentUx

    tangentUy = FloatField(default_value=0.0)
    tuy = tangentUy

    tangentUz = FloatField(default_value=0.0)
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

    tangentVx = FloatField(default_value=0.0)
    tvx = tangentVx

    tangentVy = FloatField(default_value=1.0)
    tvy = tangentVy

    tangentVz = FloatField(default_value=0.0)
    tvz = tangentVz


class TangentVCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TangentVCameraPlugOperator]
):
    __slots__ = ()

    tangentVx = FloatField(default_value=0.0)
    tvx = tangentVx

    tangentVy = FloatField(default_value=1.0)
    tvy = tangentVy

    tangentVz = FloatField(default_value=0.0)
    tvz = tangentVz


class TangentVCameraField(
    Float3CompoundBaseField[TangentVCameraAttrOperator, TangentVCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentVCameraAttrOperator
    PLUG_CLS = TangentVCameraPlugOperator

    tangentVx = FloatField(default_value=0.0)
    tvx = tangentVx

    tangentVy = FloatField(default_value=1.0)
    tvy = tangentVy

    tangentVz = FloatField(default_value=0.0)
    tvz = tangentVz
