# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class InputPlugOperator(Double3CompoundBasePlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputX", "ix"),
        ("inputY", "iy"),
        ("inputZ", "iz"),
    )

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class InputAttrOperator(Double3CompoundBaseAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class InputField(
    Double3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class SrcMinPlugOperator(
    Double3CompoundBasePlugOperator["SrcMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("srcMinX", "sminx"),
        ("srcMinY", "sminy"),
        ("srcMinZ", "sminz"),
    )

    srcMinX = DoubleField(default_value=0.0)
    sminx = srcMinX

    srcMinY = DoubleField(default_value=0.0)
    sminy = srcMinY

    srcMinZ = DoubleField(default_value=0.0)
    sminz = srcMinZ


class SrcMinAttrOperator(Double3CompoundBaseAttrOperator[SrcMinPlugOperator]):
    __slots__ = ()

    srcMinX = DoubleField(default_value=0.0)
    sminx = srcMinX

    srcMinY = DoubleField(default_value=0.0)
    sminy = srcMinY

    srcMinZ = DoubleField(default_value=0.0)
    sminz = srcMinZ


class SrcMinField(
    Double3CompoundBaseField[SrcMinAttrOperator, SrcMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SrcMinAttrOperator
    PLUG_CLS = SrcMinPlugOperator

    srcMinX = DoubleField(default_value=0.0)
    sminx = srcMinX

    srcMinY = DoubleField(default_value=0.0)
    sminy = srcMinY

    srcMinZ = DoubleField(default_value=0.0)
    sminz = srcMinZ


class SrcMaxPlugOperator(
    Double3CompoundBasePlugOperator["SrcMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("srcMaxX", "smaxx"),
        ("srcMaxY", "smaxy"),
        ("srcMaxZ", "smaxz"),
    )

    srcMaxX = DoubleField(default_value=1.0)
    smaxx = srcMaxX

    srcMaxY = DoubleField(default_value=1.0)
    smaxy = srcMaxY

    srcMaxZ = DoubleField(default_value=1.0)
    smaxz = srcMaxZ


class SrcMaxAttrOperator(Double3CompoundBaseAttrOperator[SrcMaxPlugOperator]):
    __slots__ = ()

    srcMaxX = DoubleField(default_value=1.0)
    smaxx = srcMaxX

    srcMaxY = DoubleField(default_value=1.0)
    smaxy = srcMaxY

    srcMaxZ = DoubleField(default_value=1.0)
    smaxz = srcMaxZ


class SrcMaxField(
    Double3CompoundBaseField[SrcMaxAttrOperator, SrcMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SrcMaxAttrOperator
    PLUG_CLS = SrcMaxPlugOperator

    srcMaxX = DoubleField(default_value=1.0)
    smaxx = srcMaxX

    srcMaxY = DoubleField(default_value=1.0)
    smaxy = srcMaxY

    srcMaxZ = DoubleField(default_value=1.0)
    smaxz = srcMaxZ


class DstMinPlugOperator(
    Double3CompoundBasePlugOperator["DstMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dstMinX", "dminx"),
        ("dstMinY", "dminy"),
        ("dstMinZ", "dminz"),
    )

    dstMinX = DoubleField(default_value=0.0)
    dminx = dstMinX

    dstMinY = DoubleField(default_value=0.0)
    dminy = dstMinY

    dstMinZ = DoubleField(default_value=0.0)
    dminz = dstMinZ


class DstMinAttrOperator(Double3CompoundBaseAttrOperator[DstMinPlugOperator]):
    __slots__ = ()

    dstMinX = DoubleField(default_value=0.0)
    dminx = dstMinX

    dstMinY = DoubleField(default_value=0.0)
    dminy = dstMinY

    dstMinZ = DoubleField(default_value=0.0)
    dminz = dstMinZ


class DstMinField(
    Double3CompoundBaseField[DstMinAttrOperator, DstMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DstMinAttrOperator
    PLUG_CLS = DstMinPlugOperator

    dstMinX = DoubleField(default_value=0.0)
    dminx = dstMinX

    dstMinY = DoubleField(default_value=0.0)
    dminy = dstMinY

    dstMinZ = DoubleField(default_value=0.0)
    dminz = dstMinZ


class DstMaxPlugOperator(
    Double3CompoundBasePlugOperator["DstMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dstMaxX", "dmaxx"),
        ("dstMaxY", "dmaxy"),
        ("dstMaxZ", "dmaxz"),
    )

    dstMaxX = DoubleField(default_value=1.0)
    dmaxx = dstMaxX

    dstMaxY = DoubleField(default_value=1.0)
    dmaxy = dstMaxY

    dstMaxZ = DoubleField(default_value=1.0)
    dmaxz = dstMaxZ


class DstMaxAttrOperator(Double3CompoundBaseAttrOperator[DstMaxPlugOperator]):
    __slots__ = ()

    dstMaxX = DoubleField(default_value=1.0)
    dmaxx = dstMaxX

    dstMaxY = DoubleField(default_value=1.0)
    dmaxy = dstMaxY

    dstMaxZ = DoubleField(default_value=1.0)
    dmaxz = dstMaxZ


class DstMaxField(
    Double3CompoundBaseField[DstMaxAttrOperator, DstMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DstMaxAttrOperator
    PLUG_CLS = DstMaxPlugOperator

    dstMaxX = DoubleField(default_value=1.0)
    dmaxx = dstMaxX

    dstMaxY = DoubleField(default_value=1.0)
    dmaxy = dstMaxY

    dstMaxZ = DoubleField(default_value=1.0)
    dmaxz = dstMaxZ


class OutputPlugOperator(
    Double3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ


class OutputAttrOperator(Double3CompoundBaseAttrOperator[OutputPlugOperator]):
    __slots__ = ()

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ


class OutputField(
    Double3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ
