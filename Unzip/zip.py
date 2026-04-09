import os
import time
import shutil
import tempfile
import asyncio
from Unzip.config import Config
from pyrogram import Client, filters, enums
from pyunpack import Archive
from Unzip.progress import progress_for_pyrogram

SUPPORTED_FORMATS = ('.zip', '.rar', '.7z', '.tar', '.tar.gz', '.tgz', '.tar.bz2')

active_tasks = {}


@Client.on_message(filters.document)
async def handle_file(client, message):
    user_id = message.from_user.id
    document = message.document
    file_name = document.file_name.lower()

    download_message = None
    file_path = None
    extract_dir = None

    # ✅ File size check
    if document.file_size > Config.MAX_FILE_SIZE:
        return await message.reply("⚠️ File too large. Max allowed: 2GB")

    try:
        download_message = await message.reply("⏳ Downloading your file...")
        start = time.time()

        # ✅ Download file
        file_path = await message.download(
            file_name=document.file_name,
            progress=progress_for_pyrogram,
            progress_args=("⬇️ Downloading...", download_message, start)
        )

        # ✅ Check supported formats
        if file_name.endswith(SUPPORTED_FORMATS):
            await download_message.edit("📦 Extracting archive...")

            extract_dir = os.path.join(tempfile.gettempdir(), f'extracted_{user_id}')
            os.makedirs(extract_dir, exist_ok=True)

            # ✅ Async task
            task = asyncio.create_task(
                extract_and_send_files(client, message, file_path, extract_dir, download_message, start)
            )
            active_tasks[user_id] = task
            await task

        else:
            # ✅ If not archive → just re-upload
            await download_message.edit("⬆️ Uploading your file...")

            await client.send_document(
                chat_id=message.chat.id,
                document=file_path,
                caption=f"📄 `{document.file_name}`",
                parse_mode=enums.ParseMode.MARKDOWN,  # ✅ FIXED
                progress=progress_for_pyrogram,
                progress_args=("⬆️ Uploading...", download_message, start)
            )

            await download_message.edit("✅ File uploaded successfully.")

    except Exception as e:
        if download_message:
            await download_message.edit(f"❌ Error: {e}")
        else:
            await message.reply(f"❌ Error: {e}")

    finally:
        # ✅ Cleanup
        if file_path and os.path.exists(file_path):
            os.remove(file_path)

        if extract_dir and os.path.exists(extract_dir):
            shutil.rmtree(extract_dir)

        active_tasks.pop(user_id, None)


async def extract_and_send_files(client, message, file_path, extract_dir, download_message, start):
    try:
        Archive(file_path).extractall(extract_dir)
    except Exception as e:
        await download_message.edit(f"❌ Failed to extract: {e}")
        return

    await download_message.edit("📤 Preparing files to send...")

    # ✅ Walk through extracted files
    for root, _, files in os.walk(extract_dir):
        for file_name in files:
            extracted_file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(extracted_file_path, extract_dir)

            try:
                await client.send_document(
                    chat_id=message.chat.id,
                    document=extracted_file_path,
                    file_name=relative_path,
                    caption=f"📄 `{relative_path}`",
                    parse_mode=enums.ParseMode.MARKDOWN,  # ✅ FIXED
                    progress=progress_for_pyrogram,
                    progress_args=("⬆️ Uploading...", download_message, start)
                )

            except Exception as e:
                await message.reply(f"❌ Failed to upload `{relative_path}`: {e}")

    await download_message.edit("✅ All files have been extracted and sent.")
