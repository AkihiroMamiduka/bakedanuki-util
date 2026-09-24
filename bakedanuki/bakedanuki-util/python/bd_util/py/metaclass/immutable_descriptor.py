# coding: utf-8
from typing import Any

# self
from ... import logger as u_logger
from ..cls import attr as u_py_cls_attr
from ..descriptor.immutable import ImmutableDescriptor

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class ImmutableDescriptorMeta(type):
    """``ImmutableDescriptor`` を持つクラス属性の上書きを防ぐ。"""

    def __setattr__(cls, name: str, value: Any) -> None:
        """デスクリプタのクラス属性を上書きせずに属性を設定する。

        Args:
            name: 設定する属性名。
            value: 設定する値。

        Raises:
            AttributeError: 既存の ``ImmutableDescriptor`` を上書きする場合。
        """
        attribute = u_py_cls_attr.find_attr(cls, name)

        # アトリビュートが ImmutableDescriptor 型であれば、例外を送出する
        if isinstance(attribute, ImmutableDescriptor):
            raise AttributeError(
                f"{cls.__name__}.{name} は immutable descriptor のため上書きできません"
            )

        super().__setattr__(name, value)

    def __delattr__(cls, name: str) -> None:
        """デスクリプタのクラス属性を削除せずに属性を削除する。

        Args:
            name: 削除する属性名。

        Raises:
            AttributeError: 既存の ``ImmutableDescriptor`` を削除する場合。
        """
        attribute = u_py_cls_attr.find_attr(cls, name)

        # アトリビュートが ImmutableDescriptor 型であれば、例外を送出する
        if isinstance(attribute, ImmutableDescriptor):
            raise AttributeError(
                f"{cls.__name__}.{name} は immutable descriptor のため削除できません"
            )

        super().__delattr__(name)
