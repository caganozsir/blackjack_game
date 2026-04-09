class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def show_player_hand(self):
        for card in self.cards:
            print(card)
        print(self.get_hand_value())

    def show_dealer_hand(self):
        print(self.cards[0])
        print("Dealer has " + str(self.cards[0].get_value()))

    def get_hand_value(self):
        value = 0
        ace_count = 0
        for card in self.cards:
            value += card.get_value()
            if card.rank == "Ace":
                ace_count += 1

        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1

        return value
    
    def is_bust(self):
        return self.get_hand_value() > 21
        
    def has_blackjack(self):
        return len(self.cards) == 2 and self.get_hand_value() == 21
