# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ..._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


class Short3PlugOperator(PlugOperator[A]):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        return [
            self.plug.child(0).asShort(),
            self.plug.child(1).asShort(),
            self.plug.child(2).asShort(),
        ]

    # set
    def set(self, *value: int | list[int]):
        try:
            # set(x, y, z)
            try:
                self._node._dg_mod.newPlugValueShort(
                    self.plug.child(0), value[0]
                )
                self._node._dg_mod.newPlugValueShort(
                    self.plug.child(1), value[1]
                )
                self._node._dg_mod.newPlugValueShort(
                    self.plug.child(2), value[2]
                )
            # set([x, y, z])
            except Exception:
                self._node._dg_mod.newPlugValueShort(
                    self.plug.child(0), value[0][0]
                )
                self._node._dg_mod.newPlugValueShort(
                    self.plug.child(1), value[0][1]
                )
                self._node._dg_mod.newPlugValueShort(
                    self.plug.child(2), value[0][2]
                )
        except Exception as e:
            raise TypeError(
                f"Expected either set(x, y, z) or set([x, y, z]): {value}"
            ) from e


class Short3AttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "short3"


class Short3Field(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Short3AttrOperator)
    PLUG_CLS = cast(Type[P], Short3PlugOperator)
