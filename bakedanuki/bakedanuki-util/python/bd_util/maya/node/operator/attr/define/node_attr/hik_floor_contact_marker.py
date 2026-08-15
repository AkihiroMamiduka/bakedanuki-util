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
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


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


class CompInstObjGroups_compObjectGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroups_compObjectGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compObjectGrpCompList", "cgcl"),
        ("compObjectGroupId", "cgid"),
    )

    compObjectGrpCompList = TypedField()
    cgcl = compObjectGrpCompList

    compObjectGroupId = LongField(default_value=0)
    cgid = compObjectGroupId


class CompInstObjGroups_compObjectGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroups_compObjectGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGrpCompList = TypedField()
    cgcl = compObjectGrpCompList

    compObjectGroupId = LongField(default_value=0)
    cgid = compObjectGroupId


class CompInstObjGroups_compObjectGroupsField(
    CompoundField[
        CompInstObjGroups_compObjectGroupsAttrOperator,
        CompInstObjGroups_compObjectGroupsPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CompInstObjGroups_compObjectGroupsAttrOperator
    PLUG_CLS = CompInstObjGroups_compObjectGroupsPlugOperator


class CompInstObjGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("compObjectGroups", "cog"),)

    compObjectGroups = CompInstObjGroups_compObjectGroupsField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGroups = CompInstObjGroups_compObjectGroupsField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsField(
    CompoundField[CompInstObjGroupsAttrOperator, CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompInstObjGroupsAttrOperator
    PLUG_CLS = CompInstObjGroupsPlugOperator


class ComponentTagsPlugOperator(
    CompoundPlugOperator["ComponentTagsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("componentTagName", "gtagnm"),
        ("componentTagContents", "gtagcmp"),
    )

    componentTagName = DataStringField()
    gtagnm = componentTagName

    componentTagContents = TypedField()
    gtagcmp = componentTagContents


class ComponentTagsAttrOperator(
    CompoundAttrOperator[ComponentTagsPlugOperator]
):
    __slots__ = ()

    componentTagName = DataStringField()
    gtagnm = componentTagName

    componentTagContents = TypedField()
    gtagcmp = componentTagContents


class ComponentTagsField(
    CompoundField[ComponentTagsAttrOperator, ComponentTagsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComponentTagsAttrOperator
    PLUG_CLS = ComponentTagsPlugOperator


class LocalPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["LocalPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localPositionX", "lpx"),
        ("localPositionY", "lpy"),
        ("localPositionZ", "lpz"),
    )

    localPositionX = DoubleLinearField(default_value=0.0)
    lpx = localPositionX

    localPositionY = DoubleLinearField(default_value=0.0)
    lpy = localPositionY

    localPositionZ = DoubleLinearField(default_value=0.0)
    lpz = localPositionZ


class LocalPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalPositionPlugOperator]
):
    __slots__ = ()

    localPositionX = DoubleLinearField(default_value=0.0)
    lpx = localPositionX

    localPositionY = DoubleLinearField(default_value=0.0)
    lpy = localPositionY

    localPositionZ = DoubleLinearField(default_value=0.0)
    lpz = localPositionZ


class LocalPositionField(
    DoubleLinear3CompoundBaseField[
        LocalPositionAttrOperator, LocalPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LocalPositionAttrOperator
    PLUG_CLS = LocalPositionPlugOperator

    localPositionX = DoubleLinearField(default_value=0.0)
    lpx = localPositionX

    localPositionY = DoubleLinearField(default_value=0.0)
    lpy = localPositionY

    localPositionZ = DoubleLinearField(default_value=0.0)
    lpz = localPositionZ


class WorldPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["WorldPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldPositionX", "wpx"),
        ("worldPositionY", "wpy"),
        ("worldPositionZ", "wpz"),
    )

    worldPositionX = DoubleLinearField(default_value=0.0, writable=False)
    wpx = worldPositionX

    worldPositionY = DoubleLinearField(default_value=0.0, writable=False)
    wpy = worldPositionY

    worldPositionZ = DoubleLinearField(default_value=0.0, writable=False)
    wpz = worldPositionZ


class WorldPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[WorldPositionPlugOperator]
):
    __slots__ = ()

    worldPositionX = DoubleLinearField(default_value=0.0, writable=False)
    wpx = worldPositionX

    worldPositionY = DoubleLinearField(default_value=0.0, writable=False)
    wpy = worldPositionY

    worldPositionZ = DoubleLinearField(default_value=0.0, writable=False)
    wpz = worldPositionZ


class WorldPositionField(
    DoubleLinear3CompoundBaseField[
        WorldPositionAttrOperator, WorldPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WorldPositionAttrOperator
    PLUG_CLS = WorldPositionPlugOperator


class LocalScalePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["LocalScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localScaleX", "lsx"),
        ("localScaleY", "lsy"),
        ("localScaleZ", "lsz"),
    )

    localScaleX = DoubleLinearField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleLinearField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleLinearField(default_value=1.0)
    lsz = localScaleZ


class LocalScaleAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalScalePlugOperator]
):
    __slots__ = ()

    localScaleX = DoubleLinearField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleLinearField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleLinearField(default_value=1.0)
    lsz = localScaleZ


class LocalScaleField(
    DoubleLinear3CompoundBaseField[
        LocalScaleAttrOperator, LocalScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LocalScaleAttrOperator
    PLUG_CLS = LocalScalePlugOperator

    localScaleX = DoubleLinearField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleLinearField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleLinearField(default_value=1.0)
    lsz = localScaleZ


class FloorContactsPlugOperator(
    CompoundPlugOperator["FloorContactsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("drawHandContact", "dhc"),
        ("handsContact", "hfc"),
        ("drawFeetContact", "dfc"),
        ("feetContact", "fec"),
        ("fingersContact", "fic"),
        ("toesContact", "tfc"),
    )

    drawHandContact = BoolField(default_value=True)
    dhc = drawHandContact

    handsContact = BoolField(default_value=False)
    hfc = handsContact

    drawFeetContact = BoolField(default_value=True)
    dfc = drawFeetContact

    feetContact = BoolField(default_value=False)
    fec = feetContact

    fingersContact = BoolField(default_value=False)
    fic = fingersContact

    toesContact = BoolField(default_value=False)
    tfc = toesContact


class FloorContactsAttrOperator(
    CompoundAttrOperator[FloorContactsPlugOperator]
):
    __slots__ = ()

    drawHandContact = BoolField(default_value=True)
    dhc = drawHandContact

    handsContact = BoolField(default_value=False)
    hfc = handsContact

    drawFeetContact = BoolField(default_value=True)
    dfc = drawFeetContact

    feetContact = BoolField(default_value=False)
    fec = feetContact

    fingersContact = BoolField(default_value=False)
    fic = fingersContact

    toesContact = BoolField(default_value=False)
    tfc = toesContact


class FloorContactsField(
    CompoundField[FloorContactsAttrOperator, FloorContactsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloorContactsAttrOperator
    PLUG_CLS = FloorContactsPlugOperator

    drawHandContact = BoolField(default_value=True)
    dhc = drawHandContact

    handsContact = BoolField(default_value=False)
    hfc = handsContact

    drawFeetContact = BoolField(default_value=True)
    dfc = drawFeetContact

    feetContact = BoolField(default_value=False)
    fec = feetContact

    fingersContact = BoolField(default_value=False)
    fic = fingersContact

    toesContact = BoolField(default_value=False)
    tfc = toesContact


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
