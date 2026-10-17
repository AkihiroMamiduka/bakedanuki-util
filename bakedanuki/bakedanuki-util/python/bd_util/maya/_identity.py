# coding: utf-8
"""hashの衝突を実体比較で解決する、処理中だけのMaya実体索引。"""

from maya.api import OpenMaya as om


def _object_hash(node: om.MObject) -> int:
    """名前やDAGパスに依存しない実体の候補キーを返す。"""
    return int(om.MObjectHandle(node).hashCode())


class ObjectIdentityIndex:
    """MObjectの初出順を保ち、同じ実体へ同じ連番を割り当てる。"""

    def __init__(self) -> None:
        """同期処理中に使うhash別の実体と連番を初期化する。"""
        self._buckets: dict[int, list[tuple[om.MObject, int]]] = {}
        self._count = 0

    def index(self, node: om.MObject) -> int:
        """既出の実体は同じ連番を返し、初出なら末尾へ登録する。"""
        bucket = self._buckets.setdefault(_object_hash(node), [])
        for previous, index in bucket:
            if node == previous:
                return index
        index = self._count
        bucket.append((node, index))
        self._count += 1
        return index


class PlugIdentitySet:
    """node・属性のhashで候補を絞り、MPlugの実体で重複を判定する。"""

    def __init__(self) -> None:
        """同じhashを持つ異なるplugも保持する索引を用意する。"""
        self._buckets: dict[tuple[int, int], list[om.MPlug]] = {}

    def add(self, plug: om.MPlug) -> bool:
        """初出なら登録してTrue、同じplugが既にあればFalseを返す。"""
        key = (_object_hash(plug.node()), _object_hash(plug.attribute()))
        bucket = self._buckets.setdefault(key, [])
        if any(plug == previous for previous in bucket):
            return False
        bucket.append(plug)
        return True
