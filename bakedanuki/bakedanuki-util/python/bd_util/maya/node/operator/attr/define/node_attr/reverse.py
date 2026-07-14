# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class InputPlugOperator(
    Float3CompoundBasePlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputX", "ix"),
        ("inputY", "iy"),
        ("inputZ", "iz"),
    )

    inputX = FloatField(default_value=0.0)
    ix = inputX

    inputY = FloatField(default_value=0.0)
    iy = inputY

    inputZ = FloatField(default_value=0.0)
    iz = inputZ


class InputAttrOperator(
    Float3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputX = FloatField(default_value=0.0)
    ix = inputX

    inputY = FloatField(default_value=0.0)
    iy = inputY

    inputZ = FloatField(default_value=0.0)
    iz = inputZ


class InputField(
    Float3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = FloatField(default_value=0.0)
    ix = inputX

    inputY = FloatField(default_value=0.0)
    iy = inputY

    inputZ = FloatField(default_value=0.0)
    iz = inputZ


class OutputPlugOperator(
    Float3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = FloatField(default_value=0.0, writable=False)
    ox = outputX

    outputY = FloatField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = FloatField(default_value=0.0, writable=False)
    oz = outputZ


class OutputAttrOperator(
    Float3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputX = FloatField(default_value=0.0, writable=False)
    ox = outputX

    outputY = FloatField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = FloatField(default_value=0.0, writable=False)
    oz = outputZ


class OutputField(
    Float3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = FloatField(default_value=0.0, writable=False)
    ox = outputX

    outputY = FloatField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = FloatField(default_value=0.0, writable=False)
    oz = outputZ
