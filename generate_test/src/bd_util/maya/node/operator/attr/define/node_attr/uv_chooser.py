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


class StCoordPlugOperator(
    Float2CompoundBasePlugOperator["StCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sCoord", "s"),
        ("tCoord", "t"),
    )

    sCoord = FloatField()
    s = sCoord

    tCoord = FloatField()
    t = tCoord


class StCoordAttrOperator(
    Float2CompoundBaseAttrOperator[StCoordPlugOperator]
):
    __slots__ = ()

    sCoord = FloatField()
    s = sCoord

    tCoord = FloatField()
    t = tCoord


class StCoordField(
    Float2CompoundBaseField[StCoordAttrOperator, StCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StCoordAttrOperator
    PLUG_CLS = StCoordPlugOperator

    sCoord = FloatField()
    s = sCoord

    tCoord = FloatField()
    t = tCoord


class VertexStOnePlugOperator(
    Float2CompoundBasePlugOperator["VertexStOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexStOneS", "s1s"),
        ("vertexStOneT", "s1t"),
    )

    vertexStOneS = FloatField()
    s1s = vertexStOneS

    vertexStOneT = FloatField()
    s1t = vertexStOneT


class VertexStOneAttrOperator(
    Float2CompoundBaseAttrOperator[VertexStOnePlugOperator]
):
    __slots__ = ()

    vertexStOneS = FloatField()
    s1s = vertexStOneS

    vertexStOneT = FloatField()
    s1t = vertexStOneT


class VertexStOneField(
    Float2CompoundBaseField[VertexStOneAttrOperator, VertexStOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexStOneAttrOperator
    PLUG_CLS = VertexStOnePlugOperator

    vertexStOneS = FloatField()
    s1s = vertexStOneS

    vertexStOneT = FloatField()
    s1t = vertexStOneT


class VertexStTwoPlugOperator(
    Float2CompoundBasePlugOperator["VertexStTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexStTwoS", "s2s"),
        ("vertexStTwoT", "s2t"),
    )

    vertexStTwoS = FloatField()
    s2s = vertexStTwoS

    vertexStTwoT = FloatField()
    s2t = vertexStTwoT


class VertexStTwoAttrOperator(
    Float2CompoundBaseAttrOperator[VertexStTwoPlugOperator]
):
    __slots__ = ()

    vertexStTwoS = FloatField()
    s2s = vertexStTwoS

    vertexStTwoT = FloatField()
    s2t = vertexStTwoT


class VertexStTwoField(
    Float2CompoundBaseField[VertexStTwoAttrOperator, VertexStTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexStTwoAttrOperator
    PLUG_CLS = VertexStTwoPlugOperator

    vertexStTwoS = FloatField()
    s2s = vertexStTwoS

    vertexStTwoT = FloatField()
    s2t = vertexStTwoT


class VertexStThreePlugOperator(
    Float2CompoundBasePlugOperator["VertexStThreeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexStThreeS", "s3s"),
        ("vertexStThreeT", "s3t"),
    )

    vertexStThreeS = FloatField()
    s3s = vertexStThreeS

    vertexStThreeT = FloatField()
    s3t = vertexStThreeT


class VertexStThreeAttrOperator(
    Float2CompoundBaseAttrOperator[VertexStThreePlugOperator]
):
    __slots__ = ()

    vertexStThreeS = FloatField()
    s3s = vertexStThreeS

    vertexStThreeT = FloatField()
    s3t = vertexStThreeT


class VertexStThreeField(
    Float2CompoundBaseField[VertexStThreeAttrOperator, VertexStThreePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexStThreeAttrOperator
    PLUG_CLS = VertexStThreePlugOperator

    vertexStThreeS = FloatField()
    s3s = vertexStThreeS

    vertexStThreeT = FloatField()
    s3t = vertexStThreeT


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


class VertexUvOnePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvOneU", "t1u"),
        ("vertexUvOneV", "t1v"),
    )

    vertexUvOneU = FloatField()
    t1u = vertexUvOneU

    vertexUvOneV = FloatField()
    t1v = vertexUvOneV


class VertexUvOneAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvOnePlugOperator]
):
    __slots__ = ()

    vertexUvOneU = FloatField()
    t1u = vertexUvOneU

    vertexUvOneV = FloatField()
    t1v = vertexUvOneV


class VertexUvOneField(
    Float2CompoundBaseField[VertexUvOneAttrOperator, VertexUvOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvOneAttrOperator
    PLUG_CLS = VertexUvOnePlugOperator

    vertexUvOneU = FloatField()
    t1u = vertexUvOneU

    vertexUvOneV = FloatField()
    t1v = vertexUvOneV


class VertexUvTwoPlugOperator(
    Float2CompoundBasePlugOperator["VertexUvTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvTwoU", "t2u"),
        ("vertexUvTwoV", "t2v"),
    )

    vertexUvTwoU = FloatField()
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField()
    t2v = vertexUvTwoV


class VertexUvTwoAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvTwoPlugOperator]
):
    __slots__ = ()

    vertexUvTwoU = FloatField()
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField()
    t2v = vertexUvTwoV


class VertexUvTwoField(
    Float2CompoundBaseField[VertexUvTwoAttrOperator, VertexUvTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvTwoAttrOperator
    PLUG_CLS = VertexUvTwoPlugOperator

    vertexUvTwoU = FloatField()
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField()
    t2v = vertexUvTwoV


class VertexUvThreePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvThreeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvThreeU", "t3u"),
        ("vertexUvThreeV", "t3v"),
    )

    vertexUvThreeU = FloatField()
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField()
    t3v = vertexUvThreeV


class VertexUvThreeAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvThreePlugOperator]
):
    __slots__ = ()

    vertexUvThreeU = FloatField()
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField()
    t3v = vertexUvThreeV


class VertexUvThreeField(
    Float2CompoundBaseField[VertexUvThreeAttrOperator, VertexUvThreePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvThreeAttrOperator
    PLUG_CLS = VertexUvThreePlugOperator

    vertexUvThreeU = FloatField()
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField()
    t3v = vertexUvThreeV


class VertexCameraOnePlugOperator(
    Float3CompoundBasePlugOperator["VertexCameraOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexCameraOneX", "c1x"),
        ("vertexCameraOneY", "c1y"),
        ("vertexCameraOneZ", "c1z"),
    )

    vertexCameraOneX = FloatField()
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField()
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField()
    c1z = vertexCameraOneZ


class VertexCameraOneAttrOperator(
    Float3CompoundBaseAttrOperator[VertexCameraOnePlugOperator]
):
    __slots__ = ()

    vertexCameraOneX = FloatField()
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField()
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField()
    c1z = vertexCameraOneZ


class VertexCameraOneField(
    Float3CompoundBaseField[VertexCameraOneAttrOperator, VertexCameraOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexCameraOneAttrOperator
    PLUG_CLS = VertexCameraOnePlugOperator

    vertexCameraOneX = FloatField()
    c1x = vertexCameraOneX

    vertexCameraOneY = FloatField()
    c1y = vertexCameraOneY

    vertexCameraOneZ = FloatField()
    c1z = vertexCameraOneZ


class OutUvPlugOperator(
    Float2CompoundBasePlugOperator["OutUvAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outU", "ou"),
        ("outV", "ov"),
    )

    outU = FloatField()
    ou = outU

    outV = FloatField()
    ov = outV


class OutUvAttrOperator(
    Float2CompoundBaseAttrOperator[OutUvPlugOperator]
):
    __slots__ = ()

    outU = FloatField()
    ou = outU

    outV = FloatField()
    ov = outV


class OutUvField(
    Float2CompoundBaseField[OutUvAttrOperator, OutUvPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutUvAttrOperator
    PLUG_CLS = OutUvPlugOperator

    outU = FloatField()
    ou = outU

    outV = FloatField()
    ov = outV


class OutVertexUvOnePlugOperator(
    Float2CompoundBasePlugOperator["OutVertexUvOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outVertexUvOneU", "o1u"),
        ("outVertexUvOneV", "o1v"),
    )

    outVertexUvOneU = FloatField()
    o1u = outVertexUvOneU

    outVertexUvOneV = FloatField()
    o1v = outVertexUvOneV


class OutVertexUvOneAttrOperator(
    Float2CompoundBaseAttrOperator[OutVertexUvOnePlugOperator]
):
    __slots__ = ()

    outVertexUvOneU = FloatField()
    o1u = outVertexUvOneU

    outVertexUvOneV = FloatField()
    o1v = outVertexUvOneV


class OutVertexUvOneField(
    Float2CompoundBaseField[OutVertexUvOneAttrOperator, OutVertexUvOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutVertexUvOneAttrOperator
    PLUG_CLS = OutVertexUvOnePlugOperator

    outVertexUvOneU = FloatField()
    o1u = outVertexUvOneU

    outVertexUvOneV = FloatField()
    o1v = outVertexUvOneV


class OutVertexUvTwoPlugOperator(
    Float2CompoundBasePlugOperator["OutVertexUvTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outVertexUvTwoU", "o2u"),
        ("outVertexUvTwoV", "o2v"),
    )

    outVertexUvTwoU = FloatField()
    o2u = outVertexUvTwoU

    outVertexUvTwoV = FloatField()
    o2v = outVertexUvTwoV


class OutVertexUvTwoAttrOperator(
    Float2CompoundBaseAttrOperator[OutVertexUvTwoPlugOperator]
):
    __slots__ = ()

    outVertexUvTwoU = FloatField()
    o2u = outVertexUvTwoU

    outVertexUvTwoV = FloatField()
    o2v = outVertexUvTwoV


class OutVertexUvTwoField(
    Float2CompoundBaseField[OutVertexUvTwoAttrOperator, OutVertexUvTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutVertexUvTwoAttrOperator
    PLUG_CLS = OutVertexUvTwoPlugOperator

    outVertexUvTwoU = FloatField()
    o2u = outVertexUvTwoU

    outVertexUvTwoV = FloatField()
    o2v = outVertexUvTwoV


class OutVertexUvThreePlugOperator(
    Float2CompoundBasePlugOperator["OutVertexUvThreeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outVertexUvThreeU", "o3u"),
        ("outVertexUvThreeV", "o3v"),
    )

    outVertexUvThreeU = FloatField()
    o3u = outVertexUvThreeU

    outVertexUvThreeV = FloatField()
    o3v = outVertexUvThreeV


class OutVertexUvThreeAttrOperator(
    Float2CompoundBaseAttrOperator[OutVertexUvThreePlugOperator]
):
    __slots__ = ()

    outVertexUvThreeU = FloatField()
    o3u = outVertexUvThreeU

    outVertexUvThreeV = FloatField()
    o3v = outVertexUvThreeV


class OutVertexUvThreeField(
    Float2CompoundBaseField[OutVertexUvThreeAttrOperator, OutVertexUvThreePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutVertexUvThreeAttrOperator
    PLUG_CLS = OutVertexUvThreePlugOperator

    outVertexUvThreeU = FloatField()
    o3u = outVertexUvThreeU

    outVertexUvThreeV = FloatField()
    o3v = outVertexUvThreeV


class OutVertexCameraOnePlugOperator(
    Float3CompoundBasePlugOperator["OutVertexCameraOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outVertexCameraOneX", "o1x"),
        ("outVertexCameraOneY", "o1y"),
        ("outVertexCameraOneZ", "o1z"),
    )

    outVertexCameraOneX = FloatField()
    o1x = outVertexCameraOneX

    outVertexCameraOneY = FloatField()
    o1y = outVertexCameraOneY

    outVertexCameraOneZ = FloatField()
    o1z = outVertexCameraOneZ


class OutVertexCameraOneAttrOperator(
    Float3CompoundBaseAttrOperator[OutVertexCameraOnePlugOperator]
):
    __slots__ = ()

    outVertexCameraOneX = FloatField()
    o1x = outVertexCameraOneX

    outVertexCameraOneY = FloatField()
    o1y = outVertexCameraOneY

    outVertexCameraOneZ = FloatField()
    o1z = outVertexCameraOneZ


class OutVertexCameraOneField(
    Float3CompoundBaseField[OutVertexCameraOneAttrOperator, OutVertexCameraOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutVertexCameraOneAttrOperator
    PLUG_CLS = OutVertexCameraOnePlugOperator

    outVertexCameraOneX = FloatField()
    o1x = outVertexCameraOneX

    outVertexCameraOneY = FloatField()
    o1y = outVertexCameraOneY

    outVertexCameraOneZ = FloatField()
    o1z = outVertexCameraOneZ
