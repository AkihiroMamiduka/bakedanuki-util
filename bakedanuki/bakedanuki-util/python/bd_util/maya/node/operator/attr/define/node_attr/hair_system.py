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
from ..std.at.scalar.unit.time import TimeField
from ..std.at.typed import TypedField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
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


class ClumpCurl_clumpCurl_InterpEnumPlugOperator(
    EnumPlugOperator["ClumpCurl_clumpCurl_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ClumpCurl_clumpCurl_InterpEnumAttrOperator(
    EnumAttrOperator[ClumpCurl_clumpCurl_InterpEnumPlugOperator]
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


class ClumpCurl_clumpCurl_InterpEnumField(
    EnumField[
        ClumpCurl_clumpCurl_InterpEnumAttrOperator,
        ClumpCurl_clumpCurl_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ClumpCurl_clumpCurl_InterpEnumAttrOperator
    PLUG_CLS = ClumpCurl_clumpCurl_InterpEnumPlugOperator


class ClumpFlatness_clumpFlatness_InterpEnumPlugOperator(
    EnumPlugOperator["ClumpFlatness_clumpFlatness_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ClumpFlatness_clumpFlatness_InterpEnumAttrOperator(
    EnumAttrOperator[ClumpFlatness_clumpFlatness_InterpEnumPlugOperator]
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


class ClumpFlatness_clumpFlatness_InterpEnumField(
    EnumField[
        ClumpFlatness_clumpFlatness_InterpEnumAttrOperator,
        ClumpFlatness_clumpFlatness_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ClumpFlatness_clumpFlatness_InterpEnumAttrOperator
    PLUG_CLS = ClumpFlatness_clumpFlatness_InterpEnumPlugOperator


class HairWidthScale_hairWidthScale_InterpEnumPlugOperator(
    EnumPlugOperator["HairWidthScale_hairWidthScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class HairWidthScale_hairWidthScale_InterpEnumAttrOperator(
    EnumAttrOperator[HairWidthScale_hairWidthScale_InterpEnumPlugOperator]
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


class HairWidthScale_hairWidthScale_InterpEnumField(
    EnumField[
        HairWidthScale_hairWidthScale_InterpEnumAttrOperator,
        HairWidthScale_hairWidthScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = HairWidthScale_hairWidthScale_InterpEnumAttrOperator
    PLUG_CLS = HairWidthScale_hairWidthScale_InterpEnumPlugOperator


class HairColorScale_hairColorScale_InterpEnumPlugOperator(
    EnumPlugOperator["HairColorScale_hairColorScale_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class HairColorScale_hairColorScale_InterpEnumAttrOperator(
    EnumAttrOperator[HairColorScale_hairColorScale_InterpEnumPlugOperator]
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


class HairColorScale_hairColorScale_InterpEnumField(
    EnumField[
        HairColorScale_hairColorScale_InterpEnumAttrOperator,
        HairColorScale_hairColorScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = HairColorScale_hairColorScale_InterpEnumAttrOperator
    PLUG_CLS = HairColorScale_hairColorScale_InterpEnumPlugOperator


class DisplacementScale_displacementScale_InterpEnumPlugOperator(
    EnumPlugOperator[
        "DisplacementScale_displacementScale_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class DisplacementScale_displacementScale_InterpEnumAttrOperator(
    EnumAttrOperator[
        DisplacementScale_displacementScale_InterpEnumPlugOperator
    ]
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


class DisplacementScale_displacementScale_InterpEnumField(
    EnumField[
        DisplacementScale_displacementScale_InterpEnumAttrOperator,
        DisplacementScale_displacementScale_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = DisplacementScale_displacementScale_InterpEnumAttrOperator
    PLUG_CLS = DisplacementScale_displacementScale_InterpEnumPlugOperator


class HairColorScale_hairColorScale_ColorPlugOperator(
    Float3CompoundBasePlugOperator[
        "HairColorScale_hairColorScale_ColorAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hairColorScale_ColorR", "hcscr"),
        ("hairColorScale_ColorG", "hcscg"),
        ("hairColorScale_ColorB", "hcscb"),
    )

    hairColorScale_ColorR = FloatField(default_value=0.0)
    hcscr = hairColorScale_ColorR

    hairColorScale_ColorG = FloatField(default_value=0.0)
    hcscg = hairColorScale_ColorG

    hairColorScale_ColorB = FloatField(default_value=0.0)
    hcscb = hairColorScale_ColorB


class HairColorScale_hairColorScale_ColorAttrOperator(
    Float3CompoundBaseAttrOperator[
        HairColorScale_hairColorScale_ColorPlugOperator
    ]
):
    __slots__ = ()

    hairColorScale_ColorR = FloatField(default_value=0.0)
    hcscr = hairColorScale_ColorR

    hairColorScale_ColorG = FloatField(default_value=0.0)
    hcscg = hairColorScale_ColorG

    hairColorScale_ColorB = FloatField(default_value=0.0)
    hcscb = hairColorScale_ColorB


class HairColorScale_hairColorScale_ColorField(
    Float3CompoundBaseField[
        HairColorScale_hairColorScale_ColorAttrOperator,
        HairColorScale_hairColorScale_ColorPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = HairColorScale_hairColorScale_ColorAttrOperator
    PLUG_CLS = HairColorScale_hairColorScale_ColorPlugOperator

    hairColorScale_ColorR = FloatField(default_value=0.0)
    hcscr = hairColorScale_ColorR

    hairColorScale_ColorG = FloatField(default_value=0.0)
    hcscg = hairColorScale_ColorG

    hairColorScale_ColorB = FloatField(default_value=0.0)
    hcscb = hairColorScale_ColorB


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


class ClumpCurlPlugOperator(CompoundPlugOperator["ClumpCurlAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clumpCurl_Position", "clcp"),
        ("clumpCurl_FloatValue", "clcfv"),
        ("clumpCurl_Interp", "clci"),
    )

    clumpCurl_Position = FloatField(default_value=0.0)
    clcp = clumpCurl_Position

    clumpCurl_FloatValue = FloatField(default_value=0.0)
    clcfv = clumpCurl_FloatValue

    clumpCurl_Interp = ClumpCurl_clumpCurl_InterpEnumField(default_value=0)
    clci = clumpCurl_Interp


class ClumpCurlAttrOperator(CompoundAttrOperator[ClumpCurlPlugOperator]):
    __slots__ = ()

    clumpCurl_Position = FloatField(default_value=0.0)
    clcp = clumpCurl_Position

    clumpCurl_FloatValue = FloatField(default_value=0.0)
    clcfv = clumpCurl_FloatValue

    clumpCurl_Interp = ClumpCurl_clumpCurl_InterpEnumField(default_value=0)
    clci = clumpCurl_Interp


class ClumpCurlField(
    CompoundField[ClumpCurlAttrOperator, ClumpCurlPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpCurlAttrOperator
    PLUG_CLS = ClumpCurlPlugOperator


class ClumpFlatnessPlugOperator(
    CompoundPlugOperator["ClumpFlatnessAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clumpFlatness_Position", "cflp"),
        ("clumpFlatness_FloatValue", "cflfv"),
        ("clumpFlatness_Interp", "cfli"),
    )

    clumpFlatness_Position = FloatField(default_value=0.0)
    cflp = clumpFlatness_Position

    clumpFlatness_FloatValue = FloatField(default_value=0.0)
    cflfv = clumpFlatness_FloatValue

    clumpFlatness_Interp = ClumpFlatness_clumpFlatness_InterpEnumField(
        default_value=0
    )
    cfli = clumpFlatness_Interp


class ClumpFlatnessAttrOperator(
    CompoundAttrOperator[ClumpFlatnessPlugOperator]
):
    __slots__ = ()

    clumpFlatness_Position = FloatField(default_value=0.0)
    cflp = clumpFlatness_Position

    clumpFlatness_FloatValue = FloatField(default_value=0.0)
    cflfv = clumpFlatness_FloatValue

    clumpFlatness_Interp = ClumpFlatness_clumpFlatness_InterpEnumField(
        default_value=0
    )
    cfli = clumpFlatness_Interp


class ClumpFlatnessField(
    CompoundField[ClumpFlatnessAttrOperator, ClumpFlatnessPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpFlatnessAttrOperator
    PLUG_CLS = ClumpFlatnessPlugOperator


class HairWidthScalePlugOperator(
    CompoundPlugOperator["HairWidthScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hairWidthScale_Position", "hwsp"),
        ("hairWidthScale_FloatValue", "hwsfv"),
        ("hairWidthScale_Interp", "hwsi"),
    )

    hairWidthScale_Position = FloatField(default_value=0.0)
    hwsp = hairWidthScale_Position

    hairWidthScale_FloatValue = FloatField(default_value=0.0)
    hwsfv = hairWidthScale_FloatValue

    hairWidthScale_Interp = HairWidthScale_hairWidthScale_InterpEnumField(
        default_value=0
    )
    hwsi = hairWidthScale_Interp


class HairWidthScaleAttrOperator(
    CompoundAttrOperator[HairWidthScalePlugOperator]
):
    __slots__ = ()

    hairWidthScale_Position = FloatField(default_value=0.0)
    hwsp = hairWidthScale_Position

    hairWidthScale_FloatValue = FloatField(default_value=0.0)
    hwsfv = hairWidthScale_FloatValue

    hairWidthScale_Interp = HairWidthScale_hairWidthScale_InterpEnumField(
        default_value=0
    )
    hwsi = hairWidthScale_Interp


class HairWidthScaleField(
    CompoundField[HairWidthScaleAttrOperator, HairWidthScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HairWidthScaleAttrOperator
    PLUG_CLS = HairWidthScalePlugOperator


class HairColorPlugOperator(
    Float3CompoundBasePlugOperator["HairColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hairColorR", "hcr"),
        ("hairColorG", "hcg"),
        ("hairColorB", "hcb"),
    )

    hairColorR = FloatField(default_value=0.30000001192092896)
    hcr = hairColorR

    hairColorG = FloatField(default_value=0.25)
    hcg = hairColorG

    hairColorB = FloatField(default_value=0.15000000596046448)
    hcb = hairColorB


class HairColorAttrOperator(
    Float3CompoundBaseAttrOperator[HairColorPlugOperator]
):
    __slots__ = ()

    hairColorR = FloatField(default_value=0.30000001192092896)
    hcr = hairColorR

    hairColorG = FloatField(default_value=0.25)
    hcg = hairColorG

    hairColorB = FloatField(default_value=0.15000000596046448)
    hcb = hairColorB


class HairColorField(
    Float3CompoundBaseField[HairColorAttrOperator, HairColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HairColorAttrOperator
    PLUG_CLS = HairColorPlugOperator

    hairColorR = FloatField(default_value=0.30000001192092896)
    hcr = hairColorR

    hairColorG = FloatField(default_value=0.25)
    hcg = hairColorG

    hairColorB = FloatField(default_value=0.15000000596046448)
    hcb = hairColorB


class HairColorScalePlugOperator(
    CompoundPlugOperator["HairColorScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hairColorScale_Position", "hcsp"),
        ("hairColorScale_Color", "hcsc"),
        ("hairColorScale_Interp", "hcsi"),
    )

    hairColorScale_Position = FloatField(default_value=0.0)
    hcsp = hairColorScale_Position

    hairColorScale_Color = HairColorScale_hairColorScale_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    hcsc = hairColorScale_Color

    hairColorScale_Interp = HairColorScale_hairColorScale_InterpEnumField(
        default_value=0
    )
    hcsi = hairColorScale_Interp


class HairColorScaleAttrOperator(
    CompoundAttrOperator[HairColorScalePlugOperator]
):
    __slots__ = ()

    hairColorScale_Position = FloatField(default_value=0.0)
    hcsp = hairColorScale_Position

    hairColorScale_Color = HairColorScale_hairColorScale_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    hcsc = hairColorScale_Color

    hairColorScale_Interp = HairColorScale_hairColorScale_InterpEnumField(
        default_value=0
    )
    hcsi = hairColorScale_Interp


class HairColorScaleField(
    CompoundField[HairColorScaleAttrOperator, HairColorScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HairColorScaleAttrOperator
    PLUG_CLS = HairColorScalePlugOperator


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "spr"),
        ("specularColorG", "spg"),
        ("specularColorB", "spb"),
    )

    specularColorR = FloatField(default_value=0.3499999940395355)
    spr = specularColorR

    specularColorG = FloatField(default_value=0.3499999940395355)
    spg = specularColorG

    specularColorB = FloatField(default_value=0.30000001192092896)
    spb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField(default_value=0.3499999940395355)
    spr = specularColorR

    specularColorG = FloatField(default_value=0.3499999940395355)
    spg = specularColorG

    specularColorB = FloatField(default_value=0.30000001192092896)
    spb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[
        SpecularColorAttrOperator, SpecularColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField(default_value=0.3499999940395355)
    spr = specularColorR

    specularColorG = FloatField(default_value=0.3499999940395355)
    spg = specularColorG

    specularColorB = FloatField(default_value=0.30000001192092896)
    spb = specularColorB


class DisplacementScalePlugOperator(
    CompoundPlugOperator["DisplacementScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("displacementScale_Position", "dscp"),
        ("displacementScale_FloatValue", "dscfv"),
        ("displacementScale_Interp", "dsci"),
    )

    displacementScale_Position = FloatField(default_value=0.0)
    dscp = displacementScale_Position

    displacementScale_FloatValue = FloatField(default_value=0.0)
    dscfv = displacementScale_FloatValue

    displacementScale_Interp = (
        DisplacementScale_displacementScale_InterpEnumField(default_value=0)
    )
    dsci = displacementScale_Interp


class DisplacementScaleAttrOperator(
    CompoundAttrOperator[DisplacementScalePlugOperator]
):
    __slots__ = ()

    displacementScale_Position = FloatField(default_value=0.0)
    dscp = displacementScale_Position

    displacementScale_FloatValue = FloatField(default_value=0.0)
    dscfv = displacementScale_FloatValue

    displacementScale_Interp = (
        DisplacementScale_displacementScale_InterpEnumField(default_value=0)
    )
    dsci = displacementScale_Interp


class DisplacementScaleField(
    CompoundField[DisplacementScaleAttrOperator, DisplacementScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplacementScaleAttrOperator
    PLUG_CLS = DisplacementScalePlugOperator


class FieldDataPlugOperator(CompoundPlugOperator["FieldDataAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldDataPosition", "fdp"),
        ("fieldDataVelocity", "fdv"),
        ("fieldDataMass", "fdm"),
        ("fieldDataDeltaTime", "fdt"),
    )

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class FieldDataAttrOperator(CompoundAttrOperator[FieldDataPlugOperator]):
    __slots__ = ()

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class FieldDataField(
    CompoundField[FieldDataAttrOperator, FieldDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldDataAttrOperator
    PLUG_CLS = FieldDataPlugOperator

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class CollisionDataPlugOperator(
    CompoundPlugOperator["CollisionDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionGeometry", "cge"),
        ("collisionResilience", "crs"),
        ("collisionFriction", "cfr"),
    )

    collisionGeometry = TypedField(multi=True, readable=False)
    cge = collisionGeometry

    collisionResilience = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    crs = collisionResilience

    collisionFriction = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    cfr = collisionFriction


class CollisionDataAttrOperator(
    CompoundAttrOperator[CollisionDataPlugOperator]
):
    __slots__ = ()

    collisionGeometry = TypedField(multi=True, readable=False)
    cge = collisionGeometry

    collisionResilience = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    crs = collisionResilience

    collisionFriction = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    cfr = collisionFriction


class CollisionDataField(
    CompoundField[CollisionDataAttrOperator, CollisionDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionDataAttrOperator
    PLUG_CLS = CollisionDataPlugOperator

    collisionGeometry = TypedField(multi=True, readable=False)
    cge = collisionGeometry

    collisionResilience = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    crs = collisionResilience

    collisionFriction = DoubleField(
        multi=True, default_value=0.0, readable=False
    )
    cfr = collisionFriction


class DisplayColorPlugOperator(
    Float3CompoundBasePlugOperator["DisplayColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("displayColorR", "dcr"),
        ("displayColorG", "dcg"),
        ("displayColorB", "dcb"),
    )

    displayColorR = FloatField(default_value=1.0)
    dcr = displayColorR

    displayColorG = FloatField(default_value=0.800000011920929)
    dcg = displayColorG

    displayColorB = FloatField(default_value=0.0)
    dcb = displayColorB


class DisplayColorAttrOperator(
    Float3CompoundBaseAttrOperator[DisplayColorPlugOperator]
):
    __slots__ = ()

    displayColorR = FloatField(default_value=1.0)
    dcr = displayColorR

    displayColorG = FloatField(default_value=0.800000011920929)
    dcg = displayColorG

    displayColorB = FloatField(default_value=0.0)
    dcb = displayColorB


class DisplayColorField(
    Float3CompoundBaseField[DisplayColorAttrOperator, DisplayColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayColorAttrOperator
    PLUG_CLS = DisplayColorPlugOperator

    displayColorR = FloatField(default_value=1.0)
    dcr = displayColorR

    displayColorG = FloatField(default_value=0.800000011920929)
    dcg = displayColorG

    displayColorB = FloatField(default_value=0.0)
    dcb = displayColorB


class AiHairShaderPlugOperator(
    Float3CompoundBasePlugOperator["AiHairShaderAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiHairShaderR", "ai_hair_shaderr"),
        ("aiHairShaderG", "ai_hair_shaderg"),
        ("aiHairShaderB", "ai_hair_shaderb"),
    )

    aiHairShaderR = FloatField(default_value=0.0)
    ai_hair_shaderr = aiHairShaderR

    aiHairShaderG = FloatField(default_value=0.0)
    ai_hair_shaderg = aiHairShaderG

    aiHairShaderB = FloatField(default_value=0.0)
    ai_hair_shaderb = aiHairShaderB


class AiHairShaderAttrOperator(
    Float3CompoundBaseAttrOperator[AiHairShaderPlugOperator]
):
    __slots__ = ()

    aiHairShaderR = FloatField(default_value=0.0)
    ai_hair_shaderr = aiHairShaderR

    aiHairShaderG = FloatField(default_value=0.0)
    ai_hair_shaderg = aiHairShaderG

    aiHairShaderB = FloatField(default_value=0.0)
    ai_hair_shaderb = aiHairShaderB


class AiHairShaderField(
    Float3CompoundBaseField[AiHairShaderAttrOperator, AiHairShaderPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiHairShaderAttrOperator
    PLUG_CLS = AiHairShaderPlugOperator

    aiHairShaderR = FloatField(default_value=0.0)
    ai_hair_shaderr = aiHairShaderR

    aiHairShaderG = FloatField(default_value=0.0)
    ai_hair_shaderg = aiHairShaderG

    aiHairShaderB = FloatField(default_value=0.0)
    ai_hair_shaderb = aiHairShaderB
