# coding: utf-8
import re
from collections.abc import Callable
from functools import partial
from typing import Generic, TypeVar, cast

from ....ui import qt
from . import workspace_control
from .options import DockOptions
from .restore import DockRestoreSpec
from .window import MayaDockableWindow

WindowT = TypeVar("WindowT", bound=MayaDockableWindow)
_CONTROL_ID_PATTERN = re.compile(r"^[A-Za-z_]\w*$", re.ASCII)


class MayaDockableWindowController(Generic[WindowT]):
    """MayaのworkspaceControlと1つのdockable Widgetを管理する。"""

    def __init__(
        self,
        factory: Callable[[], WindowT],
        *,
        control_id: str,
        restore: DockRestoreSpec,
        dock_options: DockOptions | None = None,
    ) -> None:
        """Widget factoryと固定control IDを受け取って初期化する。"""
        # Maya UI名とuiScriptへ安全に利用できる識別子だけを許可する。
        if not _CONTROL_ID_PATTERN.fullmatch(control_id):
            raise ValueError(
                "control_idにはPython識別子として有効な名前を指定してください"
            )

        # Widget生成処理とMaya側の固定名、初期表示設定を保持する。
        self._factory = factory
        self._control_id = control_id
        self._restore_spec = restore
        self._dock_options = dock_options or DockOptions()
        self._window: WindowT | None = None
        self._window_token: object | None = None

    @property
    def window(self) -> WindowT | None:
        """現在管理しているWidgetを返す。"""
        # Widgetが未生成または破棄済みの場合はNoneを返す。
        return self._window

    @property
    def control_id(self) -> str:
        """Widgetへ設定する固定objectNameを返す。"""
        # 初期化時に検証済みの識別子を公開する。
        return self._control_id

    @property
    def workspace_control_name(self) -> str:
        """Maya側で使用するworkspaceControl名を返す。"""
        # MayaQWidgetDockableMixinと同じ規則で固定名を構成する。
        return f"{self._control_id}WorkspaceControl"

    @property
    def dock_options(self) -> DockOptions:
        """初回生成時に使用するドッキング設定を返す。"""
        # immutableな設定をそのまま公開する。
        return self._dock_options

    @property
    def restore_spec(self) -> DockRestoreSpec:
        """Maya再起動時に使用する復元設定を返す。"""
        # 検証済みのmoduleと関数名を公開する。
        return self._restore_spec

    def show(self) -> WindowT:
        """ドッキングウィンドウを生成または再表示する。"""
        control_name = self.workspace_control_name
        attached_now = False

        # 保存済みまたは非表示のworkspaceControlがあればMaya側から復元する。
        if workspace_control.exists(control_name):
            workspace_control.restore(control_name)
            window = self._window

            # uiScriptで復元されなかった場合は既存controlへWidgetを接続する。
            if window is None:
                window = self._ensure_window()
                parent_pointer = workspace_control.find_control(control_name)
                workspace_control.attach(window, parent_pointer)
                workspace_control.register(control_name, window)
                attached_now = True
        else:
            # 初回だけDockOptionsとuiScriptをMixinへ渡してcontrolを生成する。
            window = self._ensure_window()
            show_dockable = cast(Callable[..., None], window.show)
            show_dockable(
                dockable=True,
                **self._dock_options.to_mixin_arguments(
                    self._restore_spec.to_ui_script()
                ),
            )
            workspace_control.register(control_name, window)
            attached_now = True

            # 任意の対象が指定されている場合だけ初回配置をタブへ変更する。
            tab_target = self._dock_options.tab_to_control
            if tab_target is not None:
                workspace_control.tab_to(control_name, tab_target)

        # Maya 2025のMixinを補完して親DockWidgetにも許可領域を反映する。
        workspace_control.apply_allowed_area(
            window,
            self._dock_options.allowed_area,
        )

        # 現在のタブを前面へ移動し、キーボード操作対象にする。
        window.raise_()
        window.activateWindow()

        # 新しくworkspaceControlへ接続したWidgetへlifecycle開始を通知する。
        if attached_now:
            window.dock_attached.emit()
        return window

    def restore(self) -> WindowT:
        """Mayaが復元中のworkspaceControlへWidgetを接続する。"""
        # uiScript実行中に設定されているcurrent parentを先に取得する。
        parent_pointer = workspace_control.current_parent()
        window = self._ensure_window()

        # 再生成したWidgetをMaya layoutとMixinのcallback管理へ登録する。
        workspace_control.attach(window, parent_pointer)
        workspace_control.register(self.workspace_control_name, window)
        workspace_control.apply_allowed_area(
            window,
            self._dock_options.allowed_area,
        )

        # uiScriptによるMaya layoutへの接続完了をWidgetへ通知する。
        window.dock_attached.emit()
        return window

    def close(self) -> None:
        """再表示できる状態を残してworkspaceControlを閉じる。"""
        control_name = self.workspace_control_name

        # retain設定を含むMaya標準のclose動作へ委ねる。
        if workspace_control.exists(control_name):
            workspace_control.close(control_name)
            return

        # control生成前のWidgetがあれば通常のQt closeを実行する。
        window = self._window
        if window is not None and qt.isValid(window):
            window.close()

    def dispose(self) -> None:
        """workspaceControlと管理中のWidgetを完全に破棄する。"""
        control_name = self.workspace_control_name
        window = self._window

        # 遅れて届くdestroyed通知が次のWidgetへ影響しないよう先に参照を外す。
        self._window = None
        self._window_token = None
        workspace_control.unregister(control_name)

        # Widgetが生存している間に保存とcallback解除の機会を通知する。
        if window is not None and qt.isValid(window):
            window.dock_about_to_dispose.emit()

        # workspaceControlが存在する場合は格納WidgetごとMayaから削除する。
        if workspace_control.exists(control_name):
            workspace_control.delete(control_name)
            return

        # controlへ未接続のWidgetだけQt event loopへ削除を予約する。
        if window is not None and qt.isValid(window):
            window.close()
            window.deleteLater()

    def reset_workspace_state(self) -> None:
        """WidgetとMayaが保存したworkspaceControl stateを削除する。"""
        control_name = self.workspace_control_name

        # 実体を先に破棄してから次回配置へ影響する保存状態を削除する。
        self.dispose()
        if workspace_control.state_exists(control_name):
            workspace_control.remove_state(control_name)

    def _ensure_window(self) -> WindowT:
        """管理対象Widgetを必要に応じて生成する。"""
        # 生存中のWidgetがあれば同一instanceを再利用する。
        window = self._window
        if window is not None and qt.isValid(window):
            return window

        # 固定objectNameをshow前に設定してMaya側の名前を安定させる。
        window = self._factory()
        window.setObjectName(self._control_id)
        token = object()
        self._window = window
        self._window_token = token
        window.destroyed.connect(partial(self._on_window_destroyed, token))
        return window

    def _on_window_destroyed(
        self,
        token: object,
        _object: qt.QtCore.QObject | None = None,
    ) -> None:
        """管理対象Widgetの破棄通知を処理する。"""
        # 現在管理中のWidgetから届いた通知だけを状態へ反映する。
        if token is self._window_token:
            self._window = None
            self._window_token = None
            workspace_control.unregister(self.workspace_control_name)
