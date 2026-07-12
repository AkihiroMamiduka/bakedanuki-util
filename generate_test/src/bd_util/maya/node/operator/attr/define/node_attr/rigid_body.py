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
from ..std.at.unit_scalar.time import TimeField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.string import DataStringField
from ..std.dt.vector_array import DataVectorArrayField
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


class InitialPositionPlugOperator(
    Double3CompoundBasePlugOperator["InitialPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialPositionX", "ipx"),
        ("initialPositionY", "ipy"),
        ("initialPositionZ", "ipz"),
    )

    initialPositionX = DoubleField(default_value=0.0)
    ipx = initialPositionX

    initialPositionY = DoubleField(default_value=0.0)
    ipy = initialPositionY

    initialPositionZ = DoubleField(default_value=0.0)
    ipz = initialPositionZ


class InitialPositionAttrOperator(
    Double3CompoundBaseAttrOperator[InitialPositionPlugOperator]
):
    __slots__ = ()

    initialPositionX = DoubleField(default_value=0.0)
    ipx = initialPositionX

    initialPositionY = DoubleField(default_value=0.0)
    ipy = initialPositionY

    initialPositionZ = DoubleField(default_value=0.0)
    ipz = initialPositionZ


class InitialPositionField(
    Double3CompoundBaseField[InitialPositionAttrOperator, InitialPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitialPositionAttrOperator
    PLUG_CLS = InitialPositionPlugOperator

    initialPositionX = DoubleField(default_value=0.0)
    ipx = initialPositionX

    initialPositionY = DoubleField(default_value=0.0)
    ipy = initialPositionY

    initialPositionZ = DoubleField(default_value=0.0)
    ipz = initialPositionZ


class LastPositionPlugOperator(
    Double3CompoundBasePlugOperator["LastPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lastPositionX", "lpx"),
        ("lastPositionY", "lpy"),
        ("lastPositionZ", "lpz"),
    )

    lastPositionX = DoubleField(default_value=0.0, writable=False)
    lpx = lastPositionX

    lastPositionY = DoubleField(default_value=0.0, writable=False)
    lpy = lastPositionY

    lastPositionZ = DoubleField(default_value=0.0, writable=False)
    lpz = lastPositionZ


class LastPositionAttrOperator(
    Double3CompoundBaseAttrOperator[LastPositionPlugOperator]
):
    __slots__ = ()

    lastPositionX = DoubleField(default_value=0.0, writable=False)
    lpx = lastPositionX

    lastPositionY = DoubleField(default_value=0.0, writable=False)
    lpy = lastPositionY

    lastPositionZ = DoubleField(default_value=0.0, writable=False)
    lpz = lastPositionZ


class LastPositionField(
    Double3CompoundBaseField[LastPositionAttrOperator, LastPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LastPositionAttrOperator
    PLUG_CLS = LastPositionPlugOperator

    lastPositionX = DoubleField(default_value=0.0, writable=False)
    lpx = lastPositionX

    lastPositionY = DoubleField(default_value=0.0, writable=False)
    lpy = lastPositionY

    lastPositionZ = DoubleField(default_value=0.0, writable=False)
    lpz = lastPositionZ


class LastRotationPlugOperator(
    Double3CompoundBasePlugOperator["LastRotationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lastRotationX", "lrx"),
        ("lastRotationY", "lry"),
        ("lastRotationZ", "lrz"),
    )

    lastRotationX = DoubleField(default_value=0.0, writable=False)
    lrx = lastRotationX

    lastRotationY = DoubleField(default_value=0.0, writable=False)
    lry = lastRotationY

    lastRotationZ = DoubleField(default_value=0.0, writable=False)
    lrz = lastRotationZ


class LastRotationAttrOperator(
    Double3CompoundBaseAttrOperator[LastRotationPlugOperator]
):
    __slots__ = ()

    lastRotationX = DoubleField(default_value=0.0, writable=False)
    lrx = lastRotationX

    lastRotationY = DoubleField(default_value=0.0, writable=False)
    lry = lastRotationY

    lastRotationZ = DoubleField(default_value=0.0, writable=False)
    lrz = lastRotationZ


class LastRotationField(
    Double3CompoundBaseField[LastRotationAttrOperator, LastRotationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LastRotationAttrOperator
    PLUG_CLS = LastRotationPlugOperator

    lastRotationX = DoubleField(default_value=0.0, writable=False)
    lrx = lastRotationX

    lastRotationY = DoubleField(default_value=0.0, writable=False)
    lry = lastRotationY

    lastRotationZ = DoubleField(default_value=0.0, writable=False)
    lrz = lastRotationZ


class InitialOrientationPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InitialOrientationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialOrientationX", "iox"),
        ("initialOrientationY", "ioy"),
        ("initialOrientationZ", "ioz"),
    )

    initialOrientationX = DoubleAngleField(default_value=0.0)
    iox = initialOrientationX

    initialOrientationY = DoubleAngleField(default_value=0.0)
    ioy = initialOrientationY

    initialOrientationZ = DoubleAngleField(default_value=0.0)
    ioz = initialOrientationZ


class InitialOrientationAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InitialOrientationPlugOperator]
):
    __slots__ = ()

    initialOrientationX = DoubleAngleField(default_value=0.0)
    iox = initialOrientationX

    initialOrientationY = DoubleAngleField(default_value=0.0)
    ioy = initialOrientationY

    initialOrientationZ = DoubleAngleField(default_value=0.0)
    ioz = initialOrientationZ


class InitialOrientationField(
    DoubleAngle3CompoundBaseField[InitialOrientationAttrOperator, InitialOrientationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitialOrientationAttrOperator
    PLUG_CLS = InitialOrientationPlugOperator

    initialOrientationX = DoubleAngleField(default_value=0.0)
    iox = initialOrientationX

    initialOrientationY = DoubleAngleField(default_value=0.0)
    ioy = initialOrientationY

    initialOrientationZ = DoubleAngleField(default_value=0.0)
    ioz = initialOrientationZ


class InitialVelocityPlugOperator(
    Double3CompoundBasePlugOperator["InitialVelocityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialVelocityX", "ivx"),
        ("initialVelocityY", "ivy"),
        ("initialVelocityZ", "ivz"),
    )

    initialVelocityX = DoubleField(default_value=0.0)
    ivx = initialVelocityX

    initialVelocityY = DoubleField(default_value=0.0)
    ivy = initialVelocityY

    initialVelocityZ = DoubleField(default_value=0.0)
    ivz = initialVelocityZ


class InitialVelocityAttrOperator(
    Double3CompoundBaseAttrOperator[InitialVelocityPlugOperator]
):
    __slots__ = ()

    initialVelocityX = DoubleField(default_value=0.0)
    ivx = initialVelocityX

    initialVelocityY = DoubleField(default_value=0.0)
    ivy = initialVelocityY

    initialVelocityZ = DoubleField(default_value=0.0)
    ivz = initialVelocityZ


class InitialVelocityField(
    Double3CompoundBaseField[InitialVelocityAttrOperator, InitialVelocityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitialVelocityAttrOperator
    PLUG_CLS = InitialVelocityPlugOperator

    initialVelocityX = DoubleField(default_value=0.0)
    ivx = initialVelocityX

    initialVelocityY = DoubleField(default_value=0.0)
    ivy = initialVelocityY

    initialVelocityZ = DoubleField(default_value=0.0)
    ivz = initialVelocityZ


class InitialSpinPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InitialSpinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialSpinX", "isx"),
        ("initialSpinY", "isy"),
        ("initialSpinZ", "isz"),
    )

    initialSpinX = DoubleAngleField(default_value=0.0)
    isx = initialSpinX

    initialSpinY = DoubleAngleField(default_value=0.0)
    isy = initialSpinY

    initialSpinZ = DoubleAngleField(default_value=0.0)
    isz = initialSpinZ


class InitialSpinAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InitialSpinPlugOperator]
):
    __slots__ = ()

    initialSpinX = DoubleAngleField(default_value=0.0)
    isx = initialSpinX

    initialSpinY = DoubleAngleField(default_value=0.0)
    isy = initialSpinY

    initialSpinZ = DoubleAngleField(default_value=0.0)
    isz = initialSpinZ


class InitialSpinField(
    DoubleAngle3CompoundBaseField[InitialSpinAttrOperator, InitialSpinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitialSpinAttrOperator
    PLUG_CLS = InitialSpinPlugOperator

    initialSpinX = DoubleAngleField(default_value=0.0)
    isx = initialSpinX

    initialSpinY = DoubleAngleField(default_value=0.0)
    isy = initialSpinY

    initialSpinZ = DoubleAngleField(default_value=0.0)
    isz = initialSpinZ


class CenterOfMassPlugOperator(
    Double3CompoundBasePlugOperator["CenterOfMassAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centerOfMassX", "cmx"),
        ("centerOfMassY", "cmy"),
        ("centerOfMassZ", "cmz"),
    )

    centerOfMassX = DoubleField(default_value=0.0)
    cmx = centerOfMassX

    centerOfMassY = DoubleField(default_value=0.0)
    cmy = centerOfMassY

    centerOfMassZ = DoubleField(default_value=0.0)
    cmz = centerOfMassZ


class CenterOfMassAttrOperator(
    Double3CompoundBaseAttrOperator[CenterOfMassPlugOperator]
):
    __slots__ = ()

    centerOfMassX = DoubleField(default_value=0.0)
    cmx = centerOfMassX

    centerOfMassY = DoubleField(default_value=0.0)
    cmy = centerOfMassY

    centerOfMassZ = DoubleField(default_value=0.0)
    cmz = centerOfMassZ


class CenterOfMassField(
    Double3CompoundBaseField[CenterOfMassAttrOperator, CenterOfMassPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CenterOfMassAttrOperator
    PLUG_CLS = CenterOfMassPlugOperator

    centerOfMassX = DoubleField(default_value=0.0)
    cmx = centerOfMassX

    centerOfMassY = DoubleField(default_value=0.0)
    cmy = centerOfMassY

    centerOfMassZ = DoubleField(default_value=0.0)
    cmz = centerOfMassZ


class ImpulsePlugOperator(
    Double3CompoundBasePlugOperator["ImpulseAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("impulseX", "imx"),
        ("impulseY", "imy"),
        ("impulseZ", "imz"),
    )

    impulseX = DoubleField(default_value=0.0)
    imx = impulseX

    impulseY = DoubleField(default_value=0.0)
    imy = impulseY

    impulseZ = DoubleField(default_value=0.0)
    imz = impulseZ


class ImpulseAttrOperator(
    Double3CompoundBaseAttrOperator[ImpulsePlugOperator]
):
    __slots__ = ()

    impulseX = DoubleField(default_value=0.0)
    imx = impulseX

    impulseY = DoubleField(default_value=0.0)
    imy = impulseY

    impulseZ = DoubleField(default_value=0.0)
    imz = impulseZ


class ImpulseField(
    Double3CompoundBaseField[ImpulseAttrOperator, ImpulsePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImpulseAttrOperator
    PLUG_CLS = ImpulsePlugOperator

    impulseX = DoubleField(default_value=0.0)
    imx = impulseX

    impulseY = DoubleField(default_value=0.0)
    imy = impulseY

    impulseZ = DoubleField(default_value=0.0)
    imz = impulseZ


class ImpulsePositionPlugOperator(
    Double3CompoundBasePlugOperator["ImpulsePositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("impulsePositionX", "pix"),
        ("impulsePositionY", "piy"),
        ("impulsePositionZ", "piz"),
    )

    impulsePositionX = DoubleField(default_value=0.0)
    pix = impulsePositionX

    impulsePositionY = DoubleField(default_value=0.0)
    piy = impulsePositionY

    impulsePositionZ = DoubleField(default_value=0.0)
    piz = impulsePositionZ


class ImpulsePositionAttrOperator(
    Double3CompoundBaseAttrOperator[ImpulsePositionPlugOperator]
):
    __slots__ = ()

    impulsePositionX = DoubleField(default_value=0.0)
    pix = impulsePositionX

    impulsePositionY = DoubleField(default_value=0.0)
    piy = impulsePositionY

    impulsePositionZ = DoubleField(default_value=0.0)
    piz = impulsePositionZ


class ImpulsePositionField(
    Double3CompoundBaseField[ImpulsePositionAttrOperator, ImpulsePositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImpulsePositionAttrOperator
    PLUG_CLS = ImpulsePositionPlugOperator

    impulsePositionX = DoubleField(default_value=0.0)
    pix = impulsePositionX

    impulsePositionY = DoubleField(default_value=0.0)
    piy = impulsePositionY

    impulsePositionZ = DoubleField(default_value=0.0)
    piz = impulsePositionZ


class SpinImpulsePlugOperator(
    Double3CompoundBasePlugOperator["SpinImpulseAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("spinImpulseX", "six"),
        ("spinImpulseY", "siy"),
        ("spinImpulseZ", "siz"),
    )

    spinImpulseX = DoubleField(default_value=0.0)
    six = spinImpulseX

    spinImpulseY = DoubleField(default_value=0.0)
    siy = spinImpulseY

    spinImpulseZ = DoubleField(default_value=0.0)
    siz = spinImpulseZ


class SpinImpulseAttrOperator(
    Double3CompoundBaseAttrOperator[SpinImpulsePlugOperator]
):
    __slots__ = ()

    spinImpulseX = DoubleField(default_value=0.0)
    six = spinImpulseX

    spinImpulseY = DoubleField(default_value=0.0)
    siy = spinImpulseY

    spinImpulseZ = DoubleField(default_value=0.0)
    siz = spinImpulseZ


class SpinImpulseField(
    Double3CompoundBaseField[SpinImpulseAttrOperator, SpinImpulsePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpinImpulseAttrOperator
    PLUG_CLS = SpinImpulsePlugOperator

    spinImpulseX = DoubleField(default_value=0.0)
    six = spinImpulseX

    spinImpulseY = DoubleField(default_value=0.0)
    siy = spinImpulseY

    spinImpulseZ = DoubleField(default_value=0.0)
    siz = spinImpulseZ


class VelocityPlugOperator(
    Double3CompoundBasePlugOperator["VelocityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("velocityX", "vx"),
        ("velocityY", "vy"),
        ("velocityZ", "vz"),
    )

    velocityX = DoubleField(default_value=0.0, writable=False)
    vx = velocityX

    velocityY = DoubleField(default_value=0.0, writable=False)
    vy = velocityY

    velocityZ = DoubleField(default_value=0.0, writable=False)
    vz = velocityZ


class VelocityAttrOperator(
    Double3CompoundBaseAttrOperator[VelocityPlugOperator]
):
    __slots__ = ()

    velocityX = DoubleField(default_value=0.0, writable=False)
    vx = velocityX

    velocityY = DoubleField(default_value=0.0, writable=False)
    vy = velocityY

    velocityZ = DoubleField(default_value=0.0, writable=False)
    vz = velocityZ


class VelocityField(
    Double3CompoundBaseField[VelocityAttrOperator, VelocityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VelocityAttrOperator
    PLUG_CLS = VelocityPlugOperator

    velocityX = DoubleField(default_value=0.0, writable=False)
    vx = velocityX

    velocityY = DoubleField(default_value=0.0, writable=False)
    vy = velocityY

    velocityZ = DoubleField(default_value=0.0, writable=False)
    vz = velocityZ


class SpinPlugOperator(
    Double3CompoundBasePlugOperator["SpinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("spinX", "spx"),
        ("spinY", "spy"),
        ("spinZ", "spz"),
    )

    spinX = DoubleField(default_value=0.0, writable=False)
    spx = spinX

    spinY = DoubleField(default_value=0.0, writable=False)
    spy = spinY

    spinZ = DoubleField(default_value=0.0, writable=False)
    spz = spinZ


class SpinAttrOperator(
    Double3CompoundBaseAttrOperator[SpinPlugOperator]
):
    __slots__ = ()

    spinX = DoubleField(default_value=0.0, writable=False)
    spx = spinX

    spinY = DoubleField(default_value=0.0, writable=False)
    spy = spinY

    spinZ = DoubleField(default_value=0.0, writable=False)
    spz = spinZ


class SpinField(
    Double3CompoundBaseField[SpinAttrOperator, SpinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpinAttrOperator
    PLUG_CLS = SpinPlugOperator

    spinX = DoubleField(default_value=0.0, writable=False)
    spx = spinX

    spinY = DoubleField(default_value=0.0, writable=False)
    spy = spinY

    spinZ = DoubleField(default_value=0.0, writable=False)
    spz = spinZ


class ContactPositionPlugOperator(
    Double3CompoundBasePlugOperator["ContactPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("contactX", "cnx"),
        ("contactY", "cny"),
        ("contactZ", "cnz"),
    )

    contactX = DoubleField(default_value=0.0)
    cnx = contactX

    contactY = DoubleField(default_value=0.0)
    cny = contactY

    contactZ = DoubleField(default_value=0.0)
    cnz = contactZ


class ContactPositionAttrOperator(
    Double3CompoundBaseAttrOperator[ContactPositionPlugOperator]
):
    __slots__ = ()

    contactX = DoubleField(default_value=0.0)
    cnx = contactX

    contactY = DoubleField(default_value=0.0)
    cny = contactY

    contactZ = DoubleField(default_value=0.0)
    cnz = contactZ


class ContactPositionField(
    Double3CompoundBaseField[ContactPositionAttrOperator, ContactPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ContactPositionAttrOperator
    PLUG_CLS = ContactPositionPlugOperator


class ForcePlugOperator(
    Double3CompoundBasePlugOperator["ForceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("forceX", "fx"),
        ("forceY", "fy"),
        ("forceZ", "fz"),
    )

    forceX = DoubleField(default_value=0.0, writable=False)
    fx = forceX

    forceY = DoubleField(default_value=0.0, writable=False)
    fy = forceY

    forceZ = DoubleField(default_value=0.0, writable=False)
    fz = forceZ


class ForceAttrOperator(
    Double3CompoundBaseAttrOperator[ForcePlugOperator]
):
    __slots__ = ()

    forceX = DoubleField(default_value=0.0, writable=False)
    fx = forceX

    forceY = DoubleField(default_value=0.0, writable=False)
    fy = forceY

    forceZ = DoubleField(default_value=0.0, writable=False)
    fz = forceZ


class ForceField(
    Double3CompoundBaseField[ForceAttrOperator, ForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForceAttrOperator
    PLUG_CLS = ForcePlugOperator

    forceX = DoubleField(default_value=0.0, writable=False)
    fx = forceX

    forceY = DoubleField(default_value=0.0, writable=False)
    fy = forceY

    forceZ = DoubleField(default_value=0.0, writable=False)
    fz = forceZ


class TorquePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["TorqueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("torqueX", "trx"),
        ("torqueY", "try"),
        ("torqueZ", "trz"),
    )

    torqueX = DoubleAngleField(default_value=0.0, writable=False)
    trx = torqueX

    torqueY = DoubleAngleField(default_value=0.0, writable=False)
    try_ = torqueY

    torqueZ = DoubleAngleField(default_value=0.0, writable=False)
    trz = torqueZ


class TorqueAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[TorquePlugOperator]
):
    __slots__ = ()

    torqueX = DoubleAngleField(default_value=0.0, writable=False)
    trx = torqueX

    torqueY = DoubleAngleField(default_value=0.0, writable=False)
    try_ = torqueY

    torqueZ = DoubleAngleField(default_value=0.0, writable=False)
    trz = torqueZ


class TorqueField(
    DoubleAngle3CompoundBaseField[TorqueAttrOperator, TorquePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TorqueAttrOperator
    PLUG_CLS = TorquePlugOperator

    torqueX = DoubleAngleField(default_value=0.0, writable=False)
    trx = torqueX

    torqueY = DoubleAngleField(default_value=0.0, writable=False)
    try_ = torqueY

    torqueZ = DoubleAngleField(default_value=0.0, writable=False)
    trz = torqueZ


class FieldDataPlugOperator(
    CompoundPlugOperator["FieldDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldDataPosition", "fdp"),
        ("fieldDataVelocity", "fdv"),
        ("fieldDataMass", "fdm"),
        ("deltaTime", "dt"),
    )

    fieldDataPosition = DataVectorArrayField()
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField()
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField()
    fdm = fieldDataMass

    deltaTime = TimeField(default_value=0.0)
    dt = deltaTime


class FieldDataAttrOperator(
    CompoundAttrOperator[FieldDataPlugOperator]
):
    __slots__ = ()

    fieldDataPosition = DataVectorArrayField()
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField()
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField()
    fdm = fieldDataMass

    deltaTime = TimeField(default_value=0.0)
    dt = deltaTime


class FieldDataField(
    CompoundField[FieldDataAttrOperator, FieldDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldDataAttrOperator
    PLUG_CLS = FieldDataPlugOperator

    fieldDataPosition = DataVectorArrayField()
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField()
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField()
    fdm = fieldDataMass

    deltaTime = TimeField(default_value=0.0)
    dt = deltaTime


class GeneralForcePlugOperator(
    CompoundPlugOperator["GeneralForceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputForce", "ofr"),
        ("outputTorque", "otr"),
    )

    outputForce = DataVectorArrayField()
    ofr = outputForce

    outputTorque = DataVectorArrayField()
    otr = outputTorque


class GeneralForceAttrOperator(
    CompoundAttrOperator[GeneralForcePlugOperator]
):
    __slots__ = ()

    outputForce = DataVectorArrayField()
    ofr = outputForce

    outputTorque = DataVectorArrayField()
    otr = outputTorque


class GeneralForceField(
    CompoundField[GeneralForceAttrOperator, GeneralForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GeneralForceAttrOperator
    PLUG_CLS = GeneralForcePlugOperator

    outputForce = DataVectorArrayField()
    ofr = outputForce

    outputTorque = DataVectorArrayField()
    otr = outputTorque
