# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
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


class BasePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["BaseAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseX", "bx"),
        ("baseY", "by"),
        ("baseZ", "bz"),
    )

    baseX = DoubleLinearField(default_value=1.0)
    bx = baseX

    baseY = DoubleLinearField(default_value=1.0)
    by = baseY

    baseZ = DoubleLinearField(default_value=1.0)
    bz = baseZ


class BaseAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[BasePlugOperator]
):
    __slots__ = ()

    baseX = DoubleLinearField(default_value=1.0)
    bx = baseX

    baseY = DoubleLinearField(default_value=1.0)
    by = baseY

    baseZ = DoubleLinearField(default_value=1.0)
    bz = baseZ


class BaseField(
    DoubleLinear3CompoundBaseField[BaseAttrOperator, BasePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseAttrOperator
    PLUG_CLS = BasePlugOperator

    baseX = DoubleLinearField(default_value=1.0)
    bx = baseX

    baseY = DoubleLinearField(default_value=1.0)
    by = baseY

    baseZ = DoubleLinearField(default_value=1.0)
    bz = baseZ


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
