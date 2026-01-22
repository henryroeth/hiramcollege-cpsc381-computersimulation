import yfinance as yf

# Download the data
data = yf.download("AAPL", start="2018-01-01", end="2023-01-01", interval="1d")

# Save data to CSV
data.to_csv("data/appl_6mo_data.csv")
