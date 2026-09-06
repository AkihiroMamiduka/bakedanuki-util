# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2027.ai_tone_zones import GeneratedAiToneZones
else:
    from ._generated.ai_tone_zones import GeneratedAiToneZones


class AiToneZones(GeneratedAiToneZones):
    __slots__ = ()

    NODE_TYPE = "aiToneZones"
