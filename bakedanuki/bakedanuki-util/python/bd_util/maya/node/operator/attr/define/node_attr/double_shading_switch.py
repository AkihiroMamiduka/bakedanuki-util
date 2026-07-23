# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound.float2 import Float2Field


class InputPlugOperator(
    CompoundPlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inDouble", "idl"),
        ("inShape", "is"),
    )

    inDouble = Float2Field(default_value=(0.0, 0.0))
    idl = inDouble

    inShape = MessageField()
    is_ = inShape


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inDouble = Float2Field(default_value=(0.0, 0.0))
    idl = inDouble

    inShape = MessageField()
    is_ = inShape


class InputField(
    CompoundField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class DefaultPlugOperator(
    Float2CompoundBasePlugOperator["DefaultAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("defComp1", "dc1"),
        ("defComp2", "dc2"),
    )

    defComp1 = FloatField(default_value=0.0)
    dc1 = defComp1

    defComp2 = FloatField(default_value=0.0)
    dc2 = defComp2


class DefaultAttrOperator(
    Float2CompoundBaseAttrOperator[DefaultPlugOperator]
):
    __slots__ = ()

    defComp1 = FloatField(default_value=0.0)
    dc1 = defComp1

    defComp2 = FloatField(default_value=0.0)
    dc2 = defComp2


class DefaultField(
    Float2CompoundBaseField[DefaultAttrOperator, DefaultPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultAttrOperator
    PLUG_CLS = DefaultPlugOperator

    defComp1 = FloatField(default_value=0.0)
    dc1 = defComp1

    defComp2 = FloatField(default_value=0.0)
    dc2 = defComp2


class OutputPlugOperator(
    Float2CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outComp1", "oc1"),
        ("outComp2", "oc2"),
    )

    outComp1 = FloatField(default_value=0.0, writable=False)
    oc1 = outComp1

    outComp2 = FloatField(default_value=0.0, writable=False)
    oc2 = outComp2


class OutputAttrOperator(
    Float2CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outComp1 = FloatField(default_value=0.0, writable=False)
    oc1 = outComp1

    outComp2 = FloatField(default_value=0.0, writable=False)
    oc2 = outComp2


class OutputField(
    Float2CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outComp1 = FloatField(default_value=0.0, writable=False)
    oc1 = outComp1

    outComp2 = FloatField(default_value=0.0, writable=False)
    oc2 = outComp2
