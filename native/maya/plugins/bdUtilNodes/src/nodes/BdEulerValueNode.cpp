#include "bdUtilNodes/nodes/BdEulerValueNode.h"

#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/RotateAttribute.h"

const MString BdEulerValueNode::typeName("bdEuler_Value");
const MTypeId BdEulerValueNode::typeId(0x0007F08F);

MObject BdEulerValueNode::value;
MObject BdEulerValueNode::valueX;
MObject BdEulerValueNode::valueY;
MObject BdEulerValueNode::valueZ;
MObject BdEulerValueNode::rotateOrder;

void* BdEulerValueNode::creator() {
    return new BdEulerValueNode();
}

MStatus BdEulerValueNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        value,
        valueX,
        valueY,
        valueZ,
        "value",
        "v",
        "valueX",
        "vx",
        "valueY",
        "vy",
        "valueZ",
        "vz"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(value);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateOrderAttribute(
        enumAttributeFn,
        rotateOrder,
        "rotateOrder",
        "ro"
    );
    if (!status) {
        return status;
    }
    return addAttribute(rotateOrder);
}
