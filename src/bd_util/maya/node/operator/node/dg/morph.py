# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.morph import (
    ComponentLookupListField,
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField


class MorphSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OBJECT_SPACE = 0
    WORLD_SPACE = 1


class MorphSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OBJECT_SPACE = 0
    WORLD_SPACE = 1

    NAME_MAP = {
        OBJECT_SPACE: "Object Space",
        WORLD_SPACE: "World Space",
    }


class MorphSpaceEnumField(
    EnumField[MorphSpaceEnumAttrOperator, MorphSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MorphSpaceEnumAttrOperator
    PLUG_CLS = MorphSpaceEnumPlugOperator


class MorphModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ABSOLUTE = 0
    RELATIVE = 1
    SURFACE = 2
    RETARGET = 3
    MIRROR = 4


class MorphModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ABSOLUTE = 0
    RELATIVE = 1
    SURFACE = 2
    RETARGET = 3
    MIRROR = 4

    NAME_MAP = {
        ABSOLUTE: "Absolute",
        RELATIVE: "Relative",
        SURFACE: "Surface",
        RETARGET: "Retarget",
        MIRROR: "Mirror",
    }


class MorphModeEnumField(
    EnumField[MorphModeEnumAttrOperator, MorphModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MorphModeEnumAttrOperator
    PLUG_CLS = MorphModeEnumPlugOperator


class MirrorDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5
    FLIP_X = 6
    FLIP_Y = 7
    FLIP_Z = 8


class MirrorDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5
    FLIP_X = 6
    FLIP_Y = 7
    FLIP_Z = 8

    NAME_MAP = {
        PLUS_X: "+X",
        MINUS_X: "-X",
        PLUS_Y: "+Y",
        MINUS_Y: "-Y",
        PLUS_Z: "+Z",
        MINUS_Z: "-Z",
        FLIP_X: "Flip X",
        FLIP_Y: "Flip Y",
        FLIP_Z: "Flip Z",
    }


class MirrorDirectionEnumField(
    EnumField[MirrorDirectionEnumAttrOperator, MirrorDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MirrorDirectionEnumAttrOperator
    PLUG_CLS = MirrorDirectionEnumPlugOperator


class Morph(DG):
    __slots__ = ()

    NODE_TYPE = "morph"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True)
    ocw = envelopeWeightsList

    blockGPU = BoolField()
    bgp = blockGPU

    envelope = FloatField()
    en = envelope

    function = FunctionField()
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True)
    wl = weightList

    morphSpace = MorphSpaceEnumField()
    mspc = morphSpace

    morphMode = MorphModeEnumField()
    mmd = morphMode

    morphTarget = TypedField(multi=True)
    ctrg = morphTarget

    originalMorphTarget = TypedField(multi=True)
    otrg = originalMorphTarget

    componentLookupList = ComponentLookupListField(multi=True)
    clkl = componentLookupList

    useComponentLookup = BoolField()
    uclkp = useComponentLookup

    useOriginalMorphTarget = BoolField()
    uotrg = useOriginalMorphTarget

    neighborLevel = LongField()
    nbl = neighborLevel

    neighborExponent = FloatField()
    nbe = neighborExponent

    neighborBias = FloatField()
    nbb = neighborBias

    scaleLevel = LongField()
    slvl = scaleLevel

    scaleEnvelope = FloatField()
    sen = scaleEnvelope

    uniformScaleWeight = FloatField()
    uen = uniformScaleWeight

    normalScale = FloatField()
    nsc = normalScale

    tangentPlaneScale = FloatField()
    tsc = tangentPlaneScale

    smoothNormals = LongField()
    snrm = smoothNormals

    mirrorDirection = MirrorDirectionEnumField()
    mird = mirrorDirection

    useTangentialConstraints = BoolField()
    utnc = useTangentialConstraints

    tangentialDamping = FloatField()
    tndm = tangentialDamping

    inwardConstraint = FloatField()
    iwc = inwardConstraint

    outwardConstraint = FloatField()
    owc = outwardConstraint
