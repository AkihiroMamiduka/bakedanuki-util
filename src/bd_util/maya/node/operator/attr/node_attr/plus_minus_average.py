# coding: utf-8

from ..at.float import FloatAttrOperator
from ..at.float2 import Float2AttrOperator, Float2PlugOperator
from ..at.float3 import Float3AttrOperator, Float3PlugOperator


class Input2DPlugOperator(Float2PlugOperator["Input2DAttrOperator"]):
    input2Dx = FloatAttrOperator()
    i2x = input2Dx

    input2Dy = FloatAttrOperator()
    i2y = input2Dy


class Input2DAttrOperator(Float2AttrOperator[Input2DPlugOperator]):
    PLUG_CLS = Input2DPlugOperator

    input2Dx = FloatAttrOperator()
    i2x = input2Dx

    input2Dy = FloatAttrOperator()
    i2y = input2Dy


class Input3DPlugOperator(Float3PlugOperator["Input3DAttrOperator"]):
    input3Dx = FloatAttrOperator()
    i3x = input3Dx

    input3Dy = FloatAttrOperator()
    i3y = input3Dy

    input3Dz = FloatAttrOperator()
    i3z = input3Dz


class Input3DAttrOperator(Float3AttrOperator[Input3DPlugOperator]):
    PLUG_CLS = Input3DPlugOperator

    input3Dx = FloatAttrOperator()
    i3x = input3Dx

    input3Dy = FloatAttrOperator()
    i3y = input3Dy

    input3Dz = FloatAttrOperator()
    i3z = input3Dz


class Output2DPlugOperator(Float2PlugOperator["Output2DAttrOperator"]):
    output2Dx = FloatAttrOperator()
    o2x = output2Dx

    output2Dy = FloatAttrOperator()
    o2y = output2Dy


class Output2DAttrOperator(Float2AttrOperator[Output2DPlugOperator]):
    PLUG_CLS = Output2DPlugOperator

    output2Dx = FloatAttrOperator()
    o2x = output2Dx

    output2Dy = FloatAttrOperator()
    o2y = output2Dy


class Output3DPlugOperator(Float3PlugOperator["Output3DAttrOperator"]):
    output3Dx = FloatAttrOperator()
    o3x = output3Dx

    output3Dy = FloatAttrOperator()
    o3y = output3Dy

    output3Dz = FloatAttrOperator()
    o3z = output3Dz


class Output3DAttrOperator(Float3AttrOperator[Output3DPlugOperator]):
    PLUG_CLS = Output3DPlugOperator

    output3Dx = FloatAttrOperator()
    o3x = output3Dx

    output3Dy = FloatAttrOperator()
    o3y = output3Dy

    output3Dz = FloatAttrOperator()
    o3z = output3Dz
