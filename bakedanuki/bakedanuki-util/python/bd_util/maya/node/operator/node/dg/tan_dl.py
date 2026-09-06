# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.tan_dl import GeneratedTanDL
else:
    from ._generated.tan_dl import GeneratedTanDL


class TanDL(GeneratedTanDL):
    __slots__ = ()

    NODE_TYPE = "tanDL"
