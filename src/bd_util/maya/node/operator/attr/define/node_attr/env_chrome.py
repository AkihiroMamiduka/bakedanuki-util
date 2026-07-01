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


class SkyColorPlugOperator(
    Float3CompoundBasePlugOperator["SkyColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("skyColorR", "scr"),
        ("skyColorG", "scg"),
        ("skyColorB", "scb"),
    )

    skyColorR = FloatField()
    scr = skyColorR

    skyColorG = FloatField()
    scg = skyColorG

    skyColorB = FloatField()
    scb = skyColorB


class SkyColorAttrOperator(
    Float3CompoundBaseAttrOperator[SkyColorPlugOperator]
):
    __slots__ = ()

    skyColorR = FloatField()
    scr = skyColorR

    skyColorG = FloatField()
    scg = skyColorG

    skyColorB = FloatField()
    scb = skyColorB


class SkyColorField(
    Float3CompoundBaseField[SkyColorAttrOperator, SkyColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SkyColorAttrOperator
    PLUG_CLS = SkyColorPlugOperator

    skyColorR = FloatField()
    scr = skyColorR

    skyColorG = FloatField()
    scg = skyColorG

    skyColorB = FloatField()
    scb = skyColorB


class ZenithColorPlugOperator(
    Float3CompoundBasePlugOperator["ZenithColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("zenithColorR", "zcr"),
        ("zenithColorG", "zcg"),
        ("zenithColorB", "zcb"),
    )

    zenithColorR = FloatField()
    zcr = zenithColorR

    zenithColorG = FloatField()
    zcg = zenithColorG

    zenithColorB = FloatField()
    zcb = zenithColorB


class ZenithColorAttrOperator(
    Float3CompoundBaseAttrOperator[ZenithColorPlugOperator]
):
    __slots__ = ()

    zenithColorR = FloatField()
    zcr = zenithColorR

    zenithColorG = FloatField()
    zcg = zenithColorG

    zenithColorB = FloatField()
    zcb = zenithColorB


class ZenithColorField(
    Float3CompoundBaseField[ZenithColorAttrOperator, ZenithColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ZenithColorAttrOperator
    PLUG_CLS = ZenithColorPlugOperator

    zenithColorR = FloatField()
    zcr = zenithColorR

    zenithColorG = FloatField()
    zcg = zenithColorG

    zenithColorB = FloatField()
    zcb = zenithColorB


class LightColorPlugOperator(
    Float3CompoundBasePlugOperator["LightColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightColorR", "lcr"),
        ("lightColorG", "lcg"),
        ("lightColorB", "lcb"),
    )

    lightColorR = FloatField()
    lcr = lightColorR

    lightColorG = FloatField()
    lcg = lightColorG

    lightColorB = FloatField()
    lcb = lightColorB


class LightColorAttrOperator(
    Float3CompoundBaseAttrOperator[LightColorPlugOperator]
):
    __slots__ = ()

    lightColorR = FloatField()
    lcr = lightColorR

    lightColorG = FloatField()
    lcg = lightColorG

    lightColorB = FloatField()
    lcb = lightColorB


class LightColorField(
    Float3CompoundBaseField[LightColorAttrOperator, LightColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightColorAttrOperator
    PLUG_CLS = LightColorPlugOperator

    lightColorR = FloatField()
    lcr = lightColorR

    lightColorG = FloatField()
    lcg = lightColorG

    lightColorB = FloatField()
    lcb = lightColorB


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


class HorizonColorPlugOperator(
    Float3CompoundBasePlugOperator["HorizonColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("horizonColorR", "hcr"),
        ("horizonColorG", "hcg"),
        ("horizonColorB", "hcb"),
    )

    horizonColorR = FloatField()
    hcr = horizonColorR

    horizonColorG = FloatField()
    hcg = horizonColorG

    horizonColorB = FloatField()
    hcb = horizonColorB


class HorizonColorAttrOperator(
    Float3CompoundBaseAttrOperator[HorizonColorPlugOperator]
):
    __slots__ = ()

    horizonColorR = FloatField()
    hcr = horizonColorR

    horizonColorG = FloatField()
    hcg = horizonColorG

    horizonColorB = FloatField()
    hcb = horizonColorB


class HorizonColorField(
    Float3CompoundBaseField[HorizonColorAttrOperator, HorizonColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HorizonColorAttrOperator
    PLUG_CLS = HorizonColorPlugOperator

    horizonColorR = FloatField()
    hcr = horizonColorR

    horizonColorG = FloatField()
    hcg = horizonColorG

    horizonColorB = FloatField()
    hcb = horizonColorB


class GridColorPlugOperator(
    Float3CompoundBasePlugOperator["GridColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("gridColorR", "gcr"),
        ("gridColorG", "gcg"),
        ("gridColorB", "gcb"),
    )

    gridColorR = FloatField()
    gcr = gridColorR

    gridColorG = FloatField()
    gcg = gridColorG

    gridColorB = FloatField()
    gcb = gridColorB


class GridColorAttrOperator(
    Float3CompoundBaseAttrOperator[GridColorPlugOperator]
):
    __slots__ = ()

    gridColorR = FloatField()
    gcr = gridColorR

    gridColorG = FloatField()
    gcg = gridColorG

    gridColorB = FloatField()
    gcb = gridColorB


class GridColorField(
    Float3CompoundBaseField[GridColorAttrOperator, GridColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GridColorAttrOperator
    PLUG_CLS = GridColorPlugOperator

    gridColorR = FloatField()
    gcr = gridColorR

    gridColorG = FloatField()
    gcg = gridColorG

    gridColorB = FloatField()
    gcb = gridColorB
