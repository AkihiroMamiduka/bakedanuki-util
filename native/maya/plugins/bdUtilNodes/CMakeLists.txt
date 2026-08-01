add_library(
    bdUtilNodes
    SHARED
    src/BdDoubleAddNode.cpp
    src/BdDoubleAddMultiNode.cpp
    src/BdDouble3AddNode.cpp
    src/BdDouble3AddMultiNode.cpp
    src/BdDoubleMultNode.cpp
    src/BdDoubleMultMultiNode.cpp
    src/BdDouble3MultNode.cpp
    src/BdDouble3MultMultiNode.cpp
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
