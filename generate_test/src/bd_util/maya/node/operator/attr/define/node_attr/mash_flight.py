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
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.byte import ByteField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.numeric_scalar_range.short import ShortField
from ..std.at.typed import TypedField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
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


class AlignRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class AlignRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class AlignRamp_InterpEnumField(
    EnumField[AlignRamp_InterpEnumAttrOperator, AlignRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlignRamp_InterpEnumAttrOperator
    PLUG_CLS = AlignRamp_InterpEnumPlugOperator


class CohereRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CohereRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class CohereRamp_InterpEnumField(
    EnumField[CohereRamp_InterpEnumAttrOperator, CohereRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CohereRamp_InterpEnumAttrOperator
    PLUG_CLS = CohereRamp_InterpEnumPlugOperator


class SeparateRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class SeparateRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class SeparateRamp_InterpEnumField(
    EnumField[SeparateRamp_InterpEnumAttrOperator, SeparateRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SeparateRamp_InterpEnumAttrOperator
    PLUG_CLS = SeparateRamp_InterpEnumPlugOperator


class ObstacleRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ObstacleRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class ObstacleRamp_InterpEnumField(
    EnumField[ObstacleRamp_InterpEnumAttrOperator, ObstacleRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ObstacleRamp_InterpEnumAttrOperator
    PLUG_CLS = ObstacleRamp_InterpEnumPlugOperator


class AttractorRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class AttractorRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class AttractorRamp_InterpEnumField(
    EnumField[AttractorRamp_InterpEnumAttrOperator, AttractorRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttractorRamp_InterpEnumAttrOperator
    PLUG_CLS = AttractorRamp_InterpEnumPlugOperator


class PredatorAndPreyRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class PredatorAndPreyRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class PredatorAndPreyRamp_InterpEnumField(
    EnumField[PredatorAndPreyRamp_InterpEnumAttrOperator, PredatorAndPreyRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PredatorAndPreyRamp_InterpEnumAttrOperator
    PLUG_CLS = PredatorAndPreyRamp_InterpEnumPlugOperator


class GravityRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class GravityRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class GravityRamp_InterpEnumField(
    EnumField[GravityRamp_InterpEnumAttrOperator, GravityRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GravityRamp_InterpEnumAttrOperator
    PLUG_CLS = GravityRamp_InterpEnumPlugOperator


class ArrivalRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ArrivalRamp_InterpEnumAttrOperator(EnumAttrOperator):
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


class ArrivalRamp_InterpEnumField(
    EnumField[ArrivalRamp_InterpEnumAttrOperator, ArrivalRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ArrivalRamp_InterpEnumAttrOperator
    PLUG_CLS = ArrivalRamp_InterpEnumPlugOperator


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


class InertiaPlugOperator(
    Float3CompoundBasePlugOperator["InertiaAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inertia0", "inertia0"),
        ("inertia1", "inertia1"),
        ("inertia2", "inertia2"),
    )

    inertia0 = FloatField(default_value=0.0)

    inertia1 = FloatField(default_value=0.0)

    inertia2 = FloatField(default_value=0.0)


class InertiaAttrOperator(
    Float3CompoundBaseAttrOperator[InertiaPlugOperator]
):
    __slots__ = ()

    inertia0 = FloatField(default_value=0.0)

    inertia1 = FloatField(default_value=0.0)

    inertia2 = FloatField(default_value=0.0)


class InertiaField(
    Float3CompoundBaseField[InertiaAttrOperator, InertiaPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InertiaAttrOperator
    PLUG_CLS = InertiaPlugOperator

    inertia0 = FloatField(default_value=0.0)

    inertia1 = FloatField(default_value=0.0)

    inertia2 = FloatField(default_value=0.0)


class AlignRampPlugOperator(
    CompoundPlugOperator["AlignRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("alignRamp_Position", "alignRampp"),
        ("alignRamp_FloatValue", "alignRampfv"),
        ("alignRamp_Interp", "alignRampi"),
    )

    alignRamp_Position = FloatField(default_value=0.0)
    alignRampp = alignRamp_Position

    alignRamp_FloatValue = FloatField(default_value=0.0)
    alignRampfv = alignRamp_FloatValue

    alignRamp_Interp = AlignRamp_InterpEnumField(default_value=1)
    alignRampi = alignRamp_Interp


class AlignRampAttrOperator(
    CompoundAttrOperator[AlignRampPlugOperator]
):
    __slots__ = ()

    alignRamp_Position = FloatField(default_value=0.0)
    alignRampp = alignRamp_Position

    alignRamp_FloatValue = FloatField(default_value=0.0)
    alignRampfv = alignRamp_FloatValue

    alignRamp_Interp = AlignRamp_InterpEnumField(default_value=1)
    alignRampi = alignRamp_Interp


class AlignRampField(
    CompoundField[AlignRampAttrOperator, AlignRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlignRampAttrOperator
    PLUG_CLS = AlignRampPlugOperator


class CohereRampPlugOperator(
    CompoundPlugOperator["CohereRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cohereRamp_Position", "cohereRampp"),
        ("cohereRamp_FloatValue", "cohereRampfv"),
        ("cohereRamp_Interp", "cohereRampi"),
    )

    cohereRamp_Position = FloatField(default_value=0.0)
    cohereRampp = cohereRamp_Position

    cohereRamp_FloatValue = FloatField(default_value=0.0)
    cohereRampfv = cohereRamp_FloatValue

    cohereRamp_Interp = CohereRamp_InterpEnumField(default_value=1)
    cohereRampi = cohereRamp_Interp


class CohereRampAttrOperator(
    CompoundAttrOperator[CohereRampPlugOperator]
):
    __slots__ = ()

    cohereRamp_Position = FloatField(default_value=0.0)
    cohereRampp = cohereRamp_Position

    cohereRamp_FloatValue = FloatField(default_value=0.0)
    cohereRampfv = cohereRamp_FloatValue

    cohereRamp_Interp = CohereRamp_InterpEnumField(default_value=1)
    cohereRampi = cohereRamp_Interp


class CohereRampField(
    CompoundField[CohereRampAttrOperator, CohereRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CohereRampAttrOperator
    PLUG_CLS = CohereRampPlugOperator


class SeparateRampPlugOperator(
    CompoundPlugOperator["SeparateRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("separateRamp_Position", "separateRampp"),
        ("separateRamp_FloatValue", "separateRampfv"),
        ("separateRamp_Interp", "separateRampi"),
    )

    separateRamp_Position = FloatField(default_value=0.0)
    separateRampp = separateRamp_Position

    separateRamp_FloatValue = FloatField(default_value=0.0)
    separateRampfv = separateRamp_FloatValue

    separateRamp_Interp = SeparateRamp_InterpEnumField(default_value=1)
    separateRampi = separateRamp_Interp


class SeparateRampAttrOperator(
    CompoundAttrOperator[SeparateRampPlugOperator]
):
    __slots__ = ()

    separateRamp_Position = FloatField(default_value=0.0)
    separateRampp = separateRamp_Position

    separateRamp_FloatValue = FloatField(default_value=0.0)
    separateRampfv = separateRamp_FloatValue

    separateRamp_Interp = SeparateRamp_InterpEnumField(default_value=1)
    separateRampi = separateRamp_Interp


class SeparateRampField(
    CompoundField[SeparateRampAttrOperator, SeparateRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SeparateRampAttrOperator
    PLUG_CLS = SeparateRampPlugOperator


class ObstacleRampPlugOperator(
    CompoundPlugOperator["ObstacleRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("obstacleRamp_Position", "obstacleRampp"),
        ("obstacleRamp_FloatValue", "obstacleRampfv"),
        ("obstacleRamp_Interp", "obstacleRampi"),
    )

    obstacleRamp_Position = FloatField(default_value=0.0)
    obstacleRampp = obstacleRamp_Position

    obstacleRamp_FloatValue = FloatField(default_value=0.0)
    obstacleRampfv = obstacleRamp_FloatValue

    obstacleRamp_Interp = ObstacleRamp_InterpEnumField(default_value=1)
    obstacleRampi = obstacleRamp_Interp


class ObstacleRampAttrOperator(
    CompoundAttrOperator[ObstacleRampPlugOperator]
):
    __slots__ = ()

    obstacleRamp_Position = FloatField(default_value=0.0)
    obstacleRampp = obstacleRamp_Position

    obstacleRamp_FloatValue = FloatField(default_value=0.0)
    obstacleRampfv = obstacleRamp_FloatValue

    obstacleRamp_Interp = ObstacleRamp_InterpEnumField(default_value=1)
    obstacleRampi = obstacleRamp_Interp


class ObstacleRampField(
    CompoundField[ObstacleRampAttrOperator, ObstacleRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ObstacleRampAttrOperator
    PLUG_CLS = ObstacleRampPlugOperator


class AttractorRampPlugOperator(
    CompoundPlugOperator["AttractorRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attractorRamp_Position", "attractorRampp"),
        ("attractorRamp_FloatValue", "attractorRampfv"),
        ("attractorRamp_Interp", "attractorRampi"),
    )

    attractorRamp_Position = FloatField(default_value=0.0)
    attractorRampp = attractorRamp_Position

    attractorRamp_FloatValue = FloatField(default_value=0.0)
    attractorRampfv = attractorRamp_FloatValue

    attractorRamp_Interp = AttractorRamp_InterpEnumField(default_value=1)
    attractorRampi = attractorRamp_Interp


class AttractorRampAttrOperator(
    CompoundAttrOperator[AttractorRampPlugOperator]
):
    __slots__ = ()

    attractorRamp_Position = FloatField(default_value=0.0)
    attractorRampp = attractorRamp_Position

    attractorRamp_FloatValue = FloatField(default_value=0.0)
    attractorRampfv = attractorRamp_FloatValue

    attractorRamp_Interp = AttractorRamp_InterpEnumField(default_value=1)
    attractorRampi = attractorRamp_Interp


class AttractorRampField(
    CompoundField[AttractorRampAttrOperator, AttractorRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttractorRampAttrOperator
    PLUG_CLS = AttractorRampPlugOperator


class PredatorAndPreyRampPlugOperator(
    CompoundPlugOperator["PredatorAndPreyRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("predatorAndPreyRamp_Position", "predatorAndPreyRampp"),
        ("predatorAndPreyRamp_FloatValue", "predatorAndPreyRampfv"),
        ("predatorAndPreyRamp_Interp", "predatorAndPreyRampi"),
    )

    predatorAndPreyRamp_Position = FloatField(default_value=0.0)
    predatorAndPreyRampp = predatorAndPreyRamp_Position

    predatorAndPreyRamp_FloatValue = FloatField(default_value=0.0)
    predatorAndPreyRampfv = predatorAndPreyRamp_FloatValue

    predatorAndPreyRamp_Interp = PredatorAndPreyRamp_InterpEnumField(default_value=1)
    predatorAndPreyRampi = predatorAndPreyRamp_Interp


class PredatorAndPreyRampAttrOperator(
    CompoundAttrOperator[PredatorAndPreyRampPlugOperator]
):
    __slots__ = ()

    predatorAndPreyRamp_Position = FloatField(default_value=0.0)
    predatorAndPreyRampp = predatorAndPreyRamp_Position

    predatorAndPreyRamp_FloatValue = FloatField(default_value=0.0)
    predatorAndPreyRampfv = predatorAndPreyRamp_FloatValue

    predatorAndPreyRamp_Interp = PredatorAndPreyRamp_InterpEnumField(default_value=1)
    predatorAndPreyRampi = predatorAndPreyRamp_Interp


class PredatorAndPreyRampField(
    CompoundField[PredatorAndPreyRampAttrOperator, PredatorAndPreyRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PredatorAndPreyRampAttrOperator
    PLUG_CLS = PredatorAndPreyRampPlugOperator


class GravityRampPlugOperator(
    CompoundPlugOperator["GravityRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("gravityRamp_Position", "gravityRampp"),
        ("gravityRamp_FloatValue", "gravityRampfv"),
        ("gravityRamp_Interp", "gravityRampi"),
    )

    gravityRamp_Position = FloatField(default_value=0.0)
    gravityRampp = gravityRamp_Position

    gravityRamp_FloatValue = FloatField(default_value=0.0)
    gravityRampfv = gravityRamp_FloatValue

    gravityRamp_Interp = GravityRamp_InterpEnumField(default_value=1)
    gravityRampi = gravityRamp_Interp


class GravityRampAttrOperator(
    CompoundAttrOperator[GravityRampPlugOperator]
):
    __slots__ = ()

    gravityRamp_Position = FloatField(default_value=0.0)
    gravityRampp = gravityRamp_Position

    gravityRamp_FloatValue = FloatField(default_value=0.0)
    gravityRampfv = gravityRamp_FloatValue

    gravityRamp_Interp = GravityRamp_InterpEnumField(default_value=1)
    gravityRampi = gravityRamp_Interp


class GravityRampField(
    CompoundField[GravityRampAttrOperator, GravityRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GravityRampAttrOperator
    PLUG_CLS = GravityRampPlugOperator


class ArrivalRampPlugOperator(
    CompoundPlugOperator["ArrivalRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("arrivalRamp_Position", "arrivalRampp"),
        ("arrivalRamp_FloatValue", "arrivalRampfv"),
        ("arrivalRamp_Interp", "arrivalRampi"),
    )

    arrivalRamp_Position = FloatField(default_value=0.0)
    arrivalRampp = arrivalRamp_Position

    arrivalRamp_FloatValue = FloatField(default_value=0.0)
    arrivalRampfv = arrivalRamp_FloatValue

    arrivalRamp_Interp = ArrivalRamp_InterpEnumField(default_value=1)
    arrivalRampi = arrivalRamp_Interp


class ArrivalRampAttrOperator(
    CompoundAttrOperator[ArrivalRampPlugOperator]
):
    __slots__ = ()

    arrivalRamp_Position = FloatField(default_value=0.0)
    arrivalRampp = arrivalRamp_Position

    arrivalRamp_FloatValue = FloatField(default_value=0.0)
    arrivalRampfv = arrivalRamp_FloatValue

    arrivalRamp_Interp = ArrivalRamp_InterpEnumField(default_value=1)
    arrivalRampi = arrivalRamp_Interp


class ArrivalRampField(
    CompoundField[ArrivalRampAttrOperator, ArrivalRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ArrivalRampAttrOperator
    PLUG_CLS = ArrivalRampPlugOperator


class FalloffObjectPlugOperator(
    Float3CompoundBasePlugOperator["FalloffObjectAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffObjectX", "fallObjx"),
        ("falloffObjectY", "fallObjy"),
        ("falloffObjectZ", "fallObjz"),
    )

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ


class FalloffObjectAttrOperator(
    Float3CompoundBaseAttrOperator[FalloffObjectPlugOperator]
):
    __slots__ = ()

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ


class FalloffObjectField(
    Float3CompoundBaseField[FalloffObjectAttrOperator, FalloffObjectPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffObjectAttrOperator
    PLUG_CLS = FalloffObjectPlugOperator

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ


class ObstaclesPlugOperator(
    Float3CompoundBasePlugOperator["ObstaclesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("obstacles0", "obstacles0"),
        ("obstacles1", "obstacles1"),
        ("obstacles2", "obstacles2"),
    )

    obstacles0 = FloatField(default_value=0.0)

    obstacles1 = FloatField(default_value=0.0)

    obstacles2 = FloatField(default_value=0.0)


class ObstaclesAttrOperator(
    Float3CompoundBaseAttrOperator[ObstaclesPlugOperator]
):
    __slots__ = ()

    obstacles0 = FloatField(default_value=0.0)

    obstacles1 = FloatField(default_value=0.0)

    obstacles2 = FloatField(default_value=0.0)


class ObstaclesField(
    Float3CompoundBaseField[ObstaclesAttrOperator, ObstaclesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ObstaclesAttrOperator
    PLUG_CLS = ObstaclesPlugOperator


class GravitateLocationPlugOperator(
    Float3CompoundBasePlugOperator["GravitateLocationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("gravitateLocation0", "gravitateLocation0"),
        ("gravitateLocation1", "gravitateLocation1"),
        ("gravitateLocation2", "gravitateLocation2"),
    )

    gravitateLocation0 = FloatField(default_value=0.0)

    gravitateLocation1 = FloatField(default_value=0.0)

    gravitateLocation2 = FloatField(default_value=0.0)


class GravitateLocationAttrOperator(
    Float3CompoundBaseAttrOperator[GravitateLocationPlugOperator]
):
    __slots__ = ()

    gravitateLocation0 = FloatField(default_value=0.0)

    gravitateLocation1 = FloatField(default_value=0.0)

    gravitateLocation2 = FloatField(default_value=0.0)


class GravitateLocationField(
    Float3CompoundBaseField[GravitateLocationAttrOperator, GravitateLocationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GravitateLocationAttrOperator
    PLUG_CLS = GravitateLocationPlugOperator

    gravitateLocation0 = FloatField(default_value=0.0)

    gravitateLocation1 = FloatField(default_value=0.0)

    gravitateLocation2 = FloatField(default_value=0.0)


class TargetsPlugOperator(
    Float3CompoundBasePlugOperator["TargetsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targets0", "targets0"),
        ("targets1", "targets1"),
        ("targets2", "targets2"),
    )

    targets0 = FloatField(default_value=0.0)

    targets1 = FloatField(default_value=0.0)

    targets2 = FloatField(default_value=0.0)


class TargetsAttrOperator(
    Float3CompoundBaseAttrOperator[TargetsPlugOperator]
):
    __slots__ = ()

    targets0 = FloatField(default_value=0.0)

    targets1 = FloatField(default_value=0.0)

    targets2 = FloatField(default_value=0.0)


class TargetsField(
    Float3CompoundBaseField[TargetsAttrOperator, TargetsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetsAttrOperator
    PLUG_CLS = TargetsPlugOperator


class UpVectorPlugOperator(
    Float3CompoundBasePlugOperator["UpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("upVector0", "upVector0"),
        ("upVector1", "upVector1"),
        ("upVector2", "upVector2"),
    )

    upVector0 = FloatField(default_value=0.0)

    upVector1 = FloatField(default_value=1.0)

    upVector2 = FloatField(default_value=0.0)


class UpVectorAttrOperator(
    Float3CompoundBaseAttrOperator[UpVectorPlugOperator]
):
    __slots__ = ()

    upVector0 = FloatField(default_value=0.0)

    upVector1 = FloatField(default_value=1.0)

    upVector2 = FloatField(default_value=0.0)


class UpVectorField(
    Float3CompoundBaseField[UpVectorAttrOperator, UpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpVectorAttrOperator
    PLUG_CLS = UpVectorPlugOperator

    upVector0 = FloatField(default_value=0.0)

    upVector1 = FloatField(default_value=1.0)

    upVector2 = FloatField(default_value=0.0)
