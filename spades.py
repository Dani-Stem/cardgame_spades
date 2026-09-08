# import random

# print("Spades!")
# input("press enter to play")
# print("pick your card")

# cards = ["AH","2H","3H", "4H", "5H", "6H", "7H", "8H", "9H", "JH", "QH", "KH","AS","2S","3S", "4S", "5S", "6S", "7S", "8S", "9S", "JS", "QS", "KS", "AD","2D","3D", "4D", "5D", "6D", "7D", "8D", "9D", "JD", "QD", "KD", "AC","2C","3C", "4C", "5C", "6C", "7C", "8C", "9C", "JC", "QC", "KC"]

# shuffle_cards = random.sample(cards, len(cards))

# quarter = len(shuffle_cards) // 4

# your_cards = shuffle_cards[0:quarter]
# opps_cards2 = shuffle_cards[quarter : quarter * 2]
# opps_cards3 = shuffle_cards[quarter * 2 : quarter * 3]
# opps_cards4 = shuffle_cards[quarter * 3 :]

# print(your_cards)
# print(opps_cards2)
# print(opps_cards3)
# print(opps_cards4)



# players = {1: "You", 2: "Player 2", 3: "Player 3", 4: "Player 4"} 
# first_player = players[random.randint(1, 4)] 

# print("Player to the left of the dealer goes first...")
# print(str(first_player) + " goes first")

# if first_player == "You":
#     downcard = input("pls select which card you want to play: ")
#     if downcard not in your_cards:
#         downcard = input("invalid input, please try again: ")

# elif first_player == "2":
#     for i in opps_cards2:   
#         if "A" in i and "S" not in i:
#             downcard = i
#             break
#         else:
#             if "S" not in i:
#                 downcard = i

# elif first_player == "3":
#     for i in opps_cards3:   
#         if "A" in i and "S" not in i:
#             downcard = i
#             break
#         else:
#             if "S" not in i:
#                 downcard = i

# elif first_player == "4":
#     for i in opps_cards4:   
#         if "A" in i and "S" not in i:
#             downcard = i
#             break
#         else:
#             if "S" not in i:
#                 downcard = i

# print(str(first_player) + " places down card: " + downcard) 

import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spades")
BLUE = (0, 128, 255) 
WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)

game_sceen = "start"

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
font = pygame.font.Font(None, 50)
font0 = pygame.font.Font(None, 40)
font1 = pygame.font.Font(None,15)
font2 = pygame.font.Font(None,25)
dealer = random.randint(1,4)

running = True
while running:
    # Look at all events that happened
    for event in pygame.event.get():
        # If the user clicks the window close button
        if event.type == pygame.QUIT:
            running = False

    # Optional: Fill the background color (Red, Green, Blue)
    screen.fill((50, 205, 50))
    
    if game_sceen == "start":

        pygame.draw.rect(screen, WHITE, (348, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (350, 250, 80, 110))
        pygame.draw.rect(screen, WHITE, (346, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (348, 250, 80, 110))

        text_surface = font.render("Welcome to Spades", True, WHITE)
        screen.blit(text_surface, (220, 50))
        text_surface0 = font0.render("Press Enter to Play", True, WHITE)
        screen.blit(text_surface0, (255, 100))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: 
                game_sceen = "play"

    if game_sceen == "play":

        pygame.draw.rect(screen, WHITE, (108, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (110, 250, 80, 110))
        pygame.draw.rect(screen, WHITE, (106, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (108, 250, 80, 110))

        pygame.draw.rect(screen, WHITE, (608, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (610, 250, 80, 110))
        pygame.draw.rect(screen, WHITE, (606, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (608, 250, 80, 110))

        pygame.draw.rect(screen, WHITE, (358, 48, 84, 114))
        pygame.draw.rect(screen, BLUE, (360, 50, 80, 110))
        pygame.draw.rect(screen, WHITE, (356, 48, 84, 114))
        pygame.draw.rect(screen, BLUE, (358, 50, 80, 110))

        pygame.draw.rect(screen, WHITE, (10, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (110, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (210, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (310, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (410, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (510, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (610, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (710, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (810, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (810, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (910, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (1010, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (1110, 450, 80, 110))


        text_surface = font2.render("Player to the Left of Dealer goes First", True, BLACK)
        screen.blit(text_surface, (240, 300))
        text_surface0 = font1.render("Press Enter to Continue", True, BLACK)
        screen.blit(text_surface0, (430, 320))


        if dealer == 1:
            your_label = "Dealer"
        else: 
            your_label = "Your Hand"

        if dealer == 2:
            player2_label = "Dealer"
        else: 
            player2_label = "Player 2"
        
        if dealer == 3:
            player3_label = "Dealer"
        else:
            player3_label = "Player 3"

        if dealer == 4:
            player4_label = "Dealer"
        else:
            player4_label = "Player 4"

        text_surface0 = font1.render(your_label, True, BLACK)
        screen.blit(text_surface0, (370, 430))
        text_surface0 = font1.render(player2_label, True, BLACK)
        screen.blit(text_surface0, (130, 230))
        text_surface0 = font1.render(player3_label, True, BLACK)
        screen.blit(text_surface0, (630, 230))
        text_surface0 = font1.render(player4_label, True, BLACK)
        screen.blit(text_surface0, (375, 30))

    # Update the display to show changes
    pygame.display.flip()

# Clean up and close the program
pygame.quit()#     for i in opps_cards2:   
#         if "A" in i and "S" not in i:
#             downcard = i
#             break
#         else:
#             if "S" not in i:
#                 downcard = i

# elif first_player == "3":
#     for i in opps_cards3:   
#         if "A" in i and "S" not in i:
#             downcard = i
#             break
#         else:
#             if "S" not in i:
#                 downcard = i

# elif first_player == "4":
#     for i in opps_cards4:   
#         if "A" in i and "S" not in i:
#             downcard = i
#             break
#         else:
#             if "S" not in i:
#                 downcard = i

# print(str(first_player) + " places down card: " + downcard) 

import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spades")
BLUE = (0, 128, 255) 
WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)

game_sceen = "start"

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
font = pygame.font.Font(None, 50)
font0 = pygame.font.Font(None, 40)
font1 = pygame.font.Font(None,15)
font2 = pygame.font.Font(None,25)

running = True
while running:
    # Look at all events that happened
    for event in pygame.event.get():
        # If the user clicks the window close button
        if event.type == pygame.QUIT:
            running = False

    # Optional: Fill the background color (Red, Green, Blue)
    screen.fill((50, 205, 50))
            
    if game_sceen == "start":

        pygame.draw.rect(screen, WHITE, (348, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (350, 250, 80, 110))
        pygame.draw.rect(screen, WHITE, (346, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (348, 250, 80, 110))

        text_surface = font.render("Welcome to Spades", True, WHITE)
        screen.blit(text_surface, (220, 50))
        text_surface0 = font0.render("Press Enter to Play", True, WHITE)
        screen.blit(text_surface0, (255, 100))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: 
                game_sceen = "play"

    if game_sceen == "play":

        pygame.draw.rect(screen, WHITE, (108, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (110, 250, 80, 110))
        pygame.draw.rect(screen, WHITE, (106, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (108, 250, 80, 110))

        pygame.draw.rect(screen, WHITE, (608, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (610, 250, 80, 110))
        pygame.draw.rect(screen, WHITE, (606, 248, 84, 114))
        pygame.draw.rect(screen, BLUE, (608, 250, 80, 110))

        pygame.draw.rect(screen, WHITE, (358, 48, 84, 114))
        pygame.draw.rect(screen, BLUE, (360, 50, 80, 110))
        pygame.draw.rect(screen, WHITE, (356, 48, 84, 114))
        pygame.draw.rect(screen, BLUE, (358, 50, 80, 110))

        pygame.draw.rect(screen, WHITE, (358, 448, 84, 114))
        pygame.draw.rect(screen, BLUE, (360, 450, 80, 110))
        pygame.draw.rect(screen, WHITE, (356, 448, 84, 114))
        pygame.draw.rect(screen, BLUE, (358, 450, 80, 110))

        text_surface = font2.render("Player to the Left of Dealer goes First", True, BLACK)
        screen.blit(text_surface, (240, 300))
        text_surface0 = font1.render("Press Enter to Continue", True, BLACK)
        screen.blit(text_surface0, (430, 320))

        dealer = 2

        if dealer == 1:
            your_label = "Dealer"
        else: 
            your_label = "Your Hand"

        if dealer == 2:
            player2_label = "Dealer"
        else: 
            player2_label = "Player 2"
        
        if dealer == 3:
            player3_label = "Dealer"
        else:
            player3_label = "Player 3"

        if dealer == 4:
            player4_label = "Dealer"
        else:
            player4_label = "Player 4"

        text_surface0 = font1.render(your_label, True, BLACK)
        screen.blit(text_surface0, (370, 430))
        text_surface0 = font1.render(player2_label, True, BLACK)
        screen.blit(text_surface0, (130, 230))
        text_surface0 = font1.render(player3_label, True, BLACK)
        screen.blit(text_surface0, (630, 230))
        text_surface0 = font1.render(player4_label, True, BLACK)
        screen.blit(text_surface0, (375, 30))

    # Update the display to show changes
    pygame.display.flip()

# Clean up and close the program
pygame.quit()
