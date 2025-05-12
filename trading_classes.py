'''
Trading Opportunities class:
Scrapes YahooFinance, and identifies trading opp.
based on top losing stocks and popular crytpo assets.

- Two primary methods:

1) get_trading_opportunities()
This method scrapes YahooFinance! using the yfinance package to obtain the top losing stocks of the day and most popular crypto assets. It first gets the top losing stocks by percentage change for the day using get_day_losers. Then, it obtains the top traded crypto assets by market cap using get_top_crypto.

2) get_asset_info()
'''