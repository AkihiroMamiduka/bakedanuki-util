# coding: utf-8
"""外部設定がない場合に使う、パッケージ標準の `Nodes()` 補完対象。"""

# 利用者設定は README.md の手順で、配布外の `bd_util_typing_config.pyi` に置く。
from ..typing_profiles import Maya2025Plus as DefaultNodes

__all__ = ["DefaultNodes"]
