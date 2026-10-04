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
        suit = ["Hearts", "Clubs", "Diamonds", "Spades"]
        value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [(s, v) for s in suit for v in value]

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

        return your_hand


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Spades")

        self.current_deck = Deck()
        self.dealer = random.randint(1, 4)
        self.game_screen = "start"
        self.suit = ""
        self.value = ""
        self.your_hand = self.current_deck.deal()

        self.font = pygame.font.Font(None, 50)
        self.font0 = pygame.font.Font(None, 40)
        self.font1 = pygame.font.Font(None, 15)
        self.font2 = pygame.font.Font(None, 25)
        self.spade_image = pygame.transform.smoothscale(
            pygame.image.load("spade.png").convert_alpha(), (42, 42)
        )

        self.BLUE = (0, 128, 255)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.CARD_BORDER = (200, 200, 200)
        self.RED = (200, 0, 0)

        self.run()

    def draw_card(self, surface, x, y, rank, suit):
        """Draws a playing card using pygame.draw.rect."""
        width = 80
        height = 110
        corner_radius = 8

        color = self.RED if suit in ["Hearts", "Diamonds"] else self.BLACK

        card_base = pygame.Rect(x, y, width, height)
        pygame.draw.rect(surface, self.WHITE, card_base, border_radius=corner_radius)

        pygame.draw.rect(
            surface, self.CARD_BORDER, card_base, width=2, border_radius=corner_radius
        )

        text_surface = self.font2.render(rank, True, color)
        surface.blit(text_surface, (x + 5, y + 5))

        br_text_surface = self.font2.render(rank, True, color)
        text_w, text_h = br_text_surface.get_size()
        surface.blit(
            br_text_surface, (x + width - text_w - 10, y + height - text_h - 10)
        )

        if suit == "Spades":
            spade_rect = self.spade_image.get_rect(center=card_base.center)
            surface.blit(self.spade_image, spade_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and self.game_screen == "start":
                    if event.key == pygame.K_RETURN:
                        self.game_screen = "play"

            self.screen.fill((50, 205, 50))

            if self.game_screen == "start":
                pygame.draw.rect(self.screen, self.WHITE, (348, 248, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (350, 250, 80, 110))
                pygame.draw.rect(self.screen, self.WHITE, (346, 248, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (348, 250, 80, 110))

                text_surface = self.font.render("Welcome to Spades", True, self.WHITE)
                self.screen.blit(text_surface, (220, 50))
                text_surface0 = self.font0.render(
                    "Press Enter to Play", True, self.WHITE
                )
                self.screen.blit(text_surface0, (255, 100))

            if self.game_screen == "play":
                pygame.draw.rect(self.screen, self.WHITE, (108, 248, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (110, 250, 80, 110))
                pygame.draw.rect(self.screen, self.WHITE, (106, 248, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (108, 250, 80, 110))

                pygame.draw.rect(self.screen, self.WHITE, (608, 248, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (610, 250, 80, 110))
                pygame.draw.rect(self.screen, self.WHITE, (606, 248, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (608, 250, 80, 110))

                pygame.draw.rect(self.screen, self.WHITE, (358, 48, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (360, 50, 80, 110))
                pygame.draw.rect(self.screen, self.WHITE, (356, 48, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (358, 50, 80, 110))

                card_placement = 120

                for i in range(len(self.your_hand)):
                    self.suit, self.value = self.your_hand[i]
                    self.draw_card(
                        self.screen, card_placement, 450, self.value, self.suit
                    )
                    card_placement += 40

                text_surface = self.font2.render(
                    "Player to the Left of Dealer goes First", True, self.BLACK
                )
                self.screen.blit(text_surface, (240, 300))
                text_surface0 = self.font1.render(
                    "Press Enter to Continue", True, self.BLACK
                )
                self.screen.blit(text_surface0, (430, 320))

                if self.dealer == 1:
                    your_label = "Dealer"
                else:
                    your_label = "Your Hand"

                if self.dealer == 2:
                    player2_label = "Dealer"
                else:
                    player2_label = "Player 2"

                if self.dealer == 3:
                    player3_label = "Dealer"
                else:
                    player3_label = "Player 3"

                if self.dealer == 4:
                    player4_label = "Dealer"
                else:
                    player4_label = "Player 4"

                text_surface0 = self.font1.render(your_label, True, self.BLACK)
                self.screen.blit(text_surface0, (370, 430))
                text_surface0 = self.font1.render(player2_label, True, self.BLACK)
                self.screen.blit(text_surface0, (130, 230))
                text_surface0 = self.font1.render(player3_label, True, self.BLACK)
                self.screen.blit(text_surface0, (630, 230))
                text_surface0 = self.font1.render(player4_label, True, self.BLACK)
                self.screen.blit(text_surface0, (375, 30))

            # Update the display to show changes
            pygame.display.flip()

        # Clean up and close the program
        pygame.quit()


Game()
