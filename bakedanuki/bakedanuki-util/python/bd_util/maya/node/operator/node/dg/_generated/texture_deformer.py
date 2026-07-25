# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.texture_deformer import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    TextureField,
    VectorOffsetField,
    VectorStrengthField,
    WeightListField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField


class DirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    HANDLE = 1
    VECTOR = 2


class DirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    HANDLE = 1
    VECTOR = 2

    NAME_MAP = {
        NORMAL: "Normal",
        HANDLE: "Handle",
        VECTOR: "Vector",
    }


class DirectionEnumField(
    EnumField[DirectionEnumAttrOperator, DirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DirectionEnumAttrOperator
    PLUG_CLS = DirectionEnumPlugOperator


class PointSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    UV = 2


class PointSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    UV = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
        UV: "UV",
    }


class PointSpaceEnumField(
    EnumField[PointSpaceEnumAttrOperator, PointSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointSpaceEnumAttrOperator
    PLUG_CLS = PointSpaceEnumPlugOperator


class VectorSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OBJECT = 0
    WORLD = 1
    TANGENT = 2


class VectorSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OBJECT = 0
    WORLD = 1
    TANGENT = 2

    NAME_MAP = {
        OBJECT: "Object",
        WORLD: "World",
        TANGENT: "Tangent",
    }


class VectorSpaceEnumField(
    EnumField[VectorSpaceEnumAttrOperator, VectorSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VectorSpaceEnumAttrOperator
    PLUG_CLS = VectorSpaceEnumPlugOperator


class _GeneratedTextureDeformer(DG):
    __slots__ = ()

    NODE_TYPE = "textureDeformer"

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

    texture = TextureField(default_value=(0.0, 0.0, 0.0))
    t = texture
    textureR = texture.textureR
    tr = textureR
    textureG = texture.textureG
    tg = textureG
    textureB = texture.textureB
    tb = textureB

    strength = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    s = strength

    offset = DoubleLinearField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    o = offset

    vectorStrength = VectorStrengthField(default_value=(1.0, 1.0, 1.0))
    vs = vectorStrength
    vectorStrengthX = vectorStrength.vectorStrengthX
    vsx = vectorStrengthX
    vectorStrengthY = vectorStrength.vectorStrengthY
    vsy = vectorStrengthY
    vectorStrengthZ = vectorStrength.vectorStrengthZ
    vsz = vectorStrengthZ

    vectorOffset = VectorOffsetField(default_value=(0.0, 0.0, 0.0))
    vo = vectorOffset
    vectorOffsetX = vectorOffset.vectorOffsetX
    vox = vectorOffsetX
    vectorOffsetY = vectorOffset.vectorOffsetY
    voy = vectorOffsetY
    vectorOffsetZ = vectorOffset.vectorOffsetZ
    voz = vectorOffsetZ

    direction = DirectionEnumField(default_value=1)
    d = direction

    pointSpace = PointSpaceEnumField(default_value=2)
    ps = pointSpace

    vectorSpace = VectorSpaceEnumField(default_value=0)
    vsp = vectorSpace

    handleMatrix = DataMatrixField()
    hm = handleMatrix

    handleVisibility = BoolField(default_value=True)
    v = handleVisibility
