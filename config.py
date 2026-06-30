"""
=========================================================
CONFIG
=========================================================
"""

from dotenv import load_dotenv
import os

load_dotenv()

# ==========================
# API
# ==========================

API_KEY = os.getenv("API_KEY")

# ==========================
# TELEGRAM
# ==========================

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

# ==========================
# MARKET
# ==========================

SYMBOL = "EUR/USD"

INTERVAL = "15min"

OUTPUTSIZE = 5000

# ==========================
# BOT
# ==========================

CHECK_INTERVAL = 10

TIMEZONE = "Asia/Ho_Chi_Minh"

# ==========================
# DATABASE
# ==========================

DATABASE_FILE = "database/signal.db"

# ==========================
# LOG
# ==========================

LOG_FOLDER = "logs"

LOG_FILE = "logs/eu_alert_bot.log"

LOG_LEVEL = "INFO"
print("API_KEY =", API_KEY)