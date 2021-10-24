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
from lmfit.models import ExpressionModel

# Parses through all tickers in a csv file sourced from the NASDAQ 
# and determines a Key Performance Indicator (KPI) for each security
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
# Exponential Function
def func(x, a, b, c):
	return a*np.exp(b*x) + c

# Input is a ticker - outputs a KPI calculated
# by using an Exponential regression
def lin_reg_ticker(t):
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
    
    try:
        # Weighted Exponential Regression
        exponential_model = ExpressionModel("a * exp(b * x) + c", ["x"], None, 'omit' )
        fitted_model = exponential_model.fit(y_arr, x=x_arr, a=5, b=1, c=1)
        KPI = fitted_model.params['a'].value
        return KPI
        
    except: 
        return -1;
    # KPI, b, c = popt
    # print(KPI)

    # To print a plot of the linear regression  
    #     
    # pyplot.scatter(x_arr,y_arr)
    # x_line = arange(min(x_arr), max(x_arr), 1)    
    # y_line = func(x_line, a, b, c)
    # pyplot.plot(x_line, y_line, '--', color='red')
    # pyplot.savefig("plot")
    
    return KPI

if __name__ == "__main__":
    parse_thru_tickers()