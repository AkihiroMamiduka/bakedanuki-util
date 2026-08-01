#include "bdUtilNodes/BdDbl3ValueNode.h"

#include <maya/MFnNumericAttribute.h>

#include "bdUtilNodes/Double3Attribute.h"
#include "bdUtilNodes/NumericAttribute.h"

const MString BdDbl3ValueNode::typeName("bdDbl3Value");
const MTypeId BdDbl3ValueNode::typeId(0x0007F016);

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
