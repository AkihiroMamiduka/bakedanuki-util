#include "bdUtilNodes/BdDouble3ValueNode.h"

#include <maya/MFnNumericAttribute.h>

#include "bdUtilNodes/Double3Attribute.h"
#include "bdUtilNodes/NumericAttribute.h"

const MString BdDouble3ValueNode::typeName("bdDouble3Value");
const MTypeId BdDouble3ValueNode::typeId(0x0007F016);

MObject BdDouble3ValueNode::value;
MObject BdDouble3ValueNode::valueX;
MObject BdDouble3ValueNode::valueY;
MObject BdDouble3ValueNode::valueZ;

void* BdDouble3ValueNode::creator() {
    return new BdDouble3ValueNode();
}

MStatus BdDouble3ValueNode::initialize() {
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
