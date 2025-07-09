import os
from dotenv import load_dotenv
from bot import TradingBot

# Load API keys from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Create bot instance
bot = TradingBot(API_KEY, API_SECRET)

# CLI input
print("🔁 Welcome to Binance Futures Testnet Trading Bot 🔁")

symbol = input("Enter trading symbol (e.g., BTCUSDT): ").upper()
side = input("Enter side (BUY or SELL): ").upper()
order_type = input("Enter order type (MARKET or LIMIT): ").upper()
quantity = float(input("Enter quantity: "))

price = None
if order_type == "LIMIT":
    price = float(input("Enter price: "))

# Place order
order = bot.place_order(symbol, side, order_type, quantity, price)

# Output result
if order:
    print("✅ Order placed successfully!")
else:
    print("❌ Order failed.")
