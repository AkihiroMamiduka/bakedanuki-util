# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from ..modifier import ModifierManager
from ..operator.node._core import DEFAULT_VALUE_AUTO_ADD_ATTR, NodeOperator
from ..operator.node.dg.about_to_set_value_test_node import AboutToSetValueTestNode
from ..operator.node.dg.abs_override import AbsOverride
from ..operator.node.dg.abs_unique_override import AbsUniqueOverride
from ..operator.node.dg.absolute import Absolute
from ..operator.node.dg.acos import Acos
from ..operator.node.dg.add_double_linear import AddDoubleLinear
from ..operator.node.dg.add_matrix import AddMatrix
from ..operator.node.dg.adsk_material import AdskMaterial
from ..operator.node.dg.adsk_prepare_render_globals import AdskPrepareRenderGlobals
from ..operator.node.dg.ai_abs import AiAbs
from ..operator.node.dg.ai_add import AiAdd
from ..operator.node.dg.ai_ambient_occlusion import AiAmbientOcclusion
from ..operator.node.dg.ai_aov import AiAOV
from ..operator.node.dg.ai_aov_driver import AiAOVDriver
from ..operator.node.dg.ai_aov_filter import AiAOVFilter
from ..operator.node.dg.ai_atan import AiAtan
from ..operator.node.dg.ai_atmosphere_volume import AiAtmosphereVolume
from ..operator.node.dg.ai_axf_shader import AiAxfShader
from ..operator.node.dg.ai_barndoor import AiBarndoor
from ..operator.node.dg.ai_blackbody import AiBlackbody
from ..operator.node.dg.ai_bump2d import AiBump2d
from ..operator.node.dg.ai_bump3d import AiBump3d
from ..operator.node.dg.ai_cache import AiCache
from ..operator.node.dg.ai_camera_projection import AiCameraProjection
from ..operator.node.dg.ai_car_paint import AiCarPaint
from ..operator.node.dg.ai_cell_noise import AiCellNoise
from ..operator.node.dg.ai_checkerboard import AiCheckerboard
from ..operator.node.dg.ai_clamp import AiClamp
from ..operator.node.dg.ai_clip_geo import AiClipGeo
from ..operator.node.dg.ai_collection import AiCollection
from ..operator.node.dg.ai_color_convert import AiColorConvert
from ..operator.node.dg.ai_color_correct import AiColorCorrect
from ..operator.node.dg.ai_color_jitter import AiColorJitter
from ..operator.node.dg.ai_color_to_float import AiColorToFloat
from ..operator.node.dg.ai_compare import AiCompare
from ..operator.node.dg.ai_complement import AiComplement
from ..operator.node.dg.ai_complex_ior import AiComplexIor
from ..operator.node.dg.ai_composite import AiComposite
from ..operator.node.dg.ai_cross import AiCross
from ..operator.node.dg.ai_curvature import AiCurvature
from ..operator.node.dg.ai_disable import AiDisable
from ..operator.node.dg.ai_distance import AiDistance
from ..operator.node.dg.ai_divide import AiDivide
from ..operator.node.dg.ai_dot import AiDot
from ..operator.node.dg.ai_exp import AiExp
from ..operator.node.dg.ai_facing_ratio import AiFacingRatio
from ..operator.node.dg.ai_flakes import AiFlakes
from ..operator.node.dg.ai_flat import AiFlat
from ..operator.node.dg.ai_float_to_int import AiFloatToInt
from ..operator.node.dg.ai_float_to_matrix import AiFloatToMatrix
from ..operator.node.dg.ai_float_to_rgba import AiFloatToRgba
from ..operator.node.dg.ai_fog import AiFog
from ..operator.node.dg.ai_fraction import AiFraction
from ..operator.node.dg.ai_gobo import AiGobo
from ..operator.node.dg.ai_hair import AiHair
from ..operator.node.dg.ai_image import AiImage
from ..operator.node.dg.ai_imager_color_correct import AiImagerColorCorrect
from ..operator.node.dg.ai_imager_color_curves import AiImagerColorCurves
from ..operator.node.dg.ai_imager_denoiser_noice import AiImagerDenoiserNoice
from ..operator.node.dg.ai_imager_denoiser_oidn import AiImagerDenoiserOidn
from ..operator.node.dg.ai_imager_denoiser_optix import AiImagerDenoiserOptix
from ..operator.node.dg.ai_imager_exposure import AiImagerExposure
from ..operator.node.dg.ai_imager_lens_effects import AiImagerLensEffects
from ..operator.node.dg.ai_imager_light_mixer import AiImagerLightMixer
from ..operator.node.dg.ai_imager_overlay import AiImagerOverlay
from ..operator.node.dg.ai_imager_tonemap import AiImagerTonemap
from ..operator.node.dg.ai_imager_white_balance import AiImagerWhiteBalance
from ..operator.node.dg.ai_include_graph import AiIncludeGraph
from ..operator.node.dg.ai_is_finite import AiIsFinite
from ..operator.node.dg.ai_lambert import AiLambert
from ..operator.node.dg.ai_layer_float import AiLayerFloat
from ..operator.node.dg.ai_layer_rgba import AiLayerRgba
from ..operator.node.dg.ai_layer_shader import AiLayerShader
from ..operator.node.dg.ai_length import AiLength
from ..operator.node.dg.ai_light_decay import AiLightDecay
from ..operator.node.dg.ai_log import AiLog
from ..operator.node.dg.ai_look_switch import AiLookSwitch
from ..operator.node.dg.ai_material_x_shader import AiMaterialXShader
from ..operator.node.dg.ai_materialx import AiMaterialx
from ..operator.node.dg.ai_matrix_interpolate import AiMatrixInterpolate
from ..operator.node.dg.ai_matrix_multiply_vector import AiMatrixMultiplyVector
from ..operator.node.dg.ai_matrix_transform import AiMatrixTransform
from ..operator.node.dg.ai_matte import AiMatte
from ..operator.node.dg.ai_max import AiMax
from ..operator.node.dg.ai_merge import AiMerge
from ..operator.node.dg.ai_min import AiMin
from ..operator.node.dg.ai_mix_shader import AiMixShader
from ..operator.node.dg.ai_modulo import AiModulo
from ..operator.node.dg.ai_motion_vector import AiMotionVector
from ..operator.node.dg.ai_multiply import AiMultiply
from ..operator.node.dg.ai_negate import AiNegate
from ..operator.node.dg.ai_noise import AiNoise
from ..operator.node.dg.ai_normal_map import AiNormalMap
from ..operator.node.dg.ai_normalize import AiNormalize
from ..operator.node.dg.ai_options import AiOptions
from ..operator.node.dg.ai_osl_shader import AiOslShader
from ..operator.node.dg.ai_passthrough import AiPassthrough
from ..operator.node.dg.ai_physical_sky import AiPhysicalSky
from ..operator.node.dg.ai_pow import AiPow
from ..operator.node.dg.ai_ramp_float import AiRampFloat
from ..operator.node.dg.ai_ramp_rgb import AiRampRgb
from ..operator.node.dg.ai_random import AiRandom
from ..operator.node.dg.ai_range import AiRange
from ..operator.node.dg.ai_ray_switch import AiRaySwitch
from ..operator.node.dg.ai_read_float import AiReadFloat
from ..operator.node.dg.ai_read_int import AiReadInt
from ..operator.node.dg.ai_read_rgb import AiReadRGB
from ..operator.node.dg.ai_read_rgba import AiReadRGBA
from ..operator.node.dg.ai_reciprocal import AiReciprocal
from ..operator.node.dg.ai_rgb_to_vector import AiRgbToVector
from ..operator.node.dg.ai_rgba_to_float import AiRgbaToFloat
from ..operator.node.dg.ai_round_corners import AiRoundCorners
from ..operator.node.dg.ai_set_parameter import AiSetParameter
from ..operator.node.dg.ai_set_transform import AiSetTransform
from ..operator.node.dg.ai_shadow_matte import AiShadowMatte
from ..operator.node.dg.ai_shuffle import AiShuffle
from ..operator.node.dg.ai_sign import AiSign
from ..operator.node.dg.ai_skin import AiSkin
from ..operator.node.dg.ai_sky import AiSky
from ..operator.node.dg.ai_space_transform import AiSpaceTransform
from ..operator.node.dg.ai_sqrt import AiSqrt
from ..operator.node.dg.ai_standard import AiStandard
from ..operator.node.dg.ai_standard_hair import AiStandardHair
from ..operator.node.dg.ai_standard_surface import AiStandardSurface
from ..operator.node.dg.ai_standard_volume import AiStandardVolume
from ..operator.node.dg.ai_state_float import AiStateFloat
from ..operator.node.dg.ai_state_int import AiStateInt
from ..operator.node.dg.ai_state_vector import AiStateVector
from ..operator.node.dg.ai_string_replace import AiStringReplace
from ..operator.node.dg.ai_subtract import AiSubtract
from ..operator.node.dg.ai_switch import AiSwitch
from ..operator.node.dg.ai_switch_operator import AiSwitchOperator
from ..operator.node.dg.ai_thin_film import AiThinFilm
from ..operator.node.dg.ai_toon import AiToon
from ..operator.node.dg.ai_trace_set import AiTraceSet
from ..operator.node.dg.ai_trigo import AiTrigo
from ..operator.node.dg.ai_triplanar import AiTriplanar
from ..operator.node.dg.ai_two_sided import AiTwoSided
from ..operator.node.dg.ai_user_data_bool import AiUserDataBool
from ..operator.node.dg.ai_user_data_color import AiUserDataColor
from ..operator.node.dg.ai_user_data_float import AiUserDataFloat
from ..operator.node.dg.ai_user_data_int import AiUserDataInt
from ..operator.node.dg.ai_user_data_string import AiUserDataString
from ..operator.node.dg.ai_user_data_vec2 import AiUserDataVec2
from ..operator.node.dg.ai_user_data_vector import AiUserDataVector
from ..operator.node.dg.ai_utility import AiUtility
from ..operator.node.dg.ai_uv_projection import AiUvProjection
from ..operator.node.dg.ai_uv_transform import AiUvTransform
from ..operator.node.dg.ai_vector_map import AiVectorMap
from ..operator.node.dg.ai_vector_to_rgb import AiVectorToRgb
from ..operator.node.dg.ai_volume_collector import AiVolumeCollector
from ..operator.node.dg.ai_volume_sample_float import AiVolumeSampleFloat
from ..operator.node.dg.ai_volume_sample_rgb import AiVolumeSampleRgb
from ..operator.node.dg.ai_wireframe import AiWireframe
from ..operator.node.dg.ai_write_color import AiWriteColor
from ..operator.node.dg.ai_write_float import AiWriteFloat
from ..operator.node.dg.ai_write_int import AiWriteInt
from ..operator.node.dg.ai_write_rgba import AiWriteRgba
from ..operator.node.dg.ai_write_vector import AiWriteVector
from ..operator.node.dg.aim_matrix import AimMatrix
from ..operator.node.dg.ais_env_facade import AISEnvFacade
from ..operator.node.dg.alembic_node import AlembicNode
from ..operator.node.dg.align_curve import AlignCurve
from ..operator.node.dg.align_surface import AlignSurface
from ..operator.node.dg.angle_between import AngleBetween
from ..operator.node.dg.anim_blend import AnimBlend
from ..operator.node.dg.anim_blend_in_out import AnimBlendInOut
from ..operator.node.dg.anim_blend_node_additive import AnimBlendNodeAdditive
from ..operator.node.dg.anim_blend_node_additive_da import AnimBlendNodeAdditiveDA
from ..operator.node.dg.anim_blend_node_additive_dl import AnimBlendNodeAdditiveDL
from ..operator.node.dg.anim_blend_node_additive_f import AnimBlendNodeAdditiveF
from ..operator.node.dg.anim_blend_node_additive_fa import AnimBlendNodeAdditiveFA
from ..operator.node.dg.anim_blend_node_additive_fl import AnimBlendNodeAdditiveFL
from ..operator.node.dg.anim_blend_node_additive_i16 import AnimBlendNodeAdditiveI16
from ..operator.node.dg.anim_blend_node_additive_i32 import AnimBlendNodeAdditiveI32
from ..operator.node.dg.anim_blend_node_additive_rotation import AnimBlendNodeAdditiveRotation
from ..operator.node.dg.anim_blend_node_additive_scale import AnimBlendNodeAdditiveScale
from ..operator.node.dg.anim_blend_node_boolean import AnimBlendNodeBoolean
from ..operator.node.dg.anim_blend_node_enum import AnimBlendNodeEnum
from ..operator.node.dg.anim_blend_node_time import AnimBlendNodeTime
from ..operator.node.dg.anim_clip import AnimClip
from ..operator.node.dg.anim_curve_ta import AnimCurveTA
from ..operator.node.dg.anim_curve_tl import AnimCurveTL
from ..operator.node.dg.anim_curve_tt import AnimCurveTT
from ..operator.node.dg.anim_curve_tu import AnimCurveTU
from ..operator.node.dg.anim_curve_ua import AnimCurveUA
from ..operator.node.dg.anim_curve_ul import AnimCurveUL
from ..operator.node.dg.anim_curve_ut import AnimCurveUT
from ..operator.node.dg.anim_curve_uu import AnimCurveUU
from ..operator.node.dg.anim_layer import AnimLayer
from ..operator.node.dg.anisotropic import Anisotropic
from ..operator.node.dg.aov_child_collection import AovChildCollection
from ..operator.node.dg.aov_collection import AovCollection
from ..operator.node.dg.apply_abs2_floats_override import ApplyAbs2FloatsOverride
from ..operator.node.dg.apply_abs3_floats_override import ApplyAbs3FloatsOverride
from ..operator.node.dg.apply_abs_bool_override import ApplyAbsBoolOverride
from ..operator.node.dg.apply_abs_enum_override import ApplyAbsEnumOverride
from ..operator.node.dg.apply_abs_float_override import ApplyAbsFloatOverride
from ..operator.node.dg.apply_abs_int_override import ApplyAbsIntOverride
from ..operator.node.dg.apply_abs_override import ApplyAbsOverride
from ..operator.node.dg.apply_abs_string_override import ApplyAbsStringOverride
from ..operator.node.dg.apply_connection_override import ApplyConnectionOverride
from ..operator.node.dg.apply_override import ApplyOverride
from ..operator.node.dg.apply_rel2_floats_override import ApplyRel2FloatsOverride
from ..operator.node.dg.apply_rel3_floats_override import ApplyRel3FloatsOverride
from ..operator.node.dg.apply_rel_float_override import ApplyRelFloatOverride
from ..operator.node.dg.apply_rel_int_override import ApplyRelIntOverride
from ..operator.node.dg.apply_rel_override import ApplyRelOverride
from ..operator.node.dg.arnold_aov_child_selector import ArnoldAOVChildSelector
from ..operator.node.dg.array_mapper import ArrayMapper
from ..operator.node.dg.aruba_tessellate import ArubaTessellate
from ..operator.node.dg.asin import Asin
from ..operator.node.dg.atan import Atan
from ..operator.node.dg.atan2 import Atan2
from ..operator.node.dg.attach_curve import AttachCurve
from ..operator.node.dg.attach_surface import AttachSurface
from ..operator.node.dg.attr_hierarchy_test import AttrHierarchyTest
from ..operator.node.dg.audio import Audio
from ..operator.node.dg.average import Average
from ..operator.node.dg.avg_curves import AvgCurves
from ..operator.node.dg.avg_nurbs_surface_points import AvgNurbsSurfacePoints
from ..operator.node.dg.avg_surface_points import AvgSurfacePoints
from ..operator.node.dg.axis_angle_to_quat import AxisAngleToQuat
from ..operator.node.dg.axis_from_matrix import AxisFromMatrix
from ..operator.node.dg.basic_selector import BasicSelector
from ..operator.node.dg.bevel import Bevel
from ..operator.node.dg.bevel_plus import BevelPlus
from ..operator.node.dg.bezier_curve_to_nurbs import BezierCurveToNurbs
from ..operator.node.dg.bifrost_board import BifrostBoard
from ..operator.node.dg.bifrost_geo_to_maya import BifrostGeoToMaya
from ..operator.node.dg.blend_color_sets import BlendColorSets
from ..operator.node.dg.blend_colors import BlendColors
from ..operator.node.dg.blend_device import BlendDevice
from ..operator.node.dg.blend_falloff import BlendFalloff
from ..operator.node.dg.blend_matrix import BlendMatrix
from ..operator.node.dg.blend_shape import BlendShape
from ..operator.node.dg.blend_two_attr import BlendTwoAttr
from ..operator.node.dg.blend_weighted import BlendWeighted
from ..operator.node.dg.blind_data_template import BlindDataTemplate
from ..operator.node.dg.blinn import Blinn
from ..operator.node.dg.bone_lattice import BoneLattice
from ..operator.node.dg.boolean import Boolean
from ..operator.node.dg.boundary import Boundary
from ..operator.node.dg.brownian import Brownian
from ..operator.node.dg.brush import Brush
from ..operator.node.dg.bulge import Bulge
from ..operator.node.dg.bump2d import Bump2d
from ..operator.node.dg.bump3d import Bump3d
from ..operator.node.dg.c_muscle_creator import CMuscleCreator
from ..operator.node.dg.c_muscle_multi_collide import CMuscleMultiCollide
from ..operator.node.dg.c_muscle_relative import CMuscleRelative
from ..operator.node.dg.c_muscle_shader import CMuscleShader
from ..operator.node.dg.c_muscle_smart_constraint import CMuscleSmartConstraint
from ..operator.node.dg.c_muscle_spline_deformer import CMuscleSplineDeformer
from ..operator.node.dg.c_muscle_stretch import CMuscleStretch
from ..operator.node.dg.c_muscle_system import CMuscleSystem
from ..operator.node.dg.cache_blend import CacheBlend
from ..operator.node.dg.cache_file import CacheFile
from ..operator.node.dg.camera_set import CameraSet
from ..operator.node.dg.camera_view import CameraView
from ..operator.node.dg.ceil import Ceil
from ..operator.node.dg.channels import Channels
from ..operator.node.dg.character import Character
from ..operator.node.dg.character_map import CharacterMap
from ..operator.node.dg.character_offset import CharacterOffset
from ..operator.node.dg.checker import Checker
from ..operator.node.dg.child_node import ChildNode
from ..operator.node.dg.choice import Choice
from ..operator.node.dg.chooser import Chooser
from ..operator.node.dg.clamp import Clamp
from ..operator.node.dg.clamp_range import ClampRange
from ..operator.node.dg.clip_library import ClipLibrary
from ..operator.node.dg.clip_scheduler import ClipScheduler
from ..operator.node.dg.clip_to_ghost_data import ClipToGhostData
from ..operator.node.dg.close_curve import CloseCurve
from ..operator.node.dg.close_surface import CloseSurface
from ..operator.node.dg.closest_point_on_mesh import ClosestPointOnMesh
from ..operator.node.dg.closest_point_on_surface import ClosestPointOnSurface
from ..operator.node.dg.cloth import Cloth
from ..operator.node.dg.cloud import Cloud
from ..operator.node.dg.cluster import Cluster
from ..operator.node.dg.collection import Collection
from ..operator.node.dg.color_composite import ColorComposite
from ..operator.node.dg.color_condition import ColorCondition
from ..operator.node.dg.color_constant import ColorConstant
from ..operator.node.dg.color_correct import ColorCorrect
from ..operator.node.dg.color_logic import ColorLogic
from ..operator.node.dg.color_management_globals import ColorManagementGlobals
from ..operator.node.dg.color_mask import ColorMask
from ..operator.node.dg.color_math import ColorMath
from ..operator.node.dg.color_profile import ColorProfile
from ..operator.node.dg.column_from_matrix import ColumnFromMatrix
from ..operator.node.dg.combination_shape import CombinationShape
from ..operator.node.dg.compact_plug_array_test import CompactPlugArrayTest
from ..operator.node.dg.component_falloff import ComponentFalloff
from ..operator.node.dg.component_match import ComponentMatch
from ..operator.node.dg.component_tag_base import ComponentTagBase
from ..operator.node.dg.compose_matrix import ComposeMatrix
from ..operator.node.dg.compute_global import ComputeGlobal
from ..operator.node.dg.compute_local import ComputeLocal
from ..operator.node.dg.condition import Condition
from ..operator.node.dg.connection_override import ConnectionOverride
from ..operator.node.dg.connection_unique_override import ConnectionUniqueOverride
from ..operator.node.dg.container import Container
from ..operator.node.dg.container_base import ContainerBase
from ..operator.node.dg.contrast import Contrast
from ..operator.node.dg.controller import Controller
from ..operator.node.dg.copy_color_set import CopyColorSet
from ..operator.node.dg.copy_uv_set import CopyUVSet
from ..operator.node.dg.cos import Cos
from ..operator.node.dg.cpv_color import CpvColor
from ..operator.node.dg.crater import Crater
from ..operator.node.dg.crease_set import CreaseSet
from ..operator.node.dg.create_color_set import CreateColorSet
from ..operator.node.dg.create_ptex_uv import CreatePtexUV
from ..operator.node.dg.create_uv_set import CreateUVSet
from ..operator.node.dg.cross_product import CrossProduct
from ..operator.node.dg.cryptomatte import Cryptomatte
from ..operator.node.dg.curve_from_mesh_co_m import CurveFromMeshCoM
from ..operator.node.dg.curve_from_mesh_edge import CurveFromMeshEdge
from ..operator.node.dg.curve_from_subdiv_edge import CurveFromSubdivEdge
from ..operator.node.dg.curve_from_subdiv_face import CurveFromSubdivFace
from ..operator.node.dg.curve_from_surface_bnd import CurveFromSurfaceBnd
from ..operator.node.dg.curve_from_surface_co_s import CurveFromSurfaceCoS
from ..operator.node.dg.curve_from_surface_iso import CurveFromSurfaceIso
from ..operator.node.dg.curve_info import CurveInfo
from ..operator.node.dg.curve_intersect import CurveIntersect
from ..operator.node.dg.curve_normalizer_angle import CurveNormalizerAngle
from ..operator.node.dg.curve_normalizer_linear import CurveNormalizerLinear
from ..operator.node.dg.curve_warp import CurveWarp
from ..operator.node.dg.custom_rig_default_mapping_node import CustomRigDefaultMappingNode
from ..operator.node.dg.custom_rig_retargeter_node import CustomRigRetargeterNode
from ..operator.node.dg.dag_pose import DagPose
from ..operator.node.dg.data_block_test import DataBlockTest
from ..operator.node.dg.decompose_matrix import DecomposeMatrix
from ..operator.node.dg.default_light_list import DefaultLightList
from ..operator.node.dg.default_render_utility_list import DefaultRenderUtilityList
from ..operator.node.dg.default_rendering_list import DefaultRenderingList
from ..operator.node.dg.default_shader_list import DefaultShaderList
from ..operator.node.dg.default_texture_list import DefaultTextureList
from ..operator.node.dg.delete_color_set import DeleteColorSet
from ..operator.node.dg.delete_component import DeleteComponent
from ..operator.node.dg.delete_uv_set import DeleteUVSet
from ..operator.node.dg.delta_mush import DeltaMush
from ..operator.node.dg.detach_curve import DetachCurve
from ..operator.node.dg.detach_surface import DetachSurface
from ..operator.node.dg.determinant import Determinant
from ..operator.node.dg.disk_cache import DiskCache
from ..operator.node.dg.displacement_shader import DisplacementShader
from ..operator.node.dg.display_layer import DisplayLayer
from ..operator.node.dg.display_layer_manager import DisplayLayerManager
from ..operator.node.dg.distance_between import DistanceBetween
from ..operator.node.dg.divide import Divide
from ..operator.node.dg.dof import Dof
from ..operator.node.dg.dot_product import DotProduct
from ..operator.node.dg.double_shading_switch import DoubleShadingSwitch
from ..operator.node.dg.dp_birail_srf import DpBirailSrf
from ..operator.node.dg.dyn_controller import DynController
from ..operator.node.dg.dyn_globals import DynGlobals
from ..operator.node.dg.edit_metadata import EditMetadata
from ..operator.node.dg.edits_manager import EditsManager
from ..operator.node.dg.env_ball import EnvBall
from ..operator.node.dg.env_chrome import EnvChrome
from ..operator.node.dg.env_cube import EnvCube
from ..operator.node.dg.env_facade import EnvFacade
from ..operator.node.dg.env_fog import EnvFog
from ..operator.node.dg.env_sky import EnvSky
from ..operator.node.dg.env_sphere import EnvSphere
from ..operator.node.dg.equal import Equal
from ..operator.node.dg.euler_to_quat import EulerToQuat
from ..operator.node.dg.explode_nurbs_shell import ExplodeNurbsShell
from ..operator.node.dg.expression import Expression
from ..operator.node.dg.extend_curve import ExtendCurve
from ..operator.node.dg.extend_surface import ExtendSurface
from ..operator.node.dg.extrude import Extrude
from ..operator.node.dg.facade import Facade
from ..operator.node.dg.falloff_eval import FalloffEval
from ..operator.node.dg.ff_blend_srf import FfBlendSrf
from ..operator.node.dg.ff_blend_srf_obsolete import FfBlendSrfObsolete
from ..operator.node.dg.ff_fillet_srf import FfFilletSrf
from ..operator.node.dg.ffd import Ffd
from ..operator.node.dg.file import File
from ..operator.node.dg.fillet_curve import FilletCurve
from ..operator.node.dg.fit_bspline import FitBspline
from ..operator.node.dg.float_composite import FloatComposite
from ..operator.node.dg.float_condition import FloatCondition
from ..operator.node.dg.float_constant import FloatConstant
from ..operator.node.dg.float_correct import FloatCorrect
from ..operator.node.dg.float_logic import FloatLogic
from ..operator.node.dg.float_mask import FloatMask
from ..operator.node.dg.float_math import FloatMath
from ..operator.node.dg.floor import Floor
from ..operator.node.dg.flow import Flow
from ..operator.node.dg.four_by_four_matrix import FourByFourMatrix
from ..operator.node.dg.fractal import Fractal
from ..operator.node.dg.frame_cache import FrameCache
from ..operator.node.dg.game_fbx_exporter import GameFbxExporter
from ..operator.node.dg.gamma_correct import GammaCorrect
from ..operator.node.dg.geo_connector import GeoConnector
from ..operator.node.dg.geom_bind import GeomBind
from ..operator.node.dg.geometry_filter import GeometryFilter
from ..operator.node.dg.global_cache_control import GlobalCacheControl
from ..operator.node.dg.global_stitch import GlobalStitch
from ..operator.node.dg.granite import Granite
from ..operator.node.dg.grease_pencil_sequence import GreasePencilSequence
from ..operator.node.dg.greater_than import GreaterThan
from ..operator.node.dg.grid import Grid
from ..operator.node.dg.group import Group
from ..operator.node.dg.group_id import GroupId
from ..operator.node.dg.group_parts import GroupParts
from ..operator.node.dg.guide import Guide
from ..operator.node.dg.hair_physical_shader import HairPhysicalShader
from ..operator.node.dg.hair_tube_shader import HairTubeShader
from ..operator.node.dg.harden_point import HardenPoint
from ..operator.node.dg.hardware_render_globals import HardwareRenderGlobals
from ..operator.node.dg.hardware_rendering_globals import HardwareRenderingGlobals
from ..operator.node.dg.hierarchy_test_node1 import HierarchyTestNode1
from ..operator.node.dg.hierarchy_test_node2 import HierarchyTestNode2
from ..operator.node.dg.hierarchy_test_node3 import HierarchyTestNode3
from ..operator.node.dg.hierarchy_test_node4 import HierarchyTestNode4
from ..operator.node.dg.hik_character_node import HIKCharacterNode
from ..operator.node.dg.hik_character_state_client import HIKCharacterStateClient
from ..operator.node.dg.hik_control_set_node import HIKControlSetNode
from ..operator.node.dg.hik_effector2_state import HIKEffector2State
from ..operator.node.dg.hik_effector_from_character import HIKEffectorFromCharacter
from ..operator.node.dg.hik_pinning2_state import HIKPinning2State
from ..operator.node.dg.hik_property2_state import HIKProperty2State
from ..operator.node.dg.hik_retargeter_node import HIKRetargeterNode
from ..operator.node.dg.hik_skeleton_generator_node import HIKSkeletonGeneratorNode
from ..operator.node.dg.hik_solver import HikSolver
from ..operator.node.dg.hik_solver_node import HIKSolverNode
from ..operator.node.dg.hik_state2_effector import HIKState2Effector
from ..operator.node.dg.hik_state2_fk import HIKState2FK
from ..operator.node.dg.hik_state2_global_sk import HIKState2GlobalSK
from ..operator.node.dg.hik_state2_sk import HIKState2SK
from ..operator.node.dg.hikfk2_state import HIKFK2State
from ..operator.node.dg.hiksk2_state import HIKSK2State
from ..operator.node.dg.history_switch import HistorySwitch
from ..operator.node.dg.hold_matrix import HoldMatrix
from ..operator.node.dg.hsv_to_rgb import HsvToRgb
from ..operator.node.dg.hw_reflection_map import HwReflectionMap
from ..operator.node.dg.hw_render_globals import HwRenderGlobals
from ..operator.node.dg.hyper_graph_info import HyperGraphInfo
from ..operator.node.dg.hyper_layout import HyperLayout
from ..operator.node.dg.hyper_view import HyperView
from ..operator.node.dg.ik2_bsolver import Ik2Bsolver
from ..operator.node.dg.ik_m_csolver import IkMCsolver
from ..operator.node.dg.ik_pa_solver import IkPASolver
from ..operator.node.dg.ik_r_psolver import IkRPsolver
from ..operator.node.dg.ik_s_csolver import IkSCsolver
from ..operator.node.dg.ik_spline_solver import IkSplineSolver
from ..operator.node.dg.ik_spring_solver import IkSpringSolver
from ..operator.node.dg.ik_system import IkSystem
from ..operator.node.dg.insert_knot_curve import InsertKnotCurve
from ..operator.node.dg.insert_knot_surface import InsertKnotSurface
from ..operator.node.dg.intersect_surface import IntersectSurface
from ..operator.node.dg.inverse_lerp import InverseLerp
from ..operator.node.dg.inverse_matrix import InverseMatrix
from ..operator.node.dg.jiggle import Jiggle
from ..operator.node.dg.joint_cluster import JointCluster
from ..operator.node.dg.joint_ffd import JointFfd
from ..operator.node.dg.joint_lattice import JointLattice
from ..operator.node.dg.keying_group import KeyingGroup
from ..operator.node.dg.lambert import Lambert
from ..operator.node.dg.layered_shader import LayeredShader
from ..operator.node.dg.layered_texture import LayeredTexture
from ..operator.node.dg.least_squares_modifier import LeastSquaresModifier
from ..operator.node.dg.leather import Leather
from ..operator.node.dg.length import Length
from ..operator.node.dg.lerp import Lerp
from ..operator.node.dg.less_than import LessThan
from ..operator.node.dg.light_editor import LightEditor
from ..operator.node.dg.light_fog import LightFog
from ..operator.node.dg.light_group import LightGroup
from ..operator.node.dg.light_info import LightInfo
from ..operator.node.dg.light_item import LightItem
from ..operator.node.dg.light_item_base import LightItemBase
from ..operator.node.dg.light_linker import LightLinker
from ..operator.node.dg.light_list import LightList
from ..operator.node.dg.lights_child_collection import LightsChildCollection
from ..operator.node.dg.lights_collection import LightsCollection
from ..operator.node.dg.lights_collection_selector import LightsCollectionSelector
from ..operator.node.dg.list_item import ListItem
from ..operator.node.dg.lod_thresholds import LodThresholds
from ..operator.node.dg.loft import Loft
from ..operator.node.dg.log import Log
from ..operator.node.dg.luminance import Luminance
from ..operator.node.dg.make_group import MakeGroup
from ..operator.node.dg.make_illustrator_curves import MakeIllustratorCurves
from ..operator.node.dg.make_nurb_circle import MakeNurbCircle
from ..operator.node.dg.make_nurb_cone import MakeNurbCone
from ..operator.node.dg.make_nurb_cube import MakeNurbCube
from ..operator.node.dg.make_nurb_cylinder import MakeNurbCylinder
from ..operator.node.dg.make_nurb_plane import MakeNurbPlane
from ..operator.node.dg.make_nurb_sphere import MakeNurbSphere
from ..operator.node.dg.make_nurb_torus import MakeNurbTorus
from ..operator.node.dg.make_nurbs_square import MakeNurbsSquare
from ..operator.node.dg.make_text_curves import MakeTextCurves
from ..operator.node.dg.make_three_point_circular_arc import MakeThreePointCircularArc
from ..operator.node.dg.make_two_point_circular_arc import MakeTwoPointCircularArc
from ..operator.node.dg.mandelbrot import Mandelbrot
from ..operator.node.dg.mandelbrot3_d import Mandelbrot3D
from ..operator.node.dg.marble import Marble
from ..operator.node.dg.mash_audio import MASH_Audio
from ..operator.node.dg.mash_base_node import MASH_BaseNode
from ..operator.node.dg.mash_blend import MASH_Blend
from ..operator.node.dg.mash_blend_deformer import MASH_BlendDeformer
from ..operator.node.dg.mash_breakout import MASH_Breakout
from ..operator.node.dg.mash_channel_random import MASH_ChannelRandom
from ..operator.node.dg.mash_color import MASH_Color
from ..operator.node.dg.mash_constraint import MASH_Constraint
from ..operator.node.dg.mash_curve import MASH_Curve
from ..operator.node.dg.mash_deformer import MASH_Deformer
from ..operator.node.dg.mash_delay import MASH_Delay
from ..operator.node.dg.mash_distribute import MASH_Distribute
from ..operator.node.dg.mash_dynamics import MASH_Dynamics
from ..operator.node.dg.mash_dynamics_initial_state import MASH_DynamicsInitialState
from ..operator.node.dg.mash_explode import MASH_Explode
from ..operator.node.dg.mash_id import MASH_Id
from ..operator.node.dg.mash_influence import MASH_Influence
from ..operator.node.dg.mash_inherit import MASH_Inherit
from ..operator.node.dg.mash_initial_state import MASH_InitialState
from ..operator.node.dg.mash_jiggle import MASH_Jiggle
from ..operator.node.dg.mash_legacy import MASH_Legacy
from ..operator.node.dg.mash_maths import MASH_Maths
from ..operator.node.dg.mash_multi_curve import MASH_MultiCurve
from ..operator.node.dg.mash_mute import MASH_Mute
from ..operator.node.dg.mash_noise import MASH_Noise
from ..operator.node.dg.mash_offset import MASH_Offset
from ..operator.node.dg.mash_orient import MASH_Orient
from ..operator.node.dg.mash_pfx_connect import MASH_PfxConnect
from ..operator.node.dg.mash_placer import MASH_Placer
from ..operator.node.dg.mash_point_to_curve import MASH_PointToCurve
from ..operator.node.dg.mash_python import MASH_Python
from ..operator.node.dg.mash_random import MASH_Random
from ..operator.node.dg.mash_replicator import MASH_Replicator
from ..operator.node.dg.mash_repro import MASH_Repro
from ..operator.node.dg.mash_shell_deformer import MASH_ShellDeformer
from ..operator.node.dg.mash_signal import MASH_Signal
from ..operator.node.dg.mash_spring import MASH_Spring
from ..operator.node.dg.mash_strength import MASH_Strength
from ..operator.node.dg.mash_symmetry import MASH_Symmetry
from ..operator.node.dg.mash_time import MASH_Time
from ..operator.node.dg.mash_trails import MASH_Trails
from ..operator.node.dg.mash_transform import MASH_Transform
from ..operator.node.dg.mash_trig import MASH_Trig
from ..operator.node.dg.mash_visibility import MASH_Visibility
from ..operator.node.dg.mash_waiter import MASH_Waiter
from ..operator.node.dg.mash_world import MASH_World
from ..operator.node.dg.material_facade import MaterialFacade
from ..operator.node.dg.material_info import MaterialInfo
from ..operator.node.dg.material_override import MaterialOverride
from ..operator.node.dg.material_template import MaterialTemplate
from ..operator.node.dg.material_template_override import MaterialTemplateOverride
from ..operator.node.dg.material_x_material import MaterialXMaterial
from ..operator.node.dg.material_x_surface_shader import MaterialXSurfaceShader
from ..operator.node.dg.max import Max
from ..operator.node.dg.maya_usd_geom_node import MayaUsdGeomNode
from ..operator.node.dg.maya_usd_layer_manager import MayaUsdLayerManager
from ..operator.node.dg.maya_usd_proxy_shape_listener import MayaUsdProxyShapeListener
from ..operator.node.dg.maya_usd_proxy_shape_listener_base import MayaUsdProxyShapeListenerBase
from ..operator.node.dg.membrane import Membrane
from ..operator.node.dg.min import Min
from ..operator.node.dg.modulo import Modulo
from ..operator.node.dg.morph import Morph
from ..operator.node.dg.motion_path import MotionPath
from ..operator.node.dg.motion_trail import MotionTrail
from ..operator.node.dg.mountain import Mountain
from ..operator.node.dg.movie import Movie
from ..operator.node.dg.mp_birail_srf import MpBirailSrf
from ..operator.node.dg.mult_double_linear import MultDoubleLinear
from ..operator.node.dg.mult_matrix import MultMatrix
from ..operator.node.dg.multilister_light import MultilisterLight
from ..operator.node.dg.multiply import Multiply
from ..operator.node.dg.multiply_divide import MultiplyDivide
from ..operator.node.dg.multiply_point_by_matrix import MultiplyPointByMatrix
from ..operator.node.dg.multiply_vector_by_matrix import MultiplyVectorByMatrix
from ..operator.node.dg.mute import Mute
from ..operator.node.dg.n_component import NComponent
from ..operator.node.dg.nearest_point_on_curve import NearestPointOnCurve
from ..operator.node.dg.negate import Negate
from ..operator.node.dg.network import Network
from ..operator.node.dg.node_graph_editor_bookmark_info import NodeGraphEditorBookmarkInfo
from ..operator.node.dg.node_graph_editor_bookmarks import NodeGraphEditorBookmarks
from ..operator.node.dg.noise import Noise
from ..operator.node.dg.non_linear import NonLinear
from ..operator.node.dg.normalize import Normalize
from ..operator.node.dg.nurbs_curve_to_bezier import NurbsCurveToBezier
from ..operator.node.dg.nurbs_tessellate import NurbsTessellate
from ..operator.node.dg.nurbs_to_subdiv import NurbsToSubdiv
from ..operator.node.dg.nurbs_to_subdiv_proc import NurbsToSubdivProc
from ..operator.node.dg.object_attr_filter import ObjectAttrFilter
from ..operator.node.dg.object_bin_filter import ObjectBinFilter
from ..operator.node.dg.object_filter import ObjectFilter
from ..operator.node.dg.object_grp_to_comp import ObjectGrpToComp
from ..operator.node.dg.object_multi_filter import ObjectMultiFilter
from ..operator.node.dg.object_name_filter import ObjectNameFilter
from ..operator.node.dg.object_render_filter import ObjectRenderFilter
from ..operator.node.dg.object_script_filter import ObjectScriptFilter
from ..operator.node.dg.object_set import ObjectSet
from ..operator.node.dg.object_type_filter import ObjectTypeFilter
from ..operator.node.dg.ocean import Ocean
from ..operator.node.dg.ocean_shader import OceanShader
from ..operator.node.dg.offset_cos import OffsetCos
from ..operator.node.dg.offset_curve import OffsetCurve
from ..operator.node.dg.offset_deformer import OffsetDeformer
from ..operator.node.dg.offset_surface import OffsetSurface
from ..operator.node.dg.old_blind_data_base import OldBlindDataBase
from ..operator.node.dg.old_geometry_constraint import OldGeometryConstraint
from ..operator.node.dg.optical_fx import OpticalFX
from ..operator.node.dg.override import Override
from ..operator.node.dg.pair_blend import PairBlend
from ..operator.node.dg.parent_matrix import ParentMatrix
from ..operator.node.dg.particle_age_mapper import ParticleAgeMapper
from ..operator.node.dg.particle_cloud import ParticleCloud
from ..operator.node.dg.particle_color_mapper import ParticleColorMapper
from ..operator.node.dg.particle_incand_mapper import ParticleIncandMapper
from ..operator.node.dg.particle_sampler_info import ParticleSamplerInfo
from ..operator.node.dg.particle_transp_mapper import ParticleTranspMapper
from ..operator.node.dg.partition import Partition
from ..operator.node.dg.pass_contribution_map import PassContributionMap
from ..operator.node.dg.pass_matrix import PassMatrix
from ..operator.node.dg.phong import Phong
from ..operator.node.dg.phong_e import PhongE
from ..operator.node.dg.pi import Pi
from ..operator.node.dg.pick_matrix import PickMatrix
from ..operator.node.dg.place2d_texture import Place2dTexture
from ..operator.node.dg.planar_trim_surface import PlanarTrimSurface
from ..operator.node.dg.plus_minus_average import PlusMinusAverage
from ..operator.node.dg.point_matrix_mult import PointMatrixMult
from ..operator.node.dg.point_on_curve_info import PointOnCurveInfo
from ..operator.node.dg.point_on_surface_info import PointOnSurfaceInfo
from ..operator.node.dg.poly_append import PolyAppend
from ..operator.node.dg.poly_append_vertex import PolyAppendVertex
from ..operator.node.dg.poly_auto_proj import PolyAutoProj
from ..operator.node.dg.poly_average_vertex import PolyAverageVertex
from ..operator.node.dg.poly_axis import PolyAxis
from ..operator.node.dg.poly_bevel import PolyBevel
from ..operator.node.dg.poly_bevel2 import PolyBevel2
from ..operator.node.dg.poly_bevel3 import PolyBevel3
from ..operator.node.dg.poly_bevel_cutback import PolyBevelCutback
from ..operator.node.dg.poly_blind_data import PolyBlindData
from ..operator.node.dg.poly_bool_op import PolyBoolOp
from ..operator.node.dg.poly_boolean import PolyBoolean
from ..operator.node.dg.poly_bridge_edge import PolyBridgeEdge
from ..operator.node.dg.poly_c_bool_op import PolyCBoolOp
from ..operator.node.dg.poly_chip_off import PolyChipOff
from ..operator.node.dg.poly_circularize import PolyCircularize
from ..operator.node.dg.poly_clean import PolyClean
from ..operator.node.dg.poly_close_border import PolyCloseBorder
from ..operator.node.dg.poly_collapse_edge import PolyCollapseEdge
from ..operator.node.dg.poly_collapse_f import PolyCollapseF
from ..operator.node.dg.poly_color_del import PolyColorDel
from ..operator.node.dg.poly_color_mod import PolyColorMod
from ..operator.node.dg.poly_color_per_vertex import PolyColorPerVertex
from ..operator.node.dg.poly_cone import PolyCone
from ..operator.node.dg.poly_connect_components import PolyConnectComponents
from ..operator.node.dg.poly_contour_proj import PolyContourProj
from ..operator.node.dg.poly_copy_uv import PolyCopyUV
from ..operator.node.dg.poly_crease import PolyCrease
from ..operator.node.dg.poly_crease_edge import PolyCreaseEdge
from ..operator.node.dg.poly_create_face import PolyCreateFace
from ..operator.node.dg.poly_cube import PolyCube
from ..operator.node.dg.poly_cut import PolyCut
from ..operator.node.dg.poly_cyl_proj import PolyCylProj
from ..operator.node.dg.poly_cylinder import PolyCylinder
from ..operator.node.dg.poly_del_edge import PolyDelEdge
from ..operator.node.dg.poly_del_facet import PolyDelFacet
from ..operator.node.dg.poly_del_vertex import PolyDelVertex
from ..operator.node.dg.poly_disc import PolyDisc
from ..operator.node.dg.poly_duplicate_edge import PolyDuplicateEdge
from ..operator.node.dg.poly_edge_to_curve import PolyEdgeToCurve
from ..operator.node.dg.poly_edit_edge_flow import PolyEditEdgeFlow
from ..operator.node.dg.poly_extrude_edge import PolyExtrudeEdge
from ..operator.node.dg.poly_extrude_face import PolyExtrudeFace
from ..operator.node.dg.poly_extrude_vertex import PolyExtrudeVertex
from ..operator.node.dg.poly_flip_edge import PolyFlipEdge
from ..operator.node.dg.poly_flip_uv import PolyFlipUV
from ..operator.node.dg.poly_gear import PolyGear
from ..operator.node.dg.poly_helix import PolyHelix
from ..operator.node.dg.poly_hole_face import PolyHoleFace
from ..operator.node.dg.poly_layout_uv import PolyLayoutUV
from ..operator.node.dg.poly_map_cut import PolyMapCut
from ..operator.node.dg.poly_map_del import PolyMapDel
from ..operator.node.dg.poly_map_sew import PolyMapSew
from ..operator.node.dg.poly_map_sew_move import PolyMapSewMove
from ..operator.node.dg.poly_merge_edge import PolyMergeEdge
from ..operator.node.dg.poly_merge_face import PolyMergeFace
from ..operator.node.dg.poly_merge_uv import PolyMergeUV
from ..operator.node.dg.poly_merge_vert import PolyMergeVert
from ..operator.node.dg.poly_mirror import PolyMirror
from ..operator.node.dg.poly_move_edge import PolyMoveEdge
from ..operator.node.dg.poly_move_face import PolyMoveFace
from ..operator.node.dg.poly_move_facet_uv import PolyMoveFacetUV
from ..operator.node.dg.poly_move_uv import PolyMoveUV
from ..operator.node.dg.poly_move_vertex import PolyMoveVertex
from ..operator.node.dg.poly_normal import PolyNormal
from ..operator.node.dg.poly_normal_per_vertex import PolyNormalPerVertex
from ..operator.node.dg.poly_normalize_uv import PolyNormalizeUV
from ..operator.node.dg.poly_opt_uvs import PolyOptUvs
from ..operator.node.dg.poly_pass_thru import PolyPassThru
from ..operator.node.dg.poly_pin_uv import PolyPinUV
from ..operator.node.dg.poly_pipe import PolyPipe
from ..operator.node.dg.poly_planar_proj import PolyPlanarProj
from ..operator.node.dg.poly_plane import PolyPlane
from ..operator.node.dg.poly_platonic import PolyPlatonic
from ..operator.node.dg.poly_platonic_solid import PolyPlatonicSolid
from ..operator.node.dg.poly_poke import PolyPoke
from ..operator.node.dg.poly_primitive_misc import PolyPrimitiveMisc
from ..operator.node.dg.poly_prism import PolyPrism
from ..operator.node.dg.poly_proj import PolyProj
from ..operator.node.dg.poly_project_curve import PolyProjectCurve
from ..operator.node.dg.poly_pyramid import PolyPyramid
from ..operator.node.dg.poly_quad import PolyQuad
from ..operator.node.dg.poly_reduce import PolyReduce
from ..operator.node.dg.poly_remesh import PolyRemesh
from ..operator.node.dg.poly_retopo import PolyRetopo
from ..operator.node.dg.poly_separate import PolySeparate
from ..operator.node.dg.poly_sew_edge import PolySewEdge
from ..operator.node.dg.poly_smart_extrude import PolySmartExtrude
from ..operator.node.dg.poly_smooth import PolySmooth
from ..operator.node.dg.poly_smooth_face import PolySmoothFace
from ..operator.node.dg.poly_smooth_proxy import PolySmoothProxy
from ..operator.node.dg.poly_soft_edge import PolySoftEdge
from ..operator.node.dg.poly_sph_proj import PolySphProj
from ..operator.node.dg.poly_sphere import PolySphere
from ..operator.node.dg.poly_spin_edge import PolySpinEdge
from ..operator.node.dg.poly_split import PolySplit
from ..operator.node.dg.poly_split_edge import PolySplitEdge
from ..operator.node.dg.poly_split_ring import PolySplitRing
from ..operator.node.dg.poly_split_vert import PolySplitVert
from ..operator.node.dg.poly_straighten_uv_border import PolyStraightenUVBorder
from ..operator.node.dg.poly_subd_edge import PolySubdEdge
from ..operator.node.dg.poly_subd_face import PolySubdFace
from ..operator.node.dg.poly_super_shape import PolySuperShape
from ..operator.node.dg.poly_to_subdiv import PolyToSubdiv
from ..operator.node.dg.poly_torus import PolyTorus
from ..operator.node.dg.poly_transfer import PolyTransfer
from ..operator.node.dg.poly_triangulate import PolyTriangulate
from ..operator.node.dg.poly_tweak import PolyTweak
from ..operator.node.dg.poly_tweak_uv import PolyTweakUV
from ..operator.node.dg.poly_unite import PolyUnite
from ..operator.node.dg.poly_unsmooth import PolyUnsmooth
from ..operator.node.dg.poly_uv_rectangle import PolyUVRectangle
from ..operator.node.dg.poly_wedge_face import PolyWedgeFace
from ..operator.node.dg.pose_interpolator_manager import PoseInterpolatorManager
from ..operator.node.dg.post_process_list import PostProcessList
from ..operator.node.dg.power import Power
from ..operator.node.dg.precomp_export import PrecompExport
from ..operator.node.dg.premultiply import Premultiply
from ..operator.node.dg.project_curve import ProjectCurve
from ..operator.node.dg.project_tangent import ProjectTangent
from ..operator.node.dg.projection import Projection
from ..operator.node.dg.proximity_falloff import ProximityFalloff
from ..operator.node.dg.proximity_pin import ProximityPin
from ..operator.node.dg.proximity_wrap import ProximityWrap
from ..operator.node.dg.proxy_manager import ProxyManager
from ..operator.node.dg.psd_file_tex import PsdFileTex
from ..operator.node.dg.pxr_usd_point_based_deformer_node import PxrUsdPointBasedDeformerNode
from ..operator.node.dg.pxr_usd_stage_node import PxrUsdStageNode
from ..operator.node.dg.quad_shading_switch import QuadShadingSwitch
from ..operator.node.dg.quat_add import QuatAdd
from ..operator.node.dg.quat_conjugate import QuatConjugate
from ..operator.node.dg.quat_invert import QuatInvert
from ..operator.node.dg.quat_negate import QuatNegate
from ..operator.node.dg.quat_normalize import QuatNormalize
from ..operator.node.dg.quat_prod import QuatProd
from ..operator.node.dg.quat_slerp import QuatSlerp
from ..operator.node.dg.quat_sub import QuatSub
from ..operator.node.dg.quat_to_axis_angle import QuatToAxisAngle
from ..operator.node.dg.quat_to_euler import QuatToEuler
from ..operator.node.dg.r_scontainer import RScontainer
from ..operator.node.dg.ramp import Ramp
from ..operator.node.dg.ramp_shader import RampShader
from ..operator.node.dg.rbf_srf import RbfSrf
from ..operator.node.dg.rebuild_curve import RebuildCurve
from ..operator.node.dg.rebuild_surface import RebuildSurface
from ..operator.node.dg.record import Record
from ..operator.node.dg.reference import Reference
from ..operator.node.dg.rel_override import RelOverride
from ..operator.node.dg.rel_unique_override import RelUniqueOverride
from ..operator.node.dg.remap_color import RemapColor
from ..operator.node.dg.remap_hsv import RemapHsv
from ..operator.node.dg.remap_value import RemapValue
from ..operator.node.dg.render_globals import RenderGlobals
from ..operator.node.dg.render_globals_list import RenderGlobalsList
from ..operator.node.dg.render_layer import RenderLayer
from ..operator.node.dg.render_layer_manager import RenderLayerManager
from ..operator.node.dg.render_pass import RenderPass
from ..operator.node.dg.render_pass_set import RenderPassSet
from ..operator.node.dg.render_quality import RenderQuality
from ..operator.node.dg.render_settings_child_collection import RenderSettingsChildCollection
from ..operator.node.dg.render_settings_collection import RenderSettingsCollection
from ..operator.node.dg.render_setup import RenderSetup
from ..operator.node.dg.render_setup_layer import RenderSetupLayer
from ..operator.node.dg.render_target import RenderTarget
from ..operator.node.dg.rendered_image_source import RenderedImageSource
from ..operator.node.dg.reorder_uv_set import ReorderUVSet
from ..operator.node.dg.resolution import Resolution
from ..operator.node.dg.result_curve_time_to_angular import ResultCurveTimeToAngular
from ..operator.node.dg.result_curve_time_to_linear import ResultCurveTimeToLinear
from ..operator.node.dg.result_curve_time_to_time import ResultCurveTimeToTime
from ..operator.node.dg.result_curve_time_to_unitless import ResultCurveTimeToUnitless
from ..operator.node.dg.reverse import Reverse
from ..operator.node.dg.reverse_curve import ReverseCurve
from ..operator.node.dg.reverse_surface import ReverseSurface
from ..operator.node.dg.revolve import Revolve
from ..operator.node.dg.rgb_to_hsv import RgbToHsv
from ..operator.node.dg.rigid_solver import RigidSolver
from ..operator.node.dg.rock import Rock
from ..operator.node.dg.rotate_helper import RotateHelper
from ..operator.node.dg.rotate_vector import RotateVector
from ..operator.node.dg.rotation_from_matrix import RotationFromMatrix
from ..operator.node.dg.round import Round
from ..operator.node.dg.round_constant_radius import RoundConstantRadius
from ..operator.node.dg.row_from_matrix import RowFromMatrix
from ..operator.node.dg.sampler import Sampler
from ..operator.node.dg.sampler_info import SamplerInfo
from ..operator.node.dg.scale_from_matrix import ScaleFromMatrix
from ..operator.node.dg.script import Script
from ..operator.node.dg.sculpt import Sculpt
from ..operator.node.dg.selection_list_operator import SelectionListOperator
from ..operator.node.dg.selector import Selector
from ..operator.node.dg.sequence_manager import SequenceManager
from ..operator.node.dg.sequencer import Sequencer
from ..operator.node.dg.set_range import SetRange
from ..operator.node.dg.shader_glow import ShaderGlow
from ..operator.node.dg.shader_override import ShaderOverride
from ..operator.node.dg.shading_engine import ShadingEngine
from ..operator.node.dg.shading_map import ShadingMap
from ..operator.node.dg.shape_editor_manager import ShapeEditorManager
from ..operator.node.dg.shell_deformer import ShellDeformer
from ..operator.node.dg.shell_tessellate import ShellTessellate
from ..operator.node.dg.shot import Shot
from ..operator.node.dg.shrink_wrap import ShrinkWrap
from ..operator.node.dg.simple_selector import SimpleSelector
from ..operator.node.dg.simple_test_node import SimpleTestNode
from ..operator.node.dg.simple_volume_shader import SimpleVolumeShader
from ..operator.node.dg.simplex_noise import SimplexNoise
from ..operator.node.dg.sin import Sin
from ..operator.node.dg.single_shading_switch import SingleShadingSwitch
from ..operator.node.dg.skin_binding import SkinBinding
from ..operator.node.dg.skin_cluster import SkinCluster
from ..operator.node.dg.smooth_curve import SmoothCurve
from ..operator.node.dg.smooth_step import SmoothStep
from ..operator.node.dg.smooth_tangent_srf import SmoothTangentSrf
from ..operator.node.dg.snapshot import Snapshot
from ..operator.node.dg.snow import Snow
from ..operator.node.dg.soft_mod import SoftMod
from ..operator.node.dg.solid_fractal import SolidFractal
from ..operator.node.dg.solidify import Solidify
from ..operator.node.dg.sp_birail_srf import SpBirailSrf
from ..operator.node.dg.square_srf import SquareSrf
from ..operator.node.dg.standard_surface import StandardSurface
from ..operator.node.dg.stencil import Stencil
from ..operator.node.dg.stitch_as_nurbs_shell import StitchAsNurbsShell
from ..operator.node.dg.stitch_srf import StitchSrf
from ..operator.node.dg.stroke_globals import StrokeGlobals
from ..operator.node.dg.stucco import Stucco
from ..operator.node.dg.style_curve import StyleCurve
from ..operator.node.dg.sub_curve import SubCurve
from ..operator.node.dg.sub_surface import SubSurface
from ..operator.node.dg.subd_add_topology import SubdAddTopology
from ..operator.node.dg.subd_auto_proj import SubdAutoProj
from ..operator.node.dg.subd_blind_data import SubdBlindData
from ..operator.node.dg.subd_clean_topology import SubdCleanTopology
from ..operator.node.dg.subd_hier_blind import SubdHierBlind
from ..operator.node.dg.subd_layout_uv import SubdLayoutUV
from ..operator.node.dg.subd_map_cut import SubdMapCut
from ..operator.node.dg.subd_map_sew_move import SubdMapSewMove
from ..operator.node.dg.subd_planar_proj import SubdPlanarProj
from ..operator.node.dg.subd_tweak import SubdTweak
from ..operator.node.dg.subd_tweak_uv import SubdTweakUV
from ..operator.node.dg.subdiv_collapse import SubdivCollapse
from ..operator.node.dg.subdiv_component_id import SubdivComponentId
from ..operator.node.dg.subdiv_reverse_faces import SubdivReverseFaces
from ..operator.node.dg.subdiv_to_nurbs import SubdivToNurbs
from ..operator.node.dg.subdiv_to_poly import SubdivToPoly
from ..operator.node.dg.subset_falloff import SubsetFalloff
from ..operator.node.dg.subtract import Subtract
from ..operator.node.dg.sum import Sum
from ..operator.node.dg.surface_info import SurfaceInfo
from ..operator.node.dg.surface_luminance import SurfaceLuminance
from ..operator.node.dg.surface_shader import SurfaceShader
from ..operator.node.dg.svg_to_poly import SvgToPoly
from ..operator.node.dg.sweep_mesh_creator import SweepMeshCreator
from ..operator.node.dg.sweep_profile_converter import SweepProfileConverter
from ..operator.node.dg.tan import Tan
from ..operator.node.dg.tension import Tension
from ..operator.node.dg.tex_lattice import TexLattice
from ..operator.node.dg.texture_bake_set import TextureBakeSet
from ..operator.node.dg.texture_deformer import TextureDeformer
from ..operator.node.dg.texture_to_geom import TextureToGeom
from ..operator.node.dg.time import Time
from ..operator.node.dg.time_editor import TimeEditor
from ..operator.node.dg.time_editor_anim_source import TimeEditorAnimSource
from ..operator.node.dg.time_editor_clip import TimeEditorClip
from ..operator.node.dg.time_editor_clip_base import TimeEditorClipBase
from ..operator.node.dg.time_editor_clip_evaluator import TimeEditorClipEvaluator
from ..operator.node.dg.time_editor_interpolator import TimeEditorInterpolator
from ..operator.node.dg.time_editor_tracks import TimeEditorTracks
from ..operator.node.dg.time_function import TimeFunction
from ..operator.node.dg.time_to_unit_conversion import TimeToUnitConversion
from ..operator.node.dg.time_warp import TimeWarp
from ..operator.node.dg.toon_line_attributes import ToonLineAttributes
from ..operator.node.dg.track_info_manager import TrackInfoManager
from ..operator.node.dg.transfer_attributes import TransferAttributes
from ..operator.node.dg.transfer_falloff import TransferFalloff
from ..operator.node.dg.transform_geometry import TransformGeometry
from ..operator.node.dg.translation_from_matrix import TranslationFromMatrix
from ..operator.node.dg.transpose_matrix import TransposeMatrix
from ..operator.node.dg.trim import Trim
from ..operator.node.dg.trim_with_boundaries import TrimWithBoundaries
from ..operator.node.dg.triple_shading_switch import TripleShadingSwitch
from ..operator.node.dg.truncate import Truncate
from ..operator.node.dg.tweak import Tweak
from ..operator.node.dg.type import Type
from ..operator.node.dg.type_extrude import TypeExtrude
from ..operator.node.dg.unfold3_d_optimize import Unfold3DOptimize
from ..operator.node.dg.unfold3_d_unfold import Unfold3DUnfold
from ..operator.node.dg.uniform_falloff import UniformFalloff
from ..operator.node.dg.unit_conversion import UnitConversion
from ..operator.node.dg.unit_to_time_conversion import UnitToTimeConversion
from ..operator.node.dg.unknown import Unknown
from ..operator.node.dg.unpremultiply import Unpremultiply
from ..operator.node.dg.untrim import Untrim
from ..operator.node.dg.usd_preview_surface import UsdPreviewSurface
from ..operator.node.dg.use_background import UseBackground
from ..operator.node.dg.uv_chooser import UvChooser
from ..operator.node.dg.uv_pin import UvPin
from ..operator.node.dg.value_override import ValueOverride
from ..operator.node.dg.vector_adjust import VectorAdjust
from ..operator.node.dg.vector_extrude import VectorExtrude
from ..operator.node.dg.vector_product import VectorProduct
from ..operator.node.dg.vertex_bake_set import VertexBakeSet
from ..operator.node.dg.view_color_manager import ViewColorManager
from ..operator.node.dg.volume_fog import VolumeFog
from ..operator.node.dg.volume_noise import VolumeNoise
from ..operator.node.dg.volume_shader import VolumeShader
from ..operator.node.dg.water import Water
from ..operator.node.dg.weight_geometry_filter import WeightGeometryFilter
from ..operator.node.dg.wire import Wire
from ..operator.node.dg.wood import Wood
from ..operator.node.dg.wrap import Wrap
from ..operator.node.dg.wt_add_matrix import WtAddMatrix
from ..operator.node.dg.xgm_curve_to_spline import XgmCurveToSpline
from ..operator.node.dg.xgm_hair_mapping import XgmHairMapping
from ..operator.node.dg.xgm_make_guide import XgmMakeGuide
from ..operator.node.dg.xgm_modifier_base import XgmModifierBase
from ..operator.node.dg.xgm_modifier_clump import XgmModifierClump
from ..operator.node.dg.xgm_modifier_collision import XgmModifierCollision
from ..operator.node.dg.xgm_modifier_cut import XgmModifierCut
from ..operator.node.dg.xgm_modifier_displacement import XgmModifierDisplacement
from ..operator.node.dg.xgm_modifier_guide import XgmModifierGuide
from ..operator.node.dg.xgm_modifier_linear_wire import XgmModifierLinearWire
from ..operator.node.dg.xgm_modifier_noise import XgmModifierNoise
from ..operator.node.dg.xgm_modifier_scale import XgmModifierScale
from ..operator.node.dg.xgm_modifier_sculpt import XgmModifierSculpt
from ..operator.node.dg.xgm_se_expr import XgmSeExpr
from ..operator.node.dg.xgm_spline_base import XgmSplineBase
from ..operator.node.dg.xgm_spline_cache import XgmSplineCache


class NodeCreater:
    def __init__(self, modifier_manager: ModifierManager | None = None) -> None: ...

    @property
    def modifier_manager(self) -> ModifierManager: ...

    def create(
        self,
        node_name: str,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NodeOperator: ...

    def node_class(self, node_name: str) -> type[NodeOperator]: ...

    def available_node_names(self) -> tuple[str, ...]: ...

    def __getattr__(self, node_name: str) -> Callable[..., NodeOperator]: ...

    def about_to_set_value_test_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AboutToSetValueTestNode: ...

    def abs_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AbsOverride: ...

    def abs_unique_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AbsUniqueOverride: ...

    def absolute(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Absolute: ...

    def acos(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Acos: ...

    def add_double_linear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AddDoubleLinear: ...

    def add_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AddMatrix: ...

    def adsk_material(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AdskMaterial: ...

    def adsk_prepare_render_globals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AdskPrepareRenderGlobals: ...

    def ai_abs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiAbs: ...

    def ai_add(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiAdd: ...

    def ai_ambient_occlusion(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiAmbientOcclusion: ...

    def ai_aov(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiAOV: ...

    def ai_aov_driver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiAOVDriver: ...

    def ai_aov_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiAOVFilter: ...

    def ai_atan(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiAtan: ...

    def ai_atmosphere_volume(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiAtmosphereVolume: ...

    def ai_axf_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiAxfShader: ...

    def ai_barndoor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiBarndoor: ...

    def ai_blackbody(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiBlackbody: ...

    def ai_bump2d(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiBump2d: ...

    def ai_bump3d(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiBump3d: ...

    def ai_cache(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiCache: ...

    def ai_camera_projection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiCameraProjection: ...

    def ai_car_paint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiCarPaint: ...

    def ai_cell_noise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiCellNoise: ...

    def ai_checkerboard(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiCheckerboard: ...

    def ai_clamp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiClamp: ...

    def ai_clip_geo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiClipGeo: ...

    def ai_collection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiCollection: ...

    def ai_color_convert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiColorConvert: ...

    def ai_color_correct(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiColorCorrect: ...

    def ai_color_jitter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiColorJitter: ...

    def ai_color_to_float(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiColorToFloat: ...

    def ai_compare(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiCompare: ...

    def ai_complement(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiComplement: ...

    def ai_complex_ior(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiComplexIor: ...

    def ai_composite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiComposite: ...

    def ai_cross(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiCross: ...

    def ai_curvature(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiCurvature: ...

    def ai_disable(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiDisable: ...

    def ai_distance(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiDistance: ...

    def ai_divide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiDivide: ...

    def ai_dot(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiDot: ...

    def ai_exp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiExp: ...

    def ai_facing_ratio(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiFacingRatio: ...

    def ai_flakes(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiFlakes: ...

    def ai_flat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiFlat: ...

    def ai_float_to_int(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiFloatToInt: ...

    def ai_float_to_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiFloatToMatrix: ...

    def ai_float_to_rgba(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiFloatToRgba: ...

    def ai_fog(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiFog: ...

    def ai_fraction(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiFraction: ...

    def ai_gobo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiGobo: ...

    def ai_hair(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiHair: ...

    def ai_image(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImage: ...

    def ai_imager_color_correct(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerColorCorrect: ...

    def ai_imager_color_curves(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerColorCurves: ...

    def ai_imager_denoiser_noice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerDenoiserNoice: ...

    def ai_imager_denoiser_oidn(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerDenoiserOidn: ...

    def ai_imager_denoiser_optix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerDenoiserOptix: ...

    def ai_imager_exposure(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerExposure: ...

    def ai_imager_lens_effects(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerLensEffects: ...

    def ai_imager_light_mixer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerLightMixer: ...

    def ai_imager_overlay(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerOverlay: ...

    def ai_imager_tonemap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerTonemap: ...

    def ai_imager_white_balance(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiImagerWhiteBalance: ...

    def ai_include_graph(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiIncludeGraph: ...

    def ai_is_finite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiIsFinite: ...

    def ai_lambert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiLambert: ...

    def ai_layer_float(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiLayerFloat: ...

    def ai_layer_rgba(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiLayerRgba: ...

    def ai_layer_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiLayerShader: ...

    def ai_length(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiLength: ...

    def ai_light_decay(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiLightDecay: ...

    def ai_log(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiLog: ...

    def ai_look_switch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiLookSwitch: ...

    def ai_material_x_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMaterialXShader: ...

    def ai_materialx(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMaterialx: ...

    def ai_matrix_interpolate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMatrixInterpolate: ...

    def ai_matrix_multiply_vector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMatrixMultiplyVector: ...

    def ai_matrix_transform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMatrixTransform: ...

    def ai_matte(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMatte: ...

    def ai_max(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMax: ...

    def ai_merge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMerge: ...

    def ai_min(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMin: ...

    def ai_mix_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMixShader: ...

    def ai_modulo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiModulo: ...

    def ai_motion_vector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMotionVector: ...

    def ai_multiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiMultiply: ...

    def ai_negate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiNegate: ...

    def ai_noise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiNoise: ...

    def ai_normal_map(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiNormalMap: ...

    def ai_normalize(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiNormalize: ...

    def ai_options(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiOptions: ...

    def ai_osl_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiOslShader: ...

    def ai_passthrough(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiPassthrough: ...

    def ai_physical_sky(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiPhysicalSky: ...

    def ai_pow(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiPow: ...

    def ai_ramp_float(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiRampFloat: ...

    def ai_ramp_rgb(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiRampRgb: ...

    def ai_random(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiRandom: ...

    def ai_range(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiRange: ...

    def ai_ray_switch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiRaySwitch: ...

    def ai_read_float(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiReadFloat: ...

    def ai_read_int(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiReadInt: ...

    def ai_read_rgb(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiReadRGB: ...

    def ai_read_rgba(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiReadRGBA: ...

    def ai_reciprocal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiReciprocal: ...

    def ai_rgb_to_vector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiRgbToVector: ...

    def ai_rgba_to_float(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiRgbaToFloat: ...

    def ai_round_corners(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiRoundCorners: ...

    def ai_set_parameter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiSetParameter: ...

    def ai_set_transform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiSetTransform: ...

    def ai_shadow_matte(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiShadowMatte: ...

    def ai_shuffle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiShuffle: ...

    def ai_sign(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiSign: ...

    def ai_skin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiSkin: ...

    def ai_sky(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiSky: ...

    def ai_space_transform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiSpaceTransform: ...

    def ai_sqrt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiSqrt: ...

    def ai_standard(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiStandard: ...

    def ai_standard_hair(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiStandardHair: ...

    def ai_standard_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiStandardSurface: ...

    def ai_standard_volume(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiStandardVolume: ...

    def ai_state_float(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiStateFloat: ...

    def ai_state_int(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiStateInt: ...

    def ai_state_vector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiStateVector: ...

    def ai_string_replace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiStringReplace: ...

    def ai_subtract(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiSubtract: ...

    def ai_switch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiSwitch: ...

    def ai_switch_operator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiSwitchOperator: ...

    def ai_thin_film(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiThinFilm: ...

    def ai_toon(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiToon: ...

    def ai_trace_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiTraceSet: ...

    def ai_trigo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiTrigo: ...

    def ai_triplanar(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiTriplanar: ...

    def ai_two_sided(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiTwoSided: ...

    def ai_user_data_bool(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiUserDataBool: ...

    def ai_user_data_color(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiUserDataColor: ...

    def ai_user_data_float(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiUserDataFloat: ...

    def ai_user_data_int(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiUserDataInt: ...

    def ai_user_data_string(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiUserDataString: ...

    def ai_user_data_vec2(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiUserDataVec2: ...

    def ai_user_data_vector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiUserDataVector: ...

    def ai_utility(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiUtility: ...

    def ai_uv_projection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiUvProjection: ...

    def ai_uv_transform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiUvTransform: ...

    def ai_vector_map(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiVectorMap: ...

    def ai_vector_to_rgb(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiVectorToRgb: ...

    def ai_volume_collector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiVolumeCollector: ...

    def ai_volume_sample_float(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiVolumeSampleFloat: ...

    def ai_volume_sample_rgb(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiVolumeSampleRgb: ...

    def ai_wireframe(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiWireframe: ...

    def ai_write_color(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiWriteColor: ...

    def ai_write_float(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiWriteFloat: ...

    def ai_write_int(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiWriteInt: ...

    def ai_write_rgba(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiWriteRgba: ...

    def ai_write_vector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AiWriteVector: ...

    def aim_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AimMatrix: ...

    def ais_env_facade(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AISEnvFacade: ...

    def alembic_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AlembicNode: ...

    def align_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AlignCurve: ...

    def align_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AlignSurface: ...

    def and_(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NodeOperator: ...

    def angle_between(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AngleBetween: ...

    def anim_blend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlend: ...

    def anim_blend_in_out(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendInOut: ...

    def anim_blend_node_additive(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeAdditive: ...

    def anim_blend_node_additive_da(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeAdditiveDA: ...

    def anim_blend_node_additive_dl(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeAdditiveDL: ...

    def anim_blend_node_additive_f(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeAdditiveF: ...

    def anim_blend_node_additive_fa(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeAdditiveFA: ...

    def anim_blend_node_additive_fl(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeAdditiveFL: ...

    def anim_blend_node_additive_i16(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeAdditiveI16: ...

    def anim_blend_node_additive_i32(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeAdditiveI32: ...

    def anim_blend_node_additive_rotation(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeAdditiveRotation: ...

    def anim_blend_node_additive_scale(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeAdditiveScale: ...

    def anim_blend_node_boolean(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeBoolean: ...

    def anim_blend_node_enum(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeEnum: ...

    def anim_blend_node_time(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimBlendNodeTime: ...

    def anim_clip(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimClip: ...

    def anim_curve_ta(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimCurveTA: ...

    def anim_curve_tl(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimCurveTL: ...

    def anim_curve_tt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimCurveTT: ...

    def anim_curve_tu(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimCurveTU: ...

    def anim_curve_ua(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimCurveUA: ...

    def anim_curve_ul(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimCurveUL: ...

    def anim_curve_ut(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimCurveUT: ...

    def anim_curve_uu(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimCurveUU: ...

    def anim_layer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AnimLayer: ...

    def anisotropic(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Anisotropic: ...

    def aov_child_collection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AovChildCollection: ...

    def aov_collection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AovCollection: ...

    def apply_abs2_floats_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyAbs2FloatsOverride: ...

    def apply_abs3_floats_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyAbs3FloatsOverride: ...

    def apply_abs_bool_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyAbsBoolOverride: ...

    def apply_abs_enum_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyAbsEnumOverride: ...

    def apply_abs_float_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyAbsFloatOverride: ...

    def apply_abs_int_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyAbsIntOverride: ...

    def apply_abs_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyAbsOverride: ...

    def apply_abs_string_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyAbsStringOverride: ...

    def apply_connection_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyConnectionOverride: ...

    def apply_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyOverride: ...

    def apply_rel2_floats_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyRel2FloatsOverride: ...

    def apply_rel3_floats_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyRel3FloatsOverride: ...

    def apply_rel_float_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyRelFloatOverride: ...

    def apply_rel_int_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyRelIntOverride: ...

    def apply_rel_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ApplyRelOverride: ...

    def arnold_aov_child_selector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ArnoldAOVChildSelector: ...

    def array_mapper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ArrayMapper: ...

    def aruba_tessellate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ArubaTessellate: ...

    def asin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Asin: ...

    def atan(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Atan: ...

    def atan2(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Atan2: ...

    def attach_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AttachCurve: ...

    def attach_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AttachSurface: ...

    def attr_hierarchy_test(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AttrHierarchyTest: ...

    def audio(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Audio: ...

    def average(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Average: ...

    def avg_curves(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AvgCurves: ...

    def avg_nurbs_surface_points(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AvgNurbsSurfacePoints: ...

    def avg_surface_points(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AvgSurfacePoints: ...

    def axis_angle_to_quat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AxisAngleToQuat: ...

    def axis_from_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> AxisFromMatrix: ...

    def basic_selector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BasicSelector: ...

    def bevel(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Bevel: ...

    def bevel_plus(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BevelPlus: ...

    def bezier_curve_to_nurbs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BezierCurveToNurbs: ...

    def bifrost_board(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BifrostBoard: ...

    def bifrost_geo_to_maya(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BifrostGeoToMaya: ...

    def blend_color_sets(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BlendColorSets: ...

    def blend_colors(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BlendColors: ...

    def blend_device(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BlendDevice: ...

    def blend_falloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BlendFalloff: ...

    def blend_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BlendMatrix: ...

    def blend_shape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BlendShape: ...

    def blend_two_attr(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BlendTwoAttr: ...

    def blend_weighted(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BlendWeighted: ...

    def blind_data_template(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BlindDataTemplate: ...

    def blinn(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Blinn: ...

    def bone_lattice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> BoneLattice: ...

    def boolean(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Boolean: ...

    def boundary(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Boundary: ...

    def brownian(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Brownian: ...

    def brush(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Brush: ...

    def bulge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Bulge: ...

    def bump2d(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Bump2d: ...

    def bump3d(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Bump3d: ...

    def c_muscle_creator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CMuscleCreator: ...

    def c_muscle_multi_collide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CMuscleMultiCollide: ...

    def c_muscle_relative(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CMuscleRelative: ...

    def c_muscle_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CMuscleShader: ...

    def c_muscle_smart_constraint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CMuscleSmartConstraint: ...

    def c_muscle_spline_deformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CMuscleSplineDeformer: ...

    def c_muscle_stretch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CMuscleStretch: ...

    def c_muscle_system(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CMuscleSystem: ...

    def cache_blend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CacheBlend: ...

    def cache_file(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CacheFile: ...

    def camera_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CameraSet: ...

    def camera_view(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CameraView: ...

    def ceil(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Ceil: ...

    def channels(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Channels: ...

    def character(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Character: ...

    def character_map(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CharacterMap: ...

    def character_offset(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CharacterOffset: ...

    def checker(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Checker: ...

    def child_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ChildNode: ...

    def choice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Choice: ...

    def chooser(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Chooser: ...

    def clamp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Clamp: ...

    def clamp_range(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ClampRange: ...

    def clip_library(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ClipLibrary: ...

    def clip_scheduler(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ClipScheduler: ...

    def clip_to_ghost_data(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ClipToGhostData: ...

    def close_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CloseCurve: ...

    def close_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CloseSurface: ...

    def closest_point_on_mesh(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ClosestPointOnMesh: ...

    def closest_point_on_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ClosestPointOnSurface: ...

    def cloth(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Cloth: ...

    def cloud(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Cloud: ...

    def cluster(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Cluster: ...

    def collection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Collection: ...

    def color_composite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ColorComposite: ...

    def color_condition(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ColorCondition: ...

    def color_constant(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ColorConstant: ...

    def color_correct(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ColorCorrect: ...

    def color_logic(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ColorLogic: ...

    def color_management_globals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ColorManagementGlobals: ...

    def color_mask(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ColorMask: ...

    def color_math(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ColorMath: ...

    def color_profile(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ColorProfile: ...

    def column_from_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ColumnFromMatrix: ...

    def combination_shape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CombinationShape: ...

    def compact_plug_array_test(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CompactPlugArrayTest: ...

    def component_falloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ComponentFalloff: ...

    def component_match(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ComponentMatch: ...

    def component_tag_base(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ComponentTagBase: ...

    def compose_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ComposeMatrix: ...

    def compute_global(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ComputeGlobal: ...

    def compute_local(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ComputeLocal: ...

    def condition(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Condition: ...

    def connection_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ConnectionOverride: ...

    def connection_unique_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ConnectionUniqueOverride: ...

    def container(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Container: ...

    def container_base(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ContainerBase: ...

    def contrast(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Contrast: ...

    def controller(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Controller: ...

    def copy_color_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CopyColorSet: ...

    def copy_uv_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CopyUVSet: ...

    def cos(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Cos: ...

    def cpv_color(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CpvColor: ...

    def crater(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Crater: ...

    def crease_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CreaseSet: ...

    def create_color_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CreateColorSet: ...

    def create_ptex_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CreatePtexUV: ...

    def create_uv_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CreateUVSet: ...

    def cross_product(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CrossProduct: ...

    def cryptomatte(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Cryptomatte: ...

    def curve_from_mesh_co_m(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveFromMeshCoM: ...

    def curve_from_mesh_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveFromMeshEdge: ...

    def curve_from_subdiv_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveFromSubdivEdge: ...

    def curve_from_subdiv_face(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveFromSubdivFace: ...

    def curve_from_surface_bnd(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveFromSurfaceBnd: ...

    def curve_from_surface_co_s(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveFromSurfaceCoS: ...

    def curve_from_surface_iso(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveFromSurfaceIso: ...

    def curve_info(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveInfo: ...

    def curve_intersect(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveIntersect: ...

    def curve_normalizer_angle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveNormalizerAngle: ...

    def curve_normalizer_linear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveNormalizerLinear: ...

    def curve_warp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CurveWarp: ...

    def custom_rig_default_mapping_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CustomRigDefaultMappingNode: ...

    def custom_rig_retargeter_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> CustomRigRetargeterNode: ...

    def dag_pose(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DagPose: ...

    def data_block_test(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DataBlockTest: ...

    def decompose_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DecomposeMatrix: ...

    def default_light_list(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DefaultLightList: ...

    def default_render_utility_list(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DefaultRenderUtilityList: ...

    def default_rendering_list(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DefaultRenderingList: ...

    def default_shader_list(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DefaultShaderList: ...

    def default_texture_list(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DefaultTextureList: ...

    def delete_color_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DeleteColorSet: ...

    def delete_component(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DeleteComponent: ...

    def delete_uv_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DeleteUVSet: ...

    def delta_mush(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DeltaMush: ...

    def detach_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DetachCurve: ...

    def detach_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DetachSurface: ...

    def determinant(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Determinant: ...

    def disk_cache(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DiskCache: ...

    def displacement_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DisplacementShader: ...

    def display_layer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DisplayLayer: ...

    def display_layer_manager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DisplayLayerManager: ...

    def distance_between(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DistanceBetween: ...

    def divide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Divide: ...

    def dof(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Dof: ...

    def dot_product(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DotProduct: ...

    def double_shading_switch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DoubleShadingSwitch: ...

    def dp_birail_srf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DpBirailSrf: ...

    def dyn_controller(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DynController: ...

    def dyn_globals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> DynGlobals: ...

    def edit_metadata(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> EditMetadata: ...

    def edits_manager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> EditsManager: ...

    def env_ball(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> EnvBall: ...

    def env_chrome(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> EnvChrome: ...

    def env_cube(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> EnvCube: ...

    def env_facade(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> EnvFacade: ...

    def env_fog(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> EnvFog: ...

    def env_sky(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> EnvSky: ...

    def env_sphere(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> EnvSphere: ...

    def equal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Equal: ...

    def euler_to_quat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> EulerToQuat: ...

    def explode_nurbs_shell(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ExplodeNurbsShell: ...

    def expression(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Expression: ...

    def extend_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ExtendCurve: ...

    def extend_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ExtendSurface: ...

    def extrude(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Extrude: ...

    def facade(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Facade: ...

    def falloff_eval(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FalloffEval: ...

    def ff_blend_srf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FfBlendSrf: ...

    def ff_blend_srf_obsolete(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FfBlendSrfObsolete: ...

    def ff_fillet_srf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FfFilletSrf: ...

    def ffd(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Ffd: ...

    def file(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> File: ...

    def fillet_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FilletCurve: ...

    def fit_bspline(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FitBspline: ...

    def float_composite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FloatComposite: ...

    def float_condition(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FloatCondition: ...

    def float_constant(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FloatConstant: ...

    def float_correct(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FloatCorrect: ...

    def float_logic(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FloatLogic: ...

    def float_mask(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FloatMask: ...

    def float_math(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FloatMath: ...

    def floor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Floor: ...

    def flow(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Flow: ...

    def four_by_four_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FourByFourMatrix: ...

    def fractal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Fractal: ...

    def frame_cache(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> FrameCache: ...

    def game_fbx_exporter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GameFbxExporter: ...

    def gamma_correct(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GammaCorrect: ...

    def geo_connector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GeoConnector: ...

    def geom_bind(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GeomBind: ...

    def geometry_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GeometryFilter: ...

    def global_cache_control(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GlobalCacheControl: ...

    def global_stitch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GlobalStitch: ...

    def granite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Granite: ...

    def grease_pencil_sequence(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GreasePencilSequence: ...

    def greater_than(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GreaterThan: ...

    def grid(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Grid: ...

    def group(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Group: ...

    def group_id(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GroupId: ...

    def group_parts(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> GroupParts: ...

    def guide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Guide: ...

    def hair_physical_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HairPhysicalShader: ...

    def hair_tube_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HairTubeShader: ...

    def harden_point(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HardenPoint: ...

    def hardware_render_globals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HardwareRenderGlobals: ...

    def hardware_rendering_globals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HardwareRenderingGlobals: ...

    def hierarchy_test_node1(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HierarchyTestNode1: ...

    def hierarchy_test_node2(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HierarchyTestNode2: ...

    def hierarchy_test_node3(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HierarchyTestNode3: ...

    def hierarchy_test_node4(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HierarchyTestNode4: ...

    def hik_character_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKCharacterNode: ...

    def hik_character_state_client(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKCharacterStateClient: ...

    def hik_control_set_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKControlSetNode: ...

    def hik_effector2_state(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKEffector2State: ...

    def hik_effector_from_character(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKEffectorFromCharacter: ...

    def hik_pinning2_state(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKPinning2State: ...

    def hik_property2_state(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKProperty2State: ...

    def hik_retargeter_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKRetargeterNode: ...

    def hik_skeleton_generator_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKSkeletonGeneratorNode: ...

    def hik_solver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HikSolver: ...

    def hik_solver_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKSolverNode: ...

    def hik_state2_effector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKState2Effector: ...

    def hik_state2_fk(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKState2FK: ...

    def hik_state2_global_sk(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKState2GlobalSK: ...

    def hik_state2_sk(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKState2SK: ...

    def hikfk2_state(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKFK2State: ...

    def hiksk2_state(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HIKSK2State: ...

    def history_switch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HistorySwitch: ...

    def hold_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HoldMatrix: ...

    def hsv_to_rgb(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HsvToRgb: ...

    def hw_reflection_map(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HwReflectionMap: ...

    def hw_render_globals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HwRenderGlobals: ...

    def hyper_graph_info(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HyperGraphInfo: ...

    def hyper_layout(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HyperLayout: ...

    def hyper_view(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> HyperView: ...

    def ik2_bsolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Ik2Bsolver: ...

    def ik_m_csolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> IkMCsolver: ...

    def ik_pa_solver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> IkPASolver: ...

    def ik_r_psolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> IkRPsolver: ...

    def ik_s_csolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> IkSCsolver: ...

    def ik_spline_solver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> IkSplineSolver: ...

    def ik_spring_solver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> IkSpringSolver: ...

    def ik_system(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> IkSystem: ...

    def insert_knot_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> InsertKnotCurve: ...

    def insert_knot_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> InsertKnotSurface: ...

    def intersect_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> IntersectSurface: ...

    def inverse_lerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> InverseLerp: ...

    def inverse_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> InverseMatrix: ...

    def jiggle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Jiggle: ...

    def joint_cluster(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> JointCluster: ...

    def joint_ffd(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> JointFfd: ...

    def joint_lattice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> JointLattice: ...

    def keying_group(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> KeyingGroup: ...

    def lambert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Lambert: ...

    def layered_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LayeredShader: ...

    def layered_texture(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LayeredTexture: ...

    def least_squares_modifier(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LeastSquaresModifier: ...

    def leather(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Leather: ...

    def length(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Length: ...

    def lerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Lerp: ...

    def less_than(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LessThan: ...

    def light_editor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightEditor: ...

    def light_fog(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightFog: ...

    def light_group(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightGroup: ...

    def light_info(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightInfo: ...

    def light_item(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightItem: ...

    def light_item_base(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightItemBase: ...

    def light_linker(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightLinker: ...

    def light_list(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightList: ...

    def lights_child_collection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightsChildCollection: ...

    def lights_collection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightsCollection: ...

    def lights_collection_selector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LightsCollectionSelector: ...

    def list_item(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ListItem: ...

    def lod_thresholds(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> LodThresholds: ...

    def loft(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Loft: ...

    def log(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Log: ...

    def luminance(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Luminance: ...

    def make_group(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeGroup: ...

    def make_illustrator_curves(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeIllustratorCurves: ...

    def make_nurb_circle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeNurbCircle: ...

    def make_nurb_cone(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeNurbCone: ...

    def make_nurb_cube(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeNurbCube: ...

    def make_nurb_cylinder(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeNurbCylinder: ...

    def make_nurb_plane(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeNurbPlane: ...

    def make_nurb_sphere(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeNurbSphere: ...

    def make_nurb_torus(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeNurbTorus: ...

    def make_nurbs_square(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeNurbsSquare: ...

    def make_text_curves(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeTextCurves: ...

    def make_three_point_circular_arc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeThreePointCircularArc: ...

    def make_two_point_circular_arc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MakeTwoPointCircularArc: ...

    def mandelbrot(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Mandelbrot: ...

    def mandelbrot3_d(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Mandelbrot3D: ...

    def marble(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Marble: ...

    def mash_audio(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Audio: ...

    def mash_base_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_BaseNode: ...

    def mash_blend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Blend: ...

    def mash_blend_deformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_BlendDeformer: ...

    def mash_breakout(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Breakout: ...

    def mash_channel_random(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_ChannelRandom: ...

    def mash_color(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Color: ...

    def mash_constraint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Constraint: ...

    def mash_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Curve: ...

    def mash_deformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Deformer: ...

    def mash_delay(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Delay: ...

    def mash_distribute(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Distribute: ...

    def mash_dynamics(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Dynamics: ...

    def mash_dynamics_initial_state(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_DynamicsInitialState: ...

    def mash_explode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Explode: ...

    def mash_id(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Id: ...

    def mash_influence(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Influence: ...

    def mash_inherit(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Inherit: ...

    def mash_initial_state(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_InitialState: ...

    def mash_jiggle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Jiggle: ...

    def mash_legacy(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Legacy: ...

    def mash_maths(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Maths: ...

    def mash_multi_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_MultiCurve: ...

    def mash_mute(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Mute: ...

    def mash_noise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Noise: ...

    def mash_offset(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Offset: ...

    def mash_orient(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Orient: ...

    def mash_pfx_connect(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_PfxConnect: ...

    def mash_placer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Placer: ...

    def mash_point_to_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_PointToCurve: ...

    def mash_python(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Python: ...

    def mash_random(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Random: ...

    def mash_replicator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Replicator: ...

    def mash_repro(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Repro: ...

    def mash_shell_deformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_ShellDeformer: ...

    def mash_signal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Signal: ...

    def mash_spring(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Spring: ...

    def mash_strength(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Strength: ...

    def mash_symmetry(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Symmetry: ...

    def mash_time(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Time: ...

    def mash_trails(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Trails: ...

    def mash_transform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Transform: ...

    def mash_trig(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Trig: ...

    def mash_visibility(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Visibility: ...

    def mash_waiter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_Waiter: ...

    def mash_world(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MASH_World: ...

    def material_facade(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MaterialFacade: ...

    def material_info(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MaterialInfo: ...

    def material_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MaterialOverride: ...

    def material_template(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MaterialTemplate: ...

    def material_template_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MaterialTemplateOverride: ...

    def material_x_material(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MaterialXMaterial: ...

    def material_x_surface_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MaterialXSurfaceShader: ...

    def max(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Max: ...

    def maya_usd_geom_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MayaUsdGeomNode: ...

    def maya_usd_layer_manager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MayaUsdLayerManager: ...

    def maya_usd_proxy_shape_listener(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MayaUsdProxyShapeListener: ...

    def maya_usd_proxy_shape_listener_base(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MayaUsdProxyShapeListenerBase: ...

    def membrane(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Membrane: ...

    def min(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Min: ...

    def modulo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Modulo: ...

    def morph(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Morph: ...

    def motion_path(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MotionPath: ...

    def motion_trail(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MotionTrail: ...

    def mountain(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Mountain: ...

    def movie(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Movie: ...

    def mp_birail_srf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MpBirailSrf: ...

    def mult_double_linear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MultDoubleLinear: ...

    def mult_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MultMatrix: ...

    def multilister_light(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MultilisterLight: ...

    def multiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Multiply: ...

    def multiply_divide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MultiplyDivide: ...

    def multiply_point_by_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MultiplyPointByMatrix: ...

    def multiply_vector_by_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> MultiplyVectorByMatrix: ...

    def mute(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Mute: ...

    def n_component(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NComponent: ...

    def nearest_point_on_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NearestPointOnCurve: ...

    def negate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Negate: ...

    def network(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Network: ...

    def node_graph_editor_bookmark_info(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NodeGraphEditorBookmarkInfo: ...

    def node_graph_editor_bookmarks(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NodeGraphEditorBookmarks: ...

    def noise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Noise: ...

    def non_linear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NonLinear: ...

    def normalize(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Normalize: ...

    def not_(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NodeOperator: ...

    def nurbs_curve_to_bezier(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NurbsCurveToBezier: ...

    def nurbs_tessellate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NurbsTessellate: ...

    def nurbs_to_subdiv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NurbsToSubdiv: ...

    def nurbs_to_subdiv_proc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NurbsToSubdivProc: ...

    def object_attr_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ObjectAttrFilter: ...

    def object_bin_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ObjectBinFilter: ...

    def object_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ObjectFilter: ...

    def object_grp_to_comp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ObjectGrpToComp: ...

    def object_multi_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ObjectMultiFilter: ...

    def object_name_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ObjectNameFilter: ...

    def object_render_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ObjectRenderFilter: ...

    def object_script_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ObjectScriptFilter: ...

    def object_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ObjectSet: ...

    def object_type_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ObjectTypeFilter: ...

    def ocean(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Ocean: ...

    def ocean_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> OceanShader: ...

    def offset_cos(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> OffsetCos: ...

    def offset_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> OffsetCurve: ...

    def offset_deformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> OffsetDeformer: ...

    def offset_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> OffsetSurface: ...

    def old_blind_data_base(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> OldBlindDataBase: ...

    def old_geometry_constraint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> OldGeometryConstraint: ...

    def optical_fx(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> OpticalFX: ...

    def or_(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> NodeOperator: ...

    def override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Override: ...

    def pair_blend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PairBlend: ...

    def parent_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ParentMatrix: ...

    def particle_age_mapper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ParticleAgeMapper: ...

    def particle_cloud(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ParticleCloud: ...

    def particle_color_mapper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ParticleColorMapper: ...

    def particle_incand_mapper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ParticleIncandMapper: ...

    def particle_sampler_info(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ParticleSamplerInfo: ...

    def particle_transp_mapper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ParticleTranspMapper: ...

    def partition(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Partition: ...

    def pass_contribution_map(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PassContributionMap: ...

    def pass_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PassMatrix: ...

    def phong(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Phong: ...

    def phong_e(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PhongE: ...

    def pi(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Pi: ...

    def pick_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PickMatrix: ...

    def place2d_texture(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Place2dTexture: ...

    def planar_trim_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PlanarTrimSurface: ...

    def plus_minus_average(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PlusMinusAverage: ...

    def point_matrix_mult(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PointMatrixMult: ...

    def point_on_curve_info(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PointOnCurveInfo: ...

    def point_on_surface_info(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PointOnSurfaceInfo: ...

    def poly_append(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyAppend: ...

    def poly_append_vertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyAppendVertex: ...

    def poly_auto_proj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyAutoProj: ...

    def poly_average_vertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyAverageVertex: ...

    def poly_axis(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyAxis: ...

    def poly_bevel(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyBevel: ...

    def poly_bevel2(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyBevel2: ...

    def poly_bevel3(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyBevel3: ...

    def poly_bevel_cutback(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyBevelCutback: ...

    def poly_blind_data(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyBlindData: ...

    def poly_bool_op(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyBoolOp: ...

    def poly_boolean(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyBoolean: ...

    def poly_bridge_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyBridgeEdge: ...

    def poly_c_bool_op(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCBoolOp: ...

    def poly_chip_off(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyChipOff: ...

    def poly_circularize(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCircularize: ...

    def poly_clean(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyClean: ...

    def poly_close_border(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCloseBorder: ...

    def poly_collapse_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCollapseEdge: ...

    def poly_collapse_f(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCollapseF: ...

    def poly_color_del(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyColorDel: ...

    def poly_color_mod(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyColorMod: ...

    def poly_color_per_vertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyColorPerVertex: ...

    def poly_cone(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCone: ...

    def poly_connect_components(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyConnectComponents: ...

    def poly_contour_proj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyContourProj: ...

    def poly_copy_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCopyUV: ...

    def poly_crease(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCrease: ...

    def poly_crease_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCreaseEdge: ...

    def poly_create_face(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCreateFace: ...

    def poly_cube(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCube: ...

    def poly_cut(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCut: ...

    def poly_cyl_proj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCylProj: ...

    def poly_cylinder(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyCylinder: ...

    def poly_del_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyDelEdge: ...

    def poly_del_facet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyDelFacet: ...

    def poly_del_vertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyDelVertex: ...

    def poly_disc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyDisc: ...

    def poly_duplicate_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyDuplicateEdge: ...

    def poly_edge_to_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyEdgeToCurve: ...

    def poly_edit_edge_flow(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyEditEdgeFlow: ...

    def poly_extrude_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyExtrudeEdge: ...

    def poly_extrude_face(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyExtrudeFace: ...

    def poly_extrude_vertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyExtrudeVertex: ...

    def poly_flip_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyFlipEdge: ...

    def poly_flip_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyFlipUV: ...

    def poly_gear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyGear: ...

    def poly_helix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyHelix: ...

    def poly_hole_face(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyHoleFace: ...

    def poly_layout_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyLayoutUV: ...

    def poly_map_cut(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMapCut: ...

    def poly_map_del(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMapDel: ...

    def poly_map_sew(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMapSew: ...

    def poly_map_sew_move(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMapSewMove: ...

    def poly_merge_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMergeEdge: ...

    def poly_merge_face(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMergeFace: ...

    def poly_merge_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMergeUV: ...

    def poly_merge_vert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMergeVert: ...

    def poly_mirror(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMirror: ...

    def poly_move_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMoveEdge: ...

    def poly_move_face(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMoveFace: ...

    def poly_move_facet_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMoveFacetUV: ...

    def poly_move_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMoveUV: ...

    def poly_move_vertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyMoveVertex: ...

    def poly_normal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyNormal: ...

    def poly_normal_per_vertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyNormalPerVertex: ...

    def poly_normalize_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyNormalizeUV: ...

    def poly_opt_uvs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyOptUvs: ...

    def poly_pass_thru(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPassThru: ...

    def poly_pin_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPinUV: ...

    def poly_pipe(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPipe: ...

    def poly_planar_proj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPlanarProj: ...

    def poly_plane(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPlane: ...

    def poly_platonic(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPlatonic: ...

    def poly_platonic_solid(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPlatonicSolid: ...

    def poly_poke(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPoke: ...

    def poly_primitive_misc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPrimitiveMisc: ...

    def poly_prism(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPrism: ...

    def poly_proj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyProj: ...

    def poly_project_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyProjectCurve: ...

    def poly_pyramid(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyPyramid: ...

    def poly_quad(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyQuad: ...

    def poly_reduce(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyReduce: ...

    def poly_remesh(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyRemesh: ...

    def poly_retopo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyRetopo: ...

    def poly_separate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySeparate: ...

    def poly_sew_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySewEdge: ...

    def poly_smart_extrude(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySmartExtrude: ...

    def poly_smooth(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySmooth: ...

    def poly_smooth_face(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySmoothFace: ...

    def poly_smooth_proxy(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySmoothProxy: ...

    def poly_soft_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySoftEdge: ...

    def poly_sph_proj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySphProj: ...

    def poly_sphere(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySphere: ...

    def poly_spin_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySpinEdge: ...

    def poly_split(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySplit: ...

    def poly_split_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySplitEdge: ...

    def poly_split_ring(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySplitRing: ...

    def poly_split_vert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySplitVert: ...

    def poly_straighten_uv_border(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyStraightenUVBorder: ...

    def poly_subd_edge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySubdEdge: ...

    def poly_subd_face(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySubdFace: ...

    def poly_super_shape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolySuperShape: ...

    def poly_to_subdiv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyToSubdiv: ...

    def poly_torus(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyTorus: ...

    def poly_transfer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyTransfer: ...

    def poly_triangulate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyTriangulate: ...

    def poly_tweak(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyTweak: ...

    def poly_tweak_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyTweakUV: ...

    def poly_unite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyUnite: ...

    def poly_unsmooth(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyUnsmooth: ...

    def poly_uv_rectangle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyUVRectangle: ...

    def poly_wedge_face(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PolyWedgeFace: ...

    def pose_interpolator_manager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PoseInterpolatorManager: ...

    def post_process_list(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PostProcessList: ...

    def power(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Power: ...

    def precomp_export(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PrecompExport: ...

    def premultiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Premultiply: ...

    def project_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ProjectCurve: ...

    def project_tangent(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ProjectTangent: ...

    def projection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Projection: ...

    def proximity_falloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ProximityFalloff: ...

    def proximity_pin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ProximityPin: ...

    def proximity_wrap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ProximityWrap: ...

    def proxy_manager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ProxyManager: ...

    def psd_file_tex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PsdFileTex: ...

    def pxr_usd_point_based_deformer_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PxrUsdPointBasedDeformerNode: ...

    def pxr_usd_stage_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> PxrUsdStageNode: ...

    def quad_shading_switch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuadShadingSwitch: ...

    def quat_add(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuatAdd: ...

    def quat_conjugate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuatConjugate: ...

    def quat_invert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuatInvert: ...

    def quat_negate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuatNegate: ...

    def quat_normalize(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuatNormalize: ...

    def quat_prod(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuatProd: ...

    def quat_slerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuatSlerp: ...

    def quat_sub(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuatSub: ...

    def quat_to_axis_angle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuatToAxisAngle: ...

    def quat_to_euler(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> QuatToEuler: ...

    def r_scontainer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RScontainer: ...

    def ramp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Ramp: ...

    def ramp_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RampShader: ...

    def rbf_srf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RbfSrf: ...

    def rebuild_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RebuildCurve: ...

    def rebuild_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RebuildSurface: ...

    def record(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Record: ...

    def reference(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Reference: ...

    def rel_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RelOverride: ...

    def rel_unique_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RelUniqueOverride: ...

    def remap_color(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RemapColor: ...

    def remap_hsv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RemapHsv: ...

    def remap_value(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RemapValue: ...

    def render_globals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderGlobals: ...

    def render_globals_list(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderGlobalsList: ...

    def render_layer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderLayer: ...

    def render_layer_manager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderLayerManager: ...

    def render_pass(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderPass: ...

    def render_pass_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderPassSet: ...

    def render_quality(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderQuality: ...

    def render_settings_child_collection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderSettingsChildCollection: ...

    def render_settings_collection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderSettingsCollection: ...

    def render_setup(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderSetup: ...

    def render_setup_layer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderSetupLayer: ...

    def render_target(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderTarget: ...

    def rendered_image_source(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RenderedImageSource: ...

    def reorder_uv_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ReorderUVSet: ...

    def resolution(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Resolution: ...

    def result_curve_time_to_angular(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ResultCurveTimeToAngular: ...

    def result_curve_time_to_linear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ResultCurveTimeToLinear: ...

    def result_curve_time_to_time(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ResultCurveTimeToTime: ...

    def result_curve_time_to_unitless(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ResultCurveTimeToUnitless: ...

    def reverse(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Reverse: ...

    def reverse_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ReverseCurve: ...

    def reverse_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ReverseSurface: ...

    def revolve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Revolve: ...

    def rgb_to_hsv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RgbToHsv: ...

    def rigid_solver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RigidSolver: ...

    def rock(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Rock: ...

    def rotate_helper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RotateHelper: ...

    def rotate_vector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RotateVector: ...

    def rotation_from_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RotationFromMatrix: ...

    def round(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Round: ...

    def round_constant_radius(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RoundConstantRadius: ...

    def row_from_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> RowFromMatrix: ...

    def sampler(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Sampler: ...

    def sampler_info(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SamplerInfo: ...

    def scale_from_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ScaleFromMatrix: ...

    def script(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Script: ...

    def sculpt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Sculpt: ...

    def selection_list_operator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SelectionListOperator: ...

    def selector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Selector: ...

    def sequence_manager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SequenceManager: ...

    def sequencer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Sequencer: ...

    def set_range(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SetRange: ...

    def shader_glow(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ShaderGlow: ...

    def shader_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ShaderOverride: ...

    def shading_engine(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ShadingEngine: ...

    def shading_map(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ShadingMap: ...

    def shape_editor_manager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ShapeEditorManager: ...

    def shell_deformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ShellDeformer: ...

    def shell_tessellate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ShellTessellate: ...

    def shot(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Shot: ...

    def shrink_wrap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ShrinkWrap: ...

    def simple_selector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SimpleSelector: ...

    def simple_test_node(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SimpleTestNode: ...

    def simple_volume_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SimpleVolumeShader: ...

    def simplex_noise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SimplexNoise: ...

    def sin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Sin: ...

    def single_shading_switch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SingleShadingSwitch: ...

    def skin_binding(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SkinBinding: ...

    def skin_cluster(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SkinCluster: ...

    def smooth_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SmoothCurve: ...

    def smooth_step(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SmoothStep: ...

    def smooth_tangent_srf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SmoothTangentSrf: ...

    def snapshot(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Snapshot: ...

    def snow(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Snow: ...

    def soft_mod(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SoftMod: ...

    def solid_fractal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SolidFractal: ...

    def solidify(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Solidify: ...

    def sp_birail_srf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SpBirailSrf: ...

    def square_srf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SquareSrf: ...

    def standard_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> StandardSurface: ...

    def stencil(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Stencil: ...

    def stitch_as_nurbs_shell(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> StitchAsNurbsShell: ...

    def stitch_srf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> StitchSrf: ...

    def stroke_globals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> StrokeGlobals: ...

    def stucco(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Stucco: ...

    def style_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> StyleCurve: ...

    def sub_curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubCurve: ...

    def sub_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubSurface: ...

    def subd_add_topology(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdAddTopology: ...

    def subd_auto_proj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdAutoProj: ...

    def subd_blind_data(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdBlindData: ...

    def subd_clean_topology(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdCleanTopology: ...

    def subd_hier_blind(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdHierBlind: ...

    def subd_layout_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdLayoutUV: ...

    def subd_map_cut(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdMapCut: ...

    def subd_map_sew_move(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdMapSewMove: ...

    def subd_planar_proj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdPlanarProj: ...

    def subd_tweak(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdTweak: ...

    def subd_tweak_uv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdTweakUV: ...

    def subdiv_collapse(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdivCollapse: ...

    def subdiv_component_id(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdivComponentId: ...

    def subdiv_reverse_faces(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdivReverseFaces: ...

    def subdiv_to_nurbs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdivToNurbs: ...

    def subdiv_to_poly(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubdivToPoly: ...

    def subset_falloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SubsetFalloff: ...

    def subtract(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Subtract: ...

    def sum(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Sum: ...

    def surface_info(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SurfaceInfo: ...

    def surface_luminance(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SurfaceLuminance: ...

    def surface_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SurfaceShader: ...

    def svg_to_poly(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SvgToPoly: ...

    def sweep_mesh_creator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SweepMeshCreator: ...

    def sweep_profile_converter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> SweepProfileConverter: ...

    def tan(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Tan: ...

    def tension(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Tension: ...

    def tex_lattice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TexLattice: ...

    def texture_bake_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TextureBakeSet: ...

    def texture_deformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TextureDeformer: ...

    def texture_to_geom(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TextureToGeom: ...

    def time(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Time: ...

    def time_editor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TimeEditor: ...

    def time_editor_anim_source(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TimeEditorAnimSource: ...

    def time_editor_clip(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TimeEditorClip: ...

    def time_editor_clip_base(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TimeEditorClipBase: ...

    def time_editor_clip_evaluator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TimeEditorClipEvaluator: ...

    def time_editor_interpolator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TimeEditorInterpolator: ...

    def time_editor_tracks(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TimeEditorTracks: ...

    def time_function(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TimeFunction: ...

    def time_to_unit_conversion(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TimeToUnitConversion: ...

    def time_warp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TimeWarp: ...

    def toon_line_attributes(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ToonLineAttributes: ...

    def track_info_manager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TrackInfoManager: ...

    def transfer_attributes(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TransferAttributes: ...

    def transfer_falloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TransferFalloff: ...

    def transform_geometry(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TransformGeometry: ...

    def translation_from_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TranslationFromMatrix: ...

    def transpose_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TransposeMatrix: ...

    def trim(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Trim: ...

    def trim_with_boundaries(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TrimWithBoundaries: ...

    def triple_shading_switch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TripleShadingSwitch: ...

    def truncate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Truncate: ...

    def tweak(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Tweak: ...

    def type(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Type: ...

    def type_extrude(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> TypeExtrude: ...

    def unfold3_d_optimize(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Unfold3DOptimize: ...

    def unfold3_d_unfold(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Unfold3DUnfold: ...

    def uniform_falloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> UniformFalloff: ...

    def unit_conversion(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> UnitConversion: ...

    def unit_to_time_conversion(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> UnitToTimeConversion: ...

    def unknown(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Unknown: ...

    def unpremultiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Unpremultiply: ...

    def untrim(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Untrim: ...

    def usd_preview_surface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> UsdPreviewSurface: ...

    def use_background(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> UseBackground: ...

    def uv_chooser(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> UvChooser: ...

    def uv_pin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> UvPin: ...

    def value_override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ValueOverride: ...

    def vector_adjust(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> VectorAdjust: ...

    def vector_extrude(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> VectorExtrude: ...

    def vector_product(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> VectorProduct: ...

    def vertex_bake_set(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> VertexBakeSet: ...

    def view_color_manager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> ViewColorManager: ...

    def volume_fog(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> VolumeFog: ...

    def volume_noise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> VolumeNoise: ...

    def volume_shader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> VolumeShader: ...

    def water(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Water: ...

    def weight_geometry_filter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> WeightGeometryFilter: ...

    def wire(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Wire: ...

    def wood(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Wood: ...

    def wrap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Wrap: ...

    def wt_add_matrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> WtAddMatrix: ...

    def xgm_curve_to_spline(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmCurveToSpline: ...

    def xgm_hair_mapping(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmHairMapping: ...

    def xgm_make_guide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmMakeGuide: ...

    def xgm_modifier_base(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmModifierBase: ...

    def xgm_modifier_clump(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmModifierClump: ...

    def xgm_modifier_collision(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmModifierCollision: ...

    def xgm_modifier_cut(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmModifierCut: ...

    def xgm_modifier_displacement(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmModifierDisplacement: ...

    def xgm_modifier_guide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmModifierGuide: ...

    def xgm_modifier_linear_wire(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmModifierLinearWire: ...

    def xgm_modifier_noise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmModifierNoise: ...

    def xgm_modifier_scale(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmModifierScale: ...

    def xgm_modifier_sculpt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmModifierSculpt: ...

    def xgm_se_expr(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmSeExpr: ...

    def xgm_spline_base(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmSplineBase: ...

    def xgm_spline_cache(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> XgmSplineCache: ...
