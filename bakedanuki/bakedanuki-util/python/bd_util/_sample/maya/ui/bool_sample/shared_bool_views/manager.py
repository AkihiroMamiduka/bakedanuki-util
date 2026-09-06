# coding: utf-8
from __future__ import annotations

from functools import partial
from typing import Literal

from ......maya.ui import MayaBoolBinding, MayaWindowController
from ......ui import qt
from ..bool_plug import resolve_optional_bool_plug
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
        plug = resolve_optional_bool_plug(
            maya_node_name,
            maya_attribute_name,
        )
        # bindingは個々のWindowから独立してManagerが保持する。
        self.binding = MayaBoolBinding.from_attribute(
            data, data_attribute_name, maya_plug=plug
        )
        self.data = self.binding.store.instance
        self.store = self.binding.store
        self.view_model = self.binding.view_model
        self.maya_view = self.binding.maya_view
        self._maya_description = (
            "None"
            if plug is None
            else f"{plug.node.cmd_access_name}.{maya_attribute_name}"
        )
        self._is_disposed = False

        # 各Windowの生成・再表示・破棄には既存のControllerを使用する。
        self._controller_a = MayaWindowController(
            partial(self._create_window, "A")
        )
        self._controller_b = MayaWindowController(
            partial(self._create_window, "B")
        )

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
        return self._is_disposed or self.binding.is_disposed

    @property
    def value(self) -> bool:
        """共有ViewModelが現在公開している確定値を返す。"""
        self._require_active()
        return self.binding.value

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
        return self.binding.set_value(value)

    def refresh_from_data(self) -> bool:
        """Python objectを直接変更した後、全Viewへ現在値を再反映する。"""
        self._require_active()
        return self.binding.refresh()

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
        self.binding.dispose()
        self._controller_a.dispose()
        self._controller_b.dispose()

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
