from flask import Flask
import threading
from RAUSHAN import LOGGER, AMBOT

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

def run_bot():
    LOGGER.info("The PURVI CHAT BOT Started.")
    AMBOT().start()
    idle()  # from pyrogram.idle import idle

if __name__ == "__main__":
    # Create and start the Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Run the Telegram bot in the main thread (non-blocking)
    run_bot()
    
