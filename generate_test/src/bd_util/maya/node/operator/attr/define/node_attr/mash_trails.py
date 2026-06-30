# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class TranslateOutPPPlugOperator(
    CompoundPlugOperator["TranslateOutPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionOutPP", "positionOutPP"),
        ("scaleOutPP", "scaleOutPP"),
    )

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()


class TranslateOutPPAttrOperator(
    CompoundAttrOperator[TranslateOutPPPlugOperator]
):
    __slots__ = ()

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()


class TranslateOutPPField(
    CompoundField[TranslateOutPPAttrOperator, TranslateOutPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateOutPPAttrOperator
    PLUG_CLS = TranslateOutPPPlugOperator

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()


class TranslateInPPPlugOperator(
    CompoundPlugOperator["TranslateInPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionInPP", "positionInPP"),
    )

    positionInPP = DataVectorArrayField()


class TranslateInPPAttrOperator(
    CompoundAttrOperator[TranslateInPPPlugOperator]
):
    __slots__ = ()

    positionInPP = DataVectorArrayField()


class TranslateInPPField(
    CompoundField[TranslateInPPAttrOperator, TranslateInPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateInPPAttrOperator
    PLUG_CLS = TranslateInPPPlugOperator

    positionInPP = DataVectorArrayField()


class UpVectorPlugOperator(
    Float3CompoundBasePlugOperator["UpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("upVector0", "upVector0"),
        ("upVector1", "upVector1"),
        ("upVector2", "upVector2"),
    )

    upVector0 = FloatField()

    upVector1 = FloatField()

    upVector2 = FloatField()


class UpVectorAttrOperator(
    Float3CompoundBaseAttrOperator[UpVectorPlugOperator]
):
    __slots__ = ()

    upVector0 = FloatField()

    upVector1 = FloatField()

    upVector2 = FloatField()


class UpVectorField(
    Float3CompoundBaseField[UpVectorAttrOperator, UpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpVectorAttrOperator
    PLUG_CLS = UpVectorPlugOperator

    upVector0 = FloatField()

    upVector1 = FloatField()

    upVector2 = FloatField()


class TrailTaperCurvePlugOperator(
    CompoundPlugOperator["TrailTaperCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("trailTaperCurve_Position", "trailTaperCurvep"),
        ("trailTaperCurve_Value", "trailTaperCurvev"),
    )

    trailTaperCurve_Position = FloatField()
    trailTaperCurvep = trailTaperCurve_Position

    trailTaperCurve_Value = FloatField()
    trailTaperCurvev = trailTaperCurve_Value


class TrailTaperCurveAttrOperator(
    CompoundAttrOperator[TrailTaperCurvePlugOperator]
):
    __slots__ = ()

    trailTaperCurve_Position = FloatField()
    trailTaperCurvep = trailTaperCurve_Position

    trailTaperCurve_Value = FloatField()
    trailTaperCurvev = trailTaperCurve_Value


class TrailTaperCurveField(
    CompoundField[TrailTaperCurveAttrOperator, TrailTaperCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrailTaperCurveAttrOperator
    PLUG_CLS = TrailTaperCurvePlugOperator


class BevelCapCurvePlugOperator(
    CompoundPlugOperator["BevelCapCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bevelCapCurve_Position", "bevelCapCurvep"),
        ("bevelCapCurve_Value", "bevelCapCurvev"),
    )

    bevelCapCurve_Position = FloatField()
    bevelCapCurvep = bevelCapCurve_Position

    bevelCapCurve_Value = FloatField()
    bevelCapCurvev = bevelCapCurve_Value


class BevelCapCurveAttrOperator(
    CompoundAttrOperator[BevelCapCurvePlugOperator]
):
    __slots__ = ()

    bevelCapCurve_Position = FloatField()
    bevelCapCurvep = bevelCapCurve_Position

    bevelCapCurve_Value = FloatField()
    bevelCapCurvev = bevelCapCurve_Value


class BevelCapCurveField(
    CompoundField[BevelCapCurveAttrOperator, BevelCapCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BevelCapCurveAttrOperator
    PLUG_CLS = BevelCapCurvePlugOperator


class ConnectionPointPlugOperator(
    Float3CompoundBasePlugOperator["ConnectionPointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("connectionPointX", "conLocx"),
        ("connectionPointY", "conLocy"),
        ("connectionPointZ", "conLocz"),
    )

    connectionPointX = FloatField()
    conLocx = connectionPointX

    connectionPointY = FloatField()
    conLocy = connectionPointY

    connectionPointZ = FloatField()
    conLocz = connectionPointZ


class ConnectionPointAttrOperator(
    Float3CompoundBaseAttrOperator[ConnectionPointPlugOperator]
):
    __slots__ = ()

    connectionPointX = FloatField()
    conLocx = connectionPointX

    connectionPointY = FloatField()
    conLocy = connectionPointY

    connectionPointZ = FloatField()
    conLocz = connectionPointZ


class ConnectionPointField(
    Float3CompoundBaseField[ConnectionPointAttrOperator, ConnectionPointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConnectionPointAttrOperator
    PLUG_CLS = ConnectionPointPlugOperator

    connectionPointX = FloatField()
    conLocx = connectionPointX

    connectionPointY = FloatField()
    conLocy = connectionPointY

    connectionPointZ = FloatField()
    conLocz = connectionPointZ
