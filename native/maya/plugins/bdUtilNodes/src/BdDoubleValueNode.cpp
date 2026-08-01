#include "bdUtilNodes/BdDoubleValueNode.h"

#include <maya/MFnNumericAttribute.h>

#include "bdUtilNodes/NumericAttribute.h"

const MString BdDoubleValueNode::typeName("bdDoubleValue");
const MTypeId BdDoubleValueNode::typeId(0x0007F015);

MObject BdDoubleValueNode::value;

void* BdDoubleValueNode::creator() {
    return new BdDoubleValueNode();
}

MStatus BdDoubleValueNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleAttribute(
        attributeFn,
        value,
        "value",
        "v",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    return addAttribute(value);
}
