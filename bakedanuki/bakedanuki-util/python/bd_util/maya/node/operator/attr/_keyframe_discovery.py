"""Read executed DG dependencies without choosing an editing target."""

from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, TypeVar, cast

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager

if TYPE_CHECKING:
    from ..._versioned_accessors import (  # pyright: ignore[reportMissingModuleSource]
        AnimCurveNode as AnimCurveNode,
    )

CurveNode = TypeVar("CurveNode", bound="AnimCurveNode")


def _leaves(plug: om.MPlug) -> Iterator[om.MPlug]:
    if plug.isArray:
        for index in plug.getExistingArrayAttributeIndices():
            yield from _leaves(plug.elementByLogicalIndex(index))
    elif plug.isCompound:
        for index in range(plug.numChildren()):
            yield from _leaves(plug.child(index))
    else:
        yield plug


def _roots(plug: om.MPlug, *, traverse_inputs: bool) -> list[om.MPlug]:
    roots = [plug]
    names = {plug.name()}
    if plug.isDestination:
        return roots
    node = om.MFnDependencyNode(plug.node())
    if plug.node().hasFn(om.MFn.kAnimCurve):
        if traverse_inputs and plug == node.findPlug("output", False):
            roots.append(node.findPlug("input", False))
        return roots
    # MItDependencyGraph omits internal dependencies of unconsumed outputs.
    attributes: om.MObjectArray = node.getAffectingAttributes(plug.attribute())
    for attribute in attributes:
        parent = om.MFnAttribute(attribute).parent
        while not parent.isNull():
            attribute = parent
            parent = om.MFnAttribute(attribute).parent
        for leaf in _leaves(node.findPlug(attribute, False)):
            # MPlug equality can consider different array elements equal.
            name = leaf.name()
            if name not in names:
                names.add(name)
                roots.append(leaf)
    return roots


def _validate_plug(plug: om.MPlug) -> None:
    handle = om.MObjectHandle(plug.node())
    if not handle.isAlive() or not handle.isValid():
        raise RuntimeError("The discovery plug is not available in the scene.")
    attribute = plug.attribute()
    if (
        plug.isArray
        or plug.isCompound
        or not (
            attribute.hasFn(om.MFn.kNumericAttribute)
            or attribute.hasFn(om.MFn.kUnitAttribute)
            or attribute.hasFn(om.MFn.kEnumAttribute)
        )
    ):
        raise TypeError(
            "Curve discovery requires a scalar numeric or unit plug."
        )


def _upstream(root: om.MPlug) -> om.MItDependencyGraph:
    iterator = om.MItDependencyGraph(
        root,
        om.MFn.kInvalid,
        om.MItDependencyGraph.kUpstream,
        om.MItDependencyGraph.kBreadthFirst,
        om.MItDependencyGraph.kPlugLevel,
        om.MItDependencyGraph.kDependsOn,
    )
    iterator.traversingOverWorldSpaceDependents = True
    return iterator


def has_animation(plug: om.MPlug) -> bool:
    """Keep authored keys and upstream time/expression dependencies, even if constant."""
    _validate_plug(plug)
    for root in _roots(plug, traverse_inputs=True):
        iterator = _upstream(root)
        while not iterator.isDone():
            current: om.MPlug = iterator.currentPlug()
            node = current.node()
            if current.attribute().hasFn(om.MFn.kMessageAttribute):
                iterator.prune()
            elif node.hasFn(om.MFn.kAnimCurve):
                if oma.MFnAnimCurve(node).numKeys:
                    return True
                # An empty curve's time input does not animate its output.
                iterator.prune()
            elif node.hasFn(om.MFn.kTime) or node.hasFn(om.MFn.kExpression):
                return True
            iterator.next()
    return False


def curve_objects(
    plug: om.MPlug, *, traverse_inputs: bool = False
) -> tuple[om.MObject, ...]:
    """Collect upstream curves; sampling also follows animation-driven inputs."""
    _validate_plug(plug)
    objects: list[om.MObject] = []
    # Keep each root MPlug alive until iteration finishes (Maya retains it).
    for root in _roots(plug, traverse_inputs=traverse_inputs):
        iterator = _upstream(root)
        while not iterator.isDone():
            current: om.MPlug = iterator.currentPlug()
            if current.attribute().hasFn(om.MFn.kMessageAttribute):
                iterator.prune()
            elif current.node().hasFn(om.MFn.kAnimCurve):
                node = current.node()
                output = om.MFnDependencyNode(node).findPlug("output", False)
                if current == output:
                    if node not in objects:
                        objects.append(node)
                    if not traverse_inputs:
                        iterator.prune()
                elif current != root and not traverse_inputs:
                    iterator.prune()
            iterator.next()
    return tuple(objects)


def find_anim_curves(
    plug: om.MPlug,
    modifier_manager: ModifierManager | None,
    filter_type: object,
) -> tuple[AnimCurveNode, ...]:
    # Import wrappers after the attribute definitions have been initialized.
    from ...existing_node import ExistingNode
    from ..node._core import NodeOperator

    if filter_type is not None and (
        not isinstance(filter_type, type)
        or not issubclass(filter_type, NodeOperator)
        or filter_type.NODE_TYPE
        not in (
            "animCurveTA",
            "animCurveTL",
            "animCurveTT",
            "animCurveTU",
            "animCurveUA",
            "animCurveUL",
            "animCurveUT",
            "animCurveUU",
        )
    ):
        raise TypeError(
            "filter_type must be a concrete animCurve NodeOperator class."
        )
    objects = curve_objects(plug)

    manager = (
        modifier_manager if modifier_manager is not None else ModifierManager()
    )
    curves = [
        cast("AnimCurveNode", ExistingNode(node, modifier_manager=manager))
        for node in objects
    ]
    curves.sort(key=lambda curve: curve.name)
    return tuple(
        curve
        for curve in curves
        if filter_type is None or isinstance(curve, filter_type)
    )
