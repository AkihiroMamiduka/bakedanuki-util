# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ..._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


class Long2PlugOperator(PlugOperator[A]):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        return [
            self.plug.child(0).asInt(),
            self.plug.child(1).asInt(),
        ]

    # set
    def set(self, *value: int | list[int]):
        try:
            # set(x, y)
            try:
                self._node._dg_mod.newPlugValueInt(
                    self.plug.child(0), value[0]
                )
                self._node._dg_mod.newPlugValueInt(
                    self.plug.child(1), value[1]
                )
            # set([x, y])
            except Exception:
                self._node._dg_mod.newPlugValueInt(
                    self.plug.child(0), value[0][0]
                )
                self._node._dg_mod.newPlugValueInt(
                    self.plug.child(1), value[0][1]
                )
        except Exception as e:
            raise TypeError(
                f"Expected either set(x, y) or set([x, y]): {value}"
            ) from e


class Long2AttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "long2"


class Long2Field(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Long2AttrOperator)
    PLUG_CLS = cast(Type[P], Long2PlugOperator)
