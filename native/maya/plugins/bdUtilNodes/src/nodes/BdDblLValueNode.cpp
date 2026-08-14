#include "bdUtilNodes/nodes/BdDblLValueNode.h"

#include <maya/MFnUnitAttribute.h>

#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblLValueNode::typeName("bdDblL_Value");
const MTypeId BdDblLValueNode::typeId(0x001426B4);

MObject BdDblLValueNode::value;

void* BdDblLValueNode::creator() {
    return new BdDblLValueNode();
}

MStatus BdDblLValueNode::initialize() {
    MFnUnitAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleLinearAttribute(
        attributeFn,
        value,
        "value",
        "v",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(attributeFn);
    if (!status) {
        return status;
    }

    return addAttribute(value);
}
