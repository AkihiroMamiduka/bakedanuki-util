#include "bdUtilNodes/attributes/RotateAttribute.h"

#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MObject.h>
#include <maya/MString.h>

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
) {
    MStatus status;

    childX = childAttributeFn.create(
        childXLongName,
        childXShortName,
        MFnUnitAttribute::kAngle,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    childY = childAttributeFn.create(
        childYLongName,
        childYShortName,
        MFnUnitAttribute::kAngle,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    childZ = childAttributeFn.create(
        childZLongName,
        childZShortName,
        MFnUnitAttribute::kAngle,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    parent = parentAttributeFn.create(
        parentLongName,
        parentShortName,
        childX,
        childY,
        childZ,
        &status
    );
    return status;
}

}  // namespace bd_util_nodes
