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
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.numeric_scalar_range.short import ShortField
from ..std.at.typed import TypedField
from ..std.at.unit_scalar.time import TimeField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.string import DataStringField
from ..std.dt.vector_array import DataVectorArrayField
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


class StiffnessScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class StiffnessScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class StiffnessScale_InterpEnumField(
    EnumField[StiffnessScale_InterpEnumAttrOperator, StiffnessScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StiffnessScale_InterpEnumAttrOperator
    PLUG_CLS = StiffnessScale_InterpEnumPlugOperator


class AttractionScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class AttractionScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class AttractionScale_InterpEnumField(
    EnumField[AttractionScale_InterpEnumAttrOperator, AttractionScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttractionScale_InterpEnumAttrOperator
    PLUG_CLS = AttractionScale_InterpEnumPlugOperator


class ClumpWidthScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ClumpWidthScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class ClumpWidthScale_InterpEnumField(
    EnumField[ClumpWidthScale_InterpEnumAttrOperator, ClumpWidthScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpWidthScale_InterpEnumAttrOperator
    PLUG_CLS = ClumpWidthScale_InterpEnumPlugOperator


class ClumpCurl_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ClumpCurl_InterpEnumAttrOperator(EnumAttrOperator):
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


class ClumpCurl_InterpEnumField(
    EnumField[ClumpCurl_InterpEnumAttrOperator, ClumpCurl_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpCurl_InterpEnumAttrOperator
    PLUG_CLS = ClumpCurl_InterpEnumPlugOperator


class ClumpFlatness_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ClumpFlatness_InterpEnumAttrOperator(EnumAttrOperator):
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


class ClumpFlatness_InterpEnumField(
    EnumField[ClumpFlatness_InterpEnumAttrOperator, ClumpFlatness_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpFlatness_InterpEnumAttrOperator
    PLUG_CLS = ClumpFlatness_InterpEnumPlugOperator


class HairWidthScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class HairWidthScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class HairWidthScale_InterpEnumField(
    EnumField[HairWidthScale_InterpEnumAttrOperator, HairWidthScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HairWidthScale_InterpEnumAttrOperator
    PLUG_CLS = HairWidthScale_InterpEnumPlugOperator


class HairColorScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class HairColorScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class HairColorScale_InterpEnumField(
    EnumField[HairColorScale_InterpEnumAttrOperator, HairColorScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HairColorScale_InterpEnumAttrOperator
    PLUG_CLS = HairColorScale_InterpEnumPlugOperator


class DisplacementScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class DisplacementScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class DisplacementScale_InterpEnumField(
    EnumField[DisplacementScale_InterpEnumAttrOperator, DisplacementScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplacementScale_InterpEnumAttrOperator
    PLUG_CLS = DisplacementScale_InterpEnumPlugOperator


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


class StiffnessScalePlugOperator(
    CompoundPlugOperator["StiffnessScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("stiffnessScale_Position", "stsp"),
        ("stiffnessScale_FloatValue", "stsfv"),
        ("stiffnessScale_Interp", "stsi"),
    )

    stiffnessScale_Position = FloatField(default_value=0.0)
    stsp = stiffnessScale_Position

    stiffnessScale_FloatValue = FloatField(default_value=0.0)
    stsfv = stiffnessScale_FloatValue

    stiffnessScale_Interp = StiffnessScale_InterpEnumField(default_value=0)
    stsi = stiffnessScale_Interp


class StiffnessScaleAttrOperator(
    CompoundAttrOperator[StiffnessScalePlugOperator]
):
    __slots__ = ()

    stiffnessScale_Position = FloatField(default_value=0.0)
    stsp = stiffnessScale_Position

    stiffnessScale_FloatValue = FloatField(default_value=0.0)
    stsfv = stiffnessScale_FloatValue

    stiffnessScale_Interp = StiffnessScale_InterpEnumField(default_value=0)
    stsi = stiffnessScale_Interp


class StiffnessScaleField(
    CompoundField[StiffnessScaleAttrOperator, StiffnessScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StiffnessScaleAttrOperator
    PLUG_CLS = StiffnessScalePlugOperator


class AttractionScalePlugOperator(
    CompoundPlugOperator["AttractionScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("attractionScale_Position", "atsp"),
        ("attractionScale_FloatValue", "atsfv"),
        ("attractionScale_Interp", "atsi"),
    )

    attractionScale_Position = FloatField(default_value=0.0)
    atsp = attractionScale_Position

    attractionScale_FloatValue = FloatField(default_value=0.0)
    atsfv = attractionScale_FloatValue

    attractionScale_Interp = AttractionScale_InterpEnumField(default_value=0)
    atsi = attractionScale_Interp


class AttractionScaleAttrOperator(
    CompoundAttrOperator[AttractionScalePlugOperator]
):
    __slots__ = ()

    attractionScale_Position = FloatField(default_value=0.0)
    atsp = attractionScale_Position

    attractionScale_FloatValue = FloatField(default_value=0.0)
    atsfv = attractionScale_FloatValue

    attractionScale_Interp = AttractionScale_InterpEnumField(default_value=0)
    atsi = attractionScale_Interp


class AttractionScaleField(
    CompoundField[AttractionScaleAttrOperator, AttractionScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttractionScaleAttrOperator
    PLUG_CLS = AttractionScalePlugOperator


class ClumpWidthScalePlugOperator(
    CompoundPlugOperator["ClumpWidthScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clumpWidthScale_Position", "cwsp"),
        ("clumpWidthScale_FloatValue", "cwsfv"),
        ("clumpWidthScale_Interp", "cwsi"),
    )

    clumpWidthScale_Position = FloatField(default_value=0.0)
    cwsp = clumpWidthScale_Position

    clumpWidthScale_FloatValue = FloatField(default_value=0.0)
    cwsfv = clumpWidthScale_FloatValue

    clumpWidthScale_Interp = ClumpWidthScale_InterpEnumField(default_value=0)
    cwsi = clumpWidthScale_Interp


class ClumpWidthScaleAttrOperator(
    CompoundAttrOperator[ClumpWidthScalePlugOperator]
):
    __slots__ = ()

    clumpWidthScale_Position = FloatField(default_value=0.0)
    cwsp = clumpWidthScale_Position

    clumpWidthScale_FloatValue = FloatField(default_value=0.0)
    cwsfv = clumpWidthScale_FloatValue

    clumpWidthScale_Interp = ClumpWidthScale_InterpEnumField(default_value=0)
    cwsi = clumpWidthScale_Interp


class ClumpWidthScaleField(
    CompoundField[ClumpWidthScaleAttrOperator, ClumpWidthScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpWidthScaleAttrOperator
    PLUG_CLS = ClumpWidthScalePlugOperator


class ClumpCurlPlugOperator(
    CompoundPlugOperator["ClumpCurlAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clumpCurl_Position", "clcp"),
        ("clumpCurl_FloatValue", "clcfv"),
        ("clumpCurl_Interp", "clci"),
    )

    clumpCurl_Position = FloatField(default_value=0.0)
    clcp = clumpCurl_Position

    clumpCurl_FloatValue = FloatField(default_value=0.0)
    clcfv = clumpCurl_FloatValue

    clumpCurl_Interp = ClumpCurl_InterpEnumField(default_value=0)
    clci = clumpCurl_Interp


class ClumpCurlAttrOperator(
    CompoundAttrOperator[ClumpCurlPlugOperator]
):
    __slots__ = ()

    clumpCurl_Position = FloatField(default_value=0.0)
    clcp = clumpCurl_Position

    clumpCurl_FloatValue = FloatField(default_value=0.0)
    clcfv = clumpCurl_FloatValue

    clumpCurl_Interp = ClumpCurl_InterpEnumField(default_value=0)
    clci = clumpCurl_Interp


class ClumpCurlField(
    CompoundField[ClumpCurlAttrOperator, ClumpCurlPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpCurlAttrOperator
    PLUG_CLS = ClumpCurlPlugOperator


class ClumpFlatnessPlugOperator(
    CompoundPlugOperator["ClumpFlatnessAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clumpFlatness_Position", "cflp"),
        ("clumpFlatness_FloatValue", "cflfv"),
        ("clumpFlatness_Interp", "cfli"),
    )

    clumpFlatness_Position = FloatField(default_value=0.0)
    cflp = clumpFlatness_Position

    clumpFlatness_FloatValue = FloatField(default_value=0.0)
    cflfv = clumpFlatness_FloatValue

    clumpFlatness_Interp = ClumpFlatness_InterpEnumField(default_value=0)
    cfli = clumpFlatness_Interp


class ClumpFlatnessAttrOperator(
    CompoundAttrOperator[ClumpFlatnessPlugOperator]
):
    __slots__ = ()

    clumpFlatness_Position = FloatField(default_value=0.0)
    cflp = clumpFlatness_Position

    clumpFlatness_FloatValue = FloatField(default_value=0.0)
    cflfv = clumpFlatness_FloatValue

    clumpFlatness_Interp = ClumpFlatness_InterpEnumField(default_value=0)
    cfli = clumpFlatness_Interp


class ClumpFlatnessField(
    CompoundField[ClumpFlatnessAttrOperator, ClumpFlatnessPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpFlatnessAttrOperator
    PLUG_CLS = ClumpFlatnessPlugOperator


class HairWidthScalePlugOperator(
    CompoundPlugOperator["HairWidthScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hairWidthScale_Position", "hwsp"),
        ("hairWidthScale_FloatValue", "hwsfv"),
        ("hairWidthScale_Interp", "hwsi"),
    )

    hairWidthScale_Position = FloatField(default_value=0.0)
    hwsp = hairWidthScale_Position

    hairWidthScale_FloatValue = FloatField(default_value=0.0)
    hwsfv = hairWidthScale_FloatValue

    hairWidthScale_Interp = HairWidthScale_InterpEnumField(default_value=0)
    hwsi = hairWidthScale_Interp


class HairWidthScaleAttrOperator(
    CompoundAttrOperator[HairWidthScalePlugOperator]
):
    __slots__ = ()

    hairWidthScale_Position = FloatField(default_value=0.0)
    hwsp = hairWidthScale_Position

    hairWidthScale_FloatValue = FloatField(default_value=0.0)
    hwsfv = hairWidthScale_FloatValue

    hairWidthScale_Interp = HairWidthScale_InterpEnumField(default_value=0)
    hwsi = hairWidthScale_Interp


class HairWidthScaleField(
    CompoundField[HairWidthScaleAttrOperator, HairWidthScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HairWidthScaleAttrOperator
    PLUG_CLS = HairWidthScalePlugOperator


class HairColorPlugOperator(
    Float3CompoundBasePlugOperator["HairColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hairColorR", "hcr"),
        ("hairColorG", "hcg"),
        ("hairColorB", "hcb"),
    )

    hairColorR = FloatField(default_value=0.30000001192092896)
    hcr = hairColorR

    hairColorG = FloatField(default_value=0.25)
    hcg = hairColorG

    hairColorB = FloatField(default_value=0.15000000596046448)
    hcb = hairColorB


class HairColorAttrOperator(
    Float3CompoundBaseAttrOperator[HairColorPlugOperator]
):
    __slots__ = ()

    hairColorR = FloatField(default_value=0.30000001192092896)
    hcr = hairColorR

    hairColorG = FloatField(default_value=0.25)
    hcg = hairColorG

    hairColorB = FloatField(default_value=0.15000000596046448)
    hcb = hairColorB


class HairColorField(
    Float3CompoundBaseField[HairColorAttrOperator, HairColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HairColorAttrOperator
    PLUG_CLS = HairColorPlugOperator

    hairColorR = FloatField(default_value=0.30000001192092896)
    hcr = hairColorR

    hairColorG = FloatField(default_value=0.25)
    hcg = hairColorG

    hairColorB = FloatField(default_value=0.15000000596046448)
    hcb = hairColorB


class HairColorScalePlugOperator(
    CompoundPlugOperator["HairColorScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hairColorScale_Position", "hcsp"),
        ("hairColorScale_Color", "hcsc"),
        ("hairColorScale_Interp", "hcsi"),
    )

    hairColorScale_Position = FloatField(default_value=0.0)
    hcsp = hairColorScale_Position

    hairColorScale_Color = Float3Field(default_value=(0.0, 0.0, 0.0))
    hcsc = hairColorScale_Color

    hairColorScale_Interp = HairColorScale_InterpEnumField(default_value=0)
    hcsi = hairColorScale_Interp


class HairColorScaleAttrOperator(
    CompoundAttrOperator[HairColorScalePlugOperator]
):
    __slots__ = ()

    hairColorScale_Position = FloatField(default_value=0.0)
    hcsp = hairColorScale_Position

    hairColorScale_Color = Float3Field(default_value=(0.0, 0.0, 0.0))
    hcsc = hairColorScale_Color

    hairColorScale_Interp = HairColorScale_InterpEnumField(default_value=0)
    hcsi = hairColorScale_Interp


class HairColorScaleField(
    CompoundField[HairColorScaleAttrOperator, HairColorScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HairColorScaleAttrOperator
    PLUG_CLS = HairColorScalePlugOperator


class SpecularColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecularColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specularColorR", "spr"),
        ("specularColorG", "spg"),
        ("specularColorB", "spb"),
    )

    specularColorR = FloatField(default_value=0.3499999940395355)
    spr = specularColorR

    specularColorG = FloatField(default_value=0.3499999940395355)
    spg = specularColorG

    specularColorB = FloatField(default_value=0.30000001192092896)
    spb = specularColorB


class SpecularColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecularColorPlugOperator]
):
    __slots__ = ()

    specularColorR = FloatField(default_value=0.3499999940395355)
    spr = specularColorR

    specularColorG = FloatField(default_value=0.3499999940395355)
    spg = specularColorG

    specularColorB = FloatField(default_value=0.30000001192092896)
    spb = specularColorB


class SpecularColorField(
    Float3CompoundBaseField[SpecularColorAttrOperator, SpecularColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecularColorAttrOperator
    PLUG_CLS = SpecularColorPlugOperator

    specularColorR = FloatField(default_value=0.3499999940395355)
    spr = specularColorR

    specularColorG = FloatField(default_value=0.3499999940395355)
    spg = specularColorG

    specularColorB = FloatField(default_value=0.30000001192092896)
    spb = specularColorB


class DisplacementScalePlugOperator(
    CompoundPlugOperator["DisplacementScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("displacementScale_Position", "dscp"),
        ("displacementScale_FloatValue", "dscfv"),
        ("displacementScale_Interp", "dsci"),
    )

    displacementScale_Position = FloatField(default_value=0.0)
    dscp = displacementScale_Position

    displacementScale_FloatValue = FloatField(default_value=0.0)
    dscfv = displacementScale_FloatValue

    displacementScale_Interp = DisplacementScale_InterpEnumField(default_value=0)
    dsci = displacementScale_Interp


class DisplacementScaleAttrOperator(
    CompoundAttrOperator[DisplacementScalePlugOperator]
):
    __slots__ = ()

    displacementScale_Position = FloatField(default_value=0.0)
    dscp = displacementScale_Position

    displacementScale_FloatValue = FloatField(default_value=0.0)
    dscfv = displacementScale_FloatValue

    displacementScale_Interp = DisplacementScale_InterpEnumField(default_value=0)
    dsci = displacementScale_Interp


class DisplacementScaleField(
    CompoundField[DisplacementScaleAttrOperator, DisplacementScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplacementScaleAttrOperator
    PLUG_CLS = DisplacementScalePlugOperator


class FieldDataPlugOperator(
    CompoundPlugOperator["FieldDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldDataPosition", "fdp"),
        ("fieldDataVelocity", "fdv"),
        ("fieldDataMass", "fdm"),
        ("fieldDataDeltaTime", "fdt"),
    )

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class FieldDataAttrOperator(
    CompoundAttrOperator[FieldDataPlugOperator]
):
    __slots__ = ()

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class FieldDataField(
    CompoundField[FieldDataAttrOperator, FieldDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldDataAttrOperator
    PLUG_CLS = FieldDataPlugOperator

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class CollisionDataPlugOperator(
    CompoundPlugOperator["CollisionDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionGeometry", "cge"),
        ("collisionResilience", "crs"),
        ("collisionFriction", "cfr"),
    )

    collisionGeometry = TypedField(multi=True, readable=False)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0, readable=False)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0, readable=False)
    cfr = collisionFriction


class CollisionDataAttrOperator(
    CompoundAttrOperator[CollisionDataPlugOperator]
):
    __slots__ = ()

    collisionGeometry = TypedField(multi=True, readable=False)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0, readable=False)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0, readable=False)
    cfr = collisionFriction


class CollisionDataField(
    CompoundField[CollisionDataAttrOperator, CollisionDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionDataAttrOperator
    PLUG_CLS = CollisionDataPlugOperator

    collisionGeometry = TypedField(multi=True, readable=False)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0, readable=False)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0, readable=False)
    cfr = collisionFriction


class DisplayColorPlugOperator(
    Float3CompoundBasePlugOperator["DisplayColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("displayColorR", "dcr"),
        ("displayColorG", "dcg"),
        ("displayColorB", "dcb"),
    )

    displayColorR = FloatField(default_value=1.0)
    dcr = displayColorR

    displayColorG = FloatField(default_value=0.800000011920929)
    dcg = displayColorG

    displayColorB = FloatField(default_value=0.0)
    dcb = displayColorB


class DisplayColorAttrOperator(
    Float3CompoundBaseAttrOperator[DisplayColorPlugOperator]
):
    __slots__ = ()

    displayColorR = FloatField(default_value=1.0)
    dcr = displayColorR

    displayColorG = FloatField(default_value=0.800000011920929)
    dcg = displayColorG

    displayColorB = FloatField(default_value=0.0)
    dcb = displayColorB


class DisplayColorField(
    Float3CompoundBaseField[DisplayColorAttrOperator, DisplayColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayColorAttrOperator
    PLUG_CLS = DisplayColorPlugOperator

    displayColorR = FloatField(default_value=1.0)
    dcr = displayColorR

    displayColorG = FloatField(default_value=0.800000011920929)
    dcg = displayColorG

    displayColorB = FloatField(default_value=0.0)
    dcb = displayColorB


class AiHairShaderPlugOperator(
    Float3CompoundBasePlugOperator["AiHairShaderAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiHairShaderR", "ai_hair_shaderr"),
        ("aiHairShaderG", "ai_hair_shaderg"),
        ("aiHairShaderB", "ai_hair_shaderb"),
    )

    aiHairShaderR = FloatField(default_value=0.0)
    ai_hair_shaderr = aiHairShaderR

    aiHairShaderG = FloatField(default_value=0.0)
    ai_hair_shaderg = aiHairShaderG

    aiHairShaderB = FloatField(default_value=0.0)
    ai_hair_shaderb = aiHairShaderB


class AiHairShaderAttrOperator(
    Float3CompoundBaseAttrOperator[AiHairShaderPlugOperator]
):
    __slots__ = ()

    aiHairShaderR = FloatField(default_value=0.0)
    ai_hair_shaderr = aiHairShaderR

    aiHairShaderG = FloatField(default_value=0.0)
    ai_hair_shaderg = aiHairShaderG

    aiHairShaderB = FloatField(default_value=0.0)
    ai_hair_shaderb = aiHairShaderB


class AiHairShaderField(
    Float3CompoundBaseField[AiHairShaderAttrOperator, AiHairShaderPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiHairShaderAttrOperator
    PLUG_CLS = AiHairShaderPlugOperator

    aiHairShaderR = FloatField(default_value=0.0)
    ai_hair_shaderr = aiHairShaderR

    aiHairShaderG = FloatField(default_value=0.0)
    ai_hair_shaderg = aiHairShaderG

    aiHairShaderB = FloatField(default_value=0.0)
    ai_hair_shaderb = aiHairShaderB
