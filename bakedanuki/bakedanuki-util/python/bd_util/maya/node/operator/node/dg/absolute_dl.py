# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.absolute_dl import GeneratedAbsoluteDL
else:
    from ._generated.absolute_dl import GeneratedAbsoluteDL


class AbsoluteDL(GeneratedAbsoluteDL):
    __slots__ = ()

    NODE_TYPE = "absoluteDL"
