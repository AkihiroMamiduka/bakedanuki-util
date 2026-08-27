# coding: utf-8
from __future__ import annotations

import builtins
from typing import Protocol, cast


class _RoundScalarTarget(Protocol):
    def get(self) -> float: ...

    def set(self, value: float) -> None: ...


class RoundScalarPlugOperatorMixin:
    __slots__ = ()

    def round(self, ndigits: int = 0) -> None:
        """現在の浮動小数点scalar plug値を丸めて設定する。

        Mayaのfloat / double / unit attributeを対象とし、Python側では
        ``float`` 値を扱う。float / doubleはunitless、angleはdegree、
        linearはcentimeter、timeは現在のMaya UI time unitで丸める。

        Args:
            ndigits: 丸める小数点以下の桁数。負の値も指定できる。

        Notes:
            Python組み込みの ``round()`` と同じ偶数丸めを使用する。
            呼び出し時点のscene値を ``get()`` で取得し、``set()`` と同様に
            ModifierManagerへ変更を積む。sceneへの変更は
            ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        target = cast(_RoundScalarTarget, self)
        target.set(builtins.round(target.get(), ndigits))
