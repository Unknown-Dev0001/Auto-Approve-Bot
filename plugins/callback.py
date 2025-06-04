from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "start":
        await query.message.edit_text(
            text.START.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇆', url=f"https://telegram.me/AJRAxBot?startgroup=true&admin=invite_users")],
                [InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
                 InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help')],
                [InlineKeyboardButton('⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇆', url=f"https://telegram.me/AJRAxBot?startchannel=true&admin=invite_users")]
            ])
        )

    elif query.data == "help":
        await query.message.edit_text(
            text.HELP.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('ᴜᴩᴅᴀᴛᴇꜱ', url='https://telegram.me/BotVerseRavi'),
                 InlineKeyboardButton('ꜱᴜᴩᴩᴏʀᴛ', url='https://telegram.me/BotVerseRaviSupport')],
                [InlineKeyboardButton('ʙᴀᴄᴋ', callback_data="start"),
                 InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data="close")]
            ])
        )

    elif query.data == "about":
        await query.message.edit_text(
            text.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('💥 ᴜᴩᴅᴀᴛᴇꜱ', url='https://t.me/BotVerseRavi'),
                 InlineKeyboardButton('👨‍💻 ᴏᴡɴᴇʀ', url='https://telegram.me/Unknown_RK01')],
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
            ])
        )

    elif query.data == "close":
        await query.message.delete()
