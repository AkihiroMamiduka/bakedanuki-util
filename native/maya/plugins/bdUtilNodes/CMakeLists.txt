add_library(
    bdUtilNodes
    SHARED
    src/nodes/BdDblAddNode.cpp
    src/nodes/BdDblAddMultiNode.cpp
    src/nodes/BdDbl3AddNode.cpp
    src/nodes/BdDbl3AddMultiNode.cpp
    src/nodes/BdDblMultiplyNode.cpp
    src/nodes/BdDblMultiplyMultiNode.cpp
    src/nodes/BdDbl3MultiplyNode.cpp
    src/nodes/BdDbl3MultiplyMultiNode.cpp
    src/nodes/BdDblSubtractNode.cpp
    src/nodes/BdDblSubtractMultiNode.cpp
    src/nodes/BdDbl3SubtractNode.cpp
    src/nodes/BdDbl3SubtractMultiNode.cpp
    src/nodes/BdDblDivideNode.cpp
    src/nodes/BdDblDivideMultiNode.cpp
    src/nodes/BdDbl3DivideNode.cpp
    src/nodes/BdDbl3DivideMultiNode.cpp
    src/nodes/BdDblPowerNode.cpp
    src/nodes/BdDblPowerMultiNode.cpp
    src/nodes/BdDbl3PowerNode.cpp
    src/nodes/BdDbl3PowerMultiNode.cpp
    src/nodes/BdDblLerpNode.cpp
    src/nodes/BdDbl3LerpNode.cpp
    src/nodes/BdDblWeightedSumMultiNode.cpp
    src/nodes/BdDbl3WeightedSumMultiNode.cpp
    src/nodes/BdDblMinNode.cpp
    src/nodes/BdDblMinMultiNode.cpp
    src/nodes/BdDbl3MinNode.cpp
    src/nodes/BdDbl3MinMultiNode.cpp
    src/nodes/BdDblMaxNode.cpp
    src/nodes/BdDblMaxMultiNode.cpp
    src/nodes/BdDbl3MaxNode.cpp
    src/nodes/BdDbl3MaxMultiNode.cpp
    src/nodes/BdDblClampNode.cpp
    src/nodes/BdDbl3ClampNode.cpp
    src/nodes/BdDblMapRangeNode.cpp
    src/nodes/BdDbl3MapRangeNode.cpp
    src/nodes/BdDblAbsNode.cpp
    src/nodes/BdDbl3AbsNode.cpp
    src/nodes/BdDblNegateNode.cpp
    src/nodes/BdDbl3NegateNode.cpp
    src/nodes/BdDblConditionNode.cpp
    src/nodes/BdDblConditionMultiNode.cpp
    src/nodes/BdDbl3ConditionNode.cpp
    src/nodes/BdDbl3ConditionMultiNode.cpp
    src/nodes/BdDblAverageNode.cpp
    src/nodes/BdDblAverageMultiNode.cpp
    src/nodes/BdDbl3AverageNode.cpp
    src/nodes/BdDbl3AverageMultiNode.cpp
    src/nodes/BdDblValueNode.cpp
    src/nodes/BdDbl3ValueNode.cpp
    src/attributes/ComparisonAttribute.cpp
    src/attributes/Double3Attribute.cpp
    src/attributes/NumericAttribute.cpp
    src/plugin.cpp
)

target_include_directories(
    bdUtilNodes
    PRIVATE
    "${CMAKE_CURRENT_SOURCE_DIR}/include"
    "${MAYA_LOCATION}/include"
)

target_link_libraries(
    bdUtilNodes
    PRIVATE
    "${MAYA_LOCATION}/lib/Foundation.lib"
    "${MAYA_LOCATION}/lib/OpenMaya.lib"
)

target_compile_definitions(
    bdUtilNodes
    PRIVATE
    NT_PLUGIN
    REQUIRE_IOSTREAM
)

target_compile_features(bdUtilNodes PRIVATE cxx_std_17)

if(MSVC)
    target_compile_options(
        bdUtilNodes
        PRIVATE
        /EHsc
        /permissive-
        /W4
        /Zc:__cplusplus
    )
endif()

set_target_properties(
    bdUtilNodes
    PROPERTIES
    CXX_EXTENSIONS OFF
    OUTPUT_NAME "bdUtilNodes"
    PREFIX ""
    SUFFIX ".mll"
)
