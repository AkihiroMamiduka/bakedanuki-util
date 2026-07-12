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
from ..std.dt.string_array import DataStringArrayField
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


class FieldScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class FieldScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class FieldScale_InterpEnumField(
    EnumField[FieldScale_InterpEnumAttrOperator, FieldScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldScale_InterpEnumAttrOperator
    PLUG_CLS = FieldScale_InterpEnumPlugOperator


class PointFieldDropoff_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class PointFieldDropoff_InterpEnumAttrOperator(EnumAttrOperator):
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


class PointFieldDropoff_InterpEnumField(
    EnumField[PointFieldDropoff_InterpEnumAttrOperator, PointFieldDropoff_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointFieldDropoff_InterpEnumAttrOperator
    PLUG_CLS = PointFieldDropoff_InterpEnumPlugOperator


class ViscosityScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ViscosityScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class ViscosityScale_InterpEnumField(
    EnumField[ViscosityScale_InterpEnumAttrOperator, ViscosityScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViscosityScale_InterpEnumAttrOperator
    PLUG_CLS = ViscosityScale_InterpEnumPlugOperator


class SurfaceTensionScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class SurfaceTensionScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class SurfaceTensionScale_InterpEnumField(
    EnumField[SurfaceTensionScale_InterpEnumAttrOperator, SurfaceTensionScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SurfaceTensionScale_InterpEnumAttrOperator
    PLUG_CLS = SurfaceTensionScale_InterpEnumPlugOperator


class RadiusScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class RadiusScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class RadiusScale_InterpEnumField(
    EnumField[RadiusScale_InterpEnumAttrOperator, RadiusScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RadiusScale_InterpEnumAttrOperator
    PLUG_CLS = RadiusScale_InterpEnumPlugOperator


class MassScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class MassScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class MassScale_InterpEnumField(
    EnumField[MassScale_InterpEnumAttrOperator, MassScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MassScale_InterpEnumAttrOperator
    PLUG_CLS = MassScale_InterpEnumPlugOperator


class PointFieldScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class PointFieldScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class PointFieldScale_InterpEnumField(
    EnumField[PointFieldScale_InterpEnumAttrOperator, PointFieldScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointFieldScale_InterpEnumAttrOperator
    PLUG_CLS = PointFieldScale_InterpEnumPlugOperator


class FrictionScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class FrictionScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class FrictionScale_InterpEnumField(
    EnumField[FrictionScale_InterpEnumAttrOperator, FrictionScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrictionScale_InterpEnumAttrOperator
    PLUG_CLS = FrictionScale_InterpEnumPlugOperator


class StickinessScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class StickinessScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class StickinessScale_InterpEnumField(
    EnumField[StickinessScale_InterpEnumAttrOperator, StickinessScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickinessScale_InterpEnumAttrOperator
    PLUG_CLS = StickinessScale_InterpEnumPlugOperator


class CollideStrengthScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CollideStrengthScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class CollideStrengthScale_InterpEnumField(
    EnumField[CollideStrengthScale_InterpEnumAttrOperator, CollideStrengthScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollideStrengthScale_InterpEnumAttrOperator
    PLUG_CLS = CollideStrengthScale_InterpEnumPlugOperator


class BounceScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class BounceScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class BounceScale_InterpEnumField(
    EnumField[BounceScale_InterpEnumAttrOperator, BounceScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BounceScale_InterpEnumAttrOperator
    PLUG_CLS = BounceScale_InterpEnumPlugOperator


class OpacityScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class OpacityScale_InterpEnumAttrOperator(EnumAttrOperator):
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


class OpacityScale_InterpEnumField(
    EnumField[OpacityScale_InterpEnumAttrOperator, OpacityScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityScale_InterpEnumAttrOperator
    PLUG_CLS = OpacityScale_InterpEnumPlugOperator


class Color_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Color_InterpEnumAttrOperator(EnumAttrOperator):
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


class Color_InterpEnumField(
    EnumField[Color_InterpEnumAttrOperator, Color_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Color_InterpEnumAttrOperator
    PLUG_CLS = Color_InterpEnumPlugOperator


class Incandescence_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Incandescence_InterpEnumAttrOperator(EnumAttrOperator):
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


class Incandescence_InterpEnumField(
    EnumField[Incandescence_InterpEnumAttrOperator, Incandescence_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Incandescence_InterpEnumAttrOperator
    PLUG_CLS = Incandescence_InterpEnumPlugOperator


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


class CentroidPlugOperator(
    Double3CompoundBasePlugOperator["CentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centroidX", "ctdx"),
        ("centroidY", "ctdy"),
        ("centroidZ", "ctdz"),
    )

    centroidX = DoubleField(default_value=0.0, writable=False)
    ctdx = centroidX

    centroidY = DoubleField(default_value=0.0, writable=False)
    ctdy = centroidY

    centroidZ = DoubleField(default_value=0.0, writable=False)
    ctdz = centroidZ


class CentroidAttrOperator(
    Double3CompoundBaseAttrOperator[CentroidPlugOperator]
):
    __slots__ = ()

    centroidX = DoubleField(default_value=0.0, writable=False)
    ctdx = centroidX

    centroidY = DoubleField(default_value=0.0, writable=False)
    ctdy = centroidY

    centroidZ = DoubleField(default_value=0.0, writable=False)
    ctdz = centroidZ


class CentroidField(
    Double3CompoundBaseField[CentroidAttrOperator, CentroidPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CentroidAttrOperator
    PLUG_CLS = CentroidPlugOperator

    centroidX = DoubleField(default_value=0.0, writable=False)
    ctdx = centroidX

    centroidY = DoubleField(default_value=0.0, writable=False)
    ctdy = centroidY

    centroidZ = DoubleField(default_value=0.0, writable=False)
    ctdz = centroidZ


class WorldCentroidPlugOperator(
    Double3CompoundBasePlugOperator["WorldCentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldCentroidX", "wctx"),
        ("worldCentroidY", "wcty"),
        ("worldCentroidZ", "wctz"),
    )

    worldCentroidX = DoubleField(default_value=0.0, writable=False)
    wctx = worldCentroidX

    worldCentroidY = DoubleField(default_value=0.0, writable=False)
    wcty = worldCentroidY

    worldCentroidZ = DoubleField(default_value=0.0, writable=False)
    wctz = worldCentroidZ


class WorldCentroidAttrOperator(
    Double3CompoundBaseAttrOperator[WorldCentroidPlugOperator]
):
    __slots__ = ()

    worldCentroidX = DoubleField(default_value=0.0, writable=False)
    wctx = worldCentroidX

    worldCentroidY = DoubleField(default_value=0.0, writable=False)
    wcty = worldCentroidY

    worldCentroidZ = DoubleField(default_value=0.0, writable=False)
    wctz = worldCentroidZ


class WorldCentroidField(
    Double3CompoundBaseField[WorldCentroidAttrOperator, WorldCentroidPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WorldCentroidAttrOperator
    PLUG_CLS = WorldCentroidPlugOperator

    worldCentroidX = DoubleField(default_value=0.0, writable=False)
    wctx = worldCentroidX

    worldCentroidY = DoubleField(default_value=0.0, writable=False)
    wcty = worldCentroidY

    worldCentroidZ = DoubleField(default_value=0.0, writable=False)
    wctz = worldCentroidZ


class CachedWorldCentroidPlugOperator(
    Double3CompoundBasePlugOperator["CachedWorldCentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cachedWorldCentroidX", "cwcx"),
        ("cachedWorldCentroidY", "cwcy"),
        ("cachedWorldCentroidZ", "cwcz"),
    )

    cachedWorldCentroidX = DoubleField(default_value=0.0, writable=False)
    cwcx = cachedWorldCentroidX

    cachedWorldCentroidY = DoubleField(default_value=0.0, writable=False)
    cwcy = cachedWorldCentroidY

    cachedWorldCentroidZ = DoubleField(default_value=0.0, writable=False)
    cwcz = cachedWorldCentroidZ


class CachedWorldCentroidAttrOperator(
    Double3CompoundBaseAttrOperator[CachedWorldCentroidPlugOperator]
):
    __slots__ = ()

    cachedWorldCentroidX = DoubleField(default_value=0.0, writable=False)
    cwcx = cachedWorldCentroidX

    cachedWorldCentroidY = DoubleField(default_value=0.0, writable=False)
    cwcy = cachedWorldCentroidY

    cachedWorldCentroidZ = DoubleField(default_value=0.0, writable=False)
    cwcz = cachedWorldCentroidZ


class CachedWorldCentroidField(
    Double3CompoundBaseField[CachedWorldCentroidAttrOperator, CachedWorldCentroidPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CachedWorldCentroidAttrOperator
    PLUG_CLS = CachedWorldCentroidPlugOperator

    cachedWorldCentroidX = DoubleField(default_value=0.0, writable=False)
    cwcx = cachedWorldCentroidX

    cachedWorldCentroidY = DoubleField(default_value=0.0, writable=False)
    cwcy = cachedWorldCentroidY

    cachedWorldCentroidZ = DoubleField(default_value=0.0, writable=False)
    cwcz = cachedWorldCentroidZ


class IdMappingPlugOperator(
    CompoundPlugOperator["IdMappingAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sortedId", "sid"),
        ("idIndex", "idix"),
    )

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class IdMappingAttrOperator(
    CompoundAttrOperator[IdMappingPlugOperator]
):
    __slots__ = ()

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class IdMappingField(
    CompoundField[IdMappingAttrOperator, IdMappingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdMappingAttrOperator
    PLUG_CLS = IdMappingPlugOperator

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class RandStatePlugOperator(
    Long3CompoundBasePlugOperator["RandStateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("randStateX", "rstx"),
        ("randStateY", "rsty"),
        ("randStateZ", "rstz"),
    )

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


class RandStateAttrOperator(
    Long3CompoundBaseAttrOperator[RandStatePlugOperator]
):
    __slots__ = ()

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


class RandStateField(
    Long3CompoundBaseField[RandStateAttrOperator, RandStatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RandStateAttrOperator
    PLUG_CLS = RandStatePlugOperator

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


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


class EmitterDataPlugOperator(
    CompoundPlugOperator["EmitterDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emitterDataPosition", "edp"),
        ("emitterDataVelocity", "edv"),
        ("emitterDataDeltaTime", "edt"),
    )

    emitterDataPosition = DataVectorArrayField(writable=False)
    edp = emitterDataPosition

    emitterDataVelocity = DataVectorArrayField(writable=False)
    edv = emitterDataVelocity

    emitterDataDeltaTime = TimeField(default_value=0.0, writable=False)
    edt = emitterDataDeltaTime


class EmitterDataAttrOperator(
    CompoundAttrOperator[EmitterDataPlugOperator]
):
    __slots__ = ()

    emitterDataPosition = DataVectorArrayField(writable=False)
    edp = emitterDataPosition

    emitterDataVelocity = DataVectorArrayField(writable=False)
    edv = emitterDataVelocity

    emitterDataDeltaTime = TimeField(default_value=0.0, writable=False)
    edt = emitterDataDeltaTime


class EmitterDataField(
    CompoundField[EmitterDataAttrOperator, EmitterDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmitterDataAttrOperator
    PLUG_CLS = EmitterDataPlugOperator

    emitterDataPosition = DataVectorArrayField(writable=False)
    edp = emitterDataPosition

    emitterDataVelocity = DataVectorArrayField(writable=False)
    edv = emitterDataVelocity

    emitterDataDeltaTime = TimeField(default_value=0.0, writable=False)
    edt = emitterDataDeltaTime


class CollisionDataPlugOperator(
    CompoundPlugOperator["CollisionDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionGeometry", "cge"),
        ("collisionResilience", "crs"),
        ("collisionFriction", "cfr"),
        ("collisionOffset", "cof"),
    )

    collisionGeometry = TypedField(multi=True)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0)
    cfr = collisionFriction

    collisionOffset = DoubleField(multi=True, default_value=0.01)
    cof = collisionOffset


class CollisionDataAttrOperator(
    CompoundAttrOperator[CollisionDataPlugOperator]
):
    __slots__ = ()

    collisionGeometry = TypedField(multi=True)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0)
    cfr = collisionFriction

    collisionOffset = DoubleField(multi=True, default_value=0.01)
    cof = collisionOffset


class CollisionDataField(
    CompoundField[CollisionDataAttrOperator, CollisionDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionDataAttrOperator
    PLUG_CLS = CollisionDataPlugOperator

    collisionGeometry = TypedField(multi=True)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0)
    cfr = collisionFriction

    collisionOffset = DoubleField(multi=True, default_value=0.01)
    cof = collisionOffset


class EventRandStatePlugOperator(
    Long3CompoundBasePlugOperator["EventRandStateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eventRandStateX", "ersx"),
        ("eventRandStateY", "ersy"),
        ("eventRandStateZ", "ersz"),
    )

    eventRandStateX = LongField(default_value=0)
    ersx = eventRandStateX

    eventRandStateY = LongField(default_value=0)
    ersy = eventRandStateY

    eventRandStateZ = LongField(default_value=0)
    ersz = eventRandStateZ


class EventRandStateAttrOperator(
    Long3CompoundBaseAttrOperator[EventRandStatePlugOperator]
):
    __slots__ = ()

    eventRandStateX = LongField(default_value=0)
    ersx = eventRandStateX

    eventRandStateY = LongField(default_value=0)
    ersy = eventRandStateY

    eventRandStateZ = LongField(default_value=0)
    ersz = eventRandStateZ


class EventRandStateField(
    Long3CompoundBaseField[EventRandStateAttrOperator, EventRandStatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EventRandStateAttrOperator
    PLUG_CLS = EventRandStatePlugOperator

    eventRandStateX = LongField(default_value=0)
    ersx = eventRandStateX

    eventRandStateY = LongField(default_value=0)
    ersy = eventRandStateY

    eventRandStateZ = LongField(default_value=0)
    ersz = eventRandStateZ


class InstanceDataPlugOperator(
    CompoundPlugOperator["InstanceDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("instanceAttributeMapping", "iam"),
        ("instancePointData", "ipd"),
    )

    instanceAttributeMapping = DataStringArrayField()
    iam = instanceAttributeMapping

    instancePointData = TypedField()
    ipd = instancePointData


class InstanceDataAttrOperator(
    CompoundAttrOperator[InstanceDataPlugOperator]
):
    __slots__ = ()

    instanceAttributeMapping = DataStringArrayField()
    iam = instanceAttributeMapping

    instancePointData = TypedField()
    ipd = instancePointData


class InstanceDataField(
    CompoundField[InstanceDataAttrOperator, InstanceDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InstanceDataAttrOperator
    PLUG_CLS = InstanceDataPlugOperator


class LocalForcePlugOperator(
    Float3CompoundBasePlugOperator["LocalForceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localForceX", "lfcx"),
        ("localForceY", "lfcy"),
        ("localForceZ", "lfcz"),
    )

    localForceX = FloatField(default_value=0.0)
    lfcx = localForceX

    localForceY = FloatField(default_value=0.0)
    lfcy = localForceY

    localForceZ = FloatField(default_value=0.0)
    lfcz = localForceZ


class LocalForceAttrOperator(
    Float3CompoundBaseAttrOperator[LocalForcePlugOperator]
):
    __slots__ = ()

    localForceX = FloatField(default_value=0.0)
    lfcx = localForceX

    localForceY = FloatField(default_value=0.0)
    lfcy = localForceY

    localForceZ = FloatField(default_value=0.0)
    lfcz = localForceZ


class LocalForceField(
    Float3CompoundBaseField[LocalForceAttrOperator, LocalForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalForceAttrOperator
    PLUG_CLS = LocalForcePlugOperator

    localForceX = FloatField(default_value=0.0)
    lfcx = localForceX

    localForceY = FloatField(default_value=0.0)
    lfcy = localForceY

    localForceZ = FloatField(default_value=0.0)
    lfcz = localForceZ


class LocalWindPlugOperator(
    Float3CompoundBasePlugOperator["LocalWindAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localWindX", "lwnx"),
        ("localWindY", "lwny"),
        ("localWindZ", "lwnz"),
    )

    localWindX = FloatField(default_value=0.0)
    lwnx = localWindX

    localWindY = FloatField(default_value=0.0)
    lwny = localWindY

    localWindZ = FloatField(default_value=0.0)
    lwnz = localWindZ


class LocalWindAttrOperator(
    Float3CompoundBaseAttrOperator[LocalWindPlugOperator]
):
    __slots__ = ()

    localWindX = FloatField(default_value=0.0)
    lwnx = localWindX

    localWindY = FloatField(default_value=0.0)
    lwny = localWindY

    localWindZ = FloatField(default_value=0.0)
    lwnz = localWindZ


class LocalWindField(
    Float3CompoundBaseField[LocalWindAttrOperator, LocalWindPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalWindAttrOperator
    PLUG_CLS = LocalWindPlugOperator

    localWindX = FloatField(default_value=0.0)
    lwnx = localWindX

    localWindY = FloatField(default_value=0.0)
    lwny = localWindY

    localWindZ = FloatField(default_value=0.0)
    lwnz = localWindZ


class FieldScalePlugOperator(
    CompoundPlugOperator["FieldScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldScale_Position", "fscp"),
        ("fieldScale_FloatValue", "fscfv"),
        ("fieldScale_Interp", "fsci"),
    )

    fieldScale_Position = FloatField(default_value=0.0)
    fscp = fieldScale_Position

    fieldScale_FloatValue = FloatField(default_value=0.0)
    fscfv = fieldScale_FloatValue

    fieldScale_Interp = FieldScale_InterpEnumField(default_value=0)
    fsci = fieldScale_Interp


class FieldScaleAttrOperator(
    CompoundAttrOperator[FieldScalePlugOperator]
):
    __slots__ = ()

    fieldScale_Position = FloatField(default_value=0.0)
    fscp = fieldScale_Position

    fieldScale_FloatValue = FloatField(default_value=0.0)
    fscfv = fieldScale_FloatValue

    fieldScale_Interp = FieldScale_InterpEnumField(default_value=0)
    fsci = fieldScale_Interp


class FieldScaleField(
    CompoundField[FieldScaleAttrOperator, FieldScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldScaleAttrOperator
    PLUG_CLS = FieldScalePlugOperator


class PointFieldDropoffPlugOperator(
    CompoundPlugOperator["PointFieldDropoffAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointFieldDropoff_Position", "pfdop"),
        ("pointFieldDropoff_FloatValue", "pfdofv"),
        ("pointFieldDropoff_Interp", "pfdoi"),
    )

    pointFieldDropoff_Position = FloatField(default_value=0.0)
    pfdop = pointFieldDropoff_Position

    pointFieldDropoff_FloatValue = FloatField(default_value=0.0)
    pfdofv = pointFieldDropoff_FloatValue

    pointFieldDropoff_Interp = PointFieldDropoff_InterpEnumField(default_value=0)
    pfdoi = pointFieldDropoff_Interp


class PointFieldDropoffAttrOperator(
    CompoundAttrOperator[PointFieldDropoffPlugOperator]
):
    __slots__ = ()

    pointFieldDropoff_Position = FloatField(default_value=0.0)
    pfdop = pointFieldDropoff_Position

    pointFieldDropoff_FloatValue = FloatField(default_value=0.0)
    pfdofv = pointFieldDropoff_FloatValue

    pointFieldDropoff_Interp = PointFieldDropoff_InterpEnumField(default_value=0)
    pfdoi = pointFieldDropoff_Interp


class PointFieldDropoffField(
    CompoundField[PointFieldDropoffAttrOperator, PointFieldDropoffPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointFieldDropoffAttrOperator
    PLUG_CLS = PointFieldDropoffPlugOperator


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


class ViscosityScalePlugOperator(
    CompoundPlugOperator["ViscosityScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("viscosityScale_Position", "vsscp"),
        ("viscosityScale_FloatValue", "vsscfv"),
        ("viscosityScale_Interp", "vssci"),
    )

    viscosityScale_Position = FloatField(default_value=0.0)
    vsscp = viscosityScale_Position

    viscosityScale_FloatValue = FloatField(default_value=0.0)
    vsscfv = viscosityScale_FloatValue

    viscosityScale_Interp = ViscosityScale_InterpEnumField(default_value=0)
    vssci = viscosityScale_Interp


class ViscosityScaleAttrOperator(
    CompoundAttrOperator[ViscosityScalePlugOperator]
):
    __slots__ = ()

    viscosityScale_Position = FloatField(default_value=0.0)
    vsscp = viscosityScale_Position

    viscosityScale_FloatValue = FloatField(default_value=0.0)
    vsscfv = viscosityScale_FloatValue

    viscosityScale_Interp = ViscosityScale_InterpEnumField(default_value=0)
    vssci = viscosityScale_Interp


class ViscosityScaleField(
    CompoundField[ViscosityScaleAttrOperator, ViscosityScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViscosityScaleAttrOperator
    PLUG_CLS = ViscosityScalePlugOperator


class SurfaceTensionScalePlugOperator(
    CompoundPlugOperator["SurfaceTensionScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("surfaceTensionScale_Position", "stnsp"),
        ("surfaceTensionScale_FloatValue", "stnsfv"),
        ("surfaceTensionScale_Interp", "stnsi"),
    )

    surfaceTensionScale_Position = FloatField(default_value=0.0)
    stnsp = surfaceTensionScale_Position

    surfaceTensionScale_FloatValue = FloatField(default_value=0.0)
    stnsfv = surfaceTensionScale_FloatValue

    surfaceTensionScale_Interp = SurfaceTensionScale_InterpEnumField(default_value=0)
    stnsi = surfaceTensionScale_Interp


class SurfaceTensionScaleAttrOperator(
    CompoundAttrOperator[SurfaceTensionScalePlugOperator]
):
    __slots__ = ()

    surfaceTensionScale_Position = FloatField(default_value=0.0)
    stnsp = surfaceTensionScale_Position

    surfaceTensionScale_FloatValue = FloatField(default_value=0.0)
    stnsfv = surfaceTensionScale_FloatValue

    surfaceTensionScale_Interp = SurfaceTensionScale_InterpEnumField(default_value=0)
    stnsi = surfaceTensionScale_Interp


class SurfaceTensionScaleField(
    CompoundField[SurfaceTensionScaleAttrOperator, SurfaceTensionScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SurfaceTensionScaleAttrOperator
    PLUG_CLS = SurfaceTensionScalePlugOperator


class RadiusScalePlugOperator(
    CompoundPlugOperator["RadiusScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("radiusScale_Position", "rdcp"),
        ("radiusScale_FloatValue", "rdcfv"),
        ("radiusScale_Interp", "rdci"),
    )

    radiusScale_Position = FloatField(default_value=0.0)
    rdcp = radiusScale_Position

    radiusScale_FloatValue = FloatField(default_value=0.0)
    rdcfv = radiusScale_FloatValue

    radiusScale_Interp = RadiusScale_InterpEnumField(default_value=0)
    rdci = radiusScale_Interp


class RadiusScaleAttrOperator(
    CompoundAttrOperator[RadiusScalePlugOperator]
):
    __slots__ = ()

    radiusScale_Position = FloatField(default_value=0.0)
    rdcp = radiusScale_Position

    radiusScale_FloatValue = FloatField(default_value=0.0)
    rdcfv = radiusScale_FloatValue

    radiusScale_Interp = RadiusScale_InterpEnumField(default_value=0)
    rdci = radiusScale_Interp


class RadiusScaleField(
    CompoundField[RadiusScaleAttrOperator, RadiusScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RadiusScaleAttrOperator
    PLUG_CLS = RadiusScalePlugOperator


class MassScalePlugOperator(
    CompoundPlugOperator["MassScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("massScale_Position", "msscp"),
        ("massScale_FloatValue", "msscfv"),
        ("massScale_Interp", "mssci"),
    )

    massScale_Position = FloatField(default_value=0.0)
    msscp = massScale_Position

    massScale_FloatValue = FloatField(default_value=0.0)
    msscfv = massScale_FloatValue

    massScale_Interp = MassScale_InterpEnumField(default_value=0)
    mssci = massScale_Interp


class MassScaleAttrOperator(
    CompoundAttrOperator[MassScalePlugOperator]
):
    __slots__ = ()

    massScale_Position = FloatField(default_value=0.0)
    msscp = massScale_Position

    massScale_FloatValue = FloatField(default_value=0.0)
    msscfv = massScale_FloatValue

    massScale_Interp = MassScale_InterpEnumField(default_value=0)
    mssci = massScale_Interp


class MassScaleField(
    CompoundField[MassScaleAttrOperator, MassScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MassScaleAttrOperator
    PLUG_CLS = MassScalePlugOperator


class PointFieldScalePlugOperator(
    CompoundPlugOperator["PointFieldScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointFieldScale_Position", "pfscp"),
        ("pointFieldScale_FloatValue", "pfscfv"),
        ("pointFieldScale_Interp", "pfsci"),
    )

    pointFieldScale_Position = FloatField(default_value=0.0)
    pfscp = pointFieldScale_Position

    pointFieldScale_FloatValue = FloatField(default_value=0.0)
    pfscfv = pointFieldScale_FloatValue

    pointFieldScale_Interp = PointFieldScale_InterpEnumField(default_value=0)
    pfsci = pointFieldScale_Interp


class PointFieldScaleAttrOperator(
    CompoundAttrOperator[PointFieldScalePlugOperator]
):
    __slots__ = ()

    pointFieldScale_Position = FloatField(default_value=0.0)
    pfscp = pointFieldScale_Position

    pointFieldScale_FloatValue = FloatField(default_value=0.0)
    pfscfv = pointFieldScale_FloatValue

    pointFieldScale_Interp = PointFieldScale_InterpEnumField(default_value=0)
    pfsci = pointFieldScale_Interp


class PointFieldScaleField(
    CompoundField[PointFieldScaleAttrOperator, PointFieldScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointFieldScaleAttrOperator
    PLUG_CLS = PointFieldScalePlugOperator


class FrictionScalePlugOperator(
    CompoundPlugOperator["FrictionScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("frictionScale_Position", "frscp"),
        ("frictionScale_FloatValue", "frscfv"),
        ("frictionScale_Interp", "frsci"),
    )

    frictionScale_Position = FloatField(default_value=0.0)
    frscp = frictionScale_Position

    frictionScale_FloatValue = FloatField(default_value=0.0)
    frscfv = frictionScale_FloatValue

    frictionScale_Interp = FrictionScale_InterpEnumField(default_value=0)
    frsci = frictionScale_Interp


class FrictionScaleAttrOperator(
    CompoundAttrOperator[FrictionScalePlugOperator]
):
    __slots__ = ()

    frictionScale_Position = FloatField(default_value=0.0)
    frscp = frictionScale_Position

    frictionScale_FloatValue = FloatField(default_value=0.0)
    frscfv = frictionScale_FloatValue

    frictionScale_Interp = FrictionScale_InterpEnumField(default_value=0)
    frsci = frictionScale_Interp


class FrictionScaleField(
    CompoundField[FrictionScaleAttrOperator, FrictionScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrictionScaleAttrOperator
    PLUG_CLS = FrictionScalePlugOperator


class StickinessScalePlugOperator(
    CompoundPlugOperator["StickinessScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("stickinessScale_Position", "stscp"),
        ("stickinessScale_FloatValue", "stscfv"),
        ("stickinessScale_Interp", "stsci"),
    )

    stickinessScale_Position = FloatField(default_value=0.0)
    stscp = stickinessScale_Position

    stickinessScale_FloatValue = FloatField(default_value=0.0)
    stscfv = stickinessScale_FloatValue

    stickinessScale_Interp = StickinessScale_InterpEnumField(default_value=0)
    stsci = stickinessScale_Interp


class StickinessScaleAttrOperator(
    CompoundAttrOperator[StickinessScalePlugOperator]
):
    __slots__ = ()

    stickinessScale_Position = FloatField(default_value=0.0)
    stscp = stickinessScale_Position

    stickinessScale_FloatValue = FloatField(default_value=0.0)
    stscfv = stickinessScale_FloatValue

    stickinessScale_Interp = StickinessScale_InterpEnumField(default_value=0)
    stsci = stickinessScale_Interp


class StickinessScaleField(
    CompoundField[StickinessScaleAttrOperator, StickinessScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickinessScaleAttrOperator
    PLUG_CLS = StickinessScalePlugOperator


class CollideStrengthScalePlugOperator(
    CompoundPlugOperator["CollideStrengthScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collideStrengthScale_Position", "clscp"),
        ("collideStrengthScale_FloatValue", "clscfv"),
        ("collideStrengthScale_Interp", "clsci"),
    )

    collideStrengthScale_Position = FloatField(default_value=0.0)
    clscp = collideStrengthScale_Position

    collideStrengthScale_FloatValue = FloatField(default_value=0.0)
    clscfv = collideStrengthScale_FloatValue

    collideStrengthScale_Interp = CollideStrengthScale_InterpEnumField(default_value=0)
    clsci = collideStrengthScale_Interp


class CollideStrengthScaleAttrOperator(
    CompoundAttrOperator[CollideStrengthScalePlugOperator]
):
    __slots__ = ()

    collideStrengthScale_Position = FloatField(default_value=0.0)
    clscp = collideStrengthScale_Position

    collideStrengthScale_FloatValue = FloatField(default_value=0.0)
    clscfv = collideStrengthScale_FloatValue

    collideStrengthScale_Interp = CollideStrengthScale_InterpEnumField(default_value=0)
    clsci = collideStrengthScale_Interp


class CollideStrengthScaleField(
    CompoundField[CollideStrengthScaleAttrOperator, CollideStrengthScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollideStrengthScaleAttrOperator
    PLUG_CLS = CollideStrengthScalePlugOperator


class BounceScalePlugOperator(
    CompoundPlugOperator["BounceScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bounceScale_Position", "boscp"),
        ("bounceScale_FloatValue", "boscfv"),
        ("bounceScale_Interp", "bosci"),
    )

    bounceScale_Position = FloatField(default_value=0.0)
    boscp = bounceScale_Position

    bounceScale_FloatValue = FloatField(default_value=0.0)
    boscfv = bounceScale_FloatValue

    bounceScale_Interp = BounceScale_InterpEnumField(default_value=0)
    bosci = bounceScale_Interp


class BounceScaleAttrOperator(
    CompoundAttrOperator[BounceScalePlugOperator]
):
    __slots__ = ()

    bounceScale_Position = FloatField(default_value=0.0)
    boscp = bounceScale_Position

    bounceScale_FloatValue = FloatField(default_value=0.0)
    boscfv = bounceScale_FloatValue

    bounceScale_Interp = BounceScale_InterpEnumField(default_value=0)
    bosci = bounceScale_Interp


class BounceScaleField(
    CompoundField[BounceScaleAttrOperator, BounceScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BounceScaleAttrOperator
    PLUG_CLS = BounceScalePlugOperator


class OpacityScalePlugOperator(
    CompoundPlugOperator["OpacityScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("opacityScale_Position", "opcp"),
        ("opacityScale_FloatValue", "opcfv"),
        ("opacityScale_Interp", "opci"),
    )

    opacityScale_Position = FloatField(default_value=0.0)
    opcp = opacityScale_Position

    opacityScale_FloatValue = FloatField(default_value=0.0)
    opcfv = opacityScale_FloatValue

    opacityScale_Interp = OpacityScale_InterpEnumField(default_value=0)
    opci = opacityScale_Interp


class OpacityScaleAttrOperator(
    CompoundAttrOperator[OpacityScalePlugOperator]
):
    __slots__ = ()

    opacityScale_Position = FloatField(default_value=0.0)
    opcp = opacityScale_Position

    opacityScale_FloatValue = FloatField(default_value=0.0)
    opcfv = opacityScale_FloatValue

    opacityScale_Interp = OpacityScale_InterpEnumField(default_value=0)
    opci = opacityScale_Interp


class OpacityScaleField(
    CompoundField[OpacityScaleAttrOperator, OpacityScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityScaleAttrOperator
    PLUG_CLS = OpacityScalePlugOperator


class ColorPlugOperator(
    CompoundPlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color_Position", "clp"),
        ("color_Color", "clc"),
        ("color_Interp", "cli"),
    )

    color_Position = FloatField(default_value=0.0)
    clp = color_Position

    color_Color = Float3Field(default_value=(0.0, 0.0, 0.0))
    clc = color_Color

    color_Interp = Color_InterpEnumField(default_value=0)
    cli = color_Interp


class ColorAttrOperator(
    CompoundAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    color_Position = FloatField(default_value=0.0)
    clp = color_Position

    color_Color = Float3Field(default_value=(0.0, 0.0, 0.0))
    clc = color_Color

    color_Interp = Color_InterpEnumField(default_value=0)
    cli = color_Interp


class ColorField(
    CompoundField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator


class IncandescencePlugOperator(
    CompoundPlugOperator["IncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescence_Position", "incap"),
        ("incandescence_Color", "incac"),
        ("incandescence_Interp", "incai"),
    )

    incandescence_Position = FloatField(default_value=0.0)
    incap = incandescence_Position

    incandescence_Color = Float3Field(default_value=(0.0, 0.0, 0.0))
    incac = incandescence_Color

    incandescence_Interp = Incandescence_InterpEnumField(default_value=0)
    incai = incandescence_Interp


class IncandescenceAttrOperator(
    CompoundAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescence_Position = FloatField(default_value=0.0)
    incap = incandescence_Position

    incandescence_Color = Float3Field(default_value=(0.0, 0.0, 0.0))
    incac = incandescence_Color

    incandescence_Interp = Incandescence_InterpEnumField(default_value=0)
    incai = incandescence_Interp


class IncandescenceField(
    CompoundField[IncandescenceAttrOperator, IncandescencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator
