# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ...._core import AttrOperator, PlugOperator, AttributeField
from ........py.error import UnsupportedOperationError

# maya
from maya.api import OpenMaya as om

A = TypeVar("A", bound="AttrOperator[Any]")

P = TypeVar("P", bound="PlugOperator[Any]")


class CompoundPlugOperator(PlugOperator[A]):
    __slots__ = ()

    CHILD_FIELDS: tuple[AttributeField, ...] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        child_fields = []
        seen_ids = set()
        for child_field in vars(cls).values():
            child_id = id(child_field)
            if child_id in seen_ids or not isinstance(
                child_field, AttributeField
            ):
                continue
            seen_ids.add(child_id)
            child_fields.append(child_field)

        if child_fields:
            cls.CHILD_FIELDS = tuple(child_fields)
        else:
            cls.CHILD_FIELDS = tuple(getattr(cls, "CHILD_FIELDS", ()))

    # get
    def get(self):
        raise NotImplementedError(
            "CompoundPlug does not support get operation"
        )

    # set
    def set(self, value):
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
            fn_attr.addChild(self._create_child_attr(child_field))

        self._apply_mfn_attr_options(fn_attr)
        self._node.fn_node.addAttribute(attr_obj)

    def _create_child_attr(
        self,
        child_field: AttributeField,
    ) -> om.MObject:
        child_attr = self._create_child_attr_operator(child_field)
        attr_type = child_attr.ATTR_TYPE

        if attr_type in _NUMERIC_ATTR_TYPES:
            return _create_numeric_attr(child_attr)

        if attr_type in _UNIT_ATTR_TYPES:
            return _create_unit_attr(child_attr)

        if attr_type in _MATRIX_ATTR_TYPES:
            return _create_matrix_attr(child_attr)

        if _is_scalar_compound_field(child_field):
            return _create_scalar_compound_attr(child_field, child_attr, self)

        if attr_type == "enum":
            return _create_enum_attr(child_field, child_attr)

        if attr_type == "message":
            return _create_message_attr(child_attr)

        if attr_type == "compound":
            return _create_compound_attr(child_field, child_attr, self)

        raise UnsupportedOperationError(
            "{} child '{}' attribute type '{}' is not supported by "
            "OpenMaya compound add_attr().".format(
                type(self).__name__,
                child_attr.long_name,
                attr_type,
            )
        )

    def _create_child_attr_operator(
        self,
        child_field: AttributeField,
    ) -> AttrOperator:
        parent_attr_path = self._attr_path
        attr_path = f"{parent_attr_path}.{child_field.long_name}"
        return child_field.ATTR_CLS(
            node_cls=self._oprt_attr.node_cls,
            oprt_parent=self,
            name=child_field.name,
            long_name=child_field.long_name,
            short_name=child_field.short_name,
            attr_path=attr_path,
            parent_attr_path=parent_attr_path,
            multi=child_field.multi,
            extra=False,
            default_value=child_field._default_value,
            min_value=child_field._min_value,
            max_value=child_field._max_value,
            soft_min_value=child_field._soft_min_value,
            soft_max_value=child_field._soft_max_value,
            enum_name=child_field._enum_name,
            number_of_children=child_field._number_of_children,
            readable=child_field._readable,
            writable=child_field._writable,
            category=child_field._category,
            child_index=child_field._child_index,
        )


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


def _apply_mfn_attr_options(
    fn_attr: om.MFnAttribute,
    attr: AttrOperator,
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
    attr: AttrOperator,
) -> None:
    if attr.min_value is not None:
        fn_attr.setMin(attr.min_value)
    if attr.max_value is not None:
        fn_attr.setMax(attr.max_value)
    if attr.soft_min_value is not None:
        fn_attr.setSoftMin(attr.soft_min_value)
    if attr.soft_max_value is not None:
        fn_attr.setSoftMax(attr.soft_max_value)


def _create_numeric_attr(attr: AttrOperator) -> om.MObject:
    fn_attr = om.MFnNumericAttribute()
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
        _NUMERIC_ATTR_TYPES[attr.ATTR_TYPE],
        attr.default_value,
    )
    _apply_mfn_attr_options(fn_attr, attr)
    _apply_numeric_range_options(fn_attr, attr)
    return attr_obj


def _create_unit_attr(attr: AttrOperator) -> om.MObject:
    fn_attr = om.MFnUnitAttribute()
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
        _UNIT_ATTR_TYPES[attr.ATTR_TYPE],
        attr.default_value,
    )
    _apply_mfn_attr_options(fn_attr, attr)
    _apply_numeric_range_options(fn_attr, attr)
    return attr_obj


def _create_matrix_attr(attr: AttrOperator) -> om.MObject:
    fn_attr = om.MFnMatrixAttribute()
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
        _MATRIX_ATTR_TYPES[attr.ATTR_TYPE],
    )
    _apply_mfn_attr_options(fn_attr, attr)
    return attr_obj


def _is_scalar_compound_field(child_field: AttributeField) -> bool:
    plug_cls = child_field.PLUG_CLS
    return (
        getattr(plug_cls, "CHILD_M_FN", None) is not None
        and getattr(plug_cls, "CHILD_M_ATTR_TYPE", None) is not None
        and bool(getattr(plug_cls, "_SUFFIXES", ()))
        and bool(getattr(plug_cls, "CHILD_FIELDS", ()))
    )


def _create_scalar_compound_attr(
    child_field: AttributeField,
    attr: AttrOperator,
    parent_plug: CompoundPlugOperator,
) -> om.MObject:
    scalar_plug = child_field.PLUG_CLS(
        node=parent_plug._node,
        oprt_attr=attr,
        parent_attr_path=parent_plug._attr_path,
        multi=attr.multi,
        parent_oprt_plug=parent_plug,
    )

    children_attrs = []
    for i, suffix in enumerate(scalar_plug._SUFFIXES):
        child_fn = scalar_plug.CHILD_M_FN()
        default_value = scalar_plug._child_value(
            attr.default_value,
            i,
            default=0,
        )
        child_attr = child_fn.create(
            scalar_plug.child_long_name(suffix, i),
            scalar_plug.child_short_name(suffix, i),
            scalar_plug.CHILD_M_ATTR_TYPE,
            scalar_plug._prepare_child_default_value(default_value),
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
    scalar_plug: PlugOperator,
    attr: AttrOperator,
    index: int,
) -> None:
    limit_items = (
        (attr.min_value, scalar_plug._set_child_attr_min),
        (attr.max_value, scalar_plug._set_child_attr_max),
        (attr.soft_min_value, scalar_plug._set_child_attr_soft_min),
        (attr.soft_max_value, scalar_plug._set_child_attr_soft_max),
    )
    for value, setter in limit_items:
        if value is None:
            continue
        setter(child_fn, scalar_plug._child_value(value, index))


def _create_enum_attr(
    child_field: AttributeField,
    attr: AttrOperator,
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

    name_map = getattr(child_field.PLUG_CLS, "NAME_MAP", None)
    if name_map is None:
        name_map = getattr(attr, "NAME_MAP", None)
    if name_map is None:
        raise UnsupportedOperationError(
            f"{child_field.PLUG_CLS.__name__}.NAME_MAP is not defined."
        )

    for index, name in name_map.items():
        fn_attr.addField(name, index)
    return attr_obj


def _create_message_attr(attr: AttrOperator) -> om.MObject:
    fn_attr = om.MFnMessageAttribute()
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
    )
    _apply_mfn_attr_options(fn_attr, attr)
    return attr_obj


def _create_compound_attr(
    child_field: AttributeField,
    attr: AttrOperator,
    parent_plug: CompoundPlugOperator,
) -> om.MObject:
    child_fields = getattr(child_field.PLUG_CLS, "CHILD_FIELDS", ())
    if not child_fields:
        raise UnsupportedOperationError(
            f"{child_field.PLUG_CLS.__name__} must define child fields."
        )

    fn_attr = om.MFnCompoundAttribute()
    attr_obj = fn_attr.create(
        attr.long_name,
        attr.short_name,
    )
    _apply_mfn_attr_options(fn_attr, attr)

    nested_parent = _NestedCompoundAttrParent(
        parent_plug=parent_plug,
        oprt_attr=attr,
    )
    for nested_child_field in child_fields:
        fn_attr.addChild(nested_parent._create_child_attr(nested_child_field))
    return attr_obj


class _NestedCompoundAttrParent:
    __slots__ = ("parent_plug", "_oprt_attr")

    def __init__(
        self,
        parent_plug: CompoundPlugOperator,
        oprt_attr: AttrOperator,
    ):
        self.parent_plug = parent_plug
        self._oprt_attr = oprt_attr

    @property
    def _attr_path(self) -> str:
        return self._oprt_attr._attr_path

    def _create_child_attr(
        self,
        child_field: AttributeField,
    ) -> om.MObject:
        return CompoundPlugOperator._create_child_attr(self, child_field)

    def _create_child_attr_operator(
        self,
        child_field: AttributeField,
    ) -> AttrOperator:
        return CompoundPlugOperator._create_child_attr_operator(
            self,
            child_field,
        )
