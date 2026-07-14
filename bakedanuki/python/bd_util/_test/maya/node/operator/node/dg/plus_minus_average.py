# coding: utf-8

# self
from ....... import logger as u_logger
from ...... import str as test_str
from .......maya.node.modifier import ModifierManager
from .......maya.node.operator.node.dg.plus_minus_average import (
    PlusMinusAverage,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    attribute_access()
    plug_access()
    get_set()
    get_set_short_name()


# class_access
def attribute_access():
    test_str.title("attribute_access")
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage",
            PlusMinusAverage,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.input1D",
            PlusMinusAverage.input1D,
        )
    )
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.input2D",
            PlusMinusAverage.input2D,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.input2D.input2Dx",
            PlusMinusAverage.input2D.input2Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.input2D.input2Dy",
            PlusMinusAverage.input2D.input2Dy,
        )
    )
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.input3D",
            PlusMinusAverage.input3D,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.input3D.input3Dx",
            PlusMinusAverage.input3D.input3Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.input3D.input3Dy",
            PlusMinusAverage.input3D.input3Dy,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.input3D.input3Dz",
            PlusMinusAverage.input3D.input3Dz,
        )
    )
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output1D",
            PlusMinusAverage.output1D,
        )
    )
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output2D",
            PlusMinusAverage.output2D,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output2D.output2Dx",
            PlusMinusAverage.output2D.output2Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output2D.output2Dy",
            PlusMinusAverage.output2D.output2Dy,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output2Dx",
            PlusMinusAverage.output2Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output2Dy",
            PlusMinusAverage.output2Dy,
        )
    )
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output3D",
            PlusMinusAverage.output3D,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output3D.output3Dx",
            PlusMinusAverage.output3D.output3Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output3D.output3Dy",
            PlusMinusAverage.output3D.output3Dy,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output3D.output3Dz",
            PlusMinusAverage.output3D.output3Dz,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output3Dx",
            PlusMinusAverage.output3Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output3Dy",
            PlusMinusAverage.output3Dy,
        )
    )
    logger.debug(
        "{}: {}".format(
            "PlusMinusAverage.output3Dz",
            PlusMinusAverage.output3Dz,
        )
    )


# instance_access
def plug_access():
    test_str.title("plug_access")

    modifier_manager = ModifierManager()
    node = PlusMinusAverage.create(modifier_manager, name="test")
    modifier_manager.do_it_dg()

    logger.debug(
        "{}: {}".format(
            "node",
            node,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.input1D",
            node.input1D,
        )
    )
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.input2D",
            node.input2D,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.input2D[0].input2Dx",
            node.input2D[0].input2Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.input2D[0].input2Dy",
            node.input2D[0].input2Dy,
        )
    )
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.input3D",
            node.input3D,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].input3Dx",
            node.input3D[0].input3Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].input3Dy",
            node.input3D[0].input3Dy,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].input3Dz",
            node.input3D[0].input3Dz,
        )
    )
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.output1D",
            node.output1D,
        )
    )
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.output2D",
            node.output2D,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output2D.output2Dx",
            node.output2D.output2Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output2D.output2Dy",
            node.output2D.output2Dy,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output2Dx",
            node.output2Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output2Dy",
            node.output2Dy,
        )
    )
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.output3D",
            node.output3D,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output3D.output3Dx",
            node.output3D.output3Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output3D.output3Dy",
            node.output3D.output3Dy,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output3D.output3Dz",
            node.output3D.output3Dz,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output3Dx",
            node.output3Dx,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output3Dy",
            node.output3Dy,
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output3Dz",
            node.output3Dz,
        )
    )


def get_set():
    test_str.title("get_set")

    modifier_manager = ModifierManager()
    node = PlusMinusAverage.create(modifier_manager, name="test")
    modifier_manager.do_it_dg()

    logger.debug(f"node: {node}")

    # input1D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.input1D[0].get()",
            node.input1D[0].get(),
        )
    )
    logger.debug("--set")
    node.input1D[0].set(100.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.input1D[0].get()",
            node.input1D[0].get(),
        )
    )

    # input2D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.input2D[0].get()",
            node.input2D[0].get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.input2D[0].input2Dx.get()",
            node.input2D[0].input2Dx.get(),
        )
    )
    logger.debug("--set")
    node.input2D[0].input2Dx.set(201.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.input2D[0].input2Dx.get()",
            node.input2D[0].input2Dx.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.input2D[0].input2Dy.get()",
            node.input2D[0].input2Dy.get(),
        )
    )
    logger.debug("--set")
    node.input2D[0].input2Dy.set(202.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.input2D[0].input2Dy.get()",
            node.input2D[0].input2Dy.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.input2D[0].get()",
            node.input2D[0].get(),
        )
    )

    # input3D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].get()",
            node.input3D[0].get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].input3Dx.get()",
            node.input3D[0].input3Dx.get(),
        )
    )
    logger.debug("--set")
    node.input3D[0].input3Dx.set(301.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].input3Dx.get()",
            node.input3D[0].input3Dx.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].input3Dy.get()",
            node.input3D[0].input3Dy.get(),
        )
    )
    logger.debug("--set")
    node.input3D[0].input3Dy.set(302.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].input3Dy.get()",
            node.input3D[0].input3Dy.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].input3Dz.get()",
            node.input3D[0].input3Dz.get(),
        )
    )
    logger.debug("--set")
    node.input3D[0].input3Dz.set(303.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].input3Dz.get()",
            node.input3D[0].input3Dz.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.input3D[0].get()",
            node.input3D[0].get(),
        )
    )

    # output1D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.output1D.get()",
            node.output1D.get(),
        )
    )

    # output2D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.output2D.get()",
            node.output2D.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.output2D.output2Dx.get()",
            node.output2D.output2Dx.get(),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output2Dx.get()",
            node.output2Dx.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.output2D.output2Dy.get()",
            node.output2D.output2Dy.get(),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output2Dy.get()",
            node.output2Dy.get(),
        )
    )

    # output3D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.output3D.get()",
            node.output3D.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.output3D.output3Dx.get()",
            node.output3D.output3Dx.get(),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output3Dx.get()",
            node.output3Dx.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.output3D.output3Dy.get()",
            node.output3D.output3Dy.get(),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output3Dy.get()",
            node.output3Dy.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.output3D.output3Dz.get()",
            node.output3D.output3Dz.get(),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.output3Dz.get()",
            node.output3Dz.get(),
        )
    )


def get_set_short_name():
    test_str.title("get_set_short_name")

    modifier_manager = ModifierManager()
    node = PlusMinusAverage.create(modifier_manager, name="test")
    modifier_manager.do_it_dg()

    logger.debug(f"node: {node}")

    # input1D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.i1[0].get()",
            node.i1[0].get(),
        )
    )
    logger.debug("--set")
    node.i1[0].set(100.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.i1[0].get()",
            node.i1[0].get(),
        )
    )

    # input2D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.i2[0].get()",
            node.i2[0].get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.i2[0].i2x.get()",
            node.i2[0].i2x.get(),
        )
    )
    logger.debug("--set")
    node.i2[0].i2x.set(201.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.i2[0].i2x.get()",
            node.i2[0].i2x.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.i2[0].i2y.get()",
            node.i2[0].i2y.get(),
        )
    )
    logger.debug("--set")
    node.i2[0].i2y.set(202.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.i2[0].i2y.get()",
            node.i2[0].i2y.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.i2[0].get()",
            node.i2[0].get(),
        )
    )

    # input3D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.i3[0].get()",
            node.i3[0].get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.i3[0].i3x.get()",
            node.i3[0].i3x.get(),
        )
    )
    logger.debug("--set")
    node.i3[0].i3x.set(301.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.i3[0].i3x.get()",
            node.i3[0].i3x.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.i3[0].i3y.get()",
            node.i3[0].i3y.get(),
        )
    )
    logger.debug("--set")
    node.i3[0].i3y.set(302.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.i3[0].i3y.get()",
            node.i3[0].i3y.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.i3[0].i3z.get()",
            node.i3[0].i3z.get(),
        )
    )
    logger.debug("--set")
    node.i3[0].i3z.set(303.0)
    modifier_manager.do_it_dg()
    logger.debug(
        "{}: {}".format(
            "node.i3[0].i3z.get()",
            node.i3[0].i3z.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.i3[0].get()",
            node.i3[0].get(),
        )
    )

    # output1D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.o1.get()",
            node.o1.get(),
        )
    )

    # output2D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.o2.get()",
            node.o2.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.o2.o2x.get()",
            node.o2.o2x.get(),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.o2x.get()",
            node.o2x.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.o2.o2y.get()",
            node.o2.o2y.get(),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.o2y.get()",
            node.o2y.get(),
        )
    )

    # output3D
    test_str.separator()
    logger.debug(
        "{}: {}".format(
            "node.o3.get()",
            node.o3.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.o3.o3x.get()",
            node.o3.o3x.get(),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.o3x.get()",
            node.o3x.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.o3.o3y.get()",
            node.o3.o3y.get(),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.o3y.get()",
            node.o3y.get(),
        )
    )

    test_str.separator_sub()
    logger.debug(
        "{}: {}".format(
            "node.o3.o3z.get()",
            node.o3.o3z.get(),
        )
    )
    logger.debug(
        "{}: {}".format(
            "node.o3z.get()",
            node.o3z.get(),
        )
    )
