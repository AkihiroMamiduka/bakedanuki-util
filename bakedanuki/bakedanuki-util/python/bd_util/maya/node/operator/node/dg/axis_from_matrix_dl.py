# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.axis_from_matrix_dl import (
        GeneratedAxisFromMatrixDL,
    )
else:
    from ._generated.axis_from_matrix_dl import GeneratedAxisFromMatrixDL


class AxisFromMatrixDL(GeneratedAxisFromMatrixDL):
    __slots__ = ()

    NODE_TYPE = "axisFromMatrixDL"
