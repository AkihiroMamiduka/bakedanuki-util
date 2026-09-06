# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2027.ai_imager_lens_effects import (
    BloomTintField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class BloomModeEnumPlugOperator(EnumPlugOperator["BloomModeEnumAttrOperator"]):
    __slots__ = ()

    SIMPLE = 0
    SHAPE_FILE = 1
    APERTURE = 2


class BloomModeEnumAttrOperator(EnumAttrOperator[BloomModeEnumPlugOperator]):
    __slots__ = ()

    SIMPLE = 0
    SHAPE_FILE = 1
    APERTURE = 2

    NAME_MAP = {
        SIMPLE: "simple",
        SHAPE_FILE: "shape_file",
        APERTURE: "aperture",
    }


class BloomModeEnumField(
    EnumField[BloomModeEnumAttrOperator, BloomModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BloomModeEnumAttrOperator
    PLUG_CLS = BloomModeEnumPlugOperator


class GeneratedAiImagerLensEffects(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerLensEffects"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    vignetting = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=100.0
    )

    bloomThreshold = FloatField(
        default_value=0.8999999761581421, min_value=0.0, soft_max_value=10.0
    )
    bloom_threshold = bloomThreshold

    bloomTint = BloomTintField(default_value=(1.0, 1.0, 1.0))
    bloom_tint = bloomTint
    bloomTintR = bloomTint.bloomTintR
    bloom_tintr = bloomTintR
    bloomTintG = bloomTint.bloomTintG
    bloom_tintg = bloomTintG
    bloomTintB = bloomTint.bloomTintB
    bloom_tintb = bloomTintB

    bloomRadius = FloatField(
        default_value=4.0,
        min_value=0.0,
        soft_min_value=0.009999999776482582,
        soft_max_value=12.0,
    )
    bloom_radius = bloomRadius

    bloomStrength = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=10.0
    )
    bloom_strength = bloomStrength

    bloomMode = BloomModeEnumField(default_value=2)
    bloom_mode = bloomMode

    bloomShapeFilename = DataStringField()
    bloom_shape_filename = bloomShapeFilename

    bloomShapeRotation = FloatField(
        default_value=0.0, soft_min_value=-360.0, soft_max_value=360.0
    )
    bloom_shape_rotation = bloomShapeRotation

    apertureBlades = LongField(default_value=6, min_value=3, soft_max_value=12)
    aperture_blades = apertureBlades

    apertureBladeCurvature = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    aperture_blade_curvature = apertureBladeCurvature

    apertureDispersion = FloatField(
        default_value=1.0, soft_min_value=-4.0, soft_max_value=4.0
    )
    aperture_dispersion = apertureDispersion
