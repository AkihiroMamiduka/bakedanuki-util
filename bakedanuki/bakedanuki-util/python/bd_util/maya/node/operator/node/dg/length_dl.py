# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.length_dl import GeneratedLengthDL
else:
    from ._generated.length_dl import GeneratedLengthDL


class LengthDL(GeneratedLengthDL):
    __slots__ = ()

    NODE_TYPE = "lengthDL"
