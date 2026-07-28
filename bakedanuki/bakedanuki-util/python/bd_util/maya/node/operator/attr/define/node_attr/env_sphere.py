# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)


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


class RayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["RayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayDirectionX", "rx"),
        ("rayDirectionY", "ry"),
        ("rayDirectionZ", "rz"),
    )

    rayDirectionX = FloatField(default_value=0.0)
    rx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0)
    ry = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0)
    rz = rayDirectionZ


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirectionX = FloatField(default_value=0.0)
    rx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0)
    ry = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0)
    rz = rayDirectionZ


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirectionX = FloatField(default_value=0.0)
    rx = rayDirectionX

    rayDirectionY = FloatField(default_value=0.0)
    ry = rayDirectionY

    rayDirectionZ = FloatField(default_value=1.0)
    rz = rayDirectionZ


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


class UvCoordAttrOperator(Float2CompoundBaseAttrOperator[UvCoordPlugOperator]):
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
    Float3CompoundBaseField[
        RefPointCameraAttrOperator, RefPointCameraPlugOperator
    ]
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


class ImagePlugOperator(Float3CompoundBasePlugOperator["ImageAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("imageR", "sor"),
        ("imageG", "sog"),
        ("imageB", "sob"),
    )

    imageR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    sor = imageR

    imageG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    sog = imageG

    imageB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    sob = imageB


class ImageAttrOperator(Float3CompoundBaseAttrOperator[ImagePlugOperator]):
    __slots__ = ()

    imageR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    sor = imageR

    imageG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    sog = imageG

    imageB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    sob = imageB


class ImageField(
    Float3CompoundBaseField[ImageAttrOperator, ImagePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageAttrOperator
    PLUG_CLS = ImagePlugOperator

    imageR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    sor = imageR

    imageG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    sog = imageG

    imageB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    sob = imageB


class ShearUVPlugOperator(
    Float2CompoundBasePlugOperator["ShearUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shearU", "su"),
        ("shearV", "sv"),
    )

    shearU = FloatField(default_value=0.0, min_value=-10.0, max_value=10.0)
    su = shearU

    shearV = FloatField(default_value=0.0, min_value=-10.0, max_value=10.0)
    sv = shearV


class ShearUVAttrOperator(Float2CompoundBaseAttrOperator[ShearUVPlugOperator]):
    __slots__ = ()

    shearU = FloatField(default_value=0.0, min_value=-10.0, max_value=10.0)
    su = shearU

    shearV = FloatField(default_value=0.0, min_value=-10.0, max_value=10.0)
    sv = shearV


class ShearUVField(
    Float2CompoundBaseField[ShearUVAttrOperator, ShearUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShearUVAttrOperator
    PLUG_CLS = ShearUVPlugOperator

    shearU = FloatField(default_value=0.0, min_value=-10.0, max_value=10.0)
    su = shearU

    shearV = FloatField(default_value=0.0, min_value=-10.0, max_value=10.0)
    sv = shearV
