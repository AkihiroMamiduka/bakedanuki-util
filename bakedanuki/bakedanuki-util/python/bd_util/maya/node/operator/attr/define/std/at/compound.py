# coding: utf-8
from collections.abc import Callable
from typing import Any, Never, TypeVar, Type, cast, Protocol

# self
from ...._core import AttrOperator, PlugOperator, AttributeField
from ........py.error import UnsupportedOperationError

# maya
from maya.api import OpenMaya as om

A = TypeVar("A", bound="AttrOperator[Any]")

P = TypeVar("P", bound="PlugOperator[Any]")


class _CompoundAttrParent(Protocol):

    @property
    def node(self) -> Any: ...

    @property
    def oprt_attr(self) -> AttrOperator[Any]: ...

    @property
    def attr_path(self) -> str: ...


class _ScalarCompoundPlugAdapter:
    __slots__ = ("plug",)

    def __init__(self, plug: PlugOperator[Any]) -> None:
        self.plug = plug

    @property
    def suffixes(self) -> tuple[str, ...]:
        return cast(tuple[str, ...], getattr(self.plug, "_SUFFIXES"))

    @property
    def child_attr_type(self) -> int:
        return cast(int, getattr(self.plug, "CHILD_M_ATTR_TYPE"))

    def create_child_fn(self) -> Any:
        child_fn_cls = cast(
            Callable[[], Any],
            getattr(self.plug, "CHILD_M_FN"),
        )
        return child_fn_cls()

    def child_value(
        self,
        value: Any,
        index: int,
        default: Any = None,
    ) -> Any:
        get_child_value = cast(
            Callable[[Any, int, Any], Any],
            getattr(self.plug, "_child_value"),
        )
        return get_child_value(value, index, default)

    def prepare_child_default_value(self, value: Any) -> Any:
        prepare = cast(
            Callable[[Any], Any],
            getattr(self.plug, "_prepare_child_default_value"),
        )
        return prepare(value)

    def apply_child_limit(
        self,
        method_name: str,
        child_fn: Any,
        value: Any,
    ) -> None:
        setter = cast(
            Callable[[Any, Any], None],
            getattr(self.plug, method_name),
        )
        setter(child_fn, value)

    def child_long_name(self, suffix: str, index: int) -> str:
        get_name = cast(
            Callable[[str, int | None], str],
            getattr(self.plug, "child_long_name"),
        )
        return get_name(suffix, index)

    def child_short_name(self, suffix: str, index: int) -> str:
        get_name = cast(
            Callable[[str, int | None], str],
            getattr(self.plug, "child_short_name"),
        )
        return get_name(suffix, index)


class CompoundPlugOperator(PlugOperator[A]):
    __slots__ = ()

    CHILD_FIELDS: tuple[AttributeField[Any, Any], ...] = ()

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)

        child_fields: list[AttributeField[Any, Any]] = []
        seen_ids: set[int] = set()
        for child_field in vars(cls).values():
            if not isinstance(child_field, AttributeField):
                continue
            child_field = cast(AttributeField[Any, Any], child_field)
            child_id = id(child_field)
            if child_id in seen_ids:
                continue
            seen_ids.add(child_id)
            child_fields.append(child_field)

        if child_fields:
            cls.CHILD_FIELDS = tuple(child_fields)
        else:
            cls.CHILD_FIELDS = tuple(getattr(cls, "CHILD_FIELDS", ()))

    # get
    def get(self) -> Never:
        raise NotImplementedError(
            "CompoundPlug does not support get operation"
        )

    # set
    def set(self, value: Any) -> Never:
        raise NotImplementedError(
            "CompoundPlug does not support set operation"
        )

    # add
    def add_attr(self):
        if self.exists():
            return

        child_fields = self.CHILD_FIELDS
        if not child_fields:
            raise UnsupportedOperationError(
                f"{type(self).__name__} must define child fields."
            )

        fn_attr = om.MFnCompoundAttribute()
        self._fn_attr = fn_attr
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
        )

        for child_field in child_fields:
            fn_attr.addChild(_create_child_attr(self, child_field))

        self._apply_mfn_attr_options(fn_attr)
        self._node.fn_node.addAttribute(attr_obj)


class CompoundAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "compound"


class CompoundField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], CompoundAttrOperator)
    PLUG_CLS = cast(Type[P], CompoundPlugOperator)


_NUMERIC_ATTR_TYPES = {
    "bool": om.MFnNumericData.kBoolean,
    "byte": om.MFnNumericData.kByte,
    "char": om.MFnNumericData.kChar,
    "short": om.MFnNumericData.kShort,
    "long": om.MFnNumericData.kLong,
    "long long int": om.MFnNumericData.kInt64,
    "float": om.MFnNumericData.kFloat,
    "double": om.MFnNumericData.kDouble,
}

_UNIT_ATTR_TYPES = {
    "doubleAngle": om.MFnUnitAttribute.kAngle,
    "doubleLinear": om.MFnUnitAttribute.kDistance,
    "time": om.MFnUnitAttribute.kTime,
}

_MATRIX_ATTR_TYPES = {
    "matrix": om.MFnMatrixAttribute.kDouble,
    "fltMatrix": om.MFnMatrixAttribute.kFloat,
}


def _create_child_attr(
    parent: _CompoundAttrParent,
    child_field: AttributeField[Any, Any],
) -> om.MObject:
    child_attr = _create_child_attr_operator(parent, child_field)
    attr_type = child_attr.ATTR_TYPE

    if attr_type in _NUMERIC_ATTR_TYPES:
        return _create_numeric_attr(child_attr)

    if attr_type in _UNIT_ATTR_TYPES:
        return _create_unit_attr(child_attr)

    if attr_type in _MATRIX_ATTR_TYPES:
        return _create_matrix_attr(child_attr)

    if _is_scalar_compound_field(child_field):
        return _create_scalar_compound_attr(child_field, child_attr, parent)

    if attr_type == "enum":
        return _create_enum_attr(child_field, child_attr)

    if attr_type == "message":
        return _create_message_attr(child_attr)

    if attr_type == "compound":
        return _create_compound_attr(child_field, child_attr, parent)

    raise UnsupportedOperationError(
        "{} child '{}' attribute type '{}' is not supported by "
        "OpenMaya compound add_attr().".format(
            type(parent).__name__,
            child_attr.long_name,
            attr_type,
        )
    )


def _create_child_attr_operator(
    parent: _CompoundAttrParent,
    child_field: AttributeField[Any, Any],
) -> AttrOperator[Any]:
    attr_cls = child_field.ATTR_CLS
    if attr_cls is None:
        raise TypeError(
            f"{type(child_field).__name__}.ATTR_CLS is not defined."
        )

    long_name = child_field.long_name
    short_name = child_field.short_name
    if long_name is None or short_name is None:
        raise RuntimeError(
            "{} is not initialized as a class attribute.".format(
                type(child_field).__name__
            )
        )

    parent_attr_path = parent.attr_path
    attr_path = f"{parent_attr_path}.{long_name}"
    return attr_cls(
        node_cls=parent.oprt_attr.node_cls,
        oprt_parent=parent,
        name=child_field.name,
        long_name=long_name,
        short_name=short_name,
        attr_path=attr_path,
        parent_attr_path=parent_attr_path,
        multi=child_field.multi,
        extra=False,
        default_value=child_field.default_value,
        min_value=child_field.min_value,
        max_value=child_field.max_value,
        soft_min_value=child_field.soft_min_value,
        soft_max_value=child_field.soft_max_value,
        enum_name=child_field.enum_name,
        number_of_children=child_field.number_of_children,
        readable=child_field.readable,
        writable=child_field.writable,
        category=child_field.category,
        child_index=child_field.child_index,
    )


def _plug_cls_or_raise(
    child_field: AttributeField[Any, Any],
) -> type[PlugOperator[Any]]:
    plug_cls = child_field.PLUG_CLS
    if plug_cls is None:
        raise TypeError(
            f"{type(child_field).__name__}.PLUG_CLS is not defined."
        )
    return plug_cls


def _attr_type_or_raise(attr: AttrOperator[Any]) -> str:
    attr_type = attr.ATTR_TYPE
    if attr_type is None:
        raise TypeError(f"{type(attr).__name__}.ATTR_TYPE is not defined.")
    return attr_type


def _apply_mfn_attr_options(
    fn_attr: om.MFnAttribute,
    attr: AttrOperator[Any],
) -> None:
    if attr.multi:
        fn_attr.array = True

    if attr.readable is not None:
        fn_attr.readable = attr.readable

    if attr.writable is not None:
        fn_attr.writable = attr.writable

    if attr.category is not None:
        fn_attr.addToCategory(attr.category)


def _apply_numeric_range_options(
    fn_attr: Any,
    attr: AttrOperator[Any],
) -> None:
    if attr.min_value is not None:
        fn_attr.setMin(attr.min_value)
    if attr.max_value is not None:
        fn_attr.setMax(attr.max_value)
    if attr.soft_min_value is not None:
        fn_attr.setSoftMin(attr.soft_min_value)
    if attr.soft_max_value is not None:
        fn_attr.setSoftMax(attr.soft_max_value)


def _create_numeric_attr(attr: AttrOperator[Any]) -> om.MObject:
    fn_attr = om.MFnNumericAttribute()
    attr_type = _attr_type_or_raise(attr)
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
        _NUMERIC_ATTR_TYPES[attr_type],
        attr.default_value,
    )
    _apply_mfn_attr_options(fn_attr, attr)
    _apply_numeric_range_options(fn_attr, attr)
    return attr_obj


def _create_unit_attr(attr: AttrOperator[Any]) -> om.MObject:
    fn_attr = om.MFnUnitAttribute()
    attr_type = _attr_type_or_raise(attr)
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
        _UNIT_ATTR_TYPES[attr_type],
        attr.default_value,
    )
    _apply_mfn_attr_options(fn_attr, attr)
    _apply_numeric_range_options(fn_attr, attr)
    return attr_obj


def _create_matrix_attr(attr: AttrOperator[Any]) -> om.MObject:
    fn_attr = om.MFnMatrixAttribute()
    attr_type = _attr_type_or_raise(attr)
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
        _MATRIX_ATTR_TYPES[attr_type],
    )
    _apply_mfn_attr_options(fn_attr, attr)
    return attr_obj


def _is_scalar_compound_field(
    child_field: AttributeField[Any, Any],
) -> bool:
    plug_cls = child_field.PLUG_CLS
    if plug_cls is None:
        return False
    return (
        getattr(plug_cls, "CHILD_M_FN", None) is not None
        and getattr(plug_cls, "CHILD_M_ATTR_TYPE", None) is not None
        and bool(getattr(plug_cls, "_SUFFIXES", ()))
        and bool(getattr(plug_cls, "CHILD_FIELDS", ()))
    )


def _create_scalar_compound_attr(
    child_field: AttributeField[Any, Any],
    attr: AttrOperator[Any],
    parent: _CompoundAttrParent,
) -> om.MObject:
    plug_cls = _plug_cls_or_raise(child_field)
    scalar_plug = _ScalarCompoundPlugAdapter(
        plug_cls(
            node=parent.node,
            oprt_attr=attr,
            parent_attr_path=parent.attr_path,
            multi=attr.multi,
        )
    )

    children_attrs: list[om.MObject] = []
    for i, suffix in enumerate(scalar_plug.suffixes):
        child_fn = scalar_plug.create_child_fn()
        default_value = scalar_plug.child_value(
            attr.default_value,
            i,
            default=0,
        )
        child_attr = child_fn.create(
            scalar_plug.child_long_name(suffix, i),
            scalar_plug.child_short_name(suffix, i),
            scalar_plug.child_attr_type,
            scalar_plug.prepare_child_default_value(default_value),
        )
        _apply_scalar_compound_child_limits(child_fn, scalar_plug, attr, i)
        children_attrs.append(child_attr)

    fn_attr = om.MFnNumericAttribute()
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
        *children_attrs,
    )
    _apply_mfn_attr_options(fn_attr, attr)
    return attr_obj


def _apply_scalar_compound_child_limits(
    child_fn: Any,
    scalar_plug: _ScalarCompoundPlugAdapter,
    attr: AttrOperator[Any],
    index: int,
) -> None:
    limit_items: tuple[tuple[Any, str], ...] = (
        (attr.min_value, "_set_child_attr_min"),
        (attr.max_value, "_set_child_attr_max"),
        (attr.soft_min_value, "_set_child_attr_soft_min"),
        (attr.soft_max_value, "_set_child_attr_soft_max"),
    )
    for value, method_name in limit_items:
        if value is None:
            continue
        scalar_plug.apply_child_limit(
            method_name,
            child_fn,
            scalar_plug.child_value(value, index),
        )


def _create_enum_attr(
    child_field: AttributeField[Any, Any],
    attr: AttrOperator[Any],
) -> om.MObject:
    fn_attr = om.MFnEnumAttribute()
    default_value = attr.default_value
    if default_value is None:
        default_value = 0
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
        default_value,
    )
    _apply_mfn_attr_options(fn_attr, attr)

    plug_cls = _plug_cls_or_raise(child_field)
    name_map = getattr(plug_cls, "NAME_MAP", None)
    if name_map is None:
        name_map = getattr(attr, "NAME_MAP", None)
    if name_map is None:
        raise UnsupportedOperationError(
            f"{plug_cls.__name__}.NAME_MAP is not defined."
        )

    for index, name in name_map.items():
        fn_attr.addField(name, index)
    return attr_obj


def _create_message_attr(attr: AttrOperator[Any]) -> om.MObject:
    fn_attr = om.MFnMessageAttribute()
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
    )
    _apply_mfn_attr_options(fn_attr, attr)
    return attr_obj


def _create_compound_attr(
    child_field: AttributeField[Any, Any],
    attr: AttrOperator[Any],
    parent: _CompoundAttrParent,
) -> om.MObject:
    plug_cls = _plug_cls_or_raise(child_field)
    child_fields = getattr(plug_cls, "CHILD_FIELDS", ())
    if not child_fields:
        raise UnsupportedOperationError(
            f"{plug_cls.__name__} must define child fields."
        )

    fn_attr = om.MFnCompoundAttribute()
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
    )
    _apply_mfn_attr_options(fn_attr, attr)

    nested_parent = _NestedCompoundAttrParent(
        parent=parent,
        oprt_attr=attr,
    )
    for nested_child_field in child_fields:
        fn_attr.addChild(_create_child_attr(nested_parent, nested_child_field))
    return attr_obj


class _NestedCompoundAttrParent:
    __slots__ = ("parent", "oprt_attr")

    def __init__(
        self,
        parent: _CompoundAttrParent,
        oprt_attr: AttrOperator[Any],
    ) -> None:
        self.parent = parent
        self.oprt_attr = oprt_attr

    @property
    def node(self) -> Any:
        return self.parent.node

    @property
    def attr_path(self) -> str:
        return self.oprt_attr.attr_path
