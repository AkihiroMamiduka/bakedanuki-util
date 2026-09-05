# coding: utf-8
from dataclasses import dataclass


# 任意のPython objectを正本にできることを示す最小dataclassを用意する。
@dataclass
class VisibilityData:
    """bool Views sampleで使用するPython data。"""

    visible_by_default: bool = True
