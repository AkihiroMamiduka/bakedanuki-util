# coding: utf-8
from dataclasses import dataclass


@dataclass
class TransformFloat3Data:
    """cm・degree・単位なしの3成分tupleを保持するPython正本。"""

    translate: tuple[float, float, float] = (
        1.23456789,
        2.3456789123,
        3.4567891234,
    )
    rotate: tuple[float, float, float] = (
        10.123456789,
        20.234567891,
        30.345678912,
    )
    scale: tuple[float, float, float] = (1.125, 1.25, 1.5)


@dataclass
class OffsetData:
    """Python属性に3成分tupleを保持する編集対象。"""

    offset: tuple[float, float, float] = (
        1.23456789,
        2.3456789123,
        3.4567891234,
    )
