#include "bdUtilNodes/attributes/Double3Attribute.h"

#include <maya/MFnNumericAttribute.h>
#include <maya/MFnNumericData.h>
#include <maya/MString.h>

namespace bd_util_nodes {

MStatus createDouble3Attribute(
    MFnNumericAttribute& attributeFn,
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
    const char* childZShortName,
    double defaultValue
) {
    MStatus status;

    childX = attributeFn.create(
        childXLongName,
        childXShortName,
        MFnNumericData::kDouble,
        defaultValue,
        &status
    );
    if (!status) {
        return status;
    }

    childY = attributeFn.create(
        childYLongName,
        childYShortName,
        MFnNumericData::kDouble,
        defaultValue,
        &status
    );
    if (!status) {
        return status;
    }

    childZ = attributeFn.create(
        childZLongName,
        childZShortName,
        MFnNumericData::kDouble,
        defaultValue,
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
        &status
    );
    return status;
}

}  // namespace bd_util_nodes
