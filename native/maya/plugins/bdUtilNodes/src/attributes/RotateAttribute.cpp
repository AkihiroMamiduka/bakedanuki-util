#include "bdUtilNodes/attributes/RotateAttribute.h"

#include <utility>

#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MObject.h>
#include <maya/MString.h>

namespace bd_util_nodes {

MStatus createRotateAttribute(
    MFnNumericAttribute& parentAttributeFn,
    MFnUnitAttribute& childAttributeFn,
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
    const char* childZShortName
) {
    MStatus status;

    childX = childAttributeFn.create(
        childXLongName,
        childXShortName,
        MFnUnitAttribute::kAngle,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    childY = childAttributeFn.create(
        childYLongName,
        childYShortName,
        MFnUnitAttribute::kAngle,
        0.0,
        &status
    );
    if (!status) {
        return status;
    }

    childZ = childAttributeFn.create(
        childZLongName,
        childZShortName,
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
        childX,
        childY,
        childZ,
        &status
    );
    return status;
}

MStatus createRotateOrderAttribute(
    MFnEnumAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName
) {
    MStatus status;
    attribute = attributeFn.create(
        longName,
        shortName,
        static_cast<short>(EulerRotateOrder::kXYZ),
        &status
    );
    if (!status) {
        return status;
    }

    for (const auto& field : {
             std::pair<const char*, EulerRotateOrder>{
                 "xyz",
                 EulerRotateOrder::kXYZ,
             },
             std::pair<const char*, EulerRotateOrder>{
                 "yzx",
                 EulerRotateOrder::kYZX,
             },
             std::pair<const char*, EulerRotateOrder>{
                 "zxy",
                 EulerRotateOrder::kZXY,
             },
             std::pair<const char*, EulerRotateOrder>{
                 "xzy",
                 EulerRotateOrder::kXZY,
             },
             std::pair<const char*, EulerRotateOrder>{
                 "yxz",
                 EulerRotateOrder::kYXZ,
             },
             std::pair<const char*, EulerRotateOrder>{
                 "zyx",
                 EulerRotateOrder::kZYX,
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

bool toEulerRotationOrder(
    short value,
    MEulerRotation::RotationOrder& order
) {
    switch (static_cast<EulerRotateOrder>(value)) {
        case EulerRotateOrder::kXYZ:
            order = MEulerRotation::kXYZ;
            return true;
        case EulerRotateOrder::kYZX:
            order = MEulerRotation::kYZX;
            return true;
        case EulerRotateOrder::kZXY:
            order = MEulerRotation::kZXY;
            return true;
        case EulerRotateOrder::kXZY:
            order = MEulerRotation::kXZY;
            return true;
        case EulerRotateOrder::kYXZ:
            order = MEulerRotation::kYXZ;
            return true;
        case EulerRotateOrder::kZYX:
            order = MEulerRotation::kZYX;
            return true;
    }
    return false;
}

}  // namespace bd_util_nodes
