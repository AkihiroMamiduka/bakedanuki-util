#include "bdUtilNodes/nodes/BdDblValueNode.h"

#include <maya/MFnNumericAttribute.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDblValueNode::typeName("bdDbl_Value");
const MTypeId BdDblValueNode::typeId(0x00142694);

MObject BdDblValueNode::value;

void* BdDblValueNode::creator() {
    return new BdDblValueNode();
}

MStatus BdDblValueNode::initialize() {
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
