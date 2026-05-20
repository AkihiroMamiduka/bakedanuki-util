# coding: utf-8
from typing import TypeVar, Type, cast

# self
from .._core import Attr, Plug

A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Short2Plug(Plug[A]):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        return [
            self.plug.child(0).asShort(),
            self.plug.child(1).asShort(),
        ]

    # set
    def set(self, *value: int | list[int]):
        try:
            # set(x, y)
            try:
                self._node._dg_mod.newPlugValueShort(
                    self.plug.child(0), value[0]
                )
                self._node._dg_mod.newPlugValueShort(
                    self.plug.child(1), value[1]
                )
            # set([x, y])
            except Exception:
                self._node._dg_mod.newPlugValueShort(
                    self.plug.child(0), value[0][0]
                )
                self._node._dg_mod.newPlugValueShort(
                    self.plug.child(1), value[0][1]
                )
        except Exception as e:
            raise TypeError(
                f"Expected either set(x, y) or set([x, y]): {value}"
            ) from e


class Short2Attr(Attr[P]):
    __slots__ = ()

    ATTR_TYPE = "short2"
    PLUG_CLS = cast(Type[P], Short2Plug)
