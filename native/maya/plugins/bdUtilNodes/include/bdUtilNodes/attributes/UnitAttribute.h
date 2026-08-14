#pragma once

#include <maya/MStatus.h>

class MFnUnitAttribute;
class MObject;

namespace bd_util_nodes {

MStatus createDoubleAngleAttribute(
    MFnUnitAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName,
    double defaultValue
);

MStatus createDoubleLinearAttribute(
    MFnUnitAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName,
    double defaultValue
);

MStatus configureInputUnitAttribute(MFnUnitAttribute& attributeFn);

MStatus configureOutputUnitAttribute(MFnUnitAttribute& attributeFn);

}  // namespace bd_util_nodes
