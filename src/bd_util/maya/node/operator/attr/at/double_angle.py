# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .._core import AttrOperator, PlugOperator, AttributeField


class DoubleAnglePlugOperator(PlugOperator["DoubleAngleAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asMAngle().asDegrees()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueMAngle(
            self.plug, om.MAngle(value, om.MAngle.kDegrees)
        )


class DoubleAngleAttrOperator(AttrOperator[DoubleAnglePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "doubleAngle"


class DoubleAngleField(
    AttributeField[DoubleAngleAttrOperator, DoubleAnglePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DoubleAngleAttrOperator
    PLUG_CLS = DoubleAnglePlugOperator
