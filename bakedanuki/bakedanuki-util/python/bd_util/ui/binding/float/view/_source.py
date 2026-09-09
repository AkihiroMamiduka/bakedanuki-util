# coding: utf-8
from __future__ import annotations

from typing import cast

from .... import qt
from ..binding import FloatBinding
from ..store import FloatValueStore
from ..view_model import FloatViewModel


def resolve_float_view_source(
    source: object,
) -> tuple[FloatViewModel, FloatBinding[FloatValueStore] | None]:
    """入力元を検証し、共通ViewModelと参照保持するBindingを返す。"""
    binding = None
    if isinstance(source, FloatBinding):
        # 実行時には消えるStore型引数を、読み取り専用の共通境界へ揃える。
        binding = cast(FloatBinding[FloatValueStore], source)
        view_model = binding.view_model
    elif isinstance(source, FloatViewModel):
        view_model = source
    else:
        raise TypeError(
            "view_modelにはFloatViewModelまたはFloatBindingを指定してください: "
            f"{type(source).__name__}"
        )
    if not qt.isValid(view_model):
        raise RuntimeError("表示対象のFloatViewModelは破棄されています")
    return view_model, binding
