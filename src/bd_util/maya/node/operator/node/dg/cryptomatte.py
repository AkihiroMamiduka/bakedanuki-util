# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.cryptomatte import (
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class Cryptomatte(DG):
    __slots__ = ()

    NODE_TYPE = "cryptomatte"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    sidecarManifests = BoolField()
    sidecar_manifests = sidecarManifests

    cryptomatteDepth = LongField()
    cryptomatte_depth = cryptomatteDepth

    stripObjNamespaces = BoolField()
    strip_obj_namespaces = stripObjNamespaces

    stripMatNamespaces = BoolField()
    strip_mat_namespaces = stripMatNamespaces

    aovCryptoAsset = DataStringField()
    aov_crypto_asset = aovCryptoAsset

    aovCryptoObject = DataStringField()
    aov_crypto_object = aovCryptoObject

    aovCryptoMaterial = DataStringField()
    aov_crypto_material = aovCryptoMaterial

    previewInExr = BoolField()
    preview_in_exr = previewInExr

    customOutputDriver = BoolField()
    custom_output_driver = customOutputDriver

    createDepthOutputs = BoolField()
    create_depth_outputs = createDepthOutputs

    processMaya = BoolField()
    process_maya = processMaya

    processPaths = BoolField()
    process_paths = processPaths

    processObjPathPipes = BoolField()
    process_obj_path_pipes = processObjPathPipes

    processMatPathPipes = BoolField()
    process_mat_path_pipes = processMatPathPipes

    processLegacy = BoolField()
    process_legacy = processLegacy

    userCryptoAov0 = DataStringField()
    user_crypto_aov_0 = userCryptoAov0

    userCryptoSrc0 = DataStringField()
    user_crypto_src_0 = userCryptoSrc0

    userCryptoAov1 = DataStringField()
    user_crypto_aov_1 = userCryptoAov1

    userCryptoSrc1 = DataStringField()
    user_crypto_src_1 = userCryptoSrc1

    userCryptoAov2 = DataStringField()
    user_crypto_aov_2 = userCryptoAov2

    userCryptoSrc2 = DataStringField()
    user_crypto_src_2 = userCryptoSrc2

    userCryptoAov3 = DataStringField()
    user_crypto_aov_3 = userCryptoAov3

    userCryptoSrc3 = DataStringField()
    user_crypto_src_3 = userCryptoSrc3
