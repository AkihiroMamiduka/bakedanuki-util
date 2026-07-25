# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField


class CompoundValuePlugOperator(
    CompoundPlugOperator["CompoundValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("level1S1", "l1s1"),
        ("level1S2", "l1s2"),
        ("level1S3", "l1s3"),
    )

    level1S1 = FloatField(default_value=0.0)
    l1s1 = level1S1

    level1S2 = FloatField(default_value=0.0)
    l1s2 = level1S2

    level1S3 = FloatField(default_value=0.0)
    l1s3 = level1S3


class CompoundValueAttrOperator(
    CompoundAttrOperator[CompoundValuePlugOperator]
):
    __slots__ = ()

    level1S1 = FloatField(default_value=0.0)
    l1s1 = level1S1

    level1S2 = FloatField(default_value=0.0)
    l1s2 = level1S2

    level1S3 = FloatField(default_value=0.0)
    l1s3 = level1S3


class CompoundValueField(
    CompoundField[CompoundValueAttrOperator, CompoundValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompoundValueAttrOperator
    PLUG_CLS = CompoundValuePlugOperator

    level1S1 = FloatField(default_value=0.0)
    l1s1 = level1S1

    level1S2 = FloatField(default_value=0.0)
    l1s2 = level1S2

    level1S3 = FloatField(default_value=0.0)
    l1s3 = level1S3
