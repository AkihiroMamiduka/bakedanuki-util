# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.column_from_matrix_dl import (
        GeneratedColumnFromMatrixDL,
    )
else:
    from ._generated.column_from_matrix_dl import GeneratedColumnFromMatrixDL


class ColumnFromMatrixDL(GeneratedColumnFromMatrixDL):
    __slots__ = ()

    NODE_TYPE = "columnFromMatrixDL"
