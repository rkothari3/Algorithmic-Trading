class TradingOpportunities:
    
    def __init__(self, num_stocks=25, num_crypto=25):
        """
        - Grabs the top 25 stock losers and 25 top traded crypto assets from yfinance.
        - Determines trading opportunities using simple technical trading indicators like Bollinger Bands and RSI.
        
        Methods:
            • raw_get_daily_info(): Grabs a provided site and transforms HTML to a pandas df
            • get_trading_opportunities(): Grabs df from raw_get_daily_info() and provides just the top "n" losers declared by user in n_stocks and "n" amount of top of most popular crypto assets to examine
            • get_asset_info(): a df can be provided to specify which assets you'd like info for since this method is used in the Alpaca class. If no df argument is passed then tickers from get_trading_opportunities() method are used.
        """
        self.num_stocks = num_stocks
        self.num_crypto = num_crypto
    
    def raw_get_daily_info(self, site):
        """
        - Takes a site and turns its HTML to a pandas df
        - 
        """