from Hand import Hand
import time

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def finalize(self, deck):
        print()
        print("Dealers other card is " + str(self.hand.cards[1]))
        print("Dealer has " + str(self.hand.get_hand_value()))

        while self.hand.get_hand_value() < 17:
            time.sleep(1)
            card = deck.deal_card()
            self.hand.add_card(card)
            print()
            print("Dealer gets " + card.rank + " of " + card.suit)
            print("Dealer has " + str(self.hand.get_hand_value()))
