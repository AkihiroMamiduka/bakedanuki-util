# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.typed import TypedField


class GeneratedClusterFlexorShape(Shape):
    __slots__ = ()

    NODE_TYPE = "clusterFlexorShape"

    driver = TypedField(multi=True, readable=False)
    dr = driver

    currentDriver = ShortField(default_value=-1)
    cdr = currentDriver

    flexorNodes = MessageField(multi=True, readable=False)
    fn = flexorNodes
