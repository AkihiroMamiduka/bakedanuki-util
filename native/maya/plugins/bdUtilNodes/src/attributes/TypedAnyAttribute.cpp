#include "bdUtilNodes/attributes/TypedAnyAttribute.h"

#include <maya/MFnData.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MObject.h>
#include <maya/MString.h>

namespace bd_util_nodes {

MStatus createTypedAnyAttribute(
    MFnTypedAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName
) {
    MStatus status;
    attribute = attributeFn.create(
        MString(longName),
        MString(shortName),
        MFnData::kAny,
        MObject::kNullObj,
        &status
    );
    return status;
}

MStatus configureInputTypedAttribute(MFnTypedAttribute& attributeFn) {
    MStatus status = attributeFn.setReadable(true);
    if (!status) {
        return status;
    }

    status = attributeFn.setWritable(true);
    if (!status) {
        return status;
    }

    // kAny is storable by default and rejects an explicit setStorable(true).
    return attributeFn.setKeyable(false);
}

MStatus configureOutputTypedAttribute(MFnTypedAttribute& attributeFn) {
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
