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


class SunBrightnessPlugOperator(
    Float3CompoundBasePlugOperator["SunBrightnessAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sunBrightnessR", "sur"),
        ("sunBrightnessG", "sug"),
        ("sunBrightnessB", "sub"),
    )

    sunBrightnessR = FloatField()
    sur = sunBrightnessR

    sunBrightnessG = FloatField()
    sug = sunBrightnessG

    sunBrightnessB = FloatField()
    sub = sunBrightnessB


class SunBrightnessAttrOperator(
    Float3CompoundBaseAttrOperator[SunBrightnessPlugOperator]
):
    __slots__ = ()

    sunBrightnessR = FloatField()
    sur = sunBrightnessR

    sunBrightnessG = FloatField()
    sug = sunBrightnessG

    sunBrightnessB = FloatField()
    sub = sunBrightnessB


class SunBrightnessField(
    Float3CompoundBaseField[SunBrightnessAttrOperator, SunBrightnessPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SunBrightnessAttrOperator
    PLUG_CLS = SunBrightnessPlugOperator

    sunBrightnessR = FloatField()
    sur = sunBrightnessR

    sunBrightnessG = FloatField()
    sug = sunBrightnessG

    sunBrightnessB = FloatField()
    sub = sunBrightnessB


class HaloBrightnessPlugOperator(
    Float3CompoundBasePlugOperator["HaloBrightnessAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("haloBrightnessR", "hbr"),
        ("haloBrightnessG", "hbg"),
        ("haloBrightnessB", "hbb"),
    )

    haloBrightnessR = FloatField()
    hbr = haloBrightnessR

    haloBrightnessG = FloatField()
    hbg = haloBrightnessG

    haloBrightnessB = FloatField()
    hbb = haloBrightnessB


class HaloBrightnessAttrOperator(
    Float3CompoundBaseAttrOperator[HaloBrightnessPlugOperator]
):
    __slots__ = ()

    haloBrightnessR = FloatField()
    hbr = haloBrightnessR

    haloBrightnessG = FloatField()
    hbg = haloBrightnessG

    haloBrightnessB = FloatField()
    hbb = haloBrightnessB


class HaloBrightnessField(
    Float3CompoundBaseField[HaloBrightnessAttrOperator, HaloBrightnessPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HaloBrightnessAttrOperator
    PLUG_CLS = HaloBrightnessPlugOperator

    haloBrightnessR = FloatField()
    hbr = haloBrightnessR

    haloBrightnessG = FloatField()
    hbg = haloBrightnessG

    haloBrightnessB = FloatField()
    hbb = haloBrightnessB


class SkyBrightnessPlugOperator(
    Float3CompoundBasePlugOperator["SkyBrightnessAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("skyBrightnessR", "skr"),
        ("skyBrightnessG", "skg"),
        ("skyBrightnessB", "skb"),
    )

    skyBrightnessR = FloatField()
    skr = skyBrightnessR

    skyBrightnessG = FloatField()
    skg = skyBrightnessG

    skyBrightnessB = FloatField()
    skb = skyBrightnessB


class SkyBrightnessAttrOperator(
    Float3CompoundBaseAttrOperator[SkyBrightnessPlugOperator]
):
    __slots__ = ()

    skyBrightnessR = FloatField()
    skr = skyBrightnessR

    skyBrightnessG = FloatField()
    skg = skyBrightnessG

    skyBrightnessB = FloatField()
    skb = skyBrightnessB


class SkyBrightnessField(
    Float3CompoundBaseField[SkyBrightnessAttrOperator, SkyBrightnessPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SkyBrightnessAttrOperator
    PLUG_CLS = SkyBrightnessPlugOperator

    skyBrightnessR = FloatField()
    skr = skyBrightnessR

    skyBrightnessG = FloatField()
    skg = skyBrightnessG

    skyBrightnessB = FloatField()
    skb = skyBrightnessB


class FloorColorPlugOperator(
    Float3CompoundBasePlugOperator["FloorColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("floorColorR", "fcr"),
        ("floorColorG", "fcg"),
        ("floorColorB", "fcb"),
    )

    floorColorR = FloatField()
    fcr = floorColorR

    floorColorG = FloatField()
    fcg = floorColorG

    floorColorB = FloatField()
    fcb = floorColorB


class FloorColorAttrOperator(
    Float3CompoundBaseAttrOperator[FloorColorPlugOperator]
):
    __slots__ = ()

    floorColorR = FloatField()
    fcr = floorColorR

    floorColorG = FloatField()
    fcg = floorColorG

    floorColorB = FloatField()
    fcb = floorColorB


class FloorColorField(
    Float3CompoundBaseField[FloorColorAttrOperator, FloorColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloorColorAttrOperator
    PLUG_CLS = FloorColorPlugOperator

    floorColorR = FloatField()
    fcr = floorColorR

    floorColorG = FloatField()
    fcg = floorColorG

    floorColorB = FloatField()
    fcb = floorColorB


class CloudBrightnessPlugOperator(
    Float3CompoundBasePlugOperator["CloudBrightnessAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cloudBrightnessR", "cbr"),
        ("cloudBrightnessG", "cbg"),
        ("cloudBrightnessB", "cbb"),
    )

    cloudBrightnessR = FloatField()
    cbr = cloudBrightnessR

    cloudBrightnessG = FloatField()
    cbg = cloudBrightnessG

    cloudBrightnessB = FloatField()
    cbb = cloudBrightnessB


class CloudBrightnessAttrOperator(
    Float3CompoundBaseAttrOperator[CloudBrightnessPlugOperator]
):
    __slots__ = ()

    cloudBrightnessR = FloatField()
    cbr = cloudBrightnessR

    cloudBrightnessG = FloatField()
    cbg = cloudBrightnessG

    cloudBrightnessB = FloatField()
    cbb = cloudBrightnessB


class CloudBrightnessField(
    Float3CompoundBaseField[CloudBrightnessAttrOperator, CloudBrightnessPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CloudBrightnessAttrOperator
    PLUG_CLS = CloudBrightnessPlugOperator

    cloudBrightnessR = FloatField()
    cbr = cloudBrightnessR

    cloudBrightnessG = FloatField()
    cbg = cloudBrightnessG

    cloudBrightnessB = FloatField()
    cbb = cloudBrightnessB


class SunsetBrightnessPlugOperator(
    Float3CompoundBasePlugOperator["SunsetBrightnessAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sunsetBrightnessR", "ssr"),
        ("sunsetBrightnessG", "ssg"),
        ("sunsetBrightnessB", "ssb"),
    )

    sunsetBrightnessR = FloatField()
    ssr = sunsetBrightnessR

    sunsetBrightnessG = FloatField()
    ssg = sunsetBrightnessG

    sunsetBrightnessB = FloatField()
    ssb = sunsetBrightnessB


class SunsetBrightnessAttrOperator(
    Float3CompoundBaseAttrOperator[SunsetBrightnessPlugOperator]
):
    __slots__ = ()

    sunsetBrightnessR = FloatField()
    ssr = sunsetBrightnessR

    sunsetBrightnessG = FloatField()
    ssg = sunsetBrightnessG

    sunsetBrightnessB = FloatField()
    ssb = sunsetBrightnessB


class SunsetBrightnessField(
    Float3CompoundBaseField[SunsetBrightnessAttrOperator, SunsetBrightnessPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SunsetBrightnessAttrOperator
    PLUG_CLS = SunsetBrightnessPlugOperator

    sunsetBrightnessR = FloatField()
    ssr = sunsetBrightnessR

    sunsetBrightnessG = FloatField()
    ssg = sunsetBrightnessG

    sunsetBrightnessB = FloatField()
    ssb = sunsetBrightnessB
