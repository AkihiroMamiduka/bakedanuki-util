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


class FillerColorPlugOperator(
    Float3CompoundBasePlugOperator["FillerColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fillerColorR", "fcr"),
        ("fillerColorG", "fcg"),
        ("fillerColorB", "fcb"),
    )

    fillerColorR = FloatField()
    fcr = fillerColorR

    fillerColorG = FloatField()
    fcg = fillerColorG

    fillerColorB = FloatField()
    fcb = fillerColorB


class FillerColorAttrOperator(
    Float3CompoundBaseAttrOperator[FillerColorPlugOperator]
):
    __slots__ = ()

    fillerColorR = FloatField()
    fcr = fillerColorR

    fillerColorG = FloatField()
    fcg = fillerColorG

    fillerColorB = FloatField()
    fcb = fillerColorB


class FillerColorField(
    Float3CompoundBaseField[FillerColorAttrOperator, FillerColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FillerColorAttrOperator
    PLUG_CLS = FillerColorPlugOperator

    fillerColorR = FloatField()
    fcr = fillerColorR

    fillerColorG = FloatField()
    fcg = fillerColorG

    fillerColorB = FloatField()
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

    veinColorR = FloatField()
    vcr = veinColorR

    veinColorG = FloatField()
    vcg = veinColorG

    veinColorB = FloatField()
    vcb = veinColorB


class VeinColorAttrOperator(
    Float3CompoundBaseAttrOperator[VeinColorPlugOperator]
):
    __slots__ = ()

    veinColorR = FloatField()
    vcr = veinColorR

    veinColorG = FloatField()
    vcg = veinColorG

    veinColorB = FloatField()
    vcb = veinColorB


class VeinColorField(
    Float3CompoundBaseField[VeinColorAttrOperator, VeinColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VeinColorAttrOperator
    PLUG_CLS = VeinColorPlugOperator

    veinColorR = FloatField()
    vcr = veinColorR

    veinColorG = FloatField()
    vcg = veinColorG

    veinColorB = FloatField()
    vcb = veinColorB


class GrainColorPlugOperator(
    Float3CompoundBasePlugOperator["GrainColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("grainColorR", "gcr"),
        ("grainColorG", "gcg"),
        ("grainColorB", "gcb"),
    )

    grainColorR = FloatField()
    gcr = grainColorR

    grainColorG = FloatField()
    gcg = grainColorG

    grainColorB = FloatField()
    gcb = grainColorB


class GrainColorAttrOperator(
    Float3CompoundBaseAttrOperator[GrainColorPlugOperator]
):
    __slots__ = ()

    grainColorR = FloatField()
    gcr = grainColorR

    grainColorG = FloatField()
    gcg = grainColorG

    grainColorB = FloatField()
    gcb = grainColorB


class GrainColorField(
    Float3CompoundBaseField[GrainColorAttrOperator, GrainColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GrainColorAttrOperator
    PLUG_CLS = GrainColorPlugOperator

    grainColorR = FloatField()
    gcr = grainColorR

    grainColorG = FloatField()
    gcg = grainColorG

    grainColorB = FloatField()
    gcb = grainColorB


class CenterPlugOperator(
    Float2CompoundBasePlugOperator["CenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centerU", "cu"),
        ("centerV", "cv"),
    )

    centerU = FloatField()
    cu = centerU

    centerV = FloatField()
    cv = centerV


class CenterAttrOperator(
    Float2CompoundBaseAttrOperator[CenterPlugOperator]
):
    __slots__ = ()

    centerU = FloatField()
    cu = centerU

    centerV = FloatField()
    cv = centerV


class CenterField(
    Float2CompoundBaseField[CenterAttrOperator, CenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CenterAttrOperator
    PLUG_CLS = CenterPlugOperator

    centerU = FloatField()
    cu = centerU

    centerV = FloatField()
    cv = centerV


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
