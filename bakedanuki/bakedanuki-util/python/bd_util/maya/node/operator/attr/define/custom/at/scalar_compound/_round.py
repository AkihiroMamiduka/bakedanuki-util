# coding: utf-8
from __future__ import annotations

import builtins
from collections.abc import Sequence
from typing import Protocol, cast


class _RoundCompoundTarget(Protocol):
    def get(self) -> Sequence[float]: ...

    def set(
        self,
        value: float | Sequence[float],
        *values: float,
    ) -> None: ...


class RoundCompoundPlugOperatorMixin:
    __slots__ = ()

    def round(self, ndigits: int = 0) -> None:
        """現在の浮動小数点compound値を成分ごとに丸めて設定する。

        Mayaのfloat2 / float3 / double2 / double3 / double4および
        angle / linear compound attributeを対象とする。``get()`` が返す
        専用compound値の各 ``float`` 成分を丸め、値型は維持する。
        numeric compoundはunitless、angleはdegree、linearはcentimeterで扱う。

        Args:
            ndigits: 丸める小数点以下の桁数。負の値も指定できる。

        Notes:
            Python組み込みの ``round()`` と同じ偶数丸めを使用する。
            呼び出し時点のscene値を ``get()`` で取得し、``set()`` と同様に
            ModifierManagerへ変更を積む。sceneへの変更は
            ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        target = cast(_RoundCompoundTarget, self)
        rounded_values = tuple(
            builtins.round(value, ndigits) for value in target.get()
        )
        target.set(rounded_values)
