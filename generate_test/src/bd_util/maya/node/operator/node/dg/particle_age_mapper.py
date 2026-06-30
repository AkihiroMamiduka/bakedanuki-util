# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.particle_age_mapper import OutUvCoordField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ParticleAgeMapper(DG):
    __slots__ = ()

    NODE_TYPE = "particleAgeMapper"

    outUvCoord = OutUvCoordField()
    ouv = outUvCoord
    outUCoord = outUvCoord.outUCoord
    ouc = outUCoord
    outVCoord = outUvCoord.outVCoord
    ovc = outVCoord

    particleAge = FloatField()
    pa = particleAge

    particleLifespan = FloatField()
    pls = particleLifespan

    relativeAge = BoolField()
    rea = relativeAge

    timeScale = FloatField()
    ts = timeScale

    foldAtEnd = BoolField()
    fae = foldAtEnd
