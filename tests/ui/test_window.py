# coding: utf-8
from PySide6 import QtCore, QtWidgets

from bd_util.ui import WindowController


def _process_deferred_deletes(
    application: QtWidgets.QApplication,
) -> None:
    """Qt event loopへ予約された削除処理を実行する。"""
    # DeferredDelete eventを送信してから残りのeventを処理する。
    QtCore.QCoreApplication.sendPostedEvents(
        None,
        QtCore.QEvent.Type.DeferredDelete,
    )
    application.processEvents()


def test_show_reuses_managed_window(qt_application) -> None:
    # factoryが生成したwindowを記録する。
    created_windows: list[QtWidgets.QDialog] = []

    def create_window() -> QtWidgets.QDialog:
        """生成履歴へ追加したtest用dialogを返す。"""
        # 新しいdialogを生成して呼び出し回数を確認できるようにする。
        window = QtWidgets.QDialog()
        created_windows.append(window)
        return window

    # 一度閉じたwindowを再表示する。
    controller = WindowController(create_window)
    first = controller.show()
    controller.close()
    second = controller.show()

    # factoryが一度だけ呼ばれ、同じwindowが再利用されたことを確認する。
    assert first is second
    assert controller.window is first
    assert created_windows == [first]

    # testで生成したwindowを削除する。
    controller.dispose()
    _process_deferred_deletes(qt_application)


def test_destroyed_window_is_recreated(qt_application) -> None:
    # 最初のwindowを生成してQt event loopから破棄する。
    controller = WindowController(QtWidgets.QDialog)
    first = controller.show()
    first.deleteLater()
    _process_deferred_deletes(qt_application)

    # 破棄通知によってcontrollerの参照が解除されたことを確認する。
    assert controller.window is None

    # 次のshowで新しいwindowが生成されることを確認する。
    second = controller.show()
    assert second is not first
    assert controller.window is second

    # testで生成したwindowを削除する。
    controller.dispose()
    _process_deferred_deletes(qt_application)


def test_dispose_releases_window_immediately(qt_application) -> None:
    # 管理対象となるwindowを生成する。
    controller = WindowController(QtWidgets.QDialog)
    window = controller.show()

    # dispose直後に参照が解除されてwindowが閉じることを確認する。
    controller.dispose()
    assert controller.window is None
    assert not window.isVisible()

    # event loopへ予約されたwindowの削除を完了する。
    _process_deferred_deletes(qt_application)


def test_delayed_deletion_does_not_release_replacement(
    qt_application,
) -> None:
    # 古いwindowの削除前に代わりとなるwindowを生成する。
    controller = WindowController(QtWidgets.QDialog)
    first = controller.show()
    controller.dispose()
    second = controller.show()
    _process_deferred_deletes(qt_application)

    # 古い破棄通知を受けても新しいwindowが保持されることを確認する。
    assert second is not first
    assert controller.window is second

    # testで生成したwindowを削除する。
    controller.dispose()
    _process_deferred_deletes(qt_application)
