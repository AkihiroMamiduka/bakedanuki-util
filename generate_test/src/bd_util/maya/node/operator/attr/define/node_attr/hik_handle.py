# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class PostureTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BIPED = 0
    QUADRUPED = 1


class PostureTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BIPED = 0
    QUADRUPED = 1

    NAME_MAP = {
        BIPED: "biped",
        QUADRUPED: "quadruped",
    }


class PostureTypeEnumField(
    EnumField[PostureTypeEnumAttrOperator, PostureTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PostureTypeEnumAttrOperator
    PLUG_CLS = PostureTypeEnumPlugOperator


class HipTranslationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD_RIGID = 0
    BODY_RIGID = 1


class HipTranslationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD_RIGID = 0
    BODY_RIGID = 1

    NAME_MAP = {
        WORLD_RIGID: "world rigid",
        BODY_RIGID: "body rigid",
    }


class HipTranslationModeEnumField(
    EnumField[HipTranslationModeEnumAttrOperator, HipTranslationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipTranslationModeEnumAttrOperator
    PLUG_CLS = HipTranslationModeEnumPlugOperator


class HandsFloorPivotEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    WRIST = 1
    FINGERS = 2


class HandsFloorPivotEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    WRIST = 1
    FINGERS = 2

    NAME_MAP = {
        AUTO: "auto",
        WRIST: "wrist",
        FINGERS: "fingers",
    }


class HandsFloorPivotEnumField(
    EnumField[HandsFloorPivotEnumAttrOperator, HandsFloorPivotEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandsFloorPivotEnumAttrOperator
    PLUG_CLS = HandsFloorPivotEnumPlugOperator


class HandsContactTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    WRIST = 1
    FINGER_BASE = 2
    HOOF = 3


class HandsContactTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    WRIST = 1
    FINGER_BASE = 2
    HOOF = 3

    NAME_MAP = {
        NORMAL: "normal",
        WRIST: "wrist",
        FINGER_BASE: "finger base",
        HOOF: "hoof",
    }


class HandsContactTypeEnumField(
    EnumField[HandsContactTypeEnumAttrOperator, HandsContactTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandsContactTypeEnumAttrOperator
    PLUG_CLS = HandsContactTypeEnumPlugOperator


class FeetFloorPivotEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    ANKLE = 1
    TOES = 2


class FeetFloorPivotEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    ANKLE = 1
    TOES = 2

    NAME_MAP = {
        AUTO: "auto",
        ANKLE: "ankle",
        TOES: "toes",
    }


class FeetFloorPivotEnumField(
    EnumField[FeetFloorPivotEnumAttrOperator, FeetFloorPivotEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FeetFloorPivotEnumAttrOperator
    PLUG_CLS = FeetFloorPivotEnumPlugOperator


class FeetContactTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    ANKLE = 1
    TOE_BASE = 2
    HOOF = 3


class FeetContactTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    ANKLE = 1
    TOE_BASE = 2
    HOOF = 3

    NAME_MAP = {
        NORMAL: "normal",
        ANKLE: "ankle",
        TOE_BASE: "toe base",
        HOOF: "hoof",
    }


class FeetContactTypeEnumField(
    EnumField[FeetContactTypeEnumAttrOperator, FeetContactTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FeetContactTypeEnumAttrOperator
    PLUG_CLS = FeetContactTypeEnumPlugOperator


class FingersContactTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_MINUS_SPREAD = 2


class FingersContactTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_MINUS_SPREAD = 2

    NAME_MAP = {
        STICKY: "sticky",
        SPREAD: "spread",
        STICKY_MINUS_SPREAD: "sticky-spread",
    }


class FingersContactTypeEnumField(
    EnumField[FingersContactTypeEnumAttrOperator, FingersContactTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FingersContactTypeEnumAttrOperator
    PLUG_CLS = FingersContactTypeEnumPlugOperator


class ToesContactTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_MINUS_SPREAD = 2


class ToesContactTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_MINUS_SPREAD = 2

    NAME_MAP = {
        STICKY: "sticky",
        SPREAD: "spread",
        STICKY_MINUS_SPREAD: "sticky-spread",
    }


class ToesContactTypeEnumField(
    EnumField[ToesContactTypeEnumAttrOperator, ToesContactTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ToesContactTypeEnumAttrOperator
    PLUG_CLS = ToesContactTypeEnumPlugOperator


class RollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1


class RollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1

    NAME_MAP = {
        RELATIVE: "relative",
        ABSOLUTE: "absolute",
    }


class RollExtractionModeEnumField(
    EnumField[RollExtractionModeEnumAttrOperator, RollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RollExtractionModeEnumAttrOperator
    PLUG_CLS = RollExtractionModeEnumPlugOperator


class PoleVectorPlugOperator(
    Double3CompoundBasePlugOperator["PoleVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("poleVectorX", "pvx"),
        ("poleVectorY", "pvy"),
        ("poleVectorZ", "pvz"),
    )

    poleVectorX = DoubleField(default_value=0.0)
    pvx = poleVectorX

    poleVectorY = DoubleField(default_value=0.0)
    pvy = poleVectorY

    poleVectorZ = DoubleField(default_value=1.0)
    pvz = poleVectorZ


class PoleVectorAttrOperator(
    Double3CompoundBaseAttrOperator[PoleVectorPlugOperator]
):
    __slots__ = ()

    poleVectorX = DoubleField(default_value=0.0)
    pvx = poleVectorX

    poleVectorY = DoubleField(default_value=0.0)
    pvy = poleVectorY

    poleVectorZ = DoubleField(default_value=1.0)
    pvz = poleVectorZ


class PoleVectorField(
    Double3CompoundBaseField[PoleVectorAttrOperator, PoleVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PoleVectorAttrOperator
    PLUG_CLS = PoleVectorPlugOperator

    poleVectorX = DoubleField(default_value=0.0)
    pvx = poleVectorX

    poleVectorY = DoubleField(default_value=0.0)
    pvy = poleVectorY

    poleVectorZ = DoubleField(default_value=1.0)
    pvz = poleVectorZ


class DWorldUpVectorPlugOperator(
    Double3CompoundBasePlugOperator["DWorldUpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dWorldUpVectorX", "dwux"),
        ("dWorldUpVectorY", "dwuy"),
        ("dWorldUpVectorZ", "dwuz"),
    )

    dWorldUpVectorX = DoubleField(default_value=0.0)
    dwux = dWorldUpVectorX

    dWorldUpVectorY = DoubleField(default_value=1.0)
    dwuy = dWorldUpVectorY

    dWorldUpVectorZ = DoubleField(default_value=0.0)
    dwuz = dWorldUpVectorZ


class DWorldUpVectorAttrOperator(
    Double3CompoundBaseAttrOperator[DWorldUpVectorPlugOperator]
):
    __slots__ = ()

    dWorldUpVectorX = DoubleField(default_value=0.0)
    dwux = dWorldUpVectorX

    dWorldUpVectorY = DoubleField(default_value=1.0)
    dwuy = dWorldUpVectorY

    dWorldUpVectorZ = DoubleField(default_value=0.0)
    dwuz = dWorldUpVectorZ


class DWorldUpVectorField(
    Double3CompoundBaseField[DWorldUpVectorAttrOperator, DWorldUpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DWorldUpVectorAttrOperator
    PLUG_CLS = DWorldUpVectorPlugOperator

    dWorldUpVectorX = DoubleField(default_value=0.0)
    dwux = dWorldUpVectorX

    dWorldUpVectorY = DoubleField(default_value=1.0)
    dwuy = dWorldUpVectorY

    dWorldUpVectorZ = DoubleField(default_value=0.0)
    dwuz = dWorldUpVectorZ


class DWorldUpVectorEndPlugOperator(
    Double3CompoundBasePlugOperator["DWorldUpVectorEndAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dWorldUpVectorEndX", "dwvx"),
        ("dWorldUpVectorEndY", "dwvy"),
        ("dWorldUpVectorEndZ", "dwvz"),
    )

    dWorldUpVectorEndX = DoubleField(default_value=0.0)
    dwvx = dWorldUpVectorEndX

    dWorldUpVectorEndY = DoubleField(default_value=1.0)
    dwvy = dWorldUpVectorEndY

    dWorldUpVectorEndZ = DoubleField(default_value=0.0)
    dwvz = dWorldUpVectorEndZ


class DWorldUpVectorEndAttrOperator(
    Double3CompoundBaseAttrOperator[DWorldUpVectorEndPlugOperator]
):
    __slots__ = ()

    dWorldUpVectorEndX = DoubleField(default_value=0.0)
    dwvx = dWorldUpVectorEndX

    dWorldUpVectorEndY = DoubleField(default_value=1.0)
    dwvy = dWorldUpVectorEndY

    dWorldUpVectorEndZ = DoubleField(default_value=0.0)
    dwvz = dWorldUpVectorEndZ


class DWorldUpVectorEndField(
    Double3CompoundBaseField[DWorldUpVectorEndAttrOperator, DWorldUpVectorEndPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DWorldUpVectorEndAttrOperator
    PLUG_CLS = DWorldUpVectorEndPlugOperator

    dWorldUpVectorEndX = DoubleField(default_value=0.0)
    dwvx = dWorldUpVectorEndX

    dWorldUpVectorEndY = DoubleField(default_value=1.0)
    dwvy = dWorldUpVectorEndY

    dWorldUpVectorEndZ = DoubleField(default_value=0.0)
    dwvz = dWorldUpVectorEndZ


class DTwistStartEndPlugOperator(
    Double2CompoundBasePlugOperator["DTwistStartEndAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dTwistStart", "dtst"),
        ("dTwistEnd", "dten"),
    )

    dTwistStart = DoubleField(default_value=0.0)
    dtst = dTwistStart

    dTwistEnd = DoubleField(default_value=0.0)
    dten = dTwistEnd


class DTwistStartEndAttrOperator(
    Double2CompoundBaseAttrOperator[DTwistStartEndPlugOperator]
):
    __slots__ = ()

    dTwistStart = DoubleField(default_value=0.0)
    dtst = dTwistStart

    dTwistEnd = DoubleField(default_value=0.0)
    dten = dTwistEnd


class DTwistStartEndField(
    Double2CompoundBaseField[DTwistStartEndAttrOperator, DTwistStartEndPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DTwistStartEndAttrOperator
    PLUG_CLS = DTwistStartEndPlugOperator

    dTwistStart = DoubleField(default_value=0.0)
    dtst = dTwistStart

    dTwistEnd = DoubleField(default_value=0.0)
    dten = dTwistEnd


class DTwistRampPlugOperator(
    Float3CompoundBasePlugOperator["DTwistRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dTwistRampR", "dtrr"),
        ("dTwistRampG", "dtrg"),
        ("dTwistRampB", "dtrb"),
    )

    dTwistRampR = FloatField(default_value=0.0)
    dtrr = dTwistRampR

    dTwistRampG = FloatField(default_value=0.0)
    dtrg = dTwistRampG

    dTwistRampB = FloatField(default_value=0.0)
    dtrb = dTwistRampB


class DTwistRampAttrOperator(
    Float3CompoundBaseAttrOperator[DTwistRampPlugOperator]
):
    __slots__ = ()

    dTwistRampR = FloatField(default_value=0.0)
    dtrr = dTwistRampR

    dTwistRampG = FloatField(default_value=0.0)
    dtrg = dTwistRampG

    dTwistRampB = FloatField(default_value=0.0)
    dtrb = dTwistRampB


class DTwistRampField(
    Float3CompoundBaseField[DTwistRampAttrOperator, DTwistRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DTwistRampAttrOperator
    PLUG_CLS = DTwistRampPlugOperator

    dTwistRampR = FloatField(default_value=0.0)
    dtrr = dTwistRampR

    dTwistRampG = FloatField(default_value=0.0)
    dtrg = dTwistRampG

    dTwistRampB = FloatField(default_value=0.0)
    dtrb = dTwistRampB


class SolvingPlugOperator(
    CompoundPlugOperator["SolvingAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("postureType", "pt"),
        ("expertMode", "exp"),
        ("realisticShoulderSolving", "rss"),
        ("solveFingers", "sf"),
        ("hipTranslationMode", "htm"),
    )

    postureType = PostureTypeEnumField(default_value=0)
    pt = postureType

    expertMode = BoolField(default_value=False)
    exp = expertMode

    realisticShoulderSolving = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rss = realisticShoulderSolving

    solveFingers = BoolField(default_value=True)
    sf = solveFingers

    hipTranslationMode = HipTranslationModeEnumField(default_value=0)
    htm = hipTranslationMode


class SolvingAttrOperator(
    CompoundAttrOperator[SolvingPlugOperator]
):
    __slots__ = ()

    postureType = PostureTypeEnumField(default_value=0)
    pt = postureType

    expertMode = BoolField(default_value=False)
    exp = expertMode

    realisticShoulderSolving = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rss = realisticShoulderSolving

    solveFingers = BoolField(default_value=True)
    sf = solveFingers

    hipTranslationMode = HipTranslationModeEnumField(default_value=0)
    htm = hipTranslationMode


class SolvingField(
    CompoundField[SolvingAttrOperator, SolvingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolvingAttrOperator
    PLUG_CLS = SolvingPlugOperator

    postureType = PostureTypeEnumField(default_value=0)
    pt = postureType

    expertMode = BoolField(default_value=False)
    exp = expertMode

    realisticShoulderSolving = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rss = realisticShoulderSolving

    solveFingers = BoolField(default_value=True)
    sf = solveFingers

    hipTranslationMode = HipTranslationModeEnumField(default_value=0)
    htm = hipTranslationMode


class FloorContactsPlugOperator(
    CompoundPlugOperator["FloorContactsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("handsFloorContact", "hfc"),
        ("feetFloorContact", "fec"),
        ("fingersFloorContact", "fic"),
        ("toesFloorContact", "tfc"),
    )

    handsFloorContact = BoolField(default_value=False)
    hfc = handsFloorContact

    feetFloorContact = BoolField(default_value=False)
    fec = feetFloorContact

    fingersFloorContact = BoolField(default_value=False)
    fic = fingersFloorContact

    toesFloorContact = BoolField(default_value=False)
    tfc = toesFloorContact


class FloorContactsAttrOperator(
    CompoundAttrOperator[FloorContactsPlugOperator]
):
    __slots__ = ()

    handsFloorContact = BoolField(default_value=False)
    hfc = handsFloorContact

    feetFloorContact = BoolField(default_value=False)
    fec = feetFloorContact

    fingersFloorContact = BoolField(default_value=False)
    fic = fingersFloorContact

    toesFloorContact = BoolField(default_value=False)
    tfc = toesFloorContact


class FloorContactsField(
    CompoundField[FloorContactsAttrOperator, FloorContactsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloorContactsAttrOperator
    PLUG_CLS = FloorContactsPlugOperator

    handsFloorContact = BoolField(default_value=False)
    hfc = handsFloorContact

    feetFloorContact = BoolField(default_value=False)
    fec = feetFloorContact

    fingersFloorContact = BoolField(default_value=False)
    fic = fingersFloorContact

    toesFloorContact = BoolField(default_value=False)
    tfc = toesFloorContact


class HandsFloorContactSetupPlugOperator(
    CompoundPlugOperator["HandsFloorContactSetupAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("handsFloorPivot", "hfp"),
        ("handsContactType", "hct"),
        ("handsContactStiffness", "hcs"),
    )

    handsFloorPivot = HandsFloorPivotEnumField(default_value=0)
    hfp = handsFloorPivot

    handsContactType = HandsContactTypeEnumField(default_value=0)
    hct = handsContactType

    handsContactStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcs = handsContactStiffness


class HandsFloorContactSetupAttrOperator(
    CompoundAttrOperator[HandsFloorContactSetupPlugOperator]
):
    __slots__ = ()

    handsFloorPivot = HandsFloorPivotEnumField(default_value=0)
    hfp = handsFloorPivot

    handsContactType = HandsContactTypeEnumField(default_value=0)
    hct = handsContactType

    handsContactStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcs = handsContactStiffness


class HandsFloorContactSetupField(
    CompoundField[HandsFloorContactSetupAttrOperator, HandsFloorContactSetupPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandsFloorContactSetupAttrOperator
    PLUG_CLS = HandsFloorContactSetupPlugOperator

    handsFloorPivot = HandsFloorPivotEnumField(default_value=0)
    hfp = handsFloorPivot

    handsContactType = HandsContactTypeEnumField(default_value=0)
    hct = handsContactType

    handsContactStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcs = handsContactStiffness


class ContactsPositionPlugOperator(
    CompoundPlugOperator["ContactsPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("handHeight", "hh"),
        ("handBack", "hb"),
        ("handMiddle", "hm"),
        ("handFront", "hf"),
        ("handInSide", "his"),
        ("handOutSide", "hos"),
    )

    handHeight = FloatField(default_value=7.5, min_value=0.0, max_value=10000.0)
    hh = handHeight

    handBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    hb = handBack

    handMiddle = FloatField(default_value=13.0, min_value=0.0, max_value=10000.0)
    hm = handMiddle

    handFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    hf = handFront

    handInSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    his = handInSide

    handOutSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    hos = handOutSide


class ContactsPositionAttrOperator(
    CompoundAttrOperator[ContactsPositionPlugOperator]
):
    __slots__ = ()

    handHeight = FloatField(default_value=7.5, min_value=0.0, max_value=10000.0)
    hh = handHeight

    handBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    hb = handBack

    handMiddle = FloatField(default_value=13.0, min_value=0.0, max_value=10000.0)
    hm = handMiddle

    handFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    hf = handFront

    handInSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    his = handInSide

    handOutSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    hos = handOutSide


class ContactsPositionField(
    CompoundField[ContactsPositionAttrOperator, ContactsPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ContactsPositionAttrOperator
    PLUG_CLS = ContactsPositionPlugOperator

    handHeight = FloatField(default_value=7.5, min_value=0.0, max_value=10000.0)
    hh = handHeight

    handBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    hb = handBack

    handMiddle = FloatField(default_value=13.0, min_value=0.0, max_value=10000.0)
    hm = handMiddle

    handFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    hf = handFront

    handInSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    his = handInSide

    handOutSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    hos = handOutSide


class FeetFloorContactSetupPlugOperator(
    CompoundPlugOperator["FeetFloorContactSetupAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("feetFloorPivot", "fpv"),
        ("feetContactType", "fct"),
        ("feetContactStiffness", "fcs"),
    )

    feetFloorPivot = FeetFloorPivotEnumField(default_value=0)
    fpv = feetFloorPivot

    feetContactType = FeetContactTypeEnumField(default_value=0)
    fct = feetContactType

    feetContactStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    fcs = feetContactStiffness


class FeetFloorContactSetupAttrOperator(
    CompoundAttrOperator[FeetFloorContactSetupPlugOperator]
):
    __slots__ = ()

    feetFloorPivot = FeetFloorPivotEnumField(default_value=0)
    fpv = feetFloorPivot

    feetContactType = FeetContactTypeEnumField(default_value=0)
    fct = feetContactType

    feetContactStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    fcs = feetContactStiffness


class FeetFloorContactSetupField(
    CompoundField[FeetFloorContactSetupAttrOperator, FeetFloorContactSetupPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FeetFloorContactSetupAttrOperator
    PLUG_CLS = FeetFloorContactSetupPlugOperator

    feetFloorPivot = FeetFloorPivotEnumField(default_value=0)
    fpv = feetFloorPivot

    feetContactType = FeetContactTypeEnumField(default_value=0)
    fct = feetContactType

    feetContactStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    fcs = feetContactStiffness


class FeetContactPositionPlugOperator(
    CompoundPlugOperator["FeetContactPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("footHeight", "fh"),
        ("footBack", "fra"),
        ("footMiddle", "fma"),
        ("footFront", "ffm"),
        ("footInSide", "fia"),
        ("footOutSide", "foa"),
    )

    footHeight = FloatField(default_value=7.5, min_value=0.0, max_value=10000.0)
    fh = footHeight

    footBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    fra = footBack

    footMiddle = FloatField(default_value=13.0, min_value=0.0, max_value=10000.0)
    fma = footMiddle

    footFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    ffm = footFront

    footInSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    fia = footInSide

    footOutSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    foa = footOutSide


class FeetContactPositionAttrOperator(
    CompoundAttrOperator[FeetContactPositionPlugOperator]
):
    __slots__ = ()

    footHeight = FloatField(default_value=7.5, min_value=0.0, max_value=10000.0)
    fh = footHeight

    footBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    fra = footBack

    footMiddle = FloatField(default_value=13.0, min_value=0.0, max_value=10000.0)
    fma = footMiddle

    footFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    ffm = footFront

    footInSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    fia = footInSide

    footOutSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    foa = footOutSide


class FeetContactPositionField(
    CompoundField[FeetContactPositionAttrOperator, FeetContactPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FeetContactPositionAttrOperator
    PLUG_CLS = FeetContactPositionPlugOperator

    footHeight = FloatField(default_value=7.5, min_value=0.0, max_value=10000.0)
    fh = footHeight

    footBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    fra = footBack

    footMiddle = FloatField(default_value=13.0, min_value=0.0, max_value=10000.0)
    fma = footMiddle

    footFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    ffm = footFront

    footInSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    fia = footInSide

    footOutSide = FloatField(default_value=5.0, min_value=0.0, max_value=10000.0)
    foa = footOutSide


class FingersFloorContactSetupPlugOperator(
    CompoundPlugOperator["FingersFloorContactSetupAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fingersContactType", "fcm"),
        ("fingersContactRollStiffness", "hcr"),
    )

    fingersContactType = FingersContactTypeEnumField(default_value=1)
    fcm = fingersContactType

    fingersContactRollStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcr = fingersContactRollStiffness


class FingersFloorContactSetupAttrOperator(
    CompoundAttrOperator[FingersFloorContactSetupPlugOperator]
):
    __slots__ = ()

    fingersContactType = FingersContactTypeEnumField(default_value=1)
    fcm = fingersContactType

    fingersContactRollStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcr = fingersContactRollStiffness


class FingersFloorContactSetupField(
    CompoundField[FingersFloorContactSetupAttrOperator, FingersFloorContactSetupPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FingersFloorContactSetupAttrOperator
    PLUG_CLS = FingersFloorContactSetupPlugOperator

    fingersContactType = FingersContactTypeEnumField(default_value=1)
    fcm = fingersContactType

    fingersContactRollStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    hcr = fingersContactRollStiffness


class FingerTipsSizesPlugOperator(
    CompoundPlugOperator["FingerTipsSizesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leftHandThumbTip", "ltt"),
        ("leftHandIndexTip", "lit"),
        ("leftHandMiddleTip", "lmt"),
        ("leftHandRingTip", "lrt"),
        ("leftHandPinkyTip", "lpt"),
        ("leftHandExtraFingerTip", "lxt"),
        ("rightHandThumbTip", "rtt"),
        ("rightHandIndexTip", "rit"),
        ("rightHandMiddleTip", "rmt"),
        ("rightHandRingTip", "rrt"),
        ("rightHandPinkyTip", "rpp"),
        ("rightHandExtraFingerTip", "rxt"),
    )

    leftHandThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    ltt = leftHandThumbTip

    leftHandIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lit = leftHandIndexTip

    leftHandMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lmt = leftHandMiddleTip

    leftHandRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lrt = leftHandRingTip

    leftHandPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lpt = leftHandPinkyTip

    leftHandExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lxt = leftHandExtraFingerTip

    rightHandThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rtt = rightHandThumbTip

    rightHandIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rit = rightHandIndexTip

    rightHandMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rmt = rightHandMiddleTip

    rightHandRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rrt = rightHandRingTip

    rightHandPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rpp = rightHandPinkyTip

    rightHandExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rxt = rightHandExtraFingerTip


class FingerTipsSizesAttrOperator(
    CompoundAttrOperator[FingerTipsSizesPlugOperator]
):
    __slots__ = ()

    leftHandThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    ltt = leftHandThumbTip

    leftHandIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lit = leftHandIndexTip

    leftHandMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lmt = leftHandMiddleTip

    leftHandRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lrt = leftHandRingTip

    leftHandPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lpt = leftHandPinkyTip

    leftHandExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lxt = leftHandExtraFingerTip

    rightHandThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rtt = rightHandThumbTip

    rightHandIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rit = rightHandIndexTip

    rightHandMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rmt = rightHandMiddleTip

    rightHandRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rrt = rightHandRingTip

    rightHandPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rpp = rightHandPinkyTip

    rightHandExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rxt = rightHandExtraFingerTip


class FingerTipsSizesField(
    CompoundField[FingerTipsSizesAttrOperator, FingerTipsSizesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FingerTipsSizesAttrOperator
    PLUG_CLS = FingerTipsSizesPlugOperator

    leftHandThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    ltt = leftHandThumbTip

    leftHandIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lit = leftHandIndexTip

    leftHandMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lmt = leftHandMiddleTip

    leftHandRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lrt = leftHandRingTip

    leftHandPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lpt = leftHandPinkyTip

    leftHandExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    lxt = leftHandExtraFingerTip

    rightHandThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rtt = rightHandThumbTip

    rightHandIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rit = rightHandIndexTip

    rightHandMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rmt = rightHandMiddleTip

    rightHandRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rrt = rightHandRingTip

    rightHandPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rpp = rightHandPinkyTip

    rightHandExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    rxt = rightHandExtraFingerTip


class ToesFloorContactSetupPlugOperator(
    CompoundPlugOperator["ToesFloorContactSetupAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("toesContactType", "tct"),
        ("toesContactRollStiffness", "fcr"),
    )

    toesContactType = ToesContactTypeEnumField(default_value=1)
    tct = toesContactType

    toesContactRollStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    fcr = toesContactRollStiffness


class ToesFloorContactSetupAttrOperator(
    CompoundAttrOperator[ToesFloorContactSetupPlugOperator]
):
    __slots__ = ()

    toesContactType = ToesContactTypeEnumField(default_value=1)
    tct = toesContactType

    toesContactRollStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    fcr = toesContactRollStiffness


class ToesFloorContactSetupField(
    CompoundField[ToesFloorContactSetupAttrOperator, ToesFloorContactSetupPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ToesFloorContactSetupAttrOperator
    PLUG_CLS = ToesFloorContactSetupPlugOperator

    toesContactType = ToesContactTypeEnumField(default_value=1)
    tct = toesContactType

    toesContactRollStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    fcr = toesContactRollStiffness


class ToeTipsSizesPlugOperator(
    CompoundPlugOperator["ToeTipsSizesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leftFootThumbTip", "ttl"),
        ("leftFootIndexTip", "til"),
        ("leftFootMiddleTip", "tml"),
        ("leftFootRingTip", "trl"),
        ("leftFootPinkyTip", "tpl"),
        ("leftFootExtraFingerTip", "txl"),
        ("rightFootThumbTip", "ttr"),
        ("rightFootIndexTip", "tir"),
        ("rightFootMiddleTip", "tmr"),
        ("rightFootRingTip", "trr"),
        ("rightFootPinkyTip", "tpr"),
        ("rightFootExtraFingerTip", "txr"),
    )

    leftFootThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    ttl = leftFootThumbTip

    leftFootIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    til = leftFootIndexTip

    leftFootMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tml = leftFootMiddleTip

    leftFootRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    trl = leftFootRingTip

    leftFootPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tpl = leftFootPinkyTip

    leftFootExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    txl = leftFootExtraFingerTip

    rightFootThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    ttr = rightFootThumbTip

    rightFootIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tir = rightFootIndexTip

    rightFootMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tmr = rightFootMiddleTip

    rightFootRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    trr = rightFootRingTip

    rightFootPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tpr = rightFootPinkyTip

    rightFootExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    txr = rightFootExtraFingerTip


class ToeTipsSizesAttrOperator(
    CompoundAttrOperator[ToeTipsSizesPlugOperator]
):
    __slots__ = ()

    leftFootThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    ttl = leftFootThumbTip

    leftFootIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    til = leftFootIndexTip

    leftFootMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tml = leftFootMiddleTip

    leftFootRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    trl = leftFootRingTip

    leftFootPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tpl = leftFootPinkyTip

    leftFootExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    txl = leftFootExtraFingerTip

    rightFootThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    ttr = rightFootThumbTip

    rightFootIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tir = rightFootIndexTip

    rightFootMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tmr = rightFootMiddleTip

    rightFootRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    trr = rightFootRingTip

    rightFootPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tpr = rightFootPinkyTip

    rightFootExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    txr = rightFootExtraFingerTip


class ToeTipsSizesField(
    CompoundField[ToeTipsSizesAttrOperator, ToeTipsSizesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ToeTipsSizesAttrOperator
    PLUG_CLS = ToeTipsSizesPlugOperator

    leftFootThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    ttl = leftFootThumbTip

    leftFootIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    til = leftFootIndexTip

    leftFootMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tml = leftFootMiddleTip

    leftFootRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    trl = leftFootRingTip

    leftFootPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tpl = leftFootPinkyTip

    leftFootExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    txl = leftFootExtraFingerTip

    rightFootThumbTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    ttr = rightFootThumbTip

    rightFootIndexTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tir = rightFootIndexTip

    rightFootMiddleTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tmr = rightFootMiddleTip

    rightFootRingTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    trr = rightFootRingTip

    rightFootPinkyTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    tpr = rightFootPinkyTip

    rightFootExtraFingerTip = FloatField(default_value=0.5, min_value=0.0, max_value=1000.0)
    txr = rightFootExtraFingerTip


class HeadPlugOperator(
    CompoundPlugOperator["HeadAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("headPull", "phd"),
    )

    headPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    phd = headPull


class HeadAttrOperator(
    CompoundAttrOperator[HeadPlugOperator]
):
    __slots__ = ()

    headPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    phd = headPull


class HeadField(
    CompoundField[HeadAttrOperator, HeadPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HeadAttrOperator
    PLUG_CLS = HeadPlugOperator

    headPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    phd = headPull


class LeftArmPlugOperator(
    CompoundPlugOperator["LeftArmAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leftElbowPull", "ple"),
        ("leftHandPullChest", "cpl"),
        ("leftHandPullHips", "plh"),
        ("leftFingerBasePull", "plb"),
    )

    leftElbowPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ple = leftElbowPull

    leftHandPullChest = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cpl = leftHandPullChest

    leftHandPullHips = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    plh = leftHandPullHips

    leftFingerBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plb = leftFingerBasePull


class LeftArmAttrOperator(
    CompoundAttrOperator[LeftArmPlugOperator]
):
    __slots__ = ()

    leftElbowPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ple = leftElbowPull

    leftHandPullChest = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cpl = leftHandPullChest

    leftHandPullHips = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    plh = leftHandPullHips

    leftFingerBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plb = leftFingerBasePull


class LeftArmField(
    CompoundField[LeftArmAttrOperator, LeftArmPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmAttrOperator
    PLUG_CLS = LeftArmPlugOperator

    leftElbowPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ple = leftElbowPull

    leftHandPullChest = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cpl = leftHandPullChest

    leftHandPullHips = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    plh = leftHandPullHips

    leftFingerBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plb = leftFingerBasePull


class RightArmPlugOperator(
    CompoundPlugOperator["RightArmAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rightElbowPull", "pre"),
        ("rightHandPullChest", "cpr"),
        ("rightHandPullHips", "prh"),
        ("rightFingerBasePull", "prb"),
    )

    rightElbowPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    pre = rightElbowPull

    rightHandPullChest = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cpr = rightHandPullChest

    rightHandPullHips = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    prh = rightHandPullHips

    rightFingerBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prb = rightFingerBasePull


class RightArmAttrOperator(
    CompoundAttrOperator[RightArmPlugOperator]
):
    __slots__ = ()

    rightElbowPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    pre = rightElbowPull

    rightHandPullChest = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cpr = rightHandPullChest

    rightHandPullHips = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    prh = rightHandPullHips

    rightFingerBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prb = rightFingerBasePull


class RightArmField(
    CompoundField[RightArmAttrOperator, RightArmPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmAttrOperator
    PLUG_CLS = RightArmPlugOperator

    rightElbowPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    pre = rightElbowPull

    rightHandPullChest = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cpr = rightHandPullChest

    rightHandPullHips = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    prh = rightHandPullHips

    rightFingerBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prb = rightFingerBasePull


class ChestPlugOperator(
    CompoundPlugOperator["ChestAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("chestPull", "rcp"),
    )

    chestPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rcp = chestPull


class ChestAttrOperator(
    CompoundAttrOperator[ChestPlugOperator]
):
    __slots__ = ()

    chestPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rcp = chestPull


class ChestField(
    CompoundField[ChestAttrOperator, ChestPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ChestAttrOperator
    PLUG_CLS = ChestPlugOperator

    chestPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rcp = chestPull


class HipsPlugOperator(
    CompoundPlugOperator["HipsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hipsPull", "chp"),
    )

    hipsPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    chp = hipsPull


class HipsAttrOperator(
    CompoundAttrOperator[HipsPlugOperator]
):
    __slots__ = ()

    hipsPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    chp = hipsPull


class HipsField(
    CompoundField[HipsAttrOperator, HipsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsAttrOperator
    PLUG_CLS = HipsPlugOperator

    hipsPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    chp = hipsPull


class LeftLegPlugOperator(
    CompoundPlugOperator["LeftLegAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leftKneePull", "plk"),
        ("leftFootPull", "plf"),
        ("leftToeBasePull", "plt"),
    )

    leftKneePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plk = leftKneePull

    leftFootPull = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    plf = leftFootPull

    leftToeBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plt = leftToeBasePull


class LeftLegAttrOperator(
    CompoundAttrOperator[LeftLegPlugOperator]
):
    __slots__ = ()

    leftKneePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plk = leftKneePull

    leftFootPull = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    plf = leftFootPull

    leftToeBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plt = leftToeBasePull


class LeftLegField(
    CompoundField[LeftLegAttrOperator, LeftLegPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegAttrOperator
    PLUG_CLS = LeftLegPlugOperator

    leftKneePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plk = leftKneePull

    leftFootPull = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    plf = leftFootPull

    leftToeBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plt = leftToeBasePull


class RightLegPlugOperator(
    CompoundPlugOperator["RightLegAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rightKneePull", "prk"),
        ("rightFootPull", "prf"),
        ("rightToeBasePull", "prt"),
    )

    rightKneePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prk = rightKneePull

    rightFootPull = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    prf = rightFootPull

    rightToeBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prt = rightToeBasePull


class RightLegAttrOperator(
    CompoundAttrOperator[RightLegPlugOperator]
):
    __slots__ = ()

    rightKneePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prk = rightKneePull

    rightFootPull = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    prf = rightFootPull

    rightToeBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prt = rightToeBasePull


class RightLegField(
    CompoundField[RightLegAttrOperator, RightLegPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegAttrOperator
    PLUG_CLS = RightLegPlugOperator

    rightKneePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prk = rightKneePull

    rightFootPull = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    prf = rightFootPull

    rightToeBasePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prt = rightToeBasePull


class ExtraPlugOperator(
    CompoundPlugOperator["ExtraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pullIterationCount", "pic"),
    )

    pullIterationCount = FloatField(default_value=10.0, min_value=0.0, max_value=30.0)
    pic = pullIterationCount


class ExtraAttrOperator(
    CompoundAttrOperator[ExtraPlugOperator]
):
    __slots__ = ()

    pullIterationCount = FloatField(default_value=10.0, min_value=0.0, max_value=30.0)
    pic = pullIterationCount


class ExtraField(
    CompoundField[ExtraAttrOperator, ExtraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtraAttrOperator
    PLUG_CLS = ExtraPlugOperator

    pullIterationCount = FloatField(default_value=10.0, min_value=0.0, max_value=30.0)
    pic = pullIterationCount


class StiffnessPlugOperator(
    CompoundPlugOperator["StiffnessAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("neckStiffness", "nst"),
        ("leftShoulderStiffness", "rlco"),
        ("leftArmStiffness", "rle"),
        ("leftElbowMaxExtension", "mle"),
        ("leftElbowCompressionFactor", "cle"),
        ("rightShoulderStiffness", "rrc"),
        ("rightArmStiffness", "rre"),
        ("rightElbowMaxExtension", "mre"),
        ("rightElbowCompressionFactor", "cre"),
        ("hipsEnforceGravity", "egr"),
        ("chestStiffness", "rco"),
        ("spineStiffness", "sst"),
        ("hipsStiffness", "rho"),
        ("leftKneeMaxExtension", "mlk"),
        ("leftLegStiffness", "rlk"),
        ("leftKneeCompressionFactor", "clk"),
        ("rightLegStiffness", "rrk"),
        ("rightKneeMaxExtension", "mrk"),
        ("rightKneeCompressionFactor", "crk"),
    )

    neckStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    nst = neckStiffness

    leftShoulderStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rlco = leftShoulderStiffness

    leftArmStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rle = leftArmStiffness

    leftElbowMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mle = leftElbowMaxExtension

    leftElbowCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    cle = leftElbowCompressionFactor

    rightShoulderStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rrc = rightShoulderStiffness

    rightArmStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rre = rightArmStiffness

    rightElbowMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mre = rightElbowMaxExtension

    rightElbowCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    cre = rightElbowCompressionFactor

    hipsEnforceGravity = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    egr = hipsEnforceGravity

    chestStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rco = chestStiffness

    spineStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    sst = spineStiffness

    hipsStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rho = hipsStiffness

    leftKneeMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mlk = leftKneeMaxExtension

    leftLegStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rlk = leftLegStiffness

    leftKneeCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    clk = leftKneeCompressionFactor

    rightLegStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rrk = rightLegStiffness

    rightKneeMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mrk = rightKneeMaxExtension

    rightKneeCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    crk = rightKneeCompressionFactor


class StiffnessAttrOperator(
    CompoundAttrOperator[StiffnessPlugOperator]
):
    __slots__ = ()

    neckStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    nst = neckStiffness

    leftShoulderStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rlco = leftShoulderStiffness

    leftArmStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rle = leftArmStiffness

    leftElbowMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mle = leftElbowMaxExtension

    leftElbowCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    cle = leftElbowCompressionFactor

    rightShoulderStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rrc = rightShoulderStiffness

    rightArmStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rre = rightArmStiffness

    rightElbowMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mre = rightElbowMaxExtension

    rightElbowCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    cre = rightElbowCompressionFactor

    hipsEnforceGravity = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    egr = hipsEnforceGravity

    chestStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rco = chestStiffness

    spineStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    sst = spineStiffness

    hipsStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rho = hipsStiffness

    leftKneeMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mlk = leftKneeMaxExtension

    leftLegStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rlk = leftLegStiffness

    leftKneeCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    clk = leftKneeCompressionFactor

    rightLegStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rrk = rightLegStiffness

    rightKneeMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mrk = rightKneeMaxExtension

    rightKneeCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    crk = rightKneeCompressionFactor


class StiffnessField(
    CompoundField[StiffnessAttrOperator, StiffnessPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StiffnessAttrOperator
    PLUG_CLS = StiffnessPlugOperator

    neckStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    nst = neckStiffness

    leftShoulderStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rlco = leftShoulderStiffness

    leftArmStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rle = leftArmStiffness

    leftElbowMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mle = leftElbowMaxExtension

    leftElbowCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    cle = leftElbowCompressionFactor

    rightShoulderStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rrc = rightShoulderStiffness

    rightArmStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rre = rightArmStiffness

    rightElbowMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mre = rightElbowMaxExtension

    rightElbowCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    cre = rightElbowCompressionFactor

    hipsEnforceGravity = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    egr = hipsEnforceGravity

    chestStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rco = chestStiffness

    spineStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    sst = spineStiffness

    hipsStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rho = hipsStiffness

    leftKneeMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mlk = leftKneeMaxExtension

    leftLegStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rlk = leftLegStiffness

    leftKneeCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    clk = leftKneeCompressionFactor

    rightLegStiffness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rrk = rightLegStiffness

    rightKneeMaxExtension = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mrk = rightKneeMaxExtension

    rightKneeCompressionFactor = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    crk = rightKneeCompressionFactor


class KillPitchPlugOperator(
    CompoundPlugOperator["KillPitchAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leftElbowKillPitch", "lek"),
        ("rightElbowKillPitch", "rek"),
        ("leftKneeKillPitch", "lkk"),
        ("rightKneeKillPitch", "rkk"),
    )

    leftElbowKillPitch = BoolField(default_value=False)
    lek = leftElbowKillPitch

    rightElbowKillPitch = BoolField(default_value=False)
    rek = rightElbowKillPitch

    leftKneeKillPitch = BoolField(default_value=False)
    lkk = leftKneeKillPitch

    rightKneeKillPitch = BoolField(default_value=False)
    rkk = rightKneeKillPitch


class KillPitchAttrOperator(
    CompoundAttrOperator[KillPitchPlugOperator]
):
    __slots__ = ()

    leftElbowKillPitch = BoolField(default_value=False)
    lek = leftElbowKillPitch

    rightElbowKillPitch = BoolField(default_value=False)
    rek = rightElbowKillPitch

    leftKneeKillPitch = BoolField(default_value=False)
    lkk = leftKneeKillPitch

    rightKneeKillPitch = BoolField(default_value=False)
    rkk = rightKneeKillPitch


class KillPitchField(
    CompoundField[KillPitchAttrOperator, KillPitchPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KillPitchAttrOperator
    PLUG_CLS = KillPitchPlugOperator

    leftElbowKillPitch = BoolField(default_value=False)
    lek = leftElbowKillPitch

    rightElbowKillPitch = BoolField(default_value=False)
    rek = rightElbowKillPitch

    leftKneeKillPitch = BoolField(default_value=False)
    lkk = leftKneeKillPitch

    rightKneeKillPitch = BoolField(default_value=False)
    rkk = rightKneeKillPitch


class RollExtractionPlugOperator(
    CompoundPlugOperator["RollExtractionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rollExtractionMode", "rem"),
        ("leftArmRollMode", "larm"),
        ("leftArmRoll", "lar"),
        ("leftForeArmRollMode", "lfrm"),
        ("leftForeArmRoll", "lfr"),
        ("rightArmRollMode", "rarm"),
        ("rightArmRoll", "rar"),
        ("rightForeArmRollMode", "rfrm"),
        ("rightForeArmRoll", "rfr"),
        ("leftUpLegRollMode", "lurm"),
        ("leftUpLegRoll", "lur"),
        ("leftLegRollMode", "llrm"),
        ("leftLegRoll", "llr"),
        ("rightUpLegRollMode", "rurm"),
        ("rightUpLegRoll", "rur"),
        ("rightLegRollMode", "rlrm"),
        ("rightLegRoll", "rlro"),
    )

    rollExtractionMode = RollExtractionModeEnumField(default_value=0)
    rem = rollExtractionMode

    leftArmRollMode = BoolField(default_value=False)
    larm = leftArmRollMode

    leftArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    lar = leftArmRoll

    leftForeArmRollMode = BoolField(default_value=False)
    lfrm = leftForeArmRollMode

    leftForeArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    lfr = leftForeArmRoll

    rightArmRollMode = BoolField(default_value=False)
    rarm = rightArmRollMode

    rightArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rar = rightArmRoll

    rightForeArmRollMode = BoolField(default_value=False)
    rfrm = rightForeArmRollMode

    rightForeArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rfr = rightForeArmRoll

    leftUpLegRollMode = BoolField(default_value=False)
    lurm = leftUpLegRollMode

    leftUpLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    lur = leftUpLegRoll

    leftLegRollMode = BoolField(default_value=False)
    llrm = leftLegRollMode

    leftLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    llr = leftLegRoll

    rightUpLegRollMode = BoolField(default_value=False)
    rurm = rightUpLegRollMode

    rightUpLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rur = rightUpLegRoll

    rightLegRollMode = BoolField(default_value=False)
    rlrm = rightLegRollMode

    rightLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rlro = rightLegRoll


class RollExtractionAttrOperator(
    CompoundAttrOperator[RollExtractionPlugOperator]
):
    __slots__ = ()

    rollExtractionMode = RollExtractionModeEnumField(default_value=0)
    rem = rollExtractionMode

    leftArmRollMode = BoolField(default_value=False)
    larm = leftArmRollMode

    leftArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    lar = leftArmRoll

    leftForeArmRollMode = BoolField(default_value=False)
    lfrm = leftForeArmRollMode

    leftForeArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    lfr = leftForeArmRoll

    rightArmRollMode = BoolField(default_value=False)
    rarm = rightArmRollMode

    rightArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rar = rightArmRoll

    rightForeArmRollMode = BoolField(default_value=False)
    rfrm = rightForeArmRollMode

    rightForeArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rfr = rightForeArmRoll

    leftUpLegRollMode = BoolField(default_value=False)
    lurm = leftUpLegRollMode

    leftUpLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    lur = leftUpLegRoll

    leftLegRollMode = BoolField(default_value=False)
    llrm = leftLegRollMode

    leftLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    llr = leftLegRoll

    rightUpLegRollMode = BoolField(default_value=False)
    rurm = rightUpLegRollMode

    rightUpLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rur = rightUpLegRoll

    rightLegRollMode = BoolField(default_value=False)
    rlrm = rightLegRollMode

    rightLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rlro = rightLegRoll


class RollExtractionField(
    CompoundField[RollExtractionAttrOperator, RollExtractionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RollExtractionAttrOperator
    PLUG_CLS = RollExtractionPlugOperator

    rollExtractionMode = RollExtractionModeEnumField(default_value=0)
    rem = rollExtractionMode

    leftArmRollMode = BoolField(default_value=False)
    larm = leftArmRollMode

    leftArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    lar = leftArmRoll

    leftForeArmRollMode = BoolField(default_value=False)
    lfrm = leftForeArmRollMode

    leftForeArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    lfr = leftForeArmRoll

    rightArmRollMode = BoolField(default_value=False)
    rarm = rightArmRollMode

    rightArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rar = rightArmRoll

    rightForeArmRollMode = BoolField(default_value=False)
    rfrm = rightForeArmRollMode

    rightForeArmRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rfr = rightForeArmRoll

    leftUpLegRollMode = BoolField(default_value=False)
    lurm = leftUpLegRollMode

    leftUpLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    lur = leftUpLegRoll

    leftLegRollMode = BoolField(default_value=False)
    llrm = leftLegRollMode

    leftLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    llr = leftLegRoll

    rightUpLegRollMode = BoolField(default_value=False)
    rurm = rightUpLegRollMode

    rightUpLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rur = rightUpLegRoll

    rightLegRollMode = BoolField(default_value=False)
    rlrm = rightLegRollMode

    rightLegRoll = FloatField(default_value=0.6000000238418579, min_value=0.0, max_value=1.0)
    rlro = rightLegRoll
