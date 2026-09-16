# coding: utf-8
from __future__ import annotations

from typing import cast

from ..binding import EnumBinding
from ..store import EnumValueStore
from ..view_model import EnumViewModel


def resolve_enum_view_source(
    source: object,
) -> tuple[EnumViewModel, EnumBinding[EnumValueStore] | None]:
    """入力元を検証し、共通ViewModelと参照保持するBindingを返す。"""
    binding = None
    if isinstance(source, EnumBinding):
        # 実行時には消えるStore型引数を、読み取り専用の共通境界へ揃える。
        binding = cast(EnumBinding[EnumValueStore], source)
        view_model = binding.view_model
    elif isinstance(source, EnumViewModel):
        view_model = source
    else:
        raise TypeError(
            "view_modelにはEnumViewModelまたはEnumBindingを指定してください: "
            f"{type(source).__name__}"
        )
    if view_model.is_disposed:
        raise RuntimeError("表示対象のEnumViewModelは破棄されています")
    return view_model, binding
