# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .._core import Attr, Plug


class DoubleAnglePlug(Plug["DoubleAngleAttr"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMAngle().asDegrees()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMAngle(
            self.plug, om.MAngle(value, om.MAngle.kDegrees)
        )


class DoubleAngleAttr(Attr[DoubleAnglePlug]):
    __slots__ = ()

    ATTR_TYPE = "doubleAngle"
    PLUG_CLS = DoubleAnglePlug
