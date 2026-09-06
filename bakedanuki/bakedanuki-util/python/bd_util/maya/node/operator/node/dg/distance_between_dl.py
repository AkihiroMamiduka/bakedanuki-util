# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.distance_between_dl import (
        GeneratedDistanceBetweenDL,
    )
else:
    from ._generated.distance_between_dl import GeneratedDistanceBetweenDL


class DistanceBetweenDL(GeneratedDistanceBetweenDL):
    __slots__ = ()

    NODE_TYPE = "distanceBetweenDL"
