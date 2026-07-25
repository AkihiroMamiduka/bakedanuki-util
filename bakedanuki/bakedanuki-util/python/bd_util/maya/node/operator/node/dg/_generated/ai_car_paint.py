# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_car_paint import (
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
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedAiCarPaint(DG):
    __slots__ = ()

    NODE_TYPE = "aiCarPaint"

    outColor = OutColorField(default_value=(0.5, 0.5, 0.5), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.5, 0.5, 0.5), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 0.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    hardwareColor = HardwareColorField(default_value=(0.5, 0.5, 0.5))
    hwc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hwcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hwcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hwcb = hardwareColorB

    base = FloatField(default_value=0.800000011920929, min_value=0.0, max_value=1.0)

    baseColor = BaseColorField(default_value=(1.0, 0.0, 0.0))
    base_color = baseColor
    baseColorR = baseColor.baseColorR
    base_colorr = baseColorR
    baseColorG = baseColor.baseColorG
    base_colorg = baseColorG
    baseColorB = baseColor.baseColorB
    base_colorb = baseColorB

    baseRoughness = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    base_roughness = baseRoughness

    specular = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    specularColor = SpecularColorField(default_value=(1.0, 1.0, 1.0))
    specular_color = specularColor
    specularColorR = specularColor.specularColorR
    specular_colorr = specularColorR
    specularColorG = specularColor.specularColorG
    specular_colorg = specularColorG
    specularColorB = specularColor.specularColorB
    specular_colorb = specularColorB

    specularFlipFlop = SpecularFlipFlopField(default_value=(1.0, 1.0, 1.0))
    specular_flip_flop = specularFlipFlop
    specularFlipFlopR = specularFlipFlop.specularFlipFlopR
    specular_flip_flopr = specularFlipFlopR
    specularFlipFlopG = specularFlipFlop.specularFlipFlopG
    specular_flip_flopg = specularFlipFlopG
    specularFlipFlopB = specularFlipFlop.specularFlipFlopB
    specular_flip_flopb = specularFlipFlopB

    specularLightFacing = SpecularLightFacingField(default_value=(1.0, 1.0, 1.0))
    specular_light_facing = specularLightFacing
    specularLightFacingR = specularLightFacing.specularLightFacingR
    specular_light_facingr = specularLightFacingR
    specularLightFacingG = specularLightFacing.specularLightFacingG
    specular_light_facingg = specularLightFacingG
    specularLightFacingB = specularLightFacing.specularLightFacingB
    specular_light_facingb = specularLightFacingB

    specularFalloff = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    specular_falloff = specularFalloff

    specularRoughness = FloatField(default_value=0.05000000074505806, min_value=0.0, max_value=1.0)
    specular_roughness = specularRoughness

    specularIOR = FloatField(default_value=1.5199999809265137, min_value=0.0, soft_max_value=3.0)
    specular_IOR = specularIOR

    transmissionColor = TransmissionColorField(default_value=(1.0, 1.0, 1.0))
    transmission_color = transmissionColor
    transmissionColorR = transmissionColor.transmissionColorR
    transmission_colorr = transmissionColorR
    transmissionColorG = transmissionColor.transmissionColorG
    transmission_colorg = transmissionColorG
    transmissionColorB = transmissionColor.transmissionColorB
    transmission_colorb = transmissionColorB

    flakeColor = FlakeColorField(default_value=(1.0, 1.0, 1.0))
    flake_color = flakeColor
    flakeColorR = flakeColor.flakeColorR
    flake_colorr = flakeColorR
    flakeColorG = flakeColor.flakeColorG
    flake_colorg = flakeColorG
    flakeColorB = flakeColor.flakeColorB
    flake_colorb = flakeColorB

    flakeFlipFlop = FlakeFlipFlopField(default_value=(1.0, 1.0, 1.0))
    flake_flip_flop = flakeFlipFlop
    flakeFlipFlopR = flakeFlipFlop.flakeFlipFlopR
    flake_flip_flopr = flakeFlipFlopR
    flakeFlipFlopG = flakeFlipFlop.flakeFlipFlopG
    flake_flip_flopg = flakeFlipFlopG
    flakeFlipFlopB = flakeFlipFlop.flakeFlipFlopB
    flake_flip_flopb = flakeFlipFlopB

    flakeLightFacing = FlakeLightFacingField(default_value=(1.0, 1.0, 1.0))
    flake_light_facing = flakeLightFacing
    flakeLightFacingR = flakeLightFacing.flakeLightFacingR
    flake_light_facingr = flakeLightFacingR
    flakeLightFacingG = flakeLightFacing.flakeLightFacingG
    flake_light_facingg = flakeLightFacingG
    flakeLightFacingB = flakeLightFacing.flakeLightFacingB
    flake_light_facingb = flakeLightFacingB

    flakeFalloff = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    flake_falloff = flakeFalloff

    flakeRoughness = FloatField(default_value=0.4000000059604645, min_value=0.0, max_value=1.0)
    flake_roughness = flakeRoughness

    flakeIOR = FloatField(default_value=100.0, min_value=0.0, soft_max_value=100.0)
    flake_IOR = flakeIOR

    flakeScale = FloatField(default_value=0.0010000000474974513, min_value=9.999999974752427e-07, soft_max_value=100.0)
    flake_scale = flakeScale

    flakeDensity = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    flake_density = flakeDensity

    flakeLayers = LongField(default_value=1, min_value=1, soft_max_value=4)
    flake_layers = flakeLayers

    flakeNormalRandomize = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    flake_normal_randomize = flakeNormalRandomize

    flakeCoordSpace = FlakeCoordSpaceEnumField(default_value=2)
    flake_coord_space = flakeCoordSpace

    prefName = DataStringField()
    pref_name = prefName

    coat = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    coatColor = CoatColorField(default_value=(1.0, 1.0, 1.0))
    coat_color = coatColor
    coatColorR = coatColor.coatColorR
    coat_colorr = coatColorR
    coatColorG = coatColor.coatColorG
    coat_colorg = coatColorG
    coatColorB = coatColor.coatColorB
    coat_colorb = coatColorB

    coatRoughness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    coat_roughness = coatRoughness

    coatIOR = FloatField(default_value=1.5, min_value=0.0, soft_max_value=5.0)
    coat_IOR = coatIOR

    coatNormal = CoatNormalField(default_value=(0.0, 0.0, 0.0))
    coat_normal = coatNormal
    coatNormalX = coatNormal.coatNormalX
    coat_normalx = coatNormalX
    coatNormalY = coatNormal.coatNormalY
    coat_normaly = coatNormalY
    coatNormalZ = coatNormal.coatNormalZ
    coat_normalz = coatNormalZ
