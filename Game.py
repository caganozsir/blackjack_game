from Deck import Deck
from Player import Player
from Dealer import Dealer
import time

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def initial_deal(self):
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())


    def show_hands(self):
        print()
        print("Your hand:")
        self.player.hand.show_player_hand()
        print()
        print("Dealer shows:")
        self.dealer.hand.show_dealer_hand()

    def player_turn(self):
        while not self.player.hand.is_bust():
            print()
            choice = input("Choose your move: [h]it or [s]tand: ").strip().lower()
            if choice == "h":
                self.player.hit(self.deck)
            elif choice == "s":
                print("You stand.")
                break
            else:
                print("Please type 'h' to hit or 's' to stand.")

    def dealer_turn(self):
        print()
        print("Dealer's turn...")
        time.sleep(1)
        self.dealer.finalize(self.deck)

    def determine_winner(self):
        players_hand = self.player.hand.get_hand_value()
        dealers_hand = self.dealer.hand.get_hand_value()
        if self.player.hand.is_bust():
            print("Dealer won.")
        elif self.dealer.hand.is_bust():
            print("Player won.")
        elif players_hand > dealers_hand:
            print("Player won.")
        elif dealers_hand > players_hand:
            print("Dealer won.")
        else:
            print("Draw.")

    def play(self):
        self.initial_deal()
        time.sleep(1)
        self.show_hands()
        if self.player.hand.has_blackjack() and self.dealer.hand.has_blackjack():
            time.sleep(1)
            print()
            print("Draw.")
        elif self.player.hand.has_blackjack():
            time.sleep(1)
            print()
            print("Player has blackjack. Player won.")
        elif self.dealer.hand.has_blackjack():
            time.sleep(1)
            print()
            print("Dealer has blackjack. Dealer won.")
        else:            
            self.player_turn()
            if self.player.hand.is_bust():
                time.sleep(1)
                print()
                print("Player busted.")
            else:
                self.dealer_turn()
                time.sleep(1)
                print()
                self.determine_winner()


if __name__ == "__main__":
    game = Game()
    game.play()
