# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.point_matrix_mult_dl import (
        GeneratedPointMatrixMultDL,
    )
else:
    from ._generated.point_matrix_mult_dl import GeneratedPointMatrixMultDL


class PointMatrixMultDL(GeneratedPointMatrixMultDL):
    __slots__ = ()

    NODE_TYPE = "pointMatrixMultDL"
