# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.ai_imager_inference import (
        GeneratedAiImagerInference,
    )
else:
    from ._generated.ai_imager_inference import GeneratedAiImagerInference


class AiImagerInference(GeneratedAiImagerInference):
    __slots__ = ()

    NODE_TYPE = "aiImagerInference"
