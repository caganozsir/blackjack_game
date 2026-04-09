class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank  
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def get_value(self):
        if self.rank in ["King", "Queen", "Jack"]:
            return 10
        elif self.rank in ["Ace"]:
            return 11
        else:
            return int(self.rank)