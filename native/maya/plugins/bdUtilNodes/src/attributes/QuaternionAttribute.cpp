#include "bdUtilNodes/attributes/QuaternionAttribute.h"

#include <maya/MFnNumericAttribute.h>
#include <maya/MFnNumericData.h>
#include <maya/MString.h>

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
) {
    MStatus status;

    childX = attributeFn.create(
        childXLongName,
        childXShortName,
        MFnNumericData::kDouble,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    childY = attributeFn.create(
        childYLongName,
        childYShortName,
        MFnNumericData::kDouble,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    childZ = attributeFn.create(
        childZLongName,
        childZShortName,
        MFnNumericData::kDouble,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    childW = attributeFn.create(
        childWLongName,
        childWShortName,
        MFnNumericData::kDouble,
        1.0,
        &status
    );
    if (!status) {
        return status;
    }

    parent = attributeFn.create(
        parentLongName,
        parentShortName,
        childX,
        childY,
        childZ,
        childW,
        &status
    );
    return status;
}

}  // namespace bd_util_nodes
