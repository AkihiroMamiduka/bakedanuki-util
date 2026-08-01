#pragma once

#include <maya/MObject.h>
#include <maya/MStatus.h>

class MFnNumericAttribute;

namespace bd_util_nodes {

MStatus createDoubleAttribute(
    MFnNumericAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName,
    double defaultValue
);

MStatus configureInputNumericAttribute(
    MFnNumericAttribute& attributeFn
);

MStatus configureOutputNumericAttribute(
    MFnNumericAttribute& attributeFn
);

}  // namespace bd_util_nodes
