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


class TangentUCameraPlugOperator(
    Float3CompoundBasePlugOperator["TangentUCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tangentUx", "tux"),
        ("tangentUy", "tuy"),
        ("tangentUz", "tuz"),
    )

    tangentUx = FloatField()
    tux = tangentUx

    tangentUy = FloatField()
    tuy = tangentUy

    tangentUz = FloatField()
    tuz = tangentUz


class TangentUCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TangentUCameraPlugOperator]
):
    __slots__ = ()

    tangentUx = FloatField()
    tux = tangentUx

    tangentUy = FloatField()
    tuy = tangentUy

    tangentUz = FloatField()
    tuz = tangentUz


class TangentUCameraField(
    Float3CompoundBaseField[TangentUCameraAttrOperator, TangentUCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentUCameraAttrOperator
    PLUG_CLS = TangentUCameraPlugOperator

    tangentUx = FloatField()
    tux = tangentUx

    tangentUy = FloatField()
    tuy = tangentUy

    tangentUz = FloatField()
    tuz = tangentUz


class TangentVCameraPlugOperator(
    Float3CompoundBasePlugOperator["TangentVCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tangentVx", "tvx"),
        ("tangentVy", "tvy"),
        ("tangentVz", "tvz"),
    )

    tangentVx = FloatField()
    tvx = tangentVx

    tangentVy = FloatField()
    tvy = tangentVy

    tangentVz = FloatField()
    tvz = tangentVz


class TangentVCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TangentVCameraPlugOperator]
):
    __slots__ = ()

    tangentVx = FloatField()
    tvx = tangentVx

    tangentVy = FloatField()
    tvy = tangentVy

    tangentVz = FloatField()
    tvz = tangentVz


class TangentVCameraField(
    Float3CompoundBaseField[TangentVCameraAttrOperator, TangentVCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentVCameraAttrOperator
    PLUG_CLS = TangentVCameraPlugOperator

    tangentVx = FloatField()
    tvx = tangentVx

    tangentVy = FloatField()
    tvy = tangentVy

    tangentVz = FloatField()
    tvz = tangentVz


class PixelCenterPlugOperator(
    Float2CompoundBasePlugOperator["PixelCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pixelCenterX", "pcx"),
        ("pixelCenterY", "pcy"),
    )

    pixelCenterX = FloatField()
    pcx = pixelCenterX

    pixelCenterY = FloatField()
    pcy = pixelCenterY


class PixelCenterAttrOperator(
    Float2CompoundBaseAttrOperator[PixelCenterPlugOperator]
):
    __slots__ = ()

    pixelCenterX = FloatField()
    pcx = pixelCenterX

    pixelCenterY = FloatField()
    pcy = pixelCenterY


class PixelCenterField(
    Float2CompoundBaseField[PixelCenterAttrOperator, PixelCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PixelCenterAttrOperator
    PLUG_CLS = PixelCenterPlugOperator

    pixelCenterX = FloatField()
    pcx = pixelCenterX

    pixelCenterY = FloatField()
    pcy = pixelCenterY
