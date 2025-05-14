# ======================= Imports =======================
import os
import datetime
from dotenv import load_dotenv

# Alpaca Trading and Data Imports
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderStatus
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.live import StockDataStream

# ================== Environment Setup ==================
load_dotenv()

# Load API credentials from .env
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

# =================== Trading Client ====================
tradingClient = TradingClient(
    ALPACA_API_KEY,
    ALPACA_SECRET_KEY,
    paper=True
)

# Account Summary
account_info = tradingClient.get_account()
print("Buying Power:", account_info.buying_power)
print("Cash:", account_info.cash)

# ================ Historical Data Client ===============
data_client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)

# Fetch historical stock bars for AAPL (last 7 days)
request = StockBarsRequest(
    symbol_or_symbols="AAPL",
    timeframe=TimeFrame.Day,
    start=datetime.datetime.now() - datetime.timedelta(days=7)
)
apple_data = data_client.get_stock_bars(request)

# Display fetched data
print("\nApple (AAPL) stock data:")
for bar in apple_data.data["AAPL"]:
    date = bar.timestamp.strftime("%Y-%m-%d")
    print(f"Date: {date}, Close: ${bar.close}")

# =================== Market Orders =====================

# --- Buy 1 share of AAPL ---
buy_order = MarketOrderRequest(
    symbol="AAPL",
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY
)

try:
    buy_order_result = tradingClient.submit_order(buy_order)
    print(f"\nMarket buy order submitted for AAPL: {buy_order_result.id}")
except Exception as e:
    print(f"Error submitting AAPL buy order: {e}")

# --- Sell 1 share of AAPL ---
sell_order = MarketOrderRequest(
    symbol="AAPL",
    qty=1,
    side=OrderSide.SELL,
    time_in_force=TimeInForce.DAY
)

try:
    sell_order_result = tradingClient.submit_order(sell_order)
    print(f"\nSell Order Submitted: {sell_order_result.id}")
    print(f"Status: {sell_order_result.status}")
except Exception as e:
    print(f"Error submitting AAPL sell order: {e}")

# =================== Limit Order =======================

limit_order = LimitOrderRequest(
    symbol="AAPL",
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY,
    limit_price=150.00
)

try:
    limit_order_result = tradingClient.submit_order(limit_order)
    print(f"\nLimit Order Submitted: {limit_order_result.id}")
    print(f"Status: {limit_order_result.status}")
except Exception as e:
    print(f"Error submitting AAPL limit order: {e}")

# =================== Get Orders ========================

try:
    request_params = GetOrdersRequest(
        status=OrderStatus.NEW,
        side=OrderSide.SELL
    )
    orders = tradingClient.get_orders(filter=request_params)
    print("\nFiltered Orders (New & Sell):")
    for order in orders:
        print(f"ID: {order.id}, Symbol: {order.symbol}, Qty: {order.qty}, Status: {order.status}")
except Exception as e:
    print(f"Error fetching filtered orders: {e}")

# =============== Position Management ===================

print("\n--- POSITION MANAGEMENT ---")

# View all open positions
try:
    positions = tradingClient.get_all_positions()
    if positions:
        print("\nCurrent Open Positions:")
        for position in positions:
            print(f"Symbol: {position.symbol}, Qty: {position.qty}, Market Value: ${position.market_value}")
            print(f"  Unrealized P/L: ${position.unrealized_pl} ({float(position.unrealized_plpc):.2%})")
    else:
        print("No open positions found.")
except Exception as e:
    print(f"Error fetching positions: {e}")

# Close a specific position (AAPL)
try:
    close_result = tradingClient.close_position('AAPL')
    print(f"\nClosed position: {close_result.symbol}")
except Exception as e:
    print(f"Error closing specific position: {e}")

# Close all positions (optional: cancel open orders)
try:
    cancel_orders = True
    close_all_result = tradingClient.close_all_positions(cancel_orders=cancel_orders)
    print("\nAll positions closed:")
    for symbol, result in close_all_result.items():
        if 'success' in result and result['success']:
            print(f"✓ {symbol}: Successfully closed")
        else:
            print(f"✗ {symbol}: Failed to close - {result.get('message', 'Unknown error')}")
except Exception as e:
    print(f"Error closing all positions: {e}")

# ================ Real-Time Streaming ==================

# Create live data stream instance
stream = StockDataStream(ALPACA_API_KEY, ALPACA_SECRET_KEY)

# Async callback to handle live trade data
async def handle_trade(data):
    print("\n----- New Trade Data -----")
    print(f"Symbol: {data.symbol}")
    print(f"Price: ${data.price}")
    print(f"Size: {data.size}")
    print(f"Timestamp: {data.timestamp}")
    print(f"Exchange: {data.exchange}")
    print(f"ID: {data.id}")
    print("--------------------------\n")

# Subscribe to trade updates for AAPL
stream.subscribe_trades(handle_trade, "AAPL")

# Start the stream (blocking call)
print("Starting trade stream for AAPL. Press Ctrl+C to stop.")
stream.run()
