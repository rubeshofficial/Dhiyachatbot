from flask import Flask
import threading
import signal
import sys
from RAUSHAN import LOGGER, AMBOT

# Create the Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "PURVI CHAT BOT is running"

# Function to run the Flask server
def run_flask():
    try:
        app.run(host="0.0.0.0", port=8000, debug=False, use_reloader=False)
    except Exception as e:
        LOGGER.error(f"Flask error: {e}")

# Function to run the chatbot
def run_bot():
    try:
        LOGGER.info("The PURVI CHAT BOT Started.")
        AMBOT().run()
    except Exception as e:
        LOGGER.error(f"Bot error: {e}")

# Handle shutdown gracefully
def handle_shutdown(signum, frame):
    LOGGER.info("Shutdown signal received. Exiting...")
    sys.exit(0)

# Register signal handlers
signal.signal(signal.SIGINT, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)

if __name__ == "__main__":
    # Start Flask server in a background thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Run the bot in the main thread
    run_bot()
    
