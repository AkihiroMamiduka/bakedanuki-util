# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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

    minR = FloatField()
    mnr = minR

    minG = FloatField()
    mng = minG

    minB = FloatField()
    mnb = minB


class MinAttrOperator(
    Float3CompoundBaseAttrOperator[MinPlugOperator]
):
    __slots__ = ()

    minR = FloatField()
    mnr = minR

    minG = FloatField()
    mng = minG

    minB = FloatField()
    mnb = minB


class MinField(
    Float3CompoundBaseField[MinAttrOperator, MinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinAttrOperator
    PLUG_CLS = MinPlugOperator

    minR = FloatField()
    mnr = minR

    minG = FloatField()
    mng = minG

    minB = FloatField()
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

    maxR = FloatField()
    mxr = maxR

    maxG = FloatField()
    mxg = maxG

    maxB = FloatField()
    mxb = maxB


class MaxAttrOperator(
    Float3CompoundBaseAttrOperator[MaxPlugOperator]
):
    __slots__ = ()

    maxR = FloatField()
    mxr = maxR

    maxG = FloatField()
    mxg = maxG

    maxB = FloatField()
    mxb = maxB


class MaxField(
    Float3CompoundBaseField[MaxAttrOperator, MaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxAttrOperator
    PLUG_CLS = MaxPlugOperator

    maxR = FloatField()
    mxr = maxR

    maxG = FloatField()
    mxg = maxG

    maxB = FloatField()
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

    inputR = FloatField()
    ipr = inputR

    inputG = FloatField()
    ipg = inputG

    inputB = FloatField()
    ipb = inputB


class InputAttrOperator(
    Float3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputR = FloatField()
    ipr = inputR

    inputG = FloatField()
    ipg = inputG

    inputB = FloatField()
    ipb = inputB


class InputField(
    Float3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputR = FloatField()
    ipr = inputR

    inputG = FloatField()
    ipg = inputG

    inputB = FloatField()
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

    outputR = FloatField()
    opr = outputR

    outputG = FloatField()
    opg = outputG

    outputB = FloatField()
    opb = outputB


class OutputAttrOperator(
    Float3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputR = FloatField()
    opr = outputR

    outputG = FloatField()
    opg = outputG

    outputB = FloatField()
    opb = outputB


class OutputField(
    Float3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputR = FloatField()
    opr = outputR

    outputG = FloatField()
    opg = outputG

    outputB = FloatField()
    opb = outputB
