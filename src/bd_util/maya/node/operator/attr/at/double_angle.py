# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .._core import AttrOperator, PlugOperator


class DoubleAnglePlug(PlugOperator["DoubleAngleAttr"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMAngle().asDegrees()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMAngle(
            self.plug, om.MAngle(value, om.MAngle.kDegrees)
        )


class DoubleAngleAttr(AttrOperator[DoubleAnglePlug]):
    __slots__ = ()

    ATTR_TYPE = "doubleAngle"
    PLUG_CLS = DoubleAnglePlug
