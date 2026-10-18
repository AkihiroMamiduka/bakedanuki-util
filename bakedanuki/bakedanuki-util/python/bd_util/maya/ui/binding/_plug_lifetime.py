# coding: utf-8
"""値通知を同期せず、入力対象の削除履歴と復旧前の生存だけを確認する。"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Protocol

from maya.api import OpenMaya as om

from ....ui import qt
from ..._identity import ObjectIdentityIndex
from ..callback import MayaCallbackRegistry


class LifetimeTarget(Protocol):
    """値型に依存せず、属性と祖先の削除履歴を保持する対象。"""

    plug: om.MPlug
    watched: list[om.MPlug]
    removed: bool


class _Write(Protocol):
    """値の検証・適用・復旧だけを共有する書込み契約。"""

    def validate(self) -> None:
        """書込み条件を検証する。"""
        raise NotImplementedError

    def apply(self) -> None:
        """差分を適用する。"""
        raise NotImplementedError

    def restore(self) -> None:
        """適用前の状態へ復旧する。"""
        raise NotImplementedError


class PlugLifetime:
    """一時入力の間だけnode単位で削除を監視し、別実体へ追従しない。"""

    def __init__(self) -> None:
        """書込み中のBinding破棄から独立した監視ownerを用意する。"""
        self._owner = qt.QObject()
        self._registry = MayaCallbackRegistry(self._owner)
        self._indices = ObjectIdentityIndex()
        self._targets: dict[int, list[LifetimeTarget]] = {}

    def add(self, target: LifetimeTarget) -> None:
        """初期読取り前に対象を記録し、同じnodeの監視を共有する。"""
        identity = self._indices.index(target.plug.node())
        targets = self._targets.setdefault(identity, [])
        first = not targets
        targets.append(target)
        if first:
            self._registry.register(
                int(
                    om.MNodeMessage.addAttributeChangedCallback(
                        target.plug.node(), self._on_attribute_changed
                    )
                )
            )
            self._registry.register(
                int(
                    om.MNodeMessage.addNodePreRemovalCallback(
                        target.plug.node(), self._on_node_removed
                    )
                )
            )

    def _on_attribute_changed(
        self, message: int, plug: om.MPlug, _other: om.MPlug, _data: object
    ) -> None:
        """通常の値通知は処理せず、対象または祖先の削除だけを記録する。"""
        if not message & om.MNodeMessage.kAttributeRemoved:
            return
        identity = self._indices.index(plug.node())
        for target in self._targets.get(identity, ()):
            if not target.removed and any(
                plug == watched for watched in target.watched
            ):
                target.removed = True

    def _on_node_removed(self, node: om.MObject, *_args: object) -> None:
        """削除前の同じnodeに属する全対象を恒久的に無効化する。"""
        identity = self._indices.index(node)
        for target in self._targets.get(identity, ()):
            target.removed = True

    def close(self) -> None:
        """削除履歴を保持したまま監視を解除し、ownerの破棄を予約する。"""
        try:
            self._registry.dispose()
        finally:
            self._owner.deleteLater()


@dataclass
class LifetimeWrite:
    """削除済みMPlugへ触れず、共通の差分適用・復旧を呼ぶ。"""

    original: _Write
    require_available: Callable[[], None]
    attempted: bool = False

    def validate(self) -> None:
        """生存確認後に従来の事前検証を実行する。"""
        self.require_available()
        self.original.validate()

    def apply(self) -> None:
        """書込みを実際に試みた対象だけを復旧対象へ含める。"""
        self.require_available()
        self.attempted = True
        self.original.apply()

    def restore(self) -> None:
        """未試行を除き、削除された対象への書き戻しを明示的に拒否する。"""
        if not self.attempted:
            return
        self.require_available()
        self.original.restore()
