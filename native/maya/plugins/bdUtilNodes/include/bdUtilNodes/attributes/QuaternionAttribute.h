#pragma once

#include <maya/MObject.h>
#include <maya/MStatus.h>

class MFnNumericAttribute;

namespace bd_util_nodes {

MStatus createQuaternionAttribute(
    MFnNumericAttribute& attributeFn,
    MObject& parent,
    MObject& childX,
    MObject& childY,
    MObject& childZ,
    MObject& childW,
    const char* parentLongName,
    const char* parentShortName,
    const char* childXLongName,
    const char* childXShortName,
    const char* childYLongName,
    const char* childYShortName,
    const char* childZLongName,
    const char* childZShortName,
    const char* childWLongName,
    const char* childWShortName
);

}  // namespace bd_util_nodes
