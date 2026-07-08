# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.particle_color_mapper import ParticleColorField


class ParticleColorMapper(DG):
    __slots__ = ()

    NODE_TYPE = "particleColorMapper"

    particleColor = ParticleColorField(default_value=(0.0, 0.0, 0.0))
    pc = particleColor
    particleColorR = particleColor.particleColorR
    pcr = particleColorR
    particleColorG = particleColor.particleColorG
    pcg = particleColorG
    particleColorB = particleColor.particleColorB
    pcb = particleColorB
