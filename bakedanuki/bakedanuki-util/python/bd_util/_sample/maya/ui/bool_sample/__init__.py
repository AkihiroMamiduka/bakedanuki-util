# coding: utf-8
"""bool UIの単一Window版・共有Window版と共通dataの入口。"""

# 共通dataと各sampleを、bool_sampleから型付きで辿れるように公開する。
from .data import VisibilityData
from . import bool_views, shared_bool_views

__all__ = [
    "VisibilityData",
    "bool_views",
    "shared_bool_views",
]
