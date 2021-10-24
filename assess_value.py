# @author Shaw Young
# @version 10.24.21

import yfinance as yf
import numpy as np
from numpy import sin
from numpy import arange
import scipy.optimize
from matplotlib import pyplot
import requests
from csv import DictReader
    # iterate over each line as a ordered dictionary
    
def parse_thru_tickers():
    out = dict()
    with open('nasdaq_screener.csv', 'r') as read_obj:
        reader = DictReader(read_obj)
        for row in reader:
            try:
                out[row['Symbol']] = lin_reg_ticker(row['Symbol'])
            except ValueError:
                break

    return out

def func(x, a, b, c):
	return a*np.exp(b*x) + c
    
def lin_reg_ticker(t):
    print(t)
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
    sigma = np.ones(len(y_arr)) * 0.5 
    p0 = (1, -1, -1)
    popt, _ = scipy.optimize.curve_fit(func,  x_arr,  y_arr, p0, sigma = sigma ,absolute_sigma=True )
    KPI, b, c = popt
   
    # To print a plot of the linear regression  
    #     
    # pyplot.scatter(x_arr,y_arr)
    # x_line = arange(min(x_arr), max(x_arr), 1)    
    # y_line = func(x_line, a, b, c)
    # pyplot.plot(x_line, y_line, '--', color='red')
    # pyplot.savefig("plot")
    print(KPI)
    return KPI

g = parse_thru_tickers()