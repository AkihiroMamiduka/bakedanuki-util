# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class Input_valuePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Input_valueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("valueX", "vx"),
        ("valueY", "vy"),
        ("valueZ", "vz"),
    )

    valueX = DoubleLinearField()
    vx = valueX

    valueY = DoubleLinearField()
    vy = valueY

    valueZ = DoubleLinearField()
    vz = valueZ


class Input_valueAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Input_valuePlugOperator]
):
    __slots__ = ()

    valueX = DoubleLinearField()
    vx = valueX

    valueY = DoubleLinearField()
    vy = valueY

    valueZ = DoubleLinearField()
    vz = valueZ


class Input_valueField(
    DoubleLinear3CompoundBaseField[
        Input_valueAttrOperator, Input_valuePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Input_valueAttrOperator
    PLUG_CLS = Input_valuePlugOperator

    valueX = DoubleLinearField()
    vx = valueX

    valueY = DoubleLinearField()
    vy = valueY

    valueZ = DoubleLinearField()
    vz = valueZ


class InputPlugOperator(CompoundPlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("value", "v"),
        ("weight", "w"),
    )

    value = Input_valueField(default_value=(0.0, 0.0, 0.0))
    v = value

    weight = DoubleField(default_value=0.0)
    w = weight


class InputAttrOperator(CompoundAttrOperator[InputPlugOperator]):
    __slots__ = ()

    value = Input_valueField(default_value=(0.0, 0.0, 0.0))
    v = value

    weight = DoubleField(default_value=0.0)
    w = weight


class InputField(CompoundField[InputAttrOperator, InputPlugOperator]):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


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
