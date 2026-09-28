# coding: utf-8
from __future__ import annotations

SUPPORTED_MAYA_VERSIONS = (2025, 2026, 2027)

# 生成した `NodeOperator` の公開面を比較するため、plug-in の読み込み条件を固定する。
# `dynamicGeometryAttributes` は Maya 2026 以降で読み込む。
BASE_PROFILE_PLUGIN_REQUESTS = (
    "mayaHIK",
    "invertShape",
    "curveWarp",
    "hairPhysicalShader",
    "ikSpringSolver",
    "sweep",
    "lookdevKit",
    "Type",
    "bifrostGraph",
    "modelingToolkit",
    "MayaMuscle",
    "matrixNodes",
    "polyBoolean",
    "bdUtilNodes",
    "MASH",
    "poseInterpolator",
    "ik2Bsolver",
    "xgenToolkit",
    "gameFbxExporter",
    "Unfold3D",
    "mtoa",
    "rotateHelper",
    "AbcImport",
    "sceneAssembly",
    "gpuCache",
    "mayaUsdPlugin",
    "quatNodes",
    "LookdevXMaya",
)

INVENTORY_COUNTS = {
    2025: {"registered": 1417, "generated": 1297, "skipped": 120},
    2026: {"registered": 1476, "generated": 1356, "skipped": 120},
    2027: {"registered": 1485, "generated": 1365, "skipped": 120},
}

# 初回の Maya 2025 snapshot にない対応ノードも、後続版の差分判定の基準へ含める。
BASELINE_ADDITIONAL_NODE_TYPES = (
    "aiOpenPBRSurface",
    "bifrostGraphShape",
    "bifrostRiggingContainer",
    "gpuCache",
    "mayaUsdGeometryGizmoShape",
    "mayaUsdProxyShape",
    "mayaUsdProxyShapeBase",
    "openPBRSurface",
    "xgmDescription",
    "xgmSplineDescription",
)

# 固定 profile の一覧は runtime registry と独立に保持する。
# test で `NODE_TYPE_VERSION_RANGES` と照合し、双方の登録漏れを検出する。
INTRODUCED_NODE_TYPES_BY_VERSION = {
    2025: (),
    2026: (
        "absoluteDL",
        "acosDL",
        "addDL",
        "aiCompareString",
        "aiImagerInference",
        "angleBetweenDL",
        "animInContextNode",
        "asinDL",
        "atan2DL",
        "atanDL",
        "averageDL",
        "axisFromMatrixDL",
        "ceilDL",
        "clampRangeDL",
        "columnFromMatrixDL",
        "cosDL",
        "crossProductDL",
        "determinantDL",
        "dgaDelta",
        "dgaTension",
        "dgaToArray",
        "dgaVisualizer",
        "distanceBetweenDL",
        "divideDL",
        "dotProductDL",
        "equalDL",
        "floorDL",
        "greaterThanDL",
        "inverseLerpDL",
        "lengthDL",
        "lerpDL",
        "lessThanDL",
        "logDL",
        "maxDL",
        "minDL",
        "moduloDL",
        "multDL",
        "multiplyDL",
        "multiplyPointByMatrixDL",
        "multiplyVectorByMatrixDL",
        "negateDL",
        "normalizeDL",
        "pointMatrixMultDL",
        "polySmartBevel",
        "powerDL",
        "rotateVectorDL",
        "roundDL",
        "rowFromMatrixDL",
        "scaleFromMatrixDL",
        "sinDL",
        "smoothStepDL",
        "subtractDL",
        "sumDL",
        "tanDL",
        "translationFromMatrixDL",
        "truncateDL",
        "ufeLightArea",
        "ufeLightCylinder",
        "ufeLightDefault",
        "ufeLightDirectional",
        "ufeLightDisk",
        "ufeLightDome",
        "ufeLightSphere",
        "ufeLightSpot",
    ),
    2027: (
        "UsdDefaultSettings",
        "aiGaussianSplat",
        "aiGaussianSplatShader",
        "aiLine",
        "aiNearestPoints",
        "aiShaderToRgba",
        "aiToneZones",
        "bifrostClosureConverter",
        "shotLabel",
    ),
}

REMOVED_NODE_TYPES_BY_VERSION = {
    2025: (),
    2026: (
        "addDoubleLinear",
        "mayaUsdGeometryGizmoShape",
        "multDoubleLinear",
        "pointMatrixMult",
        "polyBevelCutback",
    ),
    2027: (),
}

SCHEMA_CHANGED_NODE_TYPES_BY_VERSION = {
    2026: (
        "absolute",
        "acos",
        "aiAmbientOcclusion",
        "aiAreaLight",
        "aiCurvature",
        "aiDistance",
        "aiFlakes",
        "aiFog",
        "aiImagerLensEffects",
        "aiImagerLightMixer",
        "aiLayerShader",
        "aiLightDecay",
        "aiMeshLight",
        "aiOpenPBRSurface",
        "aiOptions",
        "aiPassthrough",
        "aiPhotometricLight",
        "aiRampFloat",
        "aiRampRgb",
        "aiRaySwitch",
        "aiRoundCorners",
        "aiSkin",
        "aiStandardHair",
        "aiStandardSurface",
        "aiSwitch",
        "aiTraceSet",
        "aiTwoSided",
        "aiUtility",
        "aiVolume",
        "angleBetween",
        "areaLight",
        "asin",
        "atan",
        "atan2",
        "average",
        "axisFromMatrix",
        "bifrostGeoToMaya",
        "bifrostRiggingContainer",
        "ceil",
        "clampRange",
        "columnFromMatrix",
        "cos",
        "crossProduct",
        "determinant",
        "distanceBetween",
        "divide",
        "dotProduct",
        "equal",
        "floor",
        "greasePlane",
        "greasePlaneRenderShape",
        "greaterThan",
        "hardwareRenderingGlobals",
        "imagePlane",
        "inverseLerp",
        "length",
        "lerp",
        "lessThan",
        "log",
        "max",
        "mayaUsdProxyShape",
        "mesh",
        "min",
        "modulo",
        "multiply",
        "multiplyPointByMatrix",
        "multiplyVectorByMatrix",
        "negate",
        "normalize",
        "openPBRSurface",
        "pointLight",
        "polyBoolean",
        "polyExtrudeEdge",
        "polySmartExtrude",
        "power",
        "rotateVector",
        "round",
        "rowFromMatrix",
        "scaleFromMatrix",
        "sin",
        "smoothStep",
        "spotLight",
        "standardSurface",
        "subtract",
        "sum",
        "tan",
        "translationFromMatrix",
        "truncate",
        "volumeLight",
    ),
    2027: (
        "MASH_Waiter",
        "aiAOVDriver",
        "aiColorJitter",
        "aiImagerDenoiserNoice",
        "aiImagerLensEffects",
        "aiImagerLightMixer",
        "aiNormalMap",
        "aiOptions",
        "aiStandIn",
        "aiUvTransform",
        "aiVolume",
        "animCurveTA",
        "animCurveTL",
        "animCurveTT",
        "animCurveTU",
        "animCurveUA",
        "animCurveUL",
        "animCurveUT",
        "animCurveUU",
        "animLayer",
        "bezierCurve",
        "bifrostBoard",
        "bifrostGraphShape",
        "bump2d",
        "character",
        "columnFromMatrix",
        "creaseSet",
        "cryptomatte",
        "gpuCache",
        "greasePlaneRenderShape",
        "hairSystem",
        "keyingGroup",
        "mayaUsdProxyShape",
        "mayaUsdProxyShapeBase",
        "mesh",
        "nCloth",
        "nParticle",
        "nRigid",
        "nurbsCurve",
        "nurbsSurface",
        "objectSet",
        "particle",
        "polySmartBevel",
        "resultCurveTimeToAngular",
        "resultCurveTimeToLinear",
        "resultCurveTimeToTime",
        "resultCurveTimeToUnitless",
        "rowFromMatrix",
        "shadingEngine",
        "shot",
        "textureBakeSet",
        "trackInfoManager",
        "vertexBakeSet",
        "xgmDescription",
        "xgmSplineDescription",
    ),
}


def profile_plugin_requests(maya_version: int) -> tuple[str, ...]:
    """指定した Maya 版で固定 profile に読み込む plug-in 名を返す。

    Args:
        maya_version: 対応している Maya の major version。

    Returns:
        `dynamicGeometryAttributes` を対象版に応じて加えた plug-in 名。

    Raises:
        ValueError: `maya_version` が未対応の場合。
    """
    if maya_version not in SUPPORTED_MAYA_VERSIONS:
        raise ValueError(f"Unsupported Maya version: {maya_version}")
    if maya_version == 2025:
        return BASE_PROFILE_PLUGIN_REQUESTS

    insertion_index = BASE_PROFILE_PLUGIN_REQUESTS.index("ik2Bsolver")
    return (
        *BASE_PROFILE_PLUGIN_REQUESTS[:insertion_index],
        "dynamicGeometryAttributes",
        *BASE_PROFILE_PLUGIN_REQUESTS[insertion_index:],
    )


def introduced_node_types(maya_version: int) -> tuple[str, ...]:
    """指定版で追加されたノード型名を返す。

    Args:
        maya_version: 対応している Maya の major version。

    Raises:
        ValueError: `maya_version` が未対応の場合。
    """
    if maya_version not in SUPPORTED_MAYA_VERSIONS:
        raise ValueError(f"Unsupported Maya version: {maya_version}")
    return INTRODUCED_NODE_TYPES_BY_VERSION[maya_version]


def removed_node_types(maya_version: int) -> tuple[str, ...]:
    """指定版で削除されたノード型名を返す。

    Args:
        maya_version: 対応している Maya の major version。

    Raises:
        ValueError: `maya_version` が未対応の場合。
    """
    if maya_version not in SUPPORTED_MAYA_VERSIONS:
        raise ValueError(f"Unsupported Maya version: {maya_version}")
    return REMOVED_NODE_TYPES_BY_VERSION[maya_version]


def node_types_to_generate(maya_version: int) -> tuple[str, ...]:
    """指定版で追加または schema 変更された生成対象のノード型名を返す。

    Maya 2025 では初回 snapshot にない追加の基準ノード型を返す。

    Args:
        maya_version: 対応している Maya の major version。

    Raises:
        ValueError: `maya_version` が未対応の場合。
    """
    if maya_version == 2025:
        return BASELINE_ADDITIONAL_NODE_TYPES
    if maya_version not in SUPPORTED_MAYA_VERSIONS:
        raise ValueError(f"Unsupported Maya version: {maya_version}")
    return tuple(
        dict.fromkeys(
            (
                *introduced_node_types(maya_version),
                *SCHEMA_CHANGED_NODE_TYPES_BY_VERSION[maya_version],
            )
        )
    )
