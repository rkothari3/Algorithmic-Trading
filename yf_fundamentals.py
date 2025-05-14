import yfinance as yf

def main():
    # Define the ticker symbol
    ticker_symbol = "MSFT"
    
    # Create a Ticker object
    ticker_data = yf.Ticker(ticker_symbol)
    
    # Get and print general information about the ticker
    print("----- Info -----")
    info = ticker_data.info
    print(info)

    # Retrieve and print historical market data
    print("\n----- Historical Data (last 1 month) -----")
    hist = ticker_data.history(period="1mo")
    print(hist)

    # Retrieve and print dividend data
    print("\n----- Dividends -----")
    dividends = ticker_data.dividends
    print(dividends)

    # Retrieve and print stock splits data
    print("\n----- Splits -----")
    splits = ticker_data.splits
    print(splits)

    # Retrieve and print corporate actions (dividends and splits)
    print("\n----- Actions -----")
    actions = ticker_data.actions
    print(actions)
    
    # Retrieve and print earnings data
    print("\n----- Earnings -----")
    earnings = ticker_data.earnings
    print(earnings)

if __name__ == "__main__":
    main()