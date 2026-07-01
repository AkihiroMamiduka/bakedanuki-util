# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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


class Weight3dPlugOperator(
    Float3CompoundBasePlugOperator["Weight3dAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weight3dX", "w3x"),
        ("weight3dY", "w3y"),
        ("weight3dZ", "w3z"),
    )

    weight3dX = FloatField()
    w3x = weight3dX

    weight3dY = FloatField()
    w3y = weight3dY

    weight3dZ = FloatField()
    w3z = weight3dZ


class Weight3dAttrOperator(
    Float3CompoundBaseAttrOperator[Weight3dPlugOperator]
):
    __slots__ = ()

    weight3dX = FloatField()
    w3x = weight3dX

    weight3dY = FloatField()
    w3y = weight3dY

    weight3dZ = FloatField()
    w3z = weight3dZ


class Weight3dField(
    Float3CompoundBaseField[Weight3dAttrOperator, Weight3dPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Weight3dAttrOperator
    PLUG_CLS = Weight3dPlugOperator

    weight3dX = FloatField()
    w3x = weight3dX

    weight3dY = FloatField()
    w3y = weight3dY

    weight3dZ = FloatField()
    w3z = weight3dZ
