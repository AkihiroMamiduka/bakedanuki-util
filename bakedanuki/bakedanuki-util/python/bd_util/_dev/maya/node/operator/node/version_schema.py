# coding: utf-8
from __future__ import annotations

SUPPORTED_MAYA_VERSIONS = (2025, 2026, 2027)

# Fixed Autodesk plug-in profile used to compare the generated NodeOperator
# surface. dynamicGeometryAttributes is bundled from Maya 2026 onward.
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

# These supported nodes were absent from the original Maya 2025 snapshot but
# are needed as the baseline for a later schema change or removal.
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

# Keep the fixed-profile inventory independent from the runtime registry.
# Tests compare these snapshots with NODE_TYPE_VERSION_RANGES so an accidental
# omission on either side is visible.
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
    if maya_version not in SUPPORTED_MAYA_VERSIONS:
        raise ValueError(f"Unsupported Maya version: {maya_version}")
    return INTRODUCED_NODE_TYPES_BY_VERSION[maya_version]


def removed_node_types(maya_version: int) -> tuple[str, ...]:
    if maya_version not in SUPPORTED_MAYA_VERSIONS:
        raise ValueError(f"Unsupported Maya version: {maya_version}")
    return REMOVED_NODE_TYPES_BY_VERSION[maya_version]


def node_types_to_generate(maya_version: int) -> tuple[str, ...]:
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
