# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class InputPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputX", "ix"),
        ("inputY", "iy"),
        ("inputZ", "iz"),
    )

    inputX = DoubleLinearField(default_value=0.0)
    ix = inputX

    inputY = DoubleLinearField(default_value=0.0)
    iy = inputY

    inputZ = DoubleLinearField(default_value=0.0)
    iz = inputZ


class InputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputX = DoubleLinearField(default_value=0.0)
    ix = inputX

    inputY = DoubleLinearField(default_value=0.0)
    iy = inputY

    inputZ = DoubleLinearField(default_value=0.0)
    iz = inputZ


class InputField(
    DoubleLinear3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = DoubleLinearField(default_value=0.0)
    ix = inputX

    inputY = DoubleLinearField(default_value=0.0)
    iy = inputY

    inputZ = DoubleLinearField(default_value=0.0)
    iz = inputZ


class SrcMinPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["SrcMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("srcMinX", "sminx"),
        ("srcMinY", "sminy"),
        ("srcMinZ", "sminz"),
    )

    srcMinX = DoubleLinearField(default_value=0.0)
    sminx = srcMinX

    srcMinY = DoubleLinearField(default_value=0.0)
    sminy = srcMinY

    srcMinZ = DoubleLinearField(default_value=0.0)
    sminz = srcMinZ


class SrcMinAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[SrcMinPlugOperator]
):
    __slots__ = ()

    srcMinX = DoubleLinearField(default_value=0.0)
    sminx = srcMinX

    srcMinY = DoubleLinearField(default_value=0.0)
    sminy = srcMinY

    srcMinZ = DoubleLinearField(default_value=0.0)
    sminz = srcMinZ


class SrcMinField(
    DoubleLinear3CompoundBaseField[SrcMinAttrOperator, SrcMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SrcMinAttrOperator
    PLUG_CLS = SrcMinPlugOperator

    srcMinX = DoubleLinearField(default_value=0.0)
    sminx = srcMinX

    srcMinY = DoubleLinearField(default_value=0.0)
    sminy = srcMinY

    srcMinZ = DoubleLinearField(default_value=0.0)
    sminz = srcMinZ


class SrcMaxPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["SrcMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("srcMaxX", "smaxx"),
        ("srcMaxY", "smaxy"),
        ("srcMaxZ", "smaxz"),
    )

    srcMaxX = DoubleLinearField(default_value=1.0)
    smaxx = srcMaxX

    srcMaxY = DoubleLinearField(default_value=1.0)
    smaxy = srcMaxY

    srcMaxZ = DoubleLinearField(default_value=1.0)
    smaxz = srcMaxZ


class SrcMaxAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[SrcMaxPlugOperator]
):
    __slots__ = ()

    srcMaxX = DoubleLinearField(default_value=1.0)
    smaxx = srcMaxX

    srcMaxY = DoubleLinearField(default_value=1.0)
    smaxy = srcMaxY

    srcMaxZ = DoubleLinearField(default_value=1.0)
    smaxz = srcMaxZ


class SrcMaxField(
    DoubleLinear3CompoundBaseField[SrcMaxAttrOperator, SrcMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SrcMaxAttrOperator
    PLUG_CLS = SrcMaxPlugOperator

    srcMaxX = DoubleLinearField(default_value=1.0)
    smaxx = srcMaxX

    srcMaxY = DoubleLinearField(default_value=1.0)
    smaxy = srcMaxY

    srcMaxZ = DoubleLinearField(default_value=1.0)
    smaxz = srcMaxZ


class DstMinPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["DstMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dstMinX", "dminx"),
        ("dstMinY", "dminy"),
        ("dstMinZ", "dminz"),
    )

    dstMinX = DoubleLinearField(default_value=0.0)
    dminx = dstMinX

    dstMinY = DoubleLinearField(default_value=0.0)
    dminy = dstMinY

    dstMinZ = DoubleLinearField(default_value=0.0)
    dminz = dstMinZ


class DstMinAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[DstMinPlugOperator]
):
    __slots__ = ()

    dstMinX = DoubleLinearField(default_value=0.0)
    dminx = dstMinX

    dstMinY = DoubleLinearField(default_value=0.0)
    dminy = dstMinY

    dstMinZ = DoubleLinearField(default_value=0.0)
    dminz = dstMinZ


class DstMinField(
    DoubleLinear3CompoundBaseField[DstMinAttrOperator, DstMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DstMinAttrOperator
    PLUG_CLS = DstMinPlugOperator

    dstMinX = DoubleLinearField(default_value=0.0)
    dminx = dstMinX

    dstMinY = DoubleLinearField(default_value=0.0)
    dminy = dstMinY

    dstMinZ = DoubleLinearField(default_value=0.0)
    dminz = dstMinZ


class DstMaxPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["DstMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dstMaxX", "dmaxx"),
        ("dstMaxY", "dmaxy"),
        ("dstMaxZ", "dmaxz"),
    )

    dstMaxX = DoubleLinearField(default_value=1.0)
    dmaxx = dstMaxX

    dstMaxY = DoubleLinearField(default_value=1.0)
    dmaxy = dstMaxY

    dstMaxZ = DoubleLinearField(default_value=1.0)
    dmaxz = dstMaxZ


class DstMaxAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[DstMaxPlugOperator]
):
    __slots__ = ()

    dstMaxX = DoubleLinearField(default_value=1.0)
    dmaxx = dstMaxX

    dstMaxY = DoubleLinearField(default_value=1.0)
    dmaxy = dstMaxY

    dstMaxZ = DoubleLinearField(default_value=1.0)
    dmaxz = dstMaxZ


class DstMaxField(
    DoubleLinear3CompoundBaseField[DstMaxAttrOperator, DstMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DstMaxAttrOperator
    PLUG_CLS = DstMaxPlugOperator

    dstMaxX = DoubleLinearField(default_value=1.0)
    dmaxx = dstMaxX

    dstMaxY = DoubleLinearField(default_value=1.0)
    dmaxy = dstMaxY

    dstMaxZ = DoubleLinearField(default_value=1.0)
    dmaxz = dstMaxZ


class OutputPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleLinearField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleLinearField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleLinearField(default_value=0.0, writable=False)
    oz = outputZ


class OutputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputX = DoubleLinearField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleLinearField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleLinearField(default_value=0.0, writable=False)
    oz = outputZ


class OutputField(
    DoubleLinear3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleLinearField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleLinearField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleLinearField(default_value=0.0, writable=False)
    oz = outputZ
