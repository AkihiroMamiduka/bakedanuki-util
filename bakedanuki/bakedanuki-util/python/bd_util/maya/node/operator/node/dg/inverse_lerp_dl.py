# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.inverse_lerp_dl import GeneratedInverseLerpDL
else:
    from ._generated.inverse_lerp_dl import GeneratedInverseLerpDL


class InverseLerpDL(GeneratedInverseLerpDL):
    __slots__ = ()

    NODE_TYPE = "inverseLerpDL"
