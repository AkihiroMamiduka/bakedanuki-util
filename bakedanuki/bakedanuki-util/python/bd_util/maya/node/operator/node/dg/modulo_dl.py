# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.modulo_dl import GeneratedModuloDL
else:
    from ._generated.modulo_dl import GeneratedModuloDL


class ModuloDL(GeneratedModuloDL):
    __slots__ = ()

    NODE_TYPE = "moduloDL"
