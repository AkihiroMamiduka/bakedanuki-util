#pragma once

#include <maya/MEulerRotation.h>
#include <maya/MStatus.h>

class MFnEnumAttribute;
class MFnNumericAttribute;
class MFnUnitAttribute;
class MObject;

namespace bd_util_nodes {

enum class EulerRotateOrder : short {
    kXYZ = 0,
    kYZX = 1,
    kZXY = 2,
    kXZY = 3,
    kYXZ = 4,
    kZYX = 5,
};

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

MStatus createRotateOrderAttribute(
    MFnEnumAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName
);

bool toEulerRotationOrder(
    short value,
    MEulerRotation::RotationOrder& order
);

}  // namespace bd_util_nodes
