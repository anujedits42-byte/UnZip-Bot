from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ParseMode

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

    # ✅ Safe username (kabhi None nahi hoga)
    name = message.from_user.first_name if message.from_user else "User"

    start_message = f"""
✨ <b>Hᴇʏ {name} Wᴇʟᴄᴏᴍᴇ!</b>

📂 <b>Yᴏᴜʀ ᴜʟᴛɪᴍᴀᴛᴇ Aʀᴄʜɪᴠᴇ Exᴛʀᴀᴄᴛᴏʀ Bᴏᴛ!</b>

🚀 <b>Fᴇᴀᴛᴜʀᴇꜱ:</b>
• Iɴꜱᴛᴀɴᴛ ZIP, RAR, 7Z, TAR ᴇxᴛʀᴀᴄᴛɪᴏɴ  
• Fᴀꜱᴛ & Sᴇᴄᴜʀᴇ ᴘʀᴏᴄᴇꜱꜱɪɴɢ  
• Dɪʀᴇᴄᴛ URL Sᴜᴘᴘᴏʀᴛ  
• Pᴀꜱꜱᴡᴏʀᴅ Pʀᴏᴛᴇᴄᴛᴇᴅ Aʀᴄʜɪᴠᴇꜱ  

⚠️ <b>18+ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ꜱᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ!</b>

📤 Jᴜꜱᴛ ꜱᴇɴᴅ ᴀɴʏ ᴀʀᴄʜɪᴠᴇ ꜰɪʟᴇ ᴛᴏ ꜱᴛᴀʀᴛ!

©️ Channel : <a href='https://t.me/anujedits76'>𝐀𝐧𝐮𝐣 𝐊𝐮𝐦𝐚𝐫</a>
"""

    await message.reply(
        start_message,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML
    )


# ❌ Cancel button (safe)
@Client.on_callback_query(filters.regex("^cancel$"))
async def cancel(client, callback_query):
    try:
        await callback_query.message.delete()
    except:
        pass


# 📖 Help command
@Client.on_message(filters.command("help"))
async def help_command(client, message):
    help_message = """
📖 <b>Hᴇʟᴘ Mᴇɴᴜ</b>

/start - Sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ  
/help - Gᴇᴛ ʜᴇʟᴘ  

📦 Tᴏ ᴜɴᴢɪᴘ: ꜱᴇɴᴅ ᴀ ZIP/RAR/7Z ғɪʟᴇ

©️ Cʜᴀɴɴᴇʟ : <a href='https://t.me/anujedits76'>𝐀𝐧𝐮𝐣 𝐊𝐮𝐦𝐚𝐫</a>
"""

    await message.reply(help_message, parse_mode=ParseMode.HTML)


# ⛔ Cancel unzip
@Client.on_callback_query(filters.regex("^cancel_unzip$"))
async def cancel_callback(client, callback_query):
    user_id = callback_query.from_user.id

    if user_id in active_tasks:
        task = active_tasks[user_id]
        task.cancel()
        await callback_query.answer("⛔ Unzipping cancelled", show_alert=True)
    else:
        await callback_query.answer("⚠️ No active task", show_alert=True)
