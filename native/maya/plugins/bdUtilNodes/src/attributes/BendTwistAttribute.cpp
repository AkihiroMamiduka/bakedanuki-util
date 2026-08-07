#include "bdUtilNodes/attributes/BendTwistAttribute.h"

#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MObject.h>
#include <maya/MString.h>

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
) {
    MStatus status;

    twist = childAttributeFn.create(
        twistLongName,
        twistShortName,
        MFnUnitAttribute::kAngle,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    bendHorizontal = childAttributeFn.create(
        bendHorizontalLongName,
        bendHorizontalShortName,
        MFnUnitAttribute::kAngle,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    bendVertical = childAttributeFn.create(
        bendVerticalLongName,
        bendVerticalShortName,
        MFnUnitAttribute::kAngle,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    parent = parentAttributeFn.create(
        parentLongName,
        parentShortName,
        twist,
        bendHorizontal,
        bendVertical,
        &status
    );
    return status;
}

}  // namespace bd_util_nodes
