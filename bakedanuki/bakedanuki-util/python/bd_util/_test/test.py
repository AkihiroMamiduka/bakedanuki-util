# coding:utf-8

# maya
from maya import cmds

# self
import bd_util as bdu
from .. import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


def main():
    nodes = bdu.Nodes()

    trsf = nodes.create.transform(name="test")

    layer = nodes.create.animLayer(name="Sample")

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    trsf.tx.keyframe.set_key(-100, frame=-100, out_tangent_type="flat")
    trsf.tx.keyframe.set_key(100, frame=100, in_tangent_type="flat")

    trsf.rx.keyframe.set_key(-100, frame=-100, out_tangent_type="flat")
    trsf.rx.keyframe.set_key(100, frame=100, in_tangent_type="flat")

    nodes.modifier_manager.do_it_dg()

    layer.add_nodes([trsf])
    trsf.tx.keyframe.anim_layer(layer).set_keys(
        [(i, i * 2) for i in range(-100, 101)]
    )

    nodes.modifier_manager.do_it_dg()

    samples = trsf.tx.sample_values(frames=range(-100, 101))
    trsf.ty.keyframe.set_keys(
        samples, in_tangent_type="auto", out_tangent_type="auto"
    )

    samples = trsf.rx.sample_values(frames=range(-100, 101))
    trsf.ry.keyframe.set_keys(
        samples, in_tangent_type="auto", out_tangent_type="auto"
    )

    nodes.modifier_manager.do_it_dg()

    trsf.ty.keyframe.reduce_keys(-50, 50, tolerance=0.01)
    trsf.ry.keyframe.reduce_keys(-50, 50, tolerance=1)

    nodes.modifier_manager.do_it_dg()

    # clip = bdu.AnimationClip.capture(
    #     [trsf],
    #     include_channel_box=True,
    # )

    # dst_0 = nodes.create.transform(name="dst_0")
    # clip.restore(nodes.modifier_manager, targets=[dst_0])

    # dst_0_0 = nodes.create.transform(name="dst_0_0")
    # clip.restore(
    #     nodes.modifier_manager,
    #     targets=[dst_0_0],
    #     to_start_frame=0,
    #     to_end_frame=500,
    # )

    # dst_0_1 = nodes.create.transform(name="dst_0_1")
    # clip.restore(
    #     nodes.modifier_manager,
    #     targets=[dst_0_1],
    # )
    # dst_0_1.tx.keyframe.scale_frames(-50, 50, scale=0.5)
    # dst_0_1.ty.keyframe.scale_frames(-50, 50, to_start=-25, to_end=25)

    # clip = bdu.AnimationClip.capture(
    #     [trsf],
    #     start_frame=-50,
    #     end_frame=50,
    #     include_channel_box=True,
    # )

    # dst_1 = nodes.create.transform(name="dst_1")
    # clip.restore(nodes.modifier_manager, targets=[dst_1])

    # dst_1_0 = nodes.create.transform(name="dst_1_0")
    # clip.restore(nodes.modifier_manager, targets=[dst_1_0], offset_frames=100)

    # dst_1_1 = nodes.create.transform(name="dst_1_1")
    # clip.restore(nodes.modifier_manager, targets=[dst_1_1], to_start_frame=200)

    # dst_1_2 = nodes.create.transform(name="dst_1_2")
    # clip.restore(nodes.modifier_manager, targets=[dst_1_2], to_end_frame=300)

    # dst_2 = nodes.create.transform(name="dst_2")
    # clip.restore(nodes.modifier_manager, targets=[dst_2], mode="replace_all")

    # clip = bdu.AnimationClip.capture(
    #     [trsf],
    #     start_frame=-50,
    #     end_frame=50,
    #     layer_mode="preserve",
    # )

    # dst_3 = nodes.create.transform(name="dst_3")
    # clip.restore(nodes.modifier_manager, targets=[dst_3])

    # clip = bdu.AnimationClip.capture(
    #     [trsf],
    #     include_channel_box=True,
    # )
    # dst_4_0 = nodes.create.transform(name="dst_4_0")
    # dst_4_1 = nodes.create.transform(name="dst_4_1")
    # dst_4_2 = nodes.create.transform(name="dst_4_2")
    # dst_4_3 = nodes.create.transform(name="dst_4_3")
    # for target in [dst_4_0, dst_4_1, dst_4_2, dst_4_3]:
    #     clip.restore(nodes.modifier_manager, targets=[target])
    # dst_4_1.tx.keyframe.set_values(
    #     -50, 50, value=25, interpolate_start=-75, interpolate_end=75
    # )
    # dst_4_2.tx.keyframe.add_values(
    #     -50, 50, offset=25, interpolate_start=-75, interpolate_end=75
    # )
    # dst_4_3.tx.keyframe.scale_values(
    #     -50, 50, scale=2, interpolate_start=-75, interpolate_end=75
    # )

    # clip = bdu.AnimationClip.capture(
    #     [trsf],
    #     include_channel_box=True,
    # )
    # dst_5_0 = nodes.create.transform(name="dst_5_0")
    # dst_5_1 = nodes.create.transform(name="dst_5_1")
    # dst_5_2 = nodes.create.transform(name="dst_5_2")
    # for target in [dst_5_0, dst_5_1, dst_5_2]:
    #     clip.restore(nodes.modifier_manager, targets=[target])
    # dst_5_1.tx.keyframe.move_frames(
    #     -25,
    #     25,
    #     offset=25,
    #     interpolate_start=-50,
    #     interpolate_end=75,
    # )
    # dst_5_2.tx.keyframe.move_frames(
    #     -25,
    #     25,
    #     offset=25,
    #     interpolate_start=-50,
    #     interpolate_end=75,
    #     interpolation="linear",
    # )

    # clip = bdu.AnimationClip.capture(
    #     [trsf],
    #     include_channel_box=True,
    # )
    # dst_6_0 = nodes.create.transform(name="dst_6_0")
    # dst_6_1 = nodes.create.transform(name="dst_6_1")
    # dst_6_2 = nodes.create.transform(name="dst_6_2")
    # for target in [dst_6_0, dst_6_1, dst_6_2]:
    #     clip.restore(nodes.modifier_manager, targets=[target])
    # dst_6_1.tx.keyframe.scale_frames(
    #     -50,
    #     50,
    #     scale=0.5,
    #     interpolate_start=-75,
    #     interpolate_end=75,
    # )
    # dst_6_2.tx.keyframe.scale_frames(
    #     -50,
    #     50,
    #     scale=0.5,
    #     pivot=0,
    #     interpolate_start=-75,
    #     interpolate_end=75,
    # )

    # clip = bdu.AnimationClip.capture(
    #     [trsf],
    #     include_channel_box=True,
    # )
    # dst_7_0 = nodes.create.transform(name="dst_7_0")
    # clip.restore(nodes.modifier_manager, targets=[dst_7_0])

    # dst_7_1 = nodes.create.transform(name="dst_7_1")
    # reduced_clip = clip.reduce_keys(tolerance=0.01)
    # reduced_clip.restore(nodes.modifier_manager, targets=[dst_7_1])

    # dst_7_2 = nodes.create.transform(name="dst_7_2")
    # reduced_clip = clip.reduce_keys(-50, 50, tolerance=0.01)
    # reduced_clip.restore(nodes.modifier_manager, targets=[dst_7_2])

    # dst_8_0 = nodes.create.transform(name="dst_8_0")
    # reduced_clip.restore(
    #     nodes.modifier_manager,
    #     targets=[dst_8_0],
    #     start_frame=-50,
    #     end_frame=50,
    #     mode="replace_range",
    # )
    # dst_8_1 = nodes.create.transform(name="dst_8_1")
    # reduced_clip.restore(
    #     nodes.modifier_manager,
    #     targets=[dst_8_1],
    #     start_frame=-50,
    #     end_frame=50,
    #     to_start_frame=100,
    #     to_end_frame=200,
    #     mode="replace_range",
    # )

    # dst_9_0 = nodes.create.transform(name="dst_9_0")
    # reduced_clip.restore(
    #     nodes.modifier_manager,
    #     targets=[dst_9_0],
    # )
    # path = reduced_clip.save(r"D:/anim_clip.json")
    # load_clip = bdu.AnimationClip.load(path)
    # dst_9_1 = nodes.create.transform(name="dst_9_1")
    # load_clip.restore(
    #     nodes.modifier_manager,
    #     targets=[dst_9_1],
    # )

    # dst_10_0 = nodes.create.transform(name="dst_10_0")
    # trsf.tx.connect(dst_10_0.tx)
    # dst_10_1 = nodes.create.transform(name="dst_10_1")
    # trsf.tx.connect(dst_10_1.tx)
    # dst_10_1.tx.keyframe.bake()

    # dst_11_0 = nodes.create.transform(name="dst_11_0")
    # trsf.tx.connect(dst_11_0.tx)
    # trsf.ty.connect(dst_11_0.ty)
    # trsf.tz.connect(dst_11_0.tz)
    # trsf.rx.connect(dst_11_0.rx)
    # trsf.ry.connect(dst_11_0.ry)
    # trsf.rz.connect(dst_11_0.rz)
    # trsf.sx.connect(dst_11_0.sx)
    # trsf.sy.connect(dst_11_0.sy)
    # trsf.sz.connect(dst_11_0.sz)
    # dst_11_0.keyframes.bake()

    # dst_11_1 = nodes.create.transform(name="dst_11_1")
    # trsf.tx.connect(dst_11_1.tx)
    # trsf.ty.connect(dst_11_1.ty)
    # trsf.tz.connect(dst_11_1.tz)
    # trsf.rx.connect(dst_11_1.rx)
    # trsf.ry.connect(dst_11_1.ry)
    # trsf.rz.connect(dst_11_1.rz)
    # trsf.sx.connect(dst_11_1.sx)
    # trsf.sy.connect(dst_11_1.sy)
    # trsf.sz.connect(dst_11_1.sz)
    # dst_11_1.keyframes.bake(include_static=True)

    # dst_11_2 = nodes.create.transform(name="dst_11_2")
    # trsf.tx.connect(dst_11_2.tx)
    # trsf.ty.connect(dst_11_2.ty)
    # trsf.tz.connect(dst_11_2.tz)
    # trsf.rx.connect(dst_11_2.rx)
    # trsf.ry.connect(dst_11_2.ry)
    # trsf.rz.connect(dst_11_2.rz)
    # trsf.sx.connect(dst_11_2.sx)
    # trsf.sy.connect(dst_11_2.sy)
    # trsf.sz.connect(dst_11_2.sz)
    # dst_11_2.keyframes.bake(include_static=False)

    dst_12_0 = nodes.create.transform(name="dst_12_0")
    trsf.tx.connect(dst_12_0.tx)
    trsf.ty.connect(dst_12_0.ty)
    trsf.tz.connect(dst_12_0.tz)

    dst_12_1 = nodes.create.transform(name="dst_12_1")
    trsf.rx.connect(dst_12_1.rx)
    trsf.ry.connect(dst_12_1.ry)
    trsf.rz.connect(dst_12_1.rz)

    dst_12_2 = nodes.create.transform(name="dst_12_2")
    trsf.sx.connect(dst_12_2.sx)
    trsf.sy.connect(dst_12_2.sy)
    trsf.sz.connect(dst_12_2.sz)

    dst_12_3 = nodes.create.transform(name="dst_12_3")
    trsf.tx.connect(dst_12_3.tx)
    trsf.ty.connect(dst_12_3.ty)
    trsf.tz.connect(dst_12_3.tz)
    trsf.rx.connect(dst_12_3.rx)
    trsf.ry.connect(dst_12_3.ry)
    trsf.rz.connect(dst_12_3.rz)
    trsf.sx.connect(dst_12_3.sx)
    trsf.sy.connect(dst_12_3.sy)
    trsf.sz.connect(dst_12_3.sz)

    targets = [dst_12_0, dst_12_1, dst_12_2, dst_12_3]

    nodes.keyframes.bake(targets, attributes=["t", "r", "s"])
    nodes.keyframes.reduce_keys(targets, tolerance=0.01)

    dst_12_3.tx.keyframe.set_weighted(True)
    dst_12_3.tx.keyframe.set_tangent_locks(
        tangents_locked=True, weights_locked=True
    )

    dst_12_3.keyframes.set_tangents(tangent_type="auto")

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    clip = bdu.AnimationClip.capture(
        nodes=[dst_12_0, dst_12_1, dst_12_2, dst_12_3]
    )

    cmds.file(newFile=True, force=True)

    nodes = bdu.Nodes()
    dst_12_0 = nodes.create.transform(name="dst_12_0")
    dst_12_1 = nodes.create.transform(name="dst_12_1")
    dst_12_2 = nodes.create.transform(name="dst_12_2")
    dst_12_3 = nodes.create.transform(name="dst_12_3")

    restore_targets = [dst_12_1, dst_12_3]

    partial_clip = clip.extract(nodes=restore_targets)
    partial_clip.restore(nodes.modifier_manager)
    nodes.keyframes.reduce_keys(restore_targets, tolerance=0.01)

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
