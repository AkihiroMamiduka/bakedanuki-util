# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.multiply_dl import GeneratedMultiplyDL
else:
    from ._generated.multiply_dl import GeneratedMultiplyDL


class MultiplyDL(GeneratedMultiplyDL):
    __slots__ = ()

    NODE_TYPE = "multiplyDL"
