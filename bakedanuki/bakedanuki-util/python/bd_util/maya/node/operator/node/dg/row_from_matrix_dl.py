# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.row_from_matrix_dl import (
        GeneratedRowFromMatrixDL,
    )
else:
    from ._generated.row_from_matrix_dl import GeneratedRowFromMatrixDL


class RowFromMatrixDL(GeneratedRowFromMatrixDL):
    __slots__ = ()

    NODE_TYPE = "rowFromMatrixDL"
