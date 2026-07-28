# coding: utf-8

from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
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

    cutPlaneCenterX = DoubleLinearField(default_value=0.0)
    pcx = cutPlaneCenterX

    cutPlaneCenterY = DoubleLinearField(default_value=0.0)
    pcy = cutPlaneCenterY

    cutPlaneCenterZ = DoubleLinearField(default_value=0.0)
    pcz = cutPlaneCenterZ


class CutPlaneCenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CutPlaneCenterPlugOperator]
):
    __slots__ = ()

    cutPlaneCenterX = DoubleLinearField(default_value=0.0)
    pcx = cutPlaneCenterX

    cutPlaneCenterY = DoubleLinearField(default_value=0.0)
    pcy = cutPlaneCenterY

    cutPlaneCenterZ = DoubleLinearField(default_value=0.0)
    pcz = cutPlaneCenterZ


class CutPlaneCenterField(
    DoubleLinear3CompoundBaseField[
        CutPlaneCenterAttrOperator, CutPlaneCenterPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CutPlaneCenterAttrOperator
    PLUG_CLS = CutPlaneCenterPlugOperator

    cutPlaneCenterX = DoubleLinearField(default_value=0.0)
    pcx = cutPlaneCenterX

    cutPlaneCenterY = DoubleLinearField(default_value=0.0)
    pcy = cutPlaneCenterY

    cutPlaneCenterZ = DoubleLinearField(default_value=0.0)
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

    cutPlaneRotateX = DoubleAngleField(default_value=0.0)
    rx = cutPlaneRotateX

    cutPlaneRotateY = DoubleAngleField(default_value=0.0)
    ry = cutPlaneRotateY

    cutPlaneRotateZ = DoubleAngleField(default_value=0.0)
    rz = cutPlaneRotateZ


class CutPlaneRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[CutPlaneRotatePlugOperator]
):
    __slots__ = ()

    cutPlaneRotateX = DoubleAngleField(default_value=0.0)
    rx = cutPlaneRotateX

    cutPlaneRotateY = DoubleAngleField(default_value=0.0)
    ry = cutPlaneRotateY

    cutPlaneRotateZ = DoubleAngleField(default_value=0.0)
    rz = cutPlaneRotateZ


class CutPlaneRotateField(
    DoubleAngle3CompoundBaseField[
        CutPlaneRotateAttrOperator, CutPlaneRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CutPlaneRotateAttrOperator
    PLUG_CLS = CutPlaneRotatePlugOperator

    cutPlaneRotateX = DoubleAngleField(default_value=0.0)
    rx = cutPlaneRotateX

    cutPlaneRotateY = DoubleAngleField(default_value=0.0)
    ry = cutPlaneRotateY

    cutPlaneRotateZ = DoubleAngleField(default_value=0.0)
    rz = cutPlaneRotateZ


class CutPlaneSizePlugOperator(
    DoubleLinear2CompoundBasePlugOperator["CutPlaneSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cutPlaneWidth", "pw"),
        ("cutPlaneHeight", "ph"),
    )

    cutPlaneWidth = DoubleLinearField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    pw = cutPlaneWidth

    cutPlaneHeight = DoubleLinearField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    ph = cutPlaneHeight


class CutPlaneSizeAttrOperator(
    DoubleLinear2CompoundBaseAttrOperator[CutPlaneSizePlugOperator]
):
    __slots__ = ()

    cutPlaneWidth = DoubleLinearField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    pw = cutPlaneWidth

    cutPlaneHeight = DoubleLinearField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    ph = cutPlaneHeight


class CutPlaneSizeField(
    DoubleLinear2CompoundBaseField[
        CutPlaneSizeAttrOperator, CutPlaneSizePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CutPlaneSizeAttrOperator
    PLUG_CLS = CutPlaneSizePlugOperator

    cutPlaneWidth = DoubleLinearField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
    pw = cutPlaneWidth

    cutPlaneHeight = DoubleLinearField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )
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

    extractOffsetX = DoubleLinearField(default_value=0.5)
    eox = extractOffsetX

    extractOffsetY = DoubleLinearField(default_value=0.5)
    eoy = extractOffsetY

    extractOffsetZ = DoubleLinearField(default_value=0.5)
    eoz = extractOffsetZ


class ExtractOffsetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ExtractOffsetPlugOperator]
):
    __slots__ = ()

    extractOffsetX = DoubleLinearField(default_value=0.5)
    eox = extractOffsetX

    extractOffsetY = DoubleLinearField(default_value=0.5)
    eoy = extractOffsetY

    extractOffsetZ = DoubleLinearField(default_value=0.5)
    eoz = extractOffsetZ


class ExtractOffsetField(
    DoubleLinear3CompoundBaseField[
        ExtractOffsetAttrOperator, ExtractOffsetPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ExtractOffsetAttrOperator
    PLUG_CLS = ExtractOffsetPlugOperator

    extractOffsetX = DoubleLinearField(default_value=0.5)
    eox = extractOffsetX

    extractOffsetY = DoubleLinearField(default_value=0.5)
    eoy = extractOffsetY

    extractOffsetZ = DoubleLinearField(default_value=0.5)
    eoz = extractOffsetZ
