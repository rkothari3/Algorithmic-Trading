import yfinance as yf
import pandas as pd
import os
from requests_html import HTMLSession

class TradingOpportunities:
    def __init__(self, num_stocks=25, num_crypto=25):
        """
        Grabs the top 25 stock losers and 25 top traded crypto assets from yfinance.
        Determines trading opportunities using simple technical trading indicators like Bollinger Bands and RSI.

        Methods:
            • raw_get_daily_info(): Grabs a provided site and transforms HTML to a pandas df
            • get_trading_opportunities(): Grabs df from raw_get_daily_info() and provides just the top "n" losers declared by user in n_stocks and "n" amount of top of most popular crypto assets to examine
            • get_asset_info(): a df can be provided to specify which assets you'd like info for since this method is used in the Alpaca class. If no df argument is passed then tickers from get_trading_opportunities() method are used.
        """
        self.num_stocks = num_stocks
        self.num_crypto = num_crypto

    def raw_get_daily_info(self, site):
        """
        Purpose: Scrapes a given website (like Yahoo Finance) and converts the HTML table into a Pandas DataFrame.

        How It Works:
            - Uses HTMLSession from requests_html to fetch the webpage.
            - Extracts HTML tables from the page using pd.read_html.
            - Returns the first table as a DataFrame.
        """
        session = HTMLSession()
        response = session.get(site)
        tables = pd.read_html(response.html.raw_html)
        df = tables[0].copy()
        df.columns = tables[0].columns  # Fixed typo here
        session.close()
        return df
