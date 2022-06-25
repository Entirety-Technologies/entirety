# pip install yfinance
import yfinance as yf

class YahooDC:

    def __init__(self):
        pass

    def get_data(self, ticker, interval, start_date, end_date):
        '''
        using this data source, you can fetch within last 60 days data
        periods: [1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max]
        intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
        ticker:'MSFT',interval:'1d',start_date:'2022-06-01',end_date:'2022-06-20'
        '''
        ticker_obj = yf.Ticker(ticker.upper())
        return ticker_obj.history(
            interval=interval,
            start=start_date,
            end=end_date
            )