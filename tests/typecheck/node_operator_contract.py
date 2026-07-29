from typing import Literal, assert_type

import bd_util as bdu
from maya.api import OpenMaya as om

from bd_util.maya.node.operator.attr import KeyframeManager
from bd_util.maya.node.operator.attr.define.node_attr.compose_matrix import (
    InputTranslateAttrOperator,
    InputTranslatePlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.wt_add_matrix import (
    WtMatrixAttrOperator,
    WtMatrixPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.matrix import (
    MatrixAttrOperator,
    MatrixPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar._base import (
    ScalarBaseAttrOperator,
    ScalarBasePlugOperator,
    ScalarBaseField,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.unit import (
    double_linear,
)
from bd_util.maya.node.operator.attr.define.std.dt.matrix import (
    DataMatrixPlugOperator,
)
from bd_util.maya.node.operator.node._core import NodeOperator
from bd_util.maya.node.operator.node.dg._generated.compose_matrix import (
    InputRotateOrderEnumAttrOperator,
    InputRotateOrderEnumPlugOperator,
    InputRotateOrderEnumField,
)
from bd_util.maya.node.operator.node.dg.compose_matrix import ComposeMatrix
from bd_util.maya.node.operator.node.dg.decompose_matrix import (
    DecomposeMatrix,
)
from bd_util.maya.node.operator.node.dg.wt_add_matrix import WtAddMatrix


def node_accessor_contract(nodes: bdu.Nodes) -> None:
    compose = nodes.create.composeMatrix(name="compose")
    assert_type(compose, ComposeMatrix)

    decompose = nodes.existing.decomposeMatrix("decompose")
    assert_type(decompose, DecomposeMatrix)

    existing = nodes.existing("existing_node")
    assert_type(existing, NodeOperator)


def descriptor_contract(compose: ComposeMatrix) -> None:
    assert_type(ComposeMatrix.outputMatrix, MatrixAttrOperator)
    assert_type(compose.outputMatrix, MatrixPlugOperator)
    assert_type(compose.omat, MatrixPlugOperator)
    assert_type(compose.outputMatrix.get(), om.MMatrix)

    assert_type(ComposeMatrix.inputTranslate, InputTranslateAttrOperator)
    assert_type(compose.inputTranslate, InputTranslatePlugOperator)
    assert_type(
        compose.inputTranslate.inputTranslateX,
        double_linear.DoubleLinearPlugOperator,
    )
    assert_type(compose.inputTranslate.inputTranslateX.get(), float)
    assert_type(compose.inputTranslate.get(), bdu.DoubleLinear3)
    assert_type(compose.inputTranslate.value, bdu.DoubleLinear3)
    assert_type(compose.inputTranslate.value_direct, bdu.DoubleLinear3)
    assert_type(compose.inputTranslate.get().x, float)
    assert_type(
        compose.inputTranslate.get().as_tuple(),
        tuple[float, float, float],
    )
    assert_type(
        compose.inputTranslate.inputTranslateX.keyframe,
        KeyframeManager,
    )

    assert_type(
        ComposeMatrix.inputRotateOrder,
        InputRotateOrderEnumAttrOperator,
    )
    assert_type(
        compose.inputRotateOrder,
        InputRotateOrderEnumPlugOperator,
    )
    assert_type(compose.inputRotateOrder.XYZ, Literal[0])
    assert_type(compose.inputRotateOrder.keyframe, KeyframeManager)


def scalar_base_contract(
    attr: InputRotateOrderEnumAttrOperator,
    plug: InputRotateOrderEnumPlugOperator,
    field: InputRotateOrderEnumField,
) -> None:
    scalar_attr: ScalarBaseAttrOperator[InputRotateOrderEnumPlugOperator] = (
        attr
    )
    scalar_plug: ScalarBasePlugOperator[InputRotateOrderEnumAttrOperator] = (
        plug
    )
    scalar_field: ScalarBaseField[
        InputRotateOrderEnumAttrOperator,
        InputRotateOrderEnumPlugOperator,
    ] = field

    assert_type(
        scalar_attr,
        InputRotateOrderEnumAttrOperator,
    )
    assert_type(
        scalar_plug,
        InputRotateOrderEnumPlugOperator,
    )
    assert_type(
        scalar_field,
        InputRotateOrderEnumField,
    )


def multi_compound_contract(nodes: bdu.Nodes) -> None:
    wt_add_matrix = nodes.create.wtAddMatrix(name="wt_add_matrix")
    assert_type(wt_add_matrix, WtAddMatrix)

    assert_type(WtAddMatrix.wtMatrix, WtMatrixAttrOperator)
    assert_type(wt_add_matrix.wtMatrix, WtMatrixPlugOperator)
    assert_type(wt_add_matrix.wtMatrix[0], WtMatrixPlugOperator)
    assert_type(wt_add_matrix.wtMatrix[next], WtMatrixPlugOperator)
    assert_type(
        wt_add_matrix.wtMatrix[next].matrixIn,
        DataMatrixPlugOperator,
    )
    assert_type(
        wt_add_matrix.wtMatrix[next].matrixIn.get(),
        om.MMatrix | None,
    )


def invalid_usage_contract(
    nodes: bdu.Nodes,
    compose: ComposeMatrix,
) -> None:
    nodes.create.composeMatrix(
        unknown_option=True
    )  # pyright: ignore[reportCallIssue]
    nodes.existing.decomposeMatrix(123)  # pyright: ignore[reportArgumentType]
    compose.outputMatrix.set(
        "not a matrix"
    )  # pyright: ignore[reportArgumentType]
    compose.inputTranslate.set(
        "not a vector"
    )  # pyright: ignore[reportArgumentType]
    nodes.create.wtAddMatrix().wtMatrix[
        len
    ]  # pyright: ignore[reportArgumentType]
    compose.does_not_exist  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
