# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.dt.matrix import DataMatrixField
from ..std.dt.mesh import DataMeshField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class CurvatureWidth_curvatureWidth_InterpEnumPlugOperator(
    EnumPlugOperator["CurvatureWidth_curvatureWidth_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CurvatureWidth_curvatureWidth_InterpEnumAttrOperator(
    EnumAttrOperator[CurvatureWidth_curvatureWidth_InterpEnumPlugOperator]
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


class CurvatureWidth_curvatureWidth_InterpEnumField(
    EnumField[
        CurvatureWidth_curvatureWidth_InterpEnumAttrOperator,
        CurvatureWidth_curvatureWidth_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CurvatureWidth_curvatureWidth_InterpEnumAttrOperator
    PLUG_CLS = CurvatureWidth_curvatureWidth_InterpEnumPlugOperator


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


class InputSurfacePlugOperator(
    CompoundPlugOperator["InputSurfaceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("surface", "srf"),
        ("inputWorldMatrix", "iwm"),
    )

    surface = DataMeshField()
    srf = surface

    inputWorldMatrix = DataMatrixField()
    iwm = inputWorldMatrix


class InputSurfaceAttrOperator(CompoundAttrOperator[InputSurfacePlugOperator]):
    __slots__ = ()

    surface = DataMeshField()
    srf = surface

    inputWorldMatrix = DataMatrixField()
    iwm = inputWorldMatrix


class InputSurfaceField(
    CompoundField[InputSurfaceAttrOperator, InputSurfacePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputSurfaceAttrOperator
    PLUG_CLS = InputSurfacePlugOperator


class CurvatureWidthPlugOperator(
    CompoundPlugOperator["CurvatureWidthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("curvatureWidth_Position", "cwdp"),
        ("curvatureWidth_FloatValue", "cwdfv"),
        ("curvatureWidth_Interp", "cwdi"),
    )

    curvatureWidth_Position = FloatField(default_value=0.0)
    cwdp = curvatureWidth_Position

    curvatureWidth_FloatValue = FloatField(default_value=0.0)
    cwdfv = curvatureWidth_FloatValue

    curvatureWidth_Interp = CurvatureWidth_curvatureWidth_InterpEnumField(
        default_value=0
    )
    cwdi = curvatureWidth_Interp


class CurvatureWidthAttrOperator(
    CompoundAttrOperator[CurvatureWidthPlugOperator]
):
    __slots__ = ()

    curvatureWidth_Position = FloatField(default_value=0.0)
    cwdp = curvatureWidth_Position

    curvatureWidth_FloatValue = FloatField(default_value=0.0)
    cwdfv = curvatureWidth_FloatValue

    curvatureWidth_Interp = CurvatureWidth_curvatureWidth_InterpEnumField(
        default_value=0
    )
    cwdi = curvatureWidth_Interp


class CurvatureWidthField(
    CompoundField[CurvatureWidthAttrOperator, CurvatureWidthPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurvatureWidthAttrOperator
    PLUG_CLS = CurvatureWidthPlugOperator


class ProfileColorPlugOperator(
    Float3CompoundBasePlugOperator["ProfileColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("profileColorR", "pcr"),
        ("profileColorG", "pcg"),
        ("profileColorB", "pcb"),
    )

    profileColorR = FloatField(default_value=0.0)
    pcr = profileColorR

    profileColorG = FloatField(default_value=0.0)
    pcg = profileColorG

    profileColorB = FloatField(default_value=0.0)
    pcb = profileColorB


class ProfileColorAttrOperator(
    Float3CompoundBaseAttrOperator[ProfileColorPlugOperator]
):
    __slots__ = ()

    profileColorR = FloatField(default_value=0.0)
    pcr = profileColorR

    profileColorG = FloatField(default_value=0.0)
    pcg = profileColorG

    profileColorB = FloatField(default_value=0.0)
    pcb = profileColorB


class ProfileColorField(
    Float3CompoundBaseField[ProfileColorAttrOperator, ProfileColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ProfileColorAttrOperator
    PLUG_CLS = ProfileColorPlugOperator

    profileColorR = FloatField(default_value=0.0)
    pcr = profileColorR

    profileColorG = FloatField(default_value=0.0)
    pcg = profileColorG

    profileColorB = FloatField(default_value=0.0)
    pcb = profileColorB


class CreaseColorPlugOperator(
    Float3CompoundBasePlugOperator["CreaseColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("creaseColorR", "ccr"),
        ("creaseColorG", "ccg"),
        ("creaseColorB", "ccb"),
    )

    creaseColorR = FloatField(default_value=0.0)
    ccr = creaseColorR

    creaseColorG = FloatField(default_value=0.0)
    ccg = creaseColorG

    creaseColorB = FloatField(default_value=0.0)
    ccb = creaseColorB


class CreaseColorAttrOperator(
    Float3CompoundBaseAttrOperator[CreaseColorPlugOperator]
):
    __slots__ = ()

    creaseColorR = FloatField(default_value=0.0)
    ccr = creaseColorR

    creaseColorG = FloatField(default_value=0.0)
    ccg = creaseColorG

    creaseColorB = FloatField(default_value=0.0)
    ccb = creaseColorB


class CreaseColorField(
    Float3CompoundBaseField[CreaseColorAttrOperator, CreaseColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CreaseColorAttrOperator
    PLUG_CLS = CreaseColorPlugOperator

    creaseColorR = FloatField(default_value=0.0)
    ccr = creaseColorR

    creaseColorG = FloatField(default_value=0.0)
    ccg = creaseColorG

    creaseColorB = FloatField(default_value=0.0)
    ccb = creaseColorB


class BorderColorPlugOperator(
    Float3CompoundBasePlugOperator["BorderColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("borderColorR", "bcr"),
        ("borderColorG", "bcg"),
        ("borderColorB", "bcb"),
    )

    borderColorR = FloatField(default_value=0.0)
    bcr = borderColorR

    borderColorG = FloatField(default_value=0.0)
    bcg = borderColorG

    borderColorB = FloatField(default_value=0.0)
    bcb = borderColorB


class BorderColorAttrOperator(
    Float3CompoundBaseAttrOperator[BorderColorPlugOperator]
):
    __slots__ = ()

    borderColorR = FloatField(default_value=0.0)
    bcr = borderColorR

    borderColorG = FloatField(default_value=0.0)
    bcg = borderColorG

    borderColorB = FloatField(default_value=0.0)
    bcb = borderColorB


class BorderColorField(
    Float3CompoundBaseField[BorderColorAttrOperator, BorderColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BorderColorAttrOperator
    PLUG_CLS = BorderColorPlugOperator

    borderColorR = FloatField(default_value=0.0)
    bcr = borderColorR

    borderColorG = FloatField(default_value=0.0)
    bcg = borderColorG

    borderColorB = FloatField(default_value=0.0)
    bcb = borderColorB


class IntersectionColorPlugOperator(
    Float3CompoundBasePlugOperator["IntersectionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("intersectionColorR", "icr"),
        ("intersectionColorG", "icg"),
        ("intersectionColorB", "icb"),
    )

    intersectionColorR = FloatField(default_value=0.0)
    icr = intersectionColorR

    intersectionColorG = FloatField(default_value=0.0)
    icg = intersectionColorG

    intersectionColorB = FloatField(default_value=0.0)
    icb = intersectionColorB


class IntersectionColorAttrOperator(
    Float3CompoundBaseAttrOperator[IntersectionColorPlugOperator]
):
    __slots__ = ()

    intersectionColorR = FloatField(default_value=0.0)
    icr = intersectionColorR

    intersectionColorG = FloatField(default_value=0.0)
    icg = intersectionColorG

    intersectionColorB = FloatField(default_value=0.0)
    icb = intersectionColorB


class IntersectionColorField(
    Float3CompoundBaseField[
        IntersectionColorAttrOperator, IntersectionColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = IntersectionColorAttrOperator
    PLUG_CLS = IntersectionColorPlugOperator

    intersectionColorR = FloatField(default_value=0.0)
    icr = intersectionColorR

    intersectionColorG = FloatField(default_value=0.0)
    icg = intersectionColorG

    intersectionColorB = FloatField(default_value=0.0)
    icb = intersectionColorB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB
