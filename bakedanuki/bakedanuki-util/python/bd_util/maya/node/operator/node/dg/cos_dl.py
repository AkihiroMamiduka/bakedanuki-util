# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.cos_dl import GeneratedCosDL
else:
    from ._generated.cos_dl import GeneratedCosDL


class CosDL(GeneratedCosDL):
    __slots__ = ()

    NODE_TYPE = "cosDL"
