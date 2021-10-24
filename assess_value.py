import yfinance as yf
from get_all_tickers import get_tickers as gt
import json
import numpy as np
from numpy import sin
from numpy import arange
import scipy.optimize
from matplotlib import pyplot


def func(x, a, b, c, d):
	return a * sin(b - x) + c * x**2 + d
    
def linRegTicker(t):
    x = list()
    y = list() 
    i = 0

    ticker_data = yf.Ticker(t)
    ticker_historical = ticker_data.history(period="max", interval="3mo")
    
    for index, row in ticker_historical.iterrows():
        if not np.isnan(row['Low']):
            y.append(row['Low'])
            x.append(i)
        i = i+1
    x_arr = np.array(x)
    y_arr = np.array(y)


    popt, _ = scipy.optimize.curve_fit(func,  x_arr,  y_arr)
    
    a, b, c, d = popt
   

    pyplot.scatter(x_arr,y_arr)
    x_line = arange(min(x_arr), max(x_arr), 1)    
    y_line = func(x_line, a, b, c, d)

    pyplot.plot(x_line, y_line, '--', color='red')
    pyplot.savefig("plot")
    
    return 2

p = linRegTicker("TWTR")

# list_of_tickers = gt.get_tickers()


# msft = yf.Ticker("MSFT")
# msft_dict = msft.info
# # print(msft_dict)

# twtr = yf.Ticker("TWTR")
# twtr_dict =twtr.info
# print(twtr_dict)
# # print(list_of_tickers)
# with open('twitter_info.txt', 'w') as twitter_info:
#      twitter_info.write(json.dumps(twtr_dict))

# twtr_historical = twtr.history(period="max", interval="1mo")
# print(twtr_historical["Low"])
# print(type(twtr_historical).__name__)
# for index, row in twtr_historical.iterrows():
#     print(row['Low'])
