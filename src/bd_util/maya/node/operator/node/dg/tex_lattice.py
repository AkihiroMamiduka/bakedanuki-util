# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.tex_lattice import (
    BoundingBoxInfField,
    BoundingBoxSupField,
    LatticePointField,
)
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class TexLattice(DG):
    __slots__ = ()

    NODE_TYPE = "texLattice"

    latticeWidth = LongField()
    lw = latticeWidth

    latticeHeight = LongField()
    lh = latticeHeight

    latticePoint = LatticePointField(multi=True)
    lp = latticePoint

    boundingBoxInf = BoundingBoxInfField()
    bbi = boundingBoxInf
    boundingBoxTop = boundingBoxInf.boundingBoxTop
    bbxt = boundingBoxTop
    boundingBoxLeft = boundingBoxInf.boundingBoxLeft
    bbxl = boundingBoxLeft

    boundingBoxSup = BoundingBoxSupField()
    bbxs = boundingBoxSup
    boundingBoxBottom = boundingBoxSup.boundingBoxBottom
    bbxb = boundingBoxBottom
    boundingBoxRight = boundingBoxSup.boundingBoxRight
    bbxr = boundingBoxRight
