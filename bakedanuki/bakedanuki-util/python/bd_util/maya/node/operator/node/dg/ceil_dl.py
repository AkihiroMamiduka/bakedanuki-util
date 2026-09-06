# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.ceil_dl import GeneratedCeilDL
else:
    from ._generated.ceil_dl import GeneratedCeilDL


class CeilDL(GeneratedCeilDL):
    __slots__ = ()

    NODE_TYPE = "ceilDL"
