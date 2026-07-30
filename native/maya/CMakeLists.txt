cmake_minimum_required(VERSION 3.27.3)

project(bakedanuki_util_maya_plugins LANGUAGES CXX)

if(NOT WIN32)
    message(FATAL_ERROR "The current native Maya build supports Windows only.")
endif()

if(NOT MSVC OR MSVC_VERSION LESS 1938)
    message(
        FATAL_ERROR
        "Maya 2025 plug-ins require Visual Studio 2022 17.8.3 or later."
    )
endif()

if(NOT CMAKE_SIZEOF_VOID_P EQUAL 8)
    message(FATAL_ERROR "Maya plug-ins must be built for a 64-bit target.")
endif()

set(MAYA_VERSION "2025" CACHE STRING "Target Maya version")
set(
    MAYA_LOCATION
    "C:/Program Files/Autodesk/Maya${MAYA_VERSION}"
    CACHE PATH
    "Maya installation directory"
)

if(NOT MAYA_VERSION STREQUAL "2025")
    message(
        FATAL_ERROR
        "Only Maya 2025 is supported by the current native build."
    )
endif()

if(NOT EXISTS "${MAYA_LOCATION}/include/maya/MPxNode.h")
    message(FATAL_ERROR "Maya headers were not found under ${MAYA_LOCATION}.")
endif()

if(NOT EXISTS "${MAYA_LOCATION}/lib/OpenMaya.lib")
    message(FATAL_ERROR "OpenMaya.lib was not found under ${MAYA_LOCATION}.")
endif()

add_subdirectory(plugins/bdUtilNodes)
