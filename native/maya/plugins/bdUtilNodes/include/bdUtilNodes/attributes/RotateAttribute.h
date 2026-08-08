#pragma once

#include <maya/MStatus.h>

class MFnNumericAttribute;
class MFnUnitAttribute;
class MObject;

namespace bd_util_nodes {

MStatus createRotateAttribute(
    MFnNumericAttribute& parentAttributeFn,
    MFnUnitAttribute& childAttributeFn,
    MObject& parent,
    MObject& childX,
    MObject& childY,
    MObject& childZ,
    const char* parentLongName,
    const char* parentShortName,
    const char* childXLongName,
    const char* childXShortName,
    const char* childYLongName,
    const char* childYShortName,
    const char* childZLongName,
    const char* childZShortName
);

}  // namespace bd_util_nodes
