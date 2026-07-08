# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hik_character_state_client import HipsScaleField
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class HIKCharacterStateClient(DG):
    __slots__ = ()

    NODE_TYPE = "HIKCharacterStateClient"

    live = BoolField(default_value=False)
    lv = live

    frameRate = DoubleField(default_value=15.0, min_value=1.0)
    fr = frameRate

    output = GenericField()
    o = output

    serverName = DataStringField()
    svn = serverName

    deviceName = DataStringField()
    dvn = deviceName

    InputCharacterDefinition = TypedField()

    hipsScale = HipsScaleField(default_value=(1.0, 1.0, 1.0))
    hipsScaleX = hipsScale.hipsScaleX
    hipsScaleY = hipsScale.hipsScaleY
    hipsScaleZ = hipsScale.hipsScaleZ

    referenceGX = MatrixField()

    OutputCharacterState = TypedField(writable=False)
