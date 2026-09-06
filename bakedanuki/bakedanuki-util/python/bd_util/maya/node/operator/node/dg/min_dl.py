# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.min_dl import GeneratedMinDL
else:
    from ._generated.min_dl import GeneratedMinDL


class MinDL(GeneratedMinDL):
    __slots__ = ()

    NODE_TYPE = "minDL"
