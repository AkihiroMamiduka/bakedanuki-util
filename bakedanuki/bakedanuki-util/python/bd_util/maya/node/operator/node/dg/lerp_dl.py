# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.lerp_dl import GeneratedLerpDL
else:
    from ._generated.lerp_dl import GeneratedLerpDL


class LerpDL(GeneratedLerpDL):
    __slots__ = ()

    NODE_TYPE = "lerpDL"
