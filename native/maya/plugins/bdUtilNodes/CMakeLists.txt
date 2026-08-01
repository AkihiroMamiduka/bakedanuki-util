add_library(
    bdUtilNodes
    SHARED
    src/BdAddDoublePairNode.cpp
    src/BdAddDoubleMultiNode.cpp
    src/BdAddDouble3PairNode.cpp
    src/BdAddDouble3MultiNode.cpp
    src/BdMultDoublePairNode.cpp
    src/BdMultDoubleMultiNode.cpp
    src/BdMultDouble3PairNode.cpp
    src/BdMultDouble3MultiNode.cpp
    src/BdSubDoublePairNode.cpp
    src/BdSubDoubleMultiNode.cpp
    src/BdSubDouble3PairNode.cpp
    src/BdSubDouble3MultiNode.cpp
    src/BdDivDoublePairNode.cpp
    src/BdDivDoubleMultiNode.cpp
    src/BdDivDouble3PairNode.cpp
    src/BdDivDouble3MultiNode.cpp
    src/BdPowDoublePairNode.cpp
    src/BdPowDoubleMultiNode.cpp
    src/BdPowDouble3PairNode.cpp
    src/BdPowDouble3MultiNode.cpp
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
