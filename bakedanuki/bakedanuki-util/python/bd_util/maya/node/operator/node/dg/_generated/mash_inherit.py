# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_inherit import (
    FalloffObjectField,
    TranslateInPPField,
    TranslateOutPPField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField


class GeneratedMASH_Inherit(DG):
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

    enablePosition = BoolField(default_value=True)

    enableScale = BoolField(default_value=True)

    enableRotation = BoolField(default_value=True)

    inTargetMatrices = MatrixField(multi=True)
    targetInMatrices = inTargetMatrices

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    Envelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    env = Envelope

    enable = BoolField(default_value=True)
    en = enable

    falloffInfo = TypedField()

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

    force = FloatField(
        default_value=0.0, soft_min_value=-2.0, soft_max_value=2.0
    )
    for_ = force

    forceVar = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    forV = forceVar

    inheritStyle = LongField(default_value=1)
    inSty = inheritStyle

    randomSeed = LongField(default_value=1, min_value=1, soft_max_value=100)
    raSe = randomSeed
