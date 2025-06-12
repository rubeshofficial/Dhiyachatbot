from flask import Flask
import threading
import asyncio
from pyrogram import idle
from RAUSHAN import LOGGER, AMBOT

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

# Start Flask in a background thread
def run_flask():
    app.run(host="0.0.0.0", port=8000)

# Async bot runner
async def run_bot():
    LOGGER.info("The PURVI CHAT BOT Started.")
    bot = AMBOT()
    await bot.start()
    print("Bot is running...")
    await idle()

if __name__ == "__main__":
    # Run Flask in a separate daemon thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Run the async bot
    asyncio.run(run_bot())
    
