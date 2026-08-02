add_library(
    bdUtilNodes
    SHARED
    src/BdDblAddNode.cpp
    src/BdDblAddMultiNode.cpp
    src/BdDbl3AddNode.cpp
    src/BdDbl3AddMultiNode.cpp
    src/BdDblMultNode.cpp
    src/BdDblMultMultiNode.cpp
    src/BdDbl3MultNode.cpp
    src/BdDbl3MultMultiNode.cpp
    src/BdDblSubNode.cpp
    src/BdDblSubMultiNode.cpp
    src/BdDbl3SubNode.cpp
    src/BdDbl3SubMultiNode.cpp
    src/BdDblDivNode.cpp
    src/BdDblDivMultiNode.cpp
    src/BdDbl3DivNode.cpp
    src/BdDbl3DivMultiNode.cpp
    src/BdDblPowNode.cpp
    src/BdDblPowMultiNode.cpp
    src/BdDbl3PowNode.cpp
    src/BdDbl3PowMultiNode.cpp
    src/BdDblLerpNode.cpp
    src/BdDbl3LerpNode.cpp
    src/BdDblWtAddMultiNode.cpp
    src/BdDbl3WtAddMultiNode.cpp
    src/BdDblMinNode.cpp
    src/BdDblMinMultiNode.cpp
    src/BdDbl3MinNode.cpp
    src/BdDbl3MinMultiNode.cpp
    src/BdDblMaxNode.cpp
    src/BdDblMaxMultiNode.cpp
    src/BdDbl3MaxNode.cpp
    src/BdDbl3MaxMultiNode.cpp
    src/BdDblClampNode.cpp
    src/BdDbl3ClampNode.cpp
    src/BdDblMapRangeNode.cpp
    src/BdDbl3MapRangeNode.cpp
    src/BdDblAbsNode.cpp
    src/BdDbl3AbsNode.cpp
    src/BdDblValueNode.cpp
    src/BdDbl3ValueNode.cpp
    src/Double3Attribute.cpp
    src/NumericAttribute.cpp
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
