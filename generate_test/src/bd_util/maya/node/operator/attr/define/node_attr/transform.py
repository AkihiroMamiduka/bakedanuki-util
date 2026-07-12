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
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field
from ..custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.quat_compound._base import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)
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
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)
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


class TranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["TranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateX", "tx"),
        ("translateY", "ty"),
        ("translateZ", "tz"),
    )

    translateX = DoubleLinearField(default_value=0.0)
    tx = translateX

    translateY = DoubleLinearField(default_value=0.0)
    ty = translateY

    translateZ = DoubleLinearField(default_value=0.0)
    tz = translateZ


class TranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TranslatePlugOperator]
):
    __slots__ = ()

    translateX = DoubleLinearField(default_value=0.0)
    tx = translateX

    translateY = DoubleLinearField(default_value=0.0)
    ty = translateY

    translateZ = DoubleLinearField(default_value=0.0)
    tz = translateZ


class TranslateField(
    DoubleLinear3CompoundBaseField[TranslateAttrOperator, TranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateAttrOperator
    PLUG_CLS = TranslatePlugOperator

    translateX = DoubleLinearField(default_value=0.0)
    tx = translateX

    translateY = DoubleLinearField(default_value=0.0)
    ty = translateY

    translateZ = DoubleLinearField(default_value=0.0)
    tz = translateZ


class RotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateX", "rx"),
        ("rotateY", "ry"),
        ("rotateZ", "rz"),
    )

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class RotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class RotateField(
    DoubleAngle3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class ScalePlugOperator(
    Double3CompoundBasePlugOperator["ScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "sx"),
        ("scaleY", "sy"),
        ("scaleZ", "sz"),
    )

    scaleX = DoubleField(default_value=1.0)
    sx = scaleX

    scaleY = DoubleField(default_value=1.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=1.0)
    sz = scaleZ


class ScaleAttrOperator(
    Double3CompoundBaseAttrOperator[ScalePlugOperator]
):
    __slots__ = ()

    scaleX = DoubleField(default_value=1.0)
    sx = scaleX

    scaleY = DoubleField(default_value=1.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=1.0)
    sz = scaleZ


class ScaleField(
    Double3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = DoubleField(default_value=1.0)
    sx = scaleX

    scaleY = DoubleField(default_value=1.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=1.0)
    sz = scaleZ


class ShearPlugOperator(
    Double3CompoundBasePlugOperator["ShearAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shearXY", "shxy"),
        ("shearXZ", "shxz"),
        ("shearYZ", "shyz"),
    )

    shearXY = DoubleField(default_value=0.0)
    shxy = shearXY

    shearXZ = DoubleField(default_value=0.0)
    shxz = shearXZ

    shearYZ = DoubleField(default_value=0.0)
    shyz = shearYZ


class ShearAttrOperator(
    Double3CompoundBaseAttrOperator[ShearPlugOperator]
):
    __slots__ = ()

    shearXY = DoubleField(default_value=0.0)
    shxy = shearXY

    shearXZ = DoubleField(default_value=0.0)
    shxz = shearXZ

    shearYZ = DoubleField(default_value=0.0)
    shyz = shearYZ


class ShearField(
    Double3CompoundBaseField[ShearAttrOperator, ShearPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShearAttrOperator
    PLUG_CLS = ShearPlugOperator

    shearXY = DoubleField(default_value=0.0)
    shxy = shearXY

    shearXZ = DoubleField(default_value=0.0)
    shxz = shearXZ

    shearYZ = DoubleField(default_value=0.0)
    shyz = shearYZ


class RotatePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["RotatePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotatePivotX", "rpx"),
        ("rotatePivotY", "rpy"),
        ("rotatePivotZ", "rpz"),
    )

    rotatePivotX = DoubleLinearField(default_value=0.0)
    rpx = rotatePivotX

    rotatePivotY = DoubleLinearField(default_value=0.0)
    rpy = rotatePivotY

    rotatePivotZ = DoubleLinearField(default_value=0.0)
    rpz = rotatePivotZ


class RotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[RotatePivotPlugOperator]
):
    __slots__ = ()

    rotatePivotX = DoubleLinearField(default_value=0.0)
    rpx = rotatePivotX

    rotatePivotY = DoubleLinearField(default_value=0.0)
    rpy = rotatePivotY

    rotatePivotZ = DoubleLinearField(default_value=0.0)
    rpz = rotatePivotZ


class RotatePivotField(
    DoubleLinear3CompoundBaseField[RotatePivotAttrOperator, RotatePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotatePivotAttrOperator
    PLUG_CLS = RotatePivotPlugOperator

    rotatePivotX = DoubleLinearField(default_value=0.0)
    rpx = rotatePivotX

    rotatePivotY = DoubleLinearField(default_value=0.0)
    rpy = rotatePivotY

    rotatePivotZ = DoubleLinearField(default_value=0.0)
    rpz = rotatePivotZ


class RotatePivotTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["RotatePivotTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotatePivotTranslateX", "rptx"),
        ("rotatePivotTranslateY", "rpty"),
        ("rotatePivotTranslateZ", "rptz"),
    )

    rotatePivotTranslateX = DoubleLinearField(default_value=0.0)
    rptx = rotatePivotTranslateX

    rotatePivotTranslateY = DoubleLinearField(default_value=0.0)
    rpty = rotatePivotTranslateY

    rotatePivotTranslateZ = DoubleLinearField(default_value=0.0)
    rptz = rotatePivotTranslateZ


class RotatePivotTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[RotatePivotTranslatePlugOperator]
):
    __slots__ = ()

    rotatePivotTranslateX = DoubleLinearField(default_value=0.0)
    rptx = rotatePivotTranslateX

    rotatePivotTranslateY = DoubleLinearField(default_value=0.0)
    rpty = rotatePivotTranslateY

    rotatePivotTranslateZ = DoubleLinearField(default_value=0.0)
    rptz = rotatePivotTranslateZ


class RotatePivotTranslateField(
    DoubleLinear3CompoundBaseField[RotatePivotTranslateAttrOperator, RotatePivotTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotatePivotTranslateAttrOperator
    PLUG_CLS = RotatePivotTranslatePlugOperator

    rotatePivotTranslateX = DoubleLinearField(default_value=0.0)
    rptx = rotatePivotTranslateX

    rotatePivotTranslateY = DoubleLinearField(default_value=0.0)
    rpty = rotatePivotTranslateY

    rotatePivotTranslateZ = DoubleLinearField(default_value=0.0)
    rptz = rotatePivotTranslateZ


class ScalePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ScalePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scalePivotX", "spx"),
        ("scalePivotY", "spy"),
        ("scalePivotZ", "spz"),
    )

    scalePivotX = DoubleLinearField(default_value=0.0)
    spx = scalePivotX

    scalePivotY = DoubleLinearField(default_value=0.0)
    spy = scalePivotY

    scalePivotZ = DoubleLinearField(default_value=0.0)
    spz = scalePivotZ


class ScalePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ScalePivotPlugOperator]
):
    __slots__ = ()

    scalePivotX = DoubleLinearField(default_value=0.0)
    spx = scalePivotX

    scalePivotY = DoubleLinearField(default_value=0.0)
    spy = scalePivotY

    scalePivotZ = DoubleLinearField(default_value=0.0)
    spz = scalePivotZ


class ScalePivotField(
    DoubleLinear3CompoundBaseField[ScalePivotAttrOperator, ScalePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScalePivotAttrOperator
    PLUG_CLS = ScalePivotPlugOperator

    scalePivotX = DoubleLinearField(default_value=0.0)
    spx = scalePivotX

    scalePivotY = DoubleLinearField(default_value=0.0)
    spy = scalePivotY

    scalePivotZ = DoubleLinearField(default_value=0.0)
    spz = scalePivotZ


class ScalePivotTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ScalePivotTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scalePivotTranslateX", "sptx"),
        ("scalePivotTranslateY", "spty"),
        ("scalePivotTranslateZ", "sptz"),
    )

    scalePivotTranslateX = DoubleLinearField(default_value=0.0)
    sptx = scalePivotTranslateX

    scalePivotTranslateY = DoubleLinearField(default_value=0.0)
    spty = scalePivotTranslateY

    scalePivotTranslateZ = DoubleLinearField(default_value=0.0)
    sptz = scalePivotTranslateZ


class ScalePivotTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ScalePivotTranslatePlugOperator]
):
    __slots__ = ()

    scalePivotTranslateX = DoubleLinearField(default_value=0.0)
    sptx = scalePivotTranslateX

    scalePivotTranslateY = DoubleLinearField(default_value=0.0)
    spty = scalePivotTranslateY

    scalePivotTranslateZ = DoubleLinearField(default_value=0.0)
    sptz = scalePivotTranslateZ


class ScalePivotTranslateField(
    DoubleLinear3CompoundBaseField[ScalePivotTranslateAttrOperator, ScalePivotTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScalePivotTranslateAttrOperator
    PLUG_CLS = ScalePivotTranslatePlugOperator

    scalePivotTranslateX = DoubleLinearField(default_value=0.0)
    sptx = scalePivotTranslateX

    scalePivotTranslateY = DoubleLinearField(default_value=0.0)
    spty = scalePivotTranslateY

    scalePivotTranslateZ = DoubleLinearField(default_value=0.0)
    sptz = scalePivotTranslateZ


class RotateAxisPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RotateAxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateAxisX", "rax"),
        ("rotateAxisY", "ray"),
        ("rotateAxisZ", "raz"),
    )

    rotateAxisX = DoubleAngleField(default_value=0.0)
    rax = rotateAxisX

    rotateAxisY = DoubleAngleField(default_value=0.0)
    ray = rotateAxisY

    rotateAxisZ = DoubleAngleField(default_value=0.0)
    raz = rotateAxisZ


class RotateAxisAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RotateAxisPlugOperator]
):
    __slots__ = ()

    rotateAxisX = DoubleAngleField(default_value=0.0)
    rax = rotateAxisX

    rotateAxisY = DoubleAngleField(default_value=0.0)
    ray = rotateAxisY

    rotateAxisZ = DoubleAngleField(default_value=0.0)
    raz = rotateAxisZ


class RotateAxisField(
    DoubleAngle3CompoundBaseField[RotateAxisAttrOperator, RotateAxisPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAxisAttrOperator
    PLUG_CLS = RotateAxisPlugOperator

    rotateAxisX = DoubleAngleField(default_value=0.0)
    rax = rotateAxisX

    rotateAxisY = DoubleAngleField(default_value=0.0)
    ray = rotateAxisY

    rotateAxisZ = DoubleAngleField(default_value=0.0)
    raz = rotateAxisZ


class TransMinusRotatePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["TransMinusRotatePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transMinusRotatePivotX", "tmrx"),
        ("transMinusRotatePivotY", "tmry"),
        ("transMinusRotatePivotZ", "tmrz"),
    )

    transMinusRotatePivotX = DoubleLinearField(default_value=0.0, writable=False)
    tmrx = transMinusRotatePivotX

    transMinusRotatePivotY = DoubleLinearField(default_value=0.0, writable=False)
    tmry = transMinusRotatePivotY

    transMinusRotatePivotZ = DoubleLinearField(default_value=0.0, writable=False)
    tmrz = transMinusRotatePivotZ


class TransMinusRotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TransMinusRotatePivotPlugOperator]
):
    __slots__ = ()

    transMinusRotatePivotX = DoubleLinearField(default_value=0.0, writable=False)
    tmrx = transMinusRotatePivotX

    transMinusRotatePivotY = DoubleLinearField(default_value=0.0, writable=False)
    tmry = transMinusRotatePivotY

    transMinusRotatePivotZ = DoubleLinearField(default_value=0.0, writable=False)
    tmrz = transMinusRotatePivotZ


class TransMinusRotatePivotField(
    DoubleLinear3CompoundBaseField[TransMinusRotatePivotAttrOperator, TransMinusRotatePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransMinusRotatePivotAttrOperator
    PLUG_CLS = TransMinusRotatePivotPlugOperator

    transMinusRotatePivotX = DoubleLinearField(default_value=0.0, writable=False)
    tmrx = transMinusRotatePivotX

    transMinusRotatePivotY = DoubleLinearField(default_value=0.0, writable=False)
    tmry = transMinusRotatePivotY

    transMinusRotatePivotZ = DoubleLinearField(default_value=0.0, writable=False)
    tmrz = transMinusRotatePivotZ


class MinTransLimitPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["MinTransLimitAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minTransXLimit", "mtxl"),
        ("minTransYLimit", "mtyl"),
        ("minTransZLimit", "mtzl"),
    )

    minTransXLimit = DoubleLinearField(default_value=-1.0)
    mtxl = minTransXLimit

    minTransYLimit = DoubleLinearField(default_value=-1.0)
    mtyl = minTransYLimit

    minTransZLimit = DoubleLinearField(default_value=-1.0)
    mtzl = minTransZLimit


class MinTransLimitAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[MinTransLimitPlugOperator]
):
    __slots__ = ()

    minTransXLimit = DoubleLinearField(default_value=-1.0)
    mtxl = minTransXLimit

    minTransYLimit = DoubleLinearField(default_value=-1.0)
    mtyl = minTransYLimit

    minTransZLimit = DoubleLinearField(default_value=-1.0)
    mtzl = minTransZLimit


class MinTransLimitField(
    DoubleLinear3CompoundBaseField[MinTransLimitAttrOperator, MinTransLimitPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinTransLimitAttrOperator
    PLUG_CLS = MinTransLimitPlugOperator

    minTransXLimit = DoubleLinearField(default_value=-1.0)
    mtxl = minTransXLimit

    minTransYLimit = DoubleLinearField(default_value=-1.0)
    mtyl = minTransYLimit

    minTransZLimit = DoubleLinearField(default_value=-1.0)
    mtzl = minTransZLimit


class MaxTransLimitPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["MaxTransLimitAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxTransXLimit", "xtxl"),
        ("maxTransYLimit", "xtyl"),
        ("maxTransZLimit", "xtzl"),
    )

    maxTransXLimit = DoubleLinearField(default_value=1.0)
    xtxl = maxTransXLimit

    maxTransYLimit = DoubleLinearField(default_value=1.0)
    xtyl = maxTransYLimit

    maxTransZLimit = DoubleLinearField(default_value=1.0)
    xtzl = maxTransZLimit


class MaxTransLimitAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[MaxTransLimitPlugOperator]
):
    __slots__ = ()

    maxTransXLimit = DoubleLinearField(default_value=1.0)
    xtxl = maxTransXLimit

    maxTransYLimit = DoubleLinearField(default_value=1.0)
    xtyl = maxTransYLimit

    maxTransZLimit = DoubleLinearField(default_value=1.0)
    xtzl = maxTransZLimit


class MaxTransLimitField(
    DoubleLinear3CompoundBaseField[MaxTransLimitAttrOperator, MaxTransLimitPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxTransLimitAttrOperator
    PLUG_CLS = MaxTransLimitPlugOperator

    maxTransXLimit = DoubleLinearField(default_value=1.0)
    xtxl = maxTransXLimit

    maxTransYLimit = DoubleLinearField(default_value=1.0)
    xtyl = maxTransYLimit

    maxTransZLimit = DoubleLinearField(default_value=1.0)
    xtzl = maxTransZLimit


class MinTransLimitEnablePlugOperator(
    CompoundPlugOperator["MinTransLimitEnableAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minTransXLimitEnable", "mtxe"),
        ("minTransYLimitEnable", "mtye"),
        ("minTransZLimitEnable", "mtze"),
    )

    minTransXLimitEnable = BoolField(default_value=False)
    mtxe = minTransXLimitEnable

    minTransYLimitEnable = BoolField(default_value=False)
    mtye = minTransYLimitEnable

    minTransZLimitEnable = BoolField(default_value=False)
    mtze = minTransZLimitEnable


class MinTransLimitEnableAttrOperator(
    CompoundAttrOperator[MinTransLimitEnablePlugOperator]
):
    __slots__ = ()

    minTransXLimitEnable = BoolField(default_value=False)
    mtxe = minTransXLimitEnable

    minTransYLimitEnable = BoolField(default_value=False)
    mtye = minTransYLimitEnable

    minTransZLimitEnable = BoolField(default_value=False)
    mtze = minTransZLimitEnable


class MinTransLimitEnableField(
    CompoundField[MinTransLimitEnableAttrOperator, MinTransLimitEnablePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinTransLimitEnableAttrOperator
    PLUG_CLS = MinTransLimitEnablePlugOperator

    minTransXLimitEnable = BoolField(default_value=False)
    mtxe = minTransXLimitEnable

    minTransYLimitEnable = BoolField(default_value=False)
    mtye = minTransYLimitEnable

    minTransZLimitEnable = BoolField(default_value=False)
    mtze = minTransZLimitEnable


class MaxTransLimitEnablePlugOperator(
    CompoundPlugOperator["MaxTransLimitEnableAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxTransXLimitEnable", "xtxe"),
        ("maxTransYLimitEnable", "xtye"),
        ("maxTransZLimitEnable", "xtze"),
    )

    maxTransXLimitEnable = BoolField(default_value=False)
    xtxe = maxTransXLimitEnable

    maxTransYLimitEnable = BoolField(default_value=False)
    xtye = maxTransYLimitEnable

    maxTransZLimitEnable = BoolField(default_value=False)
    xtze = maxTransZLimitEnable


class MaxTransLimitEnableAttrOperator(
    CompoundAttrOperator[MaxTransLimitEnablePlugOperator]
):
    __slots__ = ()

    maxTransXLimitEnable = BoolField(default_value=False)
    xtxe = maxTransXLimitEnable

    maxTransYLimitEnable = BoolField(default_value=False)
    xtye = maxTransYLimitEnable

    maxTransZLimitEnable = BoolField(default_value=False)
    xtze = maxTransZLimitEnable


class MaxTransLimitEnableField(
    CompoundField[MaxTransLimitEnableAttrOperator, MaxTransLimitEnablePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxTransLimitEnableAttrOperator
    PLUG_CLS = MaxTransLimitEnablePlugOperator

    maxTransXLimitEnable = BoolField(default_value=False)
    xtxe = maxTransXLimitEnable

    maxTransYLimitEnable = BoolField(default_value=False)
    xtye = maxTransYLimitEnable

    maxTransZLimitEnable = BoolField(default_value=False)
    xtze = maxTransZLimitEnable


class MinRotLimitPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["MinRotLimitAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minRotXLimit", "mrxl"),
        ("minRotYLimit", "mryl"),
        ("minRotZLimit", "mrzl"),
    )

    minRotXLimit = DoubleAngleField(default_value=-45.0)
    mrxl = minRotXLimit

    minRotYLimit = DoubleAngleField(default_value=-45.0)
    mryl = minRotYLimit

    minRotZLimit = DoubleAngleField(default_value=-45.0)
    mrzl = minRotZLimit


class MinRotLimitAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[MinRotLimitPlugOperator]
):
    __slots__ = ()

    minRotXLimit = DoubleAngleField(default_value=-45.0)
    mrxl = minRotXLimit

    minRotYLimit = DoubleAngleField(default_value=-45.0)
    mryl = minRotYLimit

    minRotZLimit = DoubleAngleField(default_value=-45.0)
    mrzl = minRotZLimit


class MinRotLimitField(
    DoubleAngle3CompoundBaseField[MinRotLimitAttrOperator, MinRotLimitPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinRotLimitAttrOperator
    PLUG_CLS = MinRotLimitPlugOperator

    minRotXLimit = DoubleAngleField(default_value=-45.0)
    mrxl = minRotXLimit

    minRotYLimit = DoubleAngleField(default_value=-45.0)
    mryl = minRotYLimit

    minRotZLimit = DoubleAngleField(default_value=-45.0)
    mrzl = minRotZLimit


class MaxRotLimitPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["MaxRotLimitAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxRotXLimit", "xrxl"),
        ("maxRotYLimit", "xryl"),
        ("maxRotZLimit", "xrzl"),
    )

    maxRotXLimit = DoubleAngleField(default_value=45.0)
    xrxl = maxRotXLimit

    maxRotYLimit = DoubleAngleField(default_value=45.0)
    xryl = maxRotYLimit

    maxRotZLimit = DoubleAngleField(default_value=45.0)
    xrzl = maxRotZLimit


class MaxRotLimitAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[MaxRotLimitPlugOperator]
):
    __slots__ = ()

    maxRotXLimit = DoubleAngleField(default_value=45.0)
    xrxl = maxRotXLimit

    maxRotYLimit = DoubleAngleField(default_value=45.0)
    xryl = maxRotYLimit

    maxRotZLimit = DoubleAngleField(default_value=45.0)
    xrzl = maxRotZLimit


class MaxRotLimitField(
    DoubleAngle3CompoundBaseField[MaxRotLimitAttrOperator, MaxRotLimitPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxRotLimitAttrOperator
    PLUG_CLS = MaxRotLimitPlugOperator

    maxRotXLimit = DoubleAngleField(default_value=45.0)
    xrxl = maxRotXLimit

    maxRotYLimit = DoubleAngleField(default_value=45.0)
    xryl = maxRotYLimit

    maxRotZLimit = DoubleAngleField(default_value=45.0)
    xrzl = maxRotZLimit


class MinRotLimitEnablePlugOperator(
    CompoundPlugOperator["MinRotLimitEnableAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minRotXLimitEnable", "mrxe"),
        ("minRotYLimitEnable", "mrye"),
        ("minRotZLimitEnable", "mrze"),
    )

    minRotXLimitEnable = BoolField(default_value=False)
    mrxe = minRotXLimitEnable

    minRotYLimitEnable = BoolField(default_value=False)
    mrye = minRotYLimitEnable

    minRotZLimitEnable = BoolField(default_value=False)
    mrze = minRotZLimitEnable


class MinRotLimitEnableAttrOperator(
    CompoundAttrOperator[MinRotLimitEnablePlugOperator]
):
    __slots__ = ()

    minRotXLimitEnable = BoolField(default_value=False)
    mrxe = minRotXLimitEnable

    minRotYLimitEnable = BoolField(default_value=False)
    mrye = minRotYLimitEnable

    minRotZLimitEnable = BoolField(default_value=False)
    mrze = minRotZLimitEnable


class MinRotLimitEnableField(
    CompoundField[MinRotLimitEnableAttrOperator, MinRotLimitEnablePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinRotLimitEnableAttrOperator
    PLUG_CLS = MinRotLimitEnablePlugOperator

    minRotXLimitEnable = BoolField(default_value=False)
    mrxe = minRotXLimitEnable

    minRotYLimitEnable = BoolField(default_value=False)
    mrye = minRotYLimitEnable

    minRotZLimitEnable = BoolField(default_value=False)
    mrze = minRotZLimitEnable


class MaxRotLimitEnablePlugOperator(
    CompoundPlugOperator["MaxRotLimitEnableAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxRotXLimitEnable", "xrxe"),
        ("maxRotYLimitEnable", "xrye"),
        ("maxRotZLimitEnable", "xrze"),
    )

    maxRotXLimitEnable = BoolField(default_value=False)
    xrxe = maxRotXLimitEnable

    maxRotYLimitEnable = BoolField(default_value=False)
    xrye = maxRotYLimitEnable

    maxRotZLimitEnable = BoolField(default_value=False)
    xrze = maxRotZLimitEnable


class MaxRotLimitEnableAttrOperator(
    CompoundAttrOperator[MaxRotLimitEnablePlugOperator]
):
    __slots__ = ()

    maxRotXLimitEnable = BoolField(default_value=False)
    xrxe = maxRotXLimitEnable

    maxRotYLimitEnable = BoolField(default_value=False)
    xrye = maxRotYLimitEnable

    maxRotZLimitEnable = BoolField(default_value=False)
    xrze = maxRotZLimitEnable


class MaxRotLimitEnableField(
    CompoundField[MaxRotLimitEnableAttrOperator, MaxRotLimitEnablePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxRotLimitEnableAttrOperator
    PLUG_CLS = MaxRotLimitEnablePlugOperator

    maxRotXLimitEnable = BoolField(default_value=False)
    xrxe = maxRotXLimitEnable

    maxRotYLimitEnable = BoolField(default_value=False)
    xrye = maxRotYLimitEnable

    maxRotZLimitEnable = BoolField(default_value=False)
    xrze = maxRotZLimitEnable


class MinScaleLimitPlugOperator(
    Double3CompoundBasePlugOperator["MinScaleLimitAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minScaleXLimit", "msxl"),
        ("minScaleYLimit", "msyl"),
        ("minScaleZLimit", "mszl"),
    )

    minScaleXLimit = DoubleField(default_value=-1.0)
    msxl = minScaleXLimit

    minScaleYLimit = DoubleField(default_value=-1.0)
    msyl = minScaleYLimit

    minScaleZLimit = DoubleField(default_value=-1.0)
    mszl = minScaleZLimit


class MinScaleLimitAttrOperator(
    Double3CompoundBaseAttrOperator[MinScaleLimitPlugOperator]
):
    __slots__ = ()

    minScaleXLimit = DoubleField(default_value=-1.0)
    msxl = minScaleXLimit

    minScaleYLimit = DoubleField(default_value=-1.0)
    msyl = minScaleYLimit

    minScaleZLimit = DoubleField(default_value=-1.0)
    mszl = minScaleZLimit


class MinScaleLimitField(
    Double3CompoundBaseField[MinScaleLimitAttrOperator, MinScaleLimitPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinScaleLimitAttrOperator
    PLUG_CLS = MinScaleLimitPlugOperator

    minScaleXLimit = DoubleField(default_value=-1.0)
    msxl = minScaleXLimit

    minScaleYLimit = DoubleField(default_value=-1.0)
    msyl = minScaleYLimit

    minScaleZLimit = DoubleField(default_value=-1.0)
    mszl = minScaleZLimit


class MaxScaleLimitPlugOperator(
    Double3CompoundBasePlugOperator["MaxScaleLimitAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxScaleXLimit", "xsxl"),
        ("maxScaleYLimit", "xsyl"),
        ("maxScaleZLimit", "xszl"),
    )

    maxScaleXLimit = DoubleField(default_value=1.0)
    xsxl = maxScaleXLimit

    maxScaleYLimit = DoubleField(default_value=1.0)
    xsyl = maxScaleYLimit

    maxScaleZLimit = DoubleField(default_value=1.0)
    xszl = maxScaleZLimit


class MaxScaleLimitAttrOperator(
    Double3CompoundBaseAttrOperator[MaxScaleLimitPlugOperator]
):
    __slots__ = ()

    maxScaleXLimit = DoubleField(default_value=1.0)
    xsxl = maxScaleXLimit

    maxScaleYLimit = DoubleField(default_value=1.0)
    xsyl = maxScaleYLimit

    maxScaleZLimit = DoubleField(default_value=1.0)
    xszl = maxScaleZLimit


class MaxScaleLimitField(
    Double3CompoundBaseField[MaxScaleLimitAttrOperator, MaxScaleLimitPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxScaleLimitAttrOperator
    PLUG_CLS = MaxScaleLimitPlugOperator

    maxScaleXLimit = DoubleField(default_value=1.0)
    xsxl = maxScaleXLimit

    maxScaleYLimit = DoubleField(default_value=1.0)
    xsyl = maxScaleYLimit

    maxScaleZLimit = DoubleField(default_value=1.0)
    xszl = maxScaleZLimit


class MinScaleLimitEnablePlugOperator(
    CompoundPlugOperator["MinScaleLimitEnableAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minScaleXLimitEnable", "msxe"),
        ("minScaleYLimitEnable", "msye"),
        ("minScaleZLimitEnable", "msze"),
    )

    minScaleXLimitEnable = BoolField(default_value=False)
    msxe = minScaleXLimitEnable

    minScaleYLimitEnable = BoolField(default_value=False)
    msye = minScaleYLimitEnable

    minScaleZLimitEnable = BoolField(default_value=False)
    msze = minScaleZLimitEnable


class MinScaleLimitEnableAttrOperator(
    CompoundAttrOperator[MinScaleLimitEnablePlugOperator]
):
    __slots__ = ()

    minScaleXLimitEnable = BoolField(default_value=False)
    msxe = minScaleXLimitEnable

    minScaleYLimitEnable = BoolField(default_value=False)
    msye = minScaleYLimitEnable

    minScaleZLimitEnable = BoolField(default_value=False)
    msze = minScaleZLimitEnable


class MinScaleLimitEnableField(
    CompoundField[MinScaleLimitEnableAttrOperator, MinScaleLimitEnablePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinScaleLimitEnableAttrOperator
    PLUG_CLS = MinScaleLimitEnablePlugOperator

    minScaleXLimitEnable = BoolField(default_value=False)
    msxe = minScaleXLimitEnable

    minScaleYLimitEnable = BoolField(default_value=False)
    msye = minScaleYLimitEnable

    minScaleZLimitEnable = BoolField(default_value=False)
    msze = minScaleZLimitEnable


class MaxScaleLimitEnablePlugOperator(
    CompoundPlugOperator["MaxScaleLimitEnableAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxScaleXLimitEnable", "xsxe"),
        ("maxScaleYLimitEnable", "xsye"),
        ("maxScaleZLimitEnable", "xsze"),
    )

    maxScaleXLimitEnable = BoolField(default_value=False)
    xsxe = maxScaleXLimitEnable

    maxScaleYLimitEnable = BoolField(default_value=False)
    xsye = maxScaleYLimitEnable

    maxScaleZLimitEnable = BoolField(default_value=False)
    xsze = maxScaleZLimitEnable


class MaxScaleLimitEnableAttrOperator(
    CompoundAttrOperator[MaxScaleLimitEnablePlugOperator]
):
    __slots__ = ()

    maxScaleXLimitEnable = BoolField(default_value=False)
    xsxe = maxScaleXLimitEnable

    maxScaleYLimitEnable = BoolField(default_value=False)
    xsye = maxScaleYLimitEnable

    maxScaleZLimitEnable = BoolField(default_value=False)
    xsze = maxScaleZLimitEnable


class MaxScaleLimitEnableField(
    CompoundField[MaxScaleLimitEnableAttrOperator, MaxScaleLimitEnablePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxScaleLimitEnableAttrOperator
    PLUG_CLS = MaxScaleLimitEnablePlugOperator

    maxScaleXLimitEnable = BoolField(default_value=False)
    xsxe = maxScaleXLimitEnable

    maxScaleYLimitEnable = BoolField(default_value=False)
    xsye = maxScaleYLimitEnable

    maxScaleZLimitEnable = BoolField(default_value=False)
    xsze = maxScaleZLimitEnable


class SelectHandlePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["SelectHandleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("selectHandleX", "hdlx"),
        ("selectHandleY", "hdly"),
        ("selectHandleZ", "hdlz"),
    )

    selectHandleX = DoubleLinearField(default_value=0.0)
    hdlx = selectHandleX

    selectHandleY = DoubleLinearField(default_value=0.0)
    hdly = selectHandleY

    selectHandleZ = DoubleLinearField(default_value=0.0)
    hdlz = selectHandleZ


class SelectHandleAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[SelectHandlePlugOperator]
):
    __slots__ = ()

    selectHandleX = DoubleLinearField(default_value=0.0)
    hdlx = selectHandleX

    selectHandleY = DoubleLinearField(default_value=0.0)
    hdly = selectHandleY

    selectHandleZ = DoubleLinearField(default_value=0.0)
    hdlz = selectHandleZ


class SelectHandleField(
    DoubleLinear3CompoundBaseField[SelectHandleAttrOperator, SelectHandlePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SelectHandleAttrOperator
    PLUG_CLS = SelectHandlePlugOperator

    selectHandleX = DoubleLinearField(default_value=0.0)
    hdlx = selectHandleX

    selectHandleY = DoubleLinearField(default_value=0.0)
    hdly = selectHandleY

    selectHandleZ = DoubleLinearField(default_value=0.0)
    hdlz = selectHandleZ


class RotateQuaternionPlugOperator(
    QuatCompoundBasePlugOperator["RotateQuaternionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateQuaternionX", "rqx"),
        ("rotateQuaternionY", "rqy"),
        ("rotateQuaternionZ", "rqz"),
        ("rotateQuaternionW", "rqw"),
    )

    rotateQuaternionX = DoubleField(default_value=0.0)
    rqx = rotateQuaternionX

    rotateQuaternionY = DoubleField(default_value=0.0)
    rqy = rotateQuaternionY

    rotateQuaternionZ = DoubleField(default_value=0.0)
    rqz = rotateQuaternionZ

    rotateQuaternionW = DoubleField(default_value=0.0)
    rqw = rotateQuaternionW


class RotateQuaternionAttrOperator(
    QuatCompoundBaseAttrOperator[RotateQuaternionPlugOperator]
):
    __slots__ = ()

    rotateQuaternionX = DoubleField(default_value=0.0)
    rqx = rotateQuaternionX

    rotateQuaternionY = DoubleField(default_value=0.0)
    rqy = rotateQuaternionY

    rotateQuaternionZ = DoubleField(default_value=0.0)
    rqz = rotateQuaternionZ

    rotateQuaternionW = DoubleField(default_value=0.0)
    rqw = rotateQuaternionW


class RotateQuaternionField(
    QuatCompoundBaseField[RotateQuaternionAttrOperator, RotateQuaternionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateQuaternionAttrOperator
    PLUG_CLS = RotateQuaternionPlugOperator

    rotateQuaternionX = DoubleField(default_value=0.0)
    rqx = rotateQuaternionX

    rotateQuaternionY = DoubleField(default_value=0.0)
    rqy = rotateQuaternionY

    rotateQuaternionZ = DoubleField(default_value=0.0)
    rqz = rotateQuaternionZ

    rotateQuaternionW = DoubleField(default_value=0.0)
    rqw = rotateQuaternionW
