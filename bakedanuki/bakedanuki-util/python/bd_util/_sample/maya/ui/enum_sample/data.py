# coding: utf-8
from dataclasses import dataclass

from .....ui import EnumDefinition

MODE_DEFINITION = EnumDefinition.from_mapping(
    {-2: "Negative", 0: "Off", 5: "Preview", 10: "Final"}
)
ROTATE_ORDER_DEFINITION = EnumDefinition.from_mapping(
    {0: "xyz", 1: "yzx", 2: "zxy", 3: "xzy", 4: "yxz", 5: "zyx"}
)


@dataclass
class EnumData:
    mode: int = 5
