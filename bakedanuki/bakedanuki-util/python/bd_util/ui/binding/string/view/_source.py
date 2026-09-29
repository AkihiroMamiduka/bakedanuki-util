# coding: utf-8
from __future__ import annotations

from typing import cast

from ..binding import StringBinding
from ..store import StringValueStore
from ..view_model import StringViewModel


def resolve_string_view_source(
    source: object,
) -> tuple[StringViewModel, StringBinding[StringValueStore] | None]:
    """Viewへ渡されたBindingまたはViewModelを検証する。"""
    if isinstance(source, StringBinding):
        binding = cast(StringBinding[StringValueStore], source)
        return binding.view_model, binding
    if isinstance(source, StringViewModel):
        if source.is_disposed:
            raise RuntimeError("StringViewModelは終了しています")
        return source, None
    raise TypeError(
        "view_modelにはStringViewModelまたはStringBindingが必要です"
    )
