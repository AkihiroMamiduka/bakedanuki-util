#include "bdUtilNodes/nodes/BdDblAValueNode.h"

#include <maya/MFnUnitAttribute.h>

#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblAValueNode::typeName("bdDblA_Value");
const MTypeId BdDblAValueNode::typeId(0x001426E9);

MObject BdDblAValueNode::value;

void* BdDblAValueNode::creator() {
    return new BdDblAValueNode();
}

MStatus BdDblAValueNode::initialize() {
    MFnUnitAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleAngleAttribute(
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
