# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_color_mod import (
    AlphaScaleField,
    BlueScaleField,
    GreenScaleField,
    IntensityScaleField,
    RedScaleField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class PolyColorMod(DG):
    __slots__ = ()

    NODE_TYPE = "polyColorMod"

    output = DataMeshField()
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField()
    cin = cacheInput

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField()
    vmap = vertexIdMap

    edgeIdMap = BoolField()
    emap = edgeIdMap

    faceIdMap = BoolField()
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField()
    uic = useInputComp

    baseColorName = DataStringField()
    bcn = baseColorName

    redScale = RedScaleField(multi=True)
    r = redScale

    greenScale = GreenScaleField(multi=True)
    g = greenScale

    blueScale = BlueScaleField(multi=True)
    b = blueScale

    alphaScale = AlphaScaleField(multi=True)
    a = alphaScale

    intensityScale = IntensityScaleField(multi=True)
    n = intensityScale

    huev = FloatField()
    h = huev

    satv = FloatField()
    s = satv

    value = FloatField()
    v = value
