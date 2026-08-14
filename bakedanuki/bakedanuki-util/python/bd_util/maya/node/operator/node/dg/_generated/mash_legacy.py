# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_legacy import TranslateInPPField
from ....attr.define.std.at.typed import TypedField


class GeneratedMASHLegacy(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Legacy"

    outputPoints = TypedField(writable=False)

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP
    idInPP = translateInPP.idInPP
    visibilityInPP = translateInPP.visibilityInPP

    savedData = TypedField()
