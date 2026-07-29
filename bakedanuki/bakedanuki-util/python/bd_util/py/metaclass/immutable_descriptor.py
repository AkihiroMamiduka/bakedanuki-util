# coding: utf-8
from typing import Any

# self
from ... import logger as u_logger
from ..cls import attr as u_py_cls_attr
from ..descriptor.immutable import ImmutableDescriptor

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class ImmutableDescriptorMeta(type):
    """
    変更不可能な descriptor
    """

    def __setattr__(cls, name: str, value: Any) -> None:
        """
        属性へのセット
        ImmutableDescriptor 型への変更は、禁止する

        Args:
            name (str): 属性名
            value (Any): 値

        Raises:
            AttributeError: ImmutableDescriptor 型は変更を禁止したい為、エラーを返す
        """
        attribute = u_py_cls_attr.find_attr(cls, name)

        # アトリビュートが ImmutableDescriptor 型であれば、例外を送出する
        if isinstance(attribute, ImmutableDescriptor):
            raise AttributeError(
                f"{cls.__name__}.{name} は immutable descriptor のため上書きできません"
            )

        super().__setattr__(name, value)

    def __delattr__(cls, name: str) -> None:
        """
        属性削除
        ImmutableDescriptor 型の削除は、禁止する

        Args:
            name (str): 属性名

        Raises:
            AttributeError: ImmutableDescriptor 型は削除を禁止したい為、エラーを返す
        """
        attribute = u_py_cls_attr.find_attr(cls, name)

        # アトリビュートが ImmutableDescriptor 型であれば、例外を送出する
        if isinstance(attribute, ImmutableDescriptor):
            raise AttributeError(
                f"{cls.__name__}.{name} は immutable descriptor のため削除できません"
            )

        super().__delattr__(name)
