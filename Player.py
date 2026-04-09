from Hand import Hand
import time

class Player:
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        time.sleep(0.5)
        card = deck.deal_card()
        self.hand.add_card(card)
        print()
        print("Player gets " + card.rank + " of " + card.suit)
        print("Player has " + str(self.hand.get_hand_value()))
