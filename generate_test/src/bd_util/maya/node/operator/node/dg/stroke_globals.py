# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.stroke_globals import LightDirectionField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField


class StrokeGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "strokeGlobals"

    sceneScale = DoubleField()
    pss = sceneScale

    canvasScale = DoubleField()
    pcs = canvasScale

    wrapH = BoolField()
    wrh = wrapH

    wrapV = BoolField()
    wrv = wrapV

    sceneWrapH = BoolField()
    swh = sceneWrapH

    sceneWrapV = BoolField()
    swv = sceneWrapV

    forceRealLights = BoolField()
    frl = forceRealLights

    forceDepth = BoolField()
    fdp = forceDepth

    useCanvasLight = BoolField()
    ucl = useCanvasLight

    forceTubeDirAlongPath = BoolField()
    ftd = forceTubeDirAlongPath

    lightDirection = LightDirectionField()
    ldr = lightDirection
    lightDirectionX = lightDirection.lightDirectionX
    ldx = lightDirectionX
    lightDirectionY = lightDirection.lightDirectionY
    ldy = lightDirectionY
    lightDirectionZ = lightDirection.lightDirectionZ
    ldz = lightDirectionZ
