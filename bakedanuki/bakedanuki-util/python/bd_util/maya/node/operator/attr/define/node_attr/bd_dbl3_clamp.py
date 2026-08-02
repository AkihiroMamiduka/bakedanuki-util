# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class InputPlugOperator(Double3CompoundBasePlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputX", "ix"),
        ("inputY", "iy"),
        ("inputZ", "iz"),
    )

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class InputAttrOperator(Double3CompoundBaseAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class InputField(
    Double3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class MinimumPlugOperator(
    Double3CompoundBasePlugOperator["MinimumAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minimumX", "minx"),
        ("minimumY", "miny"),
        ("minimumZ", "minz"),
    )

    minimumX = DoubleField(default_value=0.0)
    minx = minimumX

    minimumY = DoubleField(default_value=0.0)
    miny = minimumY

    minimumZ = DoubleField(default_value=0.0)
    minz = minimumZ


class MinimumAttrOperator(
    Double3CompoundBaseAttrOperator[MinimumPlugOperator]
):
    __slots__ = ()

    minimumX = DoubleField(default_value=0.0)
    minx = minimumX

    minimumY = DoubleField(default_value=0.0)
    miny = minimumY

    minimumZ = DoubleField(default_value=0.0)
    minz = minimumZ


class MinimumField(
    Double3CompoundBaseField[MinimumAttrOperator, MinimumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinimumAttrOperator
    PLUG_CLS = MinimumPlugOperator

    minimumX = DoubleField(default_value=0.0)
    minx = minimumX

    minimumY = DoubleField(default_value=0.0)
    miny = minimumY

    minimumZ = DoubleField(default_value=0.0)
    minz = minimumZ


class MaximumPlugOperator(
    Double3CompoundBasePlugOperator["MaximumAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maximumX", "maxx"),
        ("maximumY", "maxy"),
        ("maximumZ", "maxz"),
    )

    maximumX = DoubleField(default_value=1.0)
    maxx = maximumX

    maximumY = DoubleField(default_value=1.0)
    maxy = maximumY

    maximumZ = DoubleField(default_value=1.0)
    maxz = maximumZ


class MaximumAttrOperator(
    Double3CompoundBaseAttrOperator[MaximumPlugOperator]
):
    __slots__ = ()

    maximumX = DoubleField(default_value=1.0)
    maxx = maximumX

    maximumY = DoubleField(default_value=1.0)
    maxy = maximumY

    maximumZ = DoubleField(default_value=1.0)
    maxz = maximumZ


class MaximumField(
    Double3CompoundBaseField[MaximumAttrOperator, MaximumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaximumAttrOperator
    PLUG_CLS = MaximumPlugOperator

    maximumX = DoubleField(default_value=1.0)
    maxx = maximumX

    maximumY = DoubleField(default_value=1.0)
    maxy = maximumY

    maximumZ = DoubleField(default_value=1.0)
    maxz = maximumZ


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
