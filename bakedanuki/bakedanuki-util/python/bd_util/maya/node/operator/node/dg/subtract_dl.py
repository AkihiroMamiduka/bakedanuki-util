# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.subtract_dl import GeneratedSubtractDL
else:
    from ._generated.subtract_dl import GeneratedSubtractDL


class SubtractDL(GeneratedSubtractDL):
    __slots__ = ()

    NODE_TYPE = "subtractDL"
