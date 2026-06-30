# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.particle_transp_mapper import ParticleTransparencyField


class ParticleTranspMapper(DG):
    __slots__ = ()

    NODE_TYPE = "particleTranspMapper"

    particleTransparency = ParticleTransparencyField()
    pt = particleTransparency
    particleTransparencyR = particleTransparency.particleTransparencyR
    ptr = particleTransparencyR
    particleTransparencyG = particleTransparency.particleTransparencyG
    ptg = particleTransparencyG
    particleTransparencyB = particleTransparency.particleTransparencyB
    ptb = particleTransparencyB
