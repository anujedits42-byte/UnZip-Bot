# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/UnZip-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/UnZip-Bot



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

active_tasks = {}


@Client.on_message(filters.command("start"))
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📍 Update Channel", url="https://t.me/log_channel_a"),
            ],
            [
                InlineKeyboardButton("👥 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/log_channel_a"),
                InlineKeyboardButton("👩‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/anujedits76"),
            ] 
        ]
    )

    start_message = (
        f"✨ Hᴇʏ {message.from_user.first_name} Wᴇʟᴄᴏᴍᴇ!\n\n"
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

    await message.reply(start_message, reply_markup=reply_markup, parse_mode="html")


# Callback query handler
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()


@Client.on_message(filters.command("help"))
async def help_command(client, message):
    help_message = (
        "Hᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ:\n\n"
        "/start - Sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ɢᴇᴛ ᴛʜᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇꜱꜱᴀɢᴇ\n"
        "/help - Gᴇᴛ ʜᴇʟᴘ ᴏɴ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ\n\n"
        "Tᴏ ᴜɴᴢɪᴘ ᴀ ꜰɪʟᴇ, ꜱɪᴍᴘʟʏ ꜱᴇɴᴅ ᴍᴇ ᴀ ZIP ꜰɪʟᴇ ᴀɴᴅ I ᴡɪʟʟ ᴇxᴛʀᴀᴄᴛ ɪᴛꜱ ᴄᴏɴᴛᴇɴᴛꜱ ᴀɴᴅ ꜱᴇɴᴅ ᴛʜᴇᴍ ʙᴀᴄᴋ ᴛᴏ ʏᴏᴜ.\n\n"
        "©️ Cʜᴀɴɴᴇʟ : <a href='https://t.me/anujedits76'>𝐀𝐧𝐮𝐣 𝐊𝐮𝐦𝐚𝐫</a>"
    )
    await message.reply(help_message, parse_mode="html")



@Client.on_callback_query(filters.regex("cancel_unzip"))
async def cancel_callback(client, callback_query):
    user_id = callback_query.from_user.id

    if user_id in active_tasks:
        task = active_tasks[user_id]
        task.cancel()
        await callback_query.answer("⛔ Unzipping has been cancelled.", show_alert=True)
    else:
        await callback_query.answer("⚠️ No ongoing unzip operation.", show_alert=True)

