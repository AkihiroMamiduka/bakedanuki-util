# coding: utf-8
from __future__ import annotations

from typing import cast

from .... import qt
from ..binding import BoolBinding
from ..store import BoolValueStore
from ..view_model import BoolViewModel


def resolve_bool_view_source(
    source: object,
) -> tuple[BoolViewModel, BoolBinding[BoolValueStore] | None]:
    """入力元を検証し、共通ViewModelと参照保持するBindingを返す。"""
    binding = None
    if isinstance(source, BoolBinding):
        # 実行時には消えるStore型引数を、読み取り専用の共通境界へ揃える。
        binding = cast(BoolBinding[BoolValueStore], source)
        view_model = binding.view_model
    elif isinstance(source, BoolViewModel):
        view_model = source
    else:
        raise TypeError(
            "view_modelにはBoolViewModelまたはBoolBindingを指定してください: "
            f"{type(source).__name__}"
        )
    if not qt.isValid(view_model):
        raise RuntimeError("表示対象のBoolViewModelは破棄されています")
    return view_model, binding
