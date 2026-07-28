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


class SunBrightnessPlugOperator(
    Float3CompoundBasePlugOperator["SunBrightnessAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sunBrightnessR", "sur"),
        ("sunBrightnessG", "sug"),
        ("sunBrightnessB", "sub"),
    )

    sunBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sur = sunBrightnessR

    sunBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sug = sunBrightnessG

    sunBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sub = sunBrightnessB


class SunBrightnessAttrOperator(
    Float3CompoundBaseAttrOperator[SunBrightnessPlugOperator]
):
    __slots__ = ()

    sunBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sur = sunBrightnessR

    sunBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sug = sunBrightnessG

    sunBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sub = sunBrightnessB


class SunBrightnessField(
    Float3CompoundBaseField[
        SunBrightnessAttrOperator, SunBrightnessPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SunBrightnessAttrOperator
    PLUG_CLS = SunBrightnessPlugOperator

    sunBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sur = sunBrightnessR

    sunBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    sug = sunBrightnessG

    sunBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
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

    haloBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    hbr = haloBrightnessR

    haloBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    hbg = haloBrightnessG

    haloBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    hbb = haloBrightnessB


class HaloBrightnessAttrOperator(
    Float3CompoundBaseAttrOperator[HaloBrightnessPlugOperator]
):
    __slots__ = ()

    haloBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    hbr = haloBrightnessR

    haloBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    hbg = haloBrightnessG

    haloBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    hbb = haloBrightnessB


class HaloBrightnessField(
    Float3CompoundBaseField[
        HaloBrightnessAttrOperator, HaloBrightnessPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = HaloBrightnessAttrOperator
    PLUG_CLS = HaloBrightnessPlugOperator

    haloBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    hbr = haloBrightnessR

    haloBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    hbg = haloBrightnessG

    haloBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
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

    skyBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    skr = skyBrightnessR

    skyBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    skg = skyBrightnessG

    skyBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    skb = skyBrightnessB


class SkyBrightnessAttrOperator(
    Float3CompoundBaseAttrOperator[SkyBrightnessPlugOperator]
):
    __slots__ = ()

    skyBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    skr = skyBrightnessR

    skyBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    skg = skyBrightnessG

    skyBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    skb = skyBrightnessB


class SkyBrightnessField(
    Float3CompoundBaseField[
        SkyBrightnessAttrOperator, SkyBrightnessPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SkyBrightnessAttrOperator
    PLUG_CLS = SkyBrightnessPlugOperator

    skyBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    skr = skyBrightnessR

    skyBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    skg = skyBrightnessG

    skyBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
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

    floorColorR = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
    fcr = floorColorR

    floorColorG = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
    fcg = floorColorG

    floorColorB = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
    fcb = floorColorB


class FloorColorAttrOperator(
    Float3CompoundBaseAttrOperator[FloorColorPlugOperator]
):
    __slots__ = ()

    floorColorR = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
    fcr = floorColorR

    floorColorG = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
    fcg = floorColorG

    floorColorB = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
    fcb = floorColorB


class FloorColorField(
    Float3CompoundBaseField[FloorColorAttrOperator, FloorColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloorColorAttrOperator
    PLUG_CLS = FloorColorPlugOperator

    floorColorR = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
    fcr = floorColorR

    floorColorG = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
    fcg = floorColorG

    floorColorB = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
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

    cloudBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cbr = cloudBrightnessR

    cloudBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cbg = cloudBrightnessG

    cloudBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cbb = cloudBrightnessB


class CloudBrightnessAttrOperator(
    Float3CompoundBaseAttrOperator[CloudBrightnessPlugOperator]
):
    __slots__ = ()

    cloudBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cbr = cloudBrightnessR

    cloudBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cbg = cloudBrightnessG

    cloudBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cbb = cloudBrightnessB


class CloudBrightnessField(
    Float3CompoundBaseField[
        CloudBrightnessAttrOperator, CloudBrightnessPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CloudBrightnessAttrOperator
    PLUG_CLS = CloudBrightnessPlugOperator

    cloudBrightnessR = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cbr = cloudBrightnessR

    cloudBrightnessG = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cbg = cloudBrightnessG

    cloudBrightnessB = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
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

    sunsetBrightnessR = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ssr = sunsetBrightnessR

    sunsetBrightnessG = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ssg = sunsetBrightnessG

    sunsetBrightnessB = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ssb = sunsetBrightnessB


class SunsetBrightnessAttrOperator(
    Float3CompoundBaseAttrOperator[SunsetBrightnessPlugOperator]
):
    __slots__ = ()

    sunsetBrightnessR = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ssr = sunsetBrightnessR

    sunsetBrightnessG = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ssg = sunsetBrightnessG

    sunsetBrightnessB = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ssb = sunsetBrightnessB


class SunsetBrightnessField(
    Float3CompoundBaseField[
        SunsetBrightnessAttrOperator, SunsetBrightnessPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SunsetBrightnessAttrOperator
    PLUG_CLS = SunsetBrightnessPlugOperator

    sunsetBrightnessR = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ssr = sunsetBrightnessR

    sunsetBrightnessG = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ssg = sunsetBrightnessG

    sunsetBrightnessB = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ssb = sunsetBrightnessB
