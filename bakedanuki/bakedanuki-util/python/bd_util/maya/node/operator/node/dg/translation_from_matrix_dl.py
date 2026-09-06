# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.translation_from_matrix_dl import (
        GeneratedTranslationFromMatrixDL,
    )
else:
    from ._generated.translation_from_matrix_dl import (
        GeneratedTranslationFromMatrixDL,
    )


class TranslationFromMatrixDL(GeneratedTranslationFromMatrixDL):
    __slots__ = ()

    NODE_TYPE = "translationFromMatrixDL"
