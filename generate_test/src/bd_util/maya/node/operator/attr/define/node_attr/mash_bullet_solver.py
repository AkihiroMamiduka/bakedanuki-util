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
from ..std.at.matrix import MatrixField
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.byte import ByteField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.numeric_scalar_range.short import ShortField
from ..std.at.typed import TypedField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.mesh import DataMeshField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class OverrideDisplayTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    TEMPLATE = 1
    REFERENCE = 2


class OverrideDisplayTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    TEMPLATE = 1
    REFERENCE = 2

    NAME_MAP = {
        NORMAL: "Normal",
        TEMPLATE: "Template",
        REFERENCE: "Reference",
    }


class OverrideDisplayTypeEnumField(
    EnumField[OverrideDisplayTypeEnumAttrOperator, OverrideDisplayTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OverrideDisplayTypeEnumAttrOperator
    PLUG_CLS = OverrideDisplayTypeEnumPlugOperator


class OverrideLevelOfDetailEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FULL = 0
    BOUNDING_BOX = 1


class OverrideLevelOfDetailEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FULL = 0
    BOUNDING_BOX = 1

    NAME_MAP = {
        FULL: "Full",
        BOUNDING_BOX: "Bounding Box",
    }


class OverrideLevelOfDetailEnumField(
    EnumField[OverrideLevelOfDetailEnumAttrOperator, OverrideLevelOfDetailEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OverrideLevelOfDetailEnumAttrOperator
    PLUG_CLS = OverrideLevelOfDetailEnumPlugOperator


class MashCollisionShapeAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2


class MashCollisionShapeAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class MashCollisionShapeAxisEnumField(
    EnumField[MashCollisionShapeAxisEnumAttrOperator, MashCollisionShapeAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MashCollisionShapeAxisEnumAttrOperator
    PLUG_CLS = MashCollisionShapeAxisEnumPlugOperator


class MashCollisionShapeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BOX = 1
    SPHERE = 2
    CAPSULE = 3
    HULL = 4
    CYLINDER = 7


class MashCollisionShapeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BOX = 1
    SPHERE = 2
    CAPSULE = 3
    HULL = 4
    CYLINDER = 7

    NAME_MAP = {
        BOX: "box",
        SPHERE: "sphere",
        CAPSULE: "capsule",
        HULL: "hull",
        CYLINDER: "cylinder",
    }


class MashCollisionShapeEnumField(
    EnumField[MashCollisionShapeEnumAttrOperator, MashCollisionShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MashCollisionShapeEnumAttrOperator
    PLUG_CLS = MashCollisionShapeEnumPlugOperator


class MashHierarchyModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 4


class MashHierarchyModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 4

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
    }


class MashHierarchyModeEnumField(
    EnumField[MashHierarchyModeEnumAttrOperator, MashHierarchyModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MashHierarchyModeEnumAttrOperator
    PLUG_CLS = MashHierarchyModeEnumPlugOperator


class MashInitialVelocitySpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class MashInitialVelocitySpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
    }


class MashInitialVelocitySpaceEnumField(
    EnumField[MashInitialVelocitySpaceEnumAttrOperator, MashInitialVelocitySpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MashInitialVelocitySpaceEnumAttrOperator
    PLUG_CLS = MashInitialVelocitySpaceEnumPlugOperator


class CollisionShapeTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BOX = 1
    SPHERE = 2
    HULL = 4
    MESH_STATIC_ONLY = 5


class CollisionShapeTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BOX = 1
    SPHERE = 2
    HULL = 4
    MESH_STATIC_ONLY = 5

    NAME_MAP = {
        BOX: "box",
        SPHERE: "sphere",
        HULL: "hull",
        MESH_STATIC_ONLY: "mesh (static only)",
    }


class CollisionShapeTypeEnumField(
    EnumField[CollisionShapeTypeEnumAttrOperator, CollisionShapeTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionShapeTypeEnumAttrOperator
    PLUG_CLS = CollisionShapeTypeEnumPlugOperator


class PublishedNodeInfoPlugOperator(
    CompoundPlugOperator["PublishedNodeInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("publishedNode", "pnod"),
        ("isHierarchicalNode", "ihn"),
        ("publishedNodeType", "pntp"),
    )

    publishedNode = MessageField()
    pnod = publishedNode

    isHierarchicalNode = BoolField(default_value=False)
    ihn = isHierarchicalNode

    publishedNodeType = DataStringField()
    pntp = publishedNodeType


class PublishedNodeInfoAttrOperator(
    CompoundAttrOperator[PublishedNodeInfoPlugOperator]
):
    __slots__ = ()

    publishedNode = MessageField()
    pnod = publishedNode

    isHierarchicalNode = BoolField(default_value=False)
    ihn = isHierarchicalNode

    publishedNodeType = DataStringField()
    pntp = publishedNodeType


class PublishedNodeInfoField(
    CompoundField[PublishedNodeInfoAttrOperator, PublishedNodeInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PublishedNodeInfoAttrOperator
    PLUG_CLS = PublishedNodeInfoPlugOperator


class BoundingBoxPlugOperator(
    CompoundPlugOperator["BoundingBoxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boundingBoxMin", "bbmn"),
        ("boundingBoxMax", "bbmx"),
        ("boundingBoxSize", "bbsi"),
    )

    boundingBoxMin = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    bbmn = boundingBoxMin

    boundingBoxMax = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    bbmx = boundingBoxMax

    boundingBoxSize = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    bbsi = boundingBoxSize


class BoundingBoxAttrOperator(
    CompoundAttrOperator[BoundingBoxPlugOperator]
):
    __slots__ = ()

    boundingBoxMin = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    bbmn = boundingBoxMin

    boundingBoxMax = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    bbmx = boundingBoxMax

    boundingBoxSize = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    bbsi = boundingBoxSize


class BoundingBoxField(
    CompoundField[BoundingBoxAttrOperator, BoundingBoxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundingBoxAttrOperator
    PLUG_CLS = BoundingBoxPlugOperator

    boundingBoxMin = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    bbmn = boundingBoxMin

    boundingBoxMax = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    bbmx = boundingBoxMax

    boundingBoxSize = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    bbsi = boundingBoxSize


class CenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boundingBoxCenterX", "bcx"),
        ("boundingBoxCenterY", "bcy"),
        ("boundingBoxCenterZ", "bcz"),
    )

    boundingBoxCenterX = DoubleLinearField(default_value=0.0, writable=False)
    bcx = boundingBoxCenterX

    boundingBoxCenterY = DoubleLinearField(default_value=0.0, writable=False)
    bcy = boundingBoxCenterY

    boundingBoxCenterZ = DoubleLinearField(default_value=0.0, writable=False)
    bcz = boundingBoxCenterZ


class CenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CenterPlugOperator]
):
    __slots__ = ()

    boundingBoxCenterX = DoubleLinearField(default_value=0.0, writable=False)
    bcx = boundingBoxCenterX

    boundingBoxCenterY = DoubleLinearField(default_value=0.0, writable=False)
    bcy = boundingBoxCenterY

    boundingBoxCenterZ = DoubleLinearField(default_value=0.0, writable=False)
    bcz = boundingBoxCenterZ


class CenterField(
    DoubleLinear3CompoundBaseField[CenterAttrOperator, CenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CenterAttrOperator
    PLUG_CLS = CenterPlugOperator

    boundingBoxCenterX = DoubleLinearField(default_value=0.0, writable=False)
    bcx = boundingBoxCenterX

    boundingBoxCenterY = DoubleLinearField(default_value=0.0, writable=False)
    bcy = boundingBoxCenterY

    boundingBoxCenterZ = DoubleLinearField(default_value=0.0, writable=False)
    bcz = boundingBoxCenterZ


class InstObjGroupsPlugOperator(
    CompoundPlugOperator["InstObjGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("objectGroups", "og"),
    )

    objectGroups = CompoundField(multi=True)
    og = objectGroups


class InstObjGroupsAttrOperator(
    CompoundAttrOperator[InstObjGroupsPlugOperator]
):
    __slots__ = ()

    objectGroups = CompoundField(multi=True)
    og = objectGroups


class InstObjGroupsField(
    CompoundField[InstObjGroupsAttrOperator, InstObjGroupsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InstObjGroupsAttrOperator
    PLUG_CLS = InstObjGroupsPlugOperator


class ObjectColorRGBPlugOperator(
    Float3CompoundBasePlugOperator["ObjectColorRGBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("objectColorR", "obcr"),
        ("objectColorG", "obcg"),
        ("objectColorB", "obcb"),
    )

    objectColorR = FloatField(default_value=0.0)
    obcr = objectColorR

    objectColorG = FloatField(default_value=0.0)
    obcg = objectColorG

    objectColorB = FloatField(default_value=0.0)
    obcb = objectColorB


class ObjectColorRGBAttrOperator(
    Float3CompoundBaseAttrOperator[ObjectColorRGBPlugOperator]
):
    __slots__ = ()

    objectColorR = FloatField(default_value=0.0)
    obcr = objectColorR

    objectColorG = FloatField(default_value=0.0)
    obcg = objectColorG

    objectColorB = FloatField(default_value=0.0)
    obcb = objectColorB


class ObjectColorRGBField(
    Float3CompoundBaseField[ObjectColorRGBAttrOperator, ObjectColorRGBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ObjectColorRGBAttrOperator
    PLUG_CLS = ObjectColorRGBPlugOperator

    objectColorR = FloatField(default_value=0.0)
    obcr = objectColorR

    objectColorG = FloatField(default_value=0.0)
    obcg = objectColorG

    objectColorB = FloatField(default_value=0.0)
    obcb = objectColorB


class WireColorRGBPlugOperator(
    Float3CompoundBasePlugOperator["WireColorRGBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("wireColorR", "wfcr"),
        ("wireColorG", "wfcg"),
        ("wireColorB", "wfcb"),
    )

    wireColorR = FloatField(default_value=0.0)
    wfcr = wireColorR

    wireColorG = FloatField(default_value=0.0)
    wfcg = wireColorG

    wireColorB = FloatField(default_value=0.0)
    wfcb = wireColorB


class WireColorRGBAttrOperator(
    Float3CompoundBaseAttrOperator[WireColorRGBPlugOperator]
):
    __slots__ = ()

    wireColorR = FloatField(default_value=0.0)
    wfcr = wireColorR

    wireColorG = FloatField(default_value=0.0)
    wfcg = wireColorG

    wireColorB = FloatField(default_value=0.0)
    wfcb = wireColorB


class WireColorRGBField(
    Float3CompoundBaseField[WireColorRGBAttrOperator, WireColorRGBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WireColorRGBAttrOperator
    PLUG_CLS = WireColorRGBPlugOperator

    wireColorR = FloatField(default_value=0.0)
    wfcr = wireColorR

    wireColorG = FloatField(default_value=0.0)
    wfcg = wireColorG

    wireColorB = FloatField(default_value=0.0)
    wfcb = wireColorB


class DrawOverridePlugOperator(
    CompoundPlugOperator["DrawOverrideAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("overrideDisplayType", "ovdt"),
        ("overrideLevelOfDetail", "ovlod"),
        ("overrideShading", "ovs"),
        ("overrideTexturing", "ovt"),
        ("overridePlayback", "ovp"),
        ("overrideEnabled", "ove"),
        ("overrideVisibility", "ovv"),
        ("hideOnPlayback", "hpb"),
        ("overrideRGBColors", "ovrgbf"),
        ("overrideColor", "ovc"),
        ("overrideColorRGB", "ovrgb"),
        ("overrideColorA", "ovca"),
    )

    overrideDisplayType = OverrideDisplayTypeEnumField(default_value=0)
    ovdt = overrideDisplayType

    overrideLevelOfDetail = OverrideLevelOfDetailEnumField(default_value=0)
    ovlod = overrideLevelOfDetail

    overrideShading = BoolField(default_value=True)
    ovs = overrideShading

    overrideTexturing = BoolField(default_value=True)
    ovt = overrideTexturing

    overridePlayback = BoolField(default_value=True)
    ovp = overridePlayback

    overrideEnabled = BoolField(default_value=False)
    ove = overrideEnabled

    overrideVisibility = BoolField(default_value=True)
    ovv = overrideVisibility

    hideOnPlayback = BoolField(default_value=False)
    hpb = hideOnPlayback

    overrideRGBColors = BoolField(default_value=False)
    ovrgbf = overrideRGBColors

    overrideColor = ByteField(default_value=0, min_value=0, max_value=31)
    ovc = overrideColor

    overrideColorRGB = Float3Field(default_value=(0.0, 0.0, 0.0))
    ovrgb = overrideColorRGB

    overrideColorA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    ovca = overrideColorA


class DrawOverrideAttrOperator(
    CompoundAttrOperator[DrawOverridePlugOperator]
):
    __slots__ = ()

    overrideDisplayType = OverrideDisplayTypeEnumField(default_value=0)
    ovdt = overrideDisplayType

    overrideLevelOfDetail = OverrideLevelOfDetailEnumField(default_value=0)
    ovlod = overrideLevelOfDetail

    overrideShading = BoolField(default_value=True)
    ovs = overrideShading

    overrideTexturing = BoolField(default_value=True)
    ovt = overrideTexturing

    overridePlayback = BoolField(default_value=True)
    ovp = overridePlayback

    overrideEnabled = BoolField(default_value=False)
    ove = overrideEnabled

    overrideVisibility = BoolField(default_value=True)
    ovv = overrideVisibility

    hideOnPlayback = BoolField(default_value=False)
    hpb = hideOnPlayback

    overrideRGBColors = BoolField(default_value=False)
    ovrgbf = overrideRGBColors

    overrideColor = ByteField(default_value=0, min_value=0, max_value=31)
    ovc = overrideColor

    overrideColorRGB = Float3Field(default_value=(0.0, 0.0, 0.0))
    ovrgb = overrideColorRGB

    overrideColorA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    ovca = overrideColorA


class DrawOverrideField(
    CompoundField[DrawOverrideAttrOperator, DrawOverridePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DrawOverrideAttrOperator
    PLUG_CLS = DrawOverridePlugOperator

    overrideDisplayType = OverrideDisplayTypeEnumField(default_value=0)
    ovdt = overrideDisplayType

    overrideLevelOfDetail = OverrideLevelOfDetailEnumField(default_value=0)
    ovlod = overrideLevelOfDetail

    overrideShading = BoolField(default_value=True)
    ovs = overrideShading

    overrideTexturing = BoolField(default_value=True)
    ovt = overrideTexturing

    overridePlayback = BoolField(default_value=True)
    ovp = overridePlayback

    overrideEnabled = BoolField(default_value=False)
    ove = overrideEnabled

    overrideVisibility = BoolField(default_value=True)
    ovv = overrideVisibility

    hideOnPlayback = BoolField(default_value=False)
    hpb = hideOnPlayback

    overrideRGBColors = BoolField(default_value=False)
    ovrgbf = overrideRGBColors

    overrideColor = ByteField(default_value=0, min_value=0, max_value=31)
    ovc = overrideColor

    overrideColorRGB = Float3Field(default_value=(0.0, 0.0, 0.0))
    ovrgb = overrideColorRGB

    overrideColorA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    ovca = overrideColorA


class RenderInfoPlugOperator(
    CompoundPlugOperator["RenderInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("identification", "rlid"),
        ("layerRenderable", "rndr"),
        ("layerOverrideColor", "lovc"),
    )

    identification = ShortField(default_value=0)
    rlid = identification

    layerRenderable = BoolField(default_value=True)
    rndr = layerRenderable

    layerOverrideColor = ByteField(default_value=0, min_value=0, max_value=31)
    lovc = layerOverrideColor


class RenderInfoAttrOperator(
    CompoundAttrOperator[RenderInfoPlugOperator]
):
    __slots__ = ()

    identification = ShortField(default_value=0)
    rlid = identification

    layerRenderable = BoolField(default_value=True)
    rndr = layerRenderable

    layerOverrideColor = ByteField(default_value=0, min_value=0, max_value=31)
    lovc = layerOverrideColor


class RenderInfoField(
    CompoundField[RenderInfoAttrOperator, RenderInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderInfoAttrOperator
    PLUG_CLS = RenderInfoPlugOperator

    identification = ShortField(default_value=0)
    rlid = identification

    layerRenderable = BoolField(default_value=True)
    rndr = layerRenderable

    layerOverrideColor = ByteField(default_value=0, min_value=0, max_value=31)
    lovc = layerOverrideColor


class RenderLayerInfoPlugOperator(
    CompoundPlugOperator["RenderLayerInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("renderLayerId", "rli"),
        ("renderLayerRenderable", "rlr"),
        ("renderLayerColor", "rlc"),
    )

    renderLayerId = ShortField(default_value=0)
    rli = renderLayerId

    renderLayerRenderable = BoolField(default_value=True)
    rlr = renderLayerRenderable

    renderLayerColor = ByteField(default_value=0, min_value=0, max_value=31)
    rlc = renderLayerColor


class RenderLayerInfoAttrOperator(
    CompoundAttrOperator[RenderLayerInfoPlugOperator]
):
    __slots__ = ()

    renderLayerId = ShortField(default_value=0)
    rli = renderLayerId

    renderLayerRenderable = BoolField(default_value=True)
    rlr = renderLayerRenderable

    renderLayerColor = ByteField(default_value=0, min_value=0, max_value=31)
    rlc = renderLayerColor


class RenderLayerInfoField(
    CompoundField[RenderLayerInfoAttrOperator, RenderLayerInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderLayerInfoAttrOperator
    PLUG_CLS = RenderLayerInfoPlugOperator


class GhostCustomStepsPlugOperator(
    CompoundPlugOperator["GhostCustomStepsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ghostPreFrames", "gprf"),
        ("ghostPostFrames", "gpof"),
        ("ghostsStep", "gstp"),
    )

    ghostPreFrames = LongField(default_value=3)
    gprf = ghostPreFrames

    ghostPostFrames = LongField(default_value=3)
    gpof = ghostPostFrames

    ghostsStep = LongField(default_value=1, min_value=1)
    gstp = ghostsStep


class GhostCustomStepsAttrOperator(
    CompoundAttrOperator[GhostCustomStepsPlugOperator]
):
    __slots__ = ()

    ghostPreFrames = LongField(default_value=3)
    gprf = ghostPreFrames

    ghostPostFrames = LongField(default_value=3)
    gpof = ghostPostFrames

    ghostsStep = LongField(default_value=1, min_value=1)
    gstp = ghostsStep


class GhostCustomStepsField(
    CompoundField[GhostCustomStepsAttrOperator, GhostCustomStepsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostCustomStepsAttrOperator
    PLUG_CLS = GhostCustomStepsPlugOperator

    ghostPreFrames = LongField(default_value=3)
    gprf = ghostPreFrames

    ghostPostFrames = LongField(default_value=3)
    gpof = ghostPostFrames

    ghostsStep = LongField(default_value=1, min_value=1)
    gstp = ghostsStep


class GhostOpacityRangePlugOperator(
    Float2CompoundBasePlugOperator["GhostOpacityRangeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ghostFarOpacity", "gfro"),
        ("ghostNearOpacity", "gnro"),
    )

    ghostFarOpacity = FloatField(default_value=0.15000000596046448, min_value=0.0, max_value=1.0)
    gfro = ghostFarOpacity

    ghostNearOpacity = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    gnro = ghostNearOpacity


class GhostOpacityRangeAttrOperator(
    Float2CompoundBaseAttrOperator[GhostOpacityRangePlugOperator]
):
    __slots__ = ()

    ghostFarOpacity = FloatField(default_value=0.15000000596046448, min_value=0.0, max_value=1.0)
    gfro = ghostFarOpacity

    ghostNearOpacity = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    gnro = ghostNearOpacity


class GhostOpacityRangeField(
    Float2CompoundBaseField[GhostOpacityRangeAttrOperator, GhostOpacityRangePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostOpacityRangeAttrOperator
    PLUG_CLS = GhostOpacityRangePlugOperator

    ghostFarOpacity = FloatField(default_value=0.15000000596046448, min_value=0.0, max_value=1.0)
    gfro = ghostFarOpacity

    ghostNearOpacity = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    gnro = ghostNearOpacity


class GhostColorPrePlugOperator(
    Float3CompoundBasePlugOperator["GhostColorPreAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ghostColorPreR", "grr"),
        ("ghostColorPreG", "gpg"),
        ("ghostColorPreB", "gpb"),
    )

    ghostColorPreR = FloatField(default_value=0.44699999690055847, min_value=0.0, max_value=1.0)
    grr = ghostColorPreR

    ghostColorPreG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    gpg = ghostColorPreG

    ghostColorPreB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    gpb = ghostColorPreB


class GhostColorPreAttrOperator(
    Float3CompoundBaseAttrOperator[GhostColorPrePlugOperator]
):
    __slots__ = ()

    ghostColorPreR = FloatField(default_value=0.44699999690055847, min_value=0.0, max_value=1.0)
    grr = ghostColorPreR

    ghostColorPreG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    gpg = ghostColorPreG

    ghostColorPreB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    gpb = ghostColorPreB


class GhostColorPreField(
    Float3CompoundBaseField[GhostColorPreAttrOperator, GhostColorPrePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostColorPreAttrOperator
    PLUG_CLS = GhostColorPrePlugOperator

    ghostColorPreR = FloatField(default_value=0.44699999690055847, min_value=0.0, max_value=1.0)
    grr = ghostColorPreR

    ghostColorPreG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    gpg = ghostColorPreG

    ghostColorPreB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    gpb = ghostColorPreB


class GhostColorPostPlugOperator(
    Float3CompoundBasePlugOperator["GhostColorPostAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ghostColorPostR", "gar"),
        ("ghostColorPostG", "gag"),
        ("ghostColorPostB", "gab"),
    )

    ghostColorPostR = FloatField(default_value=0.878000020980835, min_value=0.0, max_value=1.0)
    gar = ghostColorPostR

    ghostColorPostG = FloatField(default_value=0.6779999732971191, min_value=0.0, max_value=1.0)
    gag = ghostColorPostG

    ghostColorPostB = FloatField(default_value=0.6629999876022339, min_value=0.0, max_value=1.0)
    gab = ghostColorPostB


class GhostColorPostAttrOperator(
    Float3CompoundBaseAttrOperator[GhostColorPostPlugOperator]
):
    __slots__ = ()

    ghostColorPostR = FloatField(default_value=0.878000020980835, min_value=0.0, max_value=1.0)
    gar = ghostColorPostR

    ghostColorPostG = FloatField(default_value=0.6779999732971191, min_value=0.0, max_value=1.0)
    gag = ghostColorPostG

    ghostColorPostB = FloatField(default_value=0.6629999876022339, min_value=0.0, max_value=1.0)
    gab = ghostColorPostB


class GhostColorPostField(
    Float3CompoundBaseField[GhostColorPostAttrOperator, GhostColorPostPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostColorPostAttrOperator
    PLUG_CLS = GhostColorPostPlugOperator

    ghostColorPostR = FloatField(default_value=0.878000020980835, min_value=0.0, max_value=1.0)
    gar = ghostColorPostR

    ghostColorPostG = FloatField(default_value=0.6779999732971191, min_value=0.0, max_value=1.0)
    gag = ghostColorPostG

    ghostColorPostB = FloatField(default_value=0.6629999876022339, min_value=0.0, max_value=1.0)
    gab = ghostColorPostB


class OutlinerColorPlugOperator(
    Float3CompoundBasePlugOperator["OutlinerColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outlinerColorR", "oclrr"),
        ("outlinerColorG", "oclrg"),
        ("outlinerColorB", "oclrb"),
    )

    outlinerColorR = FloatField(default_value=0.0)
    oclrr = outlinerColorR

    outlinerColorG = FloatField(default_value=0.0)
    oclrg = outlinerColorG

    outlinerColorB = FloatField(default_value=0.0)
    oclrb = outlinerColorB


class OutlinerColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutlinerColorPlugOperator]
):
    __slots__ = ()

    outlinerColorR = FloatField(default_value=0.0)
    oclrr = outlinerColorR

    outlinerColorG = FloatField(default_value=0.0)
    oclrg = outlinerColorG

    outlinerColorB = FloatField(default_value=0.0)
    oclrb = outlinerColorB


class OutlinerColorField(
    Float3CompoundBaseField[OutlinerColorAttrOperator, OutlinerColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutlinerColorAttrOperator
    PLUG_CLS = OutlinerColorPlugOperator

    outlinerColorR = FloatField(default_value=0.0)
    oclrr = outlinerColorR

    outlinerColorG = FloatField(default_value=0.0)
    oclrg = outlinerColorG

    outlinerColorB = FloatField(default_value=0.0)
    oclrb = outlinerColorB


class CompInstObjGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compObjectGroups", "cog"),
    )

    compObjectGroups = CompoundField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGroups = CompoundField(multi=True)
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
    DoubleLinear3CompoundBaseField[LocalPositionAttrOperator, LocalPositionPlugOperator]
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
    DoubleLinear3CompoundBaseField[WorldPositionAttrOperator, WorldPositionPlugOperator]
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
    DoubleLinear3CompoundBaseField[LocalScaleAttrOperator, LocalScalePlugOperator]
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


class InputNetworksPlugOperator(
    CompoundPlugOperator["InputNetworksAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputPoints", "inputPoints"),
        ("mashEnable", "mashEnable"),
        ("mashAutoFit", "mashAutoFit"),
        ("mashBounce", "mashBounce"),
        ("mashInitiallySleeping", "mashInitiallySleeping"),
        ("mashFriction", "mashFriction"),
        ("mashRollingFriction", "mashRollingFriction"),
        ("mashDamping", "mashDamping"),
        ("mashRollingDamping", "mashRollingDamping"),
        ("mashMass", "mashMass"),
        ("mashUseDensity", "mashUseDensity"),
        ("mashPositionStrength", "mashPositionStrength"),
        ("mashRotationalStrength", "mashRotationalStrength"),
        ("mashLinearVelocityThreshold", "mashLinearVelocityThreshold"),
        ("mashAngularVelocityThreshold", "mashAngularVelocityThreshold"),
        ("mashCollisionJitter", "mashCollisionJitter"),
        ("mashCollisionShapeLength", "mashCollisionShapeLength"),
        ("mashCollisionObjectScale", "mashCollisionObjectScale"),
        ("mashCollisionShapeAxis", "mashCollisionShapeAxis"),
        ("mashInitialVelocity", "mashInitialVelocity"),
        ("mashInitialRotationalVelocity", "mashInitialRotationalVelocity"),
        ("mashMaxVelocity", "mashMaxVelocity"),
        ("mashAngularVelocity", "mashAngularVelocity"),
        ("mashIgnoreInvisible", "mashIgnoreInvisible"),
        ("mashCollisionShape", "mashCollisionShape"),
        ("mashEmitFromCollisions", "mashEmitFromCollisions"),
        ("mashCollisionDistanceThreshold", "mashCollisionDistanceThreshold"),
        ("mashContactMaskLayers", "mashContactMaskLayers"),
        ("mashCollisionMaskLayers", "mashCollisionMaskLayers"),
        ("mashCollisionGroupLayers", "mashCollisionGroupLayers"),
        ("mashHierarchyMode", "mashHierarchyMode"),
        ("mashInitialStateJSON", "mashInitialStateJSON"),
        ("mashInitialVelocitySpace", "mashInitialVelocitySpace"),
    )

    inputPoints = TypedField()

    mashEnable = BoolField(default_value=True)

    mashAutoFit = BoolField(default_value=True)

    mashBounce = FloatField(default_value=0.30000001192092896, min_value=0.0, max_value=1.0)

    mashInitiallySleeping = BoolField(default_value=False)

    mashFriction = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=1.0)

    mashRollingFriction = FloatField(default_value=0.30000001192092896, min_value=0.0, soft_max_value=1.0)

    mashDamping = FloatField(default_value=0.009999999776482582, min_value=0.0, max_value=1.0)

    mashRollingDamping = FloatField(default_value=0.009999999776482582, min_value=0.0, max_value=1.0)

    mashMass = FloatField(default_value=1.0, min_value=0.0, soft_max_value=100.0)

    mashUseDensity = BoolField(default_value=False)

    mashPositionStrength = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    mashRotationalStrength = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    mashLinearVelocityThreshold = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mashAngularVelocityThreshold = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mashCollisionJitter = FloatField(default_value=0.009999999776482582, min_value=0.0, soft_max_value=1.0)

    mashCollisionShapeLength = FloatField(default_value=5.0, min_value=0.0, soft_max_value=10.0)

    mashCollisionObjectScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    mashCollisionShapeAxis = MashCollisionShapeAxisEnumField(default_value=1)

    mashInitialVelocity = Float3Field(default_value=(0.0, 0.0, 0.0))

    mashInitialRotationalVelocity = Float3Field(default_value=(0.0, 0.0, 0.0))

    mashMaxVelocity = FloatField(default_value=100.0, min_value=0.0, soft_max_value=100.0)

    mashAngularVelocity = FloatField(default_value=0.5, min_value=0.0, soft_max_value=2.0)

    mashIgnoreInvisible = BoolField(default_value=False)

    mashCollisionShape = MashCollisionShapeEnumField(default_value=1)

    mashEmitFromCollisions = BoolField(default_value=False)

    mashCollisionDistanceThreshold = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    mashContactMaskLayers = DataStringField()

    mashCollisionMaskLayers = DataStringField()

    mashCollisionGroupLayers = DataStringField()

    mashHierarchyMode = MashHierarchyModeEnumField(default_value=1)

    mashInitialStateJSON = DataStringField()

    mashInitialVelocitySpace = MashInitialVelocitySpaceEnumField(default_value=1)


class InputNetworksAttrOperator(
    CompoundAttrOperator[InputNetworksPlugOperator]
):
    __slots__ = ()

    inputPoints = TypedField()

    mashEnable = BoolField(default_value=True)

    mashAutoFit = BoolField(default_value=True)

    mashBounce = FloatField(default_value=0.30000001192092896, min_value=0.0, max_value=1.0)

    mashInitiallySleeping = BoolField(default_value=False)

    mashFriction = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=1.0)

    mashRollingFriction = FloatField(default_value=0.30000001192092896, min_value=0.0, soft_max_value=1.0)

    mashDamping = FloatField(default_value=0.009999999776482582, min_value=0.0, max_value=1.0)

    mashRollingDamping = FloatField(default_value=0.009999999776482582, min_value=0.0, max_value=1.0)

    mashMass = FloatField(default_value=1.0, min_value=0.0, soft_max_value=100.0)

    mashUseDensity = BoolField(default_value=False)

    mashPositionStrength = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    mashRotationalStrength = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    mashLinearVelocityThreshold = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mashAngularVelocityThreshold = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mashCollisionJitter = FloatField(default_value=0.009999999776482582, min_value=0.0, soft_max_value=1.0)

    mashCollisionShapeLength = FloatField(default_value=5.0, min_value=0.0, soft_max_value=10.0)

    mashCollisionObjectScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    mashCollisionShapeAxis = MashCollisionShapeAxisEnumField(default_value=1)

    mashInitialVelocity = Float3Field(default_value=(0.0, 0.0, 0.0))

    mashInitialRotationalVelocity = Float3Field(default_value=(0.0, 0.0, 0.0))

    mashMaxVelocity = FloatField(default_value=100.0, min_value=0.0, soft_max_value=100.0)

    mashAngularVelocity = FloatField(default_value=0.5, min_value=0.0, soft_max_value=2.0)

    mashIgnoreInvisible = BoolField(default_value=False)

    mashCollisionShape = MashCollisionShapeEnumField(default_value=1)

    mashEmitFromCollisions = BoolField(default_value=False)

    mashCollisionDistanceThreshold = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    mashContactMaskLayers = DataStringField()

    mashCollisionMaskLayers = DataStringField()

    mashCollisionGroupLayers = DataStringField()

    mashHierarchyMode = MashHierarchyModeEnumField(default_value=1)

    mashInitialStateJSON = DataStringField()

    mashInitialVelocitySpace = MashInitialVelocitySpaceEnumField(default_value=1)


class InputNetworksField(
    CompoundField[InputNetworksAttrOperator, InputNetworksPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputNetworksAttrOperator
    PLUG_CLS = InputNetworksPlugOperator


class GroundPlanePositionPlugOperator(
    Float3CompoundBasePlugOperator["GroundPlanePositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("groundPlanePositionX", "groundPlanePositionx"),
        ("groundPlanePositionY", "groundPlanePositiony"),
        ("groundPlanePositionZ", "groundPlanePositionz"),
    )

    groundPlanePositionX = FloatField(default_value=0.0)
    groundPlanePositionx = groundPlanePositionX

    groundPlanePositionY = FloatField(default_value=-20.0)
    groundPlanePositiony = groundPlanePositionY

    groundPlanePositionZ = FloatField(default_value=0.0)
    groundPlanePositionz = groundPlanePositionZ


class GroundPlanePositionAttrOperator(
    Float3CompoundBaseAttrOperator[GroundPlanePositionPlugOperator]
):
    __slots__ = ()

    groundPlanePositionX = FloatField(default_value=0.0)
    groundPlanePositionx = groundPlanePositionX

    groundPlanePositionY = FloatField(default_value=-20.0)
    groundPlanePositiony = groundPlanePositionY

    groundPlanePositionZ = FloatField(default_value=0.0)
    groundPlanePositionz = groundPlanePositionZ


class GroundPlanePositionField(
    Float3CompoundBaseField[GroundPlanePositionAttrOperator, GroundPlanePositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GroundPlanePositionAttrOperator
    PLUG_CLS = GroundPlanePositionPlugOperator

    groundPlanePositionX = FloatField(default_value=0.0)
    groundPlanePositionx = groundPlanePositionX

    groundPlanePositionY = FloatField(default_value=-20.0)
    groundPlanePositiony = groundPlanePositionY

    groundPlanePositionZ = FloatField(default_value=0.0)
    groundPlanePositionz = groundPlanePositionZ


class GroundPlaneUpVectorPlugOperator(
    Float3CompoundBasePlugOperator["GroundPlaneUpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("groundPlaneUpVectorX", "groundPlaneUpVectorx"),
        ("groundPlaneUpVectorY", "groundPlaneUpVectory"),
        ("groundPlaneUpVectorZ", "groundPlaneUpVectorz"),
    )

    groundPlaneUpVectorX = FloatField(default_value=0.0)
    groundPlaneUpVectorx = groundPlaneUpVectorX

    groundPlaneUpVectorY = FloatField(default_value=1.0)
    groundPlaneUpVectory = groundPlaneUpVectorY

    groundPlaneUpVectorZ = FloatField(default_value=0.0)
    groundPlaneUpVectorz = groundPlaneUpVectorZ


class GroundPlaneUpVectorAttrOperator(
    Float3CompoundBaseAttrOperator[GroundPlaneUpVectorPlugOperator]
):
    __slots__ = ()

    groundPlaneUpVectorX = FloatField(default_value=0.0)
    groundPlaneUpVectorx = groundPlaneUpVectorX

    groundPlaneUpVectorY = FloatField(default_value=1.0)
    groundPlaneUpVectory = groundPlaneUpVectorY

    groundPlaneUpVectorZ = FloatField(default_value=0.0)
    groundPlaneUpVectorz = groundPlaneUpVectorZ


class GroundPlaneUpVectorField(
    Float3CompoundBaseField[GroundPlaneUpVectorAttrOperator, GroundPlaneUpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GroundPlaneUpVectorAttrOperator
    PLUG_CLS = GroundPlaneUpVectorPlugOperator

    groundPlaneUpVectorX = FloatField(default_value=0.0)
    groundPlaneUpVectorx = groundPlaneUpVectorX

    groundPlaneUpVectorY = FloatField(default_value=1.0)
    groundPlaneUpVectory = groundPlaneUpVectorY

    groundPlaneUpVectorZ = FloatField(default_value=0.0)
    groundPlaneUpVectorz = groundPlaneUpVectorZ


class GravityPlugOperator(
    Float3CompoundBasePlugOperator["GravityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("gravityX", "gravityx"),
        ("gravityY", "gravityy"),
        ("gravityZ", "gravityz"),
    )

    gravityX = FloatField(default_value=0.0)
    gravityx = gravityX

    gravityY = FloatField(default_value=-9.800000190734863)
    gravityy = gravityY

    gravityZ = FloatField(default_value=0.0)
    gravityz = gravityZ


class GravityAttrOperator(
    Float3CompoundBaseAttrOperator[GravityPlugOperator]
):
    __slots__ = ()

    gravityX = FloatField(default_value=0.0)
    gravityx = gravityX

    gravityY = FloatField(default_value=-9.800000190734863)
    gravityy = gravityY

    gravityZ = FloatField(default_value=0.0)
    gravityz = gravityZ


class GravityField(
    Float3CompoundBaseField[GravityAttrOperator, GravityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GravityAttrOperator
    PLUG_CLS = GravityPlugOperator

    gravityX = FloatField(default_value=0.0)
    gravityx = gravityX

    gravityY = FloatField(default_value=-9.800000190734863)
    gravityy = gravityY

    gravityZ = FloatField(default_value=0.0)
    gravityz = gravityZ


class ActiveRigidBodyColorPlugOperator(
    Float3CompoundBasePlugOperator["ActiveRigidBodyColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("activeRigidBodyColorR", "activeRigidBodyColorr"),
        ("activeRigidBodyColorG", "activeRigidBodyColorg"),
        ("activeRigidBodyColorB", "activeRigidBodyColorb"),
    )

    activeRigidBodyColorR = FloatField(default_value=1.0)
    activeRigidBodyColorr = activeRigidBodyColorR

    activeRigidBodyColorG = FloatField(default_value=0.0)
    activeRigidBodyColorg = activeRigidBodyColorG

    activeRigidBodyColorB = FloatField(default_value=0.0)
    activeRigidBodyColorb = activeRigidBodyColorB


class ActiveRigidBodyColorAttrOperator(
    Float3CompoundBaseAttrOperator[ActiveRigidBodyColorPlugOperator]
):
    __slots__ = ()

    activeRigidBodyColorR = FloatField(default_value=1.0)
    activeRigidBodyColorr = activeRigidBodyColorR

    activeRigidBodyColorG = FloatField(default_value=0.0)
    activeRigidBodyColorg = activeRigidBodyColorG

    activeRigidBodyColorB = FloatField(default_value=0.0)
    activeRigidBodyColorb = activeRigidBodyColorB


class ActiveRigidBodyColorField(
    Float3CompoundBaseField[ActiveRigidBodyColorAttrOperator, ActiveRigidBodyColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ActiveRigidBodyColorAttrOperator
    PLUG_CLS = ActiveRigidBodyColorPlugOperator

    activeRigidBodyColorR = FloatField(default_value=1.0)
    activeRigidBodyColorr = activeRigidBodyColorR

    activeRigidBodyColorG = FloatField(default_value=0.0)
    activeRigidBodyColorg = activeRigidBodyColorG

    activeRigidBodyColorB = FloatField(default_value=0.0)
    activeRigidBodyColorb = activeRigidBodyColorB


class SleepingRigidBodyColorPlugOperator(
    Float3CompoundBasePlugOperator["SleepingRigidBodyColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sleepingRigidBodyColorR", "sleepingRigidBodyColorr"),
        ("sleepingRigidBodyColorG", "sleepingRigidBodyColorg"),
        ("sleepingRigidBodyColorB", "sleepingRigidBodyColorb"),
    )

    sleepingRigidBodyColorR = FloatField(default_value=0.7411764860153198)
    sleepingRigidBodyColorr = sleepingRigidBodyColorR

    sleepingRigidBodyColorG = FloatField(default_value=0.7411764860153198)
    sleepingRigidBodyColorg = sleepingRigidBodyColorG

    sleepingRigidBodyColorB = FloatField(default_value=0.7411764860153198)
    sleepingRigidBodyColorb = sleepingRigidBodyColorB


class SleepingRigidBodyColorAttrOperator(
    Float3CompoundBaseAttrOperator[SleepingRigidBodyColorPlugOperator]
):
    __slots__ = ()

    sleepingRigidBodyColorR = FloatField(default_value=0.7411764860153198)
    sleepingRigidBodyColorr = sleepingRigidBodyColorR

    sleepingRigidBodyColorG = FloatField(default_value=0.7411764860153198)
    sleepingRigidBodyColorg = sleepingRigidBodyColorG

    sleepingRigidBodyColorB = FloatField(default_value=0.7411764860153198)
    sleepingRigidBodyColorb = sleepingRigidBodyColorB


class SleepingRigidBodyColorField(
    Float3CompoundBaseField[SleepingRigidBodyColorAttrOperator, SleepingRigidBodyColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SleepingRigidBodyColorAttrOperator
    PLUG_CLS = SleepingRigidBodyColorPlugOperator

    sleepingRigidBodyColorR = FloatField(default_value=0.7411764860153198)
    sleepingRigidBodyColorr = sleepingRigidBodyColorR

    sleepingRigidBodyColorG = FloatField(default_value=0.7411764860153198)
    sleepingRigidBodyColorg = sleepingRigidBodyColorG

    sleepingRigidBodyColorB = FloatField(default_value=0.7411764860153198)
    sleepingRigidBodyColorb = sleepingRigidBodyColorB


class LineColourPlugOperator(
    Float3CompoundBasePlugOperator["LineColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lineColourR", "lineColourr"),
        ("lineColourG", "lineColourg"),
        ("lineColourB", "lineColourb"),
    )

    lineColourR = FloatField(default_value=1.0)
    lineColourr = lineColourR

    lineColourG = FloatField(default_value=0.7843137383460999)
    lineColourg = lineColourG

    lineColourB = FloatField(default_value=0.0)
    lineColourb = lineColourB


class LineColourAttrOperator(
    Float3CompoundBaseAttrOperator[LineColourPlugOperator]
):
    __slots__ = ()

    lineColourR = FloatField(default_value=1.0)
    lineColourr = lineColourR

    lineColourG = FloatField(default_value=0.7843137383460999)
    lineColourg = lineColourG

    lineColourB = FloatField(default_value=0.0)
    lineColourb = lineColourB


class LineColourField(
    Float3CompoundBaseField[LineColourAttrOperator, LineColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LineColourAttrOperator
    PLUG_CLS = LineColourPlugOperator

    lineColourR = FloatField(default_value=1.0)
    lineColourr = lineColourR

    lineColourG = FloatField(default_value=0.7843137383460999)
    lineColourg = lineColourG

    lineColourB = FloatField(default_value=0.0)
    lineColourb = lineColourB


class CollisionObjectsPlugOperator(
    CompoundPlugOperator["CollisionObjectsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionShapeMesh", "collisionShapeMesh"),
        ("collisionShapeMatrix", "collisionShapeMatrix"),
        ("collisionShapeBounce", "collisionShapeBounce"),
        ("collisionShapeFriction", "collisionShapeFriction"),
        ("collisionShapeDamping", "collisionShapeDamping"),
        ("collisionShapeMass", "collisionShapeMass"),
        ("collisionShapeScale", "collisionShapeScale"),
        ("collisionShapeType", "collisionShapeType"),
        ("collisionContactMaskLayers", "collisionContactMaskLayers"),
        ("collisionMaskLayers", "collisionMaskLayers"),
        ("collisionGroupLayers", "collisionGroupLayers"),
    )

    collisionShapeMesh = DataMeshField()

    collisionShapeMatrix = MatrixField()

    collisionShapeBounce = FloatField(default_value=0.30000001192092896, min_value=0.0, max_value=1.0)

    collisionShapeFriction = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=1.0)

    collisionShapeDamping = FloatField(default_value=0.009999999776482582, min_value=0.0, max_value=1.0)

    collisionShapeMass = FloatField(default_value=100.0, min_value=0.0, soft_max_value=100.0)

    collisionShapeScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    collisionShapeType = CollisionShapeTypeEnumField(default_value=1)

    collisionContactMaskLayers = DataStringField()

    collisionMaskLayers = DataStringField()

    collisionGroupLayers = DataStringField()


class CollisionObjectsAttrOperator(
    CompoundAttrOperator[CollisionObjectsPlugOperator]
):
    __slots__ = ()

    collisionShapeMesh = DataMeshField()

    collisionShapeMatrix = MatrixField()

    collisionShapeBounce = FloatField(default_value=0.30000001192092896, min_value=0.0, max_value=1.0)

    collisionShapeFriction = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=1.0)

    collisionShapeDamping = FloatField(default_value=0.009999999776482582, min_value=0.0, max_value=1.0)

    collisionShapeMass = FloatField(default_value=100.0, min_value=0.0, soft_max_value=100.0)

    collisionShapeScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    collisionShapeType = CollisionShapeTypeEnumField(default_value=1)

    collisionContactMaskLayers = DataStringField()

    collisionMaskLayers = DataStringField()

    collisionGroupLayers = DataStringField()


class CollisionObjectsField(
    CompoundField[CollisionObjectsAttrOperator, CollisionObjectsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionObjectsAttrOperator
    PLUG_CLS = CollisionObjectsPlugOperator
