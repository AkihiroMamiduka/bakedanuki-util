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

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True, default_value=1.0, writable=False)
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(default_value=1.0, min_value=-2.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
    en = envelope

    function = FunctionField(default_value=(0, 0, 0), readable=False)
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True, default_value=1.0)
    wl = weightList

    morphSpace = MorphSpaceEnumField(default_value=0)
    mspc = morphSpace

    morphMode = MorphModeEnumField(default_value=0)
    mmd = morphMode

    morphTarget = TypedField(multi=True)
    ctrg = morphTarget

    originalMorphTarget = TypedField(multi=True)
    otrg = originalMorphTarget

    componentLookupList = ComponentLookupListField(multi=True, default_value=0.0)
    clkl = componentLookupList

    useComponentLookup = BoolField(default_value=False)
    uclkp = useComponentLookup

    useOriginalMorphTarget = BoolField(default_value=False)
    uotrg = useOriginalMorphTarget

    neighborLevel = LongField(default_value=0, min_value=0, max_value=15)
    nbl = neighborLevel

    neighborExponent = FloatField(default_value=0.0, min_value=0.0, max_value=4.0)
    nbe = neighborExponent

    neighborBias = FloatField(default_value=0.0, min_value=0.0)
    nbb = neighborBias

    scaleLevel = LongField(default_value=0, min_value=0, max_value=20)
    slvl = scaleLevel

    scaleEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    sen = scaleEnvelope

    uniformScaleWeight = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    uen = uniformScaleWeight

    normalScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    nsc = normalScale

    tangentPlaneScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    tsc = tangentPlaneScale

    smoothNormals = LongField(default_value=0, min_value=0, max_value=20)
    snrm = smoothNormals

    mirrorDirection = MirrorDirectionEnumField(default_value=0)
    mird = mirrorDirection

    useTangentialConstraints = BoolField(default_value=False)
    utnc = useTangentialConstraints

    tangentialDamping = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tndm = tangentialDamping

    inwardConstraint = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    iwc = inwardConstraint

    outwardConstraint = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    owc = outwardConstraint
