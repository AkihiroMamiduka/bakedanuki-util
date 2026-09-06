# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.sin_dl import GeneratedSinDL
else:
    from ._generated.sin_dl import GeneratedSinDL


class SinDL(GeneratedSinDL):
    __slots__ = ()

    NODE_TYPE = "sinDL"
