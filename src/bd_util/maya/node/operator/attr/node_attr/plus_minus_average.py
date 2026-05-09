# coding: utf-8

from ..at.float import FloatAttr
from ..at.float2 import Float2Attr, Float2Plug
from ..at.float3 import Float3Attr, Float3Plug


class Input2DPlug(Float2Plug["Input2DAttr"]):
    input2Dx = FloatAttr()
    i2x = input2Dx

    input2Dy = FloatAttr()
    i2y = input2Dy


class Input2DAttr(Float2Attr[Input2DPlug]):
    PLUG_CLS = Input2DPlug

    input2Dx = FloatAttr()
    i2x = input2Dx

    input2Dy = FloatAttr()
    i2y = input2Dy


class Input3DPlug(Float3Plug["Input3DAttr"]):
    input3Dx = FloatAttr()
    i3x = input3Dx

    input3Dy = FloatAttr()
    i3y = input3Dy

    input3Dz = FloatAttr()
    i3z = input3Dz


class Input3DAttr(Float3Attr[Input3DPlug]):
    PLUG_CLS = Input3DPlug

    input3Dx = FloatAttr()
    i3x = input3Dx

    input3Dy = FloatAttr()
    i3y = input3Dy

    input3Dz = FloatAttr()
    i3z = input3Dz


class Output2DPlug(Float2Plug["Output2DAttr"]):
    output2Dx = FloatAttr()
    o2x = output2Dx

    output2Dy = FloatAttr()
    o2y = output2Dy


class Output2DAttr(Float2Attr[Output2DPlug]):
    PLUG_CLS = Output2DPlug

    output2Dx = FloatAttr()
    o2x = output2Dx

    output2Dy = FloatAttr()
    o2y = output2Dy


class Output3DPlug(Float3Plug["Output3DAttr"]):
    output3Dx = FloatAttr()
    o3x = output3Dx

    output3Dy = FloatAttr()
    o3y = output3Dy

    output3Dz = FloatAttr()
    o3z = output3Dz


class Output3DAttr(Float3Attr[Output3DPlug]):
    PLUG_CLS = Output3DPlug

    output3Dx = FloatAttr()
    o3x = output3Dx

    output3Dy = FloatAttr()
    o3y = output3Dy

    output3Dz = FloatAttr()
    o3z = output3Dz
