# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
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

    inputTrans = Double3Field(default_value=(0.0, 0.0, 0.0))
    it = inputTrans

    inputRotPivot = Double3Field(default_value=(0.0, 0.0, 0.0))
    irp = inputRotPivot

    inputRotTrans = Double3Field(default_value=(0.0, 0.0, 0.0))
    irt = inputRotTrans

    inputMatrix = GenericField()
    im = inputMatrix

    weight = DoubleField(default_value=1.0)
    w = weight


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputTrans = Double3Field(default_value=(0.0, 0.0, 0.0))
    it = inputTrans

    inputRotPivot = Double3Field(default_value=(0.0, 0.0, 0.0))
    irp = inputRotPivot

    inputRotTrans = Double3Field(default_value=(0.0, 0.0, 0.0))
    irt = inputRotTrans

    inputMatrix = GenericField()
    im = inputMatrix

    weight = DoubleField(default_value=1.0)
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

    objectRotPivotX = DoubleLinearField(default_value=0.0)
    orpx = objectRotPivotX

    objectRotPivotY = DoubleLinearField(default_value=0.0)
    orpy = objectRotPivotY

    objectRotPivotZ = DoubleLinearField(default_value=0.0)
    orpz = objectRotPivotZ


class ObjectRotPivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ObjectRotPivotPlugOperator]
):
    __slots__ = ()

    objectRotPivotX = DoubleLinearField(default_value=0.0)
    orpx = objectRotPivotX

    objectRotPivotY = DoubleLinearField(default_value=0.0)
    orpy = objectRotPivotY

    objectRotPivotZ = DoubleLinearField(default_value=0.0)
    orpz = objectRotPivotZ


class ObjectRotPivotField(
    DoubleLinear3CompoundBaseField[ObjectRotPivotAttrOperator, ObjectRotPivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ObjectRotPivotAttrOperator
    PLUG_CLS = ObjectRotPivotPlugOperator

    objectRotPivotX = DoubleLinearField(default_value=0.0)
    orpx = objectRotPivotX

    objectRotPivotY = DoubleLinearField(default_value=0.0)
    orpy = objectRotPivotY

    objectRotPivotZ = DoubleLinearField(default_value=0.0)
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

    objectRotTransX = DoubleLinearField(default_value=0.0)
    ortx = objectRotTransX

    objectRotTransY = DoubleLinearField(default_value=0.0)
    orty = objectRotTransY

    objectRotTransZ = DoubleLinearField(default_value=0.0)
    ortz = objectRotTransZ


class ObjectRotTransAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ObjectRotTransPlugOperator]
):
    __slots__ = ()

    objectRotTransX = DoubleLinearField(default_value=0.0)
    ortx = objectRotTransX

    objectRotTransY = DoubleLinearField(default_value=0.0)
    orty = objectRotTransY

    objectRotTransZ = DoubleLinearField(default_value=0.0)
    ortz = objectRotTransZ


class ObjectRotTransField(
    DoubleLinear3CompoundBaseField[ObjectRotTransAttrOperator, ObjectRotTransPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ObjectRotTransAttrOperator
    PLUG_CLS = ObjectRotTransPlugOperator

    objectRotTransX = DoubleLinearField(default_value=0.0)
    ortx = objectRotTransX

    objectRotTransY = DoubleLinearField(default_value=0.0)
    orty = objectRotTransY

    objectRotTransZ = DoubleLinearField(default_value=0.0)
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

    outputX = DoubleLinearField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleLinearField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleLinearField(default_value=0.0, writable=False)
    oz = outputZ


class OutputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputX = DoubleLinearField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleLinearField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleLinearField(default_value=0.0, writable=False)
    oz = outputZ


class OutputField(
    DoubleLinear3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleLinearField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleLinearField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleLinearField(default_value=0.0, writable=False)
    oz = outputZ
