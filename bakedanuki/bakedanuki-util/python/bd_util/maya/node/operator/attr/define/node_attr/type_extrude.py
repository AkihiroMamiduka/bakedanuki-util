# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.typed import TypedField


class ExtrudeCurvePlugOperator(
    CompoundPlugOperator["ExtrudeCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("extrudeCurve_Position", "excp"),
        ("extrudeCurve_Value", "excv"),
    )

    extrudeCurve_Position = FloatField(default_value=0.0)
    excp = extrudeCurve_Position

    extrudeCurve_Value = FloatField(default_value=0.0)
    excv = extrudeCurve_Value


class ExtrudeCurveAttrOperator(CompoundAttrOperator[ExtrudeCurvePlugOperator]):
    __slots__ = ()

    extrudeCurve_Position = FloatField(default_value=0.0)
    excp = extrudeCurve_Position

    extrudeCurve_Value = FloatField(default_value=0.0)
    excv = extrudeCurve_Value


class ExtrudeCurveField(
    CompoundField[ExtrudeCurveAttrOperator, ExtrudeCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtrudeCurveAttrOperator
    PLUG_CLS = ExtrudeCurvePlugOperator


class FrontBevelCurvePlugOperator(
    CompoundPlugOperator["FrontBevelCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frontBevelCurve_Position", "fbcp"),
        ("frontBevelCurve_Value", "fbcv"),
    )

    frontBevelCurve_Position = FloatField(default_value=0.0)
    fbcp = frontBevelCurve_Position

    frontBevelCurve_Value = FloatField(default_value=0.0)
    fbcv = frontBevelCurve_Value


class FrontBevelCurveAttrOperator(
    CompoundAttrOperator[FrontBevelCurvePlugOperator]
):
    __slots__ = ()

    frontBevelCurve_Position = FloatField(default_value=0.0)
    fbcp = frontBevelCurve_Position

    frontBevelCurve_Value = FloatField(default_value=0.0)
    fbcv = frontBevelCurve_Value


class FrontBevelCurveField(
    CompoundField[FrontBevelCurveAttrOperator, FrontBevelCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrontBevelCurveAttrOperator
    PLUG_CLS = FrontBevelCurvePlugOperator


class BackBevelCurvePlugOperator(
    CompoundPlugOperator["BackBevelCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backBevelCurve_Position", "bbcp"),
        ("backBevelCurve_Value", "bbcv"),
    )

    backBevelCurve_Position = FloatField(default_value=0.0)
    bbcp = backBevelCurve_Position

    backBevelCurve_Value = FloatField(default_value=0.0)
    bbcv = backBevelCurve_Value


class BackBevelCurveAttrOperator(
    CompoundAttrOperator[BackBevelCurvePlugOperator]
):
    __slots__ = ()

    backBevelCurve_Position = FloatField(default_value=0.0)
    bbcp = backBevelCurve_Position

    backBevelCurve_Value = FloatField(default_value=0.0)
    bbcv = backBevelCurve_Value


class BackBevelCurveField(
    CompoundField[BackBevelCurveAttrOperator, BackBevelCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackBevelCurveAttrOperator
    PLUG_CLS = BackBevelCurvePlugOperator


class OutComponentsPlugOperator(
    CompoundPlugOperator["OutComponentsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("capComponents", "capComponents"),
        ("bevelComponents", "bevelComponents"),
        ("extrusionComponents", "extrusionComponents"),
    )

    capComponents = TypedField()

    bevelComponents = TypedField()

    extrusionComponents = TypedField()


class OutComponentsAttrOperator(
    CompoundAttrOperator[OutComponentsPlugOperator]
):
    __slots__ = ()

    capComponents = TypedField()

    bevelComponents = TypedField()

    extrusionComponents = TypedField()


class OutComponentsField(
    CompoundField[OutComponentsAttrOperator, OutComponentsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutComponentsAttrOperator
    PLUG_CLS = OutComponentsPlugOperator

    capComponents = TypedField()

    bevelComponents = TypedField()

    extrusionComponents = TypedField()


class OuterBevelCurvePlugOperator(
    CompoundPlugOperator["OuterBevelCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outerBevelCurve_Position", "obcp"),
        ("outerBevelCurve_Value", "obcv"),
    )

    outerBevelCurve_Position = FloatField(default_value=0.0)
    obcp = outerBevelCurve_Position

    outerBevelCurve_Value = FloatField(default_value=0.0)
    obcv = outerBevelCurve_Value


class OuterBevelCurveAttrOperator(
    CompoundAttrOperator[OuterBevelCurvePlugOperator]
):
    __slots__ = ()

    outerBevelCurve_Position = FloatField(default_value=0.0)
    obcp = outerBevelCurve_Position

    outerBevelCurve_Value = FloatField(default_value=0.0)
    obcv = outerBevelCurve_Value


class OuterBevelCurveField(
    CompoundField[OuterBevelCurveAttrOperator, OuterBevelCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OuterBevelCurveAttrOperator
    PLUG_CLS = OuterBevelCurvePlugOperator
