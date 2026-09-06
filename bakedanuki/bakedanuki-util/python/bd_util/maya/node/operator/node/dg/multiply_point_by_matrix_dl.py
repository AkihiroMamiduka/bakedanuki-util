# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.multiply_point_by_matrix_dl import (
        GeneratedMultiplyPointByMatrixDL,
    )
else:
    from ._generated.multiply_point_by_matrix_dl import (
        GeneratedMultiplyPointByMatrixDL,
    )


class MultiplyPointByMatrixDL(GeneratedMultiplyPointByMatrixDL):
    __slots__ = ()

    NODE_TYPE = "multiplyPointByMatrixDL"
