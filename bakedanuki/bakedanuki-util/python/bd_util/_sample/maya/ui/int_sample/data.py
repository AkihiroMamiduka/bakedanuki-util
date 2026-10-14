# coding: utf-8
from dataclasses import dataclass


@dataclass
class IntSampleData:
    """Mayaシーンを変更せず、Python objectに保持する整数正本。"""

    signed_value: int = 42
    limited_value: int = 128
