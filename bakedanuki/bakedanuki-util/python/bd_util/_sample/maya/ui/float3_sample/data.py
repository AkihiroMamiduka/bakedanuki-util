# coding: utf-8
from dataclasses import dataclass


@dataclass
class OffsetData:
    """Python属性に3成分tupleを保持する編集対象。"""

    offset: tuple[float, float, float] = (
        1.23456789,
        2.3456789123,
        3.4567891234,
    )
