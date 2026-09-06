# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.scale_from_matrix_dl import (
        GeneratedScaleFromMatrixDL,
    )
else:
    from ._generated.scale_from_matrix_dl import GeneratedScaleFromMatrixDL


class ScaleFromMatrixDL(GeneratedScaleFromMatrixDL):
    __slots__ = ()

    NODE_TYPE = "scaleFromMatrixDL"
