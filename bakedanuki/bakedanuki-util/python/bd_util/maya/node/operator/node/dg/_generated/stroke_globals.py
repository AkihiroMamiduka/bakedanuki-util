# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.stroke_globals import LightDirectionField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedStrokeGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "strokeGlobals"

    sceneScale = DoubleField(default_value=5.0, soft_min_value=0.0, soft_max_value=100.0)
    pss = sceneScale

    canvasScale = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    pcs = canvasScale

    wrapH = BoolField(default_value=False)
    wrh = wrapH

    wrapV = BoolField(default_value=False)
    wrv = wrapV

    sceneWrapH = BoolField(default_value=False)
    swh = sceneWrapH

    sceneWrapV = BoolField(default_value=False)
    swv = sceneWrapV

    forceRealLights = BoolField(default_value=True)
    frl = forceRealLights

    forceDepth = BoolField(default_value=True)
    fdp = forceDepth

    useCanvasLight = BoolField(default_value=True)
    ucl = useCanvasLight

    forceTubeDirAlongPath = BoolField(default_value=True)
    ftd = forceTubeDirAlongPath

    lightDirection = LightDirectionField(default_value=(0.2, -0.9, -0.5))
    ldr = lightDirection
    lightDirectionX = lightDirection.lightDirectionX
    ldx = lightDirectionX
    lightDirectionY = lightDirection.lightDirectionY
    ldy = lightDirectionY
    lightDirectionZ = lightDirection.lightDirectionZ
    ldz = lightDirectionZ
