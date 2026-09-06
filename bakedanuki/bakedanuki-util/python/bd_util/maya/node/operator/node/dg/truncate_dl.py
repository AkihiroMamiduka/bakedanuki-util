# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.truncate_dl import GeneratedTruncateDL
else:
    from ._generated.truncate_dl import GeneratedTruncateDL


class TruncateDL(GeneratedTruncateDL):
    __slots__ = ()

    NODE_TYPE = "truncateDL"
