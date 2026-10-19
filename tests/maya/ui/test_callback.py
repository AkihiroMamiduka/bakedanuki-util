# coding: utf-8
import warnings
from collections.abc import Callable
from typing import cast

import pytest

from bd_util.maya.ui import MayaCallbackRegistry
from bd_util.maya.ui import callback as maya_callback
from bd_util.ui import qt


def _replace_callback_api(monkeypatch) -> dict[str, object]:
    """Maya callbackの登録と解除を記録するtest用APIへ置き換える。"""
    calls: dict[str, object] = {"removed": []}

    def add_maya_exiting(callback: Callable[..., None]) -> int:
        """Maya終了callbackを記録して固定IDを返す。"""
        calls["maya_exiting"] = callback
        return 99

    def remove_callback(callback_id: int) -> None:
        """解除されたcallback IDを記録する。"""
        removed = cast(list[int], calls["removed"])
        removed.append(callback_id)

    monkeypatch.setattr(
        maya_callback,
        "_add_maya_exiting_callback",
        add_maya_exiting,
    )
    monkeypatch.setattr(
        maya_callback,
        "_remove_callback",
        remove_callback,
    )
    return calls


def test_registry_registers_and_disposes_callbacks_in_reverse_order(
    monkeypatch,
) -> None:
    # ownerと同じ寿命で管理するcallback registryを生成する。
    calls = _replace_callback_api(monkeypatch)
    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(owner)

    # 利用側callbackだけを登録順で公開する。
    assert registry.register(10) == 10
    assert registry.register(20) == 20
    assert registry.callback_ids == (10, 20)
    assert not registry.is_disposed

    # 利用側を逆順、内部のMaya終了callbackを最後に解除する。
    registry.dispose()
    registry.dispose()
    assert registry.callback_ids == ()
    assert registry.is_disposed
    assert calls["removed"] == [20, 10, 99]


def test_registry_dispose_disconnects_owner_without_warning(
    monkeypatch,
) -> None:
    # PySide 6.8でも警告を出さないownerとの接続解除を確認する。
    calls = _replace_callback_api(monkeypatch)
    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(owner)

    # signal instanceからbound methodを探さず、保持した接続を解除する。
    with warnings.catch_warnings():
        warnings.simplefilter("error", RuntimeWarning)
        registry.dispose()
    owner.destroyed.emit()
    assert calls["removed"] == [99]


def test_registry_can_remove_one_callback(monkeypatch) -> None:
    # 個別解除結果を確認できるregistryを生成する。
    calls = _replace_callback_api(monkeypatch)
    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(owner)
    registry.register(10)
    registry.register(20)

    # 登録済みIDだけをMayaから解除し、残りはdispose時に解除する。
    assert registry.remove(10)
    assert not registry.remove(10)
    assert registry.callback_ids == (20,)
    assert calls["removed"] == [10]
    registry.dispose()
    assert calls["removed"] == [10, 20, 99]


def test_registry_removes_many_once_and_preserves_other_order(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """一括解除で重複・未登録IDを無視し、残る監視を逆順に終了する。"""
    calls = _replace_callback_api(monkeypatch)
    owner = qt.QObject()
    registry = MayaCallbackRegistry(owner)
    for identifier in (10, 20, 30, 40):
        registry.register(identifier)
    assert registry.remove_many((10, 30, 10, 90)) == 2
    assert registry.callback_ids == (20, 40)
    assert calls["removed"] == [30, 10]
    with pytest.raises(TypeError):
        registry.remove_many((20, True))
    assert registry.callback_ids == (20, 40)
    registry.dispose()
    assert registry.remove_many((20,)) == 0
    assert calls["removed"] == [30, 10, 40, 20, 99]


def test_registry_rejects_invalid_or_duplicate_callback_id(
    monkeypatch,
) -> None:
    # callback ID検証用のregistryを生成する。
    _replace_callback_api(monkeypatch)
    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(owner)

    # Maya APIから返されない値と重複登録を明確なerrorにする。
    with pytest.raises(TypeError):
        registry.register(True)
    registry.register(10)
    with pytest.raises(ValueError):
        registry.register(10)
    registry.dispose()
    with pytest.raises(RuntimeError):
        registry.register(20)


def test_registry_runs_exit_handler_before_dispose(monkeypatch) -> None:
    # Maya終了時の利用側処理とcallback解除順を共通listへ記録する。
    calls = _replace_callback_api(monkeypatch)
    events: list[str] = []
    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(
        owner,
        on_maya_exiting=lambda: events.append("maya_exiting"),
    )
    registry.register(10)
    maya_exiting = cast(Callable[..., None], calls["maya_exiting"])

    # 利用側終了処理を実行してからregistry全体を解除する。
    maya_exiting(None)
    assert events == ["maya_exiting"]
    assert registry.is_disposed
    assert calls["removed"] == [10, 99]


def test_registry_disposes_even_when_exit_handler_fails(monkeypatch) -> None:
    # 利用側終了処理の例外を再現するregistryを生成する。
    calls = _replace_callback_api(monkeypatch)

    def raise_exit_error() -> None:
        """test用の終了処理errorを送出する。"""
        raise RuntimeError("exit failed")

    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(
        owner,
        on_maya_exiting=raise_exit_error,
    )
    registry.register(10)
    maya_exiting = cast(Callable[..., None], calls["maya_exiting"])

    # 終了処理が失敗してもfinallyで全callbackを解除する。
    with pytest.raises(RuntimeError, match="exit failed"):
        maya_exiting(None)
    assert registry.is_disposed
    assert calls["removed"] == [10, 99]


def test_registry_disposes_when_owner_is_destroyed(monkeypatch) -> None:
    # ownerの外部破棄をsignalで再現するregistryを生成する。
    calls = _replace_callback_api(monkeypatch)
    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(owner)
    registry.register(10)

    # controllerを経由しない破棄でもcallbackを残さない。
    owner.destroyed.emit()
    assert registry.is_disposed
    assert calls["removed"] == [10, 99]


def test_dispose_owned_callbacks_disposes_direct_child_registries(
    monkeypatch,
) -> None:
    # 1つのownerが複数registryを持つ状態を再現する。
    calls = _replace_callback_api(monkeypatch)
    owner = qt.QtCore.QObject()
    first = MayaCallbackRegistry(owner)
    second = MayaCallbackRegistry(owner)
    first.register(10)
    second.register(20)

    # controller用helperが全registryを即時解除する。
    assert maya_callback.dispose_owned_callbacks(owner) == 2
    assert first.is_disposed
    assert second.is_disposed
    assert calls["removed"] == [10, 99, 20, 99]


def test_registry_manages_real_maya_event_callback(
    new_scene,
    maya_cmds,
    maya_om,
) -> None:
    # Maya standaloneへ実際の選択変更callbackを登録する。
    events: list[str] = []
    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(owner)
    callback_id = maya_om.MEventMessage.addEventCallback(
        "SelectionChanged",
        lambda *_args: events.append("selection_changed"),
    )
    registry.register(int(callback_id))

    # 登録中だけ選択変更通知が届くことを確認する。
    node = maya_cmds.createNode("transform")
    maya_cmds.select(node)
    assert events
    event_count = len(events)
    registry.dispose()
    maya_cmds.select(clear=True)
    assert len(events) == event_count


def test_many_callback_ids_avoid_pairwise_comparisons(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """多数IDの登録で全組合せを比較せず、登録順と逆順解除を維持する。"""
    calls = _replace_callback_api(monkeypatch)
    comparisons = 0

    class CountedId(int):
        """IDの等価比較回数だけを記録する。"""

        __hash__ = int.__hash__

        def __eq__(self, other: object) -> bool:
            """通常の整数比較を維持して呼出しを数える。"""
            nonlocal comparisons
            comparisons += 1
            return int.__eq__(self, other)

    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(owner)
    identifiers = tuple(CountedId(index) for index in range(1000, 2000))
    for identifier in identifiers:
        registry.register(identifier)
    assert comparisons <= len(identifiers)
    assert registry.callback_ids == identifiers
    registry.dispose()
    assert calls["removed"] == [*reversed(identifiers), 99]


@pytest.mark.parametrize("failure", [RuntimeError, ValueError])
def test_remove_updates_membership_before_reentry_and_api_failure(
    monkeypatch: pytest.MonkeyPatch, failure: type[Exception]
) -> None:
    """解除中の再入とAPI失敗でも所属を先に更新し、同じIDを再登録できる。"""
    _replace_callback_api(monkeypatch)
    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(owner)
    registry.register(10)
    registry.register(20)
    removed: list[int] = []
    interrupted = False

    def remove_callback(callback_id: int) -> None:
        """最初の解除中だけ再入とID再登録を行って失敗させる。"""
        nonlocal interrupted
        removed.append(callback_id)
        if interrupted:
            return
        interrupted = True
        assert registry.callback_ids == (20,)
        assert not registry.remove(callback_id)
        registry.register(callback_id)
        raise failure("検証用の解除失敗")

    monkeypatch.setattr(maya_callback, "_remove_callback", remove_callback)
    if failure is RuntimeError:
        assert registry.remove(10)
    else:
        with pytest.raises(failure, match="検証用"):
            registry.remove(10)
    assert registry.callback_ids == (20, 10)
    with pytest.raises(ValueError):
        registry.register(10)
    registry.dispose()
    assert removed == [10, 10, 20, 99]
    assert not registry.remove(10)


def test_dispose_clears_membership_before_reentrant_removal(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """全解除前に所属を空にし、再入で同じIDを二重解除しない。"""
    _replace_callback_api(monkeypatch)
    owner = qt.QtCore.QObject()
    registry = MayaCallbackRegistry(owner)
    registry.register(10)
    registry.register(20)
    removed: list[int] = []

    def remove_callback(callback_id: int) -> None:
        """Mayaの解除中にregistryを再度呼び出す。"""
        removed.append(callback_id)
        assert registry.callback_ids == ()
        assert not registry.remove(callback_id)
        registry.dispose()
        with pytest.raises(RuntimeError):
            registry.register(callback_id)

    monkeypatch.setattr(maya_callback, "_remove_callback", remove_callback)
    registry.dispose()
    assert removed == [20, 10, 99]


def test_exit_callback_registration_failure_disposes_partial_registry(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """終了監視の登録に失敗しても半初期化状態を破棄して二重解除を防ぐ。"""
    calls = _replace_callback_api(monkeypatch)
    owner = qt.QtCore.QObject()

    def fail_registration(_callback: Callable[..., None]) -> int:
        """Mayaによる終了監視登録の拒否を再現する。"""
        raise RuntimeError("検証用の登録失敗")

    monkeypatch.setattr(
        maya_callback, "_add_maya_exiting_callback", fail_registration
    )
    with pytest.raises(RuntimeError, match="検証用"):
        MayaCallbackRegistry(owner)
    children = tuple(
        child
        for child in owner.children()
        if isinstance(child, MayaCallbackRegistry)
    )
    assert len(children) == 1
    assert children[0].is_disposed
    assert children[0].callback_ids == ()
    owner.destroyed.emit()
    assert calls["removed"] == []
