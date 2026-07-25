# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedColorManagementGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "colorManagementGlobals"

    cmEnabled = BoolField(default_value=True)
    cme = cmEnabled

    configFileEnabled = BoolField(default_value=False)
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

    outputTransformEnabled = BoolField(default_value=False)
    ote = outputTransformEnabled

    outputTransformUseColorConversion = BoolField(default_value=False)
    otc = outputTransformUseColorConversion

    playblastOutputTransformEnabled = BoolField(default_value=True)
    pote = playblastOutputTransformEnabled

    playblastOutputTransformUseColorConversion = BoolField(default_value=False)
    potc = playblastOutputTransformUseColorConversion

    outputUseViewTransform = BoolField(default_value=True)
    ovt = outputUseViewTransform

    playblastOutputUseViewTransform = BoolField(default_value=True)
    povt = playblastOutputUseViewTransform

    outputTransformName = DataStringField()
    otn = outputTransformName

    playblastOutputTransformName = DataStringField()
    potn = playblastOutputTransformName
