# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField


class CompoundPlugOperator(
    CompoundPlugOperator["CompoundAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("level1S1", "l1s1"),
        ("level1S2", "l1s2"),
        ("level1S3", "l1s3"),
    )

    level1S1 = FloatField()
    l1s1 = level1S1

    level1S2 = FloatField()
    l1s2 = level1S2

    level1S3 = FloatField()
    l1s3 = level1S3


class CompoundAttrOperator(
    CompoundAttrOperator[CompoundPlugOperator]
):
    __slots__ = ()

    level1S1 = FloatField()
    l1s1 = level1S1

    level1S2 = FloatField()
    l1s2 = level1S2

    level1S3 = FloatField()
    l1s3 = level1S3


class CompoundField(
    CompoundField[CompoundAttrOperator, CompoundPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompoundAttrOperator
    PLUG_CLS = CompoundPlugOperator

    level1S1 = FloatField()
    l1s1 = level1S1

    level1S2 = FloatField()
    l1s2 = level1S2

    level1S3 = FloatField()
    l1s3 = level1S3
