from random import shuffle
from card import Card

class Deck(object):
    def __init__(self):
        self.cards =[]
        for i in range (2 , 15):
            for j in range (4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
        
    def remove_card(self):
        if len (self.cards) == 0 :
            return
        return self.cards.pop()
    
""" 
deck = Deck()
for card in deck.cards:
    print(card)
"""
