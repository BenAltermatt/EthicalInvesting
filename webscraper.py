# Benjamin Altermatt
# 2021.10.23
import requests
import time as t
import pickle
from bs4 import BeautifulSoup as bs

def generateAllCards(tickerFile):
    # read the file
    tickerstrings = list()
    tickers = list()
    file = open(tickerFile)
    try:
        tickerstrings = file.readlines()
        for x in range(len(tickerstrings)):
            ticker = tickerstrings[x][:tickerstrings[x].find(',')]
            if ticker.find('^') == -1:
                tickers.append(ticker)

    finally:
        file.close()

    cards = dict()

    og_time = t.time()
    for tickval in range(len(tickers)):
        card = generateScorecard(tickers[tickval])
        print(str((tickval + 1) / len(tickers) * 100) + "% Complete")
        deltat = t.time() - og_time
        est_time = (len(tickers) - tickval - 1) * deltat / (tickval + 1)
        print('Estimated time remaining: ' + str(est_time) + ' seconds')
        if card is not None:
            cards[tickval] = card


    print(cards)


def findTickers():
    tickers = list()

    # we have to go through every letter in the alphabet
    for x in range(65, 65 + 26):
        tickerSite = requests.get("https://www.advfn.com/nyse/newyorkstockexchange.asp?companies=" + chr(x))
        tickers.extend(scrapeTickers(bs(tickerSite, 'html.parser')))
    
    # we have to do the extra characters one
        tickerSite = requests.get("https://www.advfn.com/nyse/newyorkstockexchange.asp?companies=0")
        tickers.extend(scrapeTickers(bs(tickerSite, 'html.parser')))
    
    return tickers


def scrapeTickers(soup):
    # Unfinished
    return


def generateScorecard(tickVal):
    card = dict()

    realTick = getFifthChar(tickVal)
    if realTick == -1: # data not provided for this ticker
        return None

    page = requests.get('https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode=' + realTick)

    # there are 14 scores
    index = 0
    toBeParsed = page.text
    for x in range(14):
        # find the next score
        temp = parseScore(toBeParsed[toBeParsed.find('score'):]) 
        score = temp[0]
        toBeParsed = temp[1]

        # associate it with its category and skip if redundant category
        temp = parseCategory(toBeParsed[toBeParsed.find('TR.'):])
        toBeparsed = temp[1]

        card[temp[0]] = score
    
    return card

def parseScore(string): # read the score out and bring back the rest of the string
    substr = string[7: 10] # score is 100 max
    retstr = ""

    for x in range(len(substr)): # make sure we get the actual number
        if 48 <= ord(substr[x]) <= 57:
            retstr += substr[x]

    return int(retstr), string[10:]

def parseCategory(string): # get the category
    substr = ''
    endpoint = string.find('"')

    # we need to adjust correctly for TR. vs TR.TRESG
    if string[:endpoint].find('TRES') != -1: # uses TRES
        substr = string[8:endpoint]
    else:
        substr = string[3:endpoint]

    retstr = ''

    if len(substr) == 0:
        retstr = 'Wholistc'
    else:
        retstr = substr
    
    return retstr, string[endpoint]

def getFifthChar(ticker):
    extensions = ['O', 'K']
    finalTicker = ticker

    if(len(requests.get('https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode=' + ticker).text) > 2): #no add on
        return ticker

    for x in extensions:
        if(len(requests.get('https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode=' + ticker + '.' + x).text) > 2): # common O add on
            return ticker + '.' + x
    
    return -1 # no data found for this ticker

def main():
    final = generateAllCards('stocks.txt')
    pickle_out = open("scorecards.pickle","wb")
    pickle.dump(final, pickle_out)
    pickle_out.close()
    return

if __name__ == "__main__":
    main()


"""
page.content -> html of the page in a string
page.status_code -> staring with 2 if downloaded successfully, 4 or 5 if error


"""