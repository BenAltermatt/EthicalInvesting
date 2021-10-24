# Benjamin Altermatt
# 2021.10.23
import requests
from bs4 import BeautifulSoup as bs

def generateScorecard(tickVal):
    card = dict()

    page = requests.get('https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode=' + tickVal)
    
    # there are 14 scores
    index = 0
    toBeParsed = page.text
    for x in range(14):
        # find the next score
        temp = parseScore(toBeParsed[toBeParsed.find('score'):]) 
        score = temp[0]
        toBeParsed = temp[1]

        # associate it with its category
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


def main():
    print(generateScorecard('TWTR.K'))
    return

if __name__ == "__main__":
    main()

"""
page.content -> html of the page in a string
page.status_code -> staring with 2 if downloaded successfully, 4 or 5 if error


"""