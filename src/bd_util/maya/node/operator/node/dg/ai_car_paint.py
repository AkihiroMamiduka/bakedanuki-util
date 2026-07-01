# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_car_paint import (
    BaseColorField,
    CoatColorField,
    CoatNormalField,
    FlakeColorField,
    FlakeFlipFlopField,
    FlakeLightFacingField,
    HardwareColorField,
    NormalCameraField,
    OutColorField,
    OutTransparencyField,
    SpecularColorField,
    SpecularFlipFlopField,
    SpecularLightFacingField,
    TransmissionColorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class FlakeCoordSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    PREF = 2
    UV = 3


class FlakeCoordSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    PREF = 2
    UV = 3

    NAME_MAP = {
        WORLD: "world",
        OBJECT: "object",
        PREF: "Pref",
        UV: "UV",
    }


class FlakeCoordSpaceEnumField(
    EnumField[FlakeCoordSpaceEnumAttrOperator, FlakeCoordSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlakeCoordSpaceEnumAttrOperator
    PLUG_CLS = FlakeCoordSpaceEnumPlugOperator


class AiCarPaint(DG):
    __slots__ = ()

    NODE_TYPE = "aiCarPaint"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    hardwareColor = HardwareColorField()
    hwc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hwcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hwcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hwcb = hardwareColorB

    base = FloatField()

    baseColor = BaseColorField()
    base_color = baseColor
    baseColorR = baseColor.baseColorR
    base_colorr = baseColorR
    baseColorG = baseColor.baseColorG
    base_colorg = baseColorG
    baseColorB = baseColor.baseColorB
    base_colorb = baseColorB

    baseRoughness = FloatField()
    base_roughness = baseRoughness

    specular = FloatField()

    specularColor = SpecularColorField()
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularFlipFlop = SpecularFlipFlopField()
    specular_flip_flop = specularFlipFlop
    specularFlipFlopR = specularFlipFlop.specularFlipFlopR
    specular_flip_flopr = specularFlipFlopR
    specularFlipFlopG = specularFlipFlop.specularFlipFlopG
    specular_flip_flopg = specularFlipFlopG
    specularFlipFlopB = specularFlipFlop.specularFlipFlopB
    specular_flip_flopb = specularFlipFlopB

    specularLightFacing = SpecularLightFacingField()
    specular_light_facing = specularLightFacing
    specularLightFacingR = specularLightFacing.specularLightFacingR
    specular_light_facingr = specularLightFacingR
    specularLightFacingG = specularLightFacing.specularLightFacingG
    specular_light_facingg = specularLightFacingG
    specularLightFacingB = specularLightFacing.specularLightFacingB
    specular_light_facingb = specularLightFacingB

    specularFalloff = FloatField()
    specular_falloff = specularFalloff

    specularRoughness = FloatField()
    specular_roughness = specularRoughness

    specularIOR = FloatField()
    specular_IOR = specularIOR

    transmissionColor = TransmissionColorField()
    transmission_color = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    transmission_colorr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    transmission_colorg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    transmission_colorb = transmissionColorB

    flakeColor = FlakeColorField()
    flake_color = flakeColor
    flakeColorR = flakeColor.flakeColorR
    flake_colorr = flakeColorR
    flakeColorG = flakeColor.flakeColorG
    flake_colorg = flakeColorG
    flakeColorB = flakeColor.flakeColorB
    flake_colorb = flakeColorB

    flakeFlipFlop = FlakeFlipFlopField()
    flake_flip_flop = flakeFlipFlop
    flakeFlipFlopR = flakeFlipFlop.flakeFlipFlopR
    flake_flip_flopr = flakeFlipFlopR
    flakeFlipFlopG = flakeFlipFlop.flakeFlipFlopG
    flake_flip_flopg = flakeFlipFlopG
    flakeFlipFlopB = flakeFlipFlop.flakeFlipFlopB
    flake_flip_flopb = flakeFlipFlopB

    flakeLightFacing = FlakeLightFacingField()
    flake_light_facing = flakeLightFacing
    flakeLightFacingR = flakeLightFacing.flakeLightFacingR
    flake_light_facingr = flakeLightFacingR
    flakeLightFacingG = flakeLightFacing.flakeLightFacingG
    flake_light_facingg = flakeLightFacingG
    flakeLightFacingB = flakeLightFacing.flakeLightFacingB
    flake_light_facingb = flakeLightFacingB

    flakeFalloff = FloatField()
    flake_falloff = flakeFalloff

    flakeRoughness = FloatField()
    flake_roughness = flakeRoughness

    flakeIOR = FloatField()
    flake_IOR = flakeIOR

    flakeScale = FloatField()
    flake_scale = flakeScale

    flakeDensity = FloatField()
    flake_density = flakeDensity

    flakeLayers = LongField()
    flake_layers = flakeLayers

    flakeNormalRandomize = FloatField()
    flake_normal_randomize = flakeNormalRandomize

    flakeCoordSpace = FlakeCoordSpaceEnumField()
    flake_coord_space = flakeCoordSpace

    prefName = DataStringField()
    pref_name = prefName

    coat = FloatField()

    coatColor = CoatColorField()
    coat_color = coatColor
    coatColorR = coatColor.coatColorR
    coat_colorr = coatColorR
    coatColorG = coatColor.coatColorG
    coat_colorg = coatColorG
    coatColorB = coatColor.coatColorB
    coat_colorb = coatColorB

    coatRoughness = FloatField()
    coat_roughness = coatRoughness

    coatIOR = FloatField()
    coat_IOR = coatIOR

    coatNormal = CoatNormalField()
    coat_normal = coatNormal
    coatNormalX = coatNormal.coatNormalX
    coat_normalx = coatNormalX
    coatNormalY = coatNormal.coatNormalY
    coat_normaly = coatNormalY
    coatNormalZ = coatNormal.coatNormalZ
    coat_normalz = coatNormalZ
