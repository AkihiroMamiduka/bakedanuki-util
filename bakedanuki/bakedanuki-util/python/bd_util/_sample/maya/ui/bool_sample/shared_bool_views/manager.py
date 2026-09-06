# coding: utf-8
from __future__ import annotations

from functools import partial
from typing import Literal

from ......maya.ui import MayaBoolPlugView, MayaWindowController
from ......ui import BoolViewModel, PythonBoolAttributeStore, qt
from ..bool_plug import resolve_bool_plug, validate_maya_view_names
from .window import SharedBoolViewsWindow


class SharedBoolViewsManager:
    """1組のbool bindingと、それを共有する2つのWindowを管理する。"""

    def __init__(
        self,
        data: object,
        data_attribute_name: str,
        *,
        maya_node_name: str | None = None,
        maya_attribute_name: str | None = None,
    ) -> None:
        """任意のPython bool attributeと任意のMaya同期先を共有する。"""
        # 引数を先に検証し、Python objectの指定attributeを正本にする。
        maya_view_names = validate_maya_view_names(
            maya_node_name,
            maya_attribute_name,
        )
        self.data = data
        self.store = PythonBoolAttributeStore(data, data_attribute_name)

        # 個々のWindowから独立したQObjectへ共有ViewModelの寿命を集約する。
        self._binding_owner = qt.QObject()
        self.view_model = BoolViewModel(parent=self._binding_owner)
        self.maya_view: MayaBoolPlugView | None = None
        self._maya_description = "None"
        self._is_disposed = False

        # 各Windowの生成・再表示・破棄には既存のControllerを使用する。
        self._controller_a = MayaWindowController(
            partial(self._create_window, "A")
        )
        self._controller_b = MayaWindowController(
            partial(self._create_window, "B")
        )

        # Window生成前にStoreを接続し、Maya指定時も共通のViewを1つだけ作る。
        try:
            self.view_model.attach_store(self.store)
            if maya_view_names is not None:
                node, plug = resolve_bool_plug(*maya_view_names)
                self._maya_description = (
                    f"{node.cmd_access_name}.{maya_view_names[1]}"
                )
                self.maya_view = MayaBoolPlugView(
                    self.view_model,
                    plug,
                    self._binding_owner,
                )
        except Exception:
            # 初期同期に失敗した場合も途中生成したQObjectを残さない。
            self.dispose()
            raise

    @property
    def window_a(self) -> SharedBoolViewsWindow | None:
        """現在管理しているWindow Aを返す。"""
        return self._controller_a.window

    @property
    def window_b(self) -> SharedBoolViewsWindow | None:
        """現在管理しているWindow Bを返す。"""
        return self._controller_b.window

    @property
    def is_disposed(self) -> bool:
        """Managerが終了済みか、共有QObjectが破棄済みか返す。"""
        return (
            self._is_disposed
            or not qt.isValid(self._binding_owner)
            or not qt.isValid(self.view_model)
        )

    @property
    def value(self) -> bool:
        """共有ViewModelが現在公開している確定値を返す。"""
        self._require_active()
        return self.view_model.value.value

    def show(self) -> tuple[SharedBoolViewsWindow, SharedBoolViewsWindow]:
        """両Windowを表示し、A、Bの順で返す。"""
        # 生存中のWindowは再利用し、閉じたWindowだけを再生成する。
        return self.show_a(), self.show_b()

    def show_a(self) -> SharedBoolViewsWindow:
        """同じ共有ViewModelを使ってWindow Aを表示する。"""
        self._require_active()
        return self._controller_a.show()

    def show_b(self) -> SharedBoolViewsWindow:
        """同じ共有ViewModelを使ってWindow Bを表示する。"""
        self._require_active()
        return self._controller_b.show()

    def set_value(self, value: bool) -> bool:
        """全Windowと共通のCommandをPythonから実行する。"""
        self._require_active()
        return self.view_model.set_value_command.execute(value)

    def refresh_from_data(self) -> bool:
        """Python objectを直接変更した後、全Viewへ現在値を再反映する。"""
        self._require_active()
        return self.view_model.refresh_from_store(self.store)

    def print_data_value(self) -> None:
        """表示のsnapshotではなく、正本値をScript Editorへ出力する。"""
        self._require_active()
        print(
            f"{type(self.data).__name__}.{self.store.attribute_name} = "
            f"{self.store.read()}"
        )

    def dispose(self) -> None:
        """全Windowと共有bindingを終了し、Maya callbackを即座に解除する。"""
        # 複数回呼び出しても同じresourceを再度破棄しない。
        if self._is_disposed:
            return
        self._is_disposed = True

        # 遅延削除を待たずMaya同期を停止してから両Windowを閉じる。
        if self.maya_view is not None and qt.isValid(self.maya_view):
            self.maya_view.dispose()
        self._controller_a.dispose()
        self._controller_b.dispose()

        # 共有ViewModelとMaya ViewのQObject本体はownerと一緒に破棄する。
        if qt.isValid(self._binding_owner):
            self._binding_owner.deleteLater()

    def _create_window(
        self,
        window_name: Literal["A", "B"],
        parent: qt.QWidget | None,
    ) -> SharedBoolViewsWindow:
        """Maya main windowを親として、共有ViewModelを表示するWindowを作る。"""
        self._require_active()
        window = SharedBoolViewsWindow(
            self.view_model,
            window_name,
            data_description=(
                f"{type(self.data).__name__}.{self.store.attribute_name}"
            ),
            maya_description=self._maya_description,
            parent=parent,
        )

        # Viewからの診断要求だけを、正本を所有するManagerへ接続する。
        window.bool_views_widget.print_value_requested.connect(
            self.print_data_value
        )

        # 初回表示と再生成時はA / Bを画面中央の左右へ配置する。
        area = window.screen().availableGeometry()
        offset = -window.width() - 8 if window_name == "A" else 8
        x = max(area.left(), area.center().x() + offset)
        x = min(x, max(area.left(), area.right() - window.width() + 1))
        y = max(area.top(), area.center().y() - window.height() // 2)
        window.move(x, y)
        return window

    def _require_active(self) -> None:
        """終了後の再操作を拒否し、破棄済みQObjectへのアクセスを防ぐ。"""
        if self.is_disposed:
            raise RuntimeError(
                "共有bool views sampleは終了しています。"
                "新しいSharedBoolViewsManagerを生成してください"
            )
