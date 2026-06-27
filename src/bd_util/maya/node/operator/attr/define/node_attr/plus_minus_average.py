# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.float2 import Float2AttrOperator, Float2PlugOperator, Float2Field
from ..std.at.float3 import Float3AttrOperator, Float3PlugOperator, Float3Field


class Input2DPlugOperator(Float2PlugOperator["Input2DAttrOperator"]):
    __slots__ = ()

    input2Dx = FloatField()
    i2x = input2Dx

    input2Dy = FloatField()
    i2y = input2Dy


class Input2DAttrOperator(Float2AttrOperator[Input2DPlugOperator]):
    __slots__ = ()

    input2Dx = FloatField()
    i2x = input2Dx

    input2Dy = FloatField()
    i2y = input2Dy


class Input2DField(Float2Field[Input2DAttrOperator, Input2DPlugOperator]):
    __slots__ = ()

    ATTR_CLS = Input2DAttrOperator
    PLUG_CLS = Input2DPlugOperator


class Input3DPlugOperator(Float3PlugOperator["Input3DAttrOperator"]):
    __slots__ = ()

    input3Dx = FloatField()
    i3x = input3Dx

    input3Dy = FloatField()
    i3y = input3Dy

    input3Dz = FloatField()
    i3z = input3Dz


class Input3DAttrOperator(Float3AttrOperator[Input3DPlugOperator]):
    __slots__ = ()

    input3Dx = FloatField()
    i3x = input3Dx

    input3Dy = FloatField()
    i3y = input3Dy

    input3Dz = FloatField()
    i3z = input3Dz


class Input3DField(Float3Field[Input3DAttrOperator, Input3DPlugOperator]):
    __slots__ = ()

    ATTR_CLS = Input3DAttrOperator
    PLUG_CLS = Input3DPlugOperator


class Output2DPlugOperator(Float2PlugOperator["Output2DAttrOperator"]):
    __slots__ = ()

    output2Dx = FloatField()
    o2x = output2Dx

    output2Dy = FloatField()
    o2y = output2Dy


class Output2DAttrOperator(Float2AttrOperator[Output2DPlugOperator]):
    __slots__ = ()

    output2Dx = FloatField()
    o2x = output2Dx

    output2Dy = FloatField()
    o2y = output2Dy


class Output2DField(Float2Field[Output2DAttrOperator, Output2DPlugOperator]):
    __slots__ = ()

    ATTR_CLS = Output2DAttrOperator
    PLUG_CLS = Output2DPlugOperator

    output2Dx = FloatField()
    o2x = output2Dx

    output2Dy = FloatField()
    o2y = output2Dy


class Output3DPlugOperator(Float3PlugOperator["Output3DAttrOperator"]):
    __slots__ = ()

    output3Dx = FloatField()
    o3x = output3Dx

    output3Dy = FloatField()
    o3y = output3Dy

    output3Dz = FloatField()
    o3z = output3Dz


class Output3DAttrOperator(Float3AttrOperator[Output3DPlugOperator]):
    __slots__ = ()

    output3Dx = FloatField()
    o3x = output3Dx

    output3Dy = FloatField()
    o3y = output3Dy

    output3Dz = FloatField()
    o3z = output3Dz


class Output3DField(Float3Field[Output3DAttrOperator, Output3DPlugOperator]):
    __slots__ = ()

    ATTR_CLS = Output3DAttrOperator
    PLUG_CLS = Output3DPlugOperator

    output3Dx = FloatField()
    o3x = output3Dx

    output3Dy = FloatField()
    o3y = output3Dy

    output3Dz = FloatField()
    o3z = output3Dz
