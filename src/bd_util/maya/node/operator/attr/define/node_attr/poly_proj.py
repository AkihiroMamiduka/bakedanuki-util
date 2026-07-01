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


class ProjectionCenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ProjectionCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("projectionCenterX", "pcx"),
        ("projectionCenterY", "pcy"),
        ("projectionCenterZ", "pcz"),
    )

    projectionCenterX = DoubleLinearField()
    pcx = projectionCenterX

    projectionCenterY = DoubleLinearField()
    pcy = projectionCenterY

    projectionCenterZ = DoubleLinearField()
    pcz = projectionCenterZ


class ProjectionCenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ProjectionCenterPlugOperator]
):
    __slots__ = ()

    projectionCenterX = DoubleLinearField()
    pcx = projectionCenterX

    projectionCenterY = DoubleLinearField()
    pcy = projectionCenterY

    projectionCenterZ = DoubleLinearField()
    pcz = projectionCenterZ


class ProjectionCenterField(
    DoubleLinear3CompoundBaseField[ProjectionCenterAttrOperator, ProjectionCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProjectionCenterAttrOperator
    PLUG_CLS = ProjectionCenterPlugOperator

    projectionCenterX = DoubleLinearField()
    pcx = projectionCenterX

    projectionCenterY = DoubleLinearField()
    pcy = projectionCenterY

    projectionCenterZ = DoubleLinearField()
    pcz = projectionCenterZ


class ImageCenterPlugOperator(
    DoubleLinear2CompoundBasePlugOperator["ImageCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("imageCenterX", "icx"),
        ("imageCenterY", "icy"),
    )

    imageCenterX = DoubleLinearField()
    icx = imageCenterX

    imageCenterY = DoubleLinearField()
    icy = imageCenterY


class ImageCenterAttrOperator(
    DoubleLinear2CompoundBaseAttrOperator[ImageCenterPlugOperator]
):
    __slots__ = ()

    imageCenterX = DoubleLinearField()
    icx = imageCenterX

    imageCenterY = DoubleLinearField()
    icy = imageCenterY


class ImageCenterField(
    DoubleLinear2CompoundBaseField[ImageCenterAttrOperator, ImageCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageCenterAttrOperator
    PLUG_CLS = ImageCenterPlugOperator

    imageCenterX = DoubleLinearField()
    icx = imageCenterX

    imageCenterY = DoubleLinearField()
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

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ


class RotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ


class RotateField(
    DoubleAngle3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ


class ProjectionScalePlugOperator(
    DoubleLinear2CompoundBasePlugOperator["ProjectionScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("projectionScaleU", "psu"),
        ("projectionScaleV", "psv"),
    )

    projectionScaleU = DoubleLinearField()
    psu = projectionScaleU

    projectionScaleV = DoubleLinearField()
    psv = projectionScaleV


class ProjectionScaleAttrOperator(
    DoubleLinear2CompoundBaseAttrOperator[ProjectionScalePlugOperator]
):
    __slots__ = ()

    projectionScaleU = DoubleLinearField()
    psu = projectionScaleU

    projectionScaleV = DoubleLinearField()
    psv = projectionScaleV


class ProjectionScaleField(
    DoubleLinear2CompoundBaseField[ProjectionScaleAttrOperator, ProjectionScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProjectionScaleAttrOperator
    PLUG_CLS = ProjectionScalePlugOperator

    projectionScaleU = DoubleLinearField()
    psu = projectionScaleU

    projectionScaleV = DoubleLinearField()
    psv = projectionScaleV


class ImageScalePlugOperator(
    DoubleLinear2CompoundBasePlugOperator["ImageScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("imageScaleU", "isu"),
        ("imageScaleV", "isv"),
    )

    imageScaleU = DoubleLinearField()
    isu = imageScaleU

    imageScaleV = DoubleLinearField()
    isv = imageScaleV


class ImageScaleAttrOperator(
    DoubleLinear2CompoundBaseAttrOperator[ImageScalePlugOperator]
):
    __slots__ = ()

    imageScaleU = DoubleLinearField()
    isu = imageScaleU

    imageScaleV = DoubleLinearField()
    isv = imageScaleV


class ImageScaleField(
    DoubleLinear2CompoundBaseField[ImageScaleAttrOperator, ImageScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageScaleAttrOperator
    PLUG_CLS = ImageScalePlugOperator

    imageScaleU = DoubleLinearField()
    isu = imageScaleU

    imageScaleV = DoubleLinearField()
    isv = imageScaleV
