# coding: utf-8
from typing import Any

# self
from ... import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def find_attr(obj: Any, name: str) -> Any | None:
    """クラスの継承階層から属性の定義値を探す。

    Args:
        obj: 検索するクラスまたはインスタンス。
        name: 属性名。

    Returns:
        クラスの ``__dict__`` にある定義値。見つからなければ ``None``。
    """
    if isinstance(obj, type):
        mro = obj.__mro__
    else:
        mro = type(obj).__mro__

    for cls in mro:
        if name in cls.__dict__:
            return cls.__dict__[name]

    return None
