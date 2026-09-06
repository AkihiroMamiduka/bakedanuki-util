# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.equal_dl import GeneratedEqualDL
else:
    from ._generated.equal_dl import GeneratedEqualDL


class EqualDL(GeneratedEqualDL):
    __slots__ = ()

    NODE_TYPE = "equalDL"
