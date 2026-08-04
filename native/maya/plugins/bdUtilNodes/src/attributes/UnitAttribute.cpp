#include "bdUtilNodes/attributes/UnitAttribute.h"

#include <maya/MFnUnitAttribute.h>
#include <maya/MObject.h>
#include <maya/MString.h>

namespace bd_util_nodes {

MStatus createDoubleLinearAttribute(
    MFnUnitAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName,
    double defaultValue
) {
    MStatus status;
    attribute = attributeFn.create(
        longName,
        shortName,
        MFnUnitAttribute::kDistance,
        defaultValue,
        &status
    );
    return status;
}

MStatus configureInputUnitAttribute(MFnUnitAttribute& attributeFn) {
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

MStatus configureOutputUnitAttribute(MFnUnitAttribute& attributeFn) {
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
