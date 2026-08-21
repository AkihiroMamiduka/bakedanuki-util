# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.line_modifier import (
    ColorField,
    DropoffField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.mesh import DataMeshField


class ShapeEnumPlugOperator(EnumPlugOperator["ShapeEnumAttrOperator"]):
    __slots__ = ()

    SPHERE = 0
    CUBE = 1


class ShapeEnumAttrOperator(EnumAttrOperator[ShapeEnumPlugOperator]):
    __slots__ = ()

    SPHERE = 0
    CUBE = 1

    NAME_MAP = {
        SPHERE: "Sphere",
        CUBE: "Cube",
    }


class ShapeEnumField(EnumField[ShapeEnumAttrOperator, ShapeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ShapeEnumAttrOperator
    PLUG_CLS = ShapeEnumPlugOperator


class GeneratedLineModifier(Shape):
    __slots__ = ()

    NODE_TYPE = "lineModifier"

    shape = ShapeEnumField(default_value=0)
    shp = shape

    widthScale = DoubleField(
        default_value=5.0, soft_min_value=0.0, soft_max_value=10.0
    )
    wsc = widthScale

    widthOffset = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    wof = widthOffset

    opacityScale = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    osc = opacityScale

    opacityOffset = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    oof = opacityOffset

    surfaceOffset = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    sof = surfaceOffset

    lineExtend = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    lex = lineExtend

    modifyColor = BoolField(default_value=False)
    mcl = modifyColor

    color = ColorField(default_value=(1.0, 0.0, 0.0))
    clr = color
    colorR = color.colorR
    crr = colorR
    colorG = color.colorG
    crg = colorG
    colorB = color.colorB
    crb = colorB

    tubeScale = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    tus = tubeScale

    tubeDropout = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    tud = tubeDropout

    branchDropout = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    bdp = branchDropout

    twigDropout = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    tdp = twigDropout

    leafDropout = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    ldp = leafDropout

    flowerDropout = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    fdp = flowerDropout

    leafScale = DoubleField(
        default_value=1.0, min_value=0.0, soft_max_value=5.0
    )
    lsc = leafScale

    flowerScale = DoubleField(
        default_value=1.0, min_value=0.0, soft_max_value=5.0
    )
    fsc = flowerScale

    force = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    frc = force

    directionalForce = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    dfc = directionalForce

    displacement = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    dsp = displacement

    directionalDisplacement = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    ddc = directionalDisplacement

    dropoffNoise = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    don = dropoffNoise

    noiseFrequency = DoubleField(
        default_value=0.2, soft_min_value=0.0, soft_max_value=1.0
    )
    nfr = noiseFrequency

    dropoff = DropoffField(multi=True, default_value=(0.0, 0.0, 0))
    drp = dropoff

    occupyGridResolution = LongField(
        default_value=50, min_value=1, soft_max_value=200
    )
    ocgr = occupyGridResolution

    occupyAttraction = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    ocat = occupyAttraction

    attractRadiusScale = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    ocar = attractRadiusScale

    attractRadiusOffset = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    ocao = attractRadiusOffset

    occupyRadiusScale = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    ocrs = occupyRadiusScale

    occupyRadiusOffset = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    ocro = occupyRadiusOffset

    occupyBranchTermination = BoolField(default_value=False)
    ocbt = occupyBranchTermination

    inputMesh = DataMeshField()
    inms = inputMesh

    outLineModifier = TypedField(multi=True, writable=False)
    olm = outLineModifier
