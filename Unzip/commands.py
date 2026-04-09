from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ParseMode   # ✅ IMPORTANT

active_tasks = {}


@Client.on_message(filters.command("start"))
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📍 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url="https://t.me/log_channel_a"),
            ],
            [
                InlineKeyboardButton("👥 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/log_channel_a"),
                InlineKeyboardButton("👩‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/anujedits76"),
            ] 
        ]
    )

    name = message.from_user.first_name if message.from_user else "User"

    start_message = (
        f"✨ Hᴇʏ {name} Wᴇʟᴄᴏᴍᴇ!\n\n"
        "📂 Yᴏᴜʀ ᴜʟᴛɪᴍᴀᴛᴇ Aʀᴄʜɪᴠᴇ Exᴛʀᴀᴄᴛᴏʀ Bᴏᴛ!\n\n"

        "🚀 Fᴇᴀᴛᴜʀᴇꜱ:\n"
        "• Iɴꜱᴛᴀɴᴛ ZIP, RAR, 7Z, TAR ᴇxᴛʀᴀᴄᴛɪᴏɴ\n"
        "• Fᴀꜱᴛ & Sᴇᴄᴜʀᴇ ᴘʀᴏᴄᴇꜱꜱɪɴɢ\n"
        "• Dɪʀᴇᴄᴛ URL Sᴜᴘᴘᴏʀᴛ\n"
        "• Pᴀꜱꜱᴡᴏʀᴅ Pʀᴏᴛᴇᴄᴛᴇᴅ Aʀᴄʜɪᴠᴇꜱ\n\n"

        "⚠️ 18+ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ꜱᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ!\n\n"

        "📤 Jᴜꜱᴛ ꜱᴇɴᴅ ᴀɴʏ ᴀʀᴄʜɪᴠᴇ ꜰɪʟᴇ ᴛᴏ ꜱᴛᴀʀᴛ!\n\n"

        "©️ Channel : <a href='https://t.me/anujedits76'>𝐀𝐧𝐮𝐣 𝐊𝐮𝐦𝐚𝐫</a>"
    )

    await message.reply(
        start_message,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML   # ✅ FIXED
    )


# Cancel button
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()


# Help command
@Client.on_message(filters.command("help"))
async def help_command(client, message):
    help_message = (
        "Hᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ:\n\n"
        "/start - Sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n"
        "/help - Gᴇᴛ ʜᴇʟᴘ\n\n"
        "Tᴏ ᴜɴᴢɪᴘ ᴀ ꜰɪʟᴇ, ꜱᴇɴᴅ ᴀ ZIP ꜰɪʟᴇ.\n\n"
        "©️ Cʜᴀɴɴᴇʟ : <a href='https://t.me/anujedits76'>𝐀𝐧𝐮𝐣 𝐊𝐮𝐦𝐚𝐫</a>"
    )

    await message.reply(help_message, parse_mode=ParseMode.HTML)  # ✅ FIXED


# Cancel unzip
@Client.on_callback_query(filters.regex("cancel_unzip"))
async def cancel_callback(client, callback_query):
    user_id = callback_query.from_user.id

    if user_id in active_tasks:
        task = active_tasks[user_id]
        task.cancel()
        await callback_query.answer("⛔ Unzipping has been cancelled.", show_alert=True)
    else:
        await callback_query.answer("⚠️ No ongoing unzip operation.", show_alert=True)
