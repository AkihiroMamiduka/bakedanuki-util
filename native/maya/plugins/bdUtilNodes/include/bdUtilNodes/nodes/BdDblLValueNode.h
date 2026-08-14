#pragma once

#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class BdDblLValueNode final : public MPxNode {
public:
    static void* creator();
    static MStatus initialize();

    static const MString typeName;
    static const MTypeId typeId;

    static MObject value;
};
