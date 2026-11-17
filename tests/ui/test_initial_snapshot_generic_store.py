# coding: utf-8
"""任意Storeの読取り副作用と初回接続の互換性を維持する。"""

from __future__ import annotations

from bd_util.ui import BoolBinding, FloatBinding, FloatPresentation
from bd_util.ui.binding._initial_snapshot import (
    resync_initial_state,
    take_initial_snapshot,
)


class _DynamicFloatStore:
    """読取りと属性探索に副作用を持つ汎用Storeを再現する。"""

    def __init__(self) -> None:
        """操作の記録と、通知が必要な表示範囲を準備する。"""
        self.calls: list[str] = []
        self.value = 2.0

    def __getattr__(self, name: str) -> object:
        """新しい内部hookを汎用Storeへ探索しないことを記録する。"""
        self.calls.append(name)
        raise AttributeError(name)

    @property
    def is_available(self) -> bool:
        """可用性確認の副作用を記録する。"""
        self.calls.append("available")
        return True

    @property
    def is_writable(self) -> bool:
        """入力可否確認の副作用を記録する。"""
        self.calls.append("writable")
        return True

    @property
    def presentation(self) -> FloatPresentation:
        """初回接続で通知される表示範囲を返す。"""
        self.calls.append("presentation")
        return FloatPresentation(minimum=0.0)

    def read(self) -> float:
        """読取りごとに異なる値を返す動的getterを再現する。"""
        self.calls.append("read")
        self.value += 1.0
        return self.value

    def write(self, value: float) -> float:
        """通常の書込み契約を満たして要求値を返す。"""
        self.value = value
        return value


class _DynamicBoolStore:
    """読取り回数と入力可否の評価順を観測する汎用Store。"""

    def __init__(self) -> None:
        """操作の記録を初期化する。"""
        self.calls: list[str] = []

    @property
    def is_available(self) -> bool:
        """可用性確認を記録する。"""
        self.calls.append("available")
        return True

    @property
    def is_writable(self) -> bool:
        """値取得後の入力可否確認を記録する。"""
        self.calls.append("writable")
        return True

    def read(self) -> bool:
        """一度の読取りを記録する。"""
        self.calls.append("read")
        return True

    def write(self, value: bool) -> bool:
        """公開Store契約を満たす。"""
        return value


def test_generic_float_store_preserves_dynamic_reads_and_hook_search() -> None:
    """初期表示通知後のgetterも、汎用Storeでは省略しない。"""
    store = _DynamicFloatStore()
    binding = FloatBinding(store)
    try:
        assert binding.value == 4.0
        assert store.calls == [
            "_validate_attached_view_model",
            "available",
            "read",
            "presentation",
            "available",
            "read",
            "writable",
        ]
        store.calls.clear()
        binding.refresh()
        assert store.calls == ["available", "read", "presentation", "writable"]
        assert binding.value == 5.0
    finally:
        binding.dispose()


def test_generic_bool_store_preserves_initial_and_regular_reads() -> None:
    """初回も通常refreshも、汎用Storeをliveで評価する。"""
    store = _DynamicBoolStore()
    binding = BoolBinding(store)
    try:
        assert binding.value is True
        assert store.calls == ["available", "read", "writable"]
        store.calls.clear()
        binding.refresh()
        assert store.calls == ["available", "read", "writable"]
    finally:
        binding.dispose()


def test_snapshot_opt_in_does_not_access_proxy_class() -> None:
    """実クラスの継承だけを判定し、Proxyの動的__class__へ触れない。"""

    class Proxy:
        """__class__照会を追加した場合だけ例外を出す未知Store。"""

        def __getattribute__(self, name: str) -> object:
            """動的な型照会への依存を検出する。"""
            if name == "__class__":
                raise AssertionError("動的__class__を評価しました")
            return super().__getattribute__(name)

    source = Proxy()
    assert take_initial_snapshot(source) is None
    resync_initial_state(source)
