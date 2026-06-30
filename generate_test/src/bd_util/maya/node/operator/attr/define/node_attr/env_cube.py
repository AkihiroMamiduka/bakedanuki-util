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


class RayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["RayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayDirectionX", "rx"),
        ("rayDirectionY", "ry"),
        ("rayDirectionZ", "rz"),
    )

    rayDirectionX = FloatField()
    rx = rayDirectionX

    rayDirectionY = FloatField()
    ry = rayDirectionY

    rayDirectionZ = FloatField()
    rz = rayDirectionZ


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirectionX = FloatField()
    rx = rayDirectionX

    rayDirectionY = FloatField()
    ry = rayDirectionY

    rayDirectionZ = FloatField()
    rz = rayDirectionZ


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirectionX = FloatField()
    rx = rayDirectionX

    rayDirectionY = FloatField()
    ry = rayDirectionY

    rayDirectionZ = FloatField()
    rz = rayDirectionZ


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


class PointWorldPlugOperator(
    Float3CompoundBasePlugOperator["PointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointWorldX", "pwx"),
        ("pointWorldY", "pwy"),
        ("pointWorldZ", "pwz"),
    )

    pointWorldX = FloatField()
    pwx = pointWorldX

    pointWorldY = FloatField()
    pwy = pointWorldY

    pointWorldZ = FloatField()
    pwz = pointWorldZ


class PointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[PointWorldPlugOperator]
):
    __slots__ = ()

    pointWorldX = FloatField()
    pwx = pointWorldX

    pointWorldY = FloatField()
    pwy = pointWorldY

    pointWorldZ = FloatField()
    pwz = pointWorldZ


class PointWorldField(
    Float3CompoundBaseField[PointWorldAttrOperator, PointWorldPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointWorldAttrOperator
    PLUG_CLS = PointWorldPlugOperator

    pointWorldX = FloatField()
    pwx = pointWorldX

    pointWorldY = FloatField()
    pwy = pointWorldY

    pointWorldZ = FloatField()
    pwz = pointWorldZ


class LeftPlugOperator(
    Float3CompoundBasePlugOperator["LeftAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leftR", "ler"),
        ("leftG", "leg"),
        ("leftB", "leb"),
    )

    leftR = FloatField()
    ler = leftR

    leftG = FloatField()
    leg = leftG

    leftB = FloatField()
    leb = leftB


class LeftAttrOperator(
    Float3CompoundBaseAttrOperator[LeftPlugOperator]
):
    __slots__ = ()

    leftR = FloatField()
    ler = leftR

    leftG = FloatField()
    leg = leftG

    leftB = FloatField()
    leb = leftB


class LeftField(
    Float3CompoundBaseField[LeftAttrOperator, LeftPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftAttrOperator
    PLUG_CLS = LeftPlugOperator

    leftR = FloatField()
    ler = leftR

    leftG = FloatField()
    leg = leftG

    leftB = FloatField()
    leb = leftB


class RightPlugOperator(
    Float3CompoundBasePlugOperator["RightAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rightR", "rir"),
        ("rightG", "rig"),
        ("rightB", "rib"),
    )

    rightR = FloatField()
    rir = rightR

    rightG = FloatField()
    rig = rightG

    rightB = FloatField()
    rib = rightB


class RightAttrOperator(
    Float3CompoundBaseAttrOperator[RightPlugOperator]
):
    __slots__ = ()

    rightR = FloatField()
    rir = rightR

    rightG = FloatField()
    rig = rightG

    rightB = FloatField()
    rib = rightB


class RightField(
    Float3CompoundBaseField[RightAttrOperator, RightPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightAttrOperator
    PLUG_CLS = RightPlugOperator

    rightR = FloatField()
    rir = rightR

    rightG = FloatField()
    rig = rightG

    rightB = FloatField()
    rib = rightB


class TopPlugOperator(
    Float3CompoundBasePlugOperator["TopAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("topR", "tor"),
        ("topG", "tog"),
        ("topB", "tob"),
    )

    topR = FloatField()
    tor = topR

    topG = FloatField()
    tog = topG

    topB = FloatField()
    tob = topB


class TopAttrOperator(
    Float3CompoundBaseAttrOperator[TopPlugOperator]
):
    __slots__ = ()

    topR = FloatField()
    tor = topR

    topG = FloatField()
    tog = topG

    topB = FloatField()
    tob = topB


class TopField(
    Float3CompoundBaseField[TopAttrOperator, TopPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TopAttrOperator
    PLUG_CLS = TopPlugOperator

    topR = FloatField()
    tor = topR

    topG = FloatField()
    tog = topG

    topB = FloatField()
    tob = topB


class BottomPlugOperator(
    Float3CompoundBasePlugOperator["BottomAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bottomR", "bor"),
        ("bottomG", "bog"),
        ("bottomB", "bob"),
    )

    bottomR = FloatField()
    bor = bottomR

    bottomG = FloatField()
    bog = bottomG

    bottomB = FloatField()
    bob = bottomB


class BottomAttrOperator(
    Float3CompoundBaseAttrOperator[BottomPlugOperator]
):
    __slots__ = ()

    bottomR = FloatField()
    bor = bottomR

    bottomG = FloatField()
    bog = bottomG

    bottomB = FloatField()
    bob = bottomB


class BottomField(
    Float3CompoundBaseField[BottomAttrOperator, BottomPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BottomAttrOperator
    PLUG_CLS = BottomPlugOperator

    bottomR = FloatField()
    bor = bottomR

    bottomG = FloatField()
    bog = bottomG

    bottomB = FloatField()
    bob = bottomB


class FrontPlugOperator(
    Float3CompoundBasePlugOperator["FrontAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frontR", "frr"),
        ("frontG", "frg"),
        ("frontB", "frb"),
    )

    frontR = FloatField()
    frr = frontR

    frontG = FloatField()
    frg = frontG

    frontB = FloatField()
    frb = frontB


class FrontAttrOperator(
    Float3CompoundBaseAttrOperator[FrontPlugOperator]
):
    __slots__ = ()

    frontR = FloatField()
    frr = frontR

    frontG = FloatField()
    frg = frontG

    frontB = FloatField()
    frb = frontB


class FrontField(
    Float3CompoundBaseField[FrontAttrOperator, FrontPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrontAttrOperator
    PLUG_CLS = FrontPlugOperator

    frontR = FloatField()
    frr = frontR

    frontG = FloatField()
    frg = frontG

    frontB = FloatField()
    frb = frontB


class BackPlugOperator(
    Float3CompoundBasePlugOperator["BackAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backR", "bar"),
        ("backG", "bag"),
        ("backB", "bab"),
    )

    backR = FloatField()
    bar = backR

    backG = FloatField()
    bag = backG

    backB = FloatField()
    bab = backB


class BackAttrOperator(
    Float3CompoundBaseAttrOperator[BackPlugOperator]
):
    __slots__ = ()

    backR = FloatField()
    bar = backR

    backG = FloatField()
    bag = backG

    backB = FloatField()
    bab = backB


class BackField(
    Float3CompoundBaseField[BackAttrOperator, BackPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackAttrOperator
    PLUG_CLS = BackPlugOperator

    backR = FloatField()
    bar = backR

    backG = FloatField()
    bag = backG

    backB = FloatField()
    bab = backB
