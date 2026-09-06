# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.acos_dl import GeneratedAcosDL
else:
    from ._generated.acos_dl import GeneratedAcosDL


class AcosDL(GeneratedAcosDL):
    __slots__ = ()

    NODE_TYPE = "acosDL"
