# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_initial_state import FalloffObjectField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


class MASH_InitialState(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_InitialState"

    inputArray = DataVectorArrayField()
    inArray = inputArray

    inScale = DataVectorArrayField(readable=False)

    inRotation = DataVectorArrayField(readable=False)

    outputArray = DataVectorArrayField()
    outArray = outputArray

    outRotation = DataVectorArrayField()

    outScale = DataVectorArrayField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    falloffInfo = TypedField()

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    Envelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    env = Envelope

    enable = BoolField(default_value=True)
    en = enable

    enablePosition = BoolField(default_value=True)
    enablePos = enablePosition

    enableRotation = BoolField(default_value=False)

    enableScale = BoolField(default_value=False)

    randEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    raEn = randEnvelope

    StepEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    StEnv = StepEnvelope

    falloffObject = FalloffObjectField(default_value=(0.0, 0.0, 0.0))
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffX = BoolField(default_value=True)
    fax = falloffX

    falloffY = BoolField(default_value=True)
    fay = falloffY

    falloffZ = BoolField(default_value=True)
    faz = falloffZ

    falloffMessage = MessageField()
    fmsg = falloffMessage
