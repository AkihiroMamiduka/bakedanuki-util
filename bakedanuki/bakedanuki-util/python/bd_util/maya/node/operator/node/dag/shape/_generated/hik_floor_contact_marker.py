# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.hik_floor_contact_marker import (
    CompInstObjGroupsField,
    ComponentTagsField,
    ContactsPositionField,
    FeetContactPositionField,
    FeetFloorContactSetupField,
    FingersFloorContactSetupField,
    FloorContactsField,
    HandsFloorContactSetupField,
    LocalPositionField,
    LocalScaleField,
    ToesFloorContactSetupField,
    WorldPositionField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField


class GeneratedHikFloorContactMarker(Shape):
    __slots__ = ()

    NODE_TYPE = "hikFloorContactMarker"

    renderType = ShortField(default_value=0)
    rt = renderType

    renderVolume = BoolField(default_value=False)
    rv = renderVolume

    visibleFraction = FloatField(default_value=1.0)
    vf = visibleFraction

    hardwareFogMultiplier = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    hfm = hardwareFogMultiplier

    motionBlur = BoolField(default_value=True)
    mb = motionBlur

    visibleInReflections = BoolField(default_value=False)
    vir = visibleInReflections

    visibleInRefractions = BoolField(default_value=False)
    vif = visibleInRefractions

    castsShadows = BoolField(default_value=True)
    csh = castsShadows

    receiveShadows = BoolField(default_value=True)
    rcsh = receiveShadows

    asBackground = BoolField(default_value=False)
    asbg = asBackground

    maxVisibilitySamplesOverride = BoolField(default_value=False)
    vbo = maxVisibilitySamplesOverride

    maxVisibilitySamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    mvs = maxVisibilitySamples

    geometryAntialiasingOverride = BoolField(default_value=False)
    gao = geometryAntialiasingOverride

    antialiasingLevel = LongField(
        default_value=1, min_value=1, max_value=5, soft_max_value=5
    )
    gal = antialiasingLevel

    shadingSamplesOverride = BoolField(default_value=False)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    msa = maxShadingSamples

    volumeSamplesOverride = BoolField(default_value=False)
    vso = volumeSamplesOverride

    volumeSamples = LongField(default_value=1, soft_max_value=20)
    vss = volumeSamples

    depthJitter = BoolField(default_value=False)
    dej = depthJitter

    ignoreSelfShadowing = BoolField(default_value=False)
    iss = ignoreSelfShadowing

    primaryVisibility = BoolField(default_value=True)
    vis = primaryVisibility

    referenceObject = MessageField()
    rob = referenceObject

    compInstObjGroups = CompInstObjGroupsField(multi=True)
    ciog = compInstObjGroups

    componentTags = ComponentTagsField(multi=True)
    gtag = componentTags

    instMaterialAssign = MessageField(multi=True)
    imtla = instMaterialAssign

    pickTexture = MessageField()
    pte = pickTexture

    underWorldObject = BoolField(default_value=False)
    uwo = underWorldObject

    localPosition = LocalPositionField(default_value=(0.0, 0.0, 0.0))
    lp = localPosition
    localPositionX = localPosition.localPositionX
    lpx = localPositionX
    localPositionY = localPosition.localPositionY
    lpy = localPositionY
    localPositionZ = localPosition.localPositionZ
    lpz = localPositionZ

    worldPosition = WorldPositionField(
        multi=True, default_value=(0.0, 0.0, 0.0), writable=False
    )
    wp = worldPosition

    localScale = LocalScaleField(default_value=(1.0, 1.0, 1.0))
    los = localScale
    localScaleX = localScale.localScaleX
    lsx = localScaleX
    localScaleY = localScale.localScaleY
    lsy = localScaleY
    localScaleZ = localScale.localScaleZ
    lsz = localScaleZ

    markerSize = DoubleField(default_value=1.0)
    msz = markerSize

    floorContacts = FloorContactsField(
        default_value=(True, False, True, False, False, False),
        min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
    )
    fc = floorContacts
    drawHandContact = floorContacts.drawHandContact
    dhc = drawHandContact
    handsContact = floorContacts.handsContact
    hfc = handsContact
    drawFeetContact = floorContacts.drawFeetContact
    dfc = drawFeetContact
    feetContact = floorContacts.feetContact
    fec = feetContact
    fingersContact = floorContacts.fingersContact
    fic = fingersContact
    toesContact = floorContacts.toesContact
    tfc = toesContact

    handsFloorContactSetup = HandsFloorContactSetupField(
        default_value=(0, 0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(2.0, 3.0, 1.0),
    )
    flc = handsFloorContactSetup
    handsFloorPivot = handsFloorContactSetup.handsFloorPivot
    hfp = handsFloorPivot
    handsContactType = handsFloorContactSetup.handsContactType
    hct = handsContactType
    handsContactStiffness = handsFloorContactSetup.handsContactStiffness
    hcs = handsContactStiffness

    contactsPosition = ContactsPositionField(
        default_value=(7.5, 4.5, 13.0, 7.0, 5.0, 5.0),
        min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        max_value=(10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0),
    )
    cp = contactsPosition
    handHeight = contactsPosition.handHeight
    hh = handHeight
    handBack = contactsPosition.handBack
    hb = handBack
    handMiddle = contactsPosition.handMiddle
    hm = handMiddle
    handFront = contactsPosition.handFront
    hf = handFront
    handInSide = contactsPosition.handInSide
    his = handInSide
    handOutSide = contactsPosition.handOutSide
    hos = handOutSide

    feetFloorContactSetup = FeetFloorContactSetupField(
        default_value=(0, 0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(2.0, 3.0, 1.0),
    )
    fle = feetFloorContactSetup
    feetFloorPivot = feetFloorContactSetup.feetFloorPivot
    fpv = feetFloorPivot
    feetContactType = feetFloorContactSetup.feetContactType
    fct = feetContactType
    feetContactStiffness = feetFloorContactSetup.feetContactStiffness
    fcs = feetContactStiffness

    feetContactPosition = FeetContactPositionField(
        default_value=(7.5, 4.5, 13.0, 7.0, 5.0, 5.0),
        min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        max_value=(10000.0, 10000.0, 10000.0, 10000.0, 10000.0, 10000.0),
    )
    flf = feetContactPosition
    footHeight = feetContactPosition.footHeight
    fh = footHeight
    footBack = feetContactPosition.footBack
    fra = footBack
    footMiddle = feetContactPosition.footMiddle
    fma = footMiddle
    footFront = feetContactPosition.footFront
    ffm = footFront
    footInSide = feetContactPosition.footInSide
    fia = footInSide
    footOutSide = feetContactPosition.footOutSide
    foa = footOutSide

    fingersFloorContactSetup = FingersFloorContactSetupField(
        default_value=(1, 0.0), min_value=(0.0, 0.0), max_value=(2.0, 1.0)
    )
    flg = fingersFloorContactSetup
    fingersContactType = fingersFloorContactSetup.fingersContactType
    fcm = fingersContactType
    fingersContactRollStiffness = (
        fingersFloorContactSetup.fingersContactRollStiffness
    )
    hcr = fingersContactRollStiffness

    toesFloorContactSetup = ToesFloorContactSetupField(
        default_value=(1, 0.0), min_value=(0.0, 0.0), max_value=(2.0, 1.0)
    )
    fli = toesFloorContactSetup
    toesContactType = toesFloorContactSetup.toesContactType
    tct = toesContactType
    toesContactRollStiffness = toesFloorContactSetup.toesContactRollStiffness
    fcr = toesContactRollStiffness
