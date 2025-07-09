from binance.client import Client
import logging

class TradingBot:
    def __init__(self, api_key, api_secret):
        # Connect to Binance Futures Testnet
        self.client = Client(api_key, api_secret, testnet=True)
        
        # Setup logging
        logging.basicConfig(filename='log.txt', level=logging.INFO)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='LIMIT',
                    timeInForce='GTC',
                    quantity=quantity,
                    price=price
                )
            else:
                print("❌ Unsupported order type.")
                return None

            # Log and return the order
            logging.info(f"✅ ORDER SUCCESS: {order}")
            return order

        except Exception as e:
            logging.error(f"❌ ERROR placing order: {e}")
            print(f"Error: {e}")
            return None
