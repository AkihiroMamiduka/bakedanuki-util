# coding: utf-8
from dataclasses import dataclass


@dataclass
class WeightData:
    """Maya nodeへ保存せず、Python objectに保持する編集対象。"""

    weight: float = 0.123456789


@dataclass
class TransformFloatData:
    """cm・degree・単位なしで保持し、Mayaへ同期するPython正本。"""

    translate_x: float = 1.23456789123
    rotate_x: float = 45.123456789
    scale_x: float = 1.23456789123
