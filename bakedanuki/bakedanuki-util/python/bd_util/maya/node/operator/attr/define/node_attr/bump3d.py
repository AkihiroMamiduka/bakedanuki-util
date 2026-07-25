# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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


class PointObjPlugOperator(
    Float3CompoundBasePlugOperator["PointObjAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointObjX", "pox"),
        ("pointObjY", "poy"),
        ("pointObjZ", "poz"),
    )

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    poz = pointObjZ


class PointObjAttrOperator(
    Float3CompoundBaseAttrOperator[PointObjPlugOperator]
):
    __slots__ = ()

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
    poz = pointObjZ


class PointObjField(
    Float3CompoundBaseField[PointObjAttrOperator, PointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointObjAttrOperator
    PLUG_CLS = PointObjPlugOperator

    pointObjX = FloatField(default_value=0.0)
    pox = pointObjX

    pointObjY = FloatField(default_value=0.0)
    poy = pointObjY

    pointObjZ = FloatField(default_value=0.0)
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

    refPointObjX = FloatField(default_value=0.0)
    rpox = refPointObjX

    refPointObjY = FloatField(default_value=0.0)
    rpoy = refPointObjY

    refPointObjZ = FloatField(default_value=0.0)
    rpoz = refPointObjZ


class RefPointObjAttrOperator(
    Float3CompoundBaseAttrOperator[RefPointObjPlugOperator]
):
    __slots__ = ()

    refPointObjX = FloatField(default_value=0.0)
    rpox = refPointObjX

    refPointObjY = FloatField(default_value=0.0)
    rpoy = refPointObjY

    refPointObjZ = FloatField(default_value=0.0)
    rpoz = refPointObjZ


class RefPointObjField(
    Float3CompoundBaseField[RefPointObjAttrOperator, RefPointObjPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RefPointObjAttrOperator
    PLUG_CLS = RefPointObjPlugOperator

    refPointObjX = FloatField(default_value=0.0)
    rpox = refPointObjX

    refPointObjY = FloatField(default_value=0.0)
    rpoy = refPointObjY

    refPointObjZ = FloatField(default_value=0.0)
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
    Float3CompoundBaseField[RefPointCameraAttrOperator, RefPointCameraPlugOperator]
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


class RayOriginPlugOperator(
    Float3CompoundBasePlugOperator["RayOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayOriginX", "rox"),
        ("rayOriginY", "roy"),
        ("rayOriginZ", "roz"),
    )

    rayOriginX = FloatField(default_value=0.0)
    rox = rayOriginX

    rayOriginY = FloatField(default_value=0.0)
    roy = rayOriginY

    rayOriginZ = FloatField(default_value=0.0)
    roz = rayOriginZ


class RayOriginAttrOperator(
    Float3CompoundBaseAttrOperator[RayOriginPlugOperator]
):
    __slots__ = ()

    rayOriginX = FloatField(default_value=0.0)
    rox = rayOriginX

    rayOriginY = FloatField(default_value=0.0)
    roy = rayOriginY

    rayOriginZ = FloatField(default_value=0.0)
    roz = rayOriginZ


class RayOriginField(
    Float3CompoundBaseField[RayOriginAttrOperator, RayOriginPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayOriginAttrOperator
    PLUG_CLS = RayOriginPlugOperator

    rayOriginX = FloatField(default_value=0.0)
    rox = rayOriginX

    rayOriginY = FloatField(default_value=0.0)
    roy = rayOriginY

    rayOriginZ = FloatField(default_value=0.0)
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


class TangentUCameraPlugOperator(
    Float3CompoundBasePlugOperator["TangentUCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tangentUx", "tux"),
        ("tangentUy", "tuy"),
        ("tangentUz", "tuz"),
    )

    tangentUx = FloatField(default_value=1.0)
    tux = tangentUx

    tangentUy = FloatField(default_value=0.0)
    tuy = tangentUy

    tangentUz = FloatField(default_value=0.0)
    tuz = tangentUz


class TangentUCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TangentUCameraPlugOperator]
):
    __slots__ = ()

    tangentUx = FloatField(default_value=1.0)
    tux = tangentUx

    tangentUy = FloatField(default_value=0.0)
    tuy = tangentUy

    tangentUz = FloatField(default_value=0.0)
    tuz = tangentUz


class TangentUCameraField(
    Float3CompoundBaseField[TangentUCameraAttrOperator, TangentUCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentUCameraAttrOperator
    PLUG_CLS = TangentUCameraPlugOperator

    tangentUx = FloatField(default_value=1.0)
    tux = tangentUx

    tangentUy = FloatField(default_value=0.0)
    tuy = tangentUy

    tangentUz = FloatField(default_value=0.0)
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

    tangentVx = FloatField(default_value=0.0)
    tvx = tangentVx

    tangentVy = FloatField(default_value=1.0)
    tvy = tangentVy

    tangentVz = FloatField(default_value=0.0)
    tvz = tangentVz


class TangentVCameraAttrOperator(
    Float3CompoundBaseAttrOperator[TangentVCameraPlugOperator]
):
    __slots__ = ()

    tangentVx = FloatField(default_value=0.0)
    tvx = tangentVx

    tangentVy = FloatField(default_value=1.0)
    tvy = tangentVy

    tangentVz = FloatField(default_value=0.0)
    tvz = tangentVz


class TangentVCameraField(
    Float3CompoundBaseField[TangentVCameraAttrOperator, TangentVCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentVCameraAttrOperator
    PLUG_CLS = TangentVCameraPlugOperator

    tangentVx = FloatField(default_value=0.0)
    tvx = tangentVx

    tangentVy = FloatField(default_value=1.0)
    tvy = tangentVy

    tangentVz = FloatField(default_value=0.0)
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

    outNormalX = FloatField(default_value=0.0, writable=False)
    ox = outNormalX

    outNormalY = FloatField(default_value=0.0, writable=False)
    oy = outNormalY

    outNormalZ = FloatField(default_value=1.0, writable=False)
    oz = outNormalZ


class OutNormalAttrOperator(
    Float3CompoundBaseAttrOperator[OutNormalPlugOperator]
):
    __slots__ = ()

    outNormalX = FloatField(default_value=0.0, writable=False)
    ox = outNormalX

    outNormalY = FloatField(default_value=0.0, writable=False)
    oy = outNormalY

    outNormalZ = FloatField(default_value=1.0, writable=False)
    oz = outNormalZ


class OutNormalField(
    Float3CompoundBaseField[OutNormalAttrOperator, OutNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutNormalAttrOperator
    PLUG_CLS = OutNormalPlugOperator

    outNormalX = FloatField(default_value=0.0, writable=False)
    ox = outNormalX

    outNormalY = FloatField(default_value=0.0, writable=False)
    oy = outNormalY

    outNormalZ = FloatField(default_value=1.0, writable=False)
    oz = outNormalZ
