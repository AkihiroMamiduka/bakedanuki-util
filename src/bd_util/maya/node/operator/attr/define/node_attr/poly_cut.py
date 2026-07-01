# coding: utf-8

from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double2._base import (
    DoubleLinear2CompoundBaseAttrOperator,
    DoubleLinear2CompoundBasePlugOperator,
    DoubleLinear2CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class CutPlaneCenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CutPlaneCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cutPlaneCenterX", "pcx"),
        ("cutPlaneCenterY", "pcy"),
        ("cutPlaneCenterZ", "pcz"),
    )

    cutPlaneCenterX = DoubleLinearField()
    pcx = cutPlaneCenterX

    cutPlaneCenterY = DoubleLinearField()
    pcy = cutPlaneCenterY

    cutPlaneCenterZ = DoubleLinearField()
    pcz = cutPlaneCenterZ


class CutPlaneCenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CutPlaneCenterPlugOperator]
):
    __slots__ = ()

    cutPlaneCenterX = DoubleLinearField()
    pcx = cutPlaneCenterX

    cutPlaneCenterY = DoubleLinearField()
    pcy = cutPlaneCenterY

    cutPlaneCenterZ = DoubleLinearField()
    pcz = cutPlaneCenterZ


class CutPlaneCenterField(
    DoubleLinear3CompoundBaseField[CutPlaneCenterAttrOperator, CutPlaneCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CutPlaneCenterAttrOperator
    PLUG_CLS = CutPlaneCenterPlugOperator

    cutPlaneCenterX = DoubleLinearField()
    pcx = cutPlaneCenterX

    cutPlaneCenterY = DoubleLinearField()
    pcy = cutPlaneCenterY

    cutPlaneCenterZ = DoubleLinearField()
    pcz = cutPlaneCenterZ


class CutPlaneRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["CutPlaneRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cutPlaneRotateX", "rx"),
        ("cutPlaneRotateY", "ry"),
        ("cutPlaneRotateZ", "rz"),
    )

    cutPlaneRotateX = DoubleAngleField()
    rx = cutPlaneRotateX

    cutPlaneRotateY = DoubleAngleField()
    ry = cutPlaneRotateY

    cutPlaneRotateZ = DoubleAngleField()
    rz = cutPlaneRotateZ


class CutPlaneRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[CutPlaneRotatePlugOperator]
):
    __slots__ = ()

    cutPlaneRotateX = DoubleAngleField()
    rx = cutPlaneRotateX

    cutPlaneRotateY = DoubleAngleField()
    ry = cutPlaneRotateY

    cutPlaneRotateZ = DoubleAngleField()
    rz = cutPlaneRotateZ


class CutPlaneRotateField(
    DoubleAngle3CompoundBaseField[CutPlaneRotateAttrOperator, CutPlaneRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CutPlaneRotateAttrOperator
    PLUG_CLS = CutPlaneRotatePlugOperator

    cutPlaneRotateX = DoubleAngleField()
    rx = cutPlaneRotateX

    cutPlaneRotateY = DoubleAngleField()
    ry = cutPlaneRotateY

    cutPlaneRotateZ = DoubleAngleField()
    rz = cutPlaneRotateZ


class CutPlaneSizePlugOperator(
    DoubleLinear2CompoundBasePlugOperator["CutPlaneSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cutPlaneWidth", "pw"),
        ("cutPlaneHeight", "ph"),
    )

    cutPlaneWidth = DoubleLinearField()
    pw = cutPlaneWidth

    cutPlaneHeight = DoubleLinearField()
    ph = cutPlaneHeight


class CutPlaneSizeAttrOperator(
    DoubleLinear2CompoundBaseAttrOperator[CutPlaneSizePlugOperator]
):
    __slots__ = ()

    cutPlaneWidth = DoubleLinearField()
    pw = cutPlaneWidth

    cutPlaneHeight = DoubleLinearField()
    ph = cutPlaneHeight


class CutPlaneSizeField(
    DoubleLinear2CompoundBaseField[CutPlaneSizeAttrOperator, CutPlaneSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CutPlaneSizeAttrOperator
    PLUG_CLS = CutPlaneSizePlugOperator

    cutPlaneWidth = DoubleLinearField()
    pw = cutPlaneWidth

    cutPlaneHeight = DoubleLinearField()
    ph = cutPlaneHeight


class ExtractOffsetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ExtractOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("extractOffsetX", "eox"),
        ("extractOffsetY", "eoy"),
        ("extractOffsetZ", "eoz"),
    )

    extractOffsetX = DoubleLinearField()
    eox = extractOffsetX

    extractOffsetY = DoubleLinearField()
    eoy = extractOffsetY

    extractOffsetZ = DoubleLinearField()
    eoz = extractOffsetZ


class ExtractOffsetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ExtractOffsetPlugOperator]
):
    __slots__ = ()

    extractOffsetX = DoubleLinearField()
    eox = extractOffsetX

    extractOffsetY = DoubleLinearField()
    eoy = extractOffsetY

    extractOffsetZ = DoubleLinearField()
    eoz = extractOffsetZ


class ExtractOffsetField(
    DoubleLinear3CompoundBaseField[ExtractOffsetAttrOperator, ExtractOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtractOffsetAttrOperator
    PLUG_CLS = ExtractOffsetPlugOperator

    extractOffsetX = DoubleLinearField()
    eox = extractOffsetX

    extractOffsetY = DoubleLinearField()
    eoy = extractOffsetY

    extractOffsetZ = DoubleLinearField()
    eoz = extractOffsetZ
