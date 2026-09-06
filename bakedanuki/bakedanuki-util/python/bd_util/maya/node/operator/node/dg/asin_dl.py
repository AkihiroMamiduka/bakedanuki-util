# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.asin_dl import GeneratedAsinDL
else:
    from ._generated.asin_dl import GeneratedAsinDL


class AsinDL(GeneratedAsinDL):
    __slots__ = ()

    NODE_TYPE = "asinDL"
