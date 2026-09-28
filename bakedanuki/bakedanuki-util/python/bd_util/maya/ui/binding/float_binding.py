# coding: utf-8
from __future__ import annotations

from typing import TypeVar

from ....ui import (
    FloatBinding,
    FloatPresentation,
    FloatValueStore,
    PythonFloatAttributeStore,
    qt,
)
from .float_plug_resolver import MayaFloatPlug
from .float_plug import MayaFloatPlugView

_StoreT = TypeVar("_StoreT", bound=FloatValueStore)
_InstanceT = TypeVar("_InstanceT")


class MayaFloatBinding(FloatBinding[_StoreT]):
    """Python 正本の Store と任意の Maya float View を一組だけ管理する。"""

    def __init__(
        self,
        store: _StoreT,
        *,
        maya_plug: MayaFloatPlug | None = None,
        parent: qt.QObject | None = None,
    ) -> None:
        """`store` と任意の Maya plug を接続する。初期同期失敗時は callback を解除する。

        Args:
            store: Python 側の正本となる数値 Store。
            maya_plug: 同期先の Maya float plug。`None` なら Maya View を作らない。
            parent: この `MayaFloatBinding` を所有する `QObject`。
        """
        self._maya_view: MayaFloatPlugView | None = None
        super().__init__(store, parent=parent)
        try:
            if maya_plug is not None:
                self._maya_view = MayaFloatPlugView(
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
        maya_plug: MayaFloatPlug | None = None,
        presentation: FloatPresentation | None = None,
        parent: qt.QObject | None = None,
    ) -> MayaFloatBinding[PythonFloatAttributeStore[_InstanceT]]:
        """Python 属性を正本とし、任意の Maya plug へ同期する。

        Args:
            instance: 正本の属性を持つ Python object。
            attribute_name: 正本として扱う既存属性の名前。
            maya_plug: 同期先の Maya float plug。`None` なら Maya View を作らない。
            presentation: 公開単位から表示単位への変換と入力範囲。`None` なら既定の `FloatPresentation`。
            parent: この `MayaFloatBinding` を所有する `QObject`。

        Returns:
            Python 属性 Store を持つ `MayaFloatBinding`。
        """
        return MayaFloatBinding(
            PythonFloatAttributeStore(
                instance, attribute_name, presentation=presentation
            ),
            maya_plug=maya_plug,
            parent=parent,
        )

    @property
    def maya_view(self) -> MayaFloatPlugView | None:
        """Maya 同期状態を持つ View を返す。`maya_plug` 未指定なら `None`。"""
        return self._maya_view

    def dispose(self) -> None:
        """Maya callbackを即座に解放してからBindingを終了する。"""
        try:
            if self._maya_view is not None and qt.isValid(self._maya_view):
                self._maya_view.dispose()
        finally:
            super().dispose()
