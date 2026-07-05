# coding: utf-8
"""
extra=True の Attr を使った自動 addAttr() 機能のテスト・デモ
"""

# maya
from maya import cmds

# self
from ....... import logger as u_logger
from ...... import str as test_str
from .......maya.node.modifier import ModifierManager
from .......maya.node.operator.node.dag.transform._core import Transform
from .......maya.node.operator.attr.extra.add_attr import AddAttr

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


# class TestEnumAttrOperator(AddAttr.at.enum_attr_operator):
class TestEnumAttrOperator(AddAttr.define.at.enum.attr_operator):
    __slots__ = ()

    ALPHA = 0
    BETA = 1
    GAMMA = 2

    NAME_MAP = {
        ALPHA: "Alpha",
        BETA: "Beta",
        GAMMA: "Gamma",
    }


class TestEnumPlugOperator(AddAttr.define.at.enum.plug_operator):
    __slots__ = ()

    ALPHA = 0
    BETA = 1
    GAMMA = 2


class TestEnumField(
    AddAttr.define.at.enum.field[TestEnumAttrOperator, TestEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TestEnumAttrOperator
    PLUG_CLS = TestEnumPlugOperator


class TestExtraEnumPlugOperator(AddAttr.define.at.enum.plug_operator):
    __slots__ = ()

    ALPHA = 0
    BETA = 1
    GAMMA = 2

    NAME_MAP = {
        ALPHA: "Alpha",
        BETA: "Beta",
        GAMMA: "Gamma",
    }


class TestExtraEnumField(
    AddAttr.define.at.enum.extra_field[TestExtraEnumPlugOperator]
):
    __slots__ = ()


class MyTransform(Transform):

    # インスタンス生成時に自動 addAttr() される
    # at
    #   bool
    testBool = AddAttr.at.bool(
        default_value=False,
    )
    tbool = testBool
    #   char
    testChar = AddAttr.at.char(
        default_value=50,
        min_value=-128,
        max_value=127,
        soft_min_value=-128,
        soft_max_value=127,
    )
    tchar = testChar
    #   byte
    testByte = AddAttr.at.byte(
        default_value=50,
        min_value=0,
        max_value=255,
        soft_min_value=0,
        soft_max_value=255,
    )
    tbyte = testByte
    #   short
    testShort = AddAttr.at.short(
        default_value=10000,
        min_value=-32768,
        max_value=32767,
        soft_min_value=-30000,
        soft_max_value=30000,
    )
    tshort = testShort
    #   short2
    testShort2 = AddAttr.at.short2()
    tshort2 = testShort2
    #   short3
    testShort3 = AddAttr.at.short3()
    tshort3 = testShort3
    #   long
    testLong = AddAttr.at.long(
        default_value=1000000000,
        min_value=-2147483648,
        max_value=2147483647,
        soft_min_value=-2000000000,
        soft_max_value=2000000000,
    )
    tlong = testLong
    #   long2
    testLong2 = AddAttr.at.long2()
    tlong2 = testLong2
    #   long3
    testLong3 = AddAttr.at.long3()
    tlong3 = testLong3
    #   long_long_int
    testLongLongInt = AddAttr.at.long_long_int(
        default_value=1000000000000000000,
        soft_min_value=-9223372036854775808,
        soft_max_value=9223372036854773760,
    )
    tlongLongInt = testLongLongInt
    #   float
    testFloat = AddAttr.at.float(
        default_value=10000000000000000000,
        min_value=-99999999999999999999,
        max_value=99999999999999999999,
        soft_min_value=-99999999999999999999,
        soft_max_value=99999999999999999999,
    )
    tfloat = testFloat
    #   float2
    testFloat2 = AddAttr.at.float2()
    tfloat2 = testFloat2
    #   float3
    testFloat3 = AddAttr.at.float3()
    tfloat3 = testFloat3
    #   float_linear
    testFloatLinear = AddAttr.at.float_linear(
        default_value=10000000000000000000,
        min_value=-99999999999999999999,
        max_value=99999999999999999999,
        soft_min_value=-99999999999999999999,
        soft_max_value=99999999999999999999,
    )
    tfloat_linear = testFloatLinear
    #   float_linear2
    testFloatLinear2 = AddAttr.at.float_linear2()
    tfloatLinear2 = testFloatLinear2
    #   float_linear3
    testFloatLinear3 = AddAttr.at.float_linear3()
    tfloatLinear3 = testFloatLinear3
    #   float_angle
    testFloatAngle = AddAttr.at.float_angle(
        default_value=45,
        min_value=-720,
        max_value=720,
        soft_min_value=-360,
        soft_max_value=360,
    )
    tfloatAngle = testFloatAngle
    #   float_angle2
    testFloatAngle2 = AddAttr.at.float_angle2()
    tfloatAngle2 = testFloatAngle2
    #   float_angle3
    testFloatAngle3 = AddAttr.at.float_angle3()
    tfloatAngle3 = testFloatAngle3
    #   double
    testDouble = AddAttr.at.double(
        default_value=10000000000000000000,
        min_value=-99999999999999999999,
        max_value=99999999999999999999,
        soft_min_value=-99999999999999999999,
        soft_max_value=99999999999999999999,
    )
    tdouble = testDouble
    testDoubleMulti = AddAttr.at.double(
        default_value=10000000000000000000,
        min_value=-99999999999999999999,
        max_value=99999999999999999999,
        soft_min_value=-99999999999999999999,
        soft_max_value=99999999999999999999,
        multi=True,
    )
    tdoubleMulti = testDoubleMulti
    #   double2
    testDouble2 = AddAttr.at.double2()
    tdouble2 = testDouble2
    testDouble2Multi = AddAttr.at.double2(
        multi=True,
    )
    tdouble2Multi = testDouble2Multi
    #   double3
    testDouble3 = AddAttr.at.double3()
    tdouble3 = testDouble3
    testDouble3Multi = AddAttr.at.double3(
        multi=True,
    )
    tdouble3Multi = testDouble3Multi
    #   double4
    testDouble4 = AddAttr.at.double4()
    tdouble4 = testDouble4
    testDouble4Multi = AddAttr.at.double4(
        multi=True,
    )
    tdouble4Multi = testDouble4Multi
    #   quat
    testQuat = AddAttr.at.quat()
    tquat = testQuat
    #   double_linear
    testDoubleLinear = AddAttr.at.double_linear(
        default_value=10000000000000000000,
        min_value=-99999999999999999999,
        max_value=99999999999999999999,
        soft_min_value=-99999999999999999999,
        soft_max_value=99999999999999999999,
    )
    tdouble_linear = testDoubleLinear
    #   double_linear2
    testDoubleLinear2 = AddAttr.at.double_linear2()
    tdouble_linear2 = testDoubleLinear2
    #   double_linear3
    testDoubleLinear3 = AddAttr.at.double_linear3()
    tdouble_linear3 = testDoubleLinear3
    #   double_angle
    testDoubleAngle = AddAttr.at.double_angle(
        default_value=45,
        min_value=-720,
        max_value=720,
        soft_min_value=-360,
        soft_max_value=360,
    )
    tdouble_angle = testDoubleAngle
    #   double_angle2
    testDoubleAngle2 = AddAttr.at.double_angle2()
    tdouble_angle2 = testDoubleAngle2
    #   double_angle3
    testDoubleAngle3 = AddAttr.at.double_angle3()
    tdouble_angle3 = testDoubleAngle3

    #   matrix
    testMatrix = AddAttr.at.matrix()
    tmatrix = testMatrix

    #   flt_matrix
    testFltMatrix = AddAttr.at.flt_matrix()
    tfltMatrix = testFltMatrix

    #   enum
    testEnum = TestEnumField()
    tenm = testEnum
    testExtraEnum = TestExtraEnumField()
    texenm = testExtraEnum

    #   message
    testMessage = AddAttr.at.message()
    tmessage = testMessage

    # time
    testTime = AddAttr.at.time(
        default_value=12.345,
    )
    ttime = testTime

    #   generic
    testGeneric = AddAttr.at.generic()
    tgeneric = testGeneric

    # dt
    #   matrix
    testDataMatrix = AddAttr.dt.matrix()
    tdmatrix = testDataMatrix

    #   string
    testDataString = AddAttr.dt.string(
        default_value="Hello World!",
    )
    tdstring = testDataString

    #   double_array
    testDataDoubleArray = AddAttr.dt.double_array()
    tdDoubleArray = testDataDoubleArray

    #   float_array
    testDataFloatArray = AddAttr.dt.float_array()
    tdFloatArray = testDataFloatArray

    #   int32_array
    testDataInt32Array = AddAttr.dt.int32_array()
    tdInt32Array = testDataInt32Array

    #   vector_array
    testDataVectorArray = AddAttr.dt.vector_array()
    tdVectorArray = testDataVectorArray

    #   point_array
    testDataPointArray = AddAttr.dt.point_array()
    tdPointArray = testDataPointArray

    #   string_array
    testDataStringArray = AddAttr.dt.string_array()
    tdStringArray = testDataStringArray

    #   mesh
    testDataMesh = AddAttr.dt.mesh()
    tdMesh = testDataMesh

    #   nurbs_curve
    testDataNurbsCurve = AddAttr.dt.nurbs_curve()
    tdNurbsCurve = testDataNurbsCurve

    #   nurbs_surface
    testDataNurbsSurface = AddAttr.dt.nurbs_surface()
    tdNurbsSurface = testDataNurbsSurface

    #   lattice
    testDataLattice = AddAttr.dt.lattice()
    tdLattice = testDataLattice

    # api.OpenMaya でアトリビュートを作成できないタイプ


def main():
    extra_attrs_class_access()
    extra_attrs_instance_access()
    auto_add_attr_on_init()
    no_auto_add_attr()
    manual_add_attr_via_plug()


def extra_attrs_class_access():
    test_str.title("extra=True: class access properties")
    logger.debug(
        "{}: {}".format(
            "MyTransform._extra_attributes",
            MyTransform._extra_attributes,
        )
    )
    for attr in MyTransform._extra_attributes:
        logger.debug("  attr: {}, extra: {}".format(attr, attr.extra))


def extra_attrs_instance_access():
    test_str.title("extra=True: instance access properties")

    modifier_manager = ModifierManager()
    name = "test"
    if cmds.objExists(name):
        cmds.delete(name)
    node = MyTransform.create(modifier_manager, name="test")
    modifier_manager.do_it_dag()
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node._extra_attributes",
            node._extra_attributes,
        )
    )
    for attr in node._extra_attributes:
        logger.debug("  attr: {}, extra: {}".format(attr, attr.extra))


def auto_add_attr_on_init():
    test_str.title("extra=True: instance access properties")

    node_name = "test_auto_add"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    # ノードを作成
    cmds.createNode("transform", name=node_name, skipSelect=True)

    # Node インスタンス生成 → extra=True の Attr が自動 addAttr() される
    modifier_manager = ModifierManager()
    node = MyTransform(modifier_manager, name=node_name)

    logger.debug(
        "node.testDouble plug exists: {}".format(
            cmds.objExists(f"{node_name}.testDouble")
        )
    )
    logger.debug(
        "node.testDataMatrix plug exists: {}".format(
            cmds.objExists(f"{node_name}.testDataMatrix")
        )
    )

    # Plug 経由でアクセス
    #   at
    #       double
    logger.debug(
        "{}: {}".format(
            "node.testDouble.plug",
            node.testDouble.plug,
        )
    )
    #       double3
    val = node.testDouble3.get()
    logger.debug(
        "{}: before: {}".format(
            "node.testDouble3.get()",
            val,
        )
    )
    node.testDouble3.set(1.0, 2.0, 3.0)
    modifier_manager.do_it_dg()
    val = node.testDouble3.get()
    logger.debug(
        "{}: after : {}".format(
            "node.testDouble3.get()",
            val,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.testDouble3.x",
            node.testDouble3.x,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.testDouble3.y",
            node.testDouble3.y,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.testDouble3.z",
            node.testDouble3.z,
        )
    )
    logger.debug("node.testDouble3.x.set(11.0)")
    node.testDouble3.x.set(11.0)
    logger.debug("node.testDouble3.y.set(22.0)")
    node.testDouble3.y.set(22.0)
    logger.debug("node.testDouble3.z.set(33.0)")
    node.testDouble3.z.set(33.0)
    modifier_manager.do_it_dg()
    val_x = node.testDouble3.x.get()
    val_y = node.testDouble3.y.get()
    val_z = node.testDouble3.z.get()
    logger.debug(
        "{}: after : {}".format(
            "node.testDouble3.x.get()",
            val_x,
        )
    )
    logger.debug(
        "{}: after : {}".format(
            "node.testDouble3.y.get()",
            val_y,
        )
    )
    logger.debug(
        "{}: after : {}".format(
            "node.testDouble3.z.get()",
            val_z,
        )
    )
    #   dt
    #       matrix
    logger.debug(
        "{}: {}".format(
            "node.testDataMatrix.plug",
            node.testDataMatrix.plug,
        )
    )


def no_auto_add_attr():
    test_str.title(
        "3. extra=True: auto_add_attr=False prevents auto addAttr()"
    )

    node_name = "test_no_auto_add"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    cmds.createNode("transform", name=node_name, skipSelect=True)

    # auto_add_attr=False → addAttr() されない
    modifier_manager = ModifierManager()
    MyTransform(modifier_manager, name=node_name, auto_add_attr=False)

    logger.debug(
        "node.testDouble plug exists (should be False): {}".format(
            cmds.objExists(f"{node_name}.testDouble")
        )
    )


def manual_add_attr_via_plug():
    test_str.title("4. extra=True: manual addAttr() via Plug")

    node_name = "test_manual_add"
    if cmds.objExists(node_name):
        cmds.delete(node_name)

    cmds.createNode("transform", name=node_name, skipSelect=True)

    # auto_add_attr=False でインスタンス化
    modifier_manager = ModifierManager()
    node = MyTransform(
        modifier_manager,
        name=node_name,
        auto_add_attr=False,
    )

    # Plug 経由で任意タイミングに addAttr()
    #   double
    attr = "testDouble"
    logger.debug(
        "node.{} plug exists before add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
    node.testDouble.add_attr()
    logger.debug(
        "node.{} plug exists after manual add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
    # matrix
    attr = "testDataMatrix"
    logger.debug(
        "node.{} plug exists before add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
    node.testDataMatrix.add_attr()
    logger.debug(
        "node.{} plug exists after manual add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
    # enum
    attr = "testEnum"
    logger.debug(
        "node.{} plug exists before add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
    node.testEnum.add_attr()
    logger.debug(
        "node.{} plug exists after manual add_attr(): {}".format(
            attr, cmds.objExists(f"{node_name}.{attr}")
        )
    )
