# coding: utf-8
from collections.abc import Callable
from typing import cast

from bd_util.maya.ui import MayaDockableWindow, MayaUiStateTracker
from bd_util.maya.ui import callback as maya_callback
from bd_util.maya.ui import ui_state as maya_ui_state
from bd_util.ui import UiStateManager, qt


class _Owner(qt.QtCore.QObject):
    """QObjectのdestroyed signal境界だけを再現するtest用owner。"""

    dock_attached = qt.Signal()
    dock_closed = qt.Signal()
    dock_about_to_dispose = qt.Signal()

    def __init__(self) -> None:
        """破棄通知用signalを生成する。"""
        super().__init__()
        self.event_filters: list[qt.QtCore.QObject] = []

    def installEventFilter(self, event_filter: qt.QtCore.QObject) -> None:
        """登録されたevent filterを記録する。"""
        self.event_filters.append(event_filter)

    def removeEventFilter(self, event_filter: qt.QtCore.QObject) -> None:
        """登録済みevent filterを一覧から削除する。"""
        self.event_filters.remove(event_filter)


class _RecordingManager:
    """保存回数を記録するtest用UiStateManager。"""

    def __init__(self) -> None:
        """保存・復元回数を0で初期化する。"""
        self.save_count = 0
        self.restore_count = 0

    def save_cached(self) -> bool:
        """退避済み状態の保存回数を記録して成功を返す。"""
        self.save_count += 1
        return True

    def restore(self) -> frozenset[str]:
        """復元回数を記録して空の復元結果を返す。"""
        self.restore_count += 1
        return frozenset()


def _create_tracker(
    monkeypatch,
    *,
    bind_dockable: bool = False,
    bind_window: bool = False,
) -> tuple[
    MayaUiStateTracker,
    _RecordingManager,
    _Owner,
    dict[str, object],
]:
    """Maya callback操作を記録するtracker一式を生成する。"""
    calls: dict[str, object] = {"removed": []}

    def add_callback(callback: Callable[..., None]) -> int:
        """登録callbackを記録して固定IDを返す。"""
        calls["callback"] = callback
        return 42

    def remove_callback(callback_id: int) -> None:
        """解除されたcallback IDを記録する。"""
        removed = cast(list[int], calls["removed"])
        removed.append(callback_id)

    monkeypatch.setattr(
        maya_callback,
        "_add_maya_exiting_callback",
        add_callback,
    )
    monkeypatch.setattr(
        maya_callback,
        "_remove_callback",
        remove_callback,
    )

    manager = _RecordingManager()
    owner = _Owner()
    if bind_dockable and bind_window:
        raise ValueError("dockableと通常Windowを同時に指定できません")
    if bind_dockable:
        tracker = MayaUiStateTracker.for_dockable(
            cast(UiStateManager, manager),
            cast(MayaDockableWindow, owner),
        )
    elif bind_window:
        tracker = MayaUiStateTracker.for_window(
            cast(UiStateManager, manager),
            cast(qt.QtWidgets.QWidget, owner),
        )
    else:
        tracker = MayaUiStateTracker(
            cast(UiStateManager, manager),
            cast(qt.QtCore.QObject, owner),
        )
    return tracker, manager, owner, calls


def test_tracker_saves_and_removes_callback_on_maya_exit(monkeypatch) -> None:
    # Maya終了callbackを呼び出して、Widget破棄前の保存を再現する。
    tracker, manager, owner, calls = _create_tracker(monkeypatch)
    callback = cast(Callable[..., None], calls["callback"])
    callback(None)

    # 状態保存後にcallbackを解除し、owner破棄による二重解除を防ぐ。
    assert tracker.manager is manager
    assert manager.save_count == 1
    assert calls["removed"] == [42]
    owner.destroyed.emit()
    assert calls["removed"] == [42]


def test_tracker_removes_callback_when_owner_is_destroyed(monkeypatch) -> None:
    # Maya終了前にWindowが完全破棄される経路を再現する。
    _tracker, manager, owner, calls = _create_tracker(monkeypatch)
    owner.destroyed.emit()

    # UI stateを保存せず、古いMaya callbackだけを解除する。
    assert manager.save_count == 0
    assert calls["removed"] == [42]


def test_tracker_save_can_be_used_for_normal_close(monkeypatch) -> None:
    # Window lifecycleから呼べる公開save処理を確認する。
    tracker, manager, _owner, _calls = _create_tracker(monkeypatch)
    assert tracker.save()
    assert manager.save_count == 1


def test_window_tracker_restores_once_and_saves_on_each_close(
    monkeypatch,
) -> None:
    # 通常WindowのShow後に呼ばれる遅延復元処理を記録する。
    scheduled_callbacks: list[Callable[[], None]] = []
    monkeypatch.setattr(
        maya_ui_state,
        "_restore_later",
        scheduled_callbacks.append,
    )
    tracker, manager, owner, _calls = _create_tracker(
        monkeypatch,
        bind_window=True,
    )
    event_filter = owner.event_filters[0]

    # 初回Show後だけ復元を予約し、Closeごとに退避済み状態を保存する。
    event_filter.eventFilter(
        cast(qt.QtCore.QObject, owner),
        qt.QtCore.QEvent(qt.QtCore.QEvent.Type.Show),
    )
    event_filter.eventFilter(
        cast(qt.QtCore.QObject, owner),
        qt.QtCore.QEvent(qt.QtCore.QEvent.Type.Close),
    )
    assert len(scheduled_callbacks) == 1
    assert manager.restore_count == 0
    assert manager.save_count == 1

    # 同じWindowの再表示では保存状態を再適用せず、次のcloseだけ保存する。
    scheduled_callbacks[0]()
    event_filter.eventFilter(
        cast(qt.QtCore.QObject, owner),
        qt.QtCore.QEvent(qt.QtCore.QEvent.Type.Show),
    )
    event_filter.eventFilter(
        cast(qt.QtCore.QObject, owner),
        qt.QtCore.QEvent(qt.QtCore.QEvent.Type.Close),
    )
    assert manager.restore_count == 1
    assert len(scheduled_callbacks) == 1
    assert manager.save_count == 2
    assert tracker.manager is manager


def test_window_tracker_does_not_resave_after_close_and_delayed_destroy(
    monkeypatch,
) -> None:
    # controller.disposeと同じClose後の遅延破棄を再現する。
    _tracker, manager, owner, calls = _create_tracker(
        monkeypatch,
        bind_window=True,
    )
    event_filter = owner.event_filters[0]
    event_filter.eventFilter(
        cast(qt.QtCore.QObject, owner),
        qt.QtCore.QEvent(qt.QtCore.QEvent.Type.Close),
    )
    owner.destroyed.emit()

    # close時の一度だけ保存し、reset後に古い状態を復活させない。
    assert manager.save_count == 1
    assert calls["removed"] == [42]
    assert owner.event_filters == []


def test_window_tracker_saves_cached_state_on_external_destroy(
    monkeypatch,
) -> None:
    # Closeを通らず表示中の通常Windowが破棄される経路を再現する。
    _tracker, manager, owner, calls = _create_tracker(
        monkeypatch,
        bind_window=True,
    )
    owner.destroyed.emit()

    # Widgetを再取得せず退避済み状態を保存してcallbackを解除する。
    assert manager.save_count == 1
    assert calls["removed"] == [42]


def test_tracker_restores_once_after_dock_is_attached(monkeypatch) -> None:
    # dock接続後に呼ばれる遅延復元処理を記録する。
    scheduled_callbacks: list[Callable[[], None]] = []
    monkeypatch.setattr(
        maya_ui_state,
        "_restore_later",
        scheduled_callbacks.append,
    )
    tracker, manager, _owner, _calls = _create_tracker(monkeypatch)

    # 同じWindowから複数回要求しても復元処理は一度だけ予約する。
    tracker.restore()
    tracker.restore()
    assert len(scheduled_callbacks) == 1
    assert manager.restore_count == 0

    # 次のevent loop相当でUiStateManagerの復元処理を実行する。
    scheduled_callbacks[0]()
    assert manager.restore_count == 1


def test_tracker_skips_delayed_restore_after_owner_is_destroyed(
    monkeypatch,
) -> None:
    # 復元予約後にownerが破棄される経路を再現する。
    scheduled_callbacks: list[Callable[[], None]] = []
    monkeypatch.setattr(
        maya_ui_state,
        "_restore_later",
        scheduled_callbacks.append,
    )
    tracker, manager, owner, _calls = _create_tracker(monkeypatch)
    tracker.restore()
    owner.destroyed.emit()

    # 破棄済みWidgetへ保存状態を適用しない。
    scheduled_callbacks[0]()
    assert manager.restore_count == 0


def test_dockable_tracker_follows_controller_lifecycle(monkeypatch) -> None:
    # dock接続後の復元処理をQt event loopへ予約できるよう記録する。
    scheduled_callbacks: list[Callable[[], None]] = []
    monkeypatch.setattr(
        maya_ui_state,
        "_restore_later",
        scheduled_callbacks.append,
    )
    tracker, manager, owner, calls = _create_tracker(
        monkeypatch,
        bind_dockable=True,
    )

    # attachと通常closeをWindow signalからtrackerへ通知する。
    owner.dock_attached.emit()
    owner.dock_closed.emit()
    assert len(scheduled_callbacks) == 1
    scheduled_callbacks[0]()
    assert manager.restore_count == 1
    assert manager.save_count == 1

    # 完全破棄直前は保存後にMaya callbackとdock signalを解除する。
    owner.dock_about_to_dispose.emit()
    assert manager.save_count == 2
    assert calls["removed"] == [42]

    # 解除後の通知とowner破棄では状態を重複保存しない。
    owner.dock_closed.emit()
    owner.destroyed.emit()
    assert tracker.manager is manager
    assert manager.save_count == 2
    assert calls["removed"] == [42]


def test_dockable_tracker_saves_cached_state_on_external_destroy(
    monkeypatch,
) -> None:
    # controllerを経由しないWidget破棄を再現する。
    _tracker, manager, owner, calls = _create_tracker(
        monkeypatch,
        bind_dockable=True,
    )
    owner.destroyed.emit()

    # Widgetを再取得せず退避済み状態を保存してcallbackを解除する。
    assert manager.save_count == 1
    assert calls["removed"] == [42]


def test_tracker_ignores_callback_already_removed_by_maya(
    monkeypatch,
) -> None:
    # Maya終了処理が先にcallbackを解除した状態を再現する。
    tracker, _manager, _owner, _calls = _create_tracker(monkeypatch)

    def raise_removed_error(_callback_id: int) -> None:
        """Maya側で解除済みの場合のRuntimeErrorを送出する。"""
        raise RuntimeError("callback already removed")

    monkeypatch.setattr(
        maya_callback,
        "_remove_callback",
        raise_removed_error,
    )

    # 解除済みcallbackを正常な破棄完了として扱う。
    tracker.dispose()
    tracker.dispose()
