# coding: utf-8
from __future__ import annotations

import pytest

from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr
from bd_util.maya.node.operator.attr.define.std.at.addr import AddrField
from bd_util.maya.node.operator.node.dag.transform._core import Transform

pytestmark = pytest.mark.maya


class PlugOnlyEnumPlugOperator(AddAttr.define.at.enum.plug_operator):
    __slots__ = ()

    ALPHA = 0
    BETA = 1
    GAMMA = 2

    NAME_MAP = {
        ALPHA: "Alpha",
        BETA: "Beta",
        GAMMA: "Gamma",
    }


class PlugOnlyEnumField(
    AddAttr.define.at.enum.field[PlugOnlyEnumPlugOperator]
):
    __slots__ = ()


class PriorityEnumPlugOperator(AddAttr.define.at.enum.plug_operator):
    __slots__ = ()

    LOW = 0
    HIGH = 1

    NAME_MAP = {
        LOW: "Plug Low",
        HIGH: "Plug High",
    }


class PriorityEnumField(AddAttr.define.at.enum.field[PriorityEnumPlugOperator]):
    __slots__ = ()


class SimpleCompoundModePlugOperator(AddAttr.define.at.enum.plug_operator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class SimpleCompoundModeField(
    AddAttr.define.at.enum.field[SimpleCompoundModePlugOperator]
):
    __slots__ = ()


class SimpleNestedCompoundPlugOperator(AddAttr.define.at.compound.plug_operator):
    __slots__ = ()

    visible = AddAttr.at.bool(default_value=True)
    blend = AddAttr.at.float(
        default_value=0.5,
        min_value=0.0,
        max_value=1.0,
    )


class SimpleNestedCompoundField(
    AddAttr.define.at.compound.field[SimpleNestedCompoundPlugOperator]
):
    __slots__ = ()


class SimpleCompoundPlugOperator(AddAttr.define.at.compound.plug_operator):
    __slots__ = ()

    enabled = AddAttr.at.bool(default_value=False)
    weight = AddAttr.at.float(
        default_value=1.25,
        min_value=0.0,
        max_value=10.0,
    )
    mode = SimpleCompoundModeField()
    nested = SimpleNestedCompoundField()
    uv = AddAttr.at.double2(default_value=[4.0, 5.0])
    offset = AddAttr.at.double3(
        default_value=[1.0, 2.0, 3.0],
        min_value=[-1.0, -2.0, -3.0],
        max_value=10.0,
    )
    tangent = AddAttr.at.double4(default_value=[4.0, 5.0, 6.0, 7.0])
    orient = AddAttr.at.quat(default_value=[0.1, 0.2, 0.3, 0.4])
    floatUv = AddAttr.at.float2(default_value=[0.25, 0.75])
    color = AddAttr.at.float3(default_value=[0.1, 0.2, 0.3])
    indexPair = AddAttr.at.long2(default_value=[1, 2])
    indexTriplet = AddAttr.at.long3(default_value=[3, 4, 5])
    shortPair = AddAttr.at.short2(default_value=[6, 7])
    shortTriplet = AddAttr.at.short3(default_value=[8, 9, 10])
    linear2 = AddAttr.at.double_linear2(default_value=[11.0, 12.0])
    linear3 = AddAttr.at.double_linear3(default_value=[13.0, 14.0, 15.0])
    angle2 = AddAttr.at.double_angle2(default_value=[16.0, 17.0])
    aim = AddAttr.at.double_angle3(default_value=[10.0, 20.0, 30.0])
    floatLinear2 = AddAttr.at.float_linear2(default_value=[18.0, 19.0])
    floatLinear3 = AddAttr.at.float_linear3(
        default_value=[20.0, 21.0, 22.0]
    )
    floatAngle2 = AddAttr.at.float_angle2(default_value=[23.0, 24.0])
    floatAngle3 = AddAttr.at.float_angle3(
        default_value=[25.0, 26.0, 27.0]
    )


class SimpleCompoundField(
    AddAttr.define.at.compound.field[SimpleCompoundPlugOperator]
):
    __slots__ = ()


class ExtraCompoundTransform(Transform):
    __slots__ = ()

    extraDouble2 = AddAttr.at.double2(default_value=[1.0, 2.0])
    extraDouble3 = AddAttr.at.double3(default_value=[1.0, 2.0, 3.0])
    extraDouble4 = AddAttr.at.double4(default_value=[1.0, 2.0, 3.0, 4.0])
    extraLimitedDouble4 = AddAttr.at.double4(
        default_value=[1.0, 2.0, 3.0, 4.0],
        min_value=[-1.0, -2.0, -3.0, -4.0],
        max_value=10.0,
        soft_min_value=0.0,
        soft_max_value=[1.0, 2.0, 3.0, 4.0],
    )
    extraQuat = AddAttr.at.quat()
    extraQuatCustom = AddAttr.at.quat(default_value=[0.1, 0.2, 0.3, 0.4])
    extraFloat2 = AddAttr.at.float2(default_value=[1.0, 2.0])
    extraFloat3 = AddAttr.at.float3(default_value=[1.0, 2.0, 3.0])
    extraLong2 = AddAttr.at.long2(default_value=[1, 2])
    extraLong3 = AddAttr.at.long3(default_value=[1, 2, 3])
    extraShort2 = AddAttr.at.short2(default_value=[1, 2])
    extraShort3 = AddAttr.at.short3(default_value=[1, 2, 3])
    extraDoubleLinear2 = AddAttr.at.double_linear2(default_value=[1.0, 2.0])
    extraDoubleLinear3 = AddAttr.at.double_linear3(
        default_value=[1.0, 2.0, 3.0]
    )
    extraDoubleAngle2 = AddAttr.at.double_angle2(default_value=[10.0, 20.0])
    extraDoubleAngle3 = AddAttr.at.double_angle3(
        default_value=[10.0, 20.0, 30.0]
    )
    extraFloatLinear2 = AddAttr.at.float_linear2(default_value=[3.0, 4.0])
    extraFloatLinear3 = AddAttr.at.float_linear3(default_value=[3.0, 4.0, 5.0])
    extraFloatAngle2 = AddAttr.at.float_angle2(default_value=[30.0, 40.0])
    extraFloatAngle3 = AddAttr.at.float_angle3(
        default_value=[30.0, 40.0, 50.0]
    )
    extraNamedDouble = AddAttr.at.double(
        default_value=2.5,
        long_name="extraNamedDoubleLong",
        short_name="end",
    )
    extraOptionedDouble = AddAttr.at.double(
        default_value=3.5,
        writable=False,
        category="bdAddAttrTest",
    )
    extraMultiDouble = AddAttr.at.double(multi=True)
    extraPlugOnlyEnum = PlugOnlyEnumField()
    extraPriorityEnum = PriorityEnumField()
    extraSimpleCompound = SimpleCompoundField(category="bdSimpleCompoundTest")
    extraNamedString = AddAttr.dt.string(
        default_value="hello",
        long_name="extraNamedStringLong",
        short_name="ens",
    )


class ExtraCmdsAddAttrTransform(Transform):
    __slots__ = ()

    extraAddr = AddrField(
        extra=True,
        readable=False,
        writable=False,
        category="bdCmdsAddAttrTest",
    )


@pytest.fixture
def extra_compound_node(modifier_manager):
    node = ExtraCompoundTransform.create(
        modifier_manager,
        name="extra_compound",
    )
    modifier_manager.do_it_dag()
    modifier_manager.do_it_dg()
    return node


COMPOUND_DEFAULT_CASES = (
    ("extraDouble2", [1.0, 2.0]),
    ("extraDouble3", [1.0, 2.0, 3.0]),
    ("extraDouble4", [1.0, 2.0, 3.0, 4.0]),
    ("extraQuat", [0.0, 0.0, 0.0, 1.0]),
    ("extraQuatCustom", [0.1, 0.2, 0.3, 0.4]),
    ("extraFloat2", [1.0, 2.0]),
    ("extraFloat3", [1.0, 2.0, 3.0]),
    ("extraLong2", [1, 2]),
    ("extraLong3", [1, 2, 3]),
    ("extraShort2", [1, 2]),
    ("extraShort3", [1, 2, 3]),
    ("extraDoubleLinear2", [1.0, 2.0]),
    ("extraDoubleLinear3", [1.0, 2.0, 3.0]),
    ("extraDoubleAngle2", [10.0, 20.0]),
    ("extraDoubleAngle3", [10.0, 20.0, 30.0]),
    ("extraFloatLinear2", [3.0, 4.0]),
    ("extraFloatLinear3", [3.0, 4.0, 5.0]),
    ("extraFloatAngle2", [30.0, 40.0]),
    ("extraFloatAngle3", [30.0, 40.0, 50.0]),
)


COMPOUND_SET_CASES = (
    ("extraDouble2", [11.0, 12.0]),
    ("extraDouble3", [11.0, 12.0, 13.0]),
    ("extraDouble4", [11.0, 12.0, 13.0, 14.0]),
    ("extraQuat", [0.1, 0.2, 0.3, 0.4]),
    ("extraFloat2", [21.0, 22.0]),
    ("extraFloat3", [21.0, 22.0, 23.0]),
    ("extraLong2", [31, 32]),
    ("extraLong3", [31, 32, 33]),
    ("extraShort2", [41, 42]),
    ("extraShort3", [41, 42, 43]),
    ("extraDoubleLinear2", [51.0, 52.0]),
    ("extraDoubleLinear3", [51.0, 52.0, 53.0]),
    ("extraDoubleAngle2", [61.0, 62.0]),
    ("extraDoubleAngle3", [61.0, 62.0, 63.0]),
    ("extraFloatLinear2", [71.0, 72.0]),
    ("extraFloatLinear3", [71.0, 72.0, 73.0]),
    ("extraFloatAngle2", [81.0, 82.0]),
    ("extraFloatAngle3", [81.0, 82.0, 83.0]),
)


@pytest.mark.parametrize(("attr_name", "expected"), COMPOUND_DEFAULT_CASES)
def test_compound_defaults(extra_compound_node, attr_name, expected):
    node = extra_compound_node

    assert getattr(node, attr_name).get() == pytest.approx(expected)


@pytest.mark.parametrize(("attr_name", "values"), COMPOUND_SET_CASES)
def test_compound_set_updates_with_modifier(
    modifier_manager,
    extra_compound_node,
    attr_name,
    values,
):
    node = extra_compound_node
    plug = getattr(node, attr_name)

    plug.set(*values)
    modifier_manager.do_it_dg()

    assert plug.get() == pytest.approx(values)


def test_compound_set_accepts_tuple_and_rejects_wrong_count(
    modifier_manager,
    extra_compound_node,
):
    node = extra_compound_node

    node.extraDouble4.set((4.0, 3.0, 2.0, 1.0))
    modifier_manager.do_it_dg()
    assert node.extraDouble4.get() == pytest.approx([4.0, 3.0, 2.0, 1.0])

    with pytest.raises(TypeError, match="Expected either set"):
        node.extraDouble4.set(9.0, 8.0)

    modifier_manager.do_it_dg()
    assert node.extraDouble4.get() == pytest.approx([4.0, 3.0, 2.0, 1.0])


@pytest.mark.parametrize(("attr_name", "values"), COMPOUND_SET_CASES)
def test_compound_set_direct_updates_immediately(
    extra_compound_node,
    attr_name,
    values,
):
    node = extra_compound_node
    plug = getattr(node, attr_name)

    plug.set_direct(*values)

    assert plug.get() == pytest.approx(values)


def test_compound_set_direct_rejects_wrong_count(extra_compound_node):
    node = extra_compound_node

    node.extraDouble4.set_direct(1.0, 2.0, 3.0, 4.0)

    with pytest.raises(TypeError, match="Expected either set_direct"):
        node.extraDouble4.set_direct(9.0, 8.0)

    assert node.extraDouble4.get() == pytest.approx([1.0, 2.0, 3.0, 4.0])


def test_double4_and_quat_child_names(extra_compound_node, maya_cmds):
    node = extra_compound_node

    assert maya_cmds.attributeQuery(
        "extraDouble4",
        node=node.name,
        listChildren=True,
    ) == [
        "extraDouble4X",
        "extraDouble4Y",
        "extraDouble4Z",
        "extraDouble4W",
    ]
    assert maya_cmds.attributeQuery(
        "extraQuat",
        node=node.name,
        listChildren=True,
    ) == [
        "extraQuatX",
        "extraQuatY",
        "extraQuatZ",
        "extraQuatW",
    ]


def test_double4_and_quat_lookup(extra_compound_node):
    from bd_util.maya.node.operator.attr.lookup import lookup_attr_cls

    node = extra_compound_node

    assert lookup_attr_cls(node.name, "extraDouble4").__name__ == (
        "Double4AttrOperator"
    )
    assert lookup_attr_cls(node.name, "extraQuat").__name__ == (
        "Quat4AttrOperator"
    )


def test_add_attr_factory_names_and_options(
    extra_compound_node,
    maya_cmds,
):
    node = extra_compound_node

    assert node.extraNamedDouble.plug_name == (
        "extra_compound.extraNamedDoubleLong"
    )
    assert node.extraNamedDouble.short_name == "end"
    assert node.extraNamedDouble.get() == pytest.approx(2.5)
    assert (
        maya_cmds.attributeQuery(
            "extraNamedDoubleLong",
            node=node.name,
            shortName=True,
        )
        == "end"
    )

    assert node.extraNamedString.plug_name == (
        "extra_compound.extraNamedStringLong"
    )
    assert node.extraNamedString.short_name == "ens"
    assert node.extraNamedString.get() == "hello"
    assert (
        maya_cmds.attributeQuery(
            "extraNamedStringLong",
            node=node.name,
            shortName=True,
        )
        == "ens"
    )

    assert maya_cmds.attributeQuery(
        "extraOptionedDouble",
        node=node.name,
        readable=True,
    )
    assert not maya_cmds.attributeQuery(
        "extraOptionedDouble",
        node=node.name,
        writable=True,
    )
    assert maya_cmds.attributeQuery(
        "extraOptionedDouble",
        node=node.name,
        categories=True,
    ) == ["bdAddAttrTest"]

    assert maya_cmds.attributeQuery(
        "extraMultiDouble",
        node=node.name,
        multi=True,
    )


def test_extra_enum_field_can_be_defined_with_plug_only(
    extra_compound_node,
    maya_cmds,
):
    node = extra_compound_node

    assert isinstance(node.extraPlugOnlyEnum, PlugOnlyEnumPlugOperator)
    assert node.extraPlugOnlyEnum.ALPHA == 0
    assert (
        node.extraPlugOnlyEnum.name_by_index(node.extraPlugOnlyEnum.BETA)
        == "Beta"
    )
    assert node.extraPlugOnlyEnum.index_by_name("Gamma") == (
        node.extraPlugOnlyEnum.GAMMA
    )
    assert maya_cmds.attributeQuery(
        "extraPlugOnlyEnum",
        node=node.name,
        listEnum=True,
    ) == ["Alpha:Beta:Gamma"]


def test_enum_plug_name_map_has_priority(
    extra_compound_node,
    maya_cmds,
):
    node = extra_compound_node

    assert (
        node.extraPriorityEnum.name_by_index(node.extraPriorityEnum.LOW)
        == "Plug Low"
    )
    assert node.extraPriorityEnum.index_by_name("Plug High") == (
        node.extraPriorityEnum.HIGH
    )
    assert maya_cmds.attributeQuery(
        "extraPriorityEnum",
        node=node.name,
        listEnum=True,
    ) == ["Plug Low:Plug High"]


def test_extra_compound_field_can_be_defined_with_plug_only(
    extra_compound_node,
    maya_cmds,
):
    node = extra_compound_node

    assert isinstance(node.extraSimpleCompound, SimpleCompoundPlugOperator)
    assert node.extraSimpleCompound.enabled.get() is False
    assert node.extraSimpleCompound.weight.get() == pytest.approx(1.25)
    assert (
        node.extraSimpleCompound.mode.name_by_index(
            node.extraSimpleCompound.mode.ON
        )
        == "On"
    )
    assert node.extraSimpleCompound.mode.get() == (
        node.extraSimpleCompound.mode.OFF
    )

    assert (
        maya_cmds.attributeQuery(
            "extraSimpleCompound",
            node=node.name,
            attributeType=True,
        )
        == "compound"
    )
    assert maya_cmds.attributeQuery(
        "extraSimpleCompound",
        node=node.name,
        listChildren=True,
    ) == [
        "enabled",
        "weight",
        "mode",
        "nested",
        "uv",
        "offset",
        "tangent",
        "orient",
        "floatUv",
        "color",
        "indexPair",
        "indexTriplet",
        "shortPair",
        "shortTriplet",
        "linear2",
        "linear3",
        "angle2",
        "aim",
        "floatLinear2",
        "floatLinear3",
        "floatAngle2",
        "floatAngle3",
    ]
    assert maya_cmds.attributeQuery(
        "extraSimpleCompound",
        node=node.name,
        categories=True,
    ) == ["bdSimpleCompoundTest"]
    assert maya_cmds.attributeQuery(
        "enabled",
        node=node.name,
        attributeType=True,
    ) == "bool"
    assert maya_cmds.attributeQuery(
        "weight",
        node=node.name,
        attributeType=True,
    ) == "float"
    assert maya_cmds.attributeQuery(
        "weight",
        node=node.name,
        minimum=True,
    ) == pytest.approx([0.0])
    assert maya_cmds.attributeQuery(
        "weight",
        node=node.name,
        maximum=True,
    ) == pytest.approx([10.0])
    assert maya_cmds.attributeQuery(
        "mode",
        node=node.name,
        attributeType=True,
    ) == "enum"
    assert maya_cmds.attributeQuery(
        "mode",
        node=node.name,
        listEnum=True,
    ) == ["Off:On"]


def test_extra_compound_can_have_nested_compound_child(
    extra_compound_node,
    maya_cmds,
):
    node = extra_compound_node

    assert isinstance(
        node.extraSimpleCompound.nested,
        SimpleNestedCompoundPlugOperator,
    )
    assert node.extraSimpleCompound.nested.visible.get() is True
    assert node.extraSimpleCompound.nested.blend.get() == pytest.approx(0.5)

    assert (
        maya_cmds.attributeQuery(
            "nested",
            node=node.name,
            attributeType=True,
        )
        == "compound"
    )
    assert maya_cmds.attributeQuery(
        "nested",
        node=node.name,
        listChildren=True,
    ) == ["visible", "blend"]
    assert maya_cmds.attributeQuery(
        "visible",
        node=node.name,
        attributeType=True,
    ) == "bool"
    assert maya_cmds.attributeQuery(
        "blend",
        node=node.name,
        attributeType=True,
    ) == "float"
    assert maya_cmds.attributeQuery(
        "blend",
        node=node.name,
        minimum=True,
    ) == pytest.approx([0.0])
    assert maya_cmds.attributeQuery(
        "blend",
        node=node.name,
        maximum=True,
    ) == pytest.approx([1.0])


def test_extra_compound_can_have_custom_scalar_compound_child(
    extra_compound_node,
    maya_cmds,
):
    node = extra_compound_node

    assert node.extraSimpleCompound.uv.get() == pytest.approx([4.0, 5.0])
    assert node.extraSimpleCompound.offset.get() == pytest.approx(
        [1.0, 2.0, 3.0]
    )
    assert node.extraSimpleCompound.tangent.get() == pytest.approx(
        [4.0, 5.0, 6.0, 7.0]
    )
    assert node.extraSimpleCompound.orient.get() == pytest.approx(
        [0.1, 0.2, 0.3, 0.4]
    )
    assert node.extraSimpleCompound.floatUv.get() == pytest.approx(
        [0.25, 0.75]
    )
    assert node.extraSimpleCompound.color.get() == pytest.approx(
        [0.1, 0.2, 0.3]
    )
    assert node.extraSimpleCompound.indexPair.get() == pytest.approx([1, 2])
    assert node.extraSimpleCompound.indexTriplet.get() == pytest.approx(
        [3, 4, 5]
    )
    assert node.extraSimpleCompound.shortPair.get() == pytest.approx([6, 7])
    assert node.extraSimpleCompound.shortTriplet.get() == pytest.approx(
        [8, 9, 10]
    )
    assert node.extraSimpleCompound.linear2.get() == pytest.approx(
        [11.0, 12.0]
    )
    assert node.extraSimpleCompound.linear3.get() == pytest.approx(
        [13.0, 14.0, 15.0]
    )
    assert node.extraSimpleCompound.angle2.get() == pytest.approx(
        [16.0, 17.0]
    )
    assert node.extraSimpleCompound.aim.get() == pytest.approx(
        [10.0, 20.0, 30.0]
    )
    assert node.extraSimpleCompound.floatLinear2.get() == pytest.approx(
        [18.0, 19.0]
    )
    assert node.extraSimpleCompound.floatLinear3.get() == pytest.approx(
        [20.0, 21.0, 22.0]
    )
    assert node.extraSimpleCompound.floatAngle2.get() == pytest.approx(
        [23.0, 24.0]
    )
    assert node.extraSimpleCompound.floatAngle3.get() == pytest.approx(
        [25.0, 26.0, 27.0]
    )

    assert maya_cmds.attributeQuery(
        "uv",
        node=node.name,
        attributeType=True,
    ) == "double2"
    assert maya_cmds.attributeQuery(
        "offset",
        node=node.name,
        attributeType=True,
    ) == "double3"
    assert maya_cmds.attributeQuery(
        "offset",
        node=node.name,
        listChildren=True,
    ) == ["offsetX", "offsetY", "offsetZ"]
    assert maya_cmds.attributeQuery(
        "tangent",
        node=node.name,
        attributeType=True,
    ) == "double4"
    assert maya_cmds.attributeQuery(
        "orient",
        node=node.name,
        attributeType=True,
    ) == "double4"
    assert maya_cmds.attributeQuery(
        "floatUv",
        node=node.name,
        attributeType=True,
    ) == "float2"
    assert maya_cmds.attributeQuery(
        "color",
        node=node.name,
        attributeType=True,
    ) == "float3"
    assert maya_cmds.attributeQuery(
        "color",
        node=node.name,
        listChildren=True,
    ) == ["colorX", "colorY", "colorZ"]
    assert maya_cmds.attributeQuery(
        "indexPair",
        node=node.name,
        attributeType=True,
    ) == "long2"
    assert maya_cmds.attributeQuery(
        "indexTriplet",
        node=node.name,
        attributeType=True,
    ) == "long3"
    assert maya_cmds.attributeQuery(
        "shortPair",
        node=node.name,
        attributeType=True,
    ) == "short2"
    assert maya_cmds.attributeQuery(
        "shortTriplet",
        node=node.name,
        attributeType=True,
    ) == "short3"
    assert maya_cmds.attributeQuery(
        "linear2",
        node=node.name,
        attributeType=True,
    ) == "double2"
    assert maya_cmds.attributeQuery(
        "linear3",
        node=node.name,
        attributeType=True,
    ) == "double3"
    assert maya_cmds.attributeQuery(
        "angle2",
        node=node.name,
        attributeType=True,
    ) == "double2"
    assert maya_cmds.attributeQuery(
        "aim",
        node=node.name,
        attributeType=True,
    ) == "double3"
    assert maya_cmds.attributeQuery(
        "aim",
        node=node.name,
        listChildren=True,
    ) == ["aimX", "aimY", "aimZ"]
    assert [
        maya_cmds.attributeQuery(
            child_name,
            node=node.name,
            attributeType=True,
        )
        for child_name in ("aimX", "aimY", "aimZ")
    ] == ["doubleAngle", "doubleAngle", "doubleAngle"]
    assert [
        maya_cmds.attributeQuery(
            child_name,
            node=node.name,
            attributeType=True,
        )
        for child_name in ("floatAngle3X", "floatAngle3Y", "floatAngle3Z")
    ] == ["doubleAngle", "doubleAngle", "doubleAngle"]
    assert [
        maya_cmds.attributeQuery(
            child_name,
            node=node.name,
            minimum=True,
        )[0]
        for child_name in ("offsetX", "offsetY", "offsetZ")
    ] == pytest.approx([-1.0, -2.0, -3.0])
    assert [
        maya_cmds.attributeQuery(
            child_name,
            node=node.name,
            maximum=True,
        )[0]
        for child_name in ("offsetX", "offsetY", "offsetZ")
    ] == pytest.approx([10.0, 10.0, 10.0])


def test_double_angle3_preserves_maya_shape(
    extra_compound_node,
    maya_cmds,
):
    node = extra_compound_node
    child_names = maya_cmds.attributeQuery(
        "extraDoubleAngle3",
        node=node.name,
        listChildren=True,
    )

    assert (
        maya_cmds.attributeQuery(
            "extraDoubleAngle3",
            node=node.name,
            attributeType=True,
        )
        == "double3"
    )
    assert child_names == [
        "extraDoubleAngle3X",
        "extraDoubleAngle3Y",
        "extraDoubleAngle3Z",
    ]
    assert [
        maya_cmds.attributeQuery(
            child_name,
            node=node.name,
            attributeType=True,
        )
        for child_name in child_names
    ] == ["doubleAngle", "doubleAngle", "doubleAngle"]
    assert maya_cmds.getAttr(f"{node.name}.extraDoubleAngle3")[0] == (
        pytest.approx((10.0, 20.0, 30.0))
    )


def test_cmds_add_attr_options(modifier_manager, maya_cmds):
    created_node = ExtraCmdsAddAttrTransform.create(
        modifier_manager,
        name="extra_cmds_add_attr",
        auto_add_attr=False,
    )
    modifier_manager.do_it_dag()
    modifier_manager.do_it_dg()
    node = ExtraCmdsAddAttrTransform(
        modifier_manager,
        m_obj=created_node.m_obj,
        auto_add_attr=True,
    )

    assert maya_cmds.objExists(f"{node.name}.extraAddr")
    assert not maya_cmds.attributeQuery(
        "extraAddr",
        node=node.name,
        readable=True,
    )
    assert not maya_cmds.attributeQuery(
        "extraAddr",
        node=node.name,
        writable=True,
    )
    assert maya_cmds.attributeQuery(
        "extraAddr",
        node=node.name,
        categories=True,
    ) == ["bdCmdsAddAttrTest"]


def test_same_compound_type_child_names_do_not_bleed(extra_compound_node):
    node = extra_compound_node

    assert (
        node.extraDouble4.x.plug_name
        == "extra_compound.extraDouble4.extraDouble4X"
    )
    assert (
        node.extraLimitedDouble4.x.plug_name
        == "extra_compound.extraLimitedDouble4.extraLimitedDouble4X"
    )
    assert (
        node.extraDouble4.x.plug_name
        == "extra_compound.extraDouble4.extraDouble4X"
    )


def _query_limit(maya_cmds, node, attr_name, flag):
    return maya_cmds.attributeQuery(
        attr_name,
        node=node.name,
        **{flag: True},
    )[0]


def test_double4_child_limits_from_add_attr(extra_compound_node, maya_cmds):
    node = extra_compound_node

    child_names = [
        "extraLimitedDouble4X",
        "extraLimitedDouble4Y",
        "extraLimitedDouble4Z",
        "extraLimitedDouble4W",
    ]

    assert [
        _query_limit(maya_cmds, node, child_name, "minimum")
        for child_name in child_names
    ] == pytest.approx([-1.0, -2.0, -3.0, -4.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "maximum")
        for child_name in child_names
    ] == pytest.approx([10.0, 10.0, 10.0, 10.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "softMin")
        for child_name in child_names
    ] == pytest.approx([0.0, 0.0, 0.0, 0.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "softMax")
        for child_name in child_names
    ] == pytest.approx([1.0, 2.0, 3.0, 4.0])


def test_double4_child_limits_can_be_changed(extra_compound_node, maya_cmds):
    node = extra_compound_node

    node.extraDouble4.set_min([-4.0, -3.0, -2.0, -1.0])
    node.extraDouble4.set_max(4.0)
    node.extraDouble4.set_soft_min([-2.0, -1.0, 0.0, 1.0])
    node.extraDouble4.set_soft_max(2.0)

    child_names = [
        "extraDouble4X",
        "extraDouble4Y",
        "extraDouble4Z",
        "extraDouble4W",
    ]

    assert [
        _query_limit(maya_cmds, node, child_name, "minimum")
        for child_name in child_names
    ] == pytest.approx([-4.0, -3.0, -2.0, -1.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "maximum")
        for child_name in child_names
    ] == pytest.approx([4.0, 4.0, 4.0, 4.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "softMin")
        for child_name in child_names
    ] == pytest.approx([-2.0, -1.0, 0.0, 1.0])
    assert [
        _query_limit(maya_cmds, node, child_name, "softMax")
        for child_name in child_names
    ] == pytest.approx([2.0, 2.0, 2.0, 2.0])
