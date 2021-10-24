import pickle
import sys

cpickle = open('scorecardsshorter.pickle', 'rb')
cards = pickle.load(cpickle)
kpickle = open('KPIs.pickle', 'rb')
kpi = pickle.load(kpickle)

def makeSuggestions(eth_val):
    eth_val = eth_val / 100
    top30 = list()
    minThreshold = 0

# this is the most basic algorithm for balancing these. linear weighting
def calculateScore(ticker, eth_val):
    score = cards[ticker]['Wholistic'] / 100 * eth_val + kpi[ticker] / 10 * (1 - eth_val)
    if(kpi[ticker] < 0):
        score = -1000
    
    return score

def addToList(stocks, value):
    for x in range(len(stocks)):
        if value[1] >= stocks[x][1]:

"""
def shiftOut(stocks, index):
    for x in range():
"""

def main():
    print(cards)

if __name__ == "__main__":
    main()