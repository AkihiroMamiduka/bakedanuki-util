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


class SkyColorPlugOperator(
    Float3CompoundBasePlugOperator["SkyColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("skyColorR", "scr"),
        ("skyColorG", "scg"),
        ("skyColorB", "scb"),
    )

    skyColorR = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    scr = skyColorR

    skyColorG = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    scg = skyColorG

    skyColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    scb = skyColorB


class SkyColorAttrOperator(
    Float3CompoundBaseAttrOperator[SkyColorPlugOperator]
):
    __slots__ = ()

    skyColorR = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    scr = skyColorR

    skyColorG = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    scg = skyColorG

    skyColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    scb = skyColorB


class SkyColorField(
    Float3CompoundBaseField[SkyColorAttrOperator, SkyColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SkyColorAttrOperator
    PLUG_CLS = SkyColorPlugOperator

    skyColorR = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    scr = skyColorR

    skyColorG = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    scg = skyColorG

    skyColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
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

    zenithColorR = FloatField(
        default_value=0.3919999897480011, min_value=0.0, max_value=1.0
    )
    zcr = zenithColorR

    zenithColorG = FloatField(
        default_value=0.3919999897480011, min_value=0.0, max_value=1.0
    )
    zcg = zenithColorG

    zenithColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    zcb = zenithColorB


class ZenithColorAttrOperator(
    Float3CompoundBaseAttrOperator[ZenithColorPlugOperator]
):
    __slots__ = ()

    zenithColorR = FloatField(
        default_value=0.3919999897480011, min_value=0.0, max_value=1.0
    )
    zcr = zenithColorR

    zenithColorG = FloatField(
        default_value=0.3919999897480011, min_value=0.0, max_value=1.0
    )
    zcg = zenithColorG

    zenithColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    zcb = zenithColorB


class ZenithColorField(
    Float3CompoundBaseField[ZenithColorAttrOperator, ZenithColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ZenithColorAttrOperator
    PLUG_CLS = ZenithColorPlugOperator

    zenithColorR = FloatField(
        default_value=0.3919999897480011, min_value=0.0, max_value=1.0
    )
    zcr = zenithColorR

    zenithColorG = FloatField(
        default_value=0.3919999897480011, min_value=0.0, max_value=1.0
    )
    zcg = zenithColorG

    zenithColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
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

    lightColorR = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    lcr = lightColorR

    lightColorG = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    lcg = lightColorG

    lightColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    lcb = lightColorB


class LightColorAttrOperator(
    Float3CompoundBaseAttrOperator[LightColorPlugOperator]
):
    __slots__ = ()

    lightColorR = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    lcr = lightColorR

    lightColorG = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    lcg = lightColorG

    lightColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    lcb = lightColorB


class LightColorField(
    Float3CompoundBaseField[LightColorAttrOperator, LightColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightColorAttrOperator
    PLUG_CLS = LightColorPlugOperator

    lightColorR = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    lcr = lightColorR

    lightColorG = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    lcg = lightColorG

    lightColorB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
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

    floorColorR = FloatField(
        default_value=0.5879999995231628, min_value=0.0, max_value=1.0
    )
    fcr = floorColorR

    floorColorG = FloatField(
        default_value=0.5879999995231628, min_value=0.0, max_value=1.0
    )
    fcg = floorColorG

    floorColorB = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    fcb = floorColorB


class FloorColorAttrOperator(
    Float3CompoundBaseAttrOperator[FloorColorPlugOperator]
):
    __slots__ = ()

    floorColorR = FloatField(
        default_value=0.5879999995231628, min_value=0.0, max_value=1.0
    )
    fcr = floorColorR

    floorColorG = FloatField(
        default_value=0.5879999995231628, min_value=0.0, max_value=1.0
    )
    fcg = floorColorG

    floorColorB = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
    fcb = floorColorB


class FloorColorField(
    Float3CompoundBaseField[FloorColorAttrOperator, FloorColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloorColorAttrOperator
    PLUG_CLS = FloorColorPlugOperator

    floorColorR = FloatField(
        default_value=0.5879999995231628, min_value=0.0, max_value=1.0
    )
    fcr = floorColorR

    floorColorG = FloatField(
        default_value=0.5879999995231628, min_value=0.0, max_value=1.0
    )
    fcg = floorColorG

    floorColorB = FloatField(
        default_value=0.7839999794960022, min_value=0.0, max_value=1.0
    )
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

    horizonColorR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcr = horizonColorR

    horizonColorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcg = horizonColorG

    horizonColorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcb = horizonColorB


class HorizonColorAttrOperator(
    Float3CompoundBaseAttrOperator[HorizonColorPlugOperator]
):
    __slots__ = ()

    horizonColorR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcr = horizonColorR

    horizonColorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcg = horizonColorG

    horizonColorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcb = horizonColorB


class HorizonColorField(
    Float3CompoundBaseField[HorizonColorAttrOperator, HorizonColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HorizonColorAttrOperator
    PLUG_CLS = HorizonColorPlugOperator

    horizonColorR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcr = horizonColorR

    horizonColorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcg = horizonColorG

    horizonColorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
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

    gridColorR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gcr = gridColorR

    gridColorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gcg = gridColorG

    gridColorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gcb = gridColorB


class GridColorAttrOperator(
    Float3CompoundBaseAttrOperator[GridColorPlugOperator]
):
    __slots__ = ()

    gridColorR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gcr = gridColorR

    gridColorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gcg = gridColorG

    gridColorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gcb = gridColorB


class GridColorField(
    Float3CompoundBaseField[GridColorAttrOperator, GridColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GridColorAttrOperator
    PLUG_CLS = GridColorPlugOperator

    gridColorR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gcr = gridColorR

    gridColorG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gcg = gridColorG

    gridColorB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gcb = gridColorB
