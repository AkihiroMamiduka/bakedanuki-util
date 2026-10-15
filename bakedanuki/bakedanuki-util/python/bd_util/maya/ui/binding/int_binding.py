# coding: utf-8
from __future__ import annotations

from typing import TypeVar

from ....ui import (
    IntBinding,
    IntPresentation,
    IntValueStore,
    PythonIntAttributeStore,
    qt,
)
from .int_plug_resolver import MayaIntPlug
from .int_plug_view import MayaIntPlugView

_StoreT = TypeVar("_StoreT", bound=IntValueStore)
_InstanceT = TypeVar("_InstanceT")


class MayaIntBinding(IntBinding[_StoreT]):
    """Python正本の整数Storeと任意のMaya整数Viewを管理する。"""

    def __init__(
        self,
        store: _StoreT,
        *,
        maya_plug: MayaIntPlug | None = None,
        parent: qt.QObject | None = None,
    ) -> None:
        """Storeの確定値をMayaへ初期同期し、失敗時はcallbackを解除する。

        Args:
            store: Python側の正本となる整数Store。
            maya_plug: 同期先の既存属性。`None`ならQtとPythonだけを接続する。
            parent: Bindingの寿命を管理する所有者。
        """
        self._maya_view: MayaIntPlugView | None = None
        super().__init__(store, parent=parent)
        try:
            if maya_plug is not None:
                self._maya_view = MayaIntPlugView(
                    self.view_model, maya_plug, self
                )
        except Exception:
            self.dispose()
            raise

    @staticmethod
    def from_attribute(
        instance: _InstanceT,
        attribute_name: str,
        *,
        maya_plug: MayaIntPlug | None = None,
        presentation: IntPresentation | None = None,
        parent: qt.QObject | None = None,
    ) -> MayaIntBinding[PythonIntAttributeStore[_InstanceT]]:
        """既存Python整数属性を正本とし、任意のMaya属性へ同期する。

        Args:
            instance: 正本の属性を持つPython object。
            attribute_name: 正本として扱う既存属性の名前。
            maya_plug: Python初期値を適用するMaya属性。`None`なら未接続。
            presentation: Python側の入力範囲。`None`なら符号付き32-bit全域。
            parent: Bindingの寿命を管理する所有者。

        Returns:
            元のPython objectを具体型で保持するBinding。
        """
        return MayaIntBinding(
            PythonIntAttributeStore(
                instance, attribute_name, presentation=presentation
            ),
            maya_plug=maya_plug,
            parent=parent,
        )

    @property
    def maya_view(self) -> MayaIntPlugView | None:
        """Maya同期状態の窓口を返す。同期先未指定なら`None`。"""
        return self._maya_view

    def dispose(self) -> None:
        """Maya callbackを即座に解除してからBindingを終了する。"""
        try:
            if self._maya_view is not None and qt.isValid(self._maya_view):
                self._maya_view.dispose()
        finally:
            super().dispose()
