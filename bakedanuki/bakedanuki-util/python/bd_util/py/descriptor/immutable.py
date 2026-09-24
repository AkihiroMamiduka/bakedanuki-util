# coding: utf-8
from typing import Any

# self
from ... import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class ImmutableDescriptor:
    """属性の再代入を禁止するデスクリプタの基底クラス。"""

    __slots__ = ("_name", "_owner", "_locked")

    def __init__(self) -> None:
        object.__setattr__(self, "_locked", False)

    def __set_name__(self, owner: type[Any], name: str) -> None:
        """所有クラスと属性名を記録し、初期化後に変更を禁止する。

        Args:
            owner: この属性を定義したクラス。
            name: クラスでの属性名。
        """
        # 変数に格納
        object.__setattr__(self, "_owner", owner)
        object.__setattr__(self, "_name", name)

        # 子クラスでの追加処理
        self._on_set_name(owner, name)

        # lock
        object.__setattr__(self, "_locked", True)

    def _on_set_name(self, owner: type[Any], name: str) -> None:
        """属性名を設定した後、サブクラス固有の処理を行う。

        Args:
            owner: この属性を定義したクラス。
            name: クラスでの属性名。
        """
        pass

    def __set__(self, instance: Any, value: Any) -> None:
        """インスタンス経由の代入を拒否する。

        Args:
            instance: 代入先のインスタンス。
            value: 代入しようとした値。

        Raises:
            AttributeError: デスクリプタへの代入を試みた場合。
        """
        # instance からの代入禁止
        raise AttributeError(
            "{}.{} descriptor は {}".format(
                self._owner.__name__,
                self._name,
                "immutable です。その為、変更することはできません。",
            )
        )

    def __setattr__(self, key: str, value: Any) -> None:
        """初期化後のデスクリプタ属性の変更を拒否する。

        Args:
            key: 変更する属性名。
            value: 設定する値。

        Raises:
            AttributeError: 初期化済みの属性を変更しようとした場合。
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
