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


class SourceMinimumPlugOperator(
    Double3CompoundBasePlugOperator["SourceMinimumAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sourceMinimumX", "sminx"),
        ("sourceMinimumY", "sminy"),
        ("sourceMinimumZ", "sminz"),
    )

    sourceMinimumX = DoubleField(default_value=0.0)
    sminx = sourceMinimumX

    sourceMinimumY = DoubleField(default_value=0.0)
    sminy = sourceMinimumY

    sourceMinimumZ = DoubleField(default_value=0.0)
    sminz = sourceMinimumZ


class SourceMinimumAttrOperator(
    Double3CompoundBaseAttrOperator[SourceMinimumPlugOperator]
):
    __slots__ = ()

    sourceMinimumX = DoubleField(default_value=0.0)
    sminx = sourceMinimumX

    sourceMinimumY = DoubleField(default_value=0.0)
    sminy = sourceMinimumY

    sourceMinimumZ = DoubleField(default_value=0.0)
    sminz = sourceMinimumZ


class SourceMinimumField(
    Double3CompoundBaseField[
        SourceMinimumAttrOperator, SourceMinimumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SourceMinimumAttrOperator
    PLUG_CLS = SourceMinimumPlugOperator

    sourceMinimumX = DoubleField(default_value=0.0)
    sminx = sourceMinimumX

    sourceMinimumY = DoubleField(default_value=0.0)
    sminy = sourceMinimumY

    sourceMinimumZ = DoubleField(default_value=0.0)
    sminz = sourceMinimumZ


class SourceMaximumPlugOperator(
    Double3CompoundBasePlugOperator["SourceMaximumAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sourceMaximumX", "smaxx"),
        ("sourceMaximumY", "smaxy"),
        ("sourceMaximumZ", "smaxz"),
    )

    sourceMaximumX = DoubleField(default_value=1.0)
    smaxx = sourceMaximumX

    sourceMaximumY = DoubleField(default_value=1.0)
    smaxy = sourceMaximumY

    sourceMaximumZ = DoubleField(default_value=1.0)
    smaxz = sourceMaximumZ


class SourceMaximumAttrOperator(
    Double3CompoundBaseAttrOperator[SourceMaximumPlugOperator]
):
    __slots__ = ()

    sourceMaximumX = DoubleField(default_value=1.0)
    smaxx = sourceMaximumX

    sourceMaximumY = DoubleField(default_value=1.0)
    smaxy = sourceMaximumY

    sourceMaximumZ = DoubleField(default_value=1.0)
    smaxz = sourceMaximumZ


class SourceMaximumField(
    Double3CompoundBaseField[
        SourceMaximumAttrOperator, SourceMaximumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SourceMaximumAttrOperator
    PLUG_CLS = SourceMaximumPlugOperator

    sourceMaximumX = DoubleField(default_value=1.0)
    smaxx = sourceMaximumX

    sourceMaximumY = DoubleField(default_value=1.0)
    smaxy = sourceMaximumY

    sourceMaximumZ = DoubleField(default_value=1.0)
    smaxz = sourceMaximumZ


class TargetMinimumPlugOperator(
    Double3CompoundBasePlugOperator["TargetMinimumAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetMinimumX", "tminx"),
        ("targetMinimumY", "tminy"),
        ("targetMinimumZ", "tminz"),
    )

    targetMinimumX = DoubleField(default_value=0.0)
    tminx = targetMinimumX

    targetMinimumY = DoubleField(default_value=0.0)
    tminy = targetMinimumY

    targetMinimumZ = DoubleField(default_value=0.0)
    tminz = targetMinimumZ


class TargetMinimumAttrOperator(
    Double3CompoundBaseAttrOperator[TargetMinimumPlugOperator]
):
    __slots__ = ()

    targetMinimumX = DoubleField(default_value=0.0)
    tminx = targetMinimumX

    targetMinimumY = DoubleField(default_value=0.0)
    tminy = targetMinimumY

    targetMinimumZ = DoubleField(default_value=0.0)
    tminz = targetMinimumZ


class TargetMinimumField(
    Double3CompoundBaseField[
        TargetMinimumAttrOperator, TargetMinimumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TargetMinimumAttrOperator
    PLUG_CLS = TargetMinimumPlugOperator

    targetMinimumX = DoubleField(default_value=0.0)
    tminx = targetMinimumX

    targetMinimumY = DoubleField(default_value=0.0)
    tminy = targetMinimumY

    targetMinimumZ = DoubleField(default_value=0.0)
    tminz = targetMinimumZ


class TargetMaximumPlugOperator(
    Double3CompoundBasePlugOperator["TargetMaximumAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetMaximumX", "tmaxx"),
        ("targetMaximumY", "tmaxy"),
        ("targetMaximumZ", "tmaxz"),
    )

    targetMaximumX = DoubleField(default_value=1.0)
    tmaxx = targetMaximumX

    targetMaximumY = DoubleField(default_value=1.0)
    tmaxy = targetMaximumY

    targetMaximumZ = DoubleField(default_value=1.0)
    tmaxz = targetMaximumZ


class TargetMaximumAttrOperator(
    Double3CompoundBaseAttrOperator[TargetMaximumPlugOperator]
):
    __slots__ = ()

    targetMaximumX = DoubleField(default_value=1.0)
    tmaxx = targetMaximumX

    targetMaximumY = DoubleField(default_value=1.0)
    tmaxy = targetMaximumY

    targetMaximumZ = DoubleField(default_value=1.0)
    tmaxz = targetMaximumZ


class TargetMaximumField(
    Double3CompoundBaseField[
        TargetMaximumAttrOperator, TargetMaximumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TargetMaximumAttrOperator
    PLUG_CLS = TargetMaximumPlugOperator

    targetMaximumX = DoubleField(default_value=1.0)
    tmaxx = targetMaximumX

    targetMaximumY = DoubleField(default_value=1.0)
    tmaxy = targetMaximumY

    targetMaximumZ = DoubleField(default_value=1.0)
    tmaxz = targetMaximumZ


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
