# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.average_dl import GeneratedAverageDL
else:
    from ._generated.average_dl import GeneratedAverageDL


class AverageDL(GeneratedAverageDL):
    __slots__ = ()

    NODE_TYPE = "averageDL"
