# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class InputPlugOperator(
    CompoundPlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inQuad", "iq"),
        ("inShape", "is"),
    )

    inQuad = CompoundField()
    iq = inQuad

    inShape = MessageField()
    is_ = inShape


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inQuad = CompoundField()
    iq = inQuad

    inShape = MessageField()
    is_ = inShape


class InputField(
    CompoundField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class DefaultPlugOperator(
    CompoundPlugOperator["DefaultAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("defTriple", "dtr"),
        ("defSingle", "dsi"),
    )

    defTriple = Float3Field(default_value=(0.800000011920929, 0.800000011920929, 0.800000011920929))
    dtr = defTriple

    defSingle = FloatField(default_value=0.0)
    dsi = defSingle


class DefaultAttrOperator(
    CompoundAttrOperator[DefaultPlugOperator]
):
    __slots__ = ()

    defTriple = Float3Field(default_value=(0.800000011920929, 0.800000011920929, 0.800000011920929))
    dtr = defTriple

    defSingle = FloatField(default_value=0.0)
    dsi = defSingle


class DefaultField(
    CompoundField[DefaultAttrOperator, DefaultPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultAttrOperator
    PLUG_CLS = DefaultPlugOperator

    defTriple = Float3Field(default_value=(0.800000011920929, 0.800000011920929, 0.800000011920929))
    dtr = defTriple

    defSingle = FloatField(default_value=0.0)
    dsi = defSingle


class OutputPlugOperator(
    CompoundPlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTriple", "otr"),
        ("outSingle", "osi"),
    )

    outTriple = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    otr = outTriple

    outSingle = FloatField(default_value=0.0, writable=False)
    osi = outSingle


class OutputAttrOperator(
    CompoundAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outTriple = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    otr = outTriple

    outSingle = FloatField(default_value=0.0, writable=False)
    osi = outSingle


class OutputField(
    CompoundField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outTriple = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    otr = outTriple

    outSingle = FloatField(default_value=0.0, writable=False)
    osi = outSingle
