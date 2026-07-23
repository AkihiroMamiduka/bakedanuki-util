# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.material_template import AssignField
from ....attr.define.std.at.message import MessageField


class _GeneratedMaterialTemplate(DG):
    __slots__ = ()

    NODE_TYPE = "materialTemplate"

    assign = AssignField(multi=True)
    asg = assign

    defaultShadingEngine = MessageField()
    dsh = defaultShadingEngine
