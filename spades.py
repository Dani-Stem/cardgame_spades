#1 cards are delt
#2 dealer is chosen at random 
#2.5 if dealer is user then skip #3 jump to #4
#3 dealer places a card Down
#4 user places a card down 
#5 rest of the players place a card down
#6 winner of round is the next dealer
#7 loop back to #3

# a card is played
# the rest of the players play a card of that same suit
# if you do not have a card of the same suit play a spade or thow away a card

#winner is the highest spade or the highest card of the played suit



import random
import pygame
import time

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
        your_hand = self.cards[:quarter_size]
        opp_hand2 = self.cards[quarter_size : quarter_size * 2]
        opp_hand3 = self.cards[quarter_size * 2 : quarter_size * 3]
        opp_hand4 = self.cards[quarter_size * 3 :]
        print("your hand: " + str(your_hand))
        print("Opp 2 hand: " + str(opp_hand2))
        print("Opp 3 hand: " + str(opp_hand3))
        print("Opp 4 hand: " + str(opp_hand4))

        return your_hand, opp_hand2, opp_hand3, opp_hand4

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Spades")

        self.current_deck = Deck()
        self.dealer = 2 #random.randint(1, 4)
        self.game_screen = "start"
        self.card_down = False
        self.oppcard_down = False
        self.current_card_suit = ""
        self.you_played = ""
        self.two_played = ""
        self.three_played = ""
        self.four_played = ""
        self.winner = ""
        self.suit = ""
        self.value = ""
        self.your_hand, self.opp_hand2, self.opp_hand3, self.opp_hand4 = self.current_deck.deal()
        self.hands_played_you = []
        self.hands_played2 = []
        self.hands_played3 = []
        self.hands_played4 = []

        self.font = pygame.font.Font(None, 50)
        self.font0 = pygame.font.Font(None, 40)
        self.font1 = pygame.font.Font(None, 15)
        self.font2 = pygame.font.Font(None, 25)
        self.spade_image = pygame.transform.smoothscale(
            pygame.image.load("spade.png").convert_alpha(), (42, 42))
        self.heart_image = pygame.transform.smoothscale(
            pygame.image.load("Heart.png").convert_alpha(), (42, 42))
        self.club_image = pygame.transform.smoothscale(
            pygame.image.load("Club.png").convert_alpha(), (42, 42))
        self.diamond_image = pygame.transform.smoothscale(
            pygame.image.load("Diamond.png").convert_alpha(), (42, 42))

        self.BLUE = (0, 128, 255)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.YELLOW = (255, 255, 0)
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
        elif suit == "Hearts":
            heart_rect = self.heart_image.get_rect(center=card_base.center)
            surface.blit(self.heart_image, heart_rect)
        elif suit == "Clubs":
            club_rect = self.club_image.get_rect(center=card_base.center)
            surface.blit(self.club_image, club_rect)
        elif suit == "Diamonds":
            diamond_rect = self.diamond_image.get_rect(center=card_base.center)
            surface.blit(self.diamond_image, diamond_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # what happens when enter is pressed
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.game_screen == "start":
                            self.game_screen = "play"
                        # reset round
                        if self.dealer == 0 and self.game_screen == "play":
                            print("next players turn")
                            self.dealer = self.winner
                            self.card_down = False
                            self.oppcard_down = False 
                            self.hands_played_you.clear()
                            self.hands_played2.clear()
                            self.hands_played3.clear()
                            self.hands_played4.clear()
                            self.current_card_suit = ""
                    
            self.screen.fill((50, 205, 50))

            # start screen
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

            # play screen
            if self.game_screen == "play":

                # draw the cards for each hand
                pygame.draw.rect(self.screen, self.WHITE, (78, 248, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (80, 250, 80, 110))
                pygame.draw.rect(self.screen, self.WHITE, (76, 248, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (78, 250, 80, 110))

                pygame.draw.rect(self.screen, self.WHITE, (638, 248, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (640, 250, 80, 110))
                pygame.draw.rect(self.screen, self.WHITE, (636, 248, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (638, 250, 80, 110))

                pygame.draw.rect(self.screen, self.WHITE, (358, 48, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (360, 50, 80, 110))
                pygame.draw.rect(self.screen, self.WHITE, (356, 48, 84, 114))
                pygame.draw.rect(self.screen, self.BLUE, (358, 50, 80, 110))

                # draw the cards that each player is playing
                for i in range(len(self.hands_played_you)):
                    self.suit, self.value = self.hands_played_you[i]
                    self.draw_card(
                        self.screen, 355, 300, self.value, self.suit
                    )
                
                for i in range(len(self.hands_played2)):
                    self.suit, self.value = self.hands_played2[i]
                    self.draw_card(
                        self.screen, 80, 250, self.value, self.suit
                    )

                for i in range(len(self.hands_played3)):
                    self.suit, self.value = self.hands_played3[i]
                    self.draw_card(
                        self.screen, 640, 250, self.value, self.suit
                    )

                for i in range(len(self.hands_played4)):
                    self.suit, self.value = self.hands_played4[i]
                    self.draw_card(
                        self.screen, 360, 50, self.value, self.suit
                    )

                #drawing your hand
                card_placement = 60

                for i in range(len(self.your_hand)):
                    self.suit, self.value = self.your_hand[i]
                    self.draw_card(
                        self.screen, card_placement, 450, self.value, self.suit
                    )
                    card_placement += 50

                #adding labels based on dealer
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
                self.screen.blit(text_surface0, (370, 425))
                text_surface0 = self.font1.render(player2_label, True, self.BLACK)
                self.screen.blit(text_surface0, (100, 230))
                text_surface0 = self.font1.render(player3_label, True, self.BLACK)
                self.screen.blit(text_surface0, (660, 230))
                text_surface0 = self.font1.render(player4_label, True, self.BLACK)
                self.screen.blit(text_surface0, (375, 30))

                #coordinates for each card in your hand when selected
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(f"Mouse clicked at: {event.pos}")

                    self.card_down = True

                    if ((event.pos[0] > 60 and event.pos[0] < 110) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(0))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 110 and event.pos[0] < 160) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(1))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 160 and event.pos[0] < 210) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(2))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 210 and event.pos[0] < 260) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(3))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 260 and event.pos[0] < 310) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(4))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 310 and event.pos[0] < 360) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(5))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 360 and event.pos[0] < 410) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(6))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 410 and event.pos[0] < 460) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(7))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 460 and event.pos[0] < 510) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(8))
                        print(self.hands_played_you)
        
                    if ((event.pos[0] > 510 and event.pos[0] < 560) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(9))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 560 and event.pos[0] < 610) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(10))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 610 and event.pos[0] < 660) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(11))
                        print(self.hands_played_you)

                    if ((event.pos[0] > 660 and event.pos[0] < 710) and (event.pos[1] > 450 and event.pos[1] < 560)):
                        time.sleep(1)
                        self.hands_played_you.append(self.your_hand.pop(12))
                        print(self.hands_played_you)

                # if its your play 
                if self.dealer == 1:
                    
                    text_surface = self.font2.render(
                        "Your Move, Pls select a card", True, self.BLACK
                    )
                    self.screen.blit(text_surface, (280, 280))

                # if its not your play but you havent picked a card yet 
                elif self.card_down == False:

                    text_surface = self.font2.render(
                        "Player " + str(self.dealer) + " has placed a card down", True, self.BLACK
                    )
                    self.screen.blit(text_surface, (240, 180))

                    #adding card for current players play 
                    if self.oppcard_down == False:
                        if self.dealer == 2: 
                            self.hands_played2.append(self.opp_hand2.pop(0))
                            self.oppcard_down = True
                            self.current_card_suit = self.hands_played2[0][0]
                        if self.dealer == 3:
                            self.hands_played3.append(self.opp_hand2.pop(0))
                            self.oppcard_down = True
                            self.current_card_suit = self.hands_played3[0][0]
                        if self.dealer == 4:
                            self.hands_played4.append(self.opp_hand2.pop(0))
                            self.oppcard_down = True
                            self.current_card_suit = self.hands_played4[0][0]

                if self.card_down and self.dealer != 0: 

                    # the rest if the players place a card down 
                    if self.dealer != 2:
                        target = self.current_card_suit
                        result2 = [row for row in self.opp_hand2 if target in row]
                        print("result: " + str(result2))
                        if result2 == []:
                            target = "Spades"
                            result2 = [row for row in self.opp_hand2 if target in row]
                            print("result: " + str(result4))
                        if result2 == []:
                            result2 = self.opp_hand2[0][0]
                            print("result: " + str(result2))
                            
                        self.hands_played2.append(result2.pop(0))

                    if self.dealer != 3:
                        target = self.current_card_suit
                        result3 = [row for row in self.opp_hand3 if target in row]
                        print("result: " + str(result3))
                        if result3 == []:
                            target = "Spades"
                            result3 = [row for row in self.opp_hand3 if target in row]
                            print("result: " + str(result3))
                        if result3 == []:
                            result4 = self.opp_hand4[0][0]
                            print("result: " + str(result3))
                            
                        self.hands_played3.append(result3.pop(0))

                    if self.dealer != 4:
                        target = self.current_card_suit
                        result4 = [row for row in self.opp_hand4 if target in row]
                        print("result: " + str(result4))
                        if result4 == []:
                            target = "Spades"
                            result4 = [row for row in self.opp_hand4 if target in row]
                            print("result: " + str(result4))
                        if result4 == []:
                            result4 = self.opp_hand4[0][0]
                            print("result: " + str(result4))
                            
                        self.hands_played4.append(result4.pop(0))


                            


                    self.dealer = 0

                # converting the jqka to int values
                if self.dealer == 0:
                    self.you_played = self.hands_played_you[0][1]
                    if self.you_played == "J":
                        self.you_played = "11"
                    elif self.you_played == "Q":
                        self.you_played = "12"
                    elif self.you_played == "K":
                        self.you_played = "13"
                    elif self.you_played == "A":
                        self.you_played = "14"
                    self.two_played = self.hands_played2[0][1]
                    if self.two_played == "J":
                        self.two_played = "11"
                    elif self.two_played == "Q":
                        self.two_played = "12"
                    elif self.two_played == "K":
                        self.two_played = "13"
                    elif self.two_played == "A":
                        self.two_played = "14"
                    self.three_played = self.hands_played3[0][1]
                    if self.three_played == "J":
                        self.three_played = "11"
                    elif self.three_played == "Q":
                        self.three_played = "12"
                    elif self.three_played == "K":
                        self.three_played = "13"
                    elif self.three_played == "A":
                        self.three_played = "14"
                    self.four_played = self.hands_played4[0][1]
                    if self.four_played == "J":
                        self.four_played = "11"
                    elif self.four_played == "Q":
                        self.four_played = "12"
                    elif self.four_played == "K":
                        self.four_played = "13"
                    elif self.four_played == "A":
                        self.four_played = "14"

                    winning_card = max(int(self.you_played), int(self.two_played), int(self.three_played), int(self.four_played))

                    if winning_card == int(self.you_played):
                        self.winner = 1
                    if winning_card == int(self.two_played):
                        self.winner = 2
                    if winning_card == int(self.three_played):
                        self.winner = 3
                    if winning_card == int(self.four_played):
                        self.winner = 4

                    #if your the winner
                    if self.winner == 1:

                        text_surface = self.font2.render(
                            "You have the highest card, you win!", True, self.BLACK
                        )
                        self.screen.blit(text_surface, (270, 240))

                    # if youre not the winner
                    else: 
                        
                        text_surface = self.font2.render(
                            "Player " + str(self.winner) + " has the highest card, they win this round.", True, self.BLACK
                        )
                        self.screen.blit(text_surface, (190, 240))

                    text_surface0 = self.font1.render(
                        "Press Enter to Continue", True, self.BLACK
                    )
                    self.screen.blit(text_surface0, (435, 270))

                    text_surface0 = self.font.render(
                        "____", True, self.YELLOW
                    )
                    if self.winner == 1:
                        win_x = 358
                        win_y = 380
                    elif self.winner == 2:
                        win_x = 88
                        win_y = 320
                    elif self.winner == 3:
                        win_x = 638
                        win_y = 335
                    elif self.winner == 4:
                        win_x = 358
                        win_y = 135
                        

                    self.screen.blit(text_surface0, (win_x, win_y))
        
            # Update the display to show changes
            pygame.display.flip()

        # Clean up and close the program
        pygame.quit()

Game()
