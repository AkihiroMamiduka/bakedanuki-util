# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.particle_age_mapper import OutUvCoordField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedParticleAgeMapper(DG):
    __slots__ = ()

    NODE_TYPE = "particleAgeMapper"

    outUvCoord = OutUvCoordField(default_value=(0.0, 0.0), writable=False)
    ouv = outUvCoord
    outUCoord = outUvCoord.outUCoord
    ouc = outUCoord
    outVCoord = outUvCoord.outVCoord
    ovc = outVCoord

    particleAge = FloatField(default_value=0.0)
    pa = particleAge

    particleLifespan = FloatField(default_value=0.0)
    pls = particleLifespan

    relativeAge = BoolField(default_value=False)
    rea = relativeAge

    timeScale = FloatField(default_value=1.0)
    ts = timeScale

    foldAtEnd = BoolField(default_value=False)
    fae = foldAtEnd
