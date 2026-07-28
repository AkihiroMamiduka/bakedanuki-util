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
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.byte import ByteField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.numeric.range.short import ShortField
from ..std.at.typed import TypedField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.scalar.unit.range.float_linear import FloatLinearField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import (
    Double3Field,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound.float2 import (
    Float2Field,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import (
    Float3Field,
)
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.float3._base import (
    FloatLinear3CompoundBaseAttrOperator,
    FloatLinear3CompoundBasePlugOperator,
    FloatLinear3CompoundBaseField,
)


class OverrideDisplayTypeEnumPlugOperator(
    EnumPlugOperator["OverrideDisplayTypeEnumAttrOperator"]
):
    __slots__ = ()

    NORMAL = 0
    TEMPLATE = 1
    REFERENCE = 2


class OverrideDisplayTypeEnumAttrOperator(
    EnumAttrOperator[OverrideDisplayTypeEnumPlugOperator]
):
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
    EnumField[
        OverrideDisplayTypeEnumAttrOperator,
        OverrideDisplayTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = OverrideDisplayTypeEnumAttrOperator
    PLUG_CLS = OverrideDisplayTypeEnumPlugOperator


class OverrideLevelOfDetailEnumPlugOperator(
    EnumPlugOperator["OverrideLevelOfDetailEnumAttrOperator"]
):
    __slots__ = ()

    FULL = 0
    BOUNDING_BOX = 1


class OverrideLevelOfDetailEnumAttrOperator(
    EnumAttrOperator[OverrideLevelOfDetailEnumPlugOperator]
):
    __slots__ = ()

    FULL = 0
    BOUNDING_BOX = 1

    NAME_MAP = {
        FULL: "Full",
        BOUNDING_BOX: "Bounding Box",
    }


class OverrideLevelOfDetailEnumField(
    EnumField[
        OverrideLevelOfDetailEnumAttrOperator,
        OverrideLevelOfDetailEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = OverrideLevelOfDetailEnumAttrOperator
    PLUG_CLS = OverrideLevelOfDetailEnumPlugOperator


class RepresentationEnumPlugOperator(
    EnumPlugOperator["RepresentationEnumAttrOperator"]
):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4


class RepresentationEnumAttrOperator(
    EnumAttrOperator[RepresentationEnumPlugOperator]
):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4

    NAME_MAP = {
        A: "A",
        LA: "LA",
        RGB: "RGB",
        RGBA: "RGBA",
    }


class RepresentationEnumField(
    EnumField[RepresentationEnumAttrOperator, RepresentationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RepresentationEnumAttrOperator
    PLUG_CLS = RepresentationEnumPlugOperator


class CollisionOffsetVelocityIncrement_InterpEnumPlugOperator(
    EnumPlugOperator["CollisionOffsetVelocityIncrement_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionOffsetVelocityIncrement_InterpEnumAttrOperator(
    EnumAttrOperator[CollisionOffsetVelocityIncrement_InterpEnumPlugOperator]
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


class CollisionOffsetVelocityIncrement_InterpEnumField(
    EnumField[
        CollisionOffsetVelocityIncrement_InterpEnumAttrOperator,
        CollisionOffsetVelocityIncrement_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityIncrement_InterpEnumAttrOperator
    PLUG_CLS = CollisionOffsetVelocityIncrement_InterpEnumPlugOperator


class CollisionDepthVelocityIncrement_InterpEnumPlugOperator(
    EnumPlugOperator["CollisionDepthVelocityIncrement_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionDepthVelocityIncrement_InterpEnumAttrOperator(
    EnumAttrOperator[CollisionDepthVelocityIncrement_InterpEnumPlugOperator]
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


class CollisionDepthVelocityIncrement_InterpEnumField(
    EnumField[
        CollisionDepthVelocityIncrement_InterpEnumAttrOperator,
        CollisionDepthVelocityIncrement_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityIncrement_InterpEnumAttrOperator
    PLUG_CLS = CollisionDepthVelocityIncrement_InterpEnumPlugOperator


class CollisionOffsetVelocityMultiplier_InterpEnumPlugOperator(
    EnumPlugOperator[
        "CollisionOffsetVelocityMultiplier_InterpEnumAttrOperator"
    ]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionOffsetVelocityMultiplier_InterpEnumAttrOperator(
    EnumAttrOperator[CollisionOffsetVelocityMultiplier_InterpEnumPlugOperator]
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


class CollisionOffsetVelocityMultiplier_InterpEnumField(
    EnumField[
        CollisionOffsetVelocityMultiplier_InterpEnumAttrOperator,
        CollisionOffsetVelocityMultiplier_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityMultiplier_InterpEnumAttrOperator
    PLUG_CLS = CollisionOffsetVelocityMultiplier_InterpEnumPlugOperator


class CollisionDepthVelocityMultiplier_InterpEnumPlugOperator(
    EnumPlugOperator["CollisionDepthVelocityMultiplier_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollisionDepthVelocityMultiplier_InterpEnumAttrOperator(
    EnumAttrOperator[CollisionDepthVelocityMultiplier_InterpEnumPlugOperator]
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


class CollisionDepthVelocityMultiplier_InterpEnumField(
    EnumField[
        CollisionDepthVelocityMultiplier_InterpEnumAttrOperator,
        CollisionDepthVelocityMultiplier_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityMultiplier_InterpEnumAttrOperator
    PLUG_CLS = CollisionDepthVelocityMultiplier_InterpEnumPlugOperator


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


class BoundingBoxPlugOperator(CompoundPlugOperator["BoundingBoxAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boundingBoxMin", "bbmn"),
        ("boundingBoxMax", "bbmx"),
        ("boundingBoxSize", "bbsi"),
    )

    boundingBoxMin = Double3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    bbmn = boundingBoxMin

    boundingBoxMax = Double3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    bbmx = boundingBoxMax

    boundingBoxSize = Double3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    bbsi = boundingBoxSize


class BoundingBoxAttrOperator(CompoundAttrOperator[BoundingBoxPlugOperator]):
    __slots__ = ()

    boundingBoxMin = Double3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    bbmn = boundingBoxMin

    boundingBoxMax = Double3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    bbmx = boundingBoxMax

    boundingBoxSize = Double3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    bbsi = boundingBoxSize


class BoundingBoxField(
    CompoundField[BoundingBoxAttrOperator, BoundingBoxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundingBoxAttrOperator
    PLUG_CLS = BoundingBoxPlugOperator

    boundingBoxMin = Double3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    bbmn = boundingBoxMin

    boundingBoxMax = Double3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    bbmx = boundingBoxMax

    boundingBoxSize = Double3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
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
    CHILD_ATTR_NAMES = (("objectGroups", "og"),)

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
    Float3CompoundBaseField[
        ObjectColorRGBAttrOperator, ObjectColorRGBPlugOperator
    ]
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

    overrideColorA = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ovca = overrideColorA


class DrawOverrideAttrOperator(CompoundAttrOperator[DrawOverridePlugOperator]):
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

    overrideColorA = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
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

    overrideColorA = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ovca = overrideColorA


class RenderInfoPlugOperator(CompoundPlugOperator["RenderInfoAttrOperator"]):
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


class RenderInfoAttrOperator(CompoundAttrOperator[RenderInfoPlugOperator]):
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

    ghostFarOpacity = FloatField(
        default_value=0.15000000596046448, min_value=0.0, max_value=1.0
    )
    gfro = ghostFarOpacity

    ghostNearOpacity = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    gnro = ghostNearOpacity


class GhostOpacityRangeAttrOperator(
    Float2CompoundBaseAttrOperator[GhostOpacityRangePlugOperator]
):
    __slots__ = ()

    ghostFarOpacity = FloatField(
        default_value=0.15000000596046448, min_value=0.0, max_value=1.0
    )
    gfro = ghostFarOpacity

    ghostNearOpacity = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
    gnro = ghostNearOpacity


class GhostOpacityRangeField(
    Float2CompoundBaseField[
        GhostOpacityRangeAttrOperator, GhostOpacityRangePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = GhostOpacityRangeAttrOperator
    PLUG_CLS = GhostOpacityRangePlugOperator

    ghostFarOpacity = FloatField(
        default_value=0.15000000596046448, min_value=0.0, max_value=1.0
    )
    gfro = ghostFarOpacity

    ghostNearOpacity = FloatField(
        default_value=0.5, min_value=0.0, max_value=1.0
    )
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

    ghostColorPreR = FloatField(
        default_value=0.44699999690055847, min_value=0.0, max_value=1.0
    )
    grr = ghostColorPreR

    ghostColorPreG = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    gpg = ghostColorPreG

    ghostColorPreB = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    gpb = ghostColorPreB


class GhostColorPreAttrOperator(
    Float3CompoundBaseAttrOperator[GhostColorPrePlugOperator]
):
    __slots__ = ()

    ghostColorPreR = FloatField(
        default_value=0.44699999690055847, min_value=0.0, max_value=1.0
    )
    grr = ghostColorPreR

    ghostColorPreG = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    gpg = ghostColorPreG

    ghostColorPreB = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    gpb = ghostColorPreB


class GhostColorPreField(
    Float3CompoundBaseField[
        GhostColorPreAttrOperator, GhostColorPrePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = GhostColorPreAttrOperator
    PLUG_CLS = GhostColorPrePlugOperator

    ghostColorPreR = FloatField(
        default_value=0.44699999690055847, min_value=0.0, max_value=1.0
    )
    grr = ghostColorPreR

    ghostColorPreG = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    gpg = ghostColorPreG

    ghostColorPreB = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
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

    ghostColorPostR = FloatField(
        default_value=0.878000020980835, min_value=0.0, max_value=1.0
    )
    gar = ghostColorPostR

    ghostColorPostG = FloatField(
        default_value=0.6779999732971191, min_value=0.0, max_value=1.0
    )
    gag = ghostColorPostG

    ghostColorPostB = FloatField(
        default_value=0.6629999876022339, min_value=0.0, max_value=1.0
    )
    gab = ghostColorPostB


class GhostColorPostAttrOperator(
    Float3CompoundBaseAttrOperator[GhostColorPostPlugOperator]
):
    __slots__ = ()

    ghostColorPostR = FloatField(
        default_value=0.878000020980835, min_value=0.0, max_value=1.0
    )
    gar = ghostColorPostR

    ghostColorPostG = FloatField(
        default_value=0.6779999732971191, min_value=0.0, max_value=1.0
    )
    gag = ghostColorPostG

    ghostColorPostB = FloatField(
        default_value=0.6629999876022339, min_value=0.0, max_value=1.0
    )
    gab = ghostColorPostB


class GhostColorPostField(
    Float3CompoundBaseField[
        GhostColorPostAttrOperator, GhostColorPostPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = GhostColorPostAttrOperator
    PLUG_CLS = GhostColorPostPlugOperator

    ghostColorPostR = FloatField(
        default_value=0.878000020980835, min_value=0.0, max_value=1.0
    )
    gar = ghostColorPostR

    ghostColorPostG = FloatField(
        default_value=0.6779999732971191, min_value=0.0, max_value=1.0
    )
    gag = ghostColorPostG

    ghostColorPostB = FloatField(
        default_value=0.6629999876022339, min_value=0.0, max_value=1.0
    )
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
    Float3CompoundBaseField[
        OutlinerColorAttrOperator, OutlinerColorPlugOperator
    ]
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
    CHILD_ATTR_NAMES = (("compObjectGroups", "cog"),)

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


class ControlPointsPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ControlPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("xValue", "xv"),
        ("yValue", "yv"),
        ("zValue", "zv"),
    )

    xValue = DoubleLinearField(default_value=0.0)
    xv = xValue

    yValue = DoubleLinearField(default_value=0.0)
    yv = yValue

    zValue = DoubleLinearField(default_value=0.0)
    zv = zValue


class ControlPointsAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ControlPointsPlugOperator]
):
    __slots__ = ()

    xValue = DoubleLinearField(default_value=0.0)
    xv = xValue

    yValue = DoubleLinearField(default_value=0.0)
    yv = yValue

    zValue = DoubleLinearField(default_value=0.0)
    zv = zValue


class ControlPointsField(
    DoubleLinear3CompoundBaseField[
        ControlPointsAttrOperator, ControlPointsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ControlPointsAttrOperator
    PLUG_CLS = ControlPointsPlugOperator


class UvPivotPlugOperator(
    Double2CompoundBasePlugOperator["UvPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvPivotX", "pvx"),
        ("uvPivotY", "pvy"),
    )

    uvPivotX = DoubleField(default_value=0.0)
    pvx = uvPivotX

    uvPivotY = DoubleField(default_value=0.0)
    pvy = uvPivotY


class UvPivotAttrOperator(
    Double2CompoundBaseAttrOperator[UvPivotPlugOperator]
):
    __slots__ = ()

    uvPivotX = DoubleField(default_value=0.0)
    pvx = uvPivotX

    uvPivotY = DoubleField(default_value=0.0)
    pvy = uvPivotY


class UvPivotField(
    Double2CompoundBaseField[UvPivotAttrOperator, UvPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvPivotAttrOperator
    PLUG_CLS = UvPivotPlugOperator

    uvPivotX = DoubleField(default_value=0.0)
    pvx = uvPivotX

    uvPivotY = DoubleField(default_value=0.0)
    pvy = uvPivotY


class UvSetPlugOperator(CompoundPlugOperator["UvSetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvSetName", "uvsn"),
        ("uvSetPoints", "uvsp"),
        ("uvSetTweakLocation", "uvtw"),
    )

    uvSetName = DataStringField()
    uvsn = uvSetName

    uvSetPoints = Float2Field(multi=True, default_value=(0.0, 0.0))
    uvsp = uvSetPoints

    uvSetTweakLocation = TypedField(readable=False)
    uvtw = uvSetTweakLocation


class UvSetAttrOperator(CompoundAttrOperator[UvSetPlugOperator]):
    __slots__ = ()

    uvSetName = DataStringField()
    uvsn = uvSetName

    uvSetPoints = Float2Field(multi=True, default_value=(0.0, 0.0))
    uvsp = uvSetPoints

    uvSetTweakLocation = TypedField(readable=False)
    uvtw = uvSetTweakLocation


class UvSetField(CompoundField[UvSetAttrOperator, UvSetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = UvSetAttrOperator
    PLUG_CLS = UvSetPlugOperator


class ColorSetPlugOperator(CompoundPlugOperator["ColorSetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorName", "clsn"),
        ("clamped", "clam"),
        ("representation", "rprt"),
        ("colorSetPoints", "clsp"),
    )

    colorName = DataStringField()
    clsn = colorName

    clamped = BoolField(default_value=False)
    clam = clamped

    representation = RepresentationEnumField(default_value=4)
    rprt = representation

    colorSetPoints = CompoundField(
        multi=True, default_value=(0.0, 0.0, 0.0, 0.0)
    )
    clsp = colorSetPoints


class ColorSetAttrOperator(CompoundAttrOperator[ColorSetPlugOperator]):
    __slots__ = ()

    colorName = DataStringField()
    clsn = colorName

    clamped = BoolField(default_value=False)
    clam = clamped

    representation = RepresentationEnumField(default_value=4)
    rprt = representation

    colorSetPoints = CompoundField(
        multi=True, default_value=(0.0, 0.0, 0.0, 0.0)
    )
    clsp = colorSetPoints


class ColorSetField(CompoundField[ColorSetAttrOperator, ColorSetPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ColorSetAttrOperator
    PLUG_CLS = ColorSetPlugOperator


class BoundingBoxScalePlugOperator(
    Float3CompoundBasePlugOperator["BoundingBoxScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boundingBoxScaleX", "bscx"),
        ("boundingBoxScaleY", "bscy"),
        ("boundingBoxScaleZ", "bscz"),
    )

    boundingBoxScaleX = FloatField(default_value=1.5, min_value=1.0)
    bscx = boundingBoxScaleX

    boundingBoxScaleY = FloatField(default_value=1.5, min_value=1.0)
    bscy = boundingBoxScaleY

    boundingBoxScaleZ = FloatField(default_value=1.5, min_value=1.0)
    bscz = boundingBoxScaleZ


class BoundingBoxScaleAttrOperator(
    Float3CompoundBaseAttrOperator[BoundingBoxScalePlugOperator]
):
    __slots__ = ()

    boundingBoxScaleX = FloatField(default_value=1.5, min_value=1.0)
    bscx = boundingBoxScaleX

    boundingBoxScaleY = FloatField(default_value=1.5, min_value=1.0)
    bscy = boundingBoxScaleY

    boundingBoxScaleZ = FloatField(default_value=1.5, min_value=1.0)
    bscz = boundingBoxScaleZ


class BoundingBoxScaleField(
    Float3CompoundBaseField[
        BoundingBoxScaleAttrOperator, BoundingBoxScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BoundingBoxScaleAttrOperator
    PLUG_CLS = BoundingBoxScalePlugOperator

    boundingBoxScaleX = FloatField(default_value=1.5, min_value=1.0)
    bscx = boundingBoxScaleX

    boundingBoxScaleY = FloatField(default_value=1.5, min_value=1.0)
    bscy = boundingBoxScaleY

    boundingBoxScaleZ = FloatField(default_value=1.5, min_value=1.0)
    bscz = boundingBoxScaleZ


class CollisionOffsetVelocityIncrementPlugOperator(
    CompoundPlugOperator["CollisionOffsetVelocityIncrementAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionOffsetVelocityIncrement_Position", "covip"),
        ("collisionOffsetVelocityIncrement_FloatValue", "covifv"),
        ("collisionOffsetVelocityIncrement_Interp", "covii"),
    )

    collisionOffsetVelocityIncrement_Position = FloatField(default_value=0.0)
    covip = collisionOffsetVelocityIncrement_Position

    collisionOffsetVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    covifv = collisionOffsetVelocityIncrement_FloatValue

    collisionOffsetVelocityIncrement_Interp = (
        CollisionOffsetVelocityIncrement_InterpEnumField(default_value=0)
    )
    covii = collisionOffsetVelocityIncrement_Interp


class CollisionOffsetVelocityIncrementAttrOperator(
    CompoundAttrOperator[CollisionOffsetVelocityIncrementPlugOperator]
):
    __slots__ = ()

    collisionOffsetVelocityIncrement_Position = FloatField(default_value=0.0)
    covip = collisionOffsetVelocityIncrement_Position

    collisionOffsetVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    covifv = collisionOffsetVelocityIncrement_FloatValue

    collisionOffsetVelocityIncrement_Interp = (
        CollisionOffsetVelocityIncrement_InterpEnumField(default_value=0)
    )
    covii = collisionOffsetVelocityIncrement_Interp


class CollisionOffsetVelocityIncrementField(
    CompoundField[
        CollisionOffsetVelocityIncrementAttrOperator,
        CollisionOffsetVelocityIncrementPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityIncrementAttrOperator
    PLUG_CLS = CollisionOffsetVelocityIncrementPlugOperator


class CollisionDepthVelocityIncrementPlugOperator(
    CompoundPlugOperator["CollisionDepthVelocityIncrementAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionDepthVelocityIncrement_Position", "cdvip"),
        ("collisionDepthVelocityIncrement_FloatValue", "cdvifv"),
        ("collisionDepthVelocityIncrement_Interp", "cdvii"),
    )

    collisionDepthVelocityIncrement_Position = FloatField(default_value=0.0)
    cdvip = collisionDepthVelocityIncrement_Position

    collisionDepthVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    cdvifv = collisionDepthVelocityIncrement_FloatValue

    collisionDepthVelocityIncrement_Interp = (
        CollisionDepthVelocityIncrement_InterpEnumField(default_value=0)
    )
    cdvii = collisionDepthVelocityIncrement_Interp


class CollisionDepthVelocityIncrementAttrOperator(
    CompoundAttrOperator[CollisionDepthVelocityIncrementPlugOperator]
):
    __slots__ = ()

    collisionDepthVelocityIncrement_Position = FloatField(default_value=0.0)
    cdvip = collisionDepthVelocityIncrement_Position

    collisionDepthVelocityIncrement_FloatValue = FloatField(default_value=0.0)
    cdvifv = collisionDepthVelocityIncrement_FloatValue

    collisionDepthVelocityIncrement_Interp = (
        CollisionDepthVelocityIncrement_InterpEnumField(default_value=0)
    )
    cdvii = collisionDepthVelocityIncrement_Interp


class CollisionDepthVelocityIncrementField(
    CompoundField[
        CollisionDepthVelocityIncrementAttrOperator,
        CollisionDepthVelocityIncrementPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityIncrementAttrOperator
    PLUG_CLS = CollisionDepthVelocityIncrementPlugOperator


class CollisionOffsetVelocityMultiplierPlugOperator(
    CompoundPlugOperator["CollisionOffsetVelocityMultiplierAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionOffsetVelocityMultiplier_Position", "covmp"),
        ("collisionOffsetVelocityMultiplier_FloatValue", "covmfv"),
        ("collisionOffsetVelocityMultiplier_Interp", "covmi"),
    )

    collisionOffsetVelocityMultiplier_Position = FloatField(default_value=0.0)
    covmp = collisionOffsetVelocityMultiplier_Position

    collisionOffsetVelocityMultiplier_FloatValue = FloatField(
        default_value=0.0
    )
    covmfv = collisionOffsetVelocityMultiplier_FloatValue

    collisionOffsetVelocityMultiplier_Interp = (
        CollisionOffsetVelocityMultiplier_InterpEnumField(default_value=0)
    )
    covmi = collisionOffsetVelocityMultiplier_Interp


class CollisionOffsetVelocityMultiplierAttrOperator(
    CompoundAttrOperator[CollisionOffsetVelocityMultiplierPlugOperator]
):
    __slots__ = ()

    collisionOffsetVelocityMultiplier_Position = FloatField(default_value=0.0)
    covmp = collisionOffsetVelocityMultiplier_Position

    collisionOffsetVelocityMultiplier_FloatValue = FloatField(
        default_value=0.0
    )
    covmfv = collisionOffsetVelocityMultiplier_FloatValue

    collisionOffsetVelocityMultiplier_Interp = (
        CollisionOffsetVelocityMultiplier_InterpEnumField(default_value=0)
    )
    covmi = collisionOffsetVelocityMultiplier_Interp


class CollisionOffsetVelocityMultiplierField(
    CompoundField[
        CollisionOffsetVelocityMultiplierAttrOperator,
        CollisionOffsetVelocityMultiplierPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionOffsetVelocityMultiplierAttrOperator
    PLUG_CLS = CollisionOffsetVelocityMultiplierPlugOperator


class CollisionDepthVelocityMultiplierPlugOperator(
    CompoundPlugOperator["CollisionDepthVelocityMultiplierAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionDepthVelocityMultiplier_Position", "cdvmp"),
        ("collisionDepthVelocityMultiplier_FloatValue", "cdvmfv"),
        ("collisionDepthVelocityMultiplier_Interp", "cdvmi"),
    )

    collisionDepthVelocityMultiplier_Position = FloatField(default_value=0.0)
    cdvmp = collisionDepthVelocityMultiplier_Position

    collisionDepthVelocityMultiplier_FloatValue = FloatField(default_value=0.0)
    cdvmfv = collisionDepthVelocityMultiplier_FloatValue

    collisionDepthVelocityMultiplier_Interp = (
        CollisionDepthVelocityMultiplier_InterpEnumField(default_value=0)
    )
    cdvmi = collisionDepthVelocityMultiplier_Interp


class CollisionDepthVelocityMultiplierAttrOperator(
    CompoundAttrOperator[CollisionDepthVelocityMultiplierPlugOperator]
):
    __slots__ = ()

    collisionDepthVelocityMultiplier_Position = FloatField(default_value=0.0)
    cdvmp = collisionDepthVelocityMultiplier_Position

    collisionDepthVelocityMultiplier_FloatValue = FloatField(default_value=0.0)
    cdvmfv = collisionDepthVelocityMultiplier_FloatValue

    collisionDepthVelocityMultiplier_Interp = (
        CollisionDepthVelocityMultiplier_InterpEnumField(default_value=0)
    )
    cdvmi = collisionDepthVelocityMultiplier_Interp


class CollisionDepthVelocityMultiplierField(
    CompoundField[
        CollisionDepthVelocityMultiplierAttrOperator,
        CollisionDepthVelocityMultiplierPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollisionDepthVelocityMultiplierAttrOperator
    PLUG_CLS = CollisionDepthVelocityMultiplierPlugOperator


class SmoothOffsetPlugOperator(
    Float3CompoundBasePlugOperator["SmoothOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sofx", "sx"),
        ("sofy", "sy"),
        ("sofz", "sz"),
    )

    sofx = FloatField(default_value=0.0)
    sx = sofx

    sofy = FloatField(default_value=0.0)
    sy = sofy

    sofz = FloatField(default_value=0.0)
    sz = sofz


class SmoothOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[SmoothOffsetPlugOperator]
):
    __slots__ = ()

    sofx = FloatField(default_value=0.0)
    sx = sofx

    sofy = FloatField(default_value=0.0)
    sy = sofy

    sofz = FloatField(default_value=0.0)
    sz = sofz


class SmoothOffsetField(
    Float3CompoundBaseField[SmoothOffsetAttrOperator, SmoothOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SmoothOffsetAttrOperator
    PLUG_CLS = SmoothOffsetPlugOperator

    sofx = FloatField(default_value=0.0)
    sx = sofx

    sofy = FloatField(default_value=0.0)
    sy = sofy

    sofz = FloatField(default_value=0.0)
    sz = sofz


class PntsPlugOperator(
    FloatLinear3CompoundBasePlugOperator["PntsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pntx", "px"),
        ("pnty", "py"),
        ("pntz", "pz"),
    )

    pntx = FloatLinearField(default_value=0.0)
    px = pntx

    pnty = FloatLinearField(default_value=0.0)
    py = pnty

    pntz = FloatLinearField(default_value=0.0)
    pz = pntz


class PntsAttrOperator(FloatLinear3CompoundBaseAttrOperator[PntsPlugOperator]):
    __slots__ = ()

    pntx = FloatLinearField(default_value=0.0)
    px = pntx

    pnty = FloatLinearField(default_value=0.0)
    py = pnty

    pntz = FloatLinearField(default_value=0.0)
    pz = pntz


class PntsField(
    FloatLinear3CompoundBaseField[PntsAttrOperator, PntsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PntsAttrOperator
    PLUG_CLS = PntsPlugOperator


class VrtsPlugOperator(Float3CompoundBasePlugOperator["VrtsAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vrtx", "vx"),
        ("vrty", "vy"),
        ("vrtz", "vz"),
    )

    vrtx = FloatField(default_value=0.0)
    vx = vrtx

    vrty = FloatField(default_value=0.0)
    vy = vrty

    vrtz = FloatField(default_value=0.0)
    vz = vrtz


class VrtsAttrOperator(Float3CompoundBaseAttrOperator[VrtsPlugOperator]):
    __slots__ = ()

    vrtx = FloatField(default_value=0.0)
    vx = vrtx

    vrty = FloatField(default_value=0.0)
    vy = vrty

    vrtz = FloatField(default_value=0.0)
    vz = vrtz


class VrtsField(Float3CompoundBaseField[VrtsAttrOperator, VrtsPlugOperator]):
    __slots__ = ()

    ATTR_CLS = VrtsAttrOperator
    PLUG_CLS = VrtsPlugOperator


class EdgePlugOperator(Long3CompoundBasePlugOperator["EdgeAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("edg1", "e1"),
        ("edg2", "e2"),
        ("edgh", "eh"),
    )

    edg1 = LongField(default_value=0)
    e1 = edg1

    edg2 = LongField(default_value=0)
    e2 = edg2

    edgh = LongField(default_value=0)
    eh = edgh


class EdgeAttrOperator(Long3CompoundBaseAttrOperator[EdgePlugOperator]):
    __slots__ = ()

    edg1 = LongField(default_value=0)
    e1 = edg1

    edg2 = LongField(default_value=0)
    e2 = edg2

    edgh = LongField(default_value=0)
    eh = edgh


class EdgeField(Long3CompoundBaseField[EdgeAttrOperator, EdgePlugOperator]):
    __slots__ = ()

    ATTR_CLS = EdgeAttrOperator
    PLUG_CLS = EdgePlugOperator


class UvptPlugOperator(Float2CompoundBasePlugOperator["UvptAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvpx", "ux"),
        ("uvpy", "uy"),
    )

    uvpx = FloatField(default_value=0.0)
    ux = uvpx

    uvpy = FloatField(default_value=0.0)
    uy = uvpy


class UvptAttrOperator(Float2CompoundBaseAttrOperator[UvptPlugOperator]):
    __slots__ = ()

    uvpx = FloatField(default_value=0.0)
    ux = uvpx

    uvpy = FloatField(default_value=0.0)
    uy = uvpy


class UvptField(Float2CompoundBaseField[UvptAttrOperator, UvptPlugOperator]):
    __slots__ = ()

    ATTR_CLS = UvptAttrOperator
    PLUG_CLS = UvptPlugOperator


class ColorsPlugOperator(CompoundPlugOperator["ColorsAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "clrr"),
        ("colorG", "clrg"),
        ("colorB", "clrb"),
        ("colorA", "clra"),
    )

    colorR = FloatField(default_value=0.0)
    clrr = colorR

    colorG = FloatField(default_value=0.0)
    clrg = colorG

    colorB = FloatField(default_value=0.0)
    clrb = colorB

    colorA = FloatField(default_value=0.0)
    clra = colorA


class ColorsAttrOperator(CompoundAttrOperator[ColorsPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.0)
    clrr = colorR

    colorG = FloatField(default_value=0.0)
    clrg = colorG

    colorB = FloatField(default_value=0.0)
    clrb = colorB

    colorA = FloatField(default_value=0.0)
    clra = colorA


class ColorsField(CompoundField[ColorsAttrOperator, ColorsPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ColorsAttrOperator
    PLUG_CLS = ColorsPlugOperator


class NormalsPlugOperator(
    Float3CompoundBasePlugOperator["NormalsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalx", "nx"),
        ("normaly", "ny"),
        ("normalz", "nz"),
    )

    normalx = FloatField(default_value=1.0000000200408773e20)
    nx = normalx

    normaly = FloatField(default_value=1.0000000200408773e20)
    ny = normaly

    normalz = FloatField(default_value=1.0000000200408773e20)
    nz = normalz


class NormalsAttrOperator(Float3CompoundBaseAttrOperator[NormalsPlugOperator]):
    __slots__ = ()

    normalx = FloatField(default_value=1.0000000200408773e20)
    nx = normalx

    normaly = FloatField(default_value=1.0000000200408773e20)
    ny = normaly

    normalz = FloatField(default_value=1.0000000200408773e20)
    nz = normalz


class NormalsField(
    Float3CompoundBaseField[NormalsAttrOperator, NormalsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalsAttrOperator
    PLUG_CLS = NormalsPlugOperator


class ColorPerVertexPlugOperator(
    CompoundPlugOperator["ColorPerVertexAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("vertexColor", "vclr"),)

    vertexColor = CompoundField(multi=True)
    vclr = vertexColor


class ColorPerVertexAttrOperator(
    CompoundAttrOperator[ColorPerVertexPlugOperator]
):
    __slots__ = ()

    vertexColor = CompoundField(multi=True)
    vclr = vertexColor


class ColorPerVertexField(
    CompoundField[ColorPerVertexAttrOperator, ColorPerVertexPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorPerVertexAttrOperator
    PLUG_CLS = ColorPerVertexPlugOperator

    vertexColor = CompoundField(multi=True)
    vclr = vertexColor


class NormalPerVertexPlugOperator(
    CompoundPlugOperator["NormalPerVertexAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("vertexNormal", "vn"),)

    vertexNormal = CompoundField(multi=True)
    vn = vertexNormal


class NormalPerVertexAttrOperator(
    CompoundAttrOperator[NormalPerVertexPlugOperator]
):
    __slots__ = ()

    vertexNormal = CompoundField(multi=True)
    vn = vertexNormal


class NormalPerVertexField(
    CompoundField[NormalPerVertexAttrOperator, NormalPerVertexPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalPerVertexAttrOperator
    PLUG_CLS = NormalPerVertexPlugOperator

    vertexNormal = CompoundField(multi=True)
    vn = vertexNormal


class AiShadowColorPlugOperator(
    Float3CompoundBasePlugOperator["AiShadowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiShadowColorR", "ai_shadow_colorr"),
        ("aiShadowColorG", "ai_shadow_colorg"),
        ("aiShadowColorB", "ai_shadow_colorb"),
    )

    aiShadowColorR = FloatField(default_value=0.0)
    ai_shadow_colorr = aiShadowColorR

    aiShadowColorG = FloatField(default_value=0.0)
    ai_shadow_colorg = aiShadowColorG

    aiShadowColorB = FloatField(default_value=0.0)
    ai_shadow_colorb = aiShadowColorB


class AiShadowColorAttrOperator(
    Float3CompoundBaseAttrOperator[AiShadowColorPlugOperator]
):
    __slots__ = ()

    aiShadowColorR = FloatField(default_value=0.0)
    ai_shadow_colorr = aiShadowColorR

    aiShadowColorG = FloatField(default_value=0.0)
    ai_shadow_colorg = aiShadowColorG

    aiShadowColorB = FloatField(default_value=0.0)
    ai_shadow_colorb = aiShadowColorB


class AiShadowColorField(
    Float3CompoundBaseField[
        AiShadowColorAttrOperator, AiShadowColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiShadowColorAttrOperator
    PLUG_CLS = AiShadowColorPlugOperator

    aiShadowColorR = FloatField(default_value=0.0)
    ai_shadow_colorr = aiShadowColorR

    aiShadowColorG = FloatField(default_value=0.0)
    ai_shadow_colorg = aiShadowColorG

    aiShadowColorB = FloatField(default_value=0.0)
    ai_shadow_colorb = aiShadowColorB


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorRed", "scr"),
        ("colorGreen", "scg"),
        ("colorBlue", "scb"),
    )

    colorRed = FloatField(default_value=1.0)
    scr = colorRed

    colorGreen = FloatField(default_value=1.0)
    scg = colorGreen

    colorBlue = FloatField(default_value=1.0)
    scb = colorBlue


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorRed = FloatField(default_value=1.0)
    scr = colorRed

    colorGreen = FloatField(default_value=1.0)
    scg = colorGreen

    colorBlue = FloatField(default_value=1.0)
    scb = colorBlue


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorRed = FloatField(default_value=1.0)
    scr = colorRed

    colorGreen = FloatField(default_value=1.0)
    scg = colorGreen

    colorBlue = FloatField(default_value=1.0)
    scb = colorBlue
