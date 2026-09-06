# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.max_dl import GeneratedMaxDL
else:
    from ._generated.max_dl import GeneratedMaxDL


class MaxDL(GeneratedMaxDL):
    __slots__ = ()

    NODE_TYPE = "maxDL"
