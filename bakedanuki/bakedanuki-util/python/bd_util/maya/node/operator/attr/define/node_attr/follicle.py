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
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class StiffnessScale_stiffnessScale_InterpEnumPlugOperator(
    EnumPlugOperator["StiffnessScale_stiffnessScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class StiffnessScale_stiffnessScale_InterpEnumAttrOperator(
    EnumAttrOperator[StiffnessScale_stiffnessScale_InterpEnumPlugOperator]
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


class StiffnessScale_stiffnessScale_InterpEnumField(
    EnumField[
        StiffnessScale_stiffnessScale_InterpEnumAttrOperator,
        StiffnessScale_stiffnessScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = StiffnessScale_stiffnessScale_InterpEnumAttrOperator
    PLUG_CLS = StiffnessScale_stiffnessScale_InterpEnumPlugOperator


class ClumpWidthScale_clumpWidthScale_InterpEnumPlugOperator(
    EnumPlugOperator["ClumpWidthScale_clumpWidthScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ClumpWidthScale_clumpWidthScale_InterpEnumAttrOperator(
    EnumAttrOperator[ClumpWidthScale_clumpWidthScale_InterpEnumPlugOperator]
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


class ClumpWidthScale_clumpWidthScale_InterpEnumField(
    EnumField[
        ClumpWidthScale_clumpWidthScale_InterpEnumAttrOperator,
        ClumpWidthScale_clumpWidthScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ClumpWidthScale_clumpWidthScale_InterpEnumAttrOperator
    PLUG_CLS = ClumpWidthScale_clumpWidthScale_InterpEnumPlugOperator


class AttractionScale_attractionScale_InterpEnumPlugOperator(
    EnumPlugOperator["AttractionScale_attractionScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class AttractionScale_attractionScale_InterpEnumAttrOperator(
    EnumAttrOperator[AttractionScale_attractionScale_InterpEnumPlugOperator]
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


class AttractionScale_attractionScale_InterpEnumField(
    EnumField[
        AttractionScale_attractionScale_InterpEnumAttrOperator,
        AttractionScale_attractionScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = AttractionScale_attractionScale_InterpEnumAttrOperator
    PLUG_CLS = AttractionScale_attractionScale_InterpEnumPlugOperator


class StiffnessScalePlugOperator(
    CompoundPlugOperator["StiffnessScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("stiffnessScale_Position", "stsp"),
        ("stiffnessScale_FloatValue", "stsfv"),
        ("stiffnessScale_Interp", "stsi"),
    )

    stiffnessScale_Position = FloatField(default_value=0.0)
    stsp = stiffnessScale_Position

    stiffnessScale_FloatValue = FloatField(default_value=0.0)
    stsfv = stiffnessScale_FloatValue

    stiffnessScale_Interp = StiffnessScale_stiffnessScale_InterpEnumField(
        default_value=0
    )
    stsi = stiffnessScale_Interp


class StiffnessScaleAttrOperator(
    CompoundAttrOperator[StiffnessScalePlugOperator]
):
    __slots__ = ()

    stiffnessScale_Position = FloatField(default_value=0.0)
    stsp = stiffnessScale_Position

    stiffnessScale_FloatValue = FloatField(default_value=0.0)
    stsfv = stiffnessScale_FloatValue

    stiffnessScale_Interp = StiffnessScale_stiffnessScale_InterpEnumField(
        default_value=0
    )
    stsi = stiffnessScale_Interp


class StiffnessScaleField(
    CompoundField[StiffnessScaleAttrOperator, StiffnessScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StiffnessScaleAttrOperator
    PLUG_CLS = StiffnessScalePlugOperator


class ClumpWidthScalePlugOperator(
    CompoundPlugOperator["ClumpWidthScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clumpWidthScale_Position", "cwsp"),
        ("clumpWidthScale_FloatValue", "cwsfv"),
        ("clumpWidthScale_Interp", "cwsi"),
    )

    clumpWidthScale_Position = FloatField(default_value=0.0)
    cwsp = clumpWidthScale_Position

    clumpWidthScale_FloatValue = FloatField(default_value=0.0)
    cwsfv = clumpWidthScale_FloatValue

    clumpWidthScale_Interp = ClumpWidthScale_clumpWidthScale_InterpEnumField(
        default_value=0
    )
    cwsi = clumpWidthScale_Interp


class ClumpWidthScaleAttrOperator(
    CompoundAttrOperator[ClumpWidthScalePlugOperator]
):
    __slots__ = ()

    clumpWidthScale_Position = FloatField(default_value=0.0)
    cwsp = clumpWidthScale_Position

    clumpWidthScale_FloatValue = FloatField(default_value=0.0)
    cwsfv = clumpWidthScale_FloatValue

    clumpWidthScale_Interp = ClumpWidthScale_clumpWidthScale_InterpEnumField(
        default_value=0
    )
    cwsi = clumpWidthScale_Interp


class ClumpWidthScaleField(
    CompoundField[ClumpWidthScaleAttrOperator, ClumpWidthScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpWidthScaleAttrOperator
    PLUG_CLS = ClumpWidthScalePlugOperator


class AttractionScalePlugOperator(
    CompoundPlugOperator["AttractionScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attractionScale_Position", "atsp"),
        ("attractionScale_FloatValue", "atsfv"),
        ("attractionScale_Interp", "atsi"),
    )

    attractionScale_Position = FloatField(default_value=0.0)
    atsp = attractionScale_Position

    attractionScale_FloatValue = FloatField(default_value=0.0)
    atsfv = attractionScale_FloatValue

    attractionScale_Interp = AttractionScale_attractionScale_InterpEnumField(
        default_value=0
    )
    atsi = attractionScale_Interp


class AttractionScaleAttrOperator(
    CompoundAttrOperator[AttractionScalePlugOperator]
):
    __slots__ = ()

    attractionScale_Position = FloatField(default_value=0.0)
    atsp = attractionScale_Position

    attractionScale_FloatValue = FloatField(default_value=0.0)
    atsfv = attractionScale_FloatValue

    attractionScale_Interp = AttractionScale_attractionScale_InterpEnumField(
        default_value=0
    )
    atsi = attractionScale_Interp


class AttractionScaleField(
    CompoundField[AttractionScaleAttrOperator, AttractionScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttractionScaleAttrOperator
    PLUG_CLS = AttractionScalePlugOperator


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField(default_value=0.0)
    cr = colorR

    colorG = FloatField(default_value=0.0)
    cg = colorG

    colorB = FloatField(default_value=0.0)
    cb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.0)
    cr = colorR

    colorG = FloatField(default_value=0.0)
    cg = colorG

    colorB = FloatField(default_value=0.0)
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=0.0)
    cr = colorR

    colorG = FloatField(default_value=0.0)
    cg = colorG

    colorB = FloatField(default_value=0.0)
    cb = colorB


class OutTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTranslateX", "otx"),
        ("outTranslateY", "oty"),
        ("outTranslateZ", "otz"),
    )

    outTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outTranslateX

    outTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outTranslateY

    outTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outTranslateZ


class OutTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutTranslatePlugOperator]
):
    __slots__ = ()

    outTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outTranslateX

    outTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outTranslateY

    outTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outTranslateZ


class OutTranslateField(
    DoubleLinear3CompoundBaseField[
        OutTranslateAttrOperator, OutTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTranslateAttrOperator
    PLUG_CLS = OutTranslatePlugOperator

    outTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outTranslateX

    outTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outTranslateY

    outTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outTranslateZ


class OutRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OutRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outRotateX", "orx"),
        ("outRotateY", "ory"),
        ("outRotateZ", "orz"),
    )

    outRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outRotateX

    outRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outRotateY

    outRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outRotateZ


class OutRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutRotatePlugOperator]
):
    __slots__ = ()

    outRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outRotateX

    outRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outRotateY

    outRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outRotateZ


class OutRotateField(
    DoubleAngle3CompoundBaseField[OutRotateAttrOperator, OutRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutRotateAttrOperator
    PLUG_CLS = OutRotatePlugOperator

    outRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outRotateX

    outRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outRotateY

    outRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outRotateZ


class OutTangentPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutTangentAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTangentX", "otnx"),
        ("outTangentY", "otny"),
        ("outTangentZ", "otnz"),
    )

    outTangentX = DoubleLinearField(default_value=1.0, writable=False)
    otnx = outTangentX

    outTangentY = DoubleLinearField(default_value=0.0, writable=False)
    otny = outTangentY

    outTangentZ = DoubleLinearField(default_value=0.0, writable=False)
    otnz = outTangentZ


class OutTangentAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutTangentPlugOperator]
):
    __slots__ = ()

    outTangentX = DoubleLinearField(default_value=1.0, writable=False)
    otnx = outTangentX

    outTangentY = DoubleLinearField(default_value=0.0, writable=False)
    otny = outTangentY

    outTangentZ = DoubleLinearField(default_value=0.0, writable=False)
    otnz = outTangentZ


class OutTangentField(
    DoubleLinear3CompoundBaseField[
        OutTangentAttrOperator, OutTangentPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTangentAttrOperator
    PLUG_CLS = OutTangentPlugOperator

    outTangentX = DoubleLinearField(default_value=1.0, writable=False)
    otnx = outTangentX

    outTangentY = DoubleLinearField(default_value=0.0, writable=False)
    otny = outTangentY

    outTangentZ = DoubleLinearField(default_value=0.0, writable=False)
    otnz = outTangentZ


class OutNormalPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutNormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outNormalX", "onx"),
        ("outNormalY", "ony"),
        ("outNormalZ", "onz"),
    )

    outNormalX = DoubleLinearField(default_value=0.0, writable=False)
    onx = outNormalX

    outNormalY = DoubleLinearField(default_value=0.0, writable=False)
    ony = outNormalY

    outNormalZ = DoubleLinearField(default_value=1.0, writable=False)
    onz = outNormalZ


class OutNormalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutNormalPlugOperator]
):
    __slots__ = ()

    outNormalX = DoubleLinearField(default_value=0.0, writable=False)
    onx = outNormalX

    outNormalY = DoubleLinearField(default_value=0.0, writable=False)
    ony = outNormalY

    outNormalZ = DoubleLinearField(default_value=1.0, writable=False)
    onz = outNormalZ


class OutNormalField(
    DoubleLinear3CompoundBaseField[
        OutNormalAttrOperator, OutNormalPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutNormalAttrOperator
    PLUG_CLS = OutNormalPlugOperator

    outNormalX = DoubleLinearField(default_value=0.0, writable=False)
    onx = outNormalX

    outNormalY = DoubleLinearField(default_value=0.0, writable=False)
    ony = outNormalY

    outNormalZ = DoubleLinearField(default_value=1.0, writable=False)
    onz = outNormalZ
