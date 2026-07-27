# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_options import (
    ErrorColorBadPixelField,
    ErrorColorBadTextureField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.byte import ByteField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.dt.string import DataStringField


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


class GeneratedAiOptions(DG):
    __slots__ = ()

    NODE_TYPE = "aiOptions"

    renderGlobals = DataStringField()
    gop = renderGlobals

    imageFormat = DataStringField()
    img = imageFormat

    aovList = MessageField(multi=True, readable=False)
    aovs = aovList

    aovMode = AovModeEnumField(default_value=1)
    aovm = aovMode

    denoiseBeauty = BoolField(default_value=False)
    opdenb = denoiseBeauty

    outputVarianceAOVs = BoolField(default_value=False)
    varaovs = outputVarianceAOVs

    renderType = RenderTypeEnumField(default_value=0)
    arnrt = renderType

    outputAssBoundingBox = BoolField(default_value=False)
    assbb = outputAssBoundingBox

    preserve_scene_data = BoolField(default_value=True)
    preserveSceneData = preserve_scene_data

    progressive_rendering = BoolField(default_value=True)
    prog = progressive_rendering

    progressive_initial_level = LongField(default_value=-3, min_value=-10, max_value=100, soft_min_value=-3, soft_max_value=10)
    progil = progressive_initial_level

    threads_autodetect = BoolField(default_value=True)
    thr_auto = threads_autodetect

    threads = LongField(default_value=1, min_value=-1024, max_value=1024, soft_min_value=1)
    thrds = threads

    bucketScanning = BucketScanningEnumField(default_value=3)
    bktsc = bucketScanning

    bucketSize = LongField(default_value=64, min_value=16, soft_min_value=16, soft_max_value=256)
    bucket_size = bucketSize

    clear_before_render = BoolField(default_value=True)
    clear = clear_before_render

    force_scene_update_before_IPR_refresh = BoolField(default_value=False)
    rec_before_IPR = force_scene_update_before_IPR_refresh

    force_texture_cache_flush_after_render = BoolField(default_value=False)
    force_texture_flush = force_texture_cache_flush_after_render

    abortOnError = BoolField(default_value=True)
    abort_on_error = abortOnError

    errorColorBadTexture = ErrorColorBadTextureField(default_value=(1.0, 0.0, 0.0))
    error_color_bad_texture = errorColorBadTexture
    errorColorBadTextureR = errorColorBadTexture.errorColorBadTextureR
    error_color_bad_texturer = errorColorBadTextureR
    errorColorBadTextureG = errorColorBadTexture.errorColorBadTextureG
    error_color_bad_textureg = errorColorBadTextureG
    errorColorBadTextureB = errorColorBadTexture.errorColorBadTextureB
    error_color_bad_textureb = errorColorBadTextureB

    errorColorBadPixel = ErrorColorBadPixelField(default_value=(0.0, 0.0, 1.0))
    error_color_bad_pixel = errorColorBadPixel
    errorColorBadPixelR = errorColorBadPixel.errorColorBadPixelR
    error_color_bad_pixelr = errorColorBadPixelR
    errorColorBadPixelG = errorColorBadPixel.errorColorBadPixelG
    error_color_bad_pixelg = errorColorBadPixelG
    errorColorBadPixelB = errorColorBadPixel.errorColorBadPixelB
    error_color_bad_pixelb = errorColorBadPixelB

    abortOnLicenseFail = BoolField(default_value=True)
    abort_on_license_fail = abortOnLicenseFail

    skipLicenseCheck = BoolField(default_value=False)
    skip_license_check = skipLicenseCheck

    plugins_path = DataStringField()
    ppath = plugins_path

    AASamples = LongField(default_value=3, min_value=-10, max_value=1020, soft_min_value=1, soft_max_value=50)
    AA_samples = AASamples

    GIDiffuseSamples = LongField(default_value=2, min_value=0, max_value=100, soft_min_value=0, soft_max_value=10)
    GI_diffuse_samples = GIDiffuseSamples

    GISpecularSamples = LongField(default_value=2, min_value=0, max_value=100, soft_min_value=0, soft_max_value=10)
    GI_specular_samples = GISpecularSamples

    GITransmissionSamples = LongField(default_value=2, min_value=0, max_value=100, soft_min_value=0, soft_max_value=10)
    GI_transmission_samples = GITransmissionSamples

    GISssSamples = LongField(default_value=2, min_value=0, max_value=100, soft_min_value=0, soft_max_value=10)
    GI_sss_samples = GISssSamples

    GIVolumeSamples = LongField(default_value=2, min_value=0, soft_max_value=10)
    GI_volume_samples = GIVolumeSamples

    enableAdaptiveSampling = BoolField(default_value=False)
    enable_adaptive_sampling = enableAdaptiveSampling

    AASamplesMax = LongField(default_value=20, min_value=0, max_value=1020, soft_min_value=1, soft_max_value=100)
    AA_samples_max = AASamplesMax

    AAAdaptiveThreshold = FloatField(default_value=0.014999999664723873, min_value=0.0, soft_max_value=1.0)
    AA_adaptive_threshold = AAAdaptiveThreshold

    enableProgressiveRender = BoolField(default_value=False)
    enable_progressive_render = enableProgressiveRender

    regionMinX = LongField(default_value=-2147483648)
    region_min_x = regionMinX

    regionMaxX = LongField(default_value=-2147483648)
    region_max_x = regionMaxX

    regionMinY = LongField(default_value=-2147483648)
    region_min_y = regionMinY

    regionMaxY = LongField(default_value=-2147483648)
    region_max_y = regionMaxY

    use_sample_clamp = BoolField(default_value=False)
    usesmpclamp = use_sample_clamp

    use_sample_clamp_AOVs = BoolField(default_value=False)
    usesmpclampaovs = use_sample_clamp_AOVs

    AASampleClamp = FloatField(default_value=10.0, soft_min_value=0.0010000000474974513, soft_max_value=100.0)
    AA_sample_clamp = AASampleClamp

    indirectSampleClamp = FloatField(default_value=10.0, min_value=0.0, soft_min_value=0.0010000000474974513, soft_max_value=100.0)
    indirect_sample_clamp = indirectSampleClamp

    lock_sampling_noise = BoolField(default_value=False)
    locksn = lock_sampling_noise

    sssUseAutobump = BoolField(default_value=False)
    sss_use_autobump = sssUseAutobump

    indirectSpecularBlur = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)
    indirect_specular_blur = indirectSpecularBlur

    dielectricPriorities = BoolField(default_value=True)
    dielectric_priorities = dielectricPriorities

    AA_seed = TimeField(default_value=0.0)
    aaseed = AA_seed

    filterType = DataStringField()
    fltr = filterType

    GIDiffuseDepth = LongField(default_value=1, min_value=0, max_value=100, soft_min_value=0, soft_max_value=16)
    GI_diffuse_depth = GIDiffuseDepth

    GISpecularDepth = LongField(default_value=1, min_value=0, max_value=100, soft_min_value=0, soft_max_value=16)
    GI_specular_depth = GISpecularDepth

    GITransmissionDepth = LongField(default_value=8, min_value=0, max_value=100, soft_min_value=0, soft_max_value=16)
    GI_transmission_depth = GITransmissionDepth

    GIVolumeDepth = LongField(default_value=0, min_value=0, max_value=100, soft_min_value=0, soft_max_value=16)
    GI_volume_depth = GIVolumeDepth

    GITotalDepth = LongField(default_value=10, min_value=0, max_value=100, soft_min_value=0, soft_max_value=16)
    GI_total_depth = GITotalDepth

    autoTransparencyDepth = LongField(default_value=10, min_value=0, soft_min_value=0, soft_max_value=16)
    auto_transparency_depth = autoTransparencyDepth

    lightLinking = LightLinkingEnumField(default_value=1)
    llnk = lightLinking

    shadowLinking = ShadowLinkingEnumField(default_value=1)
    slnk = shadowLinking

    globalLightSamplesEnabled = BoolField(default_value=False)
    lsen = globalLightSamplesEnabled

    lightSamples = LongField(default_value=4, min_value=0, max_value=16, soft_max_value=10)
    light_samples = lightSamples

    lowLightThreshold = FloatField(default_value=0.0010000000474974513, min_value=0.0, soft_max_value=0.10000000149011612)
    low_light_threshold = lowLightThreshold

    motion_blur_enable = BoolField(default_value=False)
    mb_en = motion_blur_enable

    mb_lights_enable = BoolField(default_value=True)
    mb_len = mb_lights_enable

    mb_camera_enable = BoolField(default_value=True)
    mb_cen = mb_camera_enable

    mb_objects_enable = BoolField(default_value=True)
    mb_oen = mb_objects_enable

    mb_object_deform_enable = BoolField(default_value=True)
    mb_den = mb_object_deform_enable

    mb_shader_enable = BoolField(default_value=False)
    mb_sen = mb_shader_enable

    motion_steps = LongField(default_value=2, min_value=2, soft_max_value=30)
    mots = motion_steps

    range_type = Range_typeEnumField(default_value=1)
    rgtp = range_type

    motion_frames = FloatField(default_value=0.5, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    motf = motion_frames

    motion_start = FloatField(default_value=-0.25, soft_min_value=-1.0, soft_max_value=0.0)
    motstart = motion_start

    motion_end = FloatField(default_value=0.25, soft_min_value=0.0, soft_max_value=1.0)
    motend = motion_end

    maxSubdivisions = ByteField(default_value=255, min_value=0, max_value=255, soft_max_value=10)
    max_subdivisions = maxSubdivisions

    subdivFrustumCulling = BoolField(default_value=False)
    subdiv_frustum_culling = subdivFrustumCulling

    subdivFrustumPadding = FloatField(default_value=0.0)
    subdiv_frustum_padding = subdivFrustumPadding

    subdivDicingCamera = MessageField()
    subdiv_dicing_camera = subdivDicingCamera

    textureAutotile = LongField(default_value=0, min_value=0, soft_min_value=16, soft_max_value=64)
    texture_autotile = textureAutotile

    textureMaxMemoryMB = FloatField(default_value=4096.0, min_value=1024.0)
    texture_max_memory_MB = textureMaxMemoryMB

    textureMaxOpenFiles = LongField(default_value=0)
    texture_max_open_files = textureMaxOpenFiles

    textureAcceptUntiled = BoolField(default_value=True)
    texture_accept_untiled = textureAcceptUntiled

    textureAcceptUnmipped = BoolField(default_value=True)
    texture_accept_unmipped = textureAcceptUnmipped

    textureConservativeLookups = BoolField(default_value=True)
    texture_conservative_lookups = textureConservativeLookups

    textureAutoTxPath = DataStringField()
    texture_auto_tx_path = textureAutoTxPath

    autotile = BoolField(default_value=True)

    use_existing_tiled_textures = BoolField(default_value=True)
    usetx = use_existing_tiled_textures

    autotx = BoolField(default_value=True)

    renderDevice = RenderDeviceEnumField(default_value=0)
    rndrdvc = renderDevice

    render_device_fallback = Render_device_fallbackEnumField(default_value=0)
    rndfb = render_device_fallback

    manual_gpu_devices = BoolField(default_value=False)
    manualdevs = manual_gpu_devices

    render_devices = LongField(multi=True, default_value=0)
    rndev = render_devices

    gpu_max_texture_resolution = LongField(default_value=0)
    gpumtr = gpu_max_texture_resolution

    gpuDefaultNames = DataStringField()
    gpu_default_names = gpuDefaultNames

    gpuDefaultMinMemoryMB = LongField(default_value=512)
    gpu_default_min_memory_MB = gpuDefaultMinMemoryMB

    ignoreTextures = BoolField(default_value=False)
    ignore_textures = ignoreTextures

    ignoreShaders = BoolField(default_value=False)
    ignore_shaders = ignoreShaders

    ignoreAtmosphere = BoolField(default_value=False)
    ignore_atmosphere = ignoreAtmosphere

    ignoreLights = BoolField(default_value=False)
    ignore_lights = ignoreLights

    ignoreShadows = BoolField(default_value=False)
    ignore_shadows = ignoreShadows

    ignoreSubdivision = BoolField(default_value=False)
    ignore_subdivision = ignoreSubdivision

    ignoreDisplacement = BoolField(default_value=False)
    ignore_displacement = ignoreDisplacement

    ignoreBump = BoolField(default_value=False)
    ignore_bump = ignoreBump

    ignoreSmoothing = BoolField(default_value=False)
    ignore_smoothing = ignoreSmoothing

    ignoreMotionBlur = BoolField(default_value=False)
    ignore_motion_blur = ignoreMotionBlur

    ignoreMotion = BoolField(default_value=False)
    ignore_motion = ignoreMotion

    ignoreSss = BoolField(default_value=False)
    ignore_sss = ignoreSss

    ignoreDof = BoolField(default_value=False)
    ignore_dof = ignoreDof

    ignoreOperators = BoolField(default_value=False)
    ignore_operators = ignoreOperators

    ignoreImagers = BoolField(default_value=False)
    ignore_imagers = ignoreImagers

    ignore_list = DataStringField()
    igl = ignore_list

    output_ass_filename = DataStringField()
    file = output_ass_filename

    output_ass_compressed = BoolField(default_value=False)
    oasc = output_ass_compressed

    output_ass_mask = LongField(default_value=65535, min_value=0, max_value=65535)
    oamask = output_ass_mask

    log_to_file = BoolField(default_value=False)
    ltofi = log_to_file

    log_to_console = BoolField(default_value=True)
    ltocon = log_to_console

    log_filename = DataStringField()
    logf = log_filename

    log_max_warnings = LongField(default_value=5, min_value=0, soft_max_value=100)
    logw = log_max_warnings

    log_verbosity = Log_verbosityEnumField(default_value=1)
    logv = log_verbosity

    stats_enable = BoolField(default_value=False)
    statse = stats_enable

    stats_file = DataStringField()
    statsf = stats_file

    stats_mode = Stats_modeEnumField(default_value=1)
    statsm = stats_mode

    profile_enable = BoolField(default_value=False)
    profe = profile_enable

    profile_file = DataStringField()
    proff = profile_file

    mtoa_translation_info = BoolField(default_value=False)
    mtrinf = mtoa_translation_info

    background = MessageField()
    bkg = background

    atmosphere = MessageField()
    atm = atmosphere

    operator = MessageField()

    imagers = MessageField(multi=True, readable=False)

    displayAOV = DataStringField()
    daov = displayAOV

    binaryAss = BoolField(default_value=True)
    binary_ass = binaryAss

    referenceTime = FloatField(default_value=0.0)
    reference_time = referenceTime

    enable_swatch_render = BoolField(default_value=True)
    ensr = enable_swatch_render

    procedural_searchpath = DataStringField()
    pspath = procedural_searchpath

    plugin_searchpath = DataStringField()
    sspath = plugin_searchpath

    texture_searchpath = DataStringField()
    tspath = texture_searchpath

    driver = MessageField(readable=False)
    drvr = driver

    filter = MessageField(readable=False)
    filt = filter

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    drivers = MessageField(multi=True, readable=False)

    expandProcedurals = BoolField(default_value=False)
    expand_procedurals = expandProcedurals

    kickRenderFlags = DataStringField()
    kick_render_flags = kickRenderFlags

    absoluteTexturePaths = BoolField(default_value=True)
    absolute_texture_paths = absoluteTexturePaths

    absoluteProceduralPaths = BoolField(default_value=True)
    absolute_procedural_paths = absoluteProceduralPaths

    forceTranslateShadingEngines = BoolField(default_value=False)
    force_translate_shading_engines = forceTranslateShadingEngines

    exportAllShadingGroups = BoolField(default_value=False)
    export_all_shading_groups = exportAllShadingGroups

    exportFullPaths = BoolField(default_value=True)
    export_full_paths = exportFullPaths

    exportSeparator = ExportSeparatorEnumField(default_value=1)
    export_separator = exportSeparator

    exportNamespace = ExportNamespaceEnumField(default_value=1)
    export_namespace = exportNamespace

    exportDagName = ExportDagNameEnumField(default_value=0)
    export_dag_name = exportDagName

    exportPrefix = DataStringField()
    export_prefix = exportPrefix

    exportShadingEngine = BoolField(default_value=False)
    export_shading_engine = exportShadingEngine

    version = DataStringField()

    standinDrawOverride = StandinDrawOverrideEnumField(default_value=0)
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

    renderUnit = RenderUnitEnumField(default_value=0)
    render_unit = renderUnit

    sceneScale = DoubleField(default_value=1.0, min_value=0.0, soft_min_value=0.01, soft_max_value=5.0)
    scene_scale = sceneScale

    offsetOrigin = BoolField(default_value=False)
    offset_origin = offsetOrigin

    origin = MessageField()
    orig = origin

    aovShaders = MessageField(multi=True)
    aov_shaders = aovShaders

    GI_glossy_samples = LongField(default_value=1, writable=False)

    GI_refraction_samples = LongField(default_value=1, writable=False)

    textureDiffuseBlur = FloatField(default_value=0.0, writable=False)
    texture_diffuse_blur = textureDiffuseBlur

    textureSpecularBlur = FloatField(default_value=0.0, writable=False)
    texture_specular_blur = textureSpecularBlur

    exportMayaUsd = BoolField(default_value=False)
    export_maya_usd = exportMayaUsd

    avpRegionLeft = LongField(default_value=0, min_value=0)
    avp_region_left = avpRegionLeft

    avpRegionRight = LongField(default_value=0, min_value=0)
    avp_region_right = avpRegionRight

    avpRegionBottom = LongField(default_value=0, min_value=0)
    avp_region_bottom = avpRegionBottom

    avpRegionTop = LongField(default_value=0, min_value=0)
    avp_region_top = avpRegionTop
