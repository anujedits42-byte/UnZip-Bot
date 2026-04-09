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
            InlineKeyboardButton("👥 Support Group", url="https://t.me/log_channel_a"),
            InlineKeyboardButton("👩‍💻 Developer", url="https://t.me/anujedits76"),
        ] 
   ]
  )
    start_message = (
    start_message = (
    f"✨ Hᴇʏ {message.from_user.first_name} Wᴇʟᴄᴏᴍᴇ!\n\n"
    "📂 Yᴏᴜʀ ᴜʟᴛɪᴍᴀᴛᴇ Aʀᴄʜɪᴠᴇ Exᴛʀᴀᴄᴛᴏʀ Bᴏᴛ!\n\n"

    "🚀 Fᴇᴀᴛᴜʀᴇꜱ:\n"
    "• Iɴꜱᴛᴀɴᴛ ZIP, RAR, 7Z, TAR ᴇxᴛʀᴀᴄᴛɪᴏɴ\n"
    "• Fᴀꜱᴛ & Sᴇᴄᴜʀᴇ ᴘʀᴏᴄᴇꜱꜱɪɴɢ\n"
    "• Dɪʀᴇᴄᴛ URL Sᴜᴘᴘᴏʀᴛ\n"
    "• Pᴀꜱꜱᴡᴏʀᴅ Pʀᴏᴛᴇᴄᴛᴇᴅ Aʀᴄʜɪᴠᴇꜱ\n\n"

    "⚠️ 18+ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ꜱᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ!\n\n"

    "📤 Jᴜꜱᴛ ꜱᴇɴᴅ ᴀɴʏ ᴀʀᴄʜɪᴠᴇ ꜰɪʟᴇ ᴛᴏ ꜱᴛᴀʀᴛ!"
    )
    await message.reply(start_message, reply_markup=reply_markup)


# Callback query handler
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()


@Client.on_message(filters.command("help"))
async def help_command(client, message):
    help_message = (
        "Here are the commands you can use:\n\n"
        "/start - Start the bot and get the welcome message\n"
        "/help - Get help on how to use the bot\n\n"
        "To unzip a file, simply send me a ZIP file and I will extract its contents and send them back to you.\n\n"
        "©️ Channel : <a href='https://t.me/anujedits76'>𝐀𝐧𝐮𝐣 𝐊𝐮𝐦𝐚𝐫</a>"
    )
    await message.reply(help_message)



@Client.on_callback_query(filters.regex("cancel_unzip"))
async def cancel_callback(client, callback_query):
    user_id = callback_query.from_user.id

    if user_id in active_tasks:
        task = active_tasks[user_id]
        task.cancel()
        await callback_query.answer("⛔ Unzipping has been cancelled.", show_alert=True)
    else:
        await callback_query.answer("⚠️ No ongoing unzip operation.", show_alert=True)

