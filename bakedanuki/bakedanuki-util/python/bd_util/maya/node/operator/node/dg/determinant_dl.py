# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.determinant_dl import GeneratedDeterminantDL
else:
    from ._generated.determinant_dl import GeneratedDeterminantDL


class DeterminantDL(GeneratedDeterminantDL):
    __slots__ = ()

    NODE_TYPE = "determinantDL"
