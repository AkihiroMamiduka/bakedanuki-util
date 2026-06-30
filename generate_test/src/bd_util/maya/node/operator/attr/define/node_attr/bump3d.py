# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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


class RefPointObjPlugOperator(
    Float3CompoundBasePlugOperator["RefPointObjAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("refPointObjX", "rpox"),
        ("refPointObjY", "rpoy"),
        ("refPointObjZ", "rpoz"),
    )

    refPointObjX = FloatField()
    rpox = refPointObjX

    refPointObjY = FloatField()
    rpoy = refPointObjY

    refPointObjZ = FloatField()
    rpoz = refPointObjZ


class RefPointObjAttrOperator(
    Float3CompoundBaseAttrOperator[RefPointObjPlugOperator]
):
    __slots__ = ()

    refPointObjX = FloatField()
    rpox = refPointObjX

    refPointObjY = FloatField()
    rpoy = refPointObjY

    refPointObjZ = FloatField()
    rpoz = refPointObjZ


class RefPointObjField(
    Float3CompoundBaseField[RefPointObjAttrOperator, RefPointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RefPointObjAttrOperator
    PLUG_CLS = RefPointObjPlugOperator

    refPointObjX = FloatField()
    rpox = refPointObjX

    refPointObjY = FloatField()
    rpoy = refPointObjY

    refPointObjZ = FloatField()
    rpoz = refPointObjZ


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


class RayOriginPlugOperator(
    Float3CompoundBasePlugOperator["RayOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayOriginX", "rox"),
        ("rayOriginY", "roy"),
        ("rayOriginZ", "roz"),
    )

    rayOriginX = FloatField()
    rox = rayOriginX

    rayOriginY = FloatField()
    roy = rayOriginY

    rayOriginZ = FloatField()
    roz = rayOriginZ


class RayOriginAttrOperator(
    Float3CompoundBaseAttrOperator[RayOriginPlugOperator]
):
    __slots__ = ()

    rayOriginX = FloatField()
    rox = rayOriginX

    rayOriginY = FloatField()
    roy = rayOriginY

    rayOriginZ = FloatField()
    roz = rayOriginZ


class RayOriginField(
    Float3CompoundBaseField[RayOriginAttrOperator, RayOriginPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayOriginAttrOperator
    PLUG_CLS = RayOriginPlugOperator

    rayOriginX = FloatField()
    rox = rayOriginX

    rayOriginY = FloatField()
    roy = rayOriginY

    rayOriginZ = FloatField()
    roz = rayOriginZ


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


class OutNormalPlugOperator(
    Float3CompoundBasePlugOperator["OutNormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outNormalX", "ox"),
        ("outNormalY", "oy"),
        ("outNormalZ", "oz"),
    )

    outNormalX = FloatField()
    ox = outNormalX

    outNormalY = FloatField()
    oy = outNormalY

    outNormalZ = FloatField()
    oz = outNormalZ


class OutNormalAttrOperator(
    Float3CompoundBaseAttrOperator[OutNormalPlugOperator]
):
    __slots__ = ()

    outNormalX = FloatField()
    ox = outNormalX

    outNormalY = FloatField()
    oy = outNormalY

    outNormalZ = FloatField()
    oz = outNormalZ


class OutNormalField(
    Float3CompoundBaseField[OutNormalAttrOperator, OutNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutNormalAttrOperator
    PLUG_CLS = OutNormalPlugOperator

    outNormalX = FloatField()
    ox = outNormalX

    outNormalY = FloatField()
    oy = outNormalY

    outNormalZ = FloatField()
    oz = outNormalZ
