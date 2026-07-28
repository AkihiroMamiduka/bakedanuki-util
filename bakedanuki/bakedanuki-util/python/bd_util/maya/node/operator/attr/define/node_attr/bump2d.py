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
        ("uvFilterSizeX", "fsx"),
        ("uvFilterSizeY", "fsy"),
    )

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class UvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[UvFilterSizePlugOperator]
):
    __slots__ = ()

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class UvFilterSizeField(
    Float2CompoundBaseField[UvFilterSizeAttrOperator, UvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvFilterSizeAttrOperator
    PLUG_CLS = UvFilterSizePlugOperator

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


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
    Float3CompoundBaseField[
        TangentUCameraAttrOperator, TangentUCameraPlugOperator
    ]
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
    Float3CompoundBaseField[
        TangentVCameraAttrOperator, TangentVCameraPlugOperator
    ]
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


class VertexUvOnePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvOneU", "t1u"),
        ("vertexUvOneV", "t1v"),
    )

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvOneAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvOnePlugOperator]
):
    __slots__ = ()

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvOneField(
    Float2CompoundBaseField[VertexUvOneAttrOperator, VertexUvOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvOneAttrOperator
    PLUG_CLS = VertexUvOnePlugOperator

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvTwoPlugOperator(
    Float2CompoundBasePlugOperator["VertexUvTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvTwoU", "t2u"),
        ("vertexUvTwoV", "t2v"),
    )

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvTwoAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvTwoPlugOperator]
):
    __slots__ = ()

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvTwoField(
    Float2CompoundBaseField[VertexUvTwoAttrOperator, VertexUvTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvTwoAttrOperator
    PLUG_CLS = VertexUvTwoPlugOperator

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexCameraOnePlugOperator(
    Float3CompoundBasePlugOperator["VertexCameraOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexCameraOneX", "c1x"),
        ("vertexCameraOneY", "c1y"),
        ("vertexCameraOneZ", "c1z"),
    )

    vertexCameraOneX = FloatField(default_value=0.0)
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField(default_value=0.0)
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField(default_value=0.0)
    c1z = vertexCameraOneZ


class VertexCameraOneAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraOnePlugOperator]
):
    __slots__ = ()

    vertexCameraOneX = FloatField(default_value=0.0)
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField(default_value=0.0)
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField(default_value=0.0)
    c1z = vertexCameraOneZ


class VertexCameraOneField(
    Float3CompoundBaseField[
        VertexCameraOneAttrOperator, VertexCameraOnePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraOneAttrOperator
    PLUG_CLS = VertexCameraOnePlugOperator

    vertexCameraOneX = FloatField(default_value=0.0)
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField(default_value=0.0)
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField(default_value=0.0)
    c1z = vertexCameraOneZ


class VertexCameraTwoPlugOperator(
    Float3CompoundBasePlugOperator["VertexCameraTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexCameraTwoX", "c2x"),
        ("vertexCameraTwoY", "c2y"),
        ("vertexCameraTwoZ", "c2z"),
    )

    vertexCameraTwoX = FloatField(default_value=0.0)
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField(default_value=0.0)
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField(default_value=0.0)
    c2z = vertexCameraTwoZ


class VertexCameraTwoAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraTwoPlugOperator]
):
    __slots__ = ()

    vertexCameraTwoX = FloatField(default_value=0.0)
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField(default_value=0.0)
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField(default_value=0.0)
    c2z = vertexCameraTwoZ


class VertexCameraTwoField(
    Float3CompoundBaseField[
        VertexCameraTwoAttrOperator, VertexCameraTwoPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraTwoAttrOperator
    PLUG_CLS = VertexCameraTwoPlugOperator

    vertexCameraTwoX = FloatField(default_value=0.0)
    c2x = vertexCameraTwoX

    vertexCameraTwoY = FloatField(default_value=0.0)
    c2y = vertexCameraTwoY

    vertexCameraTwoZ = FloatField(default_value=0.0)
    c2z = vertexCameraTwoZ
