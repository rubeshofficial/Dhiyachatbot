from flask import Flask
import threading
import asyncio
from pyrogram import idle
from RAUSHAN import LOGGER, AMBOT

# 🟢 IMPORTANT: Import handlers to register /start, /help etc.
import RAUSHAN.modules.start  # This line is REQUIRED

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

# Flask runner
def run_flask():
    app.run(host="0.0.0.0", port=8000)

# Async bot runner
async def run_bot():
    LOGGER.info("The PURVI CHAT BOT Started.")
    bot = AMBOT()
    await bot.start()
    await idle()

if __name__ == "__main__":
    # Start Flask in background
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Run the Telegram bot
    asyncio.run(run_bot())  # ✅ Fixed the missing parenthesis here
