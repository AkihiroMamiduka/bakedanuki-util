# coding: utf-8

from typing import Any, TypeVar, Type, cast, get_args, get_origin

# self
from ....define.std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)

P = TypeVar("P", bound="CompoundPlugOperator[Any]")


class ExtraCompoundField(CompoundField[CompoundAttrOperator[P], P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[CompoundAttrOperator[P]], CompoundAttrOperator)
    PLUG_CLS = cast(Type[P], CompoundPlugOperator)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)

        for base in getattr(cls, "__orig_bases__", ()):
            if get_origin(base) is ExtraCompoundField:
                args = get_args(base)
                if args:
                    setattr(cls, "PLUG_CLS", args[0])
                break
