import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suit = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        self.cards = [Card(suit, value) for s in suit for v in value]


    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        """Removes and returns the top card from the deck."""
        if len(self.cards) > 0:
            return self.cards.pop()
        return None

my_deck = Deck()
print(f"Fresh deck size: {len(my_deck.cards)} cards")
print(f"Top 3 cards before shuffle: {my_deck.cards[:3]}\n")

my_deck.shuffle()
print("--- Deck Shuffled ---")
print(f"Top 3 cards after shuffle: {my_deck.cards[:3]}\n")

drawn_card = my_deck.deal()
print(f"Drawn card: {drawn_card}")
        
