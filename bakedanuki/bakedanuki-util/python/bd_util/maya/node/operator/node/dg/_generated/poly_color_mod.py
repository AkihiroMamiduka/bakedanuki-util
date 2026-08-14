# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_color_mod import (
    AlphaScaleField,
    BlueScaleField,
    GreenScaleField,
    IntensityScaleField,
    RedScaleField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class GeneratedPolyColorMod(DG):
    __slots__ = ()

    NODE_TYPE = "polyColorMod"

    output = DataMeshField(writable=False)
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField(default_value=0)
    cin = cacheInput

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField(default_value=False)
    vmap = vertexIdMap

    edgeIdMap = BoolField(default_value=False)
    emap = edgeIdMap

    faceIdMap = BoolField(default_value=False)
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField(default_value=True)
    uic = useInputComp

    baseColorName = DataStringField()
    bcn = baseColorName

    redScale = RedScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    r = redScale

    greenScale = GreenScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    g = greenScale

    blueScale = BlueScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    b = blueScale

    alphaScale = AlphaScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    a = alphaScale

    intensityScale = IntensityScaleField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    n = intensityScale

    huev = FloatField(
        default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0
    )
    h = huev

    satv = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    s = satv

    value = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    v = value
