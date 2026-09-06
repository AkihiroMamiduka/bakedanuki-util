# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.divide_dl import GeneratedDivideDL
else:
    from ._generated.divide_dl import GeneratedDivideDL


class DivideDL(GeneratedDivideDL):
    __slots__ = ()

    NODE_TYPE = "divideDL"
