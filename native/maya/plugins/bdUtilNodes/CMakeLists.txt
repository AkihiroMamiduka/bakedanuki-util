add_library(
    bdUtilNodes
    SHARED
    src/nodes/BdDblAddNode.cpp
    src/nodes/BdDblAddMultiNode.cpp
    src/nodes/BdDbl3AddNode.cpp
    src/nodes/BdDbl3AddMultiNode.cpp
    src/nodes/BdDblMultNode.cpp
    src/nodes/BdDblMultMultiNode.cpp
    src/nodes/BdDbl3MultNode.cpp
    src/nodes/BdDbl3MultMultiNode.cpp
    src/nodes/BdDblSubNode.cpp
    src/nodes/BdDblSubMultiNode.cpp
    src/nodes/BdDbl3SubNode.cpp
    src/nodes/BdDbl3SubMultiNode.cpp
    src/nodes/BdDblDivNode.cpp
    src/nodes/BdDblDivMultiNode.cpp
    src/nodes/BdDbl3DivNode.cpp
    src/nodes/BdDbl3DivMultiNode.cpp
    src/nodes/BdDblPowNode.cpp
    src/nodes/BdDblPowMultiNode.cpp
    src/nodes/BdDbl3PowNode.cpp
    src/nodes/BdDbl3PowMultiNode.cpp
    src/nodes/BdDblLerpNode.cpp
    src/nodes/BdDbl3LerpNode.cpp
    src/nodes/BdDblWtAddMultiNode.cpp
    src/nodes/BdDbl3WtAddMultiNode.cpp
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
    src/nodes/BdDblNegNode.cpp
    src/nodes/BdDbl3NegNode.cpp
    src/nodes/BdDblValueNode.cpp
    src/nodes/BdDbl3ValueNode.cpp
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
