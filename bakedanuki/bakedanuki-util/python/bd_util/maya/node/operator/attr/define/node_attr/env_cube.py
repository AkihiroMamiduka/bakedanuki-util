# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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


class PointWorldPlugOperator(
    Float3CompoundBasePlugOperator["PointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointWorldX", "pwx"),
        ("pointWorldY", "pwy"),
        ("pointWorldZ", "pwz"),
    )

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class PointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[PointWorldPlugOperator]
):
    __slots__ = ()

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class PointWorldField(
    Float3CompoundBaseField[PointWorldAttrOperator, PointWorldPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointWorldAttrOperator
    PLUG_CLS = PointWorldPlugOperator

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class LeftPlugOperator(Float3CompoundBasePlugOperator["LeftAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leftR", "ler"),
        ("leftG", "leg"),
        ("leftB", "leb"),
    )

    leftR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ler = leftR

    leftG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    leg = leftG

    leftB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    leb = leftB


class LeftAttrOperator(Float3CompoundBaseAttrOperator[LeftPlugOperator]):
    __slots__ = ()

    leftR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ler = leftR

    leftG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    leg = leftG

    leftB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    leb = leftB


class LeftField(Float3CompoundBaseField[LeftAttrOperator, LeftPlugOperator]):
    __slots__ = ()

    ATTR_CLS = LeftAttrOperator
    PLUG_CLS = LeftPlugOperator

    leftR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ler = leftR

    leftG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    leg = leftG

    leftB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    leb = leftB


class RightPlugOperator(Float3CompoundBasePlugOperator["RightAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rightR", "rir"),
        ("rightG", "rig"),
        ("rightB", "rib"),
    )

    rightR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rir = rightR

    rightG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rig = rightG

    rightB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rib = rightB


class RightAttrOperator(Float3CompoundBaseAttrOperator[RightPlugOperator]):
    __slots__ = ()

    rightR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rir = rightR

    rightG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rig = rightG

    rightB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rib = rightB


class RightField(
    Float3CompoundBaseField[RightAttrOperator, RightPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightAttrOperator
    PLUG_CLS = RightPlugOperator

    rightR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rir = rightR

    rightG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rig = rightG

    rightB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rib = rightB


class TopPlugOperator(Float3CompoundBasePlugOperator["TopAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("topR", "tor"),
        ("topG", "tog"),
        ("topB", "tob"),
    )

    topR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tor = topR

    topG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tog = topG

    topB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tob = topB


class TopAttrOperator(Float3CompoundBaseAttrOperator[TopPlugOperator]):
    __slots__ = ()

    topR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tor = topR

    topG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tog = topG

    topB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tob = topB


class TopField(Float3CompoundBaseField[TopAttrOperator, TopPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TopAttrOperator
    PLUG_CLS = TopPlugOperator

    topR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tor = topR

    topG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tog = topG

    topB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tob = topB


class BottomPlugOperator(Float3CompoundBasePlugOperator["BottomAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bottomR", "bor"),
        ("bottomG", "bog"),
        ("bottomB", "bob"),
    )

    bottomR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bor = bottomR

    bottomG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bog = bottomG

    bottomB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bob = bottomB


class BottomAttrOperator(Float3CompoundBaseAttrOperator[BottomPlugOperator]):
    __slots__ = ()

    bottomR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bor = bottomR

    bottomG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bog = bottomG

    bottomB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bob = bottomB


class BottomField(
    Float3CompoundBaseField[BottomAttrOperator, BottomPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BottomAttrOperator
    PLUG_CLS = BottomPlugOperator

    bottomR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bor = bottomR

    bottomG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bog = bottomG

    bottomB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bob = bottomB


class FrontPlugOperator(Float3CompoundBasePlugOperator["FrontAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frontR", "frr"),
        ("frontG", "frg"),
        ("frontB", "frb"),
    )

    frontR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    frr = frontR

    frontG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    frg = frontG

    frontB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    frb = frontB


class FrontAttrOperator(Float3CompoundBaseAttrOperator[FrontPlugOperator]):
    __slots__ = ()

    frontR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    frr = frontR

    frontG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    frg = frontG

    frontB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    frb = frontB


class FrontField(
    Float3CompoundBaseField[FrontAttrOperator, FrontPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrontAttrOperator
    PLUG_CLS = FrontPlugOperator

    frontR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    frr = frontR

    frontG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    frg = frontG

    frontB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    frb = frontB


class BackPlugOperator(Float3CompoundBasePlugOperator["BackAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backR", "bar"),
        ("backG", "bag"),
        ("backB", "bab"),
    )

    backR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bar = backR

    backG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bag = backG

    backB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bab = backB


class BackAttrOperator(Float3CompoundBaseAttrOperator[BackPlugOperator]):
    __slots__ = ()

    backR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bar = backR

    backG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bag = backG

    backB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bab = backB


class BackField(Float3CompoundBaseField[BackAttrOperator, BackPlugOperator]):
    __slots__ = ()

    ATTR_CLS = BackAttrOperator
    PLUG_CLS = BackPlugOperator

    backR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bar = backR

    backG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bag = backG

    backB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bab = backB
