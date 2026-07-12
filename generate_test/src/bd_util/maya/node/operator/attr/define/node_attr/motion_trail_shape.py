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
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound.float2 import Float2Field
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


class RepresentationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    A = 1
    LA = 2
    RGB = 3
    RGBA = 4


class RepresentationEnumAttrOperator(EnumAttrOperator):
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
    DoubleLinear3CompoundBaseField[ControlPointsAttrOperator, ControlPointsPlugOperator]
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


class UvSetPlugOperator(
    CompoundPlugOperator["UvSetAttrOperator"]
):
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


class UvSetAttrOperator(
    CompoundAttrOperator[UvSetPlugOperator]
):
    __slots__ = ()

    uvSetName = DataStringField()
    uvsn = uvSetName

    uvSetPoints = Float2Field(multi=True, default_value=(0.0, 0.0))
    uvsp = uvSetPoints

    uvSetTweakLocation = TypedField(readable=False)
    uvtw = uvSetTweakLocation


class UvSetField(
    CompoundField[UvSetAttrOperator, UvSetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvSetAttrOperator
    PLUG_CLS = UvSetPlugOperator


class ColorSetPlugOperator(
    CompoundPlugOperator["ColorSetAttrOperator"]
):
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

    colorSetPoints = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0, 0.0))
    clsp = colorSetPoints


class ColorSetAttrOperator(
    CompoundAttrOperator[ColorSetPlugOperator]
):
    __slots__ = ()

    colorName = DataStringField()
    clsn = colorName

    clamped = BoolField(default_value=False)
    clam = clamped

    representation = RepresentationEnumField(default_value=4)
    rprt = representation

    colorSetPoints = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0, 0.0))
    clsp = colorSetPoints


class ColorSetField(
    CompoundField[ColorSetAttrOperator, ColorSetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorSetAttrOperator
    PLUG_CLS = ColorSetPlugOperator


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


class TrailColorPlugOperator(
    Float3CompoundBasePlugOperator["TrailColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("trailColorR", "tcr"),
        ("trailColorG", "tcg"),
        ("trailColorB", "tcb"),
    )

    trailColorR = FloatField(default_value=0.49000000953674316)
    tcr = trailColorR

    trailColorG = FloatField(default_value=0.09799999743700027)
    tcg = trailColorG

    trailColorB = FloatField(default_value=0.125)
    tcb = trailColorB


class TrailColorAttrOperator(
    Float3CompoundBaseAttrOperator[TrailColorPlugOperator]
):
    __slots__ = ()

    trailColorR = FloatField(default_value=0.49000000953674316)
    tcr = trailColorR

    trailColorG = FloatField(default_value=0.09799999743700027)
    tcg = trailColorG

    trailColorB = FloatField(default_value=0.125)
    tcb = trailColorB


class TrailColorField(
    Float3CompoundBaseField[TrailColorAttrOperator, TrailColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrailColorAttrOperator
    PLUG_CLS = TrailColorPlugOperator

    trailColorR = FloatField(default_value=0.49000000953674316)
    tcr = trailColorR

    trailColorG = FloatField(default_value=0.09799999743700027)
    tcg = trailColorG

    trailColorB = FloatField(default_value=0.125)
    tcb = trailColorB


class ExtraTrailColorPlugOperator(
    Float3CompoundBasePlugOperator["ExtraTrailColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("extraTrailColorR", "etcr"),
        ("extraTrailColorG", "etcg"),
        ("extraTrailColorB", "etcb"),
    )

    extraTrailColorR = FloatField(default_value=0.125)
    etcr = extraTrailColorR

    extraTrailColorG = FloatField(default_value=0.09799999743700027)
    etcg = extraTrailColorG

    extraTrailColorB = FloatField(default_value=0.49000000953674316)
    etcb = extraTrailColorB


class ExtraTrailColorAttrOperator(
    Float3CompoundBaseAttrOperator[ExtraTrailColorPlugOperator]
):
    __slots__ = ()

    extraTrailColorR = FloatField(default_value=0.125)
    etcr = extraTrailColorR

    extraTrailColorG = FloatField(default_value=0.09799999743700027)
    etcg = extraTrailColorG

    extraTrailColorB = FloatField(default_value=0.49000000953674316)
    etcb = extraTrailColorB


class ExtraTrailColorField(
    Float3CompoundBaseField[ExtraTrailColorAttrOperator, ExtraTrailColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtraTrailColorAttrOperator
    PLUG_CLS = ExtraTrailColorPlugOperator

    extraTrailColorR = FloatField(default_value=0.125)
    etcr = extraTrailColorR

    extraTrailColorG = FloatField(default_value=0.09799999743700027)
    etcg = extraTrailColorG

    extraTrailColorB = FloatField(default_value=0.49000000953674316)
    etcb = extraTrailColorB


class KeyframeColorPlugOperator(
    Float3CompoundBasePlugOperator["KeyframeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("keyframeColorR", "kcr"),
        ("keyframeColorG", "kcg"),
        ("keyframeColorB", "kcb"),
    )

    keyframeColorR = FloatField(default_value=1.0)
    kcr = keyframeColorR

    keyframeColorG = FloatField(default_value=1.0)
    kcg = keyframeColorG

    keyframeColorB = FloatField(default_value=1.0)
    kcb = keyframeColorB


class KeyframeColorAttrOperator(
    Float3CompoundBaseAttrOperator[KeyframeColorPlugOperator]
):
    __slots__ = ()

    keyframeColorR = FloatField(default_value=1.0)
    kcr = keyframeColorR

    keyframeColorG = FloatField(default_value=1.0)
    kcg = keyframeColorG

    keyframeColorB = FloatField(default_value=1.0)
    kcb = keyframeColorB


class KeyframeColorField(
    Float3CompoundBaseField[KeyframeColorAttrOperator, KeyframeColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KeyframeColorAttrOperator
    PLUG_CLS = KeyframeColorPlugOperator

    keyframeColorR = FloatField(default_value=1.0)
    kcr = keyframeColorR

    keyframeColorG = FloatField(default_value=1.0)
    kcg = keyframeColorG

    keyframeColorB = FloatField(default_value=1.0)
    kcb = keyframeColorB


class ActiveKeyframeColorPlugOperator(
    Float3CompoundBasePlugOperator["ActiveKeyframeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("activeKeyframeColorR", "akr"),
        ("activeKeyframeColorG", "akg"),
        ("activeKeyframeColorB", "akb"),
    )

    activeKeyframeColorR = FloatField(default_value=1.0)
    akr = activeKeyframeColorR

    activeKeyframeColorG = FloatField(default_value=1.0)
    akg = activeKeyframeColorG

    activeKeyframeColorB = FloatField(default_value=0.0)
    akb = activeKeyframeColorB


class ActiveKeyframeColorAttrOperator(
    Float3CompoundBaseAttrOperator[ActiveKeyframeColorPlugOperator]
):
    __slots__ = ()

    activeKeyframeColorR = FloatField(default_value=1.0)
    akr = activeKeyframeColorR

    activeKeyframeColorG = FloatField(default_value=1.0)
    akg = activeKeyframeColorG

    activeKeyframeColorB = FloatField(default_value=0.0)
    akb = activeKeyframeColorB


class ActiveKeyframeColorField(
    Float3CompoundBaseField[ActiveKeyframeColorAttrOperator, ActiveKeyframeColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ActiveKeyframeColorAttrOperator
    PLUG_CLS = ActiveKeyframeColorPlugOperator

    activeKeyframeColorR = FloatField(default_value=1.0)
    akr = activeKeyframeColorR

    activeKeyframeColorG = FloatField(default_value=1.0)
    akg = activeKeyframeColorG

    activeKeyframeColorB = FloatField(default_value=0.0)
    akb = activeKeyframeColorB


class BeadColorPlugOperator(
    Float3CompoundBasePlugOperator["BeadColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("beadColorR", "bcr"),
        ("beadColorG", "bcg"),
        ("beadColorB", "bcb"),
    )

    beadColorR = FloatField(default_value=1.0)
    bcr = beadColorR

    beadColorG = FloatField(default_value=0.0)
    bcg = beadColorG

    beadColorB = FloatField(default_value=1.0)
    bcb = beadColorB


class BeadColorAttrOperator(
    Float3CompoundBaseAttrOperator[BeadColorPlugOperator]
):
    __slots__ = ()

    beadColorR = FloatField(default_value=1.0)
    bcr = beadColorR

    beadColorG = FloatField(default_value=0.0)
    bcg = beadColorG

    beadColorB = FloatField(default_value=1.0)
    bcb = beadColorB


class BeadColorField(
    Float3CompoundBaseField[BeadColorAttrOperator, BeadColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BeadColorAttrOperator
    PLUG_CLS = BeadColorPlugOperator

    beadColorR = FloatField(default_value=1.0)
    bcr = beadColorR

    beadColorG = FloatField(default_value=0.0)
    bcg = beadColorG

    beadColorB = FloatField(default_value=1.0)
    bcb = beadColorB


class SlowTrailColorPlugOperator(
    Float3CompoundBasePlugOperator["SlowTrailColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("slowTrailColorR", "str"),
        ("slowTrailColorG", "stg"),
        ("slowTrailColorB", "stb"),
    )

    slowTrailColorR = FloatField(default_value=0.23000000417232513)
    str = slowTrailColorR

    slowTrailColorG = FloatField(default_value=0.07100000232458115)
    stg = slowTrailColorG

    slowTrailColorB = FloatField(default_value=0.40400001406669617)
    stb = slowTrailColorB


class SlowTrailColorAttrOperator(
    Float3CompoundBaseAttrOperator[SlowTrailColorPlugOperator]
):
    __slots__ = ()

    slowTrailColorR = FloatField(default_value=0.23000000417232513)
    str = slowTrailColorR

    slowTrailColorG = FloatField(default_value=0.07100000232458115)
    stg = slowTrailColorG

    slowTrailColorB = FloatField(default_value=0.40400001406669617)
    stb = slowTrailColorB


class SlowTrailColorField(
    Float3CompoundBaseField[SlowTrailColorAttrOperator, SlowTrailColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SlowTrailColorAttrOperator
    PLUG_CLS = SlowTrailColorPlugOperator

    slowTrailColorR = FloatField(default_value=0.23000000417232513)
    str = slowTrailColorR

    slowTrailColorG = FloatField(default_value=0.07100000232458115)
    stg = slowTrailColorG

    slowTrailColorB = FloatField(default_value=0.40400001406669617)
    stb = slowTrailColorB


class FastTrailColorPlugOperator(
    Float3CompoundBasePlugOperator["FastTrailColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fastTrailColorR", "ftr"),
        ("fastTrailColorG", "ftg"),
        ("fastTrailColorB", "ftb"),
    )

    fastTrailColorR = FloatField(default_value=0.6119999885559082)
    ftr = fastTrailColorR

    fastTrailColorG = FloatField(default_value=0.0)
    ftg = fastTrailColorG

    fastTrailColorB = FloatField(default_value=0.0)
    ftb = fastTrailColorB


class FastTrailColorAttrOperator(
    Float3CompoundBaseAttrOperator[FastTrailColorPlugOperator]
):
    __slots__ = ()

    fastTrailColorR = FloatField(default_value=0.6119999885559082)
    ftr = fastTrailColorR

    fastTrailColorG = FloatField(default_value=0.0)
    ftg = fastTrailColorG

    fastTrailColorB = FloatField(default_value=0.0)
    ftb = fastTrailColorB


class FastTrailColorField(
    Float3CompoundBaseField[FastTrailColorAttrOperator, FastTrailColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FastTrailColorAttrOperator
    PLUG_CLS = FastTrailColorPlugOperator

    fastTrailColorR = FloatField(default_value=0.6119999885559082)
    ftr = fastTrailColorR

    fastTrailColorG = FloatField(default_value=0.0)
    ftg = fastTrailColorG

    fastTrailColorB = FloatField(default_value=0.0)
    ftb = fastTrailColorB


class TangentPointsPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["TangentPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("txValue", "txv"),
        ("tyValue", "tyv"),
        ("tzValue", "tzv"),
    )

    txValue = DoubleLinearField(default_value=0.0)
    txv = txValue

    tyValue = DoubleLinearField(default_value=0.0)
    tyv = tyValue

    tzValue = DoubleLinearField(default_value=0.0)
    tzv = tzValue


class TangentPointsAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TangentPointsPlugOperator]
):
    __slots__ = ()

    txValue = DoubleLinearField(default_value=0.0)
    txv = txValue

    tyValue = DoubleLinearField(default_value=0.0)
    tyv = tyValue

    tzValue = DoubleLinearField(default_value=0.0)
    tzv = tzValue


class TangentPointsField(
    DoubleLinear3CompoundBaseField[TangentPointsAttrOperator, TangentPointsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TangentPointsAttrOperator
    PLUG_CLS = TangentPointsPlugOperator


class FrameMarkerColorPlugOperator(
    Float3CompoundBasePlugOperator["FrameMarkerColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frameMarkerColorR", "fcr"),
        ("frameMarkerColorG", "fcg"),
        ("frameMarkerColorB", "fcb"),
    )

    frameMarkerColorR = FloatField(default_value=0.1550000011920929)
    fcr = frameMarkerColorR

    frameMarkerColorG = FloatField(default_value=0.5529999732971191)
    fcg = frameMarkerColorG

    frameMarkerColorB = FloatField(default_value=0.11100000143051147)
    fcb = frameMarkerColorB


class FrameMarkerColorAttrOperator(
    Float3CompoundBaseAttrOperator[FrameMarkerColorPlugOperator]
):
    __slots__ = ()

    frameMarkerColorR = FloatField(default_value=0.1550000011920929)
    fcr = frameMarkerColorR

    frameMarkerColorG = FloatField(default_value=0.5529999732971191)
    fcg = frameMarkerColorG

    frameMarkerColorB = FloatField(default_value=0.11100000143051147)
    fcb = frameMarkerColorB


class FrameMarkerColorField(
    Float3CompoundBaseField[FrameMarkerColorAttrOperator, FrameMarkerColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrameMarkerColorAttrOperator
    PLUG_CLS = FrameMarkerColorPlugOperator

    frameMarkerColorR = FloatField(default_value=0.1550000011920929)
    fcr = frameMarkerColorR

    frameMarkerColorG = FloatField(default_value=0.5529999732971191)
    fcg = frameMarkerColorG

    frameMarkerColorB = FloatField(default_value=0.11100000143051147)
    fcb = frameMarkerColorB


class ExtraKeyframeColorPlugOperator(
    Float3CompoundBasePlugOperator["ExtraKeyframeColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("extraKeyframeColorR", "ecr"),
        ("extraKeyframeColorG", "ecg"),
        ("extraKeyframeColorB", "ecb"),
    )

    extraKeyframeColorR = FloatField(default_value=0.45100000500679016)
    ecr = extraKeyframeColorR

    extraKeyframeColorG = FloatField(default_value=0.45100000500679016)
    ecg = extraKeyframeColorG

    extraKeyframeColorB = FloatField(default_value=0.45100000500679016)
    ecb = extraKeyframeColorB


class ExtraKeyframeColorAttrOperator(
    Float3CompoundBaseAttrOperator[ExtraKeyframeColorPlugOperator]
):
    __slots__ = ()

    extraKeyframeColorR = FloatField(default_value=0.45100000500679016)
    ecr = extraKeyframeColorR

    extraKeyframeColorG = FloatField(default_value=0.45100000500679016)
    ecg = extraKeyframeColorG

    extraKeyframeColorB = FloatField(default_value=0.45100000500679016)
    ecb = extraKeyframeColorB


class ExtraKeyframeColorField(
    Float3CompoundBaseField[ExtraKeyframeColorAttrOperator, ExtraKeyframeColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtraKeyframeColorAttrOperator
    PLUG_CLS = ExtraKeyframeColorPlugOperator

    extraKeyframeColorR = FloatField(default_value=0.45100000500679016)
    ecr = extraKeyframeColorR

    extraKeyframeColorG = FloatField(default_value=0.45100000500679016)
    ecg = extraKeyframeColorG

    extraKeyframeColorB = FloatField(default_value=0.45100000500679016)
    ecb = extraKeyframeColorB
