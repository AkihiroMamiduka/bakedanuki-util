# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.negate_dl import GeneratedNegateDL
else:
    from ._generated.negate_dl import GeneratedNegateDL


class NegateDL(GeneratedNegateDL):
    __slots__ = ()

    NODE_TYPE = "negateDL"
