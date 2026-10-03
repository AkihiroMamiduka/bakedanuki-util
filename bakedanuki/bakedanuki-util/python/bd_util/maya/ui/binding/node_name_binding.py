# coding: utf-8
from __future__ import annotations

from ....ui import StringBinding, StringViewModel, qt
from ...node.operator.node._core import NodeOperator
from .node_name import MayaNodeNameStore


class MayaNodeNameBinding(StringBinding[MayaNodeNameStore]):
    """単一ノード名を正本とするStoreと共通StringViewModelを所有する。"""

    def __init__(
        self,
        node: NodeOperator,
        *,
        parent: qt.QObject | None = None,
        rename_shapes: bool = True,
    ) -> None:
        """既存ノードを固定し、書込みなしで現在名を読み込む。

        Args:
            node: シーン上に存在する対象ノード。
            parent: Bindingとcallbackの寿命を所有するQObject。
            rename_shapes: Transformに従うShapeの改名を有効にするか。
        """
        self._owned_store: MayaNodeNameStore | None = None

        def create_store(view_model: StringViewModel) -> MayaNodeNameStore:
            """専用ViewModelへ接続するノード名Storeを生成する。"""
            store = MayaNodeNameStore(
                view_model, node, self, rename_shapes=rename_shapes
            )
            self._owned_store = store
            return store

        self._initialize(create_store, parent=parent)

    def set_value(self, value: str) -> bool:
        """現在の編集可否を再確認して改名し、実変更の有無を返す。

        ロック解除や外部の名前空間変更を反映してから入力する。
        入力が不正な場合やMayaでの改名失敗は例外として通知する。
        """
        self.refresh()
        return super().set_value(value)

    def dispose(self) -> None:
        """Maya callbackを先に解除し、共有するViewを編集停止にする。"""
        try:
            store = self._owned_store
            if store is not None and qt.isValid(store):
                store.dispose()
        finally:
            super().dispose()
