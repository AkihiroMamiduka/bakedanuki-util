# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2027.ai_gaussian_splat_shader import (
        GeneratedAiGaussianSplatShader,
    )
else:
    from ._generated.ai_gaussian_splat_shader import (
        GeneratedAiGaussianSplatShader,
    )


class AiGaussianSplatShader(GeneratedAiGaussianSplatShader):
    __slots__ = ()

    NODE_TYPE = "aiGaussianSplatShader"
