# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.particle_incand_mapper import (
    ParticleIncandescenceField,
)


class GeneratedParticleIncandMapper(DG):
    __slots__ = ()

    NODE_TYPE = "particleIncandMapper"

    particleIncandescence = ParticleIncandescenceField(
        default_value=(0.0, 0.0, 0.0)
    )
    pi = particleIncandescence
    particleIncandescenceR = particleIncandescence.particleIncandescenceR
    pir = particleIncandescenceR
    particleIncandescenceG = particleIncandescence.particleIncandescenceG
    pig = particleIncandescenceG
    particleIncandescenceB = particleIncandescence.particleIncandescenceB
    pib = particleIncandescenceB
