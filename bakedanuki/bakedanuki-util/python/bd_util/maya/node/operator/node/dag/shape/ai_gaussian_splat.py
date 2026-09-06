# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2027.ai_gaussian_splat import GeneratedAiGaussianSplat
else:
    from ._generated.ai_gaussian_splat import GeneratedAiGaussianSplat


class AiGaussianSplat(GeneratedAiGaussianSplat):
    __slots__ = ()

    NODE_TYPE = "aiGaussianSplat"
