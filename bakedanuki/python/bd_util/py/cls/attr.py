# coding: utf-8
from typing import Any

# self
from ... import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def find_attr(obj: Any, name: str) -> Any | None:
    """
    指定された名前の属性をクラス内から探して返す

    Args:
        obj (any): class または instance
        name (str): 属性名

    Returns:
        any: 属性
    """
    if isinstance(obj, type):
        mro = obj.__mro__
    else:
        mro = type(obj).__mro__

    for cls in mro:
        if name in cls.__dict__:
            return cls.__dict__[name]

    return None
