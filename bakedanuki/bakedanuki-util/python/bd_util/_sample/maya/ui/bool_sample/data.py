# coding: utf-8
from dataclasses import dataclass


# 任意のPython objectを正本にできることを示す最小dataclassを用意する。
@dataclass
class VisibilityData:
    """単一Window版と共有Window版のbool sampleで共用するPython data。"""

    visible_by_default: bool = True
