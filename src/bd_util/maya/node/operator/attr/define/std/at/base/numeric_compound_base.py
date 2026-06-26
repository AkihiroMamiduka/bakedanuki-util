# coding: utf-8
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ......... import logger as u_logger
from ....._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class NumericCompoundBasePlugOperator(PlugOperator[A]):
    __slots__ = ()

    CHILD_ATTR_TYPE: int = None
    CHILD_FN = None
    _SUFFIXES: list[str] = []
    CHILD_FIELDS: list[AttributeField] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ファンクションを作成
        self._fn_attr: om.MFnNumericAttribute = om.MFnNumericAttribute()

        for suffix, child_field in zip(self._SUFFIXES, self.CHILD_FIELDS):
            child_long_name = self.child_long_name(suffix)
            object.__setattr__(child_field, "long_name", child_long_name)
            object.__setattr__(
                child_field, "_short_name", self.child_short_name(suffix)
            )

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        state_suffix = bool(cls._SUFFIXES)
        child_state = cls.CHILD_ATTR_TYPE is None
        child_type = None
        child_fn = None

        # 子属性の情報を取得
        for key, child_field in vars(cls).items():
            # AttributeField の派生以外はスキップ
            if all(
                c.__name__ != "AttributeField"
                for c in type(child_field).__mro__
            ):
                continue
            # 子に関する情報を登録
            #   suffix
            if not state_suffix:
                cls._SUFFIXES.append(key)
                cls.CHILD_FIELDS.append(child_field)
            #   子の型
            if child_state:
                child_type = child_field.M_ATTR_TYPE
                child_fn = child_field.M_FN
        # 子属性の型を登録
        cls.CHILD_ATTR_TYPE = child_type
        cls.CHILD_FN = child_fn

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

    def set(self, *values: float | list[float]):
        try:
            # list で渡された場合は、展開する
            if isinstance(values[0], list):
                values = values[0]
            # 値をセットする
            for i, val in enumerate(values):
                self._set_child_value(self.plug.child(i), val)

        except Exception as e:
            suffix_str = ", ".join(self._SUFFIXES)
            raise TypeError(
                "Expected either set({}) or set([{}]): {}".format(
                    suffix_str, suffix_str, values
                )
            ) from e

    # add
    def child_long_name(self, suffix: str) -> str:
        return f"{self.long_name}{suffix.upper()}"

    def child_short_name(self, suffix: str) -> str:
        return f"{self.short_name}{suffix.lower()}"

    def add_attr(self):
        def _create_child_attr(
            suffix: str,
        ) -> om.MObject:
            # 子属性を作成
            child_fn = self.CHILD_FN()
            child_attr = child_fn.create(
                self.child_long_name(suffix),
                self.child_short_name(suffix),
                self.CHILD_ATTR_TYPE,
                0.0,
            )

            return child_attr

        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # アトリビュートを作成
        #   子属性
        children_attrs = []
        for suffix in self._SUFFIXES:
            children_attrs.append(_create_child_attr(suffix))
        #   親属性(double3)
        attr_obj = self._fn_attr.create(
            self.long_name,
            self.short_name,
            *children_attrs,
        )

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)


class NumericCompoundBaseAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "abc"


class NumericCompoundBaseField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], NumericCompoundBaseAttrOperator)
    PLUG_CLS = cast(Type[P], NumericCompoundBasePlugOperator)
