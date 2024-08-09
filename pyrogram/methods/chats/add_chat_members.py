#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Union, List

import pyrogram
from pyrogram import raw
from pyrogram.errors import UserPrivacyRestricted,UserAlreadyParticipant,UserNotParticipant,ChatAdminRequired


class AddChatMembers:
    async def sub_add_chat_members(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_ids: Union[Union[int, str], List[Union[int, str]]],
        forward_limit: int = 100
    ) -> bool:
        """Add new chat members to a group, supergroup or channel

        ********************
        Fixed By @SubLiquidX
        ********************

        .. include:: /_includes/usable-by/users.rst
        Parameters:
            chat_id (``int`` | ``str``):
                The group, supergroup or channel id

            user_ids (``int`` | ``str`` | List of ``int`` or ``str``):
                Users to add in the chat
                You can pass an ID (int), username (str) or phone number (str).
                Multiple users can be added by passing a list of IDs, usernames or phone numbers.

            forward_limit (``int``, *optional*):
                How many of the latest messages you want to forward to the new members. Pass 0 to forward none of them.
                Only applicable to basic groups (the argument is ignored for supergroups or channels).
                Defaults to 100 (max amount).

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Add one member to a group or channel
                await app.sub_add_chat_members(chat_id, user_id)

                # Add multiple members to a group or channel
                await app.sub_add_chat_members(chat_id, [user_id1, user_id2, user_id3])

                # Change forward_limit (for basic groups only)
                await app.sub_add_chat_members(chat_id, user_id, forward_limit=25)
        """
        if not isinstance(user_ids, list):
            user_ids = [user_ids]

        peer = await client.resolve_peer(chat_id)
        # Check if the client has admin rights in the channel/supergroup
        for user_id in user_ids:
            try:
                user_peer = await client.resolve_peer(user_id)
                await client.invoke(raw.functions.channels.GetParticipant(channel=peer, participant=user_peer))
                raise UserAlreadyParticipant
            except UserNotParticipant:
                pass  # User is not a participant, proceed to add them
            except ChatAdminRequired:
                pass  # User is not a participant, proceed to add them


        if isinstance(peer, raw.types.InputPeerChat):
            for user_id in user_ids:
                result = await client.invoke(
                    raw.functions.messages.AddChatUser(
                        chat_id=peer.chat_id,
                        user_id=await client.resolve_peer(user_id),
                        fwd_limit=forward_limit
                    )
                )
        else:
            result = await client.invoke(
                raw.functions.channels.InviteToChannel(
                    channel=peer,
                    users=[
                        await client.resolve_peer(user_id)
                        for user_id in user_ids
                    ]
                )
            )     
        if isinstance(result, types.messages.InvitedUsers):
            if result.missing_invitees:
                missing_user_ids = [invitee.user_id for invitee in result.missing_invitees]
                single_int = int(''.join(map(str, missing_user_ids)))
                missing_user = next(invitee for invitee in result.missing_invitees if invitee.user_id == single_int)
                if missing_user.premium_would_allow_invite == True:
                    raise UserPrivacyRestricted
                else:
                    raise UserPrivacyRestricted
            else:
                return True
        else:
            return True
