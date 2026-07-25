# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.double_array import DataDoubleArrayField


class GroupingPlugOperator(
    CompoundPlugOperator["GroupingAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("solidsPerCharacter", "solidsPerCharacter"),
        ("solidsPerWord", "solidsPerWord"),
        ("solidsPerLine", "solidsPerLine"),
    )

    solidsPerCharacter = DataDoubleArrayField()

    solidsPerWord = DataDoubleArrayField()

    solidsPerLine = DataDoubleArrayField()


class GroupingAttrOperator(
    CompoundAttrOperator[GroupingPlugOperator]
):
    __slots__ = ()

    solidsPerCharacter = DataDoubleArrayField()

    solidsPerWord = DataDoubleArrayField()

    solidsPerLine = DataDoubleArrayField()


class GroupingField(
    CompoundField[GroupingAttrOperator, GroupingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GroupingAttrOperator
    PLUG_CLS = GroupingPlugOperator

    solidsPerCharacter = DataDoubleArrayField()

    solidsPerWord = DataDoubleArrayField()

    solidsPerLine = DataDoubleArrayField()


class GroupIdsPlugOperator(
    CompoundPlugOperator["GroupIdsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("capGroupId", "capGroupId"),
        ("bevelGroupId", "bevelGroupId"),
        ("extrudeGroupId", "extrudeGroupId"),
        ("charGroupId", "charGroupId"),
    )

    capGroupId = LongField(default_value=1)

    bevelGroupId = LongField(default_value=1)

    extrudeGroupId = LongField(default_value=1)

    charGroupId = LongField(multi=True, default_value=0, readable=False)


class GroupIdsAttrOperator(
    CompoundAttrOperator[GroupIdsPlugOperator]
):
    __slots__ = ()

    capGroupId = LongField(default_value=1)

    bevelGroupId = LongField(default_value=1)

    extrudeGroupId = LongField(default_value=1)

    charGroupId = LongField(multi=True, default_value=0, readable=False)


class GroupIdsField(
    CompoundField[GroupIdsAttrOperator, GroupIdsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GroupIdsAttrOperator
    PLUG_CLS = GroupIdsPlugOperator

    capGroupId = LongField(default_value=1)

    bevelGroupId = LongField(default_value=1)

    extrudeGroupId = LongField(default_value=1)

    charGroupId = LongField(multi=True, default_value=0, readable=False)


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


class FrontBevelCurvePlugOperator(
    CompoundPlugOperator["FrontBevelCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frontBevelCurve_Position", "frontBevelCurvep"),
        ("frontBevelCurve_Value", "frontBevelCurvev"),
    )

    frontBevelCurve_Position = FloatField(default_value=0.0)
    frontBevelCurvep = frontBevelCurve_Position

    frontBevelCurve_Value = FloatField(default_value=0.0)
    frontBevelCurvev = frontBevelCurve_Value


class FrontBevelCurveAttrOperator(
    CompoundAttrOperator[FrontBevelCurvePlugOperator]
):
    __slots__ = ()

    frontBevelCurve_Position = FloatField(default_value=0.0)
    frontBevelCurvep = frontBevelCurve_Position

    frontBevelCurve_Value = FloatField(default_value=0.0)
    frontBevelCurvev = frontBevelCurve_Value


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
        ("backBevelCurve_Position", "backBevelCurvep"),
        ("backBevelCurve_Value", "backBevelCurvev"),
    )

    backBevelCurve_Position = FloatField(default_value=0.0)
    backBevelCurvep = backBevelCurve_Position

    backBevelCurve_Value = FloatField(default_value=0.0)
    backBevelCurvev = backBevelCurve_Value


class BackBevelCurveAttrOperator(
    CompoundAttrOperator[BackBevelCurvePlugOperator]
):
    __slots__ = ()

    backBevelCurve_Position = FloatField(default_value=0.0)
    backBevelCurvep = backBevelCurve_Position

    backBevelCurve_Value = FloatField(default_value=0.0)
    backBevelCurvev = backBevelCurve_Value


class BackBevelCurveField(
    CompoundField[BackBevelCurveAttrOperator, BackBevelCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackBevelCurveAttrOperator
    PLUG_CLS = BackBevelCurvePlugOperator


class ExtrudeCurvePlugOperator(
    CompoundPlugOperator["ExtrudeCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("extrudeCurve_Position", "extrudeCurvep"),
        ("extrudeCurve_Value", "extrudeCurvev"),
    )

    extrudeCurve_Position = FloatField(default_value=0.0)
    extrudeCurvep = extrudeCurve_Position

    extrudeCurve_Value = FloatField(default_value=0.0)
    extrudeCurvev = extrudeCurve_Value


class ExtrudeCurveAttrOperator(
    CompoundAttrOperator[ExtrudeCurvePlugOperator]
):
    __slots__ = ()

    extrudeCurve_Position = FloatField(default_value=0.0)
    extrudeCurvep = extrudeCurve_Position

    extrudeCurve_Value = FloatField(default_value=0.0)
    extrudeCurvev = extrudeCurve_Value


class ExtrudeCurveField(
    CompoundField[ExtrudeCurveAttrOperator, ExtrudeCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtrudeCurveAttrOperator
    PLUG_CLS = ExtrudeCurvePlugOperator


class OuterBevelCurvePlugOperator(
    CompoundPlugOperator["OuterBevelCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outerBevelCurve_Position", "outerBevelCurvep"),
        ("outerBevelCurve_Value", "outerBevelCurvev"),
    )

    outerBevelCurve_Position = FloatField(default_value=0.0)
    outerBevelCurvep = outerBevelCurve_Position

    outerBevelCurve_Value = FloatField(default_value=0.0)
    outerBevelCurvev = outerBevelCurve_Value


class OuterBevelCurveAttrOperator(
    CompoundAttrOperator[OuterBevelCurvePlugOperator]
):
    __slots__ = ()

    outerBevelCurve_Position = FloatField(default_value=0.0)
    outerBevelCurvep = outerBevelCurve_Position

    outerBevelCurve_Value = FloatField(default_value=0.0)
    outerBevelCurvev = outerBevelCurve_Value


class OuterBevelCurveField(
    CompoundField[OuterBevelCurveAttrOperator, OuterBevelCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OuterBevelCurveAttrOperator
    PLUG_CLS = OuterBevelCurvePlugOperator
