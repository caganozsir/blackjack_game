from Card import Card 
import random

class Deck:

    def __init__(self):
        self.deck = []
        symbols = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        for x in symbols:
            for y in values:
                self.deck.append(Card(x,y))
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
