#pragma once

#include <maya/MObject.h>
#include <maya/MStatus.h>

class MFnEnumAttribute;

namespace bd_util_nodes {

MStatus createComparisonOperationAttribute(
    MFnEnumAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName
);

MStatus createLogicOperationAttribute(
    MFnEnumAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName
);

}  // namespace bd_util_nodes
