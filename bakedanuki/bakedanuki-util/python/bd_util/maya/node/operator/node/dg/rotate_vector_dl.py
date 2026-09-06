# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.rotate_vector_dl import GeneratedRotateVectorDL
else:
    from ._generated.rotate_vector_dl import GeneratedRotateVectorDL


class RotateVectorDL(GeneratedRotateVectorDL):
    __slots__ = ()

    NODE_TYPE = "rotateVectorDL"
