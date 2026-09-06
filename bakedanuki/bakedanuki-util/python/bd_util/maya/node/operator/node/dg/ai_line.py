# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2027.ai_line import GeneratedAiLine
else:
    from ._generated.ai_line import GeneratedAiLine


class AiLine(GeneratedAiLine):
    __slots__ = ()

    NODE_TYPE = "aiLine"
