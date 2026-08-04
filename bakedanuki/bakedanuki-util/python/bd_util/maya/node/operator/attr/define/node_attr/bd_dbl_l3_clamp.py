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


class MinPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["MinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minX", "mnx"),
        ("minY", "mny"),
        ("minZ", "mnz"),
    )

    minX = DoubleLinearField(default_value=0.0)
    mnx = minX

    minY = DoubleLinearField(default_value=0.0)
    mny = minY

    minZ = DoubleLinearField(default_value=0.0)
    mnz = minZ


class MinAttrOperator(DoubleLinear3CompoundBaseAttrOperator[MinPlugOperator]):
    __slots__ = ()

    minX = DoubleLinearField(default_value=0.0)
    mnx = minX

    minY = DoubleLinearField(default_value=0.0)
    mny = minY

    minZ = DoubleLinearField(default_value=0.0)
    mnz = minZ


class MinField(
    DoubleLinear3CompoundBaseField[MinAttrOperator, MinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinAttrOperator
    PLUG_CLS = MinPlugOperator

    minX = DoubleLinearField(default_value=0.0)
    mnx = minX

    minY = DoubleLinearField(default_value=0.0)
    mny = minY

    minZ = DoubleLinearField(default_value=0.0)
    mnz = minZ


class MaxPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["MaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxX", "mxx"),
        ("maxY", "mxy"),
        ("maxZ", "mxz"),
    )

    maxX = DoubleLinearField(default_value=1.0)
    mxx = maxX

    maxY = DoubleLinearField(default_value=1.0)
    mxy = maxY

    maxZ = DoubleLinearField(default_value=1.0)
    mxz = maxZ


class MaxAttrOperator(DoubleLinear3CompoundBaseAttrOperator[MaxPlugOperator]):
    __slots__ = ()

    maxX = DoubleLinearField(default_value=1.0)
    mxx = maxX

    maxY = DoubleLinearField(default_value=1.0)
    mxy = maxY

    maxZ = DoubleLinearField(default_value=1.0)
    mxz = maxZ


class MaxField(
    DoubleLinear3CompoundBaseField[MaxAttrOperator, MaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxAttrOperator
    PLUG_CLS = MaxPlugOperator

    maxX = DoubleLinearField(default_value=1.0)
    mxx = maxX

    maxY = DoubleLinearField(default_value=1.0)
    mxy = maxY

    maxZ = DoubleLinearField(default_value=1.0)
    mxz = maxZ


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
