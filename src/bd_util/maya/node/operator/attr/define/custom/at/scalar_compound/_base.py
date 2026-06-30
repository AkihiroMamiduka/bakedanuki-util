# coding: utf-8
from collections.abc import Sequence
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ......... import logger as u_logger
from ....._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class ScalarCompoundBasePlugOperator(PlugOperator[A]):
    __slots__ = ()

    CHILD_M_FN = None
    CHILD_M_ATTR_TYPE: int = None
    _SUFFIXES: tuple[str, ...] = ()
    CHILD_FIELDS: tuple[AttributeField, ...] = ()
    CHILD_ATTR_NAMES: tuple[tuple[str, str], ...] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        suffixes = []
        child_fields = []
        seen_ids = set()

        # 子属性の情報を取得
        for key, child_field in vars(cls).items():
            # AttributeField の派生以外はスキップ
            if not isinstance(child_field, AttributeField):
                continue
            child_id = id(child_field)
            if child_id in seen_ids:
                continue
            seen_ids.add(child_id)
            # 子に関する情報を登録
            #   suffix
            suffixes.append(key)
            child_fields.append(child_field)

        if suffixes:
            cls._SUFFIXES = tuple(suffixes)
            cls.CHILD_FIELDS = tuple(child_fields)
        else:
            cls._SUFFIXES = tuple(getattr(cls, "_SUFFIXES", ()))
            cls.CHILD_FIELDS = tuple(getattr(cls, "CHILD_FIELDS", ()))

        child_attr_names = tuple(getattr(cls, "CHILD_ATTR_NAMES", ()))
        if child_attr_names and len(child_attr_names) != len(cls._SUFFIXES):
            raise ValueError(
                "{}.CHILD_ATTR_NAMES must match child field count: {} != {}".format(
                    cls.__name__,
                    len(child_attr_names),
                    len(cls._SUFFIXES),
                )
            )
        cls.CHILD_ATTR_NAMES = child_attr_names

    # get
    def _get_child_value(self, child_plug) -> float:
        pass

    def get(self) -> list[float]:
        return [
            self._get_child_value(self.plug.child(i))
            for i in range(len(self._SUFFIXES))
        ]

    # set
    def _set_child_value(self, child_plug, value: float):
        pass

    def _set_values_error(self, values) -> TypeError:
        suffix_str = ", ".join(self._SUFFIXES)
        return TypeError(
            "Expected either set({}) or set([{}]): {}".format(
                suffix_str,
                suffix_str,
                values,
            )
        )

    def _normalize_set_values(self, values) -> tuple:
        if len(values) == 1:
            value = values[0]
            if isinstance(value, Sequence) and not isinstance(
                value, (str, bytes)
            ):
                values = tuple(value)
        if len(values) != len(self._SUFFIXES):
            raise self._set_values_error(values)
        return tuple(values)

    def set(self, *values: float | Sequence[float]):
        values = self._normalize_set_values(values)
        plug = self.plug
        try:
            # 値をセットする
            for i, val in enumerate(values):
                self._set_child_value(plug.child(i), val)

        except Exception as e:
            raise self._set_values_error(values) from e

    # add
    def _child_value(self, value, index: int, default=None):
        if value is None:
            return default
        if isinstance(value, Sequence) and not isinstance(value, str):
            if len(value) != len(self._SUFFIXES):
                raise ValueError(
                    "{} must match child field count: {} != {}".format(
                        value,
                        len(value),
                        len(self._SUFFIXES),
                    )
                )
            return value[index]
        return value

    def _prepare_child_default_value(self, value):
        return value

    def _prepare_child_limit_value(self, value):
        return value

    def _set_child_attr_min(self, child_fn, value):
        if value is None:
            return
        child_fn.setMin(self._prepare_child_limit_value(value))

    def _set_child_attr_max(self, child_fn, value):
        if value is None:
            return
        child_fn.setMax(self._prepare_child_limit_value(value))

    def _set_child_attr_soft_min(self, child_fn, value):
        if value is None:
            return
        child_fn.setSoftMin(self._prepare_child_limit_value(value))

    def _set_child_attr_soft_max(self, child_fn, value):
        if value is None:
            return
        child_fn.setSoftMax(self._prepare_child_limit_value(value))

    def _child_fn(self, index: int):
        return self.CHILD_M_FN(self.plug.child(index).attribute())

    def set_min(self, value):
        for i in range(len(self._SUFFIXES)):
            self._set_child_attr_min(
                self._child_fn(i),
                self._child_value(value, i),
            )

    def set_max(self, value):
        for i in range(len(self._SUFFIXES)):
            self._set_child_attr_max(
                self._child_fn(i),
                self._child_value(value, i),
            )

    def set_soft_min(self, value):
        for i in range(len(self._SUFFIXES)):
            self._set_child_attr_soft_min(
                self._child_fn(i),
                self._child_value(value, i),
            )

    def set_soft_max(self, value):
        for i in range(len(self._SUFFIXES)):
            self._set_child_attr_soft_max(
                self._child_fn(i),
                self._child_value(value, i),
            )

    def _resolve_child_name_index(
        self, suffix: str, index: int | None
    ) -> int | None:
        if index is not None:
            return index
        try:
            return self._SUFFIXES.index(suffix)
        except ValueError:
            return None

    def child_long_name(self, suffix: str, index: int | None = None) -> str:
        index = self._resolve_child_name_index(suffix, index)
        if self.CHILD_ATTR_NAMES and index is not None:
            return self.CHILD_ATTR_NAMES[index][0]
        return f"{self.long_name}{suffix.upper()}"

    def child_short_name(self, suffix: str, index: int | None = None) -> str:
        index = self._resolve_child_name_index(suffix, index)
        if self.CHILD_ATTR_NAMES and index is not None:
            return self.CHILD_ATTR_NAMES[index][1]
        return f"{self.short_name}{suffix.lower()}"

    def add_attr(self):
        def _create_child_attr(
            suffix: str,
            index: int,
        ) -> om.MObject:
            # 子属性を作成
            child_fn = self.CHILD_M_FN()
            default_value = self._child_value(
                self._oprt_attr.default_value,
                index,
                default=0,
            )
            child_attr = child_fn.create(
                self.child_long_name(suffix),
                self.child_short_name(suffix),
                self.CHILD_M_ATTR_TYPE,
                self._prepare_child_default_value(default_value),
            )

            return child_attr

        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # アトリビュートを作成
        #   子属性
        children_attrs = []
        for i, suffix in enumerate(self._SUFFIXES):
            children_attrs.append(_create_child_attr(suffix, i))
        #   親属性(double3)
        fn_attr = om.MFnNumericAttribute()
        self._fn_attr = fn_attr
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
            *children_attrs,
        )

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)

        v = self._oprt_attr.min_value
        if v is not None:
            self.set_min(v)

        v = self._oprt_attr.max_value
        if v is not None:
            self.set_max(v)

        v = self._oprt_attr.soft_min_value
        if v is not None:
            self.set_soft_min(v)

        v = self._oprt_attr.soft_max_value
        if v is not None:
            self.set_soft_max(v)


class ScalarCompoundBaseAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "abc"


class ScalarCompoundBaseField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], ScalarCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], ScalarCompoundBasePlugOperator)
