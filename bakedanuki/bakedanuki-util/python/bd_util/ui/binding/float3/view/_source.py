# coding: utf-8
from typing import cast

from ..binding import Float3Binding
from ..store import Float3ValueStore
from ..view_model import Float3ViewModel


def resolve_float3_view_source(
    source: object,
) -> tuple[Float3ViewModel, Float3Binding[Float3ValueStore] | None]:
    """入力元を検証し、表示対象と参照保持するBindingへ解決する。"""
    binding = None
    if isinstance(source, Float3Binding):
        binding = cast(Float3Binding[Float3ValueStore], source)
        view_model = binding.view_model
    elif isinstance(source, Float3ViewModel):
        view_model = source
    else:
        raise TypeError(
            "view_modelにはFloat3ViewModelまたはFloat3Bindingを指定してください"
        )
    if view_model.is_disposed or view_model.store is None:
        raise RuntimeError(
            "表示対象のFloat3ViewModelには有効なStore接続が必要です"
        )
    return view_model, binding
