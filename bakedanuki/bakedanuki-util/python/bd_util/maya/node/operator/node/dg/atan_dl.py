# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.atan_dl import GeneratedAtanDL
else:
    from ._generated.atan_dl import GeneratedAtanDL


class AtanDL(GeneratedAtanDL):
    __slots__ = ()

    NODE_TYPE = "atanDL"
