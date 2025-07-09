# Binance_trading_bot
A Python trading bot for Binance Futures Testnet. Places Market and Limit Buy/Sell orders using CLI. Secure API handling and testnet-safe environment.
# 🔁 Binance Futures Testnet Trading Bot

A Python-based trading bot that allows users to place **Market** and **Limit** orders (Buy/Sell) on the **Binance Futures Testnet** using command-line inputs. This project is built for learning and testing, with no real money involved.

---

## 📌 Features

- Place Market and Limit orders on Binance Futures Testnet
- Supports both BUY and SELL order types
- Secure API key handling via `.env` file
- Logs all order responses and errors to `log.txt`
- Command-line interface for easy interaction

---

## 🛠 Technologies Used

- Python 3
- python-binance
- python-dotenv
- logging


---

## 📁 Project Structure

binance-trading-bot/
├── bot.py # Trading logic using Binance API
├── main.py # CLI for user input
├── .env.example # Sample environment file (no secrets)
├── log.txt # Order logs and errors
├── README.md # Project documentation
