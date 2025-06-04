from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant, ChannelInvalid, ChannelPrivate
from config import AUTH_CHANNELS
from typing import List, Tuple

async def get_fsub(bot: Client, message: Message) -> bool:
    user_id = message.from_user.id
    bot_username = (await bot.get_me()).username
    not_joined_channels: List[Tuple[str, str]] = []

    for channel_id in AUTH_CHANNELS:
        try:
            # Check if user is a participant
            await bot.get_chat_member(channel_id, user_id)
        except UserNotParticipant:
            try:
                chat = await bot.get_chat(channel_id)
                # Try getting invite link or export a new one
                invite_link = chat.invite_link
                if not invite_link:
                    invite_link = await bot.export_chat_invite_link(channel_id)
                not_joined_channels.append((chat.title, invite_link))
            except (ChannelPrivate, ChannelInvalid):
                print(f"❌ Bot cannot access channel ID: {channel_id}. Check admin rights or ID.")
                continue
        except Exception as e:
            print(f"⚠️ Unexpected error checking channel {channel_id}: {e}")
            continue

    if not_joined_channels:
        # Build inline keyboard
        join_buttons = []
        for i in range(0, len(not_joined_channels), 2):
            row = [
                InlineKeyboardButton(
                    f"{i + 1}. {title}", url=link
                )
                for title, link in not_joined_channels[i:i + 2]
            ]
            join_buttons.append(row)

        # Add "Try Again" button
        join_buttons.append([
            InlineKeyboardButton("🔄 Try Again", url=f"https://t.me/{bot_username}?start=start")
        ])

        await message.reply(
            f"**🎭 {message.from_user.mention}, you haven’t joined the required channel(s).\nPlease join by clicking the button(s) below.**",
            reply_markup=InlineKeyboardMarkup(join_buttons),
            quote=True
        )
        return False

    return True
