import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
tickers_list = ['NFLX', 'AAPL', 'AMZN', 'FB', 'GOOG']

# Import pandas
data = pd.DataFrame(columns=tickers_list)



for ticker in tickers_list:
    data[ticker] = yf.download(ticker,'2015-01-01','2020-06-01')['Adj Close']

data.head()
data.plot(figsize=(12, 7))

plt.legend()
plt.title("Stock Price", fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()