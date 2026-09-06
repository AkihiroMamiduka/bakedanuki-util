# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2027.ai_nearest_points import GeneratedAiNearestPoints
else:
    from ._generated.ai_nearest_points import GeneratedAiNearestPoints


class AiNearestPoints(GeneratedAiNearestPoints):
    __slots__ = ()

    NODE_TYPE = "aiNearestPoints"
