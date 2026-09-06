# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.multiply_vector_by_matrix_dl import (
        GeneratedMultiplyVectorByMatrixDL,
    )
else:
    from ._generated.multiply_vector_by_matrix_dl import (
        GeneratedMultiplyVectorByMatrixDL,
    )


class MultiplyVectorByMatrixDL(GeneratedMultiplyVectorByMatrixDL):
    __slots__ = ()

    NODE_TYPE = "multiplyVectorByMatrixDL"
