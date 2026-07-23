# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ......... import logger as u_logger
from ._base import (
    NumericBaseAttrOperator,
    NumericBasePlugOperator,
    NumericBaseField,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class BoolPlugOperator(NumericBasePlugOperator["BoolAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> bool:
        return self.plug.asBool()

    # set
    def set(self, value: bool):
        self._node._dg_mod.newPlugValueBool(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kBoolean)


class BoolAttrOperator(NumericBaseAttrOperator[BoolPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "bool"

    def __init__(self, *args, default_value=None, **kwargs):
        # デフォルト値
        if default_value is None:
            default_value = True
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class BoolField(NumericBaseField[BoolAttrOperator, BoolPlugOperator]):
    __slots__ = ()

    ATTR_CLS = BoolAttrOperator
    PLUG_CLS = BoolPlugOperator
