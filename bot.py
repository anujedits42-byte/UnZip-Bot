from pyrogram import Client
from Unzip.config import Config

# 🚀 Create client
app = Client(
    "unzip_bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=dict(root="Unzip")
)


# ✅ Startup event
@app.on_message()
async def alive_check(client, message):
    pass  # optional (ignore)


# 🔥 Main runner
if __name__ == "__main__":
    try:
        print("🚀 Starting UnZip Bot...")
        app.run()
        print("✅ Bot stopped")
    except Exception as e:
        print(f"❌ Error while running bot: {e}")
