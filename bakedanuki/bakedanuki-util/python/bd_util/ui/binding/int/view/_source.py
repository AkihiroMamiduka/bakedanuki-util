# coding: utf-8
from __future__ import annotations

from typing import cast

from .... import qt
from ..binding import IntBinding
from ..store import IntValueStore
from ..view_model import IntViewModel


def resolve_int_view_source(
    source: object,
) -> tuple[IntViewModel, IntBinding[IntValueStore] | None]:
    """BindingまたはViewModelから表示対象と保持参照を取り出す。"""
    binding = None
    if isinstance(source, IntBinding):
        binding = cast(IntBinding[IntValueStore], source)
        view_model = binding.view_model
    elif isinstance(source, IntViewModel):
        view_model = source
    else:
        raise TypeError(
            "view_modelにはIntViewModelまたはIntBindingを指定してください: "
            f"{type(source).__name__}"
        )
    if not qt.isValid(view_model):
        raise RuntimeError("表示対象のIntViewModelは破棄されています")
    return view_model, binding
