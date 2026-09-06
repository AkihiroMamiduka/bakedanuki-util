# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.ai_compare_string import GeneratedAiCompareString
else:
    from ._generated.ai_compare_string import GeneratedAiCompareString


class AiCompareString(GeneratedAiCompareString):
    __slots__ = ()

    NODE_TYPE = "aiCompareString"
