#include "bdUtilNodes/Double3Attribute.h"

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

MStatus configureInputDouble3Attribute(
    MFnNumericAttribute& attributeFn
) {
    MStatus status = attributeFn.setReadable(true);
    if (!status) {
        return status;
    }

    status = attributeFn.setWritable(true);
    if (!status) {
        return status;
    }

    status = attributeFn.setStorable(true);
    if (!status) {
        return status;
    }

    return attributeFn.setKeyable(true);
}

MStatus configureOutputDouble3Attribute(
    MFnNumericAttribute& attributeFn
) {
    MStatus status = attributeFn.setReadable(true);
    if (!status) {
        return status;
    }

    status = attributeFn.setWritable(false);
    if (!status) {
        return status;
    }

    status = attributeFn.setStorable(false);
    if (!status) {
        return status;
    }

    return attributeFn.setKeyable(false);
}

}  // namespace bd_util_nodes
