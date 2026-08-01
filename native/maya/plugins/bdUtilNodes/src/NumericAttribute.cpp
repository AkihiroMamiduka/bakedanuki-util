#include "bdUtilNodes/NumericAttribute.h"

#include <maya/MFnNumericAttribute.h>
#include <maya/MFnNumericData.h>
#include <maya/MString.h>

namespace bd_util_nodes {

MStatus createDoubleAttribute(
    MFnNumericAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName,
    double defaultValue
) {
    MStatus status;
    attribute = attributeFn.create(
        longName,
        shortName,
        MFnNumericData::kDouble,
        defaultValue,
        &status
    );
    return status;
}

MStatus configureInputNumericAttribute(
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

MStatus configureOutputNumericAttribute(
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
