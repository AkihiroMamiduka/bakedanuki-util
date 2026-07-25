# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField


class _GeneratedPolySeparate(DG):
    __slots__ = ()

    NODE_TYPE = "polySeparate"

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    inputPoly = DataMeshField()
    ip = inputPoly

    icount = LongField(default_value=-1)
    ic = icount

    remShells = TypedField()
    rs = remShells

    output = DataMeshField(multi=True, writable=False)
    out = output

    userSpecifiedShells = BoolField(default_value=False)
    uss = userSpecifiedShells

    startFace = LongField(default_value=0)
    sf = startFace

    endFace = LongField(default_value=0)
    ef = endFace

    inPlace = BoolField(default_value=False)
    inp = inPlace
