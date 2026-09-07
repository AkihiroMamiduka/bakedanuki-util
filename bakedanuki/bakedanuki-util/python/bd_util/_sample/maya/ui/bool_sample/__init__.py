# coding: utf-8
"""bool UIの最小版・複数属性版・共有Window版などの入口。"""

# 共通dataと各sampleを、bool_sampleから型付きで辿れるように公開する。
from .data import VisibilityData
from . import bool_views, minimal, multi_attribute, shared_bool_views

__all__ = [
    "VisibilityData",
    "bool_views",
    "minimal",
    "multi_attribute",
    "shared_bool_views",
]
