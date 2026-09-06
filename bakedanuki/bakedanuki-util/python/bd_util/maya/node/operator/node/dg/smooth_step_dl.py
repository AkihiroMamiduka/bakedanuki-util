# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.smooth_step_dl import GeneratedSmoothStepDL
else:
    from ._generated.smooth_step_dl import GeneratedSmoothStepDL


class SmoothStepDL(GeneratedSmoothStepDL):
    __slots__ = ()

    NODE_TYPE = "smoothStepDL"
