from flask import Flask
import threading
import asyncio
from RAUSHAN import LOGGER, AMBOT

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

def run_bot():
    LOGGER.info("The PURVI CHAT BOT Started.")
    bot = AMBOT()
    await bot.start()
    print("Bot is running...")
    await idle()
    

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Run the async bot using asyncio
    asyncio.run(run_bot())
    
