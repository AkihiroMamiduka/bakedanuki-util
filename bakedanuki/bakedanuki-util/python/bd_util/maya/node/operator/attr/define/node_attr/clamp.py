# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class MinPlugOperator(
    Float3CompoundBasePlugOperator["MinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minR", "mnr"),
        ("minG", "mng"),
        ("minB", "mnb"),
    )

    minR = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mnr = minR

    minG = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mng = minG

    minB = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mnb = minB


class MinAttrOperator(
    Float3CompoundBaseAttrOperator[MinPlugOperator]
):
    __slots__ = ()

    minR = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mnr = minR

    minG = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mng = minG

    minB = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mnb = minB


class MinField(
    Float3CompoundBaseField[MinAttrOperator, MinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinAttrOperator
    PLUG_CLS = MinPlugOperator

    minR = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mnr = minR

    minG = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mng = minG

    minB = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mnb = minB


class MaxPlugOperator(
    Float3CompoundBasePlugOperator["MaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxR", "mxr"),
        ("maxG", "mxg"),
        ("maxB", "mxb"),
    )

    maxR = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mxr = maxR

    maxG = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mxg = maxG

    maxB = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mxb = maxB


class MaxAttrOperator(
    Float3CompoundBaseAttrOperator[MaxPlugOperator]
):
    __slots__ = ()

    maxR = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mxr = maxR

    maxG = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mxg = maxG

    maxB = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mxb = maxB


class MaxField(
    Float3CompoundBaseField[MaxAttrOperator, MaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxAttrOperator
    PLUG_CLS = MaxPlugOperator

    maxR = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mxr = maxR

    maxG = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mxg = maxG

    maxB = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    mxb = maxB


class InputPlugOperator(
    Float3CompoundBasePlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputR", "ipr"),
        ("inputG", "ipg"),
        ("inputB", "ipb"),
    )

    inputR = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    ipr = inputR

    inputG = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    ipg = inputG

    inputB = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    ipb = inputB


class InputAttrOperator(
    Float3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputR = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    ipr = inputR

    inputG = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    ipg = inputG

    inputB = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    ipb = inputB


class InputField(
    Float3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputR = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    ipr = inputR

    inputG = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    ipg = inputG

    inputB = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    ipb = inputB


class OutputPlugOperator(
    Float3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputR", "opr"),
        ("outputG", "opg"),
        ("outputB", "opb"),
    )

    outputR = FloatField(default_value=0.0, writable=False)
    opr = outputR

    outputG = FloatField(default_value=0.0, writable=False)
    opg = outputG

    outputB = FloatField(default_value=0.0, writable=False)
    opb = outputB


class OutputAttrOperator(
    Float3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputR = FloatField(default_value=0.0, writable=False)
    opr = outputR

    outputG = FloatField(default_value=0.0, writable=False)
    opg = outputG

    outputB = FloatField(default_value=0.0, writable=False)
    opb = outputB


class OutputField(
    Float3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputR = FloatField(default_value=0.0, writable=False)
    opr = outputR

    outputG = FloatField(default_value=0.0, writable=False)
    opg = outputG

    outputB = FloatField(default_value=0.0, writable=False)
    opb = outputB
