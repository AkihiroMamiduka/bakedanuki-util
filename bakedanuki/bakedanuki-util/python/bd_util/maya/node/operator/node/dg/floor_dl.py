# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.floor_dl import GeneratedFloorDL
else:
    from ._generated.floor_dl import GeneratedFloorDL


class FloorDL(GeneratedFloorDL):
    __slots__ = ()

    NODE_TYPE = "floorDL"
