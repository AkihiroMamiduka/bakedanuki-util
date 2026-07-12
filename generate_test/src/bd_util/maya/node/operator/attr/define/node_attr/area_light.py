# coding: utf-8

from ..std.at.addr import AddrField
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
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.byte import ByteField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.numeric_scalar_range.short import ShortField
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


class ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "cr"),
        ("colorG", "cg"),
        ("colorB", "cb"),
    )

    colorR = FloatField(default_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=1.0)
    cb = colorB


class ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    colorR = FloatField(default_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=1.0)
    cb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=1.0)
    cr = colorR

    colorG = FloatField(default_value=1.0)
    cg = colorG

    colorB = FloatField(default_value=1.0)
    cb = colorB


class ShadowColorPlugOperator(
    Float3CompoundBasePlugOperator["ShadowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shadColorR", "scr"),
        ("shadColorG", "scg"),
        ("shadColorB", "scb"),
    )

    shadColorR = FloatField(default_value=0.0)
    scr = shadColorR

    shadColorG = FloatField(default_value=0.0)
    scg = shadColorG

    shadColorB = FloatField(default_value=0.0)
    scb = shadColorB


class ShadowColorAttrOperator(
    Float3CompoundBaseAttrOperator[ShadowColorPlugOperator]
):
    __slots__ = ()

    shadColorR = FloatField(default_value=0.0)
    scr = shadColorR

    shadColorG = FloatField(default_value=0.0)
    scg = shadColorG

    shadColorB = FloatField(default_value=0.0)
    scb = shadColorB


class ShadowColorField(
    Float3CompoundBaseField[ShadowColorAttrOperator, ShadowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowColorAttrOperator
    PLUG_CLS = ShadowColorPlugOperator

    shadColorR = FloatField(default_value=0.0)
    scr = shadColorR

    shadColorG = FloatField(default_value=0.0)
    scg = shadColorG

    shadColorB = FloatField(default_value=0.0)
    scb = shadColorB


class PointCameraPlugOperator(
    Float3CompoundBasePlugOperator["PointCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointCameraX", "px"),
        ("pointCameraY", "py"),
        ("pointCameraZ", "pz"),
    )

    pointCameraX = FloatField(default_value=1.0, readable=False)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0, readable=False)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0, readable=False)
    pz = pointCameraZ


class PointCameraAttrOperator(
    Float3CompoundBaseAttrOperator[PointCameraPlugOperator]
):
    __slots__ = ()

    pointCameraX = FloatField(default_value=1.0, readable=False)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0, readable=False)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0, readable=False)
    pz = pointCameraZ


class PointCameraField(
    Float3CompoundBaseField[PointCameraAttrOperator, PointCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointCameraAttrOperator
    PLUG_CLS = PointCameraPlugOperator

    pointCameraX = FloatField(default_value=1.0, readable=False)
    px = pointCameraX

    pointCameraY = FloatField(default_value=1.0, readable=False)
    py = pointCameraY

    pointCameraZ = FloatField(default_value=1.0, readable=False)
    pz = pointCameraZ


class UvCoordPlugOperator(
    Float2CompoundBasePlugOperator["UvCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uCoord", "uu"),
        ("vCoord", "vv"),
    )

    uCoord = FloatField(default_value=0.0, writable=False)
    uu = uCoord

    vCoord = FloatField(default_value=0.0, writable=False)
    vv = vCoord


class UvCoordAttrOperator(
    Float2CompoundBaseAttrOperator[UvCoordPlugOperator]
):
    __slots__ = ()

    uCoord = FloatField(default_value=0.0, writable=False)
    uu = uCoord

    vCoord = FloatField(default_value=0.0, writable=False)
    vv = vCoord


class UvCoordField(
    Float2CompoundBaseField[UvCoordAttrOperator, UvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvCoordAttrOperator
    PLUG_CLS = UvCoordPlugOperator

    uCoord = FloatField(default_value=0.0, writable=False)
    uu = uCoord

    vCoord = FloatField(default_value=0.0, writable=False)
    vv = vCoord


class UvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["UvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvFilterSizeX", "fsx"),
        ("uvFilterSizeY", "fsy"),
    )

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class UvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[UvFilterSizePlugOperator]
):
    __slots__ = ()

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class UvFilterSizeField(
    Float2CompoundBaseField[UvFilterSizeAttrOperator, UvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvFilterSizeAttrOperator
    PLUG_CLS = UvFilterSizePlugOperator

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class LightDataPlugOperator(
    LightDataPlugOperator["LightDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightDirection", "ld"),
        ("lightIntensity", "li"),
        ("lightAmbient", "la"),
        ("lightDiffuse", "ldf"),
        ("lightSpecular", "ls"),
        ("lightShadowFraction", "lsf"),
        ("preShadowIntensity", "psi"),
        ("lightBlindData", "lbl"),
    )

    lightDirection = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=False, writable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=False, writable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False, writable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, writable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=0.0, writable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, writable=False)
    lbl = lightBlindData


class LightDataAttrOperator(
    LightDataAttrOperator[LightDataPlugOperator]
):
    __slots__ = ()

    lightDirection = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=False, writable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=False, writable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False, writable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, writable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=0.0, writable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, writable=False)
    lbl = lightBlindData


class LightDataField(
    LightDataField[LightDataAttrOperator, LightDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightDataAttrOperator
    PLUG_CLS = LightDataPlugOperator

    lightDirection = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    ld = lightDirection

    lightIntensity = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    li = lightIntensity

    lightAmbient = BoolField(default_value=False, writable=False)
    la = lightAmbient

    lightDiffuse = BoolField(default_value=False, writable=False)
    ldf = lightDiffuse

    lightSpecular = BoolField(default_value=False, writable=False)
    ls = lightSpecular

    lightShadowFraction = FloatField(default_value=0.0, writable=False)
    lsf = lightShadowFraction

    preShadowIntensity = FloatField(default_value=0.0, writable=False)
    psi = preShadowIntensity

    lightBlindData = AddrField(default_value=0.0, writable=False)
    lbl = lightBlindData


class OpticalFXvisibilityPlugOperator(
    Float3CompoundBasePlugOperator["OpticalFXvisibilityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("opticalFXvisibilityR", "ovr"),
        ("opticalFXvisibilityG", "ovg"),
        ("opticalFXvisibilityB", "ovb"),
    )

    opticalFXvisibilityR = FloatField(default_value=1.0, writable=False)
    ovr = opticalFXvisibilityR

    opticalFXvisibilityG = FloatField(default_value=1.0, writable=False)
    ovg = opticalFXvisibilityG

    opticalFXvisibilityB = FloatField(default_value=1.0, writable=False)
    ovb = opticalFXvisibilityB


class OpticalFXvisibilityAttrOperator(
    Float3CompoundBaseAttrOperator[OpticalFXvisibilityPlugOperator]
):
    __slots__ = ()

    opticalFXvisibilityR = FloatField(default_value=1.0, writable=False)
    ovr = opticalFXvisibilityR

    opticalFXvisibilityG = FloatField(default_value=1.0, writable=False)
    ovg = opticalFXvisibilityG

    opticalFXvisibilityB = FloatField(default_value=1.0, writable=False)
    ovb = opticalFXvisibilityB


class OpticalFXvisibilityField(
    Float3CompoundBaseField[OpticalFXvisibilityAttrOperator, OpticalFXvisibilityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpticalFXvisibilityAttrOperator
    PLUG_CLS = OpticalFXvisibilityPlugOperator

    opticalFXvisibilityR = FloatField(default_value=1.0, writable=False)
    ovr = opticalFXvisibilityR

    opticalFXvisibilityG = FloatField(default_value=1.0, writable=False)
    ovg = opticalFXvisibilityG

    opticalFXvisibilityB = FloatField(default_value=1.0, writable=False)
    ovb = opticalFXvisibilityB


class PointWorldPlugOperator(
    Float3CompoundBasePlugOperator["PointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointWorldX", "tx"),
        ("pointWorldY", "ty"),
        ("pointWorldZ", "tz"),
    )

    pointWorldX = FloatField(default_value=1.0, readable=False)
    tx = pointWorldX

    pointWorldY = FloatField(default_value=1.0, readable=False)
    ty = pointWorldY

    pointWorldZ = FloatField(default_value=1.0, readable=False)
    tz = pointWorldZ


class PointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[PointWorldPlugOperator]
):
    __slots__ = ()

    pointWorldX = FloatField(default_value=1.0, readable=False)
    tx = pointWorldX

    pointWorldY = FloatField(default_value=1.0, readable=False)
    ty = pointWorldY

    pointWorldZ = FloatField(default_value=1.0, readable=False)
    tz = pointWorldZ


class PointWorldField(
    Float3CompoundBaseField[PointWorldAttrOperator, PointWorldPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointWorldAttrOperator
    PLUG_CLS = PointWorldPlugOperator

    pointWorldX = FloatField(default_value=1.0, readable=False)
    tx = pointWorldX

    pointWorldY = FloatField(default_value=1.0, readable=False)
    ty = pointWorldY

    pointWorldZ = FloatField(default_value=1.0, readable=False)
    tz = pointWorldZ


class NormalCameraPlugOperator(
    Float3CompoundBasePlugOperator["NormalCameraAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalCameraX", "nx"),
        ("normalCameraY", "ny"),
        ("normalCameraZ", "nz"),
    )

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class NormalCameraAttrOperator(
    Float3CompoundBaseAttrOperator[NormalCameraPlugOperator]
):
    __slots__ = ()

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ


class NormalCameraField(
    Float3CompoundBaseField[NormalCameraAttrOperator, NormalCameraPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalCameraAttrOperator
    PLUG_CLS = NormalCameraPlugOperator

    normalCameraX = FloatField(default_value=1.0)
    nx = normalCameraX

    normalCameraY = FloatField(default_value=1.0)
    ny = normalCameraY

    normalCameraZ = FloatField(default_value=1.0)
    nz = normalCameraZ
