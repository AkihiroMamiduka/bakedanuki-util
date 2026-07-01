# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_options import (
    ErrorColorBadPixelField,
    ErrorColorBadTextureField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.byte import ByteField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


class AovModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISABLED = 0
    ENABLED = 1
    BATCH_ONLY = 2


class AovModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISABLED = 0
    ENABLED = 1
    BATCH_ONLY = 2

    NAME_MAP = {
        DISABLED: "disabled",
        ENABLED: "enabled",
        BATCH_ONLY: "batch_only",
    }


class AovModeEnumField(
    EnumField[AovModeEnumAttrOperator, AovModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AovModeEnumAttrOperator
    PLUG_CLS = AovModeEnumPlugOperator


class RenderTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    INTERACTIVE = 0
    EXPORT_ASS = 1
    EXPORT_ASS_AND_KICK = 2


class RenderTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    INTERACTIVE = 0
    EXPORT_ASS = 1
    EXPORT_ASS_AND_KICK = 2

    NAME_MAP = {
        INTERACTIVE: "Interactive",
        EXPORT_ASS: "Export Ass",
        EXPORT_ASS_AND_KICK: "Export Ass and Kick",
    }


class RenderTypeEnumField(
    EnumField[RenderTypeEnumAttrOperator, RenderTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderTypeEnumAttrOperator
    PLUG_CLS = RenderTypeEnumPlugOperator


class BucketScanningEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TOP = 0
    LEFT = 1
    RANDOM = 2
    SPIRAL = 3
    HILBERT = 4


class BucketScanningEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TOP = 0
    LEFT = 1
    RANDOM = 2
    SPIRAL = 3
    HILBERT = 4

    NAME_MAP = {
        TOP: "top",
        LEFT: "left",
        RANDOM: "random",
        SPIRAL: "spiral",
        HILBERT: "hilbert",
    }


class BucketScanningEnumField(
    EnumField[BucketScanningEnumAttrOperator, BucketScanningEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BucketScanningEnumAttrOperator
    PLUG_CLS = BucketScanningEnumPlugOperator


class LightLinkingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    MAYA_LIGHT_LINKS = 1


class LightLinkingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    MAYA_LIGHT_LINKS = 1

    NAME_MAP = {
        NONE: "None",
        MAYA_LIGHT_LINKS: "Maya Light Links",
    }


class LightLinkingEnumField(
    EnumField[LightLinkingEnumAttrOperator, LightLinkingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightLinkingEnumAttrOperator
    PLUG_CLS = LightLinkingEnumPlugOperator


class ShadowLinkingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    FOLLOWS_LIGHT_LINKING = 1
    MAYA_SHADOW_LINKS = 2


class ShadowLinkingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    FOLLOWS_LIGHT_LINKING = 1
    MAYA_SHADOW_LINKS = 2

    NAME_MAP = {
        NONE: "None",
        FOLLOWS_LIGHT_LINKING: "Follows Light Linking",
        MAYA_SHADOW_LINKS: "Maya Shadow Links",
    }


class ShadowLinkingEnumField(
    EnumField[ShadowLinkingEnumAttrOperator, ShadowLinkingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowLinkingEnumAttrOperator
    PLUG_CLS = ShadowLinkingEnumPlugOperator


class Range_typeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    START_ON_FRAME = 0
    CENTER_ON_FRAME = 1
    END_ON_FRAME = 2
    CUSTOM = 3


class Range_typeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    START_ON_FRAME = 0
    CENTER_ON_FRAME = 1
    END_ON_FRAME = 2
    CUSTOM = 3

    NAME_MAP = {
        START_ON_FRAME: "Start On Frame",
        CENTER_ON_FRAME: "Center On Frame",
        END_ON_FRAME: "End On Frame",
        CUSTOM: "Custom",
    }


class Range_typeEnumField(
    EnumField[Range_typeEnumAttrOperator, Range_typeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Range_typeEnumAttrOperator
    PLUG_CLS = Range_typeEnumPlugOperator


class RenderDeviceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CPU = 0
    GPU = 1


class RenderDeviceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CPU = 0
    GPU = 1

    NAME_MAP = {
        CPU: "CPU",
        GPU: "GPU",
    }


class RenderDeviceEnumField(
    EnumField[RenderDeviceEnumAttrOperator, RenderDeviceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderDeviceEnumAttrOperator
    PLUG_CLS = RenderDeviceEnumPlugOperator


class Render_device_fallbackEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ERROR = 0
    CPU = 1


class Render_device_fallbackEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ERROR = 0
    CPU = 1

    NAME_MAP = {
        ERROR: "Error",
        CPU: "CPU",
    }


class Render_device_fallbackEnumField(
    EnumField[Render_device_fallbackEnumAttrOperator, Render_device_fallbackEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Render_device_fallbackEnumAttrOperator
    PLUG_CLS = Render_device_fallbackEnumPlugOperator


class Log_verbosityEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ERRORS = 0
    WARNINGS = 1
    INFO = 2
    DEBUG = 3


class Log_verbosityEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ERRORS = 0
    WARNINGS = 1
    INFO = 2
    DEBUG = 3

    NAME_MAP = {
        ERRORS: "Errors",
        WARNINGS: "Warnings",
        INFO: "Info",
        DEBUG: "Debug",
    }


class Log_verbosityEnumField(
    EnumField[Log_verbosityEnumAttrOperator, Log_verbosityEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Log_verbosityEnumAttrOperator
    PLUG_CLS = Log_verbosityEnumPlugOperator


class Stats_modeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OVERWRITE = 0
    APPEND = 1


class Stats_modeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OVERWRITE = 0
    APPEND = 1

    NAME_MAP = {
        OVERWRITE: "Overwrite",
        APPEND: "Append",
    }


class Stats_modeEnumField(
    EnumField[Stats_modeEnumAttrOperator, Stats_modeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Stats_modeEnumAttrOperator
    PLUG_CLS = Stats_modeEnumPlugOperator


class ExportSeparatorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PIPE = 0
    SLASH = 1


class ExportSeparatorEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PIPE = 0
    SLASH = 1

    NAME_MAP = {
        PIPE: "|",
        SLASH: "/",
    }


class ExportSeparatorEnumField(
    EnumField[ExportSeparatorEnumAttrOperator, ExportSeparatorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExportSeparatorEnumAttrOperator
    PLUG_CLS = ExportSeparatorEnumPlugOperator


class ExportNamespaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1
    ROOT = 2


class ExportNamespaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1
    ROOT = 2

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
        ROOT: "Root",
    }


class ExportNamespaceEnumField(
    EnumField[ExportNamespaceEnumAttrOperator, ExportNamespaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExportNamespaceEnumAttrOperator
    PLUG_CLS = ExportNamespaceEnumPlugOperator


class ExportDagNameEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SHAPE = 0
    TRANSFORM = 1


class ExportDagNameEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SHAPE = 0
    TRANSFORM = 1

    NAME_MAP = {
        SHAPE: "Shape",
        TRANSFORM: "Transform",
    }


class ExportDagNameEnumField(
    EnumField[ExportDagNameEnumAttrOperator, ExportDagNameEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExportDagNameEnumAttrOperator
    PLUG_CLS = ExportDagNameEnumPlugOperator


class StandinDrawOverrideEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    USE_LOCAL_SETTINGS = 0
    BOUNDING_BOX = 1
    DISABLE_DRAW = 2
    DISABLE_LOAD = 3


class StandinDrawOverrideEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    USE_LOCAL_SETTINGS = 0
    BOUNDING_BOX = 1
    DISABLE_DRAW = 2
    DISABLE_LOAD = 3

    NAME_MAP = {
        USE_LOCAL_SETTINGS: "Use Local Settings",
        BOUNDING_BOX: "Bounding Box",
        DISABLE_DRAW: "Disable Draw",
        DISABLE_LOAD: "Disable Load",
    }


class StandinDrawOverrideEnumField(
    EnumField[StandinDrawOverrideEnumAttrOperator, StandinDrawOverrideEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StandinDrawOverrideEnumAttrOperator
    PLUG_CLS = StandinDrawOverrideEnumPlugOperator


class RenderUnitEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    USE_MAYA_UNIT = 0
    USE_CUSTOM_SCALING = 1
    INCH = 2
    FEET = 3
    YARD = 4
    MILE = 5
    MILLIMETER = 6
    CENTIMETER = 7
    KILOMETER = 8
    METER = 9


class RenderUnitEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    USE_MAYA_UNIT = 0
    USE_CUSTOM_SCALING = 1
    INCH = 2
    FEET = 3
    YARD = 4
    MILE = 5
    MILLIMETER = 6
    CENTIMETER = 7
    KILOMETER = 8
    METER = 9

    NAME_MAP = {
        USE_MAYA_UNIT: "Use Maya Unit",
        USE_CUSTOM_SCALING: "Use Custom Scaling",
        INCH: "Inch",
        FEET: "Feet",
        YARD: "Yard",
        MILE: "Mile",
        MILLIMETER: "Millimeter",
        CENTIMETER: "Centimeter",
        KILOMETER: "Kilometer",
        METER: "Meter",
    }


class RenderUnitEnumField(
    EnumField[RenderUnitEnumAttrOperator, RenderUnitEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderUnitEnumAttrOperator
    PLUG_CLS = RenderUnitEnumPlugOperator


class AiOptions(DG):
    __slots__ = ()

    NODE_TYPE = "aiOptions"

    renderGlobals = DataStringField()
    gop = renderGlobals

    imageFormat = DataStringField()
    img = imageFormat

    aovList = MessageField(multi=True)
    aovs = aovList

    aovMode = AovModeEnumField()
    aovm = aovMode

    denoiseBeauty = BoolField()
    opdenb = denoiseBeauty

    outputVarianceAOVs = BoolField()
    varaovs = outputVarianceAOVs

    renderType = RenderTypeEnumField()
    arnrt = renderType

    outputAssBoundingBox = BoolField()
    assbb = outputAssBoundingBox

    preserve_scene_data = BoolField()
    preserveSceneData = preserve_scene_data

    progressive_rendering = BoolField()
    prog = progressive_rendering

    progressive_initial_level = LongField()
    progil = progressive_initial_level

    threads_autodetect = BoolField()
    thr_auto = threads_autodetect

    threads = LongField()
    thrds = threads

    bucketScanning = BucketScanningEnumField()
    bktsc = bucketScanning

    bucketSize = LongField()
    bucket_size = bucketSize

    clear_before_render = BoolField()
    clear = clear_before_render

    force_scene_update_before_IPR_refresh = BoolField()
    rec_before_IPR = force_scene_update_before_IPR_refresh

    force_texture_cache_flush_after_render = BoolField()
    force_texture_flush = force_texture_cache_flush_after_render

    abortOnError = BoolField()
    abort_on_error = abortOnError

    errorColorBadTexture = ErrorColorBadTextureField()
    error_color_bad_texture = errorColorBadTexture
    errorColorBadTextureR = errorColorBadTexture.errorColorBadTextureR
    error_color_bad_texturer = errorColorBadTextureR
    errorColorBadTextureG = errorColorBadTexture.errorColorBadTextureG
    error_color_bad_textureg = errorColorBadTextureG
    errorColorBadTextureB = errorColorBadTexture.errorColorBadTextureB
    error_color_bad_textureb = errorColorBadTextureB

    errorColorBadPixel = ErrorColorBadPixelField()
    error_color_bad_pixel = errorColorBadPixel
    errorColorBadPixelR = errorColorBadPixel.errorColorBadPixelR
    error_color_bad_pixelr = errorColorBadPixelR
    errorColorBadPixelG = errorColorBadPixel.errorColorBadPixelG
    error_color_bad_pixelg = errorColorBadPixelG
    errorColorBadPixelB = errorColorBadPixel.errorColorBadPixelB
    error_color_bad_pixelb = errorColorBadPixelB

    abortOnLicenseFail = BoolField()
    abort_on_license_fail = abortOnLicenseFail

    skipLicenseCheck = BoolField()
    skip_license_check = skipLicenseCheck

    plugins_path = DataStringField()
    ppath = plugins_path

    AASamples = LongField()
    AA_samples = AASamples

    GIDiffuseSamples = LongField()
    GI_diffuse_samples = GIDiffuseSamples

    GISpecularSamples = LongField()
    GI_specular_samples = GISpecularSamples

    GITransmissionSamples = LongField()
    GI_transmission_samples = GITransmissionSamples

    GISssSamples = LongField()
    GI_sss_samples = GISssSamples

    GIVolumeSamples = LongField()
    GI_volume_samples = GIVolumeSamples

    enableAdaptiveSampling = BoolField()
    enable_adaptive_sampling = enableAdaptiveSampling

    AASamplesMax = LongField()
    AA_samples_max = AASamplesMax

    AAAdaptiveThreshold = FloatField()
    AA_adaptive_threshold = AAAdaptiveThreshold

    enableProgressiveRender = BoolField()
    enable_progressive_render = enableProgressiveRender

    regionMinX = LongField()
    region_min_x = regionMinX

    regionMaxX = LongField()
    region_max_x = regionMaxX

    regionMinY = LongField()
    region_min_y = regionMinY

    regionMaxY = LongField()
    region_max_y = regionMaxY

    use_sample_clamp = BoolField()
    usesmpclamp = use_sample_clamp

    use_sample_clamp_AOVs = BoolField()
    usesmpclampaovs = use_sample_clamp_AOVs

    AASampleClamp = FloatField()
    AA_sample_clamp = AASampleClamp

    indirectSampleClamp = FloatField()
    indirect_sample_clamp = indirectSampleClamp

    lock_sampling_noise = BoolField()
    locksn = lock_sampling_noise

    sssUseAutobump = BoolField()
    sss_use_autobump = sssUseAutobump

    indirectSpecularBlur = FloatField()
    indirect_specular_blur = indirectSpecularBlur

    dielectricPriorities = BoolField()
    dielectric_priorities = dielectricPriorities

    AA_seed = TimeField()
    aaseed = AA_seed

    filterType = DataStringField()
    fltr = filterType

    GIDiffuseDepth = LongField()
    GI_diffuse_depth = GIDiffuseDepth

    GISpecularDepth = LongField()
    GI_specular_depth = GISpecularDepth

    GITransmissionDepth = LongField()
    GI_transmission_depth = GITransmissionDepth

    GIVolumeDepth = LongField()
    GI_volume_depth = GIVolumeDepth

    GITotalDepth = LongField()
    GI_total_depth = GITotalDepth

    autoTransparencyDepth = LongField()
    auto_transparency_depth = autoTransparencyDepth

    lightLinking = LightLinkingEnumField()
    llnk = lightLinking

    shadowLinking = ShadowLinkingEnumField()
    slnk = shadowLinking

    globalLightSamplesEnabled = BoolField()
    lsen = globalLightSamplesEnabled

    lightSamples = LongField()
    light_samples = lightSamples

    lowLightThreshold = FloatField()
    low_light_threshold = lowLightThreshold

    motion_blur_enable = BoolField()
    mb_en = motion_blur_enable

    mb_lights_enable = BoolField()
    mb_len = mb_lights_enable

    mb_camera_enable = BoolField()
    mb_cen = mb_camera_enable

    mb_objects_enable = BoolField()
    mb_oen = mb_objects_enable

    mb_object_deform_enable = BoolField()
    mb_den = mb_object_deform_enable

    mb_shader_enable = BoolField()
    mb_sen = mb_shader_enable

    motion_steps = LongField()
    mots = motion_steps

    range_type = Range_typeEnumField()
    rgtp = range_type

    motion_frames = FloatField()
    motf = motion_frames

    motion_start = FloatField()
    motstart = motion_start

    motion_end = FloatField()
    motend = motion_end

    maxSubdivisions = ByteField()
    max_subdivisions = maxSubdivisions

    subdivFrustumCulling = BoolField()
    subdiv_frustum_culling = subdivFrustumCulling

    subdivFrustumPadding = FloatField()
    subdiv_frustum_padding = subdivFrustumPadding

    subdivDicingCamera = MessageField()
    subdiv_dicing_camera = subdivDicingCamera

    textureAutotile = LongField()
    texture_autotile = textureAutotile

    textureMaxMemoryMB = FloatField()
    texture_max_memory_MB = textureMaxMemoryMB

    textureMaxOpenFiles = LongField()
    texture_max_open_files = textureMaxOpenFiles

    textureAcceptUntiled = BoolField()
    texture_accept_untiled = textureAcceptUntiled

    textureAcceptUnmipped = BoolField()
    texture_accept_unmipped = textureAcceptUnmipped

    textureConservativeLookups = BoolField()
    texture_conservative_lookups = textureConservativeLookups

    textureAutoTxPath = DataStringField()
    texture_auto_tx_path = textureAutoTxPath

    autotile = BoolField()

    use_existing_tiled_textures = BoolField()
    usetx = use_existing_tiled_textures

    autotx = BoolField()

    renderDevice = RenderDeviceEnumField()
    rndrdvc = renderDevice

    render_device_fallback = Render_device_fallbackEnumField()
    rndfb = render_device_fallback

    manual_gpu_devices = BoolField()
    manualdevs = manual_gpu_devices

    render_devices = LongField(multi=True)
    rndev = render_devices

    gpu_max_texture_resolution = LongField()
    gpumtr = gpu_max_texture_resolution

    gpuDefaultNames = DataStringField()
    gpu_default_names = gpuDefaultNames

    gpuDefaultMinMemoryMB = LongField()
    gpu_default_min_memory_MB = gpuDefaultMinMemoryMB

    ignoreTextures = BoolField()
    ignore_textures = ignoreTextures

    ignoreShaders = BoolField()
    ignore_shaders = ignoreShaders

    ignoreAtmosphere = BoolField()
    ignore_atmosphere = ignoreAtmosphere

    ignoreLights = BoolField()
    ignore_lights = ignoreLights

    ignoreShadows = BoolField()
    ignore_shadows = ignoreShadows

    ignoreSubdivision = BoolField()
    ignore_subdivision = ignoreSubdivision

    ignoreDisplacement = BoolField()
    ignore_displacement = ignoreDisplacement

    ignoreBump = BoolField()
    ignore_bump = ignoreBump

    ignoreSmoothing = BoolField()
    ignore_smoothing = ignoreSmoothing

    ignoreMotionBlur = BoolField()
    ignore_motion_blur = ignoreMotionBlur

    ignoreMotion = BoolField()
    ignore_motion = ignoreMotion

    ignoreSss = BoolField()
    ignore_sss = ignoreSss

    ignoreDof = BoolField()
    ignore_dof = ignoreDof

    ignoreOperators = BoolField()
    ignore_operators = ignoreOperators

    ignoreImagers = BoolField()
    ignore_imagers = ignoreImagers

    ignore_list = DataStringField()
    igl = ignore_list

    output_ass_filename = DataStringField()
    file = output_ass_filename

    output_ass_compressed = BoolField()
    oasc = output_ass_compressed

    output_ass_mask = LongField()
    oamask = output_ass_mask

    log_to_file = BoolField()
    ltofi = log_to_file

    log_to_console = BoolField()
    ltocon = log_to_console

    log_filename = DataStringField()
    logf = log_filename

    log_max_warnings = LongField()
    logw = log_max_warnings

    log_verbosity = Log_verbosityEnumField()
    logv = log_verbosity

    stats_enable = BoolField()
    statse = stats_enable

    stats_file = DataStringField()
    statsf = stats_file

    stats_mode = Stats_modeEnumField()
    statsm = stats_mode

    profile_enable = BoolField()
    profe = profile_enable

    profile_file = DataStringField()
    proff = profile_file

    mtoa_translation_info = BoolField()
    mtrinf = mtoa_translation_info

    background = MessageField()
    bkg = background

    atmosphere = MessageField()
    atm = atmosphere

    operator = MessageField()

    imagers = MessageField(multi=True)

    displayAOV = DataStringField()
    daov = displayAOV

    binaryAss = BoolField()
    binary_ass = binaryAss

    referenceTime = FloatField()
    reference_time = referenceTime

    enable_swatch_render = BoolField()
    ensr = enable_swatch_render

    procedural_searchpath = DataStringField()
    pspath = procedural_searchpath

    plugin_searchpath = DataStringField()
    sspath = plugin_searchpath

    texture_searchpath = DataStringField()
    tspath = texture_searchpath

    driver = MessageField()
    drvr = driver

    filter = MessageField()
    filt = filter

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    drivers = MessageField(multi=True)

    expandProcedurals = BoolField()
    expand_procedurals = expandProcedurals

    kickRenderFlags = DataStringField()
    kick_render_flags = kickRenderFlags

    absoluteTexturePaths = BoolField()
    absolute_texture_paths = absoluteTexturePaths

    absoluteProceduralPaths = BoolField()
    absolute_procedural_paths = absoluteProceduralPaths

    forceTranslateShadingEngines = BoolField()
    force_translate_shading_engines = forceTranslateShadingEngines

    exportAllShadingGroups = BoolField()
    export_all_shading_groups = exportAllShadingGroups

    exportFullPaths = BoolField()
    export_full_paths = exportFullPaths

    exportSeparator = ExportSeparatorEnumField()
    export_separator = exportSeparator

    exportNamespace = ExportNamespaceEnumField()
    export_namespace = exportNamespace

    exportDagName = ExportDagNameEnumField()
    export_dag_name = exportDagName

    exportPrefix = DataStringField()
    export_prefix = exportPrefix

    exportShadingEngine = BoolField()
    export_shading_engine = exportShadingEngine

    version = DataStringField()

    standinDrawOverride = StandinDrawOverrideEnumField()
    standin_draw_override = standinDrawOverride

    PostTranslation = DataStringField()
    post_translation = PostTranslation

    IPRRefinementStarted = DataStringField()
    ipr_refinement_started = IPRRefinementStarted

    IPRRefinementFinished = DataStringField()
    ipr_refinement_finished = IPRRefinementFinished

    IPRStepStarted = DataStringField()
    ipr_step_started = IPRStepStarted

    IPRStepFinished = DataStringField()
    ipr_step_finished = IPRStepFinished

    outputOverscan = DataStringField()
    output_overscan = outputOverscan

    renderUnit = RenderUnitEnumField()
    render_unit = renderUnit

    sceneScale = DoubleField()
    scene_scale = sceneScale

    offsetOrigin = BoolField()
    offset_origin = offsetOrigin

    origin = MessageField()
    orig = origin

    aovShaders = MessageField(multi=True)
    aov_shaders = aovShaders

    GI_glossy_samples = LongField()

    GI_refraction_samples = LongField()

    textureDiffuseBlur = FloatField()
    texture_diffuse_blur = textureDiffuseBlur

    textureSpecularBlur = FloatField()
    texture_specular_blur = textureSpecularBlur

    exportMayaUsd = BoolField()
    export_maya_usd = exportMayaUsd

    avpRegionLeft = LongField()
    avp_region_left = avpRegionLeft

    avpRegionRight = LongField()
    avp_region_right = avpRegionRight

    avpRegionBottom = LongField()
    avp_region_bottom = avpRegionBottom

    avpRegionTop = LongField()
    avp_region_top = avpRegionTop
