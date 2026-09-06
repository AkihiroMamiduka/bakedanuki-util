# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.angle_between_dl import GeneratedAngleBetweenDL
else:
    from ._generated.angle_between_dl import GeneratedAngleBetweenDL


class AngleBetweenDL(GeneratedAngleBetweenDL):
    __slots__ = ()

    NODE_TYPE = "angleBetweenDL"
