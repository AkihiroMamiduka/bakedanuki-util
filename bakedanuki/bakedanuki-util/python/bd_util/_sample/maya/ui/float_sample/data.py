# coding: utf-8
from dataclasses import dataclass


@dataclass
class WeightData:
    """Maya nodeへ保存せず、Python objectに保持する編集対象。"""

    weight: float = 0.123456789
