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
from ..std.at.numeric_scalar_range.double import DoubleField
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


class CollideModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PLANE = 0
    MESH = 1


class CollideModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PLANE = 0
    MESH = 1

    NAME_MAP = {
        PLANE: "plane",
        MESH: "mesh",
    }


class CollideModeEnumField(
    EnumField[CollideModeEnumAttrOperator, CollideModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollideModeEnumAttrOperator
    PLUG_CLS = CollideModeEnumPlugOperator


class AxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5


class AxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X_MINUS_AXIS = 0
    Y_MINUS_AXIS = 1
    Z_MINUS_AXIS = 2
    NEG_X_MINUS_AXIS = 3
    NEG_Y_MINUS_AXIS = 4
    NEG_Z_MINUS_AXIS = 5

    NAME_MAP = {
        X_MINUS_AXIS: "X-Axis",
        Y_MINUS_AXIS: "Y-Axis",
        Z_MINUS_AXIS: "Z-Axis",
        NEG_X_MINUS_AXIS: "Neg X-Axis",
        NEG_Y_MINUS_AXIS: "Neg Y-Axis",
        NEG_Z_MINUS_AXIS: "Neg Z-Axis",
    }


class AxisEnumField(
    EnumField[AxisEnumAttrOperator, AxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisEnumAttrOperator
    PLUG_CLS = AxisEnumPlugOperator


class SMOOTH_PREEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class SMOOTH_PREEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class SMOOTH_PREEnumField(
    EnumField[SMOOTH_PREEnumAttrOperator, SMOOTH_PREEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SMOOTH_PREEnumAttrOperator
    PLUG_CLS = SMOOTH_PREEnumPlugOperator


class MOVEMENTEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class MOVEMENTEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class MOVEMENTEnumField(
    EnumField[MOVEMENTEnumAttrOperator, MOVEMENTEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MOVEMENTEnumAttrOperator
    PLUG_CLS = MOVEMENTEnumPlugOperator


class COLLISIONEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class COLLISIONEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class COLLISIONEnumField(
    EnumField[COLLISIONEnumAttrOperator, COLLISIONEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = COLLISIONEnumAttrOperator
    PLUG_CLS = COLLISIONEnumPlugOperator


class SMOOTH_POSTEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class SMOOTH_POSTEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class SMOOTH_POSTEnumField(
    EnumField[SMOOTH_POSTEnumAttrOperator, SMOOTH_POSTEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SMOOTH_POSTEnumAttrOperator
    PLUG_CLS = SMOOTH_POSTEnumPlugOperator


class DISPLAYEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MINUS = 0


class DISPLAYEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MINUS = 0

    NAME_MAP = {
        MINUS: "-",
    }


class DISPLAYEnumField(
    EnumField[DISPLAYEnumAttrOperator, DISPLAYEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DISPLAYEnumAttrOperator
    PLUG_CLS = DISPLAYEnumPlugOperator


class DrawEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class DrawEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "off",
        ON: "on",
    }


class DrawEnumField(
    EnumField[DrawEnumAttrOperator, DrawEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DrawEnumAttrOperator
    PLUG_CLS = DrawEnumPlugOperator


class ShadedEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WIREFRAME_MINUS_ONLY = 0
    SHADED = 1
    WIREFRAME_MINUS_AND_MINUS_SHADED = 2


class ShadedEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WIREFRAME_MINUS_ONLY = 0
    SHADED = 1
    WIREFRAME_MINUS_AND_MINUS_SHADED = 2

    NAME_MAP = {
        WIREFRAME_MINUS_ONLY: "wireframe-only",
        SHADED: "shaded",
        WIREFRAME_MINUS_AND_MINUS_SHADED: "wireframe-and-shaded",
    }


class ShadedEnumField(
    EnumField[ShadedEnumAttrOperator, ShadedEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadedEnumAttrOperator
    PLUG_CLS = ShadedEnumPlugOperator


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


class CollideDataPlugOperator(
    CompoundPlugOperator["CollideDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldMatrixA", "wma"),
        ("worldMatrixB", "wmb"),
        ("worldMatrixABase", "wmab"),
        ("worldMatrixBBase", "wmbb"),
        ("worldMatrixPlane", "wmpln"),
        ("worldMatrixPlaneBase", "wmplnbase"),
        ("enable", "ena"),
        ("collideMode", "colmod"),
        ("axis", "ax"),
        ("triggerMin", "trgmin"),
        ("angleMin", "angmin"),
        ("angleMax", "angmax"),
        ("bias", "bis"),
        ("biasAdjust", "bisadj"),
        ("userScale", "usrscl"),
        ("manualScale", "manscl"),
        ("SMOOTH_PRE", "SMTHPRE"),
        ("smoothIterationsPre", "smipre"),
        ("smoothStrengthPre", "smstrpre"),
        ("smoothHoldPre", "hldpre"),
        ("MOVEMENT", "MOVE"),
        ("bulkA", "blka"),
        ("bulkB", "blkb"),
        ("bulkAngularA", "blkanga"),
        ("bulkAngularB", "blkangb"),
        ("bulkWidenA", "blkwida"),
        ("bulkWidenB", "blkwidb"),
        ("slideA", "slda"),
        ("slideB", "sldb"),
        ("slideRearA", "sldrera"),
        ("slideRearB", "sldrerb"),
        ("slideAngularA", "sldanga"),
        ("slideAngularB", "sldangb"),
        ("slideAngularRearA", "sldangrera"),
        ("slideAngularRearB", "sldangrerb"),
        ("wrinkleA", "wrka"),
        ("wrinkleB", "wrkb"),
        ("wrinkleSpread", "wrkspr"),
        ("COLLISION", "COLL"),
        ("flattenA", "flta"),
        ("flattenB", "fltb"),
        ("rigidA", "riga"),
        ("rigidB", "rigb"),
        ("collisionBlurIterations", "colblrit"),
        ("volumizeA", "vlma"),
        ("volumizeB", "vlmb"),
        ("volumizeOffset", "vlmoff"),
        ("volumizePuff", "vlmpuf"),
        ("volumizeDist", "vlmd"),
        ("volumizeFalloff", "vlmfall"),
        ("SMOOTH_POST", "SMTHPST"),
        ("smoothIterationsPost", "smipst"),
        ("smoothStrengthPost", "smstrpst"),
        ("smoothHoldPost", "hldpst"),
        ("lockSmartWt", "lksmrt"),
    )

    worldMatrixA = MatrixField()
    wma = worldMatrixA

    worldMatrixB = MatrixField()
    wmb = worldMatrixB

    worldMatrixABase = MatrixField()
    wmab = worldMatrixABase

    worldMatrixBBase = MatrixField()
    wmbb = worldMatrixBBase

    worldMatrixPlane = MatrixField()
    wmpln = worldMatrixPlane

    worldMatrixPlaneBase = MatrixField()
    wmplnbase = worldMatrixPlaneBase

    enable = BoolField(default_value=True)
    ena = enable

    collideMode = CollideModeEnumField(default_value=0)
    colmod = collideMode

    axis = AxisEnumField(default_value=1)
    ax = axis

    triggerMin = DoubleField(default_value=0.0, min_value=0.0, max_value=180.0)
    trgmin = triggerMin

    angleMin = DoubleField(default_value=60.0, min_value=0.0, max_value=180.0)
    angmin = angleMin

    angleMax = DoubleField(default_value=120.0, min_value=0.0, max_value=180.0)
    angmax = angleMax

    bias = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bis = bias

    biasAdjust = DoubleField(default_value=0.0, min_value=-2.0, max_value=2.0)
    bisadj = biasAdjust

    userScale = DoubleField(default_value=1.0)
    usrscl = userScale

    manualScale = DoubleField(default_value=1.0)
    manscl = manualScale

    SMOOTH_PRE = SMOOTH_PREEnumField(default_value=0)
    SMTHPRE = SMOOTH_PRE

    smoothIterationsPre = LongField(default_value=12, min_value=0)
    smipre = smoothIterationsPre

    smoothStrengthPre = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    smstrpre = smoothStrengthPre

    smoothHoldPre = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    hldpre = smoothHoldPre

    MOVEMENT = MOVEMENTEnumField(default_value=0)
    MOVE = MOVEMENT

    bulkA = DoubleField(default_value=1.0)
    blka = bulkA

    bulkB = DoubleField(default_value=1.0)
    blkb = bulkB

    bulkAngularA = DoubleField(default_value=1.0)
    blkanga = bulkAngularA

    bulkAngularB = DoubleField(default_value=1.0)
    blkangb = bulkAngularB

    bulkWidenA = DoubleField(default_value=1.0)
    blkwida = bulkWidenA

    bulkWidenB = DoubleField(default_value=1.0)
    blkwidb = bulkWidenB

    slideA = DoubleField(default_value=1.0)
    slda = slideA

    slideB = DoubleField(default_value=1.0)
    sldb = slideB

    slideRearA = DoubleField(default_value=1.0)
    sldrera = slideRearA

    slideRearB = DoubleField(default_value=1.0)
    sldrerb = slideRearB

    slideAngularA = DoubleField(default_value=1.0)
    sldanga = slideAngularA

    slideAngularB = DoubleField(default_value=1.0)
    sldangb = slideAngularB

    slideAngularRearA = DoubleField(default_value=1.0)
    sldangrera = slideAngularRearA

    slideAngularRearB = DoubleField(default_value=1.0)
    sldangrerb = slideAngularRearB

    wrinkleA = DoubleField(default_value=1.0)
    wrka = wrinkleA

    wrinkleB = DoubleField(default_value=1.0)
    wrkb = wrinkleB

    wrinkleSpread = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    wrkspr = wrinkleSpread

    COLLISION = COLLISIONEnumField(default_value=0)
    COLL = COLLISION

    flattenA = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    flta = flattenA

    flattenB = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    fltb = flattenB

    rigidA = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    riga = rigidA

    rigidB = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    rigb = rigidB

    collisionBlurIterations = LongField(default_value=5, min_value=0)
    colblrit = collisionBlurIterations

    volumizeA = DoubleField(default_value=1.0)
    vlma = volumizeA

    volumizeB = DoubleField(default_value=1.0)
    vlmb = volumizeB

    volumizeOffset = DoubleField(default_value=0.0)
    vlmoff = volumizeOffset

    volumizePuff = DoubleField(default_value=0.3, min_value=0.0, max_value=1.0)
    vlmpuf = volumizePuff

    volumizeDist = DoubleField(default_value=1.0, min_value=0.0)
    vlmd = volumizeDist

    volumizeFalloff = DoubleField(default_value=1.0, min_value=0.0)
    vlmfall = volumizeFalloff

    SMOOTH_POST = SMOOTH_POSTEnumField(default_value=0)
    SMTHPST = SMOOTH_POST

    smoothIterationsPost = LongField(default_value=12, min_value=0)
    smipst = smoothIterationsPost

    smoothStrengthPost = DoubleField(default_value=0.1, min_value=0.0, max_value=1.0)
    smstrpst = smoothStrengthPost

    smoothHoldPost = DoubleField(default_value=0.8, min_value=0.0, max_value=1.0)
    hldpst = smoothHoldPost

    lockSmartWt = BoolField(default_value=False)
    lksmrt = lockSmartWt


class CollideDataAttrOperator(
    CompoundAttrOperator[CollideDataPlugOperator]
):
    __slots__ = ()

    worldMatrixA = MatrixField()
    wma = worldMatrixA

    worldMatrixB = MatrixField()
    wmb = worldMatrixB

    worldMatrixABase = MatrixField()
    wmab = worldMatrixABase

    worldMatrixBBase = MatrixField()
    wmbb = worldMatrixBBase

    worldMatrixPlane = MatrixField()
    wmpln = worldMatrixPlane

    worldMatrixPlaneBase = MatrixField()
    wmplnbase = worldMatrixPlaneBase

    enable = BoolField(default_value=True)
    ena = enable

    collideMode = CollideModeEnumField(default_value=0)
    colmod = collideMode

    axis = AxisEnumField(default_value=1)
    ax = axis

    triggerMin = DoubleField(default_value=0.0, min_value=0.0, max_value=180.0)
    trgmin = triggerMin

    angleMin = DoubleField(default_value=60.0, min_value=0.0, max_value=180.0)
    angmin = angleMin

    angleMax = DoubleField(default_value=120.0, min_value=0.0, max_value=180.0)
    angmax = angleMax

    bias = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bis = bias

    biasAdjust = DoubleField(default_value=0.0, min_value=-2.0, max_value=2.0)
    bisadj = biasAdjust

    userScale = DoubleField(default_value=1.0)
    usrscl = userScale

    manualScale = DoubleField(default_value=1.0)
    manscl = manualScale

    SMOOTH_PRE = SMOOTH_PREEnumField(default_value=0)
    SMTHPRE = SMOOTH_PRE

    smoothIterationsPre = LongField(default_value=12, min_value=0)
    smipre = smoothIterationsPre

    smoothStrengthPre = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    smstrpre = smoothStrengthPre

    smoothHoldPre = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    hldpre = smoothHoldPre

    MOVEMENT = MOVEMENTEnumField(default_value=0)
    MOVE = MOVEMENT

    bulkA = DoubleField(default_value=1.0)
    blka = bulkA

    bulkB = DoubleField(default_value=1.0)
    blkb = bulkB

    bulkAngularA = DoubleField(default_value=1.0)
    blkanga = bulkAngularA

    bulkAngularB = DoubleField(default_value=1.0)
    blkangb = bulkAngularB

    bulkWidenA = DoubleField(default_value=1.0)
    blkwida = bulkWidenA

    bulkWidenB = DoubleField(default_value=1.0)
    blkwidb = bulkWidenB

    slideA = DoubleField(default_value=1.0)
    slda = slideA

    slideB = DoubleField(default_value=1.0)
    sldb = slideB

    slideRearA = DoubleField(default_value=1.0)
    sldrera = slideRearA

    slideRearB = DoubleField(default_value=1.0)
    sldrerb = slideRearB

    slideAngularA = DoubleField(default_value=1.0)
    sldanga = slideAngularA

    slideAngularB = DoubleField(default_value=1.0)
    sldangb = slideAngularB

    slideAngularRearA = DoubleField(default_value=1.0)
    sldangrera = slideAngularRearA

    slideAngularRearB = DoubleField(default_value=1.0)
    sldangrerb = slideAngularRearB

    wrinkleA = DoubleField(default_value=1.0)
    wrka = wrinkleA

    wrinkleB = DoubleField(default_value=1.0)
    wrkb = wrinkleB

    wrinkleSpread = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    wrkspr = wrinkleSpread

    COLLISION = COLLISIONEnumField(default_value=0)
    COLL = COLLISION

    flattenA = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    flta = flattenA

    flattenB = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    fltb = flattenB

    rigidA = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    riga = rigidA

    rigidB = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    rigb = rigidB

    collisionBlurIterations = LongField(default_value=5, min_value=0)
    colblrit = collisionBlurIterations

    volumizeA = DoubleField(default_value=1.0)
    vlma = volumizeA

    volumizeB = DoubleField(default_value=1.0)
    vlmb = volumizeB

    volumizeOffset = DoubleField(default_value=0.0)
    vlmoff = volumizeOffset

    volumizePuff = DoubleField(default_value=0.3, min_value=0.0, max_value=1.0)
    vlmpuf = volumizePuff

    volumizeDist = DoubleField(default_value=1.0, min_value=0.0)
    vlmd = volumizeDist

    volumizeFalloff = DoubleField(default_value=1.0, min_value=0.0)
    vlmfall = volumizeFalloff

    SMOOTH_POST = SMOOTH_POSTEnumField(default_value=0)
    SMTHPST = SMOOTH_POST

    smoothIterationsPost = LongField(default_value=12, min_value=0)
    smipst = smoothIterationsPost

    smoothStrengthPost = DoubleField(default_value=0.1, min_value=0.0, max_value=1.0)
    smstrpst = smoothStrengthPost

    smoothHoldPost = DoubleField(default_value=0.8, min_value=0.0, max_value=1.0)
    hldpst = smoothHoldPost

    lockSmartWt = BoolField(default_value=False)
    lksmrt = lockSmartWt


class CollideDataField(
    CompoundField[CollideDataAttrOperator, CollideDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollideDataAttrOperator
    PLUG_CLS = CollideDataPlugOperator

    worldMatrixA = MatrixField()
    wma = worldMatrixA

    worldMatrixB = MatrixField()
    wmb = worldMatrixB

    worldMatrixABase = MatrixField()
    wmab = worldMatrixABase

    worldMatrixBBase = MatrixField()
    wmbb = worldMatrixBBase

    worldMatrixPlane = MatrixField()
    wmpln = worldMatrixPlane

    worldMatrixPlaneBase = MatrixField()
    wmplnbase = worldMatrixPlaneBase

    enable = BoolField(default_value=True)
    ena = enable

    collideMode = CollideModeEnumField(default_value=0)
    colmod = collideMode

    axis = AxisEnumField(default_value=1)
    ax = axis

    triggerMin = DoubleField(default_value=0.0, min_value=0.0, max_value=180.0)
    trgmin = triggerMin

    angleMin = DoubleField(default_value=60.0, min_value=0.0, max_value=180.0)
    angmin = angleMin

    angleMax = DoubleField(default_value=120.0, min_value=0.0, max_value=180.0)
    angmax = angleMax

    bias = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bis = bias

    biasAdjust = DoubleField(default_value=0.0, min_value=-2.0, max_value=2.0)
    bisadj = biasAdjust

    userScale = DoubleField(default_value=1.0)
    usrscl = userScale

    manualScale = DoubleField(default_value=1.0)
    manscl = manualScale

    SMOOTH_PRE = SMOOTH_PREEnumField(default_value=0)
    SMTHPRE = SMOOTH_PRE

    smoothIterationsPre = LongField(default_value=12, min_value=0)
    smipre = smoothIterationsPre

    smoothStrengthPre = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    smstrpre = smoothStrengthPre

    smoothHoldPre = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    hldpre = smoothHoldPre

    MOVEMENT = MOVEMENTEnumField(default_value=0)
    MOVE = MOVEMENT

    bulkA = DoubleField(default_value=1.0)
    blka = bulkA

    bulkB = DoubleField(default_value=1.0)
    blkb = bulkB

    bulkAngularA = DoubleField(default_value=1.0)
    blkanga = bulkAngularA

    bulkAngularB = DoubleField(default_value=1.0)
    blkangb = bulkAngularB

    bulkWidenA = DoubleField(default_value=1.0)
    blkwida = bulkWidenA

    bulkWidenB = DoubleField(default_value=1.0)
    blkwidb = bulkWidenB

    slideA = DoubleField(default_value=1.0)
    slda = slideA

    slideB = DoubleField(default_value=1.0)
    sldb = slideB

    slideRearA = DoubleField(default_value=1.0)
    sldrera = slideRearA

    slideRearB = DoubleField(default_value=1.0)
    sldrerb = slideRearB

    slideAngularA = DoubleField(default_value=1.0)
    sldanga = slideAngularA

    slideAngularB = DoubleField(default_value=1.0)
    sldangb = slideAngularB

    slideAngularRearA = DoubleField(default_value=1.0)
    sldangrera = slideAngularRearA

    slideAngularRearB = DoubleField(default_value=1.0)
    sldangrerb = slideAngularRearB

    wrinkleA = DoubleField(default_value=1.0)
    wrka = wrinkleA

    wrinkleB = DoubleField(default_value=1.0)
    wrkb = wrinkleB

    wrinkleSpread = DoubleField(default_value=0.5, min_value=0.0, max_value=1.0)
    wrkspr = wrinkleSpread

    COLLISION = COLLISIONEnumField(default_value=0)
    COLL = COLLISION

    flattenA = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    flta = flattenA

    flattenB = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    fltb = flattenB

    rigidA = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    riga = rigidA

    rigidB = DoubleField(default_value=0.0, min_value=0.0, max_value=1.0)
    rigb = rigidB

    collisionBlurIterations = LongField(default_value=5, min_value=0)
    colblrit = collisionBlurIterations

    volumizeA = DoubleField(default_value=1.0)
    vlma = volumizeA

    volumizeB = DoubleField(default_value=1.0)
    vlmb = volumizeB

    volumizeOffset = DoubleField(default_value=0.0)
    vlmoff = volumizeOffset

    volumizePuff = DoubleField(default_value=0.3, min_value=0.0, max_value=1.0)
    vlmpuf = volumizePuff

    volumizeDist = DoubleField(default_value=1.0, min_value=0.0)
    vlmd = volumizeDist

    volumizeFalloff = DoubleField(default_value=1.0, min_value=0.0)
    vlmfall = volumizeFalloff

    SMOOTH_POST = SMOOTH_POSTEnumField(default_value=0)
    SMTHPST = SMOOTH_POST

    smoothIterationsPost = LongField(default_value=12, min_value=0)
    smipst = smoothIterationsPost

    smoothStrengthPost = DoubleField(default_value=0.1, min_value=0.0, max_value=1.0)
    smstrpst = smoothStrengthPost

    smoothHoldPost = DoubleField(default_value=0.8, min_value=0.0, max_value=1.0)
    hldpst = smoothHoldPost

    lockSmartWt = BoolField(default_value=False)
    lksmrt = lockSmartWt


class DrawDataPlugOperator(
    CompoundPlugOperator["DrawDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("DISPLAY", "DSPL"),
        ("draw", "drw"),
        ("shaded", "shd"),
        ("highlight", "hi"),
        ("color", "col"),
        ("colorTrigger", "coltrg"),
        ("opacity", "opa"),
        ("displaySize", "dspsiz"),
    )

    DISPLAY = DISPLAYEnumField(default_value=0)
    DSPL = DISPLAY

    draw = DrawEnumField(default_value=1)
    drw = draw

    shaded = ShadedEnumField(default_value=2)
    shd = shaded

    highlight = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    hi = highlight

    color = Float3Field(default_value=(0.0, 0.800000011920929, 0.30000001192092896), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    col = color

    colorTrigger = Float3Field(default_value=(1.0, 0.10000000149011612, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    coltrg = colorTrigger

    opacity = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    opa = opacity

    displaySize = DoubleField(default_value=1.0, min_value=0.0)
    dspsiz = displaySize


class DrawDataAttrOperator(
    CompoundAttrOperator[DrawDataPlugOperator]
):
    __slots__ = ()

    DISPLAY = DISPLAYEnumField(default_value=0)
    DSPL = DISPLAY

    draw = DrawEnumField(default_value=1)
    drw = draw

    shaded = ShadedEnumField(default_value=2)
    shd = shaded

    highlight = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    hi = highlight

    color = Float3Field(default_value=(0.0, 0.800000011920929, 0.30000001192092896), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    col = color

    colorTrigger = Float3Field(default_value=(1.0, 0.10000000149011612, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    coltrg = colorTrigger

    opacity = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    opa = opacity

    displaySize = DoubleField(default_value=1.0, min_value=0.0)
    dspsiz = displaySize


class DrawDataField(
    CompoundField[DrawDataAttrOperator, DrawDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DrawDataAttrOperator
    PLUG_CLS = DrawDataPlugOperator

    DISPLAY = DISPLAYEnumField(default_value=0)
    DSPL = DISPLAY

    draw = DrawEnumField(default_value=1)
    drw = draw

    shaded = ShadedEnumField(default_value=2)
    shd = shaded

    highlight = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    hi = highlight

    color = Float3Field(default_value=(0.0, 0.800000011920929, 0.30000001192092896), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    col = color

    colorTrigger = Float3Field(default_value=(1.0, 0.10000000149011612, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    coltrg = colorTrigger

    opacity = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    opa = opacity

    displaySize = DoubleField(default_value=1.0, min_value=0.0)
    dspsiz = displaySize
