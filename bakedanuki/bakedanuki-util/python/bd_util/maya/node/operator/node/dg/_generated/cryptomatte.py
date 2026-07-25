# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.cryptomatte import (
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedCryptomatte(DG):
    __slots__ = ()

    NODE_TYPE = "cryptomatte"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    sidecarManifests = BoolField(default_value=False)
    sidecar_manifests = sidecarManifests

    cryptomatteDepth = LongField(default_value=6)
    cryptomatte_depth = cryptomatteDepth

    stripObjNamespaces = BoolField(default_value=True)
    strip_obj_namespaces = stripObjNamespaces

    stripMatNamespaces = BoolField(default_value=True)
    strip_mat_namespaces = stripMatNamespaces

    aovCryptoAsset = DataStringField()
    aov_crypto_asset = aovCryptoAsset

    aovCryptoObject = DataStringField()
    aov_crypto_object = aovCryptoObject

    aovCryptoMaterial = DataStringField()
    aov_crypto_material = aovCryptoMaterial

    previewInExr = BoolField(default_value=False)
    preview_in_exr = previewInExr

    customOutputDriver = BoolField(default_value=False)
    custom_output_driver = customOutputDriver

    createDepthOutputs = BoolField(default_value=True)
    create_depth_outputs = createDepthOutputs

    processMaya = BoolField(default_value=True)
    process_maya = processMaya

    processPaths = BoolField(default_value=True)
    process_paths = processPaths

    processObjPathPipes = BoolField(default_value=True)
    process_obj_path_pipes = processObjPathPipes

    processMatPathPipes = BoolField(default_value=True)
    process_mat_path_pipes = processMatPathPipes

    processLegacy = BoolField(default_value=True)
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
