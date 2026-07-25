# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class InputPlugOperator(
    CompoundPlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inTriple", "it"),
        ("inShape", "is"),
    )

    inTriple = Float3Field(default_value=(0.0, 0.0, 0.0))
    it = inTriple

    inShape = MessageField()
    is_ = inShape


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inTriple = Float3Field(default_value=(0.0, 0.0, 0.0))
    it = inTriple

    inShape = MessageField()
    is_ = inShape


class InputField(
    CompoundField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class DefaultPlugOperator(
    Float3CompoundBasePlugOperator["DefaultAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("defComp1", "dc1"),
        ("defComp2", "dc2"),
        ("defComp3", "dc3"),
    )

    defComp1 = FloatField(default_value=0.800000011920929)
    dc1 = defComp1

    defComp2 = FloatField(default_value=0.800000011920929)
    dc2 = defComp2

    defComp3 = FloatField(default_value=0.800000011920929)
    dc3 = defComp3


class DefaultAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultPlugOperator]
):
    __slots__ = ()

    defComp1 = FloatField(default_value=0.800000011920929)
    dc1 = defComp1

    defComp2 = FloatField(default_value=0.800000011920929)
    dc2 = defComp2

    defComp3 = FloatField(default_value=0.800000011920929)
    dc3 = defComp3


class DefaultField(
    Float3CompoundBaseField[DefaultAttrOperator, DefaultPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultAttrOperator
    PLUG_CLS = DefaultPlugOperator

    defComp1 = FloatField(default_value=0.800000011920929)
    dc1 = defComp1

    defComp2 = FloatField(default_value=0.800000011920929)
    dc2 = defComp2

    defComp3 = FloatField(default_value=0.800000011920929)
    dc3 = defComp3


class OutputPlugOperator(
    Float3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outComp1", "oc1"),
        ("outComp2", "oc2"),
        ("outComp3", "oc3"),
    )

    outComp1 = FloatField(default_value=0.0, writable=False)
    oc1 = outComp1

    outComp2 = FloatField(default_value=0.0, writable=False)
    oc2 = outComp2

    outComp3 = FloatField(default_value=0.0, writable=False)
    oc3 = outComp3


class OutputAttrOperator(
    Float3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outComp1 = FloatField(default_value=0.0, writable=False)
    oc1 = outComp1

    outComp2 = FloatField(default_value=0.0, writable=False)
    oc2 = outComp2

    outComp3 = FloatField(default_value=0.0, writable=False)
    oc3 = outComp3


class OutputField(
    Float3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outComp1 = FloatField(default_value=0.0, writable=False)
    oc1 = outComp1

    outComp2 = FloatField(default_value=0.0, writable=False)
    oc2 = outComp2

    outComp3 = FloatField(default_value=0.0, writable=False)
    oc3 = outComp3
