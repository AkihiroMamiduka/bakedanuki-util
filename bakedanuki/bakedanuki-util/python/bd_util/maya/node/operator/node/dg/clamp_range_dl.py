# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.clamp_range_dl import GeneratedClampRangeDL
else:
    from ._generated.clamp_range_dl import GeneratedClampRangeDL


class ClampRangeDL(GeneratedClampRangeDL):
    __slots__ = ()

    NODE_TYPE = "clampRangeDL"
