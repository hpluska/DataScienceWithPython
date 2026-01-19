
import yfinance as yf
ticker_symbol = "AAPL"  # Example stock
ticker = yf.Ticker(ticker_symbol)
print(ticker.info)