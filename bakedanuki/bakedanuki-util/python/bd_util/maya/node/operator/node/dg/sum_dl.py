# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.sum_dl import GeneratedSumDL
else:
    from ._generated.sum_dl import GeneratedSumDL


class SumDL(GeneratedSumDL):
    __slots__ = ()

    NODE_TYPE = "sumDL"
