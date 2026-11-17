# coding: utf-8
"""初回接続だけで消費する内部Storeの同期結果を共有する。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import cast


@dataclass(frozen=True)
class InitialStoreSnapshot:
    """外部通知前にまとめて取得した初回表示用の値と状態。"""

    available: bool
    value: object
    writable: bool
    metadata: object = None


class InitialSnapshotSource:
    """初期読取りの安全性を保証できる内部Storeだけの明示境界。"""

    def _take_initial_snapshot(self) -> InitialStoreSnapshot | None:
        """一回だけ使える初期状態を返し、保持中のsnapshotを失効する。"""
        raise NotImplementedError

    def _resync_initial_state(self) -> None:
        """初期通知から再入した場合に、集約状態も正本へ戻す。"""
        raise NotImplementedError

    @staticmethod
    def take(source: object) -> InitialStoreSnapshot | None:
        """実クラスが明示対応したStoreからだけ初期状態を消費する。"""
        if issubclass(type(source), InitialSnapshotSource):
            return cast(InitialSnapshotSource, source)._take_initial_snapshot()
        return None

    @staticmethod
    def resync(source: object) -> None:
        """対応Storeだけの初期再同期を内部境界から呼び出す。"""
        if issubclass(type(source), InitialSnapshotSource):
            cast(InitialSnapshotSource, source)._resync_initial_state()


def take_initial_snapshot(source: object) -> InitialStoreSnapshot | None:
    """明示対応したStoreだけから初回接続用の状態を一回消費する。"""
    return InitialSnapshotSource.take(source)


def resync_initial_state(source: object) -> None:
    """初期snapshotの外部通知後は、保持値を使わず集約状態を読む。"""
    InitialSnapshotSource.resync(source)
