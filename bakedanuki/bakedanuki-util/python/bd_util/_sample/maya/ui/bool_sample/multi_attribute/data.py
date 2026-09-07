# coding: utf-8
from dataclasses import dataclass


@dataclass
class DisplayOptionsData:
    """表示設定と、その編集を許可するかを保持する。"""

    visible: bool = True
    show_labels: bool = True
    allow_editing: bool = True
