# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from ..modifier import ModifierManager
from ..operator.node._core import DEFAULT_VALUE_AUTO_ADD_ATTR, NodeOperator
from ..operator.node.dag._core import DAG
from ..operator.node.dag.shape.ai_area_light import AiAreaLight
from ..operator.node.dag.shape.ai_curve_collector import AiCurveCollector
from ..operator.node.dag.shape.ai_light_blocker import AiLightBlocker
from ..operator.node.dag.shape.ai_light_portal import AiLightPortal
from ..operator.node.dag.shape.ai_mesh_light import AiMeshLight
from ..operator.node.dag.shape.ai_photometric_light import AiPhotometricLight
from ..operator.node.dag.shape.ai_sky_dome_light import AiSkyDomeLight
from ..operator.node.dag.shape.ai_stand_in import AiStandIn
from ..operator.node.dag.shape.ai_volume import AiVolume
from ..operator.node.dag.shape.ambient_light import AmbientLight
from ..operator.node.dag.shape.angle_dimension import AngleDimension
from ..operator.node.dag.shape.annotation_shape import AnnotationShape
from ..operator.node.dag.shape.arc_length_dimension import ArcLengthDimension
from ..operator.node.dag.shape.area_light import AreaLight
from ..operator.node.dag.shape.base_lattice import BaseLattice
from ..operator.node.dag.shape.bd_controller_shape import BdControllerShape
from ..operator.node.dag.shape.bezier_curve import BezierCurve
from ..operator.node.dag.shape.camera import Camera
from ..operator.node.dag.shape.cluster_flexor_shape import ClusterFlexorShape
from ..operator.node.dag.shape.cluster_handle import ClusterHandle
from ..operator.node.dag.shape.deform_bend import DeformBend
from ..operator.node.dag.shape.deform_flare import DeformFlare
from ..operator.node.dag.shape.deform_sine import DeformSine
from ..operator.node.dag.shape.deform_squash import DeformSquash
from ..operator.node.dag.shape.deform_twist import DeformTwist
from ..operator.node.dag.shape.deform_wave import DeformWave
from ..operator.node.dag.shape.directed_disc import DirectedDisc
from ..operator.node.dag.shape.directional_light import DirectionalLight
from ..operator.node.dag.shape.distance_dim_shape import DistanceDimShape
from ..operator.node.dag.shape.dropoff_locator import DropoffLocator
from ..operator.node.dag.shape.dynamic_constraint import DynamicConstraint
from ..operator.node.dag.shape.dyn_holder import DynHolder
from ..operator.node.dag.shape.environment_fog import EnvironmentFog
from ..operator.node.dag.shape.flexor_shape import FlexorShape
from ..operator.node.dag.shape.fluid_shape import FluidShape
from ..operator.node.dag.shape.fluid_texture2_d import FluidTexture2D
from ..operator.node.dag.shape.fluid_texture3_d import FluidTexture3D
from ..operator.node.dag.shape.follicle import Follicle
from ..operator.node.dag.shape.geo_connectable import GeoConnectable
from ..operator.node.dag.shape.grease_plane import GreasePlane
from ..operator.node.dag.shape.grease_plane_render_shape import (
    GreasePlaneRenderShape,
)
from ..operator.node.dag.shape.hair_constraint import HairConstraint
from ..operator.node.dag.shape.hair_system import HairSystem
from ..operator.node.dag.shape.height_field import HeightField
from ..operator.node.dag.shape.hik_floor_contact_marker import (
    HikFloorContactMarker,
)
from ..operator.node.dag.shape.image_plane import ImagePlane
from ..operator.node.dag.shape.implicit_box import ImplicitBox
from ..operator.node.dag.shape.implicit_cone import ImplicitCone
from ..operator.node.dag.shape.implicit_sphere import ImplicitSphere
from ..operator.node.dag.shape.lattice import Lattice
from ..operator.node.dag.shape.line_modifier import LineModifier
from ..operator.node.dag.shape.locator import Locator
from ..operator.node.dag.shape.mesh import Mesh
from ..operator.node.dag.shape.motion_trail_shape import MotionTrailShape
from ..operator.node.dag.shape.n_cloth import NCloth
from ..operator.node.dag.shape.n_particle import NParticle
from ..operator.node.dag.shape.n_rigid import NRigid
from ..operator.node.dag.shape.nurbs_curve import NurbsCurve
from ..operator.node.dag.shape.nurbs_surface import NurbsSurface
from ..operator.node.dag.shape.orientation_marker import OrientationMarker
from ..operator.node.dag.shape.param_dimension import ParamDimension
from ..operator.node.dag.shape.particle import Particle
from ..operator.node.dag.shape.pfx_hair import PfxHair
from ..operator.node.dag.shape.pfx_toon import PfxToon
from ..operator.node.dag.shape.point_light import PointLight
from ..operator.node.dag.shape.position_marker import PositionMarker
from ..operator.node.dag.shape.render_box import RenderBox
from ..operator.node.dag.shape.render_cone import RenderCone
from ..operator.node.dag.shape.render_rect import RenderRect
from ..operator.node.dag.shape.render_sphere import RenderSphere
from ..operator.node.dag.shape.rigid_body import RigidBody
from ..operator.node.dag.shape.sketch_plane import SketchPlane
from ..operator.node.dag.shape.snapshot_shape import SnapshotShape
from ..operator.node.dag.shape.soft_mod_handle import SoftModHandle
from ..operator.node.dag.shape.spot_light import SpotLight
from ..operator.node.dag.shape.spring import Spring
from ..operator.node.dag.shape.stereo_rig_camera import StereoRigCamera
from ..operator.node.dag.shape.stroke import Stroke
from ..operator.node.dag.shape.subdiv import Subdiv
from ..operator.node.dag.shape.ufe_proxy_camera_shape import (
    UfeProxyCameraShape,
)
from ..operator.node.dag.shape.volume_light import VolumeLight
from ..operator.node.dag.transform._core import Transform
from ..operator.node.dag.transform.joint import Joint
from ..operator.node.dg.about_to_set_value_test_node import (
    AboutToSetValueTestNode,
)
from ..operator.node.dg.abs_override import AbsOverride
from ..operator.node.dg.abs_unique_override import AbsUniqueOverride
from ..operator.node.dg.absolute import Absolute
from ..operator.node.dg.acos import Acos
from ..operator.node.dg.add_double_linear import AddDoubleLinear
from ..operator.node.dg.add_matrix import AddMatrix
from ..operator.node.dg.adsk_material import AdskMaterial
from ..operator.node.dg.adsk_prepare_render_globals import (
    AdskPrepareRenderGlobals,
)
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
from ..operator.node.dg.anim_blend_node_additive_da import (
    AnimBlendNodeAdditiveDA,
)
from ..operator.node.dg.anim_blend_node_additive_dl import (
    AnimBlendNodeAdditiveDL,
)
from ..operator.node.dg.anim_blend_node_additive_f import (
    AnimBlendNodeAdditiveF,
)
from ..operator.node.dg.anim_blend_node_additive_fa import (
    AnimBlendNodeAdditiveFA,
)
from ..operator.node.dg.anim_blend_node_additive_fl import (
    AnimBlendNodeAdditiveFL,
)
from ..operator.node.dg.anim_blend_node_additive_i16 import (
    AnimBlendNodeAdditiveI16,
)
from ..operator.node.dg.anim_blend_node_additive_i32 import (
    AnimBlendNodeAdditiveI32,
)
from ..operator.node.dg.anim_blend_node_additive_rotation import (
    AnimBlendNodeAdditiveRotation,
)
from ..operator.node.dg.anim_blend_node_additive_scale import (
    AnimBlendNodeAdditiveScale,
)
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
from ..operator.node.dg.apply_abs2_floats_override import (
    ApplyAbs2FloatsOverride,
)
from ..operator.node.dg.apply_abs3_floats_override import (
    ApplyAbs3FloatsOverride,
)
from ..operator.node.dg.apply_abs_bool_override import ApplyAbsBoolOverride
from ..operator.node.dg.apply_abs_enum_override import ApplyAbsEnumOverride
from ..operator.node.dg.apply_abs_float_override import ApplyAbsFloatOverride
from ..operator.node.dg.apply_abs_int_override import ApplyAbsIntOverride
from ..operator.node.dg.apply_abs_override import ApplyAbsOverride
from ..operator.node.dg.apply_abs_string_override import ApplyAbsStringOverride
from ..operator.node.dg.apply_connection_override import (
    ApplyConnectionOverride,
)
from ..operator.node.dg.apply_override import ApplyOverride
from ..operator.node.dg.apply_rel2_floats_override import (
    ApplyRel2FloatsOverride,
)
from ..operator.node.dg.apply_rel3_floats_override import (
    ApplyRel3FloatsOverride,
)
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
from ..operator.node.dg.bd_any_condition_dbl import BdAnyConditionDbl
from ..operator.node.dg.bd_any_condition_dbl_a import BdAnyConditionDblA
from ..operator.node.dg.bd_any_condition_dbl_a_multi import (
    BdAnyConditionDblAMulti,
)
from ..operator.node.dg.bd_any_condition_dbl_l import BdAnyConditionDblL
from ..operator.node.dg.bd_any_condition_dbl_l_multi import (
    BdAnyConditionDblLMulti,
)
from ..operator.node.dg.bd_any_condition_dbl_multi import (
    BdAnyConditionDblMulti,
)
from ..operator.node.dg.bd_condition_dbl_case_compose import (
    BdConditionDblCaseCompose,
)
from ..operator.node.dg.bd_condition_dbl_a_case_compose import (
    BdConditionDblACaseCompose,
)
from ..operator.node.dg.bd_condition_dbl_a_extra_compose import (
    BdConditionDblAExtraCompose,
)
from ..operator.node.dg.bd_condition_dbl_extra_compose import (
    BdConditionDblExtraCompose,
)
from ..operator.node.dg.bd_condition_dbl_l_case_compose import (
    BdConditionDblLCaseCompose,
)
from ..operator.node.dg.bd_condition_dbl_l_extra_compose import (
    BdConditionDblLExtraCompose,
)
from ..operator.node.dg.bd_dbl3_abs import BdDbl3Abs
from ..operator.node.dg.bd_dbl3_add import BdDbl3Add
from ..operator.node.dg.bd_dbl3_add_multi import BdDbl3AddMulti
from ..operator.node.dg.bd_dbl3_average import BdDbl3Average
from ..operator.node.dg.bd_dbl3_average_multi import BdDbl3AverageMulti
from ..operator.node.dg.bd_dbl3_clamp import BdDbl3Clamp
from ..operator.node.dg.bd_dbl3_divide import BdDbl3Divide
from ..operator.node.dg.bd_dbl3_divide_multi import BdDbl3DivideMulti
from ..operator.node.dg.bd_dbl3_value import BdDbl3Value
from ..operator.node.dg.bd_dbl3_lerp import BdDbl3Lerp
from ..operator.node.dg.bd_dbl3_map_range import BdDbl3MapRange
from ..operator.node.dg.bd_dbl3_max import BdDbl3Max
from ..operator.node.dg.bd_dbl3_max_multi import BdDbl3MaxMulti
from ..operator.node.dg.bd_dbl3_min import BdDbl3Min
from ..operator.node.dg.bd_dbl3_min_multi import BdDbl3MinMulti
from ..operator.node.dg.bd_dbl3_negate import BdDbl3Negate
from ..operator.node.dg.bd_dbl3_multiply import BdDbl3Multiply
from ..operator.node.dg.bd_dbl3_multiply_multi import BdDbl3MultiplyMulti
from ..operator.node.dg.bd_dbl3_power import BdDbl3Power
from ..operator.node.dg.bd_dbl3_power_multi import BdDbl3PowerMulti
from ..operator.node.dg.bd_dbl3_ratio_dbl_l3 import BdDbl3RatioDblL3
from ..operator.node.dg.bd_dbl3_subtract import BdDbl3Subtract
from ..operator.node.dg.bd_dbl3_subtract_multi import BdDbl3SubtractMulti
from ..operator.node.dg.bd_dbl3_weighted_average_multi import (
    BdDbl3WeightedAverageMulti,
)
from ..operator.node.dg.bd_dbl3_weighted_sum_multi import (
    BdDbl3WeightedSumMulti,
)
from ..operator.node.dg.bd_dbl_a_abs import BdDblAAbs
from ..operator.node.dg.bd_dbl_a_add import BdDblAAdd
from ..operator.node.dg.bd_dbl_a_add_multi import BdDblAAddMulti
from ..operator.node.dg.bd_dbl_a_average import BdDblAAverage
from ..operator.node.dg.bd_dbl_a_average_multi import BdDblAAverageMulti
from ..operator.node.dg.bd_dbl_a_clamp import BdDblAClamp
from ..operator.node.dg.bd_dbl_a_divide import BdDblADivide
from ..operator.node.dg.bd_dbl_a_divide_multi import BdDblADivideMulti
from ..operator.node.dg.bd_dbl_a_lerp import BdDblALerp
from ..operator.node.dg.bd_dbl_a_lerp_shortest import BdDblALerpShortest
from ..operator.node.dg.bd_dbl_a_map_range import BdDblAMapRange
from ..operator.node.dg.bd_dbl_a_max import BdDblAMax
from ..operator.node.dg.bd_dbl_a_max_multi import BdDblAMaxMulti
from ..operator.node.dg.bd_dbl_a_min import BdDblAMin
from ..operator.node.dg.bd_dbl_a_min_multi import BdDblAMinMulti
from ..operator.node.dg.bd_dbl_a_multiply import BdDblAMultiply
from ..operator.node.dg.bd_dbl_a_multiply_multi import BdDblAMultiplyMulti
from ..operator.node.dg.bd_dbl_a_negate import BdDblANegate
from ..operator.node.dg.bd_dbl_a_shortest_delta import BdDblAShortestDelta
from ..operator.node.dg.bd_dbl_a_subtract import BdDblASubtract
from ..operator.node.dg.bd_dbl_a_subtract_multi import BdDblASubtractMulti
from ..operator.node.dg.bd_dbl_a_value import BdDblAValue
from ..operator.node.dg.bd_dbl_a_weighted_average_multi import (
    BdDblAWeightedAverageMulti,
)
from ..operator.node.dg.bd_dbl_a_weighted_sum_multi import (
    BdDblAWeightedSumMulti,
)
from ..operator.node.dg.bd_dbl_a_wrap import BdDblAWrap
from ..operator.node.dg.bd_dbl_abs import BdDblAbs
from ..operator.node.dg.bd_dbl_add import BdDblAdd
from ..operator.node.dg.bd_dbl_add_multi import BdDblAddMulti
from ..operator.node.dg.bd_dbl_average import BdDblAverage
from ..operator.node.dg.bd_dbl_average_multi import BdDblAverageMulti
from ..operator.node.dg.bd_dbl_clamp import BdDblClamp
from ..operator.node.dg.bd_dbl_divide import BdDblDivide
from ..operator.node.dg.bd_dbl_divide_multi import BdDblDivideMulti
from ..operator.node.dg.bd_dbl_value import BdDblValue
from ..operator.node.dg.bd_dbl_lerp import BdDblLerp
from ..operator.node.dg.bd_dbl_map_range import BdDblMapRange
from ..operator.node.dg.bd_dbl_max import BdDblMax
from ..operator.node.dg.bd_dbl_max_multi import BdDblMaxMulti
from ..operator.node.dg.bd_dbl_min import BdDblMin
from ..operator.node.dg.bd_dbl_min_multi import BdDblMinMulti
from ..operator.node.dg.bd_dbl_negate import BdDblNegate
from ..operator.node.dg.bd_dbl_multiply import BdDblMultiply
from ..operator.node.dg.bd_dbl_multiply_multi import BdDblMultiplyMulti
from ..operator.node.dg.bd_dbl_power import BdDblPower
from ..operator.node.dg.bd_dbl_power_multi import BdDblPowerMulti
from ..operator.node.dg.bd_dbl_ratio_dbl_l import BdDblRatioDblL
from ..operator.node.dg.bd_dbl_ratio_dbl_a import BdDblRatioDblA
from ..operator.node.dg.bd_dbl_subtract import BdDblSubtract
from ..operator.node.dg.bd_dbl_subtract_multi import BdDblSubtractMulti
from ..operator.node.dg.bd_dbl_weighted_average_multi import (
    BdDblWeightedAverageMulti,
)
from ..operator.node.dg.bd_dbl_weighted_sum_multi import BdDblWeightedSumMulti
from ..operator.node.dg.bd_euler_compose_bend_twist import (
    BdEulerComposeBendTwist,
)
from ..operator.node.dg.bd_euler_decompose_bend_twist import (
    BdEulerDecomposeBendTwist,
)
from ..operator.node.dg.bd_euler_decompose_twist import BdEulerDecomposeTwist
from ..operator.node.dg.bd_euler_limit_bend_twist import BdEulerLimitBendTwist
from ..operator.node.dg.bd_euler_value import BdEulerValue
from ..operator.node.dg.bd_quat_change_basis import BdQuatChangeBasis
from ..operator.node.dg.bd_quat_compose_bend_twist import (
    BdQuatComposeBendTwist,
)
from ..operator.node.dg.bd_quat_decompose_bend_twist import (
    BdQuatDecomposeBendTwist,
)
from ..operator.node.dg.bd_quat_decompose_twist import BdQuatDecomposeTwist
from ..operator.node.dg.bd_quat_limit_bend_twist import BdQuatLimitBendTwist
from ..operator.node.dg.bd_quat_multiply_multi import BdQuatMultiplyMulti
from ..operator.node.dg.bd_quat_value import BdQuatValue
from ..operator.node.dg.bd_rbf_bend_twist_falloff_weight import (
    BdRbfBendTwistFalloffWeight,
)
from ..operator.node.dg.bd_rbf_multi_bend_twist_falloff_weight import (
    BdRbfMultiBendTwistFalloffWeight,
)
from ..operator.node.dg.bd_rbf_multi_orientation_falloff_weight import (
    BdRbfMultiOrientationFalloffWeight,
)
from ..operator.node.dg.bd_rbf_multi_orientation_weight import (
    BdRbfMultiOrientationWeight,
)
from ..operator.node.dg.bd_rbf_multi_position_falloff_weight import (
    BdRbfMultiPositionFalloffWeight,
)
from ..operator.node.dg.bd_rbf_multi_position_weight import (
    BdRbfMultiPositionWeight,
)
from ..operator.node.dg.bd_rbf_pose_blend import BdRbfPoseBlend
from ..operator.node.dg.bd_rbf_orientation_falloff_weight import (
    BdRbfOrientationFalloffWeight,
)
from ..operator.node.dg.bd_rbf_orientation_weight import BdRbfOrientationWeight
from ..operator.node.dg.bd_rbf_position_falloff_weight import (
    BdRbfPositionFalloffWeight,
)
from ..operator.node.dg.bd_rbf_position_weight import BdRbfPositionWeight
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
from ..operator.node.dg.connection_unique_override import (
    ConnectionUniqueOverride,
)
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
from ..operator.node.dg.custom_rig_default_mapping_node import (
    CustomRigDefaultMappingNode,
)
from ..operator.node.dg.custom_rig_retargeter_node import (
    CustomRigRetargeterNode,
)
from ..operator.node.dg.dag_pose import DagPose
from ..operator.node.dg.data_block_test import DataBlockTest
from ..operator.node.dg.decompose_matrix import DecomposeMatrix
from ..operator.node.dg.default_light_list import DefaultLightList
from ..operator.node.dg.default_render_utility_list import (
    DefaultRenderUtilityList,
)
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
from ..operator.node.dg.hardware_rendering_globals import (
    HardwareRenderingGlobals,
)
from ..operator.node.dg.hierarchy_test_node1 import HierarchyTestNode1
from ..operator.node.dg.hierarchy_test_node2 import HierarchyTestNode2
from ..operator.node.dg.hierarchy_test_node3 import HierarchyTestNode3
from ..operator.node.dg.hierarchy_test_node4 import HierarchyTestNode4
from ..operator.node.dg.hik_character_node import HIKCharacterNode
from ..operator.node.dg.hik_character_state_client import (
    HIKCharacterStateClient,
)
from ..operator.node.dg.hik_control_set_node import HIKControlSetNode
from ..operator.node.dg.hik_effector2_state import HIKEffector2State
from ..operator.node.dg.hik_effector_from_character import (
    HIKEffectorFromCharacter,
)
from ..operator.node.dg.hik_pinning2_state import HIKPinning2State
from ..operator.node.dg.hik_property2_state import HIKProperty2State
from ..operator.node.dg.hik_retargeter_node import HIKRetargeterNode
from ..operator.node.dg.hik_skeleton_generator_node import (
    HIKSkeletonGeneratorNode,
)
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
from ..operator.node.dg.lights_collection_selector import (
    LightsCollectionSelector,
)
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
from ..operator.node.dg.make_three_point_circular_arc import (
    MakeThreePointCircularArc,
)
from ..operator.node.dg.make_two_point_circular_arc import (
    MakeTwoPointCircularArc,
)
from ..operator.node.dg.mandelbrot import Mandelbrot
from ..operator.node.dg.mandelbrot3_d import Mandelbrot3D
from ..operator.node.dg.marble import Marble
from ..operator.node.dg.mash_audio import MASHAudio
from ..operator.node.dg.mash_base_node import MASHBaseNode
from ..operator.node.dg.mash_blend import MASHBlend
from ..operator.node.dg.mash_blend_deformer import MASHBlendDeformer
from ..operator.node.dg.mash_breakout import MASHBreakout
from ..operator.node.dg.mash_channel_random import MASHChannelRandom
from ..operator.node.dg.mash_color import MASHColor
from ..operator.node.dg.mash_constraint import MASHConstraint
from ..operator.node.dg.mash_curve import MASHCurve
from ..operator.node.dg.mash_deformer import MASHDeformer
from ..operator.node.dg.mash_delay import MASHDelay
from ..operator.node.dg.mash_distribute import MASHDistribute
from ..operator.node.dg.mash_dynamics import MASHDynamics
from ..operator.node.dg.mash_dynamics_initial_state import (
    MASHDynamicsInitialState,
)
from ..operator.node.dg.mash_explode import MASHExplode
from ..operator.node.dg.mash_id import MASHId
from ..operator.node.dg.mash_influence import MASHInfluence
from ..operator.node.dg.mash_inherit import MASHInherit
from ..operator.node.dg.mash_initial_state import MASHInitialState
from ..operator.node.dg.mash_jiggle import MASHJiggle
from ..operator.node.dg.mash_legacy import MASHLegacy
from ..operator.node.dg.mash_maths import MASHMaths
from ..operator.node.dg.mash_multi_curve import MASHMultiCurve
from ..operator.node.dg.mash_mute import MASHMute
from ..operator.node.dg.mash_noise import MASHNoise
from ..operator.node.dg.mash_offset import MASHOffset
from ..operator.node.dg.mash_orient import MASHOrient
from ..operator.node.dg.mash_pfx_connect import MASHPfxConnect
from ..operator.node.dg.mash_placer import MASHPlacer
from ..operator.node.dg.mash_point_to_curve import MASHPointToCurve
from ..operator.node.dg.mash_python import MASHPython
from ..operator.node.dg.mash_random import MASHRandom
from ..operator.node.dg.mash_replicator import MASHReplicator
from ..operator.node.dg.mash_repro import MASHRepro
from ..operator.node.dg.mash_shell_deformer import MASHShellDeformer
from ..operator.node.dg.mash_signal import MASHSignal
from ..operator.node.dg.mash_spring import MASHSpring
from ..operator.node.dg.mash_strength import MASHStrength
from ..operator.node.dg.mash_symmetry import MASHSymmetry
from ..operator.node.dg.mash_time import MASHTime
from ..operator.node.dg.mash_trails import MASHTrails
from ..operator.node.dg.mash_transform import MASHTransform
from ..operator.node.dg.mash_trig import MASHTrig
from ..operator.node.dg.mash_visibility import MASHVisibility
from ..operator.node.dg.mash_waiter import MASHWaiter
from ..operator.node.dg.mash_world import MASHWorld
from ..operator.node.dg.material_facade import MaterialFacade
from ..operator.node.dg.material_info import MaterialInfo
from ..operator.node.dg.material_override import MaterialOverride
from ..operator.node.dg.material_template import MaterialTemplate
from ..operator.node.dg.material_template_override import (
    MaterialTemplateOverride,
)
from ..operator.node.dg.material_x_material import MaterialXMaterial
from ..operator.node.dg.material_x_surface_shader import MaterialXSurfaceShader
from ..operator.node.dg.max import Max
from ..operator.node.dg.maya_usd_geom_node import MayaUsdGeomNode
from ..operator.node.dg.maya_usd_layer_manager import MayaUsdLayerManager
from ..operator.node.dg.maya_usd_proxy_shape_listener import (
    MayaUsdProxyShapeListener,
)
from ..operator.node.dg.maya_usd_proxy_shape_listener_base import (
    MayaUsdProxyShapeListenerBase,
)
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
from ..operator.node.dg.node_graph_editor_bookmark_info import (
    NodeGraphEditorBookmarkInfo,
)
from ..operator.node.dg.node_graph_editor_bookmarks import (
    NodeGraphEditorBookmarks,
)
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
from ..operator.node.dg.pose_interpolator_manager import (
    PoseInterpolatorManager,
)
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
from ..operator.node.dg.pxr_usd_point_based_deformer_node import (
    PxrUsdPointBasedDeformerNode,
)
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
from ..operator.node.dg.render_settings_child_collection import (
    RenderSettingsChildCollection,
)
from ..operator.node.dg.render_settings_collection import (
    RenderSettingsCollection,
)
from ..operator.node.dg.render_setup import RenderSetup
from ..operator.node.dg.render_setup_layer import RenderSetupLayer
from ..operator.node.dg.render_target import RenderTarget
from ..operator.node.dg.rendered_image_source import RenderedImageSource
from ..operator.node.dg.reorder_uv_set import ReorderUVSet
from ..operator.node.dg.resolution import Resolution
from ..operator.node.dg.result_curve_time_to_angular import (
    ResultCurveTimeToAngular,
)
from ..operator.node.dg.result_curve_time_to_linear import (
    ResultCurveTimeToLinear,
)
from ..operator.node.dg.result_curve_time_to_time import ResultCurveTimeToTime
from ..operator.node.dg.result_curve_time_to_unitless import (
    ResultCurveTimeToUnitless,
)
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
from ..operator.node.dg.time_editor_clip_evaluator import (
    TimeEditorClipEvaluator,
)
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
from ..operator.node.dg.xgm_modifier_displacement import (
    XgmModifierDisplacement,
)
from ..operator.node.dg.xgm_modifier_guide import XgmModifierGuide
from ..operator.node.dg.xgm_modifier_linear_wire import XgmModifierLinearWire
from ..operator.node.dg.xgm_modifier_noise import XgmModifierNoise
from ..operator.node.dg.xgm_modifier_scale import XgmModifierScale
from ..operator.node.dg.xgm_modifier_sculpt import XgmModifierSculpt
from ..operator.node.dg.xgm_se_expr import XgmSeExpr
from ..operator.node.dg.xgm_spline_base import XgmSplineBase
from ..operator.node.dg.xgm_spline_cache import XgmSplineCache

from ..operator.node.dg.bd_dbl_l_abs import BdDblLAbs
from ..operator.node.dg.bd_dbl_l_add import BdDblLAdd
from ..operator.node.dg.bd_dbl_l_add_multi import BdDblLAddMulti
from ..operator.node.dg.bd_dbl_l_average import BdDblLAverage
from ..operator.node.dg.bd_dbl_l_average_multi import BdDblLAverageMulti
from ..operator.node.dg.bd_dbl_l_clamp import BdDblLClamp
from ..operator.node.dg.bd_dbl_l_divide import BdDblLDivide
from ..operator.node.dg.bd_dbl_l_divide_multi import BdDblLDivideMulti
from ..operator.node.dg.bd_dbl_l_lerp import BdDblLLerp
from ..operator.node.dg.bd_dbl_l_map_range import BdDblLMapRange
from ..operator.node.dg.bd_dbl_l_max import BdDblLMax
from ..operator.node.dg.bd_dbl_l_max_multi import BdDblLMaxMulti
from ..operator.node.dg.bd_dbl_l_min import BdDblLMin
from ..operator.node.dg.bd_dbl_l_min_multi import BdDblLMinMulti
from ..operator.node.dg.bd_dbl_l_multiply import BdDblLMultiply
from ..operator.node.dg.bd_dbl_l_multiply_multi import BdDblLMultiplyMulti
from ..operator.node.dg.bd_dbl_l_negate import BdDblLNegate
from ..operator.node.dg.bd_dbl_l_right_triangle import BdDblLRightTriangle
from ..operator.node.dg.bd_dbl_l_subtract import BdDblLSubtract
from ..operator.node.dg.bd_dbl_l_subtract_multi import BdDblLSubtractMulti
from ..operator.node.dg.bd_dbl_l_value import BdDblLValue
from ..operator.node.dg.bd_dbl_l_weighted_average_multi import (
    BdDblLWeightedAverageMulti,
)
from ..operator.node.dg.bd_dbl_l_weighted_sum_multi import (
    BdDblLWeightedSumMulti,
)
from ..operator.node.dg.bd_dbl_l3_abs import BdDblL3Abs
from ..operator.node.dg.bd_dbl_l3_add import BdDblL3Add
from ..operator.node.dg.bd_dbl_l3_add_multi import BdDblL3AddMulti
from ..operator.node.dg.bd_dbl_l3_average import BdDblL3Average
from ..operator.node.dg.bd_dbl_l3_average_multi import BdDblL3AverageMulti
from ..operator.node.dg.bd_dbl_l3_clamp import BdDblL3Clamp
from ..operator.node.dg.bd_dbl_l3_divide import BdDblL3Divide
from ..operator.node.dg.bd_dbl_l3_divide_multi import BdDblL3DivideMulti
from ..operator.node.dg.bd_dbl_l3_lerp import BdDblL3Lerp
from ..operator.node.dg.bd_dbl_l3_map_range import BdDblL3MapRange
from ..operator.node.dg.bd_dbl_l3_max import BdDblL3Max
from ..operator.node.dg.bd_dbl_l3_max_multi import BdDblL3MaxMulti
from ..operator.node.dg.bd_dbl_l3_min import BdDblL3Min
from ..operator.node.dg.bd_dbl_l3_min_multi import BdDblL3MinMulti
from ..operator.node.dg.bd_dbl_l3_multiply import BdDblL3Multiply
from ..operator.node.dg.bd_dbl_l3_multiply_multi import (
    BdDblL3MultiplyMulti,
)
from ..operator.node.dg.bd_dbl_l3_negate import BdDblL3Negate
from ..operator.node.dg.bd_dbl_l3_subtract import BdDblL3Subtract
from ..operator.node.dg.bd_dbl_l3_subtract_multi import BdDblL3SubtractMulti
from ..operator.node.dg.bd_dbl_l3_value import BdDblL3Value
from ..operator.node.dg.bd_dbl_l3_weighted_average_multi import (
    BdDblL3WeightedAverageMulti,
)
from ..operator.node.dg.bd_dbl_l3_weighted_sum_multi import (
    BdDblL3WeightedSumMulti,
)
from ._shape_with_transform import ShapeWithTransformCreator
from ._transform_creator import _TransformNodeCreatorMixin

class NodeCreator(_TransformNodeCreatorMixin):
    def __init__(
        self,
        modifier_manager: ModifierManager | None = None,
        *,
        namespace: str | None = None,
    ) -> None: ...
    @property
    def modifier_manager(self) -> ModifierManager: ...
    @property
    def namespace(self) -> str | None: ...
    def set_namespace(self, namespace: str | None) -> None: ...
    @property
    def with_transform(self) -> ShapeWithTransformCreator: ...
    def controllerShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        shape_name: str | None = None,
        parent: DAG | None = None,
        namespace: str | None = None,
    ) -> tuple[Transform, BdControllerShape]: ...
    def create(
        self,
        node_name: str,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: DAG | None = None,
        namespace: str | None = None,
    ) -> NodeOperator: ...
    def node_class(self, node_name: str) -> type[NodeOperator]: ...
    def available_node_names(self) -> tuple[str, ...]: ...
    def __getattr__(self, node_name: str) -> Callable[..., NodeOperator]: ...
    def aboutToSetValueTestNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AboutToSetValueTestNode: ...
    def absOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AbsOverride: ...
    def absUniqueOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AbsUniqueOverride: ...
    def absolute(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Absolute: ...
    def acos(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Acos: ...
    def addDoubleLinear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AddDoubleLinear: ...
    def addMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AddMatrix: ...
    def adskMaterial(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AdskMaterial: ...
    def adskPrepareRenderGlobals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AdskPrepareRenderGlobals: ...
    def aiAbs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiAbs: ...
    def aiAdd(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiAdd: ...
    def aiAmbientOcclusion(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiAmbientOcclusion: ...
    def aiAOV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiAOV: ...
    def aiAOVDriver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiAOVDriver: ...
    def aiAOVFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiAOVFilter: ...
    def aiAreaLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AiAreaLight: ...
    def aiAtan(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiAtan: ...
    def aiAtmosphereVolume(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiAtmosphereVolume: ...
    def aiAxfShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiAxfShader: ...
    def aiBarndoor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiBarndoor: ...
    def aiBlackbody(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiBlackbody: ...
    def aiBump2d(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiBump2d: ...
    def aiBump3d(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiBump3d: ...
    def aiCache(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiCache: ...
    def aiCameraProjection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiCameraProjection: ...
    def aiCarPaint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiCarPaint: ...
    def aiCellNoise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiCellNoise: ...
    def aiCheckerboard(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiCheckerboard: ...
    def aiClamp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiClamp: ...
    def aiClipGeo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiClipGeo: ...
    def aiCollection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiCollection: ...
    def aiColorConvert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiColorConvert: ...
    def aiColorCorrect(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiColorCorrect: ...
    def aiColorJitter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiColorJitter: ...
    def aiColorToFloat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiColorToFloat: ...
    def aiCompare(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiCompare: ...
    def aiComplement(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiComplement: ...
    def aiComplexIor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiComplexIor: ...
    def aiComposite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiComposite: ...
    def aiCross(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiCross: ...
    def aiCurvature(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiCurvature: ...
    def aiCurveCollector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AiCurveCollector: ...
    def aiDisable(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiDisable: ...
    def aiDistance(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiDistance: ...
    def aiDivide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiDivide: ...
    def aiDot(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiDot: ...
    def aiExp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiExp: ...
    def aiFacingRatio(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiFacingRatio: ...
    def aiFlakes(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiFlakes: ...
    def aiFlat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiFlat: ...
    def aiFloatToInt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiFloatToInt: ...
    def aiFloatToMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiFloatToMatrix: ...
    def aiFloatToRgba(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiFloatToRgba: ...
    def aiFog(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiFog: ...
    def aiFraction(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiFraction: ...
    def aiGobo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiGobo: ...
    def aiHair(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiHair: ...
    def aiImage(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImage: ...
    def aiImagerColorCorrect(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerColorCorrect: ...
    def aiImagerColorCurves(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerColorCurves: ...
    def aiImagerDenoiserNoice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerDenoiserNoice: ...
    def aiImagerDenoiserOidn(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerDenoiserOidn: ...
    def aiImagerDenoiserOptix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerDenoiserOptix: ...
    def aiImagerExposure(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerExposure: ...
    def aiImagerLensEffects(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerLensEffects: ...
    def aiImagerLightMixer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerLightMixer: ...
    def aiImagerOverlay(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerOverlay: ...
    def aiImagerTonemap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerTonemap: ...
    def aiImagerWhiteBalance(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiImagerWhiteBalance: ...
    def aiIncludeGraph(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiIncludeGraph: ...
    def aiIsFinite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiIsFinite: ...
    def aiLambert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiLambert: ...
    def aiLayerFloat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiLayerFloat: ...
    def aiLayerRgba(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiLayerRgba: ...
    def aiLayerShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiLayerShader: ...
    def aiLength(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiLength: ...
    def aiLightBlocker(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AiLightBlocker: ...
    def aiLightDecay(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiLightDecay: ...
    def aiLightPortal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AiLightPortal: ...
    def aiLog(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiLog: ...
    def aiLookSwitch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiLookSwitch: ...
    def aiMaterialXShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMaterialXShader: ...
    def aiMaterialx(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMaterialx: ...
    def aiMatrixInterpolate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMatrixInterpolate: ...
    def aiMatrixMultiplyVector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMatrixMultiplyVector: ...
    def aiMatrixTransform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMatrixTransform: ...
    def aiMatte(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMatte: ...
    def aiMax(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMax: ...
    def aiMerge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMerge: ...
    def aiMeshLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AiMeshLight: ...
    def aiMin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMin: ...
    def aiMixShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMixShader: ...
    def aiModulo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiModulo: ...
    def aiMotionVector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMotionVector: ...
    def aiMultiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiMultiply: ...
    def aiNegate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiNegate: ...
    def aiNoise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiNoise: ...
    def aiNormalMap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiNormalMap: ...
    def aiNormalize(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiNormalize: ...
    def aiOptions(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiOptions: ...
    def aiOslShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiOslShader: ...
    def aiPassthrough(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiPassthrough: ...
    def aiPhotometricLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AiPhotometricLight: ...
    def aiPhysicalSky(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiPhysicalSky: ...
    def aiPow(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiPow: ...
    def aiRampFloat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiRampFloat: ...
    def aiRampRgb(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiRampRgb: ...
    def aiRandom(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiRandom: ...
    def aiRange(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiRange: ...
    def aiRaySwitch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiRaySwitch: ...
    def aiReadFloat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiReadFloat: ...
    def aiReadInt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiReadInt: ...
    def aiReadRGB(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiReadRGB: ...
    def aiReadRGBA(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiReadRGBA: ...
    def aiReciprocal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiReciprocal: ...
    def aiRgbToVector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiRgbToVector: ...
    def aiRgbaToFloat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiRgbaToFloat: ...
    def aiRoundCorners(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiRoundCorners: ...
    def aiSetParameter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiSetParameter: ...
    def aiSetTransform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiSetTransform: ...
    def aiShadowMatte(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiShadowMatte: ...
    def aiShuffle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiShuffle: ...
    def aiSign(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiSign: ...
    def aiSkin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiSkin: ...
    def aiSky(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiSky: ...
    def aiSkyDomeLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AiSkyDomeLight: ...
    def aiSpaceTransform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiSpaceTransform: ...
    def aiSqrt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiSqrt: ...
    def aiStandIn(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AiStandIn: ...
    def aiStandard(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiStandard: ...
    def aiStandardHair(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiStandardHair: ...
    def aiStandardSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiStandardSurface: ...
    def aiStandardVolume(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiStandardVolume: ...
    def aiStateFloat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiStateFloat: ...
    def aiStateInt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiStateInt: ...
    def aiStateVector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiStateVector: ...
    def aiStringReplace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiStringReplace: ...
    def aiSubtract(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiSubtract: ...
    def aiSwitch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiSwitch: ...
    def aiSwitchOperator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiSwitchOperator: ...
    def aiThinFilm(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiThinFilm: ...
    def aiToon(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiToon: ...
    def aiTraceSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiTraceSet: ...
    def aiTrigo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiTrigo: ...
    def aiTriplanar(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiTriplanar: ...
    def aiTwoSided(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiTwoSided: ...
    def aiUserDataBool(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiUserDataBool: ...
    def aiUserDataColor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiUserDataColor: ...
    def aiUserDataFloat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiUserDataFloat: ...
    def aiUserDataInt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiUserDataInt: ...
    def aiUserDataString(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiUserDataString: ...
    def aiUserDataVec2(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiUserDataVec2: ...
    def aiUserDataVector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiUserDataVector: ...
    def aiUtility(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiUtility: ...
    def aiUvProjection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiUvProjection: ...
    def aiUvTransform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiUvTransform: ...
    def aiVectorMap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiVectorMap: ...
    def aiVectorToRgb(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiVectorToRgb: ...
    def aiVolume(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AiVolume: ...
    def aiVolumeCollector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiVolumeCollector: ...
    def aiVolumeSampleFloat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiVolumeSampleFloat: ...
    def aiVolumeSampleRgb(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiVolumeSampleRgb: ...
    def aiWireframe(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiWireframe: ...
    def aiWriteColor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiWriteColor: ...
    def aiWriteFloat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiWriteFloat: ...
    def aiWriteInt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiWriteInt: ...
    def aiWriteRgba(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiWriteRgba: ...
    def aiWriteVector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AiWriteVector: ...
    def aimMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AimMatrix: ...
    def AISEnvFacade(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AISEnvFacade: ...
    def AlembicNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AlembicNode: ...
    def alignCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AlignCurve: ...
    def alignSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AlignSurface: ...
    def ambientLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AmbientLight: ...
    def and_(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NodeOperator: ...
    def angleBetween(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AngleBetween: ...
    def angleDimension(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AngleDimension: ...
    def animBlend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlend: ...
    def animBlendInOut(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendInOut: ...
    def animBlendNodeAdditive(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeAdditive: ...
    def animBlendNodeAdditiveDA(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeAdditiveDA: ...
    def animBlendNodeAdditiveDL(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeAdditiveDL: ...
    def animBlendNodeAdditiveF(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeAdditiveF: ...
    def animBlendNodeAdditiveFA(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeAdditiveFA: ...
    def animBlendNodeAdditiveFL(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeAdditiveFL: ...
    def animBlendNodeAdditiveI16(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeAdditiveI16: ...
    def animBlendNodeAdditiveI32(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeAdditiveI32: ...
    def animBlendNodeAdditiveRotation(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeAdditiveRotation: ...
    def animBlendNodeAdditiveScale(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeAdditiveScale: ...
    def animBlendNodeBoolean(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeBoolean: ...
    def animBlendNodeEnum(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeEnum: ...
    def animBlendNodeTime(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimBlendNodeTime: ...
    def animClip(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimClip: ...
    def animCurveTA(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimCurveTA: ...
    def animCurveTL(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimCurveTL: ...
    def animCurveTT(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimCurveTT: ...
    def animCurveTU(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimCurveTU: ...
    def animCurveUA(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimCurveUA: ...
    def animCurveUL(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimCurveUL: ...
    def animCurveUT(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimCurveUT: ...
    def animCurveUU(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AnimCurveUU: ...
    def animLayer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        override: bool = False,
        namespace: str | None = None,
    ) -> AnimLayer: ...
    def anisotropic(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Anisotropic: ...
    def annotationShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AnnotationShape: ...
    def aovChildCollection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AovChildCollection: ...
    def aovCollection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AovCollection: ...
    def applyAbs2FloatsOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyAbs2FloatsOverride: ...
    def applyAbs3FloatsOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyAbs3FloatsOverride: ...
    def applyAbsBoolOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyAbsBoolOverride: ...
    def applyAbsEnumOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyAbsEnumOverride: ...
    def applyAbsFloatOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyAbsFloatOverride: ...
    def applyAbsIntOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyAbsIntOverride: ...
    def applyAbsOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyAbsOverride: ...
    def applyAbsStringOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyAbsStringOverride: ...
    def applyConnectionOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyConnectionOverride: ...
    def applyOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyOverride: ...
    def applyRel2FloatsOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyRel2FloatsOverride: ...
    def applyRel3FloatsOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyRel3FloatsOverride: ...
    def applyRelFloatOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyRelFloatOverride: ...
    def applyRelIntOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyRelIntOverride: ...
    def applyRelOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ApplyRelOverride: ...
    def arcLengthDimension(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> ArcLengthDimension: ...
    def areaLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> AreaLight: ...
    def arnoldAOVChildSelector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ArnoldAOVChildSelector: ...
    def arrayMapper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ArrayMapper: ...
    def arubaTessellate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ArubaTessellate: ...
    def asin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Asin: ...
    def atan(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Atan: ...
    def atan2(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Atan2: ...
    def attachCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AttachCurve: ...
    def attachSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AttachSurface: ...
    def attrHierarchyTest(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AttrHierarchyTest: ...
    def audio(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Audio: ...
    def average(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Average: ...
    def avgCurves(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AvgCurves: ...
    def avgNurbsSurfacePoints(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AvgNurbsSurfacePoints: ...
    def avgSurfacePoints(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AvgSurfacePoints: ...
    def axisAngleToQuat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AxisAngleToQuat: ...
    def axisFromMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> AxisFromMatrix: ...
    def baseLattice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> BaseLattice: ...
    def basicSelector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BasicSelector: ...
    def bdAny_ConditionDbl(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdAnyConditionDbl: ...
    def bdAny_ConditionDblA(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdAnyConditionDblA: ...
    def bdAny_ConditionDblAMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdAnyConditionDblAMulti: ...
    def bdAny_ConditionDblL(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdAnyConditionDblL: ...
    def bdAny_ConditionDblLMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdAnyConditionDblLMulti: ...
    def bdAny_ConditionDblMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdAnyConditionDblMulti: ...
    def bdConditionDblCase_Compose(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdConditionDblCaseCompose: ...
    def bdConditionDblACase_Compose(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdConditionDblACaseCompose: ...
    def bdConditionDblAExtra_Compose(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdConditionDblAExtraCompose: ...
    def bdConditionDblExtra_Compose(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdConditionDblExtraCompose: ...
    def bdConditionDblLCase_Compose(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdConditionDblLCaseCompose: ...
    def bdConditionDblLExtra_Compose(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdConditionDblLExtraCompose: ...
    def bdDbl3_Abs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Abs: ...
    def bdDbl3_Add(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Add: ...
    def bdDbl3_AddMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3AddMulti: ...
    def bdDbl3_Average(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Average: ...
    def bdDbl3_AverageMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3AverageMulti: ...
    def bdDbl3_Clamp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Clamp: ...
    def bdDbl3_Divide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Divide: ...
    def bdDbl3_DivideMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3DivideMulti: ...
    def bdDbl3_Value(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Value: ...
    def bdDbl3_Lerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Lerp: ...
    def bdDbl3_MapRange(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3MapRange: ...
    def bdDbl3_Max(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Max: ...
    def bdDbl3_MaxMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3MaxMulti: ...
    def bdDbl3_Min(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Min: ...
    def bdDbl3_MinMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3MinMulti: ...
    def bdDbl3_Negate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Negate: ...
    def bdDbl3_Multiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Multiply: ...
    def bdDbl3_MultiplyMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3MultiplyMulti: ...
    def bdDbl3_Power(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Power: ...
    def bdDbl3_PowerMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3PowerMulti: ...
    def bdDbl3_RatioDblL3(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3RatioDblL3: ...
    def bdDbl3_Subtract(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3Subtract: ...
    def bdDbl3_SubtractMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3SubtractMulti: ...
    def bdDbl3_WeightedAverageMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3WeightedAverageMulti: ...
    def bdDbl3_WeightedSumMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDbl3WeightedSumMulti: ...
    def bdDblL_Abs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLAbs: ...
    def bdDblL_Add(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLAdd: ...
    def bdDblL_AddMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLAddMulti: ...
    def bdDblL_Average(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLAverage: ...
    def bdDblL_AverageMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLAverageMulti: ...
    def bdDblL_Clamp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLClamp: ...
    def bdDblL_Divide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLDivide: ...
    def bdDblL_DivideMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLDivideMulti: ...
    def bdDblL_Lerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLLerp: ...
    def bdDblL_MapRange(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLMapRange: ...
    def bdDblL_Max(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLMax: ...
    def bdDblL_MaxMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLMaxMulti: ...
    def bdDblL_Min(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLMin: ...
    def bdDblL_MinMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLMinMulti: ...
    def bdDblL_Multiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLMultiply: ...
    def bdDblL_MultiplyMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLMultiplyMulti: ...
    def bdDblL_Negate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLNegate: ...
    def bdDblL_RightTriangle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLRightTriangle: ...
    def bdDblL_Subtract(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLSubtract: ...
    def bdDblL_SubtractMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLSubtractMulti: ...
    def bdDblL_Value(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLValue: ...
    def bdDblL_WeightedAverageMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLWeightedAverageMulti: ...
    def bdDblL_WeightedSumMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLWeightedSumMulti: ...
    def bdDblL3_Abs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Abs: ...
    def bdDblL3_Add(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Add: ...
    def bdDblL3_AddMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3AddMulti: ...
    def bdDblL3_Average(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Average: ...
    def bdDblL3_AverageMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3AverageMulti: ...
    def bdDblL3_Clamp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Clamp: ...
    def bdDblL3_Divide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Divide: ...
    def bdDblL3_DivideMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3DivideMulti: ...
    def bdDblL3_Lerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Lerp: ...
    def bdDblL3_MapRange(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3MapRange: ...
    def bdDblL3_Max(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Max: ...
    def bdDblL3_MaxMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3MaxMulti: ...
    def bdDblL3_Min(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Min: ...
    def bdDblL3_MinMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3MinMulti: ...
    def bdDblL3_Multiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Multiply: ...
    def bdDblL3_MultiplyMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3MultiplyMulti: ...
    def bdDblL3_Negate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Negate: ...
    def bdDblL3_Subtract(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Subtract: ...
    def bdDblL3_SubtractMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3SubtractMulti: ...
    def bdDblL3_Value(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3Value: ...
    def bdDblL3_WeightedAverageMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3WeightedAverageMulti: ...
    def bdDblL3_WeightedSumMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblL3WeightedSumMulti: ...
    def bdDblA_Abs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAAbs: ...
    def bdDblA_Add(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAAdd: ...
    def bdDblA_AddMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAAddMulti: ...
    def bdDblA_Average(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAAverage: ...
    def bdDblA_AverageMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAAverageMulti: ...
    def bdDblA_Clamp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAClamp: ...
    def bdDblA_Divide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblADivide: ...
    def bdDblA_DivideMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblADivideMulti: ...
    def bdDblA_Lerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblALerp: ...
    def bdDblA_LerpShortest(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblALerpShortest: ...
    def bdDblA_MapRange(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAMapRange: ...
    def bdDblA_Max(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAMax: ...
    def bdDblA_MaxMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAMaxMulti: ...
    def bdDblA_Min(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAMin: ...
    def bdDblA_MinMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAMinMulti: ...
    def bdDblA_Multiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAMultiply: ...
    def bdDblA_MultiplyMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAMultiplyMulti: ...
    def bdDblA_Negate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblANegate: ...
    def bdDblA_ShortestDelta(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAShortestDelta: ...
    def bdDblA_Subtract(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblASubtract: ...
    def bdDblA_SubtractMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblASubtractMulti: ...
    def bdDblA_Value(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAValue: ...
    def bdDblA_WeightedAverageMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAWeightedAverageMulti: ...
    def bdDblA_WeightedSumMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAWeightedSumMulti: ...
    def bdDblA_Wrap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAWrap: ...
    def bdDbl_Abs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAbs: ...
    def bdDbl_Add(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAdd: ...
    def bdDbl_AddMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAddMulti: ...
    def bdDbl_Average(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAverage: ...
    def bdDbl_AverageMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblAverageMulti: ...
    def bdDbl_Clamp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblClamp: ...
    def bdDbl_Divide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblDivide: ...
    def bdDbl_DivideMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblDivideMulti: ...
    def bdDbl_Value(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblValue: ...
    def bdDbl_Lerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblLerp: ...
    def bdDbl_MapRange(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblMapRange: ...
    def bdDbl_Max(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblMax: ...
    def bdDbl_MaxMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblMaxMulti: ...
    def bdDbl_Min(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblMin: ...
    def bdDbl_MinMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblMinMulti: ...
    def bdDbl_Negate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblNegate: ...
    def bdDbl_Multiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblMultiply: ...
    def bdDbl_MultiplyMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblMultiplyMulti: ...
    def bdDbl_Power(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblPower: ...
    def bdDbl_PowerMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblPowerMulti: ...
    def bdDbl_RatioDblL(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblRatioDblL: ...
    def bdDbl_RatioDblA(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblRatioDblA: ...
    def bdDbl_Subtract(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblSubtract: ...
    def bdDbl_SubtractMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblSubtractMulti: ...
    def bdDbl_WeightedAverageMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblWeightedAverageMulti: ...
    def bdDbl_WeightedSumMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdDblWeightedSumMulti: ...
    def bdEuler_ComposeBendTwist(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdEulerComposeBendTwist: ...
    def bdEuler_DecomposeBendTwist(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdEulerDecomposeBendTwist: ...
    def bdEuler_DecomposeTwist(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdEulerDecomposeTwist: ...
    def bdEuler_LimitBendTwist(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdEulerLimitBendTwist: ...
    def bdEuler_Value(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdEulerValue: ...
    def bdQuat_ChangeBasis(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdQuatChangeBasis: ...
    def bdQuat_ComposeBendTwist(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdQuatComposeBendTwist: ...
    def bdQuat_DecomposeBendTwist(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdQuatDecomposeBendTwist: ...
    def bdQuat_DecomposeTwist(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdQuatDecomposeTwist: ...
    def bdQuat_LimitBendTwist(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdQuatLimitBendTwist: ...
    def bdQuat_MultiplyMulti(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdQuatMultiplyMulti: ...
    def bdQuat_Value(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdQuatValue: ...
    def bdRbf_BendTwistFalloffWeight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfBendTwistFalloffWeight: ...
    def bdRbf_MultiBendTwistFalloffWeight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfMultiBendTwistFalloffWeight: ...
    def bdRbf_MultiOrientationFalloffWeight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfMultiOrientationFalloffWeight: ...
    def bdRbf_MultiOrientationWeight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfMultiOrientationWeight: ...
    def bdRbf_MultiPositionFalloffWeight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfMultiPositionFalloffWeight: ...
    def bdRbf_MultiPositionWeight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfMultiPositionWeight: ...
    def bdRbf_PoseBlend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfPoseBlend: ...
    def bdRbf_OrientationFalloffWeight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfOrientationFalloffWeight: ...
    def bdRbf_OrientationWeight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfOrientationWeight: ...
    def bdRbf_PositionFalloffWeight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfPositionFalloffWeight: ...
    def bdRbf_PositionWeight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BdRbfPositionWeight: ...
    def bevel(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Bevel: ...
    def bevelPlus(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BevelPlus: ...
    def bezierCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> BezierCurve: ...
    def bezierCurveToNurbs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BezierCurveToNurbs: ...
    def bifrostBoard(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BifrostBoard: ...
    def bifrostGeoToMaya(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BifrostGeoToMaya: ...
    def blendColorSets(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BlendColorSets: ...
    def blendColors(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BlendColors: ...
    def blendDevice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BlendDevice: ...
    def blendFalloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BlendFalloff: ...
    def blendMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BlendMatrix: ...
    def blendShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BlendShape: ...
    def blendTwoAttr(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BlendTwoAttr: ...
    def blendWeighted(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BlendWeighted: ...
    def blindDataTemplate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BlindDataTemplate: ...
    def blinn(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Blinn: ...
    def boneLattice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> BoneLattice: ...
    def boolean(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Boolean: ...
    def boundary(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Boundary: ...
    def brownian(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Brownian: ...
    def brush(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Brush: ...
    def bulge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Bulge: ...
    def bump2d(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Bump2d: ...
    def bump3d(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Bump3d: ...
    def cMuscleCreator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CMuscleCreator: ...
    def cMuscleMultiCollide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CMuscleMultiCollide: ...
    def cMuscleRelative(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CMuscleRelative: ...
    def cMuscleShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CMuscleShader: ...
    def cMuscleSmartConstraint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CMuscleSmartConstraint: ...
    def cMuscleSplineDeformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CMuscleSplineDeformer: ...
    def cMuscleStretch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CMuscleStretch: ...
    def cMuscleSystem(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CMuscleSystem: ...
    def cacheBlend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CacheBlend: ...
    def cacheFile(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CacheFile: ...
    def camera(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> Camera: ...
    def cameraSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CameraSet: ...
    def cameraView(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CameraView: ...
    def ceil(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Ceil: ...
    def channels(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Channels: ...
    def character(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Character: ...
    def characterMap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CharacterMap: ...
    def characterOffset(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CharacterOffset: ...
    def checker(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Checker: ...
    def childNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ChildNode: ...
    def choice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Choice: ...
    def chooser(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Chooser: ...
    def clamp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Clamp: ...
    def clampRange(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ClampRange: ...
    def clipLibrary(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ClipLibrary: ...
    def clipScheduler(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ClipScheduler: ...
    def clipToGhostData(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ClipToGhostData: ...
    def closeCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CloseCurve: ...
    def closeSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CloseSurface: ...
    def closestPointOnMesh(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ClosestPointOnMesh: ...
    def closestPointOnSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ClosestPointOnSurface: ...
    def cloth(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Cloth: ...
    def cloud(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Cloud: ...
    def cluster(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Cluster: ...
    def clusterFlexorShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> ClusterFlexorShape: ...
    def clusterHandle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> ClusterHandle: ...
    def collection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Collection: ...
    def colorComposite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ColorComposite: ...
    def colorCondition(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ColorCondition: ...
    def colorConstant(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ColorConstant: ...
    def colorCorrect(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ColorCorrect: ...
    def colorLogic(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ColorLogic: ...
    def colorManagementGlobals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ColorManagementGlobals: ...
    def colorMask(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ColorMask: ...
    def colorMath(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ColorMath: ...
    def colorProfile(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ColorProfile: ...
    def columnFromMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ColumnFromMatrix: ...
    def combinationShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CombinationShape: ...
    def compactPlugArrayTest(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CompactPlugArrayTest: ...
    def componentFalloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ComponentFalloff: ...
    def componentMatch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ComponentMatch: ...
    def componentTagBase(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ComponentTagBase: ...
    def composeMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ComposeMatrix: ...
    def ComputeGlobal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ComputeGlobal: ...
    def ComputeLocal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ComputeLocal: ...
    def condition(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Condition: ...
    def connectionOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ConnectionOverride: ...
    def connectionUniqueOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ConnectionUniqueOverride: ...
    def container(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Container: ...
    def containerBase(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ContainerBase: ...
    def contrast(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Contrast: ...
    def controller(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Controller: ...
    def copyColorSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CopyColorSet: ...
    def copyUVSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CopyUVSet: ...
    def cos(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Cos: ...
    def cpvColor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CpvColor: ...
    def crater(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Crater: ...
    def creaseSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CreaseSet: ...
    def createColorSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CreateColorSet: ...
    def createPtexUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CreatePtexUV: ...
    def createUVSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CreateUVSet: ...
    def crossProduct(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CrossProduct: ...
    def cryptomatte(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Cryptomatte: ...
    def curveFromMeshCoM(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveFromMeshCoM: ...
    def curveFromMeshEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveFromMeshEdge: ...
    def curveFromSubdivEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveFromSubdivEdge: ...
    def curveFromSubdivFace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveFromSubdivFace: ...
    def curveFromSurfaceBnd(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveFromSurfaceBnd: ...
    def curveFromSurfaceCoS(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveFromSurfaceCoS: ...
    def curveFromSurfaceIso(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveFromSurfaceIso: ...
    def curveInfo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveInfo: ...
    def curveIntersect(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveIntersect: ...
    def curveNormalizerAngle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveNormalizerAngle: ...
    def curveNormalizerLinear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveNormalizerLinear: ...
    def curveWarp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CurveWarp: ...
    def CustomRigDefaultMappingNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CustomRigDefaultMappingNode: ...
    def CustomRigRetargeterNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> CustomRigRetargeterNode: ...
    def dagPose(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DagPose: ...
    def dataBlockTest(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DataBlockTest: ...
    def decomposeMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DecomposeMatrix: ...
    def defaultLightList(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DefaultLightList: ...
    def defaultRenderUtilityList(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DefaultRenderUtilityList: ...
    def defaultRenderingList(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DefaultRenderingList: ...
    def defaultShaderList(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DefaultShaderList: ...
    def defaultTextureList(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DefaultTextureList: ...
    def deleteColorSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DeleteColorSet: ...
    def deleteComponent(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DeleteComponent: ...
    def deleteUVSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DeleteUVSet: ...
    def deltaMush(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DeltaMush: ...
    def deformBend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DeformBend: ...
    def deformFlare(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DeformFlare: ...
    def deformSine(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DeformSine: ...
    def deformSquash(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DeformSquash: ...
    def deformTwist(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DeformTwist: ...
    def deformWave(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DeformWave: ...
    def detachCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DetachCurve: ...
    def detachSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DetachSurface: ...
    def determinant(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Determinant: ...
    def directedDisc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DirectedDisc: ...
    def directionalLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DirectionalLight: ...
    def diskCache(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DiskCache: ...
    def displacementShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DisplacementShader: ...
    def displayLayer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DisplayLayer: ...
    def displayLayerManager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DisplayLayerManager: ...
    def distanceBetween(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DistanceBetween: ...
    def distanceDimShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DistanceDimShape: ...
    def divide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Divide: ...
    def dof(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Dof: ...
    def dotProduct(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DotProduct: ...
    def doubleShadingSwitch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DoubleShadingSwitch: ...
    def dpBirailSrf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DpBirailSrf: ...
    def dropoffLocator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DropoffLocator: ...
    def dynamicConstraint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DynamicConstraint: ...
    def dynController(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DynController: ...
    def dynGlobals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> DynGlobals: ...
    def dynHolder(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> DynHolder: ...
    def editMetadata(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> EditMetadata: ...
    def editsManager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> EditsManager: ...
    def envBall(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> EnvBall: ...
    def envChrome(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> EnvChrome: ...
    def envCube(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> EnvCube: ...
    def envFacade(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> EnvFacade: ...
    def envFog(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> EnvFog: ...
    def environmentFog(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> EnvironmentFog: ...
    def envSky(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> EnvSky: ...
    def envSphere(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> EnvSphere: ...
    def equal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Equal: ...
    def eulerToQuat(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> EulerToQuat: ...
    def explodeNurbsShell(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ExplodeNurbsShell: ...
    def expression(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Expression: ...
    def extendCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ExtendCurve: ...
    def extendSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ExtendSurface: ...
    def extrude(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Extrude: ...
    def facade(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Facade: ...
    def falloffEval(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FalloffEval: ...
    def ffBlendSrf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FfBlendSrf: ...
    def ffBlendSrfObsolete(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FfBlendSrfObsolete: ...
    def ffFilletSrf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FfFilletSrf: ...
    def ffd(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Ffd: ...
    def file(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> File: ...
    def filletCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FilletCurve: ...
    def fitBspline(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FitBspline: ...
    def flexorShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> FlexorShape: ...
    def floatComposite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FloatComposite: ...
    def floatCondition(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FloatCondition: ...
    def floatConstant(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FloatConstant: ...
    def floatCorrect(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FloatCorrect: ...
    def floatLogic(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FloatLogic: ...
    def floatMask(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FloatMask: ...
    def floatMath(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FloatMath: ...
    def floor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Floor: ...
    def flow(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Flow: ...
    def fluidShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> FluidShape: ...
    def fluidTexture2D(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> FluidTexture2D: ...
    def fluidTexture3D(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> FluidTexture3D: ...
    def follicle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> Follicle: ...
    def fourByFourMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FourByFourMatrix: ...
    def fractal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Fractal: ...
    def frameCache(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> FrameCache: ...
    def gameFbxExporter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GameFbxExporter: ...
    def gammaCorrect(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GammaCorrect: ...
    def geoConnectable(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> GeoConnectable: ...
    def geoConnector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GeoConnector: ...
    def geomBind(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GeomBind: ...
    def geometryFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GeometryFilter: ...
    def globalCacheControl(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GlobalCacheControl: ...
    def globalStitch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GlobalStitch: ...
    def granite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Granite: ...
    def greasePencilSequence(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GreasePencilSequence: ...
    def greasePlane(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> GreasePlane: ...
    def greasePlaneRenderShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> GreasePlaneRenderShape: ...
    def greaterThan(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GreaterThan: ...
    def grid(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Grid: ...
    def group(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Group: ...
    def groupId(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GroupId: ...
    def groupParts(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> GroupParts: ...
    def guide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Guide: ...
    def hairConstraint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> HairConstraint: ...
    def hairSystem(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> HairSystem: ...
    def hairPhysicalShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HairPhysicalShader: ...
    def hairTubeShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HairTubeShader: ...
    def hardenPoint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HardenPoint: ...
    def hardwareRenderGlobals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HardwareRenderGlobals: ...
    def hardwareRenderingGlobals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HardwareRenderingGlobals: ...
    def heightField(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> HeightField: ...
    def hierarchyTestNode1(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HierarchyTestNode1: ...
    def hierarchyTestNode2(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HierarchyTestNode2: ...
    def hierarchyTestNode3(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HierarchyTestNode3: ...
    def hierarchyTestNode4(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HierarchyTestNode4: ...
    def HIKCharacterNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKCharacterNode: ...
    def HIKCharacterStateClient(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKCharacterStateClient: ...
    def HIKControlSetNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKControlSetNode: ...
    def HIKEffector2State(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKEffector2State: ...
    def HIKEffectorFromCharacter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKEffectorFromCharacter: ...
    def HIKPinning2State(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKPinning2State: ...
    def HIKProperty2State(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKProperty2State: ...
    def HIKRetargeterNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKRetargeterNode: ...
    def HIKSkeletonGeneratorNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKSkeletonGeneratorNode: ...
    def hikFloorContactMarker(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> HikFloorContactMarker: ...
    def hikSolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HikSolver: ...
    def HIKSolverNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKSolverNode: ...
    def HIKState2Effector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKState2Effector: ...
    def HIKState2FK(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKState2FK: ...
    def HIKState2GlobalSK(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKState2GlobalSK: ...
    def HIKState2SK(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKState2SK: ...
    def HIKFK2State(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKFK2State: ...
    def HIKSK2State(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HIKSK2State: ...
    def historySwitch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HistorySwitch: ...
    def holdMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HoldMatrix: ...
    def hsvToRgb(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HsvToRgb: ...
    def hwReflectionMap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HwReflectionMap: ...
    def hwRenderGlobals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HwRenderGlobals: ...
    def hyperGraphInfo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HyperGraphInfo: ...
    def hyperLayout(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HyperLayout: ...
    def hyperView(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> HyperView: ...
    def ik2Bsolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Ik2Bsolver: ...
    def ikMCsolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> IkMCsolver: ...
    def ikPASolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> IkPASolver: ...
    def ikRPsolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> IkRPsolver: ...
    def ikSCsolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> IkSCsolver: ...
    def ikSplineSolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> IkSplineSolver: ...
    def ikSpringSolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> IkSpringSolver: ...
    def ikSystem(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> IkSystem: ...
    def imagePlane(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> ImagePlane: ...
    def implicitBox(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> ImplicitBox: ...
    def implicitCone(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> ImplicitCone: ...
    def implicitSphere(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> ImplicitSphere: ...
    def insertKnotCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> InsertKnotCurve: ...
    def insertKnotSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> InsertKnotSurface: ...
    def intersectSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> IntersectSurface: ...
    def inverseLerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> InverseLerp: ...
    def inverseMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> InverseMatrix: ...
    def jiggle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Jiggle: ...
    def joint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform | None = None,
        namespace: str | None = None,
    ) -> Joint: ...
    def jointCluster(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> JointCluster: ...
    def jointFfd(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> JointFfd: ...
    def jointLattice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> JointLattice: ...
    def keyingGroup(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> KeyingGroup: ...
    def lambert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Lambert: ...
    def lattice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> Lattice: ...
    def layeredShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LayeredShader: ...
    def layeredTexture(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LayeredTexture: ...
    def leastSquaresModifier(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LeastSquaresModifier: ...
    def leather(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Leather: ...
    def length(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Length: ...
    def lerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Lerp: ...
    def lessThan(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LessThan: ...
    def lightEditor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightEditor: ...
    def lightFog(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightFog: ...
    def lightGroup(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightGroup: ...
    def lightInfo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightInfo: ...
    def lightItem(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightItem: ...
    def lightItemBase(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightItemBase: ...
    def lightLinker(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightLinker: ...
    def lightList(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightList: ...
    def lightsChildCollection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightsChildCollection: ...
    def lightsCollection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightsCollection: ...
    def lightsCollectionSelector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LightsCollectionSelector: ...
    def lineModifier(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> LineModifier: ...
    def listItem(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ListItem: ...
    def locator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> Locator: ...
    def lodThresholds(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> LodThresholds: ...
    def loft(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Loft: ...
    def log(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Log: ...
    def luminance(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Luminance: ...
    def makeGroup(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeGroup: ...
    def makeIllustratorCurves(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeIllustratorCurves: ...
    def makeNurbCircle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeNurbCircle: ...
    def makeNurbCone(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeNurbCone: ...
    def makeNurbCube(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeNurbCube: ...
    def makeNurbCylinder(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeNurbCylinder: ...
    def makeNurbPlane(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeNurbPlane: ...
    def makeNurbSphere(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeNurbSphere: ...
    def makeNurbTorus(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeNurbTorus: ...
    def makeNurbsSquare(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeNurbsSquare: ...
    def makeTextCurves(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeTextCurves: ...
    def makeThreePointCircularArc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeThreePointCircularArc: ...
    def makeTwoPointCircularArc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MakeTwoPointCircularArc: ...
    def mandelbrot(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Mandelbrot: ...
    def mandelbrot3D(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Mandelbrot3D: ...
    def marble(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Marble: ...
    def MASH_Audio(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHAudio: ...
    def MASH_BaseNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHBaseNode: ...
    def MASH_Blend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHBlend: ...
    def MASH_BlendDeformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHBlendDeformer: ...
    def MASH_Breakout(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHBreakout: ...
    def MASH_ChannelRandom(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHChannelRandom: ...
    def MASH_Color(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHColor: ...
    def MASH_Constraint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHConstraint: ...
    def MASH_Curve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHCurve: ...
    def MASH_Deformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHDeformer: ...
    def MASH_Delay(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHDelay: ...
    def MASH_Distribute(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHDistribute: ...
    def MASH_Dynamics(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHDynamics: ...
    def MASH_DynamicsInitialState(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHDynamicsInitialState: ...
    def MASH_Explode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHExplode: ...
    def MASH_Id(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHId: ...
    def MASH_Influence(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHInfluence: ...
    def MASH_Inherit(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHInherit: ...
    def MASH_InitialState(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHInitialState: ...
    def MASH_Jiggle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHJiggle: ...
    def MASH_Legacy(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHLegacy: ...
    def MASH_Maths(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHMaths: ...
    def MASH_MultiCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHMultiCurve: ...
    def MASH_Mute(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHMute: ...
    def MASH_Noise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHNoise: ...
    def MASH_Offset(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHOffset: ...
    def MASH_Orient(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHOrient: ...
    def MASH_PfxConnect(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHPfxConnect: ...
    def MASH_Placer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHPlacer: ...
    def MASH_PointToCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHPointToCurve: ...
    def MASH_Python(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHPython: ...
    def MASH_Random(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHRandom: ...
    def MASH_Replicator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHReplicator: ...
    def MASH_Repro(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHRepro: ...
    def MASH_ShellDeformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHShellDeformer: ...
    def MASH_Signal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHSignal: ...
    def MASH_Spring(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHSpring: ...
    def MASH_Strength(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHStrength: ...
    def MASH_Symmetry(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHSymmetry: ...
    def MASH_Time(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHTime: ...
    def MASH_Trails(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHTrails: ...
    def MASH_Transform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHTransform: ...
    def MASH_Trig(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHTrig: ...
    def MASH_Visibility(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHVisibility: ...
    def MASH_Waiter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHWaiter: ...
    def MASH_World(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MASHWorld: ...
    def materialFacade(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MaterialFacade: ...
    def materialInfo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MaterialInfo: ...
    def materialOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MaterialOverride: ...
    def materialTemplate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MaterialTemplate: ...
    def materialTemplateOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MaterialTemplateOverride: ...
    def materialXMaterial(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MaterialXMaterial: ...
    def MaterialXSurfaceShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MaterialXSurfaceShader: ...
    def max(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Max: ...
    def mayaUsdGeomNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MayaUsdGeomNode: ...
    def mayaUsdLayerManager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MayaUsdLayerManager: ...
    def mayaUsdProxyShapeListener(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MayaUsdProxyShapeListener: ...
    def mayaUsdProxyShapeListenerBase(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MayaUsdProxyShapeListenerBase: ...
    def membrane(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Membrane: ...
    def mesh(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> Mesh: ...
    def min(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Min: ...
    def modulo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Modulo: ...
    def morph(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Morph: ...
    def motionPath(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MotionPath: ...
    def motionTrail(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MotionTrail: ...
    def motionTrailShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> MotionTrailShape: ...
    def mountain(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Mountain: ...
    def movie(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Movie: ...
    def mpBirailSrf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MpBirailSrf: ...
    def multDoubleLinear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MultDoubleLinear: ...
    def multMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MultMatrix: ...
    def multilisterLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MultilisterLight: ...
    def multiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Multiply: ...
    def multiplyDivide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MultiplyDivide: ...
    def multiplyPointByMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MultiplyPointByMatrix: ...
    def multiplyVectorByMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> MultiplyVectorByMatrix: ...
    def mute(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Mute: ...
    def nCloth(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> NCloth: ...
    def nComponent(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NComponent: ...
    def nParticle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> NParticle: ...
    def nRigid(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> NRigid: ...
    def nearestPointOnCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NearestPointOnCurve: ...
    def negate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Negate: ...
    def network(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Network: ...
    def nodeGraphEditorBookmarkInfo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NodeGraphEditorBookmarkInfo: ...
    def nodeGraphEditorBookmarks(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NodeGraphEditorBookmarks: ...
    def noise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Noise: ...
    def nonLinear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NonLinear: ...
    def normalize(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Normalize: ...
    def not_(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NodeOperator: ...
    def nurbsCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> NurbsCurve: ...
    def nurbsCurveToBezier(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NurbsCurveToBezier: ...
    def nurbsTessellate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NurbsTessellate: ...
    def nurbsSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> NurbsSurface: ...
    def nurbsToSubdiv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NurbsToSubdiv: ...
    def nurbsToSubdivProc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NurbsToSubdivProc: ...
    def objectAttrFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ObjectAttrFilter: ...
    def objectBinFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ObjectBinFilter: ...
    def objectFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ObjectFilter: ...
    def objectGrpToComp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ObjectGrpToComp: ...
    def objectMultiFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ObjectMultiFilter: ...
    def objectNameFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ObjectNameFilter: ...
    def objectRenderFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ObjectRenderFilter: ...
    def objectScriptFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ObjectScriptFilter: ...
    def objectSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ObjectSet: ...
    def objectTypeFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ObjectTypeFilter: ...
    def ocean(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Ocean: ...
    def oceanShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> OceanShader: ...
    def offsetCos(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> OffsetCos: ...
    def offsetCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> OffsetCurve: ...
    def offsetDeformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> OffsetDeformer: ...
    def offsetSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> OffsetSurface: ...
    def oldBlindDataBase(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> OldBlindDataBase: ...
    def oldGeometryConstraint(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> OldGeometryConstraint: ...
    def opticalFX(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> OpticalFX: ...
    def or_(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> NodeOperator: ...
    def orientationMarker(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> OrientationMarker: ...
    def override(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Override: ...
    def pairBlend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PairBlend: ...
    def paramDimension(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> ParamDimension: ...
    def parentMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ParentMatrix: ...
    def particle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> Particle: ...
    def particleAgeMapper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ParticleAgeMapper: ...
    def particleCloud(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ParticleCloud: ...
    def particleColorMapper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ParticleColorMapper: ...
    def particleIncandMapper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ParticleIncandMapper: ...
    def particleSamplerInfo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ParticleSamplerInfo: ...
    def particleTranspMapper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ParticleTranspMapper: ...
    def partition(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Partition: ...
    def passContributionMap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PassContributionMap: ...
    def passMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PassMatrix: ...
    def pfxHair(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> PfxHair: ...
    def pfxToon(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> PfxToon: ...
    def phong(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Phong: ...
    def phongE(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PhongE: ...
    def pi(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Pi: ...
    def pickMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PickMatrix: ...
    def place2dTexture(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Place2dTexture: ...
    def planarTrimSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PlanarTrimSurface: ...
    def plusMinusAverage(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PlusMinusAverage: ...
    def pointLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> PointLight: ...
    def pointMatrixMult(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PointMatrixMult: ...
    def pointOnCurveInfo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PointOnCurveInfo: ...
    def pointOnSurfaceInfo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PointOnSurfaceInfo: ...
    def polyAppend(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyAppend: ...
    def polyAppendVertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyAppendVertex: ...
    def polyAutoProj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyAutoProj: ...
    def polyAverageVertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyAverageVertex: ...
    def polyAxis(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyAxis: ...
    def polyBevel(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyBevel: ...
    def polyBevel2(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyBevel2: ...
    def polyBevel3(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyBevel3: ...
    def polyBevelCutback(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyBevelCutback: ...
    def polyBlindData(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyBlindData: ...
    def polyBoolOp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyBoolOp: ...
    def polyBoolean(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyBoolean: ...
    def polyBridgeEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyBridgeEdge: ...
    def polyCBoolOp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCBoolOp: ...
    def polyChipOff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyChipOff: ...
    def polyCircularize(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCircularize: ...
    def polyClean(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyClean: ...
    def polyCloseBorder(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCloseBorder: ...
    def polyCollapseEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCollapseEdge: ...
    def polyCollapseF(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCollapseF: ...
    def polyColorDel(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyColorDel: ...
    def polyColorMod(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyColorMod: ...
    def polyColorPerVertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyColorPerVertex: ...
    def polyCone(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCone: ...
    def polyConnectComponents(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyConnectComponents: ...
    def polyContourProj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyContourProj: ...
    def polyCopyUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCopyUV: ...
    def polyCrease(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCrease: ...
    def polyCreaseEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCreaseEdge: ...
    def polyCreateFace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCreateFace: ...
    def polyCube(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCube: ...
    def polyCut(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCut: ...
    def polyCylProj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCylProj: ...
    def polyCylinder(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyCylinder: ...
    def polyDelEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyDelEdge: ...
    def polyDelFacet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyDelFacet: ...
    def polyDelVertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyDelVertex: ...
    def polyDisc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyDisc: ...
    def polyDuplicateEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyDuplicateEdge: ...
    def polyEdgeToCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyEdgeToCurve: ...
    def polyEditEdgeFlow(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyEditEdgeFlow: ...
    def polyExtrudeEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyExtrudeEdge: ...
    def polyExtrudeFace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyExtrudeFace: ...
    def polyExtrudeVertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyExtrudeVertex: ...
    def polyFlipEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyFlipEdge: ...
    def polyFlipUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyFlipUV: ...
    def polyGear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyGear: ...
    def polyHelix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyHelix: ...
    def polyHoleFace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyHoleFace: ...
    def polyLayoutUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyLayoutUV: ...
    def polyMapCut(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMapCut: ...
    def polyMapDel(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMapDel: ...
    def polyMapSew(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMapSew: ...
    def polyMapSewMove(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMapSewMove: ...
    def polyMergeEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMergeEdge: ...
    def polyMergeFace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMergeFace: ...
    def polyMergeUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMergeUV: ...
    def polyMergeVert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMergeVert: ...
    def polyMirror(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMirror: ...
    def polyMoveEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMoveEdge: ...
    def polyMoveFace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMoveFace: ...
    def polyMoveFacetUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMoveFacetUV: ...
    def polyMoveUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMoveUV: ...
    def polyMoveVertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyMoveVertex: ...
    def polyNormal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyNormal: ...
    def polyNormalPerVertex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyNormalPerVertex: ...
    def polyNormalizeUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyNormalizeUV: ...
    def polyOptUvs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyOptUvs: ...
    def polyPassThru(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPassThru: ...
    def polyPinUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPinUV: ...
    def polyPipe(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPipe: ...
    def polyPlanarProj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPlanarProj: ...
    def polyPlane(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPlane: ...
    def polyPlatonic(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPlatonic: ...
    def polyPlatonicSolid(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPlatonicSolid: ...
    def polyPoke(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPoke: ...
    def polyPrimitiveMisc(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPrimitiveMisc: ...
    def polyPrism(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPrism: ...
    def polyProj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyProj: ...
    def polyProjectCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyProjectCurve: ...
    def polyPyramid(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyPyramid: ...
    def polyQuad(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyQuad: ...
    def polyReduce(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyReduce: ...
    def polyRemesh(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyRemesh: ...
    def polyRetopo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyRetopo: ...
    def polySeparate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySeparate: ...
    def polySewEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySewEdge: ...
    def polySmartExtrude(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySmartExtrude: ...
    def polySmooth(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySmooth: ...
    def polySmoothFace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySmoothFace: ...
    def polySmoothProxy(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySmoothProxy: ...
    def polySoftEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySoftEdge: ...
    def polySphProj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySphProj: ...
    def polySphere(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySphere: ...
    def polySpinEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySpinEdge: ...
    def polySplit(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySplit: ...
    def polySplitEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySplitEdge: ...
    def polySplitRing(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySplitRing: ...
    def polySplitVert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySplitVert: ...
    def polyStraightenUVBorder(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyStraightenUVBorder: ...
    def polySubdEdge(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySubdEdge: ...
    def polySubdFace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySubdFace: ...
    def polySuperShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolySuperShape: ...
    def polyToSubdiv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyToSubdiv: ...
    def polyTorus(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyTorus: ...
    def polyTransfer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyTransfer: ...
    def polyTriangulate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyTriangulate: ...
    def polyTweak(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyTweak: ...
    def polyTweakUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyTweakUV: ...
    def polyUnite(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyUnite: ...
    def polyUnsmooth(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyUnsmooth: ...
    def polyUVRectangle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyUVRectangle: ...
    def polyWedgeFace(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PolyWedgeFace: ...
    def poseInterpolatorManager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PoseInterpolatorManager: ...
    def positionMarker(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> PositionMarker: ...
    def postProcessList(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PostProcessList: ...
    def power(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Power: ...
    def precompExport(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PrecompExport: ...
    def premultiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Premultiply: ...
    def projectCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ProjectCurve: ...
    def projectTangent(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ProjectTangent: ...
    def projection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Projection: ...
    def proximityFalloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ProximityFalloff: ...
    def proximityPin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ProximityPin: ...
    def proximityWrap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ProximityWrap: ...
    def proxyManager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ProxyManager: ...
    def psdFileTex(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PsdFileTex: ...
    def pxrUsdPointBasedDeformerNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PxrUsdPointBasedDeformerNode: ...
    def pxrUsdStageNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> PxrUsdStageNode: ...
    def quadShadingSwitch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuadShadingSwitch: ...
    def quatAdd(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuatAdd: ...
    def quatConjugate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuatConjugate: ...
    def quatInvert(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuatInvert: ...
    def quatNegate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuatNegate: ...
    def quatNormalize(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuatNormalize: ...
    def quatProd(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuatProd: ...
    def quatSlerp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuatSlerp: ...
    def quatSub(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuatSub: ...
    def quatToAxisAngle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuatToAxisAngle: ...
    def quatToEuler(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> QuatToEuler: ...
    def RScontainer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RScontainer: ...
    def ramp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Ramp: ...
    def rampShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RampShader: ...
    def rbfSrf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RbfSrf: ...
    def rebuildCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RebuildCurve: ...
    def rebuildSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RebuildSurface: ...
    def record(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Record: ...
    def reference(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Reference: ...
    def relOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RelOverride: ...
    def relUniqueOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RelUniqueOverride: ...
    def remapColor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RemapColor: ...
    def remapHsv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RemapHsv: ...
    def remapValue(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RemapValue: ...
    def renderBox(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> RenderBox: ...
    def renderCone(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> RenderCone: ...
    def renderGlobals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderGlobals: ...
    def renderGlobalsList(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderGlobalsList: ...
    def renderLayer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderLayer: ...
    def renderLayerManager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderLayerManager: ...
    def renderPass(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderPass: ...
    def renderPassSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderPassSet: ...
    def renderQuality(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderQuality: ...
    def renderRect(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> RenderRect: ...
    def renderSettingsChildCollection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderSettingsChildCollection: ...
    def renderSettingsCollection(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderSettingsCollection: ...
    def renderSetup(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderSetup: ...
    def renderSetupLayer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderSetupLayer: ...
    def renderSphere(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> RenderSphere: ...
    def renderTarget(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderTarget: ...
    def renderedImageSource(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RenderedImageSource: ...
    def reorderUVSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ReorderUVSet: ...
    def resolution(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Resolution: ...
    def resultCurveTimeToAngular(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ResultCurveTimeToAngular: ...
    def resultCurveTimeToLinear(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ResultCurveTimeToLinear: ...
    def resultCurveTimeToTime(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ResultCurveTimeToTime: ...
    def resultCurveTimeToUnitless(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ResultCurveTimeToUnitless: ...
    def reverse(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Reverse: ...
    def reverseCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ReverseCurve: ...
    def reverseSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ReverseSurface: ...
    def revolve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Revolve: ...
    def rgbToHsv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RgbToHsv: ...
    def rigidBody(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> RigidBody: ...
    def rigidSolver(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RigidSolver: ...
    def rock(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Rock: ...
    def rotateHelper(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RotateHelper: ...
    def rotateVector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RotateVector: ...
    def rotationFromMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RotationFromMatrix: ...
    def round(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Round: ...
    def roundConstantRadius(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RoundConstantRadius: ...
    def rowFromMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> RowFromMatrix: ...
    def sampler(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Sampler: ...
    def samplerInfo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SamplerInfo: ...
    def scaleFromMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ScaleFromMatrix: ...
    def script(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Script: ...
    def sculpt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Sculpt: ...
    def selectionListOperator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SelectionListOperator: ...
    def selector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Selector: ...
    def sequenceManager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SequenceManager: ...
    def sequencer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Sequencer: ...
    def setRange(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SetRange: ...
    def shaderGlow(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ShaderGlow: ...
    def shaderOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ShaderOverride: ...
    def shadingEngine(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ShadingEngine: ...
    def shadingMap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ShadingMap: ...
    def shapeEditorManager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ShapeEditorManager: ...
    def shellDeformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ShellDeformer: ...
    def shellTessellate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ShellTessellate: ...
    def shot(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Shot: ...
    def shrinkWrap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ShrinkWrap: ...
    def simpleSelector(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SimpleSelector: ...
    def simpleTestNode(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SimpleTestNode: ...
    def simpleVolumeShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SimpleVolumeShader: ...
    def simplexNoise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SimplexNoise: ...
    def sin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Sin: ...
    def singleShadingSwitch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SingleShadingSwitch: ...
    def sketchPlane(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> SketchPlane: ...
    def skinBinding(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SkinBinding: ...
    def skinCluster(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SkinCluster: ...
    def smoothCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SmoothCurve: ...
    def smoothStep(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SmoothStep: ...
    def smoothTangentSrf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SmoothTangentSrf: ...
    def snapshot(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Snapshot: ...
    def snapshotShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> SnapshotShape: ...
    def snow(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Snow: ...
    def softMod(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SoftMod: ...
    def softModHandle(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> SoftModHandle: ...
    def solidFractal(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SolidFractal: ...
    def solidify(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Solidify: ...
    def spBirailSrf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SpBirailSrf: ...
    def spotLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> SpotLight: ...
    def spring(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> Spring: ...
    def squareSrf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SquareSrf: ...
    def standardSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> StandardSurface: ...
    def stencil(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Stencil: ...
    def stereoRigCamera(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> StereoRigCamera: ...
    def stitchAsNurbsShell(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> StitchAsNurbsShell: ...
    def stitchSrf(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> StitchSrf: ...
    def stroke(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> Stroke: ...
    def strokeGlobals(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> StrokeGlobals: ...
    def stucco(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Stucco: ...
    def styleCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> StyleCurve: ...
    def subCurve(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubCurve: ...
    def subSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubSurface: ...
    def subdAddTopology(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdAddTopology: ...
    def subdAutoProj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdAutoProj: ...
    def subdBlindData(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdBlindData: ...
    def subdCleanTopology(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdCleanTopology: ...
    def subdHierBlind(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdHierBlind: ...
    def subdLayoutUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdLayoutUV: ...
    def subdMapCut(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdMapCut: ...
    def subdMapSewMove(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdMapSewMove: ...
    def subdPlanarProj(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdPlanarProj: ...
    def subdTweak(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdTweak: ...
    def subdTweakUV(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdTweakUV: ...
    def subdiv(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> Subdiv: ...
    def subdivCollapse(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdivCollapse: ...
    def subdivComponentId(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdivComponentId: ...
    def subdivReverseFaces(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdivReverseFaces: ...
    def subdivToNurbs(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdivToNurbs: ...
    def subdivToPoly(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubdivToPoly: ...
    def subsetFalloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SubsetFalloff: ...
    def subtract(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Subtract: ...
    def sum(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Sum: ...
    def surfaceInfo(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SurfaceInfo: ...
    def surfaceLuminance(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SurfaceLuminance: ...
    def surfaceShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SurfaceShader: ...
    def svgToPoly(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SvgToPoly: ...
    def sweepMeshCreator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SweepMeshCreator: ...
    def sweepProfileConverter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> SweepProfileConverter: ...
    def tan(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Tan: ...
    def tension(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Tension: ...
    def texLattice(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TexLattice: ...
    def textureBakeSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TextureBakeSet: ...
    def textureDeformer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TextureDeformer: ...
    def textureToGeom(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TextureToGeom: ...
    def time(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Time: ...
    def timeEditor(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TimeEditor: ...
    def timeEditorAnimSource(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TimeEditorAnimSource: ...
    def timeEditorClip(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TimeEditorClip: ...
    def timeEditorClipBase(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TimeEditorClipBase: ...
    def timeEditorClipEvaluator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TimeEditorClipEvaluator: ...
    def timeEditorInterpolator(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TimeEditorInterpolator: ...
    def timeEditorTracks(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TimeEditorTracks: ...
    def timeFunction(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TimeFunction: ...
    def timeToUnitConversion(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TimeToUnitConversion: ...
    def timeWarp(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TimeWarp: ...
    def toonLineAttributes(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ToonLineAttributes: ...
    def trackInfoManager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TrackInfoManager: ...
    def transferAttributes(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TransferAttributes: ...
    def transferFalloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TransferFalloff: ...
    def transform(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform | None = None,
        namespace: str | None = None,
    ) -> Transform: ...
    def transformGeometry(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TransformGeometry: ...
    def translationFromMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TranslationFromMatrix: ...
    def transposeMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TransposeMatrix: ...
    def trim(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Trim: ...
    def trimWithBoundaries(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TrimWithBoundaries: ...
    def tripleShadingSwitch(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TripleShadingSwitch: ...
    def truncate(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Truncate: ...
    def tweak(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Tweak: ...
    def type(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Type: ...
    def typeExtrude(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> TypeExtrude: ...
    def Unfold3DOptimize(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Unfold3DOptimize: ...
    def Unfold3DUnfold(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Unfold3DUnfold: ...
    def ufeProxyCameraShape(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> UfeProxyCameraShape: ...
    def uniformFalloff(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> UniformFalloff: ...
    def unitConversion(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> UnitConversion: ...
    def unitToTimeConversion(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> UnitToTimeConversion: ...
    def unknown(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Unknown: ...
    def unpremultiply(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Unpremultiply: ...
    def untrim(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Untrim: ...
    def usdPreviewSurface(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> UsdPreviewSurface: ...
    def useBackground(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> UseBackground: ...
    def uvChooser(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> UvChooser: ...
    def uvPin(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> UvPin: ...
    def valueOverride(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ValueOverride: ...
    def vectorAdjust(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> VectorAdjust: ...
    def vectorExtrude(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> VectorExtrude: ...
    def vectorProduct(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> VectorProduct: ...
    def vertexBakeSet(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> VertexBakeSet: ...
    def viewColorManager(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> ViewColorManager: ...
    def volumeFog(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> VolumeFog: ...
    def volumeLight(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: Transform,
        namespace: str | None = None,
    ) -> VolumeLight: ...
    def volumeNoise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> VolumeNoise: ...
    def volumeShader(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> VolumeShader: ...
    def water(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Water: ...
    def weightGeometryFilter(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> WeightGeometryFilter: ...
    def wire(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Wire: ...
    def wood(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Wood: ...
    def wrap(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> Wrap: ...
    def wtAddMatrix(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> WtAddMatrix: ...
    def xgmCurveToSpline(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmCurveToSpline: ...
    def xgmHairMapping(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmHairMapping: ...
    def xgmMakeGuide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmMakeGuide: ...
    def xgmModifierBase(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmModifierBase: ...
    def xgmModifierClump(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmModifierClump: ...
    def xgmModifierCollision(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmModifierCollision: ...
    def xgmModifierCut(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmModifierCut: ...
    def xgmModifierDisplacement(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmModifierDisplacement: ...
    def xgmModifierGuide(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmModifierGuide: ...
    def xgmModifierLinearWire(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmModifierLinearWire: ...
    def xgmModifierNoise(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmModifierNoise: ...
    def xgmModifierScale(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmModifierScale: ...
    def xgmModifierSculpt(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmModifierSculpt: ...
    def xgmSeExpr(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmSeExpr: ...
    def xgmSplineBase(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmSplineBase: ...
    def xgmSplineCache(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        namespace: str | None = None,
    ) -> XgmSplineCache: ...
