import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient  # Allows us to connect to our account
from alpaca.data.historical import StockHistoricalDataClient  # To create historical data client
from alpaca.data.requests import StockBarsRequest  # To fetch market data
from alpaca.data.timeframe import TimeFrame
import datetime
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# Load environment variables
load_dotenv()

# Get API keys from environment variables
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

tradingClient = TradingClient(
    ALPACA_API_KEY,
    ALPACA_SECRET_KEY,
    paper=True
)
account_info = tradingClient.get_account()

# Fetch Buying Power
print(account_info.buying_power)
# Cash
print(account_info.cash)

# Create a data client for market data
data_client = StockHistoricalDataClient(
    ALPACA_API_KEY,
    ALPACA_SECRET_KEY
)

# Fetching market data -> e.g. AAPL
# Get 7 days of daily data for Apple
request = StockBarsRequest(
    symbol_or_symbols="AAPL",
    timeframe=TimeFrame.Day,
    start=datetime.datetime.now() - datetime.timedelta(days=7)
)

apple_data = data_client.get_stock_bars(request)

# Print the data
print("Apple (AAPL) stock data:")
for bar in apple_data.data["AAPL"]:
    date = bar.timestamp.strftime("%Y-%m-%d")
    print(f"Date: {date}, Close: ${bar.close}")

# ---Submitting Order---#
# Buy 1 share of Apple
buy_order = MarketOrderRequest(
    symbol="AAPL",
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY
)

# Submit purchase order
try:
    buy_order_result = tradingClient.submit_order(buy_order)
    print(f"Market buy order submitted for AAPL: {buy_order_result.id}")
except Exception as e:
    print(f"Error submitting AAPL buy order: {e}")

# Sell 1 share of AAPL
sell_order = MarketOrderRequest(
    symbol="AAPL",
    qty = 1,
    side = OrderSide.SELL,
    time_in_force=TimeInForce.DAY
)
# Submit sell order
try:
    sell_order_result = tradingClient.submit_order(sell_order)
    print(f"\nSell Order Submitted: {sell_order_result.id}")
    print(f"Status: {sell_order_result.status}")
except Exception as e:
    print(f"Error submitting AAPL sell order: {e}")