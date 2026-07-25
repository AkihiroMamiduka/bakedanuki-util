# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedHwReflectionMap(DG):
    __slots__ = ()

    NODE_TYPE = "hwReflectionMap"

    decalMode = BoolField(default_value=True)
    dm = decalMode

    cubeMap = BoolField(default_value=False)
    cm = cubeMap

    textureHasChanged = BoolField(default_value=False)
    thc = textureHasChanged

    sphereMapTextureName = DataStringField()
    smtn = sphereMapTextureName

    cubeFrontTextureName = DataStringField()
    cftn = cubeFrontTextureName

    cubeBackTextureName = DataStringField()
    cbkn = cubeBackTextureName

    cubeTopTextureName = DataStringField()
    ctpn = cubeTopTextureName

    cubeBottomTextureName = DataStringField()
    cbmn = cubeBottomTextureName

    cubeLeftTextureName = DataStringField()
    cltn = cubeLeftTextureName

    cubeRightTextureName = DataStringField()
    crtn = cubeRightTextureName
