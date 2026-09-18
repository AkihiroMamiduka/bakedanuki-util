# coding:utf-8

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

    clip = bdu.AnimationClip.capture(
        [trsf],
        include_channel_box=True,
    )

    dst_0 = nodes.create.transform(name="dst_0")
    clip.restore(nodes.modifier_manager, targets=[dst_0])

    dst_0_0 = nodes.create.transform(name="dst_0_0")
    clip.restore(
        nodes.modifier_manager,
        targets=[dst_0_0],
        to_start_frame=0,
        to_end_frame=500,
    )

    dst_0_1 = nodes.create.transform(name="dst_0_1")
    clip.restore(
        nodes.modifier_manager,
        targets=[dst_0_1],
    )
    dst_0_1.tx.keyframe.scale_frames(-50, 50, scale=0.5)
    dst_0_1.ty.keyframe.scale_frames(-50, 50, to_start=-25, to_end=25)

    clip = bdu.AnimationClip.capture(
        [trsf],
        start_frame=-50,
        end_frame=50,
        include_channel_box=True,
    )

    dst_1 = nodes.create.transform(name="dst_1")
    clip.restore(nodes.modifier_manager, targets=[dst_1])

    dst_1_0 = nodes.create.transform(name="dst_1_0")
    clip.restore(nodes.modifier_manager, targets=[dst_1_0], offset_frames=100)

    dst_1_1 = nodes.create.transform(name="dst_1_1")
    clip.restore(nodes.modifier_manager, targets=[dst_1_1], to_start_frame=200)

    dst_1_2 = nodes.create.transform(name="dst_1_2")
    clip.restore(nodes.modifier_manager, targets=[dst_1_2], to_end_frame=300)

    dst_2 = nodes.create.transform(name="dst_2")
    clip.restore(nodes.modifier_manager, targets=[dst_2], mode="replace_all")

    clip = bdu.AnimationClip.capture(
        [trsf],
        start_frame=-50,
        end_frame=50,
        layer_mode="preserve",
    )

    dst_3 = nodes.create.transform(name="dst_3")
    clip.restore(nodes.modifier_manager, targets=[dst_3])

    clip = bdu.AnimationClip.capture(
        [trsf],
        include_channel_box=True,
    )
    dst_4_0 = nodes.create.transform(name="dst_4_0")
    dst_4_1 = nodes.create.transform(name="dst_4_1")
    dst_4_2 = nodes.create.transform(name="dst_4_2")
    dst_4_3 = nodes.create.transform(name="dst_4_3")
    for target in [dst_4_0, dst_4_1, dst_4_2, dst_4_3]:
        clip.restore(nodes.modifier_manager, targets=[target])
    dst_4_1.tx.keyframe.set_values(
        -50, 50, value=25, interpolate_start=-75, interpolate_end=75
    )
    dst_4_2.tx.keyframe.add_values(
        -50, 50, offset=25, interpolate_start=-75, interpolate_end=75
    )
    dst_4_3.tx.keyframe.scale_values(
        -50, 50, scale=2, interpolate_start=-75, interpolate_end=75
    )

    clip = bdu.AnimationClip.capture(
        [trsf],
        include_channel_box=True,
    )
    dst_5_0 = nodes.create.transform(name="dst_5_0")
    dst_5_1 = nodes.create.transform(name="dst_5_1")
    dst_5_2 = nodes.create.transform(name="dst_5_2")
    for target in [dst_5_0, dst_5_1, dst_5_2]:
        clip.restore(nodes.modifier_manager, targets=[target])
    dst_5_1.tx.keyframe.move_frames(
        -25,
        25,
        offset=25,
        interpolate_start=-50,
        interpolate_end=75,
    )
    dst_5_2.tx.keyframe.move_frames(
        -25,
        25,
        offset=25,
        interpolate_start=-50,
        interpolate_end=75,
        interpolation="linear",
    )

    clip = bdu.AnimationClip.capture(
        [trsf],
        include_channel_box=True,
    )
    dst_6_0 = nodes.create.transform(name="dst_6_0")
    dst_6_1 = nodes.create.transform(name="dst_6_1")
    dst_6_2 = nodes.create.transform(name="dst_6_2")
    for target in [dst_6_0, dst_6_1, dst_6_2]:
        clip.restore(nodes.modifier_manager, targets=[target])
    dst_6_1.tx.keyframe.scale_frames(
        -50,
        50,
        scale=0.5,
        interpolate_start=-75,
        interpolate_end=75,
    )
    dst_6_2.tx.keyframe.scale_frames(
        -50,
        50,
        scale=0.5,
        pivot=0,
        interpolate_start=-75,
        interpolate_end=75,
    )

    clip = bdu.AnimationClip.capture(
        [trsf],
        include_channel_box=True,
    )
    dst_7_0 = nodes.create.transform(name="dst_7_0")
    clip.restore(nodes.modifier_manager, targets=[dst_7_0])

    dst_7_1 = nodes.create.transform(name="dst_7_1")
    reduced_clip = clip.reduce_keys(tolerance=0.01)
    reduced_clip.restore(nodes.modifier_manager, targets=[dst_7_1])

    dst_7_2 = nodes.create.transform(name="dst_7_2")
    reduced_clip = clip.reduce_keys(-50, 50, tolerance=0.01)
    reduced_clip.restore(nodes.modifier_manager, targets=[dst_7_2])

    dst_8_0 = nodes.create.transform(name="dst_8_0")
    reduced_clip.restore(
        nodes.modifier_manager,
        targets=[dst_8_0],
        start_frame=-50,
        end_frame=50,
        mode="replace_range",
    )
    dst_8_1 = nodes.create.transform(name="dst_8_1")
    reduced_clip.restore(
        nodes.modifier_manager,
        targets=[dst_8_1],
        start_frame=-50,
        end_frame=50,
        to_start_frame=100,
        to_end_frame=200,
        mode="replace_range",
    )

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
