#include "bdUtilNodes/attributes/BendTwistAttribute.h"

#include <utility>

#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MObject.h>
#include <maya/MString.h>

#include "bdUtilNodes/math/BendTwist.h"

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
    const char* bendVerticalShortName,
    double twistDefault,
    double bendHorizontalDefault,
    double bendVerticalDefault
) {
    MStatus status;

    twist = childAttributeFn.create(
        twistLongName,
        twistShortName,
        MFnUnitAttribute::kAngle,
        twistDefault,
        &status
    );
    if (!status) {
        return status;
    }

    bendHorizontal = childAttributeFn.create(
        bendHorizontalLongName,
        bendHorizontalShortName,
        MFnUnitAttribute::kAngle,
        bendHorizontalDefault,
        &status
    );
    if (!status) {
        return status;
    }

    bendVertical = childAttributeFn.create(
        bendVerticalLongName,
        bendVerticalShortName,
        MFnUnitAttribute::kAngle,
        bendVerticalDefault,
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

MStatus createBendTwistOrderAttribute(
    MFnEnumAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName
) {
    MStatus status;
    attribute = attributeFn.create(
        longName,
        shortName,
        static_cast<short>(BendTwistOrder::kTwistBend),
        &status
    );
    if (!status) {
        return status;
    }
    for (const auto& field : {
             std::pair<const char*, BendTwistOrder>{
                 "TwistBend",
                 BendTwistOrder::kTwistBend,
             },
             std::pair<const char*, BendTwistOrder>{
                 "BendTwist",
                 BendTwistOrder::kBendTwist,
             },
         }) {
        status = attributeFn.addField(
            field.first,
            static_cast<short>(field.second)
        );
        if (!status) {
            return status;
        }
    }
    status = attributeFn.setReadable(true);
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

MStatus createBendLimitModeAttribute(
    MFnEnumAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName
) {
    MStatus status;
    attribute = attributeFn.create(
        longName,
        shortName,
        static_cast<short>(BendLimitMode::kBox),
        &status
    );
    if (!status) {
        return status;
    }
    for (const auto& field : {
             std::pair<const char*, BendLimitMode>{
                 "Box",
                 BendLimitMode::kBox,
             },
             std::pair<const char*, BendLimitMode>{
                 "Ellipse",
                 BendLimitMode::kEllipse,
             },
         }) {
        status = attributeFn.addField(
            field.first,
            static_cast<short>(field.second)
        );
        if (!status) {
            return status;
        }
    }
    status = attributeFn.setReadable(true);
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

}  // namespace bd_util_nodes
