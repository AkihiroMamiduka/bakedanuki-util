# coding: utf-8
from typing import Any

# self
from ... import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class ImmutableDescriptor:
    __slots__ = ("_name", "_owner", "_locked")

    def __init__(self):
        object.__setattr__(self, "_locked", False)

    def __set_name__(self, owner, name: str):
        """
        class 定義時に 1 回だけ呼ばれる
        親クラスでセットされた、クラス変数名を受け取る仕組み

        Args:
            owner (any): 親クラス
            name (str): 親クラスでセットされた、クラス変数名
        """
        # 変数に格納
        object.__setattr__(self, "_owner", owner)
        object.__setattr__(self, "_name", name)

        # 子クラスでの追加処理
        self._on_set_name(owner, name)

        # lock
        object.__setattr__(self, "_locked", True)

    def _on_set_name(self, owner: Any, name: str):
        """
        __set_name__ 内での、子クラスの追加処理

        Args:
            owner (Any): 親クラス
            name (str): 親クラスでセットされた、クラス変数名
        """
        pass

    def __set__(self, instance: Any, value: Any):
        """
        代入処理
        このクラスへは、代入を禁止する

        Args:
            instance (Any): インスタンス
            value (Any): 値

        Raises:
            AttributeError: 代入を禁止する為、エラーを返す
        """
        # instance からの代入禁止
        raise AttributeError(
            "{}.{} descriptor は {}".format(
                self._owner.__name__,
                self._name,
                "immutable です。その為、変更することはできません。",
            )
        )

    def __setattr__(self, key: Any, value: Any):
        """
        代入処理
        このクラスへは、代入を禁止する

        Args:
            key (Any): 属性名
            value (Any): 値

        Raises:
            AttributeError: 代入を禁止する為、エラーを返す
        """
        # descriptor 自体の変更禁止
        if getattr(self, "_locked", False):
            raise AttributeError(
                "{}.{} descriptor は {}".format(
                    self._owner.__name__,
                    self._name,
                    "immutable です。その為、変更することはできません。",
                )
            )
        object.__setattr__(self, key, value)
