# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class ColorManagementGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "colorManagementGlobals"

    cmEnabled = BoolField()
    cme = cmEnabled

    configFileEnabled = BoolField()
    cfe = configFileEnabled

    configFilePath = DataStringField()
    cfp = configFilePath

    viewTransformName = DataStringField()
    vtn = viewTransformName

    viewName = DataStringField()
    vn = viewName

    displayName = DataStringField()
    dn = displayName

    workingSpaceName = DataStringField()
    wsn = workingSpaceName

    defaultInputSpaceName = DataStringField()
    din = defaultInputSpaceName

    outputTransformEnabled = BoolField()
    ote = outputTransformEnabled

    outputTransformUseColorConversion = BoolField()
    otc = outputTransformUseColorConversion

    playblastOutputTransformEnabled = BoolField()
    pote = playblastOutputTransformEnabled

    playblastOutputTransformUseColorConversion = BoolField()
    potc = playblastOutputTransformUseColorConversion

    outputUseViewTransform = BoolField()
    ovt = outputUseViewTransform

    playblastOutputUseViewTransform = BoolField()
    povt = playblastOutputUseViewTransform

    outputTransformName = DataStringField()
    otn = outputTransformName

    playblastOutputTransformName = DataStringField()
    potn = playblastOutputTransformName
