# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_inherit import (
    FalloffObjectField,
    TranslateInPPField,
    TranslateOutPPField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField


class MASH_Inherit(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Inherit"

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    scaleOutPP = translateOutPP.scaleOutPP
    rotationOutPP = translateOutPP.rotationOutPP

    enablePosition = BoolField()

    enableScale = BoolField()

    enableRotation = BoolField()

    inTargetMatrices = MatrixField(multi=True)
    targetInMatrices = inTargetMatrices

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    Envelope = FloatField()
    env = Envelope

    enable = BoolField()
    en = enable

    falloffInfo = TypedField()

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

    force = FloatField()
    for_ = force

    forceVar = FloatField()
    forV = forceVar

    inheritStyle = LongField()
    inSty = inheritStyle

    randomSeed = LongField()
    raSe = randomSeed
