# conding: utf-8

# builtin
import importlib.util
from pathlib import Path

# maya
from maya import cmds
from maya.api import OpenMaya as om

# self
from ...... import logger as u_logger
from ..... import str as test_str
from ......_dev.timer import run_timed_repeat, timer
from ......maya.node.modifier import ModifierManager
from ......maya.node.operator.node.dg.plus_minus_average import (
    PlusMinusAverage,
)
from ......maya import scene as u_scene

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

ACCURATE = False
REPEAT_COUNT = 3
INCLUDE_CACHE_CHECK = False
INCLUDE_GET_SET = False
# COUNT = 100000
COUNT = 30000
GET_SET_COUNT = COUNT
SCALAR_VALUE = 1.25
COMPOUND_VALUE = (1.25, 2.5, 3.75)

_PYMEL_VERSIONED_CACHE_NAMES = (
    "mayaApi",
    "mayaCmdsDocs",
    "mayaCmdsExamples",
    "mayaCmdsList",
)
_PYMEL_CACHE_EXTENSIONS = (".py", ".pyc.zip", ".py.zip", ".bin", ".zip")


def main(
    accurate: bool = ACCURATE,
    repeat_count: int = REPEAT_COUNT,
    include_cache_check: bool = INCLUDE_CACHE_CHECK,
    include_get_set: bool = INCLUDE_GET_SET,
):
    u_scene.new_scene()
    # create
    #   one
    test_str.title("処理速度計測(create-one)")
    _run_benchmarks(
        (
            create_one_cmds,
            create_one_pm,
            create_one_om,
            create_one_node_operator,
        ),
        accurate=accurate,
        repeat_count=repeat_count,
    )
    #   many
    test_str.title("処理速度計測(create-many)")
    _run_benchmarks(
        (
            create_many_cmds,
            create_many_pm,
            create_many_om_individual,
            create_many_om_all_together,
            create_many_node_operator,
        ),
        accurate=accurate,
        repeat_count=repeat_count,
    )
    # create_connect
    test_str.title("処理速度計測(create_connect)")
    _run_benchmarks(
        (
            create_connect_cmds,
            create_connect_pm,
            create_connect_om_individual,
            create_connect_om_all_together,
            create_connect_node_operator_connect,
            create_connect_node_operator__gt__,
        ),
        accurate=accurate,
        repeat_count=repeat_count,
    )
    # create_connect_multi
    test_str.title("処理速度計測(create_connect_multi)")
    _run_benchmarks(
        (
            create_connect_multi_cmds,
            create_connect_multi_pm,
            create_connect_multi_om_individual,
            create_connect_multi_om_all_together,
            create_connect_multi_node_operator,
        ),
        accurate=accurate,
        repeat_count=repeat_count,
    )

    if include_cache_check:
        test_str.title("処理速度計測(create_connect_multi_cache)")
        _run_benchmarks(
            (
                create_connect_multi_cmds_xyz,
                create_connect_multi_om_all_together_xyz,
                create_connect_multi_node_operator_natural_src_natural_dst,
                create_connect_multi_node_operator_reuse_src_natural_dst,
                create_connect_multi_node_operator_natural_src_reuse_dst,
                create_connect_multi_node_operator_reuse_src_reuse_dst,
            ),
            accurate=accurate,
            repeat_count=repeat_count,
        )

    if include_get_set:
        _run_get_set_benchmarks(
            accurate=accurate,
            repeat_count=repeat_count,
        )

    # set_key
    test_str.title("処理速度計測(set_key)")
    _run_benchmarks(
        (set_key_node_operator,),
        accurate=accurate,
        repeat_count=repeat_count,
    )


def main_get_set(
    accurate: bool = ACCURATE,
    repeat_count: int = REPEAT_COUNT,
):
    u_scene.new_scene()
    _run_get_set_benchmarks(
        accurate=accurate,
        repeat_count=repeat_count,
    )


def _run_get_set_benchmarks(accurate: bool, repeat_count: int):
    test_str.title("処理速度計測(set-scalar)")
    _run_benchmarks(
        (
            set_scalar_cmds,
            set_scalar_pm,
            set_scalar_om,
            set_scalar_node_operator_reuse_plug,
            set_scalar_node_operator_natural_access,
        ),
        accurate=accurate,
        repeat_count=repeat_count,
    )

    test_str.title("処理速度計測(get-scalar)")
    _run_benchmarks(
        (
            get_scalar_cmds,
            get_scalar_pm,
            get_scalar_om,
            get_scalar_node_operator_reuse_plug,
            get_scalar_node_operator_natural_access,
        ),
        accurate=accurate,
        repeat_count=repeat_count,
    )

    test_str.title("処理速度計測(set-compound)")
    _run_benchmarks(
        (
            set_compound_cmds,
            set_compound_pm,
            set_compound_om,
            set_compound_node_operator_reuse_plug,
            set_compound_node_operator_natural_access,
        ),
        accurate=accurate,
        repeat_count=repeat_count,
    )

    test_str.title("処理速度計測(get-compound)")
    _run_benchmarks(
        (
            get_compound_cmds,
            get_compound_pm,
            get_compound_om,
            get_compound_node_operator_reuse_plug,
            get_compound_node_operator_natural_access,
        ),
        accurate=accurate,
        repeat_count=repeat_count,
    )


def _run_benchmarks(funcs, accurate: bool, repeat_count: int):
    pymel_available = None
    for func in funcs:
        if func.__name__.endswith("_pm"):
            if pymel_available is None:
                pymel_available = _pymel_benchmarks_available()
            if not pymel_available:
                logger.debug(
                    f"[skip] {func.__name__}: PyMEL cache for Maya "
                    f"{_current_maya_version()} is unavailable."
                )
                continue
        _run_benchmark(func, accurate=accurate, repeat_count=repeat_count)


def _pymel_benchmarks_available() -> bool:
    try:
        spec = importlib.util.find_spec("pymel")
    except (ImportError, ValueError):
        return False

    if spec is None or spec.origin is None:
        return False

    cache_dir = Path(spec.origin).parent / "cache"
    maya_version = _current_maya_version()
    return all(
        _pymel_cache_exists(cache_dir, f"{cache_name}{maya_version}")
        for cache_name in _PYMEL_VERSIONED_CACHE_NAMES
    )


def _pymel_cache_exists(cache_dir: Path, cache_name: str) -> bool:
    return any(
        (cache_dir / f"{cache_name}{extension}").is_file()
        for extension in _PYMEL_CACHE_EXTENSIONS
    )


def _current_maya_version() -> str:
    return str(cmds.about(apiVersion=True))[:4]


def _run_benchmark(func, accurate: bool, repeat_count: int):
    if not accurate:
        func()
        return

    run_timed_repeat(func, repeat_count=repeat_count, log_each=False)


def _create_om_value_plugs():
    cmds.file(new=True, force=True)

    mod = om.MDGModifier()
    m_obj = mod.createNode("plusMinusAverage")
    mod.doIt()

    fn_node = om.MFnDependencyNode(m_obj)
    input1d = om.MPlug(
        m_obj,
        fn_node.attribute("input1D"),
    ).elementByLogicalIndex(0)
    input3d = om.MPlug(
        m_obj,
        fn_node.attribute("input3D"),
    ).elementByLogicalIndex(0)
    return mod, input1d, input3d


def _create_node_operator_value_node():
    cmds.file(new=True, force=True)

    modifier_manager = ModifierManager()
    node = PlusMinusAverage.create(modifier_manager)
    modifier_manager.do_it_dg()
    return modifier_manager, node


def _assert_benchmark_total(total: float):
    if total < 0:
        raise RuntimeError(total)


# set/get
@timer
def set_scalar_cmds():
    cmds.file(new=True, force=True)

    node = cmds.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    plug = f"{node}.input1D[0]"
    for _ in range(GET_SET_COUNT):
        cmds.setAttr(plug, SCALAR_VALUE)

    cmds.file(new=True, force=True)


@timer
def set_scalar_pm():
    from pymel import core as pm

    cmds.file(new=True, force=True)

    node = pm.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    plug = node.input1D[0]
    for _ in range(GET_SET_COUNT):
        plug.set(SCALAR_VALUE)

    cmds.file(new=True, force=True)


@timer
def set_scalar_om():
    mod, plug, _ = _create_om_value_plugs()

    for _ in range(GET_SET_COUNT):
        mod.newPlugValueFloat(plug, SCALAR_VALUE)
    mod.doIt()

    cmds.file(new=True, force=True)


@timer
def set_scalar_node_operator_reuse_plug():
    modifier_manager, node = _create_node_operator_value_node()
    plug = node.input1D[0]

    for _ in range(GET_SET_COUNT):
        plug.set(SCALAR_VALUE)
    modifier_manager.do_it_dg()

    cmds.file(new=True, force=True)


@timer
def set_scalar_node_operator_natural_access():
    modifier_manager, node = _create_node_operator_value_node()

    for _ in range(GET_SET_COUNT):
        node.input1D[0].set(SCALAR_VALUE)
    modifier_manager.do_it_dg()

    cmds.file(new=True, force=True)


@timer
def get_scalar_cmds():
    cmds.file(new=True, force=True)

    node = cmds.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    plug = f"{node}.input1D[0]"
    cmds.setAttr(plug, SCALAR_VALUE)

    total = 0.0
    for _ in range(GET_SET_COUNT):
        total += cmds.getAttr(plug)
    _assert_benchmark_total(total)

    cmds.file(new=True, force=True)


@timer
def get_scalar_pm():
    from pymel import core as pm

    cmds.file(new=True, force=True)

    node = pm.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    plug = node.input1D[0]
    plug.set(SCALAR_VALUE)

    total = 0.0
    for _ in range(GET_SET_COUNT):
        total += plug.get()
    _assert_benchmark_total(total)

    cmds.file(new=True, force=True)


@timer
def get_scalar_om():
    mod, plug, _ = _create_om_value_plugs()
    mod.newPlugValueFloat(plug, SCALAR_VALUE)
    mod.doIt()

    total = 0.0
    for _ in range(GET_SET_COUNT):
        total += plug.asFloat()
    _assert_benchmark_total(total)

    cmds.file(new=True, force=True)


@timer
def get_scalar_node_operator_reuse_plug():
    modifier_manager, node = _create_node_operator_value_node()
    plug = node.input1D[0]
    plug.set(SCALAR_VALUE)
    modifier_manager.do_it_dg()

    total = 0.0
    for _ in range(GET_SET_COUNT):
        total += plug.get()
    _assert_benchmark_total(total)

    cmds.file(new=True, force=True)


@timer
def get_scalar_node_operator_natural_access():
    modifier_manager, node = _create_node_operator_value_node()
    node.input1D[0].set(SCALAR_VALUE)
    modifier_manager.do_it_dg()

    total = 0.0
    for _ in range(GET_SET_COUNT):
        total += node.input1D[0].get()
    _assert_benchmark_total(total)

    cmds.file(new=True, force=True)


@timer
def set_compound_cmds():
    cmds.file(new=True, force=True)

    node = cmds.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    plug = f"{node}.input3D[0]"
    for _ in range(GET_SET_COUNT):
        cmds.setAttr(plug, *COMPOUND_VALUE, type="float3")

    cmds.file(new=True, force=True)


@timer
def set_compound_pm():
    from pymel import core as pm

    cmds.file(new=True, force=True)

    node = pm.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    plug = node.input3D[0]
    for _ in range(GET_SET_COUNT):
        plug.set(COMPOUND_VALUE)

    cmds.file(new=True, force=True)


@timer
def set_compound_om():
    mod, _, plug = _create_om_value_plugs()
    child_0 = plug.child(0)
    child_1 = plug.child(1)
    child_2 = plug.child(2)
    x, y, z = COMPOUND_VALUE

    for _ in range(GET_SET_COUNT):
        mod.newPlugValueFloat(child_0, x)
        mod.newPlugValueFloat(child_1, y)
        mod.newPlugValueFloat(child_2, z)
    mod.doIt()

    cmds.file(new=True, force=True)


@timer
def set_compound_node_operator_reuse_plug():
    modifier_manager, node = _create_node_operator_value_node()
    plug = node.input3D[0]
    x, y, z = COMPOUND_VALUE

    for _ in range(GET_SET_COUNT):
        plug.set(x, y, z)
    modifier_manager.do_it_dg()

    cmds.file(new=True, force=True)


@timer
def set_compound_node_operator_natural_access():
    modifier_manager, node = _create_node_operator_value_node()
    x, y, z = COMPOUND_VALUE

    for _ in range(GET_SET_COUNT):
        node.input3D[0].set(x, y, z)
    modifier_manager.do_it_dg()

    cmds.file(new=True, force=True)


@timer
def get_compound_cmds():
    cmds.file(new=True, force=True)

    node = cmds.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    plug = f"{node}.input3D[0]"
    cmds.setAttr(plug, *COMPOUND_VALUE, type="float3")

    total = 0.0
    for _ in range(GET_SET_COUNT):
        x, y, z = cmds.getAttr(plug)[0]
        total += x + y + z
    _assert_benchmark_total(total)

    cmds.file(new=True, force=True)


@timer
def get_compound_pm():
    from pymel import core as pm

    cmds.file(new=True, force=True)

    node = pm.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    plug = node.input3D[0]
    plug.set(COMPOUND_VALUE)

    total = 0.0
    for _ in range(GET_SET_COUNT):
        value = plug.get()
        total += value[0] + value[1] + value[2]
    _assert_benchmark_total(total)

    cmds.file(new=True, force=True)


@timer
def get_compound_om():
    mod, _, plug = _create_om_value_plugs()
    child_0 = plug.child(0)
    child_1 = plug.child(1)
    child_2 = plug.child(2)
    x, y, z = COMPOUND_VALUE
    mod.newPlugValueFloat(child_0, x)
    mod.newPlugValueFloat(child_1, y)
    mod.newPlugValueFloat(child_2, z)
    mod.doIt()

    total = 0.0
    for _ in range(GET_SET_COUNT):
        total += child_0.asFloat() + child_1.asFloat() + child_2.asFloat()
    _assert_benchmark_total(total)

    cmds.file(new=True, force=True)


@timer
def get_compound_node_operator_reuse_plug():
    modifier_manager, node = _create_node_operator_value_node()
    plug = node.input3D[0]
    plug.set(*COMPOUND_VALUE)
    modifier_manager.do_it_dg()

    total = 0.0
    for _ in range(GET_SET_COUNT):
        value = plug.get()
        total += value[0] + value[1] + value[2]
    _assert_benchmark_total(total)

    cmds.file(new=True, force=True)


@timer
def get_compound_node_operator_natural_access():
    modifier_manager, node = _create_node_operator_value_node()
    node.input3D[0].set(*COMPOUND_VALUE)
    modifier_manager.do_it_dg()

    total = 0.0
    for _ in range(GET_SET_COUNT):
        value = node.input3D[0].get()
        total += value[0] + value[1] + value[2]
    _assert_benchmark_total(total)

    cmds.file(new=True, force=True)


# create
@timer
def create_one_cmds():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    cmds.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_one_pm():
    from pymel import core as pm

    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    pm.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_one_om():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    mod = om.MDGModifier()
    mod.createNode("plusMinusAverage")
    mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_one_node_operator():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    modifier_manager = ModifierManager()
    PlusMinusAverage.create(modifier_manager)
    modifier_manager.do_it_dg()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_many_cmds():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    for _ in range(COUNT):
        cmds.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_many_pm():
    from pymel import core as pm

    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    for _ in range(COUNT):
        pm.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_many_om_individual():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    mod = om.MDGModifier()
    for _ in range(COUNT):
        mod.createNode("plusMinusAverage")
        mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_many_om_all_together():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    mod = om.MDGModifier()
    for _ in range(COUNT):
        mod.createNode("plusMinusAverage")
    mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_many_node_operator():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成
    modifier_manager = ModifierManager()
    for _ in range(COUNT):
        PlusMinusAverage.create(modifier_manager)
    modifier_manager.do_it_dg()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


# create_connect
@timer
def create_connect_cmds():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    parent_node = None
    for _ in range(COUNT):
        # ノードを作成
        node = cmds.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
        # ノードを接続
        if parent_node is not None:
            cmds.connectAttr(
                f"{parent_node}.output3Dx",
                f"{node}.input3D[0].input3Dx",
            )
        # parent を置き換え
        parent_node = node

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_pm():
    from pymel import core as pm

    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    parent_node = None
    for _ in range(COUNT):
        # ノードを作成
        node = pm.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
        # ノードを接続
        if parent_node is not None:
            parent_node.output3Dx >> node.input3D[0].input3Dx
        # parent を置き換え
        parent_node = node

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_om_individual():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    mod = om.MDGModifier()
    parent_m_obj = None
    for _ in range(COUNT):
        # ノードを作成
        m_obj = mod.createNode("plusMinusAverage")
        # ノードを接続
        if parent_m_obj is not None:
            src = om.MPlug(
                om.MObject(parent_m_obj),
                om.MFnDependencyNode(parent_m_obj).attribute("output3Dx"),
            )
            array_plug = om.MPlug(
                m_obj, om.MFnDependencyNode(m_obj).attribute("input3D")
            )
            dst = array_plug.elementByLogicalIndex(0).child(0)
            mod.connect(src, dst)
        mod.doIt()
        # parent を置き換え
        parent_m_obj = m_obj

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_om_all_together():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    mod = om.MDGModifier()
    parent_m_obj = None
    for _ in range(COUNT):
        # ノードを作成
        m_obj = mod.createNode("plusMinusAverage")
        # ノードを接続
        if parent_m_obj is not None:
            src = om.MPlug(
                om.MObject(parent_m_obj),
                om.MFnDependencyNode(parent_m_obj).attribute("output3Dx"),
            )
            array_plug = om.MPlug(
                m_obj, om.MFnDependencyNode(m_obj).attribute("input3D")
            )
            dst = array_plug.elementByLogicalIndex(0).child(0)
            mod.connect(src, dst)
        # parent を置き換え
        parent_m_obj = m_obj
    mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_node_operator_connect():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    modifier_manager = ModifierManager()
    parent_node = None
    for _ in range(COUNT):
        # ノードを作成
        node = PlusMinusAverage.create(modifier_manager)
        # ノードを接続
        if parent_node is not None:
            parent_node.output3Dx.connect(node.input3D[0].input3Dx)
        # parent を置き換え
        parent_node = node
    modifier_manager.do_it_dg()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_node_operator__gt__():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    modifier_manager = ModifierManager()
    parent_node = None
    for _ in range(COUNT):
        # ノードを作成
        node = PlusMinusAverage.create(modifier_manager)
        # ノードを接続
        if parent_node is not None:
            parent_node.output3Dx > node.input3D[0].input3Dx
        # parent を置き換え
        parent_node = node
    modifier_manager.do_it_dg()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


# create_connect_multi
@timer
def create_connect_multi_cmds():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    src = cmds.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    for _ in range(COUNT):
        # ノードを作成
        dst = cmds.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
        # ノードを接続
        cmds.connectAttr(
            f"{src}.output3Dx",
            f"{dst}.input3D[0].input3Dx",
        )

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_multi_pm():
    from pymel import core as pm

    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    src = pm.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    for _ in range(COUNT):
        # ノードを作成
        dst = pm.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
        # ノードを接続
        src.output3Dx >> dst.input3D[0].input3Dx

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_multi_om_individual():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    mod = om.MDGModifier()
    src_m_obj = mod.createNode("plusMinusAverage")
    for _ in range(COUNT):
        # ノードを作成
        dst_m_obj = mod.createNode("plusMinusAverage")
        # ノードを接続
        src = om.MPlug(
            om.MObject(src_m_obj),
            om.MFnDependencyNode(src_m_obj).attribute("output3Dx"),
        )
        array_plug = om.MPlug(
            dst_m_obj, om.MFnDependencyNode(dst_m_obj).attribute("input3D")
        )
        dst = array_plug.elementByLogicalIndex(0).child(0)
        mod.connect(src, dst)
        mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_multi_om_all_together():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    mod = om.MDGModifier()
    src_m_obj = mod.createNode("plusMinusAverage")
    for _ in range(COUNT):
        # ノードを作成
        dst_m_obj = mod.createNode("plusMinusAverage")
        # ノードを接続
        src = om.MPlug(
            om.MObject(src_m_obj),
            om.MFnDependencyNode(src_m_obj).attribute("output3Dx"),
        )
        array_plug = om.MPlug(
            dst_m_obj, om.MFnDependencyNode(dst_m_obj).attribute("input3D")
        )
        dst = array_plug.elementByLogicalIndex(0).child(0)
        mod.connect(src, dst)
    mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_multi_cmds_xyz():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    src = cmds.createNode(
        "plusMinusAverage",
        skipSelect=True,
    )
    for _ in range(COUNT):
        # ノードを作成
        dst = cmds.createNode(
            "plusMinusAverage",
            skipSelect=True,
        )
        # ノードを接続
        cmds.connectAttr(
            f"{src}.output3Dx",
            f"{dst}.input3D[0].input3Dx",
        )
        cmds.connectAttr(
            f"{src}.output3Dx",
            f"{dst}.input3D[0].input3Dy",
        )
        cmds.connectAttr(
            f"{src}.output3Dx",
            f"{dst}.input3D[0].input3Dz",
        )

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_multi_om_all_together_xyz():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    mod = om.MDGModifier()
    src_m_obj = mod.createNode("plusMinusAverage")
    src = om.MPlug(
        om.MObject(src_m_obj),
        om.MFnDependencyNode(src_m_obj).attribute("output3Dx"),
    )
    for _ in range(COUNT):
        # ノードを作成
        dst_m_obj = mod.createNode("plusMinusAverage")
        # ノードを接続
        dst_array_plug = om.MPlug(
            dst_m_obj, om.MFnDependencyNode(dst_m_obj).attribute("input3D")
        )
        dst_input_plug = dst_array_plug.elementByLogicalIndex(0)
        mod.connect(src, dst_input_plug.child(0))
        mod.connect(src, dst_input_plug.child(1))
        mod.connect(src, dst_input_plug.child(2))
    mod.doIt()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_multi_node_operator():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    modifier_manager = ModifierManager()
    src_node = PlusMinusAverage.create(modifier_manager)
    for _ in range(COUNT):
        # ノードを作成
        dst_node = PlusMinusAverage.create(modifier_manager)
        # ノードを接続
        src_node.output3Dx > dst_node.input3D[0].input3Dx
    modifier_manager.do_it_dg()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_multi_node_operator_natural_src_natural_dst():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    modifier_manager = ModifierManager()
    src_node = PlusMinusAverage.create(modifier_manager)
    for _ in range(COUNT):
        # ノードを作成
        dst_node = PlusMinusAverage.create(modifier_manager)
        # ノードを接続
        src_node.output3Dx > dst_node.input3D[0].input3Dx
        src_node.output3Dx > dst_node.input3D[0].input3Dy
        src_node.output3Dx > dst_node.input3D[0].input3Dz
    modifier_manager.do_it_dg()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_multi_node_operator_reuse_src_natural_dst():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    modifier_manager = ModifierManager()
    src_node = PlusMinusAverage.create(modifier_manager)
    src_plug = src_node.output3Dx
    for _ in range(COUNT):
        # ノードを作成
        dst_node = PlusMinusAverage.create(modifier_manager)
        # ノードを接続
        src_plug > dst_node.input3D[0].input3Dx
        src_plug > dst_node.input3D[0].input3Dy
        src_plug > dst_node.input3D[0].input3Dz
    modifier_manager.do_it_dg()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_multi_node_operator_natural_src_reuse_dst():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    modifier_manager = ModifierManager()
    src_node = PlusMinusAverage.create(modifier_manager)
    for _ in range(COUNT):
        # ノードを作成
        dst_node = PlusMinusAverage.create(modifier_manager)
        dst_input = dst_node.input3D[0]
        # ノードを接続
        src_node.output3Dx > dst_input.input3Dx
        src_node.output3Dx > dst_input.input3Dy
        src_node.output3Dx > dst_input.input3Dz
    modifier_manager.do_it_dg()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


@timer
def create_connect_multi_node_operator_reuse_src_reuse_dst():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    modifier_manager = ModifierManager()
    src_node = PlusMinusAverage.create(modifier_manager)
    src_plug = src_node.output3Dx
    for _ in range(COUNT):
        # ノードを作成
        dst_node = PlusMinusAverage.create(modifier_manager)
        dst_input = dst_node.input3D[0]
        # ノードを接続
        src_plug > dst_input.input3Dx
        src_plug > dst_input.input3Dy
        src_plug > dst_input.input3Dz
    modifier_manager.do_it_dg()

    # 新規シーンを開く
    cmds.file(new=True, force=True)


# set_key
@timer
def set_key_node_operator():
    # 新規シーンを開く
    cmds.file(new=True, force=True)

    # ノードを作成し接続
    modifier_manager = ModifierManager()
    node = PlusMinusAverage.create(modifier_manager)
    modifier_manager.do_it_dg()
    plug = node.input3D[0].input3Dx
    for i in range(COUNT):
        plug.keyframe.set_direct(i, i)
    modifier_manager.do_it_dg()

    # 新規シーンを開く
    cmds.file(new=True, force=True)
