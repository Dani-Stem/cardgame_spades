import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spades")

square_dims = (350, 250, 100, 100)
SQUARE_COLOR = (0, 128, 255)   


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
        self.shuffle()
        self.deal()

    def build(self):
        suit = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [v + " of " + s for s in suit for v in value]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        quarter_size = len(self.cards) // 4
        dealers_hand = self.cards[:quarter_size]
        your_hand = self.cards[quarter_size : quarter_size * 2]
        opp_hand0 = self.cards[quarter_size * 2 : quarter_size * 3]
        opp_hand1 = self.cards[quarter_size * 3 :]
        print("dealers hand: " + str(dealers_hand))
        print("your hand: " + str(your_hand))
        print("Opp 0 hand: " + str(opp_hand0))
        print("Opp 1 hand: " + str(opp_hand1))

current_deck = Deck()

running = True
while running:
    # Look at all events that happened
    for event in pygame.event.get():
        # If the user clicks the window close button
        if event.type == pygame.QUIT:
            running = False

    # Optional: Fill the background color (Red, Green, Blue)
    screen.fill((50, 205, 50))
    pygame.draw.rect(screen, SQUARE_COLOR, square_dims)

    # Update the display to show changes
    pygame.display.flip()

# Clean up and close the program
pygame.quit()


        
