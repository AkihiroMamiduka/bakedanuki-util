# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass

from .....maya.ui import MayaWindowController
from .....ui import qt
from .widget import BoolViewsWidget


class BoolViewsWindow(qt.QDialog):
    """自己完結したBoolViewsWidgetを表示するsample Window。"""

    def __init__(
        self,
        data: object,
        data_attribute_name: str,
        *,
        maya_node_name: str | None = None,
        maya_attribute_name: str | None = None,
        parent: qt.QWidget | None = None,
    ) -> None:
        """BoolViewsWidgetへbinding設定を渡してWindowへ配置する。"""
        # Window自体には表示に必要な最小限の設定だけを行う。
        super().__init__(parent)
        self.setObjectName("bdUtilBoolViewsSampleWindow")
        self.setWindowTitle("bakedanuki-util bool views")
        self.resize(480, 340)

        # bool binding一式を内包するFeature Widgetを配置する。
        self.bool_views_widget = BoolViewsWidget(
            data,
            data_attribute_name,
            maya_node_name=maya_node_name,
            maya_attribute_name=maya_attribute_name,
            parent=self,
        )

        # Window固有の操作として閉じるボタンだけを追加する。
        close_button = qt.QPushButton("Close", self)
        close_button.clicked.connect(self.close)

        # Feature WidgetとWindow操作を縦に並べる。
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.bool_views_widget)
        layout.addWidget(close_button)


@dataclass(frozen=True)
class _WindowArguments:
    """MayaWindowControllerのfactoryへ渡す次回Window設定。"""

    data: object
    data_attribute_name: str
    maya_node_name: str | None
    maya_attribute_name: str | None


class BoolViewsWindowManager:
    """sample Windowの生成引数とlifecycleをまとめて管理する。"""

    def __init__(self) -> None:
        """Window factoryへ渡す一時引数とControllerを初期化する。"""
        # show()からfactoryへ渡す引数だけをWindow生成中に保持する。
        self._pending_arguments: _WindowArguments | None = None

        # Windowの生成・再表示・破棄は既存Controllerへ委譲する。
        self._controller = MayaWindowController(self._create_window)

    @property
    def window(self) -> BoolViewsWindow | None:
        """現在管理しているsample Windowを返す。"""
        return self._controller.window

    def show(
        self,
        data: object,
        data_attribute_name: str,
        *,
        maya_node_name: str | None = None,
        maya_attribute_name: str | None = None,
    ) -> BoolViewsWindow:
        """指定したbinding構成のsample Windowを表示する。"""
        # 同じ構成のWindowは再利用し、異なる構成なら完全に作り直す。
        current_window = self._controller.window
        if current_window is not None:
            same_configuration = (
                current_window.bool_views_widget.matches_configuration(
                    data,
                    data_attribute_name,
                    maya_node_name,
                    maya_attribute_name,
                )
            )
            if not same_configuration:
                self._controller.dispose()

        # Controllerのfactoryへ今回のWindow生成引数を一時的に渡す。
        self._pending_arguments = _WindowArguments(
            data,
            data_attribute_name,
            maya_node_name,
            maya_attribute_name,
        )
        try:
            return self._controller.show()
        finally:
            # Window生成後はdataへの不要な参照をManagerへ残さない。
            self._pending_arguments = None

    def set_value(self, value: bool) -> bool:
        """表示中sampleのCommandをPythonから実行する。"""
        # 値変更はFeature Widgetが公開する共通Commandへ委譲する。
        window = self._require_window()
        return window.bool_views_widget.set_value(value)

    def refresh_from_data(self) -> bool:
        """表示中sampleへPython objectの現在値を再反映する。"""
        # Python Storeの再読込はFeature Widgetへ委譲する。
        window = self._require_window()
        return window.bool_views_widget.refresh_from_data()

    def dispose(self) -> None:
        """sample WindowとMaya callbackを完全に破棄する。"""
        # 保留中の引数を破棄してからWindow lifecycleを終了する。
        self._pending_arguments = None
        self._controller.dispose()

    def _create_window(
        self,
        parent: qt.QWidget | None,
    ) -> BoolViewsWindow:
        """show()が準備したbinding設定でsample Windowを生成する。"""
        # Window生成中だけ保持される引数をfactory側で受け取る。
        arguments = self._pending_arguments
        if arguments is None:
            raise RuntimeError(
                "bool views sampleのbinding設定が指定されていません"
            )

        # Maya main windowを親として設定済みFeature Windowを生成する。
        return BoolViewsWindow(
            arguments.data,
            arguments.data_attribute_name,
            maya_node_name=arguments.maya_node_name,
            maya_attribute_name=arguments.maya_attribute_name,
            parent=parent,
        )

    def _require_window(self) -> BoolViewsWindow:
        """表示中のsample Windowを取得し、未生成ならerrorにする。"""
        # Python操作は表示中Windowが存在する場合だけ受け付ける。
        window = self._controller.window
        if window is None:
            raise RuntimeError("bool views sampleは表示されていません")
        return window


# 短いmodule-level APIで共有する既定Managerを1つだけ保持する。
_manager = BoolViewsWindowManager()


def show(
    data: object,
    data_attribute_name: str,
    *,
    maya_node_name: str | None = None,
    maya_attribute_name: str | None = None,
) -> BoolViewsWindow:
    """任意のPython bool attributeを編集するsample Windowを表示する。"""
    # 利用者向け関数から既定Managerへbinding設定を渡す。
    return _manager.show(
        data,
        data_attribute_name,
        maya_node_name=maya_node_name,
        maya_attribute_name=maya_attribute_name,
    )


def set_value(value: bool) -> bool:
    """表示中sampleのCommandをPythonから実行する。"""
    # 既定Managerが管理しているFeature Widgetへ値変更を渡す。
    return _manager.set_value(value)


def refresh_from_data() -> bool:
    """表示中sampleへPython objectの現在値を再反映する。"""
    # 既定Managerが管理しているPython Storeを再読込する。
    return _manager.refresh_from_data()


def dispose() -> None:
    """sample WindowとMaya callbackを完全に破棄する。"""
    # 既定Managerが所有するWindow lifecycleを終了する。
    _manager.dispose()
