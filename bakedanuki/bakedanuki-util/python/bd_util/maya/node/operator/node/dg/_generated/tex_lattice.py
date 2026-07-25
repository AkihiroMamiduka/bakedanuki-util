# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.tex_lattice import (
    BoundingBoxInfField,
    BoundingBoxSupField,
    LatticePointField,
)
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedTexLattice(DG):
    __slots__ = ()

    NODE_TYPE = "texLattice"

    latticeWidth = LongField(default_value=0)
    lw = latticeWidth

    latticeHeight = LongField(default_value=0)
    lh = latticeHeight

    latticePoint = LatticePointField(multi=True, default_value=(0.0, 0.0))
    lp = latticePoint

    boundingBoxInf = BoundingBoxInfField(default_value=(0.0, 0.0))
    bbi = boundingBoxInf
    boundingBoxTop = boundingBoxInf.boundingBoxTop
    bbxt = boundingBoxTop
    boundingBoxLeft = boundingBoxInf.boundingBoxLeft
    bbxl = boundingBoxLeft

    boundingBoxSup = BoundingBoxSupField(default_value=(0.0, 0.0))
    bbxs = boundingBoxSup
    boundingBoxBottom = boundingBoxSup.boundingBoxBottom
    bbxb = boundingBoxBottom
    boundingBoxRight = boundingBoxSup.boundingBoxRight
    bbxr = boundingBoxRight
