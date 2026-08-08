#pragma once

#include <maya/MStatus.h>

class MFnEnumAttribute;
class MFnNumericAttribute;
class MFnUnitAttribute;
class MObject;

namespace bd_util_nodes {

MStatus createBendTwistAttribute(
    MFnNumericAttribute& parentAttributeFn,
    MFnUnitAttribute& childAttributeFn,
    MObject& parent,
    MObject& twist,
    MObject& bendHorizontal,
    MObject& bendVertical,
    const char* parentLongName,
    const char* parentShortName,
    const char* twistLongName,
    const char* twistShortName,
    const char* bendHorizontalLongName,
    const char* bendHorizontalShortName,
    const char* bendVerticalLongName,
    const char* bendVerticalShortName
);

MStatus createBendTwistOrderAttribute(
    MFnEnumAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName
);

}  // namespace bd_util_nodes
