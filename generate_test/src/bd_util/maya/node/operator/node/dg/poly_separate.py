# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField


class PolySeparate(DG):
    __slots__ = ()

    NODE_TYPE = "polySeparate"

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    inputPoly = DataMeshField()
    ip = inputPoly

    icount = LongField()
    ic = icount

    remShells = TypedField()
    rs = remShells

    output = DataMeshField(multi=True)
    out = output

    userSpecifiedShells = BoolField()
    uss = userSpecifiedShells

    startFace = LongField()
    sf = startFace

    endFace = LongField()
    ef = endFace

    inPlace = BoolField()
    inp = inPlace
