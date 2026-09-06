# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.normalize_dl import GeneratedNormalizeDL
else:
    from ._generated.normalize_dl import GeneratedNormalizeDL


class NormalizeDL(GeneratedNormalizeDL):
    __slots__ = ()

    NODE_TYPE = "normalizeDL"
