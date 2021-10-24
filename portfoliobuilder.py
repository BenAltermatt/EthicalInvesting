import pickle

pickle_in = open('scorecards.pickle', 'rb')
cards = pickle.load(pickle_in)

print(cards)