# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.atan2_dl import GeneratedAtan2DL
else:
    from ._generated.atan2_dl import GeneratedAtan2DL


class Atan2DL(GeneratedAtan2DL):
    __slots__ = ()

    NODE_TYPE = "atan2DL"
