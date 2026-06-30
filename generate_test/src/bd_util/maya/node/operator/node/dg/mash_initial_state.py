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

    inScale = DataVectorArrayField()

    inRotation = DataVectorArrayField()

    outputArray = DataVectorArrayField()
    outArray = outputArray

    outRotation = DataVectorArrayField()

    outScale = DataVectorArrayField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    falloffInfo = TypedField()

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    Envelope = FloatField()
    env = Envelope

    enable = BoolField()
    en = enable

    enablePosition = BoolField()
    enablePos = enablePosition

    enableRotation = BoolField()

    enableScale = BoolField()

    randEnvelope = FloatField()
    raEn = randEnvelope

    StepEnvelope = FloatField()
    StEnv = StepEnvelope

    falloffObject = FalloffObjectField()
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffX = BoolField()
    fax = falloffX

    falloffY = BoolField()
    fay = falloffY

    falloffZ = BoolField()
    faz = falloffZ

    falloffMessage = MessageField()
    fmsg = falloffMessage
