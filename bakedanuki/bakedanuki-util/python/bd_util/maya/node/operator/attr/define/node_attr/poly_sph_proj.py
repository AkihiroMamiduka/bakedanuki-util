# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)
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


class ProjectionCenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ProjectionCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("projectionCenterX", "pcx"),
        ("projectionCenterY", "pcy"),
        ("projectionCenterZ", "pcz"),
    )

    projectionCenterX = DoubleLinearField(default_value=0.0)
    pcx = projectionCenterX

    projectionCenterY = DoubleLinearField(default_value=0.0)
    pcy = projectionCenterY

    projectionCenterZ = DoubleLinearField(default_value=0.0)
    pcz = projectionCenterZ


class ProjectionCenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ProjectionCenterPlugOperator]
):
    __slots__ = ()

    projectionCenterX = DoubleLinearField(default_value=0.0)
    pcx = projectionCenterX

    projectionCenterY = DoubleLinearField(default_value=0.0)
    pcy = projectionCenterY

    projectionCenterZ = DoubleLinearField(default_value=0.0)
    pcz = projectionCenterZ


class ProjectionCenterField(
    DoubleLinear3CompoundBaseField[ProjectionCenterAttrOperator, ProjectionCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProjectionCenterAttrOperator
    PLUG_CLS = ProjectionCenterPlugOperator

    projectionCenterX = DoubleLinearField(default_value=0.0)
    pcx = projectionCenterX

    projectionCenterY = DoubleLinearField(default_value=0.0)
    pcy = projectionCenterY

    projectionCenterZ = DoubleLinearField(default_value=0.0)
    pcz = projectionCenterZ


class ImageCenterPlugOperator(
    Double2CompoundBasePlugOperator["ImageCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("imageCenterX", "icx"),
        ("imageCenterY", "icy"),
    )

    imageCenterX = DoubleField(default_value=0.5)
    icx = imageCenterX

    imageCenterY = DoubleField(default_value=0.5)
    icy = imageCenterY


class ImageCenterAttrOperator(
    Double2CompoundBaseAttrOperator[ImageCenterPlugOperator]
):
    __slots__ = ()

    imageCenterX = DoubleField(default_value=0.5)
    icx = imageCenterX

    imageCenterY = DoubleField(default_value=0.5)
    icy = imageCenterY


class ImageCenterField(
    Double2CompoundBaseField[ImageCenterAttrOperator, ImageCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageCenterAttrOperator
    PLUG_CLS = ImageCenterPlugOperator

    imageCenterX = DoubleField(default_value=0.5)
    icx = imageCenterX

    imageCenterY = DoubleField(default_value=0.5)
    icy = imageCenterY


class RotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateX", "rx"),
        ("rotateY", "ry"),
        ("rotateZ", "rz"),
    )

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class RotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class RotateField(
    DoubleAngle3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class ProjectionScalePlugOperator(
    DoubleLinear2CompoundBasePlugOperator["ProjectionScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("projectionHorizontalSweep", "phs"),
        ("projectionVerticalSweep", "pvs"),
    )

    projectionHorizontalSweep = DoubleLinearField(default_value=180.0, min_value=0.0, max_value=360.0)
    phs = projectionHorizontalSweep

    projectionVerticalSweep = DoubleLinearField(default_value=90.0, min_value=0.0, max_value=180.0)
    pvs = projectionVerticalSweep


class ProjectionScaleAttrOperator(
    DoubleLinear2CompoundBaseAttrOperator[ProjectionScalePlugOperator]
):
    __slots__ = ()

    projectionHorizontalSweep = DoubleLinearField(default_value=180.0, min_value=0.0, max_value=360.0)
    phs = projectionHorizontalSweep

    projectionVerticalSweep = DoubleLinearField(default_value=90.0, min_value=0.0, max_value=180.0)
    pvs = projectionVerticalSweep


class ProjectionScaleField(
    DoubleLinear2CompoundBaseField[ProjectionScaleAttrOperator, ProjectionScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProjectionScaleAttrOperator
    PLUG_CLS = ProjectionScalePlugOperator

    projectionHorizontalSweep = DoubleLinearField(default_value=180.0, min_value=0.0, max_value=360.0)
    phs = projectionHorizontalSweep

    projectionVerticalSweep = DoubleLinearField(default_value=90.0, min_value=0.0, max_value=180.0)
    pvs = projectionVerticalSweep


class ImageScalePlugOperator(
    Double2CompoundBasePlugOperator["ImageScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("imageScaleU", "isu"),
        ("imageScaleV", "isv"),
    )

    imageScaleU = DoubleField(default_value=1.0)
    isu = imageScaleU

    imageScaleV = DoubleField(default_value=1.0)
    isv = imageScaleV


class ImageScaleAttrOperator(
    Double2CompoundBaseAttrOperator[ImageScalePlugOperator]
):
    __slots__ = ()

    imageScaleU = DoubleField(default_value=1.0)
    isu = imageScaleU

    imageScaleV = DoubleField(default_value=1.0)
    isv = imageScaleV


class ImageScaleField(
    Double2CompoundBaseField[ImageScaleAttrOperator, ImageScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageScaleAttrOperator
    PLUG_CLS = ImageScalePlugOperator

    imageScaleU = DoubleField(default_value=1.0)
    isu = imageScaleU

    imageScaleV = DoubleField(default_value=1.0)
    isv = imageScaleV
