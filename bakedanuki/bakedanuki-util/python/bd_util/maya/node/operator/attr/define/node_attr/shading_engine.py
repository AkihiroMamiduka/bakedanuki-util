# coding: utf-8

from ..std.at.addr import AddrField
from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import (
    Float3Field,
)


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


class ChannelSetColorPlugOperator(
    Float3CompoundBasePlugOperator["ChannelSetColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("channelSetColorR", "cscolr"),
        ("channelSetColorG", "cscolg"),
        ("channelSetColorB", "cscolb"),
    )

    channelSetColorR = FloatField(default_value=0.5)
    cscolr = channelSetColorR

    channelSetColorG = FloatField(default_value=0.5)
    cscolg = channelSetColorG

    channelSetColorB = FloatField(default_value=0.5)
    cscolb = channelSetColorB


class ChannelSetColorAttrOperator(
    Float3CompoundBaseAttrOperator[ChannelSetColorPlugOperator]
):
    __slots__ = ()

    channelSetColorR = FloatField(default_value=0.5)
    cscolr = channelSetColorR

    channelSetColorG = FloatField(default_value=0.5)
    cscolg = channelSetColorG

    channelSetColorB = FloatField(default_value=0.5)
    cscolb = channelSetColorB


class ChannelSetColorField(
    Float3CompoundBaseField[
        ChannelSetColorAttrOperator, ChannelSetColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ChannelSetColorAttrOperator
    PLUG_CLS = ChannelSetColorPlugOperator

    channelSetColorR = FloatField(default_value=0.5)
    cscolr = channelSetColorR

    channelSetColorG = FloatField(default_value=0.5)
    cscolg = channelSetColorG

    channelSetColorB = FloatField(default_value=0.5)
    cscolb = channelSetColorB


class DefaultShadowsPlugOperator(
    LightDataPlugOperator["DefaultShadowsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dShadowDirection", "dsd"),
        ("dShadowIntensity", "dsi"),
        ("dShadowAmbient", "dsa"),
        ("dShadowDiffuse", "dsf"),
        ("dShadowSpecular", "dss"),
        ("dShadowShadowFraction", "dssf"),
        ("dShadowPreShadowIntensity", "dsps"),
        ("dShadowBlindData", "dbld"),
    )

    dShadowDirection = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    dsd = dShadowDirection

    dShadowIntensity = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    dsi = dShadowIntensity

    dShadowAmbient = BoolField(default_value=False, readable=False)
    dsa = dShadowAmbient

    dShadowDiffuse = BoolField(default_value=False, readable=False)
    dsf = dShadowDiffuse

    dShadowSpecular = BoolField(default_value=False, readable=False)
    dss = dShadowSpecular

    dShadowShadowFraction = FloatField(default_value=0.0, readable=False)
    dssf = dShadowShadowFraction

    dShadowPreShadowIntensity = FloatField(default_value=0.0, readable=False)
    dsps = dShadowPreShadowIntensity

    dShadowBlindData = AddrField(default_value=0.0, readable=False)
    dbld = dShadowBlindData


class DefaultShadowsAttrOperator(
    LightDataAttrOperator[DefaultShadowsPlugOperator]
):
    __slots__ = ()

    dShadowDirection = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    dsd = dShadowDirection

    dShadowIntensity = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    dsi = dShadowIntensity

    dShadowAmbient = BoolField(default_value=False, readable=False)
    dsa = dShadowAmbient

    dShadowDiffuse = BoolField(default_value=False, readable=False)
    dsf = dShadowDiffuse

    dShadowSpecular = BoolField(default_value=False, readable=False)
    dss = dShadowSpecular

    dShadowShadowFraction = FloatField(default_value=0.0, readable=False)
    dssf = dShadowShadowFraction

    dShadowPreShadowIntensity = FloatField(default_value=0.0, readable=False)
    dsps = dShadowPreShadowIntensity

    dShadowBlindData = AddrField(default_value=0.0, readable=False)
    dbld = dShadowBlindData


class DefaultShadowsField(
    LightDataField[DefaultShadowsAttrOperator, DefaultShadowsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultShadowsAttrOperator
    PLUG_CLS = DefaultShadowsPlugOperator

    dShadowDirection = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    dsd = dShadowDirection

    dShadowIntensity = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    dsi = dShadowIntensity

    dShadowAmbient = BoolField(default_value=False, readable=False)
    dsa = dShadowAmbient

    dShadowDiffuse = BoolField(default_value=False, readable=False)
    dsf = dShadowDiffuse

    dShadowSpecular = BoolField(default_value=False, readable=False)
    dss = dShadowSpecular

    dShadowShadowFraction = FloatField(default_value=0.0, readable=False)
    dssf = dShadowShadowFraction

    dShadowPreShadowIntensity = FloatField(default_value=0.0, readable=False)
    dsps = dShadowPreShadowIntensity

    dShadowBlindData = AddrField(default_value=0.0, readable=False)
    dbld = dShadowBlindData


class LinkedShadowsPlugOperator(
    LightDataPlugOperator["LinkedShadowsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lShadowDirection", "lsd"),
        ("lShadowIntensity", "lsi"),
        ("lShadowAmbient", "lsa"),
        ("lShadowDiffuse", "lsf"),
        ("lShadowSpecular", "lss"),
        ("lShadowShadowFraction", "lssf"),
        ("lShadowPreShadowIntensity", "lsps"),
        ("lShadowBlindData", "lbld"),
    )

    lShadowDirection = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    lsd = lShadowDirection

    lShadowIntensity = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    lsi = lShadowIntensity

    lShadowAmbient = BoolField(default_value=False, readable=False)
    lsa = lShadowAmbient

    lShadowDiffuse = BoolField(default_value=False, readable=False)
    lsf = lShadowDiffuse

    lShadowSpecular = BoolField(default_value=False, readable=False)
    lss = lShadowSpecular

    lShadowShadowFraction = FloatField(default_value=0.0, readable=False)
    lssf = lShadowShadowFraction

    lShadowPreShadowIntensity = FloatField(default_value=0.0, readable=False)
    lsps = lShadowPreShadowIntensity

    lShadowBlindData = AddrField(default_value=0.0, readable=False)
    lbld = lShadowBlindData


class LinkedShadowsAttrOperator(
    LightDataAttrOperator[LinkedShadowsPlugOperator]
):
    __slots__ = ()

    lShadowDirection = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    lsd = lShadowDirection

    lShadowIntensity = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    lsi = lShadowIntensity

    lShadowAmbient = BoolField(default_value=False, readable=False)
    lsa = lShadowAmbient

    lShadowDiffuse = BoolField(default_value=False, readable=False)
    lsf = lShadowDiffuse

    lShadowSpecular = BoolField(default_value=False, readable=False)
    lss = lShadowSpecular

    lShadowShadowFraction = FloatField(default_value=0.0, readable=False)
    lssf = lShadowShadowFraction

    lShadowPreShadowIntensity = FloatField(default_value=0.0, readable=False)
    lsps = lShadowPreShadowIntensity

    lShadowBlindData = AddrField(default_value=0.0, readable=False)
    lbld = lShadowBlindData


class LinkedShadowsField(
    LightDataField[LinkedShadowsAttrOperator, LinkedShadowsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LinkedShadowsAttrOperator
    PLUG_CLS = LinkedShadowsPlugOperator


class IgnoredShadowsPlugOperator(
    LightDataPlugOperator["IgnoredShadowsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("xShadowDirection", "xsd"),
        ("xShadowIntensity", "xsi"),
        ("xShadowAmbient", "xsa"),
        ("xShadowDiffuse", "xsf"),
        ("xShadowSpecular", "xss"),
        ("xShadowShadowFraction", "xssf"),
        ("xShadowPreShadowIntensity", "xsps"),
        ("xShadowBlindData", "xbld"),
    )

    xShadowDirection = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    xsd = xShadowDirection

    xShadowIntensity = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    xsi = xShadowIntensity

    xShadowAmbient = BoolField(default_value=False, readable=False)
    xsa = xShadowAmbient

    xShadowDiffuse = BoolField(default_value=False, readable=False)
    xsf = xShadowDiffuse

    xShadowSpecular = BoolField(default_value=False, readable=False)
    xss = xShadowSpecular

    xShadowShadowFraction = FloatField(default_value=0.0, readable=False)
    xssf = xShadowShadowFraction

    xShadowPreShadowIntensity = FloatField(default_value=0.0, readable=False)
    xsps = xShadowPreShadowIntensity

    xShadowBlindData = AddrField(default_value=0.0, readable=False)
    xbld = xShadowBlindData


class IgnoredShadowsAttrOperator(
    LightDataAttrOperator[IgnoredShadowsPlugOperator]
):
    __slots__ = ()

    xShadowDirection = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    xsd = xShadowDirection

    xShadowIntensity = Float3Field(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    xsi = xShadowIntensity

    xShadowAmbient = BoolField(default_value=False, readable=False)
    xsa = xShadowAmbient

    xShadowDiffuse = BoolField(default_value=False, readable=False)
    xsf = xShadowDiffuse

    xShadowSpecular = BoolField(default_value=False, readable=False)
    xss = xShadowSpecular

    xShadowShadowFraction = FloatField(default_value=0.0, readable=False)
    xssf = xShadowShadowFraction

    xShadowPreShadowIntensity = FloatField(default_value=0.0, readable=False)
    xsps = xShadowPreShadowIntensity

    xShadowBlindData = AddrField(default_value=0.0, readable=False)
    xbld = xShadowBlindData


class IgnoredShadowsField(
    LightDataField[IgnoredShadowsAttrOperator, IgnoredShadowsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IgnoredShadowsAttrOperator
    PLUG_CLS = IgnoredShadowsPlugOperator


class BogusAttributePlugOperator(
    LightDataPlugOperator["BogusAttributeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bogusDirection", "bld"),
        ("bogusIntensity", "bli"),
        ("bogusAmbient", "bla"),
        ("bogusDiffuse", "blf"),
        ("bogusSpecular", "bls"),
        ("bogusShadowFraction", "blp"),
        ("bogusPreShadowIntensity", "blps"),
        ("bogusBlindData", "bbld"),
    )

    bogusDirection = Float3Field(default_value=(0.0, 0.0, 0.0), readable=False)
    bld = bogusDirection

    bogusIntensity = Float3Field(default_value=(0.0, 0.0, 0.0), readable=False)
    bli = bogusIntensity

    bogusAmbient = BoolField(default_value=False, readable=False)
    bla = bogusAmbient

    bogusDiffuse = BoolField(default_value=False, readable=False)
    blf = bogusDiffuse

    bogusSpecular = BoolField(default_value=False, readable=False)
    bls = bogusSpecular

    bogusShadowFraction = FloatField(default_value=0.0, readable=False)
    blp = bogusShadowFraction

    bogusPreShadowIntensity = FloatField(default_value=0.0, readable=False)
    blps = bogusPreShadowIntensity

    bogusBlindData = AddrField(default_value=0.0, readable=False)
    bbld = bogusBlindData


class BogusAttributeAttrOperator(
    LightDataAttrOperator[BogusAttributePlugOperator]
):
    __slots__ = ()

    bogusDirection = Float3Field(default_value=(0.0, 0.0, 0.0), readable=False)
    bld = bogusDirection

    bogusIntensity = Float3Field(default_value=(0.0, 0.0, 0.0), readable=False)
    bli = bogusIntensity

    bogusAmbient = BoolField(default_value=False, readable=False)
    bla = bogusAmbient

    bogusDiffuse = BoolField(default_value=False, readable=False)
    blf = bogusDiffuse

    bogusSpecular = BoolField(default_value=False, readable=False)
    bls = bogusSpecular

    bogusShadowFraction = FloatField(default_value=0.0, readable=False)
    blp = bogusShadowFraction

    bogusPreShadowIntensity = FloatField(default_value=0.0, readable=False)
    blps = bogusPreShadowIntensity

    bogusBlindData = AddrField(default_value=0.0, readable=False)
    bbld = bogusBlindData


class BogusAttributeField(
    LightDataField[BogusAttributeAttrOperator, BogusAttributePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BogusAttributeAttrOperator
    PLUG_CLS = BogusAttributePlugOperator


class AiCustomAOVsPlugOperator(
    CompoundPlugOperator["AiCustomAOVsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aovName", "aov_name"),
        ("aovInput", "aov_input"),
    )

    aovName = DataStringField()
    aov_name = aovName

    aovInput = MessageField()
    aov_input = aovInput


class AiCustomAOVsAttrOperator(CompoundAttrOperator[AiCustomAOVsPlugOperator]):
    __slots__ = ()

    aovName = DataStringField()
    aov_name = aovName

    aovInput = MessageField()
    aov_input = aovInput


class AiCustomAOVsField(
    CompoundField[AiCustomAOVsAttrOperator, AiCustomAOVsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiCustomAOVsAttrOperator
    PLUG_CLS = AiCustomAOVsPlugOperator


class AiSurfaceShaderPlugOperator(
    Float3CompoundBasePlugOperator["AiSurfaceShaderAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiSurfaceShaderR", "ai_surface_shaderr"),
        ("aiSurfaceShaderG", "ai_surface_shaderg"),
        ("aiSurfaceShaderB", "ai_surface_shaderb"),
    )

    aiSurfaceShaderR = FloatField(default_value=0.0)
    ai_surface_shaderr = aiSurfaceShaderR

    aiSurfaceShaderG = FloatField(default_value=0.0)
    ai_surface_shaderg = aiSurfaceShaderG

    aiSurfaceShaderB = FloatField(default_value=0.0)
    ai_surface_shaderb = aiSurfaceShaderB


class AiSurfaceShaderAttrOperator(
    Float3CompoundBaseAttrOperator[AiSurfaceShaderPlugOperator]
):
    __slots__ = ()

    aiSurfaceShaderR = FloatField(default_value=0.0)
    ai_surface_shaderr = aiSurfaceShaderR

    aiSurfaceShaderG = FloatField(default_value=0.0)
    ai_surface_shaderg = aiSurfaceShaderG

    aiSurfaceShaderB = FloatField(default_value=0.0)
    ai_surface_shaderb = aiSurfaceShaderB


class AiSurfaceShaderField(
    Float3CompoundBaseField[
        AiSurfaceShaderAttrOperator, AiSurfaceShaderPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiSurfaceShaderAttrOperator
    PLUG_CLS = AiSurfaceShaderPlugOperator

    aiSurfaceShaderR = FloatField(default_value=0.0)
    ai_surface_shaderr = aiSurfaceShaderR

    aiSurfaceShaderG = FloatField(default_value=0.0)
    ai_surface_shaderg = aiSurfaceShaderG

    aiSurfaceShaderB = FloatField(default_value=0.0)
    ai_surface_shaderb = aiSurfaceShaderB


class AiVolumeShaderPlugOperator(
    Float3CompoundBasePlugOperator["AiVolumeShaderAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiVolumeShaderR", "ai_volume_shaderr"),
        ("aiVolumeShaderG", "ai_volume_shaderg"),
        ("aiVolumeShaderB", "ai_volume_shaderb"),
    )

    aiVolumeShaderR = FloatField(default_value=0.0)
    ai_volume_shaderr = aiVolumeShaderR

    aiVolumeShaderG = FloatField(default_value=0.0)
    ai_volume_shaderg = aiVolumeShaderG

    aiVolumeShaderB = FloatField(default_value=0.0)
    ai_volume_shaderb = aiVolumeShaderB


class AiVolumeShaderAttrOperator(
    Float3CompoundBaseAttrOperator[AiVolumeShaderPlugOperator]
):
    __slots__ = ()

    aiVolumeShaderR = FloatField(default_value=0.0)
    ai_volume_shaderr = aiVolumeShaderR

    aiVolumeShaderG = FloatField(default_value=0.0)
    ai_volume_shaderg = aiVolumeShaderG

    aiVolumeShaderB = FloatField(default_value=0.0)
    ai_volume_shaderb = aiVolumeShaderB


class AiVolumeShaderField(
    Float3CompoundBaseField[
        AiVolumeShaderAttrOperator, AiVolumeShaderPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiVolumeShaderAttrOperator
    PLUG_CLS = AiVolumeShaderPlugOperator

    aiVolumeShaderR = FloatField(default_value=0.0)
    ai_volume_shaderr = aiVolumeShaderR

    aiVolumeShaderG = FloatField(default_value=0.0)
    ai_volume_shaderg = aiVolumeShaderG

    aiVolumeShaderB = FloatField(default_value=0.0)
    ai_volume_shaderb = aiVolumeShaderB
