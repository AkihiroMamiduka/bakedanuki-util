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


class FillerColorPlugOperator(
    Float3CompoundBasePlugOperator["FillerColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fillerColorR", "fcr"),
        ("fillerColorG", "fcg"),
        ("fillerColorB", "fcb"),
    )

    fillerColorR = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fcr = fillerColorR

    fillerColorG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fcg = fillerColorG

    fillerColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fcb = fillerColorB


class FillerColorAttrOperator(
    Float3CompoundBaseAttrOperator[FillerColorPlugOperator]
):
    __slots__ = ()

    fillerColorR = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fcr = fillerColorR

    fillerColorG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fcg = fillerColorG

    fillerColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fcb = fillerColorB


class FillerColorField(
    Float3CompoundBaseField[FillerColorAttrOperator, FillerColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FillerColorAttrOperator
    PLUG_CLS = FillerColorPlugOperator

    fillerColorR = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fcr = fillerColorR

    fillerColorG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fcg = fillerColorG

    fillerColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    fcb = fillerColorB


class VeinColorPlugOperator(
    Float3CompoundBasePlugOperator["VeinColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("veinColorR", "vcr"),
        ("veinColorG", "vcg"),
        ("veinColorB", "vcb"),
    )

    veinColorR = FloatField(default_value=0.2980000078678131, min_value=0.0, max_value=1.0)
    vcr = veinColorR

    veinColorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vcg = veinColorG

    veinColorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vcb = veinColorB


class VeinColorAttrOperator(
    Float3CompoundBaseAttrOperator[VeinColorPlugOperator]
):
    __slots__ = ()

    veinColorR = FloatField(default_value=0.2980000078678131, min_value=0.0, max_value=1.0)
    vcr = veinColorR

    veinColorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vcg = veinColorG

    veinColorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vcb = veinColorB


class VeinColorField(
    Float3CompoundBaseField[VeinColorAttrOperator, VeinColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VeinColorAttrOperator
    PLUG_CLS = VeinColorPlugOperator

    veinColorR = FloatField(default_value=0.2980000078678131, min_value=0.0, max_value=1.0)
    vcr = veinColorR

    veinColorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vcg = veinColorG

    veinColorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    vcb = veinColorB


class RipplesPlugOperator(
    Float3CompoundBasePlugOperator["RipplesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ripplesX", "rx"),
        ("ripplesY", "ry"),
        ("ripplesZ", "rz"),
    )

    ripplesX = FloatField(default_value=1.0, min_value=0.0)
    rx = ripplesX

    ripplesY = FloatField(default_value=1.0, min_value=0.0)
    ry = ripplesY

    ripplesZ = FloatField(default_value=1.0, min_value=0.0)
    rz = ripplesZ


class RipplesAttrOperator(
    Float3CompoundBaseAttrOperator[RipplesPlugOperator]
):
    __slots__ = ()

    ripplesX = FloatField(default_value=1.0, min_value=0.0)
    rx = ripplesX

    ripplesY = FloatField(default_value=1.0, min_value=0.0)
    ry = ripplesY

    ripplesZ = FloatField(default_value=1.0, min_value=0.0)
    rz = ripplesZ


class RipplesField(
    Float3CompoundBaseField[RipplesAttrOperator, RipplesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RipplesAttrOperator
    PLUG_CLS = RipplesPlugOperator

    ripplesX = FloatField(default_value=1.0, min_value=0.0)
    rx = ripplesX

    ripplesY = FloatField(default_value=1.0, min_value=0.0)
    ry = ripplesY

    ripplesZ = FloatField(default_value=1.0, min_value=0.0)
    rz = ripplesZ


class DepthPlugOperator(
    Float2CompoundBasePlugOperator["DepthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("depthMin", "dmn"),
        ("depthMax", "dmx"),
    )

    depthMin = FloatField(default_value=0.0, min_value=0.0)
    dmn = depthMin

    depthMax = FloatField(default_value=20.0, min_value=0.0)
    dmx = depthMax


class DepthAttrOperator(
    Float2CompoundBaseAttrOperator[DepthPlugOperator]
):
    __slots__ = ()

    depthMin = FloatField(default_value=0.0, min_value=0.0)
    dmn = depthMin

    depthMax = FloatField(default_value=20.0, min_value=0.0)
    dmx = depthMax


class DepthField(
    Float2CompoundBaseField[DepthAttrOperator, DepthPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DepthAttrOperator
    PLUG_CLS = DepthPlugOperator

    depthMin = FloatField(default_value=0.0, min_value=0.0)
    dmn = depthMin

    depthMax = FloatField(default_value=20.0, min_value=0.0)
    dmx = depthMax
