# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class InputPlugOperator(
    CompoundPlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputTrans", "it"),
        ("inputRotPivot", "irp"),
        ("inputRotTrans", "irt"),
        ("inputMatrix", "im"),
        ("weight", "w"),
    )

    inputTrans = Double3Field()
    it = inputTrans

    inputRotPivot = Double3Field()
    irp = inputRotPivot

    inputRotTrans = Double3Field()
    irt = inputRotTrans

    inputMatrix = GenericField()
    im = inputMatrix

    weight = DoubleField()
    w = weight


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputTrans = Double3Field()
    it = inputTrans

    inputRotPivot = Double3Field()
    irp = inputRotPivot

    inputRotTrans = Double3Field()
    irt = inputRotTrans

    inputMatrix = GenericField()
    im = inputMatrix

    weight = DoubleField()
    w = weight


class InputField(
    CompoundField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class ObjectRotPivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ObjectRotPivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("objectRotPivotX", "orpx"),
        ("objectRotPivotY", "orpy"),
        ("objectRotPivotZ", "orpz"),
    )

    objectRotPivotX = DoubleLinearField()
    orpx = objectRotPivotX

    objectRotPivotY = DoubleLinearField()
    orpy = objectRotPivotY

    objectRotPivotZ = DoubleLinearField()
    orpz = objectRotPivotZ


class ObjectRotPivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ObjectRotPivotPlugOperator]
):
    __slots__ = ()

    objectRotPivotX = DoubleLinearField()
    orpx = objectRotPivotX

    objectRotPivotY = DoubleLinearField()
    orpy = objectRotPivotY

    objectRotPivotZ = DoubleLinearField()
    orpz = objectRotPivotZ


class ObjectRotPivotField(
    DoubleLinear3CompoundBaseField[ObjectRotPivotAttrOperator, ObjectRotPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ObjectRotPivotAttrOperator
    PLUG_CLS = ObjectRotPivotPlugOperator

    objectRotPivotX = DoubleLinearField()
    orpx = objectRotPivotX

    objectRotPivotY = DoubleLinearField()
    orpy = objectRotPivotY

    objectRotPivotZ = DoubleLinearField()
    orpz = objectRotPivotZ


class ObjectRotTransPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ObjectRotTransAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("objectRotTransX", "ortx"),
        ("objectRotTransY", "orty"),
        ("objectRotTransZ", "ortz"),
    )

    objectRotTransX = DoubleLinearField()
    ortx = objectRotTransX

    objectRotTransY = DoubleLinearField()
    orty = objectRotTransY

    objectRotTransZ = DoubleLinearField()
    ortz = objectRotTransZ


class ObjectRotTransAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ObjectRotTransPlugOperator]
):
    __slots__ = ()

    objectRotTransX = DoubleLinearField()
    ortx = objectRotTransX

    objectRotTransY = DoubleLinearField()
    orty = objectRotTransY

    objectRotTransZ = DoubleLinearField()
    ortz = objectRotTransZ


class ObjectRotTransField(
    DoubleLinear3CompoundBaseField[ObjectRotTransAttrOperator, ObjectRotTransPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ObjectRotTransAttrOperator
    PLUG_CLS = ObjectRotTransPlugOperator

    objectRotTransX = DoubleLinearField()
    ortx = objectRotTransX

    objectRotTransY = DoubleLinearField()
    orty = objectRotTransY

    objectRotTransZ = DoubleLinearField()
    ortz = objectRotTransZ


class OutputPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleLinearField()
    ox = outputX

    outputY = DoubleLinearField()
    oy = outputY

    outputZ = DoubleLinearField()
    oz = outputZ


class OutputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputX = DoubleLinearField()
    ox = outputX

    outputY = DoubleLinearField()
    oy = outputY

    outputZ = DoubleLinearField()
    oz = outputZ


class OutputField(
    DoubleLinear3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleLinearField()
    ox = outputX

    outputY = DoubleLinearField()
    oy = outputY

    outputZ = DoubleLinearField()
    oz = outputZ
