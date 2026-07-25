# coding: utf-8
from __future__ import annotations

from importlib import metadata
from typing import Any

from maya import cmds
from maya.api import OpenMaya as om

from ._core import (
    AdapterUnavailable,
    BaseBenchmarkAdapter,
    OperationResult,
    UnsupportedScenario,
)


_BATCHED_MODES = {
    "scalar_set": "batched",
    "create_nodes": "batched",
    "create_connect_chain": "batched",
    "matrix_graph": "batched",
}

_HYBRID_MODES = {
    "scalar_set": "batched",
    "create_nodes": "hybrid",
    "create_connect_chain": "hybrid",
    "matrix_graph": "hybrid",
}


def default_adapters() -> list[BaseBenchmarkAdapter]:
    return [
        CmdsAdapter(),
        OpenMayaAdapter(),
        NodeOperatorAdapter(),
        PyMELAdapter(),
        CymelAdapter(),
        CmdxAdapter(),
        AlOmxAdapter(),
    ]


class CmdsAdapter(BaseBenchmarkAdapter):
    name = "maya.cmds"

    def load(self) -> None:
        self.version = str(cmds.about(version=True))

    def run_scenario(
        self,
        scenario_name: str,
        count: int,
        state: dict[str, Any],
    ) -> OperationResult:
        if scenario_name == "wrap_existing":
            raise UnsupportedScenario(
                "maya.cmds has no node wrapper equivalent"
            )
        return super().run_scenario(scenario_name, count, state)

    def wrap_node(self, node_name: str) -> str:
        return node_name

    def scalar_plug(self, node: str) -> str:
        return f"{node}.input1X"

    def read_scalar(self, plug: str) -> float:
        return cmds.getAttr(plug)

    def set_scalar_repeated(
        self,
        plug: str,
        count: int,
        value: float,
    ) -> None:
        for _ in range(count):
            cmds.setAttr(plug, value)

    def create_nodes(self, count: int) -> OperationResult:
        for _ in range(count):
            cmds.createNode("multiplyDivide", skipSelect=True)
        return OperationResult()

    def create_connect_chain(self, count: int) -> OperationResult:
        previous = None
        last_destination = None
        for _ in range(count):
            node = cmds.createNode("multiplyDivide", skipSelect=True)
            if previous is not None:
                last_destination = f"{node}.input1X"
                cmds.connectAttr(f"{previous}.outputX", last_destination)
            previous = node
        return OperationResult(last_destination=last_destination)

    def create_matrix_graph(self, count: int) -> OperationResult:
        last_destination = None
        for _ in range(count):
            compose = cmds.createNode("composeMatrix", skipSelect=True)
            mult = cmds.createNode("multMatrix", skipSelect=True)
            decompose = cmds.createNode("decomposeMatrix", skipSelect=True)
            cmds.connectAttr(
                f"{compose}.outputMatrix",
                f"{mult}.matrixIn[0]",
            )
            last_destination = f"{decompose}.inputMatrix"
            cmds.connectAttr(f"{mult}.matrixSum", last_destination)
        return OperationResult(last_destination=last_destination)


class OpenMayaAdapter(BaseBenchmarkAdapter):
    name = "OpenMaya"
    execution_modes = _BATCHED_MODES

    def load(self) -> None:
        self.version = str(cmds.about(apiVersion=True))

    def wrap_node(self, node_name: str) -> om.MFnDependencyNode:
        selection = om.MSelectionList()
        selection.add(node_name)
        return om.MFnDependencyNode(selection.getDependNode(0))

    def scalar_plug(self, node: om.MFnDependencyNode) -> om.MPlug:
        return om.MPlug(node.object(), node.attribute("input1X"))

    def read_scalar(self, plug: om.MPlug) -> float:
        return plug.asFloat()

    def set_scalar_repeated(
        self,
        plug: om.MPlug,
        count: int,
        value: float,
    ) -> None:
        modifier = om.MDGModifier()
        for _ in range(count):
            modifier.newPlugValueFloat(plug, value)
        modifier.doIt()

    def create_nodes(self, count: int) -> OperationResult:
        modifier = om.MDGModifier()
        for _ in range(count):
            modifier.createNode("multiplyDivide")
        modifier.doIt()
        return OperationResult()

    def create_connect_chain(self, count: int) -> OperationResult:
        modifier = om.MDGModifier()
        previous = None
        last_destination = None
        for _ in range(count):
            node = modifier.createNode("multiplyDivide")
            if previous is not None:
                source = _om_plug(previous, "outputX")
                destination = _om_plug(node, "input1X")
                modifier.connect(source, destination)
                last_destination = destination
            previous = node
        modifier.doIt()
        return OperationResult(
            last_destination=(
                last_destination.name()
                if last_destination is not None
                else None
            )
        )

    def create_matrix_graph(self, count: int) -> OperationResult:
        modifier = om.MDGModifier()
        last_destination = None
        for _ in range(count):
            compose = modifier.createNode("composeMatrix")
            mult = modifier.createNode("multMatrix")
            decompose = modifier.createNode("decomposeMatrix")
            matrix_in = _om_plug(mult, "matrixIn").elementByLogicalIndex(0)
            destination = _om_plug(decompose, "inputMatrix")
            modifier.connect(_om_plug(compose, "outputMatrix"), matrix_in)
            modifier.connect(_om_plug(mult, "matrixSum"), destination)
            last_destination = destination
        modifier.doIt()
        return OperationResult(
            last_destination=(
                last_destination.name()
                if last_destination is not None
                else None
            )
        )


class NodeOperatorAdapter(BaseBenchmarkAdapter):
    name = "NodeOperator"
    execution_modes = _BATCHED_MODES

    def load(self) -> None:
        import bd_util
        from bd_util.maya.node.modifier import ModifierManager
        from bd_util.maya.node.nodes import Nodes

        self.version = bd_util.__version__
        self._modifier_manager_cls = ModifierManager
        self._nodes_cls = Nodes

    def setup_scenario(self, scenario_name: str) -> dict[str, Any]:
        if scenario_name in {
            "wrap_existing",
            "plug_access",
            "scalar_get",
            "scalar_set",
        }:
            self._active_modifier = self._modifier_manager_cls()
            self._active_nodes = self._nodes_cls(
                modifier_manager=self._active_modifier
            )
        return super().setup_scenario(scenario_name)

    def wrap_node(self, node_name: str) -> Any:
        return self._active_nodes.existing.multiplyDivide(node_name)

    def scalar_plug(self, node: Any) -> Any:
        return node.input1X

    def read_scalar(self, plug: Any) -> float:
        return plug.get()

    def set_scalar_repeated(
        self,
        plug: Any,
        count: int,
        value: float,
    ) -> None:
        for _ in range(count):
            plug.set(value)
        self._active_modifier.do_it_dg()

    def create_nodes(self, count: int) -> OperationResult:
        modifier = self._modifier_manager_cls()
        nodes = self._nodes_cls(modifier_manager=modifier)
        for _ in range(count):
            nodes.create.multiplyDivide()
        modifier.do_it_dg()
        return OperationResult()

    def create_connect_chain(self, count: int) -> OperationResult:
        modifier = self._modifier_manager_cls()
        nodes = self._nodes_cls(modifier_manager=modifier)
        previous = None
        last_destination = None
        for _ in range(count):
            node = nodes.create.multiplyDivide()
            if previous is not None:
                last_destination = node.input1X
                previous.outputX.connect(last_destination)
            previous = node
        modifier.do_it_dg()
        return OperationResult(
            last_destination=(
                str(last_destination)
                if last_destination is not None
                else None
            )
        )

    def create_matrix_graph(self, count: int) -> OperationResult:
        modifier = self._modifier_manager_cls()
        nodes = self._nodes_cls(modifier_manager=modifier)
        last_destination = None
        for _ in range(count):
            compose = nodes.create.composeMatrix()
            mult = nodes.create.multMatrix()
            decompose = nodes.create.decomposeMatrix()
            compose.outputMatrix.connect(mult.matrixIn[0])
            mult.matrixSum.connect(decompose.inputMatrix)
            last_destination = decompose.inputMatrix
        modifier.do_it_dg()
        return OperationResult(
            last_destination=(
                str(last_destination)
                if last_destination is not None
                else None
            )
        )


class PyMELAdapter(BaseBenchmarkAdapter):
    name = "PyMEL"

    def load(self) -> None:
        from .. import process_speed

        if not process_speed._pymel_benchmarks_available():
            raise AdapterUnavailable(
                "PyMEL cache for this Maya version is unavailable"
            )

        import pymel
        from pymel import core as pm

        self.version = _package_version("pymel")
        self._pm = pm

    def wrap_node(self, node_name: str) -> Any:
        return self._pm.PyNode(node_name)

    def scalar_plug(self, node: Any) -> Any:
        return node.input1X

    def read_scalar(self, plug: Any) -> float:
        return plug.get()

    def set_scalar_repeated(
        self,
        plug: Any,
        count: int,
        value: float,
    ) -> None:
        for _ in range(count):
            plug.set(value)

    def create_nodes(self, count: int) -> OperationResult:
        for _ in range(count):
            self._pm.createNode("multiplyDivide", skipSelect=True)
        return OperationResult()

    def create_connect_chain(self, count: int) -> OperationResult:
        previous = None
        last_destination = None
        for _ in range(count):
            node = self._pm.createNode(
                "multiplyDivide",
                skipSelect=True,
            )
            if previous is not None:
                last_destination = node.input1X
                previous.outputX.connect(last_destination)
            previous = node
        return OperationResult(
            last_destination=(
                last_destination.name()
                if last_destination is not None
                else None
            )
        )

    def create_matrix_graph(self, count: int) -> OperationResult:
        last_destination = None
        for _ in range(count):
            compose = self._pm.createNode(
                "composeMatrix",
                skipSelect=True,
            )
            mult = self._pm.createNode("multMatrix", skipSelect=True)
            decompose = self._pm.createNode(
                "decomposeMatrix",
                skipSelect=True,
            )
            compose.outputMatrix.connect(mult.matrixIn[0])
            mult.matrixSum.connect(decompose.inputMatrix)
            last_destination = decompose.inputMatrix
        return OperationResult(
            last_destination=(
                last_destination.name()
                if last_destination is not None
                else None
            )
        )


class CymelAdapter(BaseBenchmarkAdapter):
    name = "cymel"

    def load(self) -> None:
        import cymel
        import cymel.main as cm

        self.version = cymel.__version__
        self._cm = cm

    def wrap_node(self, node_name: str) -> Any:
        return self._cm.CyObject(node_name)

    def scalar_plug(self, node: Any) -> Any:
        return node.input1X

    def read_scalar(self, plug: Any) -> float:
        return plug.get()

    def set_scalar_repeated(
        self,
        plug: Any,
        count: int,
        value: float,
    ) -> None:
        for _ in range(count):
            plug.set(value)

    def create_nodes(self, count: int) -> OperationResult:
        for _ in range(count):
            self._cm.nt.MultiplyDivide()
        return OperationResult()

    def create_connect_chain(self, count: int) -> OperationResult:
        previous = None
        last_destination = None
        for _ in range(count):
            node = self._cm.nt.MultiplyDivide()
            if previous is not None:
                last_destination = node.input1X
                last_destination.connect(previous.outputX)
            previous = node
        return OperationResult(
            last_destination=(
                str(last_destination)
                if last_destination is not None
                else None
            )
        )

    def create_matrix_graph(self, count: int) -> OperationResult:
        last_destination = None
        for _ in range(count):
            compose = self._cm.nt.ComposeMatrix()
            mult = self._cm.nt.MultMatrix()
            decompose = self._cm.nt.DecomposeMatrix()
            mult.matrixIn[0].connect(compose.outputMatrix)
            decompose.inputMatrix.connect(mult.matrixSum)
            last_destination = decompose.inputMatrix
        return OperationResult(
            last_destination=(
                str(last_destination)
                if last_destination is not None
                else None
            )
        )


class CmdxAdapter(BaseBenchmarkAdapter):
    name = "cmdx"
    execution_modes = _HYBRID_MODES

    def load(self) -> None:
        import cmdx

        self.version = cmdx.__version__
        self._cmdx = cmdx

    def wrap_node(self, node_name: str) -> Any:
        return self._cmdx.encode(node_name)

    def scalar_plug(self, node: Any) -> Any:
        return node["input1X"]

    def read_scalar(self, plug: Any) -> float:
        return plug.read()

    def set_scalar_repeated(
        self,
        plug: Any,
        count: int,
        value: float,
    ) -> None:
        modifier = self._cmdx.DGModifier()
        for _ in range(count):
            modifier.setAttr(plug, value)
        modifier.doIt()

    def create_nodes(self, count: int) -> OperationResult:
        modifier = self._cmdx.DGModifier()
        for _ in range(count):
            modifier.createNode("multiplyDivide")
        modifier.doIt()
        return OperationResult()

    def create_connect_chain(self, count: int) -> OperationResult:
        modifier = self._cmdx.DGModifier()
        previous = None
        last_destination = None
        for _ in range(count):
            node = modifier.createNode("multiplyDivide")
            if previous is not None:
                last_destination = node["input1X"]
                modifier.connect(previous["outputX"], last_destination)
            previous = node
        modifier.doIt()
        return OperationResult(
            last_destination=(
                last_destination.path()
                if last_destination is not None
                else None
            )
        )

    def create_matrix_graph(self, count: int) -> OperationResult:
        modifier = self._cmdx.DGModifier()
        last_destination = None
        for _ in range(count):
            compose = modifier.createNode("composeMatrix")
            mult = modifier.createNode("multMatrix")
            decompose = modifier.createNode("decomposeMatrix")
            modifier.connect(
                compose["outputMatrix"],
                mult["matrixIn"][0],
            )
            modifier.connect(
                mult["matrixSum"],
                decompose["inputMatrix"],
            )
            last_destination = decompose["inputMatrix"]
        modifier.doIt()
        return OperationResult(
            last_destination=(
                last_destination.path()
                if last_destination is not None
                else None
            )
        )


class AlOmxAdapter(BaseBenchmarkAdapter):
    name = "AL_omx"
    execution_modes = _HYBRID_MODES

    def load(self) -> None:
        from AL import omx

        self.version = _package_version("AL-omx")
        self._omx = omx

    def wrap_node(self, node_name: str) -> Any:
        return self._omx.XNode(node_name)

    def scalar_plug(self, node: Any) -> Any:
        return node.input1X

    def read_scalar(self, plug: Any) -> float:
        return plug.get()

    def set_scalar_repeated(
        self,
        plug: Any,
        count: int,
        value: float,
    ) -> None:
        modifier = self._omx.XModifier()
        for _ in range(count):
            modifier.newPlugValueFloat(plug, value)
        modifier.doIt()

    def create_nodes(self, count: int) -> OperationResult:
        modifier = self._omx.XModifier()
        for _ in range(count):
            modifier.createDGNode("multiplyDivide")
        modifier.doIt()
        return OperationResult()

    def create_connect_chain(self, count: int) -> OperationResult:
        modifier = self._omx.XModifier()
        previous = None
        last_destination = None
        for _ in range(count):
            node = modifier.createDGNode("multiplyDivide")
            if previous is not None:
                last_destination = node.input1X
                modifier.connect(previous.outputX, last_destination)
            previous = node
        modifier.doIt()
        return OperationResult(
            last_destination=(
                str(last_destination)
                if last_destination is not None
                else None
            )
        )

    def create_matrix_graph(self, count: int) -> OperationResult:
        modifier = self._omx.XModifier()
        last_destination = None
        for _ in range(count):
            compose = modifier.createDGNode("composeMatrix")
            mult = modifier.createDGNode("multMatrix")
            decompose = modifier.createDGNode("decomposeMatrix")
            modifier.connect(
                compose.outputMatrix,
                mult.matrixIn.elementByLogicalIndex(0),
            )
            modifier.connect(mult.matrixSum, decompose.inputMatrix)
            last_destination = decompose.inputMatrix
        modifier.doIt()
        return OperationResult(
            last_destination=(
                str(last_destination)
                if last_destination is not None
                else None
            )
        )


def _om_plug(node: om.MObject, attribute_name: str) -> om.MPlug:
    function_set = om.MFnDependencyNode(node)
    return om.MPlug(node, function_set.attribute(attribute_name))


def _package_version(distribution_name: str) -> str:
    try:
        return metadata.version(distribution_name)
    except metadata.PackageNotFoundError:
        return "unknown"
