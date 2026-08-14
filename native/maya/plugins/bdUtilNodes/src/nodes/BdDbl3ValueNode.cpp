#include "bdUtilNodes/nodes/BdDbl3ValueNode.h"

#include <maya/MFnNumericAttribute.h>

#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDbl3ValueNode::typeName("bdDbl3_Value");
const MTypeId BdDbl3ValueNode::typeId(0x00142695);

MObject BdDbl3ValueNode::value;
MObject BdDbl3ValueNode::valueX;
MObject BdDbl3ValueNode::valueY;
MObject BdDbl3ValueNode::valueZ;

void* BdDbl3ValueNode::creator() {
    return new BdDbl3ValueNode();
}

MStatus BdDbl3ValueNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
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
        "vz",
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
