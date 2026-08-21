# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class PressureScale_pressureScale_InterpEnumPlugOperator(
    EnumPlugOperator["PressureScale_pressureScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class PressureScale_pressureScale_InterpEnumAttrOperator(
    EnumAttrOperator[PressureScale_pressureScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class PressureScale_pressureScale_InterpEnumField(
    EnumField[
        PressureScale_pressureScale_InterpEnumAttrOperator,
        PressureScale_pressureScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = PressureScale_pressureScale_InterpEnumAttrOperator
    PLUG_CLS = PressureScale_pressureScale_InterpEnumPlugOperator


class CameraPointPlugOperator(
    Double3CompoundBasePlugOperator["CameraPointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cameraPointX", "cpx"),
        ("cameraPointY", "cpy"),
        ("cameraPointZ", "cpz"),
    )

    cameraPointX = DoubleField(default_value=0.0)
    cpx = cameraPointX

    cameraPointY = DoubleField(default_value=0.0)
    cpy = cameraPointY

    cameraPointZ = DoubleField(default_value=0.0)
    cpz = cameraPointZ


class CameraPointAttrOperator(
    Double3CompoundBaseAttrOperator[CameraPointPlugOperator]
):
    __slots__ = ()

    cameraPointX = DoubleField(default_value=0.0)
    cpx = cameraPointX

    cameraPointY = DoubleField(default_value=0.0)
    cpy = cameraPointY

    cameraPointZ = DoubleField(default_value=0.0)
    cpz = cameraPointZ


class CameraPointField(
    Double3CompoundBaseField[CameraPointAttrOperator, CameraPointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CameraPointAttrOperator
    PLUG_CLS = CameraPointPlugOperator

    cameraPointX = DoubleField(default_value=0.0)
    cpx = cameraPointX

    cameraPointY = DoubleField(default_value=0.0)
    cpy = cameraPointY

    cameraPointZ = DoubleField(default_value=0.0)
    cpz = cameraPointZ


class NormalPlugOperator(
    Double3CompoundBasePlugOperator["NormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalX", "nmx"),
        ("normalY", "nmy"),
        ("normalZ", "nmz"),
    )

    normalX = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    nmx = normalX

    normalY = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    nmy = normalY

    normalZ = DoubleField(
        default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    nmz = normalZ


class NormalAttrOperator(Double3CompoundBaseAttrOperator[NormalPlugOperator]):
    __slots__ = ()

    normalX = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    nmx = normalX

    normalY = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    nmy = normalY

    normalZ = DoubleField(
        default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    nmz = normalZ


class NormalField(
    Double3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normalX = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    nmx = normalX

    normalY = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    nmy = normalY

    normalZ = DoubleField(
        default_value=1.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    nmz = normalZ


class PathCurvePlugOperator(CompoundPlugOperator["PathCurveAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("curve", "crv"),
        ("samples", "smp"),
        ("opposite", "opp"),
    )

    curve = GenericField()
    crv = curve

    samples = LongField(default_value=0)
    smp = samples

    opposite = BoolField(default_value=False)
    opp = opposite


class PathCurveAttrOperator(CompoundAttrOperator[PathCurvePlugOperator]):
    __slots__ = ()

    curve = GenericField()
    crv = curve

    samples = LongField(default_value=0)
    smp = samples

    opposite = BoolField(default_value=False)
    opp = opposite


class PathCurveField(
    CompoundField[PathCurveAttrOperator, PathCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PathCurveAttrOperator
    PLUG_CLS = PathCurvePlugOperator


class OutPointPlugOperator(
    Double3CompoundBasePlugOperator["OutPointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outPointX", "ox"),
        ("outPointY", "oy"),
        ("outPointZ", "oz"),
    )

    outPointX = DoubleField(default_value=0.0)
    ox = outPointX

    outPointY = DoubleField(default_value=0.0)
    oy = outPointY

    outPointZ = DoubleField(default_value=0.0)
    oz = outPointZ


class OutPointAttrOperator(
    Double3CompoundBaseAttrOperator[OutPointPlugOperator]
):
    __slots__ = ()

    outPointX = DoubleField(default_value=0.0)
    ox = outPointX

    outPointY = DoubleField(default_value=0.0)
    oy = outPointY

    outPointZ = DoubleField(default_value=0.0)
    oz = outPointZ


class OutPointField(
    Double3CompoundBaseField[OutPointAttrOperator, OutPointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutPointAttrOperator
    PLUG_CLS = OutPointPlugOperator


class OutNormalPlugOperator(
    Double3CompoundBasePlugOperator["OutNormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outNormalX", "onx"),
        ("outNormalY", "ony"),
        ("outNormalZ", "onz"),
    )

    outNormalX = DoubleField(default_value=0.0, writable=False)
    onx = outNormalX

    outNormalY = DoubleField(default_value=0.0, writable=False)
    ony = outNormalY

    outNormalZ = DoubleField(default_value=0.0, writable=False)
    onz = outNormalZ


class OutNormalAttrOperator(
    Double3CompoundBaseAttrOperator[OutNormalPlugOperator]
):
    __slots__ = ()

    outNormalX = DoubleField(default_value=0.0, writable=False)
    onx = outNormalX

    outNormalY = DoubleField(default_value=0.0, writable=False)
    ony = outNormalY

    outNormalZ = DoubleField(default_value=0.0, writable=False)
    onz = outNormalZ


class OutNormalField(
    Double3CompoundBaseField[OutNormalAttrOperator, OutNormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutNormalAttrOperator
    PLUG_CLS = OutNormalPlugOperator


class PressureScalePlugOperator(
    CompoundPlugOperator["PressureScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pressureScale_Position", "pscp"),
        ("pressureScale_FloatValue", "pscfv"),
        ("pressureScale_Interp", "psci"),
    )

    pressureScale_Position = FloatField(default_value=0.0)
    pscp = pressureScale_Position

    pressureScale_FloatValue = FloatField(default_value=0.0)
    pscfv = pressureScale_FloatValue

    pressureScale_Interp = PressureScale_pressureScale_InterpEnumField(
        default_value=0
    )
    psci = pressureScale_Interp


class PressureScaleAttrOperator(
    CompoundAttrOperator[PressureScalePlugOperator]
):
    __slots__ = ()

    pressureScale_Position = FloatField(default_value=0.0)
    pscp = pressureScale_Position

    pressureScale_FloatValue = FloatField(default_value=0.0)
    pscfv = pressureScale_FloatValue

    pressureScale_Interp = PressureScale_pressureScale_InterpEnumField(
        default_value=0
    )
    psci = pressureScale_Interp


class PressureScaleField(
    CompoundField[PressureScaleAttrOperator, PressureScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PressureScaleAttrOperator
    PLUG_CLS = PressureScalePlugOperator
