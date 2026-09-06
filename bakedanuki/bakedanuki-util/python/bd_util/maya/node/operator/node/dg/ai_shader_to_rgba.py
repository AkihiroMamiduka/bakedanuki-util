# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2027.ai_shader_to_rgba import GeneratedAiShaderToRgba
else:
    from ._generated.ai_shader_to_rgba import GeneratedAiShaderToRgba


class AiShaderToRgba(GeneratedAiShaderToRgba):
    __slots__ = ()

    NODE_TYPE = "aiShaderToRgba"
