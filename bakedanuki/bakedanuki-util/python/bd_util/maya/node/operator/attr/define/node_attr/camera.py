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
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound.double2 import Double2Field
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
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


class OverrideDisplayTypeEnumPlugOperator(EnumPlugOperator["OverrideDisplayTypeEnumAttrOperator"]):
    __slots__ = ()

    NORMAL = 0
    TEMPLATE = 1
    REFERENCE = 2


class OverrideDisplayTypeEnumAttrOperator(EnumAttrOperator[OverrideDisplayTypeEnumPlugOperator]):
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


class OverrideLevelOfDetailEnumPlugOperator(EnumPlugOperator["OverrideLevelOfDetailEnumAttrOperator"]):
    __slots__ = ()

    FULL = 0
    BOUNDING_BOX = 1


class OverrideLevelOfDetailEnumAttrOperator(EnumAttrOperator[OverrideLevelOfDetailEnumPlugOperator]):
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


class CameraAperturePlugOperator(
    Double2CompoundBasePlugOperator["CameraApertureAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("horizontalFilmAperture", "hfa"),
        ("verticalFilmAperture", "vfa"),
    )

    horizontalFilmAperture = DoubleField(default_value=1.4173200000000001, min_value=3.9370000000000004e-05, max_value=1200.0, soft_min_value=0.1, soft_max_value=10.0)
    hfa = horizontalFilmAperture

    verticalFilmAperture = DoubleField(default_value=0.94488, min_value=3.9370000000000004e-05, max_value=1200.0, soft_min_value=0.1, soft_max_value=10.0)
    vfa = verticalFilmAperture


class CameraApertureAttrOperator(
    Double2CompoundBaseAttrOperator[CameraAperturePlugOperator]
):
    __slots__ = ()

    horizontalFilmAperture = DoubleField(default_value=1.4173200000000001, min_value=3.9370000000000004e-05, max_value=1200.0, soft_min_value=0.1, soft_max_value=10.0)
    hfa = horizontalFilmAperture

    verticalFilmAperture = DoubleField(default_value=0.94488, min_value=3.9370000000000004e-05, max_value=1200.0, soft_min_value=0.1, soft_max_value=10.0)
    vfa = verticalFilmAperture


class CameraApertureField(
    Double2CompoundBaseField[CameraApertureAttrOperator, CameraAperturePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CameraApertureAttrOperator
    PLUG_CLS = CameraAperturePlugOperator

    horizontalFilmAperture = DoubleField(default_value=1.4173200000000001, min_value=3.9370000000000004e-05, max_value=1200.0, soft_min_value=0.1, soft_max_value=10.0)
    hfa = horizontalFilmAperture

    verticalFilmAperture = DoubleField(default_value=0.94488, min_value=3.9370000000000004e-05, max_value=1200.0, soft_min_value=0.1, soft_max_value=10.0)
    vfa = verticalFilmAperture


class FilmOffsetPlugOperator(
    Double2CompoundBasePlugOperator["FilmOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("horizontalFilmOffset", "hfo"),
        ("verticalFilmOffset", "vfo"),
    )

    horizontalFilmOffset = DoubleField(default_value=0.0)
    hfo = horizontalFilmOffset

    verticalFilmOffset = DoubleField(default_value=0.0)
    vfo = verticalFilmOffset


class FilmOffsetAttrOperator(
    Double2CompoundBaseAttrOperator[FilmOffsetPlugOperator]
):
    __slots__ = ()

    horizontalFilmOffset = DoubleField(default_value=0.0)
    hfo = horizontalFilmOffset

    verticalFilmOffset = DoubleField(default_value=0.0)
    vfo = verticalFilmOffset


class FilmOffsetField(
    Double2CompoundBaseField[FilmOffsetAttrOperator, FilmOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilmOffsetAttrOperator
    PLUG_CLS = FilmOffsetPlugOperator

    horizontalFilmOffset = DoubleField(default_value=0.0)
    hfo = horizontalFilmOffset

    verticalFilmOffset = DoubleField(default_value=0.0)
    vfo = verticalFilmOffset


class ShakePlugOperator(
    Double2CompoundBasePlugOperator["ShakeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("horizontalShake", "hs"),
        ("verticalShake", "vs"),
    )

    horizontalShake = DoubleField(default_value=0.0)
    hs = horizontalShake

    verticalShake = DoubleField(default_value=0.0)
    vs = verticalShake


class ShakeAttrOperator(
    Double2CompoundBaseAttrOperator[ShakePlugOperator]
):
    __slots__ = ()

    horizontalShake = DoubleField(default_value=0.0)
    hs = horizontalShake

    verticalShake = DoubleField(default_value=0.0)
    vs = verticalShake


class ShakeField(
    Double2CompoundBaseField[ShakeAttrOperator, ShakePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShakeAttrOperator
    PLUG_CLS = ShakePlugOperator

    horizontalShake = DoubleField(default_value=0.0)
    hs = horizontalShake

    verticalShake = DoubleField(default_value=0.0)
    vs = verticalShake


class PostProjectionPlugOperator(
    CompoundPlugOperator["PostProjectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("preScale", "psc"),
        ("filmTranslate", "ct"),
        ("filmRollControl", "frc"),
        ("postScale", "ptsc"),
    )

    preScale = DoubleField(default_value=1.0, min_value=1e-10)
    psc = preScale

    filmTranslate = Double2Field(default_value=(0.0, 0.0))
    ct = filmTranslate

    filmRollControl = CompoundField()
    frc = filmRollControl

    postScale = DoubleField(default_value=1.0, min_value=1e-10)
    ptsc = postScale


class PostProjectionAttrOperator(
    CompoundAttrOperator[PostProjectionPlugOperator]
):
    __slots__ = ()

    preScale = DoubleField(default_value=1.0, min_value=1e-10)
    psc = preScale

    filmTranslate = Double2Field(default_value=(0.0, 0.0))
    ct = filmTranslate

    filmRollControl = CompoundField()
    frc = filmRollControl

    postScale = DoubleField(default_value=1.0, min_value=1e-10)
    ptsc = postScale


class PostProjectionField(
    CompoundField[PostProjectionAttrOperator, PostProjectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PostProjectionAttrOperator
    PLUG_CLS = PostProjectionPlugOperator

    preScale = DoubleField(default_value=1.0, min_value=1e-10)
    psc = preScale

    filmTranslate = Double2Field(default_value=(0.0, 0.0))
    ct = filmTranslate

    filmRollControl = CompoundField()
    frc = filmRollControl

    postScale = DoubleField(default_value=1.0, min_value=1e-10)
    ptsc = postScale


class PanPlugOperator(
    Double2CompoundBasePlugOperator["PanAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("horizontalPan", "hpn"),
        ("verticalPan", "vpn"),
    )

    horizontalPan = DoubleField(default_value=0.0)
    hpn = horizontalPan

    verticalPan = DoubleField(default_value=0.0)
    vpn = verticalPan


class PanAttrOperator(
    Double2CompoundBaseAttrOperator[PanPlugOperator]
):
    __slots__ = ()

    horizontalPan = DoubleField(default_value=0.0)
    hpn = horizontalPan

    verticalPan = DoubleField(default_value=0.0)
    vpn = verticalPan


class PanField(
    Double2CompoundBaseField[PanAttrOperator, PanPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PanAttrOperator
    PLUG_CLS = PanPlugOperator

    horizontalPan = DoubleField(default_value=0.0)
    hpn = horizontalPan

    verticalPan = DoubleField(default_value=0.0)
    vpn = verticalPan


class TumblePivotPlugOperator(
    Double3CompoundBasePlugOperator["TumblePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tumblePivotX", "tpx"),
        ("tumblePivotY", "tpy"),
        ("tumblePivotZ", "tpz"),
    )

    tumblePivotX = DoubleField(default_value=0.0)
    tpx = tumblePivotX

    tumblePivotY = DoubleField(default_value=0.0)
    tpy = tumblePivotY

    tumblePivotZ = DoubleField(default_value=0.0)
    tpz = tumblePivotZ


class TumblePivotAttrOperator(
    Double3CompoundBaseAttrOperator[TumblePivotPlugOperator]
):
    __slots__ = ()

    tumblePivotX = DoubleField(default_value=0.0)
    tpx = tumblePivotX

    tumblePivotY = DoubleField(default_value=0.0)
    tpy = tumblePivotY

    tumblePivotZ = DoubleField(default_value=0.0)
    tpz = tumblePivotZ


class TumblePivotField(
    Double3CompoundBaseField[TumblePivotAttrOperator, TumblePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TumblePivotAttrOperator
    PLUG_CLS = TumblePivotPlugOperator

    tumblePivotX = DoubleField(default_value=0.0)
    tpx = tumblePivotX

    tumblePivotY = DoubleField(default_value=0.0)
    tpy = tumblePivotY

    tumblePivotZ = DoubleField(default_value=0.0)
    tpz = tumblePivotZ


class DisplayGateMaskColorPlugOperator(
    Float3CompoundBasePlugOperator["DisplayGateMaskColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("displayGateMaskColorR", "dgcr"),
        ("displayGateMaskColorG", "dgcg"),
        ("displayGateMaskColorB", "dgcb"),
    )

    displayGateMaskColorR = FloatField(default_value=0.5)
    dgcr = displayGateMaskColorR

    displayGateMaskColorG = FloatField(default_value=0.5)
    dgcg = displayGateMaskColorG

    displayGateMaskColorB = FloatField(default_value=0.5)
    dgcb = displayGateMaskColorB


class DisplayGateMaskColorAttrOperator(
    Float3CompoundBaseAttrOperator[DisplayGateMaskColorPlugOperator]
):
    __slots__ = ()

    displayGateMaskColorR = FloatField(default_value=0.5)
    dgcr = displayGateMaskColorR

    displayGateMaskColorG = FloatField(default_value=0.5)
    dgcg = displayGateMaskColorG

    displayGateMaskColorB = FloatField(default_value=0.5)
    dgcb = displayGateMaskColorB


class DisplayGateMaskColorField(
    Float3CompoundBaseField[DisplayGateMaskColorAttrOperator, DisplayGateMaskColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayGateMaskColorAttrOperator
    PLUG_CLS = DisplayGateMaskColorPlugOperator

    displayGateMaskColorR = FloatField(default_value=0.5)
    dgcr = displayGateMaskColorR

    displayGateMaskColorG = FloatField(default_value=0.5)
    dgcg = displayGateMaskColorG

    displayGateMaskColorB = FloatField(default_value=0.5)
    dgcb = displayGateMaskColorB


class BackgroundColorPlugOperator(
    Float3CompoundBasePlugOperator["BackgroundColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backgroundColorR", "colr"),
        ("backgroundColorG", "colg"),
        ("backgroundColorB", "colb"),
    )

    backgroundColorR = FloatField(default_value=0.0)
    colr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.0)
    colg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.0)
    colb = backgroundColorB


class BackgroundColorAttrOperator(
    Float3CompoundBaseAttrOperator[BackgroundColorPlugOperator]
):
    __slots__ = ()

    backgroundColorR = FloatField(default_value=0.0)
    colr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.0)
    colg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.0)
    colb = backgroundColorB


class BackgroundColorField(
    Float3CompoundBaseField[BackgroundColorAttrOperator, BackgroundColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BackgroundColorAttrOperator
    PLUG_CLS = BackgroundColorPlugOperator

    backgroundColorR = FloatField(default_value=0.0)
    colr = backgroundColorR

    backgroundColorG = FloatField(default_value=0.0)
    colg = backgroundColorG

    backgroundColorB = FloatField(default_value=0.0)
    colb = backgroundColorB


class AiPositionPlugOperator(
    Float3CompoundBasePlugOperator["AiPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiPositionX", "ai_positionx"),
        ("aiPositionY", "ai_positiony"),
        ("aiPositionZ", "ai_positionz"),
    )

    aiPositionX = FloatField(default_value=0.0)
    ai_positionx = aiPositionX

    aiPositionY = FloatField(default_value=0.0)
    ai_positiony = aiPositionY

    aiPositionZ = FloatField(default_value=0.0)
    ai_positionz = aiPositionZ


class AiPositionAttrOperator(
    Float3CompoundBaseAttrOperator[AiPositionPlugOperator]
):
    __slots__ = ()

    aiPositionX = FloatField(default_value=0.0)
    ai_positionx = aiPositionX

    aiPositionY = FloatField(default_value=0.0)
    ai_positiony = aiPositionY

    aiPositionZ = FloatField(default_value=0.0)
    ai_positionz = aiPositionZ


class AiPositionField(
    Float3CompoundBaseField[AiPositionAttrOperator, AiPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiPositionAttrOperator
    PLUG_CLS = AiPositionPlugOperator


class AiLookAtPlugOperator(
    Float3CompoundBasePlugOperator["AiLookAtAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiLookAtX", "ai_look_atx"),
        ("aiLookAtY", "ai_look_aty"),
        ("aiLookAtZ", "ai_look_atz"),
    )

    aiLookAtX = FloatField(default_value=0.0)
    ai_look_atx = aiLookAtX

    aiLookAtY = FloatField(default_value=0.0)
    ai_look_aty = aiLookAtY

    aiLookAtZ = FloatField(default_value=-1.0)
    ai_look_atz = aiLookAtZ


class AiLookAtAttrOperator(
    Float3CompoundBaseAttrOperator[AiLookAtPlugOperator]
):
    __slots__ = ()

    aiLookAtX = FloatField(default_value=0.0)
    ai_look_atx = aiLookAtX

    aiLookAtY = FloatField(default_value=0.0)
    ai_look_aty = aiLookAtY

    aiLookAtZ = FloatField(default_value=-1.0)
    ai_look_atz = aiLookAtZ


class AiLookAtField(
    Float3CompoundBaseField[AiLookAtAttrOperator, AiLookAtPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiLookAtAttrOperator
    PLUG_CLS = AiLookAtPlugOperator


class AiUpPlugOperator(
    Float3CompoundBasePlugOperator["AiUpAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiUpX", "ai_upx"),
        ("aiUpY", "ai_upy"),
        ("aiUpZ", "ai_upz"),
    )

    aiUpX = FloatField(default_value=0.0)
    ai_upx = aiUpX

    aiUpY = FloatField(default_value=1.0)
    ai_upy = aiUpY

    aiUpZ = FloatField(default_value=0.0)
    ai_upz = aiUpZ


class AiUpAttrOperator(
    Float3CompoundBaseAttrOperator[AiUpPlugOperator]
):
    __slots__ = ()

    aiUpX = FloatField(default_value=0.0)
    ai_upx = aiUpX

    aiUpY = FloatField(default_value=1.0)
    ai_upy = aiUpY

    aiUpZ = FloatField(default_value=0.0)
    ai_upz = aiUpZ


class AiUpField(
    Float3CompoundBaseField[AiUpAttrOperator, AiUpPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiUpAttrOperator
    PLUG_CLS = AiUpPlugOperator


class AiScreenWindowMinPlugOperator(
    Float2CompoundBasePlugOperator["AiScreenWindowMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiScreenWindowMinX", "ai_screen_window_minx"),
        ("aiScreenWindowMinY", "ai_screen_window_miny"),
    )

    aiScreenWindowMinX = FloatField(default_value=-1.0)
    ai_screen_window_minx = aiScreenWindowMinX

    aiScreenWindowMinY = FloatField(default_value=-1.0)
    ai_screen_window_miny = aiScreenWindowMinY


class AiScreenWindowMinAttrOperator(
    Float2CompoundBaseAttrOperator[AiScreenWindowMinPlugOperator]
):
    __slots__ = ()

    aiScreenWindowMinX = FloatField(default_value=-1.0)
    ai_screen_window_minx = aiScreenWindowMinX

    aiScreenWindowMinY = FloatField(default_value=-1.0)
    ai_screen_window_miny = aiScreenWindowMinY


class AiScreenWindowMinField(
    Float2CompoundBaseField[AiScreenWindowMinAttrOperator, AiScreenWindowMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiScreenWindowMinAttrOperator
    PLUG_CLS = AiScreenWindowMinPlugOperator


class AiScreenWindowMaxPlugOperator(
    Float2CompoundBasePlugOperator["AiScreenWindowMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiScreenWindowMaxX", "ai_screen_window_maxx"),
        ("aiScreenWindowMaxY", "ai_screen_window_maxy"),
    )

    aiScreenWindowMaxX = FloatField(default_value=1.0)
    ai_screen_window_maxx = aiScreenWindowMaxX

    aiScreenWindowMaxY = FloatField(default_value=1.0)
    ai_screen_window_maxy = aiScreenWindowMaxY


class AiScreenWindowMaxAttrOperator(
    Float2CompoundBaseAttrOperator[AiScreenWindowMaxPlugOperator]
):
    __slots__ = ()

    aiScreenWindowMaxX = FloatField(default_value=1.0)
    ai_screen_window_maxx = aiScreenWindowMaxX

    aiScreenWindowMaxY = FloatField(default_value=1.0)
    ai_screen_window_maxy = aiScreenWindowMaxY


class AiScreenWindowMaxField(
    Float2CompoundBaseField[AiScreenWindowMaxAttrOperator, AiScreenWindowMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiScreenWindowMaxAttrOperator
    PLUG_CLS = AiScreenWindowMaxPlugOperator


class AiShutterCurvePlugOperator(
    Float2CompoundBasePlugOperator["AiShutterCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiShutterCurveX", "ai_shutter_curvex"),
        ("aiShutterCurveY", "ai_shutter_curvey"),
    )

    aiShutterCurveX = FloatField(default_value=1206030336.0)
    ai_shutter_curvex = aiShutterCurveX

    aiShutterCurveY = FloatField(default_value=6.978466352337589e-43)
    ai_shutter_curvey = aiShutterCurveY


class AiShutterCurveAttrOperator(
    Float2CompoundBaseAttrOperator[AiShutterCurvePlugOperator]
):
    __slots__ = ()

    aiShutterCurveX = FloatField(default_value=1206030336.0)
    ai_shutter_curvex = aiShutterCurveX

    aiShutterCurveY = FloatField(default_value=6.978466352337589e-43)
    ai_shutter_curvey = aiShutterCurveY


class AiShutterCurveField(
    Float2CompoundBaseField[AiShutterCurveAttrOperator, AiShutterCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiShutterCurveAttrOperator
    PLUG_CLS = AiShutterCurvePlugOperator


class AiRayOriginPlugOperator(
    Float3CompoundBasePlugOperator["AiRayOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiRayOriginX", "ai_ray_originx"),
        ("aiRayOriginY", "ai_ray_originy"),
        ("aiRayOriginZ", "ai_ray_originz"),
    )

    aiRayOriginX = FloatField(default_value=0.0)
    ai_ray_originx = aiRayOriginX

    aiRayOriginY = FloatField(default_value=0.0)
    ai_ray_originy = aiRayOriginY

    aiRayOriginZ = FloatField(default_value=0.0)
    ai_ray_originz = aiRayOriginZ


class AiRayOriginAttrOperator(
    Float3CompoundBaseAttrOperator[AiRayOriginPlugOperator]
):
    __slots__ = ()

    aiRayOriginX = FloatField(default_value=0.0)
    ai_ray_originx = aiRayOriginX

    aiRayOriginY = FloatField(default_value=0.0)
    ai_ray_originy = aiRayOriginY

    aiRayOriginZ = FloatField(default_value=0.0)
    ai_ray_originz = aiRayOriginZ


class AiRayOriginField(
    Float3CompoundBaseField[AiRayOriginAttrOperator, AiRayOriginPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiRayOriginAttrOperator
    PLUG_CLS = AiRayOriginPlugOperator

    aiRayOriginX = FloatField(default_value=0.0)
    ai_ray_originx = aiRayOriginX

    aiRayOriginY = FloatField(default_value=0.0)
    ai_ray_originy = aiRayOriginY

    aiRayOriginZ = FloatField(default_value=0.0)
    ai_ray_originz = aiRayOriginZ


class AiRayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["AiRayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiRayDirectionX", "ai_ray_directionx"),
        ("aiRayDirectionY", "ai_ray_directiony"),
        ("aiRayDirectionZ", "ai_ray_directionz"),
    )

    aiRayDirectionX = FloatField(default_value=0.0)
    ai_ray_directionx = aiRayDirectionX

    aiRayDirectionY = FloatField(default_value=0.0)
    ai_ray_directiony = aiRayDirectionY

    aiRayDirectionZ = FloatField(default_value=0.0)
    ai_ray_directionz = aiRayDirectionZ


class AiRayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[AiRayDirectionPlugOperator]
):
    __slots__ = ()

    aiRayDirectionX = FloatField(default_value=0.0)
    ai_ray_directionx = aiRayDirectionX

    aiRayDirectionY = FloatField(default_value=0.0)
    ai_ray_directiony = aiRayDirectionY

    aiRayDirectionZ = FloatField(default_value=0.0)
    ai_ray_directionz = aiRayDirectionZ


class AiRayDirectionField(
    Float3CompoundBaseField[AiRayDirectionAttrOperator, AiRayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiRayDirectionAttrOperator
    PLUG_CLS = AiRayDirectionPlugOperator

    aiRayDirectionX = FloatField(default_value=0.0)
    ai_ray_directionx = aiRayDirectionX

    aiRayDirectionY = FloatField(default_value=0.0)
    ai_ray_directiony = aiRayDirectionY

    aiRayDirectionZ = FloatField(default_value=0.0)
    ai_ray_directionz = aiRayDirectionZ


class AiUvRemapPlugOperator(
    Float3CompoundBasePlugOperator["AiUvRemapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiUvRemapR", "ai_uv_remapr"),
        ("aiUvRemapG", "ai_uv_remapg"),
        ("aiUvRemapB", "ai_uv_remapb"),
    )

    aiUvRemapR = FloatField(default_value=0.0)
    ai_uv_remapr = aiUvRemapR

    aiUvRemapG = FloatField(default_value=0.0)
    ai_uv_remapg = aiUvRemapG

    aiUvRemapB = FloatField(default_value=0.0)
    ai_uv_remapb = aiUvRemapB


class AiUvRemapAttrOperator(
    Float3CompoundBaseAttrOperator[AiUvRemapPlugOperator]
):
    __slots__ = ()

    aiUvRemapR = FloatField(default_value=0.0)
    ai_uv_remapr = aiUvRemapR

    aiUvRemapG = FloatField(default_value=0.0)
    ai_uv_remapg = aiUvRemapG

    aiUvRemapB = FloatField(default_value=0.0)
    ai_uv_remapb = aiUvRemapB


class AiUvRemapField(
    Float3CompoundBaseField[AiUvRemapAttrOperator, AiUvRemapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiUvRemapAttrOperator
    PLUG_CLS = AiUvRemapPlugOperator

    aiUvRemapR = FloatField(default_value=0.0)
    ai_uv_remapr = aiUvRemapR

    aiUvRemapG = FloatField(default_value=0.0)
    ai_uv_remapg = aiUvRemapG

    aiUvRemapB = FloatField(default_value=0.0)
    ai_uv_remapb = aiUvRemapB


class AiLensTiltAnglePlugOperator(
    Float2CompoundBasePlugOperator["AiLensTiltAngleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiLensTiltAngleX", "ai_lens_tilt_anglex"),
        ("aiLensTiltAngleY", "ai_lens_tilt_angley"),
    )

    aiLensTiltAngleX = FloatField(default_value=0.0)
    ai_lens_tilt_anglex = aiLensTiltAngleX

    aiLensTiltAngleY = FloatField(default_value=0.0)
    ai_lens_tilt_angley = aiLensTiltAngleY


class AiLensTiltAngleAttrOperator(
    Float2CompoundBaseAttrOperator[AiLensTiltAnglePlugOperator]
):
    __slots__ = ()

    aiLensTiltAngleX = FloatField(default_value=0.0)
    ai_lens_tilt_anglex = aiLensTiltAngleX

    aiLensTiltAngleY = FloatField(default_value=0.0)
    ai_lens_tilt_angley = aiLensTiltAngleY


class AiLensTiltAngleField(
    Float2CompoundBaseField[AiLensTiltAngleAttrOperator, AiLensTiltAnglePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiLensTiltAngleAttrOperator
    PLUG_CLS = AiLensTiltAnglePlugOperator

    aiLensTiltAngleX = FloatField(default_value=0.0)
    ai_lens_tilt_anglex = aiLensTiltAngleX

    aiLensTiltAngleY = FloatField(default_value=0.0)
    ai_lens_tilt_angley = aiLensTiltAngleY


class AiLensShiftPlugOperator(
    Float2CompoundBasePlugOperator["AiLensShiftAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiLensShiftX", "ai_lens_shiftx"),
        ("aiLensShiftY", "ai_lens_shifty"),
    )

    aiLensShiftX = FloatField(default_value=0.0)
    ai_lens_shiftx = aiLensShiftX

    aiLensShiftY = FloatField(default_value=0.0)
    ai_lens_shifty = aiLensShiftY


class AiLensShiftAttrOperator(
    Float2CompoundBaseAttrOperator[AiLensShiftPlugOperator]
):
    __slots__ = ()

    aiLensShiftX = FloatField(default_value=0.0)
    ai_lens_shiftx = aiLensShiftX

    aiLensShiftY = FloatField(default_value=0.0)
    ai_lens_shifty = aiLensShiftY


class AiLensShiftField(
    Float2CompoundBaseField[AiLensShiftAttrOperator, AiLensShiftPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiLensShiftAttrOperator
    PLUG_CLS = AiLensShiftPlugOperator

    aiLensShiftX = FloatField(default_value=0.0)
    ai_lens_shiftx = aiLensShiftX

    aiLensShiftY = FloatField(default_value=0.0)
    ai_lens_shifty = aiLensShiftY
