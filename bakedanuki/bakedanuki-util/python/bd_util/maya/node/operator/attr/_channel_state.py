# coding: utf-8
from typing import Any, cast, Literal

from maya import cmds
from maya.api import OpenMaya as om

from .....py.error import UnsupportedOperationError
from ._core import PlugOperator


class ChannelBoxStateMixin:
    __slots__ = ()

    def _channel_box_state_plugs(self) -> tuple[om.MPlug, ...]:
        raise NotImplementedError

    def _require_indexed_channel_box_target(self) -> None:
        plug_operator = cast(PlugOperator[Any], self)
        if plug_operator.multi and plug_operator.index is None:
            raise UnsupportedOperationError(
                "Channel Box state operations require an indexed multi "
                f"plug: {plug_operator.plug_name}"
            )

    def _set_channel_box_state(
        self,
        *,
        keyable: bool,
        channel_box: bool,
        direct: bool,
    ) -> None:
        plugs = self._channel_box_state_plugs()
        flag_values: tuple[tuple[Literal["keyable", "channel_box"], bool], ...]
        if keyable:
            flag_values = (("channel_box", False), ("keyable", True))
        else:
            flag_values = (
                ("keyable", False),
                ("channel_box", channel_box),
            )
        if direct:
            for plug in plugs:
                for flag_name, value in flag_values:
                    if flag_name == "keyable":
                        plug.isKeyable = value
                    else:
                        plug.isChannelBox = value
            return

        plug_operator = cast(PlugOperator[Any], self)
        for plug in plugs:
            for flag_name, value in flag_values:

                def set_state(
                    target_plug: om.MPlug = plug,
                    target_flag: Literal["keyable", "channel_box"] = flag_name,
                    target_value: bool = value,
                ) -> None:
                    plug_name = target_plug.name()
                    if not cmds.objExists(plug_name):
                        raise RuntimeError(
                            "Channel Box state plug is not available when "
                            "the queued command executes: "
                            f"{plug_name!r}"
                        )
                    if target_flag == "keyable":
                        cmds.setAttr(plug_name, keyable=target_value)
                    else:
                        cmds.setAttr(plug_name, channelBox=target_value)

                dg_mod = plug_operator.node.modifier_manager.dg_mod
                dg_mod.pythonCommandToExecute(set_state)

    def set_keyable(self) -> None:
        """scalar plugをChannel BoxのKeyable状態に予約する。

        ``keyable=True``、``channelBox=False``へ設定する。変更は
        ``ModifierManager.do_it_dg()``の実行時に反映される。scalar
        compoundでは各scalar childへ展開する。
        """
        self._set_channel_box_state(
            keyable=True,
            channel_box=False,
            direct=False,
        )

    def set_keyable_direct(self) -> None:
        """scalar plugをChannel BoxのKeyable状態へ即時変更する。

        ``keyable=True``、``channelBox=False``へ設定する。
        scalar compoundでは各scalar childへ展開する。ModifierManagerの
        undo / redo対象外。
        """
        self._set_channel_box_state(
            keyable=True,
            channel_box=False,
            direct=True,
        )

    def set_channel_box(self) -> None:
        """scalar plugをNonkeyable Displayed状態に予約する。

        ``keyable=False``、``channelBox=True``へ設定する。変更は
        ``ModifierManager.do_it_dg()``の実行時に反映される。scalar
        compoundでは各scalar childへ展開する。
        """
        self._set_channel_box_state(
            keyable=False,
            channel_box=True,
            direct=False,
        )

    def set_channel_box_direct(self) -> None:
        """scalar plugをNonkeyable Displayed状態へ即時変更する。

        ``keyable=False``、``channelBox=True``へ設定する。
        scalar compoundでは各scalar childへ展開する。ModifierManagerの
        undo / redo対象外。
        """
        self._set_channel_box_state(
            keyable=False,
            channel_box=True,
            direct=True,
        )

    def set_hidden(self) -> None:
        """scalar plugをNonkeyable Hidden状態に予約する。

        ``keyable=False``、``channelBox=False``へ設定する。
        scalar compoundでは各scalar childへ展開する。
        ``MFnAttribute.hidden``は変更しない。変更は
        ``ModifierManager.do_it_dg()``の実行時に反映される。
        """
        self._set_channel_box_state(
            keyable=False,
            channel_box=False,
            direct=False,
        )

    def set_hidden_direct(self) -> None:
        """scalar plugをNonkeyable Hidden状態へ即時変更する。

        ``keyable=False``、``channelBox=False``へ設定し、
        scalar compoundでは各scalar childへ展開する。
        ``MFnAttribute.hidden``は変更しない。ModifierManagerの
        undo / redo対象外。
        """
        self._set_channel_box_state(
            keyable=False,
            channel_box=False,
            direct=True,
        )
