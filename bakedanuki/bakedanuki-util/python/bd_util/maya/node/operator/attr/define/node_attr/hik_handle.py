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
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField


class Solving_postureTypeEnumPlugOperator(
    EnumPlugOperator["Solving_postureTypeEnumAttrOperator"]
):
    __slots__ = ()

    BIPED = 0
    QUADRUPED = 1


class Solving_postureTypeEnumAttrOperator(
    EnumAttrOperator[Solving_postureTypeEnumPlugOperator]
):
    __slots__ = ()

    BIPED = 0
    QUADRUPED = 1

    NAME_MAP = {
        BIPED: "biped",
        QUADRUPED: "quadruped",
    }


class Solving_postureTypeEnumField(
    EnumField[
        Solving_postureTypeEnumAttrOperator,
        Solving_postureTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Solving_postureTypeEnumAttrOperator
    PLUG_CLS = Solving_postureTypeEnumPlugOperator


class Solving_hipTranslationModeEnumPlugOperator(
    EnumPlugOperator["Solving_hipTranslationModeEnumAttrOperator"]
):
    __slots__ = ()

    WORLD_RIGID = 0
    BODY_RIGID = 1


class Solving_hipTranslationModeEnumAttrOperator(
    EnumAttrOperator[Solving_hipTranslationModeEnumPlugOperator]
):
    __slots__ = ()

    WORLD_RIGID = 0
    BODY_RIGID = 1

    NAME_MAP = {
        WORLD_RIGID: "world rigid",
        BODY_RIGID: "body rigid",
    }


class Solving_hipTranslationModeEnumField(
    EnumField[
        Solving_hipTranslationModeEnumAttrOperator,
        Solving_hipTranslationModeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Solving_hipTranslationModeEnumAttrOperator
    PLUG_CLS = Solving_hipTranslationModeEnumPlugOperator


class HandsFloorContactSetup_handsFloorPivotEnumPlugOperator(
    EnumPlugOperator["HandsFloorContactSetup_handsFloorPivotEnumAttrOperator"]
):
    __slots__ = ()

    AUTO = 0
    WRIST = 1
    FINGERS = 2


class HandsFloorContactSetup_handsFloorPivotEnumAttrOperator(
    EnumAttrOperator[HandsFloorContactSetup_handsFloorPivotEnumPlugOperator]
):
    __slots__ = ()

    AUTO = 0
    WRIST = 1
    FINGERS = 2

    NAME_MAP = {
        AUTO: "auto",
        WRIST: "wrist",
        FINGERS: "fingers",
    }


class HandsFloorContactSetup_handsFloorPivotEnumField(
    EnumField[
        HandsFloorContactSetup_handsFloorPivotEnumAttrOperator,
        HandsFloorContactSetup_handsFloorPivotEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = HandsFloorContactSetup_handsFloorPivotEnumAttrOperator
    PLUG_CLS = HandsFloorContactSetup_handsFloorPivotEnumPlugOperator


class HandsFloorContactSetup_handsContactTypeEnumPlugOperator(
    EnumPlugOperator["HandsFloorContactSetup_handsContactTypeEnumAttrOperator"]
):
    __slots__ = ()

    NORMAL = 0
    WRIST = 1
    FINGER_BASE = 2
    HOOF = 3


class HandsFloorContactSetup_handsContactTypeEnumAttrOperator(
    EnumAttrOperator[HandsFloorContactSetup_handsContactTypeEnumPlugOperator]
):
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


class HandsFloorContactSetup_handsContactTypeEnumField(
    EnumField[
        HandsFloorContactSetup_handsContactTypeEnumAttrOperator,
        HandsFloorContactSetup_handsContactTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = HandsFloorContactSetup_handsContactTypeEnumAttrOperator
    PLUG_CLS = HandsFloorContactSetup_handsContactTypeEnumPlugOperator


class FeetFloorContactSetup_feetFloorPivotEnumPlugOperator(
    EnumPlugOperator["FeetFloorContactSetup_feetFloorPivotEnumAttrOperator"]
):
    __slots__ = ()

    AUTO = 0
    ANKLE = 1
    TOES = 2


class FeetFloorContactSetup_feetFloorPivotEnumAttrOperator(
    EnumAttrOperator[FeetFloorContactSetup_feetFloorPivotEnumPlugOperator]
):
    __slots__ = ()

    AUTO = 0
    ANKLE = 1
    TOES = 2

    NAME_MAP = {
        AUTO: "auto",
        ANKLE: "ankle",
        TOES: "toes",
    }


class FeetFloorContactSetup_feetFloorPivotEnumField(
    EnumField[
        FeetFloorContactSetup_feetFloorPivotEnumAttrOperator,
        FeetFloorContactSetup_feetFloorPivotEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FeetFloorContactSetup_feetFloorPivotEnumAttrOperator
    PLUG_CLS = FeetFloorContactSetup_feetFloorPivotEnumPlugOperator


class FeetFloorContactSetup_feetContactTypeEnumPlugOperator(
    EnumPlugOperator["FeetFloorContactSetup_feetContactTypeEnumAttrOperator"]
):
    __slots__ = ()

    NORMAL = 0
    ANKLE = 1
    TOE_BASE = 2
    HOOF = 3


class FeetFloorContactSetup_feetContactTypeEnumAttrOperator(
    EnumAttrOperator[FeetFloorContactSetup_feetContactTypeEnumPlugOperator]
):
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


class FeetFloorContactSetup_feetContactTypeEnumField(
    EnumField[
        FeetFloorContactSetup_feetContactTypeEnumAttrOperator,
        FeetFloorContactSetup_feetContactTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FeetFloorContactSetup_feetContactTypeEnumAttrOperator
    PLUG_CLS = FeetFloorContactSetup_feetContactTypeEnumPlugOperator


class FingersFloorContactSetup_fingersContactTypeEnumPlugOperator(
    EnumPlugOperator[
        "FingersFloorContactSetup_fingersContactTypeEnumAttrOperator"
    ]
):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_MINUS_SPREAD = 2


class FingersFloorContactSetup_fingersContactTypeEnumAttrOperator(
    EnumAttrOperator[
        FingersFloorContactSetup_fingersContactTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_MINUS_SPREAD = 2

    NAME_MAP = {
        STICKY: "sticky",
        SPREAD: "spread",
        STICKY_MINUS_SPREAD: "sticky-spread",
    }


class FingersFloorContactSetup_fingersContactTypeEnumField(
    EnumField[
        FingersFloorContactSetup_fingersContactTypeEnumAttrOperator,
        FingersFloorContactSetup_fingersContactTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FingersFloorContactSetup_fingersContactTypeEnumAttrOperator
    PLUG_CLS = FingersFloorContactSetup_fingersContactTypeEnumPlugOperator


class ToesFloorContactSetup_toesContactTypeEnumPlugOperator(
    EnumPlugOperator["ToesFloorContactSetup_toesContactTypeEnumAttrOperator"]
):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_MINUS_SPREAD = 2


class ToesFloorContactSetup_toesContactTypeEnumAttrOperator(
    EnumAttrOperator[ToesFloorContactSetup_toesContactTypeEnumPlugOperator]
):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_MINUS_SPREAD = 2

    NAME_MAP = {
        STICKY: "sticky",
        SPREAD: "spread",
        STICKY_MINUS_SPREAD: "sticky-spread",
    }


class ToesFloorContactSetup_toesContactTypeEnumField(
    EnumField[
        ToesFloorContactSetup_toesContactTypeEnumAttrOperator,
        ToesFloorContactSetup_toesContactTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ToesFloorContactSetup_toesContactTypeEnumAttrOperator
    PLUG_CLS = ToesFloorContactSetup_toesContactTypeEnumPlugOperator


class RollExtraction_rollExtractionModeEnumPlugOperator(
    EnumPlugOperator["RollExtraction_rollExtractionModeEnumAttrOperator"]
):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1


class RollExtraction_rollExtractionModeEnumAttrOperator(
    EnumAttrOperator[RollExtraction_rollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1

    NAME_MAP = {
        RELATIVE: "relative",
        ABSOLUTE: "absolute",
    }


class RollExtraction_rollExtractionModeEnumField(
    EnumField[
        RollExtraction_rollExtractionModeEnumAttrOperator,
        RollExtraction_rollExtractionModeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = RollExtraction_rollExtractionModeEnumAttrOperator
    PLUG_CLS = RollExtraction_rollExtractionModeEnumPlugOperator


class SolvingPlugOperator(CompoundPlugOperator["SolvingAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("postureType", "pt"),
        ("expertMode", "exp"),
        ("realisticShoulderSolving", "rss"),
        ("solveFingers", "sf"),
        ("hipTranslationMode", "htm"),
    )

    postureType = Solving_postureTypeEnumField(default_value=0)
    pt = postureType

    expertMode = BoolField(default_value=False)
    exp = expertMode

    realisticShoulderSolving = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    rss = realisticShoulderSolving

    solveFingers = BoolField(default_value=True)
    sf = solveFingers

    hipTranslationMode = Solving_hipTranslationModeEnumField(default_value=0)
    htm = hipTranslationMode


class SolvingAttrOperator(CompoundAttrOperator[SolvingPlugOperator]):
    __slots__ = ()

    postureType = Solving_postureTypeEnumField(default_value=0)
    pt = postureType

    expertMode = BoolField(default_value=False)
    exp = expertMode

    realisticShoulderSolving = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    rss = realisticShoulderSolving

    solveFingers = BoolField(default_value=True)
    sf = solveFingers

    hipTranslationMode = Solving_hipTranslationModeEnumField(default_value=0)
    htm = hipTranslationMode


class SolvingField(CompoundField[SolvingAttrOperator, SolvingPlugOperator]):
    __slots__ = ()

    ATTR_CLS = SolvingAttrOperator
    PLUG_CLS = SolvingPlugOperator

    postureType = Solving_postureTypeEnumField(default_value=0)
    pt = postureType

    expertMode = BoolField(default_value=False)
    exp = expertMode

    realisticShoulderSolving = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    rss = realisticShoulderSolving

    solveFingers = BoolField(default_value=True)
    sf = solveFingers

    hipTranslationMode = Solving_hipTranslationModeEnumField(default_value=0)
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

    handsFloorPivot = HandsFloorContactSetup_handsFloorPivotEnumField(
        default_value=0
    )
    hfp = handsFloorPivot

    handsContactType = HandsFloorContactSetup_handsContactTypeEnumField(
        default_value=0
    )
    hct = handsContactType

    handsContactStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    hcs = handsContactStiffness


class HandsFloorContactSetupAttrOperator(
    CompoundAttrOperator[HandsFloorContactSetupPlugOperator]
):
    __slots__ = ()

    handsFloorPivot = HandsFloorContactSetup_handsFloorPivotEnumField(
        default_value=0
    )
    hfp = handsFloorPivot

    handsContactType = HandsFloorContactSetup_handsContactTypeEnumField(
        default_value=0
    )
    hct = handsContactType

    handsContactStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    hcs = handsContactStiffness


class HandsFloorContactSetupField(
    CompoundField[
        HandsFloorContactSetupAttrOperator, HandsFloorContactSetupPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = HandsFloorContactSetupAttrOperator
    PLUG_CLS = HandsFloorContactSetupPlugOperator

    handsFloorPivot = HandsFloorContactSetup_handsFloorPivotEnumField(
        default_value=0
    )
    hfp = handsFloorPivot

    handsContactType = HandsFloorContactSetup_handsContactTypeEnumField(
        default_value=0
    )
    hct = handsContactType

    handsContactStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
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

    handHeight = FloatField(
        default_value=7.5, min_value=0.0, max_value=10000.0
    )
    hh = handHeight

    handBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    hb = handBack

    handMiddle = FloatField(
        default_value=13.0, min_value=0.0, max_value=10000.0
    )
    hm = handMiddle

    handFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    hf = handFront

    handInSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    his = handInSide

    handOutSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    hos = handOutSide


class ContactsPositionAttrOperator(
    CompoundAttrOperator[ContactsPositionPlugOperator]
):
    __slots__ = ()

    handHeight = FloatField(
        default_value=7.5, min_value=0.0, max_value=10000.0
    )
    hh = handHeight

    handBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    hb = handBack

    handMiddle = FloatField(
        default_value=13.0, min_value=0.0, max_value=10000.0
    )
    hm = handMiddle

    handFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    hf = handFront

    handInSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    his = handInSide

    handOutSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    hos = handOutSide


class ContactsPositionField(
    CompoundField[ContactsPositionAttrOperator, ContactsPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ContactsPositionAttrOperator
    PLUG_CLS = ContactsPositionPlugOperator

    handHeight = FloatField(
        default_value=7.5, min_value=0.0, max_value=10000.0
    )
    hh = handHeight

    handBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    hb = handBack

    handMiddle = FloatField(
        default_value=13.0, min_value=0.0, max_value=10000.0
    )
    hm = handMiddle

    handFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    hf = handFront

    handInSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    his = handInSide

    handOutSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
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

    feetFloorPivot = FeetFloorContactSetup_feetFloorPivotEnumField(
        default_value=0
    )
    fpv = feetFloorPivot

    feetContactType = FeetFloorContactSetup_feetContactTypeEnumField(
        default_value=0
    )
    fct = feetContactType

    feetContactStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    fcs = feetContactStiffness


class FeetFloorContactSetupAttrOperator(
    CompoundAttrOperator[FeetFloorContactSetupPlugOperator]
):
    __slots__ = ()

    feetFloorPivot = FeetFloorContactSetup_feetFloorPivotEnumField(
        default_value=0
    )
    fpv = feetFloorPivot

    feetContactType = FeetFloorContactSetup_feetContactTypeEnumField(
        default_value=0
    )
    fct = feetContactType

    feetContactStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    fcs = feetContactStiffness


class FeetFloorContactSetupField(
    CompoundField[
        FeetFloorContactSetupAttrOperator, FeetFloorContactSetupPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FeetFloorContactSetupAttrOperator
    PLUG_CLS = FeetFloorContactSetupPlugOperator

    feetFloorPivot = FeetFloorContactSetup_feetFloorPivotEnumField(
        default_value=0
    )
    fpv = feetFloorPivot

    feetContactType = FeetFloorContactSetup_feetContactTypeEnumField(
        default_value=0
    )
    fct = feetContactType

    feetContactStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
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

    footHeight = FloatField(
        default_value=7.5, min_value=0.0, max_value=10000.0
    )
    fh = footHeight

    footBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    fra = footBack

    footMiddle = FloatField(
        default_value=13.0, min_value=0.0, max_value=10000.0
    )
    fma = footMiddle

    footFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    ffm = footFront

    footInSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    fia = footInSide

    footOutSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    foa = footOutSide


class FeetContactPositionAttrOperator(
    CompoundAttrOperator[FeetContactPositionPlugOperator]
):
    __slots__ = ()

    footHeight = FloatField(
        default_value=7.5, min_value=0.0, max_value=10000.0
    )
    fh = footHeight

    footBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    fra = footBack

    footMiddle = FloatField(
        default_value=13.0, min_value=0.0, max_value=10000.0
    )
    fma = footMiddle

    footFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    ffm = footFront

    footInSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    fia = footInSide

    footOutSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    foa = footOutSide


class FeetContactPositionField(
    CompoundField[
        FeetContactPositionAttrOperator, FeetContactPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FeetContactPositionAttrOperator
    PLUG_CLS = FeetContactPositionPlugOperator

    footHeight = FloatField(
        default_value=7.5, min_value=0.0, max_value=10000.0
    )
    fh = footHeight

    footBack = FloatField(default_value=4.5, min_value=0.0, max_value=10000.0)
    fra = footBack

    footMiddle = FloatField(
        default_value=13.0, min_value=0.0, max_value=10000.0
    )
    fma = footMiddle

    footFront = FloatField(default_value=7.0, min_value=0.0, max_value=10000.0)
    ffm = footFront

    footInSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    fia = footInSide

    footOutSide = FloatField(
        default_value=5.0, min_value=0.0, max_value=10000.0
    )
    foa = footOutSide


class FingersFloorContactSetupPlugOperator(
    CompoundPlugOperator["FingersFloorContactSetupAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fingersContactType", "fcm"),
        ("fingersContactRollStiffness", "hcr"),
    )

    fingersContactType = FingersFloorContactSetup_fingersContactTypeEnumField(
        default_value=1
    )
    fcm = fingersContactType

    fingersContactRollStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    hcr = fingersContactRollStiffness


class FingersFloorContactSetupAttrOperator(
    CompoundAttrOperator[FingersFloorContactSetupPlugOperator]
):
    __slots__ = ()

    fingersContactType = FingersFloorContactSetup_fingersContactTypeEnumField(
        default_value=1
    )
    fcm = fingersContactType

    fingersContactRollStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    hcr = fingersContactRollStiffness


class FingersFloorContactSetupField(
    CompoundField[
        FingersFloorContactSetupAttrOperator,
        FingersFloorContactSetupPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FingersFloorContactSetupAttrOperator
    PLUG_CLS = FingersFloorContactSetupPlugOperator

    fingersContactType = FingersFloorContactSetup_fingersContactTypeEnumField(
        default_value=1
    )
    fcm = fingersContactType

    fingersContactRollStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
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

    leftHandThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    ltt = leftHandThumbTip

    leftHandIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lit = leftHandIndexTip

    leftHandMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lmt = leftHandMiddleTip

    leftHandRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lrt = leftHandRingTip

    leftHandPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lpt = leftHandPinkyTip

    leftHandExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lxt = leftHandExtraFingerTip

    rightHandThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rtt = rightHandThumbTip

    rightHandIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rit = rightHandIndexTip

    rightHandMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rmt = rightHandMiddleTip

    rightHandRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rrt = rightHandRingTip

    rightHandPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rpp = rightHandPinkyTip

    rightHandExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rxt = rightHandExtraFingerTip


class FingerTipsSizesAttrOperator(
    CompoundAttrOperator[FingerTipsSizesPlugOperator]
):
    __slots__ = ()

    leftHandThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    ltt = leftHandThumbTip

    leftHandIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lit = leftHandIndexTip

    leftHandMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lmt = leftHandMiddleTip

    leftHandRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lrt = leftHandRingTip

    leftHandPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lpt = leftHandPinkyTip

    leftHandExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lxt = leftHandExtraFingerTip

    rightHandThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rtt = rightHandThumbTip

    rightHandIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rit = rightHandIndexTip

    rightHandMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rmt = rightHandMiddleTip

    rightHandRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rrt = rightHandRingTip

    rightHandPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rpp = rightHandPinkyTip

    rightHandExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rxt = rightHandExtraFingerTip


class FingerTipsSizesField(
    CompoundField[FingerTipsSizesAttrOperator, FingerTipsSizesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FingerTipsSizesAttrOperator
    PLUG_CLS = FingerTipsSizesPlugOperator

    leftHandThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    ltt = leftHandThumbTip

    leftHandIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lit = leftHandIndexTip

    leftHandMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lmt = leftHandMiddleTip

    leftHandRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lrt = leftHandRingTip

    leftHandPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lpt = leftHandPinkyTip

    leftHandExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    lxt = leftHandExtraFingerTip

    rightHandThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rtt = rightHandThumbTip

    rightHandIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rit = rightHandIndexTip

    rightHandMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rmt = rightHandMiddleTip

    rightHandRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rrt = rightHandRingTip

    rightHandPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rpp = rightHandPinkyTip

    rightHandExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    rxt = rightHandExtraFingerTip


class ToesFloorContactSetupPlugOperator(
    CompoundPlugOperator["ToesFloorContactSetupAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("toesContactType", "tct"),
        ("toesContactRollStiffness", "fcr"),
    )

    toesContactType = ToesFloorContactSetup_toesContactTypeEnumField(
        default_value=1
    )
    tct = toesContactType

    toesContactRollStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    fcr = toesContactRollStiffness


class ToesFloorContactSetupAttrOperator(
    CompoundAttrOperator[ToesFloorContactSetupPlugOperator]
):
    __slots__ = ()

    toesContactType = ToesFloorContactSetup_toesContactTypeEnumField(
        default_value=1
    )
    tct = toesContactType

    toesContactRollStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    fcr = toesContactRollStiffness


class ToesFloorContactSetupField(
    CompoundField[
        ToesFloorContactSetupAttrOperator, ToesFloorContactSetupPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ToesFloorContactSetupAttrOperator
    PLUG_CLS = ToesFloorContactSetupPlugOperator

    toesContactType = ToesFloorContactSetup_toesContactTypeEnumField(
        default_value=1
    )
    tct = toesContactType

    toesContactRollStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
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

    leftFootThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    ttl = leftFootThumbTip

    leftFootIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    til = leftFootIndexTip

    leftFootMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tml = leftFootMiddleTip

    leftFootRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    trl = leftFootRingTip

    leftFootPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tpl = leftFootPinkyTip

    leftFootExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    txl = leftFootExtraFingerTip

    rightFootThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    ttr = rightFootThumbTip

    rightFootIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tir = rightFootIndexTip

    rightFootMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tmr = rightFootMiddleTip

    rightFootRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    trr = rightFootRingTip

    rightFootPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tpr = rightFootPinkyTip

    rightFootExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    txr = rightFootExtraFingerTip


class ToeTipsSizesAttrOperator(CompoundAttrOperator[ToeTipsSizesPlugOperator]):
    __slots__ = ()

    leftFootThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    ttl = leftFootThumbTip

    leftFootIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    til = leftFootIndexTip

    leftFootMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tml = leftFootMiddleTip

    leftFootRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    trl = leftFootRingTip

    leftFootPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tpl = leftFootPinkyTip

    leftFootExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    txl = leftFootExtraFingerTip

    rightFootThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    ttr = rightFootThumbTip

    rightFootIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tir = rightFootIndexTip

    rightFootMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tmr = rightFootMiddleTip

    rightFootRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    trr = rightFootRingTip

    rightFootPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tpr = rightFootPinkyTip

    rightFootExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    txr = rightFootExtraFingerTip


class ToeTipsSizesField(
    CompoundField[ToeTipsSizesAttrOperator, ToeTipsSizesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ToeTipsSizesAttrOperator
    PLUG_CLS = ToeTipsSizesPlugOperator

    leftFootThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    ttl = leftFootThumbTip

    leftFootIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    til = leftFootIndexTip

    leftFootMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tml = leftFootMiddleTip

    leftFootRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    trl = leftFootRingTip

    leftFootPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tpl = leftFootPinkyTip

    leftFootExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    txl = leftFootExtraFingerTip

    rightFootThumbTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    ttr = rightFootThumbTip

    rightFootIndexTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tir = rightFootIndexTip

    rightFootMiddleTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tmr = rightFootMiddleTip

    rightFootRingTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    trr = rightFootRingTip

    rightFootPinkyTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    tpr = rightFootPinkyTip

    rightFootExtraFingerTip = FloatField(
        default_value=0.5, min_value=0.0, max_value=1000.0
    )
    txr = rightFootExtraFingerTip


class HeadPlugOperator(CompoundPlugOperator["HeadAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("headPull", "phd"),)

    headPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    phd = headPull


class HeadAttrOperator(CompoundAttrOperator[HeadPlugOperator]):
    __slots__ = ()

    headPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    phd = headPull


class HeadField(CompoundField[HeadAttrOperator, HeadPlugOperator]):
    __slots__ = ()

    ATTR_CLS = HeadAttrOperator
    PLUG_CLS = HeadPlugOperator

    headPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    phd = headPull


class LeftArmPlugOperator(CompoundPlugOperator["LeftArmAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("leftElbowPull", "ple"),
        ("leftHandPullChest", "cpl"),
        ("leftHandPullHips", "plh"),
        ("leftFingerBasePull", "plb"),
    )

    leftElbowPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ple = leftElbowPull

    leftHandPullChest = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    cpl = leftHandPullChest

    leftHandPullHips = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    plh = leftHandPullHips

    leftFingerBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    plb = leftFingerBasePull


class LeftArmAttrOperator(CompoundAttrOperator[LeftArmPlugOperator]):
    __slots__ = ()

    leftElbowPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ple = leftElbowPull

    leftHandPullChest = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    cpl = leftHandPullChest

    leftHandPullHips = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    plh = leftHandPullHips

    leftFingerBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    plb = leftFingerBasePull


class LeftArmField(CompoundField[LeftArmAttrOperator, LeftArmPlugOperator]):
    __slots__ = ()

    ATTR_CLS = LeftArmAttrOperator
    PLUG_CLS = LeftArmPlugOperator

    leftElbowPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    ple = leftElbowPull

    leftHandPullChest = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    cpl = leftHandPullChest

    leftHandPullHips = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    plh = leftHandPullHips

    leftFingerBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    plb = leftFingerBasePull


class RightArmPlugOperator(CompoundPlugOperator["RightArmAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rightElbowPull", "pre"),
        ("rightHandPullChest", "cpr"),
        ("rightHandPullHips", "prh"),
        ("rightFingerBasePull", "prb"),
    )

    rightElbowPull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    pre = rightElbowPull

    rightHandPullChest = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    cpr = rightHandPullChest

    rightHandPullHips = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    prh = rightHandPullHips

    rightFingerBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    prb = rightFingerBasePull


class RightArmAttrOperator(CompoundAttrOperator[RightArmPlugOperator]):
    __slots__ = ()

    rightElbowPull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    pre = rightElbowPull

    rightHandPullChest = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    cpr = rightHandPullChest

    rightHandPullHips = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    prh = rightHandPullHips

    rightFingerBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    prb = rightFingerBasePull


class RightArmField(CompoundField[RightArmAttrOperator, RightArmPlugOperator]):
    __slots__ = ()

    ATTR_CLS = RightArmAttrOperator
    PLUG_CLS = RightArmPlugOperator

    rightElbowPull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    pre = rightElbowPull

    rightHandPullChest = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    cpr = rightHandPullChest

    rightHandPullHips = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    prh = rightHandPullHips

    rightFingerBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    prb = rightFingerBasePull


class ChestPlugOperator(CompoundPlugOperator["ChestAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("chestPull", "rcp"),)

    chestPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rcp = chestPull


class ChestAttrOperator(CompoundAttrOperator[ChestPlugOperator]):
    __slots__ = ()

    chestPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rcp = chestPull


class ChestField(CompoundField[ChestAttrOperator, ChestPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ChestAttrOperator
    PLUG_CLS = ChestPlugOperator

    chestPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rcp = chestPull


class HipsPlugOperator(CompoundPlugOperator["HipsAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("hipsPull", "chp"),)

    hipsPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    chp = hipsPull


class HipsAttrOperator(CompoundAttrOperator[HipsPlugOperator]):
    __slots__ = ()

    hipsPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    chp = hipsPull


class HipsField(CompoundField[HipsAttrOperator, HipsPlugOperator]):
    __slots__ = ()

    ATTR_CLS = HipsAttrOperator
    PLUG_CLS = HipsPlugOperator

    hipsPull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    chp = hipsPull


class LeftLegPlugOperator(CompoundPlugOperator["LeftLegAttrOperator"]):
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

    leftToeBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    plt = leftToeBasePull


class LeftLegAttrOperator(CompoundAttrOperator[LeftLegPlugOperator]):
    __slots__ = ()

    leftKneePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plk = leftKneePull

    leftFootPull = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    plf = leftFootPull

    leftToeBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    plt = leftToeBasePull


class LeftLegField(CompoundField[LeftLegAttrOperator, LeftLegPlugOperator]):
    __slots__ = ()

    ATTR_CLS = LeftLegAttrOperator
    PLUG_CLS = LeftLegPlugOperator

    leftKneePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    plk = leftKneePull

    leftFootPull = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    plf = leftFootPull

    leftToeBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    plt = leftToeBasePull


class RightLegPlugOperator(CompoundPlugOperator["RightLegAttrOperator"]):
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

    rightToeBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    prt = rightToeBasePull


class RightLegAttrOperator(CompoundAttrOperator[RightLegPlugOperator]):
    __slots__ = ()

    rightKneePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prk = rightKneePull

    rightFootPull = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    prf = rightFootPull

    rightToeBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    prt = rightToeBasePull


class RightLegField(CompoundField[RightLegAttrOperator, RightLegPlugOperator]):
    __slots__ = ()

    ATTR_CLS = RightLegAttrOperator
    PLUG_CLS = RightLegPlugOperator

    rightKneePull = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    prk = rightKneePull

    rightFootPull = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    prf = rightFootPull

    rightToeBasePull = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    prt = rightToeBasePull


class ExtraPlugOperator(CompoundPlugOperator["ExtraAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("pullIterationCount", "pic"),)

    pullIterationCount = FloatField(
        default_value=10.0, min_value=0.0, max_value=30.0
    )
    pic = pullIterationCount


class ExtraAttrOperator(CompoundAttrOperator[ExtraPlugOperator]):
    __slots__ = ()

    pullIterationCount = FloatField(
        default_value=10.0, min_value=0.0, max_value=30.0
    )
    pic = pullIterationCount


class ExtraField(CompoundField[ExtraAttrOperator, ExtraPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ExtraAttrOperator
    PLUG_CLS = ExtraPlugOperator

    pullIterationCount = FloatField(
        default_value=10.0, min_value=0.0, max_value=30.0
    )
    pic = pullIterationCount


class StiffnessPlugOperator(CompoundPlugOperator["StiffnessAttrOperator"]):
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

    leftShoulderStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rlco = leftShoulderStiffness

    leftArmStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rle = leftArmStiffness

    leftElbowMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mle = leftElbowMaxExtension

    leftElbowCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cle = leftElbowCompressionFactor

    rightShoulderStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rrc = rightShoulderStiffness

    rightArmStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rre = rightArmStiffness

    rightElbowMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mre = rightElbowMaxExtension

    rightElbowCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cre = rightElbowCompressionFactor

    hipsEnforceGravity = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    egr = hipsEnforceGravity

    chestStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    rco = chestStiffness

    spineStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    sst = spineStiffness

    hipsStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rho = hipsStiffness

    leftKneeMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mlk = leftKneeMaxExtension

    leftLegStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rlk = leftLegStiffness

    leftKneeCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    clk = leftKneeCompressionFactor

    rightLegStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rrk = rightLegStiffness

    rightKneeMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mrk = rightKneeMaxExtension

    rightKneeCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    crk = rightKneeCompressionFactor


class StiffnessAttrOperator(CompoundAttrOperator[StiffnessPlugOperator]):
    __slots__ = ()

    neckStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    nst = neckStiffness

    leftShoulderStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rlco = leftShoulderStiffness

    leftArmStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rle = leftArmStiffness

    leftElbowMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mle = leftElbowMaxExtension

    leftElbowCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cle = leftElbowCompressionFactor

    rightShoulderStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rrc = rightShoulderStiffness

    rightArmStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rre = rightArmStiffness

    rightElbowMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mre = rightElbowMaxExtension

    rightElbowCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cre = rightElbowCompressionFactor

    hipsEnforceGravity = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    egr = hipsEnforceGravity

    chestStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    rco = chestStiffness

    spineStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    sst = spineStiffness

    hipsStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rho = hipsStiffness

    leftKneeMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mlk = leftKneeMaxExtension

    leftLegStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rlk = leftLegStiffness

    leftKneeCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    clk = leftKneeCompressionFactor

    rightLegStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rrk = rightLegStiffness

    rightKneeMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mrk = rightKneeMaxExtension

    rightKneeCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    crk = rightKneeCompressionFactor


class StiffnessField(
    CompoundField[StiffnessAttrOperator, StiffnessPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StiffnessAttrOperator
    PLUG_CLS = StiffnessPlugOperator

    neckStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    nst = neckStiffness

    leftShoulderStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rlco = leftShoulderStiffness

    leftArmStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rle = leftArmStiffness

    leftElbowMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mle = leftElbowMaxExtension

    leftElbowCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cle = leftElbowCompressionFactor

    rightShoulderStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rrc = rightShoulderStiffness

    rightArmStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rre = rightArmStiffness

    rightElbowMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mre = rightElbowMaxExtension

    rightElbowCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    cre = rightElbowCompressionFactor

    hipsEnforceGravity = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    egr = hipsEnforceGravity

    chestStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    rco = chestStiffness

    spineStiffness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    sst = spineStiffness

    hipsStiffness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    rho = hipsStiffness

    leftKneeMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mlk = leftKneeMaxExtension

    leftLegStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rlk = leftLegStiffness

    leftKneeCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    clk = leftKneeCompressionFactor

    rightLegStiffness = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    rrk = rightLegStiffness

    rightKneeMaxExtension = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    mrk = rightKneeMaxExtension

    rightKneeCompressionFactor = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    crk = rightKneeCompressionFactor


class KillPitchPlugOperator(CompoundPlugOperator["KillPitchAttrOperator"]):
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


class KillPitchAttrOperator(CompoundAttrOperator[KillPitchPlugOperator]):
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

    rollExtractionMode = RollExtraction_rollExtractionModeEnumField(
        default_value=0
    )
    rem = rollExtractionMode

    leftArmRollMode = BoolField(default_value=False)
    larm = leftArmRollMode

    leftArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    lar = leftArmRoll

    leftForeArmRollMode = BoolField(default_value=False)
    lfrm = leftForeArmRollMode

    leftForeArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    lfr = leftForeArmRoll

    rightArmRollMode = BoolField(default_value=False)
    rarm = rightArmRollMode

    rightArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rar = rightArmRoll

    rightForeArmRollMode = BoolField(default_value=False)
    rfrm = rightForeArmRollMode

    rightForeArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rfr = rightForeArmRoll

    leftUpLegRollMode = BoolField(default_value=False)
    lurm = leftUpLegRollMode

    leftUpLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    lur = leftUpLegRoll

    leftLegRollMode = BoolField(default_value=False)
    llrm = leftLegRollMode

    leftLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    llr = leftLegRoll

    rightUpLegRollMode = BoolField(default_value=False)
    rurm = rightUpLegRollMode

    rightUpLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rur = rightUpLegRoll

    rightLegRollMode = BoolField(default_value=False)
    rlrm = rightLegRollMode

    rightLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rlro = rightLegRoll


class RollExtractionAttrOperator(
    CompoundAttrOperator[RollExtractionPlugOperator]
):
    __slots__ = ()

    rollExtractionMode = RollExtraction_rollExtractionModeEnumField(
        default_value=0
    )
    rem = rollExtractionMode

    leftArmRollMode = BoolField(default_value=False)
    larm = leftArmRollMode

    leftArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    lar = leftArmRoll

    leftForeArmRollMode = BoolField(default_value=False)
    lfrm = leftForeArmRollMode

    leftForeArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    lfr = leftForeArmRoll

    rightArmRollMode = BoolField(default_value=False)
    rarm = rightArmRollMode

    rightArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rar = rightArmRoll

    rightForeArmRollMode = BoolField(default_value=False)
    rfrm = rightForeArmRollMode

    rightForeArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rfr = rightForeArmRoll

    leftUpLegRollMode = BoolField(default_value=False)
    lurm = leftUpLegRollMode

    leftUpLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    lur = leftUpLegRoll

    leftLegRollMode = BoolField(default_value=False)
    llrm = leftLegRollMode

    leftLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    llr = leftLegRoll

    rightUpLegRollMode = BoolField(default_value=False)
    rurm = rightUpLegRollMode

    rightUpLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rur = rightUpLegRoll

    rightLegRollMode = BoolField(default_value=False)
    rlrm = rightLegRollMode

    rightLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rlro = rightLegRoll


class RollExtractionField(
    CompoundField[RollExtractionAttrOperator, RollExtractionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RollExtractionAttrOperator
    PLUG_CLS = RollExtractionPlugOperator

    rollExtractionMode = RollExtraction_rollExtractionModeEnumField(
        default_value=0
    )
    rem = rollExtractionMode

    leftArmRollMode = BoolField(default_value=False)
    larm = leftArmRollMode

    leftArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    lar = leftArmRoll

    leftForeArmRollMode = BoolField(default_value=False)
    lfrm = leftForeArmRollMode

    leftForeArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    lfr = leftForeArmRoll

    rightArmRollMode = BoolField(default_value=False)
    rarm = rightArmRollMode

    rightArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rar = rightArmRoll

    rightForeArmRollMode = BoolField(default_value=False)
    rfrm = rightForeArmRollMode

    rightForeArmRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rfr = rightForeArmRoll

    leftUpLegRollMode = BoolField(default_value=False)
    lurm = leftUpLegRollMode

    leftUpLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    lur = leftUpLegRoll

    leftLegRollMode = BoolField(default_value=False)
    llrm = leftLegRollMode

    leftLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    llr = leftLegRoll

    rightUpLegRollMode = BoolField(default_value=False)
    rurm = rightUpLegRollMode

    rightUpLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rur = rightUpLegRoll

    rightLegRollMode = BoolField(default_value=False)
    rlrm = rightLegRollMode

    rightLegRoll = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    rlro = rightLegRoll
